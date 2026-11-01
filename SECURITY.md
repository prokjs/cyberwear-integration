# Security and privacy

HUD viewer targeting uses avatar contact/proximity and camera geometry, not authenticated identity, encryption or guaranteed privacy. Co-located cameras may be indistinguishable. Network-synced parameters can remain accessible outside the displayed panel. A configured display name is not identity proof. Public body inventory/portrait is not covered by diagnostic sharing gates.

OSC UDP is unauthenticated and unencrypted. Keep destinations local/trusted; the included example sends only to loopback. Do not expose VRChat's OSC endpoint to the internet or rely on the HUD as a medical/security device.

Never commit or post tokens, Pulsoid Widget IDs/URLs, private sensor readings, private avatar data or credentials. Do not put secrets in uploaded HUD text. Public history can retain removed files; report and rotate exposed credentials promptly.

For a sensitive vulnerability, use GitHub's private vulnerability reporting if enabled on this repository. If unavailable, do not post exploit details or sensitive data publicly; use an established private contact with the maintainer. Ordinary redacted integration issues belong in public issues.
