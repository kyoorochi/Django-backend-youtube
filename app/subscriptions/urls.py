from django.urls import path
from . import views

# api/v1/sub
urlpatterns = [
    path('', views.SubscriptionList.as_view(), name='sub-list'),
    path('<int:pk>', views.SubscriptionDetail.as_view(), name='sub-detail') #api/vi/sub/{pk}
]