#!/usr/bin/env python3
"""
Build the Coordination Commons reference space.

Reads the markdown corpus in _source/ and emits plain static HTML at the
repository root. There is no runtime dependency: the emitted site is HTML +
one CSS file + one small JS file, servable by GitHub Pages as-is.

    pip install markdown
    python3 _build/build.py

Everything about the site's shape lives in the MANIFEST below.
"""

import html
import os
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_source"

# --------------------------------------------------------------------------
# Site configuration
# --------------------------------------------------------------------------

SITE = {
    "title": "The Coordination Commons",
    "tagline": "A DRep reference space",
    "author": "Styg",
    "handle": "styg50",
    "base": "https://github.com/styg-DRep/coordination-commons.git",
    "drep_id": "drep1yfaq8dsam7nusdccey2x2p684f6ulhr42pv24tslv0terqs3nq50q",  
}

FUNNELS = [
    {
        "slug": "foundations",
        "name": "Foundations",
        "kicker": "The derivation",
        "blurb": "What money is, what a blockchain makes of it, and the rights that follow. "
                 "This is the deep root: nothing elsewhere on this site is asserted that is not derived here.",
        "lede": "Four documents carry a single derivation through successive registers — from an ontology of "
                "money, through the architecture that changes what holding means, to six rights and the "
                "conditions of the consent they protect. Everything else on this site is an application of "
                "or a derivation from what is on these pages.",
    },
    {
        "slug": "seam",
        "name": "The Seam",
        "kicker": "The marked joint",
        "blurb": "The single place where description becomes prescription — stated openly so it can be "
                 "inspected and contested, rather than distributed invisibly through the argument.",
        "lede": "Every path through this work crosses one joint: the crossing from what this chain <em>is</em> "
                "to what its governance <em>owes</em>. That crossing is real. It is not a deduction, and it is "
                "not hidden. These pages hold it in one place, argue for holding it that way, and audit whether "
                "the rest of the corpus keeps its promise to mark it.",
        "seam": True,
    },
    {
        "slug": "instruments",
        "name": "Instruments",
        "kicker": "How the votes get made",
        "blurb": "The working method: how proposals are sorted, what the diagnostic reads, and when "
                 "abstention is the honest instrument rather than a dodge.",
        "lede": "Theory that never touches a ballot is not a governance practice. These are the instruments "
                "that convert the derivation into decisions — a sort that decides how much analysis an action "
                "earns, a diagnostic that reads whether the field can still sense its own damage, and the "
                "discipline that governs what each vote token is actually claiming.",
    },
    {
        "slug": "rationales",
        "name": "Rationales",
        "kicker": "The record",
        "blurb": "The votes themselves, with their full reasoning. Each one is permanently addressable "
                 "and links back to the instruments and foundations it invoked.",
        "lede": "A vote without a published reason is an assertion of authority. Each rationale here states "
                "the verdict, shows the working, and names which parts of the corpus it leaned on — so a "
                "disagreement can be taken up at the place it actually starts.",
    },
    {
        "slug": "notes",
        "name": "Notes",
        "kicker": "Working diagnostics",
        "blurb": "Shorter pieces: findings under test, evidence anchors, and diagnoses that recur across "
                 "loci. Held at candidate status until real usage settles them.",
        "lede": "Not everything here is settled, and marking which is which is part of the method. These are "
                "working notes — diagnoses that have passed a test or two but not enough of them, evidence "
                "anchors from outside the ecosystem, and analyses that map the ground the corpus stands on.",
    },
]

FUNNEL_BY_SLUG = {f["slug"]: f for f in FUNNELS}

# --------------------------------------------------------------------------
# The nodes. Order within a funnel is reading order.
# --------------------------------------------------------------------------

