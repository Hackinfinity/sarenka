
from django.urls import path
from knowledge_base.views import Dowload_data
from knowledge_base.views import Written_from_database

urlpatterns = [
    path('add_to_database',  Dowload_data.data_url_database),
    path('<slug:cwe_number>/json',  Written_from_database.data_to_json, name='my_custom_sql'),
]