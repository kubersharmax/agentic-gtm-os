# AMDA — Augmented Marketing Decision Architecture

**Version 1.2** · By [Kuber Sharma](https://kubersharma.com) · Full specification at [kubersharma.com/frameworks/amda](https://kubersharma.com/frameworks/amda)

---

## The problem

Most enterprise AI governance fails in one of two directions.

The first failure is coercive governance: every AI output requires human review before use. Adoption collapses because the humans become the bottleneck. The system designed to make AI safe makes AI useless.

The second failure is ungoverned autonomy: AI outputs flow directly into external channels without review. Compliance violations appear. Legal gets involved. The governance team intervenes and the coercive failure follows.

AMDA solves this by classifying decisions rather than treating all AI decisions the same.

---

## The framework

Three zones, defined by decision stakes and reversibility:

### Zone 1: AI-Primary

**Definition:** High-volume, low-stakes, fully reversible decisions where AI acts independently.

**Criteria:**
- Decision affects only internal workflow state
- Can be reversed or corrected at negligible cost
- No external exposure in this step

**Examples:** First-pass copy drafts, internal research summaries, data categorization, initial competitive analysis

**Governance:** AI acts. Log is kept. Periodic audit sample.

**Typical volume:** ~70% of total AI decision volume in instrumented product marketing workflows.

---

### Zone 2: Collaborative

**Definition:** Moderate-stakes decisions where AI drafts, human reviews before external output.

**Criteria:**
- Output reaches external audiences (customers, press, partners, regulators)
- Incorrect output carries reputational or compliance cost
- Human review adds material value (not just rubber-stamp)

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

**Governance:** AI provides research and draft options. Human decides and executes.

---

## Classification questions

When classifying a decision:

1. **Who sees the output?** Internal only (Zone 1 candidate) vs. external audience (Zone 2 or 3).
2. **What is the reversal cost?** Near-zero (Zone 1) vs. reputational/financial (Zone 2/3).
3. **Whose career is affected if this goes wrong?** No one's specifically (Zone 1) vs. a named executive (Zone 3).

---

## Production data

From 16 enterprise product launches under AMDA governance:

| Metric | Result |
|--------|--------|
| AI tool adoption rate | 84% |
| Compliance violation reduction | 67% |
| Time-to-market improvement | 34% |
| Messaging engagement lift | 47% |
| Consensus cycles (before) | 3.8 rounds |
| Consensus cycles (after) | 1.6 rounds |

---

## Version history

| Version | Change |
|---------|--------|
| v1.0 | Initial three-zone classification (2023) |
| v1.1 | Added classification questions; formalized reversal cost as primary sort criterion |
| v1.2 | Production data added from 16 launches; Zone 1 volume benchmark established |

---

## Citation

If you use AMDA in your work, please cite:

> Sharma, K. (2023). AMDA: Augmented Marketing Decision Architecture. kubersharma.com/frameworks/amda.

Academic paper under review: *Journal of the Academy of Marketing Science* (JAMS), 2026.

---

## License

[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/) — Share and cite with attribution. No derivatives.
