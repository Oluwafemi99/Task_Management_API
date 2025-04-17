from django.urls import path
from .views import (UserCreateView, UserDeleteView, UserlistViews,
                    MarkTaskCompleteView, MarkTaskInCompleteView,
                    TaskCreateView, TaskListView, UserDetailsView,
                    TaskDeleteView)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('user/list/', UserlistViews.as_view(), name='user-list'),
    path('tasks/<int:pk>/complete/', MarkTaskCompleteView.as_view(), name='tasks-complete'),
    path('tasks/<int:pk>/incomplete/', MarkTaskInCompleteView.as_view(), name='task=incomplete'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/list/', TaskListView.as_view(), name='task-list'),
    path('user/<int:pk>/details/', UserDetailsView.as_view(), name='user-details'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', obtain_auth_token, name='logout')
]
