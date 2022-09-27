from django.contrib.auth import  logout
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import *
from datetime import datetime,date

# Create your views here.
def loginsave(request):
    if request.method =='POST':
        if login.objects.filter(uname=request.POST['uname'], password=request.POST['password']):
            member=login.objects.get(uname=request.POST['uname'], password=request.POST['password'])
            return render(request,'admin_dashboard.html',{'member':member})
        elif Staff.objects.filter(username=request.POST['uname'], password=request.POST['password']):
            a=Staff.objects.get(username=request.POST['uname'], password=request.POST['password'])
            request.session['staff_id']=a.id
            s=Staff.objects.all()
            return render(request,'index_staff_dashboard.html',{'a':a,'s':s})

        elif Admission.objects.filter(username=request.POST['uname'], password=request.POST['password']):
            b=Admission.objects.get(username=request.POST['uname'], password=request.POST['password'])
            request.session['admission_id']=b.id
            print(request.session['admission_id'])
            return render(request,'index_student_dashboard.html',{'b':b})

        elif Institute_details.objects.filter(username=request.POST['uname'], password=request.POST['password']):
            c=Institute_details.objects.get(username=request.POST['uname'], password=request.POST['password'])
            request.session['Institute_id']=c.id            
            return render(request,'institute_dashboard.html',{'c':c})
        else:
            msg = "invalid username or password"
            return render(request ,'Login.html',{'msg':msg})
    return render(request, 'Login.html')


def logouts(request):
    logout(request)
    return redirect('loginsave')
       


#-----------------------ADMIN---------------------#



def index_admin(request):
    return render(request,"base_admin.html")

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")


#--------------------------INSTITUTE----------------#

def index_institute(request):
    return render(request,"base_institute.html")

def institute_dashboard(request):
    s=request.session['Institute_id']
    c=Institute_details.objects.get(id=s)
    return render(request,"institute_dashboard.html",{'c':c})


def viewinstitute(request):
    if request.method == 'GET':
        inss = Institute_details.objects.all()
        return render(request, 'admin_institute_view.html', {'ins':inss})
    else:
        imag = request.FILES['im']
        i = Institute_details()
        i.username = request.POST.get('username')
        i.password = request.POST.get('password')
        i.name = request.POST.get('name')
        i.desig = request.POST.get('desig')
        i.address = request.POST.get('address')
        i.contact = request.POST.get('contact')
        i.email = request.POST.get('email')
        i.image = imag
        i.save()
        return redirect ('admin_institute_view')


def deleteinstitute(request, ins_id):
    de = Institute_details.objects.get(id=ins_id)
    de.delete()
    return redirect('admin_institute_view')

def Institute_visitor(request):
    if request.method == 'GET':
        data = Visitor.objects.all()
        return render(request,"institute_visitors.html",{'data':data})
    else:
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        guardian = request.POST['guardian']
        school = request.POST['school']
        gender = request.POST['gender']
        purpose = request.POST['purpose']
        time=request.POST['time']
        date=request.POST['date']
        new= Visitor(name=name,place=place,email=email,contact=contact,address=address,guardian=guardian,
        school=school,gender=gender,purpose=purpose,date=date,time=time)
        new.save()
        return redirect('Institute_visitor')

def institute_visitors_delete(request,id):
    var = Visitor.objects.get(id=id)
    var.delete()
    return redirect('Institute_visitor')


def institute_staff(request):
    if request.method == 'GET':
        data = Staff.objects.all()
        return render(request,"institute_staff.html",{'data':data})
    else:
        name = request.POST.get('name')
        department = request.POST.get('department')
        contact = request.POST.get('contact')
        photo = request.POST.get('photo')
        desig= request.POST.get('desig')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        check = request.POST.get('coursename')
        new= Staff(name=name,department=department,desig=desig,contact=contact,photo=photo,email=email,
        username=username,password=password,check=check)
        new.save()
        return redirect('institute_staff')

def institute_staff_delete(request,id):
    var = Staff.objects.get(id=id)
    var.delete()
    return redirect('institute_staff')


def institute_staff_update(request,id):
    var= Staff.objects.filter(id=id)
    vars=Staff.objects.get(id=id)
    ba = Staff.objects.all()
    return render(request,'institute_staff_update.html',{'ba':ba,'var':var,'vars':vars})



