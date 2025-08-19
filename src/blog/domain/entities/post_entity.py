from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class Post:
    title: str
    description: str
    id: UUID = uuid4()
    created: datetime = datetime.now()
    updated: Optional[datetime] = None