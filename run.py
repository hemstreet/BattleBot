#!/usr/bin/env python
from battleBot import BattleBot
from flask import Flask, render_template

bot = BattleBot()

app = Flask(__name__)


@app.route("/")
def main_route():
    return render_template('_home.html')


@app.route("/attack")
def attack_route():
    bot.attack()

    return render_template('_attack.html')


@app.route("/move/<direction>/<speed>")
def move_route(direction, speed):
    bot.move(direction, speed)
    return render_template('_move.html',  **locals())


if __name__ == "__main__":
    app.run()
