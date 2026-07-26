# Concept Graph Schema for the Constitutional Coordination Commons Project

**Status:** Working draft, v0.1
**Purpose:** Define the frontmatter schema and edge type vocabulary used to author the concept graph in Obsidian and render it through Quartz.
**Audience:** The author and any future collaborators contributing to the framework.

---

## Why This Document Exists

The hub-and-spoke architecture commits the project to two things that are in tension: a deep derivational center, and standalone public-facing spokes. A typed concept graph is the mechanism that lets both be true. Concepts are nodes with stable definitions and explicit relationships; artifacts (primers, tools, papers, case studies) are nodes that *use* and *introduce* concepts. The graph lets readers move by concept across spokes, lets authors check coverage and consistency, and lets the derivational chain be rendered rather than implied.

The schema below is the minimum needed to do this work. It is intentionally smaller than what mature knowledge-graph systems support. Resist expanding the edge vocabulary until real authoring proves a new type is necessary, because every new edge type creates an authoring burden across the whole vault.

---

## Two Node Types

Every markdown file in the vault is either a **concept node** or an **artifact node**. The distinction matters because they serve different functions and render differently.

A **concept node** defines a single concept in the framework. It is the canonical home of that concept's definition, its position in the derivational chain, and its typed relationships to other concepts. Concept nodes live under `/concepts/` and use a single canonical filename (e.g. `coordination-commons.md`). They are short — generally a definition, a short derivation note, and frontmatter doing the structural work.

An **artifact node** is any piece of writing meant to be read on its own — a primer, a working paper, a tool, a case study, an explainer, an amendment rationale. Artifact nodes live under `/artifacts/<spoke>/` and reference concepts. They are where the actual prose of the project lives.

The split keeps definitions stable and reusable. A concept's definition lives in one place; every artifact that uses the concept links to it; readers get consistent meaning across the whole vault.

---

## Concept Node Schema

```yaml
---
# Identity
type: concept
id: coordination-commons
canonical_name: "Coordination Commons"
aliases:
  - "coordination protocol commons"
  - "monetary commons"

# Position in the framework
status: stable                   # exploratory | contested | stable | placeholder
chain_position: foundational     # foundational | derived | applied | diagnostic
spoke_home: A                    # the spoke that owns the canonical definition
hub_member: true                 # is this part of the deep hub?

# Definitional content
one_line: "A shared infrastructure for coordinating productive exchange that cannot legitimately be owned by any subset of its participants."
canonical_artifact: "[[The_Coordination_Commons]]"
introduced_in: "[[The_Coordination_Commons]]"

# Typed edges — see edge vocabulary below
derives_from:
  - "[[money-as-protocol]]"
  - "[[productive-agency]]"
refines:
  - "[[commons]]"
contrasts_with:
  - "[[private-infrastructure]]"
  - "[[shareholder-claim]]"
composed_of:
  - "[[symbolic-claim]]"
  - "[[settlement]]"
  - "[[constitutive-participation]]"
instantiated_by:
  - "[[open-source-p2p-blockchain]]"
violated_by:
  - "[[enclosure]]"
  - "[[reification]]"
  - "[[toll-extraction]]"
protected_by:
  - "[[settlement-access-right]]"
  - "[[governance-participation-right]]"

# Provenance and revision
last_revised: 2026-05-18
revision_notes: "[[changelog#coordination-commons]]"
contested_by: []                 # links to objection notes
open_questions:
  - "[[oq-commons-boundary]]"

# Tags for filtering and views
tags:
  - concept
  - hub
  - foundational
---

## Definition

A coordination commons is a shared infrastructure for coordinating productive
exchange whose value emerges from the participation of all its co-constituents,
and which therefore cannot legitimately be owned, enclosed, or governed by
any subset of those participants without violating the foundational
relationship that gives it value.

## Why It Sits Where It Sits in the Chain

The concept follows from the money ontology: once money is understood as a
coordination protocol rather than a commodity, the question of *what the
protocol coordinates* and *whose participation constitutes it* yields the
commons claim. It precedes the rights derivation because the constitutive
relationship between participants and the commons is what generates rights
rather than preferences.

## Notes on Use

This concept is foundational and should be linked, not paraphrased, in artifacts
that depend on its specific meaning. The aliases above capture common informal
usage; the canonical name should be preferred in formal artifacts.
```

