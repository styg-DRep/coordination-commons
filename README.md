# The Coordination Commons

The public reference space behind the Cardano DRep voting rationales of Jeremy Bolander
(`@styg50`). Static HTML, no framework, no build step required to serve.

## Deploying to GitHub Pages

1. Create a repository (the URL below assumes `coordination-commons`).
2. **Set the canonical origin.** Open `_build/build.py` and edit `SITE["base"]` to your published
   URL, then re-run the build (below). Every "cite this page" permalink is generated from it, so
   this is the one thing to get right before the first link goes into a rationale.
   While you're there, fill in `SITE["drep_id"]` once re-registration is done.
3. Commit everything and push to `main`.
4. Settings → Pages → Source: **Deploy from a branch** → `main` / `/ (root)`.

`.nojekyll` is already present, so GitHub serves the files as-is rather than running Jekyll over
them. A `CNAME` file at the root will switch it to a custom domain.

## Editing

Two ways, and both are fine:

- **Edit the HTML directly.** The output is plain semantic HTML with one stylesheet. Nothing will
  break. This is the right move for a typo or a quick correction.
- **Edit the markdown and rebuild.** Source documents live in `_source/`. Requires Python and one
  dependency:

  ```
  pip install markdown
  python3 _build/build.py
  ```

  The build wipes and regenerates the five funnel directories only. It never touches `assets/`,
  so hand edits to CSS and JS are safe.

Everything about the site's shape — which documents are published, which funnel they sit in,
reading order, card copy, typed edges, and which pages carry the seam marker — lives in the
`MANIFEST` and `FUNNELS` lists at the top of `_build/build.py`. Adding a document is one entry in
`MANIFEST` plus a file in `_source/`.

## Structure

```
/                        the Space — five doors, all converging on the seam
/foundations/            the derivation: ontology → primer → rights → consent
/seam/                   the marked joint, and the engineering crossing
/instruments/            intake and sort, the diagnostic, abstention spines
/rationales/             the voting record, one addressable page per vote
/notes/                  working diagnostics, evidence anchors, trajectory maps
/index-of-work/          every page, by funnel
/about/                  how to cite, how it re-versions, the falsification terms
```

## Citation design

This is the point of the site, so it is worth stating plainly. Every page carries a permanent URL
in a citation block, and every `h2`/`h3` gets a stable `id` plus a `§` anchor that copies a deep
link to that section alone. Rationales should cite the section, not the site:

```
https://<base>/foundations/rights/#the-right-to-settlement-access
```

Because the anchors are derived from heading text, **renaming a heading breaks inbound links from
rationales already on chain.** If a heading has been cited, keep its old `id` (add
`{#old-id}` to the heading in the markdown source — `attr_list` is enabled) rather than letting
the slug drift.

## Adding a rationale

Add the markdown to `_source/`, then add a `MANIFEST` entry in the `rationales` funnel with a
`vote` block:

```python
{
    "slug": "some-action", "funnel": "rationales", "src": "some-action.md",
    "title": "…", "subtitle": "…",
    "kicker": "Voting rationale · Treasury Withdrawal",
    "strip_contents": True, "strip_meta_table": True, "demote": True,
    "vote": {"verdict": "ABSTAIN", "gaid": "gov_action1…",
             "ga_type": "Treasury Withdrawal",
             "submitted": "…", "expires": "…"},
    "card": "One or two sentences for the ledger and the index.",
},
```

The three cleanup flags are for documents exported from Google Docs. Markdown authored natively
needs none of them.

## Notes

- No analytics, no cookies, no trackers, no browser storage. Nothing about a visit is recorded.
- Type is [Ysabeau Office](https://fonts.google.com/specimen/Ysabeau+Office), loaded from Google
  Fonts with a system fallback stack. To remove the third-party request entirely, download the
  `.ttf` files into `assets/fonts/` and replace the `@import` at the top of `assets/site.css` with
  local `@font-face` rules.
- Dark mode follows the OS setting. The seam is the only element in the palette that uses a second
  hue, in both themes — crossing the joint is meant to be legible as colour.
- `_source/` is published along with everything else. If you would rather it not be, move it
  outside the repo and point `SRC` in the build script at the new location.
