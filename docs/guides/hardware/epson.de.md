# Drucker einrichten: Epson TM-m30iii und Epson TM-T88vii 

Bei diesem Artikel handelt es sich um eine Schnellstart-Anleitung für die Verwendung von Druckern der Marke Epson zusammen mit pretix. 
Er erklärt, wie Sie den Drucker aufbauen und über die App pretixPRINT mit Kassen oder Scan-Smartphones verbinden. 
Falls Sie den Drucker mit einem Desktop-Computer verbinden wollen, konsultieren Sie die Dokumentation des Herstellers. 

!!! Note 
    Diese Seite ersetzt nicht die Dokumentation für die Geräte selbst. 
    Informieren Sie sich auf der Webseite des Herstellers über die Modelle [Epson TM-m30iii](https://www.epson.de/de_DE/support/sc/tm-m30iii/s/s3018#manuals) und [Epson TM-T88vii](https://www.epson.de/de_DE/support/sc/tm-t88vii/s/s2258#manuals). 

Die Geräte Epson TM-m30iii und TM-T88vii unterscheiden sich in der Bedienung nur in folgenden Punkten voneinander: 

 - Position des Stromschalters (TM-m30iii: Oberseite. TM-T88vii: Vorderseite)
 - Öffnen der Materialklappe (TM-m30iii: nach hinten schieben. TM-T88vii: nach unten drücken)
 - Die Anschlüsse am TM-m30iii sind unter einer Abdeckung verborgen, die entfernt werden kann. 
   Am TM-T88vii ist keine solche Abdeckung vorhanden. 

## Voraussetzungen

Für die Stromversorgung des Geräts benötigen Sie eine Steckdose in der Nähe. 
Für die Netzwerkverbindung brauchen Sie einen Router mit einem freien LAN-Anschluss oder eine alternative Lösung. 
Als Material benötigen Sie aufgerolltes bedruckbares Thermopapier mit einer Breite von 80mm. 

## Anleitung

Mit dem Epson TM-m30iii oder TM-T88vii können Sie Belege drucken. 
Sie müssen Ihren Drucker mit Strom, einer Netzwerkverbindung und bedruckbarem Material versorgen. 
Dann testen Sie die Konfiguration. 

Falls die Hardware nicht vorkonfiguriert wurde, drucken Sie eine Konfigurationsseite. 
Danach verbinden Sie den Drucker über unsere App pretixPRINT mit der Kasse oder den Scannern. 
Diese Schritte werden im Folgenden genauer erklärt. 

### Drucker anschließen

Stellen Sie zuerst sicher, dass der Drucker **nicht** mit dem Strom verbunden ist und **nicht** eingeschaltet ist. 
Legen Sie dann das Druckmaterial in den Drucker ein. 

**TM-m30iii:** Schieben Sie den grauen Hebel an der Oberseite des Geräts nach hinten und öffnen Sie die Materialklappe. 
**TM-T88vii:** Drücken Sie das graue Element an der Oberseite des Geräts nach unten und öffnen Sie die Materialklappe. 

Legen Sie die Papierrolle so in die Vertiefung im inneren des Geräts, dass das Papier an der Vorderseite des Innenraums nach oben läuft. 
Ziehen Sie das Papier ein Stück weit nach oben und schließen Sie die Klappe, sodass das Papier glatt und gerade aus dem Schlitz ragt. 

Überprüfen Sie, ob der Stromschalter des Druckers ausgeschaltet ist, und schalten Sie ihn gegebenenfalls aus. 
Verbinden oder entfernen Sie **keine** Kabel, während der Drucker eingeschaltet ist. 
Alle Anschlüsse befinden sich hinten und unten am Gerät. 
Beim TM-m30iii können Sie die Abdeckung an der Unterseite des Geräts entfernen, um Zugang zu den Anschlüssen zu erhalten. 

Um den Drucker über **LAN** an den Router anzuschließen, stecken Sie ein LAN-Kabel in die entsprechende Buchse am Drucker. 
Stecken Sie das andere Ende des LAN-Kabels in einen freien LAN-Anschluss an Ihrem Router. 

Alternativ zum Anschluss über LAN können Sie den Drucker auch über **USB** anschließen. 
Um das zu tun, stecken Sie ein USB-Typ-B-Kabel in die entsprechende Buchse am Drucker. 
Stecken Sie das andere Ende des Kabels in einen freien USB-Anschluss an Ihrer Kasse. 

**TM-m30iii:** Drücken Sie den Stromschalter an der Oberseite des Druckers ein. 
**TM-T88vii:** Legen Sie den Stromschalter an der Vorderseite des Druckers um. 

### Konfiguration testen

!!! Note 
    Falls Sie Hardware von uns gemietet haben, dann ist sie bereits betriebsbereit konfiguriert. 
    Das gilt auch, falls Sie Hardware von uns gekauft haben und vor dem Versand eine entsprechende Konfiguration in Auftrag gegeben haben. 

    In diesen Fällen müssen Sie die Konfiguration nur testen. 
    Sie können die beiden Unterabschnitte [Konfigurationsseite drucken](epson.de.md#konfigurationsseite-drucken) und [Drucker mit Scan-Smartphone oder Kasse verbinden](epson.de.md#drucker-mit-scan-smartphone-oder-kasse-verbinden) überspringen. 

Um die Konfiguration zu testen, starten Sie das Android-Gerät (Kasse oder Scan-Smartphone), von dem Sie den Drucker ansteuern wollen. 
Überprüfen Sie, ob das Gerät mit einem WLAN verbunden ist, dessen Name mit `pretix_onsite` beginnt. 
Öffnen Sie die App pretixPRINT. 

pretixPRINT erlaubt die Einrichtung von Druckern für drei verschiedene Verwendungszwecke: Belegdrucker, Ticketdrucker und Badgedrucker. 
Falls ein Drucker für eine dieser Rollen eingerichtet ist, wird er unter der entsprechenden Überschrift mit der Art der Verbindung und gegebenenfalls seiner IP-Adresse angezeigt. 

Tippen Sie neben der Anzeige des Druckers in pretixPRINT das Drei-Punkte-Menü :btn-icon:fa3-ellipsis-v:: und dann :btn:Testseite drucken:. 
Beobachten Sie, ob der Drucker wie erwartet eine Testseite produziert. 
Falls Sie mehrere Drucker von dem Android-Gerät aus ansteuern wollen, führen Sie den Schritt einmal für jeden der Drucker durch. 

Falls der Drucker keine Testseite produziert oder es dabei zu Problemen kommt, lesen Sie den Abschnitt [Problemlösung](epson.de.md#problemlosung). 
Um die gesamte Konfiguration selbst vorzunehmen, lesen Sie die beiden Unterabschnitte [Konfigurationsseite drucken](epson.de.md#konfigurationsseite-drucken) und [Drucker mit Scan-Smartphone oder Kasse verbinden](epson.de.md#drucker-mit-scan-smartphone-oder-kasse-verbinden). 

### Konfigurationsseite drucken

!!! Note 
    Falls Sie den Drucker via USB anschließen, können Sie diesen Schritt überspringen. 
    Der Drucker druckt nur bei aktiver Netzwerkverbindung automatisch eine Konfigurationsseite. 
    Sie benötigen die Konfigurationsseite nicht, da die Verbindung über USB keine IP-Adresse erfordert. 

Die Drucker produzieren innerhalb einer Minute nach dem Einschalten automatisch eine Konfigurationsseite. 
Das funktioniert nur, wenn der Drucker mit Stromversorgung und Router verbunden ist und Papier hat. 
Falls Sie erneut eine Konfigurationsseite drucken wollen, schalten Sie den Drucker aus, warten Sie einen Moment ab, und schalten Sie ihn dann wieder ein. 
Die Konfigurationsseite könnte z.B. so aussehen: 

!["Ein Streifen graublaues Belegpapier mit Text: IP Address 192.168.214.101 SubnetMask 255.255.255.0 Gateway 192.168.214.1 DHCP Enable"](../../assets/screens/hardware-setup/epson-test.jpg "Epson Konfigurationsseite des Druckers")

Die IP-Adresse des Druckers befindet sich in der Zeile, die mit `IP Address` beginnt. 
Diese IP-Adresse benötigen Sie, um Scan-Smartphones und Kassen mit den Druckern zu verbinden. 
Das wird im nächsten Abschnitt näher erklärt. 

### Drucker mit Scan-Smartphone oder Kasse verbinden

Auf Android-Geräten (Scan-Smartphone und Kasse) können Sie unsere App pretixPRINT benutzen, um Drucker anzusteuern. 
Dieser Abschnitt erklärt, wie Sie die Drucker TM-m30iii und TM-T88vii über die App verbinden und die Funktion testen. 

pretixPRINT erlaubt die Einrichtung von Druckern für drei verschiedene Verwendungszwecke: Belegdrucker, Ticketdrucker und Badgedrucker. 
Daher zeigt die App drei verschiedene Schaltflächen mit der Beschriftung "Drucker einrichten" an. 
Entscheidend ist die Überschrift oberhalb der Schaltfläche, die dem Verwendungszweck entspricht. 

Drucker für Belege und Tickets richten Sie üblicherweise an einer Kasse ein. 
Das ermöglicht es, für jede Transaktion am POS einen Kaufbeleg und die erworbenen Tickets auszudrucken. 
Badgedrucker richten Sie dagegen normalerweise am Scanner ein, um am Einlass für jede teilnehmende Person ein passendes Badge zu drucken. 

Die Drucker Epson TM-m30iii und TM-T88vii sind für die Verwendung als Belegdrucker geeignet. 
Um den Drucker als Belegdrucker mit einem Scan-Smartphone oder einer Kasse zu verbinden, öffnen Sie pretixPRINT auf dem Scan-Smartphone oder der Kasse und tippen dann unter "Belegdrucker" auf :btn:Drucker einrichten:. 

Falls der Drucker über das **Netzwerk** verbunden ist, wählen Sie auf der Seite "Wie ist Ihr Drucker verbunden?" die Option "Netzwerk (LAN/WLAN)" und tippen :btn:Weiter:. 
Geben Sie die IP-Adresse des Druckers ein. 
Das Feld "Port" können Sie in den meisten Fällen unverändert lassen. 
Tippen Sie dann :btn:Weiter:. 

Falls der Drucker über **USB** verbunden ist, wählen Sie auf der Seite "Wie ist Ihr Drucker verbunden?" die Option "USB (experimentell, funktioniert nicht auf allen Geräten)". 
Tippen Sie dann den Button :btn:Gerät auswählen: und wählen Sie den Drucker aus der Liste aus. 
Daraufhin trägt die App die Seriennummer in das entsprechende Feld ein. 
Tippen Sie dann :btn:Weiter:. 

Auf der Seite "Welches Protokoll spricht Ihr Drucker?" wählen Sie "ESC/POS-Bondrucker (z.B. Epson, Bixolon, ...)" und tippen Sie :btn:Weiter:. 
Auf der nächsten Seite wählen Sie unter Dialekt "Epson, Bixolon, Metapace, SNBC", passen Sie falls nötig die Wartezeit an, und tippen :btn:Weiter:. 

Tippen Sie :btn:Testseite drucken: und beobachten Sie, ob der verbundene Drucker wie erwartet druckt. 
Tippen Sie :btn:Einstellungen speichern:. 

!!! Note 
    Die Konfigurationsseite des Druckers und die Testseite von pretixPRINT erfüllen unterschiedliche Funktionen. 
    Die Konfigurationsseite des Druckers testet die Funktion des Druckers und enthält Informationen zur Verbindung wie die IP-Adresse. 
    Die Testseite von pretixPRINT bestätigt, dass die Verbindung zwischen dem Gerät (Kasse oder Scan-Smartphone) und dem Drucker besteht und dass die beiden Geräte mit dem richtigen Protokoll kommunizieren. 

Wiederholen Sie diese Schritte an allen Geräten, mit denen Sie drucken möchten. 
Die pretixPRINT-Testseite könnte beim Epson TM-m30iii und TM-T88vii z.B. so aussehen: 

!["Ein Streifen graublaues Belegpapier mit Text, einer Zeile zum Testen der Breite des Belegpapiers, und einem QR-Code"](../../assets/screens/hardware-setup/epson-pretixprint.jpg "pretixPRINT-Testseite aus Epson-Drucker")

Falls bei der pretixPRINT-Testseite Probleme auftauchen, werfen Sie einen Blick auf [den entsprechenden Abschnitt](epson.de.md#drucker-druckt-pretixprint-testseite-nicht) unter [Problemlösung](epson.de.md#problemlosung). 

## Problemlösung 

### Drucker druckt nicht

**Problem:** Sie können den Drucker nicht dazu bringen, zu drucken – nicht einmal seine eigene Konfigurationsseite wie beschrieben unter [Konfigurationsseite drucken](epson.de.md#Konfigurationsseite-drucken). 

**Lösung:** Stellen Sie sicher, dass: 

 - der Drucker mit Strom versorgt wird (das Netzteil/Stromkabel sollte verbunden sein und die Status-LED am Drucker sollte leuchten)
 - das passende Material eingelegt ist
 - das Material richtig eingelegt ist
 - das Gehäuse des Druckers geschlossen ist

Wenn all diese Punkte erfüllt sind, liegt möglicherweise ein technisches Problem vor. 
Lesen Sie die Dokumentation des Herstellers oder kontaktieren Sie unseren [Support](mailto:support@pretix.eu). 

### Drucker druckt pretixPRINT-Testseite nicht

**Problem:** Der Drucker druckt die eigene Konfigurationsseite zwar richtig aus, aber nicht die pretixPRINT-Testseite wie beschrieben unter [Drucker mit Scan-Smartphone oder Kasse verbinden](epson.de.md#drucker-mit-scan-smartphone-oder-kasse-verbinden). 

**Lösung:** Überprüfen Sie zuerst, ob pretixPRINT auf dem Gerät womöglich für die Benutzung mit einem anderen Drucker konfiguriert ist. 
Dazu versorgen Sie alle mitgelieferten Drucker mit Strom, Netzwerkverbindung und Druckmaterial. 
Versuchen Sie dann erneut, die pretixPRINT-Testseite zu drucken. 

Falls die Testseite nun von einem anderen Drucker ausgedruckt wird, bedeutet das, dass pretixPRINT auf dem Gerät für die Benutzung mit diesem Drucker konfiguriert ist. 
Passen Sie Ihren Hardware-Aufbau entsprechend an. 

Falls die Testseite von keinem der Drucker ausgedruckt wird, liegt ein anderes Problem vor. 
Stellen Sie sicher, dass das Gerät, auf dem pretixPRINT läuft, mit dem korrekten WLAN verbunden ist (bei von uns vermieteten Routern fängt der Netzwerkname mit `pretix-onsite` an). 

Überprüfen Sie die IP-Adresse in pretixPRINT und korrigieren Sie sie gegebenenfalls. 
Stellen Sie auch sicher, dass in pretixPRINT das richtige Protokoll ausgewählt ist (plus gegebenenfalls der richtige Dialekt). 
Die Auswahl des Protokolls hängt vom Modell des Druckers ab. 
Für mehr Informationen zu IP-Adresse und Protokoll lesen Sie den Abschnitt [Drucker mit Scan-Smartphone oder Kasse verbinden](epson.de.md#drucker-mit-scan-smartphone-oder-kasse-verbinden). 

Speichern Sie die Einstellungen in pretixPRINT und testen Sie erneut. 

### Druckauftrag kommt auf einem anderen Drucker an

**Problem:** Die pretixPRINT-Testseite oder Ihre anderen Druckaufträge werden zwar gedruckt, aber von einem anderen Drucker als erwartet. 
Die in pretixPRINT hinterlegte IP-Adresse ist also nicht die des gewünschten Druckers. 

**Lösung:** Verwenden Sie das Gerät mit dem verbundenen Drucker. 
Passen Sie Ihren Hardware-Aufbau entsprechend an. 

Alternativ können Sie die IP-Adresse auf die des gewünschten Druckers ändern. 
Speichern Sie die Einstellungen und testen Sie erneut. 

### Druckauftrag enthält Unsinn 

**Problem:** Die pretixPRINT-Testseite oder Ihre anderen Druckaufträge werden zwar ausgedruckt, enthalten aber Unsinn (z.B. Sonderzeichen oder zufällige Zeichenfolgen). 
Das deutet darauf hin, dass in pretixPRINT das falsche Protokoll für den Drucker konfiguriert ist. 

**Lösung:** Ändern Sie in pretixPRINT Protokoll und gegebenenfalls Dialekt, mit dem das Gerät den Drucker anspricht. 
Speichern Sie die Einstellungen und testen Sie erneut. 

## Weitere Informationen

 - [EPSON TM-m30ii: Inbetriebnahme ](https://www.youtube.com/watch?v=iT_66QIcY0I) auf YouTube (deutsch)
