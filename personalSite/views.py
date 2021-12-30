# from django.shortcuts import render
from .models import Post
# from django.contrib import messages


from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID



# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

def homepg(request):
    # posts = Post.objects.all()
    return render(request, 'homepg.html')

def resumepg(request):
    # posts = Post.objects.get(id=pk)
    return render(request, 'resumepg.html')

# def message(request):
#     if request.method == "POST":
#         # name = request.POST['name']
#         # subject = request.POST['subject']
#         email = request.POST.get("email")
#         # body = request.POST['body']
#         print(email)
#         messages.success(request, "Email received. thank You! ") # message

#     # return render(request, "marketing/index.html")
#     return render(request, 'homepg.html')

# def subscription(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         body = request.POST['body']
#         print(email)
#         print(body)
#         messages.success(request, "Email received. thank You! ") # message

#     return render(request, "mail.html")

# Subscription Logic
def subscribe(name, subject, email, body):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {
            "NAME": name,
            "BODY": body,
            "SUBJECT": subject,
        }
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))




# Views here.
def subscription(request):
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        body = request.POST['body']
        subscribe(name, subject, email, body)                    # function to access mailchimp
        messages.success(request, "Thank you for your email! ") # message

    # return render(request, "mail.html")
    return render(request, "homepg.html")