def institute_staff_updatesave(request,id):
    if request.method == 'POST':
        var = Staff.objects.get(id=id)
        var.name= request.POST.get('name')
        var.desig= request.POST.get('desig')
        var.department= request.POST.get('department')
        var.contact= request.POST.get('contact')
        var.photo= request.POST.get('photo')
        var.email= request.POST.get('email')
        var.username= request.POST.get('username')
        var.password= request.POST.get('password')
        var.check= request.POST.get('check')
        var.save()
        m="Updated successfully"
        return render(request,'institute_staff_update.html',{'m':m})   

def institute_admission(request):
    if request.method == 'GET':
        data = Admission.objects.all()
        var=Portions.objects.all()
        return render(request,"institute_admission.html",{'data':data,'var':var})
    else:
        sname = request.POST['sname']
        caddress = request.POST['caddress']
        paddress = request.POST['paddress']
        dob = request.POST['dob']
        gender = request.POST['gender']
        father = request.POST['father']
        foccu = request.POST['foccu']
        fcontact = request.POST['fcontact']
        mother = request.POST['mother']
        moccu = request.POST['moccu']
        mcontact = request.POST['mcontact']
        quali = request.POST['quali']
        marks = request.POST['marks']
        certificate = request.POST['certificate']
        trans = request.POST['trans']
        blood = request.POST['blood']
        clas= Portions.objects.get(id=request.POST['sclass'])
        username=request.POST['username']
        password=request.POST['password']
        photo=request.POST['photo']
        print(clas)
        new = Admission(sname=sname,caddress=caddress,paddress=paddress,dob=dob,photo=photo,
        gender=gender,father=father,foccu=foccu,fcontact=fcontact,mother=mother,moccu=moccu,mcontact=mcontact,
        quali=quali,marks=marks,certificate=certificate,blood=blood,portion_id=clas,trans=trans,username=username,password=password)
        new.save()
        return redirect('institute_admission')
    
def institute_admission_delete(request,id):
    var = Admission.objects.get(id=id)
    var.delete()
    return redirect('institute_admission')

def institute_transport(request):
    if request.method == 'GET':
        data = Bus.objects.all()
        a=Staff.objects.all()
        b=driver.objects.all()
        return render(request,"institute_transport.html",{'a':a,'b':b,'data':data})
    else:
        bno = request.POST['bno']
        regno=request.POST['regno']
        drive=driver.objects.get(dname=request.POST['driver'])
        Staf= Staff.objects.get(name=request.POST['staff'])
        new = Bus(bno=bno,regno=regno,driver=drive,Staff=Staf)
        new.save()
        return redirect('institute_transport')
    
def institute_transport_delete(request,id):
    var = Bus.objects.get(id=id)
    var.delete()
    return redirect('institute_transport')

def institute_bus(request):
    return render(request,"institute_bus.html") 


def driver_details(request):
    if request.method == 'GET':
        data = driver.objects.all()
        return render(request,"driver_details.html",{'data':data})
    else:
        dname = request.POST['dname']
        dphoto = request.POST['dphoto']
        dcontact = request.POST['dcontact']
        daddress= request.POST['daddress']
        demail= request.POST['demail']
        dlicesence=request.POST['dlicesence']
        accname=request.POST['accname']
        accno=request.POST['accno']
        ifsc=request.POST['ifsc']
        new = driver(dname=dname,dphoto=dphoto,dcontact=dcontact,
        daddress=daddress,demail=demail,dlicesence=dlicesence,accname=accname,accno=accno,ifsc=ifsc)
        new.save()
        return redirect('driver_details')

def driver_details_delete(request,id):
    var = Bus.objects.get(id=id)
    var.delete()
    return redirect('driver_details')   


