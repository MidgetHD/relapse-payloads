// Loaded only after the exploit confirms elfldr, to keep the pre-exploit page
// as close to SonicIso's original as possible.
window.PAYLOAD_TILES = [
    { title: "Kstuff", description: "Load first (kstuff-lite v1.11).", name: "kstuff.elf", key: "kstuff" },
    { title: "ShadowMountPlus", description: "Load after Kstuff (1.7beta2).", name: "shadowmountplus.elf", key: "shadow" },
    { title: "etaHEN", description: "Load after Kstuff and ShadowMountPlus.", name: "etaHEN.elf", key: "etahen" },
    ...(window.PAYLOAD_TILES || []),
];
