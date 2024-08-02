from django.urls import path,include
from Guest import views
app_name="wguest"


urlpatterns = [
   path('HomePage/',views.homepage,name='homepage'),
   path('MyProfile/',views.myprofile,name='myprofile'),
   path('Portfolio/',views.portfolio,name='portfolio'),

   path('EditProfile/',views.edit_profile,name='editprofile'),
   
    
 

]