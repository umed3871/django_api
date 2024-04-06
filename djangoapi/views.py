from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    # friends = ['ankit', 'mahesh', 'pinku'] to print non-dict objects set safe to false
    friends = {'ankit': 30, 'mahesh': 35, 'pinku': 40}
    return JsonResponse(friends)
