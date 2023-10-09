from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'core'

urlpatterns = [
    # Home page
    path('', HomeView.as_view(), name='home'),

    # Checkout page
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    # Order summary page
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),

    # Product detail page (uses a slug)
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),

    # Add an item to the cart
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),

    # Add a coupon to the cart
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),

    # Remove an item from the cart
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),

    # Remove a single item from the cart
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),

    # Payment page with payment_option parameter (e.g., stripe or paypal)
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),

    # Request a refund page
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