def bus_details(request,id):
    if request.method == 'GET':
        h=Bus.objects.get(id=id)
        data = trans_details.objects.filter(bus_id=h)
        return render(request,"bus_details.html",{'data':data,'h':h})
    else:
        student_name = request.POST['student_name']
        batch=request.POST['batch']
        pickup = request.POST['pickup']
        destination = request.POST['destination']
        gender = request.POST['gender']
        contact = request.POST['contact']
        guardname = request.POST['guardname']
        guardcontact = request.POST['guardcontact']
        bfee=request.POST['bfee']
        h=Bus.objects.get(id=id)
        drive=h.driver
        staf=h.Staff
        new = trans_details(student_name=student_name,batch=batch,pickup=pickup,destination=destination,
        gender=gender,contact=contact,guardname=guardname,guardcontact=guardcontact,bfee=bfee,
        Staff_id=staf,driver_id=drive,bus_id=h)
        new.save()
        return redirect(bus_details, id=h.id)

 

def exam_result(request):
    return render(request,"exam_result.html")

def classes(request):
    return render(request,"classes.html")

def add_onlineclass(request):
    if request.method == 'GET':
        var=Portions.objects.all()
        var1=Staff.objects.all()
        data=Online.objects.all()
        return render(request,"add_onlineclass.html",{'var':var,'var1':var1,'data':data})
    else:
        topic=request.POST['topic']
        date = request.POST['date']
        stime = request.POST['stime']
        etime = request.POST['etime']
        thumb = request.POST['thumb']
        url = request.POST['url']
        onlineclass=Portions.objects.get(name=request.POST['onlineclass'])
        teacher=Staff.objects.get(name=request.POST['teacher'])
        new = Online(topic=topic,date=date,stime=stime,etime=etime,
        thumb=thumb,url=url,portions_id=onlineclass,staff_id=teacher)
        new.save()
        return redirect(add_onlineclass)

def add_recordedclass(request):
    if request.method == 'GET':
        v=Portions.objects.all()
        d=Recorded.objects.all()
        return render(request,"add_recordedclass.html",{'var':v,'data':d})
    else:
        topic=request.POST['topic']
        sub=request.POST['sub']
        thmb = request.POST['thmb']
        url = request.POST['url']
        recordedclass=Portions.objects.get(name=request.POST['recordedclass'])
        re= Recorded(topic=topic,thmb=thmb,url=url,portions_id=recordedclass,sub=sub)
        re.save()
        return redirect(add_recordedclass)

def add_studymaterial(request):
    if request.method == 'GET':
        var=Portions.objects.all()
        data=Studymaterial.objects.all()
        return render(request,"add_studymaterial.html",{'var':var,'data':data})
    else:
        subject=request.POST['subject']
        pdfnote=request.POST['pdfnote']
        thumb = request.POST['thumb']
        study=Portions.objects.get(name=request.POST['mat'])
        re= Studymaterial(subject=subject,pdfnote=pdfnote,thumb=thumb,portions_id=study)
        re.save()
        return redirect(add_studymaterial)

def add_class(request):
        if request.method == 'GET':
            data=Portions.objects.all()
            return render(request,"add_class.html",{'data':data})
        else:
            clas=request.POST['cls']
            div=request.POST['div']
            sub1 = request.POST['sub1']
            sub2 = request.POST['sub2']
            sub3 = request.POST['sub3']
            sub4 = request.POST['sub4']
            sub5 = request.POST['sub5']
            sub6 = request.POST['sub6']
            sub7 = request.POST['sub7']
            sub8 = request.POST['sub8']
            sub9 = request.POST['sub9']
            sub10 = request.POST['sub10']
            re= Portions(name=clas,div=div,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,sub7=sub7,sub8=sub8,sub9=sub9,sub10=sub10)
            re.save()
            return redirect(add_class)

def student_fee(request):
    if request.method == 'GET':
        var=Admission.objects.all()
        data=Fee.objects.all()
        return render(request,"student_fee.html",{'var':var,'data':data})
    else:
        admsnfee=request.POST['afee']
        tutfee=request.POST['tfee']
        unifee = request.POST['ufee']
        busfee = request.POST['bfee']
        labfee = request.POST['lfee']
        exmfee = request.POST['efee']
        statu = request.POST['st']
        st=Admission.objects.get(sname=request.POST['stu'])
        re= Fee(student_id=st,admsnfee=admsnfee,tutfee=tutfee,exmfee=exmfee,unifee=unifee,labfee=labfee,busfee=busfee,status=statu)
        re.save()
        return redirect(student_fee)

   




#----------------student-------------#

def index_student(request):
    return render(request,"base_student.html")

def index_student_dashboard(request):
    return render(request,"index_student_dashboard.html")

