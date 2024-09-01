from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .apps import AccountsConfig

app_name = AccountsConfig.name

# router = DefaultRouter()
# router.register(r'/accounts/', views.UserList)
# router.register(r'/accounts/<int:pk>/', views.UserItem)
#
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('accounts/', views.UserList.as_view(), name='user_list'),
    path('accounts/<int:pk>/', views.UserItem.as_view(), name='user_item'),
]


#
# urlpatterns += [
#     path('', views.home, name='home'),
#     # path('add/', views.add_person, name='add_person'),
#     # path('delete/<int:person_id>/', views.delete_person, name='delete_person'),
# ]
