from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, Field
from django import forms
from landingpage.models import LandingPageForm


class SignUpForm(forms.ModelForm):
    class Meta:
        model = LandingPageForm

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Field('name', placeholder='Name', css_class='span10', template='landingpage/no-label.html'),
            Field('organization', placeholder='Organization', css_class='span10', template='landingpage/no-label.html'),
            Field('email', placeholder='Email Address', css_class='span10', template='landingpage/no-label.html'),
            Submit('submit','Get in touch')
        )

        super(SignUpForm, self).__init__(*args, **kwargs)

class EmailForm(forms.Form):
    emails = forms.CharField()