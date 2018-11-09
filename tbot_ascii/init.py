import telebot
import config

bot = telebot.TeleBot(config.token)

'''@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)'''

@bot.message_handler(content_types=["text"])
def change_text_message(message):

	ascii_text=[]

   	for i in range(len(message.text)):
   		#ascii_text.append(0)
		ascii_text.append(map(ord, message.text[i]))
			
		ascii_string = " ".join(str(e) for e in ascii_text)

	bot.send_message(message.chat.id, ascii_string)

if __name__ == '__main__':
    bot.polling(none_stop=True)