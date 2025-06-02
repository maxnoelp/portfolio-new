from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from portfolio.landingpage.forms import ContactForm
from portfolio.landingpage.models import AboutMe
from portfolio.landingpage.models import Projects


def landing_page(request):
    projects = Projects.objects.all()
    me = AboutMe.objects.all()
    return render(
        request,
        "landingpage/index.html",
        {
            "projects": projects,
            "me": me,
            "frontend_stack": [
                {
                    "name": "Vue.js",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg",
                },
                {
                    "name": "Bootstrap",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg",
                },
                {
                    "name": "Flet",
                    "icon": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Vue.js_Logo_2.svg",
                },
            ],
            "backend_stack": [
                {
                    "name": "Django",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg",
                },
                {
                    "name": "Django CMS",
                    "icon": "https://upload.wikimedia.org/wikipedia/commons/7/74/Django_logo.svg",
                },
                {
                    "name": "PostgreSQL",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg",
                },
                {
                    "name": "Python",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
                },
            ],
            "tools_stack": [
                {
                    "name": "Git",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
                },
                {
                    "name": "Docker",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg",
                },
                {
                    "name": "Jira",
                    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jira/jira-original.svg",
                },
                {
                    "name": "AI",
                    "icon": "https://upload.wikimedia.org/wikipedia/commons/0/04/OpenAI_Logo.svg",
                },
            ],
        },
    )


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "Thanks for your message, we will get back to you soon!",
            )
            send_mail(
                subject="Anfrage Prinz-Code.de",
                message=(
                    f"Von: {form.cleaned_data['name']} "
                    f"({form.cleaned_data['email']})\n\n{form.cleaned_data['message']}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,  # <-- nicht hart verdrahten
                recipient_list=["noelpmax@gmail.com"],
            )

            return render(request, "landingpage/contact.html", {"form": ContactForm()})
    else:
        form = ContactForm()
    return render(request, "landingpage/contact.html", {"form": form})
