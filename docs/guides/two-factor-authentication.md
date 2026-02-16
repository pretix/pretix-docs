# Two-factor authentication 

By default, your pretix account is secured with a single factor: your password. 
You can add a second factor to improve security. 
This is called "two-factor authentication" or **2FA**. 

The second security factor can be a WebAuthn-compatible hardware token or an authenticator application. 
This article explains the advantages of 2FA and how to set it up for your pretix user account. 

## Background information 

Depending on your usage of pretix and permission settings, your user account can grant access to a lot of sensitive information. 
This sensitive information can include, for example, company secrets, payment history, and your customers' contact data. 

A strong password offers a good baseline level of security. 
But potential malicious actors can breach passwords through malware, social engineering, and other methods. 

A second factor for authentication makes such an attack significantly more difficult. 
An attacker would have to gain access to both your 2FA device and your account credentials. 
Detecting a breach of one security factor can give you enough time to change it before the attacker can also breach the other factor. 

We recommend setting up 2FA for all user accounts at your organization. 
If you want to require your coworkers to use 2FA for their pretix accounts, refer to the article on [Teams](teams.md#requiring-two-factor-authentication-2fa). 
Once everyone on your team has done so, a malicious attack is very unlikely to succeed. 

## Prerequisites

Depending on the authentication method you intend to use, you need to have: 

 - a WebAuthn-compatible hardware token such as a Yubikey **or** 
 - an authenticator app capable of generating time-based one-time passwords (TOTP), such as Microsoft Authenticator, Google Authenticator, or Bitwarden. 

## How to

Log in to your pretix user account. 
Click the :btn-icon:fa3-user:[Your name]: button in the top right corner. 
This takes you to your user account settings. 

!["Page titled 'Account settings', displaying settings for 'Full name', 'Language', 'Default timezone', 'Notifications', 'Email', 'Password', 'Two-factor authentication', 'Authorized applications', and 'Account history'."](../assets/screens/account/account-settings.png "Account settings")

Before you set up 2FA, you should store your **emergency tokens** outside of pretix. 
You can use these codes in place of your 2FA device in case you lose access to it. 
Copy the codes and print them or write them down on paper. 
Store that paper in a safe place such as a locked drawer. 

Alternatively, you can store the emergency tokens digitally in an encrypted file or in a password manager. 
**Do not** store them in the same password manager or database that also contains your account password. 

!!! Note 
    Ensure that you have stored your emergency tokens outside of pretix and that you know where to find them. 
    You need these tokens in case you lose access to your 2FA device. 

Take a look at the "Two-factor authentication" setting. 
If 2FA is disabled, then there is a gray "Disabled" tag next to it. 
In order to enable 2FA, click the :btn:Enable: button. 

!["Page titled 'Two-factor authentication', displaying the 'Two factor status' as 'currently disabled', a button for adding a new registered device, and emergency tokens."](../assets/screens/account/two-factor-authentication.png "Two-factor authentication")

On the next page, click the :btn-icon:fa3-plus:Add a new device: button. 
Enter a name. 
The next steps are different depending on whether you want to use [a TOTP app](#using-a-totp-app) or a [hardware token](#using-a-hardware-token). 

!!! Note 
    Once you have set up 2FA, losing access to the device for 2FA means also losing access to your pretix user account. 
    In order to prevent such a situation, you can add multiple devices. 

    However, every additional method for logging in to your account offers potential attackers an additional point of entry. 
    In order to maximize security, only add a single device for 2FA. 

The advantage of a TOTP app is that you probably already have a device on hand which you can use for TOTP. 
This can be your work phone, your personal phone, another mobile device, or a separate computer. 
If this is the case, then you can use the device you already have on hand for 2FA. 

If you use separate applications for password storage and TOTP generation, then the TOTP method offers good security. 
However, like all software run on a device connected to the internet, a TOTP app is vulnerable to malware. 

A hardware token is much cheaper than a smartphone. 
If you need to buy a new device for 2FA, then this can be an advantage. 
Another advantage is that hardware tokens are less susceptible to software attacks. 

You must remove your hardware token from the computer and keep it on your person whenever you are not actively using it. 
One downside of the hardware token is that it is typically smaller than a phone and only used for authentication purposes. 
Thus, it can potentially be easier to lose. 

### Using a TOTP app 

Under "Device type", select `Smartphone with the Authenticator application`. 
Then, click the :btn:Continue: button. 

!["Page titled 'Add a two-factor authentication device', instructing you to download an authenticator app, scan a QR code, alternatively enter a code in the app, and then enter the code from the app in the pretix backend."](../assets/screens/account/add-device.png "Add a two-factor authentication device—App")

Open your TOTP app. 
Create a new entry for the TOTP secret. 
Scan the QR code that the pretix backend is displaying. 
Alternatively, click :btn:Can't scan the barcode?: and enter the code displayed under `3`. 

!!! Note 
    **Do not** store your password and your TOTP secret in the same password manager. 
    If it is possible to access both factors through the same primary password, then the second factor only offers very little increased security compared to single-factor authentication. 
    
    For instance, **do not** add the TOTP secret to the same password manager entry as your pretix user account data. 
    Use separate apps for TOTP generation and password storage, or at least separate databases. 

Save the entry in your TOTP app. 
It should now display a six-digit code that changes every 30 seconds. 
This code is the time-based one-time password. 
Enter it in the pretix backend in the field labeled "Enter the displayed code here". 
Then, click the :btn:Continue: button. 

This takes you back to the page titled "Two-factor authentication". 
The page will now state that 2FA is enabled and under "Registered devices", it will list the device running the TOTP app. 

From now on, you will need both your password and the TOTP from your app to log in to your pretix user account. 

### Using a hardware token 

Connect the hardware token to your computer. 
Under "Device type", select `WebAuthn-compatible hardware token (e.g. Yubikey)`. 
Then, click the :btn:Continue: button. 

!["Page titled 'Add a two-factor authentication device', instructing you to connect a WebAuthn device."](../assets/screens/account/add-device-webauthn.png "Add a two-factor authentication device—Hardware")

A new page will open and your browser will prompt you to activate your hardware token. 
Activate it. 
For instance, if you are using a Yubikey, touch the blinking capacitive button. 

This takes you back to the page titled "Two-factor authentication". 
The page will now state that 2FA is enabled and under "Registered devices", it will list the hardware token. 

From now on, you will need both your password and the hardware token to log in to your pretix user account. 

## Troubleshooting 

### You have lost access to your 2FA device

If you have lost access to your 2FA device because it is broken, stolen, or lost, then you should take the following steps: 

 - use one of your emergency tokens to log in 
 - remove the 2FA device from your user account 
 - acquire a replacement for the lost 2FA device 
 - add that device to your account 

In order to do so, open the [login page](https://pretix.eu/control/login). 
Enter your email address and password. 
When the page prompts you to touch your hardware key or enter the TOTP, enter one of the emergency tokens instead. 
Then, click the :btn:Continue: button. 

You can only use each emergency token once. 
Delete it from the list or cross it out after you have used it. 

Click the :btn-icon:fa3-user:[Your name]: button in the top right corner. 
This takes you to your user account settings. 
Click :btn:Change two-factor settings:. 
Seek out the lost device in the list and click the :btn:Remove: button next to it. 
If this is the only connected 2FA device, then this action will disable 2FA for your account. 

Acquire a replacement for the lost 2FA device. 
Add that device to your account as described under [How to](#how-to). 

### You have lost access to your 2FA device and to the emergency tokens 

If you have lost access to your 2FA device and to the emergency tokens, you should contact our support via [email](mailto:support@pretix.eu) or [phone](tel:+4962213217750). 

## See also 

If you want to require your coworkers to use 2FA for their pretix accounts, refer to the article on [Teams](teams.md#requiring-two-factor-authentication-2fa). 