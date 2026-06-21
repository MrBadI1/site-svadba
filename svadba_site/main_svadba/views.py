from django.shortcuts import render, redirect

from .models import GuestResponse


def invite_view(request):

    if request.method == "POST":

        print(request.POST)

        name = request.POST.get("name")

        will_come = request.POST.get("will_come")

        alcohol = request.POST.getlist("alcohol")

        alcohol_comment = request.POST.get("alcohol_comment")

        GuestResponse.objects.create(

            name=name,

            will_come=(will_come == "yes"),

            alcohol=alcohol,

            alcohol_comment=alcohol_comment
        )

        return redirect("/")

    return render(request, "main/index.html")
