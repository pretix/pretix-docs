# Banküberweisung

Banküberweisungen sind eine der zahlreichen Möglichkeiten, in pretix Zahlungen abzuwickeln.
Zahlungen per Banküberweisung gehen direkt auf Ihrem Bankkonto ein.
Standardmäßig überwacht pretix nicht, welche Zahlungen auf Ihrem Bankkonto eingehen.
Wenn Sie pretix Hosted nutzen, können Sie Ihr Bankkonto über unsere Integration mit GoCardless verbinden, damit Bankdaten automatisch importiert werden.

Sie haben folgende Alternativen, um pretix über Zahlungseingänge zu informieren: Sie geben Zahlungen manuell als abgeschlossen frei oder Sie importieren regelmäßig digitale Kontoauszüge.
Dieser Artikel erklärt, wie Sie die Verbindung zu einem Bankkonto einrichten, um darauf Zahlungen über pretix zu empfangen.
Sie erfahren außerdem, wie Sie pretix über Zahlungseingänge informieren.

!!! Hinweis
    pretix führt keine automatischen Erstattungen per Überweisung durch.
    Wenn ein Kund\*in eine Bestellung storniert, die Erstattung über die zuvor verwendete Zahlungsmethode erhalten möchte und diese Zahlungsmethode eine Banküberweisung war, werden Sie per E-Mail benachrichtigt.
    Sie müssen die Erstattung dann manuell vornehmen.

## Voraussetzungen

Sie richten Zahlungsdienstleister auf Veranstaltungsebene ein. Zuerst müssen Sie also eine Veranstaltung anlegen.
Sie benötigen Zugriff auf das Bankkonto, das Sie mit pretix verwenden möchten.

## Anleitung

Folgende Schritte sind erforderlich, um in pretix Banküberweisungen als Zahlungsmethode zu nutzen:

 1. Zum Einrichten von Banküberweisungen die Erweiterung für Banküberweisungen aktivieren und die Einstellungen für die Überweisungen anpassen
 2. Den automatischen Import von Transaktionen einrichten **oder** regelmäßig digitale Kontoauszüge importieren
 3. Transaktionen manuell freigeben
 4. Transaktionen manuell bearbeiten

Dieser Abschnitt erklärt diese Schritte ausführlich.

### Banküberweisungen einrichten

Wenn Sie in pretix Zahlungen per Banküberweisung erhalten möchten, muss die Erweiterung "Banküberweisung" aktiviert sein.
Sie prüfen folgendermaßen nach, ob die Erweiterung aktiv ist: Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Erweiterungen:.
Wechseln Sie zum Reiter :btn:Zahlungsdienstleister:.

Auf dieser Seite wird die Erweiterung "Banküberweisung" oben angezeigt.
Sie sollte standardmäßig aktiv sein.
Wenn sie aktiv ist, hat sie ein grünes Tag ":fa3-check: Aktiv", einen weißen Button "Deaktivieren" und zwei Dropdown-Menüs.
Wenn sie inaktiv ist, fehlt das Tag und es gibt einen violetten Button :btn:Aktivieren:.
Vergewissern Sie sich, dass die Erweiterung aktiv ist.

![Seite 'Zahlungseinstellungen'. Der Reiter 'Zahlungsdienstleister' ist geöffnet und zeigt eine Liste mit den folgenden Einträgen: Banküberweisung, Wertgutschein, PayPal, SEPA-Lastschrift und Stripe. Die Option 'Wertgutschein' ist aktiv, alle anderen Einträge sind inaktiv. Neben allen Einträgen ist ein Button 'Einstellungen'.](../../assets/screens/payment-providers/payment-settings.png "Zahlungseinstellungen" )

Sie können direkt zu den Einstellungen für Banküberweisungen springen, indem Sie das Dropdown-Menü :btn-icon:fa3-gear:Einstellungen: und anschließend :btn:Zahlung > Banküberweisung: klicken.

Alternativ navigieren Sie zu :navpath:Ihre Veranstaltung →  :fa3-wrench: Einstellungen → Zahlung:.
Der Reiter :btn:Zahlungsdienstleister: auf dieser Seite zeigt die Liste aktiver Zahlungsdienstleister.
Die Liste sollte jetzt einen Eintrag für Banküberweisungen mit einem roten Tag ":fa3-remove: Deaktiviert" enthalten.

Die Erweiterung ist zwar aktiv, aber Sie haben Banküberweisungen für die Veranstaltung noch nicht als Zahlungsdienstleister eingerichtet.
Klicken Sie den Button :btn-icon:fa3-gear:Einstellungen: neben "Banküberweisung".
Dadurch gelangen Sie zu der Seite, auf der Sie Banküberweisungen einrichten.

