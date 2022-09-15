#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko
import pytest
import responses

from cool_service.tests.fixtures import (
    mock_get_countries_dict,
    mock_get_countries_response,
    mock_get_priority_codes_response
)
from cool_service import settings
from cool_service.integrations.services import get_countries, get_priority_codes


@pytest.fixture
def mock_countries_endpoint(mock_get_countries_dict):
    responses.add(
        responses.GET, settings.COUNTRIES_ENDPOINT,
        json=mock_get_countries_dict, status=200
    )


@pytest.fixture
def mock_priorities_endpoint(mock_get_priority_codes_response):
    responses.add(
        responses.GET, settings.PRIORITY_ENDPOINT,
        json=mock_get_priority_codes_response(), status=200
    )


@responses.activate
def test_countries_endpoint(
        mock_countries_endpoint,
        mock_get_countries_dict
):
    countries = get_countries()
    assert countries == mock_get_countries_dict


@responses.activate
def test_priorities_endpoint(
        mock_priorities_endpoint, mock_get_priority_codes_response
):
    priorities = get_priority_codes()
    assert priorities == mock_get_priority_codes_response()