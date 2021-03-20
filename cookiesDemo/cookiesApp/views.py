from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome page</h1>")


# set cookies TimeStap 35.00 video 8

def cookies_count_view(request):
    count = request.COOKIES.get('count',0)
    totalCount = int(count) + 1
    response = render(request, 'cookiesApp/cookie.html', context={'count': totalCount})
    # How set the cookies TimeStamp : 43:00 8th video
    response.set_cookie('count',totalCount)
    return response
    '''
    KEY - VALUE PAIR
    Cookies Present ==> get('key') return corresponding key VALUE
    Cookies Absent ==> get() la default value set panna mudiuim
                        cookies illanaa 5 is default value
                        eg: get('key',5)

    request.COOKIES('count',0)
    'count' = Cookies irrutha cookie count ah yaduthu vaikuim
    else
    'count' ah zero inu vaitchukuim

    -> each abd every time request varapothu cookies count ah increace pandra
        totalCount = int(count) + 1

    Note:- return in String values
    '''


    # Set Seesion ID timeStamp 59:00

def session_count_view(request):
    count = request.session.get('count', 0)
    totalCount = int(count) + 1
    # dict format
    request.session['scount'] = totalCount
    print(request.session.get_expiry_date())
    return render(request, 'cookiesApp/session.html', context={'scount': totalCount})

    # enga maintain yakaraa session ID db la store yakuim so * migrate * migrate kuduthatha db la update yakuim
