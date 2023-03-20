from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('registration_form', views.registration_form, name='registration_form'),

    path('reset_password', views.reset_password, name='reset_password'),
    path('internshipform', views.internshipform, name='internshipform'),
    path('internship_save', views.internship_save, name='internship_save'), 
    path('get_warns', views.get_warns, name='get_warns'),
    path('get_requ', views.get_requ, name='get_requ'), 
    path('logout', views.logout, name='logout'),
    
    #---------------------------------------------------------------------------Admin Section
    path('ad_base', views.ad_base, name='ad_base'),
    path('ad_profile', views.ad_profile, name='ad_profile'),
    path('ad_dashboard', views.ad_dashboard, name='ad_dashboard'),
    path('ad_create_work', views.ad_create_work, name='ad_create_work'),
    path('save_create_work', views.save_create_work, name='save_create_work'),
    path('ad_view_work', views.ad_view_work, name='ad_view_work'),
    path('ad_view_clint/<int:id>', views.ad_view_clint, name='ad_view_clint'), 
    path('update_client/<int:id>', views.update_client, name='update_client'),
    path('ad_daily_work_det', views.ad_daily_work_det, name='ad_daily_work_det'),
    path('ad_work_analiz_det', views.ad_work_analiz_det, name='ad_work_analiz_det'),
    path('flt_dt_analiz', views.flt_dt_analiz, name='flt_dt_analiz'),
    path('ad_work_progress', views.ad_work_progress, name='ad_work_progress'),
    path('flt_progress', views.flt_progress, name='flt_progress'),
    path('ad_work_progress_det/<int:id>', views.ad_work_progress_det, name='ad_work_progress_det'),
    path('ad_warning_ex', views.ad_warning_ex, name='ad_warning_ex'),
    path('ad_warning_sugg_dash/<int:id>', views.ad_warning_sugg_dash, name='ad_warning_sugg_dash'),
    path('ad_warning_det/<int:id>', views.ad_warning_det, name='ad_warning_det'),
    path('ad_suggestions_det/<int:id>', views.ad_suggestions_det, name='ad_suggestions_det'),  
    path('change_pass', views.change_pass, name='change_pass'),  
   
    path('ad_imagechange/<int:id>', views.ad_imagechange, name='ad_imagechange'),
    path('ad_accountset', views.ad_accountset, name='ad_accountset'),  
    #---------------------------------------------------------------------------Executive Section
    path('ex_base', views.ex_base, name='ex_base'),
    path('ex_profile', views.ex_profile, name='ex_profile'),
    path('ex_dashboard', views.ex_dashboard, name='ex_dashboard'), 
    path('ex_daily_work_clint', views.ex_daily_work_clint, name='ex_daily_work_clint'), 
    path('ex_daily_work_det/<int:id>', views.ex_daily_work_det, name='ex_daily_work_det'),
    path('daily_work_done/<int:id>', views.daily_work_done, name='daily_work_done'),
    path('ex_weekly_rep_clint', views.ex_weekly_rep_clint, name='ex_weekly_rep_clint'),
    path('ex_weekly_rep_clint_det/<int:id>', views.ex_weekly_rep_clint_det, name='ex_weekly_rep_clint_det'),
    path('sv_wk_rp/<int:id>', views.sv_wk_rp, name='sv_wk_rp'),
    path('ex_view_work_clint', views.ex_view_work_clint, name='ex_view_work_clint'),
    path('ex_view_clint_det/<int:id>', views.ex_view_clint_det, name='ex_view_clint_det'),  
    path('ex_warning', views.ex_warning, name='ex_warning'),
    path('add_warning/<int:id>', views.add_warning, name='add_warning'),
    path('add_suggestion/<int:id>', views.add_suggestion, name='add_suggestion'),  

    path('ex_warnings_dash', views.ex_warnings_dash, name='ex_warnings_dash'),
    path('ex_suggestions', views.ex_suggestions, name='ex_suggestions'),
    path('ex_change_pass', views.ex_change_pass, name='ex_change_pass'),
    path('ex_accountset', views.ex_accountset, name='ex_accountset'),
    path('ex_imagechange/<int:id>', views.ex_imagechange, name='ex_imagechange'),

     #---------------marketing head
   
    path('he_profile', views.he_profile, name='he_profile'),
    path('he_project', views.he_project, name='he_project'),
    path('he_view_works',views.he_view_works,name='he_view_works'),
    path('he_work_asign/<int:pk>',views.he_work_asign,name='he_work_asign'),
    path('he_daily_task',views.he_daily_task,name='he_daily_task'),
    path('he_workprogress_executive',views.he_workprogress_executive,name='he_workprogress_executive'),
    path('he_progress_report/<int:pk>',views.he_progress_report,name='he_progress_report'),
    path('he_feedback',views.he_feedback,name='he_feedback'),
    path('he_feedbacke1/<int:pk>',views.he_feedbacke1,name='he_feedbacke1'),
    path('he_feedback_submit/<int:pk>',views.he_feedback_submit,name='he_feedback_submit'),
    path('he_work_add/<int:id>',views.he_work_add,name='he_work_add')
    
    
]