#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko

import csv
from typing import BinaryIO, Callable, Dict, Iterator

from cool_service.err import ArgumentError


FileReaderT = Callable[[BinaryIO], Iterator[dict]]


def _read_file_csv(file_data: BinaryIO) -> Iterator[dict]:
    return csv.DictReader(file_data)


def _read_file_xml(file_data: BinaryIO) -> Iterator[dict]:
    raise NotImplementedError


def _read_file_xls(file_data: BinaryIO) -> Iterator[dict]:
    raise NotImplementedError


READER_DISPATCHER: Dict[str, FileReaderT] = {
    "csv": _read_file_csv,
    # to be registered after implemented, to avoid NotImplementedError in prod
    # "xml": _read_file_xml,
    # "xls": _read_file_xls
}


def read_file(file_data: BinaryIO) -> Iterator[dict]:
    """
    Read and parse structured file
    
    For simplicity, we assume meaningful file was provided.
    This way we are relieved from actual file inspection (akin to
    `file <filename>` call in terminal and subsequent dispatch)
    """
    # TODO: we can add all support for .tar .zip archives right away,
    #       but for the sake of simplicity we won't
    file_ext = file_data.name.split('.')[-1]
    reader = READER_DISPATCHER.get(file_ext)

    if reader is None:
        # `file_ext` may be left with some gibberish if filename is broken
        # to keep exception readable, supply full file name instead
        raise ArgumentError(
            f"Unable to parse {file_data.name}. "
            f"Expected formats: {', '.join(READER_DISPATCHER.keys())}"
        )
    
    return reader(file_data)
