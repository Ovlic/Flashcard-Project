
from flask import Flask, render_template, redirect, url_for, request, session
import time, random, countries, os, redis
from flask_session import Session

from quiz_base import CorrectAnswer
from flask_wtf import FlaskForm as Form
from wtforms import RadioField

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')
app.secret_key = os.urandom(24)

sess = Session()
sess.init_app(app)


def random_quiz():
    country_capital = countries.get_random_country()
    thecountry = country_capital['country']
    thecapital = country_capital['capital']
    random_capitals = countries.get_three_capitals()
    correct_answer = (thecapital, thecapital)
    random_capitals.append((thecapital, thecapital))
    random.shuffle(random_capitals)
    return thecountry, thecapital, random_capitals, correct_answer

thecountry, thecapital, random_capitals, correct_answer = random_quiz()

incorrect_answers = []
countries_guessed = []
counter = 0
correct_counter = 0
question_counter = 5
percent_counter = 0
percent_increase = 100/question_counter

def add_to_session(
    thecountry: str,
    thecapital: str, 
    random_capitals: list, 
    correct_answer: tuple, 
    incorrect_answers: list,
    countries_guessed: list,
    counter: int,
    correct_counter: int,
    question_counter: int,
    percent_counter: int,
    percent_increase: float
    ):
    session['thecountry'] = thecountry
    session['thecapital'] = thecapital
    session['random_capitals'] = random_capitals
    session['correct_answer'] = correct_answer
    session['incorrect_answers'] = incorrect_answers
    session['countries_guessed'] = countries_guessed
    session['counter'] = counter
    session['correct_counter'] = correct_counter
    session['question_counter'] = question_counter
    session['percent_counter'] = percent_counter
    session['percent_increase'] = percent_increase
    print(f"Type test: {type(session.get('counter', None))}")

def get_from_session():
    print(f"Type test from get: {type(session.get('counter', None))}")
    thecountry = session.get('thecountry', None)
    thecapital = session.get('thecapital', None)
    random_capitals = session.get('random_capitals', None)
    correct_answer = session.get('correct_answer', None)
    incorrect_answers = session.get('incorrect_answers', None)
    countries_guessed = session.get('countries_guessed', None)
    counter = (session.get('counter', None))
    correct_counter = session.get('correct_counter', None)
    question_counter = session.get('question_counter', None)
    percent_counter = session.get('percent_counter', None)
    percent_increase = session.get('percent_increase', None)
    return thecountry, thecapital, random_capitals, correct_answer, incorrect_answers, countries_guessed, counter, correct_counter, question_counter, percent_counter, percent_increase


