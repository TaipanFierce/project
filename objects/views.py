from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.utils import timezone

from .models import Objects


class ObjectsView(generic.ListView):
    model = Objects
    template_name = 'objects/objects.html'