MANIFEST = [
    # ---------------------------------------------------------- foundations
    {
        "slug": "what-cardano-is", "funnel": "foundations", "src": "what-cardano-is.md",
        "kicker": "Stance",
        "card": "The short form of the whole position: what I hold this chain to be, what that commits "
                "me to, the three readings I do not hold, and the four things that would change my mind.",
        "seam_note": True,
    },
    {
        "slug": "money-ontology", "funnel": "foundations", "src": "money_ontology_paper.md",
        "title": "The Coordination Commons",
        "subtitle": "Toward a first-principles ontology of money and the rights of rational productive agents",
        "kicker": "Working paper · Layer 1 · The deepest root",
        "meta": {"type": "working paper", "layer": "1", "status": "draft"},
        "card": "The deepest root. Money as a symbolic coordination protocol rather than an enclosed "
                "asset — and the reification sequence that follows when the symbol is mistaken for the thing.",
        "seam_note": True,
    },
    {
        "slug": "primer", "funnel": "foundations", "src": "blockchain_money_primer.md",
        "title": "From Coordination Protocol to Constitutional Commons",
        "subtitle": "A primer on blockchain architecture, the nature of money, and why the connection generates real rights",
        "kicker": "Primer · Layer 2 · The public on-ramp", "strip_lead_h2": True,
        "meta": {"type": "primer", "layer": "2", "status": "published"},
        "card": "The lower-friction entrance. Translates the ontology into the blockchain context and "
                "explains why a holder is not an investor, a user, or a voter.",
        "edges_extra": [("derives_from", "The Coordination Commons (money ontology)", "foundations/money-ontology")],
    },
    {
        "slug": "rights", "funnel": "foundations", "src": "holder_rights_articulation.md",
        "title": "The Rights of Participants in a Constitutional Coordination Commons",
        "subtitle": "From one foundational commitment to six derived rights, each named by the specific way it can be severed",
        "kicker": "Working paper · Layer 1 · The rights derivation",
        "meta": {"type": "working paper", "layer": "1", "status": "draft"},
        "card": "Six rights, each traced from the foundational commitment to the specific abrogation path "
                "that severs it. This is the specification of what the governance-layer sensor detects.",
        "edges_extra": [
            ("derives_from", "The Coordination Commons (money ontology)", "foundations/money-ontology"),
            ("deepened_by", "The Transaction as Constitutional Moment", "foundations/transaction-as-constitutional-moment"),
            ("read_by", "Finishing Verifiable Reflexivity (the diagnostic)", "instruments/field-fitness-audit"),
        ],
        "seam_note": True,
        "ends_at_seam": True,
    },
    {
        "slug": "transaction-as-constitutional-moment", "funnel": "foundations",
        "src": "The_Transaction_as_Constitutional_Moment.md",
        "title": "The Transaction as Constitutional Moment",
        "subtitle": "The consent reconstruction of fees and monetary policy in a coordination commons",
        "kicker": "Working paper · Layer 1 · Deepens the rights derivation", "strip_lead_h2": True,
        "meta": {"type": "working paper", "layer": "1", "status": "draft"},
        "card": "Turns “here are the rights” into “here are the conditions under which the consent the "
                "commons rests on stays genuine.” The fee-consent branch of the derivation.",
        "edges_extra": [("derives_from", "The Rights of Participants", "foundations/rights")],
    },
    {
        "slug": "sieve-and-frontier", "funnel": "foundations", "src": "The_Sieve_and_the_Frontier.md",
        "kicker": "Working paper · Layer 2 · Integration",
        "card": "Why the Coordination Commons cannot fully integrate with the UDHR, and what it adds at "
                "the rights frontier. Also where the walls-and-knobs distinction is instantiated.",
    },
    {
        "slug": "place-severance", "funnel": "foundations", "src": "Place_Severance_Derivation_Note.md",
        "kicker": "Derivation note · Layer 2 · Anchor",
        "card": "A finding that belongs beneath the foundational right rather than beside the six: the "
                "place axis of identity. A derivation note, not a seventh right.",
    },
    # ----------------------------------------------------------------- seam
    {
        "slug": "the-half-we-havent-built-yet", "funnel": "seam", "src": "the-half-we-havent-built-yet.md",
        "kicker": "Invitation · The shortest way in",
        "meta": {"type": "invitation", "status": "draft for vetting"},
        "card": "Start here if you are new. Cardano shipped a transaction that proves its own correctness "
                "with no one you have to trust. There is a second half to that achievement, one layer up, "
                "still unbuilt.",
    },
    {
        "slug": "verification-gap", "funnel": "seam", "src": "the_verification_gap.md",
        "kicker": "Primer · Layer 2 · The builder-native door",
        "card": "Consensus proves procedure, and at the consensus layer procedure <em>is</em> legitimacy. "
                "One layer up it is not — so the same proof verifies the wrong invariant. A verifiably "
                "valid vote can be an illegitimate one.",
        "edges_extra": [("hands_normative_content_to", "The Rights of Participants", "foundations/rights")],
    },
    {
        "slug": "what-the-second-sensor-reads", "funnel": "seam", "src": "what-the-second-sensor-reads.md",
        "kicker": "Invitation · Continues the first",
        "meta": {"type": "invitation", "status": "draft for vetting"},
        "card": "The instrument was named and left empty on purpose. This is what fills it — and why the "
                "conditions are discovered rather than decreed.",
    },
    {
        "slug": "legibility", "funnel": "seam", "src": "The_Legibility_of_the_Seam.md",
        "kicker": "Methodological note · Layer 1 · Governs the corpus",
        "card": "The third stance, between uninterrogable certainty and uninterrogable uncertainty. The "
                "epistemic commitment that obliges every document here to carry the question alongside "
                "the conclusion.",
    },
    {
        "slug": "audit", "funnel": "seam", "src": "Seam_Legibility_Audit_and_Coherence_Plan.md",
        "kicker": "Audit · Layer 2 · The corpus checked against its own standard",
        "card": "Does every statement of the foundation actually mark the crossing? Findings, diffs, and a "
                "coherence plan — marked VERIFIED or CANDIDATE, because claiming coverage not performed "
                "would be the exact failure under audit.",
    },
    # ---------------------------------------------------------- instruments
    {
        "slug": "field-fitness-audit", "funnel": "instruments", "src": "field-fitness-audit.md",
        "kicker": "Instrument · Layer 3 · The diagnostic",
        "card": "The four failures, run in order, with the six rights as the integrity sensor. Framed as "
                "fitness gaps rather than accusations, designed to be run jointly and re-run over time.",
        "edges_extra": [
            ("derives_from", "The Rights of Participants", "foundations/rights"),
            ("continues_from", "The Verification Gap", "seam/verification-gap"),
        ],
        "seam_note": True,
    },
    {
        "slug": "intake-and-sort", "funnel": "instruments", "src": "proposal-intake-and-sort.md",
        "kicker": "Instrument · Layer 3 · The ingestion layer",
        "card": "Three axes decide how much analysis a governance action earns: wall-versus-knob, "
                "exit-remediability, and epistemic-dependency depth. On-chain action type is not one of them.",
    },
    {
        "slug": "abstention-spines", "funnel": "instruments", "src": "abstention-spines.md",
        "kicker": "Instrument · Layer 3 · The vote-token layer",
        "card": "For a registered DRep, silence and NO are indistinguishable. Explicit abstention is the "
                "only genuinely neutral act — and five spines govern when it is the honest one.",
    },
    {
        "slug": "sensor-coverage-map", "funnel": "instruments", "src": "Failure_3_Worked__Sensor_Coverage_Map.md",
        "kicker": "Worked example · Companion to the diagnostic",
        "card": "Failure 3 run against the real Cardano governance layer: which of the six rights have a "
                "sensor that registers pressure before the damage is structural, and which are unlit.",
    },
    # ----------------------------------------------------------- rationales
    {
        "slug": "constitution-v1", "funnel": "rationales",
        "src": "gov_action133jnaewfsq8x6v08ndd87l2yqryp63r30t2dkceacxx5cply5n7sqzlcyqf - Cardano Consitution Voting Rationale.md",
        "title": "Cardano Constitution to Replace the Interim Constitution",
        "subtitle": "Establishing the evaluative framework: a Hippocratic floor, four mid-range criteria, and a commitment to judge trajectories rather than snapshots",
        "kicker": "Voting rationale · Update to Constitution",
        "strip_contents": True, "strip_meta_table": True, "demote": True,
        "vote": {
            "verdict": "YES",
            "gaid": "gov_action133jnaewfsq8x6v08ndd87l2yqryp63r30t2dkceacxx5cply5n7sqzlcyqf",
            "ga_type": "Update to Constitution",
            "submitted": "30 January 2025 (Epoch 537)",
            "expires": "5 March 2025 (Epoch 544)",
        },
        "card": "The rationale that set the framework everything since has been measured against — "
                "including the commitment to evaluate over time that obliged the v2.4 review below.",
        "edges_extra": [("establishes", "the Hippocratic floor and the four mid-range criteria", None)],
    },
    {
        "slug": "treasury-tax-tau", "funnel": "rationales",
        "src": "Gov_action1js2s9v92zpxg2rge0y3jt9zy626he2m67x9kx9phw4r942kvsn6sqfym0d7 - Protocol Parameter Change.md",
        "title": "Decrease Treasury Tax from 20% to 10%",
        "subtitle": "On the history of tau, the evidentiary standard a parameter model has to meet, and why the maximum possible change is the wrong first move",
        "kicker": "Voting rationale · Protocol Parameter Change",
        "strip_contents": True, "strip_meta_table": True, "demote": True,
        "vote": {
            "verdict": "NO",
            "gaid": "gov_action1js2s9v92zpxg2rge0y3jt9zy626he2m67x9kx9phw4r942kvsn6sqfym0d7",
            "ga_type": "Protocol Parameter Change (economic)",
            "submitted": "13 February 2025 (Epoch 539)",
            "expires": "15 March 2025 (Epoch 546)",
        },
        "card": "A parameter vote that is really a modelling-standards argument: what evidence a change of "
                "this size owes, and why continuous iterative change beats a pendulum swing.",
    },
    {
        "slug": "constitution-v2-4", "funnel": "rationales", "src": "v2.4_Amendment_Voting_Rationale.md",
        "title": "Cardano Constitution v2.4",
        "subtitle": "Entered after the fact: a procedural objection, a Hippocratic-floor failure, and three coordinated moves that re-ground the constitution on ownership",
        "kicker": "Voting rationale · Update to Constitution · Retrospective",
        "strip_meta_table": True, "demote": True,
        "vote": {
            "verdict": "NO",
            "gaid": "gov_action1jxne7hynfd7frcczwumd2eggps4kvy0msjztz9t0mutpy870ksgqqp6vp3p",
            "ga_type": "Update to Constitution",
            "submitted": "Epoch 601 (Dec 15, 2025)",
            "expires": "Epoch 608 (Jan 19, 2026)",
        },
        "card": "Recorded late and on purpose. The vote that revealed YES/NO as the wrong instrument for "
                "the constitutional problem that mattered most — and the ontological drift that prompted "
                "the corpus beneath this site.",
        "edges_extra": [
            ("obliged_by", "the trajectory commitment made in the v1.0 rationale", "rationales/constitution-v1"),
            ("diagnoses", "the reification sequence named in the money ontology", "foundations/money-ontology"),
        ],
        "seam_note": True,
    },
    # ---------------------------------------------------------------- notes
    {
        "slug": "tenets-to-rights", "funnel": "notes", "src": "From_Tenets_to_Rights__A_Trajectory_Map.md",
        "kicker": "Analysis · Orientation",
        "card": "A trajectory map of Articles I and II across constitutional versions — the lay of the "
                "land for anyone joining the argument midway.",
    },
    {
        "slug": "the-good-is-not-its-measure", "funnel": "notes", "src": "The_Good_Is_Not_Its_Measure.md",
        "kicker": "Method · Layer 2 · Candidate",
        "card": "Quantity substitution as a scale-free move: one diagnosis that holds across loci, and a "
                "correction that does not.",
    },
    {
        "slug": "the-good-that-is-not-a-quantity", "funnel": "notes", "src": "The_Good_That_Is_Not_a_Quantity.md",
        "kicker": "Method · Layer 3 · Candidate · Institution locus",
        "card": "When a proposal relocates a public good from a relation to a quantity — and why the "
                "relocation, not the return, is the question.",
    },
    {
        "slug": "the-freedom-that-is-not-a-balance", "funnel": "notes", "src": "The_Freedom_That_Is_Not_a_Balance.md",
        "kicker": "Method · Layer 3 · Candidate · Agent locus",
        "card": "The same engine re-indexed from the institution to the individual holder: freedom "
                "conflated with wealth, and the exit that discloses which one you were holding.",
    },
    {
        "slug": "anti-impermanence-root", "funnel": "notes", "src": "The_Anti-Impermanence_Root.md",
        "kicker": "Note · Layer 1 · Candidate",
        "card": "Reification, causal time, and the affective substrate of control — the root beneath the "
                "reification error in the money ontology.",
    },
    {
        "slug": "reciprocity-is-equality-contingent", "funnel": "notes", "src": "reciprocity_is_equality_contingent.md",
        "kicker": "Evidence note · Layer 1",
        "card": "An external empirical anchor: expectations of reciprocal generosity are specific to equal "
                "relationships — a candidate distal sensor for relational capture.",
    },
    {
        "slug": "concept-graph-schema", "funnel": "notes", "src": "concept_graph_schema.md",
        "title": "Concept Graph Schema",
        "subtitle": "The frontmatter schema and typed-edge vocabulary the corpus is authored against",
        "kicker": "Infrastructure · Working draft",
        "card": "How the corpus is wired: node types, the nine edge relations, and the deliberate gap "
                "where the most important edge on the site is left untyped.",
    },
]