@app.route('/', methods=['GET', 'POST'])
def wtf_quiz(): 
    global incorrect_answers, counter, percent_counter, percent_increase, correct_counter, question_counter, countries_guessed, thecountry, thecapital, random_capitals, correct_answer
    print("***************")
    if counter in request.args:
        counter = int(request.args['counter'])
        print(f"Got counter from request.args, counter = {counter}")
    print(request.args['thecountry'] if 'thecountry' in request.args else "No thecountry")
    if counter != 0:
        thecountry, thecapital, random_capitals, correct_answer, incorrect_answers, countries_guessed, fake_counter, correct_counter, question_counter, percent_counter, percent_increase = get_from_session()
    else:
        session['counter'] = counter
        print(f"Set counter in session, counter = {counter}")

    if 'thecountry' in request.args:
        thecountry = request.args['thecountry']
        print("Got thecountry from request.args")
    if 'thecapital' in request.args:
        thecapital = request.args['thecapital']
        print("Got thecapital from request.args")

    if 'random_capitals' in request.args:
        random_capitals_str = request.args['random_capitals']
        random_capitals_str = random_capitals_str.replace("'", "").replace('"', '')
        random_capitals = []
        for capital_pair in random_capitals_str[2:-2].split("), ("):
            random_capitals.append(tuple(capital_pair.split(", ")))
        print("Got random_capitals from request.args")

    if 'correct_answer' in request.args:
        correct_answer = request.args['correct_answer']
        print("Got correct_answer from request.args")

    print(f"thecountry: {thecountry}")
    print(f"thecapital: {thecapital}")
    print(f"random_capitals: {random_capitals}")
    print(f"correct_answer: {correct_answer}")
    print(f"counter: {counter}")
    print("-----------------")
    print("here")
    

    class PopQuizTest(Form):
        class Meta:
            csrf = False
            
        q1 = RadioField(
                f"The capital of {thecountry} is ...",
                choices=random_capitals,
                validators=[CorrectAnswer(thecapital)]
            )

    form = PopQuizTest()
    answer = str(form.q1.validators[0].answer)
    counter += 1
    # print("Country: ", thecountry)
    # print("Capital: ", thecapital)
    # print(f"Answer: {answer}")

    if form.is_submitted():
        print("Submitted!")

    if form.validate():
        print("Valid!")

    if form.validate_on_submit(): 
        print("CORRECT ANSWER!")
        countries_guessed.append(thecountry)
        correct_counter += 1
        percent_counter = (correct_counter/question_counter) * 100
        #time.sleep(2)
        #return redirect(url_for('passed')) 
    elif form.is_submitted():
            if form.errors[next(iter(form.errors))][0] == 'Incorrect answer.':
                print("WRONG ANSWER!")
                question_counter += 1
                percent_counter = (correct_counter/question_counter) * 100
                incorrect_answers.append({
                    "thecountry": thecountry,
                    "thecapital": thecapital,
                    "random_capitals": random_capitals,
                    "correct_answer": correct_answer,
                    "run_min": (counter+1)+4 # +1 so it counts at the next round
                    })
                print(f"Added {thecountry} to incorrect answers.")
                
            else:
                print("form.errors: ", form.errors)
    if form.is_submitted():
        time.sleep(2)
        if percent_counter >= 100:
            return redirect(url_for('passed'))
        if incorrect_answers != []:
            redo_chance = bool(random.getrandbits(1))
            if redo_chance or counter/question_counter == 1:
                print("Redo chance!")
                if incorrect_answers[0]['run_min'] <= counter:
                    print("Run min reached!")
                    thecountry = incorrect_answers[0]['thecountry']
                    thecapital = incorrect_answers[0]['thecapital']
                    random_capitals = incorrect_answers[0]['random_capitals']
                    correct_answer = incorrect_answers[0]['correct_answer']
                    incorrect_answers.pop(0)
                    print(f"Removed {thecountry} from incorrect answers.")

                    add_to_session(
                        thecountry,
                        thecapital, 
                        random_capitals, 
                        correct_answer, 
                        incorrect_answers,
                        countries_guessed,
                        counter,
                        correct_counter,
                        question_counter,
                        percent_counter,
                        percent_increase
                        )

                    return redirect(url_for('wtf_quiz'), code=307)
                else:
                    print("Run min not reached, cancel redo chance.")

        thecountry, thecapital, random_capitals, correct_answer = random_quiz()
        if thecountry in countries_guessed:
            print("Country already guessed, redoing...")
            thecountry, thecapital, random_capitals, correct_answer = random_quiz()

        print(f"NEW CAPITAL: {thecapital}")

        add_to_session(
            thecountry,
            thecapital, 
            random_capitals, 
            correct_answer, 
            incorrect_answers,
            countries_guessed,
            counter,
            correct_counter,
            question_counter,
            percent_counter,
            percent_increase
            )
        print(f"random_capitals: {random_capitals}")
        return redirect(url_for('wtf_quiz', thecountry=thecountry, thecapital=thecapital, random_capitals=str(random_capitals), correct_answer=correct_answer, counter=counter))



    return render_template('quiz.html', 
        form=form, 
        question=form.q1,
        answer=answer, 
        percent_counter=percent_counter, 
        # counter=counter, 
        percent_increase=percent_increase, 
        question_counter=question_counter,
        correct_counter=correct_counter,
        )


@app.route('/passed')
def passed(): 
    return render_template('passed.html')


if __name__ == '__main__':
    print("Starting app...")
    app.secret_key = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.run(debug=True)
    # If error with no access: go to chrome://net-internals/#sockets and flush sockets
