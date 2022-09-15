#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko
from pathlib import Path
from unittest.mock import Mock

import pytest

from cool_service.dataset.file_reader import read_file
from cool_service.err import ArgumentError


@pytest.fixture
def csv_file():
    f = open(Path(__file__).parent / 'data' / 'sales-short.csv', 'r')
    yield f
    f.close()


def test_csv_is_parsed_correctly(csv_file):
    # make sure we're evaluating iterator
    data = list(read_file(csv_file))
    expected = [{
        'Region': 'Sub-Saharan Africa', 'Country': 'Chad',
        'Item Type': 'Office Supplies', 'Sales Channel': 'Online',
        'Order Priority': 'L', 'Order Date': '1/27/2011',
        'Order ID': '292494523', 'Ship Date': '2/12/2011', 'Units Sold': '4484',
        'Unit Price': '651.21', 'Unit Cost': '524.96',
        'Total Revenue': '2920025.64', 'Total Cost': '2353920.64',
        'Total Profit': '566105.00'
    }]
    assert data == expected


def test_unsupported_type_rejected():
    file_stub = Mock()
    file_stub.name = 'abra-cadabra.foobar'
    
    with pytest.raises(ArgumentError):
        list(read_file(file_stub))