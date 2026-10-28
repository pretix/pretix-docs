# Erweiterungen

Erweiterungen sind optionale Softwaremodule, die Sie für jede Veranstaltung einzeln aktivieren oder deaktivieren können. 
Erweiterungen stellen unter anderem folgende Funktionen bereit: 

 - native Funktionen wie Badges für Teilnehmende, [E-Mails](email.md) und Sitzpläne
 - Integrationen mit [Zahlungsdienstleistern](payment/index.md) wie [Mollie](payment/mollie.md) oder [PayPal](payment/paypal.md)
 - Integrationen mit externen Diensten wie Google Analytics oder Venueless 
 - Ausgabeformate wie PDF-Tickets oder Umsatzberichte 

Einige Erweiterungen sind standardmäßig aktiv, andere müssen Sie erst aktivieren. 
Welche Erweiterungen Sie nutzen können, hängt von der pretix-Edition ab, die Sie verwenden. 
Einige Erweiterungen müssen Sie erst installieren, um sie aktivieren zu können. 
Wenn Sie pretix Enterprise nutzen, lesen Sie den Artikel über die [Installation von Erweiterungen für pretix Enterprise](../self-hosting/installation/enterprise.md). 

Dieser Artikel erklärt, wie Sie pretix-Erweiterungen nutzen, die bereits verfügbar sind. 
Wenn Sie selbst eine Erweiterung programmieren möchten, lesen Sie die [Dokumentation für Entwickler\*innen](https://docs.pretix.eu/dev/).

Um zu erfahren, wie Sie Zahlungsdienstleister für Ihre Veranstaltungen aktivieren, lesen Sie den Artikel über [Zahlungsdienstleister](payment/index.md). 

## Voraussetzungen

Erweiterungen gelten auf Veranstaltungsebene, Sie müssen also zuerst eine Veranstaltung anlegen. 

## Anleitung

Um Erweiterungen zu aktivieren oder zu deaktivieren, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Erweiterungen:.   
Sie gelangen zum Reiter :btn:Funktionen:, auf dem Erweiterungen für optionale Funktionen aufgeführt sind. 
Weitere Erweiterungen für Funktionen wie etwa Integrationen mit Zahlungsdienstleistern oder anderen externen Diensten finden Sie auf den anderen Reitern, die Sie oben auf der Seite sehen. 

![Auf der Seite 'Verfügbare Erweiterungen' ist der Reiter 'Funktionen' geöffnet. Als empfohlene Erweiterungen werden Aussteller, Badges, Digitale Inhalte und E-Mails verschicken angezeigt. Badges ist aktiv und hier finden sich Buttons für Einstellungen und zum Deaktivieren der Erweiterung.](../assets/screens/plugins/available.de.png "Empfohlene Erweiterungen auf dem Reiter Funktionen")

Wählen Sie auf jedem Reiter die Erweiterungen, die Sie verwenden möchten, und klicken Sie den Button :btn:Aktivieren: daneben. 
Sie können auch nach bestimmten Stichwörtern suchen, um die gewünschte Erweiterung zu finden. 

Eine aktivierte Erweiterung erkennen Sie an dem grünen Tag ":fa3-check: Aktiv" daneben und an dem weißen Button "Deaktivieren" anstelle des violetten Buttons "Aktivieren". 
Wenn Sie nur aktive Erweiterungen anzeigen möchten, klicken Sie beim Umschalter "Alle|aktiv" neben dem Suchfeld die Option :btn:Aktiv:. 
Deaktivieren Sie alle aktiven Erweiterungen, die Sie für Ihre Veranstaltung nicht nutzen möchten. 

### Erweiterungen konfigurieren

Einige aktivierte Erweiterungen fügen dem Menü der Seitenleiste einen eigenen Eintrag hinzu, über den Sie die dazugehörigen Einstellungen aufrufen. 
Falls zu einer aktiven Erweiterung Einstellungsseiten gehören, werden neben der Seite "Verfügbare Einstellungen" zusätzliche Buttons angezeigt. 
Um Erweiterungen zu konfigurieren, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Erweiterungen:.    
Suchen Sie die Erweiterung und klicken Sie das dazugehörige Dropdown-Menü :btn-icon:fa3-gear: Einstellungen:. 
Das Dropdown-Menü enthält Links zu den Einstellungsseiten für die betreffende Erweiterung. 

### Erweiterungen steuern

Einige aktivierte Erweiterungen fügen dem Menü der Seitenleiste einen eigenen Eintrag hinzu, über den Sie ihre Funktionsweise steuern können. 
Beispielsweise erfasst die Funktion "Statistiken" Statistiken zu den über Ihren Shop eingegangenen Bestellungen und zeigt diese im pretix-Backend an. 
Der Zahlungsdienstleister "Banküberweisung" erfordert den Umgang mit Importen von Bankdaten und Erstattungen. 
Um derartige Funktionen einer Erweiterung zu steuern, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Erweiterungen:.
Suchen Sie die Erweiterung und klicken Sie das Dropdown-Menü :btn-icon:fa3-compass: Gehe zu: daneben. 
Das Dropdown-Menü enthält Links zu Seiten, die für die betreffende Erweiterung relevant sind. 

## Weitere Informationen

Weitere Informationen über Erweiterungen zum Abwickeln von [Zahlungen](payment/index.md) finden Sie in den folgenden Artikeln: 

 - [Banküberweisung](payment/bank-transfer.md) 
 - [ePayBL](payment/epaybl.md)
 - [Mollie](payment/mollie.md)
 - [PayPal](payment/paypal.md) 
 - [Stripe](payment/stripe.md)

Weitere Informationen zu Erweiterungen für [Integrationen](integrations/index.md) mit externen Diensten finden Sie in den folgenden Artikeln: 

 - [GetYourGuide](integrations/getyourguide.md)
 - [HubSpot](integrations/hubspot.md)
 - [SAML-Authentifizierung vor dem Verkauf](integrations/presale-saml.md)
