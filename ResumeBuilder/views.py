from distutils.command import config
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render 
import pyrebase 
config = {
    'apiKey': "AIzaSyA2nhYiAg4J-N-EgEeQU25kJ8yonDMR_F8",
    'authDomain': "resumebuilder-e2b17.firebaseapp.com",
    'databaseURL': "https://resumebuilder-e2b17-default-rtdb.firebaseio.com/",
    'projectId': "resumebuilder-e2b17",
    'storageBucket': "resumebuilder-e2b17.appspot.com",
    'messagingSenderId': "4787927490821",
    'appId': "1:478792749082:web:fe0915f2bce4d6d55281a3",
    'measurementId': "G-RQ72XTDY9W"
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()

s1 = ''
data6 = {}
inc = 0

def homepage(request):
    return render(request, "HomePage.html")

def homepage1(request):
    if inc ==1:
        pass
    else:
        return HttpResponseRedirect('/warning/')
    return render(request, "homepage1.html")

def login(request):
    try:
        if request.method == "POST":
            global s1, inc
            s1 = request.POST.get('first1')
            s2 = request.POST.get('first2')
            try:
                user = auth.sign_in_with_email_and_password(s1, s2)
                inc = 1
                return HttpResponseRedirect('/homepage1/')   
            except:
                message="Invalid Email or Password"
                return render(request, "login.html", {"message":message})
    except:
       pass
       session_id=user['idToken']
       request.session['uid']=str(session_id)
    return render(request, "login.html")

def sign(request):
    data={}
    try:
        if request.method == "POST":
            s1 = request.POST.get('first1')
            s2 = request.POST.get('first2')
            s3 = request.POST.get('first3')
            s4 = request.POST.get('first4')
            s5 = request.POST.get('first5')
            data = {
                    'username':s1,'name':s2,
                    'surname':s3,'email':s4,
                    }
            try:
                auth.create_user_with_email_and_password(s4,s5)
                db.child('users').push(data)
                return HttpResponseRedirect('/login/')   
            except:
                message="This Email Already Exists"
                return render(request, "sign.html", {"message":message})
    except:
       pass
    return render(request, "sign.html")

def logout(request):
    global inc
    try:
        inc = 0
        del request.session['uid']
    except:
        pass
    return render(request, "homepage.html")

def reset(request):
    try:
        if request.method == "POST":
            s1 = request.POST.get('first1')
            try:
                message  = "A email to reset password is successfully sent"
                auth.send_password_reset_email(s1)
                return render(request, "reset_password.html", {"message":message})
            except:
                message  = "Something went wrong, Please check the email you provided is registered or not"
                return render(request, "reset_password.html", {"message":message})
    except:
        pass
    return render(request, "reset_password.html")

def warning(request):
    return render(request, "warning.html")
 
def page1(request):
    data = {}
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')
    try:
        if request.method == "POST":
            p1 = request.POST.get('first1')
            p2 = request.POST.get('first2')
            p3 = request.POST.get('first3')
            p4 = request.POST.get('first4')
            p5 = request.POST.get('first5')
            p6 = request.POST.get('first6')
            p7 = request.POST.get('first7')
            p8 = request.POST.get('first8')
            p9 = request.POST.get('first9')
            p10 = request.POST.get('first10')
            data = {
                'fname' : p1,'lname' : p2,'email' : p3,'mobile' : p4,
                'website' : p5,'github' : p6,'linkedin' : p7,
                'twitter' : p8,'facebook' : p9,'instagram' : p10,
            }
            allID = db.child('users').get()
            for ID in allID.each():
                if ID.val()['email']==s1:
                    db.child('users').child(ID.key()).child("personal").set(data)
            return HttpResponseRedirect('/educational-details/')    
    except:
       pass
    return render(request, "page1.html", data)

def page2(request):
    data = {}
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')
    try:
        if request.method == "POST":
            e1 = request.POST.get('first1')
            e2 = request.POST.get('first2')
            e3 = request.POST.get('first3')
            e4 = request.POST.get('first4')
            e5 = request.POST.get('first5')
            e6 = request.POST.get('first6')
            e7 = request.POST.get('first7')
            e8 = request.POST.get('first8')
            e9 = request.POST.get('first9')
            e10 = request.POST.get('first10') 
            data = {
                'college' : e1,'qualification_College' : e2,
                'description_College' : e3,'school' : e4,
                'qualification_School' : e5,'description_School' : e6,
                'date1': e7,'date2': e8,'date3': e9,'date4': e10,
            }
            allID = db.child("users").get()
            for ID in allID.each():
                if ID.val()['email']==s1:
                    db.child('users').child(ID.key()).child("education").set(data)
            return HttpResponseRedirect('/project-developed/')               
    except:
       pass
    return render(request, "page2.html", data)

def page3(request):
    data = {}
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')
    try:
        if request.method == "POST":
            global d1, d2, d3, d4, d5, d6, d7, d8, d9
            d1 = request.POST.get('first1')
            d2 = request.POST.get('first2')
            d3 = request.POST.get('first3')
            d4 = request.POST.get('first4')
            d5 = request.POST.get('first5')
            d6 = request.POST.get('first6')
            d7 = request.POST.get('first7')
            d8 = request.POST.get('first8')
            d9 = request.POST.get('first9') 
            data = {
                'Project1_title' : d1,'Project1_link' : d2,'Project1_Desc' : d3,
                'Project2_title' : d4,'Project2_link' : d5,'Project2_Desc' : d6,
                'Project3_title' : d7,'Project3_link' : d8,'Project3_Desc' : d9,
            }
            allID = db.child("users").get()
            for ID in allID.each():
                if ID.val()['email']==s1:                 
                    db.child('users').child(ID.key()).child("projects").set(data)
            return HttpResponseRedirect('/experience-details/')           
    except:
       pass
    return render(request, "page3.html", data)

def page4(request):
    data = {}
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')
    try:
        if request.method == "POST":
            Ex1 = request.POST.get('first1')
            Ex2 = request.POST.get('first2')
            Ex3 = request.POST.get('first3')
            Ex4 = request.POST.get('first4')
            Ex5 = request.POST.get('first5')
            Ex6 = request.POST.get('first6')
            Ex7 = request.POST.get('first7')
            Ex8 = request.POST.get('first8')
            Ex9 = request.POST.get('first9')
            Ex10 = request.POST.get('first10')  
            data = {
                'Exp1_institution' : Ex1,'Exp1_StartDate' : Ex2,'Exp1_EndDate' : Ex3,
                'Exp1_desc' : Ex4,'Exp2_institution' : Ex5,'Exp2_StartDate' : Ex6,
                'Exp2_EndDate' : Ex7,'Exp2_desc' : Ex8,'Exp1_position': Ex9,
                'Exp2_position': Ex10,
            }
            allID = db.child("users").get()
            for ID in allID.each():
                if ID.val()['email']==s1:                 
                    db.child('users').child(ID.key()).child("experience").set(data)
            return HttpResponseRedirect('/extra-details/')             
    except:
       pass
    return render(request, "page4.html", data)

def page5(request):
    data = {}
    data1 = {}
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')
    try:
        if request.method == "POST":
            global sl1, sl2, sl3, sl4, sl5, sl6, sl7, sl8, sl9, sl10, sl11, sl12
            sl1 = request.POST.get('first1')
            sl2 = request.POST.get('first2')
            sl3 = request.POST.get('first3')
            sl4 = request.POST.get('first4')
            sl5 = request.POST.get('first5')
            sl6 = request.POST.get('first6')
            sl7 = request.POST.get('first7')
            sl8 = request.POST.get('first8')
            sl9 = request.POST.get('first9')
            sl10 = request.POST.get('first10')
            sl11 = request.POST.get('first11')
            sl12 = request.POST.get('first12')
            data = {
                'skill1' : sl1,'skill2' : sl2,'skill3' : sl3,
                'skill4' : sl4,'skill5' : sl5,'skill6' : sl6,
                'interest1' : sl7,'interest2' : sl8,'interest3' : sl9,
                'interest4' : sl10,'interest5' : sl11,'interest6' : sl12,
            }
            allID = db.child("users").get()
            for ID in allID.each():
                if ID.val()['email']==s1:
                    db.child('users').child(ID.key()).child("extra").set(data)
            return HttpResponseRedirect('/resume/')              
    except:
       pass
    return render(request, "page5.html", data1)

def resume(request):
    data1 = {} 
    data2 = {}
    data3 = {}
    data4 = {}
    data5 = {}
    global data6 
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')
    allID = db.child("users").get()
    for ID in allID.each():
            if ID.val()['email']==s1:
                data1 = db.child('users').child(ID.key()).child('personal').get().val()
                data2 = db.child('users').child(ID.key()).child('education').get().val()
                data3 = db.child('users').child(ID.key()).child('projects').get().val()
                data4 = db.child('users').child(ID.key()).child('experience').get().val()
                data5 = db.child('users').child(ID.key()).child('extra').get().val()
                data6 = {**data1, **data2, **data3, **data4, **data5}
    return render(request, "resume.html", data6)

def download(request):
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')

    return render(request, "download.html", data6)

def download1(request):

    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')

    return render(request, "download1.html", data6)

def selecttemp(request):
    if inc == 1:
        pass
    else:
        return HttpResponseRedirect('/warning/')     
    return render(request, "selecttemp.html", data6)


