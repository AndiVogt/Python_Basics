# HTML-Überblick

## Einführung

HTML (Hypertext Markup Language) ist die grundlegende Sprache des Webs. Sie wird verwendet, um die Struktur und den Inhalt von Webseiten zu definieren. HTML-Dokumente sind die Bausteine des World Wide Web und werden von Webbrowsern interpretiert, um die angezeigten Seiten darzustellen.

## Grundstruktur

Ein HTML-Dokument hat eine standardisierte Struktur, die aus Elementen besteht:

- `<!DOCTYPE html>`: Definiert den Dokumenttyp und HTML-Version.
- `<html>`: Das Wurzelelement, das das gesamte HTML-Dokument umschließt.
- `<head>`: Enthält Metadaten, Titel und Verweise auf externe Ressourcen wie CSS.
- `<body>`: Enthält den sichtbaren Inhalt der Webseite.

Beispiel:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Seitentitel</title>
</head>
<body>
    <h1>Überschrift</h1>
    <p>Ein Absatz.</p>
</body>
</html>
```

## Wichtige Elemente

- Überschriften: `<h1>` bis `<h6>`, wobei `<h1>` die höchste Ebene ist.
- Absätze: `<p>` für Textabsätze.
- Links: `<a href="URL">Linktext</a>` zum Verlinken von Seiten.
- Bilder: `<img src="bild.jpg" alt="Beschreibung">` für das Einbinden von Bildern.
- Listen: `<ul>` für ungeordnete und `<ol>` für geordnete Listen, mit `<li>` für Listenelemente.

## Formulare

Formulare werden mit `<form>` erstellt und enthalten Eingabeelemente wie `<input>`, `<textarea>` und `<button>`.

## Tabellen

Tabellen werden mit `<table>` erstellt und enthalten `<tr>` (Tabellenzeilen), `<td>` (Tabellenzellen) und optional `<th>` (Tabellenkopfzellen).

## Semantische HTML-Elemente

Semantische Elemente wie `<article>`, `<section>`, `<nav>`, `<header>`, `<footer>` usw. bieten eine klarere Struktur und Bedeutung für den Inhalt.

## CSS und JavaScript

- CSS (Cascading Style Sheets) wird verwendet, um das Aussehen und Layout von Webseiten zu gestalten.
- JavaScript ermöglicht interaktive Funktionen auf Webseiten.

## Verwendung von XPath in Verbindung mit HTML

XPath (XML Path Language) ist eine Sprache, um Teile eines XML-Dokuments auszuwählen. In Verbindung mit HTML kann XPath verwendet werden, um spezifische Elemente oder Knoten in HTML-Dokumenten zu lokalisieren und zu manipulieren, was besonders nützlich in der Webautomatisierung ist.

- **XPath-Ausdrücke**: XPath verwendet Pfade, um auf spezifische Elemente in einem HTML-Dokument zuzugreifen. Zum Beispiel: `//p` wählt alle `<p>`-Elemente aus.

- **Attribute auswählen**: Mit XPath können Sie auch spezifische Attribute auswählen, z.B. `//a[@href]` wählt alle Anker-Elemente mit einem `href`-Attribut.

- **Textinhalte auswählen**: XPath kann verwendet werden, um den Textinhalt von Elementen zu extrahieren, z.B. `//p/text()` gibt den Text aller `<p>`-Elemente zurück.

## Bedeutung für Webautomatisierung

HTML ist die Grundlage für Webautomatisierung, da Tools wie Selenium oder BeautifulSoup HTML-Elemente manipulieren und analysieren. XPath wird verwendet, um spezifische Elemente in einem HTML-Dokument zu lokalisieren und zu selektieren, was für die Automatisierung von Webaktivitäten wie das Ausfüllen von Formularen, das Klicken auf Links usw. wesentlich ist.

In späteren Abschnitten wird darauf eingegangen, wie XPath in Kombination mit Python für die Webautomatisierung eingesetzt wird.
