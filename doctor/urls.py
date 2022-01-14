from pydoc import doc
from django.urls import path

from doctor.views import doc_homepage, login

from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login, name = 'login'),
    path('doctor/', doc_homepage, name = 'doc_homepage'),
    path('doctor/register/', doc_register, name = 'doc_register'),    
    path('doctor/prescription', view_prescription, name='view_prescription'),
    path('prescription/add', add_prescription),
    path('alldoctors/',doc_info),
    path('medicines/',view_all_meds,name='view_all_meds'),
    path('medicine/<int:id>',view_one_med, name='view_meds'),
]