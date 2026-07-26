---
title: Abstention Spines
subtitle: The vote-token layer — what each vote claims, when abstention is the honest instrument, and the disciplines that keep a standing posture from becoming a role
type: instrument
layer: 3
status: v1.0 (settled for use; re-version at seam review)
audience: [DReps, proposers, delegators, Constitutional Committee, governance working groups]
role: vote-token layer of the DRep voting framework; companion to the intake and sort
diagnoses: [silence mistaken for neutrality, sector-keyed standing policy, quantity substitution via spillover, standing posture drifting into role]
edges:
  - derives_from → Proposal Intake and Sort (lane assignment precedes token selection)
  - derives_from → holder_rights_articulation (the six rights as the violation tests)
  - refines → The Good That Is Not a Quantity (burden shift at the institution locus; the §7 held tension)
  - refines → Reciprocity Is Equality-Contingent (debt-language vs. role-language, run reflexively)
  - evidenced_by → v2.4 Amendment Voting Rationale (the ballot as wrong instrument)
  - instantiates → The Sieve and the Frontier (the repair operation, applied to standing policy)
related_rights: [commons integrity, self-determination, governance participation, informational integrity, unit of account integrity]
---

# Abstention Spines

*This document governs the last step: which token gets cast, and what that token claims. It runs downstream of the sort, which assigns depth of analysis. Depth is not a vote. This is where the vote is chosen.*

---

## 1. There is no null action

For a registered DRep the four options are three.

| Token | Numerator | Denominator |
|---|---|---|
| **YES** | ✓ | ✓ |
| **NO** | — | ✓ |
| **SILENCE** | — | ✓ |
| **ABSTAIN** | — | — |

Silence and NO are mechanically indistinguishable. Every action that crosses the desk receives a vote whether or not one is cast, and the uncast vote is NO.

Two consequences, and they run opposite to intuition.

**The DRep who quietly skips what they haven't studied is casting unearned NOs at volume.** Not neutrality — obstruction, delivered by default and never rationalized. Under this framework that is the worst available posture, because it produces findings without analysis and never has to say so.

**Explicit abstention is the only genuinely neutral act available,** and it is neutral in a specific sense: it returns delegated stake to inertness. Against the counterfactual of NO it lowers the passage bar; against the counterfactual of the stake not existing it is exactly nil.

So the operative question is not *am I helping this pass*. It is:

> **Have I derived a warrant to deploy delegated stake against this?**

NO deploys. ABSTAIN withholds deployment. The burden sits on the derivation, where this framework puts every other burden.

*Verification note: these mechanics follow CIP-1694's treatment of active voting stake. Thresholds and vote-counting rules are themselves governance-controlled and have been amended. Re-verify against current ledger rules at each seam review rather than treating this table as settled.*

---

## 2. The boundary rule

> **NO is a claim about the action. ABSTAIN is a claim about the fit between the ballot and the action.**

If the analysis produces a finding about the action's effect, that finding is expressible as NO and NO is owed. If the analysis produces a finding the ballot cannot carry, ABSTAIN is the honest token and the rationale does the work the vote cannot.

### Two species of NO

They are not interchangeable, and the rationale must say which one it is.

**NO-remediable — the burden was not discharged.** The proposal failed a published test. The defect is in the submission, not in the thing submitted. This NO is a specification: it names what would make the resubmission succeed. Register is instructional, not adversarial.

**NO-terminal — a commons relation is harmed.** A rights finding. The defect is in the action, and no resubmission of the same action cures it. This NO does not offer a path, because offering one would misrepresent the finding.

Collapsing these makes every NO read as terminal, which converts a mentoring posture into an obstructive one at exactly the moment the framework is trying to teach. Keep them separate in the rationale, in the log, and in the trajectory record — the ratio between them over time is itself a reading of whether the published burden is doing its work.

---

## 3. The five spines

Each spine is a fixed skeleton with tuned slots. The skeleton is what makes the methodology auditable across cases; the slots are what keep it from being a rubber stamp.

### Spine 1 — Instrument mismatch

**What it claims.** The analysis produced a finding the ballot cannot carry.

**Two directions, and both occur.**
- *Ballot narrower than the object.* The action is unobjectionable on its own terms; its real significance is as evidence of a trajectory. NO misrepresents the action; YES ratifies the trajectory reading.
- *Ballot weaker than the object.* A structurally load-bearing constraint is carried by a non-binding instrument. The Net Change Limit is the standing case: it conditions how every downstream treasury action is read, which places it high on epistemic-dependency, yet it arrives as an Info Action.

**Trigger test.** Can the finding be stated as a property of *this* action? If the finding is about the class, the trajectory, or the instrument itself, the ballot cannot reach it.

