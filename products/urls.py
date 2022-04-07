from django.urls import path
from . import views


urlpatterns = [
    path("categories/", views.all_categories, name="products"),
    path("category-products/<int:pk>/", views.category_products, name="category_products"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("check/", views.check_product, name="check_code"),
]
