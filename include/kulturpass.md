Der [KulturPass](https://www.kulturpass.de/) ist ein Programm der deutschen Bundesregierung für alle, die im laufenden Jahr ihren 18. Geburtstag feiern. 
Sie erhalten ab ihrem 18. Geburtstag ein Budget von 200 Euro, das sie für Eintrittskarten, Bücher, CDs, Platten und vieles andere einsetzen können. 
Als Ticketing-System stellt pretix einen automatisierten Prozess für den Verkauf von Eintrittskarten über den KulturPass-Marktplatz bereit. 

Dieser Artikel erklärt die Einrichtung der Schnittstelle zwischen dem KulturPass-Marktplatz und Ihrem pretix-Shop, die Verwaltung von KulturPass-Bestellungen und den Bestellprozess aus Sicht der Kund*innen. 

## Voraussetzungen

Sie benötigen Zugriff auf ein Veranstalterkonto und mindestens eine Veranstaltung. 
Außerdem müssen Sie sich bei kulturpass.de registrieren, einen Shop einrichten und Angebote erstellen. 
Falls Sie das nicht bereits getan haben, registrieren Sie Ihr Unternehmen/Ihre Einrichtung zunächst auf der [KulturPass-Webseite](https://storefront.prod.kulturpass.de/seller-registration). 

## Anleitung

### Verbindung der Konten

!!! Warning 
    Ein KulturPass-Shop kann nur mit einem einzigen externen System verbunden werden. 
    Wenn der KulturPass-Shop mit mehreren externen Systemen verbunden ist, ist es nicht möglich, Bestellungen zu verarbeiten oder Angebote automatisiert an den KulturPass-Marktplatz zu übermitteln. 
    Eingehende Bestellungen automatisch abgelehnt, da sie nicht eindeutig zugeordnet werden können. 
    Das gilt auch, wenn Sie Ihren KulturPass-Shop mit mehreren pretix-Veranstalterkonten verbinden. 

    Wenn Sie mehrere Systeme haben, die den KulturPass-Marktplatz bedienen sollen, wenden Sie sich bitte an den KulturPass-Support, um sich einen weiteren Shop einrichten zu lassen.

Um Ihr pretix-Veranstalterkonto mit Ihrem KulturPass-Konto zu verbinden, navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → KulturPass:. 
Hinterlegen Sie hier den "API Schlüssel" und die "Shop ID" Ihres KulturPass-Shops. 

Sie finden den API-Schlüssel im [KulturPass-Backend](https://kulturpass-de.mirakl.net/) indem Sie diesen aufrufen und sich einloggen. 
Klicken Sie das Benutzer-Symbol in der oberen, rechten Ecke, :btn:Profil: und dann "API Schlüssel".
Sie finden die Shop-ID, indem Sie in der Navigation links "Einstellungen" und dann "Shop" auswählen.

### Verbindung und Konfiguration der Veranstaltung 

Jede einzelne Veranstaltung, die Sie über den KulturPass anbieten möchten, benötigt die KulturPass-Erweiterung. 
Um diese zu aktivieren, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Erweiterungen: und wechseln Sie zum Tab :btn:Integrationen:. 
Aktivieren Sie hier das Plugin "KulturPass". 

Wenn es sich bei Ihrer Veranstaltung um eine Einzelveranstaltung handelt (keine Veranstaltungsreihe) dann navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → KulturPass:. 
Wenn es sich bei Ihrer Veranstaltung um eine Veranstaltungsreihe handelt, dann navigieren Sie stattdessen zu :navpath:Ihre Veranstaltung → :fa3-calendar: Termine: und erstellen oder bearbeiten Sie einen der Termine, die Sie den über KulturPass-Marktplatz anbieten möchten. 
Aktivieren Sie das Kontrollkästchen "Diese Veranstaltung über den KulturPass anbieten". 
Sobald Sie das getan haben, werden weitere Einstellungen angezeigt. 

Geben Sie die notwendigen Informationen ein. 
Der KulturPass-Marktplatz verwendet ausschließlich die Informationen, die Sie hier angeben. 
Verwenden Sie daher präzise Titel und Beschreibungen. 
Klicken Sie dann den :btn:Speichern:-Knopf. 
Wiederholen Sie diese Schritte für jede Veranstaltung oder jeden Termin innerhalb einer Veranstaltungsreihe, für die Sie den KulturPass nutzen möchten. 
Es kann einige Zeit dauern, bis hier vorgenommene Einstellungen im KulturPass-System angezeigt werden. 

!!! Note 
    Der KulturPass-Marktplatz zeigt nicht die gleiche Fülle von Informationen an, die Ihr pretix-Ticketshop anzeigt. 
    Schreiben Sie daher in den Feldern "Veranstaltungstitel" und "Veranstaltungsbeschreibung" aussagekräftige Texte, die nicht mit den Veranstaltungen anderer Anbietender verwechselt werden können. 

### Anbieten von Produkten über den KulturPass-Marktplatz 

Nachdem Sie die KulturPass-Erweiterung aktiviert haben, können Sie einzelne Produkte über den KulturPass-Marktplatz anbieten. 
Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte: und bearbeiten Sie das relevante Produkt. 
Öffnen Sie den Tab :btn:Zusätzliche Einstellungen: und setzen Sie das Häkchen bei "Das Produkt kann mit dem KulturPass erworben werden".
Wiederholen Sie diese Schritte für jedes Produkt, dass Sie über den KulturPass-Marktplatz anbieten möchten. 
Sie können beliebig viele Produkte über den KulturPass-Marktplatz anbieten. 

!!! Note 
    Ihr Angebot wird im KulturPass-Marktplatz immer mit dem höchsten einzelnen Produktpreis gelistet. 
    Wenn Sie ein Produkt für 100 € über den KulturPass-Marktplatz anbieten, wird Ihr Angebot dort mit 100 € gelistet. 
    Das gilt sogar dann, wenn alle anderen Produkte in Ihrem Shop z.B. nur 5 € kosten. 
    Das KulturPass-Guthaben einer kaufenden Person muss mindestens 100 Euro betragen, damit sie Ihr Angebot in Anspruch nehmen kann. 

    Die kaufende Person wählt erst mit dem KulturPass-Einlösecode im Wert von 100 € in Ihrem pretix-Shop ein Produkt aus. 
    Das Restguthaben wird nach dem Kauf automatisch zurückerstattet und dem KulturPass-Konto gutgeschrieben.

### Konfiguration des Marktplatz-Eintrages

Sobald Sie mindestens eine Veranstaltung konfiguriert und live geschaltet haben, übermittelt pretix die Daten automatisch in regelmäßigen Abständen an das KulturPass-System (Mirakl). 

Der Export der Produkte und Angebote kann einige Zeit in Anspruch nehmen. 
Alle neuen Angebote werden händisch von den Betreibenden der KulturPass-Plattform geprüft, bevor sie sie freigeben. 
Außerdem muss eine Synchronisation zwischen dem Hintergrundsystem und der KulturPass-App erfolgen. 
pretix hat keinen Einfluss auf die Dauer dieser Prozesse. 

Nachdem pretix erstmalig Angebote an das KulturPass-System übermittelt hat, müssen Sie Ihren Shop KulturPass-Shop einmalig freischalten. 
Loggen Sie sich hierzu in das [KulturPass-Backend](https://kulturpass-de.mirakl.net/) ein. 


## Verwalten von KulturPass-Bestellungen

Sobald Sie Ihr Veranstalterkonto, ihre Veranstaltung/Termine und Produkte für die Integration mit dem KulturPass-System eingerichtet haben, müssen Sie sich um nichts weiteres kümmern. 
pretix übermittelt automatisch Ihre Veranstaltungen, wickelt die Einlösung der Tickets ab und führt die Abrechnung mit dem Hintergrund-System durch.

Die Gelder für mit dem KulturPass bezahlte Tickets erhalten Sie in Form einer Sammelüberweisung von der Stiftung Digitale Chancen auf das Bankkonto ,das Sie bei der Einrichtung Ihres KulturPass-Kontos angegeben haben. 
In Ihrem [KulturPass-Backend](https://kulturpass-de.mirakl.net/) können Sie über den Menüpunkt "Buchhaltung" Ihre bereits erfolgten und kommenden Auszahlungen betrachten.

!!! Warning
    Bearbeiten Sie **niemals** eingehenden Bestellungen, Produkte oder Angebote im KulturPass-Backend. 
    Sie würden damit riskieren, dass die Datenbasis zwischen pretix und dem KulturPass-System divergiert und es zu fehlerhaften Buchungen kommt. 
    Nehmen Sie Korrekturbuchungen und Änderungen ausschließlich über pretix vor. 
    Sollte eine händische Änderung notwendig werden, wenden Sie sich bitte an den pretix-Support. 

Erstattungen für Stornierungen und Absagen können Sie weiterhin über das pretix-Backend vornehmen. 
Der zurückzuerstattende Betrag wird dem KulturPass-Konto automatisch gutgeschrieben.

!!! Note 
    Nach Ausgabe eines KulturPass-Einlösecodes kann dieser von der kaufenden Person jederzeit storniert werden. 
    Das System kann ihn ebenfalls stornieren, wenn er nicht binnen 48 Stunden vollständig eingelöst wurde. 
    Daher kann das zu Fluktuationen im Guthaben kommen, das im KulturPass-Backend angezeigt wird. 
    Auszahlungen erfolgen frühestens 48 Stunden nach der Aufgabe einer KulturPass-Bestellungen. 
    Ihr Guthaben wird daher in der Regel nicht ins Negative gehen.

## Ablauf für kaufende Personen

Für Besuchende Ihres pretix-Shops verhält sich der KulturPass wie eine Zahlungsmethode und wird im Bestellprozess neben Ihren anderen Zahlungsmethoden angeboten.
Wenn sie KulturPass als Zahlungsmethode auswählen, können Sie sich dort anmelden oder registrieren und ihr Guthaben erhalten. 

KulturPass-Nutzende können ein Angebot einer Veranstaltung auswählen, die via pretix vertrieben wird und erhalten dann innerhalb von 20 Minuten einen Einlösecode und einen Link. 
Der Link bringt die Person direkt auf die Seite der betreffenden pretix-Veranstaltung, wo sie den Code für entsprechend markierte Produkte einlösen kann. 
Beim Bezahlen schlägt der Shop der kaufenden Person vor, den KulturPass-Einlösecode zu nutzen. 

Wenn Artikel gewählt werden, die günstiger als der Wert des Einlösecodes sind, dann wird das Restguthaben automatisch auf das KulturPass-Konto erstattet.
Wenn die Artikel insgesamt teurer sind, dann kann die kaufende Person die Differenz mit einem anderen regulären Zahlungsmittel begleichen. 
Einlösecodes, die Kunden nicht binnen 48 Stunden eingelöst werden, werden automatisch storniert und dem KulturPass-Konto wieder gutgeschrieben. 
Dieser Mechanismus greift auch, wenn eine Veranstaltung in der Zwischenzeit ausverkauft wird und daher der Einlösecode nicht mehr nutzbar ist.

## Siehe auch

Weitergehende Informationen zum KulturPass finden Sie auch auf der [Webseite des KulturPasses](https://www.kulturpass.de/) sowie im [KulturPass Serviceportal](https://service.kulturpass.de/help/).
