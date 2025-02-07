# Ticket secrets 

Every individual product sold via pretix has a ticket secret. 
It is a series of characters that can be represented as a QR code. 
The ticket secret serves as a unique identifier. 
The QR code can be scanned with pretixSCAN to validate a ticket at your event's check-in. 
By default, the ticket secret is generated randomly. 

This article tells you about pretix' default method for ticket secret generation in detail. 
It also tells you how to change that behavior to a signature-based secret generation scheme if necessary. 

## Prerequisites

Ticket secrets are handled on the event level, so you have to create an event first. 

## Default behavior: random ticket secret generation

Every individual product sold via pretix has a ticket secret. 
This ticket secret is a code that can be represented as a sequence of characters or a QR code. 
By default, this code is randomly generated and consists of 32 lower case letters and numbers. 
To avoid confusion, the characters `o`, `O`, `1`, `i`, and `l` are **not** used. 

If you want to change the length of the ticket secret code, navigate to :navpath:Your event: → :fa3-wrench: Settings → Tickets:.
Under "Length of ticket codes", choose a number between 12 and 64. 

The approach with random ticket secrets has several advantages: 

 - Codes are short and easy to scan or type. 
 - Guessing or forging a valid ticket code is impossible. 
 - The code remains the same even if the product itself changes due to rebooking. 

Random ticket secrets can only be validated by checking them against the database. 
The device running pretixSCAN needs access to a database containing all ticket secrets that have been generated for the current event. 

The default behavior of pretixSCAN is that it downloads the entire database onto the device itself. 
This makes it possible to fall back to offline mode when the connection between the scanning device and the server is unreliable or unavailable. 

There are a few situation in which this can lead to problems: 

 - If the number of valid tickets for a single event exceeds 25,000, downloading the entire database onto the scanning device may be too resource-heavy and time-consuming. 
 - If losing sensible data contained in the ticket database along with one of the scanning devices is unacceptable. 
 - If the scanners operate in offline mode regularly and tickets have to be valid instantly after purchase (and a delay of a few minutes is unacceptable)

If one or more conditions apply to the event you are organizing, you may want to switch to the pretix signature scheme for ticket secret generation instead. 
The next section tells you how it works. 
For all other cases, we recommend using the default option with randomly generated ticket secrets. 

## Alternative method: ticket secret generation via signature scheme

pretix offers an alternative to random ticket secrets: a signature-based code generation scheme called "pretix signature scheme 1". 
Secrets generated with this scheme encode the product, the product variation, and, in case of an event series, the date. 

The secret is then signed with an Ed25519 signature to prevent forging. 
This means that neither a working connection to the server nor a database stored on the scanning device is necessary for ticket validation. 
pretixSCAN needs only the ticket secret itself to validate the product. 

The signature-based approach has two main downsides: 
First, scanning in offline mode is much more limited. 
The scanning device does not have information about attendee names, seating, previous uses of the ticket, etc. 
Thus, printing badges is also not possible. 

Second, if one of the main data points (product, variation, or date) is changed, then the ticket secret has to be moved to a revocation list and a new ticket secret has to be generated. 
If the ticket is canceled, it also has to be moved to the revocation list. 

The revocation list needs to be downloaded by all scanning devices, though it is usually much smaller than the full ticket database. 
The original ticket becomes unusable and the attendee has to download the updated version of the ticket. 

If you want to switch to the signature scheme, navigate to :navpath:Your event → :fa3-wrench: Settings → Tickets:.
Under "Ticket code generator", select "pretix signature scheme 1". 

## Comparison of scanning behavior 

| Scan mode                                    | Online                | Offline                    |                                   |                          |                                                                           |
|----------------------------------------------|-----------------------|----------------------------|                                   |                          |                                                                           |
| **Synchronization setting**                      | **any**                   | **Synchronize orders**         |                                   | **Don't synchronize orders** |                                                                           |
| **Ticket secrets**                               | **any**                   | **Random**                     | **Signed**                            | **Random**                   | **Signed**                                                                    |
| Scenario supported on platforms              | Android, Desktop, iOS | Android, Desktop, iOS      | Android, Desktop                  | Android, Desktop, iOS    | Android, Desktop, iOS                                                     |
| Synchronization speed for large data sets    |                       | slow                       | slow                              | fast                     | fast                                                                      |
| Tickets can be scanned                       | yes                   | yes                        | yes                               | no                       | yes                                                                       |
| Ticket is valid after sale                   | immediately           | next sync (~5 minutes)     | immediately                       | never                    | immediately                                                               |
| Same ticket can be scanned multiple times    | no                    | yes, before data is synced | yes, before data is synced        | n/a                      | yes, always                                                               |
| Custom check-in rules                        | yes                   | yes                        | yes (limited directly after sale) | n/a                      | yes, but only based on product, variation and date, not on previous scans |
| Name and seat visible on scanner             | yes                   | yes                        | yes (except directly after sale)  | n/a                      | no                                                                        |
| Order-specific check-in attention flag       | yes                   | yes                        | yes (except directly after sale)  | n/a                      | no                                                                        |
| Ticket search by order code or name          | yes                   | yes                        | yes (except directly after sale)  | no                       | no                                                                        |
| Check-in statistics on scanner               | yes                   | yes                        | mostly accurate                   | no                       | no                                                                        |
| Support for add-on check-in with main ticket | yes                   | yes                        | yes (except directly after sale)  | no                       | no                                                                        |

## Additional information 

pretix does not support generating linear barcodes, also known as 1D barcodes. 
There are several reasons for this: 

 1. A linear barcode with 32 characters is too long to be scanned from a phone screen or from a small printed ticket. 
 2. A linear barcode does not have the redundancy of a QR code, so scanning it from damaged or dirty paper may be impossible. 
 3. Laser barcode scanners do not work on most phone screens, so a more advanced barcode scanner is necessary anyway. 