def student_pr(request):
    return render(request,"student_pr.html")

def exams(request):
    return render(request,"exams.html")


def student_recordedclass(request):
    if request.method == 'GET':
        ids=request.session['admission_id']
        re=Recorded.objects.filter(portions_id_id=ids)
        return render(request,"recordedclass.html",{'rr':re})    

def student_onlineclass(request):
    if request.method == 'GET':
        ids=request.session['admission_id']
        dat=Online.objects.filter(portions_id_id=ids).filter(status="True")
        #dat=Online.objects.filter(status="True")
        currentdate=date.today()
        mem = datetime.now()
        currenttime=mem.strftime("%H:%M:%S")
        for i in dat:
            exp_date=i.date
            a= i.etime
            exp_time=a.strftime("%H:%M:%S")
            print(exp_time) 
            if currentdate>exp_date:
                value=Online.objects.get(id=i.id)
                value.status="False"
                value.save()
            elif currentdate==exp_date:
                if currenttime>exp_time:
                    value=Online.objects.get(id=i.id)
                    value.status="False"
                    value.save()
        return render(request,"onlineclass.html",{'dd':dat})

def student_studymaterial(request):
    ids=request.session['admission_id']
    data=Studymaterial.objects.filter(portions_id_id=ids)
    return render(request,"studymaterial.html",{'data':data})


def fees(request):
    # data = Fee.objects.all()
    ids=request.session['admission_id']
    print(ids)
    data=Fee.objects.filter(student_id_id=ids)
    return render(request,'fees.html',{'data':data})  

def student_librarycard(request):
    return render(request,"librarycard.html")

#---------------staff------------------#

def index_staff(request):
    s=request.session['staff_id']
    a=Staff.objects.get(id=s)
    h=a.check
    h1=h.split(',')
    print(h1)
    return render(request,"base_staff.html",{'a':a,'h1':h1})

def index_staff_dashboard(request):
    s=request.session['staff_id']
    a=Staff.objects.get(id=s)
    h=a.check
    h1=h.split(',')
    print(h1)
    return render(request,"index_staff_dashboard.html",{'a':a,'h1':h1})



def save_image(request):
    return render(request,"save_image.html")



#-------------------copies-----------------#
def staff(request):
    if request.method == 'GET':
        data = Staff.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')
        return render(request,"staff_copy.html",{'data':data,'h1':h1})
    else:
        name = request.POST.get('name')
        department = request.POST.get('department')
        contact = request.POST.get('contact')
        photo = request.POST.get('photo')
        desig= request.POST.get('desig')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        check = request.POST.get('coursename')
        new= Staff(name=name,department=department,desig=desig,contact=contact,photo=photo,email=email,
        username=username,password=password,check=check)
        new.save()
        return redirect('staff')


def staff_update(request,id):
    if request.method == 'POST':
        var = Staff.objects.get(id=id)
        var.name= request.POST.get('name')
        var.desig= request.POST.get('desig')
        var.department= request.POST.get('department')
        var.contact= request.POST.get('contact')
        var.photo= request.POST.get('photo')
        var.email= request.POST.get('email')
        # var.username= request.POST.get('username')
        var.password= request.POST.get('password')
        var.check= request.POST.get('coursename')
        var.save()
        m="Updated successfully"
        return redirect('staff') 

def staff_delete(request,id):
    var = Staff.objects.get(id=id)
    var.delete()
    return redirect('staff')

def fee(request):
    if request.method == 'GET':
        var=Admission.objects.all()
        data=Fee.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')
        return render(request,"fee_copy.html",{'var':var,'data':data,'h1':h1})
    else:
        admsnfee=request.POST['afee']
        tutfee=request.POST['tfee']
        unifee = request.POST['ufee']
        busfee = request.POST['bfee']
        labfee = request.POST['lfee']
        exmfee = request.POST['efee']
        statu = request.POST['st']
        st=Admission.objects.get(sname=request.POST['stu'])
        re= Fee(student_id=st,admsnfee=admsnfee,tutfee=tutfee,exmfee=exmfee,unifee=unifee,labfee=labfee,busfee=busfee,status=statu)
        re.save()
        return redirect('fee')



