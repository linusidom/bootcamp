from django.shortcuts import render
from orders.models import Order
# Create your views here.
def order_history(request):
	orders = Order.objects.filter(billing_profile__user=request.user)
	print(orders)
	context = {
		'orders': orders
	}
	return render(request, 'orders/order_history.html', context)
