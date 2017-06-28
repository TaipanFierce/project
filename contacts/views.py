from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Contacts


class ContactsView(generic.ListView):
    model = Contacts
    template_name = 'contacts/contacts.html'