def visitor(request):
    if request.method == 'GET':
        data = Visitor.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')
        return render(request,"visitors.html",{'data':data,'h1':h1})
    else:
        name = request.POST['name']
        place = request.POST['place']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        guardian = request.POST['guardian']
        school = request.POST['school']
        gender = request.POST['gender']
        purpose = request.POST['purpose']
        time = request.POST['time']
        date = request.POST['date']
        new = Visitor(name=name,place=place,email=email,contact=contact,address=address,guardian=guardian,
        school = school,gender=gender,purpose=purpose,date=date,time=time)
        new.save()
        return redirect('visitor')
   

def visitor_delete(request,id):
    var = Visitor.objects.get(id=id)
    var.delete()
    return redirect('visitor')

def admission(request):
    if request.method == 'GET':
        data = Admission.objects.all()
        var=Portions.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')
        return render(request,"admission.html",{'data':data,'var':var,'h1':h1})
    else:
        sname = request.POST['sname']
        caddress = request.POST['caddress']
        paddress = request.POST['paddress']
        dob = request.POST['dob']
        gender = request.POST['gender']
        father = request.POST['father']
        foccu = request.POST['foccu']
        fcontact = request.POST['fcontact']
        mother = request.POST['mother']
        moccu = request.POST['moccu']
        mcontact = request.POST['mcontact']
        quali = request.POST['quali']
        marks = request.POST['marks']
        certificate = request.POST['certificate']
        trans = request.POST['trans']
        blood = request.POST['blood']
        clas= Portions.objects.get(id=request.POST['sclass'])
        username=request.POST['username']
        password=request.POST['password']
        photo=request.POST['photo']
        print(clas)
        new = Admission(sname=sname,caddress=caddress,paddress=paddress,dob=dob,photo=photo,
        gender=gender,father=father,foccu=foccu,fcontact=fcontact,mother=mother,moccu=moccu,mcontact=mcontact,
        quali=quali,marks=marks,certificate=certificate,blood=blood,portion_id=clas,trans=trans,username=username,password=password)
        new.save()
        return redirect('admission')


def admission_delete(request,id):
    var = Admission.objects.get(id=id)
    var.delete()
    return redirect('admission')

def lead(request):
    if request.method == 'GET':
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')

        return render(request,'lead.html',{'h1':h1})

def trans_copy(request):
    if request.method == 'GET':
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')
        return render(request,"trans_copy.html",{'h1':h1}) 

def driver_details_copy(request):
    if request.method == 'GET':
        data = driver.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')
        return render(request,"driver_details_copy.html",{'data':data,'h1':h1})
    else:
        dname = request.POST['dname']
        dphoto = request.POST['dphoto']
        dcontact = request.POST['dcontact']
        daddress= request.POST['daddress']
        demail= request.POST['demail']
        dlicesence=request.POST['dlicesence']
        accname=request.POST['accname']
        accno=request.POST['accno']
        ifsc=request.POST['ifsc']
        new = driver(dname=dname,dphoto=dphoto,dcontact=dcontact,
        daddress=daddress,demail=demail,dlicesence=dlicesence,accname=accname,accno=accno,ifsc=ifsc)
        new.save()
        return redirect('driver_details_copy')

def driver_details_copy_delete(request,id):
    var = Bus.objects.get(id=id)
    var.delete()
    return redirect('driver_details_copy')  


def institute_Transportation_copy(request):
    if request.method == 'GET':
        data = Bus.objects.all()
        a1=Staff.objects.all()
        b=driver.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        h=a.check
        h1=h.split(',')
        return render(request,"institute_transport_copy.html",{'a':a1,'b':b,'data':data,'h1':h1})
    else:
        bno = request.POST['bno']
        regno=request.POST['regno']
        drive=driver.objects.get(dname=request.POST['driver'])
        Staf= Staff.objects.get(name=request.POST['staff'])
        new = Bus(bno=bno,regno=regno,driver=drive,Staff=Staf)
        new.save()
        return redirect('institute_Transportation_copy')
    
def institute_transport_copy_delete(request,id):
    var = Bus.objects.get(id=id)
    var.delete()
    return redirect('institute_Transportation_copy')

