# Scalus 2026 — Treasury Withdrawal (₳2,464,844) — Voting Rationale

| Governance Voting Rationale |  |
| ----- | :---- |
| GAID | *[Scalus 2026 GAID — to be filled]* |
| Title | Scalus 2026: Maintenance, Dijkstra Readiness, Interoperability & Application Runtime (Lantr Engineering) |
| Type of GA | Treasury Withdrawals |
| Date submitted | *[epoch / date — to be filled]* |
| Expiration Date | *[epoch / date — to be filled]* |

# Contents

- [1.0 Introduction](#1.0-introduction)
  - [1.1 Summary](#1.1-summary)
  - [1.2 Description of Governance Action](#1.2-description-of-governance-action)
- [2.0 Discussion](#2.0-discussion)
  - [2.1 The question a for-profit treasury request has to answer](#2.1-the-question-a-for-profit-treasury-request-has-to-answer)
  - [2.2 Why this reads as a low-scrutiny proposal — and why that is the right reading](#2.2-why-this-reads-as-a-low-scrutiny-proposal)
  - [2.3 The construction, and the money it asks for](#2.3-the-construction-and-the-money-it-asks-for)
  - [2.4 What the vote does not reach](#2.4-what-the-vote-does-not-reach)
- [3.0 Conclusion](#3.0-conclusion)
- [References / Sources](#references-sources)

# 1.0 Introduction {#1.0-introduction}

## 1.1 Summary {#1.1-summary}

We are voting **YES** on the Scalus 2026 treasury withdrawal — ₳2,464,844 over nine months to Lantr Engineering, to maintain the Scalus development platform, ready it for the Dijkstra hard fork, deepen its reuse across the JVM and JavaScript stacks, and ship a scoped first step toward an application runtime.

The reason is straightforward, and its being straightforward is the point. Scalus is open-source infrastructure the ecosystem already depends on — directly, in the protocols built on it, and indirectly, through its components embedded in tooling many teams use every day (MeshJS, Lucid Evolution, Evolution SDK, the Cardano Client Lib, Yaci). Keeping a shared, freely forkable good like that maintained and current through a protocol transition is close to the clearest case there is for what the treasury exists to fund.

There is a test this DRep applies to any treasury request from a for-profit entity, and it is worth naming because Lantr is one: a for-profit drawing treasury funds has to show its claim rests on maintaining something the whole ecosystem depends on and can freely use, not on growth it projects while keeping the upside. Scalus meets that test plainly — the good is a non-rival public asset under an open licence, and the ask funds the effort to maintain and extend it, with no private-surplus mechanism attached. The construction around the money is sound, the amount is modest, the exposure is staged, and the whole thing reverses simply by not being renewed. This is a proposal with little that could go wrong unseen, and that is exactly what a low-scrutiny reading means. The one thing worth carrying forward is not an objection but a note for future cycles, set out at the end.

## 1.2 Description of Governance Action {#1.2-description-of-governance-action}

This Treasury Withdrawals action requests ₳2,464,844 (about $394,375 at the proposal's $0.16/ADA reference rate) for nine months of milestone-based work, July 2026 through March 2027, with no contingency. Lantr Engineering is the sole vendor. The work spans three lines beyond continuous maintenance: readiness for the Dijkstra hard fork (Plutus V4, nested transactions, accounts, and the associated ledger and tooling changes), interoperability improvements across the JVM and JS/TS ecosystems, and a bounded first release of an application runtime, validated through reference applications and early users.

The funds are held and released through the audited SundaeSwap treasury-contracts framework, with milestone-based vesting, an independent oversight board (members from Blink Labs, the Cardano Foundation, and IOG) that co-signs disbursements and can pause or halt funding, third-party technical assurance from No.Witness Labs, and an independent financial audit. Escrowed funds are set to auto-abstain in governance and cannot be delegated to a stake pool, and anything unspent at expiry sweeps back to the treasury automatically. The proposal is a reduced resubmission of an earlier, larger Scalus proposal (₳8.5M over twelve months), rescoped to answer the scale concerns raised in that vote. It discloses prior funding — earlier Catalyst awards and a 2025 treasury grant of ₳657,692 — and sits within the current 350M net-change limit at submission.

# 2.0 Discussion {#2.0-discussion}

## 2.1 The question a for-profit treasury request has to answer {#2.1-the-question-a-for-profit-treasury-request-has-to-answer}

The treasury is a shared resource, held in trust for the whole ecosystem, and a for-profit company asking to draw from it raises a fair question about the shape of the claim. This DRep states that question as a standing test, published so it is applied the same way every time: the question is not whether the recipient is a company — it is whether the thing being funded is the maintenance of something the ecosystem collectively depends on and can freely use, or the funding of a private venture that keeps its own upside. The first is a claim rooted in the commons. The second is not, and arguments from projected growth do not convert one into the other.

Scalus discharges that test about as cleanly as a for-profit request can. The good is open-source under Apache 2.0 — non-rival, freely usable, and forkable, so nothing here is enclosed or made exclusive. Its degradation would be felt across the ecosystem precisely because so much tooling embeds its components, which is the mark of a genuine commons relation rather than a private one. And the ask carries no private-surplus instrument: no performance fee, no equity, no revenue share. The funding buys engineering effort, priced as effort, against a public asset the ecosystem keeps regardless of how Lantr fares commercially. That the same team also builds commercial products on top of Scalus does not change this — the platform itself remains the shared, forkable good, and the treasury is paying to maintain that good, not to underwrite the products. This is worth saying with some care because the contrast is real: a request that asked the treasury to fund growth while routing the resulting upside to a private party would be a different proposal facing a much harder question. This one does not.

## 2.2 Why this reads as a low-scrutiny proposal — and why that is the right reading {#2.2-why-this-reads-as-a-low-scrutiny-proposal}

This DRep sorts every action before reading its merits, to decide how much scrutiny it earns — the goal being to spend the most attention where the most could go wrong without announcing itself. Scalus earns a light reading, and it is worth being explicit that "light" is a description of risk surface, not of quality. A few things account for it. This is a single, self-contained decision, not one half of a pair of actions arranged so the real commitment lands where scrutiny is lowest — a maneuver this DRep watches for, and which is simply absent here. It tunes a spend within the existing rules rather than changing any structural constraint or installing a standing default. If it proves a poor use of funds in eighteen months, reversing it costs nothing more than declining to renew: the term ends on its own, unspent funds return automatically, and because the code is open-source and forkable, the ecosystem keeps everything already built and no party is left holding leverage against the reversal. And if the work degraded, the degradation would show up loudly through ordinary channels — public repositories, releases, download counts, conformance tests, third-party assurance, and the many dependent projects that would notice breakage first.

None of those readings requires trust in the proposer; they are properties of the action's structure, and they are the reason this proposal does not need the deeper machinery this DRep reserves for actions that can fail quietly or irreversibly. Most sound proposals read this way. A framework that manufactured suspicion here would be miscalibrated, and part of what this reading is for is to say plainly when there is little to contest.

## 2.3 The construction, and the money it asks for {#2.3-the-construction-and-the-money-it-asks-for}

This DRep's framework reads relations rather than pricing allocations, so the question of whether ₳2,464,844 is well spent — the right amount, the right instrument, a good use of finite treasury against everything else it could fund — is read through a separate capital-stewardship instrument maintained by a peer DRep. For open-source infrastructure, that instrument treats the continuity of the public asset itself as the principal return to the treasury, which is the right frame for what this is.

On that reading the proposal is in good order. The amount is modest — roughly on par, in dollar terms, with the single 2025 grant, and a substantial reduction from the earlier version. The exposure is staged rather than released at once: milestone vesting, a board that must co-sign disbursements and any one of whose members can pause a milestone, and an automatic sweep of anything unused. The delivery record is real — every milestone of the 2025 cycle was delivered on time, with additional work beyond the committed scope. The ADA pricing is honest: the $0.16 reference rate sits slightly below the current market price of around $0.17, and the proposal commits to hedging into stable assets on receipt, a direct and candid response to the roughly fifty-percent purchasing-power loss the 2025 grant suffered as ADA fell during that delivery window. Most importantly for a capital-stewardship read, there is no private-capture structure for the instrument to flag — no upside routed away from the commons. The allocation reading concurs with the vote; it finds nothing that should lower it.

## 2.4 What the vote does not reach {#2.4-what-the-vote-does-not-reach}

A few observations belong in this DRep's longer-run record rather than in the vote, because they are about trajectory across cycles rather than about this action, which is sound.

The first concerns the application runtime. It is the one workstream that reaches beyond maintaining what already exists toward building something new, and while it is bounded, open-source, and validated with real teams this cycle, it is the part most worth watching over time. An application runtime that the ecosystem comes to build on could, in a few cycles, become infrastructure whose health the ecosystem reads *through* — at which point a future Scalus proposal would earn a deeper look than this one does. That is a note for the next reading, not a reservation on this one.

The second is about recurring funding generally. This is the second Scalus treasury withdrawal in twenty-four months, and a maintainer the ecosystem depends on can, over enough cycles, drift from being funded because it earns each round toward being funded because too much now depends on it to stop. The thing that keeps that exit genuinely open is the forkability of the code, and the honest discipline is to re-read at each renewal whether that exit is still real. Today it plainly is.

The last is not about Scalus at all. The proposal's own retrospective describes a treasury process where a bundled budgeting path stretched five to six months from proposal to first payment, offered no protection against ADA's decline, and carried standing governance risk in the bundling itself — enough that this proposer, like others before it, chose to submit independently and on-chain instead. That teams capable of maintaining critical infrastructure are routing around the coordinated process is a signal about the process worth tracking on its own, separately from any single vote.

# 3.0 Conclusion {#3.0-conclusion}

We vote **YES**. Scalus is public infrastructure the ecosystem already relies on, the request maintains and extends it as a freely forkable common good, and the for-profit test that a treasury request of this kind must meet is met plainly — the claim rests on a maintained commons relation, not on a private surplus. The construction is sound, the amount modest, the exposure staged, the delivery record demonstrated, and the whole action reverses by simply not being renewed.

The framework's work here was not to find fault but to confirm that the burden is discharged and the risk surface is genuinely shallow, and to say so without manufacturing scrutiny the action does not warrant. The one thing carried forward is a matter for future cycles rather than this vote: to re-read, as the runtime grows and the funding recurs, whether the ecosystem's exit from this dependency stays as open as the code's licence currently keeps it.

Thank you for reading this rationale and for supporting it with your delegation.

# References / Sources {#references-sources}

The following background may help a reader new to this DRep's approach. Each is linked once, at first relevance:

- *The evaluation framework* — this DRep's standing method of judging governance actions by their long-run trajectory and their risk of failing unseen, rather than by a single snapshot, first set out in the rationale on the Cardano Constitution. *[link]*
- *The claim a for-profit makes on the shared treasury* — the published test distinguishing the maintenance of a non-rival, forkable good the ecosystem depends on from the funding of a private surplus. *[link]*
- *The DRep Treasury Rule Book* — the capital-stewardship instrument, maintained by a peer DRep, used here as the allocation check. *[link]*

DRep ID: drep1y239dn6nzlrlua9ku2d0jr4j3l6f344shcmjljtpt9mu6ps4u76rw
DRep Profile (tempo): https://tempo.vote/drep-profile?dRepId=drep1y239dn6nzlrlua9ku2d0jr4j3l6f344shcmjljtpt9mu6ps4u76rw

Stay in touch!
ReachYourPeople: https://www.ryp.io/projects/45
X: https://x.com/styg50

---

# Appendix: Published Sort and Instrument Record

*This appendix records the structured sort and instrument readings beneath the rationale above. It is published for audit and for parsing across many rationales, and it uses the framework's internal vocabulary deliberately — the accessible account of every point below is in the rationale body. Background on any term is available on the Coordination Commons site.*

## A.1 Sort

| Axis | Reading |
| :-- | :-- |
| Axis 0 — pairing pre-sort | **Does not fire.** Single self-contained action; within the existing 350M NCL at submission, not paired with a permission-expander. No size-match, no in-flight consumer, no rescue clause. **Unit of analysis = the single action.** |
| Axis 1 — wall / knob | **Knob.** Tunes a bounded spend within the existing constraint structure; installs no structural default, converts no recurring decision into a default (sunsets at term with automatic sweep), admits no senior claim-holder. The runtime workstream is new capability, but open-source/forkable — not a structural constraint. |
| Axis 2 — exit-remediability | **R3** (reversal by inaction) — the action lapses on its own terms; not renewing is the default, unspent funds sweep, and forkability keeps the exit open with no dependency-holding party created. Ordinary R0 on already-earned tranches. **No decay flag** — reversal cost does not rise over the life of the action. |
| Axis 3 — epistemic-dependency | **D1** — conditions readings within its own domain (developer tooling). Degradation registers loudly through external channels (public repos, releases, download counts, conformance tests, third-party assurance, dependent projects). Not D2/D3. |
| Lane | **Shallow.** (Routing rule, first match: knob · R2/R3 · D0/D1 → shallow lane.) Matches Appendix A archetype A — the discrete maintainer. |

## A.2 Instruments run

| Instrument | Version | Role this run |
| :-- | :-- | :-- |
| proposal-intake-and-sort | v1.1 | Pairing pre-sort (no fire) and the three sorting axes → shallow lane |
| DRep Treasury Rule Book | v17 | Fiduciary gate as a subordinate allocation check (see A.5) |
| field-fitness-audit | — | Hippocratic-floor residue; institution-via-funding fork (no fire — forkable, non-entrenching) |

**Did not fire (shallow lane).** The full six-rights battery, distal sensing, and the reflexive check are not triggered — the action is a knob, remediable by inaction, and non-self-concealing. Manufacturing a full-lane read here would be miscalibration. The shallow lane runs the procedural check, the Hippocratic floor, and the public-goods reconstruction (A.3), plus the subordinate fiduciary gate (A.5).

## A.3 Shallow-lane integrity checks

- **Procedural / constitutionality.** Passes. Within the 350M NCL at submission; prior withdrawal disclosed (second in 24 months); ada-denominated; administrator specified (SundaeSwap escrow + oversight board); separate script account, auto-abstain DRep delegation, no SPO delegation; automatic failsafe sweep. Guardrails TREASURY-02a / 03a / 04a acknowledged.
- **Hippocratic floor.** Clears. Bounded, forkable, overseen, swept — no risk of irreversible harm to the commons.
- **Public-goods reconstruction (Q1–Q2).** Q1 (good as a relation): the maintained capacity of the ecosystem to build, test, and operate complex Cardano applications on the JVM/JS stacks, kept working through the Dijkstra transition — a relation, not merely a deliverable, and one many teams depend on transitively. Q2 (rivalrous / excluded): non-rival, Apache 2.0, forkable; no one excluded. Recipient's for-profit status not asked and not bearing on the answer.
- **Private-surplus burden (published test).** **Discharged.** A for-profit maintaining a non-rival good the ecosystem depends on presents a commons-derived claim; no performance fee or private-surplus instrument is attached, and the funded growth is real productive infrastructure rather than price/valuation/attention. Per the spine's decision table (burden discharged; relation genuinely served): *evaluate on the merits like anything else.*

## A.4 Abstention-spine check and vote token

- **No abstention spine triggered** — there is no finding, no burden contest, no instrument-mismatch, and no directional hazard to route.
- **Token: YES.** A clean pass: burden discharged, sort shallow, procedural and Hippocratic checks clear, fiduciary gate concurs.

## A.5 Fiduciary gate — concurs

- **Scorecard:** Commercial / Hybrid / Infrastructure by economic substance (open-source infrastructure), with the §1.2 overlay — public asset, operability, and continuity treated as the principal treasury return; recurring maintenance of a genuine public good weights toward the public-good frame.
- **Request-size / exposure:** modest — ~₳2.46M / ~$394K at $0.16, roughly on par (USD) with the single 2025 grant and well within the NCL. ADA at ~$0.17 today, so the reference rate is slightly sub-market; hedge-to-stables on receipt committed.
- **Upfront-exposure discipline:** well-served — SundaeSwap escrow, milestone vesting, board co-sign to disburse, any-one-member pause, automatic sweep, kick-off plus delivery-conditioned tranches.
- **Commercial return structure:** no private-capture instrument (no performance fee, equity, or revenue share) — the treasury-pays-while-company-keeps-all-upside red flag is absent.
- **Opportunity cost / portfolio:** not excessive at this size for infrastructure many teams depend on; the speculative element (runtime) is bounded to ~0.5 FTE.
- **Result:** gate reaches **concur.** The gate can lower a YES, never raise a NO; here it finds nothing to lower.

## A.6 Trajectory / distal-signal log

- **Re-sort at renewal (Axis 2 decay, across cycles).** Watch for drift from the discrete-maintainer reading (archetype A, shallow) toward a standing-dependency reading — funded because too much depends on it to stop. Forkability is the load-bearing exit; re-read at each renewal whether it remains real. Second withdrawal in 24 months noted as the baseline for this track.
- **Runtime as a candidate archetype shift.** The application runtime is the workstream most likely, over cycles, to move Scalus toward an instrument layer the ecosystem's own account renders through (archetype B / D-depth increase), which would earn a deeper lane on a future proposal. Not present now.
- **Ecosystem-process signal (not this proposal).** The retrospective documents a bundled budgeting path of ~5–6 months to first payment, no process-level ADA hedge, and standing bundling governance risk — enough that capable infrastructure teams are submitting independently and on-chain to route around it. A process-level reading for the trajectory ledger, independent of this vote.
- **Sole-vendor concentration.** Single point of accountability; bounded and mitigated by the oversight board, term, and sweep. Logged, not vote-bearing.