MANIFEST_BY_SLUG = {}
for n in MANIFEST:
    n["path"] = f"{n['funnel']}/{n['slug']}"
    MANIFEST_BY_SLUG[n["path"]] = n

# Aliases for resolving frontmatter `edges:` targets to real pages.
ALIASES = {
    "money_ontology_paper": "foundations/money-ontology",
    "the coordination commons": "foundations/money-ontology",
    "blockchain_money_primer": "foundations/primer",
    "from coordination protocol to constitutional commons": "foundations/primer",
    "holder_rights_articulation": "foundations/rights",
    "the rights of participants": "foundations/rights",
    "the rights of participants in a constitutional coordination commons": "foundations/rights",
    "the_transaction_as_constitutional_moment": "foundations/transaction-as-constitutional-moment",
    "the transaction as constitutional moment": "foundations/transaction-as-constitutional-moment",
    "the_sieve_and_the_frontier": "foundations/sieve-and-frontier",
    "the sieve and the frontier": "foundations/sieve-and-frontier",
    "place_severance_derivation_note": "foundations/place-severance",
    "place-severance": "foundations/place-severance",
    "what-cardano-is": "foundations/what-cardano-is",
    "what cardano is": "foundations/what-cardano-is",
    "the_verification_gap": "seam/verification-gap",
    "the verification gap": "seam/verification-gap",
    "the_legibility_of_the_seam": "seam/legibility",
    "the legibility of the seam": "seam/legibility",
    "seam_legibility_audit_and_coherence_plan": "seam/audit",
    "the-half-we-havent-built-yet": "seam/the-half-we-havent-built-yet",
    "what-the-second-sensor-reads": "seam/what-the-second-sensor-reads",
    "field-fitness-audit": "instruments/field-fitness-audit",
    "finishing verifiable reflexivity": "instruments/field-fitness-audit",
    "proposal-intake-and-sort": "instruments/intake-and-sort",
    "proposal intake and sort": "instruments/intake-and-sort",
    "abstention-spines": "instruments/abstention-spines",
    "abstention spines": "instruments/abstention-spines",
    "failure_3_worked__sensor_coverage_map": "instruments/sensor-coverage-map",
    "from_tenets_to_rights__a_trajectory_map": "notes/tenets-to-rights",
    "the_good_is_not_its_measure": "notes/the-good-is-not-its-measure",
    "the good is not its measure": "notes/the-good-is-not-its-measure",
    "the_good_that_is_not_a_quantity": "notes/the-good-that-is-not-a-quantity",
    "the good that is not a quantity": "notes/the-good-that-is-not-a-quantity",
    "the_freedom_that_is_not_a_balance": "notes/the-freedom-that-is-not-a-balance",
    "the freedom that is not a balance": "notes/the-freedom-that-is-not-a-balance",
    "the_anti-impermanence_root": "notes/anti-impermanence-root",
    "reciprocity_is_equality_contingent": "notes/reciprocity-is-equality-contingent",
    "concept_graph_schema": "notes/concept-graph-schema",
}

