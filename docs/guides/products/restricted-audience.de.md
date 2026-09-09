# Eingeschränkte Teilnahmeberechtigung

Nicht alle Veranstaltungen dürfen von allen besucht werden.
Manchmal gibt es gute Gründe, den Zutritt zu Ihrer Veranstaltung oder zu [Teilen Ihrer Veranstaltung](sessions.md) auf einen bestimmten Personenkreis zu beschränken.
In pretix haben Sie mehrere Möglichkeiten, dies umzusetzen.
Dieser Artikel erläutert Ihnen alle Optionen.

## Option A: Verpflichtende Gutscheincodes

Mit Gutscheinen sorgen Sie dafür, dass ein Produkt (oder mehrere Produkte) nur für einen ausgewählten Kreis geladener Gäste verfügbar ist.
Eine ausführliche Anleitung finden Sie unter [Gutscheine: Verfügbarkeit exklusiver Produkte](../vouchers.md#exclusive-product-availability).

## Option B: Freigabe von Bestellungen

Wenn Sie noch nicht genau wissen, wer an einer Veranstaltung teilnehmen wird, den Zutritt aber dennoch auf einen bestimmten Personenkreis beschränken möchten, können Sie einstellen, dass Bestellungen freigegeben werden müssen.
Dies ist nützlich, wenn Sie bestimmten Gruppen, etwa der Presse oder Studierenden, Rabatte oder kostenlose Produkte anbieten.
Eine verpflichtende Freigabe gibt Ihnen die Möglichkeit, vor der Bestätigung der Bestellung zu prüfen, ob die Kund/*innen wirklich Mitglieder der betreffenden Gruppe sind.

Um die Freigabe für ein Produkt verpflichtend zu machen, navigieren Sie zu :navpath:Veranstaltung → :fa3-ticket: Produkte → Produkte: und bearbeiten Sie die Zutrittsprodukte.
Scrollen Sie auf dem Reiter :btn:Allgemein: an das Seitenende und markieren Sie dort das Kontrollkästchen "Die Bestellung dieses Produktes erfordert eine manuelle Freigabe".
Kund/*innen können dann ein solches Produkt bestellen, gelangen aber erst zur Zahlung, nachdem Sie die Bestellung freigegeben haben.

Bestellungen, die auf Freigabe warten, verhalten sich wie Bestellungen, die auf Zahlung warten.
Wenn jemand eine solche Bestellung tätigt, werden die Produkte im Kontingent und, falls vorhanden, auch im Sitzplan reserviert.

!!! Hinweis
    Die Einstellung "Die Bestellung dieses Produktes erfordert eine manuelle Freigabe" wirkt sich auf die gesamte Bestellung aus.
    Wenn ein/*e Kund/*in mehrere Produkte bestellt, von denen mindestens eines eine Freigabe erfordert, ist für die gesamte Bestellung eine Freigabe erforderlich.
    Wenn Sie die Freigabe verweigern, müssen Sie die Bestellung unter Umständen aufteilen.

Um eingehende Bestellungen zu prüfen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-shopping-cart: Bestellungen → Alle Bestellungen:.
Jede Bestellung, die ein freigabepflichtiges Produkt enthält, geben Sie nun manuell frei bzw. lehnen sie ab.
Anschließend erhält der/*die Kund/*in eine E-Mail mit der Bestätigung, dass die Bestellung freigegeben wurde und nun bezahlt werden kann.

Der wesentliche Nachteil dieser Vorgehensweise besteht darin, dass Ihre Kund/*innen auf diese Weise zweimal mit dem Shop interagieren müssen: einmal bei der Bestellung und ein zweites Mal bei der Zahlung.
Von diesem Nachteil nicht betroffen sind vollständig kostenlose Bestellungen, denn für diese entfällt der Zahlungsschritt.
Der wesentliche Vorteil dieser Vorgehensweise liegt darin, dass Sie bei jeder einzelnen Bestellung die Kontrolle darüber haben, wer an der Veranstaltung teilnimmt.

## Option C: Registrierte Kund/*innen und Mitgliedschaften

Sie können Ihre Veranstaltung auf einen bestimmten Personenkreis beschränken, indem Sie eine Mitgliedschaft als Voraussetzung für den Kauf eines Tickets definieren.
Wie Sie dies einrichten, erläutert der Artikel über [Kund/*innenkonten](../customer-accounts.md).
Weitere Informationen über das Gewähren und Fordern von Mitgliedschaften finden Sie unter [Dauerkarten](index.md#option-a-memberships-and-multiple-tickets).
