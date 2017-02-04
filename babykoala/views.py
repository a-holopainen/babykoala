from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "names": {
            "name1": "rob1",
            "name2": "rob2",
            "name3": "rob3",
            "name4": "rob4",
            "name5": "rob5",
            "name6": "rob6"
        },
        "animals": [
            {
                "name": "bear",
                "weight": 400
            },
            {
                "name": "rabbit",
                "weight": 15
            },
            {
                "name": "whale",
                "weight": 4000
            }
        ]
    }

    return render(request, 'index.html', context)