Wählen Sie den "Kontotyp".
Wenn Sie "SEPA-Bankkonto" wählen, müssen Sie den Namen von Kontoinhaber\*in, IBAN, BIC und den Namen der Bank angeben.
Wenn Sie "Anderes Bankkonto" wählen, müssen Sie in den Feldern bei "Angaben zum Bankkonto" die vollständigen Angaben der Bankverbindung eintragen.

Alle Einstellungen weiter unten auf der Seite sind optional.
Sehen Sie sich die Seite genau an und aktivieren Sie alle Einstellungen, die Sie für Ihre Veranstaltung für diesen Zahlungsdienstleister wünschen.
Wenn alles wie gewünscht eingerichtet ist, blättern Sie zum Seitenanfang. Dort kreuzen Sie das Kontrollkästchen an, mit dem Sie bestätigen, dass Sie verstanden haben, wie Banküberweisungen in pretix funktionieren, und auch das Kontrollkästchen neben "Zahlungsmethode aktivieren".
Den Kund\*innen stehen in Ihrem Shop nun Banküberweisungen als Zahlungsoption zur Verfügung.

### Zahlungseingänge automatisch überwachen

Für pretix Hosted arbeiten wir mit [GoCardless](https://gocardless.com) zusammen, um eine nahtlose Integration zu gewährleisten. Dadurch können Sie bei [mehreren Tausend Banken in über 30 Ländern](https://gocardless.com/bank-account-data/coverage/) Transaktionen automatisch importieren.
Alternativ haben Sie die Möglichkeit, regelmäßig digitale Kontoauszüge zu importieren, um pretix über Zahlungseingänge zu informieren.
Dieser Abschnitt erläutert die Vorgehensweise bei beiden Optionen.

#### Option A: Transaktionen mit GoCardless automatisch importieren

<!-- md:hosted -->

Wenn Sie pretix Hosted nutzen, können Sie den automatischen Import von Transaktionen über die pretix-Integration mit GoCardless aktivieren.
Diese Funktion gilt auf Veranstalterebene. Das bedeutet, dass die über dieses Verfahren importierten Bankdaten für alle Veranstaltungen des Veranstalters verfügbar sind.
Navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-bank: Banküberweisung → Automatischer Import:.

![Seite mit dem Titel 'Automatischer Import von Transaktionen'. Die Seite enthält Text mit den Unterüberschriften 'Warum Transaktionen automatisch importieren?', 'Nicht zugeordnete Zahlungen' und 'Sicherheit und Datenschutz', außerdem einen Button, um nicht zugeordnete Zahlungen zur Prüfung hochzuladen.](../../assets/screens/payment/automatic-transaction-import.png "Automatischer Import von Transaktionen" )

Wählen Sie Ihr Land, Ihre Bank und das Datum, ab dem Sie Transaktionen importieren möchten.
Wenn Sie das Feld "Transaktionen importieren seit" leer lassen, importiert pretix so viele Transaktionen wie möglich.
Das sind in der Regel alle Transaktionen der letzten 90 Tage.

Dies kann zu Problemen führen, falls Sie Bankdaten bisher mit einem anderen Verfahren in dasselbe Veranstalterkonto importiert haben.
Möglicherweise sind die Daten unterschiedlich formatiert, wodurch die Software Transaktionen eventuell nicht als identisch erkennt.
Wenn das bei Ihnen der Fall ist, wählen Sie den ersten Tag, für den Sie in dieses Veranstalterkonto noch keine Bankdaten importiert haben.
Lassen Sie keine Lücke zwischen alten und neuen Importen, etwa wenn Sie für einen Tag bereits vor dem Buchungsschluss Daten importiert haben.

Falls Sie bisher noch kein anderes Verfahren für den Import von Bankdaten verwendet haben, können Sie dieses Feld leer lassen.

Klicken Sie den Button :btn-icon:fa3-sign-in: Mit Bank verbinden:.
Damit gelangen Sie zu einer Webseite bei ob.gocardless.com, die Sie auffordert, der Verarbeitung Ihrer Daten durch GoCardless zuzustimmen und die Anmeldedaten für Ihre Bank einzugeben.
Befolgen Sie zum Abschluss der Autorisierung die Anweisungen der Website.
Die Website leitet Sie dann wieder zurück zum Backend von pretix.

Wenn Ihr GoCardless-Konto Angaben für mehrere Konten bei derselben Bank enthält, müssen Sie das Bankkonto wählen, aus dem Sie Daten importieren möchten.
Wählen Sie ein Startdatum zum Import der Transaktionen und bestätigen Sie den Vorgang, indem Sie den Button :btn:Mit Bank verbinden: klicken.
Wenn Sie jetzt zurück zur Seite "Automatischer Import" navigieren, werden dort die Bankkonten angezeigt, die Sie auf der vorigen Seite als verbunden gewählt haben.
Wenn der automatische Import aktiv ist, sollten Sie gelegentlich nachsehen, ob es ungeklärte Transaktionen gibt.

Die häufigste Ursache für ungeklärte Transaktionen sind falsch geschriebene oder fehlende Bestellnummern im Verwendungszweck.
Falls das Bankkonto auch für Transaktionen genutzt wird, die nichts mit Verkäufen über pretix zu tun haben, entstehen auch dadurch ungeklärte Transaktionen.
pretix gibt Ihnen die Möglichkeit, diese Transaktionen manuell zu verarbeiten.
Der folgende Abschnitt erklärt, wie Sie [ungeklärte Transaktionen manuell verarbeiten](bank-transfer.md#handling-unresolved-transactions).

#### Option B: Bankdaten importieren

Besorgen Sie sich einen Export der Transaktionsdaten Ihres Bankkontos.
Dieser Export muss eine Datei im Format CSV oder MT940 sein.
Sie muss folgende Angaben enthalten:

 - Datum
 - Betrag
 - Verwendungszweck
 - Zahler\*in
 - IBAN
 - BIC

Geben Sie bei "Zahler\*in" den Namen der Person an, von der die Zahlung stammt.
IBAN und BIC sind IBAN und BIC des Bankkontos, von dem die Zahlung stammt.
IBAN und BIC sind optional, aber wenn Sie sie angeben, können Sie mehr Funktionen in pretix nutzen, etwa die automatische Erstellung von Erstattungsdateien.

Sie haben zwei Optionen: Bankdaten für alle Veranstaltungen auf der Veranstalterebene importieren oder Bankdaten für eine Einzelveranstaltung importieren.
Wir empfehlen die erste Option, außer Sie haben für jede Ihrer Veranstaltungen ein eigenes Bankkonto.

Wenn Sie Daten für **alle Veranstaltungen** eines Veranstalters importieren möchten, navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-bank: Banküberweisung:.
Sie gelangen zu einer Seite mit dem Titel "Bankdaten importieren".

Wenn Sie die Daten für eine **Einzelveranstaltung** importieren möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-bank: Banküberweisung:.
Auch hier gelangen Sie zu einer Seite mit dem Titel "Bankdaten importieren".
Die beiden Seiten sind sehr ähnlich, aber eine gilt für die Ebene der Veranstaltung, die andere für die des Veranstalters.
Unabhängig von der gewählten Option ist die Vorgehensweise ab hier dieselbe.

Klicken Sie den Button :btn:Durchsuchen…: und wählen Sie die Exportdatei, die Sie hochladen möchten.

Klicken Sie den Button :btn:Upload starten:.
pretix fordert Sie jetzt auf anzugeben, welche Spalte Ihrer Datei welche Daten enthält.
Der folgende Screenshot zeigt am Beispiel einer kleinen CSV-Datei, wie eine solche Zuordnung aussehen kann.

![Seite 'Bankdaten importieren' mit einem Dialogfeld, das auffordert, Spalten einer CSV-Datei den Datenkategorien Datum, Betrag, Verwendungszweck, Zahler\*in, IBAN und BIC zuzuordnen. Radiobuttons und Kontrollkästchen ordnen die einzelnen Datenkategorien der Spalte der CSV-Datei zu, die die entsprechenden Angaben enthält. ](../../assets/screens/payment-providers/import-bank-data.png "Bankdaten importieren" )

Klicken Sie :btn:Weiter:.
Während Ihre Daten verarbeitet werden, zeigt pretix einen Ladebildschirm und anschließend einen Überblick, wie viele Bestellungen als bezahlt oder ungültig erkannt oder ignoriert wurden.
Das System ignoriert Transaktionen, die Sie bereits zuvor mit demselben Verfahren importiert haben.

Bei diesem Verfahren kann es gelegentlich ungeklärte Transaktionen geben.
Die häufigste Ursache dafür sind falsch geschriebene oder fehlende Bestellnummern im Verwendungszweck.
Falls das Bankkonto auch für Transaktionen genutzt wird, die nichts mit Verkäufen über pretix zu tun haben, entstehen auch dadurch ungeklärte Transaktionen.
In diesem Bildschirm können Sie eingreifen und Fehler manuell korrigieren.

Eine ausführlichere Anleitung, wie Sie [ungeklärte Transaktionen manuell verarbeiten](bank-transfer.md#handling-unresolved-transactions), finden Sie im Abschnitt weiter unten.

### Transaktionen manuell freigeben

![Eine Seite mit dem Titel 'Bestellungen' zeigt eine Liste mit einer Bestellung. Deren Status ist 'ausstehend', 0,00 € von 250,00 € bezahlt.](../../assets/screens/payment/orders.png "Bestellungen" )

Ergänzend zur [automatischen Option A](bank-transfer.md#option-a-automatic-transaction-import-using-gocardless) und zur [halbautomatischen Option B](bank-transfer.md#option-b-importing-bank-data), die beide oben beschrieben sind, haben Sie in pretix auch die Möglichkeit, Transaktionen manuell freizugeben.
Dazu navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-shopping-cart: Bestellungen:.
Diese Seite zeigt alle Bestellungen an, die Kund\*innen in Ihrem Shop getätigt haben.
Wenn ein Kund\*in eine Bestellung getätigt hat und Sie die Zahlung dafür noch nicht erhalten haben, zeigt die Seite diese Bestellung mit dem gelben Status-Tag ":fa3-money: Ausstehend" an.
Für Bestellungen, die per Banküberweisung bezahlt werden sollen, ist dies zu erwarten.

Klicken Sie die Bestellnummer einer der ausstehenden Bestellungen.
Dadurch gelangen Sie zur Seite "Bestellungsdetails" für diese Bestellung.

Prüfen Sie die Transaktionsdaten Ihres Bankkontos.
Wenn die Transaktionsdaten Ihres Bankkontos einen Eintrag enthalten, der zu der fraglichen Bestellung passt, klicken Sie oben auf der Seite mit den Bestellungsdetails den Button :btn-icon:fa3-check:Als bezahlt markieren:.

![Seite mit dem Titel 'Bestellung als bezahlt markieren'. Sie zeigt Optionen zum Ändern des Zahlungsbetrags von 250,00 € und des Zahlungsdatums sowie die Option, den Kund\*in per E-Mail zu informieren.](../../assets/screens/payment/order-mark-as-paid.png "Bestellungen" )

!!! Warnung
    Vergewissern Sie sich, bevor Sie die Bestellung als bezahlt markieren, dass Bestellung, Preis und Datum korrekt sind.
    Nachdem pretix eine Zahlung erfasst hat, ist es **nicht** mehr möglich, sie zu löschen.

Passen Sie Betrag und Datum der Zahlung bei Bedarf an.
Standardmäßig informiert pretix den Kund\*in per E-Mail darüber, dass die Bestellung als bezahlt markiert wurde.
Sie können das verhindern, indem Sie den Haken aus dem Kontrollkästchen neben "Kund\*in per E-Mail informieren" entfernen.
Bestätigen Sie den Zahlungseingang, indem Sie den Button :btn:Zahlung erstellen: klicken.

Dadurch gelangen Sie zurück zur Seite "Bestellungsdetails", die oben jetzt die Nachricht "Die Zahlung wurde erstellt" anzeigt und oben rechts ein grünes Tag mit dem Text ":fa3-check: Bezahlt".
Wiederholen Sie diese Vorgehensweise für jede auf der Seite "Bestellungen" aufgeführte Bestellung.

### Ungeklärte Transaktionen manuell verarbeiten

Sie können ungeklärte Transaktionen auf Veranstalter- oder auf Veranstaltungsebene verarbeiten.

Wenn Sie den automatischen Import über **GoCardless** nutzen oder Bankdaten auf **Veranstalterebene** importiert haben, navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-bank: Banküberweisung:. Sie gelangen zu einer Seite mit dem Titel "Bankdaten importieren".
Wenn Sie Bankdaten auf **Veranstaltungsebene** importiert haben, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-bank: Banküberweisung:. Sie gelangen zu einer Seite mit dem Titel "Bankdaten importieren".
Ab hier ist die Vorgehensweise dieselbe.

Wenn es ungeklärte Transaktionen gibt, zeigt diese Seite sie in der Liste "Ungeklärte Transaktionen" an.
Sie haben für jede Transaktion in der Liste zwei Optionen:
Sie können pretix anweisen, die Transaktion zu ignorieren, indem Sie den Butten :btn-icon:fa3-trash:: klicken, oder Sie können nach der passenden Bestellung suchen und der Transaktion die Bestellnummer zuordnen.

Dazu verwenden Sie das Feld "Bestellnummer" der ungeklärten Transaktion.
Sie können einen Teil der Bestellnummer, des Namens des bzw. der Käufer\*in, den Namen eines bzw. einer Teilnehmer\*in oder der E-Mail-Adresse eingeben, über die die Bestellung getätigt wurde.
Wählen Sie die passende Bestellung aus den angezeigten Suchergebnissen und klicken Sie zur Bestätigung den Button :btn-icon:fa3-check::.
Wiederholen Sie diese Vorgehensweise für alle ungeklärten Bestellungen.

Um Bestellungen anzuzeigen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-shopping-cart: Bestellungen:.

Löschen Sie Transaktionen nur dann, wenn sie nichts mit Ihrer Veranstaltung zu tun haben und Sie keine passende Bestellung finden.
Wenn pretix eine Transaktion in der Vergangenheit bereits importiert hat, erkennt die Software sie als Duplikat und ignoriert sie beim erneuten Import, auch wenn der frühere Eintrag gelöscht wurde.
