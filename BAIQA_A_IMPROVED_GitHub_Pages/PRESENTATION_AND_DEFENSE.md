# Baiqa — 8–10-minute presentation and viva preparation

These are suggestions for an oral presentation. **Do not read without understanding.** Personalize the script to your own reasoning, especially why you preferred faculty alerts, why you rejected diagnosis, and what you challenged about AI's draft. Use the website as the visual aid; no additional slide deck is required.

## Suggested speaking time

| Timing | Website section | Aim |
|---|---|---|
| 0:00–0:50 | Hero | Hook: What if the first sign of academic difficulty is a change nobody connects? Introduce Baiqa as a proposal, not a real university tool. |
| 0:50–2:00 | Problem | Present Sergazina's n=7,078 sample, 1,737 students ever recorded on probation (24.5% in this one-university sample), the interview-reported ~54:1 student/faculty ratio in one program, and 678.1k higher-education students nationally. The interview evidence supports the problem but does not establish nationwide prevalence of missed alerts. State the social-science question: care versus surveillance. |
| 2:00–3:30 | Data | Explain three incompatible data sources and the original figures. MICS is about youth screening, not LMS inference. The local chart uses Table 2 of Sergazina (727/3640 women and 1010/3438 men, 1737/7078 total ever on probation). The Nebraska trial figure uses actual passing counts (29/32 vs 24/33) but does not prove Baiqa works. |
| 3:30–5:10 | Research | Compare different methods: Kazakhstan correlational work, LMS prediction, randomized intervention, privacy and method biases. Highlight the genuine gap: local, self-baseline alert plus human outreach versus existing alternatives. |
| 5:10–6:35 | Solution + demo | Show one fictional student with changing grades/submit time and another with activity down but grades stable. Explain what professor sees and what the system **does not** infer. |
| 6:35–8:10 | Pilot and bill | Three arms: current support, simple rule, Baiqa. Five costs with humans and privacy as central. Demonstrate alert-volume sensitivity and state exclusions from cost estimate. |
| 8:10–9:20 | Verdict | Conditional pilot only if added value over simple alerts, lawful processing, safe opt-in, human oversight, evaluation, and capacity. If not, choose the simpler system. |
| 9:20–9:45 | Transparency | Name your own original concept, AI contributions and rejected suggestions; acknowledge limitations. |

## Likely professor questions — concise defensible answers

**1. Isn't this already in Moodle?** Moodle has learning analytics and a dropout model. Baiqa is a *proposed* self-baseline change detection and human support workflow. Its addition has to be tested; if Moodle's existing system suffices, Baiqa should not be deployed.

**2. Why use AI at all?** It may help integrate multiple changing indicators, but the research does not demonstrate superiority. The pilot must compare against simple transparent rules. It's legitimate to conclude no further ML is justified.

**3. How can you infer mental health from grades?** We cannot. Baiqa makes no mental-health inference or diagnosis. The cause is unknown, and outreach offers a choice of academic or support resources.

**4. What is genuinely Kazakhstan-specific?** A 7,078-person one-university sample found 1,737 students ever on probation, and administrators described workload and tracking barriers. One program had a reported ~54:1 student/faculty ratio. This is not a national estimate of missed alerts. There is also 576-person academic-wellbeing research and local Moodle modeling.

**5. What is your original real-data visualization?** The bar comparison derived from Hasan & Khan (2023) Table 4: 29/32 = 90.6% pass for AI messages; 24/33 = 72.7% in the control. The source's one-sided p value is .0352, but the trial is small and its comparison is not Baiqa. Also original visuals of the Kazakhstan MICS results and Sergazina's local probation counts.

**6. Is 17.9 points an effect of Baiqa?** No. It is an observed difference in one external trial of messages to students; it establishes plausibility of testing interventions, not Baiqa performance or causal benefits in Kazakhstan.

**7. Why can't Moodle logs establish study time?** Activity events are proxies; students can read offline and browser sessions do not measure attention. Kovanović et al. show that time-on-task choices change analytic findings.

**8. What are the five costs?** Environmental (compute, cooling water, embodied hardware); economic (development and staff capacity); labor (alerts create review/counseling work); governance (institutions control sensitive educational monitoring); data ethics (consent, bias, breaches, wrongful alerts).