SEAM_NOTE_HTML = (
    '<aside class="seam-note">\n'
    '  <h3>The seam</h3>\n'
    '  <p>This page inherits a crossing. Somewhere upstream the argument moves from <em>what this chain '
    'is</em> to <em>what its governance owes</em>, and that move is not a deduction. It is held in exactly '
    'one place, marked, so it can be inspected and attacked rather than distributed invisibly through the '
    'reasoning. If you want to disagree with the conclusions here at their root, '
    '<a href="{seam}">the joint is over here</a>.</p>\n'
    '</aside>\n'
)

# --------------------------------------------------------------------------
# Markdown handling
# --------------------------------------------------------------------------

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def split_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    body = text[m.end():]
    fm, key, buf = {}, None, []
    for line in raw.split("\n"):
        if re.match(r"^\s*#", line) or not line.strip():
            continue
        m2 = re.match(r"^(\w[\w\-]*):\s*(.*)$", line)
        if m2:
            if key:
                fm[key] = buf if len(buf) > 1 or (key == "edges") else (buf[0] if buf else fm.get(key, ""))
            key, val, buf = m2.group(1), m2.group(2).strip(), []
            if val and val not in (">", "|", ">-", "|-"):
                fm[key] = val.strip("\"'")
                key = None
            else:
                fm[key] = ""
        elif key:
            item = line.strip()
            if item.startswith("- "):
                buf.append(item[2:].strip())
            elif item:
                buf.append(item)
    if key and buf:
        fm[key] = buf
    return fm, body


def clean_markdown(text, node=None):
    node = node or {}
    # Google-Docs export debris
    text = re.sub(r"!\[[^\]]*\]\[[^\]]*\]", "", text)          # undefined image refs
    text = re.sub(r"^\s*\[image\d+\]:.*\n?", "", text, flags=re.M)
    text = text.replace("\u00a0", " ")

    # The document's own H1 repeats the page title we already print.
    text = re.sub(r"\A\s*#\s+.+?\n", "", text, count=1)
    if node.get("strip_lead_h2"):
        text = re.sub(r"\A\s*##\s+.+?\n", "", text, count=1)
    # ...and the rule that usually follows it
    text = re.sub(r"\A\s*(?:-{3,}|\*{3,})\s*\n", "", text, count=1)

    if node.get("strip_contents"):
        # The exported "# Contents" list duplicates the sidebar we generate.
        text = re.sub(r"^#\s*Contents\s*$.*?(?=^#\s)", "", text, flags=re.M | re.S)

    if node.get("strip_meta_table"):
        # The exported header table duplicates the "The vote" panel.
        text = re.sub(r"^\|.*\n(?:^\|.*\n)*", "", text, count=1, flags=re.M)

    if node.get("demote"):
        # Documents that use H1 for their own sections sit one level below
        # the page title.
        text = re.sub(r"^(#{1,4})(\s+\S)", r"#\1\2", text, flags=re.M)

    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def slugify(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).lower()
    s = re.sub(r"[^\w\s\-]", "", s, flags=re.U)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s or "section"


def render_markdown(text):
    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "smarty"],
        extension_configs={"smarty": {"smart_dashes": True, "smart_quotes": True}},
    )
    return md.convert(text)


HEAD_RE = re.compile(r"<h([23])(?P<attrs>[^>]*)>(?P<inner>.*?)</h\1>", re.S)


def anchor_headings(body_html):
    """Give every h2/h3 a stable id, an anchor link, and collect a TOC."""
    toc, seen = [], {}

    def repl(m):
        lvl, attrs, inner = m.group(1), m.group("attrs"), m.group("inner")
        idm = re.search(r'id=["\']([^"\']+)["\']', attrs)
        if idm:
            hid = idm.group(1)
            attrs = attrs.replace(idm.group(0), "").strip()
        else:
            hid = slugify(inner)
        base = hid
        n = seen.get(base, 0)
        seen[base] = n + 1
        if n:
            hid = f"{base}-{n+1}"
        label = re.sub(r"<[^>]+>", "", inner).strip()
        toc.append((int(lvl), hid, label))
        sp = (" " + attrs.strip()) if attrs.strip() else ""
        anchor = f'<a class="anchor" href="#{hid}" aria-label="Link to this section">§</a>'
        return f'<h{lvl} id="{hid}"{sp}>{inner}{anchor}</h{lvl}>'

    return HEAD_RE.sub(repl, body_html), toc


# --------------------------------------------------------------------------
# HTML chrome
# --------------------------------------------------------------------------

def esc(s):
    return html.escape(str(s), quote=True)


def rel(depth):
    return "../" * depth if depth else "./"


def masthead(depth, current=None):
    r = rel(depth)
    items = []
    for f in FUNNELS:
        cls = ' class="is-seam"' if f.get("seam") else ""
        cur = ' aria-current="page"' if current == f["slug"] else ""
        items.append(f'<a href="{r}{f["slug"]}/"{cls}{cur}>{esc(f["name"])}</a>')
    ac = ' aria-current="page"'
    items.append(f'<a href="{r}index-of-work/"{ac if current == "index" else ""}>All work</a>')
    items.append(f'<a href="{r}about/"{ac if current == "about" else ""}>About</a>')
    return (
        '<header class="masthead">\n  <div class="shell">\n'
        f'    <a class="wordmark" href="{r}">The Coordination Commons <span>· a DRep reference</span></a>\n'
        f'    <nav aria-label="Primary">{"".join(items)}</nav>\n'
        "  </div>\n</header>\n"
    )


