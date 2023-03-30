
from flask import Flask, render_template, redirect, url_for, request
import time, random, countries, os, json, sqlite3, requests

from quiz_base import CorrectAnswer
from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from datetime import datetime

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
from user import User

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "719501886935-d5j4qtigtm929l1e43oh8mk8fa3l8973.apps.googleusercontent.com")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "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")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

app = Flask(__name__)
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403


# # Naive database setup
# try:
#     import db
#     from user import User
#     db.init_db_command()
# except sqlite3.OperationalError:
#     # Assume it's already been created
#     pass

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# OAuth2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



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

@app.route("/index")
def index():
    if current_user.is_authenticated:
        return (
            f"""<p>Hello, {current_user.name}! You're logged in! Email: {current_user.email}</p>
            <div><p>Google Profile Picture:</p>
            <img src="{current_user.profile_pic}" alt="Google profile pic"></img></div>
            <a class="button" href="/logout">Logout</a>
            <a class="button" href="/quiz">Start Quiz</a>

            """
        )
    else:
        return '''
        <div class="row">
  <div class="col-md-3">
    <a class="btn btn-outline-dark" href="/login" role="button" style="text-transform:none">
      <img width="20px" style="margin-bottom:3px; margin-right:5px" alt="Google sign-in" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/512px-Google_%22G%22_Logo.svg.png" />
      Login with Google
    </a>
  </div>
</div>
<!-- Minified CSS and JS -->
<link   rel="stylesheet" 
        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
        crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" 
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" 
        crossorigin="anonymous">
</script>'''


@app.route('/', methods=['GET', 'POST'])
def wtf_quiz(): 
    global incorrect_answers, counter, percent_counter, percent_increase, correct_counter, question_counter, countries_guessed, thecountry, thecapital, random_capitals, correct_answer
    if counter != 0:
        pass
        #thecountry, thecapital, random_capitals, correct_answer, incorrect_answers, countries_guessed, fake_counter, correct_counter, question_counter, percent_counter, percent_increase = get_from_session()

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
    # print("Country: ", thecountry)
    # print("Capital: ", thecapital)
    # print(f"Answer: {answer}")

    if form.is_submitted():
        print("Submitted!")
        counter += 1

    if form.validate():
        print("Valid!")

    if form.validate_on_submit(): 
        print("CORRECT ANSWER!")
        countries_guessed.append(thecountry)
        correct_counter += 1
        percent_counter = (correct_counter/question_counter) * 100
 
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
            print(question_counter)
            print(counter/question_counter)
            if redo_chance or counter/question_counter == 1:
                print("Redo chance!")
                if incorrect_answers[0]['run_min'] <= counter or counter/question_counter == 1:
                    print("Run min reached!")
                    thecountry = incorrect_answers[0]['thecountry']
                    thecapital = incorrect_answers[0]['thecapital']
                    random_capitals = incorrect_answers[0]['random_capitals']
                    correct_answer = incorrect_answers[0]['correct_answer']
                    incorrect_answers.pop(0)
                    print(f"Removed {thecountry} from incorrect answers.")

                    return redirect(url_for('wtf_quiz'))
                else:
                    print("Run min not reached, cancel redo chance.")

        thecountry, thecapital, random_capitals, correct_answer = random_quiz()
        if thecountry in countries_guessed:
            print("Country already guessed, redoing...")
            thecountry, thecapital, random_capitals, correct_answer = random_quiz()

        print(f"NEW CAPITAL: {thecapital}")

        print(f"random_capitals: {random_capitals}")
        return redirect(url_for('wtf_quiz'))



    return render_template('quiz.html', 
        form=form, 
        question=form.q1,
        answer=answer, 
        percent_counter=percent_counter, 
        counter=counter, 
        percent_increase=percent_increase, 
        question_counter=question_counter,
        correct_counter=correct_counter,
        )


@app.route('/passed')
def passed(): 
    global counter, percent_counter, percent_increase, correct_counter, question_counter, countries_guessed, thecountry, thecapital, random_capitals, correct_answer, incorrect_answers
    thescore = round((5/question_counter)*100, 2)

    if current_user.is_authenticated:
        print("User is authenticated.")
        user = User.get_from_email(current_user.email)
        user.games.save_new_game(user.id, datetime.now().timestamp, thescore)
        print("Game saved.")
        user.stats.update_stats(user.id, thescore, True if thescore == 100 else False)
        print("Stats updated.")


    return render_template('passed.html')

@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in our db with the information provided
    # by Google
    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    # Doesn't exist? Add to database
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in
    print("Logging in user %s" % users_name)
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


if __name__ == '__main__':
    print("Starting app...")
    app.secret_key = os.urandom(24)
    app.run(debug=True, ssl_context=("certificate.crt", "privateKey.key"))
    # If error with no access: go to chrome://net-internals/#sockets and flush sockets
