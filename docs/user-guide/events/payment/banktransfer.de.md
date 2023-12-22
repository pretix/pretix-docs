# Banküberweisung

Um Zahlungen per Banküberweisung zu akzeptieren, müssen Sie nur ein wichtiges Feld in den Einstellungen von pretix ausfüllen: Unter "Bank
Kontodaten" sollten Sie alles angeben, was man wissen muss, um Ihnen Geld zu überweisen, z.B. Ihre IBAN und BIC,
den Namen Ihrer Bank und bei Auslandsüberweisungen möglichst auch Ihre Adresse und die Adresse der Bank.

pretix teilt dem Nutzer automatisch mit, dass er den Auftragscode in die Zahlungsreferenz aufnehmen soll, damit eingehende Überweisungen
automatisch den Zahlungen zugeordnet werden können.

## Importieren von Zahlungsdaten

Der einfachste Weg, Zahlungsdaten zu importieren, ist der Download einer CSV-Datei aus Ihrem Online-Banking. Die meisten Banken bieten einen CSV
Export in irgendeiner Form an. Sie können in pretix unter "Bankdaten importieren" eine neue Datei hochladen:

![Bankdaten hochladen](img/bank1.png)

Wenn Sie eine Datei zum ersten Mal hochladen, weiß pretix nicht, welche Informationen in welcher Spalte enthalten sind, da jede
Bank völlig unterschiedliche CSV-Dateien erstellt. Daher wird pretix Sie nach diesen Informationen fragen. Es zeigt Ihnen die
Daten der von Ihnen importierten Datei und fordert Sie auf, die Bedeutung der Spalten zu definieren. Sie können eine Spalte auswählen, die das
Sie können eine Spalte auswählen, die das Zahlungsdatum enthält und eine, die den gezahlten Betrag enthält. Sie können mehrere Spalten auswählen, die Informationen enthalten
über den Zahler oder die Zahlungsreferenz enthalten. Alle anderen Spalten werden ignoriert.


Sobald Sie fortfahren, wird pretix versuchen, die Zahlungen automatisch den jeweiligen Aufträgen zuzuordnen. Es wird Ihnen mitgeteilt, wie
viele Aufträge korrekt verarbeitet werden konnten und wie viele nicht. Sie können dann zurück zur Upload-Seite gehen, um sich alle
Überweisungen aus Ihrem Kontoauszug zu sehen, die noch nicht einem Auftrag zugeordnet werden konnten. Über das Eingabefeld und die Schaltflächen auf der
auf der linken Seite jeder Transaktion können Sie manuell einen Auftragscode eingeben, um die Transaktion zuzuordnen, oder sie einfach aus der Liste streichen, z. B.
wenn die Transaktion überhaupt nicht mit der Veranstaltung in Verbindung steht.


!!! tip

    Wenn Sie sich nicht scheuen, etwas technischer zu werden und Ihre Bank das HBCI/FinTS-Protokoll unterstützt (wie die meisten
    deutschen Banken), können Sie [pretix-bankool](https://github.com/pretix/pretix-banktool) verwenden, um diesen Prozess vollständig zu automatisieren.
