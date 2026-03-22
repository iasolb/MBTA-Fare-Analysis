# MBTA Fare Policy — Research Plan & Ideation

**Team:** Michael Mehall, Evan Crow, Michael Tian, Leandros Manwaring, Ian Solberg
**Course:** ECON 3416 — April 2026

---

## Central Research Question

> **Are fare gates on the MBTA worth it? Do the revenues they protect exceed their total costs — including capital, maintenance, and the ridership they suppress?**

More precisely: what is the break-even evasion rate at which fare gates become net fiscally positive, and does the MBTA's observed evasion rate clear that threshold?

---

## What We Dropped and Why

### Original Angle: Travel Time as the Outcome Variable
The initial framing used `avg_travel_time_sec` as the dependent variable and gate activity (`associated_gate_total`) as the key independent, with the hypothesis that gate congestion causes measurable travel delays.

**Why we moved away from it:**
- The dataset measures *train* travel time (departure → arrival), not *passenger* door-to-door time. Gates slow individuals who miss trains, but don't delay the train itself.
- Effect size would be too small to be a meaningful policy argument — seconds per trip.
- Endogeneity: high gate activity correlates with busy lines that may actually have *faster* headways, flipping the expected sign.
- Hard to isolate the gate mechanism from general station busyness.

**What travel time data is still good for:** Characterizing demand concentration across corridors and time buckets — feeding into the revenue/evasion weighting downstream.

---

## Reframed Argument: Full Cost-Benefit Analysis

Gates are a policy instrument. Like any instrument, they have costs and benefits. The paper's job is to quantify both sides and find the break-even.

### The Cost-Benefit Equation

```
Net Annual Cost of Keeping Gates =

  COSTS OF GATES:
  + Annualized capital cost (installation + hardware, amortized over lifespan)
  + Annual maintenance & fare collection operations (~$50M/yr system-wide)
  + Foregone ridership revenue (riders deterred by friction × $2.40/trip)

  BENEFITS OF GATES:
  + Revenue protected from evasion (incremental evasion Δ × annual boardings × $2.40)

  COSTS OF HONOR SYSTEM (offsets benefit):
  - Proof-of-payment enforcement cost (inspectors, transit police)

If Net Annual Cost > 0 → gates are a net fiscal drain → honor system is preferable
If Net Annual Cost < 0 → gates pay for themselves → keep them
```

### The Break-Even Framing (Core Result)

Solve for the break-even evasion rate Δe* such that:

```
Revenue Protected = Total Gate Cost
Δe* × Boardings × Fare = Capital_annualized + Maintenance - Enforcement_honor
```

Then ask: is the MBTA's observed incremental evasion rate (with gates vs. without) above or below Δe*?

- With gates: ~10% evasion (MBTA 2019 Fare Evasion Study)
- Without gates (honor systems): ~15–30% observed in comparable cities
- Incremental evasion Δe ≈ 5–20 percentage points — this is the range to test

---

## The Three Main Variables

### 1. Evasion & Revenue

| Item | Notes |
|------|-------|
| MBTA fare price | $2.40/trip (rapid transit) |
| Annual rapid transit boardings | ~300K/day → ~110M/year |
| Current evasion rate | ~10% (MBTA 2019 study) |
| Honor system evasion rate | 15–30% range (comparable cities) |
| Annual revenue at risk | Δevasion × 110M × $2.40 |

**Revenue protected by gates** = incremental evasion prevented × boardings × fare price. This is the primary benefit of gates and needs to be compared directly against costs.

### 2. Ridership Suppression (Fare Elasticity)

Gates create friction and fares create price barriers. Both reduce ridership below its potential.

**Fare elasticity of demand for urban transit:** -0.3 to -0.4 short run, -0.6 to -0.8 long run (FTA literature).

Meaning: a 10% effective price increase (or friction equivalent) reduces ridership 3–4% in the short run.

**Why this matters:**
- Lost riders = lost fare revenue, compounding the evasion problem
- If honor systems reduce friction and increase ridership, new rider revenue partially offsets evasion losses
- Net ridership effect of removing gates could be positive — some cities (Kansas City fare-free, European honor systems) saw ridership increases post-removal

**Formula:**
```
Ridership Gain from Removing Gates = ε × (friction_reduction_as_%_price_equivalent) × Baseline_Boardings
Additional Revenue = Ridership_Gain × Fare × (1 - new_evasion_rate)
```

Note: estimating friction reduction as a price equivalent is hard — we may need to use a range/sensitivity analysis here rather than a point estimate.

### 3. Gate Costs

| Cost Item | Estimated Range | Source |
|-----------|----------------|--------|
| Gate hardware (per unit) | $50,000–$100,000 | Industry estimates |
| Number of rapid transit gates | ~400+ | MBTA |
| Total capital (annualized, 20yr) | ~$10–20M/yr | Estimated |
| Fare collection operations (system-wide) | ~$50M/yr | MBTA budget |
| Honor system enforcement (POP inspectors) | $5–15M/yr | Comparable cities |

Net cost savings from removing gates ≈ $35–65M/yr (before accounting for evasion revenue loss).

---

## The State Subsidy / Bailout Angle

This is the fiscal policy dimension that connects the paper to broader public finance:

```
MBTA Operating Deficit = Operating Costs - Fare Revenue - Federal Aid
                       ↑ filled by Massachusetts state general fund (taxes)
```

If evasion increases under honor system:
- Fare revenue drops
- Deficit widens
- MA Legislature must increase MBTA subsidy → effectively a tax on all residents, including non-riders

**But the counterargument:**
- Gate maintenance costs also widen the deficit — they're a line item the state currently subsidizes
- If gates cost more to operate than the revenue they protect, the state is subsidizing a net-negative instrument
- The honest framing: taxpayers fund the MBTA either way. The question is which configuration minimizes that burden.

