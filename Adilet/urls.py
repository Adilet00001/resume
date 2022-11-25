from django.urls import path
from . import views
urlpatterns = [
    path('news/', views.news),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.Newdetail.as_view(), name='detail'),
    # path('<int:pk>/update', views.NewUpdate.as_view(), name='update'),
    # path('<int:pk>/delete', views.NewDelete.as_view(), name='delete')
]