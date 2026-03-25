# MBTA Fare Gates

This document outlines the analysis I want to add to the project. Ian's work allocates enforcement resources across existing gated stations using a short-haul evasion model. I want to extend that argument to ask: should the MBTA add gates to the non-gated Green Line surface stops, and does the ROI justify it?

---

## The Expansion Argument

Gates work because they eliminate the behavioral pathways through which evasion occurs — present bias, default effects, mental accounting, social norm cascades (see behavioral section below). The MBTA's own data shows this clearly:

| Segment | Enforcement | Evasion Rate | Annual Revenue Lost |
|---------|-------------|--------------|---------------------|
| Gated subway | Hard gate | ~1% | Minimal |
| Green Line surface | Honor/POP | ~10% | ~$4.5M/yr (FMCB 2019) |

Green Line surface stops are also the highest short-haul segment in the system — above-ground neighborhood hops where mental accounting makes the $2.40 fare feel most disproportionate. This means the behavioral case for gating is strongest exactly where there are no gates.

---

## Behavioral Economics of Fare Evasion

The cost-benefit numbers tell us *whether* gates pay off; behavioral economics tells us *why* people evade without them and *why* gates work as an intervention.

### Why People Evade Without Gates

#### 1. Present Bias (Hyperbolic Discounting)
The decision to evade is made in the moment, at the platform. The cost of paying ($2.40) is immediate and certain. The cost of getting caught (fine, embarrassment) is small in probability and distant in time. Present-biased individuals systematically overweight immediate costs relative to future costs — so even riders who *intend* to pay can rationalize skipping when facing a platform with no physical barrier.

> **Formal mechanism:** Under hyperbolic discounting, a rider discounts future punishment at rate δ < 1. If p = probability of inspection, F = fine, and the rider is present-biased (β < 1):
> `Expected cost of evasion = β × p × F`
> At low inspection rates (p ≈ 0.01–0.05 on POP systems), even non-biased individuals may rationally evade. Present bias compounds this — β makes future fines feel even smaller.

**Why gates fix it:** Gates eliminate the in-the-moment choice entirely. Payment happens before entry — it's structurally mandatory, not a decision.

#### 2. Default Effects and Opt-In Compliance
Honor/POP systems require an active choice to pay. Paying is opt-in. Behavioral research (Thaler & Sunstein, 2008) consistently shows that opt-in compliance is lower than opt-out compliance — people stick with whatever requires less effort.

- **Gated system:** Default = you cannot board without paying. Compliance is ~99%.
- **Honor system:** Default = board freely; paying requires finding a validator, tapping, waiting. Compliance is ~70–85%.

The 15–30% evasion observed on honor systems (vs. ~1% on gated) is partially a default effect, not purely moral failure. Riders aren't deciding to steal — they're defaulting to the path of least resistance.

#### 3. Mental Accounting and Trip Value
Riders mentally evaluate the fare against the perceived value of the trip. For short-haul trips, $2.40 feels disproportionate — you're paying full price for a 2-stop ride you could have walked in 20 minutes. This is classic mental accounting (Thaler, 1985): people don't evaluate money fungibly; the same $2.40 feels like a better deal on a 45-minute commute than on a 4-minute hop.

**This is why Barabino et al. (2015) find 1.41x higher evasion on short-haul trips** — it's not just that inspectors are less likely to board a short trip, it's that the fare-to-value ratio triggers a stronger sense of unfairness, lowering the psychological cost of evasion.

**Why gates fix it:** Gates impose the payment regardless of trip length. There's no opportunity to mentally renegotiate the fare-value tradeoff at the platform.

#### 4. Social Norm Cascades
In high-evasion environments, evasion becomes normalized. Seeing others skip payment signals that the behavior is acceptable and enforcement is absent. This creates a positive feedback loop: more visible evasion → lower perceived social cost of evasion → more evasion (Cialdini et al., 1990).

**Why this is especially dangerous on POP systems:** On a POP platform, evasion is visible to every waiting rider. On a gated system, no one can board without paying, so there's no social signal to normalize.

