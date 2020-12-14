from django.shortcuts import render, HttpResponse
import requests
from .forms import TicketForm

# Create your views here.
def home_view(request):
    headers = {'orgId':'orgId','Authorization': 'Zoho-oauthtoken'}
    response = requests.get('https://desk.zoho.com/api/v1/tickets', headers=headers)
    ticket_data = response.json()
    return render(request, 'ticket_list.html', {'ticket_data': ticket_data})

def ticketform_view(request):
    headers = {'orgId':'orgId','Authorization': 'Zoho-oauthtoken'}
    if request.method=="GET":
        form=TicketForm()
        return render(request,'create_ticket_form.html',{'form':form})
    if request.method=="POST":
        form=TicketForm(request.POST)
        if form.is_valid():
            print("form",form)
            data=form.data()
            data['contact_id']={
                'first_name': request.GET['first_name'],
                'last_name': request.GET['last_name'],
                'email': request.GET['email']
            }
            json_data=data.json()
            response = requests.post('https://desk.zoho.com/api/v1/tickets', data=json_data, headers=headers)
            return HttpResponse("Form Submitted")