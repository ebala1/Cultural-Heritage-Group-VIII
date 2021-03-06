### Cultural-Heritage-Group-VIII

**Projektbeschreibung:**

Unser Projekt beschäftigt sich mit der Identifizierung von den geschlechtsspezifischen 
(seien es physische oder nach Möglichkeit auch andere Auffälligkeiten wie Kleidung, Werkzeuge etc.)
Merkmalen und der automatischen Zuordnung von Figuren zu den Kategorien: männlich, weiblich, weder noch (nicht feststellbar).
Für diese Aufgabe haben wir uns die Programmierbibliothek OpenCV und deren Funktionen angeschaut. 
Diese umfassen beispielsweise das maschinelle Lernen auf Basis von sogenannter Haar Cascades, angelehnt an die Viola-Jones-Methode. 
Letztere ist eine effiziente mathematische
Methode, die zur Mustererkennung in digitalen Bildern verwendet wird. Haar Cascades sind
Klassifizierer, die darauf trainiert werden können, bestimmte Objekte zu erkennen.
Diese sind frei verfügbar, können aber auch mittels eigener Bilder und Aufnahmen für spezifische Zwecke erstellt werden.

**Projekt - Features:**

- **Sprache:** *Python* (evtl. auch *C++*)

- **Framework:** *OpenCV*

- **Navigation/Menü:** Menü besteht aus Bildauswahl, Auswahl des Users soll auf Merkmale durch das Programm untersucht werden 

- Ausgabe: Analyse ergab Kategorie x aufgrund der Attribute y

- es soll eine Rückfrage erfolgen, ob noch ein Bild ausgegeben werden soll, andernfalls soll das Programm beendet werden

 - **Extras:** lustige Überschriften/"Stories" zu ausgewählten Bildern


**Sitzung 03 (25.04.2018): Planung / Aufgabenverteilung**

- OpenCV downloaden!

- Bilder (Rohdaten) ZIP-Datei downloaden

- Bilder bearbeiten: 

Im Bilder-Ordner (siehe oben oder die ZIP-Datei von der Seminarseite runterladen) sind die Bilder der Felsenmalerei im Ordner *image-raw*.

Bis zur nächsten Woche:
1. Einzelne Personen aus den Bildern herausschneiden.

2. Alle bearbeiteten Bilder in den Ordner: "images-edited" kopieren.

3. Diese Bilder nochmal manuell nach "female", "male" oder "human/undefined" sortieren und im Ordner "images-gender" ablegen


**Sitzung 04 (02.05.2018)**

- Gemeinsam die Bilder kurz durchgehen 

- Datenbank anlegen, mit Merkmalen die eindeutig zeigen, was als weiblich, männlich oder human bezeichnet werden kann


**Roadmap - Vorhaben über die nächsten vier Wochen:**

 - User Interface aufbauen 
 - Bilder zur Analyse auswählen
 - zwei Bilder einlesen lassen (Stereotypen: männlich/weiblich) ->Vergleich mit der Datenbank -> Ausgabe der Differenz in Prozent Bestimmung des Geschlechts 


**Aufgabenverteilung:**

- Maria : GUI --> Implementierung folgt noch
- Ebru, Frederike & Merve: Code für Bilder einlesen & vergleichen
- Iris: Code für die Prozentausgabe


**Links zu den Bildern**

*Images-Edited:*
 
 [![Images-Edited|Google Drive](https://image.ibb.co/eRFVon/google_drive_logo.jpg)](https://drive.google.com/open?id=1KkN06yyineu1V6Q8mkar38t0XHAABS8t)

*Images-Gender:*

[![Images-Gender|Google Drive](https://image.ibb.co/eRFVon/google_drive_logo.jpg)](https://drive.google.com/open?id=1yHSwLRjFWr03dvh_SYK67EFnmbd90YbN)


**Links zu den Tutorials**

*Bilder Vergleichen mit dem Ergebnis True oder False:*

[![Tutorial|YouTube](https://cdn.iconscout.com/public/images/icon/free/png-128/youtube-logo-social-media-3f4643d91d60144c-128x128.png)](https://www.youtube.com/watch?v=T5pRlIbr6gg)

[![Tutorial|YouTube](https://cdn.iconscout.com/public/images/icon/free/png-128/youtube-logo-social-media-3f4643d91d60144c-128x128.png)](https://www.youtube.com/watch?v=LNzC4NYYWdg)

[![Tutorial|YouTube](https://cdn.iconscout.com/public/images/icon/free/png-128/youtube-logo-social-media-3f4643d91d60144c-128x128.png)](https://www.youtube.com/watch?v=KDxLJ6GrSwI)


*Python/Tkinter: GUI*

[![Tutorial: Python/GUI|YouTube](https://cdn.iconscout.com/public/images/icon/free/png-128/youtube-logo-social-media-3f4643d91d60144c-128x128.png)](https://www.youtube.com/watch?v=RJB1Ek2Ko_Y)










