# Widget

If you want to include your ticket shop on your event website or blog, you can use the embeddable widget. 
This way, users can buy their tickets without leaving your website. 
Alternatively, you can use the [pretix Button](widget.md#pretix-button) to instantly select some products and proceed to checkout for the user. 

Your embedded widget could look like the following:

<link rel="stylesheet" type="text/css" href="https://pretix.eu/demo/democon/widget/v2.css" crossorigin>
<script type="text/javascript" src="https://pretix.eu/widget/v2.en.js" async crossorigin></script>
<pretix-widget event="https://pretix.eu/demo/democon/"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javacript, please <a target="_blank" href="https://pretix.eu/demo/democon/">click here</a>.
        </div>
    </div>
</noscript>

This article will guide you through the basic setup of the widget and some advanced configuration options. 

## Prerequisites 

You need to create at least one event before you can offer access to your ticket shop through the widget. 
The website will only display the widget if your ticket shop is active. 

You need to have a website and the ability to make changes to it. 
Some basic knowledge of JavaScript is helpful. 

## General usage

This section explains how to embed the pretix widget or the pretix button on your website once or several times, as well as how to style the widget. 
It also explains how to use the widget for more than just a singular event or a single date within an event series. 

### Embedding the widget on your website

In order to obtain the HTML code for embedding your shop on your website, navigate to :navpath:Your Event → Settings → Widget:. 
Choose the "Language" for the widget. 
The page also allows you to choose a "Pre-selected voucher" for the widget. 
This can be useful if you want to offer discounts or voucher-exclusive products to visitors of your website. 
Once you have made your choices, click the :btn:Generate widget code: button. 

The website will produce two code snippets. 
The first snippet sources the CSS and JavaScript resources for the widget from the pretix server. 
Add this snippet to the `<head>` part of your website if you want to comply general conventions in webdesign. 
This has the advantage of slightly better performance on slow connections. 
Alternatively, you can also add it to `<body>`. 
The code snippet will look similar to this: 

```
<link rel="stylesheet" type="text/css" href="https://pretix.eu/demo/democon/widget/v2.css">
<script type="text/javascript" src="https://pretix.eu/widget/v2.en.js" async></script>
```
Add the second code snippet at the position where you want the widget to appear on your website. 
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

!!! Note 
    The examples provided in this article all use the base URL `pretix.eu`, the organizer `demo`, and the event `democon`.
    If you want to apply these examples to your own event and website, you need to replace these strings with the ones matching your event. 
    The easiest way to ensure that you have the right code is using the code generator. 
    Navigate to :navpath:Your Event → Settings → Widget:, click the :btn:Generate widget code: button, and copy the code snippets from there. 

### Embedding multiple widgets on your website

If you want to embed multiple widgets for different events on your page, add the first snippet only **once**. 
Generate the second snippet for every event and add each one to your website's HTML. 

!!! Note

    Some website builders such as Jimdo have trouble with our custom HTML tag. 
    In that case, edit the opening and closing tags in the first line of the second code snippet:  
    Replace `<pretix-widget …>` with `<div class="pretix-widget-compat" …>`.  
    Replace `</pretix-widget>` with `</div>`.  

### Styling

You can use CSS to customize the appearance of the widget to match your website. 
If you use your browser's developer tools to inspect the rendered HTML of the widget, you will see that nearly every element has a custom class and all classes are prefixed with `pretix-widget`. 
You can override the styles or use your own custom stylesheet. 

!!! Note 
    The widget is designed to conform with European accessibility standards. 
    Make sure that any changes you make to customize the widget do not break accessibility, for instance by choosing colors with too little contrast. 


### pretix Button

Instead of the full widget, you can also display a simple button. 
Clicking this button adds a predefined set of to the cart and proceeds to checkout. 
You can try out this behavior here:

<pretix-button event="https://pretix.eu/demo/democon/" items="item_6424">Buy ticket!</pretix-button>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javascript, please <a target="_blank" href="https://pretix.eu/demo/democon/">click here</a>.
        </div>
    </div>
</noscript>

You can embed the pretix Button just like the pretix Widget. 
In order to add the pretix Button to your website, add the CSS and JavaScript resources as described under ["Embedding the widget on your website"](widget.md#embedding-the-widget-on-your-website)
Then, instead of the `pretix-widget` tag, use the `pretix-button` tag:

```
<pretix-button event="https://pretix.eu/demo/democon/" items="item_6424=1">
    Buy ticket!
</pretix-button>
```
Use the `items` attribute to specify the items to be added to the cart. 
The syntax of this attribute is: 

```item_ITEMID=1,item_ITEMID=2,variation_ITEMID_VARID=4```

Replace each instance of `ITEMID` with the ID of the item to be added. 
Replace each instance of `VARID` with the ID of variations of those items. 
Omit `variation_ITEMID_VARID=4` if the items do not have variations. 
Use the number behind the `=` symbol to specify the number of this item or variation to be added to the cart. 

If you do not include the `items` attribute or do not pass a valid product or variation ID, clicking the button will open your ticket shop in a new browser tab without adding any items to the cart. 

If the button is linked to an event series, use the `subevent`-attribute to specify the date for which the items should be added to the cart. 

The button supports the optional attributes `voucher`, `disable-iframe`, and `skip-ssl-check`.
You can style the button using the `pretix-button` CSS class.

### Using the widget for multiple events

You can display multiple event shops in a single widget. 
If you want to include all your public events, pass the URL to your customer account to the `event` attribute instead of an event: 

```
<pretix-widget event="https://pretix.eu/demo/"></pretix-widget>
``` 

### Using the widget for an event series 

You can link the widget to an event series. 
By default, the widget will display all dates in the event series. 
If you want to display only a single date from the series, use the `subevent` attribute: 

```
<pretix-widget event="https://pretix.eu/demo/series/" subevent="4387749"></pretix-widget>
```

You can use the `list-type` attribute to define if your events will be displayed in a monthly calendar view, a weekly calendar view, or a list view. 
If you do not include this attribute, it will default to the setting you chose under :navpath:Your organizer → :fa3-wrench: Settings → General:.  

```
<pretix-widget event="https://pretix.eu/demo/series/" list-type="list"></pretix-widget>
<pretix-widget event="https://pretix.eu/demo/series/" list-type="calendar"></pretix-widget>
<pretix-widget event="https://pretix.eu/demo/series/" list-type="week"></pretix-widget>
```

For performance reasons, the system will always display a monthly calendar view if you have more than 100 events. 
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

## Advanced

### Loading

This section explains how to customize the way in which the widget loads and opens. 

#### Opening the widget dynamically

You can call a function to open the widget dynamically in response to a user action. 
This is similar to the behavior of the [pretix Button](widget.md#pretix-button), but you can call it from any part of your website's code. 

Usually, this will open an overlay with your ticket shop. 
In some circumstances, such as missing HTTPS encryption or a small screen size, it will open a new tab instead. 
Therefore, only call this function *in direct response to a user action*, otherwise most browsers will block it as an unwanted pop-up. 

Call `window.PretixWidget.open`, which has the following signature:

```
window.PretixWidget.open(target_url[, voucher[, subevent[, items[, widget_data[, skip_ssl_check]]]]]) 
```

Parameters:

- **target_url** (string): The URL of the ticket shop. 
- **voucher** (string): A voucher code to be pre-selected, or `null`.
- **subevent** (string): A date from an event series to be pre-selected, or `null`.
- **items** (array): A collection of items to be put in the cart, of the form `[{"item": "item_3", "count": 1}, {"item": "variation_5_6", "count": 4}]`
- **widget_data** (object): Additional data to be passed to the shop, see below.
- **skip_ssl_check** (boolean): Whether to ignore the check for HTTPS. 
  Only use this during development.

#### Loading the widget dynamically 

You may need to control when and how the widget loads, for example because you want to modify user data (see below) dynamically via JavaScript. 
You can register a listener that will be run before creating the widget:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    // Will be run before we create the widget.
}
</script>
```

You can suppress the loading of the widget or modify the user data passed to the widget:

```
<script type="text/javascript">
window.pretixWidgetCallback = function () {
    window.PretixWidget.build_widgets = false;
    window.PretixWidget.widget_data["email"] = "test@example.org";
}
</script>
```

In order to trigger loading the widgets, call `window.PretixWidget.buildWidgets()`.

#### Waiting for the widget to load or close

If you want to run custom JavaScript once the widget is fully loaded or when it is closed, you can register callback functions:

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

You can run these functions multiple times, for example if you have multiple widgets on a page or if the user changes the list/calendar view. 

### Customizing the user experience 

This section explains how to customize the behavior of the widget regarding user experience. 

#### Always open a new tab

By default, the checkout process will open in a new tab on devices with smaller screens. 
If you want the checkout process to always open in a new tab regardless of screen size, you can pass the `disable-iframe` attribute: 

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-iframe></pretix-widget>
```

#### Always show event info

By default, the widget will only display event info such as title, location, and front page text if it is linked to an event series. 
You can pass the optional `display-event-info` attribute to change this behavior. 
If you pass it with the value `"false"`, even an event series will be displayed without information. 
Pass it with the value `"auto"` for the default behavior. 
Any value other than `"false"` or `"auto"` is handled like `"true"`. 

```
<pretix-widget event="https://pretix.eu/demo/democon/" display-event-info></pretix-widget>
```

#### Pre-selecting a voucher

You can pre-select a voucher for the widget with the `voucher` attribute:

```
<pretix-widget event="https://pretix.eu/demo/democon/" voucher="ABCDE123456"></pretix-widget>
```

This way, the widget will only display products that can be bought with the voucher and prices will be changed as defined by the voucher. 
You do **not** need to copy and edit this code. 
It may be easier to generate a code snippet that includes a voucher by using the "Pre-selected voucher" field on the widget settings page. 

Here is an example of a widget with a voucher pre-selected: 

<pretix-widget event="https://pretix.eu/demo/democon/" voucher="ABCDE123456"></pretix-widget>
<noscript>
   <div class="pretix-widget">
        <div class="pretix-widget-info-message">
            JavaScript is disabled in your browser. 
            To access our ticket shop without javascript, please <a target="_blank" href="https://pretix.eu/demo/democon/">click here</a>.
        </div>
    </div>
</noscript>

#### Disabling the voucher input

If you want to disable voucher input in the widget, you can pass the `disable-vouchers` attribute:

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-vouchers></pretix-widget>
```

#### Filtering products

You can filter the products displayed in the widget by passing a list of product IDs separated by commas. 
In order to find a product's ID, navigate to :navpath:Event → :fa3-ticket: Products → Products:. 
The page displays the product ID as a number preceded by a hashtag below the product's name in the list. 
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

#### Filtering by metadata attributes 

If you are hosting several events or dates in an event series, but only want to display some of them in the widget, then you should use metadata attributes. 
This section explains how to create metadata attributes, assign them to your events or dates, and set a filter in the widget. 

You can create metadata attributes by navigating to :navpath:Your organizer → :fa3-wrench: Settings → Event metadata: and clicking the :btn-icon:fa3-plus: Create a new property: button. 

If you want to assign the metadata property to a singular event, navigate to :navpath:Your event → :fa3-wrench: Settings → General:. 
On the :btn:Basics: tab, edit the relevant property under "Meta data". 

If you want to assign the property to dates in an event series, navigate to :navpath:Your event → :fa3-calendar: Dates:. 
Edit or create the dates in question and set the relevant property under "Meta data". 

For example, if you set up a metadata property called "Promoted" that you set to "Yes" on some events, you can pass a filter like this:

```
<pretix-widget event="https://pretix.eu/demo/series/" list-type="list" filter="attr[Promoted]=Yes"></pretix-widget>
```

If you have enabled public filters in your metadata attribute configuration, the widget will display a filter form. 
To disable the filter form, use:

```
<pretix-widget event="https://pretix.eu/demo/democon/" disable-filters></pretix-widget>
```

### User data

This section explains how to handle user data using the widget. 

#### Passing user data to the widget

If you display the widget on a page that requires user login, you can pre-fill fields in the checkout process with known user data. 
This can save your customers some typing and increase conversions. 
You can also pass additional data attributes with that information: 

```
<pretix-widget event="https://pretix.eu/demo/democon/"
    data-attendee-name-given-name="Jamie"
    data-attendee-name-family-name="Doe"
    data-invoice-address-name-given-name="Jamie"
    data-invoice-address-name-family-name="Doe"
    data-email="test@example.org"
    data-question-L9G8NG9M="Foobar">
</pretix-widget>
```

You can also do this on the pretix Button, but you also need to specify the `items` attribute. 

Data attributes are reactive. 
Thus, you can use JavaScript to change them. 
Once the user has started the checkout process, pretix does not update data attributes in the existing checkout process. 
Doing so would interrupt the process and the user would have to start over. 

When updating data attributes through JavaScript, make sure you do not have a stale reference to the HTMLNode of the widget. 
When the widget is created, it is possible that the original HTMLNode is replaced. 
Use the following code to ensure that the reference is fresh:  

```document.querySelectorAll("pretix-widget, pretix-button, .pretix-widget-wrapper")```

Currently the following data attributes are understood by pretix:

 - `data-email` will pre-fill the order email field as well as the attendee email field (if enabled).

 - `data-question-IDENTIFIER` will pre-fill the answer for the question with the given identifier. 
 You can view identifiers by navigating to :navpath:Your event → :fa3-ticket: Products → Questions:. 
 In order to set an internal identifier, edit or create a question, switch to the :btn:Advanced: tab and use the "Internal identifier" field. 

 - `data-attendee-name` will pre-fill the last part of the name. 
   The exact behavior depends on your configuration under :navpath:Your event → :fa3-wrench: Settings → General:, on the :btn:Customer and attendee data: tab. 
   For more control over the name that is pre-filled, use the following attributes. 
   The best choice depends on your configuration of the naming scheme in the event settings. 
    - `data-attendee-name-full-name`
     -  `data-attendee-name-given-name`
     - `data-attendee-name-family-name`
     - `data-attendee-name-middle-name`
     - `data-attendee-name-title`
     - `data-attendee-name-calling-name`
     - `data-attendee-name-latin-transcription`
   
 - `data-invoice-address-FIELD` will pre-fill the corresponding field of the invoice address. 
   Possible values for `FIELD` are:  
     - `company`
     - `street`
     - `zipcode`
     - `city`
     - `country` (expects a two-character country code)
     - `internal-reference`
     - `vat-id`
     - `custom-field`
     - fields specified by the naming scheme such as `name-title` or `name-given-name` 
     `country` 

 - If `data-fix="true"` is given, the user will not be able to change the other given values later. 
   This currently only works for the order email address as well as the invoice address. 
   The user will always be able to modify attendee-level fields and questions. 
   This is not a security feature. 
   Users can easily override it. 
   Do not rely on this for authentication.

 - If `data-consent="…"` is given, the cookie consent mechanism will adopt the consent for the given cookie providers. 
   All other providers will be disabled, no consent dialog will be shown and it will not be possible to change the cookie settings inside the widget. 
   This is useful if you already asked the user for consent and do not want the widget to aske them again. 
   Example: `data-consent="facebook,google_analytics"`
   If the user has refused consent for all cookie providers, use `data-consent="none"` to disable all providers.
   The following values are supported by the pretix "Tracking codes" plugin: 
     - `adform`
     - `facebook`
     - `gosquared`
     - `google_ads`
     - `google_analytics`
     - `hubspot`
     - `linkedin`
     - `matomo`
     - `twitter`

Any active pretix plugins might understand more data attributes. 
For instance, if you are using the campaigns plugin, you can pass a campaign ID as a value to `data-campaign`. 
This way, the plugin will count all orders made through this widget towards this campaign. 

#### Using tracking with the pretix Widget

If you use the tracking plugin, you can enable cross-domain tracking. 
When you run your pretix shop on a subdomain of your main tracking domain, then you do not need cross-domain tracking. 
Tracking across subdomains works with no cross-domain tracking setup needed. 
Refer to the article on [custom domains](custom-domain.md) for further information. 

Add the embedding website to your [referral exclusions](https://support.google.com/analytics/answer/2795830) in your Google Analytics settings.

Add Google Analytics like you would on any other page, including your [window.dataLayer]{.title-ref} and [gtag]{.title-ref} configurations. 
Add the widget code. 
Then you have two options:

The first option is blocking the loading of the widget until Google's client and session ID are loaded, or for a maximum of two seconds. 
This is similar to [loading the widget dynamically](widget.md#loading-the-widget-dynamically). 
If it takes longer than two seconds to load, client and session ID are not passed to the widget. 
Include the following code on your website after replacing all occurrences of <MEASUREMENT_ID\> with your Google Analytics MEASUREMENT_ID (G-XXXXXXXX):

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

The other option is asynchronously setting data-attributes. 
The widgets are displayed immediately, but once the user has entered checkout, data attributes are not updated. 
Include the following code on your website after replacing all occurrences of \<MEASUREMENT_ID\> with your Google Analytics MEASUREMENT_ID (G-XXXXXXXX):

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

### Security

This section explains aspects of embedding the widget that are relevant for security: SSL/HTTPS, policy settings on your website, and domain verification for certain payment methods. 

#### SSL

Buying a ticket usually involves entering sensitive data. 
Thus, we strongly suggest that you use SSL/HTTPS for the page that includes the widget. 
Initiatives such as [Let's Encrypt](https://letsencrypt.org/) allow you to obtain a SSL certificate free of charge.

pretix will use SSL for all data transferred from the widget even if the widget is included on a non-SSL site. 
However, if you are not using SSL for your site, it is possible for a man-in-the-middle attacker to make malicious changes to the widget. 
Using SSL for data transfers is standard practice now. 
Your customers might not trust your website if their browser does not display the secure lock icon :fa3-lock: while they are using it. 

If your website does not use SSL, the checkout process will open in a new tab in your customer's browsers. 
If you are confident that you have a good reason for not using SSL, you can override this behavior with the `skip-ssl-check` attribute:

```
<pretix-widget event="https://pretix.eu/demo/democon/" skip-ssl-check></pretix-widget>
```

#### Content Security Policy

If you are using a Content Security Policy (CSP) on your website, you may need to make some adjustments. 
If your pretix shop is running under a custom domain, you need to add the following rules:

 - `script-src`: `'unsafe-eval' https://pretix.eu` (adjust to your domain for self-hosted pretix)
 - `style-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted)
 - `connect-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted)
 - `frame-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted)
 - `img-src`: `https://pretix.eu` (adjust to your domain for self-hosted pretix **and** for custom domain on pretix Hosted). 
    For pretix Hosted, also add `https://cdn.pretix.space`. 

#### Offering Apple Pay via Stripe through the widget

If you are using Stripe as a payment provider and want to offer Apple Pay through the widget, then you have to verify the domain with Apple Pay first. 
pretix will automatically validate the domain that is being used for your shop regardless of the edition of pretix and your domain settings. 
But when embedding the widget on your website, your domain will also need to get validation in order to be able to use it for Apple Pay. 

Please refer to the Stripe documentation page on how to [register domains for payment methods](https://stripe.com/docs/payments/payment-methods/pmd-registration) for further information. 

#### External payment providers and Cross Origin Opener Policy

If you use a payment provider that opens a new window during checkout (such as PayPal), then setting `Cross-Origin-Opener-Policy: same-origin` results in an empty popup window being opened in the foreground. 
This is due to JavaScript not having access to the opened window. 
To mitigate this, you either need to [always open the widget's checkout in a new tab](widget.md#always-open-a-new-tab) or set `Cross-Origin-Opener-Policy: same-origin-allow-popups`. 

#### Working with Cross Origin Embedder Policy

The pretix Widget is not compatible with `Cross-Origin-Embedder-Policy: require-corp`. 
If you include the `crossorigin` attributes on the `<script>` and `<link>` tag, then the widget can display a calendar or product list. 
But it will not be able to open the checkout process in an iframe. 
If you also set `Cross-Origin-Opener-Policy: same-origin`, then the widget can auto-detect that it is running in an isolated environment and will instead open the checkout process in a new tab.

## Versioning

Whenever possible, we make changes or improvements to the widget in a way that does not interfere with any of the configuration options listed on this page and does not cause compatibility issues with custom styling of your page.
Occasionally, we do however need to make changes that change the structure of the widget and might cause incompatibility.
In this case, we release a new version of the widget, noted by an incremented version number in both the script and stylesheet location.

New versions of the widget are announced with the monthly pretix release notes, also available through [our newsletter](https://pretix.eu/about/en/blog/).
You can then switch to the new version at a time of your choice with the chance to test if any changes to your custom styling is necessary.

When announcing a new version, we also announce a date of deprecation for the old version.
After this date, we will automatically replace the old version with the new one.
In other words, if you do not upgrade to the new version intentionally, you will automatically be upgraded after the deprecation date – with the possibility of some issues with custom styling.

## Changelog

### Version 2

- Various changes to the HTML structure of the widget have been made to improve the accessibility of the widget.
The most significant changes have been made to the calendar view, which now resembles the calendar view of the standalone ticket shop more closely.
The updated default stylesheet comes with stronger color contrasts, clear highlighting of focused elements and similar accessibility features.

- The attribute `single-item-select` has been removed and a button-style rendering is now always used.

**Availability**:
Version 2 is available starting with pretix 2025.5.0 (released late May, 2025).

**Deprecation schedule**:
Starting with pretix 2025.6.0 (released late June, 2025), all users of version 1 will be automatically upgraded to version 2.
This time frame is kept intentionally short to allow all users easy compliance with the [European Accessibility Act](https://en.wikipedia.org/wiki/European_Accessibility_Act).

## Troubleshooting 

### The code copied from this page does not work 

The examples provided in this article all use the base URL `pretix.eu`, the organizer `demo`, and the event `democon`. 
Your own event will use different organizer and event slugs. 
If you want to apply these examples to your own event and website, you need to replace these strings with the ones matching your event. 
The easiest way to ensure that you have the right code is using the code generator. 
Navigate to :navpath:Your Event → Settings → Widget:, click the :btn:Generate widget code: button, and copy the code snippets from there. 