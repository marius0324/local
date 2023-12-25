from django.urls import path
from . import views
from .views import BBLogoutView, CreateProduct
from .views import BBLoginView
from .views import register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.home, name='home'),
                  path('services/', views.ListProduct.as_view(), name='services'),
                  path('about/', views.about, name='about'),
                  path('contact/', views.contact, name='contact'),
                  path('add_service/', CreateProduct.as_view(), name='add_service'),
                  path('accounts/login/', BBLoginView.as_view(), name='login'),
                  path('accounts/register/', register, name='register'),
                  path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)