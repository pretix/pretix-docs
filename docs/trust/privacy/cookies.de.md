# Verwendung von Cookies

## Shop

Falls Ihr pretix-Shop die Standardkonfiguration verwendet, setzt er bei allen Clients, die darauf zugreifen (z. B. beim Ticketkauf), die folgenden Cookies: 

<table>
<thead>
<tr>
<th>Name</th>
<th>Inhalt</th>
<th>Lebensdauer</th>
<th>Grund</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__Host-pretix_csrftoken</code></td>
<td>Zufällige ID</td>
<td>365 Tage</td>
<td>Sicherheitstoken für das Einreichen von Formularen. Dient als Sicherheitsmaßnahme gegen <a href="https://de.wikipedia.org/wiki/Cross-Site-Request-Forgery" target="_blank">CSRF-Angriffe</a>.<br>
Wir bewerten dieses Cookie als technisch notwendig, um die gewünschte Funktion bereitzustellen.
Deshalb ist dafür keine Einwilligung erforderlich.
Wir führen diese ID nicht mit anderen Datenquellen zusammen und verwenden sie nicht für Tracking.</td>
</tr>
<tr>
<td><code>__Host-pretix_session</code></td>
<td>Sitzungs-ID</td>
<td>14 Tage</td>
<td>Dieses Cookie dient dazu, die Benutzer*innensitzung über das Neuladen der Seite hinweg wiederzuerkennen, und unterstützt damit alle Funktionen, die dies benötigen, etwa die Zuordnung eines Warenkorbs zu einem*einer Benutzer*in oder die Anmeldung am Kund*innenkonto.<br>
Das Cookie wird nur gesetzt, wenn Benutzer*innen eine Funktion nutzen, die es erfordert.<br>
Wir bewerten dieses Cookie als technisch notwendig, um die gewünschte Funktion bereitzustellen.
Deshalb ist dafür keine Einwilligung erforderlich.
In der Standardkonfiguration wird dieses Cookie nicht zu Tracking-Zwecken genutzt.</td>
</tr>
<tr>
<td><code>pretix_language</code></td>
<td>Sprach-ID, beispielsweise "en" oder "de"</td>
<td>10 Jahre</td>
<td>Dient zum Speichern der von dem*der Benutzer*in für die Anzeige des Shops gewählten Sprache, damit wir den Shop später wieder in genau dieser bevorzugten Sprache anzeigen können.
Wird nur gesetzt, wenn der*die Benutzer*in die Sprache selbst festlegt.<br>
Wir bewerten dieses Cookie als technisch notwendig, um die gewünschte Funktion bereitzustellen.
Deshalb ist dafür keine Einwilligung erforderlich.
Wegen des geringen Informationsgehalts ist es praktisch unmöglich, dieses Cookie zum Tracking zu verwenden.</td>
</tr>
<tr>
<td><code>__proxy_session</code></td>
<td>Zufällige ID</td>
<td>7 Tage</td>
<td>Nur für pretix Hosted: Dies ist ein Sicherheitstoken für unser Kapazitätsmanagement, damit der Shop auch bei starker Nachfrage zuverlässig läuft.<br>
Wir bewerten dieses Cookie als technisch notwendig, um die gewünschte Funktion bereitzustellen.
Deshalb ist dafür keine Einwilligung erforderlich.
Wir führen diese ID nicht mit anderen Datenquellen zusammen und verwenden sie nicht für Tracking.</td>
</tr>
<tr>
<td><code>cookie-consent-&lt;shop&gt;</code><br><small>(Lokal gespeichert)</small></td>
<td>Einwilligungseinstellungen</td>
<td>dauerhaft</td>
<td>Falls unser Modul für die Cookie-Einwilligung für Cookies externer Anbieter genutzt wird (z. B. Tracking-Anbieter), speichern wir, welchen Cookies der*die Benutzer*in zugestimmt hat und welche abgelehnt wurden.
Dies ist erforderlich, um später die erteilte Zustimmung umzusetzen und nur die Tracking-Funktionen zu laden, für die eine Einwilligung vorliegt.
Da diese Angaben lokal und nicht in einem Cookie gespeichert werden, werden sie niemals an unseren Server übertragen und nur innerhalb des Browsers verwaltet.</td>
</tr>
</tbody>
</table>

Es ist möglich, dass durch die Nutzung von Erweiterungen zusätzliche Cookies gesetzt werden, z. B. durch die Einbindung von Zahlungsdienstleistern oder Tracking-Skripten.

## pretix-Widget

Beim **Laden** des Widgets auf einer Seite setzt pretix noch **keine** Cookies im Browser.
Erst wenn der\*die Benutzer\*in mit dem Widget interagiert (also ein Produkt wählt und den Kaufvorgang startet), wird ein Cookie gesetzt.

Für die umgebende Website werden die in der folgenden Tabelle aufgeführten Cookies gesetzt.
Zusätzlich werden bei Verwendung des Widgets auch alle Cookies gesetzt, die im Abschnitt "Shop" aufgeführt sind.

<table>
<thead>
<tr>
<th>Name</th>
<th>Inhalt</th>
<th>Lebensdauer</th>
<th>Grund</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pretix_widget_&lt;ticketshop_url&gt;</code></td>
<td>Warenkorb-ID</td>
<td>30 Tage</td>
<td>Das Cookie ermöglicht es Benutzer\*innen, den Kauf nach einer Unterbrechung (z. B. einem Absturz des Browsers) fortzusetzen, ohne die reservierten Tickets zu verlieren.<br>
Wir bewerten dieses Cookie als technisch notwendig, um die gewünschte Funktion bereitzustellen, sodass dafür keine Einwilligung erforderlich ist.
</tr>
</tbody>
</table>

## Management der Cookie-Einwilligungen

Wir bewerten alle oben aufgeführten Cookies als technisch notwendig, um die gewünschte Funktion bereitzustellen.
Daher ist unter der [EU-Datenschutzrichtlinie für elektronische Kommunikation](https://de.wikipedia.org/wiki/Datenschutzrichtlinie_für_elektronische_Kommunikation) keine Einwilligung erforderlich.

Zu pretix gehört eine native Funktion, um für Erweiterungen ein einheitliches Management der Cookie-Einwilligungen bereitzustellen.
Um diese Funktion zu aktivieren, navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Datenschutz:.
Eigene Erweiterungen müssen Sie in diese Funktion einbinden, wie in unserer [Entwicklerdokumentation](https://docs.pretix.eu/dev/development/api/cookieconsent.html) beschrieben.

Wenn Sie das Widget verwenden, können Sie Angaben zu Cookie-Einwilligungen von der umgebenden Website an den pretix-Shop [übergeben](../../guides/widget.md#benutzerinnendaten-der-website-fur-das-widget-nutzen), damit die Einwilligung nicht wiederholt abgefragt wird.

