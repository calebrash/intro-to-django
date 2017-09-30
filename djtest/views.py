from django.views.generic import View
from django.shortcuts import render

from djtest.models import Customer
from djtest.forms import CustomerEditForm

class CustomersListView(View):
    def get(self, request):
        return render(request, 'customers_list.html', {
            'customers': Customer.objects.all(),
        })

class CustomerEditView(View):

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        form = CustomerEditForm(instance=customer)

        return render(request, 'customers_edit.html', {
            'customer': customer,
            'form': form,
        })

    def post(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        form = CustomerEditForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()

        return render(request, 'customers_edit.html', {
            'customer': customer,
            'form': form,
        })

