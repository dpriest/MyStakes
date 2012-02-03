from config import settings
from web import form

number_form = form.Form(
        form.Textbox('number',
            form.notnull,
            form.regexp('^-?\d+$', 'Not a number.'),
            form.Validator('Not greater 10.', lambda x: int(x)>10),
            description='Enter a number greater 10:'))


class signin:

    def GET(self):
        my_form = number_form()
        return settings.render.signin(my_form)

    def POST(self):
        my_form = number_form()
        if not my_form.validates():
            return settings.render.signin(my_form)
        else:
            number = my_form['number'].value
            if int(number) % 2:
                return "odd"
            else:
                return "even"
