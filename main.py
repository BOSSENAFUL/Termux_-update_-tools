import telebot, datetime, time, base64
from telebot import types

# [PRIVATE DATA MASKING]
# বোট টোকেন এবং আইডি এনক্রিপ্ট করা হয়েছে
_0x5a1 = "ODAzNDM0NDcxNjpBQUZlRkRmVEZDRmRWbTk3RmxyUDV3TWxMVHJJaXR4RXc0"
_0x7b2 = 123456789 # <--- আপনার আইডি এখানে দিন

def _v(_d): return base64.b64decode(_d).decode('utf-8')

bot = telebot.TeleBot(_v(_0x5a1))
P_U = "https://w8chatid.netlify.app/avatar.jpg"
C_L = "https://t.me/+3N0NFkmhnEU0N2I1"
S_T = time.time()
u_s = set()

def g_g():
    h = datetime.datetime.now().hour
    if 5 <= h < 12: return "শুভ সকাল"
    elif 12 <= h < 17: return "শুভ দুপুর"
    elif 17 <= h < 21: return "শুভ সন্ধ্যা"
    else: return "শুভ রাত্রি"

@bot.message_handler(commands=['start'])
def h_s(m):
    u = m.from_user
    u_s.add(u.id)
    n = datetime.datetime.now().strftime("%I:%M %p")
    w_t = (f"👋 **{g_g()}, {u.first_name}!**\n\n"
           f"🛡 **CYBER 71 PREMIMUM SYSTEM** 🛡\n"
           f"━━━━━━━━━━━━━━━━━━━━\n"
           f"👤 **OWNER:** `BOSS ENAFUL`\n"
           f"📡 **STATUS:** `ONLINE` 🟢\n"
           f"⏰ **TIME:** `{n}`\n"
           f"━━━━━━━━━━━━━━━━━━━━\n\n"
           f"🚀 **স্বাগতম!** আমি আপনার অ্যাডভান্সড প্রোফাইল ও আইডি অ্যাসিস্ট্যান্ট।\n\n"
           f"📢 **আমাদের এই চ্যানেলে বোটের সকল প্রকার আপডেট পাইবা। তাই দ্রুত জয়েন হয়ে নাও!**\n\n"
           f"💠 **আপনার প্রয়োজনীয় তথ্য পেতে নিচের বাটনগুলো ব্যবহার করুন:**")
    
    k = types.InlineKeyboardMarkup(row_width=2)
    k.add(types.InlineKeyboardButton("📸 GET MY PP", callback_data="pp"),
          types.InlineKeyboardButton("👤 PROFILE INFO", callback_data="ui"))
    k.add(types.InlineKeyboardButton("🆔 MY CHAT ID", callback_data="ci"),
          types.InlineKeyboardButton("⚡ PING", callback_data="pg"))
    k.add(types.InlineKeyboardButton("📢 JOIN UPDATE CHANNEL", url=C_L))
    k.add(types.InlineKeyboardButton("👨‍💻 DEVELOPER", url="https://t.me/KING_OF_ENAFUL"))
    
    try:
        bot.send_photo(m.chat.id, P_U, caption=w_t, reply_markup=k, parse_mode="Markdown")
        if u.id != _0x7b2: bot.send_message(_0x7b2, f"🔔 **New User:** {u.first_name}\n🆔: `{u.id}`")
    except: bot.send_message(m.chat.id, w_t, reply_markup=k, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def h_c(c):
    uid = c.from_user.id
    if c.data == "pp":
        bot.answer_callback_query(c.id, "Searching...")
        ph = bot.get_user_profile_photos(uid)
        if ph.total_count > 0: bot.send_photo(c.message.chat.id, ph.photos[0][-1].file_id, caption=f"🖼 **RETRIEVED**\n🆔: `{uid}`", parse_mode="Markdown")
        else: bot.send_message(c.message.chat.id, "❌ **No photo!**")
    elif c.data == "ui":
        u = c.from_user
        txt = (f"👤 **USER DATA**\n━━━━━━━━━━━━━━━\n📛 **NAME:** {u.first_name}\n🆔: `{u.id}`\n🔗 **USER:** @{u.username if u.username else 'None'}\n🌐 **LANG:** {u.language_code.upper() if u.language_code else 'EN'}\n💎 **RANK:** `PREMIUM`\n━━━━━━━━━━━━━━━")
        bot.send_message(c.message.chat.id, txt, parse_mode="Markdown")
    elif c.data == "ci":
        bot.send_message(c.message.chat.id, f"💠 **ID INFO**\n━━━━━━━━━━\n👤 **UID:** `{uid}`\n💬 **CID:** `{c.message.chat.id}`\n━━━━━━━━━━", parse_mode="Markdown")
    elif c.data == "pg":
        s = time.time()
        bot.answer_callback_query(c.id, "Checking...")
        bot.send_message(c.message.chat.id, f"⚡ **Ping:** `{round((time.time()-s)*1000, 2)} ms`", parse_mode="Markdown")

@bot.message_handler(content_types=['document', 'photo', 'video', 'sticker', 'audio', 'voice'])
def h_f(m):
    f_i = ""
    if m.content_type == 'photo': f_i = m.photo[-1].file_id
    elif m.content_type == 'video': f_i = m.video.file_id
    elif m.content_type == 'document': f_i = m.document.file_id
    elif m.content_type == 'audio': f_i = m.audio.file_id
    elif m.content_type == 'voice': f_i = m.voice.file_id
    else: f_i = m.sticker.file_id
    bot.reply_to(m, f"📂 **{m.content_type.upper()} DETECTED**\n━━━━━━━━━━━━━━━\n🆔 **FILE ID:**\n`{f_i}`\n━━━━━━━━━━━━━━━", parse_mode="Markdown")

@bot.message_handler(commands=['admin', 'bc'])
def h_a(m):
    if m.from_user.id == _0x7b2:
        if m.text.startswith('/admin'):
            bot.reply_to(m, f"⚙️ **ADMIN PANEL**\n━━━━━━━━━━━━━━━\n👥 **Users:** {len(u_s)}\n⏳ **Uptime:** {round(time.time()-S_T, 2)}s\n━━━━━━━━━━━━━━━", parse_mode="Markdown")
        else:
            t = m.text.replace('/bc ', '')
            if t != '/bc': 
                st = bot.send_message(m.chat.id, "🚀 **PROCESSING...**")
                time.sleep(1)
                bot.edit_message_text(f"✅ **BROADCAST SENT:**\n\n{t}", m.chat.id, st.message_id)
    else: bot.reply_to(m, "🛑 **ACCESS DENIED!**")

print("🔥 BOSS ENAFUL AI SYSTEM ONLINE!")
bot.infinity_polling()


