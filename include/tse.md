Dieser Artikel erklärt den Umgang mit einer technischen Sicherheitseinrichtung (TSE) in Verbindung mit einem Gerät, auf dem pretixPOS läuft. 
Jede Kasse im deutschen Rechtsraum muss mit einer TSE ausgestattet sein. 
Wenn Sie eine Kasse von pretix oder von einem Drittanbieter gekauft haben, dann müssen Sie dort eine TSE einbauen. 
Physikalisch handelt es sich bei einer TSE meistens um eine microSD-Karte oder um einen USB-Stick. 

Wenn Sie eine Kasse inklusive TSE für den Gebrauch mit pretixPOS **mieten**, dann nehmen wir die Einrichtung bereits vollständig für Sie vor. 

## Voraussetzungen 

Sie benötigen ein Kassengerät mit der App pretixPOS und eine TSE. 

## Anleitung 

Die folgenden Abschnitte behandeln die ordnungsgemäße Einrichtung, Entfernung, und den Austausch einer TSE.

### TSE einrichten

Setzen Sie die TSE in Ihr Kassengerät ein. 
Öffnen Sie pretixPOS auf Ihrem Kassengerät, tippen Sie den Button :btn:Einstellungen: und dann :btn-icon:fa3-gavel: Fiskalisierung / Technische Sicherheitseinrichtung:. 
Falls pretixPOS einen Neustart zum Erkennen der TSE anfordert, starten Sie das Gerät neu und navigieren Sie erneut zum Menü :btn-icon:fa3-gavel: Fiskalisierung / Technische Sicherheitseinrichtung:. 
Tippen Sie den Button :btn-icon:fa3-microchip: Neue Sicherheitseinrichtung hinzufügen:. 
Wählen Sie in dem Dialog den Typ (Hersteller) der TSE, die Sie soeben eingesetzt haben, und tippen Sie :btn:OK:. 

![App pretixPOS, Dialog 'Swissbit TSE-Einrichtung' mit Hinweistext sowie Eingabefeldern für PIN, PUK, Zeitadmin-PIN und Zugangsdaten-Seed.](../../assets/screens/pos/einrichtung-swissbit.png "Swissbit TSE-Einrichtung")

