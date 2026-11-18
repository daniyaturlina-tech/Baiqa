# BAIQA — When the Pattern Changes

A colorful, static, responsive research website for the Fall 2026 PLS419 final project **An AI Answer for Kazakhstan**.

**Project status:** A research proposal and interactive fictional demonstration. This is **not** a real Moodle plugin, AI model, clinical tool, or live alert service. No real students or personal records are used.

## Open locally

Open `index.html` in a web browser. It loads `styles.css`, `script.js`, and the optional research figure from `assets/`.

The site uses one font family across all text: **Manrope** (loaded from Google Fonts when online, with one consistent sans-serif fallback). It has no build tools or external JavaScript libraries.

## Publish with GitHub Pages

1. Create a public GitHub repository, for example `baiqa-pls419`.
2. Upload **the contents of this folder** to the repository root (the `index.html` file must be at the root).
3. Open **Settings → Pages** in the repository.
4. Under **Build and deployment**, select **Deploy from a branch**, then choose `main` and `/ (root)`, then Save.
5. GitHub will display the site's URL when publication completes; it is usually `https://YOUR-USERNAME.github.io/baiqa-pls419/`.

No GitHub deployment or live URL has been performed as part of this package.

## Site sections

- 01 The Problem — scope, social-science question, local research and evidence gap
- 02 Background & Data — original chart based on real MICS 2024 published data, limitations of Moodle records
- 03 Research — thematic literature comparison and two documented implemented interventions
- 04 Solution — fictional, interactive Baiqa dashboard and comparison to simple rules and existing Moodle analytics
- 05 The Bill — hypothetical budget and switchable environmental scenarios, all five syllabus cost dimensions
- 06 Verdict — conditional pilot recommendation
- 07 AI Transparency — human-originated decisions, AI assistance and rejected ideas
- 08 References & Methods — traceable sources and evidence disclaimers

## Data provenance and limitations

- `data/mics_2024_youth_screening_indicators.csv` contains published weighted estimates and confidence intervals from Li et al. (2026), Table 1, using Kazakhstan MICS 2024 youth survey respondents aged 15–24. These indicators are **not diagnoses**, and **not specifically university student prevalence**. The chart is a visualization derived from published data, not primary research.
- The fictional student dashboard displays synthetic **illustrative** scores and course engagement to explain the proposed interface. It is not a trained ML model, test of academic risk, or estimate of mental health.
- `data/illustrative_pilot_budget.csv` records a hypothetical six-month budget; values rely on assumed hours and wage proxies, not supplier quotations. Environmental numbers are scenario calculations, not actual electricity bills.
- The underlying Open University Learning Analytics Dataset (OULAD) was identified but **not processed** for this project, so the website does not claim a real Moodle-data model or its performance.
- The project lacks nationally representative evidence of faculty missing academic change signals and lacks a measured Kazakhstan trend in that outcome. It explicitly identifies this as an empirical gap.

## Before final academic submission

Read every paper linked in References and verify the exact claim being cited. Have the student author review and revise the AI transparency statement to reflect actual final decisions. If adding real student data, undertake institutional permissions, ethics and legal review first; do not upload identifiable student records to this website or general-purpose AI services.

## Editing colors and font

Colors and the single font are defined in the first `:root` CSS selector in `styles.css`. All section content is editable in `index.html`. The simulated dataset and interaction logic are in `script.js`.

## Evidence upgrade (November 2026)

- Section 1 now includes official Kazakhstan higher-education enrollment (678.1 thousand, 116 institutions, 2025–26) for scope, clearly **not** a rate of missed faculty alerts.
- Section 2 adds an author-generated, source-reproducible comparison of the 2023 Hasan & Khan randomized trial (29/32 versus 24/33 passing). Source: PLOS ONE Table 4, DOI 10.1371/journal.pone.0288844. See `data/hasan_khan_2023_trial_pass_rates.csv` and `data/reproduce_trial_chart.py`; the plot is `assets/trial-outcomes-2023.png`. It is an external implementation, **not** a measured Baiqa effect.
- Section 3 includes a 9-source critical evidence table distinguishing what each design establishes and its limitations.
- A separate pilot-evaluation section compares no new analytics, simple rules, and Baiqa, including safety stop conditions.
- The costs section includes an interactive staff-hours sensitivity model (10min review; 15min outreach for 30% of alerts; 24wk). Numbers are assumed, not predictive. Water use is discussed without an invented numeric estimate.
- The OULAD individual records remain unprocessed because they were not available to this environment; no academic-behavior ML results are claimed.
- Before publication, the student should critique/refine the draft, verify the references, and export the actual AI Process Log.

## Local Kazakhstan academic probation evidence added

- Original aggregated-data chart from Sergazina (2024), Table 2: women 727/3640, men 1010/3438, combined 1737/7078 ever on probation. These are **one-university descriptive rates**, not causal or national estimates. See `data/sergazina_2024_probation_table2.csv` and `data/reproduce_probation_chart.py`.
- The same thesis, section 4.6.6 (faculty workload), reports one program's ~54:1 student-to-faculty ratio from administrator interviews; interviewees described heavy workload and delayed recognition, and recommended data management improvements. This supports a limited institutional concern but does **not** give a national missed-alert rate.
- All visible chart text now comes from website HTML/CSS using a single Manrope font; static chart PNGs remain in the assets folder for research records but are not displayed as separate-font image charts.

## November 2026 research upgrade

- Added an interactive original re-visualization of **real OULAD** Table 5 results from Wu, Jia & Pham (2026), with within-cohort vs next-year validation toggles. Source CSV: `data/oulad_2026_published_top5_precision.csv`.
- Added findings from Sánchez Trujillo et al. (2026) concerning **false alert workload** and the small AUC difference between logistic regression and random forest.
- Added a deeper three-way literature synthesis and an interactive side-by-side cost scenario comparing ordinary monitoring, transparent rules and Baiqa; this hypothetical scenario is separate from the earlier ₸2.02m budget.
- Cost source assumptions and summary are in `data/compare_3_pilot_options.csv`. Run `python data/reproduce_oulad_and_pilot.py` to verify calculations.
- **Do not claim that these studies evaluated Baiqa**. They studied UK Open University academic outcomes; individual student data were not downloaded or reanalysed here.
