from django.urls import path
from . import views
from django.urls import include
from .views import logout_now

app_name = 'tasks'   # همین نام می‌شود namespace


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('adding' , views.add_task , name = 'add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edittt_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('signup/', views.signup_view, name='signup'),  # /tasks/accounts/  برای ثبت‌نام سفارشی
    path('logout/', logout_now, name='logout'),  # همین نام پیش‌فرض را override کن
    path('', include('django.contrib.auth.urls')),     # این خط همه‌ی مسیرهای لاگین را می‌آورد
    

]
