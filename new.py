

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
ok = 0
async for x in bot.iter_dialogs(limit=5):
   try:
      await bot.send_message(x.id, "hello "+str(ok))
      ok+1
   execpt pass
