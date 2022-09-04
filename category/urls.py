from django.urls import path

from . import views
from .views import (add_category, create_order, get_json_car_data,
                    get_json_car_data2, get_json_grade_data,
                    get_json_leave_data, get_json_level_data,
                    get_json_model_data, get_json_position_data,
                    get_json_step_data, main_view)

urlpatterns = [
    # path('', main_view, name='main-view'),
    path('',views.main_view2,name='main_views'),   
    path('cars-json/', get_json_car_data,name='cars-json'),
    path('cars-jsons/', get_json_car_data2,name='cars-jsons'),
    path('models-json/<str:car>/', get_json_model_data,name='models-json'),
    path('models-jsons/<str:department>/', get_json_position_data, name='models-json'),
    path('models-jsonss/<str:position>/', get_json_level_data, name='models-json'),
    path('models-jsonsss/<str:level>/', get_json_grade_data, name='models-json'),
    path('models-jsonsss/<str:grade>/', get_json_grade_data, name='models-json'),
    path('models-jsonssss/<str:step>/', get_json_step_data, name='models-json'),
    path('models-jsonsssss/<str:leave>/', get_json_leave_data, name='models-json'),
    path('create/', create_order, name='create-order'),
    path('creates/', add_category, name='create-order'),
]