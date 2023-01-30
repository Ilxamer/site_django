from django.urls import path, include
from . import views

urlpatterns = [
	path('category/<int:id_cat>',views.category, name='Category'),
	path('info',views.info, name = 'Info'),
	path('main', views.main, name = 'main'),
	path('product/<int:id_prod>',views.product, name = 'Product'),
	path('contact', views.contact, name = 'Contact'),
]
