from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
   
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
    path('multi/',views.multi,name="multiselect"),
    path('img/',views.img,name="img"),
       path('img_dis/',views.img_dis,name="img_dis"),
    path('builtin/',views.builtin,name='builtin')
]