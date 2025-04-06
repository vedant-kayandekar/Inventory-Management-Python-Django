from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product , Order
from .forms import ProductForm ,UpdateProductForm, OrderAdd
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required(login_url='user-login')
def index(request):
    orders =  Order.objects.all()
    products =  Product.objects.all()
    total_staff = User.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    
    if request.method =='POST':
       ordering = OrderAdd(request.POST)
       if ordering.is_valid():
           instance = ordering.save(commit=False)
           instance.staff = request.user
           instance.comment = 'hel'
           instance.save()
           return redirect('dashboard-index')
    else:
        ordering = OrderAdd()    
    context = {
        'orders':orders,
        'ordering':ordering,
        'total_staff':total_staff,
        'total_products':total_products,
        'total_orders':total_orders,
        'products': products,
        
    }
    return render(request, 'dashboard/index.html',context)

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

# @login_required(login_url='user-login')
# def product(request):
#     items = Product.objects.all()


#     if request.method == 'POST':
#         add_product_form = ProductForm(request.POST)
#         if add_product_form.is_valid():
#             add_product_form.save()
#             product_name = add_product_form.cleaned_data.get('name')
#             messages.success(request, f'{product_name} has been added successfully')
#             return redirect('dashboard-product')
#     else:
#         add_product_form = ProductForm()


#     context = {
#         'items': items,
#         'add_product_form': add_product_form,
#     }
#     return render(request, 'dashboard/product.html', context)


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()

    if request.method == 'POST':
        add_product_form = ProductForm(request.POST)
        if add_product_form.is_valid():
            product_name = add_product_form.cleaned_data.get('name')
            # Check if the product with the same name already exists
            if not Product.objects.filter(name__iexact=product_name).exists():
                add_product_form.save()
                messages.success(request, f'{product_name} has been added successfully')
            else:
                messages.warning(request, f'{product_name} already exists')
            return redirect('dashboard-product')
    else:
        add_product_form = ProductForm()

    context = {
        'items': items,
        'add_product_form': add_product_form,
    }
    return render(request, 'dashboard/product.html', context)






@login_required(login_url='user-login')
def product_delete(request,pk):
    item = Product.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

@login_required(login_url='user-login')
def product_update(request,pk):
    item = Product.objects.get(id=pk)

    if request.method == 'POST':
        update = UpdateProductForm(request.POST, instance=item)
        if update.is_valid():
            update.save()
            return redirect('dashboard-product')
    else:
        update = UpdateProductForm(instance=item)

    context = {
        'update': update
         }
        
    return render(request,'dashboard/product_update.html',context )

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()

    context = {
        'workers': workers
    }

    return render(request, 'dashboard/staff.html', context)
    

def staff_detail(request,pk):
    staff_workers = User.objects.get(id=pk)
    context = {
        'staff_workers': staff_workers
    }
    return render(request,'dashboard/staff_detail.html', context)

@login_required(login_url='user-login')
def order(request):
    all_orders =  Order.objects.all()

    if request.method == 'Post':
        ordering = OrderAdd(request.Post)
        if ordering.is_valid():
            ordering.save()
        else:
            ordering = OrderAdd(instance=id)
        
    context = {
        'all_orders': all_orders,
        # 'ordering': ordering,
    }

    return render(request, 'dashboard/order.html', context)




@login_required(login_url='user-login')
def staff_index(request):

    if request.method == 'Post':
        ordering = OrderAdd(request.Post)
        if ordering.is_valid():
            ordering.save()
        else:
            ordering = OrderAdd(instance=id)
        
    # context = {
    #    'ordering': ordering,
    # }

    # return render(request, 'dashboard/index.html', context)
    pass
