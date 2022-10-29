from django.urls import path
from managements.employee import my_feedback, my_notifications

from managements.hrm import employee, employee_leave, notifications

from . import adminviews, directorviews, views

from .hrm import profile, employee,employee_leave,employee_feedback,employee_search,notifications
from .employee import my_leave,my_feedback, my_notifications
# from accounts.directorviews import add_employee,add_employee,add_employee_save,manage_employee,edit_employee,delete_employee,add_admin,add_admin_save,manage_admin,edit_admin,edit_admin_save,delete_admin,edit_employee_save


urlpatterns = [
    # views

    path('error/', views.error_page, name='error_page'),
    path('firebase-messaging-sw.js/',
         views.showFirebaseJS, name='show_firebase_js'),

    path('hrm_profile/', profile.director_profile,
         name='director_profile'),
    path('hrm_profile_save/', profile.director_profile_save,
         name='director_profile_save'),

    # setting up dashboard for all staffs
    path('department/', directorviews.department, name='department'),
    path('department/', directorviews.create_department, name='crud_ajax_create'),
    path('create_department_save/', directorviews.create_department_save,
         name='create_department_save'),
    path('department/<int:department_id>/',
         directorviews.update_department, name='crud_ajax_update'),
    path('department/', directorviews.update_department_save,
         name='update_department_save'),
    path('ajax/crud/delete/',  directorviews.DeleteDepartment.as_view(),
         name='crud_ajax_delete'),

    
    #    profile template
    path('all_staff_profile/', directorviews.all_staff_profile,
         name='all_staff_profile'),
    path('all_staff_profile_template/<int:employee_id>/',
         directorviews.all_staff_profile_template, name='all_staff_profile_template'),
    # ============================================================

    #     END  DIRECTOR MANAGEMENT PATH

    # ============================================================

    # '''

    # employee
    path('employee/add/', employee.add_employee, name='add-employee'),
    path('employee/add/save', employee.add_employee_save, name='add-employee-save'),
    path('employee/manage', employee.manage_employee, name='manage-employee'),
    path('update/<int:employee_id>/employee/',
         employee.edit_employee, name='editemployee'),
    path('employee/update/save/', employee.edit_employee_save,
         name='editemployeesave'),
    path('delete/<int:employee_id>/',
         employee.delete_employee, name='delete_user'),
    path('add/upload/employee/', employee.add_upload_employee,
         name='add_upload_employee'),

    # employee feedbacks
    path('employee/feedback/message/', employee_feedback.employee_feedback_message,
         name='employee_feedback_message'),
    path('search/feedback/', employee_feedback.search_feedback, name='search_feedback'),
    path('employee/feedback/message/replied/', employee_feedback.employee_feedback_message_replied,
         name='employee_feedback_message_replied'),

    #  employee leave response path
    path('employee/leave/view/', employee_leave.employee_leave_view,
         name='employee_leave_view'),
    path('search/leave/', employee_leave.search_leave, name='search_leave'),
    path('employee/approve/leave/<str:leave_id>/',
         employee_leave.employee_approve_leave, name='employee_approve_leave'),
    path('employee/disapprove/leave/<str:leave_id>',
         employee_leave.employee_disapprove_leave, name='employee_disapprove_leave'),

    # employee notifications
    path('director/send/notification/employee/', notifications.director_send_notification_employee,
         name='director_send_notification_employee'),
    # path('employee_send_notification/',directorviews.employee_send_notification,name='employee_send_notification'),
    path('search/notify/', notifications.search_notify, name='search_notify'),
    path('send/employee/notification/', notifications  .send_employee_notification,
         name='send_employee_notification'),
    path('search/', employee_search.search_query, name='search'),

    # employeee category
    path('add/category/list/', directorviews.add_category_view,
         name='add_category_list'),
    path('update/category/<int:category_id>/',
         directorviews.update_category, name='update_category'),

    #employee payroll manager
    path('payroll/manager/',directorviews.payroll_manager,name='payroll_manager'),
    path('payroll/manager/upload/',directorviews.payroll_manager_upload,name='payroll_manager_upload'),
    # ============================================================
    # all admin path

    #  =============================================================

    path('add-admin/', directorviews.add_admin, name='add_admin'),
    path('added-admin/', directorviews.add_admin_save, name='add_admin_save'),
    path('manage-admin/', directorviews.manage_admin, name='manage_admin'),
    path('edit-admin/<int:admin_id>/',
         directorviews.edit_admin, name='edit_admin'),
    path('edit-admin-save/', directorviews.edit_admin_save, name='edit_admin_save'),
    path('delete/<int:admin_id>/', directorviews.delete_admin, name='delete_admin'),
    path('search_admin/', directorviews.search_admin, name='search_admin'),

    # admin leave response

    path('admin_leave_view/', directorviews.admin_leave_view,
         name='admin_leave_view'),
    path('admin_search_leave/', employee_leave.search_leave,
         name='admin_search_leave'),
    path('admin_approve_leave/<str:leave_id>/',
         directorviews.admin_approve_leave, name='admin_approve_leave'),
    path('admin_disapprove_leave/<str:leave_id>',
         directorviews.admin_disapprove_leave, name='admin_disapprove_leave'),

    # admin feedback path

    path('admin-feedback-message/', directorviews.admin_feedback_message,
         name='admin_feedback_message'),
    path('admin_search_feedback/', directorviews.admin_search_feedback,
         name='admin_search_feedback'),
    path('admin_feedback_message_replied/', directorviews.admin_feedback_message_replied,
         name='admin_feedback_message_replied'),

    # admin notifications path

    path('director_send_notification_admin/', directorviews.director_send_notification_admin,
         name='director_send_notification_admin'),
    path('admin_search_notify/', directorviews.admin_search_notify,
         name='admin_search_notify'),
    path('send_admin_notification/', directorviews.send_admin_notification,
         name='send_admin_notification'),

    # path('search/',directorviews.search_query,name='search'),


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


    path('employee/apply/leave/', my_leave.employee_apply_leave,
         name='employee_apply_leave'),
    path('employee/apply/leave/save/', my_leave.employee_apply_leave_save,
         name='employee_apply_leave_save'),
    path('employee/feedback/', my_feedback.employee_feedback,
         name='employee_feedback'),
    path('employee/feedback/save/', my_feedback.employee_feedback_save,
         name='employee_feedback_save'),
    path('employee/fcmtoken/save/', my_notifications.employee_fcmtoken_save,
         name='employee_fcmtoken_save'),
    path('employee/all/notificaton/', my_notifications.employee_all_notificaton,
         name='employee_all_notificaton'),


    # '''
    # ============================================================

    #     END  EMPLOYEE MANAGEMENT PATH

    # ============================================================
    # '''
     # CHECKING FOE EMAILS AND USERNAME 
    path('check_email_exist/', views.check_email_exist,
         name='check_email_exist'),
    path('check_username_exist/', views.check_username_exist,
         name='check_username_exist'),

    # '''
    # ============================================================

    #       ADMIN MANAGEMENT PATH

    # ============================================================

    path('admin_apply_leave/', adminviews.admin_apply_leave,
         name='admin_apply_leave'),
    path('admin_apply_leave_save/', adminviews.admin_apply_leave_save,
         name='admin_apply_leave_save'),
    path('admin_feedback/', adminviews.admin_feedback, name='admin_feedback'),
    path('admin_feedback_save/', adminviews.admin_feedback_save,
         name='admin_feedback_save'),
    path('admin_fcmtoken_save/', adminviews.admin_fcmtoken_save,
         name='admin_fcmtoken_save'),
    path('admin_all_notificaton/', adminviews.admin_all_notificaton,
         name='admin_all_notificaton'),



    # '''
    # ============================================================

    #     END  EMPLOYEE MANAGEMENT PATH

    # ============================================================
]
