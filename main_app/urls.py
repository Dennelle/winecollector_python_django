from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wines/', views.wines_index, name="index"),
    path('wines/<int:wine_id>/', views.wines_detail, name='detail'),
    # CBVs Class based views
    path('wines/create', views.WineCreate.as_view(), name='wines_create'),
    path('wines/<int:pk>/update/', views.WineUpdate.as_view(), name='wines_update'),
    path('wines/<int:pk>/delete/', views.WineDelete.as_view(), name='wines_delete'),
    path('wines/<int:wine_id>/add_drinking',views.add_drinking, name='add_drinking'),
    path('wines/<int:wine_id>/assoc_country/<int:country_id>', views.assoc_country, name='assoc_country'),
    path('countries/', views.CountryList.as_view(), name='countries_index'),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name='countries_detail'),
    path('countries/create/', views.CountryCreate.as_view(), name='countries_create'),
    path('countries/<int:pk>/update/', views.CountryUpdate.as_view(), name='countries_update'),
    path('countries/<int:pk>delete/', views.CountryDelete.as_view(), name='countries_delete'),
]
