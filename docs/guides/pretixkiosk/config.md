# Configuration file

pretixKIOSK reads its configuration from a configuration file.
It tries to find this file with the name `config.properties` in the current working directory of the execution process.

pretixKIOSK expects the file to be in the `.properties` format as specified in the [Java documentation](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Properties.html#load(java.io.Reader)).
pretixKIOSK will refuse to start if the config file is invalid.

## Configuration parameters

### Hardware abstraction

| Parameter                                 | Required | Description                                                                                                                                                                     |
|-------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `hardwareType`                            | Required | Type of hardware abstraction layer. Currently supported: `fischer` for Fischer Electronics vending machines, `mock` for use in testing and `plain` for simple cashless machines |
| `hardwareIp`                              | Required | IP address of hardware abstraction layer (usually `127.0.0.1` for `fischer`, ignored otherwise)                                                                                 |
| `hardwarePort`                            | Required | Port of the hardware abstraction layer (usually `1001` for fischer, ignored otherwise)                                                                                          |
| `hardwareIsSimulated`                     | Optional | Set to `true` if the hardware layer is not a real vending machine                                                                                                               |
| `hardwareTraceLogging`                    | Optional | Set to `true` to enable extended logging of hardware events (for debugging)                                                                                                     |
| `hardwareStockTimeout`                    | Required | Set to the number of seconds the hardware layer may take to commit stock changes                                                                                                |
| `hopper1Threshold` ... `hopper8Threshold` | Required | Number of coins to be considered "low" in the coin hoppers 1 to 8                                                                                                               |

### Payment

| Parameter                      | Required | Description                                                                                                                          |
|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| `cashPaymentEnabled`           | Optional | Set to `false` to disable cash payment (`true` by default)                                                                           |
| `cardPaymentEnabled`           | Optional | Set to `false` to disable card payment (`true` by default)                                                                           |
| `acceptedCoins`                | Required | Comma-separated list of coin values (in cents) of accepted coins (example "20,50,100,200). Leave blank to indicate no coins accepted |
| `zvtHost`                      | Required | IP address of the payment terminal                                                                                                   |
| `zvtPort`                      | Required | ZVT port of the payment terminal                                                                                                     |
| `zvtPassword`                  | Required | ZVT password of the payment terminal (always 6 digits, often "000000")                                                               |
| `zvtTraceLogging`              | Optional | Set to `true` to enable extended logging of ZVT events (for debugging)                                                               |
| `zvtAbortEnabled`              | Optional | Set to `true` if the payment terminal allows external interruption of payments (needs to be tested per terminal type)                |
| `zvtPrinterCharsPerLine`       | Required | Set to the number of characters that fit in one line of the payment terminal's printer. Set to 0 if unknown or no printer            |
| `zvtEcrReceiptPrinting`        | Optional | Set to `true` if card payment receipts should be printed by the kiosk instead of the terminal                                        |
| `zvtEcrReceiptPrintingTimeout` | Required | Set to the number of seconds to wait for the card terminal to send a receipt                                                          |
| `zvtMerchantReceiptString`     | Required | Set to a string contained in all merchant receipts to avoid printing them                                                            |

### Printing

| Parameter                         | Required | Description                                                                                                                      |
|-----------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| `ticketPrinterName`               | Required | Name of the printer that should be used for printing tickets                                                                     |
| `ticketPrinterType`               | Required | Type of the printer that should be used for printing tickets (`custom` for CUSTOM printers on Windows, `default` otherwise)      |
| `ticketPrinterHasLowPaperSensor`  | Optional | Set to `true` if the ticket printer has a low sensor value that should be used (currently only supported for `custom` printers)  |
| `ticketPrintUseAwtMode`           | Optional | For internal use, set to `true` if printer does not work otherwise.                                                              |
| `ticketPrintFallBackToReceipt`    | Optional | Whether tickets should be printed as receipts on the receipt printer if the ticket printer is not available                      |
| `receiptPrinterName`              | Required | Name of the printer that should be used for printing receipts                                                                    |
| `receiptPrinterType`              | Required | Type of the printer that should be used for printing receipts (`custom` for CUSTOM printers on Windows, `default` otherwise)     |
| `receiptPrinterHasLowPaperSensor` | Optional | Set to `true` if the receipt printer has a low sensor value that should be used (currently only supported for `custom` printers) |
| `receiptPrintUseAwtMode`          | Optional | For internal use, set to `true` if printer does not work otherwise.                                                              |
| `receiptFontSize`                 | Required | Font size for regular text on receipts                                                                                           |
| `receiptPageWidth`                | Required | Width of receipts in millimeters                                                                                                 |
| `receiptMarginLeft`               | Required | Left margin before receipt content in millimeters                                                                                 |
| `receiptMarginTop`                | Required | Top margin before receipt content in millimeters                                                                                  |
| `receiptMarginBottom`             | Required | Bottom margin after receipt content in millimeters                                                                                 |
| `printTraceLogging`               | Optional | Set to `true` to enable extended logging of print events (for debugging)                                                         |

### Closings

| Parameter                 | Required | Description                                                                 |
|---------------------------|----------|-----------------------------------------------------------------------------|
| `scheduledClosingEnabled` | Optional | Set to `true` if a cash session should be automatically closed once per day |
| `scheduledClosingHour`    | Required | Set to the hour of the day the scheduled closing should be performed        |
| `scheduledClosingMinute`  | Required | Set to the minute of the hour the scheduled closing should be performed      |

## Example file

```
hardwareType=plain
hardwareIp=127.0.0.1
hardwarePort=1001
hardwareIsSimulated=False
hardwareTraceLogging=False
hardwareStockTimeout=10

hopper1Threshold=4
hopper2Threshold=4
hopper3Threshold=4
hopper4Threshold=4
hopper5Threshold=4
hopper6Threshold=4
hopper7Threshold=4
hopper8Threshold=4

paymentTerminalType=zvt
zvtHost=192.168.1.123
zvtPassword=000000
zvtPort=22000
zvtTraceLogging=True
zvtAbortEnabled=True
zvtPrinterCharsPerLine=35
zvtEcrReceiptPrinting=True
zvtEcrReceiptPrintingTimeout=10
zvtMerchantReceiptString=H-Ä-N-D-L-E-R-B-E-L-E-G

cashPaymentEnabled=False
cardPaymentEnabled=True
acceptedCoins=20,50,100,200

printTraceLogging=False

ticketPrinterName=RECEIPT
ticketPrinterType=default
ticketPrinterHasLowPaperSensor=False
ticketPrintUseAwtMode=False
ticketPrintFallBackToReceipt=True

receiptPrinterName=RECEIPT
receiptPrinterType=default
receiptPrinterHasLowPaperSensor=False
receiptPrintUseAwtMode=False
receiptFontSize=10.0
receiptPageWidth=80.0
receiptMarginLeft=2.0
receiptMarginTop=5.0
receiptMarginBottom=20.0

scheduledClosingEnabled=False
scheduledClosingHour=0
scheduledClosingMinute=0
```
