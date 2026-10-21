# Eigene Domain

Standardmäßig ist ein mit pretix erstellter Shop unter einer URL wie zum Beispiel `https://pretix.eu/tut/tutcon27` abrufbar.
Dieses Beispiel verwendet unser Hosting-Angebot, die Domain ist daher `pretix.eu`.
Die Kurzform des Veranstalters ist `tut` und die Kurzform der Veranstaltung ist `tutcon27`.

Für Ihre Shops können Sie auch eine eigene Domain verwenden.
Dieser Artikel erläutert, wie Sie eine eigene Domain einrichten und für Ihre Veranstaltungen verwenden.

## Voraussetzungen

Sie müssen Inhaber\*in der Domain sein, die Sie als eigene Domain verwenden möchten.

Eigene Domains richten Sie auf Veranstalterebene ein.
Wenn Sie eine eigene Domain aktivieren möchten, benötigen Sie Zugriff auf ein Veranstalterkonto.
Außerdem benötigen Sie Zugriff auf jeden Veranstaltungsshop, für den Sie die eigene Domain verwenden möchten.

## Anleitung

Wie Sie zum Einrichten einer eigenen Domain vorgehen, hängt davon ab, wo Ihre Shops gehostet werden.
Wenn Sie [pretix Hosted](#pretix-hosted) nutzen, hosten wir Ihre Shops für Sie unter `pretix.eu`.
Wenn Sie [pretix Enterprise oder pretix Community](#pretix-enterprise-und-pretix-community) nutzen, läuft pretix auf Ihrem eigenen Server.
Lesen Sie weiter bei dem Abschnitt, der auf Sie zutrifft.

### pretix Hosted

Navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Eigene Domain:. 
Diese Seite zeigt einen DNS-Eintrag an, der ungefähr folgendermaßen aussieht:

**CNAME tut.cname.pretix.eu.**

Bei Ihnen lautet der DNS-Eintrag anders.
Erstellen Sie anhand des hier angezeigten DNS-Eintrags bei Ihrem Domain-Registrar oder DNS-Anbieter eine neue **Subdomain**.
Wie Sie dazu genau vorgehen müssen, hängt vom jeweiligen Domain-Registrar bzw. DNS-Anbieter ab.
In der Regel enthält die dortige Benutzeroberfläche ein Menü namens "DNS-Einträge", "DNS-Einstellungen" oder ähnlich.

Als Alternative zur Subdomain können Sie für den pretix-Shop auch Ihre Hauptdomain nutzen.
Wir empfehlen, eine `www.`-Subdomain zu erstellen und eine Weiterleitung von der Hauptdomain zu dieser Subdomain einzurichten.

Warten Sie ab, bis die Änderungen aktiv sind.
Dies kann einige Minuten, aber auch einige Stunden dauern.

Öffnen Sie das pretix-Backend und navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Eigene Domain:.
Geben Sie in das Feld "Domainname" die eben erstellte Subdomain ein.
Weisen Sie der Domain unter "Domain-Nutzung" eine von drei Rollen zu:

pretix nutzt die "Haupt-Domain des Veranstalters" für Ihre Veranstalterseite und alle Veranstaltungen, für die keine andere Domain angegeben wurde.
pretix nutzt die "Veranstaltungs-Domain" für eine Einzelveranstaltung.
Für bestimmte Veranstaltungen können Sie auch eine individuelle "Alternative Domain" wählen.
Weitere Informationen dazu finden Sie weiter unten im Abschnitt [Eine Veranstaltung zu einer alternativen Domain verschieben](custom-domain.md#eine-veranstaltung-zu-einer-alternativen-domain-verschieben).

Veranstaltungen, die einer alternativen Domain zugewiesen wurden, werden auf dieser alternativen Domain angezeigt.
Die Veranstalterseite wird **nicht** auf der alternativen Domain angezeigt.
Wenn Benutzer\*innen versuchen, auf der alternativen Domain Ihr Veranstalterkonto aufzurufen, leitet der Browser sie zur Hauptdomain des Veranstalters um, auf der alle Veranstaltungen aufgeführt sind.

Wenn Sie alle Optionen nach Bedarf gewählt haben, klicken Sie den Button :btn:Domain einrichten:.
Es kann einige Minuten dauern, bis die Änderungen in Kraft treten.

### pretix Enterprise und pretix Community

Wenn Sie pretix Enterprise oder pretix Community nutzen, konfigurieren Sie Ihren Webserver oder Reverse Proxy so, dass Anfragen an die neue Domain an pretix übergeben werden.
Wie Sie dazu genau vorgehen müssen, hängt von Ihrer konkreten Konfiguration ab.

Navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen und wechseln Sie zum Reiter :btn:Domains:.
Klicken Sie den Button :btn-icon:fa3-plus: Domain hinzufügen:. 
Auf der Seite wird eine neue, leere Zeile angezeigt.
Geben Sie in dieser neuen Zeile den Namen der neuen Domain in das Feld "Domainname" ein.

Wählen Sie einen Modus für die neue Domain.
pretix nutzt die "Veranstalterdomain" für Ihre Veranstalterseite und alle Veranstaltungen, für die keine andere Domain angegeben wurde.
pretix nutzt die "Veranstaltungs-Domain" für eine Einzelveranstaltung.
Geben Sie im Feld "Veranstaltung" eine Veranstaltung an.
Für bestimmte Veranstaltungen können Sie auch eine individuelle "Alternative Veranstalterdomain für einzelne Veranstaltungen" wählen.
Weitere Informationen dazu finden Sie weiter unten im Abschnitt [Eine Veranstaltung zu einer alternativen Domain verschieben](custom-domain.md#eine-veranstaltung-zu-einer-alternativen-domain-verschieben).

Veranstaltungen, die einer alternativen Domain zugewiesen wurden, werden auf dieser alternativen Domain angezeigt.
Die Veranstalterseite wird **nicht** auf der alternativen Domain angezeigt.
Wenn Benutzer\*innen versuchen, auf der alternativen Domain Ihr Veranstalterkonto aufzurufen, leitet der Browser sie zur Hauptdomain des Veranstalters um, auf der alle Veranstaltungen aufgeführt sind.

Wenn Sie alle Optionen nach Bedarf gewählt haben, klicken Sie den Button :btn:Domain einrichten:.
Es kann einige Minuten dauern, bis die Änderungen in Kraft treten.

### Eine Veranstaltung zu einer alternativen Domain verschieben

Wenn Sie im Modus "Alternative Domain" (pretix Hosted) oder "Alternative Veranstalterdomain für einzelne Veranstaltungen" (pretix Enterprise und pretix Community) eine Domain eingerichtet haben, müssen Sie die betreffenden Veranstaltungen zur alternativen Domain verschieben.

Dazu navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Allgemein:. 
Klicken Sie auf dem Reiter :btn:Eckdaten: das Dropdown-Menü "Domain".
Die Standardeinstellung ist `Wie das Veranstalterkonto`.
Wählen Sie die gewünschte alternative Domain aus der Liste und klicken Sie den Button :btn:Speichern:.