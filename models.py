from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Category')
    image = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name='image')
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               verbose_name='Category',
                               related_name='subcategories')

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return 'https://i.pinimg.com/474x/0e/42/3a/0e423a132937a10630cb227b4229145a.jpg'

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Category: pk={self.pk}, title={self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Product name')
    price = models.FloatField(verbose_name='price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    quantity = models.IntegerField(default=0, verbose_name='quantity')
    description = models.TextField(default='Soon...', verbose_name='content')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', related_name='products')
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=30, verbose_name='size (mm)')
    color = models.CharField(max_length=40, default='Silver', verbose_name='color/material')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return 'https://i.pinimg.com/474x/0e/42/3a/0e423a132937a10630cb227b4229145a.jpg'
        else:
            return 'https://i.pinimg.com/474x/0e/42/3a/0e423a132937a10630cb227b4229145a.jpg'

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Product: pk{self.pk}, title{self.title}, price{self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Gallery(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Photo')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Review(models.Model):
    text = models.TextField(verbose_name='Comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class FavouriteProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Favourite product'
        verbose_name_plural = 'Favourite products'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    first_name = models.CharField(max_length=255, verbose_name='Name customer', default='')
    last_name = models.CharField(max_length=255, verbose_name='Last name customer', default='')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data of order')
    shipping = models.BooleanField(default=True, verbose_name='Shipping')

    def __str__(self):
        return str(self.pk) + ' '

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        total_price = sum([product.get_total_price for product in order_products])
        return total_price

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        total_quantity = sum([product.quantity for product in order_products])
        return total_quantity


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Product")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name='Order')
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Quantity")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order product'
        verbose_name_plural = 'Orders products'

    @property
    def get_total_price(self):
        total_price = self.product.price * self.quantity
        return total_price


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    region = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Shipping address'
        verbose_name_plural = 'Shipping addresses'
