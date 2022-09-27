from django.db import models

# Create your models here.

class designation(models.Model):
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class login(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                             related_name='design', null=True, blank=True)
    uname = models.CharField(max_length=240, null=True, blank=True)
    password = models.CharField(max_length=240, null=True, blank=True)
    

class Institute_details(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    contact = models.IntegerField()
    desig=models.CharField(max_length=400,default=0)
    image = models.ImageField(upload_to='gallery',default=0)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Staff(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    name = models.CharField(max_length=500)
    department = models.CharField(max_length=300)
    desig=models.CharField(max_length=400,default=0)
    contact = models.IntegerField()
    photo = models.ImageField(upload_to='gallery')
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.TextField(max_length=50)
    check= models.TextField(max_length=250,default=0) 
    


class Visitor(models.Model):
    name = models.CharField(max_length=500)
    place= models.CharField(max_length=250)
    contact = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=250)
    guardian = models.CharField(max_length=1000) 
    school = models.CharField(max_length=250)
    gender = models.CharField(max_length=100)
    purpose = models.CharField(max_length=1000) 
    date=models.DateField(auto_now_add=False, auto_now=False,null=True)
    time=models.TimeField(max_length=250,default=0)


class Portions(models.Model):
    name=models.CharField(max_length=250)
    div=models.CharField(max_length=250)
    sub1=models.CharField(max_length=250)
    sub2=models.CharField(max_length=250)
    sub3=models.CharField(max_length=250)
    sub4=models.CharField(max_length=250)
    sub5=models.CharField(max_length=250)
    sub6=models.CharField(max_length=250)
    sub7=models.CharField(max_length=250)
    sub8=models.CharField(max_length=250)
    sub9=models.CharField(max_length=250)
    sub10=models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Admission(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    portion_id = models.ForeignKey(Portions, on_delete=models.DO_NOTHING,null=True, blank=True)
    sname = models.CharField(max_length=500)
    caddress = models.CharField(max_length=250)
    paddress = models.CharField(max_length=250)
    dob = models.DateField(max_length=100)
    gender = models.CharField(max_length=100)
    father = models.CharField(max_length=1000)
    foccu = models.CharField(max_length=1000)
    fcontact = models.CharField(max_length=1000) 
    mother = models.CharField(max_length=1000,default=0)
    moccu = models.CharField(max_length=1000, default=0)
    mcontact = models.CharField(max_length=1000,default=0)
    quali = models.CharField(max_length=250)
    marks=models.IntegerField()
    certificate=models.FileField(upload_to='docx',max_length=250,null=True,blank=True)
    blood = models.CharField(max_length=250)
    username = models.CharField(max_length=100,default=0)
    password = models.CharField(max_length=150,default=0)
    trans=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='docx',max_length=250,null=True,blank=True)


class driver(models.Model):
    dname=models.CharField(max_length=250)
    dphoto=models.ImageField(upload_to='docx',max_length=250,null=True,blank=True)
    daddress=models.CharField(max_length=250)
    dcontact=models.CharField(max_length=250)
    demail=models.EmailField(max_length=250)
    dlicesence=models.CharField(max_length=250)
    accname=models.CharField(max_length=500, default=0) 
    accno=models.CharField(max_length=500, default=0)
    ifsc=models.CharField(max_length=500, default=0)


class Bus(models.Model):
    driver = models.ForeignKey(driver, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    Staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    bno=models.CharField(max_length=250) 
    photo=models.ImageField(upload_to='docx',max_length=250,null=True,blank=True)
    regno=models.CharField(max_length=250)
    
class trans_details(models.Model):
    driver_id = models.ForeignKey(driver, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    Staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    bus_id = models.ForeignKey(Bus, on_delete=models.DO_NOTHING,
                              null=True, blank=True)
    student_name=models.CharField(max_length=250) 
    batch=models.CharField(max_length=250)
    pickup=models.CharField(max_length=250)
    destination=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    contact=models.CharField(max_length=250)
    guardname=models.CharField(max_length=250)
    guardcontact=models.CharField(max_length=250)
    bfee=models.IntegerField()

class Recorded(models.Model):
    portions_id=models.ForeignKey(Portions, on_delete=models.DO_NOTHING,null=True, blank=True)
    topic=models.CharField(max_length=250,default=0)
    sub=models.CharField(max_length=250,default=0)
    thmb=models.ImageField(upload_to='docx',max_length=250,null=True,blank=True)
    url=models.URLField(default=0)

class Studymaterial(models.Model):
    portions_id=models.ForeignKey(Portions, on_delete=models.DO_NOTHING,null=True, blank=True)
    subject=models.CharField(max_length=250,null=True)
    pdfnote=models.ImageField(upload_to="media")
    thumb=models.ImageField(upload_to='media',max_length=250,null=True,blank=True)

class Online(models.Model):
    portions_id=models.ForeignKey(Portions, on_delete=models.DO_NOTHING,null=True, blank=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING,null=True, blank=True)
    sname=models.CharField(max_length=250,default=0)
    topic=models.CharField(max_length=250,default=0)
    date=models.DateField(max_length=250)
    stime=models.TimeField(max_length=250,default=0)
    etime=models.TimeField(max_length=250,default=0)
    thumb=models.ImageField(upload_to='docx',max_length=250,null=True,blank=True)
    url=models.URLField(default=0)
    status=models.CharField(max_length=250,default='True')

class Fee(models.Model):
    student_id=models.ForeignKey(Admission, on_delete=models.DO_NOTHING,null=True, blank=True)
    admsnfee=models.CharField(max_length=1000,default=0)
    tutfee=models.CharField(max_length=1000,default=0)
    exmfee=models.CharField(max_length=1000,default=0)
    busfee=models.CharField(max_length=1000,default=0)
    labfee=models.CharField(max_length=1000,default=0)
    unifee=models.CharField(max_length=1000,default=0)
    status=models.CharField(max_length=1000,default=0)






















































