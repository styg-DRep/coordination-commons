---
title: Proposal Intake and Sort
subtitle: The three axes that decide how much analysis a governance action earns — and the intake form that reads them
type: instrument
layer: 3
status: v1.0 (settled for use; re-version at seam review)
audience: [DReps, proposers, Constitutional Committee, treasury administration, delegators]
role: ingestion layer for the DRep voting framework; public methodology artifact
diagnoses: [sector-label batching, significance scoring, wall-to-knob conversion, self-concealing dependency]
edges:
  - derives_from → field-fitness-audit (the four failures; Failure 3 sensing; kernel-radius calibration)
  - derives_from → holder_rights_articulation (the six rights as the integrity sensor)
  - refines → The Good That Is Not a Quantity (entrenchment test; burden shift; wall-to-knob tell)
  - instantiates → The Sieve and the Frontier (walls and knobs)
  - evidenced_by → v2.4 Amendment Voting Rationale (procedural fail-state as a finding independent of merits)
  - tested_by → three open-source infrastructure archetypes (Appendix A)
related_rights: [informational integrity, commons integrity, self-determination, governance participation, unit of account integrity]
---

# Proposal Intake and Sort

*Every governance action gets read. Not every governance action earns the same reading. This document fixes how that decision is made, so that it is made the same way twice and can be audited by anyone.*

---

## 0. What this instrument does and does not do

This is the ingestion layer. It takes a governance action and returns **a lane** — how much analysis the action earns, and which instruments run on it.

It does **not** return a vote. It does not score, rank, or recommend. The distinction is load-bearing and is imported directly from the governing register principle: *persuade about the problem; instrument the reading.* An intake form that delivered verdicts would be a persuasion funnel wearing an instrument's clothes, and would fail the same test this framework applies to everything else.

It is published for two reasons. First, transparency: a methodology that cannot be inspected cannot be argued with, and the argument is the work. Second, co-learning: two of the seven questions below are questions no proposal template currently asks, and the most useful thing this artifact can do is make them askable.

**A note on register, held throughout.** A low sort result is not a low-quality proposal. A high sort result is not an accusation. The sort measures *how much can go wrong that would not announce itself* — nothing more. Most good proposals sort shallow. That is what shallow means.

---

## 1. Why type is not the sort key

Cardano defines seven on-chain action types. They are the right unit for the ledger and the wrong unit for analysis, because they do not track anything the derivation cares about. Two treasury withdrawals with identical sector tags can sit three tiers of scrutiny apart; a parameter change and a treasury withdrawal can sit in the same cell.

Sector labels fail the same way, and worse, because they invite batching by the recipient's tax status rather than by the structure of the claim.

The sort therefore runs on three axes drawn from the derivation. Action type and sector are retained as **metadata**, not as sort keys.

---

## 2. Axis 1 — Wall, knob, or wall-building

**The distinction.** A *wall* is a structural constraint whose function is to make a class of outcome unreachable by ordinary governance count. A *knob* is a setting whose function is to be tuned within a range. A wall is not a knob set very tight; it is a different kind of object, and the difference is what the two remaining axes explain.

**Three states, not two.**

| State | Definition |
|---|---|
| **Knob** | Tunes a setting within the existing constraint structure. The structure itself is untouched. |
| **Wall-touching** | Approval requires a constraint currently treated as unreachable to be treated as tunable — *or* installs a structural default where a per-action decision stood. |
| **Wall-building** | Installs or hardens a structural constraint. |

**Wall-building is not presumptively good.** It faces the entrenchment test in the other direction: hardness should track inverse exit-remediability and epistemic-dependency depth, so a proposed wall must show that the failure it guards is genuinely irremediable or genuinely self-concealing. A wall installed around a remediable, visible failure is a knob welded shut, and a knob welded shut is a standing invitation to capture on the other side.

**The fail-state is not touching a wall.** Walls can be legitimately changed; that is what an amendment is for. The fail-state is touching a wall **through an instrument that does not acknowledge it** — an amendment wearing interpretation's clothes, or a structural default installed through an ordinary funding action.

**Tells, in rough order of reliability:**

- The action changes *what range exists* rather than a setting within a range.
- The action is framed as clarification or interpretation but cannot proceed without a structural constraint being reinterpreted.
- The action converts a recurring decision into a default (renewal-by-default, standing authority, evergreen allocation). Defaults are walls in reverse: they make the *absence* of a decision determinative.
- The action admits a class of claim-holder whose entitlement does not reconstruct from the participant-rights framework and sits senior to the commons' own discretion.

**Burden.** Where the wall-touching reading is contested, the burden sits on the party proposing that the constraint is tunable — not on the party asserting it is a wall.

---

## 3. Axis 2 — Exit-remediability

**The definition.** The cost and reachability of reversal if the action proves wrong. Not "is it technically reversible" but: *who* must act, through *what instrument*, against *whose* resistance, and does the passage of time raise or lower that cost.

