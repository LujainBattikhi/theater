from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, ButtonHolder, HTML
from django import forms
from django.utils.translation import gettext_lazy as _


class MessageForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    body = forms.CharField(widget=forms.Textarea(), required=True)

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-md-6"),
                Div('email', css_class="col-md-6"),
                Div('subject', css_class="col-md-12"),
                Div('body', css_class="col-md-12"),
                ButtonHolder(
                    HTML('asd'),
                    Submit(_('Send'), 'Send'),

                ),
                css_class="row"
            ),
        )
