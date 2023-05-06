from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChsngeForm, MyPasswordRestForm, MySetPasswordForm
from django.contrib.auth.forms import UserCreationForm



urlpatterns = [
    #path('', views.home),
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('pluscart/', views.plus_cart),
    
    
    path('cart/', views.show_cart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),  
    #path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),
#    path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name= 'app/login.html', authentication_form=LoginForm), name='login'),
#    path('registration/', views.customerregistration, name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChsngeForm,  success_url='app/passwordchangedone/'),   name='changepassword' ),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views. PasswordResetView.as_view(template_name='app/password_rest.html', form_class= MyPasswordRestForm), name='password_reset'), 
    path('password-reset-done/', auth_views. PasswordResetDoneView.as_view(template_name='app/password_rest_done.html'), name='password_reset_done'), 
    path('password-reset-confirm/<uidb64>/<token>', auth_views. PasswordResetConfirmView.as_view(template_name='app/password_rest_confirm.html', form_class=MySetPasswordForm),name ='password_reset_confirm'), 
    path('password-reset-complite/', auth_views. PasswordResetCompleteView.as_view(template_name='app/password_rest_complite.html'), name='password_reset_complete'), 

    
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