def bus_details_copy(request,id):
    if request.method == 'GET':
        h=Bus.objects.get(id=id)
        data = trans_details.objects.filter(bus_id=h)
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        t=a.check
        h1=t.split(',')
        return render(request,"bus_details_copy.html",{'data':data,'h':h,'h1':h1})
    else:
        student_name = request.POST['student_name']
        batch=request.POST['batch']
        pickup = request.POST['pickup']
        destination = request.POST['destination']
        gender = request.POST['gender']
        contact = request.POST['contact']
        guardname = request.POST['guardname']
        guardcontact = request.POST['guardcontact']
        bfee=request.POST['bfee']
        h=Bus.objects.get(id=id)
        drive=h.driver
        staf=h.Staff
        new = trans_details(student_name=student_name,batch=batch,pickup=pickup,destination=destination,
        gender=gender,contact=contact,guardname=guardname,guardcontact=guardcontact,bfee=bfee,
        Staff_id=staf,driver_id=drive,bus_id=h)
        new.save()
        return redirect(bus_details_copy, id=h.id)

def classes_copy(request):
    if request.method == 'GET':
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        t=a.check
        h1=t.split(',')
        return render(request,"classes_copy.html",{'h1':h1})

def add_onlineclass_copy(request):
    if request.method == 'GET':
        var=Portions.objects.all()
        var1=Staff.objects.all()
        data=Online.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        t=a.check
        h1=t.split(',')
        return render(request,"add_onlineclass_copy.html",{'var':var,'var1':var1,'data':data,'h1':h1})
    else:
        topic=request.POST['topic']
        date = request.POST['date']
        stime = request.POST['stime']
        etime = request.POST['etime']
        thumb = request.POST['thumb']
        url = request.POST['url']
        onlineclass=Portions.objects.get(name=request.POST['onlineclass'])
        teacher=Staff.objects.get(name=request.POST['teacher'])
        new = Online(topic=topic,date=date,stime=stime,etime=etime,
        thumb=thumb,url=url,portions_id=onlineclass,staff_id=teacher)
        new.save()
        return redirect(add_onlineclass_copy)

def add_recordedclass_copy(request):
    if request.method == 'GET':
        v=Portions.objects.all()
        d=Recorded.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        t=a.check
        h1=t.split(',')
        return render(request,"add_recordedclass_copy.html",{'var':v,'data':d,'h1':h1})
    else:
        topic=request.POST['topic']
        sub=request.POST['sub']
        thmb = request.POST['thmb']
        url = request.POST['url']
        recordedclass=Portions.objects.get(name=request.POST['recordedclass'])
        re= Recorded(topic=topic,thmb=thmb,url=url,portions_id=recordedclass,sub=sub)
        re.save()
        return redirect(add_recordedclass_copy)

def add_studymaterial_copy(request):
    if request.method == 'GET':
        var=Portions.objects.all()
        data=Studymaterial.objects.all()
        s=request.session['staff_id']
        a=Staff.objects.get(id=s)
        t=a.check
        h1=t.split(',')
        return render(request,"add_studymaterial_copy.html",{'var':var,'data':data,'h1':h1})
    else:
        subject=request.POST['subject']
        pdfnote=request.POST['pdfnote']
        thumb = request.POST['thumb']
        study=Portions.objects.get(name=request.POST['mat'])
        re= Studymaterial(subject=subject,pdfnote=pdfnote,thumb=thumb,portions_id=study)
        re.save()
        return redirect(add_studymaterial_copy)

def add_class_copy(request):
        if request.method == 'GET':
            data=Portions.objects.all()
            s=request.session['staff_id']
            a=Staff.objects.get(id=s)
            t=a.check
            h1=t.split(',')
            return render(request,"add_class_copy.html",{'data':data,'h1':h1})
        else:
            clas=request.POST['cls']
            div=request.POST['div']
            sub1 = request.POST['sub1']
            sub2 = request.POST['sub2']
            sub3 = request.POST['sub3']
            sub4 = request.POST['sub4']
            sub5 = request.POST['sub5']
            sub6 = request.POST['sub6']
            sub7 = request.POST['sub7']
            sub8 = request.POST['sub8']
            sub9 = request.POST['sub9']
            sub10 = request.POST['sub10']
            re= Portions(name=clas,div=div,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,sub7=sub7,sub8=sub8,sub9=sub9,sub10=sub10)
            re.save()
            return redirect(add_class_copy)