def footer(depth):
    r = rel(depth)
    fl = "".join(f'<li><a href="{r}{f["slug"]}/">{esc(f["name"])}</a></li>' for f in FUNNELS)
    return f"""<footer class="site-foot">
  <div class="shell">
    <div class="cols">
      <div>
        <h4>The space</h4>
        <p>The public reference behind the voting rationales of <strong>{esc(SITE['author'])}</strong>,
        a Cardano DRep. Everything asserted in a vote of mine is derived somewhere on these pages, and
        every page is permanently addressable so a disagreement can start where it actually starts.</p>
      </div>
      <div><h4>Funnels</h4><ul>{fl}</ul></div>
      <div><h4>Elsewhere</h4><ul>
        <li><a href="{r}index-of-work/">Index of all work</a></li>
        <li><a href="{r}about/">About &amp; how to cite</a></li>
        <li><a href="https://x.com/{esc(SITE['handle'])}" rel="me noopener">@{esc(SITE['handle'])}</a></li>
        <li><a href="https://gov.tools" rel="noopener">GovTool</a></li>
      </ul></div>
    </div>
    <p class="fine">These pages re-version. Where a page and the corpus beneath it disagree, the corpus
    governs and the page is out of date. Rights here are argued to be discovered rather than decreed —
    which means the argument is open to being shown wrong, and the four falsification conditions are
    published on <a href="{r}foundations/what-cardano-is/#9-what-would-change-my-mind">the stance page</a>.</p>
  </div>
</footer>
"""


def shell(*, title, description, body, depth, current=None, canonical=""):
    r = rel(depth)
    full_title = title if title == SITE["title"] else f"{title} · {SITE['title']}"
    can = f'\n<link rel="canonical" href="{esc(SITE["base"].rstrip("/"))}/{canonical}">' if canonical is not None else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="author" content="{esc(SITE['author'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{esc(SITE['title'])}">{can}
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{masthead(depth, current)}
<main id="main">
{body}
</main>
{footer(depth)}
<script src="{r}assets/site.js" defer></script>
</body>
</html>
"""


def cite_block(node_title, url, depth, extra=""):
    return f"""<section class="cite panel" id="cite">
  <h3>Cite this page</h3>
  <p>This URL is stable. Link it directly from a voting rationale, a forum post, or a proposal comment.</p>
  <p class="perma"><span>{esc(url)}</span>
     <button class="copy" type="button" data-copy="{esc(url)}">Copy link</button></p>
  <p style="margin-bottom:0"><small>{esc(SITE['author'])}, “{esc(node_title)},” <em>{esc(SITE['title'])}</em>. {extra}</small></p>
</section>
"""


def lineage_block(edges):
    if not edges:
        return ""
    rows = []
    for relname, label, target in edges:
        lab = label if target is None else f'<a href="{target}">{label}</a>'
        rows.append(f'<li><span class="rel">{esc(relname)}</span><span>{lab}</span></li>')
    return (
        '<section class="panel" id="lineage">\n  <h3>Derivation lineage</h3>\n'
        f'  <ul class="lineage">{"".join(rows)}</ul>\n</section>\n'
    )


# --------------------------------------------------------------------------
# Edge parsing
# --------------------------------------------------------------------------

EDGE_RE = re.compile(r"^\s*(\w+)\s*(?:→|->|:)\s*(.+?)\s*$")


def parse_edges(fm, depth, own_path):
    out = []
    raw = fm.get("edges") or []
    if isinstance(raw, str):
        raw = [raw]
    for item in raw:
        item = re.sub(r"\s*#.*$", "", str(item)).strip()
        m = EDGE_RE.match(item)
        if not m:
            continue
        relname, label = m.group(1), m.group(2).strip()
        key = re.sub(r"\s*\(.*?\)\s*$", "", label).strip()
        key = re.sub(r"\.md$", "", key).strip().lower()
        key = re.sub(r"\s*§.*$", "", key).strip()
        target = ALIASES.get(key)
        if target and target != own_path:
            target = rel(depth) + target + "/"
        else:
            target = None
        out.append((relname, esc(label), target))
    return out


# --------------------------------------------------------------------------
# Page builders
# --------------------------------------------------------------------------

def write(path_parts, content):
    out = ROOT.joinpath(*path_parts)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    return out


def build_node(node, prev_node, next_node):
    depth = 2
    r = rel(depth)
    src_text = (SRC / node["src"]).read_text(encoding="utf-8")
    fm, body_md = split_frontmatter(src_text)
    body_md = clean_markdown(body_md, node)

    title = node.get("title") or fm.get("title") or node["slug"].replace("-", " ").title()
    subtitle = node.get("subtitle") or fm.get("subtitle") or ""
    if isinstance(subtitle, list):
        subtitle = " ".join(subtitle)

    body_html = render_markdown(body_md)
    body_html, toc = anchor_headings(body_html)

    funnel = FUNNEL_BY_SLUG[node["funnel"]]

    # ---- meta strip
    meta = dict(node.get("meta") or {})
    for k in ("type", "layer", "status"):
        if k not in meta and fm.get(k):
            v = fm[k]
            meta[k] = v if isinstance(v, str) else ", ".join(v)
    meta_items = "".join(f"<li><b>{esc(k)}</b> {esc(v)}</li>" for k, v in meta.items() if v)

    vote = node.get("vote")
    if vote:
        meta_items = (
            f'<li><b>vote</b> {esc(vote["verdict"])}</li>'
            f'<li><b>action</b> {esc(vote["ga_type"])}</li>'
            f'<li><b>submitted</b> {esc(vote["submitted"])}</li>'
        )
    meta_html = f'<ul class="metastrip">{meta_items}</ul>' if meta_items else ""

    # ---- rail
    toc_items = []
    for lvl, hid, label in toc:
        cls = ' class="lvl3"' if lvl == 3 else ""
        toc_items.append(f'<li{cls}><a href="#{hid}">{esc(label)}</a></li>')
    rail = ""
    if len(toc_items) > 2:
        rail = (
            '<aside class="rail">\n  <h2>On this page</h2>\n'
            f'  <nav aria-label="On this page"><ol>{"".join(toc_items)}</ol></nav>\n'
            f'  <h2>In {esc(funnel["name"])}</h2>\n'
            f'  <nav><ol><li><a href="{r}{funnel["slug"]}/">← All {esc(funnel["name"].lower())}</a></li></ol></nav>\n'
            "</aside>\n"
        )
    else:
        rail = f'<aside class="rail"><h2>In {esc(funnel["name"])}</h2><nav><ol><li><a href="{r}{funnel["slug"]}/">← All {esc(funnel["name"].lower())}</a></li></ol></nav></aside>\n'

    # ---- lineage
    edges = parse_edges(fm, depth, node["path"])
    for relname, label, target in node.get("edges_extra", []):
        t = (rel(depth) + target + "/") if target else None
        edges.append((relname, esc(label), t))
    lineage = lineage_block(edges)

    # ---- seam note
    seam_html = ""
    if node.get("seam_note"):
        seam_html = SEAM_NOTE_HTML.format(seam=f"{r}seam/legibility/")

    # ---- vote panel
    vote_html = ""
    if vote:
        vc = {"YES": "v-yes", "NO": "v-no", "ABSTAIN": "v-abstain"}.get(vote["verdict"], "v-abstain")
        vote_html = f"""<section class="panel" id="the-vote">
  <h3>The vote</h3>
  <p><span class="verdict {vc}">{esc(vote['verdict'])}</span> on this governance action.</p>
  <ul class="lineage">
    <li><span class="rel">GAID</span><span style="font-family:var(--mono);font-size:.82rem;word-break:break-all">{esc(vote['gaid'])}</span></li>
    <li><span class="rel">Action type</span><span>{esc(vote['ga_type'])}</span></li>
    <li><span class="rel">Submitted</span><span>{esc(vote['submitted'])}</span></li>
    <li><span class="rel">Expires</span><span>{esc(vote['expires'])}</span></li>
  </ul>
