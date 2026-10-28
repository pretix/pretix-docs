---
title: Konfigurationsdatei
---
# Konfigurationsdatei

pretixKIOSK liest seine Konfiguration aus einer Konfigurationsdatei aus.
Es sucht nach dieser Datei im aktuellen Arbeitsverzeichnis des Ausführungsprozesses unter dem Namen `config.properties`.

pretixKIOSK geht davon aus, dass diese Datei im Format `.properties` ist, wie in der [Java-Dokumentation](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Properties.html#load(java.io.Reader)) spezifiziert.
pretixKIOSK startet nicht, wenn die Konfigurationsdatei ungültig ist.

## Konfigurationsparameter

### Hardware-Abstraktion

| Parameter                                 | Erforderlich | Beschreibung                                                                                                                                                                |
|-------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `hardwareType`                            | Erforderlich | Art der Hardware-Abstraktionsebene. Aktuell unterstützt: `fischer` für Verkaufsautomaten von Fischer Electronics, `mock` zur Verwendung bei Tests und `plain` für einfache bargeldlose Automaten |
| `hardwareIp`                              | Erforderlich | IP-Adresse der Hardware-Abstraktionsebene (meist `127.0.0.1` für `fischer`, anderenfalls ignoriert)                                                                         |
| `hardwarePort`                            | Erforderlich | Port der Hardware-Abstraktionsebene (meist `1001` für `fischer`, anderenfalls ignoriert)                                                                                    |
| `hardwareIsSimulated`                     | Optional | Auf `true` setzen, wenn die Hardwareebene kein echter Verkaufsautomat ist                                                                                                              |
| `hardwareTraceLogging`                    | Optional | Auf `true` setzen, wenn Hardwareereignisse umfangreich protokolliert werden sollen (zum Debugging)                                                                                     |
| `hardwareStockTimeout`                    | Erforderlich | Die Anzahl Sekunden, die die Hardwareebene zum Schreiben von Änderungen im Warenbestand benötigen darf                                                                      |
| `hopper1Threshold` ... `hopper8Threshold` | Erforderlich | Anzahl Münzen, ab der der Füllstand in den Münzbehältern 1 bis 8 als niedrig gilt                                                                                           |

### Zahlung

| Parameter                      | Erforderlich| Beschreibung                                                                                                                      |
|--------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------|
| `cashPaymentEnabled`           | Optional | Auf `false` setzen, um Barzahlungen auszuschließen (standardmäßig `true` )                                                           |
| `cardPaymentEnabled`           | Optional | Auf `false` setzen, um Kartenzahlungen auszuschließen (standardmäßig `true` )                                                        |
| `acceptedCoins`                | Erforderlich | Mit Kommas getrennte Liste von Werten (in Cent) der akzeptierten Münzen (Beispiel "20,50,100,200"). Leer lassen, wenn keine Münzen akzeptiert werden |
| `zvtHost`                      | Erforderlich | IP-Adresse des Bezahlterminals                                                                                                   |
| `zvtPort`                      | Erforderlich | ZVT-Port des Bezahlterminals                                                                                                     |
| `zvtPassword`                  | Erforderlich | ZVT-Passwort des Bezahlterminals (immer 6 Ziffern, oft "000000")                                                                 |
| `zvtTraceLogging`              | Optional | Auf `true` setzen, wenn ZVT-Ereignisse umfangreich protokolliert werden sollen (zum Debugging)                                              |
| `zvtAbortEnabled`              | Optional | Auf `true` setzen, wenn das Bezahlterminal eine externe Unterbrechung des Zahlungsvorgangs zulässt (muss für jeden Terminaltyp getestet werden) |
| `zvtPrinterCharsPerLine`       | Erforderlich | Die Anzahl Zeichen, die in eine Zeile des Druckers im Bezahlterminal passen. Auf 0 setzen, falls dieser Wert unbekannt oder kein Drucker vorhanden ist |
| `zvtEcrReceiptPrinting`        | Optional | Auf `true` setzen, falls die Kartenzahlungsbelege vom Ticketautomaten gedruckt werden sollen, nicht vom Terminal                     |
| `zvtEcrReceiptPrintingTimeout` | Erforderlich | Die Anzahl Sekunden, die der Automat wartet, bis das Bezahlterminal einen Beleg sendet                                                 |
| `zvtMerchantReceiptString`     | Erforderlich | Auf eine Zeichenfolge in allen Händlerbelegen setzen, damit diese nicht gedruckt werden                                          |

### Drucken

| Parameter                         | Erforderlich| Beschreibung                                                                                                                  |
|-----------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------|
| `ticketPrinterName`               | Erforderlich | Name des Druckers, der die Tickets drucken soll                                                                              |
| `ticketPrinterType`               | Erforderlich | Typ des Druckers, der die Tickets drucken soll (`custom` für CUSTOM-Drucker unter Windows, ansonsten `default`)   |
| `ticketPrinterHasLowPaperSensor`  | Optional | Auf `true` setzen, wenn der Ticketdrucker die Sensormeldung berücksichtigen soll, dass das Papier zu Ende geht (derzeit nur für `custom`-Drucker unterstützt) |
| `ticketPrintUseAwtMode`           | Optional | Zum internen Gebrauch, auf `true` setzen, wenn der Drucker sonst nicht funktioniert                                              |
| `ticketPrintFallBackToReceipt`    | Optional | Gibt an, ob Tickets als Belege vom Bondrucker gedruckt werden sollen, wenn kein Ticketdrucker verfügbar ist                      |
| `receiptPrinterName`              | Erforderlich | Name des Druckers, der die Belege drucken soll                                                                               |
| `receiptPrinterType`              | Erforderlich | Typ des Druckers, der die Belege drucken soll (`custom` für CUSTOM-Drucker unter Windows, ansonsten `default`)   |
| `receiptPrinterHasLowPaperSensor` | Optional | Auf `true` setzen, wenn der Bondrucker die Sensormeldung berücksichtigen soll, dass das Papier zu Ende geht (derzeit nur für `custom`-Drucker unterstützt) |
| `receiptPrintUseAwtMode`          | Optional | Zum internen Gebrauch, auf `true` setzen, wenn der Drucker sonst nicht funktioniert                                              |
| `receiptFontSize`                 | Erforderlich | Die Schriftgröße für Normaltext auf Belegen                                                                                  |
| `receiptPageWidth`                | Erforderlich | Breite der Belege in Millimeter                                                                                              |
| `receiptMarginLeft`               | Erforderlich | Breite des linken Rands vor Beginn des Belegtextes in Millimeter                                                              |
| `receiptMarginTop`                | Erforderlich | Breite des oberen Rands vor Beginn des Belegtextes in Millimeter                                                              |
| `receiptMarginBottom`             | Erforderlich | Breite des unteren Rands nach dem Belegtext in Millimeter                                                                      |
| `printTraceLogging`               | Optional | Auf `true` setzen, wenn Druck-Ereignisse umfangreich protokolliert werden sollen (zum Debugging)                                 |

### Schließzeiten

| Parameter                 | Erforderlich| Beschreibung                                                             |
|---------------------------|--------------|-------------------------------------------------------------------------|
| `scheduledClosingEnabled` | Optional | Auf `true` setzen, wenn der Geschäftsbetrieb automatisch einmal täglich beendet werden soll |
| `scheduledClosingHour`    | Erforderlich | Gibt die Stunde an, zu der der geplante Kassenabschluss durchgeführt werden soll |
| `scheduledClosingMinute`  | Erforderlich | Gibt die Minute an, zu der der geplante Kassenabschluss durchgeführt werden soll |

## Beispieldatei

```
hardwareType=plain
hardwareIp=127.0.0.1
hardwarePort=1001
hardwareIsSimulated=False
hardwareTraceLogging=False
hardwareStockTimeout=10

hopper1Threshold=4
hopper1Threshold=4
hopper1Threshold=4
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
