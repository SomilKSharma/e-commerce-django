# Import necessary modules and models
from django import template
from core.models import Order

# Create a template library instance
register = template.Library()

# Define a custom template filter called 'cart_item_count'
@register.filter
def cart_item_count(user):
    # Check if the user is authenticated
    if user.is_authenticated:
        # Query the Order model to get all orders for the user that are not yet 'ordered'
        qs = Order.objects.filter(user=user, ordered=False)

        # Check if there are any uncompleted orders
        if qs.exists():
            # Return the count of items in the first uncompleted order
            return qs[0].items.count()

    # Return 0 if the user is not authenticated or has no uncompleted orders
    return 0
