from django.http import HttpResponse
from pymail import settings
from django.core.mail import send_mail


def mail(request):
    subject = "Greetings"
    msg = "Hi good Morning !"
    to = "vinaykumar.6101993@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)
