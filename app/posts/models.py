from django.db import models

# Create your models here.


class Post(models.Model):
    """
    인스타그램의 포스트
    """
    author =
    content =
    like_users = 'PostLike를 통한 Many-to-Many구현'
    created =
    pass

class PostComment(models.Model):
    """
    각 포스트이 댓글(Many-to-one)
    """
    pass

class PostLike(models.Model):
    """
    사용자가 좋아요 누른 Postwjdqhfmf wjwkd
    Many-to-many필드를 중간모델(Intermediate Model)을 거쳐 사용
    언제 생성되었는지를 Extra field로 저장!(created)
    """
    pass