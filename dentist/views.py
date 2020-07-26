from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":

        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email to who ever u want !!
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['assistant@doc.com'],  # to whom
        )

        return render(request, 'contact.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message': message
        })
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def service(request):
    return render(request, 'service.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']
        '''
        # send email
        appointment = your_name + "" + your_phone + " " + your_time + "" + your_address + "" + your_scheldule + "" + your_time + "" + your_message
        send_mail(
            'Appointment_request',  # subject
            appointment,  # message
            your_email,  # from email
            ['assistant@doc.com'],  # to whom
        )
        '''

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_address': your_address,
            'your_scheldule': your_scheldule,
            'your_time': your_time,
            'your_message': your_message,
            'your_email': your_email
        })

    else:
        return render(request, 'home.html', {})
