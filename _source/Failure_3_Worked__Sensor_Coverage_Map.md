---
title: "Failure 3, Worked — A Sensor-Coverage Map of the Cardano Governance Layer"
type: worked-example
status: draft 1.0
role: companion to the field-fitness audit (slots in as Appendix B, or stands alone)
extends: field-fitness-audit.md
instrument_inventory: Cardano Governance Health KPI Report v1.0 (GHWG, Intersect Civics Committee, 3 Dec 2025)
also_related:
  - The_Rights_of_Participants_in_a_Constitutional_Coordination_Commons.md
  - the_verification_gap.md
  - From_Tenets_to_Rights__A_Trajectory_Map.md
---

# Failure 3, Worked — A Sensor-Coverage Map of the Cardano Governance Layer

## What this is, and the boundary it respects

The field-fitness audit's third check reads: *for each of the six rights, ask whether the field has a sensor that registers pressure on it before the damage is structural, or whether it only notices once the harm is done. Map the sensors that exist against the pressures the field actually faces. The gaps are your blind spots.*

Running that check requires two things: the six rights (the specification of what a healthy governance field protects) and an inventory of the sensors the field actually has. For the first time, the second thing exists as a real document. The Governance Health Working Group's KPI Report is the most complete, most carefully reasoned inventory of governance-layer sensors the ecosystem has produced. This worked example runs Failure 3 against the Cardano governance layer using that report as the sensor inventory.

One boundary has to be stated plainly, because it is easy to get wrong. **The field under audit is the Cardano governance layer. The report is not the field; it is the field's account of what it can currently see about itself.** We are not auditing the GHWG, and we are certainly not running the full four-failure diagnostic on a measurement document — a KPI catalogue has no roadmap to fuse with its identity, no reorientation history, no crisis-turning pattern, so Failures 1, 2, and 4 have nothing to grip. That would be stretching the instrument past its appropriate use. Failure 3 is the one check the report is built to feed, because Failure 3 is the only check whose input *is* a sensor inventory. The report doesn't get audited. It gets read, as the answer to "what does this field currently sense?"

A second boundary, in the audit's own register: this is a **fitness map, not an indictment.** Every gap named below is a place the field cannot yet see itself, not a place the GHWG failed. As the next section shows, the report draws most of these boundaries itself, openly, and stops at them on purpose.

## The instrument we are reading from

In the framework's terms, the GHWG report is the most sophisticated possible version of the **first instrument panel** — the growth-and-throughput dashboard the audit warns "cannot tell vitality from a tumor drawing its own blood supply, because a captured ecosystem can climb every one of [its metrics] right up until the host fails." Participation, decentralization, treasury health, activity, accessibility: this is the panel that reads the things a healthy-looking system shows on its surface.

What makes it useful rather than merely an example of the problem is how aware it is of its own edge. The report states, as its own first key insight, that high turnout does not guarantee high-quality decisions and that quantitative activity must be paired with qualitative proxies. It calls its present work "plumbing — getting the basic counts and rates correct," and defers the grading of rationale quality, debate sentiment, and actor competence to a future phase it names "Semantic Governance." It labels its own Rationale Rate metric "quantity over quality (initially)."

That self-awareness is the whole reason the map below is legible. The blind spots are not an oversight an outsider is imposing. They are the boundary the builders themselves drew and then, honestly, stopped at — having clearly thought hard, and having discovered that they could not reach the integrity layer by adding more metrics of the same kind. A clumsy dashboard could be dismissed. This one cannot, and its sophistication is exactly what makes the absence of the second panel *more* visible: the second panel is a different instrument, not more of the first. The GHWG built panel one well and named panel two as future work. The rights derivation is the principled version of the panel two they gestured at.

That parallel is worth holding onto, because it recurs. **The GHWG report stands to the integrity sensor as the constitutional Tenets stand to the rights** (see the trajectory map): both gesture accurately at what is needed, neither derives it, and both name the missing thing as future work. The ecosystem keeps producing honest gestures toward the integrity layer and stopping at the seam. This is one more.

## The check, run

For each of the six rights: what does the report sense, what does it actually measure, and what does the right require that the measurement misses?

### 1 — Settlement access · *out of frame, appropriately*

