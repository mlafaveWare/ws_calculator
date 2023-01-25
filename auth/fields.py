from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms.fields import Field, CharField
from django.forms.widgets import TextInput

class EmailHandler(CharField):
    widget = TextInput
    default_validators = []
    default_error_messages = {
        'required': 'Default Required Error Message',
        'email': 'please enter a valid email address or multiple addresses separated by commas'
    }

    def to_python(self, value):
        if not value:
            return []
        value = value.replace(' ', '')
        return value.split(',')

    def validate(self, value):
        super().validate(value)
        for email in value:
            try:
                validate_email(email)
            except ValidationError:
                raise ValidationError(
                    self.error_messages['email'],
                    code = 'email'
                )