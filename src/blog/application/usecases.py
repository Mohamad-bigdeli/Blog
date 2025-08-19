from ..domain.repositories.post_repository import PostRepository
from ..domain.entities.post_entity import Post
from typing import Optional, List
from django.core.exceptions import ValidationError


class PostService:
    
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def get_post(self, post_id: int) -> Optional[Post]:
        try:
            return self.repo.get_by_id(post_id)
        except Exception as e:
            raise ValidationError(str(e))
        
    def get_posts(self) -> List[Post]:
        return self.repo.get_list()
    
    def create(self, title: str, descriptoin: str) -> None:
        post = Post(title=title, description=descriptoin)
        self.repo.create(post=post)
    
    def update(self, post_id: int, title: str, description: str) -> None:
        try:
            return self.repo.update(post_id=post_id, title=title, description=description)
        except Exception as e:
            raise ValidationError(str(e))
    
    def delete(self, post_id: int):
        try:
            return self.repo.delete(post_id=post_id)
        except Exception as e:
            raise ValidationError(str(e))
    
        