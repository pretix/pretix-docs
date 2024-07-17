# pretixSCAN—Android app 

pretixSCAN is a powerful Android application that helps you handle the check-in at your events. 
The primary function of pretixSCAN is to validate tickets, but it also offers many other features, such as: 

 - searching for participants manually if they do not have their ticket on hand 

This article will tell you how to get install pretixSCAN for **Android** and how to make use of its features. 

pretixSCAN is also available for Windows, Linux, and iOS. 
Those versions of the software will be documented on separate pages. 
This article is about the Android version of pretixSCAN, which is also the most feature-rich version of the application. 

pretixSCAN is not to be confused with our other apps: pretixPRINT, which takes care of the printing of tickets, badges and receipts for you; pretixPOS, which handles product sales; or pretixLEAD, which collects and manages contact data of attendees at your event. 

## Prerequisites

pretixSCAN is meant for use with an event hosted using pretix. 
This article assumes that you are hosting an event with pretix. 

You need to have access to a device running Android version 5 or newer; for full functionality, Android version 6 or newer. 
The device also needs to have a camera or integrated code scanner. 
See our [support policy](https://docs.pretix.eu/en/latest/user/android-version-support.html#pretixscan) for more information. 

You also need access to a separate device from which you can access the pretix backend while you are setting up your device running pretixSCAN. 

## How To

### Installation and setup 

pretixSCAN comes preinstalled on the scanner smartphones that are available for rent and for sale on our website. 
You can skip this step if you are using devices that you rented or bought from us. 
For more information on our hardware offers, visit [our website](https://pretix.eu/about/en/hardware/scan). 

You can install pretixSCAN on your Android device [through the Google Play Store](https://play.google.com/store/apps/details?id=eu.pretix.pretixscan.droid) like any other app. 
When you launch pretixSCAN for the first time, confirm that you understand the privacy and security implications of storing attendee data on your device. 
You have to grant pretixSCAN access to the device's camera in order to use the core functionality of validating tickets. 
pretixSCAN will start accessing the scanner or camera instantly once you have granted permission. 
It will also display a text box telling you to create a new device in our organizer account in the pretix backend. 
The next section is going to tell you how to do that. 

### Connecting the device to the pretix backend 

Open the [pretix backend](https://pretix.eu/control/) and navigate to [Your organizer] :fontawesome-solid-arrow-right: ":btn:fontawesome-solid-mobile-screen: Devices". 
Give the device a unique and recognizable name such as "Entrance B phone 1". 
You can authorize the device for all events or limit its access to certain events only. 
Select "pretixSCAN" from the "Security profile" dropdown menu. 

You may add the device to a gate if you have previously created gates to group devices into. 
This can be helpful if you are hosting an event with more than one entrance (gate). 

Once you click :btn:Save:, you will be taken to a page displaying a QR code. 
Use pretixSCAN on your Android device to scan the QR code. 
If you have trouble scanning the QR code, there is an alternative solution: 
Tap the three button menu in the top right corner of the pretixSCAN app and then tap "Manual setup". 
You will be asked to enter a system URL and a token. 
If you are using pretix Hosted, the system URL will always be https://pretix.eu. 
If you are self-hosting pretix (pretix Community or pretix Enterprise), you will have to enter the address of your server. 
Enter the token displayed in the backend in the field in the pretixSCAN app. 

![pretixSCAN app with a popup titled 'Select Event', listing a single entry called 'Tutorial Conference'. There are buttons labeled 'SHOW CALENDAR' and 'OK'.](../assets/screens/scan/select-event.png "pretixSCAN Select Event" ) 

Once you scanned the QR code or entered the token successfully, the app will ask you to select the event you want to scan tickets for. 
Check the event in the list or in the calendar and tap :btn:OK:. 
Then, select a check-in list and tap :btn:OK: again. 
The app will now land you on the main screen and download event data from the server. 

### Scanning tickets 

pretixSCAN will scan any QR code or barcode it can detect via the device's camera or scanner. 
Simply point the device at the code you want to scan. 

## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

 - [pretixSCAN repository on GitHub](https://github.com/pretix/pretixscan-android)
 - [Kurzanleitung pretixSCAN on Youtube (German)](https://www.youtube.com/watch?v=csy017Dm6vA)

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 