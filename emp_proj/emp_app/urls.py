from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('all_emp',views.all, name='all'),
    path('add_emp',views.add, name='add'),
    path('remove_emp',views.remove, name='remove'),
    path('remove_emp/<int:emp_id>',views.remove, name='remove_id'),
    path('filter_emp',views.filter, name='filter')
]
