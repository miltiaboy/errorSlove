class script(object):
    START_TXT = """<b>𝖧𝖾𝗒 {}, 𝖨 𝖠𝗆 <a href=https://t.me/{}>{}</a>, 𝖧𝖺𝗉𝗉𝗒 🖤 𝖳𝗈 𝖧𝖺𝗏𝖾 𝖸𝗈𝗎

Here You Can Request Movie's, Just Sent <a href='https://t.me/mcu_Mammootty_bot'>Movie Name</a> With Proper <a href='https://www.google.com/'>Google</a> Spelling..!!

Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟꜱ Cʟɪᴄᴋ /help

Cᴏɴᴛᴀᴄᴛ Bᴏᴛ Dᴇᴠᴇʟᴏᴘᴇʀ (Oʀ) Rᴇᴘᴏʀᴛ Bᴜɢꜱ..!! 👉 @MCU_ADMIN_V1_BOT</b>"""

    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    STATUS_TXT2 = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𝗗𝗕 𝟭
𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌         - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB

𝗗𝗕 𝟮
𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌         - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB

𝗗𝗕 𝟯
📦 𝖴𝗌𝖾𝗋𝗌            - <code>{}</code>
🖥️ 𝖢𝗁𝖺𝗍𝗌            - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""


    MOVREQ_TXT = """<b><blockquote> 🚸 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖱𝗎𝗅𝖾𝗌 🚸

🌿ഇംഗ്ലീഷ് ഭാഷയിൽ തന്നെ movies/Series റിക്വസ്റ്റ് ചെയ്യുക 
🌿റിലീസ് ആവാത്ത മൂവീസ് ചോദിച്ചു സമയം കളയണ്ട 
🌿സിനിമയുടെ പേര് വർഷം എന്നിവ മാത്രം അയച്ചാൽ മതി 
🌿ഉണ്ടോ,തരുവോ,മൂവി,ലിങ്ക്,സിനിമ എന്നീ ഡയലോഗ്കൾ വേണ്ട കേട്ടോ 
🌿സ്റ്റൈലിഷ് അക്ഷരങ്ങൾ ഉപയോഗിക്കരുത് 
🌿സിംബൽസിന്റെ ആവശ്യവും ഇവിടെ വരുന്നില്ല.. അത് ഒഴിവാക്കുക(+:;'!-|...𝖾𝗍𝖼)</blockquote></b>"""
    
    NORSLTS = """𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>


𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <code>{}</code>"""


    CUSTOM_FILE_CAPTION = """<b>𝐻𝑒𝑙𝑙𝑜 👋 {mention} 😍
    
{file_caption}

╔═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╗ 
➲ <a href='t.me/MCUupdatesLINKS'>@OTT UPDTES</a>
➲ <a href='https://t.me/+uA5gEKm8WXk1ZTll'>@MAIN CHANNEL</a>
╚═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╝
</b>"""
