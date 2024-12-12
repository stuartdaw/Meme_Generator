"""Ingestor to encapsulate other document ingestors."""
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """Class to encapsulate ingestion methods."""

    ingestors = [CSVIngestor, TXTIngestor, DOCXIngestor, PDFIngestor,]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse all document type by using the other ingestors."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
