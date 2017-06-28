from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Reviews
from django.views.generic.edit import CreateView


class ReviewsView(generic.ListView):  # представление в виде списка
    template_name = 'reviews/reviews.html'
    context_object_name = 'latest_reviews_list'

    def get_queryset(self):
        """Return the last ten published."""
        return Reviews.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class ReviewsCreate(CreateView):
    model = Reviews
    template_name = 'reviews/reviews.html'
    fields = ['customer', 'review_text']
    success_url = reverse_lazy('reviews:reviews')
