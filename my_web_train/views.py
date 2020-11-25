from django.shortcuts import render, redirect
# ดึงมาจาก template
from django.http import HttpResponse, HttpResponseRedirect
import datetime


def about(request):
    return HttpResponse('<h1> My name is Nattapong </h1>')

# test parameter path
def search(request, keyword, page):
    return HttpResponse(f'<h1>Keyword is : {keyword} Page is : {page} </h1>')

# test parameter path
def date(request, day, month, year):
    return HttpResponse(f'<h1><center> ค้นหาวันที่ : {day} เดือน : {month} ปี : {year} </center></h1>')

# test regular expression path
def drink(request, drink):
    return HttpResponse(f'<h1><center> You drink is : {drink} </center></h1>')

def find_page(request, key, page):
    page = int(page) #แปลง page จาก string to integer
    preview = ''
    if page > 1:
        preview =f'<a href="/find/{key}/{page - 1}"> Preview </a>'
    else:
        preview = ''
    next = f'<a href="/find/{key}/{page + 1}"> Next </a>'

    return HttpResponse(f'{preview} &nbsp&nbsp&nbsp&nbsp {next}')

# test query string
def map(request):
    type = request.GET.get('type', 'hybrid')
    lat = request.GET.get('lat', '13.1111')
    long = request.GET.get('long', '10.2222')
    zoom = request.GET.get('z', '11')

    return HttpResponse(f"Map type : {type} <br> Location : {lat}, {long}<br> Zoom : {zoom}")

# แสดงผลด้วย template HTML
def home(request):
    return render(request, 'index.html')

def variable(request):
    dt = datetime.datetime.today()
    data = {
        'title' : 'DTL Variable',
        'message' : 'Hello Django Template Language',
        'name' : 'Nattapong Ngamphak',
        'company' : 'TOT Public Company',
        'tel' : '0888888888',
        'email' : 'nattapong.ng@tot.co.th',
        'color' : ['red', 'green', 'blue'],
        'car' : {'t' : 'toyota', 'h' : 'Honda', 'a' : 'aston martin'},
        'date' : dt
    }
    return render(request, 'variable.html', data)

def tag_if(request):

    data = {
        'b' : 10,
        'score' : 85,
        'home_goal' : 4,
        'guest_goal' : 4
    }
    
    return render(request, 'tag.html', data)

def tag_loop(request):
    data = {
        'rang' : range(0, 6),
        'list' : ['red', 'blue', 'green', 'black'],
        'dict' : {'a' : 'ant', 'b' : 'boy', 'c' : 'cat'}
    }
    return render(request, 'tag.html', data)


# test filter
def filter_sample(request):
    data = {
        'str' : 'Nattapong',
        'list' : ['One', 'Two', 'Three'],
        'int' : 300,
        'float' : 1.5,
        'none' : None
    }

    return render(request, 'filter.html', data)

def filter_number(request):
    data = {
        'haha' : 555,
        'number2' : 10,
        'file_size' : 356789123333,
        'int' : 300,
        'float' : 1.5
    }

    return render(request, 'filter.html', data)

def filter_url(request):
    data = {
        'str1' : 'Please visit http://nattapong.pythonanywhere.com',
        'str2' : 'Sent email to nattapong.ng@tot.co.th',
        'str3' : 'visit my solarwinds http://nattapong.pythonanywhere.com/document/'
    }

    return render(request, 'filter.html', data)































