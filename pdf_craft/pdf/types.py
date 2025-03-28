from typing import Callable
from enum import auto, Enum


# func(completed_pages: int, all_pages: int) -> None
PDFPageExtractorProgressReport = Callable[[int, int], None]

class ORCLevel(Enum):
  Once = auto()
  OncePerLayout = auto()
