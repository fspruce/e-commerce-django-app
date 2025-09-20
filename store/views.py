from django.shortcuts import render
from dal_select2.views import Select2QuerySetView
from .models import Tag

# Create your views here.


def index(request):
    return render(request, "store/index.html")


class TagAutocomplete(Select2QuerySetView):
    create_field = "name"

    def get_queryset(self):
        # Only allow authenticated users to use the autocomplete
        if not self.request.user.is_authenticated:
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            # Filter the queryset bvased o nthe search term 'self.q'
            qs = qs.filter(name__icontains=self.q)

        return qs
