# CSGO Translate

This program translates messages sent in the game Counter-Strike: Global Offensive by using Google Translates API. CSGO Translate will not get you banned since it does not modify the game files in any way, nor does it read or write to memory. To retrieve the gamechat, CSGO Translate checks the logfile for CSGOs console. 


## Installation

#### Requirements
```
unicodedata
googletrans
time
pydirectinput
pyperclip
threading
```

To enable console logging in CSGO, write `con_logfile conlog.log` in the CSGO console. This will create a file at `..\steamapps\common\Counter-Strike Global Offensive\csgo\conlog.log` which logs your console.


## Usage
```cmd
  > python csgo-translate.py USERNAME MY_LANGUAGE_CODE CONSOLE_LOG_PATH AUTO_SEND_TRANSLATION
  > python csgo-translate.py vinhed en "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\conlog.log" true
```

#### USERNAME
Enter your in-game username to enable sending translated messages<br>
Ex. `vinhed`

#### MY_LANGUAGE_CODE
Enter your Language Code from https://sites.google.com/site/opti365/translate_codes. This is the language all messages will be translated to.<br>
Ex. `en`

#### CONSOLE_LOG_PATH
Enter the path to your console-log file. The default path is `..\steamapps\common\Counter-Strike Global Offensive\csgo\conlog.log`<br>
Ex. `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\conlog.log`

#### AUTO_SEND_TRANSLATION
If true, your translated message will be sent directly after translation is done. Otherwise it will only be copied to your clipboard.<br>
Ex. `true/false`

### Retrieving Messages
All messages sent in the gamechat will be translated and output in the program console.<br>
Ex. `<Russian> vinhed: How are you?`<br>
![](https://raw.githubusercontent.com/vinhed/csgo-translate/main/images/RetrieveMessages.jpg?token=GHSAT0AAAAAABYYZIHL6BO3FV73R4TBFKNEYZCEJZQ)

### Sending Messages
To send translated messages in the gamechat, use the syntax `:TO_LANGUAGE_CODE MESSAGE` in the gamechat.<br>
Ex. `:ru Hello, how are you?`<br>
Out. `Привет, как дела?`<br>
![](https://raw.githubusercontent.com/vinhed/csgo-translate/main/images/SendMessages.jpg?token=GHSAT0AAAAAABYYZIHLKKW24LEXPDHLPAJIYZCEKFA)
