# Teams

Sie müssen nicht alle Events selbst managen. pretix erlaubt Ihnen, Kolleg*innen einzuladen und dafür unterschiedliche Teams mit unterschiedlichen Berechtigungen anzulegen.
Dieser Artikel erklärt, wie Sie die "Teams"-Einstellungen nutzen, Teams anlegen, Team-Einladungen verschicken, eine solche Einladung selbst annehmen und wie Sie die Zwei-Faktor-Authentifizierung einschalten.

## Voraussetzungen

Um Teams anzulegen und die Berechtigungen zu verwalten, benötigen Sie selbst Administrator*innen-Rechte für das Veranstalterkonto.
Wenn Sie keinen Zugriff auf ein Veranstalterkonto haben, suchen Sie wahrscheinlich den Abschnitt, in dem erklärt wird, wie Sie eine Team-Einladung annehmen (LINK).

## How-To

Navigieren Sie zu Ihrem :navpath:Veranstalterkonto →  :fa3-users: Teams:.
Diese Seite zeigt Ihnen sämtliche Teams Ihres Veranstalterkontos.
Wenn Sie an dieser Stelle in Ihrem Veranstalterkonto noch keine Änderungen vorgenommen haben, wird hier nur ein Team mit dem Namen "Administratoren" gelistet.
Dieses Team hat sämtliche Berechtigungen und enthält nur Ihr Benutzer*innenkonto. Sie können die Mitglieder eines Teams und die API-Tokens sehen, wenn Sie den Button :btn-icon:fa3-list:: rechts neben dem Teamnamen anklicken.
Die Berechtigungen und Einstellungen für ein Team können Sie einsehen und ändern, wenn Sie den Button :btn-icon:fa3-edit:: anklicken.

## Ein neues Team anlegen

Wenn Sie in Ihrem Veranstalterkonto zu Teams navigieren, klicken Sie den Button :btn-icon:fa3-plus: Create a new team:, um ein neues Team anzulegen.

Sie können den Namen und die Berechtigungen für das Team frei wählen. Das neue Team können Sie beispielsweise "Mitarbeiter*innen" nennen, um es vom Administratoren-Team zu unterscheiden. Sie können im Abschnitt "Veranstalter-Berechtigungen" entweder alle Berechtigungen vergeben, indem Sie die Checkbox "Alle Veranstalter-Berechtigungen" auswählen, oder beispielsweise die folgenden individuellen Veranstalter-Berechtigungen vergeben:
"Veranstaltungen" auf "Zugang zu existieren Veranstaltungen und neue Veranstaltungen erstellen", "Wertgutscheine" auf "Lesen und ändern" und "Kunden" auf "Lesen und ändern" setzen. 

Die Option "Alle Veranstalter-Berechtigungen" bezieht sich auf sämtliche Einstellungen im Veranstalterkonto selbst, für die auf dieser Seite keine Optionen explizit aufgeführt sind. Wenn die URL der Einstellungs-Seite Ihres Veranstalterkontos /control/organizer/ enthält, dann wird die Berechtigung für die Optionen auf dieser Seite über die vorher genannte Option vergeben. Dies bezieht sich nur auf die Einstellungen, die nicht explizit auf dieser Seite unter "Veranstalter-Berechtigungen" auswählbar sind.

Im Abschnitt "Veranstaltungs-Berechtigungen" können Sie entweder Zugriff auf alle Veranstaltungs-Berechtigungen vergeben, indem Sie die Option "Alle Veranstaltungs-Berechtigungen" auswählen. Wenn die URL der Einstellungs-Seite Ihrer Veranstaltung /control/event/ enthält, dann wird die Berechtigung für die Optionen auf dieser Seite über die vorher genannte Option vergeben. Dies bezieht sich nur auf die Einstellungen, die nicht explizit auf dieser Seite unter "Veranstaltungs-Berechtigungen" auswählbar sind. Oder Sie wählen beispielsweise die folgenden individuellen Berechtigungen aus: "Allgemeine Einstellungen" auf "Lesen und ändern", "Produkte, Kontingente und Fragen" auf "Lesen und ändern", "Bestellungen" auf "Alle lesen" und "Gutscheine" auf "Lesen und ändern" setzen.

Wenn Sie unterschiedliche Berechtigungen für andere Veranstaltungen vergeben möchten, müssen Sie ein neues Team anlegen und dafür die passenden Berechtigungen auswählen und dieses Team auf die gewünschten Veranstaltungen einschränken.

Die Namenskonventionen für Ihre Teamnamen und die Berechtigungen hängen von Ihren individuellen Anforderungen ab. Die Namen und Berechtigungen können auch später noch jederzeit verändert werden. Es zahlt sich aber aus und Sie vermeiden zukünftige Probleme und Verwirrungen, wenn Sie hier ein wenig Zeit investieren und Ihre Anforderungen und Berechtigungen vorher festlegen, bevor Sie Kolleg*innen in die jeweiligen Teams einladen. Klicken Sie den Speichern Button, um das neu angelegte Team zu speichern. Danach werden Sie auf die Übersichtsseite der Team-Mitglieder weitergeleitet.

