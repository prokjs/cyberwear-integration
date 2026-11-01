# Integrate with prokjs's personal link receiver HUD and chips

Before adding the receiver or another chip, the installer checks the whole avatar against VRChat's **256 synced-bit limit** on disposable merged NDMF builds. This includes shared inputs and parameters generated only during other addons' build passes, not just the declared preview. Receiver declarations use **32 bits**, plus **8 bits per included library chip** (normally **48 bits** with its two starter chips); overlapping inputs count once. Rejection reports current/projected usage and the required capacity without disabling tracking or leaving a partial installation. Temporary compatibility-build outputs are removed. The settings preview is explicitly marked as declared usage; later non-NDMF SDK callbacks can still require final SDK validation. Shader/performance warnings are not automatically the cause of a blocking error.

Chip tools use **Tools > prokjs > [Asset] > Chip > Generate** and **Generate and install on selected avatar**. Equivalent upgrade/removal actions use **Upgrade installed chip** / **Remove from selected avatar** where supported. Chip prefab roots, filenames and receiver labels use **[Asset Name] Chip**: **Personal Link Receiver Chip**, **Battery Floater Chip**, **Eye Headlight Chip**. The receiver starter chips remain passive visuals; the name does not grant product features. Asset GUIDs and runtime module IDs stay stable. Rebuild the chip setup and upload again after updating.

[All languages](../../README.md) · English is the source guide · Contract snapshot: 2026-11-01

## 1. Choose the integration you need

| Goal | Supported path |
| --- | --- |
| Show an attached addon in the HUD's installed-product list | Ship a schema-1 `AddonDefinition` with your own assets. |
| Offer your addon's chip visual in receiver upload setup | Set `chipVisualPrefab` on that definition; use a separate static visual-only prefab. |
| Display real heart rate or battery readings | Supply the existing OSC parameters from a local tool. |
| Connect an avatar accessory to the receiver | Use the V1 VRChat Contacts contract and respect port/viewer consent. |
| Control your own addon through a functional chip module | Use `chipModuleId` / `chipInstallerType` and the explicit provider contract in section 4; the addon owns behavior. |
| Add arbitrary sensor fields or custom HUD widgets | No general public interface is established. Propose a contract extension; do not disguise unrelated data as BPM or battery. |

The **receiver owns its HUD, configured text, inventory, readings and consent**. A connector does not copy those into its own avatar. Compatible V1 connectors can view receiver-owned display content without receiving every new addon's metadata. This is not a guarantee of arbitrary future compatibility.

This repository publishes developer documentation and an explicitly synthetic OSC example. **The receiver asset, standalone integration asset and additional creator-supplied guide are not distributed here yet.** Obtain the actual receiver package separately from prokjs. Do not infer a release download from this guide. The documentation does not expose private product source or grant rights to paid assets.

```mermaid
flowchart TD
    ADDON[Your attached addon] -->|AddonDefinition at avatar build| LIST[Receiver installed-product list]
    VISUAL[Your static chip visual] -->|Select before upload| CHIP[Receiver slot and owner-hand interaction]
    TOOL[Your local real-data tool] -->|Existing OSC inputs| HUD[Receiver diagnostic HUD]
    CONNECTOR[Compatible avatar connector] -->|V1 Contacts and consent| HUD
    LIST --> HUD
```

## 2. Prepare a development avatar

1. Use a licensed humanoid avatar and back up the project/source scene. No avatar is supplied here.
2. The receiver's documented environment is **Unity 2022.3.22f1, VRChat Avatars SDK 3.10.6, Modular Avatar 1.18.7 and NDMF 1.14.8**, installed through VCC as appropriate. Other versions are not automatically validated.
3. Import the receiver package obtained separately. Select the original avatar outside Play Mode and run **Tools > prokjs > Personal Link Receiver > Attach to selected avatar**. A bare prefab drag is only a visual preview, not the native setup.
4. Fit the receiver manually and save the scene. Use the receiver's HUD settings/preview to configure name, optional information and language. Do not install an overlapping old receiver at the same socket.
5. PC/Built-in shaders are the documented target. Standalone Quest/Android compatibility is not established.