**9. Why do you show national youth mental-health data if the system isn't clinical?** It establishes a limited context for wellbeing, not the rate of overlooked cases, nor a prediction target. It's kept separate from academic behavior analysis.

**10. How is your ₸2.02m budget derived?** It's a hypothetical six-month subtotal built from stated hour assumptions and broad wage proxies. It's not vendor pricing. Source prices, security and support demand need actual quotations; a calculator explores faculty labor sensitivity.

**11. When would you terminate the pilot?** If no added student-support benefit versus simple rules, unacceptable false-alert disparities, unlawful access or privacy incidents, coercive outreach, or overwhelmed staff.

**12. What's the most compelling criticism of your own proposal?** Existing Moodle analytics and ordinary teacher attention might achieve comparable outcomes with less surveillance. More data might create more false alerts, workload and loss of trust. The design therefore supports a conditional trial, not rollout.

## Source and AI-authorship reminders

- Do **not** claim national evidence of professors missing struggling students: not established.
- Do **not** claim OULAD raw data was analysed: not done in this environment.
- Do **not** claim a working machine-learning model or live Moodle integration: the dashboard is fictional.
- Do **not** claim the UK Jisc code is Kazakh law; it is an ethical framework.
- Your professor will require independent explanation of any figure, source or analytic choice.
- Update the AI transparency statement after making your own edits and document accepted/rejected suggestions in the process log.

## November 2026 evidence upgrade — use this in the defense

**New real-data chart:** Wu, Jia & Pham (2026), *Frontiers in Education*, analysed 27,553 eligible Open University course enrollments. Baiqa's chart is an **original visual comparison of their published Table 5**, not an independent re-analysis of student records. It shows precision within the top 5% highest predicted risk for three feature sets. Within-cohort: background-only 68.73%, behavior-only 86.55%, all-features 93.82%. Later-year evaluation: 66.54%, 56.87%, 74.55% respectively. The prediction target is failure or later withdrawal, **never mental health or a request for counseling**. The changed performance is a reason to validate locally.

**Second real-data finding:** Sánchez Trujillo et al. (2026), *Data* 11(11), 281, analysed OULAD with longitudinal assessment features. At one threshold they estimated ~427 withdrawal-risk alerts per 1,000 enrollments, about 93 true eventual withdrawals and ~333 non-withdrawals (rounding differences). These are NOT measured Baiqa false alarms. A person who did not withdraw may still deserve support; the purpose is to show that alerts take human time. The same article found logistic regression AUC 0.7102 versus random forest 0.7104 at day 84 in the later-cohort test—little evidence to prefer the more complex option on this dataset.

**Better literature argument:** Compare three claims separately: (1) predictive signal exists in behavior (but cannot infer psychology); (2) intervention effectiveness must be evaluated experimentally, not inferred from ROC-AUC; (3) model complexity and additional personal data may worsen governance and fairness tradeoffs. Pardo & Siemens and Kovanović critique different parts of this chain.

**More specific economic comparison:** A separate, clearly hypothetical 24-week sensitivity analysis uses ₸3,040/hr as a generic labor proxy (national mean monthly salary / assumed 160 hours), 10-min review per flag, 30% of flags taking another 15 min, and 10 flags/week. At these assumptions: existing manual monitoring 96h → ₸291,840; rule alerts with ₸250,000 setup → ₸426,320; Baiqa with ₸1,450,000 setup and ₸1,181 electricity → ₸1,627,501. Their effectiveness is not assumed equal; the purpose is to ask whether Baiqa's **~₸1.20m extra** over simple rules can be justified. This comparison is separate from the detailed ~₸2.02m earlier budget, not to be added to it.

**A question your professor may ask:** "Why hasn't the exact Baiqa model been validated on Kazakhstan data?" Answer: no access to confidential student-level data; no trained model; the project explicitly proposes ethics-reviewed retrospective validation, then an opt-in prospective pilot with a simple-rule control. We prefer a falsifiable claim to a fabricated model result.

**Methodological transparency:** The new OULAD graphic is a *secondary re-visualization* from published table data. The downloaded website package includes a CSV and a standard-library Python reproduction file. It is still not an independent analysis of OULAD's individual records; acknowledge this distinction.