!!! Note
  Wenn ein Team-Mitglied keine Berechtigung für einen Bereich des Systems hat, kann es eventuell trotzdem Daten dieses Bereichs einsehen, wenn dieser mit anderen Bereichen in pretix verknüpft ist. Beispielsweise kann ein Team-Mitglied mit Berechtigung zum Zugriff auf die Bestellungen auch den Wertgutschein einsehen, der mit einer Bestellung angelegt oder zur Bezahlung einer Bestellung verwendet wurde.

## Eine Person ins Team einladen

Navigieren Sie zu :navpath:Veranstalterkonto → :fa3-users: Teams: und wählen Sie das Team aus, für das Sie eine Einladung verschicken möchten. Sie können eine Person einladen, indem Sie die E-Mail-Adresse der Person in das Eingabefeld unterhalb der Mitgliederliste des Teams eingeben oder einfügen und rechts neben dem Eingabefeld auf den Button "Hinzufügen" klicken. Wenn die eingeladene Person bereits über ein pretix-Benutzerkonto verfügt und dieser die gleiche E-Mail-Adresse verwendet, wird die Person sofort dem Team hinzugefügt. In diesem Fall wird die Person nicht vom System benachrichtigt, weshalb Sie die Person darüber informieren sollten. Die Person wird entweder mit einem grauen oder grünen :fa3-shield: Symbol rechts neben der E-Mail-Adresse aufgelistet, abhängig davon, ob diese die Zwei-Faktor-Authentifizierung aktiviert haben oder nicht.

Wenn die eingeladene Person noch kein pretix-Benutzerkonto hat, erhält sie eine E-Mail mit einer Einladung, einen Account anzulegen. In diesem Fall erscheint rechts in der Mitglieder-Liste neben der E-Mail-Adresse ein :fa3-envelope-o: Symbol mit dem Status "eingeladen, Antwort ausstehend" und ein :btn-icon:fa3-rotate-right::-Button, um die Einladung erneut per E-Mail zu verschicken.

!!! Note
  Auf dieser Seite können Sie auch einen API-Token anlegen, der Zugriff auf die pretix API erlaubt. Der API-Token erhält die gleichen Berechtigungen, die für die Mitglieder des Teams gelten. Weitere Informationen zu API-Tokens finden Sie in unserer [API Dokumentation](https://docs.pretix.eu/en/latest/api/tokenauth.html).

## Eine Einladung annehmen

Wenn Sie zum Team eingeladen wurden und noch kein pretix-Benutzerkonto haben, erhalten Sie eine E-Mail wie oben auf dem Screenshot zu sehen. Wenn Sie den Link in der E-Mail anklicken, werden Sie zu pretix weitergeleitet und haben in dem Dialogfenster die Möglichkeit, ein Passwort anzugeben und den "Registrieren"-Button anzuklicken, um einen Account anzulegen. Sie werden daraufhin zum Dashboard weitergeleitet und die Nachricht "Willkommen zu pretix! Sie sind nun Mitglied vom Team "Mitarbeiter*innen". Damit haben Sie Zugriff auf das Veranstalterkonto und die Veranstaltungen, so wie die Berechtigungen im Team "Mitarbeiter*innen" es vorsehen.

Wenn Sie zu einem Team eingeladen wurden und bereits ein pretix-Benutzerkonto haben, können Sie sich in pretix einloggen und haben Zugriff auf das Veranstalterkonto und die Veranstaltungen, so wie die Berechtigungen im Team "Mitarbeiter*innen" es vorsehen.

## Zwei-Faktor-Authentifizierung einschalten

Sie können alle Team-Mitglieder dazu verpflichten, die Zwei-Faktor-Authentifizierung zu verwenden. Wählen Sie dazu ein bestehendes Team aus oder legen Sie ein neues an. Wählen Sie die Checkbox "Alle Mitglieder dieses Teams müssen Zwei-Faktor-Authentifizierung nutzen" an. Es kann ein paar Minuten dauern, bis dieses Setting für alle Mitglieder des Teams gilt.

Wenn ein Team-Mitglied, das noch keine Zwei-Faktor-Authentifizierung verwendet, sich das nächste Mal in pretix einloggt, wird es auf die Seite "Zwei-Faktor-Authentifizierung" weitergeleitet. Es ist nicht möglich, diese Seite zu überspringen, bis die Zwei-Faktor-Authentifizierung aktiviert wurde.

Wenn Sie mehr über die erhöhte Sicherheit erfahren möchten, welche die Zwei-Faktor-Authentifizierung mit sich bringt und wie Sie diese für Ihr Benutzerkonto einschalten, lesen Sie unseren Artikel zur Zwei-Faktor-Authentifizierung (LINK).

## Zwei-Faktor-Authentifizierung einrichten

Wenn pretix Sie direkt nach dem Login zur Seite "Zwei-Faktor-Authentifizierung" weiterleitet, hat die Person, welche die Teams in Ihrem Veranstalterkonto verwaltet, die Option zur Verwendung der Zwei-Faktor-Authentifizierung verpflichtend für Ihr Benutzerkonto eingeschaltet. Um zu erfahren, wie Sie die Zwei-Faktor-Authentifizierung richtig einrichten, lesen Sie unseren Artikel zur Zwei-Faktor-Authentifizierung (LINK).
