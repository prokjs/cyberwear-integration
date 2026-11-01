# Cyberwear Integration

Public developer guides for integrating third-party addons, tools, connectors and chip visuals with **prokjs's personal link receiver HUD**.

## Complete guides / 전체 가이드 / 完全ガイド / 完整指南 / Guías completas

| Language | Guide |
| --- | --- |
| English | [HUD, receiver, addon and chip integration](Documentation/en/README.md) |
| 한국어 | [HUD·리시버·애드온·칩 연동 가이드](Documentation/ko/README.md) |
| 日本語 | [HUD・レシーバー・アドオン・チップ連携ガイド](Documentation/ja/README.md) |
| 简体中文 | [HUD、接收器、插件和芯片集成指南](Documentation/zh/README.md) |
| Español | [Integración del HUD, receptor, complementos y chips](Documentation/es/README.md) |

Every guide covers the same registration schema, chip authoring and slot interaction, OSC input types, V1 Contacts, consent, setup and distribution checks. English is the source text; machine identifiers are unchanged across languages.

## What you can integrate now

- **Addon inventory:** register your own attached product using schema-1 `AddonDefinition`, without patching a fixed receiver catalog.
- **Chips:** register a static chip visual, select it before avatar upload, and use the receiver's native owner-hand/slot interaction.
- **Live readings:** feed supported heart-rate/battery inputs through local OSC.
- **Avatar connectors:** use the receiver's V1 contact protocol while respecting wearer and viewer choices.

Registration does not create arbitrary HUD widgets, and chip visuals do not activate or license products. The guides explain these boundaries and how to propose an extension.

## Contents and availability

This repository contains documentation and a [Python OSC wire example](examples/send_heart_rate.py). The example sends explicitly synthetic values, not real sensor measurements. It requires Python 3.9+ and no extra modules.

**No receiver Unity package, standalone integration asset, paid product asset, avatar or sensor driver is included.** The integration asset and additional creator-supplied guide can be published here when supplied; they are not available downloads today. Obtain the actual compatible receiver separately from prokjs. A public repository is not proof of a BOOTH release.

Target documented environment: Unity 2022.3.22f1, VRChat Avatars SDK 3.10.6, Modular Avatar 1.18.7, NDMF 1.14.8 and PC/Built-in rendering. Other versions and standalone Quest/Android are not established as supported. Read the guide before making compatibility claims.

## Contributing and licensing

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) and [CHANGELOG.md](CHANGELOG.md). Use issues for proposed integrations and pull requests for corrections/examples. Public examples must not contain secrets, private readings, paid/private source or unlicensed assets.

[MIT](LICENSE) applies only to this repository's documentation and example code. It does not relicense separately supplied product assets, dependencies, fonts, third-party work or branding. Third-party integrations must not imply official endorsement.