Falls Ihre TSE noch nicht eingerichtet wurde, dann definieren Sie nun die Zugangsdaten. 
Welche Daten das genau sind, hängt von Hersteller und Modell der TSE ab. 
Beim Hersteller Swissbit benötigen Sie z.B. eine 5-stellige PIN, eine 6-stellige PUK, sowie eine 5-stellige Zeitadmin-PIN. 
Nähere Informationen zu den Zugangsdaten nach Hersteller und Modell der TSE finden Sie im Abschnitt Abschnitt [9.7 Fiskalisierung / Technische Sicherheitseinrichtung](https://download.pretix.eu/pretixpos.pdf#section.9.7) des pretixPOS-Nutzerhandbuchs. 

Notieren Sie diese Daten unbedingt und verwahren Sie sie an einem sicheren Ort. 
Sollten die Zugangsdaten zu einer TSE verloren gehen, dann kann sie nicht mehr benutzt werden. 

!!! Note 
    Verwahren Sie die Zugangsdaten so, dass sie nicht in die Hände von Unbefugten gelangen können. 
    Sorgen Sie aber auch dafür, dass die Daten bei Bedarf (z.B. Steuerprüfung oder Tausch der TSE) auffindbar sind, wenn Sie nicht persönlich anwesend sind. 
    Treffen Sie Vorkehrungen für den Fall, dass sich Ihre Zuständigkeit ändert (z.B. wenn Sie Ihren Job wechseln). 

Falls Ihre TSE bereits eingerichtet wurde, dann geben Sie die bereits in der TSE konfigurierten Zugangsdaten ein. 

In beiden Fällen stellen Sie sicher, dass die eingegebenen Daten mit den notierten Daten übereinstimmen und tippen dann :btn:OK:. 
Es dauert einen Moment, die TSE einzurichten. 

!!! Warning 
    Während pretixPOS die TSE einrichtet, dürfen Sie sie **auf keinen Fall** entfernen, die App beenden, oder die Kasse ausschalten. 
    Dies kann dazu führen, dass die TSE unbrauchbar wird. 

Sobald pretixPOS damit fertig ist, die TSE einzurichten, werden Sie auf die Seite mit dem Titel "Sicherheitseinrichtung verwalten" geleitet. 
Melden Sie Ihre Kasse nun beim Finanzamt an oder aktualisieren Sie die dort hinterlegten Angaben. 
Für mehr Informationen lesen Sie den Artikel zur [Anmeldung von Kassen in Deutschland](register.md). 
Nachdem Sie das getan haben, können Sie Kasse und TSE für den regulären Betrieb verwenden. 

### TSE-Speicher exportieren 

Wenn eine Steuerprüfung ansteht oder wenn Sie die TSE außer Betrieb nehmen wollen, dann sollten Sie den TSE-Speicher exportieren. 
Um dies zu tun, öffnen Sie auf Ihrem Kassengerät pretixPOS, tippen Sie den Button :btn:Einstellungen:, dann :btn-icon:fa3-gavel: Fiskalisierung / Technische Sicherheitseinrichtung:, und dann :btn-icon:fa3-microchip: Sicherheitseinrichtung verwalten:. 
Tippen Sie :btn:TSE-Speicher exportieren:.
Wählen Sie einen Ordner auf dem Kassengerät aus, in den die TSE-Daten exportiert werden sollen.

Sichern Sie die Exportdatei mindestens auf einem zweiten Gerät. 
Da diese Exportdatei für Ihre Buchhaltung relevant ist, sollten Sie sie genau so archivieren, wie Ihre sonstigen Buchhaltungsdaten. 
Sie können die Datei beispielsweise mit einem USB-Stick oder einer SD-Speicherkarte auf ein anderes Gerät übertragen. 
Achten Sie darauf, dass die Exportdatei später leicht aufgefunden und zugeordnet werden kann. 

### TSE entfernen

Um eine TSE ordnungsgemäß zu entfernen, öffnen Sie auf Ihrem Kassengerät pretixPOS, tippen Sie den Button :btn:Einstellungen:, dann :btn-icon:fa3-gavel: Fiskalisierung / Technische Sicherheitseinrichtung:, und dann :btn-icon:fa3-microchip: Sicherheitseinrichtung verwalten:. 
Tippen Sie den Button :btn:Gerät abmelden:. 
In dem sich daraufhin öffnenden Dialog geben Sie die PIN der TSE ein. 
Sie können die Kasse nun ausschalten und die TSE entfernen. 
Danach können Sie sie wieder wie unter [TSE einrichten](tse.md#tse-einrichten) beschrieben an einer Kasse anmelden. 

Falls Sie die Kasse außer Betrieb nehmen und nicht sofort eine neue TSE einsetzen, dann melden Sie das nun dem Finanzamt. 
Für mehr Informationen lesen Sie den Artikel zur [Anmeldung von Kassen in Deutschland](register.md). 

### TSE tauschen

Um eine TSE zu tauschen, folgen Sie zunächst den Schritten unter [TSE-Speicher exportieren](tse.md#tse-speicher-exportieren), um die Daten der alten TSE zu exportieren. 
Nachdem der Export abgeschlossen ist, folgen Sie den Schritten unter [TSE entfernen](tse.md#tse-entfernen) und entfernen die alte TSE. 
Falls Sie daraufhin sofort eine neue TSE einsetzen, müssen Sie dem Finanzamt zu diesem Zeitpunkt noch nicht Meldung machen. 

Nachdem die TSE entfernt ist, folgen Sie den Schritten unter [TSE einrichten](tse.md#tse-einrichten) und nehmen die neue TSE in Betrieb. 
Aktualisieren Sie jetzt die Anmeldung Ihrer Kasse beim Finanzamt. 
Für mehr Informationen lesen Sie den Artikel zur [Anmeldung von Kassen in Deutschland](register.md). 
Nachdem Sie das getan haben, können Sie die Kasse mit der neuen TSE für den regulären Betrieb verwenden. 

## Weiterführende Informationen 

Für nähere Informationen zu pretixPOS konsultieren Sie das [pretixPOS-Nutzerhandbuch](https://download.pretix.eu/pretixpos.pdf). 