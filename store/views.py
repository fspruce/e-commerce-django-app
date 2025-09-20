from django.shortcuts import render
from django.http import HttpResponse
from dal_select2.views import Select2QuerySetView
from .models import Tag

# Create your views here.


def home_page_view(request):
    return HttpResponse("<h1>Hello, World!</h1>")


class TagAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # Only allow authenticated users to use the autocomplete
        if not self.request.user.is_authenticated:
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            # Filter the queryset bvased o nthe search term 'self.q'
            qs = qs.filter(name__icontains=self.q)

        return qs
