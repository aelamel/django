from django.http.response import HttpResponse


def home(request):
    return HttpResponse("""
        <h1> Hello World </h1>
    """)