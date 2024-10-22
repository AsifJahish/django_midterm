from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.views.generic import TemplateView
from .models import Category

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class SellerProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product
    template_name = 'products/seller_product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def test_func(self):
        return hasattr(self.request.user, 'seller')

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user.seller)

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('seller_products')

    def test_func(self):
        return hasattr(self.request.user, 'seller')

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        form.instance.slug = slugify(form.instance.name)
        messages.success(self.request, 'Product created successfully!')
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('seller_products')

    def test_func(self):
        product = self.get_object()
        return self.request.user.seller == product.seller

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        messages.success(self.request, 'Product updated successfully!')
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('seller_products')

    def test_func(self):
        product = self.get_object()
        return self.request.user.seller == product.seller


class HomeView(TemplateView):
    template_name = 'homep.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Make sure you're passing categories to the template
        return context