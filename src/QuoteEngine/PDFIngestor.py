"""Ingestor to implement IngestorInterface for PDF files."""
from typing import List
import subprocess
import os
import random
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """Class to ingest PDF files."""

    allowed_doc_types = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Implement abstract class method for pdf files."""
        if not cls.can_ingest(path):
            raise f"Can't ingest {path}. Not a valid PDF file."

        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        file_ref = open(tmp, 'r')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\r\n').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)

        return quotes
