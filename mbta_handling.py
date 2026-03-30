import pandas as pd
import geopandas as gpd
from Research_Framework.ResearchHandler import ResearchHandler
from typing import Optional


def blank(df: pd.DataFrame) -> pd.DataFrame:
    return df


def time_bucket(t, dt: Optional[bool] = False) -> str:
    # Extract hour from string like '(17:00:00)'
    if not dt:
        hour = int(t.strip("()").split(":")[0])
    else:
        hour = t
    if 5 <= hour < 7:
        return "Early Morning"
    elif 7 <= hour < 10:
        return "AM Rush"
    elif 10 <= hour < 15:
        return "Midday"
    elif 15 <= hour < 19:
        return "PM Rush"
    elif 19 <= hour < 22:
        return "Evening"
    else:
        return "Late Night"


def build_policy_flow(
    nodes_fp: str, gse_fp: str, travel_times_hr_fp: str, travel_time_lr_fp: str
) -> pd.DataFrame:
    """
    Builds a merged DataFrame of avg travel times and source/destination gate activity
    by station-line pair and time bucket, for policy targeting.
    """
    try:
        # --- Load data ---
        nodes = gpd.read_file(nodes_fp)
        gse = pd.read_csv(gse_fp)
        travel_times_hr = pd.read_csv(travel_times_hr_fp, low_memory=False)
        travel_times_lr = pd.read_csv(travel_time_lr_fp, low_memory=False)
        # --- Build station table ---
        gse["line"] = (
            gse["route_or_line"]
            .str.replace("Line", "", regex=False)
            .str.strip()
            .str.upper()
        )
        gse["station_line"] = gse["station_name"].str.strip() + ", " + gse["line"]
        gse_cols = gse[
            [
                "service_date",
                "time_period",
                "station_name",
                "station_line",
                "gated_entries",
            ]
        ]

        rows = []
        node_id = 0
        for _, row in nodes[["STATION", "LINE"]].iterrows():
            for line in row["LINE"].split("/"):
                rows.append(
                    {
                        "node_id": node_id,
                        "station_line": f"{row['STATION']}, {line.strip()}",
                        "line": line.strip(),
                    }
                )
                node_id += 1

        stations = pd.DataFrame(rows).set_index("node_id")
        station_table = stations.merge(gse_cols, on="station_line", how="left")

        # --- Gate activity aggregation ---
        gates = (
            station_table.dropna(subset=["gated_entries"])
            .groupby(["station_line", "time_period"])["gated_entries"]
            .mean()
            .reset_index()
        )
        gates["time_bucket"] = gates["time_period"].apply(time_bucket)
        gate_flow = (
            gates.groupby(["station_line", "time_bucket"])["gated_entries"]
            .sum()
            .reset_index()
            .rename(columns={"gated_entries": "avg_gated_entries"})
        )

        travel_times = pd.concat([travel_times_hr, travel_times_lr])
        # --- Travel time prep ---
        trips = travel_times[
            [
                "from_stop_name",
                "to_stop_name",
                "travel_time_sec",
                "route_id",
                "from_stop_departure_datetime",
            ]
        ].copy()
        trips.rename(
            columns={
                "route_id": "line",
                "from_stop_name": "source",
                "to_stop_name": "destination",
            },
            inplace=True,
        )
        trips["line"] = trips["line"].str.upper().str.split("-").str[0]
        trips["station_line_source"] = trips["source"] + ", " + trips["line"]
        trips["station_line_destination"] = trips["destination"] + ", " + trips["line"]
        trips.drop(columns=["source", "destination"], inplace=True)

        # Filter to underground stations only
        underground = set(station_table["station_line"].unique())
        trips = trips[trips["station_line_source"].isin(underground)]

        # Time bucket
        trips.dropna(subset=["from_stop_departure_datetime"], inplace=True)
        trips["from_stop_departure_datetime"] = pd.to_datetime(
            trips["from_stop_departure_datetime"]
        )
        trips["hour"] = trips["from_stop_departure_datetime"].dt.hour
        trips["time_bucket"] = trips["hour"].apply(lambda h: time_bucket(h, dt=True))

        # --- Travel time aggregation ---
        travel_flow = (
            trips.groupby(
                [
                    "station_line_source",
                    "station_line_destination",
                    "line",
                    "time_bucket",
                ]
            )["travel_time_sec"]
            .mean()
            .reset_index()
            .rename(columns={"travel_time_sec": "avg_travel_time_sec"})
        )

        # --- Merge source gate activity ---
        merged = (
            travel_flow.merge(
                gate_flow,
                left_on=["station_line_source", "time_bucket"],
                right_on=["station_line", "time_bucket"],
                how="left",
            )
            .rename(columns={"avg_gated_entries": "source_avg_gated_entries"})
            .drop(columns=["station_line"])
        )

        # --- Merge destination gate activity ---
        merged = (
            merged.merge(
                gate_flow,
                left_on=["station_line_destination", "time_bucket"],
                right_on=["station_line", "time_bucket"],
                how="left",
            )
            .rename(columns={"avg_gated_entries": "dest_avg_gated_entries"})
            .drop(columns=["station_line"])
        )

        return (
            merged.sort_values("source_avg_gated_entries", ascending=False)
            .reset_index(drop=True)
            .fillna({"source_avg_gated_entries": 0, "dest_avg_gated_entries": 0})
        )
    except Exception as e:
        print(f"Issue initializing data. {e}")
        return pd.DataFrame()