**Equity tension:**
- Honor system → higher evasion → higher subsidy needed → taxes rise for everyone including lower-income non-riders
- Gates → fare friction → lower-income riders who can't pay are excluded or evade out of necessity → gates are regressive in access
- Both systems have regressive features; the paper should acknowledge this is a distributional tradeoff, not just an efficiency one

---

## Data Sources Needed

| Variable | Source | Status |
|----------|--------|--------|
| Gate activity by station/time | `data/output_data/mbta_gate_flows_clean.csv` | **Have it** |
| Travel times by corridor/time | Same file | **Have it** |
| Annual MBTA fare revenue by line | MBTA Blue Book (annual report) | Need to pull |
| Annual rapid transit boardings | MBTA Blue Book | Need to pull |
| Historical fare changes + ridership response | MBTA service delivery reports | Need to pull |
| MBTA evasion rate estimate | MBTA 2019 Fare Evasion Study | Need to pull |
| Gate maintenance / fare collection budget | MBTA operating budget | Need to pull |
| Value of Travel Time (VTT) | USDOT 2024 guidance (~$17.90/hr local transit) | Available |
| Transit fare elasticity | FTA literature review | Available (-0.35 standard) |
| Honor system evasion rates (other cities) | Published transit authority reports | Need to pull |
| Census income by station catchment | ACS 5-year by tract | Available |

---

## Potential Empirical Extensions

### Extension A: Within-MBTA Natural Experiment
The Green Line above-ground segments use proof-of-payment (no gates). Underground Green Line stations are gated. This is a natural experiment within the same city and agency.
- Need: APC (Automatic Passenger Counter) data for Green Line surface ridership
- Pipeline: extend `build_policy_flow()` with a `build_bus_comparison()` function
- Challenge: surface vs. underground isn't a clean comparison (different vehicles, neighborhoods, station density)

### Extension B: Boston Fare-Free Bus Pilot (2022–2023)
MBTA ran a fare-free pilot on Routes 28, 23, and 29. MBTA published a full evaluation with before/after ridership and on-time performance.
- Same city, same agency, different enforcement model
- Gives a real natural experiment with temporal variation
- Most tractable extension given existing data infrastructure

### Extension C: Cross-City Comparison (Descriptive)
Use NTD (National Transit Database) for agency-level comparison:

| City | System | Model |
|------|--------|-------|
| DC (WMATA) | Metro | Full fare gates |
| NYC (MTA) | Subway | Full fare gates |
| Denver (RTD) | Light Rail | Full honor/POP |
| LA Metro | Rail | Honor/POP |
| Portland (TriMet) | MAX | Full honor/POP |

Compare fare revenue per boarding, evasion rates, operating cost per rider. Not causal, but useful framing for the policy context section.

### Extension D: Heckman Selection (If Evasion Data Available)
Gate tap-in counts are a selected sample — they don't capture evaders. If we can get survey or APC data with total boardings, Heckman two-step can correct for the selection bias in observed ridership. The `Research_Framework/examples/heckman_selection.py` has the template for this.

---

## Analysis Roadmap

### Phase 1: Descriptive (Use Existing Dataset)
- Summary statistics: ridership concentration by line, time bucket, station
- Visualize: gate activity heatmap by station × time bucket
- Identify high-value corridors (top 20% of gate activity accounts for what % of total entries?)

### Phase 2: Back-of-Envelope Revenue Model
- Pull MBTA Blue Book: total fare revenue, annual boardings, current deficit
- Estimate revenue at risk under honor system using evasion rate range
- Estimate gate cost savings
- Solve for break-even evasion rate Δe*

### Phase 3: Ridership Elasticity
- Apply -0.35 short-run elasticity to estimate ridership change under honor system
- Translate to additional revenue (new riders × fare × (1 - evasion rate))
- Sensitivity analysis: what if elasticity is -0.2? -0.5?

### Phase 4: OLS Regression (Empirical Core)
Even with the travel time argument dropped, regression is still valuable:
- `log(gate_entries) ~ line_FE + time_bucket_FE` — characterize what drives demand concentration
- If we get historical data: `Δridership ~ Δfare + line_FE + year_FE` — estimate elasticity directly

### Phase 5: Break-Even and Policy Conclusion
- Combine revenue model + elasticity + gate costs into unified break-even calculation
- Present as a range (sensitivity table) rather than a point estimate
- Conclusion: gates are [worth it / not worth it] given MBTA's specific cost structure and observed evasion

---

## Open Questions

1. Can we get the MBTA 2019 Fare Evasion Study directly, or do we rely on the summary statistics reported in news coverage?
2. Is gate maintenance cost reported as a line item in the MBTA budget, or is it bundled into broader fare collection operations?
3. Do we have enough data to estimate fare elasticity directly (need multiple fare change periods), or do we cite the literature?
4. Should we attempt the Green Line surface/underground comparison, or is the confounding too severe for the scope of this paper?
5. How do we handle the equity argument — as a separate section or woven throughout?

---

## Paper Outline (Draft)

1. **Introduction** — The honor system debate; what's at stake for the MBTA
2. **Background** — How the MBTA fare system works; peer city examples; prior evasion studies
3. **Data** — Description of our dataset; what it measures and what it doesn't
4. **Descriptive Analysis** — Ridership concentration; which corridors and times matter most
5. **Cost-Benefit Framework** — Gate costs vs. revenue protection; the break-even model
6. **Ridership Elasticity** — What removing gate friction does to demand
7. **Fiscal Impact** — State subsidy implications; who bears the cost under each regime
8. **Equity Considerations** — Distributional effects on low-income riders
9. **Conclusion** — Break-even result; policy recommendation; limitations

---

*Last updated: March 2026*
