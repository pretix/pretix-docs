## Einführung

!!! Note "Hinweis"
    Sollten Sie lediglich schnell entscheiden wollen, welcher Kontierungsmodus in den Einstellungen der pretix ePayBL-Erweiterung gewählt werden soll, so springen Sie direkt zur Sektion [Kontierungsmodus](epaybl.md#kontierungsmodus).

ePayBL ist eine von vielen Methoden für die Abwicklung von Zahlungen in pretix. 
ePayBL (kurz für ePayment des Bundes und der Länder) ist ein Zahlungssystem für Aufgabenträger des Bundes, der Länder und der Kommunen in Deutschland. 
Es bietet in der Anwendung besondere Vorteile wie etwa die automatische Erfassung von Zahlungsbelegen, Kontierungen und Steuermerkmalen. 
Außerdem kann die ePayBL-Integration Buchungen direkt in Haushaltskassen und Buchhaltungssysteme übertragen. 

ePayBL ist kein eigenständiger Zahlungsdienstleister, sondern nur eine Komponente im komplexen System der Zahlungsabwicklung für Behörden und Kommunen. 
Trotzdem können Sie ePayBL genau so in pretix verwalten wie jeden anderen Zahlungsdienstleister. 
ePayBL unterstützt folgende Zahlungsmethoden: Kreditkarte, PayPal, Rechnung, SEPA-Lastschrift und Vorkasse. 
Dieser Artikel erklärt, wie Sie Ihr pretix-Konto mit Ihrem ePayBL-System verbinden können, um es für Zahlungen über pretix zu verwenden. 

### Hintergrundinformationen

ePayBL stellt das Bindeglied zwischen den Fachverfahren, Haushaltssystemen und dem eigentlichen Zahlungsdienstleister dar. 
Der Zahlungsdienstleister zieht Gelder ein und zahlt sie an den Händler aus. 
pretix bietet direkte Integrationen mit den meisten Zahlungsdienstleistern an. 
Wenn Sie die Anbindung an Ihre Haushaltssysteme nicht benötigen, dann können Sie statt ePayBL auch einen anderen Zahlungsdienstleister mit pretix verbinden und nutzen. 

Nicht jeder IT-Dienstleister bietet seinen Nutzenden immer sofort die neueste Version von ePayBL an. 
Das kann z.B. an Updatezyklen oder speziellen Anpassungen liegen. 
Deswegen sind trotz Standardisierung nicht alle ePayBL-Systeme exakt gleich ansprechbar. 

Die pretix-Erweiterung "ePayBL" bindet pretix an den ePayBL-Konnektor an. 
Der ePayBL-Konnektor steht optional zwischen den Fachverfahren und dem ePayBL-Server. 
Er bietet den Fachverfahren eine dauerhaft gleichbleibende Schnittstelle an. 
Gleichzeitig kann er mit jeder Version des ePayBL-Servers kommunizieren, unabhängig von Updatezyklen und individuellen Anpassungen. 

Der ePayBL-Konnektor benutzt möglicherweise andere Anmeldedaten als der Server selbst. 

!!! Note "Hinweis"
    pretix erlaubt keine Erstattungen von bereits geleisteten Zahlungen über ePayBL. 
    Der Prozess hierfür unterscheidet sich von Behörde zu Behörde und muss daher manuell durchgeführt werden.

## Voraussetzungen

Zahlungsdienstleister werden auf der Veranstaltungsebene eingerichtet. 
Daher müssen Sie zuerst eine Veranstaltung erstellen. 
Stellen Sie sicher, dass Ihr ePayBL-System eingerichtet und einsatzbereit ist. 
Für die Einrichtung der Verbindung zwischen pretix und ePayBL brauchen Sie Zugriff auf die jeweiligen Anmeldedaten einschließlich SSL-Client-Zertifikat und SSL-Client-Zertifikatspasswort. 

## Anleitung 

Die Einrichtung von ePayBL zur Abwicklung von Zahlungen in pretix besteht aus den folgenden Schritten: 

 1. Aktivieren Sie die Erweiterung ePayBL
 2. Geben Sie Ihre ePayBL-Anmeldedaten in pretix ein 
 3. Wählen Sie den Kontierungsmodus
 4. Aktivieren Sie die Zahlungsmethode 
 5. Schalten Sie das System ggf. von "test" auf "prod" 

Dieser Abschnitt wird Sie durch die genannten Schritte führen. 

### Aktivierung der Erweiterung

![Ausschnitt der Liste der Erweiterungen für Zahlungsdienstleister. Unter anderem zeigt die Liste ePayBL an. Dieser Eintrag ist als aktiv markiert und hat einen Button mit der Aufschrift 'Deaktivieren'.](../../assets/screens/payment-providers/plugins-list-de.png "Liste der Erweiterungen")

Navigieren Sie zu :navpath:Ihre Veranstaltung: → :fa3-wrench: Einstellungen → Erweiterungen. 
Öffnen Sie den Reiter :btn:Zahlungsmethoden:. 
Die Erweiterung ePayBL wird in der Liste auf dieser Seite angezeigt.  
Wenn sie aktiv ist, dann ist sie mit der grünen Markierung ":fa3-check: aktiv" und einem weißen Button "Deaktivieren" versehen. 
Wenn sie nicht aktiv ist, dann fehlt die Markierung und es wird ein lila Button :btn:Aktivieren: angezeigt. 
Aktivieren Sie die Erweiterung gegebenenfalls. 

### Eingabe der Anmeldedaten 

![Zahlungseinstellungen. Der Tab "Zahlungsmethoden" ist offen und zeigt eine Liste mit den folgenden Einträgen: Banküberweisung, PayPal, SEPA-Lastschrift, Stripe, Wertgutschein / Geschenkgutschein und ePayBL. Banküberweisung und Gutschein sind aktiviert, alle anderen sind deaktiviert. Alle Einträge haben einen Button für Einstellungen.](../../assets/screens/payment-providers/payment-settings-de.png "Zahlungseinstellungen")

Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Zahlung:. 
Der Reiter :btn:Zahlungsmethoden: auf dieser Seite zeigt die Liste aktiver Zahlungsdienstleister an. 
Diese Liste sollte nun einen Eintrag für ePayBL mit einer roten Markierung ":fa3-times: Deaktiviert" beinhalten. 
Die Erweiterung ist aktiv. 
Dadurch taucht ePayBL in dieser Liste auf und Sie haben Zugriff auf die Einstellungen. 
Sie haben ePayBL aber noch nicht als Zahlungsdienstleister eingerichtet und für Ihren Shop aktiviert. 

Klicken Sie neben ePayBL den Button :btn-icon:fa3-cog:Einstellungen:. 
Wählen Sie unter "System" zunächst ein Testsystem aus. 
Geben Sie Mandantennummer, Bewirtschafternummer, SSL-Client-Zertifikatspasswort und Kennzeichen Mahnverfahren ein. 
Laden Sie Ihr SSL-Client-Zertifikat hoch, indem Sie den Button :btn:Durchsuchen...: klicken und die Zertifikatsdatei auf Ihrem Computer auswählen. 
Wählen Sie dann den Kontierungsmodus.

### Kontierungsmodus

ePayBL wurde für die Abwicklung von Online-Zahlungsvorgängen in der Verwaltung geschaffen. 
In diesem Umfeld ist üblicherweise klar definiert, was ein\*e Kund\*in gerade bezahlt und wohin das Geld genau fließt. 
Diese Annahmen lassen sich in einem Ticketshop wie pretix nur zum Teil abbilden.

Die ePayBL-Integration für pretix bietet daher zwei unterschiedliche Kontierungsmodi an. 
Diese Modi unterscheiden sich dahingehend, wie Buchungen erfasst und an den ePayBL-Konnektor und die dahinterliegenden Haushaltssysteme gemeldet werden. 

Im Modus "pro Zahlvorgang" überträgt die Erweiterung pro Bestellung nur den Gesamtbetrag aus Produktpreisen, Gebühren und Steuern an den ePayBL-Konnektor und nicht die einzelnen Beträge. 
Nachträgliche Änderungen der Bestellung sind möglich. 
Dieser Modus erfordert zusätzliche Informationen in den ePayBL-Einstellungen in pretix. 

Im Modus "pro Position/Artikel" überträgt die Erweiterung jede einzelne Bestellposition.
Kund\*innen können nur einmalig erfolgreich bezahlen. 
Es ist nicht möglich, die übertragenen Daten nachträglich zu ändern. 
Gebühren (für Zahlung, Versand, Storno oder Service) können nicht übertragen werden. 
Dieser Modus erfordert zusätzliche Einstellungen bei allen Produkten in pretix.  

Die nächsten beiden Unterabschnitte stellen Ihnen die beiden Optionen im Detail vor. 

#### Kontierung pro Zahlvorgang

Der Modus "pro Zahlvorgang" fasst alle Positionen einer Bestellung zu einer einzelnen zusammen und übermittelt diese an den ePayBL-Konnektor. 
In diesem Modus schlüsselt die Erweiterung die Preise der einzelnen Produkte sowie die Steueranteile nicht auf. 
Der Steueranteil wird immer als 0 % übertragen. 
Die Erweiterung überträgt also pro Bestellung nur einen Gesamtbetrag an den ePayBL-Konnektor. 

Wählen Sie unter "Kontierung" die Option "pro Zahlungsvorgang". 
Daraufhin zeigt die Seite weitere Eingabefelder an. 
Geben Sie Kennzeichen für Haushaltsstelle und Objektnummer sowie optional ein Kontierungsobjekt `HREF` in die entsprechenden Felder ein. 
pretix nutzt diese Daten für jede Übertragung einer Bestellung an den ePayBL-Konnektor. 

Der Vorteil dieser Option ist, dass Bestellungen verändert werden können und dass pro Bestellung mehr als eine erfolgreiche Zahlung geleistet werden kann. 
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

Die Vorteile dieser Option sind, dass die größtmögliche Menge an Kontierungsdaten an den ePayBL-Konnektor übertragen wird und dass ein separates Verbuchen von Leistungen auf unterschiedliche Haushaltsstellen möglich ist. 
Ein Nachteil der Kontierung pro Position/Artikel ist, dass keine Gebühren-Positionen (Versandkosten, Zahlungs-, Storno- oder Servicegebühren) übertragen werden können. 

Ein weiterer Nachteil ist, dass Kund*innen pro Bestellung nur eine einzige erfolgreiche Zahlung leisten können. 
Die Schnittstelle zum ePayBL-Konnektor unterstützt in diesem Modus nur die erstmalige Übermittlung einer Bestellung, nicht aber die Aktualisierung der Daten der Bestellung. 
Bestellungen können zwar in pretix nachträglich verändert werden, aber das führt nicht zu einer Aktualisierung der Informationen auf Seiten von ePayBL. 

### Weitere Einstellungen 

Alle weiteren Einstellungen auf dieser Seite sind optional. 
Aktivieren Sie alle Einstellungen, die Sie für Ihre Veranstaltung bei ePayBL verwenden wollen. 
Wenn Sie Zahlungen per Kreditkarte oder PayPal über ePayBL anbieten wollen, dann aktivieren Sie die entsprechenden Kontrollkästchen. 

Sobald Sie zufrieden sind, haken Sie das Kontrollkästchen neben "Aktiviere Zahlungsmethode" an und klicken Sie den Button :btn:Speichern:. 
ePayBL und die weiteren Zahlungsmethoden, die Sie hier aktiviert haben, werden nun als Optionen für kaufende Personen in Ihrem Ticketshop angezeigt. 

Sobald Sie Ihren Ticketshop live schalten, wählen Sie unter "System" eine Option, die mit "integration" oder "prod" endet (also **nicht** mit "test") und klicken den Button :btn:Speichern:. 