A few notes on the design:

The `id` field uses kebab-case and matches the filename. Wikilinks throughout the vault use this id; the `canonical_name` is purely for display. This separation lets you rename a concept's display form without breaking links.

`status` is the single most important field for readers. It tells them whether to treat a concept as load-bearing or provisional. `placeholder` is reserved for concepts that have a name but no real derivation yet — useful for noting future work without pretending it's done.

`chain_position` is a coarse classifier of where the concept lives in the derivational logic. `foundational` sits in the hub. `derived` follows from foundational concepts (e.g. specific rights). `applied` is concepts that emerge in operational work (e.g. specific capture patterns). `diagnostic` is concepts used in tests or rubrics. This isn't a strict hierarchy; it's a navigation aid.

`canonical_artifact` is the artifact a reader should be sent to if they want the full treatment, not just the definition. It may differ from `introduced_in` over time, as treatments mature.

---

## Artifact Node Schema

```yaml
---
# Identity
type: artifact
id: blockchain-money-primer
title: "From Coordination Protocol to Constitutional Commons: A Primer"

# Classification
artifact_class: primer           # working_paper | primer | tool | education |
                                 # case_study | amendment | objection | one_pager
spoke: B
depth_level: 2                   # 1=standalone, 2=lightly-grounded,
                                 # 3=hub-dependent, 4=constitutional-action
status: stable                   # draft | review | stable | archived
version: "1.2"

# Audience and use
audience:
  - DReps
  - SPOs
  - rights-interested token holders
reading_time_minutes: 25
prerequisites: []
reading_paths:
  - drep-onboarding
  - amendment-author-orientation

# Concept relationships
introduces_concepts:
  - "[[coordination-commons]]"
  - "[[constitutive-participation]]"
uses_concepts:
  - "[[money-as-protocol]]"
  - "[[productive-agency]]"
  - "[[settlement]]"
tests_concepts: []               # case studies and tools populate this

# Provenance
last_revised: 2026-05-18
authors:
  - primary-author
revision_history: "[[changelog#blockchain-money-primer]]"
objections: []
license: CC-BY-SA-4.0

tags:
  - artifact
  - primer
  - spoke-B
---
```

The `depth_level` and `prerequisites` fields together drive the site's readiness gates. A reader hitting a depth-3 artifact can be shown a "this assumes familiarity with X, Y, Z" panel that links into the prerequisite artifacts. A depth-1 artifact promises it can be read cold.

`reading_paths` are the curated journeys mentioned in the architecture feedback — finite, named, with clear endpoints. They're the third axis alongside spokes and depth levels.

`introduces_concepts` vs `uses_concepts` matters more than it looks. An artifact *introduces* a concept when it provides the canonical or near-canonical treatment; it *uses* a concept when it depends on the treatment elsewhere. Quartz can render the difference: a concept page can show "introduced in" prominently and "used in" as a secondary list.

---

## Edge Type Vocabulary

The edge types are deliberately small. Each one carries an argumentative function that an untyped link would obscure. Every edge is directional unless explicitly noted; the inverse is computed at render time, not authored on both ends.

### derives_from / derives

The spine of the framework. A concept *derives_from* the concepts whose prior establishment is logically required for it. Use sparingly — only for relationships where the dependency is strict, not merely thematic. The graph of `derives_from` edges should be a directed acyclic graph rooted at the money ontology; if you find a cycle, something is wrong with the derivation.

*Example:* `coordination-commons` derives_from `money-as-protocol`.

### refines / refined_by

