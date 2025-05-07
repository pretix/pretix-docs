Dieser Artikel erklärt den Umgang mit einer technischen Sicherheitseinrichtung (TSE) in Verbindung mit einem Gerät, auf dem pretixPOS läuft. 
Jede Kasse im deutschen Rechtsraum muss mit einer TSE ausgestattet sein. 
Wenn Sie eine Kasse von pretix oder von einem Drittanbieter gekauft haben, dann müssen Sie dort eine TSE einbauen. 
Physikalisch handelt es sich bei einer TSE meistens um eine microSD-Karte oder um einen USB-Stick. 

Wenn Sie eine Kasse inklusive TSE für den Gebrauch mit pretixPOS **mieten**, dann nehmen wir die Einrichtung bereits fertig für Sie vor. 

## Voraussetzungen 

Sie benötigen ein Kassengerät mit der App pretixPOS und eine TSE. 

## Anleitung 

Die folgenden Abschnitte behandeln die ordnungsgemäße Einrichtung, Entfernung, und das Tauschen einer alten TSE gegen eine neue. 

### TSE einrichten

Setzen Sie die TSE in Ihr Kassengerät ein. 
Schalten Sie die Kasse ein, öffnen Sie pretixPOS, tippen Sie den Button :btn:Einstellungen: und dann :btn-icon:fa3-gavel: Fiskalisierung / Technische Sicherheitseinrichtung:. 
Tippen Sie den Button :btn-icon:fa3-microchip: Neue Sicherheitseinrichtung hinzufügen:. 
Wählen Sie in dem Dialog den Typ (Hersteller) der TSE, die Sie soeben eingesetzt haben, und tippen Sie :btn:OK:. 

Falls Ihre TSE noch nie zuvor benutzt wurde, dann definieren Sie nun die Zugangsdaten. 
Welche Daten das genau sind, hängt von Hersteller und Modell der TSE ab. 
Beim Hersteller Swissbit benötigen Sie z.B. eine 5-stellige PIN, eine 6-stellige PUK, sowie eine 5-stellige Zeitadmin-PIN. 
Nähere Informationen zu den Zugangsdaten nach Hersteller und Modell der TSE finden Sie im Abschnitt Abschnitt [9.7 Fiskalisierung / Technische Sicherheitseinrichtung](https://download.pretix.eu/pretixpos.pdf#section.9.7) des pretixPOS-Nutzerhandbuchs. 

Notieren Sie diese Daten unbedingt und verwahren Sie sie an einem sicheren Ort. 
Sollten die Zugangsdaten zu einer TSE verloren gehen, dann kann sie nicht mehr benutzt werden. 

!!! Note 
    Verwahren Sie die Zugangsdaten so, dass sie nicht in die Hände von Unbefugten gelangen können. 
    Sorgen Sie aber auch dafür, dass die Daten bei Bedarf (z.B. Steuerprüfung oder Tausch der TSE) auffindbar sind, wenn Sie nicht persönlich anwesend sind. 
    Treffen Sie Vorkehrungen für den Fall, dass sich Ihre Zuständigkeit ändert (z.B. wenn Sie Ihren Job wechseln). 

Falls Ihre TSE schon einmal benutzt wurde, dann geben Sie die bereits in der TSE konfigurierten Zugangsdaten ein. 

In beiden Fällen stellen Sie sicher, dass Sie die richtigen Daten eingegeben haben und tippen dann :btn:OK:. 
Es dauert einen Moment, die TSE einzurichten. 

!!! Warning 
    Während pretixPOS die TSE einrichtet, dürfen Sie sie **auf keinen Fall** entfernen, die App beenden, oder die Kasse ausschalten. 
    Dies kann dazu führen, dass die TSE unbrauchbar wird. 

Sobald pretixPOS damit fertig ist, die TSE einzurichten, werden Sie auf die Seite mit dem Titel "Sicherheitseinrichtung verwalten" geleitet. 
Für die weiteren Optionen auf dieser Seite konsultieren Sie den Abschnitt [9.7 Fiskalisierung / Technische Sicherheitseinrichtung](https://download.pretix.eu/pretixpos.pdf#section.9.7) im pretixPOS-Nutzerhandbuch. 

Melden Sie Ihre Kasse nun beim Finanzamt an oder aktualisieren Sie die Angaben. 
TK nach dem Mergen auf register.md verlinken
Nachdem Sie das getan haben, können Sie Kasse und TSE für den regulären Betrieb verwenden. 

### TSE-Speicher exportieren 

Wenn eine Steuerprüfung ansteht oder wenn Sie die TSE außer Betrieb nehmen wollen, dann sollten Sie den TSE-Speicher exportieren. 
Um dies zu tun, öffnen Sie auf Ihrem Kassengerät pretixPOS, tippen Sie den Button :btn:Einstellungen:, dann :btn-icon:fa3-gavel: Fiskalisierung / Technische Sicherheitseinrichtung:, und dann :btn-icon:fa3-microchip: Sicherheitseinrichtung verwalten:. 
Tippen Sie :btn:TSE-Speicher exportieren:.
Wählen Sie einen Ordner auf dem Kassengerät aus, in den die TSE-Daten exportiert werden sollen.

Sichern Sie die Exportdatei mindestens auf einem zweites Gerät. 
Im besten Fall archivieren Sie die Exportdatei genau so, wie Sie auch Ihre Buchhaltungsdaten archivieren. 
Sie können die Datei beispielsweise mit einem USB-Stick oder einer SD-Speicherkarte auf ein anderes Gerät übertragen. 

### TSE entfernen

Um eine TSE zu entfernen, öffnen Sie auf Ihrem Kassengerät pretixPOS, tippen Sie den Button :btn:Einstellungen:, dann :btn-icon:fa3-gavel: Fiskalisierung / Technische Sicherheitseinrichtung:, und dann :btn-icon:fa3-microchip: Sicherheitseinrichtung verwalten:. 
Tippen Sie den Button :btn:Gerät abmelden:. 
In dem sich daraufhin öffnenden Dialog geben Sie die PIN der TSE ein. 
Schalten Sie die Kasse aus und entfernen Sie die TSE. 
Sie können sie nun an einer anderen Kasse oder erneut an derselben Kasse anmelden. 

Falls Sie die Kasse außer Betrieb nehmen und nicht sofort eine neue TSE einsetzen, dann melden Sie das nun dem Finanzamt. 
TK nach dem Mergen auf register.md verlinken

### TSE tauschen

Um eine TSE zu tauschen, folgen Sie zunächst den Schritten unter [TSE-Speicher exportieren](tse.md#tse-speicher-exportieren), um die Daten der alten TSE zu exportieren. 
Nachdem der Export abgeschlossen ist, folgen Sie den Schritten unter [TSE entfernen](tse.md#tse-entfernen) und entfernen die alte TSE. 
Nachdem die TSE entfernt ist, folgen Sie den Schritten unter [TSE einrichten](tse.md#tse-einrichten) und nehmen die neue TSE in Betrieb. 
Aktualisieren Sie die Anmeldung Ihrer Kasse beim Finanzamt. 
TK nach dem Mergen auf register.md verlinken
Nachdem Sie das getan haben, können Sie die Kasse mit der neuen TSE für den regulären Betrieb verwenden. 