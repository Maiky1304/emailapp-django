from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail

def index(request):
    try:
        alert = request.session['alert']
    except KeyError:
        alert = None

    try:
        outbox = request.session['outbox']
    except KeyError:
        outbox = []
        request.session['outbox'] = list()
        
    return render(request, 'index.html', { 'alert': alert, 'outbox': outbox, 'total_size': len(outbox) })


def mail_send(request):
    email = request.POST['email']
    subject = request.POST['subject']
    content = request.POST['content']

    delivered = send_mail(
            subject=subject,
            message=content,
            from_email='mailapp@mg.bmt.fyi',
            recipient_list=[email]
        ) == True

    if delivered:
        request.session['outbox'].append(request.POST)

    request.session['alert'] = {
        'type': 'success',
        'message': 'Message was succesfully sent.'
    } if delivered else {
        'type': 'danger',
        'message': 'Message could not be delivered.'
    }
    return redirect('/')