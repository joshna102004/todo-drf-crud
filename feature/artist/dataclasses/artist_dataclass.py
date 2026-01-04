from dataclasses import dataclass
from typing import Optional

@dataclass
class ArtistData:
    name: str
    genre: Optional[str] = None
    debut_year: Optional[int] = None
