# relapse

PS5 WebKit + kernel exploit chain (relapse / aio), firmware **7.00 - 13.60**.

Retail and testkit build. Devkits want the [relapse-dev](https://github.com/soniciso1/relapse-dev) build instead.

Open the page on the console and let it run. A successful run draws the payload menu
in place and sends each ELF through the console'"'"'s own syscalls to `127.0.0.1:9021`,
so no server-side support is needed and this works from any static host.

Supported: 7.00, 7.01, 7.20, 7.40, 7.60, 7.61, 8.00, 8.20, 8.40, 8.60, 9.00, 9.20,
9.40, 9.60, 10.00, 10.01, 10.20, 10.40, 11.00, 11.20, 11.60, 12.00, 12.02, 12.20,
12.40, 12.60, 12.70, 13.00, 13.20, 13.40, 13.42, 13.60.

10.60 and 11.40 are absent: those firmware images are missing the modules the offsets
have to be read out of.

`elf.html` is a standalone payload menu for the already-jailbroken case. It needs a
host that runs code and can reach the console (`api/` ships PHP and node handlers),
so it does not work on GitHub Pages - use the run page's own menu there.

## Payloads added in this fork

Open `https://midgethd.github.io/relapse-payloads/` on the PS5. Once the exploit
reports `elfldr is up on 127.0.0.1:9021`, use the on-page menu to send Kstuff,
ShadowMountPlus, then etaHEN in that order. The page sends each ELF from the
console to its own loader; GitHub Pages only serves the files.

| Menu item | File | Source | SHA-256 |
| --- | --- | --- | --- |
| Kstuff | `payloads/kstuff.elf` | [kstuff-lite v1.11 mirror](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/kstuff-lite_v1.11.elf) | `ab9a6cb4d3b1daf139d4d646e402b1cf569071acd64599c936d7a3a6164dc779` |
| ShadowMountPlus | `payloads/shadowmountplus.elf` | [ShadowMountPlus 1.7beta2 mirror](https://github.com/itsPLK/ps5-payloads-mirror/releases/download/payloads-mirror/ShadowMountPlus_1.7beta2.elf) | `3f716a7b2220c7e87e87452ae05cad689ef842d3beb4cdad6c526cb6dfc2b6b5` |
| etaHEN | `payloads/etaHEN.elf` | User-supplied ELF from an etaHEN community post | `8ce5ab4eaff10679920bf7397bb081ca9c18aa159d134cae8f1af3a4290b91b6` |

These payloads come from separate projects: [kstuff-lite](https://github.com/EchoStretch/kstuff-lite),
[ShadowMountPlus](https://github.com/drakmor/ShadowMountPlus), and
[etaHEN](https://github.com/etaHEN/etaHEN). Their compatibility with firmware
13.40 has not yet been confirmed by a successful run of all three on the PS5.
