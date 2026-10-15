# Stripe

Stripe ist eine der zahlreichen Möglichkeiten, in pretix Zahlungen abzuwickeln. 
Sie können Stripe für folgende Zahlungsmethoden einsetzen: 
Affirm, Alipay, Apple Pay, Bancontact, EPS, Google Pay, iDEAL, Klarna, Kreditkarte, MobilePay, Multibanco, Przelewy24, Revolut Pay, SEPA-Bankeinzug, Swish, TWINT und WeChat Pay. 
Dieser Artikel erklärt, wie Sie Ihr Stripe-Konto verknüpfen, um darauf Zahlungen über pretix zu empfangen. 

## Voraussetzungen

Zahlungsdienstleister richten Sie auf Veranstaltungsebene ein, Sie müssen also zuerst eine Veranstaltung anlegen. 
Sie benötigen ein aktives Stripe-Händlerkonto. 
Ein normales Stripe-Konto ist **nicht** ausreichend für die Integration mit pretix. 
Eine [Anleitung zum Anlegen eines Stripe-Händlerkontos](https://stripe.com/de/resources/more/how-to-get-a-merchant-account) finden Sie auf der Stripe-Website. 

## Anleitung

Folgende Schritte sind erforderlich, um Stripe in pretix als Zahlungsdienstleister einzurichten: 

 1. Aktivieren Sie die Stripe-Erweiterung. 
 2. Verknüpfen Sie Ihr Stripe-Händlerkonto. 
 3. Tragen Sie auf der Seite mit Einstellungen für Stripe die notwendigen Informationen ein.
 4. Nehmen Sie optionale Anpassungen vor.
 5. Aktivieren Sie Zahlungen über Stripe.
 6. Testen Sie die eingerichtete Zahlungsmethode. 
 7. Schalten Sie den API-Endpunkt für Stripe live. 

Dieser Abschnitt erklärt diese Schritte ausführlich. 

![Seite mit Einstellungen für Erweiterungen. Der Reiter "Zahlungsmethoden" ist geöffnet und zeigt die Erweiterungen für Banküberweisungen, Mollie, PayPal und Stripe, die alle aktiv sind.](../../assets/screens/payment-providers/plugins-top.png "Verfügbare Erweiterungen")

Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Erweiterungen:.
Wechseln Sie zum Reiter :btn:Zahlungsmethoden:. 
Auf dieser Seite wird die Erweiterung für Stripe oben angezeigt. 
Sie sollte standardmäßig aktiv sein. 
Wenn sie aktiv ist, hat sie ein grünes Tag ":fa3-check: Aktiv", einen weißen Button "Deaktivieren" und zwei Dropdown-Menüs. 
Wenn sie inaktiv ist, fehlt das Tag und es gibt einen violetten Button :btn:Aktivieren:. 
Vergewissern Sie sich, dass die Erweiterung aktiv ist. 

![Seite "Zahlungseinstellungen". Der Reiter 'Zahlungsmethoden' ist geöffnet und zeigt eine Liste mit den folgenden Einträgen: Banküberweisung, Wertgutschein/Geschenkgutschein, PayPal, SEPA-Lastschrift und Stripe. Die Option 'Wertgutschein/Geschenkgutschein' ist aktiviert, alle anderen Einträge sind deaktiviert. Neben allen Einträgen sind Buttons mit dem Text 'Einstellungen'.](../../assets/screens/payment-providers/payment-settings.png "Zahlungseinstellungen" )

Sie können direkt zu den Einstellungen für Stripe springen, indem Sie das Dropdown-Menü :btn-icon:fa3-gear:Einstellungen: und anschließend :btn:Zahlung > Stripe: klicken. 

Alternativ navigieren Sie zu :navpath:Ihre Veranstaltung →  :fa3-wrench: Einstellungen → Zahlung:. 
Der Reiter :btn:Zahlungsdienstleister: auf dieser Seite enthält eine Liste aktiver Zahlungsdienstleister. 
Die Liste sollte jetzt einen Eintrag für Stripe mit einem roten Tag ":fa3-times: Deaktiviert" enthalten. 

Die Erweiterung ist zwar aktiv, aber Sie haben Stripe für die Veranstaltung noch nicht als Zahlungsdienstleister eingerichtet. 
Klicken Sie den Button :btn-icon:fa3-gear:Einstellungen: neben Stripe. 
Dadurch gelangen Sie zu der Seite mit den Einstellungen für Stripe, wo derzeit nur der Button :btn:Mit Stripe verbinden: angezeigt wird. 

Das weitere Vorgehen hängt ab hier davon ab, ob Sie pretix Hosted oder eine selbst gehostete Edition von pretix (Community oder Enterprise) verwenden. 

### Verknüpfung zu Stripe mit pretix Hosted 

<!-- md:hosted -->

Klicken Sie den Button und schließen Sie die Anmeldung und Autorisierung bei Stripe ab. 

![Stripe-Website mit dem pretix-Logo links, dem Text 'pretix.eu arbeitet mit Stripe für eine sichere Zahlungsabwicklung' und rechts einer Eingabemaske mit der Überschrift 'Loslegen mit Stripe'. Darunter können Sie die E-Mail-Adresse Ihres Stripe-Kontos eingeben.](../../assets/screens/payment-providers/stripe-connect-account.png "Verknüpfung des Stripe-Kontos" )

Nachdem Sie sich bei Stripe angemeldet und autorisiert haben, sieht die Seite mit den Stripe-Einstellungen im pretix-Backend anders aus. 
Statt des einen Buttons sehen Sie nun zahlreiche Einstellungsmöglichkeiten. 
Die Seite zeigt Ihr Stripe-Konto im oberen Bereich an. 

Es gibt mehrere Kontrollkästchen zum Aktivieren von Zahlungsmethoden wie Kreditkarten, Alipay oder KLARNA für die Abwicklung über Stripe. 
Markieren Sie das Kontrollkästchen bei jeder Zahlungsmethode, die Sie aktivieren möchten. 
Einige der hier angebotenen Zahlungsmethoden müssen Sie in den Einstellungen Ihres Stripe-Kontos separat aktivieren. 
Prüfen Sie in den Kontoeinstellungen auf der Stripe-Website oder in der App, welche Einstellungen es dort für die gewünschten Zahlungsmethoden gibt, und aktivieren Sie diese. 

Alle weiteren Einstellungen auf dieser Seite sind optional. 
Sehen Sie sich die Einstellungen auf dieser Seite genau an und aktivieren Sie alle, die Sie für Ihre Veranstaltung für diesen Zahlungsdienstleister wünschen. 
Wenn alles wie gewünscht eingerichtet ist, scrollen Sie zum Seitenanfang und kreuzen das Kontrollkästchen neben "Zahlungsmethode aktivieren" an. 
Die Zahlungsmethoden, die Sie auf dieser Seite und in Ihrem Stripe-Konto aktiviert haben, stehen nun den Kund\*innen in Ihrem Shop beim Bezahlvorgang als Zahlungsoptionen zur Verfügung. 

Wenn Sie Ihren Shop live schalten, ändern Sie auf dieser Seite die Option "API-Endpunkt" von "Test-System" zu "Live". 
Solange die Veranstaltung noch im Testmodus ist, verwendet die pretix-Software immer den Test-Endpunkt von Stripe, unabhängig von der Einstellung hier. 

### Verknüpfung zu Stripe mit einer selbst gehosteten Edition von pretix 

<!-- md:community --> 
<!-- md:enterprise -->

Wenn Sie pretix Community oder pretix Enterprise verwenden und Ihr Konto noch nicht mit Stripe verbunden haben, zeigt die Seite mit den Einstellungen für Stripe Felder für API-Schlüssel an. 
Gehen Sie zu [https://dashboard.stripe.com/login](https://dashboard.stripe.com/login) und melden Sie sich mit Ihrem Konto an. 
Die Seite "API" im Stripe-Backend zeigt zwei Schlüsselpaare mit je einem geheimen und einem öffentlichen Schlüssel an: ein Paar für den Sandbox-Modus und ein Paar für den Live-Modus. 
Wenn Sie Zahlungen über Stripe testen möchten, kopieren Sie die Sandbox-Schlüssel von der Stripe-Seite für APIs in die entsprechenden Felder auf der pretix-Seite mit Stripe-Einstellungen. 

Wenn alles zum Empfang von Zahlungen über Stripe bereit ist, kopieren Sie die echten Schlüssel von der Stripe-Seite für APIs in die entsprechenden Felder auf der pretix-Seite mit Stripe-Einstellungen.
Weitere Informationen finden Sie in der Stripe-Dokumentation über [API-Schlüssel](https://docs.stripe.com/keys#obtain-api-keys).  

Sie müssen außerdem einen Webhook erstellen, damit Stripe Informationen wie beispielsweise stornierte Zahlungen an pretix weitergeben kann. 
Kopieren Sie die Webhook-URL aus dem Info-Feld im unteren Bereich der pretix-Seite mit Stripe-Einstellungen. 
Öffnen Sie [https://dashboard.stripe.com/webhooks](https://dashboard.stripe.com/webhooks) und erstellen Sie ein neues Ziel. 
Wählen Sie bei der Einrichtung des Ereignisziels, dass alle Ereignistypen an pretix gesendet werden. 
Fügen Sie die Webhook-URL in das entsprechende Feld ein und klicken Sie :tbn:Create destination:. 
Weitere Informationen finden Sie in der Stripe-Dokumentation auf den Seiten über [Ereignisziele](https://docs.stripe.com/workbench/event-destinations). 

Nachdem Sie die Verknüpfung zwischen pretix und Stripe eingerichtet haben, zeigt die Seite mit den Stripe-Einstellungen im pretix-Backend zahlreiche Einstellungen. 
Alle neuen Einstellungen hier sind optional. 
Sehen Sie sich die Einstellungen auf dieser Seite genau an und aktivieren Sie alle, die Sie für Ihre Veranstaltung für diesen Zahlungsdienstleister wünschen. 
Wenn alles wie gewünscht eingerichtet ist, scrollen Sie zum Seitenanfang und kreuzen das Kontrollkästchen neben "Zahlungsmethode aktivieren" an. 
Nun stehen Stripe und die anderen hier aktivierten Zahlungsmethoden Ihren Kund\*innen in Ihrem Shop als Zahlungsoption zur Verfügung. 

Wenn Sie Ihren Shop live schalten, ändern Sie auf dieser Seite die Option "API-Endpunkt" von "Test-System" zu "Live". 
Solange die Veranstaltung noch im Testmodus ist, verwendet die pretix-Software immer den Test-Endpunkt von Stripe, unabhängig von der Einstellung hier. 
