# Widget

If you want to include your ticket shop on your event website or blog, you can use our embeddable widget. 
This way, users can buy their tickets without leaving your website. 

In order to obtain the HTML code for embedding your shop on your website, navigate to :navpath:Your Event → Settings → Widget:. 
Choose the "Language" in which the widget should be displayed. 
You may also choose a "Pre-selected voucher" for the widget. 
Once you have made your choices, click the :btn:Generate widget code: button. 

The website will produce two code snippets. 
Add the first code snippet to the `<head>` part of your website if possible. 
Alternatively, you can add it to `<body>`. 
It will look similar to this: 

```
<link rel="stylesheet" type="text/css" href="https://pretix.eu/demo/democon/widget/v1.css">
<script type="text/javascript" src="https://pretix.eu/widget/v1.en.js" async></script>
```
Add the second code snippet at the position where you want the widget to be displayed on your website. 
It will look similar to this: 

```
<pretix-widget event="https://pretix.eu/demo/democon/"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javascript, please <a target="_blank" href="https://pretix.eu/demo/democon/">click here</a>.
        </div>
    </div>
</noscript>
```

If you want to embed multiple widgets for different events on your page, add the first snippet only **once**. 
Generate the second snippet for every event and add each one to your website's HTML. 

!!! Note

    Some website builders such as Jimdo have trouble with our custom HTML tag. 
    In that case, edit the opening and closing tags in the first line of the second code snippet:  
    Replace `<pretix-widget …>` with `<div class="pretix-widget-compat" …>`.  
    Replace `</pretix-widget>` with `</div>`.  

## Example

Your embedded widget could look like the following:

<link rel="stylesheet" type="text/css" href="https://pretix.eu/demo/democon/widget/v1.css">
<script type="text/javascript" src="https://pretix.eu/widget/v1.en.js" async></script>
<pretix-widget event="https://pretix.eu/demo/democon/"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javascript, please <a target="_blank" href="https://pretix.eu/demo/democon/">click here</a>.
        </div>
    </div>
</noscript>

## Styling

You can use CSS to customize the appearance of the widget to match your website. 
If you use your browser's developer tools to inspect the rendered HTML of the widget, you will see that nearly every element has a custom class and all classes are prefixed with `pretix-widget`. 
You can override the styles or use your own custom stylesheet. 

## SSL

