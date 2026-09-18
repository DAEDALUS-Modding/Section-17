# Client companion plan

Section 17 ships as one server mod. Every host uploads it to the server at game start and every joining player downloads it, yet 73% of the zip is textures that only the client renders. Second Wave, Legion, Bugs, and Thorosmen each split the same kind of content into a server mod plus a hidden client companion. This document measures what a split would save for Section 17, lists three packaging defects found on the way, and proposes how to do the split in PAEIOU.

Measured against the v0.8.2 release asset `s17-server.zip` and the `main` tree at 823a58a (v0.8.3 unreleased). The "zipped" column is the sum of the zip's own per-entry compressed sizes.

## What the shipped zip contains

270 files, 29.80 MB raw, 7.46 MB zipped.

| class | files | raw MB | zipped MB |
|---|---|---|---|
| textures (papa) | 57 | 23.42 | 5.45 |
| meshes (papa) | 24 | 5.02 | 1.49 |
| animations (papa) | 15 | 0.82 | 0.28 |
| build-bar icons (60x60 png) | 22 | 0.15 | 0.15 |
| unit, ammo, and tool json | 95 | 0.16 | 0.04 |
| strategic icons (52x52 png) | 23 | 0.02 | 0.02 |
| pfx (including `.pfx.json`) | 22 | 0.17 | 0.02 |
| AI json, unit list, UI js, modinfo | 12 | 0.03 | 0.00 |

Papa files were classified by header, not by filename: bytes 8 to 25 hold nine uint16 table counts. A file with a non-zero vertex buffer, index buffer, mesh, skeleton, or model count is a mesh; otherwise a non-zero texture count makes it a texture; otherwise it is an animation. No file was ambiguous. Filename rules do not work here: `sigma_panels.papa` is a mesh and `solar_cell_idle.papa` is an animation.

## What a split saves

The proposed split follows Second Wave: textures, animations, and both icon sets go to the client companion; meshes, unit specs, pfx, AI data, `unit_list.json`, the UI scripts, and the `scenes` entry stay in the server mod.

| | files | raw MB | zipped MB |
|---|---|---|---|
| server mod today | 270 | 29.80 | 7.46 |
| server mod after split | 153 | 5.39 | 1.56 |
| client companion | 117 | 24.41 | 5.90 |

Per game, the host's upload and each joiner's download shrink by 5.9 MB (79%), and the server holds 24 MB less mod data. The companion is a one-time Community Mod Manager download, refreshed only when art changes.

If animations turn out to belong server-side (see the verification step below), the server mod is 1.84 MB zipped and the companion 5.62 MB.

## Defects in the shipped zip

Found by resolving every path the zip's json and pfx files reference against the zip itself, `pa/`, and `pa_ex1/`. All three are fixable in the source tree and should go out with the same release as the split, because the first two decide what the companion carries.

### 1. Solar Cell ships with no textures

`PAEIOU_units/solar_cell/meta.json`:

```json
{
    "model": [
        "solar_cell.papa",
        "naval/solar_cell.papa"
    ],
    ...
}
```

PAEIOU reads the key `models`, not `model` (`client_behavior` in `core.py`: `if "models" in meta: loc_models = meta["models"]`), so the list is ignored. Even with the key fixed, the second entry names `naval/solar_cell.papa` while the file, and the reference in `solar_cell.json`, is `naval/naval_solar_cell.papa`, and PAEIOU only adds `_diffuse`, `_mask`, and `_material` for a model name that the unit spec also references. Result: the zip carries the two meshes and two idle animations for the Solar Cell but none of its six texture files, so the unit renders untextured.

Fix:

```json
"models": [
    "solar_cell.papa",
    "naval/naval_solar_cell.papa"
]
```

Adds 2.10 MB raw / 0.32 MB zipped, all of it to the companion.

### 2. Ligma `ion_engine.pfx` references two papa files that never ship

`PAEIOU_units/ligma/ion_engine.pfx` names `/pa/units/paeiou/ligma/torus.papa` (twice) and `/pa/units/paeiou/ligma/torus_large.papa` as literal paths. PAEIOU copies only files named through `{...}` templates (`paeiou_substitution`), so neither papa is in the zip and the effect's mesh emitters have nothing to draw. `center_rings.pfx` in the same folder does it correctly with `{center_rings.papa}` and `{sphere.papa}`.

Fix: replace the three literal paths with `{torus.papa}` and `{torus_large.papa}`. Adds 82 KB raw / 20 KB zipped. These are meshes, so they stay in the server mod.

### 3. Floater `second_ammo.json` points at effects that do not exist

`PAEIOU_units/floater/second_ammo.json` references `/pa/units/land/tank_hover/tank_hover_ammo_hit.pfx` and `/pa/units/land/tank_hover/tank_hover_ammo_trail.pfx`. Neither file exists in `pa/` or `pa_ex1/`. The stock `tank_hover_ammo.json` uses `/pa/effects/specs/tank_light_proj.pfx` for its trail and has no `died` effect.

Fix: point the trail at `/pa/effects/specs/tank_light_proj.pfx` and either drop the `died` effect or pick a stock hit effect.

## Optional texture reductions

These are judgment calls for the maintainers. None is required for the split.

