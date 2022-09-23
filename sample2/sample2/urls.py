from django.contrib import admin
from django.urls import path
from sell.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
    SuccessView,
    CancelView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', ProductLandingPageView.as_view(), name="base-page"),
    path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]