Buying a ticket usually involves entering sensitive data. 
Thus, we strongly suggest that you use SSL/HTTPS for the page that includes the widget. 
Initiatives such as [Let's Encrypt](https://letsencrypt.org/) allow you to obtain a SSL certificate free of charge.

pretix will use SSL for all data transferred from the widget even if the widget is included on a non-SSL site. 
However, if you are not using SSL for your site, it is possible for a man-in-the-middle attacker to make malicious changes to the widget. 
Using SSL for data transfers is a standard practice now. 
Your customers might not trust your website if their browser does not display the secure lock icon :fa3-lock: while they are using it. 

If your website does not use SSL, the checkout process will open in a new tab in your customer's browsers. 
If you are confident to have a good reason for not using SSL, you can override this behavior with the `skip-ssl-check` attribute:

```
<pretix-widget event="https://pretix.eu/demo/democon/" skip-ssl-check></pretix-widget>
```

!!! Note 
    The examples provided in this article all use the base URL `pretix.eu`, the organizer `demo`, and the event `democon`.
    If you want to apply these examples to your own event and website, you need to replace these strings with the ones matching your event. 

## Always open a new tab

By default, the checkout process will open in a new tab on devices with smaller screens. 
If you want the checkout process to always open a new tab regardless of screen size, you can pass the `disable-iframe` attribute: 

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-iframe></pretix-widget>
```

## Always show events info

By default, the widget will only display event info such as title, location, and front page text if it is linked to an event series. 
You can pass the optional `display-event-info` attribute to change this behavior. 
If you pass it with the value `"false"`, even an event series will be displayed without information. 
If you pass the attribute with `"true"` or any other value other than 
Pass it with the value `"auto"` for the default behavior. 
Any other value than `"false"` or `"auto"` is handled like `"true"`. 

```
<pretix-widget event="https://pretix.eu/demo/democon/" display-event-info></pretix-widget>
```

## Pre-selecting a voucher

You can pre-select a voucher for the widget with the `voucher` attribute:

```
<pretix-widget event="https://pretix.eu/demo/democon/" voucher="ABCDE123456"></pretix-widget>
```

This way, the widget will only display products that can be bought with the voucher and prices will be changed as defined by the voucher. 
You can also generate a code snippet that includes a voucher by using the "Pre-selected voucher" field on the widget settings page. 

<pretix-widget event="https://pretix.eu/demo/democon/" voucher="ABCDE123456"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javascript, please <a target="_blank" href="https://pretix.eu/demo/democon/">click here</a>.
        </div>
    </div>
</noscript>

## Disabling the voucher input

If you want to disable voucher input in the widget, you can pass the `disable-vouchers` attribute:

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-vouchers></pretix-widget>
```

## Enabling the button-style single item select

By default, the widget uses simple checkboxes for the selection of items that can only be bought in quantities of one. 
This is different from the shop page, which uses a button containing a checkbox and the label ":fa3-shopping-cart: Select". 
If you want to use the same style of checkbox button in the widget, pass the `single-item-select` attribute:

```
<pretix-widget event="https://pretix.eu/demo/democon/" single-item-select="button"></pretix-widget>
```

The result will look like this:

![A plain wide button containing a checkbox, a shopping cart symbol and the text "Select"](../assets/screens/widget/checkbox_button.png "Button-like checkbox")

!!! Note

    Due to compatibility with existing widget installations, the default value for `single-item-select` is `checkbox`. 
    This might change in the future, so make sure, to set the attribute to `single-item-select="checkbox"` if you need it.

## Filtering products

You can filter the products shown in the widget by passing a list of product IDs separated by comma. 
In order to find a product's ID, navigate to :navpath:Event → :fa3-ticket: Products → Products:. 
The product ID is displayed as a number preceded by a hashtag below the product's name in the list. 
You need the number **without** the hashtag. 
Alternatively, edit the product. 
The number before the last slash in the URL is the product ID.

In order to display only products `#562195` and `#562202` in the widget, pass them like this: 

```
<pretix-widget event="https://pretix.eu/demo/democon/" items="562195,562202"></pretix-widget>
```

You can also filter for categories. 
In order to find a category's ID, navigate to :navpath:Your event → :fa3-ticket: Products → Categories:. 
Edit the category in question. 
The number before the last slash in the URL is the category ID.
In order to display only products from the categories `#162620` and `#162647` in the widget, pass them like this: 

```
<pretix-widget event="https://pretix.eu/demo/democon/" categories="162620,162647"></pretix-widget>
```

You can also filter for product variations. 
In order to find a product variation's ID, navigate to :navpath:Event → :fa3-ticket: Products → Products:. 
Edit the product in question and open the :btn:Variations: tab. 
The product ID is displayed as a number preceded by a hashtag below the variation's name in the list. 
You need the number **without** the hashtag. 

In order to display only variations `#437143`, `#437154`, and `#437155` in the widget, pass them like this: 

```
<pretix-widget event="https://pretix.eu/demo/democon/" variations="437143,437154,437155"></pretix-widget>
```

## Multi-event selection

You can display multiple event shops in a single widget. 

If you want to display only a single date from an event series, use the `subevent` attribute: 

```
<pretix-widget event="https://pretix.eu/demo/series/" subevent="4387749"></pretix-widget>
```

If you do not use the `subevent` attribute, all dates in the event series will be displayed. 

If you want to include all your public events, pass the URL to your customer account to the `event` attribute instead of an event: 

```
<pretix-widget event="https://pretix.eu/demo/"></pretix-widget>
```

You can use the `list-type` attribute to define if your events will be displayed in a monthly calendar view, a weekly calendar view or a list view. 
If you do not include this attribute,it will default to the setting you setting you chose under :navpath:Your organizer → :fa3-wrench: Settings → General, 
If you do not set it, the choice will be taken from your organizer settings:

```
<pretix-widget event="https://pretix.eu/demo/series/" list-type="list"></pretix-widget>
<pretix-widget event="https://pretix.eu/demo/series/" list-type="calendar"></pretix-widget>
<pretix-widget event="https://pretix.eu/demo/series/" list-type="week"></pretix-widget>
```

For performance reasons, the system will always display a calendar view if you have more than 100 events. 
You can see an example here:

<pretix-widget event="https://pretix.eu/demo/series/" list-type="calendar"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javascript, please <a target="_blank" href="https://pretix.eu/demo/series/">click here</a>.
        </div>
    </div>
</noscript>

You can filter events by metadata attributes. 
You can create these attributes by navigating to :navpath:Your organizer → :fa3-wrench: Settings → Event metadata: and clicking the :btn-icon:fa3-plus: Create a new property: button. 

If you want to assign the metadata property to a singular event, navigate to :navpath:Your event → :fa3-wrench: Settings → General:. 
On the :btn:Basics: tab, edit the relevant property under "Meta data". 

If you want to assign the property to dates in an event series, navigate to :navpath:Your event → :fa3-calendar: Dates:. 
Edit or create the dates in question and set the relevant property under "Meta data". 

For example, if you set up a metadata property called "Promoted" that you set to "Yes" on some events, you can pass a filter like this:

```
<pretix-widget event="https://pretix.eu/demo/series/" list-type="list" filter="attr[Promoted]=Yes"></pretix-widget>
```

If you have enabled public filters in your meta data attribute configuration, the widget will display a filter form. 
To disable the filter form, use:

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-filters></pretix-widget>
```

## pretix Button

Instead of a product list, you can also display just a single button. 
When pressed, the button will add a number of products associated with the button to the cart and will immediately proceed to checkout. 
You can try out this behavior here:

<pretix-button event="https://pretix.eu/demo/democon/" items="item_6424=1">Buy ticket!</pretix-button>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javascript, please <a target="_blank" href="https://pretix.eu/demo/democon/">click here</a>.
        </div>
    </div>
</noscript>

You can embed the pretix Button just like the pretix Widget. 
Just like above, first embed the CSS and JavaScript resources. 
Then, instead of the `pretix-widget` tag, use the `pretix-button` tag:

```
<pretix-button event="https://pretix.eu/demo/democon/" items="item_6424=1">
    Buy ticket!
</pretix-button>
```

The `pretix-button` element takes an additional `items` attribute that specifies the items that should be added to the cart. 
The syntax of this attribute is `item_ITEMID=1,item_ITEMID=2,variation_ITEMID_VARID=4` where `ITEMID` are the internal IDs of items to be added and `VARID` are the internal IDs of variations of those items, if the items have variations. 
If you omit the `items` attribute, the general start page will be presented.

In case you are using an event series, you will need to specify the date for which the item(s) should be put in the cart. 
This can be done by specifying the `subevent`-attribute. 

Just as the widget, the button supports the optional attributes `voucher`, `disable-iframe`, and `skip-ssl-check`.

You can style the button using the `pretix-button` CSS class.

## Dynamically opening the widget

You can get the behavior of the pretix button without a button at all, so you can trigger it from your own code in response to a user action. 
Usually, this will open an overlay with your ticket shop, however in some cases, such as missing HTTPS encryption on your case or a really small screen (mobile), it will open a new tab instead of an overlay. 
Therefore, make sure you call this *in direct response to a user action*, otherwise most browser will block it as an unwanted pop-up.

To do so, you can call `window.PretixWidget.open`, which has the following signature:

```
window.PretixWidget.open(target_url[, voucher[, subevent[, items[, widget_data[, skip_ssl_check]]]]]) 
```

Parameters:

- **target_url** (string): The URL of the ticket shop. 
- **voucher** (string): A voucher code to be pre-selected, or `null`.
- **subevent** (string): A subevent to be pre-selected, or `null`.
- **items** (array): A collection of items to be put in the cart, of the form `[{"item": "item_3", "count": 1}, {"item": "variation_5_6", "count": 4}]`
- **widget_data** (object): Additional data to be passed to the shop, see below.
- **skip_ssl_check** (boolean): Whether to ignore the check for HTTPS. 
  Only to be used during development.

## Dynamically loading the widget

If you need to control the way or timing the widget loads, for example because you want to modify user data (see below) dynamically via JavaScript, you can register a listener that we will call before creating the widget:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    // Will be run before we create the widget.
}
</script>
```

You can suppress us loading the widget and/or modify the user data passed to the widget:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    window.PretixWidget.build_widgets = false;
    window.PretixWidget.widget_data["email"] = "test@example.org";
}
</script>
```

If you want to trigger loading the widgets, call `window.PretixWidget.buildWidgets()`.

## Waiting for the widget to load or close

If you want to run custom JavaScript once the widget is fully loaded or when it is closed, you can register callback functions. 
Note that these function might be run multiple times, for example if you have multiple widgets on a page or if the user switches e.g. from an event list to an event detail view:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    window.PretixWidget.addLoadListener(function () {
        console.log("Widget has loaded!");
    });
    window.PretixWidget.addCloseListener(function () {
        console.log("Widget has been closed!");
    });
}
</script>
```

