class script(object):
    START_TXT = """๐ท๐ด๐ปL๐พ {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/Jaison_Tg_Bot>๐น๐ฐ๐ธ๐๐พ๐ฝ</a>,๐๐ฟ๐ด๐ป๐ป๐ธ๐ฝ๐ถ ๐ธ๐ ๐ฟ ๐ฐ ๐ ๐บ ๐ด ๐ ๐ธ๐ต ๐๐ ๐ฐ๐๐ด ๐ฐ ๐ผ๐พ๐๐ธ๐ด ๐ป๐พ๐๐ด๐ ๐ ๐น๐๐๐ ๐น๐พ๐ธ๐ฝ ๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ถ๐ธ๐๐ด ๐ผ๐พ๐๐ธ๐ด ๐ฝ๐ฐ๐ผ๐ด ๐
๐๐ท๐ด๐ฝ ๐๐พ๐พ๐ฝ ๐๐ ๐๐ธ๐ป๐ป ๐ถ๐ด๐ ๐๐ท๐ด ๐ผ๐พ๐๐ธ๐ด ๐ค  ๐ถ๐๐พ๐๐ฟ ๐ป๐ธ๐ฝ๐บ ๐๐ ๐ธ๐ ๐ธ๐ฝ ๐๐ท๐ด ๐ณ๐ด๐๐ฒ๐๐ธ๐ฟ๐๐ธ๐พ๐ฝ ๐ฅธ
๐ผ๐ ๐ณ๐ด๐๐ด๐ป๐พ๐ฟ๐ด๐๐ ๐๐

๐ฑ๐พ๐ ๐ผ๐ฐ๐บ๐ด๐: <a href=https://t.me/Bad_Bunny_444>๐โ ๐๐ฏ๐ข๐๐ช</a>
๐ณ๐ด๐๐ด๐ป๐พ๐ฟ๐ด๐: <a href=https://t.me/PshycoJoker>๐๐๐</a>"""


    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
โฏ ๐ฒ๐๐ด๐ฐ๐๐พ๐: <a href=https://t.me/ANKIT3690>แฅด๊ชฎ๊ช</a>
โฏ ๐ฒ๐๐ด๐ฐ๐๐พ๐: <a href=https://t.me/MR_BADDD>๐ผ๏ธ๐๏ธ ๐ฑ๏ธ๐ฐ๏ธ๐ณ๏ธ๐ณ๏ธ</a>
โฏ ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: v1.0.1 [ ๐ฑ๐ด๐๐ฐ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
โฏ ๐๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐๐๐.
๐เดเดจเตเดคเดพเดเดพ เดฎเตเดจเต เดจเตเดเตเดเตเดจเตเดจเต เดจเดฟเดจเดเตเดเต เดเดตเดถเตเดฏเดฎเดพเดฏเดฟเดเตเดเตเดณเตเดณเดคเต เดเดตเดฟเดเต เดเดฒเตเดฒ 

<b>๐ณ๐ด๐๐ด๐ป๐พ๐ฟ๐ด๐๐:</b>
โฏ <a href=https://t.me/Bad_Bunny_444>๐.๐</a>
โฏ <a href=https://t.me/MR_BADDD>๐ผ๏ธ๐๏ธ ๐ฑ๏ธ๐ฐ๏ธ๐ณ๏ธ๐ณ๏ธ</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ๐น๐ฐ๐ธ๐๐พ๐ฝ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ๐ฟ๐ฐ๐๐บ๐ด๐ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ๐ฑ๐ฐ๐ณ ๐ฑ๐๐ฝ๐ฝ๐ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ๐ฟ๐ฐ๐๐บ๐ด๐

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """แฅด๊ชฎ๊ช: <b>แฅด๊ชฎ๊ช</b>

<b>๐ณ๐ด๐๐ด๐ป๐พ๐ฟ๐ด๐๐:</b>
โขโฏ <a href=https://t.me/MR_BADDD>MR BADD</a>
โขโฏ <a href=https://t.me/Bad_Bunny_444>๐.๐</a>"""

    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
