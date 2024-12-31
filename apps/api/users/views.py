from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class Login(LoginView):
    http_method_names = ["post"]

    @csrf_exempt
    def post(request):
        return HttpResponse("Hello again")
