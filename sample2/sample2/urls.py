from django.contrib import admin
from django.urls import path
from sell.views import (
    CreateChekoutSessionView,
    ProductLandingPageView,
    SuccessView,
    CancelView,
)                    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductLandingPageView.as_view(), name="base-page"),
    path('create-checkout-session/<pk>/', CreateChekoutSessionView.as_view(), name='create-checkout-session'),
]
