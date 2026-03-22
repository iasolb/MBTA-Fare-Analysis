# Data Pipeline — MBTA Fare Analysis

## Final Output

`output_data/mbta_gate_flows_clean.csv` — 5,558 rows, 7 columns. Each row represents a directed station pair on a single rapid transit line during a time-of-day bucket, combining average travel duration with fare gate entry volume for February 2026.

| Column | Type | Description |
|--------|------|-------------|
| `station_line_source` | str | Origin station and line, e.g. `Kendall/MIT, RED` |
| `station_line_destination` | str | Destination station and line |
| `line` | str | RED, ORANGE, or BLUE |
| `time_bucket` | str | Early Morning (5–7), AM Rush (7–10), Midday (10–15), PM Rush (15–19), Evening (19–22), Late Night (22–5) |
| `avg_travel_time_sec` | float | Mean travel time in seconds across all trips in the period |
| `source_avg_gated_entries` | float | Mean fare gate entries at the origin station |
| `dest_avg_gated_entries` | float | Mean fare gate entries at the destination station |

## Source Data

Three datasets are combined to produce the final output. Raw files are excluded from version control via `.gitignore`.

**MBTA Node Shapefile** (`data/mbta_rapid_transit/MBTA_NODE.shp`) — Defines the rapid transit station network. Each node has a `STATION` name and `LINE` field (e.g. `RED`, `ORANGE/BLUE` for transfer stations). This serves as the canonical list of underground stations.

**Gated Station Entries** (`data/GSE/GSE.csv`) — Fare gate tap-in counts published by the MBTA, broken down by station, line, service date, and 30-minute time period. The `route_or_line` field contains values like `"Red Line"` which are normalized to uppercase line codes.

**High-Resolution Travel Times** (`data/TravelTimes_2026/2026-02_HRTravelTimes.csv`) — Trip-level records with origin stop, destination stop, departure timestamp, and travel duration in seconds for February 2026.

## Pipeline Steps

The full pipeline is implemented in `build_policy_flow()` in `mbta_handling.py`.

### 1. Station Table Construction

The node shapefile is expanded so that transfer stations (e.g. `Downtown Crossing` on `ORANGE/RED`) produce one row per line. A composite key `station_line` is created by joining station name and line (e.g. `Downtown Crossing, ORANGE`). The same key is built on the GSE data after normalizing `route_or_line` → uppercase line code, and the two are merged on `station_line` via a left join.

### 2. Gate Activity Aggregation

Gated entries are averaged across all service dates for each `station_line` + `time_period` (30-min bin). The 48 half-hour bins are then mapped into 6 time-of-day buckets using `time_bucket()`, and the half-hour averages are summed within each bucket to produce a single `avg_gated_entries` value per station-line per time bucket.

### 3. Travel Time Preparation

The travel times dataset is filtered to only include trips originating at stations present in the node shapefile (the "underground" filter). The `route_id` field is uppercased to match the line codes, and a composite `station_line_source` / `station_line_destination` key is built. Departure timestamps are converted to hours and mapped to the same 6 time buckets.

### 4. Travel Time Aggregation

Trips are grouped by source, destination, line, and time bucket. Travel time is averaged within each group to produce `avg_travel_time_sec`.

### 5. Gate Activity Merge

The aggregated travel times are left-joined to the gate activity table twice — once on `station_line_source` to get `source_avg_gated_entries`, and once on `station_line_destination` to get `dest_avg_gated_entries`. Both joins key on `station_line` + `time_bucket`.

### 6. Missing Gate Data

Three stations have no corresponding records in the GSE dataset: `State, ORANGE`, `State, BLUE`, and `Massachusetts Avenue, ORANGE`. These stations appear in the travel times data but have no fare gate entries recorded. Their gate entry values are filled with `0` rather than dropped, to preserve the travel time information for those corridors.

## Assumptions and Limitations

- Gate entries reflect *tap-ins only* — they do not capture exits, transfers, or riders who evade the fare gate, which is directly relevant to the honor system vs. fare gate policy question.
- The 0-fill for missing gate stations (State, Mass Ave) means those stations will appear as low-activity origins/destinations despite likely having significant foot traffic.
- Travel times are averaged across all service dates in February 2026, which includes both weekdays and weekends. No weekday/weekend split is applied.
- The underground filter removes surface-level stops (e.g. Green Line above-ground segments) that appear in the travel times data but not in the node shapefile.