## 3. Register your addon without modifying the receiver

The receiver supplies the editor-only type **`Prokjs.AssetInventory.Editor.AddonDefinition`**. Do not create a second copy or rename its script. Keep its script GUID **`d9e78870673d4c149455cd26a227eb0a`** intact. A consumer needs the actual compatible receiver/framework installed; this repository alone does not install it.

1. Create your own folder, for example **`Assets/MyCyberwear`**. Put your product prefabs, meshes, materials and controllers there.
2. Within that folder choose **Assets > Create > prokjs > Addon Definition**.
3. Fill the fields below. Attach the real product to the avatar, not the definition asset.
4. Distribute your definition and your owned assets with their Unity `.meta` files. Do not bundle another copy of the shared schema or private receiver/paid assets.

| Field | Required contract | Example |
| --- | --- | --- |
| `schemaVersion` | `1`; unsupported schemas fail. | `1` |
| `id` | Unique stable product ID, not a version; no whitespace/control characters. | `mybrand.wrist-display` |
| `displayName` | Nonempty single-line text; no control characters or leading/trailing whitespace. | `Wrist Display` |
| `bodySlot` | Same text constraints as display name. | `WRIST` |
| `order` | Integer sort order; ties use ordinal stable ID. | `100` |
| `assetFolder` | Your own Unity folder containing the definition; not all of `Assets`/`Packages`. | Drag `Assets/MyCyberwear` here. |
| `prefabs` | Optional additional prefab **asset roots**, not scene instances, children or missing entries. | Your product prefab asset. |
| `chipVisualPrefab` | Optional static chip visual asset root; see section 4. | Your separately authored chip prefab. |

Attachment needs an owned folder or at least one valid prefab reference. Duplicate IDs and invalid definitions fail with a correction message; fix them rather than suppressing the error.

**What counts as installed:** real attached prefab provenance or referenced mesh/material/animation-controller assets, including inactive objects and disabled/unpacked assets. Imported folders, object names and registration alone do not establish installation. Duplicate instances show once.

**How it reaches the HUD:** NDMF bakes recognized attached addons onto the disposable build clone at avatar build/upload; source materials are not rewritten. **Refresh selected avatar inventory** updates the editor preview, not a required manual upload step. This is an upload-time inventory snapshot—not live enabled/disabled state, purchase detection or licensing. Adding/removing an addon requires another avatar build/upload to change the uploaded inventory.

## 4. Author and integrate chips

### Make the visual

Create an original mesh/material and a separate prefab asset representing the chip. Throughout this prefab hierarchy, only **Transform, MeshFilter and MeshRenderer** components are allowed, and at least one MeshRenderer is required. Do not include scripts, missing scripts, Animator, SkinnedMeshRenderer, PhysBones, contacts, colliders, lights or whole product controllers. Put functionality on your actual addon, not inside this visual-only prefab.

Author the complete visual at **0.9 mm wide (X) × 14 mm long (Y)** with at most **0.7 mm relief depth (Z)**; the receiver channel is **1.1 × 14.6 mm**. Updated receiver authoring proportionally reduces oversized library visuals to fit both physical slots, including independently scaled slots; smaller intentional fits are not enlarged. Inspect orientation, offsets and clipping, then save and re-upload after changes. This sizing update does not establish live VRChat acceptance.

Set the addon's `chipVisualPrefab` to that prefab. Leave it unassigned if you do not offer a chip. A chip visual is optional; addon registration does not require one.

### Include chips in the avatar upload

1. Install the compatible product on the avatar, then use **HUD settings and preview > Chip assets included in upload > Auto-detect installed cyberwear chips**. Detection populates the upload library; it does not install imported-only products, seat chips, replace occupants or change a product's power mode.
2. For an optional passive visual, open **Advanced**, choose a registered visual or **Chip visual prefab (upload)**, then **Add chip to library**. Use **Available chips > Select chip** to select its actual scene object.
3. Save and upload with the desired chip assets included. VRChat cannot download a new prefab into an already uploaded avatar. The two **Personal Link Receiver Chip** starters remain passive visuals.

### In-world interaction