The right to submit a transaction and have it processed without discrimination is a *transaction-layer* right, and the report is a *governance-participation* instrument, so almost nothing maps. The nearest touch is **Deposit Cost Burden** (the ada deposit for DRep registration or governance-action submission, indexed to fiat) — but that meters the toll on *governance submission*, not the toll on ordinary settlement. The absence here is structurally correct, not a gap to charge against the GHWG: settlement access is the right that verifiable reflexivity already half-secures at the transaction layer, and a governance dashboard is not where it would live. Worth recording only as a reminder: nothing in the governance-layer panel would register a settlement-access erosion (a fee regime quietly pricing out small participants while preserving the large). That sensor belongs to the engine, not here.

### 2 — Unit-of-account integrity · *shell only*

The report watches the treasury *level and flow* — **Treasury Balance Rate** (Core: ada spent ÷ ada added) and **Treasury Spend vs NCL** (Future). These are real fiscal-sustainability sensors. But unit-of-account integrity is not about the treasury's level; it is about whether *the measuring instrument itself stays honest* — whether the monetary parameters participants consented to (issuance schedule, treasury cut, the very definition of the unit) are altered in substance to benefit controlling actors. Nothing in the suite senses that.

The sharpest demonstration: the v2.4 amendment that inserted "store of value" into Tenet 10 — a substantive change to the constitution's *definition of the unit of account*, and the reification error the rights framework exists to correct — would be **completely invisible** to this entire report. There is no metric whose movement would register that the ontology of the money had been changed. The fiscal panel is bright; the integrity-of-the-measure panel is dark.

### 3 — Governance participation · *best-sensed, but only on the quantitative axis*

This is where the report is genuinely strong, and the strength is real: **Delegation Decentralization (Gini)**, **DRep Voting Correlation**, **Entity Voting Power Concentration** (HHI/Gini on entity-aggregated stake), **Top-100 DRep Concentration Volatility**, **SPO Entity Voting Power Concentration**, and **Min Attack Vector** (actors needed to collude to meet a threshold) are bona fide enclosure sensors. In the instruments-layer vocabulary, they sense the **walls** — the unreachable-by-count concentration thresholds — being approached. A field that watches these is genuinely watching for stake-weighted capture of governance.

But the enclosure that the Trajectory Assessment found most active in this ecosystem is *qualitative and interpretive*, not stake-weighted: agenda control (what gets drafted, what reaches a vote), and the **interpretive concentration in the Constitutional Committee** — the accumulation of sufficiency-and-completeness determination power that the assessment flagged as growing through accreted responsibility rather than formal grant. The report under-senses this axis. **CC Vote Agreement Rate** catches CC *groupthink*; nothing catches CC interpretive *scope-creep*. **Gov Action Volume & Source** and **Success Rate by Source** (the bias check, with its candid "Inst. may have more resources" caveat) are a genuine partial agenda-control sensor — perhaps the report's most underrated integrity-adjacent metric. But the structural concentration of *interpretive authority* — power over what counts as constitutional — has no instrument. Participation is well-sensed where it is countable, and thin where it is a matter of who decides what things mean.

### 4 — Informational integrity · *availability sensed, veracity unsensed* (the load-bearing gap)

The report has several sensors that look like informational-integrity sensors: **DRep Rationale Rate**, **Gov Info Availability** (% actions with human-readable vote pages), **Governance Data Parity** (do explorers agree), **DRep Metadata Completeness**, and **Gov Action Consequence Analysis** (Future). But read what each one actually measures: every single one senses the *existence, reachability, or consistency* of information — not its *truth*. Rationale Rate counts whether a rationale is present (the report itself flags "quantity over quality"). Info Availability counts whether a readable page exists. Data Parity checks whether two explorers show the same numbers — consistency, which is not veracity; two explorers can agree on a false figure. Metadata Completeness counts filled fields.

None of them senses whether the information is *accurate*, or whether consent is being given against a true picture of what is being consented to. This is **the verification gap, rendered as instrumentation**: a stack of procedural-availability proxies standing in for a legitimacy property they cannot reach. And informational integrity is the load-bearing right — the condition under which any other violation can be recognized at all — so a blind spot here is a blind spot that hides every other blind spot. The report is honest about this too: veracity-grading is exactly what it defers to the future "Semantic Governance" phase.

