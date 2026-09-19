# System Engineering & KI-Praxis (Blog)

Quellen des Blogs **System Engineering & KI-Praxis**: Praxisberichte über KI-gestützte Softwareentwicklung aus dem Systemhaus-Alltag. Die Website wird mit MkDocs Material gebaut und über GitHub Pages veröffentlicht.

Veröffentlicht unter: <https://bmarnau.github.io/blog-projekt/>

## Aufbau

| Ordner | Inhalt |
|---|---|
| `00_guidelines/` | Leitlinien: KI-Zusammenarbeit, Veröffentlichungs-Workflow, Ton und Stil |
| `01_backlog/` | Themenideen |
| `02_posts/` | Entwürfe je Beitrag (`<Jahr-Monat>_<thema>/draft.md`) |
| `docs/` | Inhalt der Website (Artikel, Themen, Über mich, interne Vorlagen) |
| `scripts/check_content.py` | Inhaltsprüfung, läuft in der CI |
| `mkdocs.yml` | Konfiguration und Navigation der Website |

## Lokal ansehen

```bash
pip install -r requirements.txt
python scripts/check_content.py
mkdocs serve
```

## Neuen Beitrag veröffentlichen

1. Entwurf in `02_posts/<Jahr-Monat>_<thema>/draft.md` schreiben.
2. Fertigen Artikel unter `docs/artikel/` ablegen und in `mkdocs.yml` unter `nav:` eintragen.
3. Nach `main` pushen. Der Workflow `.github/workflows/deploy.yml` prüft die Inhalte und veröffentlicht die Seite.

Details: [`00_guidelines/publishing_workflow.md`](00_guidelines/publishing_workflow.md).

## Lizenz

Siehe [LICENSE](LICENSE).
