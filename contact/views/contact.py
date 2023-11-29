from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

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

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects.all()\
        .filter(show=True)\
        .filter(Q(first_name__icontains=search_value) | 
                Q(last_name__icontains=search_value)
            )[0:50]
    
    context = {'contacts': contacts, 'site_title': 'Contatos'}
    
    return render(
        request,
        'contact/index.html',
        context,        
    )