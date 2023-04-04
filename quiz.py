from flask_wtf import FlaskForm as Form
from wtforms import RadioField
from wtforms.validators import ValidationError


class CorrectAnswer(object):
    def __init__(self, answer):
        self.answer = answer

    def __call__(self, form, field):
        message = 'Incorrect answer.'

        if field.data != self.answer:
            raise ValidationError(message)

"""class PopQuiz(Form):
    class Meta:
        csrf = False

    def __init__(self, *, question_label:str, choices:list, answer:str, **kwargs):
        self.question_label = question_label
        self.choices = choices
        self.answer = answer
        super().__init__(**kwargs,)

    @property
    def q1(self):
        return RadioField(
            self.question_label,
            choices=self.choices,
            validators=[CorrectAnswer(self.answer)]
        )
"""


class PopQuiz(Form):
    class Meta:
        csrf = False

    question_label:str = ...
    choices:list = [(..., ...), (...,...)]
    answer:str = ...
        

    q1 = RadioField(
            question_label,
            choices=choices,
            validators=[CorrectAnswer(answer)]
        )

class PopQuiz(Form):
    class Meta:
        csrf = False

    q1 = RadioField(
        "The answer to question one is False.",
        choices=[('True', 'True'), ('False', 'False')],
        validators=[CorrectAnswer('False')]
    )