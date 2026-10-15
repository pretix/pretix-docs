# PayPal

PayPal ist eine der zahlreichen Möglichkeiten, in pretix Zahlungen abzuwickeln.
Sie können PayPal für folgende Zahlungsmethoden einsetzen:
Echtzeitzahlung über ein PayPal-Konto, "Jetzt kaufen, später bezahlen" mit PayPal-Konto, SEPA-Bankeinzug und alternative Zahlungsmethoden wie EPS, iDEAL und andere.

Dieser Artikel erklärt, wie Sie Ihr PayPal-Konto verknüpfen, um darauf Zahlungen über pretix zu empfangen.

## Voraussetzungen

Zahlungsdienstleister richten Sie auf Veranstaltungsebene ein, Sie müssen also zuerst eine Veranstaltung anlegen.
Vergewissern Sie sich, dass Sie ein aktives PayPal-Geschäftskonto haben.
Ein normales PayPal-Konto ist **nicht** ausreichend für die Integration mit pretix.

## Anleitung

Folgende Schritte sind erforderlich, um PayPal in pretix als Zahlungsdienstleister einzurichten:

 1. Aktivieren Sie die PayPal-Erweiterung.
 2. Verknüpfen Sie Ihr PayPal-Konto.
 3. Tragen Sie auf der Seite mit Einstellungen für PayPal die notwendigen Informationen ein.
 4. Nehmen Sie optionale Anpassungen vor.
 5. Aktivieren Sie Zahlungen über PayPal.
 6. Testen Sie die eingerichtete Zahlungsmethode.

Dieser Abschnitt erklärt diese Schritte ausführlich.

![Seite mit Einstellungen für Erweiterungen. Der Reiter "Zahlungsmethoden" ist geöffnet und zeigt die Erweiterungen für Banküberweisungen, Mollie, PayPal und Stripe, die alle aktiv sind.](../../assets/screens/payment/plugins-top.de.png "Verfügbare Erweiterungen")

Navigieren Sie zu :navpath:Ihre Veranstaltung →  :fa3-wrench: Einstellungen → Erweiterungen:.
Wechseln Sie zum Reiter :btn:Zahlungsmethoden:.
Auf dieser Seite wird die Erweiterung für PayPal oben angezeigt.
Sie sollte standardmäßig aktiv sein.
Wenn sie aktiv ist, hat sie ein grünes Tag ":fa3-check: Aktiv", einen weißen Button "Deaktivieren" und zwei Dropdown-Menüs.
Wenn sie inaktiv ist, fehlt das Tag und es gibt einen violetten Button :btn:Aktivieren:.
Vergewissern Sie sich, dass die Erweiterung aktiv ist.

![Seite "Zahlungseinstellungen". Der Reiter "Zahlungsmethoden" ist geöffnet und zeigt eine Liste mit den folgenden Einträgen: Banküberweisung, Wertgutschein/Geschenkgutschein, PayPal, SEPA-Lastschrift und Mollie; Wertgutschein/Geschenkgutschein ist aktiviert, alle anderen Einträge sind deaktiviert. Neben jedem der Einträge ist ein Button 'Einstellungen'.](../../assets/screens/payment/payment-settings.de.png "Zahlungseinstellungen" )

Sie können direkt zu den Einstellungen für PayPal springen, indem Sie das Dropdown-Menü :btn-icon:fa3-gear:Einstellungen: und anschließend :btn:Zahlung > PayPal: klicken.

Alternativ navigieren Sie zu :navpath:Ihre Veranstaltung →  :fa3-wrench: Einstellungen → Zahlung:.
Der Reiter :btn:Zahlungsdienstleister: auf dieser Seite enthält eine Liste aktiver Zahlungsdienstleister.
Die Liste sollte jetzt einen Eintrag für PayPal mit einem roten Tag ":fa3-times: Deaktiviert" enthalten.
Die Erweiterung ist zwar aktiv, aber Sie haben PayPal für die Veranstaltung noch nicht als Zahlungsdienstleister eingerichtet und aktiviert.
Klicken Sie den Button :btn-icon:fa3-gear:Einstellungen: neben PayPal.
Dadurch gelangen Sie zu der Seite mit Einstellungen für PayPal.

Das weitere Vorgehen hängt ab hier davon ab, ob Sie pretix Hosted oder eine selbstgehostete Edition von pretix (Community oder Enterprise) verwenden.

