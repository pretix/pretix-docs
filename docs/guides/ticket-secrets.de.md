# Ticket-Codes

Jedes einzelne Produkt, das Sie über pretix verkaufen, hat einen Ticket-Code.
Der Ticket-Code ist eine Zeichenfolge, die als QR-Code dargestellt werden kann und als eindeutiger Identifikator dient.
Der QR-Code kann bei der Veranstaltung mit pretixSCAN gescannt werden, um ein Zutrittsticket oder einen Kaufbeleg für Merchandise zu validieren.
Standardmäßig werden Ticket-Codes nach dem Zufallsprinzip generiert.

Dieser Artikel erläutert ausführlich, wie pretix beim Generieren von Ticket-Codes standardmäßig vorgeht.
Er erklärt außerdem, wie Sie diese Vorgehensweise bei Bedarf auf eine signaturbasierte Generierung der Codes umstellen.

## Voraussetzungen

Ticket-Codes gelten auf Veranstaltungsebene, Sie müssen also zuerst eine Veranstaltung anlegen.

## Standard: Zufallsgenerierung von Ticket-Codes

Bei jedem Verkauf eines einzelnen Produkts generiert pretix einen Ticket-Code als eindeutigen Identifikator für das Produkt.
Der Ticket-Code kann als Zeichenfolge oder als QR-Code dargestellt werden.
Standardmäßig wird dieser Code nach dem Zufallsprinzip generiert und besteht aus 32 Kleinbuchstaben und Ziffern.
Um Verwechslungen vorzubeugen, werden die Zeichen `o`, `O`, `1`, `i` und `l` **nicht** verwendet.

Wenn Sie die Länge des Ticket-Codes ändern möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Tickets:.
Wählen Sie unter "Länge von Ticketcodes" eine Länge von 12 bis 64 Zeichen.

Die Verwendung von zufallsgesteuerten Ticket-Codes hat mehrere Vorteile:

 - Die Codes sind kurz und einfach zu scannen oder einzugeben.
 - Es ist unmöglich, einen gültigen Ticket-Code zu erraten oder zu fälschen.
 - Der Code bleibt auch dann unverändert, wenn sich das Produkt bei einer Umbuchung ändert.

Nach dem Zufallsprinzip erzeugte Ticket-Codes können nur durch den Abgleich mit der Datenbank validiert werden.
Das Gerät, auf dem pretixSCAN läuft, benötigt Zugriff auf eine Datenbank mit allen Ticket-Codes, die für die jeweilige Veranstaltung generiert wurden.

pretixSCAN lädt standardmäßig die gesamte Datenbank auf das Gerät herunter.
Dies ermöglicht den Wechsel in den Offline-Modus, wenn keine zuverlässige Verbindung zwischen Scangerät und Server mehr verfügbar ist.

Es gibt einige wenige Situationen, in denen dies zu Problemen führen kann:

 - Sie verkaufen mehr als 25.000 Tickets für eine einzige Veranstaltung, wodurch das Herunterladen der gesamten Datenbank auf das Scangerät zu viele Ressourcen und zu viel Zeit benötigt.
 - Sie stufen das Risiko, zusammen mit einem der Scangeräte auch die vertraulichen Daten in der Ticket-Datenbank zu verlieren,als nicht hinnehmbar ein.
 - Die Scanner arbeiten regelmäßig im Offline-Modus und die Tickets müssen unmittelbar nach dem Kauf validiert werden.
 Selbst eine Wartezeit von wenigen Minuten ist nicht akzeptabel.

Wenn mindestens eine dieser Bedingungen auf Ihre Veranstaltung zutrifft, kann es sinnvoll sein, stattdessen die signaturbasierte Generierung von Ticket-Codes zu nutzen.
Wie diese funktioniert, erfahren Sie im folgenden Abschnitt.
Für alle anderen Fälle empfehlen wir das Standardverfahren mit der Zufallsgenerierung von Ticket-Codes.

## Alternative: signaturbasierte Generierung von Ticket-Codes

!!! Hinweis
    Die signaturbasierte Generierung von Ticket-Codes ist nur für besondere Anwendungsfälle gedacht, vor allem für Veranstaltungen mit über 25.000 Tickets.
    Wenn Sie sich nicht sicher sind, ob Sie diese Funktion benötigen, dann ist das höchstwahrscheinlich nicht der Fall.

pretix bietet eine Alternative zur zufallsgesteuerten Generierung von Ticket-Codes an: ein signaturbasiertes Verfahren namens "pretix Signaturverfahren 1".
Codes, die damit generiert wurden, enthalten das Produkt, die Produktvariante und bei Veranstaltungsreihen auch den Termin.

