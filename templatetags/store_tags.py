from django import template
from store.models import Category, FavouriteProducts


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=True)


@register.simple_tag()
def get_categories_page():
    return Category.objects.filter(parent=None)


@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)


@register.simple_tag()
def get_sorted():
    sorters = [
        {
            'title': 'Price',
            'sorters': [
                ('price', 'minus'),
                ('-price', 'plus'),
            ]
        },
        {
            'title': 'Color',
            'sorters': [
                ('color', 'A - Z'),
                ('-color', 'Z - A'),
            ]
        },
        {
            'title': 'Size',
            'sorters': [
                ('size', 'minus'),
                ('-size', 'plus'),
            ]
        }
    ]
    return sorters


@register.simple_tag()
def get_favourite_products(user):
    fav = FavouriteProducts.objects.filter(user=user)
    products = [i.product for i in fav]
    print(f'Favourite products {products}')
    return products