</section>
"""

    # ---- ends-at-seam push
    tail = ""
    if node.get("ends_at_seam"):
        tail = (
            '<aside class="seam-note">\n  <h3>Where this ends</h3>\n'
            '  <p>These six are not a philosophy wing. They are the specification of what a '
            'governance-layer sensor would have to read — and nothing has yet been built to read them. '
            f'That gap is the subject of <a href="{r}instruments/field-fitness-audit/">the diagnostic</a>, '
            f'and the reason it exists is set out in <a href="{r}seam/verification-gap/">The Verification Gap</a>.</p>\n'
            "</aside>\n"
        )

    url = f"{SITE['base'].rstrip('/')}/{node['path']}/"
    cite_extra = f"GAID {esc(vote['gaid'])}." if vote else ""
    cite = cite_block(title, url, depth, cite_extra)

    # ---- prev / next
    nav_parts = []
    if prev_node:
        nav_parts.append(
            f'<a class="prev" href="{r}{prev_node["path"]}/"><span class="lbl">Previous in {esc(funnel["name"])}</span>'
            f'<span class="ttl">{esc(prev_node.get("title") or prev_node["slug"].replace("-", " ").title())}</span></a>'
        )
    if next_node:
        nav_parts.append(
            f'<a class="next" href="{r}{next_node["path"]}/"><span class="lbl">Next in {esc(funnel["name"])}</span>'
            f'<span class="ttl">{esc(next_node.get("title") or next_node["slug"].replace("-", " ").title())}</span></a>'
        )
    updown = ""
    if nav_parts:
        cls = "updown pair" if len(nav_parts) == 2 else "updown"
        updown = f'<div class="{cls}">{"".join(nav_parts)}</div>'

    crumb = (
        f'<p class="eyebrow"><a href="{r}">Space</a><span class="sep">›</span>'
        f'<a href="{r}{funnel["slug"]}/">{esc(funnel["name"])}</a>'
        + (f'<span class="sep">›</span>{esc(node.get("kicker", ""))}' if node.get("kicker") else "")
        + "</p>"
    )

    body = f"""<div class="shell">
  <div class="page-head">
    <div class="headwrap">
      {crumb}
      <h1>{esc(title)}</h1>
      {f'<p class="standfirst">{esc(subtitle)}</p>' if subtitle else ''}
      {meta_html}
    </div>
  </div>
  <div class="doc">
    {rail}
    <article class="body">
      {vote_html}
      {seam_html}
      {body_html}
      {tail}
      {lineage}
      {cite}
      {updown}
    </article>
  </div>
</div>
"""
    desc = re.sub(r"<[^>]+>", "", node.get("card", subtitle or title))[:180]
    write([node["funnel"], node["slug"], "index.html"],
          shell(title=title, description=desc, body=body, depth=depth,
                current=node["funnel"], canonical=f"{node['path']}/"))
    return {"title": title, "subtitle": subtitle, "desc": desc}


def build_funnel(funnel, nodes):
    depth = 1
    r = rel(depth)
    if funnel["slug"] == "rationales":
        rows = []
        for n in nodes:
            v = n["vote"]
            vc = {"YES": "v-yes", "NO": "v-no", "ABSTAIN": "v-abstain"}.get(v["verdict"], "v-abstain")
            rows.append(f"""<a class="ledger-row" href="{r}{n['path']}/">
  <span class="verdict {vc}">{esc(v['verdict'])}</span><h3>{esc(n['title'])}</h3>
  <span class="when">{esc(v['ga_type'])} · submitted {esc(v['submitted'])}</span>
  <span class="gaid">{esc(v['gaid'])}</span>
</a>""")
        listing = f'<div class="ledger">{"".join(rows)}</div>'
    else:
        cards = []
        for n in nodes:
            t = n.get("title") or n["slug"].replace("-", " ").title()
            cls = "card is-seam" if funnel.get("seam") else "card"
            cards.append(f"""<a class="{cls}" href="{r}{n['path']}/">
  <span class="kicker">{esc(n.get('kicker',''))}</span>
  <h3>{esc(t)}</h3>
  <p>{n.get('card','')}</p>
</a>""")
        listing = f'<div class="cards">{"".join(cards)}</div>'

    body = f"""<div class="shell">
  <div class="page-head">
    <div class="headwrap">
      <p class="eyebrow"><a href="{r}">Space</a><span class="sep">›</span>{esc(funnel['kicker'])}</p>
      <h1>{esc(funnel['name'])}</h1>
      <p class="standfirst">{funnel['lede']}</p>
    </div>
  </div>
  {listing}
  <p style="max-width:var(--measure);color:var(--muted);font-size:.94rem">
    Every page in this funnel is permanently addressable and carries its own citation block, so a
    rationale can point at the exact argument it relies on rather than at the site in general.
    <a href="{r}index-of-work/">See the full index of work →</a>
  </p>
</div>
"""
    write([funnel["slug"], "index.html"],
          shell(title=funnel["name"], description=funnel["blurb"], body=body,
                depth=depth, current=funnel["slug"], canonical=f"{funnel['slug']}/"))


def converge_svg():
    """The five funnels drawn so the seam sits beneath and between them."""
    cols = [
        ("Foundations", "foundations/", 90),
        ("Instruments", "instruments/", 300),
        ("Rationales", "rationales/", 510),
        ("Notes", "notes/", 720),
    ]
    lines, labels = [], []
    for name, href, x in cols:
        lines.append(f'<path class="cx-line to-seam" d="M {x} 46 C {x} 110, 405 110, 405 148"/>')
        labels.append(
            f'<a href="{href}"><rect class="cx-node" x="{x-78}" y="14" width="156" height="32" rx="16"/>'
            f'<text class="cx-label" x="{x}" y="35" text-anchor="middle">{name}</text></a>'
        )
    return f"""<div class="converge" aria-hidden="false">
