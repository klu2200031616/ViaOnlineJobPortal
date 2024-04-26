from django.urls import path, include
from .views import *


urlpatterns=[


	path('ti', sample6, name="ti"),
	path('home', home, name="home"),
	path('aboutus', aboutus, name="aboutus"),
	path('login1', login1, name="login1"),
	path('adminlogin', adminlogin, name="adminlogin"),
path('jobseekerhome', jobseekerhome, name="jobseekerhome"),
	path('employerlogin', employerlogin, name="employerlogin"),
	path('register', register, name="register"),
	path('employerRegister', employerRegister, name="employerRegister"),
path('employerhome', employerhome, name="employerhome"),
	path('appliedjobs', appliedjobs, name="appliedjobs"),
# path('apply', apply, name="apply"),
path('apply/<int:job_id>/', apply, name='apply'),
path('select_candidate/<str:user_>/<str:company_>/', select_candidate, name='select_candidate'),
    path('reject_candidate/<str:user_>/<str:company_>/', reject_candidate, name='reject_candidate'),
path('candidates', candidates, name="candidates"),
path('post', post, name="post"),
path('jobslist', jobslist, name="jobslist"),

	path('it', it, name="it"),
path('Programming',programming, name="Programming"),
path('verbalreason',verbalreason, name="verbalreason"),
path('webdevelopment',webdevelopment, name="webdevelopment"),
    path('resume',resume, name="resume"),

	path('contactus', contactus, name='contactus'),

	path('profile/', profile, name='profile'),
path('profile2', profile2, name='profile2'),
	path('profile/edit/', edit_profile, name='edit_profile'),
path('email_template',email_template , name='email_template'),
path('send_email_with_button',send_email_with_button,name="send_email_with_button"),
	path('send_email/<str:user_>/', send_email, name='send_email'),

]