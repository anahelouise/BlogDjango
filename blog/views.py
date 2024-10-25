from django.shortcuts import render
from faker import Faker

fake = Faker ('pt_BR')

# Create your views here.
def index(request):
    posts = []
    for _ in range(5):
        posts.append({
            "title": fake.sentence(),
            "sumary": fake.paragraph(),
            "featured_image": None if _ % 2 == 0 else fake.image_url()
        })
    return render(request, 'index.html', {'posts': posts})