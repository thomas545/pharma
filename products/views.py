from django.shortcuts import render
from django.db.models import Q
from .models import Category, Product, SKU


def all_categories(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(
        request,
        "products.html",
        context={"categories": categories, "products": products},
    )


def category_products(request, pk):
    categories = Category.objects.filter(pk=pk)
    products = Product.objects.filter(category_id=pk)
    return render(
        request,
        "products.html",
        context={"categories": categories, "products": products},
    )


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    related_products = Product.objects.filter(category=product.category).exclude(
        pk=product.pk
    )

    return render(
        request,
        "product_detail.html",
        context={"product": product, "related_products": related_products},
    )


def check_product(request):
    qs = SKU.objects.all()
    message = ""
    product = None
    serial = request.GET.get("serial", None)

    if serial != "" and serial is not None:
        new_qs = qs.filter(Q(serial_number__iexact=serial))
        if new_qs:
            message = "Your Product Is Correct"
            product = new_qs.first().product
        else:
            message = "wrong"

    context = {
        "queryset": qs,
        "product": product,
        "serial": serial,
        "message": message,
    }
    return render(request , "check.html", context)
