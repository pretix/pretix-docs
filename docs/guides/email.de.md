# E-Mail-Einstellungen

pretix gibt Ihnen viele Optionen, um Kund\*innen und Teilnehmende per E-Mail zu kontaktieren – auf Veranstalter- und Veranstaltungsebene.
Sie können dazu den vom System bereitgestellten E-Mail-Server oder den Ihres Unternehmens verwenden.
pretix stellt zahlreiche vorkonfigurierte E-Mail-Nachrichten bereit, die Sie an Ihre Anforderungen anpassen können.
Dieser Artikel erläutert, wie Sie die für den E-Mail-Server gewünschte Lösung in pretix einrichten und wie Sie E-Mail-Inhalte anpassen.

## Voraussetzungen

Ihr Konto muss aktiviert sein, damit Sie pretix zum Versand von E-Mails nutzen können.
Weitere Informationen finden Sie im Tutorial-Abschnitt zur [Aktivierung des Kontos](../tutorial/single-events/organizer-account.md#activation).

## Anleitung

### Allgemeine E-Mail-Einstellungen

Standardmäßig werden die allgemeinen E-Mail-Einstellungen auf Veranstalterebene verwaltet.
Navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → E-Mail:.
Klicken Sie den Button :btn-icon:fa3-edit: Bearbeiten: neben "Versandmethode" und wählen Sie eine der folgenden drei Optionen:

 1. **System-Standard benutzen:** der vom System bereitgestellte E-Mail-Server.
 pretix versendet E-Mails von der Adresse `noreply@pretixmail.com`.
 Bei E-Mails zur Registrierung eines Kund\*innenkontos, zum Ändern der Mail-Adresse und zum Zurücksetzen des Passworts ist im Namensfeld der Name Ihres Veranstalterkontos eingetragen.
 Bei allen anderen E-Mails steht im Namensfeld der Name der Veranstaltung.
 Als Antwortadresse dient die Kontaktadresse Ihres Veranstalters.
 Wenn Sie die Antwortadresse ändern möchten, navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Allgemein:, ändern Sie den Eintrag bei "Kontakt-E-Mail" und klicken Sie den Button :btn:Speichern:.
 2. **Eigene Absendeadresse mit System-Mailserver benutzen:** der vom System bereitgestellte E-Mail-Server.
 pretix versendet E-Mails von einer individuell festgelegten Adresse.
 Dazu müssen Sie dem SPF-Eintrag Ihres Mailservers den pretix-Anwendungsserver hinzufügen (siehe [Den E-Mail-Server des Systems mit einer individuellen Absendeadresse verwenden](email.md#den-e-mail-server-des-systems-mit-einer-individuellen-absendeadresse-verwenden) unten).
 3. **Eigenen SMTP-Server verwenden:** Sie verwenden den SMTP-Server Ihres Unternehmens und können Ihre E-Mails vollständig individuell gestalten.

Wenn Sie die allgemeinen E-Mail-Einstellungen für eine bestimmte Veranstaltung ändern möchten, können Sie diese Einstellungen für diese Veranstaltung entsperren.
Das Entsperren der Einstellungen kann nicht rückgängig gemacht werden.
Sobald sie einmal entsperrt sind, wirken sich Änderungen an den E-Mail-Einstellungen für Ihren Veranstalter nicht mehr auf die Einstellungen für die betreffende Veranstaltung aus.
Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → E-Mail: und klicken Sie die Buttons :btn-icon:fa3-unlock: Entsperren: wie erforderlich.

### Den E-Mail-Server des Systems mit einer individuellen Absendeadresse verwenden

Wenn Sie eine E-Mail-Adresse mit Ihrer eigenen Domain als Absendeadresse verwenden und keinen eigenen SMTP-Server nutzen, müssen Sie den pretix-Anwendungsserver zu Ihrem SPF-Eintrag hinzufügen.
Dies ist notwendig, damit andere E-Mail-Anbieter Ihre E-Mails nicht fälschlicherweise als Spam einstufen.

Sie können in der Verwaltungskonsole des Anbieters, über den Ihre Domain läuft, einen SPF-Eintrag hinzufügen.
Die genaue Vorgehensweise ist von Provider zu Provider unterschiedlich.
Die Einstellungen befinden sich meist auf einer Seite mit dem Namen "DNS-Einträge" oder ähnlich.

Wenn Sie unseren Hosting-Dienst unter pretix.eu nutzen, können Sie Ihren SPF-Eintrag mit den folgenden Angaben ergänzen:

`include:_spf.pretix.eu`

Ein vollständiger Eintrag kann zum Beispiel so aussehen:

`v=spf1 a mx include:_spf.pretix.eu ~all`

Informationen zur korrekten Implementierung finden Sie in der [SPF-Spezifikation](http://www.open-spf.org/SPF_Record_Syntax/).

Wenn Sie Ihre E-Mails mit DKIM authentifizieren möchten, richten Sie für die Subdomain `pretix._domainkey` einen `CNAME`-Eintrag mit dem Ziel `dkim.pretix.eu` ein:

`pretix._domainkey.meinedomain.de. CNAME dkim.pretix.eu.`

Um DKIM für Ihre Domain auf unseren Mail-Servern zu aktivieren, wenden Sie sich an unser Support-Team.

Wenn Sie viele E-Mails auf einmal verschicken, verlangen E-Mail-Anbieter wie Google Mail außerdem, dass Sie eine DMARC-Richtlinie haben.
Eine DMARC-Richtlinie `p=none` genügt.

### E-Mail-Inhalte anpassen

Wenn Sie den Inhalt Ihrer E-Mails zur Registrierung eines Kund\*innenkontos, zum Ändern der Mail-Adresse und zum Zurücksetzen des Passworts anpassen möchten, navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → E-Mail: und wechseln Sie zum Reiter :btn:E-Mail-Inhalt:.
Die E-Mails für alle anderen Zwecke passen Sie auf Veranstaltungsebene an.

Wenn Sie den Inhalt Ihrer E-Mails zu Bestellungen, gekauften Produkten und Zahlungen anpassen möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → E-Mail: und wechseln Sie zum Reiter :btn:E-Mail-Inhalt:.
E-Mails rund um Kund\*innenkonten werden auf Veranstalterebene verwaltet.

Die folgende Tabelle enthält eine Liste aller verfügbaren Platzhalter und ihrer Funktionen sowie Beispiele.
Nicht alle Platzhalter sind für alle E-Mail-Typen verfügbar.
Die jeweils verfügbaren Platzhalter sind im Backend unterhalb der Felder für Betreff und Text der E-Mails aufgeführt.

| Platzhalter                        | Funktion                                                                                                       | Beispiel            |
|------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------|
| `{attendee_name}`                  | Name des/der teilnehmenden Person, für die das Ticket gilt                                                     | Jordan Doe |
| `{code}`                           | Bestellnummer **oder** Gutscheincode für die Warteliste                                                        | F8VVL **oder** 68CYU2H6ZTP3WLK5 |
| `{comment}`                        | Grund für die Ablehnung oder die Stornierung einer Bestellung                                                  | Hier können Sie eine eigene Begründung einfügen. |
| `{currency}`                       | Dreibuchstabiger Code der Währung für diese Veranstaltung                                                      | EUR |
| `{event}`                          | Name der Veranstaltung                                                                                         | Tutorial-Konferenz |
| `{event_admission_time}`           | Einlasszeit für die Veranstaltung                                                                              | 18:00 |
| `{event_location}`                 | Veranstaltungsort                                                                                              | Berthold-Mogel-Straße 1 |
| `{event_slug}`                     | Kurzform der Veranstaltung                                                                                     | tutcon27 |
| `{expire_date}`                    | Ablaufdatum für die Bestellung                                                                                 | 2024-11-13 |
| `{hours}`                          | Anzahl der Stunden, in denen der Gutscheincode für die Warteliste eingelöst werden kann                        | 48 |
| `{invoice_company}`                | Unternehmen für die Rechnungsadresse                                                                           | Beispiel AG |
| `{invoice_name}`                   | Name für die Rechnungsadresse                                                                                  | Jordan Doe |
| `{name}`                           | Beliebige Anrede des Empfängers/der Empfängerin (z. B. Name der Rechnungsadresse, Name des ersten Tickets)     | Fr. Doe |
| `{name_family_name}`               | Nachname des Empfängers/der Empfängerin                                                                        | Doe |
| `{name_for_salutation}`            | Wunsch-Anrede, -Titel, -Name                                                                                   | Dr. Jordan Doe |
| `{name_given_name}`                | Vorname des Empfängers/der Empfängerin                                                                         | Jordan |
| `{order_modification_deadline_date_and_time}` | Uhrzeit und Datum bis zu denen die Bestellung geändert werden kann                                  | 4. Juni 2027, 18:00 |
| `{orders}`                         | Liste von Bestellungen einschl. Links zu Statusseiten, individuell für die E-Mail für "Link erneut senden (vom Benutzer beantragt)" |  • TUTCON27-F8VVL - https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/open/abcdefghi/ <br> • TUTCON27-HIDHK - https://pretix.eu/tut/tutcon27/order/HIDHK/98kusd8ofsj8dnkd/open/jklmnopqr/ <br> • TUTCON27-OPKSB - https://pretix.eu/tut/tutcon27/order/OPKSB/09pjdksflosk3njd/open/stuvwxy2z/ |
| `{organizer}`                      | Name des Veranstalters                                                                                         | Tutorial Ltd. |
| `{payment_info}`                   | Angaben zur Zahlungsmethode (z. B. Bankverbindung)                                                             | Dieser Betrag wurde Ihrer Karte belastet. |
| `{product}`                        | Das Produkt, das jetzt auf der Warteliste zur Verfügung steht                                                  | Ermäßigtes Ticket |
| `{refund_amount}`                  | Bei E-Mails zu abgesagten Veranstaltungen der Erstattungsbetrag mit Währung                                    | 42,23 € |
| `{subevent}`                       | Die betreffende Veranstaltung in einer Veranstaltungsreihe                                                     | Tutorial-Konferenz |
| `{subevent_date_form}`             | Das Datum der betreffenden Veranstaltung in einer Veranstaltungsreihe                                          | 4. Juni 2027, Mitternacht |
| `{total}`                          | Gesamter Rechnungsbetrag für die Bestellung                                                                    | 42,23 |
| `{total_with_currency}`            | Gesamter Rechnungsbetrag für die Bestellung mit länderspezifischem Währungssymbol                              | 42,23 € |
| `{url}`                            | Veranstaltungsebene: URL der Download-/Statusseite der Bestellung **oder** Veranstalterebene: URL zur Kontoaktivierung | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/open/98kusd8ofsj8dnkd/ **oder** https://pretix.eu/tut/account/activate?token=RAW71yeKrZiYgQCxh7DLLmoQbJePha |
| `{url_cancel}`                     | URL der Seite zur Stornierung der Bestellung                                                                   | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/cancel |
| `{url_info_change}`                | URL der Seite mit Ticketinformationen zur Bestellung                                                           | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/modify |
| `{url_products_change}`            | URL zur Seite mit den Produkten in der Bestellung                                                              | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/change |
| `{url_remove}`                     | URL zum Austragen aus der Warteliste                                                                           | https://pretix.eu/tut/tutcon27/waitinglist/remove?voucher=68CYU2H6ZTP3WLK5 |

Klicken Sie den Reiter :btn-icon:fa3-tv: Vorschau:, um eine Vorschau der E-Mail zu sehen, in der die Platzhalter durch Beispielangaben ersetzt werden.
Wenn Sie einen Platzhalter verwendet haben, der für diese Art von E-Mail nicht verfügbar ist, sehen Sie eine Fehlermeldung mit dem Text "Ungültiger Platzhalter: {platzhalter}".

Die E-Mail "Kostenlose Bestellung" wird verschickt, wenn die Bestellung ausschließlich kostenlose Produkte enthält.
Die E-Mail "Getätigte Bestellung" wird verschickt, wenn der Rechnungsbetrag für eine Bestellung größer als null ist.
Die E-Mail "Bezahlte Bestellung" wird verschickt, wenn die Zahlung für eine Bestellung verbucht ist.
Je nach Zahlungsmethode kann diese E-Mail unmittelbar nach der E-Mail "Getätigte Bestellung" verschickt werden.

### E-Mails manuell verschicken

Alle der oben beschriebenen E-Mail-Einstellungen sind mit bestimmten Aktionen im pretix-Backend verknüpft.
Darüber hinaus können Sie aber auch zu selbstgewählten Zeitpunkten E-Mails verschicken.

Wenn Sie eine E-Mail sofort verschicken möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-envelope: E-Mails verschicken → E-Mails verschicken:.
Wenn Ihre E-Mail eine Warteliste betrifft, wählen Sie :btn:Warteliste:.
Wenn Ihre E-Mail für Aussteller relevant ist, wählen Sie :btn:Aussteller:.
Diese Option wird nur angezeigt, wenn die Erweiterung "Aussteller" aktiviert ist.
Wählen Sie in allen anderen Fällen :btn:Bestellungen oder Teilnehmer\*innen:.

Sie können anhand von Produkt, Bestellstatus, Zeitpunkt der Bestellung und Check-in-Status weiter einschränken, wer eine E-Mail erhält.
Den Betreff und den Mailtext können Sie mit eigenen Texten und Platzhaltern gestalten.
Sie können Tickets, Kalendereinträge und andere Dateien anhängen.
Wenn der Inhalt der E-Mail Ihren Vorstellungen entspricht, klicken Sie :btn:E-Mail-Vorschau:.
Der Button ":fa3-send: Absenden" zeigt die Anzahl der in Frage kommenden Empfänger\*innen an.
Auf der Vorschauseite können Sie die Einstellungen noch einmal überprüfen und anschließend den Button :btn-icon:fa3-send: Absenden (# passende Bestellungen): klicken.

Wenn die E-Mail zu einem bestimmten späteren Zeitpunkt verschickt werden soll, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-envelope: E-Mails verschicken → Geplante E-Mails:.
Diese Seite zeigt eine Liste aller Regeln für geplante E-Mails an.
Um eine neue Regel hinzuzufügen, klicken Sie den Button :btn:Neue Regel erstellen:.
Legen Sie Inhalt, Empfänger\*innen sowie Datum und Uhrzeit für den Versand der E-Mail fest.
Für Datum und Uhrzeit können Sie einen festen Zeitpunkt angeben oder den Zeitpunkt relativ zum Beginn oder Ende der Veranstaltung festlegen.