This closes a loop with the trajectory map. The constitution dropped IOG's Tenet 11 — the one tenet that named *verifiability and freedom from asymmetry* as a user right. The dashboard's deepest blind spot and the constitution's dropped tenet are **the same gap**, appearing once in the instrumentation and once in the normative text. Neither the rules nor the readings name veracity. That is not a coincidence; it is the governance-layer void showing up in both registers.

### 5 — Commons integrity · *partial — a treasury-capture seed, nothing wider*

The right that the shared substrate stays a commons owned by no subset is partly visible. **Success Rate by Source** and **Gov Action Volume & Source** are, in embryo, treasury-enclosure sensors — they can register whether allocations systematically favor structurally advantaged actors. **Entity Voting Power Concentration** touches the control-concentration dimension. So treasury enclosure is partially sensed, which is more than nothing. But protocol-layer enclosure, and the broader conversion of public capacity into private advantage beyond the treasury line item, have no instrument. The commons can be captured at layers the treasury metrics never look at.

### 6 — Self-determination · *essentially unsensed — the structural blind spot*

This is the synthesis right, and its distinctive abrogation is *temporal*: the slow capture of a participant's future through lock-in, dependency capture, and productive capture, accreting so gradually that no single step looks like coercion. The report is built from snapshots and rates. **Post-Vote Delegation Flow** (Future) and **Delegation Churn** touch *movement*, but they read it as liquidity and responsiveness — not as exit-remediability or as the onset of lock-in. Nothing senses exit becoming punitive, the commons engineering its own indispensability, or output being quietly redirected to maintain the position of controlling actors.

The temporal signature — harm below the threshold of any single observable event — is precisely what a snapshot-and-rate dashboard structurally cannot see. This is the audit's core warning in its purest form: the place where the growth panel is brightest and the integrity panel is darkest is exactly where a captured system keeps every metric green until the host fails.

### Summary

| Right | Sensed by the report? | The instrument(s) — and what they miss |
| :-- | :-- | :-- |
| **Settlement access** | Out of frame (appropriately) | Deposit Cost Burden touches the *submission* toll, not settlement. Transaction-layer right; belongs to the engine, not a governance dashboard. |
| **Unit-of-account integrity** | Shell only | Treasury Balance Rate / Spend-vs-NCL watch the treasury *level*. Nothing senses the *measure itself* being altered — the v2.4 "store of value" insertion would be invisible. |
| **Governance participation** | Best-sensed — quantitative axis only | Gini, DRep Correlation, Entity Concentration, Top-100 Volatility, Min Attack Vector sense the *walls* (stake-weighted enclosure). Interpretive/agenda enclosure — incl. CC scope-creep — under-sensed. |
| **Informational integrity** | Availability, not veracity | Rationale Rate, Info Availability, Data Parity, Metadata Completeness sense *existence/reachability/consistency*, never *truth*. The verification gap, instrumented. Load-bearing. |
| **Commons integrity** | Partial | Success Rate by Source is a real treasury-capture seed. Protocol-layer enclosure and wider public→private conversion: uncovered. |
| **Self-determination** | Essentially unsensed | Snapshots and rates cannot read a *temporal* abrogation. No lock-in / dependency-capture / productive-capture sensor. The structural blind spot. |

## The shape is the finding

Read the column of verdicts top to bottom and the pattern is unmistakable: the dashboard is **dense exactly where governance is countable and procedural** — turnout, Gini, rates, concentration, availability — and **dark exactly where legitimacy lives** — the veracity of consent, the integrity of the measure, the slow capture of a participant's future.

That boundary is not new. It is the *same* boundary as the verification gap (consensus proves procedure; legitimacy is not procedure), and the *same* boundary as the Tenet coverage in the trajectory map (dense on the transaction layer, thin on the governance layer). The instrument the ecosystem actually built reaches its leading edge precisely where verifiable reflexivity falls silent — and stops there. Three independent artifacts, the same seam.

