from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method == "POST":

        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(request.POST["product_id"])
        
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        context = {
            "total_charge": total_charge,
            "quantity_ordered": quantity_from_form,
            "product_price": price_from_form,
        }
    return render(request, "store/checkout.html" , context)

def success(request):
    if request.method == "POST":
       description=request.POST['description'] 
       price=request.POST['price']
       Product.objects.create(description=description, price=price)
       price_float=float(price)
       context = {
            "description": description,
            "price": price_float,
        }
      
    return render(request, "store/success.html",context)