<svg viewBox="0 0 810 205" role="img" aria-label="Diagram: the four funnels all converge on the seam">
  {''.join(lines)}
  {''.join(labels)}
  <a href="seam/">
    <rect class="cx-node" x="309" y="148" width="192" height="38" rx="19" style="stroke:var(--seam);stroke-width:1.5"/>
    <text class="cx-seam" x="405" y="172" text-anchor="middle">THE SEAM</text>
  </a>
</svg>
</div>"""


def build_index():
    depth = 0
    doors = []
    for i, f in enumerate(FUNNELS, 1):
        cls = "door is-seam wide" if f.get("seam") else "door"
        doors.append(f"""<a class="{cls}" href="{f['slug']}/">
  <span class="num">{i:02d}</span>
  <h3>{esc(f['name'])}</h3>
  <p>{f['blurb']}</p>
  <span class="enters">{esc(f['kicker'])}</span>
</a>""")
    body = f"""<div class="shell">
  <section class="hero">
    <h1>The Coordination Commons</h1>
    <p class="lede">The public reference behind my votes as a Cardano DRep. Everything I assert in a
    rationale is derived somewhere on these pages, so if you disagree with a vote of mine, you can go
    to the place the disagreement actually starts, and argue with that instead.</p>
    <p class="sig">{esc(SITE['author'])} · <a href="https://x.com/{esc(SITE['handle'])}" rel="me noopener">@{esc(SITE['handle'])}</a>{f" · DRep <code>{esc(SITE['drep_id'])}</code>" if SITE['drep_id'] else ""}</p>
  </section>

  <section class="claim">
    <p>Cardano is an open-source, peer-to-peer, decentralized blockchain built to enable
    self-determination through participatory constitution of a coordination commons.</p>
    <p class="attrib">The claim everything here unpacks, stated in full, with what would falsify it, on
    <a href="foundations/what-cardano-is/">What Cardano Is</a>.</p>
  </section>

  <div class="narrow" style="margin-inline:0">
    <h2 style="margin-top:0">Why this site exists</h2>
    <p>A vote is a compression. On-chain, a rationale gets a few thousand characters to carry reasoning
    that took months to build, and the parts that do the real work (what money is for, what a holder
    actually is, which rights follow and how) get squeezed into assertions that read like preferences.</p>
    <p>So the reasoning lives here instead, at full length, at stable addresses. A rationale can then do
    the thing a rationale should do: state a verdict, show the working specific to <em>this</em> action,
    and link out to the derivation rather than smuggling it in.</p>
    <p>Two commitments govern everything below. First, the rights argued for here are treated as
    <em>discovered</em> rather than decreed, which means the whole structure is exposed to being shown
    wrong, and the conditions that would show it are published rather than implied. Second, the single
    place where this argument crosses from description to prescription is marked and held in one page,
    not distributed invisibly through the rest.</p>
  </div>

  <h2>Five ways in</h2>
  <p style="max-width:var(--measure);color:var(--muted)">Enter by the kind of attention you brought.
  Whichever you take, the path runs through the same crossing.</p>
  <div class="doors">
    {''.join(doors)}
  </div>

  {converge_svg()}

  <div class="narrow" style="margin-inline:0;margin-bottom:4rem">
    <h2>If you are here from a rationale</h2>
    <p>The link that brought you here points at a specific argument, not at this page. Its citation
    block carries the permanent URL, and its lineage panel shows what it derives from and what derives
    from it. To see the shape of the whole thing at once, use
    <a href="index-of-work/">the index of all work</a>; to see how it is meant to be cited and how it
    re-versions, see <a href="about/">About</a>.</p>
  </div>
</div>
"""
    write(["index.html"], shell(
        title=SITE["title"],
        description="The public reference corpus behind the Cardano DRep votes of Styg — "
                    "money ontology, rights derivation, the marked seam, and the voting instruments.",
        body=body, depth=depth, canonical=""))


def build_index_of_work(rendered):
    depth = 1
    r = rel(depth)
    groups = []
    for f in FUNNELS:
        items = []
        for n in MANIFEST:
            if n["funnel"] != f["slug"]:
                continue
            info = rendered[n["path"]]
            items.append(
                f'<li><a href="{r}{n["path"]}/"><span class="k">{esc(f["name"])}</span>'
                f'<span class="t">{esc(info["title"])}</span>'
                f'<span class="d">{n.get("card","")}</span></a></li>'
            )
        groups.append(
            f'<section class="index-group"><h2>{esc(f["name"])}</h2>'
            f'<ul class="index-list">{"".join(items)}</ul></section>'
        )
    body = f"""<div class="shell">
  <div class="page-head"><div class="headwrap">
    <p class="eyebrow"><a href="{r}">Space</a><span class="sep">›</span>Index</p>
    <h1>Index of all work</h1>
    <p class="standfirst">Every published page, in reading order within its funnel. {len(MANIFEST)} documents.</p>
  </div></div>
  {''.join(groups)}
