from datetime import date

from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

def home(request):
    return render(request, "home.html")

def jobseekerhome(request):
    return render(request,"jobseekerhome.html");
def sample6(request):
    return render(request, "base.html")

def aboutus(request):
    return render(request, "aboutus.html")

def login1(request):
    error=" "
    if request.method=="POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1= ViaUser.objects.get(user=user)
                if user1.type =="jobseeker":
                    login(request,user)
                    # return redirect('jobseekerhome', username=u)
                    error="no"

                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"

    d={'error':error}

    return render(request,'login1.html',d)


def employerlogin(request):
    error=" "
    if request.method=="POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user1 = authenticate(username=u,password=p)
        if user1:
            try:
                user2= Employer.objects.get(user=user1)
                if user2.type =="employer":
                    login(request,user1)
                    # return redirect('jobseekerhome', username=u)
                    error="no"

                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"

    d={'error':error}

    return render(request,'employerlogin.html',d)


def adminlogin(request):
    return render(request, "adminlogin.html")



def register(request):
    error =" "
    if request.method =='POST':
        f=request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        try:
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           ViaUser.objects.create(user=user,mobile=con,image=i,gender=gen ,type="jobseeker")
           error="no"
        except:
            error="yes"

    d= {'error':error}
    return render(request,'register.html',d)


def employerRegister(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        c = request.POST['cname']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        loc = request.POST['location']
        r = request.POST['role']
        off = request.POST['office_number']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p, email=e)
            Employer.objects.create(user=user, mobile=con, image=i, gender=gen, company=c, type="employer")
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"

    d = {'error': error}
    if error == "no":
        return redirect('employerRegister')
    return render(request, 'employerRegister.html', d)



def it(request):
    return render(request,'it.html')

def programming(request):
    return render(request,'Programming.html')
def verbalreason(request):
    return render(request,'verbalreason.html')
def webdevelopment(request):
    return render(request,'webdevelopment.html')
def resume(request):
    return render(request,'resume.html')


def appliedjobs(request):
    # Retrieve applied jobs for the current user
    applied_jobs = AppliedJobs.objects.filter(candidate=request.user)

    return render(request, 'appliedjobs.html', {'applied_jobs': applied_jobs})





def employerhome(request):
    return render(request, 'employerhome.html')



def apply(request, job_id):
    if request.method == 'POST':
        resume = request.FILES.get('resume')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')
        cgpa = request.POST.get('cgpa')
        marksheet = request.FILES.get('marksheet')
        github = request.POST.get('github')

        job = Job.objects.get(pk=job_id)
        email=request.user
        position = job.title
        employer = job.recruiter
        company_name = job.company

        applied_job = AppliedJobs.objects.create(
            resume=resume,
            name=name,
            gender=gender,
            address=address,
            qualification=qualification,
            cgpa=cgpa,
            marksheet=marksheet,
            github=github,
            candidate=request.user,
            email=email,
            employer=employer,
            position=position,  # Setting the position as job title
            company_name=company_name,
        )
        return render(request, 'apply.html', {'job': job, 'error': 'no'})
    else:
        job = Job.objects.get(pk=job_id)
        return render(request, 'apply.html', {'job': job})

def select_candidate(request,  user_, company_):

    candidate= AppliedJobs.objects.get( email=user_, company_name=company_)

    candidate.status = 'selected'
    candidate.save()
    email = EmailMessage(
        'Via Job Portal',
        ' <a>Congratulations!. You are shortlisted</a>',
        'kavyanimmagadda12@gmail.com',
        [user_],
    )
    email.content_subtype = "html"
    email.send()
    return redirect('candidates')

def reject_candidate(request, user_, company_):
    candidate = AppliedJobs.objects.get(email=user_, company_name=company_)

    candidate.status = 'unselected'
    candidate.save()
    email = EmailMessage(
        'Via Job Portal',
        ' <a>Better Luck next time!. You are not shortlisted. Wish to see you again .</a>',
        'kavyanimmagadda12@gmail.com',
        [user_],
    )
    email.content_subtype = "html"
    email.send()
    return redirect('candidates')



def post(request):
    error = ""

    # Check if the user has an employer
    if hasattr(request.user, 'employer'):
        if request.method == 'POST':
            title = request.POST.get('jobtitle')
            salary = request.POST.get('salary')
            skills = request.POST.get('skills')
            start_date = request.POST.get('start-date')
            end_date = request.POST.get('end-date')
            experience = request.POST.get('experience')
            location = request.POST.get('location')
            description = request.POST.get('description')
            company = request.user.employer.company  # Get company name from logged-in user's employer
            image = request.FILES.get('logo')
            recruiter = request.user.employer

            try:
                Job.objects.create(
                    title=title,
                    salary=salary,
                    skills=skills,
                    start_date=start_date,
                    end_date=end_date,
                    experience=experience,
                    location=location,
                    description=description,
                    company=company,
                    image=image,
                    recruiter=recruiter
                )
                error = "no"
            except Exception as e:
                error = "yes"
                print(e)  # Print the error
    else:
        error = "User has no employer"

    d = {'error': error}
    return render(request, 'post.html', d)


def jobslist(request):
    jobs = Job.objects.all()
    user = request.user

    data = AppliedJobs.objects.filter(email=user)

    return render(request, 'jobslist.html', {'jobs': jobs})
def candidates(request):
    applied_jobs = AppliedJobs.objects.filter(employer=request.user)
    return render(request, 'candidates.html', {'applied_jobs': applied_jobs})

def contactus(request):
    error = " "
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            contact = Contact.objects.create(name=name, email=email, message=message)
            contact.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'contactus.html', d)


def profile(request):
    # Get the logged-in user's ViaUser object
    viauser = ViaUser.objects.get(user=request.user)
    return render(request, 'profile.html', {'viauser': viauser})

def profile2(request):
    # Get the logged-in user's Employer object
    employer = Employer.objects.get(user=request.user)
    return render(request, 'profile2.html', {'employer': employer})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'mobile': user.viauser.mobile,
            'image': user.viauser.image,
            'gender': user.viauser.gender,
        }
        form = UserChangeForm(initial=initial_data)
        form.fields['email'].widget.attrs['readonly'] = True  # Make email field readonly
    return render(request, 'profile.html', {'user': user, 'edit': True, 'form': form})


from django.core.mail import EmailMessage

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def email_template(request):
    return render(request, 'email_template.html')

def send_email_with_button(request):
    if request.method == 'POST':

        email_ = request.POST.get('email')
        email = EmailMessage(
            'Via Job Portal',
            ' <a>Thanks For Registering in our Via Job Port</a>',
            'kavyanimmagadda12@gmail.com',
            [email_],
        )
        email.content_subtype = "html"
        email.send()
        return render(request,'register.html')

def send_email(request,user_):
    if request.method == 'POST':

        email = EmailMessage(
            'Via Job Portal',
            ' <a>Congratulations!. You are shortlisted</a>',
            'kavyanimmagadda12@gmail.com',
            [user_],
        )
        email.content_subtype = "html"
        email.send()
        return render(request, 'candidates.html')