A concept *refines* a more general concept by specifying it further. Use when the refining concept could substitute for the general one in some contexts but adds precision or constraint.

*Example:* `constitutional-debt` refines `governance-gap`. `tokenomic-capture` refines `capture`.

### contrasts_with (symmetric)

A concept *contrasts_with* another concept when the contrast is doing real definitional work — when readers will best understand the concept by understanding what it is *not*. This is the only symmetric edge type; authoring it on one side renders it on both.

*Example:* `token-holder` contrasts_with `shareholder`, `citizen`, `customer`.

### composed_of / composes

A concept is *composed_of* its structural parts. Use when the parts are themselves concepts with their own pages, not merely component ideas.

*Example:* `reciprocity-loop` is composed_of `service-to-commons`, `recognition`, `proportionate-return`.

### instantiated_by / instantiates

An abstract concept is *instantiated_by* a concrete instance. Use to connect framework-level concepts to specific cases, mechanisms, or implementations.

*Example:* `coordination-commons` instantiated_by `open-source-p2p-blockchain`. `capture-pattern` instantiated_by `treasury-syndicate-formation` (in a case study).

### violated_by / violates

A right or commons condition is *violated_by* specific mechanisms. The inverse direction — `violates` on the mechanism side — is computed automatically.

*Example:* `unit-of-account-integrity` violated_by `tokenomic-capture`, `silent-issuance-adjustment`.

### protected_by / protects

A right or commons condition is *protected_by* mechanisms, rights, or constraints. Symmetrically computed.

*Example:* `coordination-commons` protected_by `settlement-access-right`, `governance-participation-right`.

### tested_by / tests

A concept is *tested_by* diagnostic tools, checklists, or case studies that exercise it. This is how operational artifacts surface back into the concept graph.

*Example:* `public-capacity` tested_by `[[public-capacity-test]]`. `capture-pattern` tested_by `[[treasury-capture-checklist]]`.

### evidenced_by / evidence_for

A claim or pattern is *evidenced_by* case studies, governance actions, or empirical observations.

*Example:* `enclosure-sequence` evidenced_by `[[case-historical-fiat-capture]]`.

---

## A Note on What's *Not* Here

I left out several edge types you might expect to see, because they would expand authoring burden faster than they pay off:

`related_to` — too vague to render usefully; degrades into untyped backlinks.

`implies` and `entails` — these are doing the same work as `derives_from` for most cases; collapse them.

`opposes` — usually `contrasts_with` is what you actually mean; reserve `opposes` for the rare case of genuine normative opposition between concepts.

`see_also` — the wikilinks in prose handle this; no need to formalize.

If a real authoring need arises that none of the above edges fits, add a type. Don't pre-populate.

---

## Naming Conventions

Filenames and ids are lowercase, hyphen-separated, singular: `coordination-commons.md`, not `Coordination_Commons.md` or `coordination-commonses.md`.

Concept ids should be nouns or noun phrases. Mechanisms (things that violate) can be verbs nominalized: `enclosure`, `toll-extraction`, `silent-issuance-adjustment`.

Rights use the pattern `<thing>-<right-type>` where useful: `settlement-access-right`, `governance-participation-right`, `unit-of-account-integrity` (here the integrity is the right).

Aliases capture how the ecosystem actually talks. Include misleading or overloaded terms here so the canonical concept is findable from common search queries.

---

## Authoring Views (Obsidian Dataview)

The schema is designed to be queryable with Obsidian's Dataview plugin. Some views I'd recommend setting up from day one:

A **coverage view** that lists every concept with `status: placeholder` so unfinished derivations are visible.

A **derivation map** that walks `derives_from` recursively from any chosen concept back to the foundational concepts. This is the author's check on whether the chain is intact.

An **orphan check** that lists concepts with no incoming edges — these are either foundational or genuinely orphaned, and you want to know which.

