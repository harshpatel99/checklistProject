from django.shortcuts import render

from .models import Category, Checklist, User

# Create your views here.


def checkList(request):

    if request.method == 'POST':
        requestData = dict(request.POST)
        checked = User.objects.get(email="harsh@test.com")

        count = 0

        print(requestData)
        print(checked.checkedList.values())

        if "check" in requestData:
            for new in requestData['check']:
                if eval(new) not in checked.checkedList.values():
                    print(new)
                    User.objects.get(
                        email="harsh@test.com").checkedList.add(eval(new)['id'])
                    count += 1

            for old in checked.checkedList.values():
                if str(old) not in requestData['check']:
                    print(old)
                    User.objects.get(
                        email="harsh@test.com").checkedList.remove(old['id'])
                    count += 1

        categories = Category.objects.all()
        checkList = Checklist.objects.all().values()
        checked = User.objects.get(email="harsh@test.com").checkedList.values()

        return render(request, 'checklist/index.html', {
            'categories': categories,
            'checklist': checkList,
            'checkedItems': checked,
            'updated': count
        })

    categories = Category.objects.all()
    checkList = Checklist.objects.all().values()
    checked = User.objects.get(email="harsh@test.com").checkedList.values()

    return render(request, 'checklist/index.html', {
        'categories': categories,
        'checklist': checkList,
        'checkedItems': checked,
        'updated': 0
    })


""" def checkList(request):
    return render(request, 'checklist/index.html', {
        "checklist": [{
            "categories": [{
                "name": "essentials"
            }, {
                "name": "electronics"
            }, {
                "name": "kitchen"
            }, {
                "name": "clothing"
            }],
            "data": [{
                "id": "101",
                "name": "Passport",
                "category": "Essentials",
                "description": "",
                "needed": True,
                "url": "https://www.google.com",
                "checked": True
            },
                {
                "id": "102",
                "name": "Residence Permit",
                "category": "Essentials",
                "description": "",
                "needed": True,
                "url": "https://www.google.com",
                "checked": True
            },
                {
                "id": "103",
                "name": "Flight Ticket",
                "category": "Essentials",
                "description": "",
                "needed": False,
                "url": "",
                "checked": False
            },
                {
                "id": "104",
                "name": "Multi-currancy/Forex Car",
                "category": "Essentials",
                "description": "",
                "needed": False,
                "url": "https://www.google.com",
                "checked": True
            }, {
                "id": "201",
                "name": "Smartphone",
                "category": "Electronics",
                "description": "",
                "needed": True,
                "url": "",
                "checked": False
            },
                {
                "id": "202",
                "name": "Laptop",
                "category": "Electronics",
                "description": "",
                "needed": False,
                "url": "https://www.google.com",
                "checked": False
            },
                {
                "id": "203",
                "name": "Tablet/Kindle",
                "category": "Electronics",
                "description": "",
                "needed": False,
                "url": "",
                "checked": True
            },
                {
                "id": "204",
                "name": "Chargers",
                "category": "Electronics",
                "description": "",
                "needed": False,
                "url": "https://www.google.com",
                "checked": False
            }, {
                "id": "301",
                "name": "Cooker & Pan",
                "category": "Kitchen",
                "description": "",
                "needed": True,
                "url": "",
                "checked": True
            },
                {
                "id": "302",
                "name": "Water Bottle",
                "category": "Kitchen",
                "description": "",
                "needed": True,
                "url": "",
                "checked": False
            },
                {
                "id": "303",
                "name": "Rolling Board",
                "category": "Kitchen",
                "description": "",
                "needed": False,
                "url": "https://www.google.com",
                "checked": False
            },
                {
                "id": "304",
                "name": "Lunchbox",
                "category": "Kitchen",
                "description": "",
                "needed": True,
                "url": "https://www.google.com",
                "checked": True
            }, {
                "id": "401",
                "name": "Thermal Wear",
                "category": "Clothing",
                "description": "",
                "needed": True,
                "url": "",
                "checked": False
            },
                {
                "id": "402",
                "name": "Winter Jacket",
                "category": "Clothing",
                "description": "",
                "needed": False,
                "url": "",
                "checked": True
            },
                {
                "id": "403",
                "name": "Sweater",
                "category": "Clothing",
                "description": "",
                "needed": True,
                "url": "",
                "checked": False
            },
                {
                "id": "404",
                "name": "Suit",
                "category": "Clothing",
                "description": "",
                "needed": False,
                "url": "",
                "checked": True
            }]
        }]
    })
 """
