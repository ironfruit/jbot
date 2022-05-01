from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Friday')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
   'chatterbot.corpus.english.greetings',
   'chatterbot.corpus.english.conversations',
   'chatterbot.corpus.english.food',
   'chatterbot.corpus.english.emotion',
   'chatterbot.corpus.english.health',
   'chatterbot.corpus.english.movies',
   'chatterbot.corpus.english.psychology',
   'chatterbot.corpus.english.trivia'
)

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[38;2;255;255;255m"

# Now let's get a response to a greeting
while True:
    try:
        bot_input = chatbot.get_response(input())
        colored_bot_input = colored(255, 0, 0, bot_input)
        print(colored_bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break