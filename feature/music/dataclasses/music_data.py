from dataclasses import dataclass

@dataclass
class MusicData:
    title: str
    artist: str
    genre: str = ""
    year: int | None = None
