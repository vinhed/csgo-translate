import sys

iso639 = {'af': 'Afrikaans', 'ga': 'Irish', 'sq': 'Albanian', 'it': 'Italian', 'ar': 'Arabic', 'ja': 'Japanese',
          'az': 'Azerbaijani', 'kn': 'Kannada', 'eu': 'Basque', 'ko': 'Korean', 'bn': 'Bengali', 'la': 'Latin',
          'be': 'Belarusian', 'lv': 'Latvian', 'bg': 'Bulgarian', 'lt': 'Lithuanian', 'ca': 'Catalan',
          'mk': 'Macedonian', 'zh-CN': 'Chinese Simplified', 'ms': 'Malay', 'zh-TW': 'Chinese Traditional',
          'mt': 'Maltese', 'hr': 'Croatian', 'no': 'Norwegian', 'cs': 'Czech', 'fa': 'Persian', 'da': 'Danish',
          'pl': 'Polish', 'nl': 'Dutch', 'pt': 'Portuguese', 'en': 'English', 'ro': 'Romanian', 'eo': 'Esperanto',
          'ru': 'Russian', 'et': 'Estonian', 'sr': 'Serbian', 'tl': 'Filipino', 'sk': 'Slovak', 'fi': 'Finnish',
          'sl': 'Slovenian', 'fr': 'French', 'es': 'Spanish', 'gl': 'Galician', 'sw': 'Swahili', 'ka': 'Georgian',
          'sv': 'Swedish', 'de': 'German', 'ta': 'Tamil', 'el': 'Greek', 'te': 'Telugu', 'gu': 'Gujarati', 'th': 'Thai',
          'ht': 'Haitian Creole', 'tr': 'Turkish', 'iw': 'Hebrew', 'uk': 'Ukrainian', 'hi': 'Hindi', 'ur': 'Urdu',
          'hu': 'Hungarian', 'vi': 'Vietnamese', 'is': 'Icelandic', 'cy': 'Welsh', 'id': 'Indonesian', 'yi': 'Yiddish'}

class CSGOTranslate:
    import unicodedata
    from googletrans import Translator
    from time import sleep
    import pydirectinput
    import pyperclip
    import threading

    version = "1.0.0"

    def __init__(self, _config):
        self.config = _config
        open(self.config['console_path'], "w").close()
        self.console_file = open(self.config['console_path'], "r", encoding='utf-8')

        print(f"\nRunning CSGO Translate - Version: {self.version}")
        self.print_config()

        self.messages_to_send = []
        self.translator = self.Translator()
        self.csgo_translate()

    def print_config(self):
        for option in list(self.config.keys()):
            print(f'{option.replace("_", " ").capitalize()}: {self.config[option]}')
        print("\n")

    # Write chat messages
    def write_chat(self):
        while True:
            self.sleep(0.01)
            if len(self.messages_to_send) == 0:
                continue
            else:
                message = self.messages_to_send[0]
            self.messages_to_send.pop(0)
            if message[0] != ':':
                continue
            if self.config['auto_send']:
                self.pydirectinput.press('y')
            tmp = message.split(" ")
            to_lang = tmp[0][1:]
            to_trans = ' '.join(tmp[1:])
            try:
                translated_message = self.translator.translate(to_trans, dest=to_lang, src=self.config['language'])
                self.pyperclip.copy(translated_message.text)
                if self.config['auto_send']:
                    self.pydirectinput.keyDown('ctrl')
                    self.pydirectinput.keyDown('v')
                    self.sleep(0.01)
                    self.pydirectinput.keyUp('v')
                    self.pydirectinput.keyUp('ctrl')
                    self.pydirectinput.press('enter')
                    print(f"Sent translation <{iso639[to_lang]}>")
                else:
                    print(f"Translation copied to clipboard <{iso639[to_lang]}>")
            except ValueError:
                print("Invalid Language-code, refer to https://sites.google.com/site/opti365/translate_codes")

    # Read chat messages
    def check_for_chat_message(self, content):
        messages = []
        if content != "":
            for line in [line for line in content.split("\n") if line != ""]:
                if ":" in line and ('\u200e' in line or '\u200f' in line):
                    data = self.unicodedata.normalize("NFKD", line)
                    sender = data.split(":")[0][:-2]
                    message = ':'.join(data.split(":")[1:])[1:]
                    messages.append({'sender':sender, 'message':message})
        return messages

    def read_chat(self):
        while True:
            self.sleep(0.01)
            content = self.console_file.read()
            messages = self.check_for_chat_message(content)
            if len(messages) > 0:
                for message in messages:
                    sender = message['sender']
                    message = message['message']
                    if sender == self.config['username']:
                        self.messages_to_send.append(message)
                        continue
                    translated_message = self.translator.translate(message, dest=self.config['language'])
                    origin = translated_message.src
                    if origin in iso639.keys():
                        origin = iso639[translated_message.src]
                    print(f"<{origin}> {sender}: {translated_message.text}")

    def csgo_translate(self):
        write_thread = self.threading.Thread(target=self.write_chat, daemon=True)
        write_thread.start()
        self.read_chat()

if __name__ == '__main__':
    config = {
        'username': "USERNAME",
        'language': "en",
        'console_path': "...\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\conlog.log",
        'auto_send': "True"
    }

    if len(sys.argv) == 5:
        config['username'] = sys.argv[1]
        config['language'] = sys.argv[2]
        config['console_path'] = sys.argv[3]
        config['auto_send'] = sys.argv[4]

    if config['language'] not in list(iso639.keys()):
        print("Invalid Language-code, refer to https://sites.google.com/site/opti365/translate_codes")
        sys.exit()

    if config['auto_send'].lower() == 'true':
        config['auto_send'] = True
    else:
        config['auto_send'] = False

    translate = CSGOTranslate(config)