### Verknüpfung zu PayPal mit pretix Hosted

<!-- md:hosted -->

Wenn Sie pretix Hosted verwenden und Ihr Konto noch nicht mit PayPal verknüpft haben, zeigt die Seite mit den Einstellungen für PayPal nur den Button :btn:Mit PayPal verbinden: an.
Klicken Sie den Button und schließen Sie die Anmeldung und Autorisierung bei PayPal ab.


![PayPal-Website mit dem pretix-Logo oben rechts und einer Eingabemaske in der Mitte, in der steht: 'Verknüpfen Sie ein PayPal-Konto, um auf pretix GmbH Geld akzeptieren zu können'. Darunter können Sie Ihre E-Mail-Adresse eingeben und Ihr Land bzw. Ihre Region auswählen.](../../assets/screens/payment/paypal-connect-account.de.png "Mit PayPal verknüpfen" )

Nachdem Sie sich bei PayPal angemeldet und autorisiert haben, sieht die Seite mit den PayPal-Einstellungen im pretix-Backend anders aus.
Statt des einen Buttons sehen Sie nun zahlreiche Einstellungsmöglichkeiten.
Im oberen Bereich der Seite wird Ihre PayPal-Händlerkonto-ID angezeigt.

Alle Einstellungen hier sind optional.
Sehen Sie sich die Einstellungen auf dieser Seite genau an und aktivieren Sie alle, die Sie für Ihre Veranstaltung für diesen Zahlungsdienstleister wünschen.
Wenn alles wie gewünscht eingerichtet ist, scrollen Sie zum Seitenanfang und kreuzen das Kontrollkästchen neben "Zahlungsmethode aktivieren" an.
Nun stehen PayPal und die anderen hier aktivierten Zahlungsmethoden Ihren Kund\*innen in Ihrem Shop als Zahlungsoption zur Verfügung.

### Verknüpfung zu PayPal mit einer selbst gehosteten Edition von pretix

<!-- md:community -->
<!-- md:enterprise -->

Wenn Sie pretix Community oder pretix Enterprise verwenden und Ihr Konto noch nicht mit PayPal verknüpft haben, zeigt die Seite mit den Einstellungen für PayPal die Felder "Client-ID" und "Secret" an.
Gehen Sie zu [https://developer.paypal.com](https://developer.paypal.com) und melden Sie sich an Ihrem Konto an.
Erstellen Sie eine neue REST-API-Anwendung und stellen Sie sie von "Sandbox" auf "Live" um.
Kopieren Sie Client-ID und Secret von der Seite der REST-API-App für PayPal auf die pretix-Seite mit PayPal-Einstellungen.
Weitere Informationen finden Sie in der PayPal-Dokumentation über [PayPal-REST-APIs](https://developer.paypal.com/api/rest/).

Sie müssen außerdem einen Webhook erstellen, damit PayPal Informationen wie beispielsweise stornierte Zahlungen an pretix weitergeben kann.
Kopieren Sie die Webhook-URL aus dem Info-Feld im unteren Bereich der pretix-Seite mit PayPal-Einstellungen.
Öffnen Sie [https://developer.paypal.com](https://developer.paypal.com) und bearbeiten Sie die REST-API-App, die Sie für diese Veranstaltung erstellt haben.
Fügen Sie einen Webhook hinzu und fügen Sie die Webhook-URL in das entsprechende Feld ein.
Markieren Sie das Kontrollkästchen neben "All Events" und speichern Sie die Einstellungen.

Nachdem Sie die Verknüpfung zwischen pretix und PayPal eingerichtet haben, zeigt die Seite mit den PayPal-Einstellungen im pretix-Backend zahlreiche Einstellungen.
Alle neuen Einstellungen hier sind optional.
Sehen Sie sich die Einstellungen auf dieser Seite genau an und aktivieren Sie alle, die Sie für Ihre Veranstaltung für diesen Zahlungsdienstleister wünschen.
Wenn alles wie gewünscht eingerichtet ist, scrollen Sie zum Seitenanfang und kreuzen das Kontrollkästchen neben "Zahlungsmethode aktivieren" an.
Nun stehen PayPal und die anderen hier aktivierten Zahlungsmethoden Ihren Kund\*innen in Ihrem Shop als Zahlungsoption zur Verfügung.
