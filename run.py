#!/usr/bin/env python
from battleBot import BattleBot
from flask import Flask

bot = BattleBot()

app = Flask(__name__)


@app.route("/")
def main_route():
    return "Home"


@app.route("/attack")
def attack_route():
    bot.attack()
    return "Attack"


@app.route("/move/<direction>/<speed>")
def move_route(direction, speed):
    bot.move(direction, speed)
    return "Move " + direction + " " + speed


if __name__ == "__main__":
    app.run()
