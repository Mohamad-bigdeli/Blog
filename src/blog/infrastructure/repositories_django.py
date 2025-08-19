from django.core.exceptions import ValidationError
from .models import Post
from ..domain.repositories.post_repository import PostRepository
from datetime import datetime


class DjangoPostRepository(PostRepository):
    
    def get_by_id(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist as e:
            raise ValidationError(str(e))
    
    def get_list(self):
        return Post.objects.all()
    
    def create(self, post):
        post = Post(
            id=post.id,
            title=post.title,
            description=post.description,
            created=post.created,
            updated=post.updated 
        )
        post.save()

    def update(self, post_id, title=None, description=None):
        try:
            post = Post.objects.get(id=post_id)
            post.title = title
            post.description = description
            post.updated = datetime.now()
            post.save()
        except Post.DoesNotExist as e:
            raise ValidationError(str(e))
    
    def delete(self, post_id):
        try:
            return Post.objects.filter(id=post_id).delete()
        except Post.DoesNotExist as e:
            raise ValidationError(str(e))