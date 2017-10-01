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
        """
        Handle GET requests in the `get` handler. `customer_id` comes from the url regexp in
        urls.py.
        """
        customer = Customer.objects.get(id=customer_id)
        form = CustomerEditForm(instance=customer)

        return render(request, 'customers_edit.html', {
            'customer': customer,
            'form': form,
        })

    def post(self, request, customer_id):
        """
        Handle POST requests in the `post` handler. In this function, we pass the POST object to
        the form to validate and save our udpated model. If the form is invalid, validations
        errors will appear in the form.
        """
        customer = Customer.objects.get(id=customer_id)
        form = CustomerEditForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()

        return render(request, 'customers_edit.html', {
            'customer': customer,
            'form': form,
        })

