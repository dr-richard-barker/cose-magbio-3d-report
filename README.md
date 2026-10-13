# CoSE MagBio-3D — Interactive Report

**Live:** https://dr-richard-barker.github.io/cose-magbio-3d-report/

Design-stage report for the CoSE MagBio-3D three-axis closed-loop Helmholtz chamber for
biology, by Collaborative Science Environment Inc. (Madison, Wisconsin):

- **Chamber Inspector** — the parametric CAD (nested square Helmholtz pairs, split formers,
  Petri rack) with layer toggles and a section cut.
- **Field Visualizer** — the Biot–Savart model of the coils, run in your browser: set the coil
  currents and see slice maps, 3D field arrows and lines, and the field in each dish. On load
  the page checks itself against reference values from the Python model.
- **Cost & BOM** and the **13 engineering dossiers** (summaries).

> **Status: design stage.** No cage has been wound and no driver or firmware has been built.
> Nothing on these pages has been measured: geometry and fields are model outputs, prices are
> targets, and no bill of materials has been quoted.

## How this repo is made

The files here are generated in the CoSE design repository (`cad/build.py`) and copied by its
`tools/publish_report.sh`. Do not edit them here; changes would be overwritten on the next
publish. To view locally, run `python3 serve.py` in this folder and open
http://localhost:8415 (the page loads its data with `fetch`, so opening `index.html` directly
from disk does not work).

## Licence

Hardware design data (the CAD meshes in `assets/cad/`): CERN-OHL-S-2.0. Software (the page and
`serve.py`): MIT. See [LICENSE](LICENSE).

© 2026 Collaborative Science Environment Inc.