**The rationale must carry** the finding in full. This spine is the one where the rationale is the entire point of voting at all.

**Guard — and this spine needs one, because it is the most abusable.** *The mismatch must be statable before knowing which way the vote would otherwise go.* "The ballot can't reach my concern" will excuse any inconvenient vote if allowed to arrive late. If the mismatch appears only once a NO looks costly, it is rationalization and the token is NO.

**Expiry.** Recurring mismatch on the same instrument is not a series of individual abstentions — it is a finding about the instrument, and it belongs in the trajectory log as a candidate for a proposal rather than a vote.

---

### Spine 2 — Jurisdictional

**What it claims.** No rights-relevant reading exists. The question falls entirely within a domain the derivation does not reach.

**Narrower than it appears.** The framework has process purchase almost everywhere, even where it has none on the merits. A hard fork qualifies only when the guardrails discipline, testing record, and rollback story are clean — because if they are not, the finding is procedural and the derivation reaches it.

**Trigger test.** Run all six rights. All six return null, *and* the procedural checks pass. Both conditions, not either.

**Not this spine:** "I don't understand the technical content." That is either insufficiency or an obligation to study, and dressing it as jurisdiction is a competence claim disguised as a scope claim.

**The rationale must carry** which domain, why the derivation is silent there, and what would give it purchase.

**Expiry — and this one matters.** Repeated jurisdictional abstention in the same domain is not a stable scope limit. It is a gap in the derivation. Log the recurrence; after the second, the appropriate response is corpus work, not another abstention.

---

### Spine 3 — Burden contested

**The standing thing is the burden, not the abstention.** This is the correction that this spine exists to encode. A standing abstain keyed to a *sector* fires on recipients rather than on claim structure, and it fires wrongly — a for-profit maintainer of a non-rival, discretely-delivered tool presents a commons-derived claim by every axis the framework recognizes. Keyed to sector, the policy would obstruct it; and since abstention has a direction, the mis-fire is not a null act.

**The published burden** (full text at Appendix A): any proposal seeking treasury funds for an activity generating private surplus must demonstrate that a commons relation is maintained, stated in relation terms. Expected-value and ecosystem-growth arguments do not discharge it, because they answer a quantity question in place of the relation question.

**Where each outcome lands.**

| Situation | Token |
|---|---|
| Burden discharged; relation genuinely served | Evaluate on the merits like anything else |
| Burden not attempted; relation not articulable | **NO-remediable** — a stated, published test was failed |
| Relation harmed | **NO-terminal** |
| Burden attempted in good faith; contest is at the margin | **ABSTAIN — this spine** |

**Trigger test.** The relation argument was made, is intelligible, and the disagreement sits where "maintaining the relation" and "managing the quantity" describe the same trade from two honest frames. That margin is real and the corpus is explicit that it should not be pretended crisp; collapsing it prematurely reintroduces foreclosure from the other direction.

**The rationale must carry** what would have discharged the burden, what was offered, and precisely where the two frames diverge. It must *not* adjudicate the margin — the abstention is the acknowledgment that the margin is genuine.

**Seam note, to be carried in the rationale rather than hidden.** The burden's answerability rests on the money ontology: the index points outward to a network of *productive* claims, so growth reflecting real productive activity serves the relation while growth in price, valuation, or attention does not. That is what makes the burden specific rather than rhetorical. It is also the part of the corpus most likely to re-version under real usage. State the ground with the burden, so that if the ontology moves the burden moves with it rather than outliving its justification.

---

### Spine 4 — Insufficiency

**What it claims.** The proposal cannot be evaluated, and NO would assert a merits finding that has not been earned.

**The distinction that carries the whole spine.**
- Completeness *required* by the constitution or the framework, and absent → **NO.** That is a finding.
- The framework's own novel questions — Q4 reversal, Q6 dependency, Q7 self-registration — unasked and therefore unanswered → **ABSTAIN.** The gap is in the ecosystem's vocabulary, not in the proposal's compliance.

**The rationale must carry** which questions went unanswered, and the acknowledgment that they were novel. Opacity raises vigilance on the reading, not on the proposer.

**Expiry, with a named horizon.** Once the intake questions are published and in circulation, "unanswered" stops being novel. Set the horizon explicitly — **one full governance cycle after publication** — after which an unanswered Q4/Q6/Q7 converts from insufficiency-abstain to NO-remediable. Without a named horizon this spine has no floor and will quietly absorb every hard case.

---

### Spine 5 — Reflexive

**What it claims.** The DRep is a party, a beneficiary, or a downstream consumer of the thing being decided.

**Mandatory at D3** — the band where the field funds its own eyes.

