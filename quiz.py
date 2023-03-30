
from quiz_base import PopQuiz, CorrectAnswer
from flask_wtf import FlaskForm as Form
from wtforms import RadioField
import countries, random


country_capital = countries.get_random_country()
thecountry = country_capital['country']
thecapital = country_capital['capital']
random_capitals = countries.get_three_capitals()
correct_answer = (thecapital, thecapital)
random_capitals.append((thecapital, thecapital))
random.shuffle(random_capitals)

def random_quiz():
    global thecountry, thecapital, random_capitals, correct_answer
    country_capital = countries.get_random_country()
    thecountry = country_capital['country']
    thecapital = country_capital['capital']
    random_capitals = countries.get_three_capitals()
    correct_answer = (thecapital, thecapital)
    random_capitals.append((thecapital, thecapital))
    random.shuffle(random_capitals)

    print("thecountry: ", thecountry)
    print("thecapital: ", thecapital)

    #return PopQuizTest()


class PopQuizTest(Form):
    class Meta:
        csrf = False
        
    q1 = RadioField(
            f"The capital of {thecountry} is ...",
            choices=random_capitals,
            validators=[CorrectAnswer(thecapital)]
        )