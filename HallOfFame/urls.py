from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from halls import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    # AUTH
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # Halls
    path('halloffame/create', views.CreateHall.as_view(), name='create_hall'),
    path('halloffame/<int:pk>', views.DetailHall.as_view(), name='detail_hall'),
    path('halloffame/<int:pk>/update', views.UpdateHall.as_view(), name='update_hall'),
    path('halloffame/<int:pk>/delete', views.DeleteHall.as_view(), name='delete_hall'),
    # Videos
    path('halloffame/<int:pk>/add_video', views.add_video, name='video_search'),
    path('video/search', views.video_search, name='add_video'),
    path('video/<int:pk>/delete', views.DeleteVideo.as_view(), name='delete_video'),
    # Сброс пароля
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset/form.html',
                                              html_email_template_name='password_reset/email.html',
                                              subject_template_name='password_reset/subject_email.txt'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset/done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/complete.html'),
         name='password_reset_complete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
