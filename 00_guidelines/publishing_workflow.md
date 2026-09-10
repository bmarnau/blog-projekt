# Veröffentlichungs-Workflow (Publishing Process)

Dieser Blog nutzt **Single Source of Truth**: Das Git-Repository baut bei jedem `push` automatisch die öffentliche Website über GitHub Actions und MkDocs Material.

## 1. Einmaliges Setup auf GitHub
1. Öffne das Repo auf GitHub: `https://github.com/bmarnau/blog-projekt`
2. Navigiere zu **Settings** -> **Pages**.
3. Wähle unter **Build and deployment** -> **Source**: `Deploy from a branch`.
4. Wähle als Branch **`gh-pages`** und Ordner **`/ (root)`**.
5. Speichere die Einstellung.

## 2. Standard-Workflow für neue Beiträge
1. **Entwurf schreiben:** Erstelle einen Ordner in `02_posts/` und trage deinen Rohtext in `draft.md` ein.
2. **Inhaltsverzeichnis aktualisieren:** Trage den neuen Beitrag in der `mkdocs.yml` unter `nav:` ein.
3. **Pushen:**
   ```bash
   git add .
   git commit -m "feat: neuer Blogbeitrag zu Thema X"
   git push origin main
>>    ```
>>
>> ## 3. Einbindung in MS Teams
>> 1. Öffne den gewünschten Kanal in MS Teams.
>> 2. Klicke oben auf das **`+` (Tab hinzufügen)**.
>> 3. Wähle **Website**.
>> 4. Trage die URL `[https://bmarnau.github.io/blog-projekt/](https://bmarnau.github.io/blog-projekt/)` ein.
