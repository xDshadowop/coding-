

'''
def lmao():
  try:
    if k == 10:
      return (".")
    else:
      return ("no")
  except Exception as T:
   print(T)
 
k = lmao()
print (k)


'''
'''
async for x in bot.iter_messages(event.chat_id):
  if x.text.startswith("Shadow"):
    await bot.forward_messages(event.chat_id, x.id, event.chat_id)
    break
  else:
    continue
'''
'''
ok = 0
async for x in bot.iter_dialogs(limit=5):
   try:
      await bot.send_message(x.id, "hello "+str(ok))
      ok+1
   execpt pass'''





# COPYRIGHT 2022-2023 BY @LEGENDX22

from operator import truediv
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
string_session = "1BVtsOHoBuy8oxCgT6dguCR806Rn_xbxvpSAXaJyZFtqCQJKEP3LfrCbjLU7qIChHALNYtWAIusGIyezk0nCExGp3wEiMAJezQas6ajtqPPE33Of1MSrIR1nPtydBUGoYqMNg6uSgVDZG_tdzXfThSCBbpeFui5NVmZLtfKkQvX7od2L5JiahoULKARS6sLds2jlKTKN_3NIMtyzYGYkcgWoQe6ptNC4syVkT5-AmKy6rTg3Svo9-Rxwxl9Y6R6X63iSYR9IXu608rnHsiW6H_wr_fAsqdWb9D8QauY_pNKn3wza9w2zQy2CdcWPrKUnKUtsN-onU_qA1PWZIifHYXz35YVQdWEg="


def cc_digits(cc):
    k = cc[::-1]
    k = k[0:16]
    k = k[::-1]
    return k


'''
0: 16
1: 2
2: 4
3: 3
'''

# def valid_cc(hehe):
#         if len(cc_digits(hehe[0])) != 16:

#             return "False"
#         if len(hehe[[1]]) != 2:
#             return "False"
#         if len(hehe[2]) != 4:
#             return "False"
#         if len(hehe[3]) != 3:
#             return "False"


def text_to_cc(text):
    hehe = text.split("|")
    if len(hehe) == 4:
        cc_numbers = cc_digits(hehe[0])
        cc_month = hehe[1]
        cc_year = hehe[2]
        cc_cvv = hehe[3]
        full_cc = f"{cc_numbers}|{cc_month}|{cc_year}|{cc_cvv[0:3]}"
        return full_cc
    else:
        return False



api_id = 1621727
api_hash = "31350903c528876f79527398c09660ce"
token = "5318623425:AAGSiVJZ3STd9YgnZBTZYydL3mIfKWeuGHI"

async def ses_join(ses, chat):
    async with TelegramClient(StringSession(ses), api_id,  api_hash) as bot:
        await bot(JoinChannelRequest(chat))
        return True

async def ses_leave(ses, chat):
    async with TelegramClient(StringSession(ses), api_id,  api_hash) as bot:
        try:
            chat = await bot.get_entity(int(chat))
        except:
            chat = await bot.get_entity(str(chat))
        await bot(LeaveChannelRequest(chat))
        return True


async def ses_chats(ses):
    async with TelegramClient(StringSession(ses), api_id,  api_hash) as bot:
        text = ""
        async for x  in bot.iter_dialogs():
          if x.message.post:
            try:
                text += f"Channel: {x.name} ID: {x.id}\n"
            except:
                pass
          else:
              pass
        return text
            


async def ses_run(ses, chat, limit_of_msgs):
    credit_cards = ""
    async with TelegramClient(StringSession(ses), api_id,  api_hash) as bot:
        print("session logged in successfully")
        try:
            chat = await bot.get_entity(int(chat))
            print(chat)
        except:
            # print("chat is string")
            chat = await bot.get_entity(str(chat))
        async for x in bot.iter_messages(chat):
                try:
                    x.text
                except:
                    continue
                if str(x.id) == str(limit_of_msgs):
                    # print("matched")
                    return credit_cards
                else:
                    print("hehe")
                    if str(x.text) == "None":
                        pass
                    else:
                        credit_cards += str(x.text) + "\n"
        return credit_cards


bot = TelegramClient("cc_scrape", api_id, api_hash).start(bot_token=token)
legendx = [1967548493]

def make_file(cc):
    f = open("cc.txt", "w")
    f.write(cc)
    f.close()

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.respond("Hello sir This is cc scrape bot\nBy @LEGENDX22")

@bot.on(events.NewMessage(incoming=True, pattern="/stats", from_users=legendx))
async def stats(event):
    k  = await ses_chats(string_session)
    await event.respond(k)

@bot.on(events.NewMessage(incoming=True, pattern="/join", from_users=legendx))
async def join(event):
    text = event.text.split(" ", 1)[1]
    k  = await ses_join(string_session, text)
    await event.respond("done")

@bot.on(events.NewMessage(incoming=True, pattern="/leave", from_users=legendx))
async def leave(event):
    text = event.text.split(" ", 1)[1]
    await ses_leave(string_session, text)
    await event.respond("done")

@bot.on(events.NewMessage(incoming=True, pattern="/scrape", from_users=legendx))
async def work(event):
    text =  event.text.split(" ", 1)[1]
    chat_id =  text.split(" ", 1)[0]
    msg_id =  text.split(" ", 1)[1]
    await event.respond("ok running")
    cc = await ses_run(string_session, chat_id, msg_id)
    k = iter(cc.splitlines())
    cc = ""
    for x in k:
        ok = text_to_cc(x)
        if ok:
            cc += str(ok) + "\n"
        else:
            pass
    cc = str(cc).replace("`", "")
    make_file(cc)
    await event.respond(file="cc.txt")
    print(str(ok))

bot.run_until_disconnected()
