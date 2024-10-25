from django.shortcuts import render
from faker import Faker

fake = Faker ('pt_BR')

# Create your views here.
def index(request):
    images = [
        '/static/img/image1.jpg',
        '/static/img/image2.jpg',
        '/static/img/image3.jpg',
    ]

    posts = []
    for _ in range(5):
        posts.append({
            "title": fake.sentence(),
            "sumary": fake.paragraph(),
            "featured_image": None if _ % 2 == 0 else fake.image_url()
            #"featured_imafe": none if i % 2 == 0 else images[i % len(images)]
        })
    return render(request, 'index.html', {'post': posts})
 
