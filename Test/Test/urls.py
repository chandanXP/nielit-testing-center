from django.urls import path, include
from todo.views import *

urlpatterns = [
    path('', upload_csv, name='upload_csv'),
    path('add_subject/', add_subject, name='add_subject'),
    path('create_test/', create_test, name='create_test'),
    path('running-test/', running_test, name='running_test'),
    path('test_page/<str:subject_code>/', fetch_subject_detail, name='top_10_questions'),
    path('submit-test/', submit_test, name='submit_test'),
    path('auth/', include('authentication.urls')),

]
