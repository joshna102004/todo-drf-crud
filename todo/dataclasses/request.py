from dataclasses import dataclass
from typing import Optional

# Used for creating a new Todo (POST)
@dataclass
class TodoData:
    title: str
    description: str
    is_completed: bool = False

# Used for PUT / PATCH updates
@dataclass
class TodoUpdateData:
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
