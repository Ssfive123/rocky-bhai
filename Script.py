class script(object):
    START_TXT = """<b>π§α΄ΚΚα΄ {} ππ»ββοΈπ¬Κ π­α΄α΄α΄ Ιͺs <a href='https://t.me/MH_elonmusk_bot'>π€Κα΄Ι΄ π¬α΄sα΄.</a> π  π²α΄α΄Κα΄ π±α΄Κα΄α΄ πΆΙͺα΄Κ π¬α΄Ι΄Κ π α΄α΄α΄’ΙͺΙ΄Ι’ π₯α΄α΄α΄α΄Κα΄s. π¨ π’α΄Ι΄ π―Κα΄α΄ Ιͺα΄α΄ π¬α΄α΄ Ιͺα΄s & π§α΄Κα΄ πΈα΄α΄ π³α΄ π¬α΄Ι΄α΄Ι’α΄ πΈα΄α΄Κ π¦Κα΄α΄α΄s, π©α΄sα΄ π α΄α΄ π¬α΄ π³α΄ πΈα΄α΄Κ π¦Κα΄α΄α΄ π s π α΄α΄ΙͺΙ΄ π Ι΄α΄ π€Ι΄α΄α΄Κ.....π₯°</b>
"""
    HELP_TXT = """<b>Hα΄ΚΚα΄ {}
    
π π’α΄α΄α΄α΄Ι΄α΄ Κα΄Κα΄ π</b>"""
    ABOUT_TXT = """<b>ββββ[ α΄α΄‘Ι΄α΄Κ α΄α΄α΄α΄ΙͺΚκ± ]ββββ
    
β’ κ°α΄ΚΚ Ι΄α΄α΄α΄ : sΚΙͺα΄ α΄
β’ α΄κ±α΄ΚΙ΄α΄α΄α΄ : @OGGY123kph
β’ α΄α΄Κα΄α΄Ι΄α΄Ι΄α΄ α΄α΄ ΚΙͺΙ΄α΄ : <a href='https://t.me/OGGY123kph'>α΄ΚΙͺα΄α΄ Κα΄Κα΄</a>
β Failure is an option here. If things are not failing, you are not innovating enough. β</b>"""
    SOURCE_TXT = """<b>NOTE:</b>

- ΰ΄ΰ΄ͺΰ΅ΰ΄ͺΰ΅ ΰ΄ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅ΰ΄ ΰ΄¨ΰ΅ΰ΄ΰ΅ΰ΄ΰ΄Ώ ΰ΄ΰ΄°ΰ΅ΰ΄¨ΰ΅ΰ΄¨ΰ΅ .

<b>DEVS:</b>
- <a href=https://t.me/smovieofficial>dk [OFLINE]</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ππΌπππΈ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- BOT Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ππΌπππΈ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+_gaIOMP_AjM0MWNl)</code>

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
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ππΌπππΈ

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """π ?ΙͺΚα΄s sα΄α΄ α΄α΄: <code>{}</code>
π€ α΄sα΄Κs: <code>{}</code>
π₯ Ι’Κα΄α΄α΄s: <a href='https://t.me/movie_hub_main'>π¬α΄α΄ Ιͺα΄ π§α΄Κ</a> α΄Ι΄ΚΚ
π α΄α΄α΄α΄α΄Ιͺα΄α΄: <code>{}</code> πΌππ±"""
 
    LOG_TEXT_G = """π? α΄α΄ΚΚ Κα΄α΄ #NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """π? α΄α΄ΚΚ Κα΄α΄ #NewUser
ID - <code>{}</code>
Name - {}
"""