- Your own hand reveals the owner-only hover card. A fresh fist/grab picks up or removes a chip; open/release to rearm, then make a new grab at **either empty slot** to insert it.
- Each hand holds one chip. Only two chips can be seated at once, regardless of library size. Occupied slots reject insertion without swapping; other players cannot operate your chip controls. Same-hand overlap prioritizes the right slot. Hand-to-hand transfer is not included.
- Universal protocol 2 synchronizes **one Location integer per included library chip: 8 bits each**, even when unseated. Hover, requests and owner UI remain local. Interaction uses native `GestureLeft`/`GestureRight = 1`, not uploaded custom runtime scripts.
- Removing/ejecting frees the occupied slot. Power-off alone leaves it occupied. Passive visuals grant no license or product activation; a registered functional addon can gate its own behavior through its explicit module integration. There is no general arbitrary HUD-widget or sensor-field API.

Functional addon authors can set `chipModuleId` to a stable runtime ID and `chipInstallerType` to the full editor type name (without assembly qualification). Expose `public static GameObject EnsureReceiverChip(GameObject avatar, GameObject receiver, string language)` and return the real registered library item with that exact ID. The addon owns installation and behavior; keep receiver consent intact. Passive data-only registrations may use a `visual.*` module ID with `chipVisualPrefab` and no provider. Existing target-library modules are reused; a conflicting module on another receiver is rejected.

## 5. Supply live data to the HUD

Enable **PC VRChat > Action Menu > Options > OSC > Enabled**. The normal local destination is **`127.0.0.1:9000`** over UDP. Every address below begins with **`/avatar/parameters/`**. Own only the inputs your tool actually supplies; do not run competing senders for the same fields or write consent controls.

| Parameter | OSC type | Meaning |
| --- | --- | --- |
| `Juice/Level` | Float (`f`) | Normalized 0–1 battery level; interpret with state. |
| `Juice/State` | Int (`i`) | 0 unknown; 1 battery; 2 charging; 3 battery-free/external/unlimited state. State 3 must reflect confirmed capability or an explicit user override, not an assumption that wired means unlimited. |
| `Juice/Heartbeat` | Bool (`T`/`F`) | Alternating battery-transport heartbeat, not a constant true and not BPM. |
| `PersonalLink/Heartbeat` | Bool (`T`/`F`) | Alternating monitoring-transport heartbeat; useful for HR-only monitoring. |
| `hr_percent` | Float (`f`) | BPM divided by 200; 120 BPM is 0.6. |
| `hr_connected` | Bool (`T`/`F`) | Valid current HR data, not merely a connected sensor socket. |

Send a changing heartbeat at approximately one-second cadence **while monitoring**, not merely while your app window is open. The generated HUD has separate eight-second changing-heartbeat watchdogs; either fresh heartbeat marks transport available. **Transport activity does not prove each sensor is fresh.** Your tool must clear `hr_connected`/HR values when its source is missing, invalid or stale, and send battery state 0 when battery data is unavailable. Stop/exit should clear owned availability; abrupt termination cannot guarantee a final packet. Another active heartbeat can keep transport available, so do not rely only on the HUD watchdog for sensor expiry.

Do not present demo input as measured data. A successful UDP send does not prove the avatar received the correct parameters. The receiver/framework declares these inputs; inspect the actual avatar OSC configuration if receipt fails. Do not duplicate incompatible animator/expression declarations.

### Run the explicitly synthetic wire example

Requires Python 3.9+; no third-party modules. From the repository root:

```sh
python examples/send_heart_rate.py --bpm 120 --seconds 3
```

This sends **synthetic 120 BPM**, `hr_connected = true` and an alternating `PersonalLink/Heartbeat` once per second, then clears its HR input. It is an encoding/integration example, **not a sensor driver**. Do not use it alongside a real HR sender or claim its output is live. Adapt the sending functions to your real source and its freshness checks; preserve the parameter types and normalization. No battery, consent or chip state is written by the example.

## 6. Connect a third-party avatar accessory

The shared V1 contact identifiers are:

| Tag | Role |
| --- | --- |
| `ProkjsPersonalLinkSocketV1` | Receiver's open socket. |
| `ProkjsPersonalLinkAvailableSocketV1` | Open unoccupied socket available for acquisition. |
| `ProkjsPersonalLinkConnectedPlugV1` | Compatible plug tip sender. |
| `ProkjsPersonalLinkViewerV1` | Eligible viewer viewpoint sender. |
| `ProkjsPersonalLinkViewerEnV1`, `ProkjsPersonalLinkViewerKoV1`, `ProkjsPersonalLinkViewerJaV1`, `ProkjsPersonalLinkViewerZhV1`, `ProkjsPersonalLinkViewerEsV1` | Matching viewer language tags. |

Use the separately supplied receiver/free plug as the practical reference when available. The free plug's contact is at its electrical nose (local +Y). Put viewer targeting at the actual avatar viewpoint, not arbitrarily on the tool mesh. Do not advertise occupied sockets as available or bypass user opt-in. A matching tag alone is not a complete latch solver or proof of compatibility: your accessory owns its native deployment, grabbing, constraints and disconnection behavior. No private HUD buffers or generated controller names are a supported third-party API.

**Port enabled** and **Share readings** start OFF; receiver **View HUD** starts ON. The receiver owner must open the port and opt in to sharing; viewer eligibility does not override those choices. Compatible connector-side viewer controls must also respect the viewer's choice. A paid cable is not required for free receiver/plug/HUD use.

The public body inventory/portrait remains public. Diagnostic information follows the receiver's gates. Geometric targeting is **not authentication, encryption or guaranteed privacy**; co-located cameras may be indistinguishable, and synced readings remain accessible outside the display. Configured names are not authenticated usernames. OSC UDP is unauthenticated/unencrypted: keep it local/trusted. Never upload credentials or secrets in HUD text, assets or bug reports.

## 7. Verification before distribution

- **Registration:** an imported-but-unattached addon stays absent; an attached addon appears once; inactive/unpacked variants still recognize real provenance. Duplicate IDs and bad references produce actionable failures.
- **Upload inventory:** verify the build-time result after changing installed addons without relying on a manual preview refresh. Ensure source materials are not modified.
- **Chips:** verify selection, visual-only component validation, both empty slots, occupied-slot rejection, fresh-grab/rearm, one chip per hand, right-slot hover priority and owner-only operation. Check empty/held/seated labels, power-off occupancy, removal freeing the actual slot, clipping, saved state and remote replication. Budget every included chip at 8 synced bits, not just the seated ones.
- **Telemetry:** check the actual uploaded avatar receives correct float/int/bool types and normalized values. Test missing sensors, stale HR while another heartbeat continues, stop/restart and no heartbeat for over eight seconds. Unknown must remain unknown; synthetic data must remain identified as synthetic.
- **Connections:** use two actual consenting VRChat clients; test port closed/open, sharing off/on, viewer off/on, occupied socket handling, disconnect/reconnect and unrelated viewers. Test your own device's reach/constraint rules; do not assume another product's settings apply.
- **Platforms:** test desktop and PCVR/stereo as claimed, avatar scaling and the versions you advertise. Do not extrapolate Quest support or universal avatar compatibility from editor success.
- **Clean package:** import into a clean supported project; include your assets, definition and `.meta` files and required notices, not paid/private source, avatar assets, credentials or Unity caches.

Source inspection and local OSC loopback checks do not establish uploaded-avatar, two-client, physical-sensor or in-headset acceptance. No such acceptance is claimed by this repository.

## 8. Distribution and support

Keep a unique stable addon ID across releases, preserve asset GUIDs and declare the required receiver/schema version. Translate visible labels, not protocol identifiers. Use **Cyberwear** as the ecosystem category; third-party projects must not imply official endorsement. The MIT license here covers only this repository's documentation/example, not separately provided product assets, fonts, SDKs or your addon.

Open a GitHub issue with your integration type, receiver/addon versions, Unity/SDK/MA/NDMF versions, desktop/PCVR mode, expected/actual behavior and minimal steps. Remove names, private readings, tokens and Widget IDs. Propose arbitrary-data fields or chip activation APIs openly instead of modifying private receiver implementation details.
