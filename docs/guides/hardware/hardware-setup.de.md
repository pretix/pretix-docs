# Hardware-Einrichtung 

Dieser Artikel behandelt die Einrichtung von Hardware für Ihre Veranstaltung. 
Wir bieten [professionelle Hardware](https://pretix.eu/about/de/hardware) zur Miete und zum Kauf an. 
Mit diesen Geräten können Sie Produkte verkaufen, am Einlass Tickets kontrollieren, sowie Belege, Tickets und Badges ausdrucken. 
Dazu nutzen Sie unsere Apps pretixPOS, pretixPRINT und pretixSCAN. 

Diese Funktionen können Sie auch mit Ihrer eigenen Hardware abdecken, solange Sie ein funktionierendes Netzwerk haben und Ihre Geräte kompatibel mit unseren Apps sind. 

Bei Mietaufträgen richtet unser Team die Geräte üblicherweise vor dem Versand an Sie so ein, dass Sie sie nur noch anschließen und testen müssen. 
Je nach Auftragslage und Verfügbarkeit der Hardware ist dies jedoch nicht immer möglich. 

Falls Sie Hardware von uns kaufen, gibt es eine größere Vielfalt an Geräten und Konfigurationsmöglichkeiten. 
Dieser Artikel behandelt in erster Linie die Einrichtung unserer Miethardware. 

## Voraussetzungen

Die Voraussetzungen hängen von Ihrem individuellen Anwendungsfall ab. 
In jedem Fall brauchen Sie ausreichend Steckdosen und entweder mobilen Datenempfang oder einen Kabelanschluss für die Internetverbindung. 

## Anleitung

Packen Sie Ihre Hardware-Lieferung aus und überprüfen Sie diese auf Vollständigkeit. 
Wenn Sie die Geräte von uns gemietet haben, hilft Ihnen der Lieferschein dabei. 
Die Einrichtung der Hardware besteht aus folgenden Schritten: 

 - Router anschließen und in Betrieb nehmen (außer Sie verbinden die Hardware mit einem geeigneten bestehenden Netzwerk)
 - Scan-Smartphones in Betrieb nehmen (falls Sie die Hardware für die Einlasskontrolle nutzen)
 - Kassen anschließen und in Betrieb nehmen (falls Sie die Hardware für den Verkauf nutzen)
 - Drucker anschließen, mit Scannern oder Kassen verbinden und in Betrieb nehmen

Je nach Anwendungsfall sind eventuell nur einige dieser Schritte für Sie relevant. 
Falls Sie die Hardware **nicht** bei uns gemietet haben, müssen Sie zusätzlich dazu noch die Konfiguration der Geräte vornehmen. 

### Router einrichten 

Als Router vermieten wir üblicherweise den Teltonika RUTX11. 
Sie erkennen das Gerät an den Antennen auf der Rückseite und den nummerierten LAN-Buchsen an der Vorderseite. 

Schließen Sie das Netzteil an die Buchse mit der Aufschrift "PWR" am Router und an eine Steckdose an. 
Warten Sie ab, bis die LEDs des Routers nicht mehr blinken, sondern durchgängig leuchten. 
Das kann einige Minuten dauern. 
In dieser Zeit können Sie die Geräte (Scanner, Kassen oder Drucker) **noch nicht** über LAN oder WLAN mit dem Router verbinden. 
Warten Sie damit ab, bis die LEDs des Routers nicht mehr blinken. 

Um die mobile Datenverbindung des Routers zu nutzen, werfen Sie einen Blick auf die LEDs "2G", "3G" und "4G" über dem "SIM1"-Slot des Routers. 
Sobald die LEDs nicht mehr abwechselnd blinken, sondern eine der LEDs durchgängig leuchtet, hat der Router eine mobile Datenverbindung hergestellt. 
Alternativ zur mobilen Datenverbindung können Sie den Router über die WAN-Buchse an den kabelgebundenen Internetanschluss am Einsatzort anschließen. 

Wenn die LEDs "2.4" und "5" unterhalb von "WiFi" durchgängig leuchten, dann stellt der Router ein Netz mit 2,4 GHz und ein Netz mit 5 GHz zur Verfügung. 
Die Namen dieser Netze lauten `pretix_onsite` und `pretix_onsite_5ghz`. 
Falls Sie mehrere Router von uns gemietet haben, werden an die Namen ein Unterstrich und eine Zahl angehängt, z.B. `pretix_onsite_1` und `pretix_onsite_5ghz_1`. 

Verbinden Sie die anderen Geräte über LAN-Kabel oder über WLAN mit dem Router. 
Scan-Smartphones verbinden Sie immer mit dem WLAN. 
Drucker verbinden Sie mit einem LAN-Kabel mit einem der nummerierten LAN-Anschlüsse am Router. 
Verbinden Sie den Drucker **nicht** mit dem WAN-Anschluss am Router. 
Alternativ verbinden Sie den Drucker mit dem WLAN oder per USB direkt mit dem auftraggebenden Gerät. 

### Alternative: Eigenes Netzwerk

Alternativ zum einem unserer Router können Sie die Hardware auch an Ihr eigenes Netzwerk anschließen. 
Das Netzwerk muss folgende Voraussetzungen erfüllen: 

 - Alle Geräte mit pretixSCAN oder pretixPOS brauchen eine stabile https-fähige Internetverbindung für die Synchronisation mit dem pretix-Server. 
 - Alle Android-Geräte brauchen eine stabile Internetverbindung für Updates und Gerätemanagement über die Google-Server. 
 - Geräte mit pretixPRINT müssen über verschiedene TCP- und UDP-Ports mit den Druckern kommunizieren können. Das bedeutet: 
   - **keine** Trennung von kabelgebundenem und kabellosen LAN in unterschiedliche lokale Netzwerke
   - **keine** Client Isolation
   - **keine** lokalen Firewalls oder sonstige Blockaden der Kommunikation zwischen den Geräten 

Wir empfehlen daher, dass Sie potenzielle Verbindungsprobleme vermeiden, indem Sie einen unserer Router nutzen. 
Die Konfiguration unserer Router erfüllt all die oben genannten Voraussetzungen. 

### Scan-Smartphones einrichten 

Die von uns vermieteten Scan-Smartphones sind robuste Geräte mit eingebautem Scanner. 
Vor dem Einsatz sollten Sie bei allen Scan-Smartphones rechtzeitig den Akkustand prüfen und Sie gegebenenfalls laden. 

Je nach Bestellumfang und Verfügbarkeit haben Sie eine Ladestation geliefert bekommen. 
Die Ladestation bietet Platz für bis zu fünf Smartphones. 
Verbinden Sie die Ladestation über das mitgelieferte Kabel mit dem Netzteil. 
Verbinden Sie das Netzteil über das passende Stromkabel mit einer Steckdose. 

Stecken Sie dann die Scan-Smartphones in die Steckplätze der Ladestation. 
Bei erfolgreicher Verbindung mit der Station vibrieren die Geräte, spielen einen Ton ab oder schalten den Bildschirm ein. 
Das genaue Verhalten hängt von den Einstellungen des jeweiligen Scan-Smartphones ab. 

!!! Note 
    Die Ladestation ist nur mit bestimmten Scan-Smartphone-Modellen kompatibel. 
    Versuchen Sie **nicht**, ein Gerät mit Gewalt in den Steckplatz zu stecken. 
    Sie können Ihre privaten Smartphones **nicht** über die Ladestation laden. 

Falls Sie keine Ladestation zur Verfügung haben, nutzen Sie ein herkömmliches Ladegerät. 
Stecken Sie das mitgelieferte USB-C-Ladekabel in die Buchse unten am Scan-Smartphone und verbinden Sie das andere Ende des Kabels mit dem Ladeadapter. 
Stecken Sie den Ladeadapter in eine Steckdose. 

Nachdem das Scan-Smartphone ausreichend geladen ist, schalten Sie es ein und verbinden Sie es mit dem WLAN des Routers. 

### Kasse einrichten 

Die von uns vermieteten Kassen sind Tablets mit großem Bildschirm und einem eingebauten Belegdrucker oder einem Standfuß. 
Schließen Sie die Kasse an das Netzteil und an eine Steckdose an. 
Schalten Sie Sie ein und verbinden Sie mit dem Netzwerk. 

Falls Sie eine Kassenschublade verwenden, verbinden Sie diese über den dafür vorgesehenen Anschluss (RJ11) mit der Kasse. 

### Drucker einrichten 

Wir bieten Drucker für drei verschiedene Anwendungen an: Belege, Tickets und Badges (Namensschilder). 
Die von uns angebotenen Ticketdrucker wie z.B. der Boca Lemur können auch Butterfly-Badges drucken. 
Für Badges in Form von Klebeetiketten verwenden Sie hingegen einen Etikettendrucker wie z.B. den Bixolon XD5-40d. 

Unabhängig von der genauen Anwendung müssen Sie Ihren Drucker mit Strom, einer Verbindung (LAN, WLAN oder USB) und bedruckbarem Material versorgen. 
Falls Sie die Hardware von uns gemietet haben, testen Sie, ob die Konfiguration wie gewünscht funktioniert. 

Falls Sie die Hardware gekauft haben, drucken Sie eine Konfigurationsseite auf dem Drucker. 
Dann  verbinden Sie den Drucker über unsere App pretixPRINT mit der Kasse oder den Scannern. 

Falls Sie den Drucker mit einem Desktop-Computer verbinden wollen, konsultieren Sie die Dokumentation des jeweiligen Herstellers. 

Für mehr Informationen zum Testen der Konfiguration und zum Verbinden von Druckern mit Android-Geräten mit pretixPRINT lesen Sie folgende Seiten: 

 - Belegdrucker [Epson TM-m30iii und Epson TM-T88vii](epson.de.md)
 - Ticket- oder Butterfly-Badgedrucker [Boca Lemur und Boca Lemur C](boca.de.md)
 - Badgedrucker für Klebeetiketten [Bixolon XD5-40d](bixolon.de.md)

Falls Sie den **integrierten** Drucker der Kasse als Belegdrucker verwenden wollen, legen Sie geeignetes bedruckbares Material ein. 
Öffnen Sie auf der Kasse die App pretixPRINT. 
Tippen Sie unter der Überschrift "Belegdrucker" das Drei-Punkte-Menü :btn-icon:ellipsis-v:: und dann :btn:Testseite drucken:. 
Falls Sie die Hardware von uns gemietet haben, sollte das ohne Probleme funktionieren. 

Falls unter "Belegdrucker" kein Eintrag vorhanden ist oder das Drucken nicht funktioniert, tippen Sie :btn:Drucker einrichten:. 
Auf der Seite "Wie ist Ihr Drucker verbunden?" wählen Sie die Option "Eingebauter Drucker (SUNMI)" und tippen :btn:Weiter:. 
Sie müssen keine IP-Adresse angeben.
Unter "Protokoll" und "Dialekt" wählen Sie die jeweils einzige Möglichkeit. 

Tippen Sie :btn:Testseite drucken: und beobachten Sie, ob der verbundene Drucker wie erwartet druckt. 
Tippen Sie :btn:Einstellungen speichern:. 

## Problemlösung 

### LEDs 3G und 4G am Router blinken abwechselnd 

**Problem:** Der Router kann keine mobile Datenverbindung herstellen. 
Der Teltonika RUTX11 verhält sich in diesem Fall wie folgt:  
Die LEDs mit den Beschriftungen "3G" und "4G" am Router blinken abwechselnd. 
Die Statusanzeige mit den fünf Balken daneben leuchtet nicht. 

**Lösung:** Überprüfen Sie, ob Sie mit anderen Geräten am gleichen Ort eine stabile mobile Datenverbindung haben. 
Wenn dies der Fall ist, deutet das auf eine Fehlfunktion am Router oder an der eingebauten SIM-Karte hin. 
Kontaktieren Sie unseren Support. 

Falls Sie auch mit anderen Geräten keine brauchbare mobile Datenverbindung herstellen können, liegt das Problem womöglich beim Mobilfunkanbieter. 
Falls Sie einen kabelgebundenen Internetanschluss am Einsatzort zur Verfügung haben, schließen Sie den Router über die WAN-Buchse daran an. 
Für die Einlasskontrolle können Sie auf den Offline-Modus von pretixSCAN ausweichen. 
Für alle weiteren Fragen kontaktieren Sie unseren [Support](mailto:support@pretix.eu). 

### Drucker druckt Konfigurationsseite nicht

**Problem:** Sie können einen Drucker nicht dazu bringen, seine eigene Konfigurationsseite zu drucken (wie beschrieben unter [Konfigurationsseite drucken](hardware-setup.de.md#Konfigurationsseite-drucken)). 

**Lösung:** Stellen Sie sicher, dass: 

 - der Drucker mit Strom versorgt wird (das Netzteil/-kabel sollte verbunden sein) 
 - der Drucker eingeschaltet ist (falls vorhanden sollten Status-LED oder Display am Drucker leuchten)
 - das passende Material eingelegt ist
 - die Klappe des Druckers geschlossen ist (falls vorhanden)

Wenn all diese Punkte erfüllt sind, liegt möglicherweise ein technisches Problem vor. 
Lesen Sie die Dokumentation des Herstellers oder kontaktieren Sie unseren [Support](mailto:support@pretix.eu). 

### IP-Adresse auf der Konfigurationsseite lautet 0.0.0.0 

**Problem:** Die Konfigurationsseite des Druckers liefert als IP-Adresse `0.0.0.0` oder ein ähnlich unbrauchbares Ergebnis. 
Der Drucker ist also nicht mit dem Netzwerk verbunden. 

**Lösung:** Prüfen Sie, ob der Router mit Strom versorgt und eingeschaltet ist. 

Bei einer Verbindung über **LAN** prüfen Sie, ob das LAN-Kabel richtig in der Buchse des Druckers steckt. 
Prüfen Sie, ob das andere Ende desselben LAN-Kabels in der LAN-Buchse (**nicht** in der WAN-Buchse) des Routers steckt. 
Verwenden Sie gegebenenfalls ein anderes Kabel. 

Bei einer Verbindung über **WLAN** prüfen Sie, ob der WLAN-Dongle verbunden ist, beziehungsweise ob der Drucker eine aktive WLAN-Verbindung anzeigt. 

Geben Sie dem Drucker etwa eine Minute Zeit, um sich mit dem Netzwerk zu verbinden. 
Drucken Sie dann eine neue Konfigurationsseite aus, um die korrekte IP-Adresse zu erhalten. 

### Drucker druckt pretixPRINT-Testseite nicht

**Problem:** Der Drucker druckt die Konfigurationsseite zwar richtig aus, aber nicht die pretixPRINT-Testseite wie beschrieben unter [Drucker mit Scan-Smartphone oder Kasse verbinden](hardware-setup.de.md#drucker-mit-scan-smartphone-oder-kasse-verbinden). 

**Lösung:** Überprüfen Sie: 

 - ob das Gerät, auf dem pretixPRINT läuft, mit dem korrekten WLAN verbunden ist (bei von uns vermieteten Routern fängt der Netzwerkname mit `pretix-onsite` an)
 - ob die IP-Adresse in pretixPRINT korrekt ist
 - ob in pretixPRINT das richtige Protokoll ausgewählt ist (plus gegebenenfalls der richtige Dialekt) 

Speichern Sie die Einstellungen in pretixPRINT und testen Sie erneut. 

### Druckauftrag kommt auf einem anderen Drucker an

**Problem:** Die pretixPRINT-Testseite oder Ihre anderen Druckaufträge werden zwar gedruckt, aber von einem anderen Drucker als erwartet. 

**Lösung:** Die in pretixPRINT hinterlegte IP-Adresse ist nicht die des gewünschten Druckers. 
Verwenden Sie das Gerät mit dem verbundenen Drucker. 
Passen Sie Ihren Hardware-Aufbau entsprechend an. 

Alternativ können Sie die IP-Adresse auf die des gewünschten Druckers ändern. 
Speichern Sie die Einstellungen und testen Sie erneut. 

### Druckauftrag enthält Unsinn 

**Problem:** Die pretixPRINT-Testseite oder Ihre anderen Druckaufträge werden zwar ausgedruckt, enthalten aber Unsinn (z.B. Sonderzeichen oder zufällige Zeichenfolgen). 

**Lösung:** In pretixPRINT ist das falsche Protokoll für den Drucker konfiguriert. 
Ändern Sie in pretixPRINT Protokoll und gegebenenfalls Dialekt, mit dem das Gerät den Drucker anspricht. 
Speichern Sie die Einstellungen und testen Sie erneut. 