**Evidence:** Green Line surface evasion (~10%) is 10× the subway rate (~1%). Part of this gap is the social norm effect — riders observe others not tapping and update their belief about whether payment is expected.

---

### Why Gates Are the Right Behavioral Intervention

| Behavioral Problem | Honor System Response | Gate Response |
|--------------------|----------------------|---------------|
| Present bias | Relies on rider overriding in-the-moment temptation | Eliminates the choice point entirely |
| Default effects | Paying is opt-in → low compliance | Paying is mandatory → near-universal compliance |
| Mental accounting (short trips) | Rider can decline payment if value seems low | No opt-out regardless of trip length |
| Social norm cascade | Visible evasion normalizes further evasion | No visible evasion possible |

**The behavioral case for gates:** Gates are not a nudge — they are a commitment device that removes the cognitive and behavioral pathways through which evasion occurs. For a population with predictable present bias and default sensitivity, hard constraints outperform soft interventions.

**The behavioral case against gates:** Gate friction is itself a behavioral tax on compliant riders. The hassle of tapping, waiting for the gate to open, and navigating crowded entry points creates real disutility — especially for infrequent riders. This friction may deter marginal riders entirely, which is a real cost even if it doesn't show up in the evasion statistics.

---

### Key Citations
- Thaler & Sunstein (2008) — *Nudge* — default effects and opt-in compliance
- O'Donoghue & Rabin (1999) — present bias and self-control in economic decisions
- Kahneman & Tversky (1979) — prospect theory, loss aversion, probability weighting
- Thaler (1985) — mental accounting
- Cialdini et al. (1990) — social norms and descriptive vs. injunctive norm effects
- Barabino et al. (2015) — short-haul evasion multiplier (OR = 0.7065, p = 0.008) — **already in project**

---

## Gate ROI Analysis

### Cost-Benefit Equation

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

### Break-Even Framing

```
Revenue Protected = Total Gate Cost
Δe* × Boardings × Fare = Capital_annualized + Maintenance - Enforcement_honor
```

- With gates: ~1% evasion (gated subway, FMCB 2019)
- Without gates (surface/honor): ~10–30% observed
- Incremental evasion Δe ≈ 9–29 percentage points for surface expansion

### Gate Costs

| Cost Item | Estimated Range | Source |
|-----------|----------------|--------|
| Gate hardware (per unit) | $50,000–$100,000 | Industry estimates |
| Number of existing rapid transit gates | ~400+ | MBTA |
| Total capital (annualized, 20yr) | ~$10–20M/yr | Estimated |
| Fare collection operations (system-wide) | ~$50M/yr | MBTA budget |
| Honor system enforcement (POP inspectors) | $5–15M/yr | Comparable cities |
| Per-gate hardware + install (surface expansion) | $50,000–$100,000 per gate | AFC 2.0 audit |

**Surface expansion estimate:** ~60–100 new gate units across 20–25 surface stations = $3–10M capital (annualized: $150K–$500K/yr over 20yr). Compare against $4.5M/yr in recoverable evasion revenue → positive ROI under most assumptions.

---

## Analysis Plan (Extension E)

This builds directly on Ian's allocation model. He answered: "where should enforcement go across existing gated stations?" I answer: "which non-gated stations should be gated first?"

Both use the same Barabino short-haul finding, just applied to different problems.

### Steps

1. **Estimate surface boardings** — backsolve from FMCB 2019: $4.5M ÷ (10% × $2.40) ≈ 18.75M/yr. Apportion by branch (B/C/D/E) using ridership share if available, otherwise equal split as sensitivity.

2. **Assign short_haul_exposure** — literature assumption for surface stops: ~0.70–0.90 (most above-ground trips are under 900 sec).

3. **Apply Ian's enforcement score** to rank expansion priority:
   `enforcement_score = estimated_boardings × (1 + short_haul_exposure)`

