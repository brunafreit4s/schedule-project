from typing import Any
from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import render, get_object_or_404
from contact.forms import ContactForm

# Create your forms here.
def create(request):
    if request.method == 'POST':
        context = { 'form': ContactForm(request.POST) }

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = { 'form': ContactForm() }
    return render(
        request,
        'contact/create.html',
        context,
    )

def update(request, contact_id):
    #single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id).first())
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    contact_name = f'{ single_contact.first_name } { single_contact.last_name }'
    context = {'contact': single_contact, 'site_title': contact_name}
    
    return render(
        request,
        'contact/contact.html',
        context,
    )

def delete(request, contact_id):
    #single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id).first())
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    contact_name = f'{ single_contact.first_name } { single_contact.last_name }'
    context = {'contact': single_contact, 'site_title': contact_name}
    
    return render(
        request,
        'contact/contact.html',
        context,
    )
