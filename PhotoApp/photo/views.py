from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos':photos})

#get_object_or_404: 모델로부터 데이터를 찾되, 없으면 404에러 반환 (데이터 찾는 기준: pk, 즉 id)
def photo_detail(request,pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo':photo})

def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            #commit=True가 default. 만약 False로 설정하면, 바로 데이터베이스에 저장하지 않는다. 따라서 save()를 추가로 해줘야 함.
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_post.html', {'form': form})

def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        #instance : 수정 대상이 될 데이터 설정
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form':form})
