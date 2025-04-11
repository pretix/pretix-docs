# Kassen

{% include "warning-tax.de.md" %}

Dieser Artikel erklärt die Anmeldung von Kassensystemen in Deutschland. 
Falls Sie als Einzelperson oder Firma steuerpflichtig in der Bundesrepublik Deutschland sind und eine Kasse haben, die Sie für den Verkauf über pretix benutzen, dann ist dieser Artikel relevant für Sie. 
Das gilt nicht nur dann, wenn Sie selbst eine Kasse besitzen, sondern auch, wenn Sie eine Kasse von pretix mieten. 

## Voraussetzungen 

What conditions have to be met for this information to be applicable? Which settings have to be adjusted, which plugins have to be activated, which previous knowledge is assumed by the article? 

## Anleitung 

### pretixPOS-Kasse mit pretix verbinden 

Um ein Gerät, auf dem pretixPOS läuft, mit pretix zu verbinden, navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-shopping-basket: Kassensystem → Kassen: und klicken den Button :btn-icon:fa3-plus: Neues Gerät verbinden:. 
Wählen Sie Namen und Veranstaltungen. 
Unter "Security profile" wählen Sie "pretixPOS" und klicken dann den Button :btn:Speichern:. 
Auf der nächsten Seite werden ein QR-Code und ein Anmeldecode angezeigt.

Öffnen Sie die App pretixPOS auf dem Kassengerät und scannen Sie den QR-Code oder geben Sie den Anmeldecode ein. 
pretixPOS stellt Ihnen nun folgende Frage: "In welchem Land ist der Betrieb dieser Kasse steuerpflichtig?". 
Wählen Sie das entsprechende Land aus und tippen Sie auf den Button :btn:OK:. 
Wählen Sie dann eine oder mehrere Veranstaltungen, für die Sie die Kasse benutzen möchten. 

### Betriebsstätte anlegen

Die Anmeldung von Kassen in Deutschland erfolgt immer als Bruttomeldung, bei der alle Kassen an einer Betriebsstätte gesammelt übermittelt werden. 
Legen Sie daher zunächst in pretix eine Betriebsstätte an. 
Navigieren Sie dazu zu :navpath:Ihr Veranstalter → :fa3-shopping-basket: Kassensystem → Kassenanmeldung (DE) und klicken Sie den Button :btn-icon:fa3-plus: Neue Betriebsstätte anlegen:. 

Auf der Seite mit dem Titel "Neue Betriebsstätte anlegen" geben Sie zunächst Steuernummer, Bundesland und Umsatzsteuer-Identifikationsnummer an. 
Wählen Sie dann unter "Rechtsform" entweder "Natürliche Person" oder "Firma" aus. 
Abhängig von Ihrer Auswahl werden unterschiedliche Eingabefelder angezeigt. 
Füllen Sie diese aus. 

Falls die Daten Ihrer Betriebsstätte mit Ihren Daten als Steuerpflichtiger übereinstimmen, klicken Sie den Button :btn:Daten des Steuerpflichtigen übernehmen:.
Falls nicht, füllen Sie diese Felder ebenfalls aus. 
Sobald Sie den Button :btn:Speichern: klicken, prüft pretix, ob die eingegebene Steuernummer gültig ist, und ob die anderen Eingaben vollständig sind. 


### Kasse einer Betriebsstätte zuweisen

## Problemlösung 

What are common problems that could be encountered here? How do you solve them? 

## Weitere Informationen

Lesen Sie unseren Blogbeitrag: [So geht's: Kassenanmeldung in Deutschland](https://pretix.eu/about/de/blog/20250317-so-gehts-kassenanmeldung-in-deutschland/). 

## Siehe auch

Link to other relevant guides, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 