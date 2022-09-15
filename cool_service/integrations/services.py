#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko

from typing import List

import pydantic.error_wrappers
import requests

from cool_service.integrations.err import SchemaValidationError
from cool_service.integrations.schemas import Country
from cool_service.settings import COUNTRIES_ENDPOINT, PRIORITY_ENDPOINT


def get_countries() -> List[Country]:
    resp = requests.get(COUNTRIES_ENDPOINT)
    resp.raise_for_status()
    
    data = resp.json()
    try:
        return [Country(**obj) for obj in data]
    except pydantic.error_wrappers.ValidationError as e:
        raise SchemaValidationError(
            "Unable to fetch countries. Schema validation failed"
        ) from e


def get_priority_codes() -> List[str]:
    resp = requests.get(PRIORITY_ENDPOINT)
    resp.raise_for_status()

    data = resp.json()
    if (not isinstance(data, list) or
            any(not isinstance(item, str) for item in data)):
        raise SchemaValidationError(
            "Unable to fetch priority codes. Schema validation failed"
        )
    return data
