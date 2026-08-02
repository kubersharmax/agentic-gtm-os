# Agentic GTM OS

> Frameworks, models, and operating principles for taking AI agent products to market in enterprise contexts.

By [Kuber Sharma](https://kubersharma.com), Senior Director of Product Marketing at UiPath. Twelve years marketing enterprise software at Microsoft, Salesforce, Tableau, and UiPath, within a twenty-year marketing career.

---

## What this is

Enterprise AI is not primarily a technology problem. It is a trust, governance, and go-to-market problem. The models work. The difficulty is getting organizations to deploy them in production at scale.

This repository contains four frameworks developed in enterprise product marketing functions across Microsoft Azure Machine Learning, Salesforce and Tableau, and UiPath's agentic platform. Each came out of a live problem and was applied against real launches. Where a framework carries field evidence, the scope and limits of that evidence are stated with it.

---

## Frameworks

### [AMDA, the Augmented Marketing Decision Architecture](frameworks/amda.md)

A three-zone governance model for AI decision-making in enterprise marketing workflows. Classifies every AI-assisted decision by stakes and reversibility: AI-Primary, Collaborative, Human-Primary.

Developed at Tableau (Salesforce) prior to 2025, further applied and refined at UiPath from 2025.

Observational deployment results from 16 enterprise product launches in a single product marketing function. This is an observational deployment study, not a controlled experiment. Headline figures: 84% adoption of a non-blocking AI compliance tool within six months against near-zero for a functionally equivalent blocking tool in the same organization; 67% reduction in recorded messaging-compliance exceptions against the prior six-month baseline; 34% shorter time from brief sign-off to first external publication; cross-functional consensus rounds down from 3.8 to 1.6. Full methods and scope note in the [specification](frameworks/amda.md#methods-and-scope).

Full specification: [kubersharma.com/frameworks/amda](https://kubersharma.com/frameworks/amda) · [Reference card](https://kubersharma.com/frameworks/amda-reference)

---

### [The Pilot Trap](frameworks/pilot-trap.md)

A five-stage model for why most enterprise AI never leaves proof-of-concept.

Excitement. Scoping. Sandboxing. Stall. Abandonment. The trap springs at sandboxing, when IT security, procurement, and legal arrive to the party nobody invited them to.

Full specification: [kubersharma.com/frameworks/pilot-trap](https://kubersharma.com/frameworks/pilot-trap) · [Reference card](https://kubersharma.com/frameworks/pilot-trap-reference)

---

### [The Trust Architecture](frameworks/trust-architecture.md)

A three-layer model for building enterprise buyer trust when the product does something buyers have never bought before.

Technical Trust, Operational Trust, Strategic Trust. Buyers evaluate bottom to top. Vendors pitch top to bottom. That is the mismatch.

Full specification: [kubersharma.com/frameworks/trust-architecture](https://kubersharma.com/frameworks/trust-architecture) · [Reference card](https://kubersharma.com/frameworks/trust-architecture-reference)

---

### [The Belief Bridge](frameworks/belief-bridge.md)

A four-plank model for closing the gap between what a product does and what a buyer believes it will do for them specifically.

Evidence. Analogy. Proof Point. Transfer. Most GTM motions build three planks. The fourth is the one vendors skip and the one buyers need.

Full specification: [kubersharma.com/frameworks/belief-bridge](https://kubersharma.com/frameworks/belief-bridge) · [Reference card](https://kubersharma.com/frameworks/belief-bridge-reference)

---

## Playbook

### [The Zero-Copy Revolution: a technical GTM playbook](frameworks/zero-copy-playbook.md)

Not a fifth framework. An operating manual for running segmentation and activation logic inside the data warehouse rather than shuttling customer signals out to a marketing platform first.

Covers the ETL tax, the architecture shift, and the ninety-day sequence. Pairs with the negative-ICP schema in `frameworks/negative-icp-filter.json`.

---

## Reference implementation

`run_onion_filter.py` is a worked example, not a production system. It scores a prospect's agentic readiness by matching stack signals against the negative-ICP schema in `frameworks/negative-icp-filter.json`, then runs a demonstration comparison between a legacy and a modern prospect using illustrative data.

```bash
python run_onion_filter.py
```

No dependencies beyond the standard library. Python 3.10 or later.

---

## Writing

The long-form thinking behind these frameworks lives at [kubersharma.com/writing](https://kubersharma.com/writing).

- [The Pilot Trap: why most enterprise AI stalls before production](https://kubersharma.com/writing/the-pilot-trap)
- [Agent, Automation, or Human? A Decision Boundary Matrix](https://kubersharma.com/writing/decision-boundary-matrix)
- [How to Calculate AI Agent ROI: the formula CFOs actually need](https://kubersharma.com/writing/ai-agent-roi)
- [Enterprise Agentic AI Governance: an operating model, not a policy document](https://kubersharma.com/writing/enterprise-agentic-governance)
- [AI Agents as GTM Copilots](https://kubersharma.com/writing/ai-agents-gtm-copilots), published in [diginomica](https://diginomica.com/agentic-ai-not-one-size-fits-all-solution-agents-automation-human), May 2026

---

## Reference cards

Printable single-page references for each framework, licensed CC BY-ND 4.0. Share and cite freely with attribution.

[kubersharma.com/downloads](https://kubersharma.com/downloads)

---

## Research status

*The Human-AI Interface in Product Marketing: Frameworks for Augmented Decision-Making in Enterprise SaaS*, a manuscript developing AMDA into a formal taxonomy and evaluating its observational evidence, is under review at the *Journal of the Academy of Marketing Science*. Submitted July 29, 2026 to the AI-Driven Marketing special issue.

---

## License

Framework text and diagrams: [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/). Share and cite with attribution, no derivatives.

Code samples and reference implementations: MIT. See [LICENSE](LICENSE).

---

## Contact

kuber@kubersharma.com · [kubersharma.com](https://kubersharma.com) · [LinkedIn](https://www.linkedin.com/in/kubersharma)
