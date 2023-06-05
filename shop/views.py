from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from artisan.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Category,OrderProduct,Order, ShippingAddress
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from artisan.models import Product


# Create your views here.
def shop(request):
    context = {
        'products': Product.objects.all()
    }
    print("Welcome to the shop", context)
    return render(request, 'shop_index.html', context)

def product(request, category_slug , product_id):
    recent_products = Product.objects.all().order_by('-date')[:4]
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'recent_products': recent_products
    }
    return render(request, 'shop_index.html', context)
class StoreCart(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(customer=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'store_cart.html', context)
        except ObjectDoesNotExist:
            return redirect("store")


# TODO: redirect to cart page or update cart counter
@login_required
def add_to_cart(request, slug): 
    product = get_object_or_404(Product, slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        customer=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(customer=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            # messages.info(request, "This item quantity was updated.")
            # return render(request,"shop_index.html",{'product':product})
            return redirect("store_cart")
        else:
            order.products.add(order_product)
            # messages.info(request, "This item was added to your cart.")
            return redirect("store_cart")
    else:
        
        order = Order.objects.create(customer=request.user)
        order.products.add(order_product)
        # messages.info(request, "This item was added to your cart.")
        return redirect("store_cart")


@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        customer=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                customer=request.user,
                ordered=False
            )[0]
            order.products.remove(order_product)
            order_product.delete()
            # messages.info(request, "This item was removed from your cart.")
            return redirect("store_cart")
        else:
            # messages.info(request, "This item was not in your cart")
            return redirect('store_cart')
    else:
        # messages.info(request, "You do not have an active order")
        return redirect("store_cart")


@login_required
def store_cart(request):
    try:
        order = Order.objects.get(customer=request.user, ordered=False)
        context = {
            'object': order
        }
        return render(request, 'shop_cart.html', context)
    
    except ObjectDoesNotExist:
        # messages.error(request, "You do not have an active order")
        return redirect("store_cart")


@login_required
def order_success(request):
    return render(request, 'order_success.html')

@login_required
def checkout(request):
    if request.method == "POST":
        # checkout logic
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        print(address, city, state, zip_code)

        checkout_address = ShippingAddress(
            address=address,
            city=city,
            state=state,
            zip_code=zip_code
        )

        checkout_address.save()
        order = Order.objects.get(customer=request.user, ordered=False)
        order.shipping_address = checkout_address
        order.ordered = True
        order.save()

        return render(request, 'order_success.html')


    else:
        try:
            order = Order.objects.get(customer=request.user, ordered=False)
            context = {
                'object': order
            }
            return render(request, 'shop_checkout.html', context)
        except ObjectDoesNotExist:
            # messages.error(request, "You do not have an active order")
            return redirect("shop")