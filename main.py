import telebot
import os
import random
import requests
images = os.listdir('images')


bot = telebot.TeleBot('7663125275:AAEOh5TO84wldZCSM71hX2bs-ZvZO-I31l8')

@bot.message_handler(commands=['meme'])
def send_meme(massege):
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:
        bot.send_photo(massege.chat.id, f)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['dog'])
def dog(message):
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)


    

@bot.message_handler(commands=['fact'])
def command(message):
    facts = ['Экология — наука, изучающая взаимоотношения живых организмов между собой и с окружающей средой.',
             'Экология важна в нашей жизни потому, что она изучает и помогает поддерживать баланс в природных системах,'
             ' от которых зависит наше существование. Без здорового состояния экосистем мы рискуем потерять важные ресурсы, такие как чистая вода, воздух и пища.']
    bot.send_message(message.chat.id, random.choice(facts))
    


@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "Зачем нужна экология?")
    answer_options = ["просто так",
                        "она нужна чтобы мы были счастливы",
                        "она нужна чтобы наш мир был чист, и мы дышали свежим воздухом",
                        "она не нужна"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Зачем нужна экология?",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )


@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass


bot.polling()