Um Fälschungen auszuschließen, wird der Ticket-Code mit einer Ed25519-Signatur signiert.
Dadurch benötigt das Scangerät für die Ticket-Validierung weder eine aktive Verbindung zum Server, noch muss die Datenbank auf dem Gerät gespeichert werden.
pretixSCAN benötigt nur den Ticket-Code, um das Produkt zu validieren.

Das Signaturverfahren hat zwei wesentliche Nachteile:
Erstens gibt es beim Scannen im Offline-Modus deutliche Einschränkungen.
Das Scangerät hat keine Informationen zu Namen der Teilnehmer\*innen, Sitzplätzen, vorheriger Nutzung des Tickets usw.
Daher ist es auch nicht möglich, Badges zu drucken.

Zweitens muss der Ticket-Code auf eine Widerrufsliste verschoben werden und es muss ein neuer Ticket-Code generiert werden, wenn einer der wesentlichen Datenpunkte (Produkt, Variante oder Termin) geändert wurde.
Auch wenn das Produkt storniert wird, muss der Ticket-Code auf die Widerrufsliste verschoben werden.

Alle Scangeräte müssen die Widerrufsliste herunterladen.
Sie ist allerdings in der Regel deutlich kleiner als die gesamte Ticket-Datenbank.
Das ursprüngliche Produkt ist nicht mehr nutzbar, daher muss der\*die Teilnehmer\*in die aktualisierte Produktversion herunterladen.

Wenn Sie das Signaturverfahren verwenden möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Tickets:.
Wählen Sie unter "Ticket-Code-Generator" die Option "pretix Signaturverfahren 1".

## Vergleich des Verhaltens beim Scannen

| Scan-Modus                                               | Online                  | Offline                          |                                  |                                        |                                                                          |
| -------------------------------------------------------- | ----------------------- | -------------------------------- | -------------------------------- | -------------------------------------- | ------------------------------------------------------------------------ |
| ----------------------------------------------           | ----------------------- | ----------------------------     |                                  |                                        |                                                                          |
| **Einstellung für die Synchronisierung**                 | **Beliebig**            | **Bestellungen synchronisieren** |                                  | **Bestellungen nicht synchronisieren** |                                                                          |
| **Ticket-Codes**                                         | **Beliebig**            | **Zufällig**                     | **Signiert**                     | **Zufällig**                           | **Signiert**                                                             |
| Unterstützt von welchen Plattformen                      | Android, Desktop, iOS   | Android, Desktop, iOS            | Android, Desktop                 | Android, Desktop, iOS                  | Android, Desktop, iOS                                                    |
| Geschwindigkeit der Synchronisierung (große Datenmengen) |                         | langsam                          | langsam                          | schnell                                | schnell                                                                  |
| Tickets scanbar                                          | ja                      | ja                               | ja                               | nein                                   | ja                                                                       |
| Ticket nach dem Verkauf gültig                           | sofort                  | nächste Sync. (~5 Minuten)       | sofort                           | nie                                    | sofort                                                                   |
| Ein Ticket mehrfach scanbar                              | nein                    | ja, vor Daten-Sync.              | ja, vor Daten-Sync.              | n. zutr.                               | ja, immer                                                                |
| Eigene Check-in-Regeln                                   | ja                      | ja                               | ja (direkt nach Kauf beschränkt) | n. zutr.                               | ja, aber nur für Produkt, Variante und Termin, nicht für vorherige Scans |
| Name und Sitzplatz am Scanner sichtbar                   | ja                      | ja                               | ja (außer direkt nach Kauf)      | n. zutr.                               | nein                                                                     |
| Bestellungsspezifischer Check-in-Marker                  | ja                      | ja                               | ja (außer direkt nach Kauf)      | n. zutr.                               | nein                                                                     |
| Ticket-Suche nach Bestellnummer oder Name                | ja                      | ja                               | ja (außer direkt nach Kauf)      | n. zutr.                               | nein                                                                     |
| Check-in-Statistik auf Scanner                           | ja                      | ja                               | meist korrekt                    | nein                                   | nein                                                                     |
| Zusatzprodukt-Check-in mit Hauptticket möglich           | ja                      | ja                               | ja (außer direkt nach Kauf)      | nein                                   | nein                                                                     |

## Weitere Informationen

pretix unterstützt keine Generierung vom 1D-Strichcodes mit Linien.
Dies hat mehrere Gründe:

 1. Ein 1D-Strichcode mit 32 Zeichen ist zu lang, als dass er mit einem Smartphone-Bildschirm oder von einem kleinen gedruckten Ticket gescannt werden könnte.
 2. Ein 1D-Strichcode hat nicht die Redundanz eines QR-Codes, daher kann das Scannen von einem beschädigten oder schmutzigen Stück Papier fehlschlagen.
 3. Strichcode-Laserscanner funktionieren auf den meisten Smartphone-Bildschirmen nicht, daher muss ohnehin ein leistungsfähigerer Strichcode-Scanner eingesetzt werden.