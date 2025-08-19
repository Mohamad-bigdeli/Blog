from ..entities.post_entity import Post
from abc import ABC, abstractmethod
from typing import List, Optional

class PostRepository(ABC):
    
    @abstractmethod
    def get_list(self) -> List[Post]:
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Optional[Post]:
        pass
    
    @abstractmethod
    def create(self, post: Post) -> None:
        pass

    @abstractmethod
    def update(self, post_id:int, title: str=None, description: str=None) -> None:
        pass

    @abstractmethod
    def delete(self, post_id: int) -> None:
        pass