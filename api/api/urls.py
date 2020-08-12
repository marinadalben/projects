from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import EmployeeCreateView, EmployeeDetail
from django.contrib import admin

urlpatterns = {
    url(r'^admin/', admin.site.urls),
    url(r'^employee/$', EmployeeCreateView.as_view(), name='add'),
    url(r'^employee/$', EmployeeCreateView.as_view(), name='list'),
    url(r'^employee/(?P<pk>[0-9]+)/$', EmployeeDetail.as_view(), name='remove'),
}

urlpatterns = format_suffix_patterns(urlpatterns)