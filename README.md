# Laceball World Ranking

Public ranking site for the International Federation of Laceball Associations (IFLA).

- `index.html` – the ranking table (open it directly or host it with GitHub Pages). `index.html#Japan` opens on a nation.
- `map.html` – world map of member nations shaded by ranking; non-members are blacked out. Click a nation for its card (rank, points, movement, fixtures). `map.html#Japan` opens zoomed on a nation.
- `data.js` – ranking snapshots, flags, regions and the fixture list. Both pages read it, so update rankings here.
- `world.js` – pre-projected world outline for the map (Natural Earth 1:50m, public domain).
- `flags/` – one SVG flag per nation (flag-icons, MIT).
- `source/` – `template.html` (ranking page design and logic) plus the build scripts.

Each ranking date is a snapshot in `SNAPSHOTS` in `data.js`, newest first. To publish a new ranking, add a snapshot at the top; points, order and +/- movement are computed in the pages.

Fixtures go in `FIXTURES` at the bottom of `data.js`, e.g. `{ date: '2026-11-14', home: 'France', away: 'Spain', venue: 'Paris', comp: 'Friendly' }`. The map shows each nation's upcoming ones; nations with none show TBD.
