import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6379366888:AAHAkBbvCnzxzmOu23oaPjQ0MeBEEiR4q6c)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BJWap1wBu05O0K_pc4JILjWjOwDS4V__QUY3b4hkAcdr9hiS1fp6gxYTpkLmZLWvuUQAkej-7luylU_tzsVw1W__BMMk9RkokVzTnwIYYm0ObG6cMxH-UkkaVGvoiHqxgjX87EGqopxPcPbryDvVL24Gm4wjN_GkQ6eVJGXCxzzmgIjl4V_Qy11XiW9jGXIyyrpc4m732mVnWv-IbiE0j0p0dJo1rQ-60iM8t7TkJI0sNaYmdnz_nOufYo91uze8vJTVV2swXxmYmm9qUg3IEZ748C-LP5F3fmMf-B1WvASfyiG2l9lrHWfpjDEjweKNEbzJJl1Cs5kIYKx3U_CE1RWWt_AlzOY=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
