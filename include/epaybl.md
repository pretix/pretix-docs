## Einführung

!!! Note 
    Sollten Sie lediglich schnell entscheiden wollen, welcher Kontierungsmodus in den Einstellungen des pretix ePayBL-plugins gewählt werden soll, so springen Sie direkt zur Sektion [Kontierungsmodus](epaybl.md#kontierungsmodus).

ePayBL ist eine von vielen Methoden für die Abwicklung von Zahlungen in pretix. 
ePayBL (kurz für ePayment des Bundes und der Länder), ist ein Zahlungssystem für Aufgabenträger des Bundes, der Länder und der Kommunen in Deutschland. 
Es in der Anwendung besondere Vorteile wie etwa die automatische Erfassung von Zahlungsbelegen, Kontierungen und Steuermerkmalen, sowie das Übertragen von Buchungen in Haushaltskassen und Buchhaltungssysteme. 
Obwohl ePayBL nur eine Komponente im komplexen Systems der Zahlungsabwicklung für Behörden und Kommunen ist, kann es in pretix genau so verwaltet werden, wie jeder andere Zahlungsdienstleister. 
ePayBL unterstützt folgende Zahlungsmethoden: Kreditkarte, PayPal, Rechnung, SEPA-Lastschrift und Vorkasse. 
Dieser Artikel erklärt, wie Sie sich mit Ihrem ePayBL-System verbinden können, um es für Zahlungen über pretix zu verwenden. 

## Voraussetzungen

Zahlungsdienstleister werden auf der Veranstaltungsebene eingerichtet, daher müssen Sie zuerst eine Veranstaltung erstellen. 
Stellen Sie sicher, dass Ihr ePayBL-System eingerichtet und einsatzbereit ist. 
Für die EInrichtung brauchen Sie Zugriff auf die Anmeldedaten einschließlich SSL-Client-Zertifikat und SSL-Client-Zertifikatspasswort. 

## Anleitung 

Die Einrichtung von ePayBL zur Abwicklung von Zahlungen in pretix besteht aus den folgenden Schritten: 

 1. Aktivieren Sie die Erweiterung ePayBL
 2. Geben Sie Ihre ePayBL-Anmeldedaten in pretix ein 
 3. Nehmen Sie optionale Einstellungen vor
 4. Aktivieren Sie die Zahlungsmethode 
 5. Testen Sie sie 
 6. Schalten Sie das System ggf. von "Test" auf "Produktion". 

Dieser Abschnitt wird Sie in allen Einzelheiten durch diese Schritte führen. 

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Mollie; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

Navigieren Sie zu :navpath:Ihre Veranstaltung: → :fa3-wrench: Einstellungen → Erweiterungen. 
Öffnen Sie den Reiter :btn:Zahlungsmethoden:. 
Die Erweiterung ePayBL wird in der Liste auf dieser Seite angezeigt.  
Wenn sie aktiviert ist, dann ist sie mit der grünen Markierung ":fa3-check: aktiv" und einem weißen Knopf "Deaktivieren" versehen. 
Wenn sie nicht aktiviert ist, dann fehlt die Markierung und es wird ein lila Knopf :Aktivieren: angezeigt. 
Aktivieren Sie das Plugin. 

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
Die nächsten beiden Unterabschnitte stellen Ihnen die beiden Optionen vor und helfen Ihnen bei der Entscheidung. 

### Kontierung pro Position/Artikel

Dieser Modus "pro Position/Artikel" versucht den klassischen behördentypischen ePayBL-Zahlungsvorgang abzubilden. 
Jede einzelne Position, die ein Kunde in den Warenkorb legt, wird genau so an ePayBL und die Hintergrundsysteme übermittelt.
Wenn Sie diesen Kontierungsmodus wählen, dann müssen Sie bei Ihren Produkten die relevanten Informationen angeben. 

Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte: und bearbeiten Sie eines der Produkte. 
Öffnen Sie den Tab :btn:Zusätzliche Einstellungen: und hinterlegen Sie Kennzeichen für Haushaltsstelle und Objektnummer sowie optional ein Kontierungsobjekt (`HREF`; z.B. `stsl=Steuerschlüssel;psp=gsb:Geschäftsbereich,auft:Innenauftrag,kst:Kostenstelle;`). 
Wiederholen Sie diese Schritte für jedes Produkt, dessen Kauf an ePayBL übermittelt werden soll. 

Die Vorteile dieser Option sind, dass die größtmögliche Menge an Kontierungsdaten an ePayBL übertragen wird und dass ein separates Verbuchen von Leistungen auf unterschiedliche Haushaltsstellen möglicht ist. 
Ein Nachteil der Kontierung pro Position/Artikel ist, dass keine Gebühren-Positionen (Versandkosten, Zahlungs-, Storno- oder Servicegebühren) übertragen werden können. 
Bitte kontaktieren Sie unseren Support, falls Sie diese Funktionen benötigen. 

Ein weiterer Nachteil ist, dass Kund*innen pro Bestellung nur eine einzige Zahlung leisten können. 
Das kann zu Frust führen. 

pretix bietet die Option an, dass ein Veranstalter eine Bestellung jederzeit verändern kann: Ändern von Preisen von Positionen in einer aufgegebenen Bestellung, Zubuchen und Entfernen von Bestellpositionen, etc. 
Hat der Kunde seine ursprüngliche Bestellung jedoch schon über ePayBL bezahlt, kann pretix nicht mehr die komplette Bestellung mit den passenden Kontierungen übertragen – es müsste nur ein Differenz-Abbild zwischen Ursprungsbestellung und aktueller Bestellung übertragen werden. 
Aber auch wenn eine "Nachmeldung" möglich wäre, so wäre ein konkretes Auflösen für was jetzt genau gezahlt wird, nicht mehr möglich.

Daher gilt bei der Nutzung der Kontierung pro Position/Artikel: Der Kunde kann nur eine (erfolgreiche) Zahlung auf seine Bestellung leisten.

### Kontierung pro Zahlvorgang

Dieser Modus verabschiedet sich vom behördlichen "Jede Position gehört genau zu einem Haushaltskonto und muss genau zugeordnet werden". 
Stattdessen werden alle Bestellpositionen – inklusive eventuell definierter Gebühren – vermengt und nur als ein großer Warenkorb, genauer gesagt eine einzige Position, an ePayBL sowie die Hintergrundsysteme gemeldet.

Während im "pro Postion/Artikel"-Modus jeder Artikel einzeln übermittelt wird und damit auch korrekt pro Artikel der jeweilige Brutto- und Nettopreis sowie der anfallende Steuerbetrag und ein Steuerkennzeichen (mit Hilfe des optionalen `HREF`-Attributs) übermittelt werden, ist dies im "pro Zahlvorgang"-Modus nicht möglich.

Stattdessen übermittelt pretix nur einen Betrag für den gesamten Warenkorb: Bruttopreis == Nettopreis. 
Der Steuerbetrag wird hierbei als 0 übermittelt.

Die Angabe einer Haushaltsstelle und Objektnummer sowie optional der `HREF`-Kontierungsinformationen ist jedoch weiterhin notwendig – allerdings nicht mehr individuell für jeden Artikel/jede Position sondern nur für die gesamte Bestellung. 
Diese Daten sind direkt in den ePayBL-Einstellungen der Veranstaltung unter Einstellungen -\> Zahlung -\> ePayBL vorzunehmen

In der Praxis bedeutet dies, dass in einem angeschlossenen Haushaltssystem nicht nachvollzogen kann, welche Positionen konkret erworben und bezahlt wurden – stattdessen kann nur der Fakt, dass etwas verkauft wurde, erfasst werden.

Je nach Aufbau und Vorgaben der Finanzbuchhaltung kann dies jedoch ausreichend sein – wenn bspw. eine Ferienfahrt angeboten wird und seitens der Haushaltssysteme nicht erfasst werden muss, wie viel vom Gesamtbetrag einer Bestellung auf die Ferienfahrt an sich, auf einen Zubringerbus und einen Satz Bettwäsche entfallen ist, sondern (vereinfacht gesagt) es ausreichend ist, dass "Eine Summe X für die Haushaltsstelle/Objektnummer geflossen ist".

Dieser Modus der Kontierung bietet Ihnen auch als Vorteil gegenüber dem vorhergehenden an, dass die Bestellungen der Kunden jederzeit erweitert und verändert werden können – auch wenn die Ursprungsbestellung schon bezahlt wurde und nur noch eine Differenz gezahlt wird.

## Weiterführende Informationen 

ePayBL stellt das Bindeglied zwischen den Fachverfahren, Haushaltssystemen und dem eigentlichen Zahlungsdienstleister, dem sog. ZV-Provider dar. 
Dieser ZV-Provider ist die Stelle, welche die eigentlichen Kundengelder einzieht und an den Händler auszahlt. 
Das Gros der Zahlungsdienstleister unterstützt pretix hierbei auch direkt; sprich: Sollten Sie die Anbindung an Ihre Haushaltssysteme nicht benötigen, kann eine direkte Anbindung in der Regel ebenso – und dies bei meist vermindertem Aufwand – vorgenommen werden.

In der Vergangenheit zeigte sich jedoch schnell, dass nicht jeder IT-Dienstleister seinen Nutzenden immer sofort die neueste Version von ePayBL angeboten hat. 
Die Gründe hierfür sind mannigfaltig: Von fest vorgegebenen Update-Zyklen bis hin zu Systemen mit speziellen Anpassungen, kann leider nicht davon ausgegangen werden, dass alle ePayBL-Systeme exakt gleich ansprechbar sind – auch wenn es sich dabei eigentlich um einen standardisierten Dienst handelt.

Aus diesem Grund gibt es mit dem ePayBL-Konnektor eine weitere Abstraktionsschicht, welche optional zwischen den Fachverfahren und dem ePayBL-Server sitzt. 
Dieser Konnektor wird so gepflegt, dass er zum einen den Fachverfahren eine dauerhaft gleichartige Schnittstelle bietet, gleichzeitig aber auch mit jeder Version des ePayBL-Servers kommunizieren kann – egal wie neu oder alt, wie regulär oder angepasst diese ist.

Im Grunde müsste daher eigentlich immer gesagt werden, dass pretix eine Anbindung an den ePayBL-Konnektor bietet; nicht an "ePayBL" oder den "ePayBL-Server". 
Diese Unterscheidung kann bei der Ersteinrichtung und Anforderung von Zugangsdaten von Relevanz sein. 
Da in der Praxis jedoch beide Begriffe gleichbedeutend genutzt werden, wird im Folgenden auch nur von einer ePayBL-Anbindung die Rede sein – auch wenn explizit der Konnektor gemeint ist.

## Kontierungsmodus 

ePayBL ist ein Produkt, welches für die Abwicklung von Online-Zahlungsvorgängen in der Verwaltung geschaffen wurde: 
Ein Umfeld, in dem klar definiert ist, was ein Kunde gerade bezahlt und wohin das Geld genau fließt. 
Diese Annahmen lassen sich in einem Ticketshop wie pretix jedoch nur teilweise genauso abbilden.

Die ePayBL-Integration für pretix bietet daher zwei unterschiedliche Modi an, wie Buchungen erfasst und an ePayBL und damit auch an die dahinterliegenden Haushaltssysteme gemeldet werden können.


## Einschränkungen

Zum aktuellen Zeitpunkt erlaubt die pretix-Anbindung an ePayBL nicht das durchführen von Erstattungen von bereits geleisteten Zahlungen. 
Der Prozess hierfür unterscheidet sich von Behörde zu Behörde und muss daher händisch durchgeführt werden.
