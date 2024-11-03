from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import datetime


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def owner_register(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        img = request.FILES['img']
        aa = Tbl_User(idproof=img, name=name, phone=phone, address=address, email=email, pswd=pswd, status='pending',
                      user_type='owner')
        aa.save()
        txt = """<script>alert('success...');window.location='/owner_register/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'register.html')

def buyer_reg(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        img = request.FILES['img']
        aa = Tbl_User(idproof=img, name=name, phone=phone, address=address, email=email, pswd=pswd, status='pending',
                      user_type='buyer')
        aa.save()
        txt = """<script>alert('success...');window.location='/buyer_reg/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'buyer_reg.html')

def driver_reg(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        img = request.FILES['img']
        aa = Tbl_User(idproof=img, name=name, phone=phone, address=address, email=email, pswd=pswd, status='pending',
                      user_type='driver')
        aa.save()
        txt = """<script>alert('success...');window.location='/driver_reg/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'driver_reg.html')

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pswd"]
        chk = Tbl_User.objects.filter(email=email, pswd=password, user_type="admin")
        chk1 = Tbl_User.objects.filter(email=email, pswd=password, user_type="owner", status='approved')
        chk2 = Tbl_User.objects.filter(email=email, pswd=password, user_type="buyer")
        chk3 = Tbl_User.objects.filter(email=email, pswd=password, user_type="police")
        chk4 = Tbl_User.objects.filter(email=email, pswd=password, user_type="driver", status='approved')

        if chk:
            for x in chk:
                request.session['id'] = x.id
            return render(request, 'Admin/admin_home.html')
        elif chk1:
            for x in chk1:
                request.session['id'] = x.id
            return render(request, 'Owner/owner_home.html')
        elif chk2:
            for x in chk2:
                request.session['id'] = x.id
            return HttpResponseRedirect('/buyer_home/')
        elif chk3:
            for x in chk3:
                request.session['id'] = x.id
            return render(request, 'Police/police_home.html')
        elif chk4:
            for x in chk4:
                request.session['id'] = x.id
            return render(request, 'Driver/driver_home.html')
        else:
            return render(request, 'login.html', {'msg': 'Invalid login credentials.!'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
    return HttpResponseRedirect('/')

# -----------------------Admin-------------------------------
def admin_home(request):
    return render(request, 'Admin/admin_home.html')

def admin_ownerlist(request):
    var = Tbl_User.objects.all().filter(user_type='owner', status='pending')
    var1 = Tbl_User.objects.all().filter(user_type='owner', status='approved')
    var2 = Tbl_User.objects.all().filter(user_type='owner', status='rejected')
    return render(request, 'Admin/admin_ownerlist.html', {'var': var, 'var1': var1, 'var2': var2})

def admin_buyerlist(request):
    var = Tbl_User.objects.all().filter(user_type='buyer', status='pending')
    return render(request, 'Admin/admin_buyerlist.html', {'var': var})

def admin_driverlist(request):
    var = Tbl_User.objects.all().filter(user_type='driver', status='pending')
    var1 = Tbl_User.objects.all().filter(user_type='driver', status='approved')
    var2 = Tbl_User.objects.all().filter(user_type='driver', status='rejected')
    return render(request, 'Admin/admin_driverlist.html', {'var': var, 'var1': var1, 'var2': var2})

def admin_owner_approve(request):
    ii = request.GET['id']
    var = Tbl_User.objects.all().filter(id=ii).update(status='approved')
    return HttpResponseRedirect('/admin_ownerlist/')

def admin_owner_reject(request):
    ii = request.GET['id']
    var = Tbl_User.objects.all().filter(id=ii).update(status='rejected')
    return HttpResponseRedirect('/admin_ownerlist/')

def admin_driver_approve(request):
    ii = request.GET['id']
    var = Tbl_User.objects.all().filter(id=ii).update(status='approved')
    return HttpResponseRedirect('/admin_driverlist/')

def admin_driver_reject(request):
    ii = request.GET['id']
    var = Tbl_User.objects.all().filter(id=ii).update(status='rejected')
    return HttpResponseRedirect('/admin_driverlist/')

def admin_add_police(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        img = request.FILES['img']
        aa = Tbl_User(idproof=img, name=name, phone=phone, address=address, email=email, pswd=pswd, status='pending',
                      user_type='police')
        aa.save()
        txt = """<script>alert('success...');window.location='/admin_add_police/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Admin/admin_add_police.html')

def admin_policelist(request):
    var = Tbl_User.objects.all().filter(user_type='police')
    return render(request, 'Admin/admin_view_police.html', {'var': var})

def admin_feedback(request):
    var = Tbl_feedback.objects.all()
    return render(request, 'Admin/admin_feedback.html', {'var': var})

def admin_delete_feedback(request):
    ii = request.GET['id']
    var = Tbl_feedback.objects.all().filter(id=ii)
    var.delete()
    return HttpResponseRedirect('/admin_feedback/')


def admin_view_products(request):
    var = Tbl_Product.objects.all()
    return render(request, 'Admin/admin_view_products.html', {'var': var})


# -----------------------Owner-------------------------------
def owner_home(request):
    return render(request, 'Owner/owner_home.html')

def owner_profile(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    return render(request, 'Owner/owner_profile.html', {'var': var})

def owner_edit_profile(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    if request.method == "POST":
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        aa = Tbl_User.objects.all().filter(id=myid).update(phone=phone, address=address, email=email, pswd=pswd)
        txt = """<script>alert('success...');window.location='/owner_profile/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Owner/owner_edit_profile.html', {'var': var})

def owner_add_product(request):
    myid = request.session['id']
    if request.method == "POST":
        img = request.FILES['img']
        name = request.POST['name']
        number = request.POST['number']
        seat = request.POST['seat']
        specification = request.POST['specification']
        price = request.POST['price']
        uid = Tbl_User.objects.get(id=myid)
        aa = Tbl_Product(img=img, name=name, car_number=number, seat=seat, specification=specification, price=price,
                         user_id=uid, status='pending')
        aa.save()
        txt = """<script>alert('success...');window.location='/owner_add_product/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Owner/owner_add_product.html')

def owner_view_product(request):
    myid = request.session['id']
    var = Tbl_Product.objects.all().filter(user_id=myid)
    return render(request, 'Owner/owner_view_product.html', {'var': var})

def owner_edit_product(request):
    myid = request.session['id']
    if request.method == "POST":
        specification = request.POST['specification']
        price = request.POST['price']
        pid = request.POST['ii']
        aa = Tbl_Product.objects.all().filter(id=pid).update(specification=specification, price=price)
        txt = """<script>alert('success...');window.location='/owner_view_product/';</script>"""
        return HttpResponse(txt)
    else:
        ii = request.GET['id']
        var = Tbl_Product.objects.all().filter(id=ii)
        return render(request, 'Owner/owner_edit_product.html', {'var': var, 'ii': ii})

def owner_feedback(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    if request.method == "POST":
        feedback = request.POST['feedback']
        uid = Tbl_User.objects.get(id=myid)
        aa = Tbl_feedback(feedback=feedback, user_id=uid)
        aa.save()
        txt = """<script>alert('success...');window.location='/owner_feedback/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Owner/owner_feedback.html', {'var': var})

def owner_view_request(request):
    myid = request.session['id']
    own = Tbl_User.objects.all().filter(id=myid)
    for x in own:
        owner_email = x.email
    var = Tbl_booking.objects.all().filter(owner_email=owner_email, status='pending')
    var1 = Tbl_booking.objects.all().filter(owner_email=owner_email, status='approved')
    var2 = Tbl_booking.objects.all().filter(owner_email=owner_email, status='rejected')
    return render(request, 'Owner/owner_view_request.html', {'var': var, 'var1': var1, 'var2': var2})

def owner_approve_request(request):
    ii = request.GET['id']
    var = Tbl_booking.objects.all().filter(id=ii).update(status='approved')
    return HttpResponseRedirect('/owner_view_request/')

def owner_reject_request(request):
    ii = request.GET['id']
    var = Tbl_booking.objects.all().filter(id=ii).update(status='rejected')
    return HttpResponseRedirect('/owner_view_request/')

def owner_del_product(request):
    d_id=request.GET['id']
    val= Tbl_Product.objects.filter(id=d_id).delete()
    return HttpResponseRedirect('/owner_view_product/')


# -----------------------Buyer-------------------------------
def buyer_home(request):
    var = Tbl_Product.objects.all()
    # var = Tbl_Product.objects.all().filter(status='pending')
    return render(request, 'Buyer/buyer_home.html',{'var':var})

def buyer_profile(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    return render(request, 'Buyer/buyer_profile.html', {'var': var})

def buyer_edit_prof(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    if request.method == "POST":
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        aa = Tbl_User.objects.all().filter(id=myid).update(phone=phone, address=address, email=email, pswd=pswd)
        txt = """<script>alert('success...');window.location='/buyer_profile/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Buyer/buyer_edit_prof.html', {'var': var})

def buyer_feedback(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    if request.method == "POST":
        feedback = request.POST['feedback']
        uid = Tbl_User.objects.get(id=myid)
        aa = Tbl_feedback(feedback=feedback, user_id=uid)
        aa.save()
        txt = """<script>alert('success...');window.location='/buyer_feedback/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Buyer/buyer_feedback.html', {'var': var})

# def buyer_request_product(request):
#     myid = request.session['id']
#     if request.method == "POST":
#         idd = request.POST['ii']
#         owner = Tbl_Product.objects.all().filter(id=idd)
#         for x in owner:
#             owner_email = x.user_id.email
#         uid = Tbl_User.objects.get(id=myid)
#         pid = Tbl_Product.objects.get(id=idd)
#         date = datetime.datetime.today()
#         fromdate = request.POST['fromdate']
#         todate = request.POST['todate']
#         hrs = request.POST['hrs']
#         ii = request.GET['id']
#         print('ii-',ii)
#         total_price=request.POST['total_price']
#         var = Tbl_Product.objects.all().filter(id=idd).update(status='requested')
#         var1 = Tbl_Product.objects.filter(id=ii)
#         print('var1-',var)
#         aa = Tbl_booking(owner_email=owner_email, buyer_id=uid, product_id=pid, date=date, fromdate=fromdate,
#                          todate=todate, hrs=hrs,totalprice=total_price, status='pending')
#         aa.save()
#         # return HttpResponseRedirect('/buyer_home/')
#         return render(request, 'Buyer/buyer_request_form.html', {'var1':var1})

#     else:
#         ii = request.GET['id']
#         return render(request, 'Buyer/buyer_request_form.html', {'ii': ii})
def buyer_request_product(request):
    myid = request.session['id']
    if request.method == "POST":
        idd = request.POST['ii']
        owner = Tbl_Product.objects.all().filter(id=idd)
        # ownid=Tbl_User.objects.get(id=owner)
        for x in owner:
            owner_email = x.user_id.email
            ownid=x.user_id
        uid = Tbl_User.objects.get(id=myid)
        pid = Tbl_Product.objects.get(id=idd)
        date = datetime.datetime.today()
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        day = request.POST['hrs']
        # ii = request.GET['id']
        total_price=request.POST['total_price']
        var = Tbl_Product.objects.all().filter(id=idd).update(status='requested')
        # var1 = Tbl_Product.objects.filter(id=ii)
        aa = Tbl_booking(owner_email=owner_email, buyer_id=uid, product_id=pid,owner_id=owner_email, date=date, fromdate=fromdate,
                         todate=todate, day=day,totalprice=total_price, status='pending')
        aa.save()
        return render(request, 'Buyer/buyer_request_form.html')
    else:
        # ii = request.GET['id']
        ii = request.GET.get('id')

        product = Tbl_Product.objects.get(id=ii)
        price = product.price
        return render(request, 'Buyer/buyer_request_form.html', {'ii': ii, 'price': price})


def buyer_request_status(request):
    myid = request.session['id']
    var = Tbl_booking.objects.all().filter(buyer_id=myid)
    return render(request, 'Buyer/buyer_request_status.html', {'var': var})

def buyer_view_driver(request):
    var = Tbl_User.objects.all().filter(user_type='driver')
    return render(request, 'Buyer/buyer_view_driver.html', {'var': var})

def buyer_view_police(request):
    var = Tbl_User.objects.all().filter(user_type='police')
    return render(request, 'Buyer/buyer_view_police.html', {'var': var})

def buyer_driver_request(request):
    myid = request.session['id']
    if request.method == "POST":
        idd = request.POST['ii']
        driver = Tbl_User.objects.all().filter(id=idd)
        for x in driver:
            driver_email = x.email
            driver_phone = x.phone
            drv_id=x.id
        uid = Tbl_User.objects.get(id=myid)
        date = datetime.datetime.today()
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        hrs = request.POST['hrs']
        total_price=request.POST['total_price']
        aa = Tbl_driverBook(driver_phone=driver_phone, driver_email=driver_email, buyer_id=uid, date=date,
                            fromdate=fromdate, todate=todate, day=hrs, totalprice=total_price,driverid=drv_id,status='pending')
        aa.save()

        subject = 'Car Rent System Team'
        message = f'Hi , You have a request form customer Please login your account..'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [driver_email, ]
        send_mail(subject, message, email_from, recipient_list)
        # return HttpResponseRedirect('/doctor_view_patient/')

        return HttpResponseRedirect('/buyer_view_driver/')
    else:
        ii = request.GET['id']
        return render(request, 'Buyer/buyer_driver_request.html', {'ii': ii})

def buyer_driver_req_status(request):
    myid = request.session['id']
    print(myid)
    bid = Tbl_User.objects.all().filter(id=myid)
    for x in bid:
        buy_id = x.id
    
    var = Tbl_driverBook.objects.all().filter(status='pending',buyer_id=buy_id)
    var2 = Tbl_driverBook.objects.all().filter(status='approved',buyer_id=buy_id)
    var3 = Tbl_driverBook.objects.all().filter(status='rejected',buyer_id=buy_id)
    var4 = Tbl_driverBook.objects.all().filter(status='Paid',buyer_id=buy_id)

    # var4 = Tbl_driver_price.objects.all().filter()
    return render(request, 'Buyer/buyer_driver_req_status.html', {'var': var, 'var2': var2, 'var3': var3, 'var4':var4})

def buyer_complaints(request):
    myid = request.session['id']
    police = Tbl_User.objects.all().filter(user_type='police')
    if request.method == "POST":
        subject = request.POST['subject']
        description = request.POST['description']
        location = request.POST['location']
        police_email = request.POST['police']
        date = datetime.datetime.today()
        uid = Tbl_User.objects.get(id=myid)
        aa = Tbl_complaint(police_email=police_email, buyer_id=uid, subject=subject, description=description,
                           location=location, date=date, status='pending')
        aa.save()
        return HttpResponseRedirect('/buyer_complaint_status/')
    else:
        return render(request, 'Buyer/buyer_complaints.html', {'police': police})

def buyer_complaint_status(request):
    myid = request.session['id']
    var = Tbl_complaint.objects.all().filter(buyer_id=myid)
    return render(request, 'Buyer/buyer_complaint_status.html', {'var': var})

def buyer_product_review(request):
    myid=request.session['id']
    if request.method=="POST":
        review=request.POST['review']
        idd=request.POST['ii']
        pid=Tbl_Product.objects.get(id=idd)
        uid=Tbl_User.objects.get(id=myid)
        aa=Tbl_Review(review=review,product_id=pid,user_id=uid)
        aa.save()
        return HttpResponseRedirect('/buyer_home/')
    else:
        ii=request.GET['id']
        var=Tbl_Product.objects.all().filter(id=ii)
        rev=Tbl_Review.objects.all().filter(product_id=ii)
        return render(request,'Buyer/user_product_details.html',{'var':var,'ii':ii,'rev':rev})


# -----------------------Driver-------------------------------
def driver_home(request):
    return render(request, 'Driver/driver_home.html')
    
def driver_profile(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    return render(request, 'Driver/driver_profile.html', {'var': var})

def driver_edit_prof(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    if request.method == "POST":
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        aa = Tbl_User.objects.all().filter(id=myid).update(phone=phone, address=address, email=email, pswd=pswd)
        txt = """<script>alert('success...');window.location='/driver_profile/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Driver/driver_edit_prof.html', {'var': var})

def driver_view_req(request):
    myid = request.session['id']
    drive = Tbl_User.objects.all().filter(id=myid)
    for x in drive:
        driver_email = x.email
    var = Tbl_driverBook.objects.all().filter(driver_email=driver_email, status='pending')
    var1 = Tbl_driverBook.objects.all().filter(driver_email=driver_email, status='approved')
    var2 = Tbl_driverBook.objects.all().filter(driver_email=driver_email, status='rejected')
    return render(request, 'Driver/driver_view_req.html', {'var': var, 'var1': var1, 'var2': var2})

def driver_approve_request(request):
    ii = request.GET['id']
    var = Tbl_driverBook.objects.all().filter(id=ii).update(status='approved')
    return HttpResponseRedirect('/driver_view_req/')

def driver_reject_request(request):
    ii = request.GET['id']
    var = Tbl_driverBook.objects.all().filter(id=ii).update(status='rejected')
    return HttpResponseRedirect('/driver_view_req/')


# -----------------------Police-------------------------------
def police_home(request):
    return render(request, 'Police/police_home.html')

def police_profile(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    return render(request, 'Police/police_profile.html', {'var': var})

def police_edit_prof(request):
    myid = request.session['id']
    var = Tbl_User.objects.all().filter(id=myid)
    if request.method == "POST":
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        pswd = request.POST['pswd']
        aa = Tbl_User.objects.all().filter(id=myid).update(phone=phone, address=address, email=email, pswd=pswd)
        txt = """<script>alert('success...');window.location='/police_profile/';</script>"""
        return HttpResponse(txt)
    else:
        return render(request, 'Police/police_edit_profile.html', {'var': var})

def police_view_complaint(request):
    myid = request.session['id']
    police = Tbl_User.objects.all().filter(id=myid)
    for x in police:
        police_email = x.email
    var = Tbl_complaint.objects.all().filter(police_email=police_email, status='pending')
    var1 = Tbl_complaint.objects.all().filter(police_email=police_email, status='replied')
    return render(request, 'Police/police_view_complaint.html', {'var': var, 'var1': var1})

def police_reply(request):
    myid = request.session['id']
    if request.method == "POST":
        reply = request.POST['reply']
        idd = request.POST['ii']
        aa = Tbl_complaint.objects.all().filter(id=idd).update(reply=reply, status='replied')
        return HttpResponseRedirect('/police_view_complaint/')
    else:
        ii = request.GET['id']
        sub = Tbl_complaint.objects.all().filter(id=ii)
        return render(request, 'Police/police_reply.html', {'sub': sub, 'ii': ii})

def police_remove_complaint(request):
    ii = request.GET['id']
    var = Tbl_complaint.objects.all().filter(id=ii)
    var.delete()
    return HttpResponseRedirect('/police_view_complaint/')

def buyer_driver_payment(request):
    myid_b = request.session['id']
    booking_id = request.GET.get('id')
    print('bookingiddd',booking_id)
    did = None
    if booking_id:
        booking = Tbl_driverBook.objects.all().get(id=booking_id)
        total_price = booking.totalprice
        did=booking.driverid
        print('did--',did)
    else:
        total_price = 0
    if request.method == "POST":
       
        # if booking_id:
            id_b = Tbl_User.objects.get(id=myid_b)
            cname = request.POST['cname']
            cnum = request.POST['cnum']
            exp = request.POST['exp']
            cvv = request.POST['cvv']
            total_price=request.POST['price']
            booking_id=request.POST['booking_id']
            # driver = Tbl_User.objects.get(id=did)
            booking = Tbl_driverBook.objects.all().get(id=booking_id)
            d_id=booking.driverid
            driver = Tbl_User.objects.get(id=d_id)

            print(d_id)

            if booking_id:
                # did=booking.driverid
                pay = Tbl_buyer_payment(cardname=cname, cardnum=cnum, expiry=exp, cvvnum=cvv,price=total_price ,buyer_id=id_b, driver_id=driver,status='Paid')
                print(pay)
                pay.save()
                return HttpResponseRedirect('/buyer_home/')
    return render(request, 'Buyer/buyer_payment.html',{'total_price':total_price,'booking_id': booking_id})


def driver_price(request):
    if request.method == "POST":
        price = request.POST['price']
        Tbl_driver_price(price=price).save()
        return render(request, 'Driver/driver_home.html')
    return render(request, 'Driver/driver_price.html')


def payment_status(request):
    driver_id = request.session['id']
    var1 = Tbl_buyer_payment.objects.filter(driver_id=driver_id)
    return render(request, 'driver/payment_status.html', {'var1': var1})

def view_paymentdetails(request):
    var = Tbl_buyer_payment.objects.all()
    return render(request, 'Admin/All_payment_details.html', {'var': var})

# def buyer_car_payment(request):
#     myid_b = request.session['id']
#     if request.method == "POST":
#         id_buyer = Tbl_User.objects.filter(id=myid_b)
#         cname = request.POST['cname']
#         cnum = request.POST['cnum']
#         exp = request.POST['exp']
#         cvv = request.POST['cvv']
#         price = request.POST['price']
#         paycar = Tbl_buyer_car_payment(cardname=cname, cardnum=cnum, expiry=exp, cvvnum=cvv, price=price, buyer_id=id_buyer,status='Paid')
#         paycar.save()
#         return HttpResponseRedirect('/buyer_home/')
#     return render(request, 'Buyer/buyer_car_payment.html')
# def buyer_car_payment(request):
#     myid_b = request.session['id']
#     booking_id = request.GET.get('id')
    
#     if booking_id:
#         try:
#             booking = Tbl_booking.objects.get(id=booking_id)
#             total_price = booking.totalprice
#             ownid=booking.owner_email
#             print(ownid)
#         except Tbl_booking.DoesNotExist:
#             total_price = 0
#     else:
#         total_price = 0
  
#     if request.method == "POST":    
#         # id_buyer = Tbl_User.objects.filter(id=myid_b)
#             id_buyer = Tbl_User.objects.get(id=myid_b)
#             cname = request.POST['cname']
#             cnum = request.POST['cnum']
#             exp = request.POST['exp']
#             cvv = request.POST['cvv']
#             price = request.POST['price']
#             booking = Tbl_booking.objects.get(id=booking_id)
#             total_price = booking.totalprice
#             ownid=booking.owner_email
          
#             paycar = Tbl_buyer_car_payment(cardname=cname, cardnum=cnum, expiry=exp, cvvnum=cvv, price=price, buyer_id=id_buyer,owner_id=ownid,status='Paid')
#             paycar.save()
#             return HttpResponseRedirect('/buyer_home/')
def buyer_car_payment(request):
    myid_b = request.session['id']
    booking_id = request.GET.get('id')
    
    if booking_id:
        try:
            booking = Tbl_booking.objects.get(id=booking_id)
            total_price = booking.totalprice
            ownid = booking.owner_email
        except Tbl_booking.DoesNotExist:
            total_price = 0
            ownid = None
    else:
        total_price = 0
        ownid = None

    if request.method == "POST":    
        id_buyer = Tbl_User.objects.get(id=myid_b)
        cname = request.POST['cname']
        cnum = request.POST['cnum']
        exp = request.POST['exp']
        cvv = request.POST['cvv']
        price = request.POST['price']
        paycar = Tbl_buyer_car_payment(cardname=cname, cardnum=cnum, expiry=exp, cvvnum=cvv, price=price, buyer_id=id_buyer,status='Paid')
        paycar.save()
        return HttpResponseRedirect('/buyer_home/')

    # get the total price from Tbl_booking
    else:
        return render(request, 'Buyer/buyer_car_payment.html', {'total_price':total_price})

def car_payment_view(request):
    # myid = request.session['id']
    var1=Tbl_buyer_car_payment.objects.all()
    return render(request,'Owner/owner_car_payment_view.html',{'var1':var1})

# def buyer_chekout(request):
#     myid=request.session['id']
#     var_p=Tbl_buyer_payment.objects.all().filter(id=myid)
#     return render(request,'Buyer/buyer_product_checkout.html',{'var_p':var_p})
    
