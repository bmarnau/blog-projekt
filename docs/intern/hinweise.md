# Hinweise und Entscheidungen

!!! warning "Öffentlich erreichbarer Arbeitsbereich"
    „Intern“ bedeutet hier: redaktioneller Arbeitsbereich. Da der Blog über GitHub Pages veröffentlicht wird, bietet diese Seite keinen Zugriffsschutz. Vertrauliche Informationen gehören nicht hierher.

Auf dieser Seite werden Empfehlungen, offene Entscheidungen und Arbeitsregeln für den Blog gesammelt. So bleiben sie an einer Stelle auffindbar und können später bewusst bestätigt, geändert oder verworfen werden.

## Positionierung

**Arbeitsfassung:**

> Ein Praxisblog über KI-gestützte Softwareentwicklung aus Sicht eines System Engineers – mit echten Fehlern, nachvollziehbaren Entscheidungen und wiederverwendbaren Regeln.

**Zielgruppe:** IT-Administratoren, Trainer und System Engineers, die mit KI erste Softwarelösungen bauen, aber keine klassische Entwicklerlaufbahn haben.

## Inhaltliche Leitlinien

- Ein Artikel beginnt mit einem konkreten Problem oder einer konkreten Frage.
- Eigene Beobachtungen werden von Vermutungen und allgemeinen Aussagen getrennt.
- Fehler und Irrwege dürfen sichtbar bleiben, sofern daraus eine belastbare Erkenntnis entsteht.
- Fachbegriffe werden beim ersten Auftreten kurz erklärt.
- Die Artikellänge folgt dem Inhalt; 300–500 Wörter sind ein Richtwert, keine Grenze.
- Jeder Artikel liefert mindestens eine übertragbare Regel, Checkliste oder Entscheidungshilfe.

## Empfohlener Artikelaufbau

1. Ausgangslage
2. Was konkret passiert ist
3. Woran der Fehler erkennbar war
4. Warum das System so reagiert hat
5. Was geändert wurde
6. Die daraus entstandene Regel
7. Checkliste für Leser

## Sprachliche Leitlinien

- direkt, sachlich und pragmatisch,
- kurze Absätze und aussagekräftige Zwischenüberschriften,
- kein Marketing-Sprech und keine künstliche Dramatisierung,
- konkrete Verben statt abstrakter Substantivketten,
- Unsicherheit offen benennen,
- deutsch schreiben; etablierte englische Fachbegriffe nur verwenden, wenn sie präziser sind.

## Zusammenarbeit mit KI

### Klare Rollenverteilung

Der Autor liefert den erlebten Vorfall, die fachliche Einordnung, die Bewertung und die eigentliche Erzählstimme. Der Text soll erkennbar in seinen Worten entstehen.

KI übernimmt eine unterstützende Rolle. Sie darf:

- logische Lücken und unklare Begriffe markieren,
- Gedanken sortieren und alternative Gliederungen vorschlagen,
- Rückfragen stellen, wenn ein Zusammenhang für Leser nicht nachvollziehbar ist,
- Sprache und Rechtschreibung redaktionell prüfen, ohne den Text in einen fremden Stil umzuschreiben,
- Bilder, Zeichnungen, Diagramme und andere visuelle Erklärungen vorbereiten,
- technische Annahmen zur Überprüfung kennzeichnen.

KI darf keine Passagen als vermeintliche persönliche Erfahrung verfassen und keine nicht erlebten Vorfälle, Messergebnisse oder Quellen erfinden. Vor einer Veröffentlichung bestätigt der Autor alle fachlichen Aussagen und entscheidet über jede sprachliche Änderung.

### Abgrenzung zu Relingit

Bei [„Die Fahrt zum Kunden“](https://berndmarnau.de/relingit/) wurde KI erfolgreich als kreativer Partner für eine fiktionale Geschichte und deren Veröffentlichung eingesetzt. Im Blog ist ihre Rolle enger gefasst: strukturelle und redaktionelle Unterstützung sowie die Erstellung von Bildern und Zeichnungen. Diese Unterscheidung soll gegenüber den Lesern transparent bleiben.

## Gestaltung

- Die öffentliche Navigation bleibt auf Start, Artikel, Themen und Über mich konzentriert.
- Der Arbeitsbereich wird optisch und sprachlich als solcher gekennzeichnet.
- Textbreite und Kontrast haben Vorrang vor Dekoration.
- Screenshots und Diagramme müssen eine konkrete Erklärung unterstützen.
- Codebeispiele erhalten Kontext: Zweck, relevante Stelle und Ergebnis.
- Hinweisblöcke verwenden einheitliche Rollen: Fehlerbild, Ursache, Praxisregel und Werkstattstatus.

## Reichweite

- Jeder Titel beschreibt ein konkretes Problem oder Ergebnis.
- Neue Beiträge werden aktiv in passenden Teams-Kanälen, Schulungen oder beruflichen Netzwerken geteilt.
- Ein verlässlicher Rhythmus ist wichtiger als hohe Frequenz.
- Autor, Erfahrungshintergrund und Einsatz der KI bleiben transparent.
- Später ergänzen: RSS, Suchmaschinen-Anmeldung und eine einfache, datenschutzfreundliche Reichweitenmessung.

## Technische Entscheidungen

- MkDocs Material bleibt zunächst die Basis.
- Nur veröffentlichbare Seiten liegen unter `docs/`.
- Entwürfe und Redaktionsdateien bleiben außerhalb von `docs/`.
- Die Website wird aus Git gebaut und über GitHub Pages bereitgestellt.
- Bei jedem Push und Pull Request prüft die CI Navigation, lokale Links, Bilder und die H1-Struktur aller Seiten.
- Der MkDocs-Build läuft im strengen Modus; Warnungen verhindern damit die Veröffentlichung.
- Abhängigkeiten sind fest versioniert, damit CI und Deployment dieselbe Werkzeugversion verwenden.
- Vor jeder Veröffentlichung werden zusätzlich die mobile Darstellung und wichtige Seiten im Browser geprüft.

## Offene Entscheidungen

- Soll der Arbeitsbereich dauerhaft öffentlich sichtbar bleiben oder später in ein privates Repository umziehen?
- Soll der Blog langfristig unter einer eigenen Domain erscheinen?
- Welche zwei bis drei Themenreihen sollen den roten Faden bilden?
- Welche reale Information kann den ersten Artikel zu den 4.000 Lint-Fehlern belegen?

## Änderungsprotokoll

| Datum | Entscheidung |
| --- | --- |
| 10.09.2026 | Positionierung geschärft und Zielgruppe festgelegt |
| 10.09.2026 | Öffentliche Navigation von internen Arbeitsunterlagen getrennt |
| 10.09.2026 | Artikellänge als Richtwert statt starre Grenze definiert |
| 10.09.2026 | Transparente Beschreibung der KI-Unterstützung eingeführt |
| 10.09.2026 | Rollenverteilung präzisiert: eigene Worte des Autors, KI für Struktur, Redaktion und Visualisierung |
| 10.09.2026 | Automatische CI-Prüfung für Inhalte, Links, Navigation und Website-Build ergänzt |
