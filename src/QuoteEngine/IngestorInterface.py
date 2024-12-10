from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract class for ingestors. Take different quote docs and parse"""

    allowed_doc_types = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Take the doc path and determine if it can be ingested"""
        ext = path.split('.')[-1]
        return ext in cls.allowed_doc_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse the doc path. Different doc type classes to override"""
        pass

