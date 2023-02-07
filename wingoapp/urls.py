from django.urls import path
from . import views

urlpatterns = [

    # dashboard paths

    path('', views.indexPage, name='indexPage'),
    path('dashboard_default', views.dashboard_default, name='index'),
    path('dashboard_ecommerce', views.dashboard_ecommerce, name='dashboard_ecommerce'),

    # users paths

    path('users_users_profile', views.users_users_profile, name='users_users_profile'),
    path('users_users_edit', views.users_users_edit, name='users_users_edit'),
    path('users_users_card', views.users_users_card, name='users_users_card'),

    # others path
    # error pages

    path('error_page_1', views.error_page_1, name='error_page_1'),
    path('error_page_2', views.error_page_2, name='error_page_2'),
    path('error_page_3', views.error_page_3, name='error_page_3'),
    path('error_page_4', views.error_page_4, name='error_page_4'),

    # authentication paths

    path('login', views.login_simple, name='login'),
    path('login_simple', views.login_simple, name='login_simple'),
    path('login_with_bg_image', views.login_with_bg_image, name='login_with_bg_image'),
    path('login_with_image_two', views.login_with_image_two, name='login_with_image_two'),
    path('login_with_validation', views.login_with_validation, name='login_with_validation'),
    path('login_with_tooltip', views.login_with_tooltip, name='login_with_tooltip'),
    path('login_with_sweetalert', views.login_with_sweetalert, name='login_with_sweetalert'),
    path('register_simple', views.register_simple, name='register_simple'),
    path('register_with_bg_image', views.register_with_bg_image, name='register_with_bg_image'),
    path('register_with_bg_video', views.register_with_bg_video, name='register_with_bg_video'),
    path('unlock_user', views.unlock_user, name='unlock_user'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('create_password', views.create_password, name='create_password'),
    path('maintenance', views.maintenance, name='maintenance'),
    path('logout_view', views.logout_view, name='logout_view'),

    # carreras
    path('carreras', views.carreras_listas.as_view(template_name='carreras/carreras/carreras.html'), name='carreras'),
    path('carreras_eliminar/<int:pk>', views.carreras_eliminar, name='carreras_eliminar'),
    path('carreras_agregar', views.carreras_agregar, name='carreras_agregar'),
    path('carreras_modificar/<int:pk>', views.carreras_modificar, name='carreras_modificar'),
    path('carreras_ver/<int:pk>', views.carreras_ver, name='carreras_ver'),
    # support ticket path

]
