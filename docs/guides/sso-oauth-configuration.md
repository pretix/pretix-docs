# Configuring OAuth SSO with GitHub, Google, and Wikimedia

SSO (Single Sign-On) allows your customers to log in to your pretix shop using their existing accounts from popular platforms. This has several benefits:

- Simplified login experience without creating new passwords
- Higher conversion rates at checkout as users skip account creation
- Reduced support requests for forgotten passwords
- Access to verified email addresses from trusted providers

This guide walks you through setting up GitHub, Google, and Wikimedia login options for your pretix shop.

## Before you start

You'll need:

- A pretix shop with customer accounts enabled
- Admin access to your pretix organizer settings
- Access to create OAuth applications in GitHub, Google, or Wikimedia

## Setting up customer accounts

First, let's make sure customer accounts are properly enabled:

1. Go to **Your organizer → Settings → General**
2. Click the **Customer accounts** tab
3. Check "Allow customers to create accounts"
4. Decide about the "Allow customers to log in with email address and password" option:
   - Keep it checked if you want to offer both password and SSO login (recommended to start)
   - Uncheck it if you want to force SSO-only login

## Setting up GitHub login

GitHub is great for developer-focused events, hackathons, or tech conferences.

### Create your GitHub OAuth App

1. Sign in to GitHub and navigate to [Settings → Developer settings → OAuth Apps](https://github.com/settings/developers)
2. Click "New OAuth App"
3. Fill in the details:
   - **Application name**: Something your users will recognize, like "MyConference Tickets"
   - **Homepage URL**: Your main website (e.g., `https://myconference.com`)
   - **Application description**: A brief explanation, like "Ticket purchases for MyConference"
   - **Authorization callback URL**: This is critical! Use:
     ```
     https://your-pretix-domain.com/your-organizer/oauth2/v1/callback
     ```
     Replace `your-pretix-domain.com` with your actual domain and `your-organizer` with your pretix organizer slug.

4. Click "Register application"
5. On the next screen, note your **Client ID**
6. Generate a new client secret and copy it immediately (you won't be able to see it again)

### Configure GitHub in pretix

1. In your pretix admin, go to **Your organizer → Customer accounts → SSO providers**
2. Click "Create a new SSO provider"
3. Complete the form:
   - **Provider name**: `GitHub` (internal reference name)
   - **Login button label**: `Sign in with GitHub` (visible to customers)
   - **Single-sign-on method**: `OpenID Connect`
   - **Issuer URL**: `https://github.com`
   - **Client ID**: Paste from GitHub (looks like `a1b2c3d4e5f6g7h8i9j0`)
   - **Client secret**: Paste from GitHub (looks like `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9`)
   - **Scopes**: `openid user:email` (to get verified email addresses)
   - Leave other fields with default values
   - **Email address claim**: `email`
   - **Identity claim**: `sub`
   - First/last name claims can be left empty as GitHub doesn't consistently provide these

4. Save your changes

## Setting up Google login

Google login is perfect for general audience events as most people already have a Google account.

### Create your Google OAuth credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project or select an existing one
3. Navigate to **APIs & Services → Credentials**
4. Click "Create Credentials" then "OAuth client ID"
5. If you haven't configured the consent screen yet:
   - Select "External" for most cases
   - Enter basic app information - your organization name and support email
   - For "Authorized domains" add your pretix domain
   - Add your email for developer contact information
   - You only need basic scopes for OAuth login, so select only what's necessary

6. Back on the OAuth client creation screen:
   - Application type: "Web application"
   - Name: Your ticket shop name
   - Authorized JavaScript origins: `https://your-pretix-domain.com`
   - Authorized redirect URIs: `https://your-pretix-domain.com/your-organizer/oauth2/v1/callback`

7. Click "Create" and note both the **Client ID** and **Client Secret**

### Configure Google in pretix

1. Go to **Your organizer → Customer accounts → SSO providers**
2. Click "Create a new SSO provider"
3. Fill in the details:
   - **Provider name**: `Google`
   - **Login button label**: `Continue with Google`
   - **Single-sign-on method**: `OpenID Connect`
   - **Issuer URL**: `https://accounts.google.com`
   - **Client ID**: Use the value from Google (looks like `123456789012-abc123def456ghi789jkl012mno345p.apps.googleusercontent.com`)
   - **Client secret**: Use the value from Google (looks like `GOCSPX-A1b2C3d4E5f6G7h8I9j0K1l2M3`)
   - **Scopes**: `openid email profile`
   - **Email address claim**: `email`
   - **Identity claim**: `sub`
   - **First name claim**: `given_name`
   - **Last name claim**: `family_name`

4. Save the configuration

## Setting up Wikimedia login

Wikimedia login is useful for events related to Wikipedia, open knowledge communities, and educational institutions.

### Register your Wikimedia OAuth consumer

1. Go to [Meta-Wiki's OAuth Consumer Registration](https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose)
2. Complete the registration form:
   - **Application name**: Your event or organization name
   - **Application description**: Brief explanation of your use case
   - **OAuth callback URL**: `https://your-pretix-domain.com/your-organizer/oauth2/v1/callback`
   - **Contact email**: Your support email
   - **Public RSA key**: Leave blank (not needed)
   - **Consumer version**: `1.0` (OAuth 1.0a)
   - **Applicable project**: Usually "all" is appropriate
   - **Permissions**: Basic rights and High-volume editing (minimum required)
   - **Grant types**: `authorization_code`

3. Accept the developer agreement and submit
4. After approval (which may take some time), note your **Consumer Key** and **Consumer Secret**

### Configure Wikimedia in pretix

1. In pretix, go to **Your organizer → Customer accounts → SSO providers**
2. Click "Create a new SSO provider"
3. Fill in the form:
   - **Provider name**: `Wikimedia`
   - **Login button label**: `Log in with Wikimedia`
   - **Single-sign-on method**: `OpenID Connect`
   - **Issuer URL**: `https://meta.wikimedia.org/w/rest.php/oauth2`
   - **Client ID**: Your Consumer Key (looks like `a12b34c56d78e90f1a2b3c4d5e6f7g8h`)
   - **Client secret**: Your Consumer Secret (looks like `a12b34c56d78e90f1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9`)
   - **Scopes**: `openid profile email`
   - **Email address claim**: `email`
   - **Identity claim**: `sub`
   - First and last name claims can be left empty

4. Save your settings

## Testing the login flow

Always test your SSO setup before going live:

1. Open your pretix shop in an incognito/private browser window
2. Go to any event and start the checkout process
3. When prompted to log in or create an account, you should see buttons for your configured providers
4. Click each button and verify you're correctly redirected to the login page
5. After logging in, you should be sent back to pretix with your account connected

## Troubleshooting common issues

If your setup doesn't work, check these common problems:

### The redirect doesn't work (OAuth error)

**Problem**: After login, you get an error about invalid redirect or client.

**Solution**: 
- Double-check that the callback URL in your OAuth provider settings **exactly** matches what pretix expects
- The URL should be: `https://your-pretix-domain.com/your-organizer/oauth2/v1/callback`
- Be careful about trailing slashes and typos

### Missing user information

**Problem**: Login works but name or email information isn't passed to pretix.

**Solution**:
- Verify you've requested the correct scopes:
  - GitHub: `openid user:email`
  - Google: `openid email profile`
  - Wikimedia: `openid profile email`
- Check the claim mappings in your SSO provider configuration

### Users can't log in with SSO

**Problem**: The login buttons don't appear or don't work.

**Solution**:
- Confirm your OAuth client is active/published (Google requires publishing the OAuth consent screen)
- Make sure your callback domain has HTTPS properly configured
- Check browser console for JavaScript errors
- Verify your pretix installation is publicly accessible

## Advanced tips

### Looking professional with branded buttons

Customers respond better to a polished, branded experience:

- Use clear, action-oriented button text like "Continue with Google" instead of just "Google"
- If you have multiple SSO options, list the most popular one first
- Consider custom button styling to match your event branding

### Security considerations

Implement these best practices for production use:

- Regularly audit your OAuth applications and rotate client secrets annually
- Only request the minimum necessary scopes
- Consider implementing a backup login method in case an SSO provider has an outage
- For high-security events, remember that SSO security is only as strong as the provider's security

### When to use SSO-only login

Disabling password login in favor of SSO-only works best when:

1. Your audience primarily uses one of your SSO providers already
2. You've set up multiple SSO options to accommodate different users
3. You want to enforce stronger authentication than password-based login

To switch to SSO-only mode:
1. Go to **Your organizer → Settings → General → Customer accounts**
2. Uncheck "Allow customers to log in with email address and password"

## Finding SSO Settings in pretix

If you're new to pretix and having trouble locating the SSO configuration pages, follow these steps:

### Accessing Customer Account Settings

1. Log in to your pretix admin panel with your organizer account
2. From the main dashboard, locate and click on your organizer name in the left sidebar
3. In the organizer menu, click on the settings icon (⚙️) or the "Settings" option
4. In the Settings page, locate and click on the "Customer accounts" tab
5. Ensure the "Allow customers to create accounts" checkbox is enabled
6. Save your changes if you made any modifications

### Accessing SSO Provider Configuration

1. Return to your organizer dashboard
2. Look for the "Customer accounts" menu item in the left sidebar (it has a user icon 👤)
   - This option only appears after you've enabled customer accounts in the settings
3. Click on "Customer accounts" to expand the submenu
4. Select "SSO providers" from the submenu
5. You'll now see the SSO providers management page where you can add, edit, or delete providers

If you don't see these options:
- Verify you have sufficient administrative permissions
- Make sure customer accounts are enabled
- Check that you're using a pretix version that supports SSO (4.0 or newer)

## Complete Client-Side Testing Guide

After setting up your SSO providers, it's crucial to thoroughly test the experience from your customers' perspective. Here's a comprehensive testing plan:

### Basic Login Flow Testing

1. **Open an incognito/private browser window**
   - This ensures you're starting with a clean session without existing cookies or login data

2. **Navigate to your pretix shop front-end**
   - Go to: `https://your-pretix-domain.com/your-organizer/`
   - Or go to any specific event page: `https://your-pretix-domain.com/your-organizer/your-event/`

3. **Start the checkout process**
   - Select an event if you're on the organizer page
   - Choose a ticket/product 
   - Click "Add to cart" and then proceed to checkout

4. **At the customer information step**
   - You should see login options at the top of the form
   - Look for the SSO buttons you configured (e.g., "Continue with Google")

5. **Click on one of the SSO provider buttons**
   - You should be redirected to the provider's login page
   - For GitHub: GitHub's login page should appear
   - For Google: Google's account selection and/or login page should appear
   - For Wikimedia: Wikimedia's login screen should appear

6. **Authenticate with the provider**
   - Enter your credentials for that service
   - Approve any permission requests

7. **Verify the redirect back to pretix**
   - After successful authentication, you should be automatically redirected back to pretix
   - You should now be logged in
   - The checkout form may be partially filled with information from your SSO provider

8. **Complete the purchase process**
   - Continue with the checkout to ensure everything works end-to-end

### Testing Edge Cases

Test these scenarios to ensure robust SSO implementation:

1. **New vs. Existing Customer**
   - Test with a social account that has never been used with your pretix shop
   - Test with a social account that has been used before
   - Test with a social account whose email matches an existing customer account

2. **Account Linking**
   - Create an account using email/password
   - Then try logging in with SSO using the same email address
   - Verify the accounts are correctly linked

3. **Multiple SSO Providers**
   - If you have multiple SSO providers configured, test logging in with each one
   - Try using different SSO providers with the same email address

4. **Session Persistence**
   - Log in via SSO
   - Close the browser (not just the tab)
   - Return to your shop and see if the session persists as expected

5. **Mobile Testing**
   - Test the SSO flow on mobile devices
   - Verify the redirect works properly in mobile browsers

### Verification Checklist

After completing a login, verify these important details:

- ✅ The user is properly authenticated
- ✅ The correct name appears in the account section (if available from the provider)
- ✅ The correct email is associated with the account
- ✅ Any previous orders are accessible if the account was linked
- ✅ The user can access their customer dashboard at `https://your-pretix-domain.com/your-organizer/customer/`

### Troubleshooting During Testing

If you encounter issues during testing:

1. **Check browser console for errors**
   - Open developer tools (F12 or right-click > Inspect)
   - Look for error messages in the Console tab

2. **Examine the URL when errors occur**
   - Often, OAuth errors will appear in the URL parameters
   - Look for parameters like `error=` or `error_description=`

3. **Verify redirection**
   - Use browser developer tools to monitor network requests
   - Check if redirects are happening as expected
   - Look for 4xx or 5xx responses

4. **Test in multiple browsers**
   - Some issues might be browser-specific
   - Try at least Chrome, Firefox, and Safari

5. **Verify HTTPS**
   - OAuth redirects typically require secure connections
   - Make sure your SSL certificate is valid

By thoroughly testing all these scenarios, you'll ensure a smooth experience for your customers when they use SSO to access your pretix shop. 
