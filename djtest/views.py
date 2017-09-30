from django.views.generic import View
from django.shortcuts import render

from djtest.models import Customer

class CustomersListView(View):
    def get(self, request):
        return render(request, 'customers_list.html', {
            'customers': Customer.objects.all(),
        })

