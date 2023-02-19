from django.shortcuts import render,redirect
from users.models import *
import spacy.cli
import nltk
import requests
import json
from pprint import pprint
spacy.load('en_core_web_sm')

from pyresparser import ResumeParser
# Create your views here.
# @login_required(login_url="login")


def users_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        emailid = request.POST.get('emailid')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')
        mobileno = request.POST.get('mobileno')
        dob = request.POST.get('dob')
        password1 = request.POST.get('password1')
        collegename = request.POST.get('collegename')

        register = Register(username=username, emailid=emailid, fname=fname, lname=lname, gender=gender, country=country, city=city, mobileno=mobileno, dob=dob, collegename=collegename, password1=password1)
        register.save()
        return redirect('login')

    return render(request, "users/register.html")

def users_login(request):
    # if request.user.is_authenticated:
    #     print('jhjasgdfdasjgsjagfdsgjgdjskafjk')
    #     return redirect('login')
    # else:
    if request.method == 'POST':
        emailid = request.POST.get('emailid')
        password1 = request.POST.get('password')

        record = Register.objects.only('emailid')
        l = len(record)
        print(emailid)
        print('emailid', password1)
        for i in range(l):
            print(record[i].emailid)

            if record[i].emailid == emailid:
                print('record[0].emailid')
                

                if record[i].password1 == password1:
                    request.session['username'] = emailid
                    return redirect("/users/hackathons/")
                    # if request.session.has_key('username'):
                    #     emailid = request.session['username']

                    #     print('dfdfds',emailid)


        # if user is not None:
        #     login(request, user)
        #     return redirect('login')
        # else:
        #     messages.info(request, 'User or Password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)


def register_hackathon(request):
    if request.method == 'POST':
        hack_name = request.POST.get('hack_name')
        org_name = request.POST.get('org_name')
        desc_name = request.POST.get('desc_name')
        rules = request.POST.get('rules')
        h_url = request.POST.get('h_url')
        guide = request.POST.get('guide')
        sdt = request.POST.get('sdt')
        edt = request.POST.get('edt')
        mini = request.POST.get('min')
        maxi = request.POST.get('max')
        domain = request.POST.get('domain')
        skills = request.POST.get('skills')
        mod_of_ev = request.POST.get('mod_of_ev')

        register = RegisterHackathon(name_hackathon=hack_name,Organization_name=org_name,Description_hack=desc_name,rules = rules,hackathon_url=h_url,Guidelines=guide,start_date_time=sdt,end_date_time=edt,minimum_no_team=mini,maximum_no_team=maxi,mode_of_event=mod_of_ev, domain=domain,skills=skills)
        register.save()

        return redirect("/users/hackathons/")
        

    return render(request, "users/hack-register.html")

def see_hackathon(request):
    hacks = RegisterHackathon.objects.all()
    print(request.session['username'])
    # print(context)
    # print()
    return render(request, "users/hackathons.html",{'hack':hacks})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        register = Contact(name=name,email=email,message=message)
        register.save()

        return redirect("/")

    return render(request, "users/contact.html")


def show_hackathon(request,pk):

    hk = RegisterHackathon.objects.get(pk=pk)
     
    return render(request, "users/show_hackathon.html",{'hk':hk})

def part_register(request,pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        c_name = request.POST.get('c_name')
        domain = request.POST.get('domain')
        course = request.POST.get('course')
        c_spec = request.POST.get('c_spec')
        year = request.POST.get('year')
        teamname = request.POST.get('teamname')
        diff_able = request.POST.get('diff_able')
        citizen = request.POST.get('citizen')
        # resume = request.POST.get('resume')
        github = request.POST.get('github')
        resume = request.FILES['resume']
        print(resume)

       
        # github

        username = github
        user = requests.get('https://api.github.com/users/'+username)
        user_json = json.loads(user.content or user.text)
        repo = int(user_json['public_repos'])
        print(repo)
        repos = requests.get('https://api.github.com/users/'+username+'/repos', params={'type':'owner','sort':'pushed'})
        repos_json = (json.loads(repos.content))
        star = 0
        lang = []
        for i in repos_json:
            star += int(i['stargazers_count'])
            lang.append(str(i['language']))
            
        lang = set(lang)
        lang = list(lang)
        print(star, lang)
        lan=""
        for i in lang:
            lan+=i
            lan+=" "
        
        # repo , star , lang
        # github


        # Resume


        print(resume.name)
        path = 'C:\\Users\\asus\\Documents\\Hackniche-2023\\codeastra\\media\\documents\\'+resume.name
        print(path)
        data = ResumeParser(path).get_extracted_data()
        l = list(data.keys())
        for i in l:
            print(i,data[i])

        l_skills = data["skills"]
        s_skills=""
        for i in l_skills:
            s_skills+=i
            s_skills+=" "
        l_exp = data["experience"]
        s_exp=""
        if l_exp is not None:
            for i in l_exp:
                s_exp+=i
                s_exp+=" "
            
        else:
            s_exp=""
        s_desg=""
        l_desg = data["designation"]
        if l_desg is not None:
            for i in l_desg:
                s_desg+=i
                s_desg+=" "
            
        else:
            l_exp = ""
        l_no_of_exp = data["total_experience"]
        # Resume
        pk = pk
        hacks = ParticipateHackathon.objects.get(pk=pk)
        skillsi = hacks.skills
        
        count = 0
        l=0
        score=0
        for i in skillsi:
            if i in s_skills:
                count+=1
            l +=1
        score = count/l*100
        score += repo *5
        score += star*10
        score += l_no_of_exp
        count = 0
        l=0
        for i in skillsi:
            if i in lan:
                count+=1
            l +=1
        score += count/l*100

        print("DFSKHFDJSKFDHSJHFSKJHFDLSHDFSKJDHSFKDJHFSKDFJHJDFHSKDJSHDKJFSHDFKJSHF")

        register = ParticipateHackathon(name=name,email=email,gender=gender,college_name=c_name,domain=domain,course=course,c_spec=c_spec,year=year,diff_able=diff_able,citizen=citizen,github=github,resume=resume,skills=s_skills,experience = s_exp,designation=s_desg,no_of_exp =l_no_of_exp,no_of_repos=repo,no_of_stars=star,languages_used=lan, score=score, hack_id=pk, teamname=teamname)
        register.save()
        
        return redirect("/users/hackathons")
        
    return render(request, "users/parti_register.html")

# def evaluation(request):
#     hacks = ParticipateHackathon.objects.all()
#     skills = hacks.skills
#     domain = hacks.domain
#     best_answer = []

#     # logic to find candidates
#     for i in range(0,len(new1)-1):
#         for j in range(0,len(new2)-1):
#             ans = []
#             if len(ans)>=len(best_answer):
#                 best_answer = list(ans)    
#     if len(best_answer) > 5:
#         return " ".join(best_answer)
#     return ""
def index(request):
    
    return render(request, "index.html")

def admin_index(request):
    if request.session.has_key('username'):
        emailid = request.session['username']
    # print('email',emailid)
    hacki = RegisterHackathon.objects.all()
    # print(emailid)
    return render(request, "admin_side/admin.html", {'hack':hacki})

def hack_details(request,pk):
    if request.session.has_key('username'):
        emailid = request.session['username']
    hacki = ParticipateHackathon.objects.filter(hack_id=pk).order_by('teamname').values()

    # hacki = ParticipateHackathon.objects.group_by('teamname')
    

    print(hacki)
    return render(request, "admin_side/hack-details.html", {'hack':hacki})