One principle from the audit has to be wired in here, because the map invites the opposite reflex. *When a region goes dark, the instinct is to read "no information" as "no problem." That instinct is backward, and it is precisely the instinct capture relies on.* The bright, green, well-instrumented metrics — turnout climbing, Gini stable, treasury healthy — are not reassurance about unit-of-account integrity or self-determination. They are the dashboard of a region the field can see, sitting next to regions it cannot. A healthy sensor raises vigilance on what is visible when something goes dark. The correct reading of a green growth panel beside an unlit integrity panel is not "we are fine"; it is "we are blind in exactly the places capture would choose to operate."

## The blind instrument names its own blind spot

The report's final appendix lists its open questions for future iterations. The first item is:

> *Constitutional Debt: How do we define and measure "debt" in the Constitution (unresolved issues)?*

This is Failure 3 reaching its purest expression: the field's blind spot, named by the blind instrument itself. The single most sophisticated growth-and-participation panel the ecosystem has produced points, in its own closing pages, at the one thing it does not know how to measure — and that one thing is the constitutional debt, which is the same object as the governance-layer void, which is the same object as the unsettled rights.

The institutional context makes it sharper still. By the recovered history, the Governance Health effort is the initiative that advanced fast on growth metrics and drew energy and funding away from the Future Workstreams group — the body that existed to carry the debt forward — during the same window in which Constitution 2.0 slid off every Civics Committee agenda as "out of scope." The growth-instrument effort outcompeted the debt effort for attention, and the report that effort produced now names the debt as its open question. The instrument that won the resources is pointing back at the void the defunded effort was built to fill, and saying, in as many words: *I cannot see this.* That is not a failure of candor. It is the most honest thing a first panel can do — mark the edge of its own light.

## What this map calibrates

The audit closes on "the one number neither of us can set alone": how early and how wide the governance layer should sense pressure on the integrity axis — the kernel radius, tuned jointly by whoever owns throughput and whoever owns integrity, because set too narrow the field is blind at its leading edge and set too wide it becomes autoimmune.

This map is the **input** to that calibration, not the calibration itself. It says *where* the integrity panel is dark; it does not say how far ahead each dark region should be lit. Two of the six rights (unit-of-account integrity, self-determination) are effectively unlit; two are partial (commons integrity, governance participation on its qualitative axis); one is present-but-mismeasured (informational integrity, availability standing in for veracity); one is appropriately elsewhere (settlement access). That distribution is the agenda for the joint conversation. The throughput side will rightly ask which of these dark regions are worth the cost of a new sensor and which are distant shadows; the integrity side will rightly insist that the load-bearing one — informational-integrity veracity — cannot be deferred, because it is the sensor that makes every other sensor trustworthy. Neither side can set that alone. The map renders the tradeoff; it does not resolve it.

## How to use this finding

In the audit's register, the gaps are **fitness gaps, not accusations**, and each names something concrete that would close it:

- **Unit-of-account integrity** — a sensor that watches the monetary parameters and the unit's *definition* for substantive change, not just the treasury's balance. The first thing it would have caught is the T10 "store of value" insertion.
- **Informational integrity (veracity)** — the report's own deferred "Semantic Governance" phase, built on a derivation rather than on LLM-graded vibes. This is the one to refuse to defer; it is load-bearing.
- **Governance participation (qualitative)** — an interpretive-concentration sensor for the CC's sufficiency power, complementing the stake-weighted Gini suite already in place.
- **Self-determination** — a temporal sensor: exit-remediability and dependency-depth over time, reading the slow signal the snapshots cannot.
- **Commons integrity** — extend the Success-Rate-by-Source seed past the treasury to protocol-layer and public→private conversion.

And the register matters as much as the content. The GHWG built an honest, careful first panel and marked its own edge. The work here is not to grade that panel down but to build the second one it pointed at — the integrity sensor the rights derivation specifies, calibrated jointly with the people who own the first. That collaboration is the same shape, one layer down, as the whole relationship between the engineering and the rights work: neither half completes the instrument alone.

---

*Method note: this is a Failure 3 worked example, audited against the Cardano governance layer with the GHWG KPI Report v1.0 as the sensor inventory. The report is treated as the field's self-account, not as the object of audit. The six rights and the four failures are specified in the field-fitness audit; this example is intended to slot in as a companion appendix demonstrating the sensing check on a real instrument set.*
