from django.urls import path
from . import views
urlpatterns = [
    path('<int:page_num>', views.programming_page),
    path('<topic>/', views.news_page)

]