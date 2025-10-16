# eakte_reorder

> Die Geschäftstätigkeit der Verwaltung folgt dem Grundsatz der Schriftlichkeit. Sie besteht im Erstellen, Versenden, Empfangen und Registrieren von Dokumenten (Aktenbildung) und wird durch die Aktenführung unterstützt. Die Aktenführung sichert ein nachvollziehbares transparentes Verwaltungshandeln und ist Voraussetzung für eine sachgerechte Archivierung — *[§ 2 der Registraturrichtlinie des Bundes (vergleichbare Regelungen in den Ländern)](https://www.bmi.bund.de/SharedDocs/downloads/DE/veroeffentlichungen/themen/ministerium/registraturrichtlinie.pdf?__blob=publicationFile&v=8)*

## Hindergrund

Traditionell werden Akten in der Justiz so geführt, dass jeder Posteingang mehr oder weniger chronologisch abgeheftet wird. Die Dokumente in der Akte werden anschließend seitenweise foliiert, d. h., jedes einzelne Blatt erhält oben rechts eine fortlaufende Ziffer. Diese Ziffer ist üblicherweise innerhalb der gesamten Akte einmalig. Eine Ausnahme stellen lediglich einige Behörden dar, die jeden Band einer Akte beginnend mit "1" neu nummerieren. Die Foliierung ermöglicht es unter anderem, die Reihenfolge der Aufnahme der Schriftstücke in die Akte genau nachzuvollziehen, z. B. bei der Entnahme einzelner Blätter. Es kommt auch vor, dass auf bereits eingeordneten Seiten im Nachhinein handschriftliche Vermerke angebracht, also ergänzt und so verändert werden. Solche Änderungen lassen sich in der physischen Akte nachvollziehen, zumal sie in der Regel mit einem Datum und einer Unterschrift versehen sind. 

In der Justiz hält die elektronische Akte zunehmend Einzug und wird Rechtsanwältinnen und Rechtsanwälten über Akteneinsichtsportale zur Verfügung gestellt. Im zentralen Akteneinsichtsportal gibt es zwei Möglichkeiten, die Dateien herunterzuladen: Einerseits gibt es eine einzelne PDF-Datei, die den (unterstellten) gesamten Datenbestand abbildet, und andererseits — je nach Verfügbarkeit — eine ZIP-Datei, die aus mehreren PDF-Dokumenten besteht. In dieser ZIP-Datei ist jedes Dokument (zum Beispiel ein Beschluss, eine Vernehmung oder ein Vermerk) als separate Datei abgelegt.

In einer elektronischen Akte ist mir aufgefallen, dass im „Gesamt-PDF” mehrfach die Blattzahl „1” vorkam. Es sah so aus, als wären mehrere Dateien nach der Nummerierung der Seiten zusammengeführt worden. Nachdem ich die einzelnen PDF-Dateien anhand des Änderungsdatums sortiert hatte, ergab sich eine komplett andere Reihenfolge. Es ist unklar, inwiefern und aus welchem Grund ein Dokument verändert wurde. Eine Verfälschung möchte ich nicht unterstellen. Konkret ergab sich in der elektronischen Akte, in der mir dieses Problem aufgefallen ist, nach der Neusortierung Folgendes: Im von der Behörde zur Verfügung gestellten Gesamtdokument war die erste relevante Seite eine Strafanzeige, die das Datum 25.07.2025 trägt. Diese war mit der Blattzahl „1” versehen. Nach der Sortierung anhand des Änderungsdatums war die erste relevante Seite jedoch eine E-Mail, die im Text das Datum 28.07.2025 ausweist und die die Seitenzahl „13” trägt. **Es ist nicht nachvollziehbar, warum das PDF-Dokument, das aus der E-Mail vom 28. Juli 2025 erstellt wurde, ein Änderungsdatum aufweist, das vor dem auf der Strafanzeige ausgewiesenen Datum liegt.**

Die Änderungszeitpunkte in ihrer Reihenfolge lassen *teilweise* auf einen automatisierten Vorgang schließen:

```
2025-07-28 18:15:18+02:00
2025-07-28 18:15:19+02:00
2025-07-28 18:15:19+02:00
2025-07-28 18:15:19+02:00
2025-07-28 18:15:20+02:00
…
2025-07-29 10:47:50+02:00
2025-07-29 10:47:50+02:00
2025-07-29 11:01:36+02:00
2025-07-29 12:05:31+02:00
…
2025-09-10 14:44:17+02:00
2025-09-11 10:19:28+02:00
2025-09-16 12:53:03+02:00
2025-09-16 12:53:05+02:00
```

Diese fehlende Transparenz beeinträchtigt sowohl die Übersichtlichkeit als auch die Verlässlichkeit der Aktenführung und ist m. E. ein wesentliches Problem. Aktuell ist es nicht möglich, sich einen sachgerechten Überblick über die Entstehungsgeschichte und die "Entwicklung" einer Akte zu verschaffen. Der Grundsatz „Aktenklarheit und Aktenwahrheit” ist damit verletzt.

## Zum Skript

Das Skript entpackt die ZIP-Datei (bitte in „zipped.zip“ umbenennen, oder den Dateinamen anpassen) und führt die einzelnen Dateien zusammen, und zwar in der chronologischen Reihenfolge des Änderungsdatums (Modification Date, „mdate“), wie es in den Metadaten der jeweiligen PDF-Datei gespeichert ist.
