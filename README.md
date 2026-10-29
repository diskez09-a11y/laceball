# Laceball World Ranking

Public ranking page for the International Federation of Laceball Associations (IFLA).

- `index.html` – the finished single-page site (open it directly or host it with GitHub Pages).
- `flags/` – one SVG flag per nation (flag-icons, MIT).
- `source/` – `template.html` (page design and logic) plus the build scripts used to insert ranking data.

Each ranking date is a snapshot in the page's `SNAPSHOTS` list, newest first. To publish a new ranking, add a snapshot at the top; points, order and +/- movement are computed in the page.
