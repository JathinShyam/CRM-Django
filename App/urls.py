from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer_record/<int:pk>', views.customer_record, name='customer_record'),
    path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
    path('send_email/', views.send_email, name='send_email'),
    path('import_csv/', views.import_csv, name='import_csv'),
    path('search/', views.search_results, name='search_results'),
    path('submit_query/', views.submit_query, name='submit_query'),
    path('view_queries/', views.view_queries, name='view_queries'),
    path('assign_lead/', views.assign_lead, name='assign_lead'),

]
