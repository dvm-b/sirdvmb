#HELL YEAH BITCH FINALLY I DID IT, CRY HARDER YOU WON'T GET THE TOKEN DICKHEAD
import requests
import sys


api = "https://dvmbmem.vercel.app/api/"

ch = "@reuiews"

red = "\033[31m";green = "\033[32m";cya = "\033[36m";reset = "\033[0m"

def userid():
    while True:
        try:
            
            anim(f""" ㅤ{cya}ㅤ[ ⚚ ]    𝐄𝚗𝚝𝚎𝚛 𝐈𝙳 𝐁𝚎𝚕𝚘𝚠 𝐓𝚘 𝐂𝚑𝚎𝚌𝚔 ⏎{reset}""")
            return int(input(f" ㅤ{white}ㅤ➡ ㅤ"))
        except ValueError:
            anim(f""" ㅤ{red}ㅤ[ ⚚ ]    𝐈𝚜 𝐘𝚘𝚞𝚛 𝐁𝚛𝚊𝚒𝚗 𝐋𝚘𝚌𝚊𝚝𝚎𝚍 𝐈𝚗 𝐘𝚘𝚞𝚛 𝐀𝚜𝚜?  {reset}""")

def mem(uid):
    try:
        response = requests.get(api, params={"user_id": uid}, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        anim(f" ㅤ{red}ㅤ[ ⚚ ]    𝐔𝚗𝚊𝚋𝚕𝚎 𝐓𝚘 𝐅𝚎𝚝𝚌𝚑 𝐀𝚙𝚒 {e}")
        sys.exit(1)
    except ValueError as e:
        anim(f" ㅤ{red}ㅤ[ ⚚ ]    𝐈𝚗𝚟𝚊𝚕𝚒𝚍 𝐑𝚎𝚜𝚙𝚘𝚗𝚜𝚎 𝐅𝚛𝚘𝚖 𝐀𝚙𝚒")
        sys.exit(1)

    if data.get("ok") and data.get("member"):
        anim(f" ㅤ{green}ㅤ[ ⚚ ]    𝐆𝚘𝚘𝚍 𝐁𝚘𝚢")
    else:

        anim(f" ㅤ{red}ㅤ[ ⚚ ]    𝐉𝚘𝚒𝚗 𝐀𝚕𝚕 𝐂𝚑𝚊𝚗𝚗𝚎𝚕𝚜 / 𝐀𝚍𝚍 𝐅𝚘𝚕𝚍𝚎𝚛")
        webbrowser.open("https://t.me/addlist/-zdOU4i16nNjZjll")
        anim(f" ㅤ{cya}ㅤ[ ⚚ ]    𝐀𝚏𝚝𝚎𝚛 𝐉𝚘𝚒𝚗𝚒𝚗𝚐, 𝐑𝚎𝚜𝚝𝚊𝚛𝚝 𝐓𝚑𝚎 𝐓𝚘𝚘𝚕")
        sys.exit(0)

anim(f" ㅤ{cya}ㅤ[ ⚚ ]    𝐉𝚘𝚒𝚗 𝐀𝚕𝚕 𝐂𝚑𝚊𝚗𝚗𝚎𝚕𝚜 𝐅𝚒𝚛𝚜𝚝 𝐓𝚘 𝐏𝚛𝚘𝚌𝚎𝚎𝚍")
uid = userid()

mem(uid)
