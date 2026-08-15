# AMDA, the Augmented Marketing Decision Architecture

**Version 1.2** · By [Kuber Sharma](https://kubersharma.com) · Full specification at [kubersharma.com/frameworks/amda](https://kubersharma.com/frameworks/amda)

---

## The problem

Most enterprise AI governance fails in one of two directions.

The first failure is coercive governance: every AI output requires human review before use. Adoption collapses because the humans become the bottleneck. The system designed to make AI safe makes AI useless.

The second failure is ungoverned autonomy: AI outputs flow directly into external channels without review. Compliance exceptions appear. Legal gets involved. The governance team intervenes and the coercive failure follows.

AMDA addresses this by classifying decisions rather than treating all AI decisions the same.

---

## The framework

Three zones, defined by decision stakes and reversibility.

### Zone 1: AI-Primary

**Definition:** High-volume, low-stakes, fully reversible decisions where AI acts independently.

**Criteria:**
- Decision affects only internal workflow state
- Can be reversed or corrected at negligible cost
- No external exposure in this step

**Examples:** First-pass copy drafts, internal research summaries, data categorization, initial competitive analysis

**Governance:** AI acts. A log is kept. Periodic audit sample.

**Observed volume:** Roughly 70% of AI decision volume in the deployment described below. This is a classification of the decision types involved in those launches, not a universal benchmark.

---

### Zone 2: Collaborative

**Definition:** Moderate-stakes decisions where AI drafts and a human reviews before external output.

**Criteria:**
- Output reaches external audiences (customers, press, partners, regulators)
- Incorrect output carries reputational or compliance cost
- Human review adds material value rather than a rubber stamp

**Examples:** Customer-facing messaging, press releases, regulatory filings, partner commitments, pricing communications

**Governance:** AI drafts. Human reviews. Human approves before send. AI does not send.

---

### Zone 3: Human-Primary

**Definition:** High-stakes, low-volume, irreversible decisions where AI informs but does not act.

**Criteria:**
- Decision is irreversible or difficult to reverse
- Carries legal, regulatory, executive, or reputational exposure
- Wrong outcome has career-level consequences for the decision-maker

**Examples:** M&A communications, executive positioning, legal filings, board materials, crisis response

**Governance:** AI provides research and draft options. A named human decides and executes.

Keep this zone small. If it is not small, decisions have been miscategorized.

---

## Classification questions

Three questions, in order.

1. **Can it be corrected if it is wrong?** Reversible decisions tolerate AI autonomy. Irreversible ones do not.
2. **Who sees the output, and what follows?** Internal only points to Zone 1. Crossing a legal, executive, or external boundary pulls a decision up out of Zone 1.
3. **How often does it happen?** High-frequency standardized decisions are where a per-output human gate is fatal to adoption. Low-frequency, high-consequence decisions can absorb human ownership without becoming a bottleneck.

---

## Deployment results

Observed across 16 enterprise product launches in the product marketing function at Tableau, a Salesforce company, prior to 2025.

| Metric | Result |
|---|---|
| Adoption of the non-blocking AI compliance tool within six months | 84% (against near-zero for a functionally equivalent blocking tool in the same organization over the same period) |
| Reduction in recorded messaging-compliance exceptions | 67% against the prior six-month baseline |
| Time from brief sign-off to first external publication | 34% shorter |
| Cross-functional consensus rounds per positioning decision | 3.8 down to 1.6 |
| Lift in owned-channel content engagement | 47% |
| Share of decision volume in the AI-Primary zone | Approximately 70% |

---

## Methods and scope

**Methods note:** These figures come from a single observational deployment at Tableau (Salesforce), prior to 2025. This is not a controlled study. Unit of analysis: individual product launches. The 84% adoption figure compares a non-blocking tool to a blocking equivalent in the same organization over the same period. Reduction in compliance exceptions was measured against the prior six-month baseline. Time-to-market improvement was measured from brief sign-off to first external publish. Consensus rounds reflect internal tracking of cross-functional review cycles. Engagement lift reflects content performance data from owned channels. The approximate 70% AI-Primary share is a classification of the decision types involved in these launches, not a universal benchmark. Results reflect one context and yours may differ. A fuller methods appendix is in progress.

---

## Provenance and version history

Developed at Tableau (Salesforce) to solve a live governance problem in the product marketing function, then generalized and formalized. Further applied and refined at UiPath beginning in 2025.

| Version | Date | Change |
|---|---|---|
| v1.0 | Pre-2025 | Developed at Tableau (Salesforce) across the product marketing function. Three zones, bounded-autonomy principle. Observed across 16 product launches. |
| v1.1 | 2025 | Further applied and refined at UiPath. Formalized as a task-allocation taxonomy with the three classification questions. |
| v1.2 | Jul 2026 | Published specification. Reference card issued. |

---

## Research status

*The Human-AI Interface in Product Marketing: Frameworks for Augmented Decision-Making in Enterprise SaaS*, a manuscript developing AMDA into a formal taxonomy and evaluating its observational evidence, was submitted to the *Journal of the Academy of Marketing Science* in July 2026, to the AI-Driven Marketing special issue. Editorial decision pending.

---

## Citation

> Sharma, K. (2026). *The Augmented Marketing Decision Architecture (AMDA): a three-zone taxonomy for human-AI decision authority in enterprise marketing.* Retrieved from https://kubersharma.com/frameworks/amda

---

## License

[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/). Share and cite with attribution. No derivatives.
