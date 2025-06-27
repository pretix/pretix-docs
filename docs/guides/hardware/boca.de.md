# Drucker einrichten: Boca Lemur und Boca Lemur C 

Bei diesem Artikel handelt es sich um eine Schnellstart-Anleitung für die Verwendung von Druckern der Marke Boca zusammen mit pretix. 
Er erklärt, wie Sie den Drucker aufbauen und über die App pretixPRINT mit Scan- und Kassengeräten verbinden. 

Note !!! 
    Diese Seite ersetzt nicht die Dokumentation für die Geräte selbst. 
    Informieren Sie sich auf der Webseite des Herstellers über die Modelle [Boca Lemur](https://tls-bocasystems.com/de/225/lemur/) und [Boca Lemur C](https://tls-bocasystems.com/de/232/lemur-c/). 

Die Geräte Lemur und Boca Lemur C unterscheiden sich in der Bedienung nur in folgenden Punkten voneinander: 

 - Stromversorgung (Lemur: integriertes Netzteil und Kaltgeräteanschluss. Lemur C: externes Netzteil) 
 - Position der Buttons und LEDs (Lemur: linke Seite. Lemur C: rechte Seite) 
 - Bildschirm (der Lemur besitzt einen Bildschirm, der Lemur C nicht)
 - maximale Druckbreite (Lemur: 101mm, Lemur C: 82mm)

## Voraussetzungen

Für die Stromversorgung des Geräts benötigen Sie eine Steckdose in der Nähe. 
Für die Netzwerkverbindung brauchen Sie einen Router mit einem freien LAN-Anschluss oder eine alternative Lösung. 
Sie benötigen bedruckbares Thermopapier, z.B. in Form von Tickets oder Butterfly-Badges, mit einer Breite von 50mm bis 82mm (Lemur C) oder 50mm bis 101mm (Lemur) und einer schwarzen Steuermarke auf der Rückseite. 

## Anleitung

Sie können den Lemur und den Lemur C als Ticketdrucker oder als Badgedrucker verwenden. 
Unabhängig von der genauen Anwendung müssen Sie Ihren Drucker mit Strom, einer Netzwerkverbindung und bedruckbarem Material versorgen. 
Dann drucken Sie eine Testseite. 
Schließlich verbinden Sie den Drucker über unsere App pretixPRINT mit der Kasse oder den Scannern. 
Diese Schritte werden im folgenden genauer erklärt. 

#### Drucker anschließen

Stecken Sie ein LAN-Kabel in die Buchse mit der Aufschrift "ETHERNET" an der Rückseite des Druckers. 
Stecken Sie das andere Ende des LAN-Kabels in den freien LAN-Anschluss an Ihrem Router. 

**Lemur:** Verbinden Sie den Stromanschluss des Routers über ein Kaltgerätekabel mit einer Steckdose. 
**Lemur C:** Schließen Sie das Netzteil an den Drucker und an eine Steckdose an. 

Schalten Sie das Gerät ein, indem Sie den Schalter an der rechten Seite umlegen. 
Beim Lemur ist der Schalter in einer Nische verborgen. 
Daraufhin sollten der Bildschirm (nur Lemur) und mindestens eine LED an der Seite des Druckers aufleuchten. 

Legen Sie Ihr Druckmaterial so bereit, dass die bedruckbare Seite nach oben zeigt und die schwarzen quadratischen Markierungen an dem Ende liegen, das weiter vom Drucker entfernt ist. 
Schieben Sie das Papier in den Drucker, bis dieser das Papier automatisch einzieht. 
Falls der Drucker mit einer Schneideeinrichtung ausgestattet ist (Lemur: manche, Lemur C: alle), schneidet er das erste Ticket bzw. den ersten Badge ab. 

#### Testseite drucken

Um eine Testseite auszudrucken, drücken Sie an der Seite des Geräts den Button mit dem Label "TEST". 
Die Testseite könnte z.B. so aussehen: 

!["Ein weißes Ticket mit lila Randstreifen, glänzendem pretix-Logo und schwarzem Aufdruck. Der Testdruck enthält Text in verschiedenen Schriftarten sowie Barcodes. Die IP-Adresse lautet 192.168.214.142"](../../assets/screens/hardware-setup/boca-test.jpg "Boca Testseite des Druckers")

Die IP-Adresse befindet sich im oberen linken Viertel des Ausdrucks in der Zeile, die mit `IP ADD=` beginnt. 
Diese IP-Adresse benötigen Sie, um Scan-Smartphones und Kassen mit den Druckern zu verbinden. 
Das wird im nächsten Abschnitt näher erklärt. 

#### Drucker mit Scan-Smartphone oder Kasse verbinden

Auf den Android-Geräten (Scan-Smartphone und Kasse) können Sie unsere App pretixPRINT benutzen, um Drucker anzusteuern. 
Dieser Abschnitt erklärt Ihnen, wie Sie die Drucker Lemur und Lemur C über die App verbinden und die Funktion testen. 

pretixPRINT erlaubt die Einrichtung von Druckern für drei verschiedene Verwendungszwecke: Belegdrucker, Ticketdrucker und Badgedrucker. 
Daher zeigt die App drei verschiedene Schaltflächen mit der Beschriftung "Drucker einrichten" an. 
Entscheidend ist die Überschrift oberhalb der Schaltfläche, die dem Verwendungszweck entspricht. 

Beleg- und Ticketdrucker richten Sie üblicherweise an einer Kasse ein. 
Das ermöglicht es, für jede Transaktion am POS einen Kaufbeleg und die erworbenen Tickets auszudrucken. 
Den Badgedrucker richten Sie dagegen am Scanner ein, um am Einlass für jede teilnehmende Person einen passenden Badge zu drucken. 

Sie können die Drucker Lemur und Lemur C sowohl als Ticketdrucker als auch als Badgedrucker verwenden. 
Um den Drucker als Ticketdrucker mit einer Kasse zu verbinden, öffnen Sie pretixPRINT auf der Kasse und tippen dann unter "Ticketdrucker" auf :btn:Drucker einrichten. 
Um den Drucker als Badgedrucker mit einem Scan-Smartphone zu verbinden, öffnen Sie pretixPRINT auf dem Smartphone und tippen dann unter "Badgedrucker" auf :btn:Drucker einrichten. 
Unabhängig von Ihrer Auswahl ist der Prozess danach immer der gleiche. 

Wenn der Drucker über das Netzwerk verbunden ist, wählen Sie auf der Seite "Wie ist Ihr Drucker verbunden?" die Option "Netzwerk (LAN/WLAN)" und tippen :btn:Weiter:. 
Geben Sie die IP-Adresse des Routers ein. 
Das Feld "Port" können Sie in den meisten Fällen unverändert lassen. 
Tippen Sie dann :btn:Weiter:. 

Auf der Seite "Welches Protokoll spricht Ihr Drucker?" wählen Sie "FGL-Ticketdrucker (z.B. Boca, Practical Automation, ...)" und tippen Sie :btn:Weiter:. 
Lassen Sie auf der nächsten Seite unter "DPI" die Eingabe `200` unverändert, da der Drucker nur 200 DPI unterstützt. 
Nehmen Sie hier gegebenenfalls Feineinstellungen vor und tippen Sie erneut :btn:Weiter:. 

Tippen Sie :btn:Testseite drucken: und beobachten Sie, ob der verbundene Drucker wie erwartet druckt. 
Tippen Sie :btn:Einstellungen speichern:. 

!!! Note 
    Die Testseite des Druckers und die Testseite von pretixPRINT erfüllen unterschiedliche Funktionen. 
    Die Testseite des Druckers testet die Funktion des Druckers und enthält Informationen zur Verbindung wie die IP-Adresse. 
    Die Testseite von pretixPRINT bestätigt, dass die Verbindung zwischen dem Gerät (Kasse oder Scan-Smartphone) und dem Drucker besteht und dass die beiden Geräte mit dem richtigen Protokoll kommunizieren. 

Wiederholen Sie diese Schritte an allen Geräten, mit denen Sie drucken möchten. 
Die pretixPRINT-Testseite könnte beim Lemur und Lemur C z.B. so aussehen: 

!["Ein weißes Ticket mit lila Randstreifen, glänzendem pretix-Logo und schwarzem Aufdruck. Der Testdruck enthält Text in verschiedenen Schriftgrößen, Muster, Streifen und pretix-Logos."](../../assets/screens/hardware-setup/boca-pretixprint.jpg "pretixPRINT-Testseite aus Boca-Drucker")

Falls bei der pretixPRINT-Testseite Probleme auftauchen, werfen Sie einen Blick auf [den entsprechenden Abschnitt](boca.de.md#drucker-druckt-pretixprint-testseite-nicht) unter [Problemlösung](boca.de.md#problemlösung). 

## Problemlösung 

#### Drucker druckt die eigene Testseite nicht

**Problem:** Sie können einen Drucker nicht dazu bringen können, seine eigene Testseite zu drucken wie beschrieben unter [Testseite drucken](boca.de.md#testseite-drucken). 

**Lösung:** Überprüfen Sie: 

 - ob der Drucker mit Strom versorgt wird (das Netzteil/Stromkabel sollte verbunden sein und Status-LED oder Display am Drucker sollten leuchten)
 - ob das passende Material eingelegt ist
 - ob das Material richtig eingelegt ist
 - ob das Gehäuse des Druckers geschlossen ist

Wenn all diese Punkte erfüllt sind, liegt möglicherweise ein technisches Problem vor. 
Lesen Sie die Dokumentation des Herstellers oder kontaktieren Sie unseren [Support](mailto:support@pretix.eu). 

#### IP-Adresse auf der Testseite lautet 0.0.0.0 

**Problem:** Die Testseite des Druckers liefert als IP-Adresse `0.0.0.0` oder ein ähnlich unbrauchbares Ergebnis. 

**Lösung:** Der Drucker ist nicht mit dem Netzwerk verbunden. 
Prüfen Sie, ob das LAN-Kabel richtig in der Buchse des Druckers steckt. 
Prüfen Sie, ob das andere Ende desselben LAN-Kabels in der LAN-Buchse (**nicht** in der WAN-Buchse) des Routers steckt. 
Verwenden Sie gegebenenfalls ein anderes Kabel. 

Geben Sie dem Drucker etwa eine Minute Zeit, um sich mit dem Netzwerk zu verbinden. 
Drucken Sie dann eine neue Testseite aus, um die korrekte IP-Adresse zu erhalten. 

#### Drucker druckt pretixPRINT-Testseite nicht

**Problem:** Der Drucker druckt die eigene Testseite zwar richtig aus, aber nicht die pretixPRINT-Testseite wie beschrieben unter [Drucker mit Scan-Smartphone oder Kasse verbinden](boca.de.md#drucker-mit-scan-smartphone-oder-kasse-verbinden). 

**Lösung:** Überprüfen Sie: 

 - ob das Gerät, auf dem pretixPRINT läuft, mit dem korrekten WLAN verbunden ist (SSID fängt an mit `pretix-onsite`)
 - ob die IP-Adresse in pretixPRINT korrekt ist
 - ob in pretixPRINT das richtige Protokoll ausgewählt ist (plus gegebenenfalls der richtige Dialekt) 

Speichern Sie die Einstellungen in pretixPRINT und testen Sie erneut. 

#### Druckauftrag kommt auf einem anderen Drucker an

**Problem:** Die pretixPRINT-Testseite oder Ihre anderen Druckaufträge werden zwar gedruckt, aber von einem anderen Drucker als erwartet. 

**Lösung:** Die in pretixPRINT hinterlegte IP-Adresse ist nicht die des gewünschten Druckers. 
Verwenden Sie das Gerät mit dem verbundenen Drucker. 
Passen Sie Ihren Hardware-Aufbau entsprechend an. 

Alternativ können Sie die IP-Adresse auf die des gewünschten Druckers ändern. 
Speichern Sie die Einstellungen und testen Sie erneut. 

#### Druckauftrag enthält Unsinn 

**Problem:** Die pretixPRINT-Testseite oder Ihre anderen Druckaufträge werden zwar ausgedruckt, enthalten aber Unsinn (z.B. Sonderzeichen oder zufällige Zeichenfolgen). 

**Lösung:** In pretixPRINT ist das falsche Protokoll für den Drucker konfiguriert. 
Ändern Sie in pretixPRINT Protokoll und gegebenenfalls Dialekt, mit dem das Gerät den Drucker anspricht. 
Speichern Sie die Einstellungen und testen Sie erneut. 

## Weitere Informationen

 - [Boca Lemur: Inbetriebname](https://www.youtube.com/watch?v=w5n8h9GMDyg) auf YouTube (deutsch)
 - [Boca Lemur: Öffnen des Druckkopfs](https://www.youtube.com/watch?v=xmT-tPVkHhs) auf YouTube (deutsch)
 - [Boca Lemur C: Öffnen des Druckkopfs]( https://www.youtube.com/watch?v=zjdRD_SUmhA) auf YouTube (deutsch)