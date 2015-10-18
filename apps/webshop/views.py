# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView, RedirectView
from apps.webshop.models import Category, Product, Order, OrderLine
from apps.webshop.forms import OrderForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class CartMixin(LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super(CartMixin, self).get_context_data(**kwargs)
        context['order_line'] = self.current_order_line()
        return context

    def current_order_line(self):
        order_line = OrderLine.objects.filter(user=self.request.user, paid=False).first()
        if not order_line:
            order_line = OrderLine.objects.create(user=self.request.user)
        return order_line


class Home(CartMixin, TemplateView):
    template_name = 'webshop/base.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryDetail(CartMixin, DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'webshop/category.html'


class ProductDetail(CartMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'webshop/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['orderform'] = OrderForm
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = OrderForm(request.POST)
        if form.is_valid():
            order_line = self.current_order_line()
            # Checking if product has already been added to cart
            order = order_line.orders.filter(product=product).first()
            if order:
                # Adding to existing order
                order.quantity += form.cleaned_data['quantity']
                messages.info(
                    request,
                    'Produktet \'{product}\' var allerede i handlekurven din. Antall har blitt oppdatert til {quantity}.'
                    .format(product=product, quantity=order.quantity)
                )
            else:
                # Creating new order
                order = Order(
                    product=product, price=product.price,
                    quantity=form.cleaned_data['quantity'],
                    order_line=order_line)
                messages.success(
                    request,
                    '\'{product}\' x {quantity} har blitt lagt til i handlekurven.'
                    .format(product=product, quantity=order.quantity)
                )
            order.save()
        else:
            messages.error(request, 'Vennligst oppgi et gyldig antall')
        return super(ProductDetail, self).get(request, *args, **kwargs)


class Checkout(CartMixin, TemplateView):
    template_name = 'webshop/checkout.html'

    def post(self, request, *args, **kwargs):
        order_line = self.current_order_line()
        if order_line.count_orders() > 0:
            order_line.pay()
            messages.success(request, 'Kjøp fullført!')
        else:
            messages.error(request, 'Ingen varer valgt')
        return super(Checkout, self).get(request, *args, **kwargs)


class RemoveOrder(CartMixin, RedirectView):
    pattern_name = 'webshop_checkout'

    def post(self, request, *args, **kwargs):
        order_line = self.current_order_line()
        order_id = request.POST.get('id')
        if order_id:
            Order.objects.filter(order_line=order_line, id=order_id).delete()
        else:
            Order.objects.filter(order_line=order_line).delete()
        return super(RemoveOrder, self).post(request, *args, **kwargs)