A **contested-concepts view** that lists concepts where `contested_by` is non-empty, sorted by recency. This is the live dashboard of the project's open arguments.

An **artifact coverage view** that lists every concept and counts how many artifacts introduce or use it. Concepts with zero artifact uses are candidates for either removal or future writing; concepts with many uses but only one introducing artifact may need clearer canonical treatment.

A **reading path view** that, for each named path in `reading_paths`, lists the artifacts in order. This is the editorial check on whether paths actually exist as coherent journeys.

These queries are also the foundation for Quartz components later — the same Dataview logic translates to data-driven Astro components.

---

## Quartz Rendering Notes

Quartz handles the basic case (wikilinks, popover previews, backlinks, graph view) out of the box. The schema above requires some custom transformers and components beyond that.

**Typed backlinks.** The default Quartz backlinks panel is untyped. A custom transformer should read the edge fields from frontmatter and group backlinks by relationship type. On a concept page, this renders as sections: "Derives from," "Refined by," "Instantiated by," "Violated by," etc. This is the single most important visible difference between this site and a generic Quartz vault.

**Definition peek.** Quartz's popover previews can show the first paragraph of a linked page on hover. For concept nodes, the `one_line` frontmatter field is a better preview than the first paragraph — short, definitional, and reliable. A small modification to the popover component to prefer `one_line` when the linked node is a concept is worth the effort.

**Status badges.** Render `status` as a visible badge on every concept and artifact page. Readers should never have to guess whether they're looking at stable or exploratory content.

**Depth and prerequisite gating.** On artifact pages with `depth_level >= 3`, render a prerequisite panel at the top with links to the prerequisite artifacts and a one-line summary of what each contributes. This makes the architecture's dependency model visible.

**Reading paths.** Implement reading paths as a separate top-level navigation. Each path has its own page that walks the artifacts in order with brief connective tissue between them. The frontmatter field on each artifact populates these automatically.

**Concept page template.** Concept pages should render in a consistent layout: name, aliases, status, one-line definition, derivation note, typed-edge sections, canonical-artifact link, open questions, contested-by notes. The body content of the markdown file fills the middle section; the rest is frontmatter-driven.

**Graph view filtering.** The default graph view is overwhelming and rarely useful at full scale. Configure it to filter by edge type — let readers see just the derivation graph, just the violations graph, etc. This turns the graph view from a curiosity into a genuine analytic tool.

---

## Adoption Path

Don't migrate everything at once. The schema is most valuable when applied to the concepts that do the most argumentative work; trying to backfill every minor term will exhaust the authoring effort.

A reasonable sequence: take the core concepts you've already worked out (money-as-protocol, coordination-commons, constitutive-participation, the named rights, the named capture mechanisms, constitutional-debt), give each a concept page with full frontmatter, and link the existing artifacts to them via `introduces_concepts` and `uses_concepts`. That alone is enough to power the most important reader behaviors: peek, typed backlinks, walk-the-derivation.

Once that core is live, every new artifact authored introduces or refers to concepts using the same conventions, and the graph grows naturally. Concepts that prove hard to fit the schema are the ones worth examining — usually they reveal a real ambiguity in the framework, not a defect in the schema.

---

## Open Questions for This Schema

These are real open questions worth surfacing rather than papering over.

How should *contested* concepts work in practice? A concept whose definition is itself disputed needs a different rendering treatment than a stable concept with contested applications. Possibly a `contested` status value with a required `contestation_note` field.

How should the schema handle Cardano-specific concepts (Tenets, DReps, Constitutional Committee, gov actions) that have their own canonical definitions elsewhere? Probably as concept nodes with a `external_canonical_source` field pointing to the official definition, plus the framework's analysis of how the concept fits.

How should multi-author authorship and contributor attribution be represented when the project gains collaborators? The `authors` field is a placeholder; a real solution will need integration with whatever attribution conventions the project adopts.

These should be resolved by the time the second wave of concept pages is authored, not before — let real use surface what's needed.
