from django.shortcuts import render, redirect
from PList.models import  Barangay, TravelerProfile 


def home_page(request):
    barangays = Barangay.objects.all() 
    return render(request, 'homepage.html',{'barangays' : barangays })



def view_list(request, barangay_id):
    barangay_ = Barangay.objects.get(id=barangay_id)
    return render(request, 'SignUp.html', {'barangay': barangay_})


def new_list(request):
    barangay_ = Barangay.objects.create()
    #Item.objects.create(npet=request.POST['pet'],nname =request.POST['owner'],nAddress=request.POST['address'],nBreed =request.POST['breed'],nDay =request.POST['birthday'], barangay=barangay_)
    return redirect(f'/PList/{barangay_.id}/')

def add_item(request, barangay_id):
    barangay_ = Barangay.objects.get(id=barangay_id)
    #Item.objects.create(npet=request.POST['pet'],nBreed =request.POST['breed'],nDay =request.POST['birthday'],barangay=barangay_)
    return redirect(f'/PList/{barangay_.id}/')

def DataBarangay(request):
    userp = UserProfile(fullname="Justcasey", age="21", email="happykid@gmail.com", address="San antonio zambales")
    userp.save()

    userp = Barangay.objects.all()
    result = 'Printing all entries in UserProfile model : <br>'
    for x in userp:
        res += x.fullname+"<br>"

    userpp = Barangay.objects.get(id="1")
    res += 'Printing One Entry <br>'
    res += userpp.email

    res += '<br> Deleting an entry <br>'
    userpp.delete()

    userp = UserProfile(fullname="Justcasey", age="21", email="Justcasey@gmail.com", address="San antonio zambales")
    userp.save()
    res += 'Updating entry <br>'

    userp = UserProfile.objects.get(fullname="Justcasey")
    userp.Position = "Representative"
    userp.save()
    res = ""

    mf = UserProfile.objects.filter(fullname="Justcasey")
    res += "Found : %s results<br>"%len(qs)

    mf = UserProfile.objects.order_by(email="Justcasey@gmail.com")
    for x in qs:
        res += x.fullname + x.email +'<br>'


'''def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(rmyname =request.POST['myname'],igs =request.POST['gs'],nGen =request.POST['Gen'],cadds=request.POST['adds'],enum =request.POST['num'],semaladd=request.POST['emaladd'],list=list_)
    return redirect(f'/PList/{list_.id}/')'''