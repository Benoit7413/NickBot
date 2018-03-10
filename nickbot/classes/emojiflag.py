import re


class EmojiFlag:

    def add(nick, code):
        if code == "":
            return nick
        res = ""
        s = ""
        regex = re.compile(r"(AF|AX|AL|DZ|AS|AD|AO|AI|AQ|AG|AR|AM|AW"
                           "|AU|AT|AZ|BS|BH|BD|BB|BY|BE|BZ|BJ|BM|BT"
                           "|BO|BQ|BA|BW|BV|BR|IO|BN|BG|BF|BI|KH|CM"
                           "|CA|CV|KY|CF|TD|CL|CN|CX|CC|CO|KM|CG|CD"
                           "|CK|CR|CI|HR|CU|CW|CY|CZ|DK|DJ|DM|DO|EC"
                           "|EG|SV|GQ|ER|EE|ET|FK|FO|FJ|FI|FR|GF|PF"
                           "|TF|GA|GM|GE|DE|GH|GI|GR|GL|GD|GP|GU|GT"
                           "|GG|GN|GW|GY|HT|HM|VA|HN|HK|HU|IS|IN|ID"
                           "|IR|IQ|IE|IM|IL|IT|JM|JP|JE|JO|KZ|KE|KI"
                           "|KP|KR|KW|KG|LA|LV|LB|LS|LR|LY|LI|LT|LU"
                           "|MO|MK|MG|MW|MY|MV|ML|MT|MH|MQ|MR|MU|YT"
                           "|MX|FM|MD|MC|MN|ME|MS|MA|MZ|MM|NA|NR|NP"
                           "|NL|NC|NZ|NI|NE|NG|NU|NF|MP|NO|OM|PK|PW"
                           "|PS|PA|PG|PY|PE|PH|PN|PL|PT|PR|QA|RE|RO"
                           "|RU|RW|BL|SH|KN|LC|MF|PM|VC|WS|SM|ST|SA"
                           "|SN|RS|SC|SL|SG|SX|SK|SI|SB|SO|ZA|GS|SS"
                           "|ES|LK|SD|SR|SJ|SZ|SE|CH|SY|TW|TJ|TZ|TH"
                           "|TL|TG|TK|TO|TT|TN|TR|TM|TC|TV|UG|UA|AE"
                           "|GB|US|UM|UY|UZ|VU|VE|VN|VG|VI|WF|EH|YE"
                           "|ZM|ZW)", re.IGNORECASE)
        matches = re.finditer(regex, code)
        for matchNum, match in enumerate(matches):
            unicodes = s.join([chr(127365 + ord(char.lower()))
                               for char in match.group()])
            res += " " + unicodes

        return nick + " |" + res

    def remove(nick):
        res = ""
        regex = r"[\U0001F1E6-\U0001F1FF ]+"
        nick_split = nick.split(" | ")
        matches = re.search(regex, nick_split[-1], re.UNICODE)
        if matches:
            return nick.replace(" | " + matches.group(), "")
        else:
            return nick

    def change(nick, new):
        nick = EmojiFlag.remove(nick)
        if new == "":
            return nick
        nick = EmojiFlag.add(nick, new)
        return nick
