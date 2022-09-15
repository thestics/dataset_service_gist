#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko

import pytest

from cool_service.integrations.schemas import Country


@pytest.fixture()
def mock_get_countries_dict():
    return [{
        "code": "TD", "name": "Chad", "description": "Foo",
        "region": "Sub-Saharan Africa"
    }]


@pytest.fixture()
def mock_get_countries_response(mock_get_countries_dict):
    return lambda: [
        Country(**o) for o in mock_get_countries_dict
    ]


@pytest.fixture()
def mock_get_priority_codes_response():
    return lambda: [
        "C", "L", "M", "H"
    ]
