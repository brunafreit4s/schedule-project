from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    contacts = Contact.objects.all().filter(show=True)    
    context = {'contacts': contacts, 'site_title': 'Contatos'}
    #print(contacts.query)
    
    return render(
        request,
        'contact/index.html',
        context,
    )

# Create your views here.
def contact(request, contact_id):
    #single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id).first())
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    contact_name = f'{ single_contact.first_name } { single_contact.last_name }'
    context = {'contact': single_contact, 'site_title': contact_name}
    
    return render(
        request,
        'contact/contact.html',
        context,
    )