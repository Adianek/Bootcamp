from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def do_math(req, operation, arg1, arg2):
    result = None

    if operation == "add":
        result = arg1 + arg2
    elif operation == "sub":
        result = arg1 - arg2
    elif operation == "mul":
        result = arg1 * arg2
    elif operation == "div":
        if arg2 == 0:
            result = "Nie Dziel przez zero"
        else:
            result = arg1 / arg2
    return HttpResponse(result)