**Measure the failure mode, not the action.** This is the single most common misreading and the one to guard hardest. An action can be trivially reversible while the failure it enables is not. A treasury deployment can be unwound on paper while the position it created cannot be exited in the crisis that would require exiting it. A delegation constraint can be restored after a vote it already moved. Ask what happens if this is *wrong*, then ask whether *that* can be undone.

**Bands.**

| Band | Reading |
|---|---|
| **R3 — reversal by inaction** | The action lapses on its own terms. Not renewing is the default. |
| **R2 — reversal by ordinary action** | Reversible through normal process, against no interest the action itself created. |
| **R1 — reversal by contested action** | Reversal requires initiating against a party holding resources, standing, or dependency created by the original action. |
| **R0 — irremediable** | The failure mode cannot be undone after the fact regardless of subsequent action. |

**Decay flag.** Remediability is not static. Dependency-generating actions have *decaying* remediability: an action that reads R2 at enactment reads R1 at renewal and R0 at the third cycle, without any further decision being taken. Where decay is present, sort on the terminal band, not the opening one, and record the decay explicitly. This is the temporal signature of self-determination abrogation, and it is the reason no single snapshot of an action reads it correctly.

---

## 4. Axis 3 — Epistemic-dependency depth

**The definition.** How many other readings are conditioned by this one. Not how important the action is — how much else becomes *unreadable*, rather than merely wrong, if this is wrong.

**Bands.**

| Band | Reading |
|---|---|
| **D0** | Nothing reads through it. |
| **D1** | Conditions readings within its own domain. |
| **D2** | Conditions readings the governance layer uses to evaluate *other* actions. |
| **D3** | Conditions the field's account of itself — including the sensor that would register this action's own failure. |

**D3 is the reflexive band, and it is the one the growth dashboard cannot see.** A reading that conditions its own detection fails invisibly by construction: the corruption disables the instrument that would catch it. This is the informational-integrity finding at the funding layer, and it is why entrenchment hardness tracks self-concealment depth rather than stated importance.

**The D3 question, stated plainly:** *if this degraded, what would register the degradation — and does that registration run through the thing being funded?*

---

## 5. The routing rule

The three axes are **not collapsed into a score.** This is deliberate and it is not fastidiousness: a single significance number would be a quantity substitution performed on the framework's own instrument — the relation (how much can go wrong unseen) reified into a proxy (a rank), with an optimization frame following it in. The axes are non-collinear by design. An action can be maximal on one and null on the other two, and the reason *which* axis it is maximal on determines which instruments run.

Routing is therefore lexical, not additive. Run in order; the first match assigns the lane.

1. **Wall-touching through a non-acknowledging instrument** → **Gate 2 arrest.** Structural analysis only. The finding is procedural and stands independent of the merits; no merits analysis is owed, and offering one would obscure the finding. The rationale must state what would make this a different proposal.
2. **R0 or R1 (including by decay)** → **full lane.** Hippocratic floor, six-rights read, trajectory and precedent assessment.
3. **D3** → **full lane + mandatory distal sensing + mandatory reflexive check.** The reflexive check is not optional here: D3 is by definition the band where the field is funding its own eyes.
4. **D2 with an aggregate, temporal, or semiotic harm signature** → **full lane + distal sensing.**
5. **Wall-building** → **full lane**, running the entrenchment test in the confirming direction.
6. **Everything else — knob, R2/R3, D0/D1** → **shallow lane.** Procedural check, Hippocratic floor, public-goods reconstruction, vote, short rationale.

**Distal sensing is triggered by harm signature, not by action type or by stakes.** Discrete harms are already covered by the violation tests; running the distal battery on them is cost without signal, and a sensor that fires on everything is the autoimmune failure the kernel-radius calibration exists to prevent. Distal sensing fires on harms that are aggregate (no single step is the violation), temporal (the capture is of a future), or semiotic (the reframing precedes and enables the taking).

---

## 6. The intake form

Seven substantive questions. Each is tagged with the axis it feeds and with whether the proposer can answer it or the DRep must derive it. **Answers are not taken at face value where the axis is contested; the tags say who speaks first, not who decides.**

### §0 — Identification *(metadata, not sort key)*
GAID · on-chain action type · submission and expiration epochs · proposer · amount and denomination · sector, if one is claimed.

### §1 — The good
**Q1. What is the good, stated as a relation rather than a deliverable?** *(proposer)*
A deliverable is a thing produced. A relation is a capacity, security, or standing the commons maintains. Both are legitimate answers; the question is which one is being funded, because only the second is a public good in this framework's sense.

**Q2. Is the good rivalrous? Who is excluded, and by what mechanism?** *(proposer; DRep verifies)*
Feeds the public-goods reconstruction. Note that the recipient's commercial or non-commercial status is *not* asked here and does not bear on the answer.

### §2 — The constraint landscape *(Axis 1)*
**Q3. Does approval require any structural constraint to be treated as tunable, or install a default where a per-action decision now stands?** *(DRep derives; proposer may contest)*
Includes: denomination requirements, delegation and auto-abstain constraints, seniority rules, per-cycle decision points, and any renewal that occurs by default rather than by action.

