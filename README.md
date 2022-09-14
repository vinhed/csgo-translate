# CSGO Translate

This program translates messages sent in the game Counter-Strike: Global Offensive. CSGO Translate uses Google Translates API to translate messages sent in the gamechat. CSGO Translate will not get you banned since it does not modify the game files in any way, nor does it read or write to memory. To retrieve the gamechat, CSGO Translate checks the logfile for CSGOs console. 


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
