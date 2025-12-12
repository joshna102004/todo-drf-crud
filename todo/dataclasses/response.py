from dataclasses import dataclass
from datetime import datetime

@dataclass
class TodoResponseData:
    id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime
