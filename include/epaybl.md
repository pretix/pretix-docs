## Einführung

!!! Note 
    Sollten Sie lediglich schnell entscheiden wollen, welcher Kontierungsmodus in den Einstellungen des pretix ePayBL-plugins gewählt werden soll, so springen Sie direkt zur Sektion [Kontierungsmodus](epaybl.md#kontierungsmodus).

ePayBL ist eine von vielen Methoden für die Abwicklung von Zahlungen in pretix. 
ePayBL (kurz für ePayment des Bundes und der Länder) ist ein Zahlungssystem für Aufgabenträger des Bundes, der Länder und der Kommunen in Deutschland. 
Es bietet in der Anwendung besondere Vorteile wie etwa die automatische Erfassung von Zahlungsbelegen, Kontierungen und Steuermerkmalen, sowie das Übertragen von Buchungen in Haushaltskassen und Buchhaltungssysteme. 
Obwohl ePayBL nur eine Komponente im komplexen Systems der Zahlungsabwicklung für Behörden und Kommunen ist, kann es in pretix genau so verwaltet werden, wie jeder andere Zahlungsdienstleister. 
ePayBL unterstützt folgende Zahlungsmethoden: Kreditkarte, PayPal, Rechnung, SEPA-Lastschrift und Vorkasse. 
Dieser Artikel erklärt, wie Sie sich mit Ihrem ePayBL-System verbinden können, um es für Zahlungen über pretix zu verwenden. 

### Hintergrundinformationen

ePayBL stellt das Bindeglied zwischen den Fachverfahren, Haushaltssystemen und dem eigentlichen Zahlungsdienstleister dar. 
Der Zahlungsdienstleister zieht Gelder ein und zahlt sie an den Händler aus. 
pretix bietet direkte Integrationen mit den meisten Zahlungsdienstleistern an. 
Wenn Sie die Anbindung an Ihre Haushaltssysteme nicht benötigen, dann können Sie statt ePayBL auch einen anderen Zahlungsdienstleister mit pretix verbinden und nutzen. 

Nicht jeder IT-Dienstleister bietet seinen Nutzenden immer sofort die neueste Version von ePayBL an. 
Das kann z.B. an Updatezyklen oder speziellen Anpassungen liegen. 
Deswegen sind trotz Standardisierung nicht alle ePayBL-Systeme exakt gleich ansprechbar. 

Die Erweiterung "ePayBL" für pretix bindet an den ePayBL-Konnektor an. 
Der ePayBL-Konnektor steht optional zwischen den Fachverfahren und dem ePayBL-Server. 
Er bietet den Fachverfahren eine dauerhaft gleichbleibende Schnittstelle an. 
Gleichzeitig kann er mit jeder Version des ePayBL-Servers kommunizieren, unabhängig von Version und individuellen Anpassungen. 

Die Tatsache, dass pretix an den ePayBL-Konnektor anbindet, kann für die Ersteinrichtung und Anforderung von Zugangsdaten relevant sein. 

!!! Note 
    pretix erlaubt keine Erstattungen von bereits geleisteten Zahlungen über ePayBL. 
    Der Prozess hierfür unterscheidet sich von Behörde zu Behörde und muss daher händisch durchgeführt werden.

## Voraussetzungen

Zahlungsdienstleister werden auf der Veranstaltungsebene eingerichtet, daher müssen Sie zuerst eine Veranstaltung erstellen. 
Stellen Sie sicher, dass Ihr ePayBL-System eingerichtet und einsatzbereit ist. 
Für die EInrichtung brauchen Sie Zugriff auf die Anmeldedaten einschließlich SSL-Client-Zertifikat und SSL-Client-Zertifikatspasswort. 

## Anleitung 

Die Einrichtung von ePayBL zur Abwicklung von Zahlungen in pretix besteht aus den folgenden Schritten: 

 1. Aktivieren Sie die Erweiterung ePayBL
 2. Geben Sie Ihre ePayBL-Anmeldedaten in pretix ein 
 3. Wählen Sie den Kontierungsmodus
 4. Nehmen Sie optionale Einstellungen vor
 5. Aktivieren Sie die Zahlungsmethode 
 6. Testen Sie sie 
 7. Schalten Sie das System ggf. von "Test" auf "Produktion". 

Dieser Abschnitt wird Sie in allen Einzelheiten durch die genannten Schritte führen. 

### Aktivierung der Erweiterung

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Mollie; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

Navigieren Sie zu :navpath:Ihre Veranstaltung: → :fa3-wrench: Einstellungen → Erweiterungen. 
Öffnen Sie den Reiter :btn:Zahlungsmethoden:. 
Die Erweiterung ePayBL wird in der Liste auf dieser Seite angezeigt.  
Wenn sie aktiviert ist, dann ist sie mit der grünen Markierung ":fa3-check: aktiv" und einem weißen Knopf "Deaktivieren" versehen. 
Wenn sie nicht aktiviert ist, dann fehlt die Markierung und es wird ein lila Knopf :Aktivieren: angezeigt. 
Aktivieren Sie das Plugin. 

### Eingabe der Anmeldedaten 

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Mollie; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Zahlung:. 
Der Reiter :btn:Zahlungsmethoden: auf dieser Seite zeigt die Liste aktiver Zahlungsdienstleister an. 
Diese Liste sollte nun einen Eintrag für ePayBL mit einer roten Markierung ":fa3-times: Deaktiviert" beinhalten. 
Die Erweiterung ist aktiviert, aber ePayBL wurde noch nicht als Zahlungsdienstleister eingerichtet und aktiviert. 

Klicken Sie neben ePayBL den Knopf :btn-icon:fa3-cog:Einstellungen:. 
Wählen Sie unter "System" zunächst ein Testsystem aus. 
Geben Sie Mandantennummer, Bewirtschafternummer, SSL-Client-Zertifikatspasswort und Kennzeichen Mahnverfahren ein. 
Laden Sie Ihr SSL-Client-Zertifikat hoch, indem Sie den Knopf :btn:Durchsuchen...: klicken und die Zertifikatsdatei auf Ihrem Computer auswählen. 
Wählen Sie dann den Kontierungsmodus.

### Kontierungsmodus

ePayBL wurde für die Abwicklung von Online-Zahlungsvorgängen in der Verwaltung geschaffen. 
In diesem Umfeld ist üblicherweise klar definiert, was ein\*e Kund\*in gerade bezahlt und wohin das Geld genau fließt. 
Diese Annahmen lassen sich in einem Ticketshop wie pretix nur zum Teil abbilden.

Die ePayBL-Integration für pretix bietet daher zwei unterschiedliche Kontierungsmodi an. 
Diese Modi unterscheiden sich dahingehend, wie Buchungen erfasst und an den ePayBL-Konnektor und die dahinterliegenden Haushaltssysteme gemeldet werden. 
Die nächsten beiden Unterabschnitte stellen Ihnen die beiden Optionen vor und helfen Ihnen bei der Entscheidung. 

#### Kontierung pro Zahlvorgang

Der Modus "pro Zahlvorgang" fasst alle Positionen einer Bestellung zu einer einzelnen zusammen und übermittelt diese an den ePayBL-Konnektor. 
In diesem Modus werden die Preise der einzelnen Produkte sowie die Anteile an Steuern nicht unterschieden. 
Der Steueranteil wird immer als 0 übertragen. 

Wenn Sie den Modus "pro Zahlvorgang" auswählen, dann geben Sie auf derselben Seite Kennzeichen für Haushaltsstelle und Objektnummer sowie optional ein Kontierungsobjekt `HREF` ein. 
pretix nutzt diese Daten für jede Übertragung einer Bestellung an den ePayBL-Konnektor. 

Der Vorteil dieser Option ist, dass Bestellungen verändert werden können und dass pro Bestellung mehr als eine Zahlung geleistet werden kann. 
Diese Daten können ohne Probleme an den ePayBL-Konnektor übertragen werden. 

Der Nachteil dieser Option ist, dass ein angeschlossenes Haushaltssystem nicht nachvollziehen kann, welche Positionen konkret erworben und bezahlt wurden. 
Es erfasst nur die Tatsache, dass etwas verkauft und bezahlt wurde. 
Das kann je nach Anwendungsfall sowie Aufbau und Vorgaben der Finanzbuchhaltung ausreichend sein. 

#### Kontierung pro Position/Artikel

Der Modus "pro Position/Artikel" versucht den klassischen behördentypischen ePayBL-Zahlungsvorgang abzubilden. 
Jede einzelne Position, die ein Kunde in den Warenkorb legt, wird genau so an den ePayBL-Konnektor und die Hintergrundsysteme übermittelt.
Wenn Sie diesen Kontierungsmodus wählen, dann müssen Sie bei Ihren Produkten die relevanten Informationen angeben. 

Schließen Sie zunächst die Einrichtung von ePayBL ab, so wie sie im Rest dieses Artikels geschildert ist. 
**Nachdem** Sie das getan haben und Ihre Einstellungen gespeichert haben, bearbeiten Sie Ihre Produkte. 
Navigieren Sie dazu zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte: und bearbeiten Sie eines der Produkte. 
Öffnen Sie den Tab :btn:Zusätzliche Einstellungen: und geben Sie Kennzeichen für Haushaltsstelle und Objektnummer sowie optional ein Kontierungsobjekt `HREF` ein. 
Wiederholen Sie diese Schritte für jedes Produkt, dessen Kauf an den ePayBL-Konnektor übermittelt werden soll. 

Die Vorteile dieser Option sind, dass die größtmögliche Menge an Kontierungsdaten an den ePayBL-Konnektor übertragen wird und dass ein separates Verbuchen von Leistungen auf unterschiedliche Haushaltsstellen möglicht ist. 
Ein Nachteil der Kontierung pro Position/Artikel ist, dass keine Gebühren-Positionen (Versandkosten, Zahlungs-, Storno- oder Servicegebühren) übertragen werden können. 

Ein weiterer Nachteil ist, dass Kund*innen pro Bestellung nur eine einzige Zahlung leisten können. 
Die Schnittstelle zum ePayBL-Konnektor unterstützt in diesem Modus nur die erstmalige Übermittlung einer Bestellung, nicht aber die Aktualisierung der Daten der Bestellung. 
Bestellungen können zwar in pretix nachträglich verändert werden, aber das führt nicht zu einer Aktualisierung der Informationen auf Seiten von ePayBL. 

### Weitere Einstellungen 

Auf dieser Seite gibt es Kontrollkästchen für die weiteren Zahlungsmethoden PayPal und Kreditkarte. 
Aktivieren Sie diese, falls Sie Zahlungen per PayPal oder Kreditkarte via ePayBL empfangen möchten. 

Alle weiteren Einstellungen auf dieser Seite sind optional. 
Werfen Sie einen genauen Blick auf die Seite und aktivieren Sie alle Einstellungen, die Sie für Ihre Veranstaltung bei ePayBL verwenden wollen. 
Sobald Sie zufrieden sind, aktivieren Sie das Kontrollkästchen neben "Aktiviere Zahlungsmethode" und klicken Sie den Knopf :btn:Speichern:. 
ePayBL und die weiteren Zahlungsmethoden, die Sie hier aktiviert haben, werden nun als Optionen für kaufende Personen in Ihrem Ticketshop angezeigt. 

Sobald Sie Ihren Ticketshop live schalten, wählen Sie unter "System" eine Option, die **nicht** mit dem Hinweis "test" endet. 