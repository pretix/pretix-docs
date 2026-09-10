# Widget

Mit dem pretix-Widget können Sie Ihren Shop auf Ihrer Website einbinden.
Über das Widget können Kund\*innen Tickets kaufen, ohne Ihre Website zu verlassen.
Eine Alternative zum Widget ist der [pretix-Button](widget.md#pretix-button).
Dieser Button fügt dem Warenkorb die gewählten Produkte hinzu und leitet den\*die Kund\*in zur Kasse weiter.

Das eingebettete Widget kann zum Beispiel so aussehen:

<link rel="stylesheet" type="text/css" href="https://pretix.eu/demo/democon/widget/v2.css" crossorigin>
<script type="text/javascript" src="https://pretix.eu/widget/v2.en.js" async crossorigin></script>
<pretix-widget event="https://pretix.eu/demo/democon/"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript ist in Ihrem Browser deaktiviert.
            Um unseren Ticketshop ohne JavaScript aufzurufen, klicken Sie bitte <a target="_blank" href="https://pretix.eu/demo/democon/">hier</a>.
        </div>
    </div>
</noscript>

Dieser Artikel erläutert die grundlegende Einrichtung des Widgets und einige der weiterführenden Konfigurationsoptionen.

## Voraussetzungen

Sie müssen mindestens eine Veranstaltung erstellen, bevor Sie den Shop-Zugang über das Widget bereitstellen können.
Das Widget wird nur auf der Website angezeigt, wenn der Shop aktiv ist.

Sie benötigen eine Website sowie die Möglichkeit, Änderungen daran vorzunehmen.
Grundkenntnisse über JavaScript sind hilfreich.

## Allgemeine Verwendung

Dieser Abschnitt erläutert, wie Sie das [pretix-Widget](widget.md#embedding-the-widget-on-your-website) oder den [pretix-Button](widget.md#pretix-button) auf Ihrer Website einbinden, entweder einmal oder [mehrfach](widget.md#embedding-multiple-widgets-on-your-website).

### Das Widget auf der Website einbinden

Sie können das pretix-Widget auf Ihrer Website einbinden, indem Sie aus dem pretix-Backend zwei Code-Abschnitte kopieren und in den HTML-Code Ihrer Website einfügen.
Diese Code-Abschnitte finden Sie hier :navpath:Ihre Veranstaltung → Einstellungen → Widget:.
Wählen Sie die "Sprache" für das Widget und klicken Sie den Button :btn:Widget-Code generieren:.

Die Website erstellt daraufhin zwei Code-Abschnitte.
Der erste Abschnitt lädt die CSS- und JavaScript-Ressourcen für das Widget vom pretix-Server.
Fügen Sie diesen Abschnitt in den `<head>`-Abschnitt Ihrer Website ein, wenn Sie die Konventionen des Webdesigns beachten möchten.
Damit reagiert Ihre Webseite bei langsamen Verbindungen etwas schneller.
Sie können den Abschnitt aber auch in den `<body>` einfügen.
Der Code-Abschnitt sieht ungefähr so aus:

```
<link rel="stylesheet" type="text/css" href="https://pretix.eu/demo/democon/widget/v2.css">
<script type="text/javascript" src="https://pretix.eu/widget/v2.en.js" async></script>
```

Fügen Sie den zweiten Code-Abschnitt an der Position Ihrer Website ein, an der das Widget angezeigt werden soll.
Der Abschnitt sieht ungefähr so aus:

```
<pretix-widget event="https://pretix.eu/demo/democon/"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript ist in Ihrem Browser deaktiviert.
            Um unseren Ticketshop ohne JavaScript aufzurufen, klicken Sie bitte <a target="_blank" href="https://pretix.eu/demo/democon/">hier</a>.
        </div>
    </div>
</noscript>
```

!!! Hinweis

    Einige Website-Anbieter wie Jimdo haben Probleme mit unserem speziellen HTML-Tag.
    Falls ein solches Problem bei Ihnen auftritt, bearbeiten Sie die Anfangs- und End-Tags in der ersten Zeile des zweiten Code-Abschnitts folgendermaßen:
    Ersetzen Sie `<pretix-widget …>` mit `<div class="pretix-widget-compat" …>`.
    Ersetzen Sie `</pretix-widget>` mit `</div>`.

Alle Beispiele in diesem Artikel arbeiten mit der Basis-URL `pretix.eu`, dem Veranstalter `demo` und der Veranstaltung `democon`.
Wenn Sie unsere Beispiele für Ihre eigene Veranstaltung und Ihre Website übernehmen möchten, müssen Sie die betreffenden Ausdrücke für Ihre Veranstaltung anpassen.

Der einfachste Weg, den korrekten Code zu erhalten, ist unser Code-Generator.
Navigieren Sie zu :navpath:Ihre Veranstaltung → Einstellungen → Widget:, klicken Sie den Button :btn:Widget-Code generieren: und kopieren Sie die Code-Abschnitte von dort.

### Mehrere Widgets auf der Website einbinden

!!! Hinweis
    Wenn Sie das Widget für mehrere Veranstaltungen verwenden möchten, ist es nicht notwendig, mehrere Widgets einzubinden.
    Lesen Sie dazu [Das Widget für mehrere Veranstaltungen nutzen](widget.md#using-the-widget-for-multiple-events).

Wenn Sie mehrere Widgets für verschiedene Veranstaltungen auf Ihrer Website einbinden möchten, fügen Sie den ersten Code-Abschnitt nur **einmal** ein.
Generieren Sie den zweiten Code-Abschnitt für jede Veranstaltung neu und fügen Sie die jeweiligen Abschnitte in den HTML-Code Ihrer Website ein.

### pretix-Button

Als Alternative zum umfangreicheren Widget können Sie auf Ihrer Website einen einfachen Button einbinden.
Dieser Button fügt dem Warenkorb eine vordefinierte Auswahl an Produkten hinzu und leitet zur Kasse weiter.
Sie können dieses Verhalten hier ausprobieren:

<pretix-button event="https://pretix.eu/demo/democon/" items="item_6424=1">Ticket kaufen!</pretix-button>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript ist in Ihrem Browser deaktiviert.
            Um unseren Ticketshop ohne JavaScript aufzurufen, klicken Sie bitte <a target="_blank" href="https://pretix.eu/demo/democon/">hier</a>.
        </div>
    </div>
</noscript>

Sie fügen den pretix-Button genauso ein wie das pretix-Widget.
Dazu binden Sie die CSS- und JavaScript-Ressourcen ein wie unter [Das Widget auf der Website einbinden](widget.md#embedding-the-widget-on-your-website) beschrieben.
Verwenden Sie statt des Tags `pretix-widget` das Tag `pretix-button`:

```
<pretix-button event="https://pretix.eu/demo/democon/" items="item_6424=1">
    Ticket kaufen!
</pretix-button>
```
Mit dem Attribut `items` geben Sie an, welche Artikel der Button in den Warenkorb legt.
Dieses Attribut hat folgende Syntax:

```
item_ITEMID=1,item_ITEMID=2,variation_ITEMID_VARID=4
```

Ersetzen Sie jedes Vorkommen von `ITEMID` mit der ID des Produkts, das hinzugefügt werden soll.
Ersetzen Sie jedes Vorkommen von `VARID` mit der ID der Produktvariante des Produkts.
Lassen Sie den Teil `variation_ITEMID_VARID=4` weg, falls Ihre Produkte **keine** Varianten haben.
Geben Sie anhand der Zahl nach dem `=` die Nummer des Produkts bzw. der Variante an, die in den Warenkorb gelegt werden sollen.

Wenn Sie das Attribut `items` **nicht** angeben oder **keine** gültige Produkt- oder Varianten-ID übergeben, öffnet ein Klick auf den Button den Shop in einem neuen Reiter des Browsers und es werden keine Produkte in den Warenkorb gelegt.
Standardmäßig berücksichtigt diese Seite **keine** Elemente im Warenkorb, die zuvor (über den Button oder das Widget) hinzugefügt wurden, und der auf dieser Seite angelegte Warenkorb wird gelöscht, falls die Seite mit dem Button neu geladen wird.
Um den Warenkorb zu speichern, der in dieser Ansicht angelegt wurde, und den Warenkorb zu verwenden, der von anderen Buttons und Widgets auf derselben Seite angelegt wurde, verwenden Sie das Attribut `keep-cart`.

Wenn Sie den Button mit einer Veranstaltungsreihe verknüpfen, geben Sie über das Attribut `subevent` den Termin an, für den Produkte in den Warenkorb gelegt werden sollen.

Der Button unterstützt die optionalen Attribute `voucher`, `disable-iframe` und `skip-ssl-check`.
Für den Button-Stil können Sie die CSS-Klasse `pretix-button` verwenden.

## Anwendungsfälle

Dieser Abschnitt behandelt alle Anwendungsfälle über die einfache Einbindung des Widgets auf Ihrer Website hinaus:

 - das Widget für [mehrere Veranstaltungen](widget.md#using-the-widget-for-multiple-events) oder eine [Veranstaltungsreihe](widget.md#using-the-widget-for-an-event-series) nutzen
 - die [Produktverfügbarkeit](widget.md#product-availability) beeinflussen
 - das Widget-[Verhalten anpassen](widget.md#customizing-widget-behavior)
 - die [Benutzer\*innen-Daten](widget.md#using-your-websites-user-data-for-the-widget) der Website für das Widget nutzen
 - [Tracking](widget.md#using-tracking-with-the-pretix-widget) mit dem Widget nutzen
 - Kompatibilität mit den [Sicherheit](widget.md#security)seinstellungen Ihrer Website

### Das Widget für mehrere Veranstaltungen nutzen

Sie können mehrere Veranstaltungs-Shops in einem einzigen Widget anzeigen.
Wenn Sie **alle** öffentlichen Veranstaltungen in Ihrem Veranstalterkonto aufführen möchten, entfernen Sie den Veranstaltungs-Slug aus der URL im Attribut `event`, aber behalten Sie den Slug für Sie als Veranstalter:

```
<pretix-widget event="https://pretix.eu/demo/"></pretix-widget>
```

#### Das Widget für ausgewählte Veranstaltungen nutzen

Wenn Sie mehrere Veranstaltungen planen, aber nur einige davon im Widget aufführen möchten, sollten Sie **Metadaten-Attribute** verwenden.
Dieser Abschnitt erläutert, wie Sie Metadaten-Attribute erstellen, Veranstaltungen zuweisen und einen Filter im Widget einrichten.

Sie erstellen Metadaten-Attribute folgendermaßen: Navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Veranstaltungs-Metadaten: und klicken Sie den Button :btn-icon:fa3-plus: Neue Eigenschaft erstellen:.
Sie können beispielsweise eine Metadaten-Eigenschaft namens "Werbung" mit den Werten `True` und `False` erstellen, wobei `False` der Standardwert ist.

Um einer Veranstaltung die Metadaten-Eigenschaft zuzuweisen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Allgemein:.
Bearbeiten Sie auf dem Reiter :btn:Eckdaten: unter "Metadaten" die entsprechende Eigenschaft.

Wenn Sie beispielsweise eine Metadaten-Eigenschaft namens "Werbung" mit den Werten `True` und `False` erstellen, die für einige Veranstaltungen `True` ist, können Sie folgenden Filter einrichten.

```
<pretix-widget event="https://pretix.eu/demo/" list-type="list" filter="attr[Werbung]=True"></pretix-widget>
```

Wenn Sie in der Konfiguration der Metadaten-Attribute öffentliche Filter aktiviert haben, zeigt das Widget ein Filterformular an.
Mit folgendem Code deaktivieren Sie das Filterformular:

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-filters></pretix-widget>
```

### Das Widget für eine Veranstaltungsreihe nutzen

Sie können das Widget mit einer Veranstaltungsreihe verknüpfen.
Standardmäßig zeigt das Widget **alle Termine** der Veranstaltungsreihe an.
Wenn Sie im Widget nur [bestimmte Termine anzeigen](widget.md#using-the-widget-for-a-selection-of-dates) möchten, können Sie diese über das Metadaten-Attribut filtern.
Wenn Sie im Widget nur [einen einzigen Termin anzeigen](widget.md#using-the-widget-for-a-single-date) möchten, verwenden Sie die Termin-ID.

Anhand des Attributs `list-type` legen Sie fest, ob das Widget die Termine in einem Monatskalender, einem Wochenkalender oder als Liste anzeigt.
Falls Sie dieses Attribut **nicht** angeben, wird die Standardeinstellung verwendet, die Sie unter :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Allgemein: festgelegt haben.

```
<pretix-widget event="https://pretix.eu/demo/series/" list-type="list"></pretix-widget>
<pretix-widget event="https://pretix.eu/demo/series/" list-type="calendar"></pretix-widget>
<pretix-widget event="https://pretix.eu/demo/series/" list-type="week"></pretix-widget>
```

Wenn Sie mehr als 100 Veranstaltungen haben, zeigt das System aus Performance-Gründen immer einen Monatskalender an.
Dieser sieht beispielsweise so aus:

<pretix-widget event="https://pretix.eu/demo/series/" list-type="calendar"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript ist in Ihrem Browser deaktiviert.
            Um unseren Ticketshop ohne JavaScript aufzurufen, klicken Sie bitte <a target="_blank" href="https://pretix.eu/demo/series/">hier</a>.
        </div>
    </div>
</noscript>

#### Das Widget für ausgewählte Termine nutzen

Wenn Sie im Widget nur bestimmte Termine anzeigen möchten, können Sie diese über das **Metadaten-Attribut** filtern.
Dieser Abschnitt erläutert, wie Sie Metadaten-Attribute erstellen, Terminen zuweisen und einen Filter im Widget einrichten.

Sie erstellen Metadaten-Attribute folgendermaßen: Navigieren Sie zu :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Veranstaltungs-Metadaten: und klicken Sie den Button :btn-icon:fa3-plus: Neue Eigenschaft erstellen:.
Sie können beispielsweise eine Metadaten-Eigenschaft namens "Werbung" mit den Werten `True` und `False` erstellen, wobei `False` der Standardwert ist.

Um die Metadaten-Eigenschaft ausgewählten Terminen zuzuweisen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-calendar: Termine:.
Wählen Sie die Termine, die Sie im Widget anzeigen möchten, und klicken Sie den Button :btn-icon:fa3-edit: Ausgewählte bearbeiten (#):.
Markieren Sie unter "Metadaten" das Kontrollkästchen "ändern" neben dem Attribut und wählen Sie den gewünschten Wert.
So können Sie beispielsweise den Wert des Attributs "Werbung" zu `True` ändern.

Sie können auch einen oder mehrere neue Termine erstellen und das Attribut "Metadaten" auf den gewünschten Wert setzen.

Anschließend fügen Sie dem Widget-Code einen Filter-Parameter hinzu.
Verwenden Sie folgenden Code, um nur Termine anzuzeigen, deren Metadaten-Attribut "Werbung" `True` ist.

```
<pretix-widget event="https://pretix.eu/demo/series/" list-type="list" filter="attr[Werbung]=True"></pretix-widget>
```

Wenn Sie in der Konfiguration der Metadaten-Attribute öffentliche Filter aktiviert haben, zeigt das Widget ein Filterformular an.
Mit folgendem Code deaktivieren Sie das Filterformular:

```
<pretix-widget event="https://pretix.eu/demo/series/" disable-filters></pretix-widget>
```

#### Das Widget für einen einzigen Termin nutzen

Wenn Sie das Widget nur für einen einzigen Termin einer Veranstaltungsreihe nutzen möchten, übergeben Sie dem Attribut `subevent` die Termin-ID.
So ermitteln Sie die Termin-ID: Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-calendar: Termine:.
Die Seite zeigt in der Liste unter dem Namen des Termins ein Raute-Zeichen gefolgt von einer Zahl – der Termin-ID.
Sie brauchen nur die Zahl, **ohne** das Raute-Zeichen.
Sie können den Termin auch direkt bearbeiten.
Die Zahl vor dem letzten Schrägstrich in der URL ist die Produkt-ID, hier also die ID des Termins.

Wenn das Widget nur den Termin `#4387749` anzeigen soll, übergeben Sie die Termin-ID dem Attribut `subevent` folgendermaßen :

```
<pretix-widget event="https://pretix.eu/demo/series/" subevent="4387749"></pretix-widget>
```

Das Attribut `subevent` kann nur eine einzige Termin-ID als Argument haben.
Mit dieser Vorgehensweise ist es **nicht** möglich, nach mehr als einem Termin zu filtern.
Wenn Sie mehrere, aber nicht alle Termine einer Veranstaltungsreihe anzeigen möchten, [filtern Sie nach dem Metadaten-Attribut](widget.md#using-the-widget-for-a-selection-of-dates).

### Produktverfügbarkeit

Dieser Abschnitt erläutert, wie Sie die Produktverfügbarkeit im Widget über Filter oder vorausgewählte Gutscheine steuern.

#### Bestimmte Produkte nur über das Widget anbieten

Wenn Sie bestimmte Produkte ausschließlich über das Widget und nicht im Shop anbieten möchten, sollten Sie im Widget einen **Gutschein vorauswählen**.
Einen Gutschein vorauswählen bedeutet, dass sich das Widget so verhält, als habe der\*die Kund\*in den Gutscheincode eingegeben.
Dieser Abschnitt erläutert, wie Sie ein Produkt ausschließlich über einen Gutschein verfügbar machen und wie Sie den Gutschein über das Attribut `voucher` im Widget vorauswählen.

Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Produkte: und erstellen oder bearbeiten Sie das betreffende Zutrittsprodukt.
Wechseln Sie zum Reiter :btn:Verfügbarkeit: und markieren Sie das Kontrollkästchen neben "Dieses Produkt kann nur mit einem Gutschein gekauft werden".

Setzen Sie den Schalter für die Sichtbarkeit neben dieser Option auf "Verstecke das Produkt, wenn es nicht verfügbar ist" (:btn-icon:fa3-eye-slash::).
Dadurch wird das Produkt im Shop nicht angezeigt.
Es wird nur Personen angezeigt, die einen Gutschein besitzen.

Wenn Sie die Verfügbarkeit für mehrere Produkte einschränken möchten, führen Sie die oben beschriebenen Schritte für jedes Produkt aus.
Erstellen Sie ein Kontingent, das alle Produkte enthält, die nur über das Widget verfügbar sein sollen.

Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-tags: Gutscheine: und klicken Sie den Button :btn-icon:fa3-plus: Neuen Gutschein erstellen:.
Übernehmen Sie den automatisch generierten Vorschlag im Feld "Gutscheincode" oder geben Sie einen eigenen Code ein.
Geben Sie im Feld "Maximale Nutzungen" eine hohe Zahl ein, zum Beispiel 999999.

Wählen Sie unter "Produkt" das Produkt aus, das Sie über das Widget zur Verfügung stellen möchten.
Wenn es mehr als ein Produkt gibt, wählen Sie das Kontingent, das alle betreffenden Produkte enthält.
Markieren Sie unten auf der Seite das Kontrollkästchen neben "Zeigt versteckte Produkte an, die zu diesem Gutschein passen".

Verschicken Sie den Gutscheincode **nicht** als E-Mail und geben Sie ihn an **niemanden** weiter.
Klicken Sie stattdessen den Button :btn:Speichern:, kopieren Sie den Gutscheincode (beispielsweise `ABCDE123456`) und übergeben Sie ihn dem Attribut `voucher`:

```
<pretix-widget event="https://pretix.eu/demo/democon/" voucher="ABCDE123456"></pretix-widget>
```

So zeigt das Widget nur Produkte an, die Kund\*innen mit dem Gutschein kaufen können, und es werden die im Gutschein hinterlegten Preise angezeigt.
Ein Beispiel für ein Widget mit vorausgewähltem Gutschein können Sie unter [Rabatte über das Widget anbieten](widget.md#offering-discounts-through-the-widget) ansehen.

#### Nur bestimmte Produkte über das Widget anbieten

Dieser Abschnitt erläutert, wie Sie nur einige Ihrer Produkte im Widget anbieten.

Sie können die im Widget angezeigten Produkte anhand einer Liste von Produkt-IDs, getrennt durch Kommas, filtern.
So ermitteln Sie die Produkt-IDs: Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Produkte:.
Die Seite zeigt in der Liste unter dem Namen des Produkts ein Raute-Zeichen gefolgt von einer Zahl – der Produkt-ID.
Sie brauchen nur die Zahl, **ohne** das Raute-Zeichen.
Sie können das Produkt auch direkt bearbeiten.
Die Zahl vor dem letzten Schrägstrich in der URL ist die Produkt-ID, hier also die ID des Termins.

Wenn das Widget nur die Produkte `#562195` und `#562202` anzeigen soll, geben Sie diese folgendermaßen an:

```
<pretix-widget event="https://pretix.eu/demo/democon/" items="562195,562202"></pretix-widget>
```

#### Nur bestimmte Kategorien über das Widget anbieten

Die im Widget angebotenen Produkte können Sie nach Kategorie filtern.
So ermitteln Sie die Kategorie-ID: Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Kategorien:.
Bearbeiten Sie die gewünschte Kategorie.
Die Zahl vor dem letzten Schrägstrich in der URL ist die Kategorie-ID.

Wenn das Widget nur Produkte aus den Kategorien `#162620` und `#162647` anzeigen soll, geben Sie diese folgendermaßen an:

```
<pretix-widget event="https://pretix.eu/demo/democon/" categories="162620,162647"></pretix-widget>
```
#### Nur bestimmte Produktvarianten über das Widget anbieten

Die im Widget angebotenen Produkte können Sie auch nach Produktvariante filtern.
So ermitteln Sie die Produktvarianten-ID: Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Produkte:.
Bearbeiten Sie das betreffende Produkt und wechseln Sie zum Reiter :btn:Varianten:.
Die Seite zeigt in der Liste unter dem Namen der Produktvariante ein Raute-Zeichen gefolgt von einer Zahl – der Varianten-ID.
Sie brauchen nur die Zahl, **ohne** das Raute-Zeichen.

Wenn das Widget nur die Varianten `#437143`, `#437154` und `#437155` anzeigen soll, geben Sie diese folgendermaßen an:

```
<pretix-widget event="https://pretix.eu/demo/democon/" variations="437143,437154,437155"></pretix-widget>
```

### Preise und Zahlung

Dieser Abschnitt erläutert, wie Sie [Rabatte über das Widget anbieten](widget.md#offering-discounts-through-the-widget), [die Eingabe von Gutscheinen deaktivieren](widget.md#disabling-the-voucher-input) und wie Sie über das Widget [Apple Pay](widget.md#offering-apple-pay-via-stripe-through-the-widget) mit Stripe verwenden.
Alle übrigen Zahlungsdienstleister und -methoden sollten problemlos mit dem Widget funktionieren.

#### Rabatte über das Widget anbieten

Wenn Sie Kund\*innen, die über das Widget bestellen, Rabatte gewähren möchten, sollten Sie im Widget **einen Gutschein vorauswählen**.
Einen Gutschein vorauswählen bedeutet, dass sich das Widget so verhält, als habe der\*die Kund\*in den Gutscheincode eingegeben.
Dieser Abschnitt erläutert, wie Sie im Widget-Code einen Gutschein anhand des Attributs `voucher` vorauswählen, um exklusiv über das Widget einen Rabatt anzubieten.

Erstellen Sie einen Gutschein, wie im Artikel über Gutscheine unter [Begrenzte Rabatte anbieten](vouchers.md#offering-a-limited-discount) beschrieben.
Geben Sie den Gutscheincode **nicht** öffentlich und **nicht** Kund\*innen direkt bekannt.
Übergeben Sie den Gutscheincode (beispielsweise `ABCDE123456`) stattdessen dem Attribut `voucher`:

```
<pretix-widget event="https://pretix.eu/demo/democon/" voucher="ABCDE123456"></pretix-widget>
```

So zeigt das Widget nur Produkte an, die Kund\*innen mit dem Gutschein kaufen können, und es werden die im Gutschein hinterlegten Preise angezeigt.
Sie müssen das Code-Beispiel von oben **nicht** kopieren und bearbeiten.
Manchmal ist es einfacher, einen Code-Abschnitt mit dem Gutschein zu generieren, indem Sie das Feld "Vorausgewählter Gutschein" auf der Seite mit den Widget-Einstellungen aktivieren.

Hier ist ein Beispiel für das Widget mit vorausgewähltem Gutschein:

<pretix-widget event="https://pretix.eu/demo/democon/" voucher="ABCDE123456"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript ist in Ihrem Browser deaktiviert.
            Um unseren Ticketshop ohne JavaScript aufzurufen, klicken Sie bitte <a target="_blank" href="https://pretix.eu/demo/democon/">hier</a>.
        </div>
    </div>
</noscript>

#### Eingabe von Gutscheinen deaktivieren

Wenn Sie die Möglichkeit deaktivieren möchten, im Widget einen Gutschein einzugeben, können Sie das Attribut `disable-vouchers` nutzen:

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-vouchers></pretix-widget>
```

#### Apple Pay über Stripe im Widget anbieten

Wenn Sie Stripe als Zahlungsdienstleister nutzen und im Widget auch Zahlungen über Apple Pay anbieten möchten, müssen Sie die Domain zuerst bei Apple Pay registrieren.
pretix validiert die Domain, die Sie für Ihren Shop nutzen, automatisch und unabhängig von der pretix-Edition und Ihren Domain-Einstellungen.
Aber wenn Sie das Widget auf Ihrer Website einbinden, muss Ihre Domain auch validiert werden, damit sie mit Apple Pay verwendet werden kann.

Weitere Informationen, wie Sie [Domains für Zahlungsmethoden registrieren](https://stripe.com/docs/payments/payment-methods/pmd-registration), finden Sie in der Dokumentation von Stripe.

### Das Widget-Verhalten anpassen

Dieser Abschnitt erläutert, wie Sie verschiedene Aspekte des Widgets anpassen: sein Aussehen, wie es geladen wird und sich öffnet, wie die Seite mit der Kasse geöffnet wird und wie Informationen zur Veranstaltung angezeigt werden.

#### Aussehen

Sie können das Aussehen des Widgets oder des Buttons über ein CSS an die Gestaltung Ihrer Website anpassen.
Mit den Entwicklerwerkzeugen des Browsers können Sie die HTML-Darstellung des Widgets überprüfen.
Fast jedes Element hat eine eigene Klasse und alle Klassen haben das Präfix `pretix-widget`.
Sie können die Stile überschreiben oder ein eigenes Stylesheet verwenden.

!!! Hinweis
    Wir haben das Widget so entwickelt, dass es die Vorgaben der Europäischen Union zur Barrierefreiheit erfüllt.
    Achten Sie darauf, diese Barrierefreiheit durch Ihre Anpassungen am Widget **nicht** zu beschädigen, etwa indem Sie Farben mit zu geringen Kontrasten wählen.

#### Das Widget dynamisch öffnen

Sie können eine Funktion aufrufen, um das Widget als Reaktion auf eine Aktion des\*der Benutzer\*in dynamisch zu öffnen.
Dies ist ähnlich wie das Verhalten des [pretix-Buttons](widget.md#pretix-button), aber Sie können das Widget von jedem Teil des Website-Codes aufrufen.

Der Aufruf der Funktion öffnet ein Overlay mit dem Shop.
Unter bestimmten Umständen, etwa bei einer fehlenden HTTPS-Verschlüsselung oder auf einem kleinen Bildschirm, öffnet die Funktion stattdessen einen neuen Reiter.
Sie sollten diese Funktion daher nur als direkte Reaktion auf eine Aktion des\*der Benutzer\*in aufrufen.
Anderenfalls werden die meisten Browser das Widget als unerwünschtes Popup einstufen und blockieren.

Rufen Sie die Funktion `window.PretixWidget.open` auf, die folgendermaßen aufgebaut ist:

```
window.PretixWidget.open(target_url[, voucher[, subevent[, items[, widget_data[, skip_ssl_check]]]]])
```

Parameter:

 - **target_url** (String): Die URL des Shops.
 - **voucher** (String): ein vorausgewählter Gutscheincode oder `null`.
 - **subevent** (String): ein vorausgewählter Termin aus einer Veranstaltungsreihe oder `null`.
 - **items** (Array): eine Zusammenstellung von Artikeln, die in den Warenkorb gelegt werden sollen, in folgender Form`[{"item": "item_3", "count": 1}, {"item": "variation_5_6", "count": 4}]`.
 - **widget_data** (Objekt): weitere Daten, die dem Shop übergeben werden.
 - **skip_ssl_check** (Boolean): gibt an, ob die Prüfung auf HTTPS ignoriert werden soll.
   Überspringen Sie diese Prüfung auf der aktiven Website **nicht**.
   Überspringen Sie sie nur während der Entwicklung.

#### Das Widget dynamisch laden

Es kann notwendig sein zu steuern, wann und wie das Widget geladen wird, etwa weil Sie mit JavaScript [Benutzer\*innendaten dynamisch verändern](widget.md#using-your-websites-user-data-for-the-widget) möchten.
Sie können einen Listener registrieren, der vor der Erstellung des Widgets ausgeführt wird:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    // Wird ausgeführt, bevor wir das Widget erzeugen.
}
</script>
```

Sie können das Laden des Widgets unterdrücken oder die Benutzer\*innendaten, die dem Widget übergeben werden, verändern:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    window.PretixWidget.build_widgets = false;
    window.PretixWidget.widget_data["email"] = "test@beispiel.org";
}
</script>
```

Das Laden des Widgets lösen Sie mit dem Aufruf von `window.PretixWidget.buildWidgets()` aus.

#### Warten auf das Laden oder Schließen des Widgets

Wenn Sie eigenen JavaScript-Code ausführen möchten, sobald das Widget vollständig geladen ist oder wenn es geschlossen wurde, können Sie Callback-Funktionen registrieren:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    window.PretixWidget.addLoadListener(function () {
        console.log("Widget wurde geladen!");
    });
    window.PretixWidget.addCloseListener(function () {
        console.log("Widget wurde geschlossen!");
    });
}
</script>
```

Sie können diese Funktionen mehrmals ausführen, etwa einmal für jedes Widget auf der Seite oder jedes Mal, wenn der\*die Benutzer\*in die Listen- bzw. Kalenderansicht ändert.

#### Immer einen neuen Reiter öffnen

Auf Geräten mit kleinerem Bildschirm öffnet sich die Kasse standardmäßig in einem neuen Reiter.
Wenn die Kasse unabhängig von der Bildschirmgröße immer in einem neuen Reiter geöffnet werden soll, können Sie das Attribut `disable-iframe` übergeben:

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-iframe></pretix-widget>
```

#### Informationen zur Veranstaltung ein- oder ausblenden

Wenn Sie das Widget mit einer Veranstaltungsreihe verknüpft haben, zeigt es standardmäßig Informationen zur Veranstaltung an, etwa Titel, Ort und Beschreibung.
Diese Informationen werden für Einzelveranstaltungen **nicht** angezeigt.
Sie können dieses Verhalten über das optionale Attribut `display-event-info` steuern.

Wenn das Widget eine Veranstaltungsreihe **ohne** Informationen anzeigen soll, setzen Sie das Attribut auf den Wert `"false"`.
Das Standardverhalten aktivieren Sie über das Attribut `display-event-info` mit dem Wert  `"auto"`.
Wenn das Widget eine Einzelveranstaltung **mit** Informationen anzeigen soll, setzen Sie das Attribut auf den Wert `"true"`.
Das Widget behandelt alle Werte, die nicht `"false"` oder `"auto"` sind, als `"true"`.

```
<pretix-widget event="https://pretix.eu/demo/democon/" display-event-info></pretix-widget>
```

### Benutzer\*innendaten der Website für das Widget nutzen

Dieser Abschnitt erläutert, wie Sie Daten von Benutzer\*innen mit dem Widget verarbeiten.

Wenn Sie das Widget auf einer Seite anzeigen, für die sich Benutzer\*innen anmelden müssen, können Sie deren bekannte Daten auf der Seite mit der  Kasse bereits in die Felder eintragen.
Das kann Ihren Benutzer\*innen Tipparbeit ersparen und zu mehr Kaufabschlüssen führen.
Sie können zusammen mit diesen Angaben auch weitere Datenattribute übergeben:

```
<pretix-widget event="https://pretix.eu/demo/democon/"
    data-attendee-name-given-name="Maxi"
    data-attendee-name-family-name="Musterperson"
    data-invoice-address-name-given-name="Maxi"
    data-invoice-address-name-family-name="Musterperson"
    data-email="test@beispiel.org"
    data-question-L9G8NG9M="Foobar">
</pretix-widget>
```

Wenn Sie dies über den pretix-Button umsetzen möchten, müssen Sie auch das Attribut `items` angeben.

Datenattribute sind reaktiv.
Sie können sie daher mit JavaScript ändern.
Sobald der\*die Benutzer\*in zur Kasse geht, ändert pretix Datenattribute im dadurch begonnenen Kassenprozess **nicht mehr**.
Eine solche Änderung würde den Prozess unterbrechen und der\*die Benutzer\*in müsste von vorne anfangen.

Eine Änderung der Datenattribute über JavaScript erfordert einen frischen Verweis auf den HTMLNode des Widgets.
Beim Erstellen des Widgets wird der ursprüngliche HTMLNode möglicherweise ersetzt und dann würde der Verweis ins Leere laufen.
Um einen frischen Verweis zu erzwingen, verwenden Sie folgenden Code:

```document.querySelectorAll("pretix-widget, pretix-button, .pretix-widget-wrapper")```

pretix kann die folgenden Datenattribute verarbeiten:

 - `data-email` füllt vorab die Felder für die E-Mail zur Bestellungsabwicklung und die E-Mail des\*der Teilnehmer\*in aus (sofern aktiviert).

 - `data-question-IDENTIFIER` trägt vorab die Antwort auf die Frage mit dem angegebenen Identifikator (IDENTIFIER) ein.
 Um Identifikatoren anzuzeigen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Fragen:.
 Um einen internen Identifikator festzulegen, bearbeiten oder erstellen Sie eine Frage, wechseln Sie zum Reiter :btn:Erweitert: und nutzen Sie das Feld "Interne Referenz".

 - `data-attendee-name` trägt vorab den letzten Teil des Namens ein.
   Das genaue Verhalten hängt davon ab, welche Konfiguration Sie unter :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Allgemein auf dem Reiter :btn:Kunden- und Teilnehmerdaten: vorgenommen haben.
   Den vorab eingetragenen Namen können Sie anhand der folgenden Attribute genauer steuern.
   Welche Auswahl sich für Ihre Zwecke am besten eignet, hängt davon ab, wie Sie das Namensformat in den Veranstaltungseinstellungen konfiguriert haben.
    - `data-attendee-name-full-name`
     - `data-attendee-name-given-name`
     - `data-attendee-name-family-name`
     - `data-attendee-name-middle-name`
     - `data-attendee-name-title`
     - `data-attendee-name-calling-name`
     - `data-attendee-name-latin-transcription`

 - `data-invoice-address-FIELD` füllt das entsprechende Feld der Rechnungsanschrift aus.
   Mögliche Werte für `FIELD` sind:
     - `company`
     - `street`
     - `zipcode`
     - `city`
     - `country` (dies muss der zweibuchstabige Ländercode sein)
     - `internal-reference`
     - `vat-id`
     - `custom-field`
     - Felder, die durch das Namensformat definiert sind, etwa `name-title` oder `name-given-name`
     `country`

 - Wenn Sie `data-fix="true"` setzen, können die Benutzer\*innen die übrigen vorab ausgefüllten Felder **nicht mehr** ändern.
   Dies funktioniert nur für die E-Mail-Adresse zur Bestellungsabwicklung und für die Rechnungsanschrift.
   Benutzer\*innen werden immer die Felder und Fragen auf Teilnehmer\*innenebene ändern können.

!!! Hinweis
    Das Attribut `data-fix="true"` ist **keine** Sicherheitsfunktion.
    Die Benutzer\*innen Ihrer Website können es übersteuern.
    Verwenden Sie es **nicht** zur Authentifizierung.

 - Wenn Sie `data-consent="…"` setzen, übernimmt die Funktion zur Cookie-Zustimmung die Zustimmung für die angegebenen Cookie-Anbieter.
   Damit werden alle anderen Anbieter deaktiviert.
   Das Widget fragt die Zustimmung **nicht** in einem eigenen Dialog ab.
   Es ist **nicht** möglich, die Cookie-Einstellungen innerhalb des Widgets zu ändern.
   Dies ist nützlich, wenn Sie die Zustimmung der Benutzer\*innen bereits abgefragt haben und **nicht** möchten, dass das Widget erneut fragt.
   Beispiel: `data-consent="facebook,google_analytics"`
   Wenn der\*die Benutzer\*in die Zustimmung für alle Cookie-Anbieter verweigert hat, verwenden Sie `data-consent="none"`, um alle Anbieter zu deaktivieren.
   Die pretix-Integration "Tracking-Codes" unterstützt folgende Werte:
     - `adform`
     - `facebook`
     - `gosquared`
     - `google_ads`
     - `google_analytics`
     - `hubspot`
     - `linkedin`
     - `matomo`
     - `twitter`

Alle aktiven pretix-Erweiterungen können Daten in Datenattribute eintragen, mit denen pretix umgehen kann.
Wenn Sie beispielsweise die Erweiterung "Kampagnen-Tracking" aktiviert haben, können Sie dem Attribut `data-campaign` eine Kampagnen-ID zuweisen.
Dann zählt pretix alle Bestellungen, die über dieses Widget getätigt werden, für diese Kampagne.

### Tracking mit dem pretix-Widget verwenden

Wenn Sie die Erweiterung "Tracking-Codes" aktiviert haben, können Sie domainübergreifendes Tracking aktivieren.
Dies ist nur erforderlich, wenn Ihr pretix-Shop und die Website, in die Sie das Widget einbinden, auf zwei getrennten Domains gehostet sind.
Wenn Sie den pretix-Shop auf einer Subdomain der Hauptdomain, die Tracking verwendet, betreiben, benötigen Sie **kein** domainübergreifendes Tracking.
Die Integration von Tracking-Codes unterstützt das Tracking auch auf angeschlossenen Subdomains, sodass Sie dann **kein** domainübergreifendes Tracking benötigen.
Weitere Informationen finden Sie im Artikel über [eigene Domains](custom-domain.md).

Fügen Sie die Website mit dem Widget in Ihren Einstellungen für Google Analytics der [Verweis-Ausschlussliste](https://support.google.com/analytics/answer/2795830?hl=de) hinzu.

Fügen Sie Google Analytics genauso hinzu wie alle anderen Seiten, auch die Konfigurationen `[window.dataLayer]{.title-ref}` und `[gtag]{.title-ref}`.
Fügen Sie den Widget-Code hinzu.
Sie haben nun zwei Optionen:

Option 1 besteht darin, das Laden des Widgets so lange zu blockieren, bis Googles Client- und Sitzungs-ID geladen wurden, oder maximal für zwei Sekunden.
Dies ist ähnlich wie das [dynamische Laden des Widgets](widget.md#loading-the-widget-dynamically).
Wenn der Ladevorgang länger als zwei Sekunden dauert, werden Client- und Sitzungs-ID **nicht** an das Widget übergeben.

Option 2 besteht darin, Datenattribute asynchron zu setzen.
Die Website zeigt Widgets sofort an, aber es ist **nicht mehr** möglich, ein Datenattribut zu verändern, sobald der\*die Benutzer\*in zur Kasse geht.

Wenn Sie die erste Option verwenden (also das Laden des Widgets vorübergehend blockieren) möchten, fügen Sie den folgenden Code auf Ihrer Website ein.
Ersetzen Sie alle Vorkommen von `<MESS-ID>` mit Ihrer Mess-ID von Google Analytics `(G-XXXXXXXX)`:

```
<script type="text/javascript">
    window.pretixWidgetCallback = function () {
        window.PretixWidget.build_widgets = false;
        window.addEventListener('load', function() { // Abwarten, bis GA geladen ist
            if (!window['google_tag_manager']) {
                window.PretixWidget.buildWidgets();
                return;
            }

            var clientId;
            var sessionId;
            var loadingTimeout;
            function build() {
                // mit loadingTimeout sicherstellen, dass build() nur einmal aufgerufen wird
                if (!loadingTimeout) return;
                window.clearTimeout(loadingTimeout);
                loadingTimeout = null;
                if (clientId) window.PretixWidget.widget_data["tracking-ga-id"] = clientId;
                if (sessionId) window.PretixWidget.widget_data["tracking-ga-sessid"] = sessionId;
                window.PretixWidget.buildWidgets();
            };
            // pretix-Widgets werden auch dann erstellt, wenn gtag client_id und oder session_id nicht lädt
            loadingTimeout = window.setTimeout(build, 2000);

            gtag('get', ‚<MESS-ID>', 'client_id', function(id) {
                clientId = id;
                if (sessionId !== undefined) build();
            });
            gtag('get', ‚<MESS-ID>', 'session_id', function(id) {
                sessionId = id;
                if (clientId !== undefined) build();
            });
        });
    };
</script>
```

Wenn Sie die andere Option nutzen (also Datenattribute asynchron setzen) möchten, fügen Sie den folgenden Code auf Ihrer Website ein.
Ersetzen Sie alle Vorkommen von `<MESS-ID>` mit Ihrer Mess-ID von Google Analytics `(G-XXXXXXXX)`:

```
<script type="text/javascript">
    window.addEventListener('load', function() {
        gtag('get', ‚<MESS-ID>', 'client_id', function(id) {
            const widgets = document.querySelectorAll("pretix-widget, pretix-button, .pretix-widget-wrapper");
            widgets.forEach(widget => widget.setAttribute("data-tracking-ga-id", id))
        });
        gtag('get', ‚<MESS-ID>', 'session_id', function(id) {
            const widgets = document.querySelectorAll("pretix-widget, pretix-button, .pretix-widget-wrapper");
            widgets.forEach(widget => widget.setAttribute("data-tracking-ga-sessid", id))
        });
    });
</script>
```

### Sicherheit

Dieser Abschnitt erläutert sicherheitsrelevante Aspekte bei der Einbindung des Widgets: Einstellungen für SSL/HTTPS sowie die Richtlinien auf Ihrer Website.

#### SSL

Der Kauf eines Tickets erfordert in der Regel die Eingabe vertraulicher Daten.
Wir empfehlen daher dringend, auf der Seite mit dem Widget SSL/HTTPS zu verwenden.
Über Initiativen wie [Let’s Encrypt](https://letsencrypt.org/) können Sie ein kostenloses SSL-Zertifikat erhalten.

pretix nutzt für alle vom Widget übertragenen Daten SSL, selbst wenn Sie das Widget auf einer nicht durch SSL geschützten Website verwenden.
Wenn Sie **kein** SSL für Ihre Website verwenden, ist es allerdings möglich, durch Man-in-the-Middle-Angriffe schädliche Änderungen an Widget vorzunehmen.
Heutzutage ist es Standard, für alle Datenübertragungen SSL zu verwenden.
Manche Kund\*innen vertrauen Ihrer Website eventuell nur, wenn sie beim Zugriff auf die Website im Browser das Schlosssymbol :fa3-lock: sehen.

Verwendet Ihre Website **kein** SSL, ruft der Gang zur Kasse einen neuen Reiter im Browser auf.
Wenn Sie einen wirklich guten Grund dafür haben, **kein** SSL zu verwenden, können Sie dieses Verhalten mit dem Attribut `skip-ssl-check` übersteuern.

```
<pretix-widget event="https://pretix.eu/demo/democon/" skip-ssl-check></pretix-widget>
```

#### Content Security Policy (CSP)

Wenn Sie auf Ihrer Website eine Content Security Policy (CSP) verwenden, müssen Sie unter Umständen einige Anpassungen vornehmen.
Wenn Ihr pretix-Shop auf einer eigenen Domain läuft, müssen Sie die folgenden Regeln hinzufügen:

 - `script-src`: `'unsafe-eval' https://pretix.eu` (Tragen Sie hier Ihre Domain mit dem selbst gehosteten pretix ein.)
 - `style-src`: `https://pretix.eu` (Tragen Sie hier Ihre Domain mit dem selbst gehosteten pretix **und** die eigene Domain bei pretix Hosted ein.)
 - `connect-src`: `https://pretix.eu` (Tragen Sie hier Ihre Domain mit dem selbst gehosteten pretix **und** die eigene Domain bei pretix Hosted ein.)
 - `frame-src`: `https://pretix.eu` (Tragen Sie hier Ihre Domain mit dem selbst gehosteten pretix **und** die eigene Domain bei pretix Hosted ein.)
 - img-src`: `https://pretix.eu` (Tragen Sie hier Ihre Domain mit dem selbst gehosteten pretix **und** die eigene Domain bei pretix Hosted ein.)
    Fügen Sie für pretix Hosted auch `https://cdn.pretix.cloud` hinzu.

#### "Cross Origin Opener Policy"

Falls Sie auf Ihrer Website `Cross-Origin-Opener-Policy: same-origin` setzen und einen Zahlungsdienstleister verwenden, der für den Gang zur Kasse ein neues Fenster öffnet (PayPal zum Beispiel), wird im Vordergrund ein leeres Fenster geöffnet.
Das liegt daran, dass JavaScript keinen Zugriff auf dieses Fenster hat.
Dieses Problem lösen Sie, indem Sie entweder [für das Widget beim Gang zur Kasse immer einen neuen Reiter öffnen](widget.md#always-open-a-new-tab) oder `Cross-Origin-Opener-Policy: same-origin-allow-popups` setzen.

#### "Cross Origin Embedder Policy"

Das pretix-Widget ist nicht kompatibel mit `Cross-Origin-Embedder-Policy: require-corp`.
Wenn Sie in den Tags `<script>` und `<link>` die Attribute `crossorigin` verwenden, kann das Widget zwar einen Kalender oder eine Produktliste anzeigen.
Es wird aber nicht in der Lage sein, die Kasse in einem iframe zu öffnen.
Wenn Sie auch `Cross-Origin-Opener-Policy: same-origin` setzen, kann das Widget erkennen, dass es in einer isolierten Umgebung läuft, und öffnet für die Kasse dann einen neuen Reiter.

## Fehlerbehebung

### Der von dieser Seite kopierte Code funktioniert nicht

Wenn Sie Code-Beispiele von dieser Seite für Ihre eigene Veranstaltung und Ihre Website übernehmen möchten, müssen Sie bestimmte Ausdrücke so ändern, dass sie für Ihre Veranstaltung gelten.
Alle Beispiele in diesem Artikel arbeiten mit der Basis-URL `pretix.eu`, dem Veranstalter `demo` und der Veranstaltung `democon` oder der Veranstaltungsreihe `series`.
Für Ihre eigenen Veranstaltungen verwenden Sie andere Veranstalter- und Veranstaltungs-Slugs.
Auch wenn Sie eine andere Domain nutzen, müssen Sie in den Code die entsprechende Basis-URL eintragen.

Wenn Sie unsere Beispiele für Ihre eigene Veranstaltung und Ihre Website übernehmen möchten, müssen Sie die betreffenden Ausdrücke für Ihre Veranstaltung anpassen.
Der einfachste Weg, den korrekten Code zu erhalten, ist unser Code-Generator.
Navigieren Sie zu :navpath:Ihre Veranstaltung → Einstellungen → Widget:, klicken Sie den Button :btn:Widget-Code generieren: und kopieren Sie die Code-Abschnitte von dort.

## Widget-Versionen

Wenn wir Änderungen am Widget vornehmen, vermeiden wir es nach Möglichkeit, die auf dieser Seite vorgestellten Konfigurationsoptionen zu ändern oder Kompatibilitätsprobleme mit der individuellen Gestaltung Ihrer Seite zu verursachen.
Es kann aber gelegentlich notwendig sein, Änderungen vorzunehmen, die sich auf die Widget-Struktur auswirken und Inkompatibilitäten verursachen können.
In solchen Fällen geben wir eine neue Version des Widgets heraus, die Sie an der höheren Versionsnummer an den Positionen von Script und Stylesheet erkennen.

Neue Widget-Versionen kündigen wir in den monatlichen Release-Notes von pretix an, die Sie auch über [unseren Newsletter](https://pretix.eu/about/en/blog/) beziehen können.
Sie können dann zu einem selbstgewählten Zeitpunkt auf die neue Version umstellen und haben so die Möglichkeit zu testen, ob Änderungen an Ihrer Gestaltung notwendig sind.

Wenn wir eine neue Version ankündigen, kündigen wir gleichzeitig an, wann die alte Version abgeschaltet wird.
Nach diesem Datum ersetzen wir die alte Version automatisch durch die neue.
Anders ausgedrückt: Wenn Sie nicht selbst manuell auf die neue Version umstellen, werden Sie nach dem Abschaltdatum automatisch umgestellt.
Dies kann zu Problemen führen, falls Sie die Widget-Gestaltung individuell angepasst haben.

## Changelog

### Version 2

 - Wir haben die HTML-Struktur des Widgets geändert, um die Barrierefreiheit des Widgets zu verbessern.
   Die deutlichsten Änderungen haben wir an der Kalenderansicht vorgenommen, die jetzt der Kalenderansicht im eigenständigen Shop ähnlicher sieht.
   Das geänderte Standard-Stylesheet bringt stärkere Farbkontraste, eine klare Hervorhebung des aktiven Elements und ähnliche Merkmale für bessere Barrierefreiheit.

 - Wir haben das Attribut `single-item-select` entfernt.
   Das Widget verwendet jetzt immer eine Darstellung im Button-Stil.

**Verfügbarkeit**:
Version 2 ist ab pretix 2025.5.0 verfügbar (veröffentlicht Ende Mai 2025).

**Abschaltung älterer Versionen**:
Ab pretix 2025.6.0 (veröffentlicht Ende Juni 2025) werden alle Benutzer\*innen von Version 1 automatisch auf Version 2 umgestellt.
Wir halten diese Frist bewusst kurz, damit unsere Kund\*innen die Anforderungen des [EU-Barrierefreiheitsstärkungsgesetzes](https://de.wikipedia.org/wiki/Barrierefreiheitsstärkungsgesetz) leichter erfüllen können.