from django.shortcuts import render, get_object_or_404
from django.views import generic
from dal_select2.views import Select2QuerySetView
from .models import Product, Tag

# Create your views here.


def index(request):
    return render(request, "store/index.html")


class ProductList(generic.ListView):
    queryset = Product.objects.filter(published=True)
    template_name = "store/index.html"
    paginate_by = 6
    context_object_name = "product_list"


def product_detail(request, slug):
    queryset = Product.objects.filter(published=True)
    product = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "store/product_detail.html",
        {
            "product": product,
        },
    )


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
