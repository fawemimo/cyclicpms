from django.urls import path 

# from accounts.directorviews import add_employee,add_employee,add_employee_save,manage_employee,edit_employee,delete_employee,add_admin,add_admin_save,manage_admin,edit_admin,edit_admin_save,delete_admin,edit_employee_save

from .import directorviews

from .import employeeviews

from .import views

from .directorviews import AddCategoryForEmployeeListView,AddCategoryForEmployeeCreateView,AddCategoryForEmployeeUpdateView

urlpatterns = [
    # views

    path('error/',views.error_page,name='error_page'),
    path('firebase-messaging-sw.js/',views.showFirebaseJS,name='show_firebase_js'),

    path('director_profile/',directorviews.director_profile,name='director_profile'),
    path('director_profile_save/',directorviews.director_profile_save,name='director_profile_save'),
    
    # class based views 
    
    path('add_category_list/',AddCategoryForEmployeeListView.as_view(),name='add_category_list'),
    # path('add_category_list_add/',AddCategoryForEmployeeCreateView.as_view(),name='add_category_list_add'),
    path('add_category_list_add/',directorviews.add_category_for_employee,name='add_category_list_add'),
    path('<int:pk>/',AddCategoryForEmployeeUpdateView.as_view(),name='add_category_list_change'),
    path('ajax_load_grades', directorviews.load_grades, name='ajax_load_grades'),
    path('employee_category_delete/<int:employee_id>/',directorviews.employee_category_delete,name='employee_category_delete'),
    # '''
    # ============================================================

    #     END  DIRECTOR MANAGEMENT PATH

    # ============================================================

    # '''

    # employee
    # path('add_category_employee/',directorviews.add_category_employee,name='add_category_employee'),
    # path('get_json_level_data/',get_json_level_data,name='get_json_level_data'),
    # path('<str:grade>/',get_json_model_data,name='get_json_model_data'),
    # path('save_add_category/',save_add_category,name='save_add_category'),
    # path('add/',directorviews.add_employee,name='add'),
    path('add-employee/',directorviews.add_employee,name='add-employee'),
    path('added/',directorviews.add_employee_save,name='add-employee-save'),
    path('manage-employee/',directorviews.manage_employee,name='manage-employee'),
    path('edit-employee/<int:employee_id>/',directorviews.edit_employee,name='editemployee'),
    path('edit-employee-save/',directorviews.edit_employee_save,name='editemployeesave'),
    path('delete/<int:employee_id>/',directorviews.delete_employee,name='delete_user'),
    path('employee-feedback-message/',directorviews.employee_feedback_message,name='employee_feedback_message'),
    path('employee_feedback_message_replied/',directorviews.employee_feedback_message_replied,name='employee_feedback_message_replied'),
    path('employee_leave_view/',directorviews.employee_leave_view,name='employee_leave_view'),
    path('employee_approve_leave/<str:leave_id>/',directorviews.employee_approve_leave,name='employee_approve_leave'),
    path('employee_disapprove_leave/<str:leave_id>',directorviews.employee_disapprove_leave,name='employee_disapprove_leave'),
    path('employee_send_notification/',directorviews.employee_send_notification,name='employee_send_notification'),
    path('send_employee_notification/',directorviews.send_employee_notification,name='send_employee_notification'),


    # admin

    path('add-admin/',directorviews.add_admin,name='add_admin'),
    path('added-admin/',directorviews.add_admin_save,name='add_admin_save'),
    path('manage-admin/',directorviews.manage_admin,name='manage_admin'),
    path('edit-admin/<int:admin_id>/',directorviews.edit_admin,name='edit_admin'),
    path('edit-admin-save/',directorviews.edit_admin_save,name='edit_admin_save'),
    path('delete/<int:admin_id>/',directorviews.delete_admin,name='delete_admin'),
    # path('admin_fcmtoken_save/',directorviews.admin_fcmtoken_save,name='admin_fcmtoken_save'),

    # '''
    # ============================================================

    #     END  DIRECTOR MANAGEMENT PATH

    # ============================================================

    # '''

    # '''
    # ============================================================

    #      EMPLOYEE MANAGEMENT PATH

    # ============================================================
    # '''


    path('employee_apply_leave/',employeeviews.employee_apply_leave,name='employee_apply_leave'),
    path('employee_apply_leave_save/',employeeviews.employee_apply_leave_save,name='employee_apply_leave_save'),
    path('employee_feedback/',employeeviews.employee_feedback,name='employee_feedback'),
    path('employee_feedback_save/',employeeviews.employee_feedback_save,name='employee_feedback_save'),
    path('employee_fcmtoken_save/',employeeviews.employee_fcmtoken_save,name='employee_fcmtoken_save'),
    path('employee_all_notificaton/',employeeviews.employee_all_notificaton,name='employee_all_notificaton'),


    # '''
    # ============================================================

    #     END  EMPLOYEE MANAGEMENT PATH

    # ============================================================
    # '''

    path('check_email_exist/',directorviews.check_email_exist,name='check_email_exist'),
    path('check_username_exist/',directorviews.check_username_exist,name='check_username_exist'),
]
