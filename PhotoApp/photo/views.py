from django.shortcuts import render, get_object_or_404
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos':photos})

#get_object_or_404: 모델로부터 데이터를 찾되, 없으면 404에러 반환 (데이터 찾는 기준: pk, 즉 id)
def photo_detail(request,pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo':photo})
