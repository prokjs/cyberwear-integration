# Contributing

Read the [complete integration guide](Documentation/en/README.md) before proposing a new addon or tool. Guides are also available in [all five languages](README.md).

## Issues

Use an issue for integration questions, receiver compatibility reports and proposed public interfaces. Include integration type (inventory, chip, OSC or connector), receiver/addon versions, Unity/SDK/Modular Avatar/NDMF versions, desktop/PCVR mode, expected/actual behavior and minimal reproduction steps. Redact private readings, names, credentials, tokens and Widget IDs.

The current interfaces do not establish arbitrary data widgets or chip-controlled product activation. Propose those as explicit contract changes; do not claim existing support, repurpose BPM/battery for unrelated data, or depend on private generated controller/shader details.

## Pull requests

- Keep addon IDs and published wire identifiers stable. New schemas or contact versions require an explicit compatibility discussion.
- Update English and the Korean, Japanese, Simplified Chinese and Spanish guides together. Preserve exact identifiers and safety/verification boundaries in every language.
- Provide exercised verification: OSC wire checks for tools; actual clean-import and avatar checks for Unity assets; two-client/in-headset results for claims requiring them. State what was not exercised.
- Submit only original or appropriately licensed code/assets with notices. No paid/private source, third-party avatars, per-avatar generated fits, Unity caches or credentials.
- Keep synthetic examples clearly labeled. Never present synthetic values as real measurements.

Contributions to documentation/example code are under this repository's MIT license. Do not submit a product asset under that license unless you own the rights and explicitly intend that grant. Any separately licensed asset needs its own clear license before publication.
