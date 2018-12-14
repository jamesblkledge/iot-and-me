# Written By Mourad Lasga

import json, time
from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/iot-and-me')

@app.route('/')
def homepage():
    return "Hi, how are you doing?"

@ask.launch
def start_skill():
    welcome_message = "Hi, ask me a specific question?"
    return question(welcome_message)

@ask.intent('QuestionOneIntent')
def question_1():
    output = "Nothing Much. I\'ve heard that MozFest is cool, especially IoT & Me!"
    with open('./alexa.txt', 'w') as alexa_responses:
        alexa_responses.write('1')
    return statement(output)

@ask.intent('QuestionTwoIntent')
def question_2():
    output = "I\'m Already Tracer..."
    with open('./alexa.txt', 'w') as alexa_responses:
        alexa_responses.write('2')
    return statement(output)

@ask.intent('QuestionThreeIntent')
def question_3():
    output = "Fortnite, Spiderman and Call of Duty Black Ops 4."
    with open('./alexa.txt', 'w') as alexa_responses:
        alexa_responses.write('3')
    return statement(output)

@ask.intent('QuestionFourIntent')
def question_4():
    output = "You\'re the best!"
    with open('./alexa.txt', 'w') as alexa_responses:
        alexa_responses.write('4')
    return statement(output)

if __name__ == '__main__':
    app.run(debug=False)