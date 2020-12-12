from django import forms
import requests

class TicketForm(forms.Form):
    category_choices = (('cat1', 'Cat1'), ('cat1', 'Cat2'), ('cat3', 'Cat3'))
    priority_choices = (('low', 'Low - General Guidance'), ('medium', 'Medium - System Impaired'),
                        ('high', 'High - Production System Down'))

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        # from the department API call get the department data dynamically
        headers = {'orgId': 'orgId', 'Authorization': 'Zoho-oauthtoken'}
        response = requests.get('https://desk.zoho.com/api/v1/departments', headers=headers)
        dep_choices = [(dep[id],dep['name']) for dep in response.data()]
        # dep_choices = (('current', 'Current'), ('expired', 'Expired'), ('upcoming', 'Upcoming'))
        self.fields['department'].choices = dep_choices

    subject=forms.CharField()
    description=forms.CharField()
    department=forms.ChoiceField()
    category=forms.ChoiceField(choices=category_choices)
    priority=forms.ChoiceField(choices=priority_choices)