## Passing user data to the widget

If you display the widget in a restricted area of your website and you want to pre-fill fields in the checkout process with known user data to save your users some typing and increase conversions, you can pass additional data attributes with that information:

```
<pretix-widget event="https://pretix.eu/demo/democon/"
    data-attendee-name-given-name="John"
    data-attendee-name-family-name="Doe"
    data-invoice-address-name-given-name="John"
    data-invoice-address-name-family-name="Doe"
    data-email="test@example.org"
    data-question-L9G8NG9M="Foobar">
</pretix-widget>
```

This works for the pretix button as well, if you also specify a product.

As data attributes are reactive, you can change them with JavaScript as well. 
Please note that once the user started the checkout process, we do not update the data-attributes in the existing checkout process to not interrupt the checkout UX.

When updating data-attributes through JavaScript, make sure you do not have a stale reference to the HTMLNode of the widget. 
When the widget is created, the original HTMLNode can happen to be replaced. 
So make sure to always have a fresh reference like so `document.querySelectorAll("pretix-widget, pretix-button, .pretix-widget-wrapper")`

Currently, the following attributes are understood by pretix itself:

 - `data-email` will pre-fill the order email field as well as the attendee email field (if enabled).

 - `data-question-IDENTIFIER` will pre-fill the answer for the question with the given identifier. 
 You can view and set identifiers in the *Questions* section of the backend.

 - Depending on the person name scheme configured in your event settings, you can pass one or more of `data-attendee-name-full-name`, `data-attendee-name-given-name`, `data-attendee-name-family-name`, `data-attendee-name-middle-name`, `data-attendee-name-title`, `data-attendee-name-calling-name`, `data-attendee-name-latin-transcription`. 
 If you don't know or don't care, you can also just pass a string as `data-attendee-name`, which will pre-fill the last part of the name, whatever that is.

 - `data-invoice-address-FIELD` will pre-fill the corresponding field of the invoice address. 
 Possible values for `FIELD` are `company`, `street`, `zipcode`, `city`, `country`, `internal-reference`, `vat-id`, and `custom-field`, as well as fields specified by the naming scheme such as `name-title` or `name-given-name` (see above). `country` expects a two-character country code.

 - If `data-fix="true"` is given, the user will not be able to change the other given values later. 
 This currently only works for the order email address as well as the invoice address. 
 Attendee-level fields and questions can always be modified. 
 Note that this is not a security feature and can easily be overridden by users, so do not rely on this for authentication.

 - If `data-consent="…"` is given, the cookie consent mechanism will adopt the consent for the given cookie providers. 
 All other providers will be disabled, no consent dialog will be shown and it will not be possible to change the cookie settings inside the widget. 
 This is useful if you already asked the user for consent and don't want them to be asked again. 
 Example: `data-consent="facebook,google_analytics"`

    When using the pretix-tracking plugin, the following values are supported:: `adform, facebook, gosquared, google_ads, google_analytics, hubspot, linkedin, matomo, twitter`

    If the user has refused consent for all cookie providers, use `data-consent="none"` to disable all providers.