</div>
"""
    write(["index-of-work", "index.html"], shell(
        title="Index of all work", description="Every published page in the corpus, by funnel.",
        body=body, depth=depth, current="index", canonical="index-of-work/"))


def build_about():
    depth = 1
    r = rel(depth)
    body = f"""<div class="shell">
  <div class="page-head"><div class="headwrap">
    <p class="eyebrow"><a href="{r}">Space</a><span class="sep">›</span>About</p>
    <h1>About this space</h1>
    <p class="standfirst">What it is for, who wrote it, how to cite it, and the terms on which it
    expects to be wrong.</p>
  </div></div>
  <div class="doc">
    <aside class="rail">
      <h2>On this page</h2>
      <nav><ol>
        <li><a href="#what-this-is">What this is</a></li>
        <li><a href="#how-to-cite">How to cite</a></li>
        <li><a href="#versioning">Versioning</a></li>
        <li><a href="#the-seam">The seam</a></li>
        <li><a href="#disagreeing">Disagreeing well</a></li>
        <li><a href="#colophon">Colophon</a></li>
      </ol></nav>
    </aside>
    <article class="body">
      <h2 id="what-this-is">What this is<a class="anchor" href="#what-this-is">§</a></h2>
      <p>I am a Cardano DRep. This site is the reference corpus my voting rationales point into: a money
      ontology, a blockchain primer, a rights derivation, the instruments I sort and judge proposals
      with, and the record of the votes themselves.</p>
      <p>It exists because on-chain rationales are short and the reasoning behind them is not. Rather
      than re-assert a foundation in every vote, or worse, leave it implicit, I publish it once and link
      to it. That has a second effect I want: it makes the foundation attackable. A reader who thinks a
      vote of mine was wrong can find the exact page the disagreement starts on.</p>

      <h2 id="how-to-cite">How to cite<a class="anchor" href="#how-to-cite">§</a></h2>
      <p>Every page carries a citation block with its permanent URL, and every section heading is
      independently addressable — hover a heading and click the <span style="color:var(--faint)">§</span>
      to copy a deep link to that section alone. Cite the section, not the site, wherever you can.</p>
      <pre><code>Bolander, J. “&lt;Page title&gt;.” The Coordination Commons.
{esc(SITE['base'])}/&lt;funnel&gt;/&lt;page&gt;/#&lt;section&gt;</code></pre>
      <p>The corpus is public and forkable. Quote it, fork it, or argue with it in print; I would rather
      be contested accurately than agreed with vaguely.</p>

      <h2 id="versioning">Versioning<a class="anchor" href="#versioning">§</a></h2>
      <p>These documents re-version. Some of them will change substantially, and I expect parts of the
      money ontology in particular to fall away as real governance usage clarifies what actually
      mattered. Theory here is not rewritten in advance of evidence; lived usage is the mechanism by
      which the corpus updates.</p>
      <p>That creates a tension I would rather name than manage quietly: the more my votes depend on
      this corpus for their legitimacy, the more expensive it becomes to revise, which cuts directly
      against the commitment that none of it is exempt from change. The structural response is the seam,
      below.</p>

      <h2 id="the-seam">The seam<a class="anchor" href="#the-seam">§</a></h2>
      <aside class="seam-note">
        <h3>The one marked joint</h3>
        <p>This argument crosses once, from <em>what this chain is</em> to <em>what its governance owes</em>.
        I do not claim that crossing is a deduction. I claim it is a single, visible, auditable seam,
        stated openly so it can be inspected and contested rather than distributed invisibly through the
        argument where it cannot be found. A framework with one marked joint has not confused itself with
        universality. It is a framework you can audit.</p>
        <p>Pages that inherit the crossing say so, and point here:
        <a href="{r}seam/legibility/">The Legibility of the Seam</a> ·
        <a href="{r}seam/audit/">the audit of whether the corpus keeps that promise</a>.</p>
      </aside>

      <h2 id="disagreeing">Disagreeing well<a class="anchor" href="#disagreeing">§</a></h2>
      <p>Four things would move me off the position, and I would rather be shown them early than late.
      They are stated in full on <a href="{r}foundations/what-cardano-is/#9-what-would-change-my-mind">the
      stance page</a>: that the productive capacity is not what the commons is for; that a condition I
      have named is politics wearing a right's clothes; that the coordination-index reading of the unit
      explains less than the store-of-value reading; or that lived autonomy is improving under a rival
      reading while my framework describes a decline.</p>
      <p>The last of those is the one I am least confident I would notice in time, and finding a sensor
      for it is an open problem I am working on in the open.</p>

      <h2 id="colophon">Colophon<a class="anchor" href="#colophon">§</a></h2>
      <p>Static HTML, one stylesheet, no framework, no analytics, no cookies, no trackers, and no
      browser storage. Nothing about your visit is recorded by this site. Set in
      <a href="https://fonts.google.com/specimen/Ysabeau+Office" rel="noopener">Ysabeau Office</a> by
      Christian Thalmann. Source documents are authored as markdown with typed frontmatter against
      <a href="{r}notes/concept-graph-schema/">the concept graph schema</a>, and the site is generated
      from them once and committed as plain files.</p>
      <p>Contact: <a href="https://x.com/{esc(SITE['handle'])}" rel="me noopener">@{esc(SITE['handle'])}</a>.</p>
      {cite_block("About this space", f"{SITE['base'].rstrip('/')}/about/", depth)}
    </article>
  </div>
</div>
"""
    write(["about", "index.html"], shell(
        title="About", description="What this reference space is for, how to cite it, and the terms on "
                                   "which it expects to be wrong.",
        body=body, depth=depth, current="about", canonical="about/"))


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def build_extras():
    body = """<div class="shell">
  <div class="page-head"><div class="headwrap">
    <p class="eyebrow">404</p>
    <h1>No page at this address</h1>
    <p class="standfirst">Pages here are meant to be permanent, so this is more likely my mistake than
    yours. The full index of work will have what you were pointed at.</p>
    <p><a href="/index-of-work/">Index of all work</a> &nbsp;·&nbsp; <a href="/">Return to the space</a></p>
  </div></div>
</div>
"""
    write(["404.html"], shell(title="Not found", description="No page at this address.",
                              body=body, depth=0, canonical=None))

    base = SITE["base"].rstrip("/")
    urls = [""] + [f"{f['slug']}/" for f in FUNNELS] + [f"{n['path']}/" for n in MANIFEST] \
           + ["index-of-work/", "about/"]
    entries = "".join(f"  <url><loc>{base}/{u}</loc></url>\n" for u in urls)
    write(["sitemap.xml"],
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + entries + "</urlset>\n")

    write(["robots.txt"], f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n")


def main():
    missing = [n["src"] for n in MANIFEST if not (SRC / n["src"]).exists()]
    if missing:
        sys.exit("Missing source files:\n  " + "\n  ".join(missing))

    for f in FUNNELS:
        shutil.rmtree(ROOT / f["slug"], ignore_errors=True)

    # Resolve every title up front, so cross-references (prev/next, cards,
    # the index) never fall back to a slug.
    for n in MANIFEST:
        if not n.get("title"):
            fm, _ = split_frontmatter((SRC / n["src"]).read_text(encoding="utf-8"))
            t = fm.get("title")
            if isinstance(t, list):
                t = t[0]
            n["title"] = (t or n["slug"].replace("-", " ").title()).strip("\"'")

    rendered = {}
    for f in FUNNELS:
        nodes = [n for n in MANIFEST if n["funnel"] == f["slug"]]
        for i, n in enumerate(nodes):
            info = build_node(n, nodes[i - 1] if i else None,
                              nodes[i + 1] if i + 1 < len(nodes) else None)
            rendered[n["path"]] = info
        build_funnel(f, nodes)

    build_index()
    build_index_of_work(rendered)
    build_about()
    build_extras()
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built {len(MANIFEST)} node pages, {len(FUNNELS)} funnels, 3 top-level pages.")


if __name__ == "__main__":
    main()
