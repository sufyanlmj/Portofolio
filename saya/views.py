from django.shortcuts import render, redirect
from .forms import *

app_name = 'saya'

def home(request):
    profile = Profile.objects.all()
    about = Abaut.objects.all()
    sertifikat = Sertifikat.objects.all()
    project = Project.objects.all()

    context = {
        'active_menu': 'about',
        'show_hello': True,
        'profile': profile,
        'about': about,
        'sertifikat': sertifikat,
        'project': project,
    }
    return render(request, 'home.html', context)

def dasbor(request):
    profile = Profile.objects.all()

    context = {
        'active_menu': 'dasbor',
        'profile': profile,
    }
    return render(request, 'dasbor.html', context)

def daftar(request):
    data_semua = []

    for p in Profile.objects.all():
        data_semua.append({
            'type': 'Profile',
            'col1': p.name,
            'col2': p.age,
            'col3': p.email,
        })

    for a in Abaut.objects.all():
        data_semua.append({
            'type': 'About',
            'col1': a.judul,
            'col2': a.tanggal,
            'col3': a.deskripsi,
        })

    for s in Sertifikat.objects.all():
        data_semua.append({
            'type': 'Sertifikat',
            'col1': s.judul_sertifikat,
            'col2': s.tanggal,
            'col3': s.deskripsi,
        })

    for pr in Project.objects.all():
        data_semua.append({
            'type': 'Project',
            'col1': pr.judul,
            'col2': '',
            'col3': pr.deskripsi,
        })

    context = {
        'data_semua': data_semua
    }
    return render(request, 'daftar.html', context)


# ABOUT
def about(request):
    profile = Profile.objects.all()
    about = Abaut.objects.all()
    if request.method == 'POST':
        form = AbautForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = AbautForm()
    context = {
        'active_menu': 'about',
        'form': form,
        'profile': profile,
        'about': about,
    }
    return render(request, 'about.html', context)

def about_create(request):
    if request.method == 'POST':
        form = AbautForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AbautForm()
    context = {
        'active_menu': 'about',
        'form': form,
    }
    return render(request, 'form.html', context)

def about_update(request, pk):
    about = Abaut.objects.get(pk=pk)
    if request.method == 'POST':
        form = AbautForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = AbautForm(instance=about)
    context = {
        'active_menu': 'about',
        'form': form,
    }
    return render(request, 'form.html', context)

def about_delete(request, pk):
    about = Abaut.objects.get(pk=pk)
    about.delete()
    return redirect('saya:home')

# PROFILE
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profile.html', context)

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = ProfileForm()
    context = {
        'active_menu': 'profile',
        'form': form,
    }
    return render(request, 'form.html', context)

def profile_update(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'active_menu': 'profile',
        'form': form,
    }
    return render(request, 'form.html', context)

def profile_delete(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile.foto.delete(save=False)
    profile.delete()
    return redirect('saya:home')



# SERTIFIKAT
def sertifikat(request):
    profile = Profile.objects.all()
    sertifikat = Sertifikat.objects.all()
    if request.method == 'POST':
        form = SertifikatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = SertifikatForm()
    context = {
        'active_menu': 'sertifikat',
        'form': form,
        'profile': profile,
        'sertifikat': sertifikat,

    }
    return render(request, 'sertifikat.html', context)

def sertifikat_create(request):
    if request.method == 'POST':
        form = SertifikatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SertifikatForm()
    context = {
        'active_menu': 'sertifikat',
        'form': form,
    }
    return render(request, 'form.html', context)

def sertifikat_update(request, pk):
    sertifikat = Sertifikat.objects.get(pk=pk)
    if request.method == 'POST':
        form = SertifikatForm(request.POST, instance=sertifikat)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = SertifikatForm(instance=sertifikat)
    context = {
        'active_menu': 'sertifikat',
        'form': form,
    }
    return render(request, 'form.html', context)

def sertifikat_delete(request, pk):
    sertifikat = Sertifikat.objects.get(pk=pk)
    sertifikat.foto.delete(save=False)
    sertifikat.delete()
    return redirect('saya:home')



# PROJECT
def project(request):
    profile = Profile.objects.all()
    project = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = ProjectForm()
    context = {
        'active_menu': 'projects',
        'form': form,
        'project': project,
        'profile': profile
    }
    return render(request, 'project.html', context)

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = ProjectForm()
    context = {
        'active_menu': 'projects',
        'form': form,
    }
    return render(request, 'form.html', context)

def project_update(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = ProjectForm(instance=project)
    context = {
        'active_menu': 'projects',
        'form': form,
    }
    return render(request, 'form.html', context)

def project_delete(request, pk):
    project = Project.objects.get(pk=pk)
    project.foto.delete(save=False)
    project.delete()
    return redirect('saya:home')




# SKILLS
def skills(request):
    profile = Profile.objects.all()

    context = {
        'active_menu': 'skills',
        'profile': profile,
    }
    return render(request, 'skill.html', context)

def design(request):
    profile = Profile.objects.all()
    design = Design.objects.all()
    context = {
        'active_menu': 'design',
        'design': design,
        'profile': profile,
    }
    return render(request, 'design.html', context)

def design_create(request):
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DesignForm()
    context = {
        'active_menu': 'design',
        'form': form,
    }
    return render(request, 'form.html', context)

def design_update(request, pk):
    design = Design.objects.get(pk=pk)
    if request.method == 'POST':
        form = DesignForm(request.POST, instance=design)
        if form.is_valid():
            form.save()
            return redirect('saya:home')
    else:
        form = DesignForm(instance=design)
    context = {
        'active_menu': 'design',
        'form': form,
    }
    return render(request, 'form.html', context)

def design_delete(request, pk):
    design = Design.objects.get(pk=pk)
    design.foto.delete(save=False)
    design.delete()
    return redirect('saya:home')