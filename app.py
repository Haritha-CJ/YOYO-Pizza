from flask import Flask

bot = Flask(__name__)


@bot.route("/test")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    bot.run()