**Trigger test: specific versus general interest.** A specific interest is one the proposal creates or reinforces — it funds an instrument your readings run through, or a body you sit in. A general interest is the condition of being a participant at all: you hold ada, you use the chain, you benefit from its security. General interest does not disqualify, and treating it as though it did would hollow out participation entirely and hand the field to those who claim no stake.

**The rationale must carry** the nature of the interest, stated plainly and without minimization.

---

## 4. The expiry discipline

**Every standing posture carries three things or it is not legitimate:**

1. **The derivation** that produced it.
2. **The condition under which it lifts** — stated positively, as something that could actually obtain.
3. **A review cadence** — a date, not a feeling.

The reason is reflexive and it comes from the corpus. Under a co-constituent framing an institutional posture registers as a debt and generates an expectation of correction. Under a hierarchical framing the same posture registers as precedent — *that's just what they do* — and the bookkeeping stops. A standing abstention without an expiry is exactly how a DRep's own practice completes that transition. The sensor built to detect relational drift has to be run on the hand holding it.

Practical form: a public register of standing postures, each with derivation, lift condition, cadence, and date of last review. Postures past review date are suspended, not carried.

---

## 5. The mentoring hazard

Coaching a proposer toward a relation-articulation before the vote is a deliberative pre-stage, privately supplied. It partially reconstructs at the DRep layer a capacity the constitution removed, and it is the most valuable thing this framework enables.

It also accrues informal interpretive authority — the judicial-supremacy concern, reappearing one level down, at the DRep's own level. A proposer who succeeds because they got the private coaching, in an ecosystem where others did not, has been governed by something that never appeared in any register.

**Two disciplines, both cheap.**

- **Publish the burden** so that the coaching is redundant. The published test is the anti-capture form of the private lesson. This is the primary remedy and it is already in hand.
- **Keep the exchange in public register.** Where coaching happens, it happens where it can be read. Not because private conversation is illegitimate, but because a deliberative stage that exists only in DMs is a deliberative stage no one can audit — and the whole argument for reconstructing it was that the ecosystem needed one it could see.

---

## 6. The spine template

Fixed skeleton. Tuned slots in brackets. Every abstention rationale carries all seven; none is optional, and a slot that cannot be filled is a signal the spine was mis-selected.

1. **Token and spine.** *Abstain, [spine name].*
2. **Sort record.** Axis readings, lane assigned, instruments run. Carried forward from intake, not restated.
3. **What the analysis found.** The substantive reading, in full. Length tracks the finding, not the token.
4. **Why the ballot cannot carry it.** The mismatch, stated specifically. This is the slot that distinguishes abstention from evasion.
5. **What this abstention does mechanically.** Plain statement that the stake is withheld from the active voting stake and that this is not the same as opposition. Delegators are owed this every time.
6. **Lift condition.** What would change the token, stated as something that could obtain.
7. **Distal-signal.** Anything the reading surfaced that belongs in the trajectory log rather than in this vote — aggregate, temporal, or semiotic signals that no single action carries.

Slot 7 is where this framework's distinctive value accumulates. A vote is a snapshot; the log is the trajectory; and trajectory over snapshot is the commitment the original rationale made.

---

## Appendix A — The private-surplus burden, as published

> **Treasury funds may fund the maintenance of commons relations. They may not fund the transfer of a private surplus.**
>
> This is a test of claim structure, not of the recipient. A for-profit entity maintaining a non-rival good the ecosystem depends on presents a commons-derived claim. A non-profit entity funding an activity whose benefit is captured privately does not. The recipient's tax status is not asked and does not bear on the answer.
>
> **Where a proposal seeks funds for an activity generating private surplus, the burden is on the proposal** to demonstrate that a commons relation is maintained, stated in relation terms — what capacity, security, or standing of the commons this preserves, and how its degradation would be recognized.
>
> **Expected-value and ecosystem-growth arguments do not discharge this burden.** They answer a quantity question — *will the number rise in expectation* — in place of the relation question, and once the substitution is accepted the legitimacy question has been answered in the quantity's terms before it could be asked.
>
> **Growth arguments are answerable, and specifically.** The unit is an index pointing outward to a network of productive claims. Growth that reflects real productive activity does serve the relation. Growth in price, in total value locked, or in attention does not. Show productive activity.
>
> **A proposal that does not attempt the burden receives a NO that names what would succeed on resubmission.** A proposal that attempts it in good faith and is contested only at the margin receives an abstention that says so. A proposal that harms a commons relation receives a NO that offers no path, because none exists.

---

*Method note: this instrument selects vote tokens downstream of the sort. Its central mechanical premise is that silence is not neutrality — for a registered DRep, the uncast vote is a NO — and its central discipline is that no standing posture survives without a derivation, a lift condition, and a review date. Findings are fitness gaps, not accusations. The five spines are the abstentions visible now; the method for finding a sixth is the same method that found these, and the list is expected to move.*
