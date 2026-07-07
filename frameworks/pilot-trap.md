# The Pilot Trap

**By [Kuber Sharma](https://kubersharma.com)** · Full specification at [kubersharma.com/frameworks/pilot-trap](https://kubersharma.com/frameworks/pilot-trap)

---

## The pattern

Every enterprise AI initiative starts the same way. A senior leader sees a demo. The demo is genuinely impressive. A small team is named to run a pilot. The pilot is funded, scoped, and kicked off. Six months later, the pilot has ended. The workload it was supposed to handle is still being handled the old way.

This is not bad luck. It is a five-stage pattern so consistent it has a name.

---

## The five stages

### Stage 01: Excitement

A senior leader sees a demo. The capability is real. The use case is plausible. A Slack channel gets named. Energy is high. Budget is approved on a phone call.

### Stage 02: Scoping

The team picks a use case. The use case is chosen for how well it will demo, not how well it will deploy. The pilot boundary is drawn around what the model can do, not what the workflow requires. The deliverable is "validate feasibility."

### Stage 03: Sandboxing (the trap springs here)

The team builds in a sandbox. The sandbox has none of the integrations, none of the policies, and none of the people who own production. The pilot works beautifully.

Then production calls. Production brings three friends: IT security, procurement, and legal. None of them were at the demo. None were at the scoping meeting. They are now setting deployment terms, and the terms differ from what the pilot was built against.

### Stage 04: Stall

The pilot does not officially fail. It stalls. The next review meeting moves out a quarter, then two. The executive sponsor moves to the next priority. The success criteria remain unsigned.

### Stage 05: Abandonment

Nobody decides to abandon the pilot. It is abandoned by the absence of a decision to continue it. The workload continues to be done the old way. There is now an audit log.

---

## The fix

The trap springs at Stage 03, and it is the only stage where the framework changes the outcome. By Stage 04, the pilot is over.

Naming the trap lets you put IT security, procurement, and legal in the room at Stage 02 (Scoping). Their answer is rarely yes, and usually not until next quarter. That is the point. The pilot designed against the right calendar deploys. The pilot designed against the wrong calendar is theatre.

---

## Where it came from

Named in October 2025, in an internal memo for a UiPath customer who had been running AI pilots for two years without a single one reaching production. The earliest version was a slide from a Microsoft offsite in 2018: "the pilot ends, the workflow continues."

---

## License

[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/) — Share and cite with attribution. No derivatives.
