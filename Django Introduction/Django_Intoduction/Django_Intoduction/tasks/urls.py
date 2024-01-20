#Do always when creating new Django App:


#1. (Optional) move to project directory
#2. Create "urls.py" file
#3.Register this Django App's  in "urls.py" in the project's "urls.py" file
#4.Register this Django App in "settings.py"

from django.urls import path
from .views import index

urlpatterns = (
    path('', index),

)