- **Ligma textures are a 2048 set**: 5.59 MB DXT5 diffuse plus two 2.80 MB DXT1 mask and material files, 11.19 MB raw and 2.86 MB zipped, which is 38% of the whole zip. Sigma, the MLA counterpart, ships a 1024 set at 0.70 MB each. Re-exporting Ligma at 1024 would save about 8.4 MB raw and 2.1 MB zipped.
- **Horntail and Poseidon mask and material files are DXT5** (349.7 KB each). Every other unit, and the stock game, use DXT1 for these (174.9 KB). About 0.7 MB raw, near zero zipped; the cost is VRAM only.
- **Two build-bar icons are 16-bit PNG with EXIF and tEXt chunks**: Energy Coil (13.5 KB) and Katrina (11.7 KB) against 4 to 8 KB for the rest. Trivial.

## Repository-side waste

The working tree is 158 MB against 30 MB shipped. Git history keeps the bytes regardless, so deleting these only shrinks checkouts; it is listed for completeness.

- 11 Blender autosaves `*.blend1`, 13.4 MB. Delete and add `*.blend1` to `.gitignore`.
- `sigma/textures_2048/`, an unused 2048 texture set, 16.0 MB.
- `big_bill/papa/`, a superseded 1024 set plus an empty 104-byte `titan_yandercannon.papa`, 2.1 MB.
- `floater/papa/` and `pineapple/papa/`, byte-identical copies of the top-level `model*.papa` files, 0.9 MB.
- `ligma/ligma.papa_noballs`, 1.0 MB.
- `naval_dcl/` (7.4 MB) has no `unit.json` and is not in `unit_add_list.txt`; `equestrian/` likewise, though tiny.
- 1920x1080 renders used only as icon sources (`*/uv_textures/icon_buildbar.png` in ten units, two `raw_img.png`, `raw_render.png`, `img_big.png`), about 13.5 MB.
- Source art (`.blend`, `.max`, `.cpt`, `.pdn`, fbx, uv, final textures), about 85 MB. Keeping it in the repo is the maintainers' call; nothing beyond the autosaves and duplicates is recommended here.

## Proposed plan

### 1. Generate two trees

PAEIOU emits one tree today: `server_behavior` is commented out and `client=True` runs the same `client_behavior`. Its README says a split is a planned capability. Until PAEIOU grows one, do the split in `call_paeiou.py` after generation into `gen/`. Both `genserver/` and `genclient/` are already in `.gitignore`.

Rule: move every `.papa` whose header has zero vertex-buffer, index-buffer, mesh, skeleton, and model counts, and every `.png`, to `genclient/` at the same relative path. Everything else stays in `genserver/`.

```python
import struct

def is_client_papa(path):
    with open(path, "rb") as f:
        counts = struct.unpack("<9H", f.read(26)[8:26])
    # strings, textures, vertex buffers, index buffers, materials,
    # meshes, skeletons, models, animations
    return not any(counts[i] for i in (2, 3, 5, 6, 7))
```

Textures, animations, and icons are consumed only by the renderer, so they are safe on the client. Meshes stay on the server because the sim reads them for bounds and placement. Offer the rule upstream to PAEIOU once it has been through a release.

### 2. Two modinfos

Server, `export/modinfo.json`: add

```json
"dependencies": ["com.pa.daedelus.experimentals.companion"],
"companions": ["com.pa.daedelus.experimentals.companion"]
```

and keep `scenes`, `context: "server"`, and priority 90.

Client, new `export_client/modinfo.json` (mirrors `pa.mla.unit.addon.companion`):

```json
{
    "identifier": "com.pa.daedelus.experimentals.companion",
    "display_name": "Section 17 - Endgame Units - Companion",
    "description": "Section 17 companion: unit textures, animations, and icons.",
    "author": "Team DAEDALUS, Quildtide, Taiga, Anonemous2, Bot, Quitch",
    "signature": "not yet implemented",
    "forum": "<same as server>",
    "priority": 110,
    "icon": "https://raw.githubusercontent.com/DAEDALUS-Modding/Section-17/main/icon.jpg",
    "titansOnly": true,
    "category": ["addon", "unit", "expansion", "titans"],
    "scenes": {},
    "context": "client",
    "dependencies": ["com.pa.daedelus.experimentals"],
    "hidden": true,
    "date": "...",
    "build": "...",
    "version": "..."
}
```

Keep the existing `daedelus` spelling in the identifier; the UI script folder is `com.pa.daedalus.experimentals` and can stay as it is.

The `forum` field currently points at `forums.planetaryannihilation.com`, which is offline. Steam or GitHub Discussions links are the current convention.

### 3. Fix the three references

Apply the fixes in the Defects section so the companion carries the Solar Cell textures and the server mod carries the Ligma tori.

### 4. Release order

Publish `s17-client.zip` and register the companion in the community mods list first, then release the server mod that depends on it. This is the order the Bug Faction split used. A server release without the companion available strips every Section 17 unit of its textures for any player who has not yet picked up the companion.

### 5. Verification

- Build both zips. Install them locally, or drop them over the CMM `download/` copies after the client has reached the start screen.
- Run an AI-vs-AI skirmish on a small map with both AIs at a high difficulty and spectate.
- Screenshot each unit textured. Watch the Ligma (ion engine tori) and the Solar Cell (both variants) in particular.
- Check the build bar and the strategic icons for every unit.
- Grep the client log for missing texture and animation errors.
- If any bone-driven weapon misbehaves with animations on the client, move animations back to the server mod (the fallback numbers above) and retest.
- Restore the release zips and `.dlmeta` files afterwards if the CMM copies were replaced.

## Consumers

GW-AI-Overhaul harvests Section 17 from the server zip only, so the split needs no change there. Its Section 17 test could list the companion alongside the server id, the way its Second Wave test lists `pa.mla.unit.addon.companion`, but nothing breaks without that.
