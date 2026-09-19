# System Engineering & KI-Praxis (Blog)

Praxisberichte über KI-gestützte Softwareentwicklung aus dem Systemhaus-Alltag: was beim Entwickeln mit KI und Agenten funktioniert, wo es scheitert und welche Regeln daraus entstehen.

Die Website wird mit [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) gebaut und liegt unter <https://bmarnau.github.io/blog-projekt/>.

## Struktur

| Pfad | Inhalt |
| --- | --- |
| `docs/` | Quelltexte der Website (Startseite, Artikel, Themen, Über mich, interne Hinweise). |
| `mkdocs.yml` | Konfiguration und Navigation der Website. |
| `00_guidelines/` | Redaktionelle Leitlinien: Zusammenarbeit mit KI, Veröffentlichungs-Workflow, Ton und Stil. |
| `01_backlog/` | Themenideen. |
| `02_posts/` | Entwürfe neuer Beiträge, je Beitrag ein Ordner mit `draft.md`. |
| `scripts/check_content.py` | Prüft die Inhalte vor der Veröffentlichung. |
| `.github/workflows/` | CI (`ci.yml`) und Veröffentlichung (`deploy.yml`). |

## Lokal arbeiten

```bash
pip install -r requirements.txt
python scripts/check_content.py
mkdocs serve
```

Die Vorschau ist danach unter <http://127.0.0.1:8000> erreichbar.

## Veröffentlichen

Bei jedem Push auf `main` prüft der Workflow `deploy.yml` die Inhalte und veröffentlicht die Website. Den genauen Ablauf für neue Beiträge beschreibt [`00_guidelines/publishing_workflow.md`](00_guidelines/publishing_workflow.md).

## Lizenz

Siehe [LICENSE](LICENSE).
