from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from .forms import *
from django.contrib import messages


def recipe_list(request):
    recipes = Recipe.objects.filter(is_active=True).order_by('-id')
    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipe/list.html', ctx)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ctx = {
        'recipe': recipe
    }
    return render(request, 'recipe/detail.html', ctx)


@login_required
def recipe_create(request, *args, **kwargs):
    form = RecipeCreateForm()
    if request.method == "POST":
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form.save_m2m()
            return redirect(reverse('recipes:detail', kwargs={"slug": obj.slug}))
    ctx = {
        'form': form
    }
    return render(request, 'recipe/create.html', ctx)


@login_required
def recipe_update(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    form = RecipeUpdateForm(instance=obj)
    if request.method == 'POST':
        form = RecipeUpdateForm(data=request.POST, instance=obj)
        if form.is_valid():
            return redirect(reverse('recipes:detail', kwargs={'slug': obj.slug}))
    ctx = {
        'form': form
    }
    return render(request, 'recipe/update.html', ctx)


@login_required
def recipe_delete(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, f"<b>{obj.title}</b> o'chirildi")
        return redirect('recipes:list')
    ctx = {
        'recipe': obj
    }
    return render(request, 'recipe/delete.html', ctx)
