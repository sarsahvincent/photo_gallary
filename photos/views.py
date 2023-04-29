from django.shortcuts import render, redirect
from .models import Category, Photo


# Create your views here.


def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        # get all photos, go into the category , get the name of the category
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    print("categories", categories)
    context = {
        "categories": categories,
        "photos": photos
    }

    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)

    context = {
        'photo': photo
    }
    return render(request, 'photos/photo.html', context)


def add_photo(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            # this will check if there is a category with the same name as the new name
            # if it's true, if you will just update the name , if not then it will go create a new one
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        Photo.objects.create(
            category=category,
            description=data['description'],
            image=image
        )

        return redirect('gallery')

    context = {
        'categories': categories
    }
    return render(request, 'photos/add.html', context)