4. **Revenue projection per branch:**
   `revenue_recovered = 0.09 × annual_boardings × $2.40` (9pp evasion reduction: 10% → 1%)

5. **Gate cost model** from AFC 2.0 audit:
   `gate_cost = per_gate_hardware × gates_needed`

6. **Break-even:**
   `break_even_years = gate_capital / annual_revenue_recovered`

### Outputs — 2 Charts

- **Bar chart:** annual revenue recovery potential by Green Line branch (B, C, D, E), ranked by enforcement score
- **Break-even waterfall:** cumulative capital cost vs. cumulative revenue recovered over 10 years, with sensitivity bands (evasion 8%/10%/15%, per-gate cost $50K/$75K/$100K)

### Sensitivity Parameters

| Parameter | Low | Base | High |
|-----------|-----|------|------|
| Evasion rate at surface | 8% | 10% | 15% |
| Per-gate hardware cost | $50K | $75K | $100K |
| Short_haul_exposure | 0.60 | 0.75 | 0.90 |

### Pipeline Note

Does NOT require modifying `mbta_handling.py`. Surface station data is a standalone DataFrame (hardcoded or pulled from MBTA open data) merged with Ian's allocation output for comparison.

---

## Data Sources

| Variable | Source | Status |
|----------|--------|--------|
| Gate activity by station/time | `data/output_data/mbta_gate_flows_clean.csv` | **Have it** |
| MBTA evasion rate by mode | FMCB 2019 board presentation (downloaded) | **Have it** |
| Gate maintenance / fare collection budget | MBTA operating budget (downloaded) | **Have it** |
| Transit fare elasticity | FTA literature review | Available (-0.35 standard) |
| Green Line surface boardings by branch | FMCB 2019 backsolve / MBTA open data | Estimate available |
| Per-gate installation cost (surface) | AFC 2.0 audit (downloaded) | Need to extract from PDF |
| Honor system evasion rates (other cities) | NTD / agency reports | Need to pull |

---

## Open Questions

1. Can the FMCB 2019 $4.5M Green Line surface figure be disaggregated by branch (B/C/D/E), or does it need to be apportioned by ridership share?
2. Is gate maintenance cost broken out as a line item in the MBTA budget, or bundled into fare collection operations?
3. How do we handle the equity argument — gates on surface stops may disproportionately burden lower-income neighborhood riders?

---

## Data Update (March 25, 2026)

### Ridership Data Acquired

Downloaded **Fall 2024 MBTA Rail Ridership by SDP Time Period, Route/Line, and Stop** from the MBTA Open Data Portal. This provides actual station-level boardings (`total_ons`/`total_offs`) for all 70 Green Line stops including surface stations.

- **File:** `data/input_data/Fall_2024_MBTA_Rail_Ridership_by_SDP_Time_Period,_Route_Line,_and_Stop.csv`
- **Season:** Fall 2024 (Aug 25 – Dec 14, 75 weekday service days)
- **Coverage:** All Green Line stops (both gated underground and surface)
- **Key fields:** `stop_name`, `total_ons`, `total_offs`, `average_ons`, `day_type_name`, `time_period_name`

### What Changed in the Analysis

1. **Station-level boardings now from data**, not fabricated estimates. Real numbers are much lower than the backsolve suggested (~5.5M total surface boardings vs. 18.75M backsolve). The backsolve overestimated because it attributed all $4.5M in lost revenue to surface stops, but underground Green Line stops also use honor-system enforcement.
2. **Branch mapping** is hardcoded (MBTA system geography — factual, not an estimate). The route_id in the data is just "Green" with no branch split.
3. **gates_needed** is still an assumption (tiered by daily boardings: ≥800→4, ≥400→3, else→2).
4. **short_haul_exposure** is still a literature-based assumption (Barabino et al. 2015), interpolated by stop position within branch (inner=0.90, outer=0.60).

### Open Questions Resolved

1. ✅ Branch-level disaggregation is now possible from data — station-level boardings mapped to B/C/D/E branches.

---

*Last updated: March 25, 2026*
