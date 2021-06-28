from django.shortcuts import redirect, render
from PList.models import Barangay, TravelerProfile, Trequest, Requirements, Status
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    barangays = Barangay.objects.all()
    return render(request, 'Login.html',{'barangays': barangays})

def new_item(request):
    barangayt_= Barangay.objects.create(zbarangay = request.POST['TBarangay'],municipal = request.POST['Amunicipal'],address = request.POST['Oaddress'])
    return redirect(f'/{barangayt_.id}/view_list')

def view_list(request,barangay_id):
    barangay_= Barangay.objects.get(id = barangay_id)
    #barangay = Tname.objects.filter(barangay = barangay_id)
    return render(request,'Sgnup.html', {'barangay': barangay_})

def add_item(request,barangay_id):
    barangay_= Barangay.objects.get(id= barangay_id)
    TravelerProfile.objects.create (Tname=request.POST['lname'],birthday = request.POST['Fbirthday'],gender = request.POST['Gender'],address = request.POST['Faddress'],cnumber = request.POST['ccnumber'],email = request.POST['eaddress'],barangay = barangay_)
    return redirect ('/signup2')

def edit(request, id):
    barangays = Barangay.objects.get(id=id)
    context = {'barangays':barangays}
    return render(request, 'ssuppp.html', context)

def update(request, id):
    barangay = Barangay.objects.get(id=id)
    barangay.zbarangay =request.POST['TBarangay']
    barangay.municipal =request.POST['Amunicipal']
    barangay.address=request.POST['Oaddress']
    barangay.save()
    return redirect('/')

def delete(request, id):

    barangay = Barangay.objects.get(id=id)
    barangay.delete()
    return redirect('/')


def signup2(request):


    return render(request, 'Signup.html')


def signup3(request):

    return render(request, 'ssup.html')

def signup4(request):

    return render(request, 'ssupp.html')











'''def home_page(request):
    barangays = Barangay.objects.all() 
    return render(request, 'home.html',{'barangays' : barangays })
def new

def login(request):
    #login_ = Barangay.objects.get(id=barangay_id)
    return render(request, 'Login.html')


def signup1(request):

    return render(request, 'Sgnup.html')

def signup2(request):


    return render(request, 'Signup.html')


def signup3(request):

    return render(request, 'ssup.html')

def signup4(request):

    return render(request, 'ssupp.html')'''







'''def new_list(request):
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
        res += x.fullname + x.email +'<br>'''


'''def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(rmyname =request.POST['myname'],igs =request.POST['gs'],nGen =request.POST['Gen'],cadds=request.POST['adds'],enum =request.POST['num'],semaladd=request.POST['emaladd'],list=list_)
    return redirect(f'/PList/{list_.id}/')'''
