from django.conf.urls import url
from django.contrib import admin

from djtest.views import CustomersListView, CustomerEditView

urlpatterns = [
    url(r'^customers/$', CustomersListView.as_view(), name='customers_list'),
    url(r'^customers/(?P<customer_id>\d+)/$', CustomerEditView.as_view(), name='customers_edit'),
    url(r'^admin/', admin.site.urls),
]