### §3 — Reversal *(Axis 2)*
**Q4. If this were wrong in eighteen months, what reverses it — who initiates, through what instrument, against what resistance?** *(proposer answers; DRep derives independently)*

**Q5. Does the cost of reversal rise over the life of the action?** *(DRep derives)*
The decay flag. Sort on the terminal band.

### §4 — Dependency *(Axis 3)*
**Q6. What reads through this? Name the downstream readings and count the layers.** *(proposer answers; DRep derives independently)*

**Q7. If this degraded, what would register the degradation — and does that registration run through the thing being funded?** *(DRep derives; proposer's answer is itself data)*

### §5 — The reflexive check *(mandatory at D3, discretionary elsewhere)*
Does this action fund, condition, or constitute any instrument through which this DRep's own readings are made? Is the DRep a party, a beneficiary, or a downstream consumer? A sensor that cannot read the hand holding it is not a sensor.

### §6 — Sort output
Axis 1 state · Axis 2 band (+ decay flag) · Axis 3 band · lane assigned · instruments triggered · **no vote, no score, no recommendation.**

---

## 7. Reading a non-answer

Q4, Q6, and Q7 are not currently asked by any proposal template in the ecosystem. Most proposals will not answer them, and **a non-answer is not a defect in the proposal.** It is a reading of the ecosystem's present vocabulary, and it belongs in the trajectory log rather than in the finding.

The distinction that does matter: a proposal that *cannot* answer Q7 and a proposal that *has not been asked* Q7 are different objects. Where the question has been put and the answer is unavailable, that unavailability is substantive — the absence of a sensor is exactly what Failure 3 reads. Where the question was never put, the appropriate response is to put it, publicly, and let the answer inform the next cycle.

Opacity raises vigilance; it does not lower it. But it raises vigilance on the *reading*, not on the proposer.

---

## 8. Interaction with standing policies

**The sort runs before any standing policy is applied.** This ordering is protective, and the case it protects against is concrete: a for-profit entity maintaining a widely-used open-source tool carries a commercial sector label while presenting a non-rivalrous good with discrete delivery — a commons-derived claim by every axis that matters. A standing policy keyed to the sector label would fire on it wrongly.

That mis-fire is not a null act. Explicit abstention removes delegated stake from the active voting stake and therefore lowers the bar for passage, which means a mis-triggered standing abstain has a direction. The sort is what keeps standing policy from doing work the derivation did not authorize. *(Treated fully in the abstention spines; noted here because the ordering constraint lives in this document.)*

---

## 9. How to use this

**Run it over time, not once.** Actions with decay flags must be re-sorted at each renewal, and the movement between sorts is the finding — not either sort alone.

**Run the sort before reading the merits.** The lane determines which instruments run. Reading the merits first and then choosing the depth is how the depth ends up chosen to fit a conclusion already reached.

**Publish the sort with the rationale.** The lane assignment and the axis readings are part of the reasoning, not scaffolding to be discarded. A reader who disagrees with the vote should be able to locate whether the disagreement is about the sort or about the analysis, because those are different arguments and only one of them is about the proposal.

**Argue with the axes.** Find an action the axes sort wrongly and the axes change. That is the mechanism by which this instrument stays an instrument.

---

## Appendix A — Calibration: three open-source infrastructure archetypes

Constructed, not real. All three carry an identical sector tag and an identical ask shape.

| | **A — discrete maintainer** | **B — instrument layer** | **C — standing administrator** |
|---|---|---|---|
| Shape | 12-month funding, named deliverables, sunsets at term | Operational funding for chain-indexing, metrics, or governance-portal infrastructure | Multi-year evergreen allocation to an administering entity, renewal by default |
| **Axis 1** | Knob | Knob | **Wall-touching** — installs a structural default; touches the funds-holding constraint |
| **Axis 2** | R3 — lapses on its own terms | R1 — reversal contested; the capacity to *notice* degradation runs through the thing degrading | R1, decaying toward R0 |
| **Axis 3** | D1 | **D3** — the governance layer's self-account renders through it | D2 |
| **Lane** | Shallow | Full + distal sensing + reflexive check | Gate 2 arrest |

**What the sort caught.** A and B are indistinguishable by sector, by ask shape, and by register, and sit two tiers apart. B is the case where the framework has something to say that nothing else in the ecosystem is saying — and it is a live instance of the standing distal-sensor inquiry, arriving as a vote rather than as an architectural question.

**What the sort refused.** B and C are both high-entrenchment for entirely unrelated reasons, and neither is high on all three axes. Any composite score would have flattened that difference and routed them identically. They route to different lanes and produce different findings.

---

*Method note: this instrument sorts governance actions by how much can go wrong that would not announce itself. It assigns depth of analysis; it does not assign votes, and its output is never a verdict. The three axes are drawn from the field-fitness audit and the entrenchment findings; the routing rule is lexical rather than additive by design. Findings are fitness gaps, not accusations. Re-run each cycle; sort before reading merits; publish with the rationale.*
