# Hardware-Einrichtung 

Dieser Artikel behandelt die Einrichtung von Hardware für Ihr Event. 
Wir bieten [professionelle Hardware](https://pretix.eu/about/de/hardware) zur Miete und zum Kauf an. 
Mit diesen Geräten können Sie Produkte verkaufen, Einlasskontrolle machen, sowie Belege, Tickets und Badges ausdrucken.  
Dazu nutzen Sie unsere Apps pretixPOS, pretixPRINT und pretixSCAN sowie einen WLAN-Router. 
Diese Funktionen können Sie auch mit Ihrer eigenen Hardware abdecken, solange Sie ein funktionierendes Netzwerk haben und Ihre Geräte kompatible mit unseren Apps sind. 

## Voraussetzungen

Die Voraussetzungen hängen von Ihrem individuellen Anwendungsfall ab. 
Für die Einrichtung eines Druckers benötigen Sie einen dünnen, stabilen Gegenstand wie z.B. eine geradegebogene Büroklammer. 

## Anleitung

Packen Sie Ihre Hardware-Lieferung aus und überprüfen Sie diese anhand des Lieferscheins auf Vollständigkeit. 
Die Einrichtung der Hardware besteht aus folgenden Schritten: 

 - Router einrichten (außer Sie verbinden die Hardware mit einem bestehenden Netzwerk)
 - Scan-Smartphones einrichten (falls Sie die Hardware für die Einlasskontrolle nutzen)
 - Kassengerät einrichten (falls Sie die Hardware für den Verkauf nutzen)
 - Drucker einrichten 

Je nach Anwendungsfall sind eventuell nur einige dieser Schritte für Sie relevant. 

### Router einrichten 

Die von uns angebotenen Router sind metallfarbene Kästen mit mehreren Antennen und nummerierten LAN-Ports. 

Schließen Sie das Netzteil an die "PWR"-Buchse am Router und an eine Steckdose an. 
Warten Sie ab, bis die LEDs des Routers nicht mehr blinken, sondern durchgängig leuchten. 
Das kann einige Minuten dauern. 

Falls Sie den Router mit dem Netzwerk am Veranstaltungsort verbinden wollen, dann verbinden Sie den "WAN"-Port des Routers mit einem LAN-Kabel mit einem Switch. 
Falls Sie die mobile Datenverbindung des Routers nutzen wollen, werfen Sie einen Blick auf die LEDs "2G", "3G" und "4G" über dem "SIM1"-Slot des Routers. 
Sobald die LEDs nicht mehr abwechselnd blinken, sondern eine der LEDs durchgängig leuchtet, hat der Router eine mobile Datenverbindung hergestellt.  

Wenn die LEDs "2.4" und "5" unterhalb von "WiFi" durchgängig leuchten, dann stellt  der Router ein Netz mit 2,4 GHz und ein Netz mit 5 GHz zur Verfügung. 
Die SSIDs dieser Netze lauten `pretix_onsite` und `pretix_onsite_5ghz`. 
Falls Sie mehrere Router verwenden, werden an die SSIDs ein Unterstrich und eine Zahl angehängt, z.B. `pretix_onsite_1` und `pretix_onsite_5ghz_1`. 

Verbinden Sie die anderen Geräte über LAN-Kabel oder über WLAN mit dem Router. 
Smartphones verbinden Sie immer mit dem WLAN. 
Drucker verbinden Sie mit einem LAN-Kabel mit einem der nummerierten LAN-Anschlüsse am Router. 
Verbinden Sie den Drucker **nicht** mit dem Anschluss mit der Aufschrift "WAN" am Router. 

### Drucker einrichten 

Wir bieten Drucker für drei verschiedene Anwendungen an: Belege, Tickets und Badges. 
Unabhängig von der genauen Anwendung müssen Sie Ihren Drucker mit Strom, einer Internetverbindung und bedruckbarem Material versorgen. 
Dann drucken Sie eine Testseite. 
Diese Schritte werden im folgenden genauer erklärt. 

#### Anschließen

Falls Ihr Drucker intern über eine Rolle mit Material versorgt wird (Thermopapier oder Labels), dann legen Sie zunächst diese Rolle ein. 
Verbinden Sie den Drucker dann über ein LAN-Kabel mit einem der nummerierten "LAN"-Anschlüsse des Routers. 
Schließen Sie das Netzteil an den Drucker und an eine Steckdose an. 

Falls Ihr Drucker über einen flachen Papierstapel mit Material versorgt wird (Tickets oder Butterfly-Badges), dann schieben Sie das Papier jetzt in den Drucker. 
Die bedruckbare Seite muss nach oben Zeigen und die schwarzen quadratischen Markierungen auf der Unterseite müssen sich an der Seite befinden, die weiter vom Drucker entfernt ist. 
Der Drucker zieht das Ticketpapier automatisch ein und schneidet das erste Ticket ab. 

#### Testseite drucken

Das Ausdrucken einer **Testseite** wird je nach Modell des Druckers unterschiedlich ausgelöst: 

 - Die Belegdrucker **Epson TM-m30iii** und **TM-T88vii** drucken innerhalb einer Minute nach Einschalten automatisch eine Testseite. 
   Das funktioniert nur, wenn der Drucker mit Stromversorgung und Router verbunden ist und Papier hat. 
   Falls Sie erneut eine Testseite drucken wollen, schalten Sie den Drucker aus und wieder ein. 
 - Der Etikettendrucker **Bixolon XD5-40d** hat neben dem Strom- und LAN-Anschluss ein wenige Millimeter breites Loch, in dem ein Button verborgen ist. 
   Schalten Sie den Drucker ein und benutzen Sie einen dünnen, stabilen Gegenstand wie z.B. eine geradegebogene Büroklammer, um den Knopf zu drücken. 
   Das löst den Druck einer Testseite aus. 
 - Die Ticketdrucker **Boca Lemur** und **Lemur C** haben an der Seite drei Aussparungen, in denen jeweils eine Status-LED und ein Knopf verborgen sind. 
   Drücken Sie den Knopf unter dem Label "TEST — NO TKT". 
   Dies löst den Druck einer Testseite aus. 

Falls der Drucker keine Testseite druckt, dann ist entweder das Material nicht richtig eingelegt, oder es gibt ein technisches Problem mit dem Drucker. 
Überprüfen Sie, ob die Rolle bzw. der Papierstapel richtig in den Drucker eingelegt sind. 
Falls Sie danach noch immer keine Testseite drucken können, konsultieren Sie die Dokumentation des Herstellers oder kontaktieren Sie unseren Support. 

Sie können der Testseite die IP-Adresse des Druckers entnehmen. 
Diese IP-Adresse benötigen Sie, um Scan-Smartphones und Kassengeräte mit den Druckern zu verbinden. 
Das wird in den nächsten Abschnitten näher erklärt. 

### Scan-Smartphones einrichten 

Die von uns angebotenen Scan-Smartphones sind robuste, schwere Smartphones mit eingebautem Scanner. 
Unser Team hat das Mietgerät bereits Ihrem Veranstalterkonto hinzugefügt. 
Schließen Sie das Smartphone an ein Ladegerät an oder stecken Sie es in die Ladestation, bis der Akku ausreichend geladen ist. 
Schalten Sie es ein und verbinden Sie es mit dem WLAN des Routers. 

#### Badgedrucker verbinden

Falls Sie beim Einlass Badges drucken wollen, dann öffnen Sie auf dem Scan-Smartphone die App pretixPRINT. 
Unter "Badgedrucker" tippen Sie :btn:Drucker einrichten:. 

!!! Note
    pretixPRINT erlaubt die Einrichtung von drei verschiedenen Arten von Druckern. 
    Daher zeigt die App drei verschiedene Schaltflächen mit der Beschriftung "Drucker einrichten" an. 
    Für die Einlasskontrolle ergibt es keinen Sinn, Ticket- oder Belegdrucker einzusetzen. 
    Tippen Sie daher die Schaltfläche unter der Überschrift "Badgedrucker". 

Auf der Seite "Wie ist Ihr Drucker verbunden?" wählen Sie "Netzwerk (LAN/WLAN) und tippen :btn:Weiter:. 
Geben Sie die IP-Adresse des Routers ein. 
Das Feld "Port" können Sie in den meisten Fällen unverändert lassen. 
Bearbeiten Sie es nur dann, wenn die Testseite des Druckers eine Port-Nummer ausgibt, die **nicht** `9100` lautet. 
Tippen Sie dann :btn:Weiter:. 

Auf der Seite "Welches Protokoll spricht Ihr Drucker?" wählen Sie das Protokoll aus, das am ehesten zu Ihrem Drucker passt. 
Falls Sie einen Ticketdrucker der Marke Lemur verwenden, wählen Sie "FGL-Ticketdrucker (z.B. Boca, Practical Automation, ...)". 
Falls Sie einen Etikettendrucker der Marke Lemur verwenden, wählen Sie 

### Kassengerät einrichten 

Die von uns angebotenen Kassengeräte sind Tablets mit großem Bildschirm und einem eingebauten Belegdrucker oder einem Standfuß. 
Unser Team hat das Mietgerät bereits Ihrem Veranstalterkonto hinzugefügt. 


## Problemlösung 

What are common problems that could be encountered here? How do you solve them? 

## Weiterführende Informationen

What other media do we have on the subject? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## Siehe auch 

Link to other relevant guides, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 