Any configured pretix plugins might understand more data fields. 
For example, if the appropriate plugins on pretix Hosted or pretix Enterprise are active, you can pass the following fields:

 - If you use the campaigns plugin, you can pass a campaign ID as a value to `data-campaign`. 
 This way, all orders made through this widget will be counted towards this campaign.

 - If you use the tracking plugin, you can enable cross-domain tracking. 
 Please note: when you run your pretix-shop on a subdomain of your main tracking domain, then you do not need cross-domain tracking as tracking automatically works across subdomains. 
 See `custom_domain`{.interpreted-text role="ref"} for how to set this up.

Add the embedding website to your [Referral exclusions](https://support.google.com/analytics/answer/2795830) in your Google Analytics settings.

Add Google Analytics as you normally would with all your [window.dataLayer]{.title-ref} and [gtag]{.title-ref} configurations. 
Also add the widget code normally. 
Then you have two options:

- Block loading of the widget at most 2 seconds or until Google's client- and session-ID are loaded. 
  This method uses [window.pretixWidgetCallback]{.title-ref}. 
  Note that if it takes longer than 2 seconds to load, client- and session-ID are never passed to the widget. 
  Make sure to replace all occurrences of <MEASUREMENT_ID\> with your Google Analytics MEASUREMENT_ID (G-XXXXXXXX):

```
<script type="text/javascript">
    window.pretixWidgetCallback = function () {
        window.PretixWidget.build_widgets = false;
        window.addEventListener('load', function() { // Wait for GA to be loaded
            if (!window['google_tag_manager']) {
                window.PretixWidget.buildWidgets();
                return;
            }

            var clientId;
            var sessionId;
            var loadingTimeout;
            function build() {
                // use loadingTimeout to make sure build() is only called once
                if (!loadingTimeout) return;
                window.clearTimeout(loadingTimeout);
                loadingTimeout = null;
                if (clientId) window.PretixWidget.widget_data["tracking-ga-id"] = clientId;
                if (sessionId) window.PretixWidget.widget_data["tracking-ga-sessid"] = sessionId;
                window.PretixWidget.buildWidgets();
            };
            // make sure to build pretix-widgets if gtag fails to load either client_id or session_id
            loadingTimeout = window.setTimeout(build, 2000);

            gtag('get', '<MEASUREMENT_ID>', 'client_id', function(id) {
                clientId = id;
                if (sessionId !== undefined) build();
            });
            gtag('get', '<MEASUREMENT_ID>', 'session_id', function(id) {
                sessionId = id;
                if (clientId !== undefined) build();
            });
        });
    };
</script>
``` 

- Or asynchronously set data-attributes – the widgets are shown immediately, but once the user has started checkout, data-attributes are not updated. 
  Make sure to replace all occurrences of \<MEASUREMENT_ID\> with your Google Analytics MEASUREMENT_ID (G-XXXXXXXX):

``` 
<script type="text/javascript">
    window.addEventListener('load', function() {
        gtag('get', '<MEASUREMENT_ID>', 'client_id', function(id) {
            const widgets = document.querySelectorAll("pretix-widget, pretix-button, .pretix-widget-wrapper");
            widgets.forEach(widget => widget.setAttribute("data-tracking-ga-id", id))
        });
        gtag('get', '<MEASUREMENT_ID>', 'session_id', function(id) {
            const widgets = document.querySelectorAll("pretix-widget, pretix-button, .pretix-widget-wrapper");
            widgets.forEach(widget => widget.setAttribute("data-tracking-ga-sessid", id))
        });
    });
</script>  
``` 

## Offering wallet payments (Apple Pay, Google Pay) within the widget

Some payment providers (such as Stripe) also offer Apple or Google Pay. 
But in order to use them, the domain of the payment needs to be approved first. 
As of right now, pretix will take care of the domain verification process for you automatically, when using Stripe. 
However, pretix can only validate the domain that is being used for your default, "stand-alone" shop (such as <https://pretix.eu/demo/democon/> ).

When embedding the widget on your website, the domain of the embedding page will also need to be validated in order to be able to use it for wallet payments.

The details might vary from payment provider to payment provider, but generally speaking, it will either involve just telling your payment provider the domain name and (for Apple Pay) placing an `apple-developer-merchantid-domain-association`-file into the `.well-known`-directory of your domain.

Further reading:

 - [Stripe Payment Method Domain registration](https://stripe.com/docs/payments/payment-methods/pmd-registration)

## Content Security Policy

When using a Content Security Policy (CSP) on your website, you may need to make some adjustments. 
If your pretix shop is running under a custom domain, you need to add the following rules:

 - `script-src`: `'unsafe-eval' https://pretix.eu` (adjust to your domain for self-hosted pretix)
 - `style-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted)
 - `connect-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted)
 - `frame-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted)
 - `img-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted) and for pretix Hosted additionally add `https://cdn.pretix.space`

## External payment providers and Cross-Origin-Opener-Policy

If you use a payment provider that opens a new window during checkout (such as PayPal), be aware that setting `Cross-Origin-Opener-Policy: same-origin` results in an empty popup-window being opened in the foreground. 
This is due to JavaScript not having access to the opened window. 
To mitigate this, you either need to always open the widget's checkout in a new tab (see `Always open a new tab`{.interpreted-text role="ref"}) or set `Cross-Origin-Opener-Policy: same-origin-allow-popups`. 

## Working with Cross-Origin-Embedder-Policy

The pretix widget is unfortunately not compatible with `Cross-Origin-Embedder-Policy: require-corp`. 
If you include the `crossorigin` attributes on the `<script>` and `<link>` tag as shown above, the widget can show a calendar or product list, but will not be able to open the checkout process in an iframe. 
If you also set `Cross-Origin-Opener-Policy: same-origin`, the widget can auto-detect that it is running in an isolated enviroment and will instead open the checkout process in a new tab.
