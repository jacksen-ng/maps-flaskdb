# forms.py - defines form formats and its restrictions on flaskdb
# Copyright (C) 2024 Yasuhiro Hayashi

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length
from flaskdb.widgets import *

from flaskdb.widgets import ButtonField

class UserForm(FlaskForm):
    username = StringField(
        "User Name",
        validators = [
            DataRequired(message="ユーザ名は必須です。"),
            length(max=64, message="64文字以内で入力してください。"),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = ButtonField("Submit")

    def copy_from(self, user):
        self.username.data = user.username

    def copy_to(self, user):
        user.username = self.username.data
