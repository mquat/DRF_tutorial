#modeling: 현실에 있는 개체의 특징들을 뽑아, 이를 구성 요소로 만드는 과정
#migrations: "a verseion control system for your database schema"

#makemigrations: 업데이트된 모델 내용을 기록하여 파일로 만들어줌(migrations 폴더)
#(새로 만든 앱의 sql command를 생성하는 작업. python manage.py sqlmigrate 라고 치면, sql command를 볼 수 있다)

#migrate: makemigrations를 통해 생성된 파일을 실제 데이터베이스에 적용시키는 과정

from django.db import models

class Photo(models.Model):
    title       = models.CharField(max_length=50)
    author      = models.CharField(max_length=50)
    image       = models.CharField(max_length=200)
    description = models.TextField()
    price       = models.IntegerField()
