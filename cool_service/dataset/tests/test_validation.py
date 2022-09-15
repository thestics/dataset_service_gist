#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko

import pytest
from cool_service.tests.fixtures import (
    mock_get_countries_dict,
    mock_get_countries_response,
    mock_get_priority_codes_response
)
from cool_service.dataset.validation import (
    LowestProfitValidator,
    HighestCostValidator,
    CountryRegionValidator,
    PriorityValidator,
    validate,
)


@pytest.fixture
def mock_validators(mock_get_countries_response,
                    mock_get_priority_codes_response):
    return [
        LowestProfitValidator(),
        HighestCostValidator(),
        CountryRegionValidator(countries_getter=mock_get_countries_response),
        PriorityValidator(priority_getter=mock_get_priority_codes_response)
    ]


@pytest.mark.parametrize(
    'total_profit', [0, 2_000]
)
@pytest.mark.parametrize(
    'total_cost', [10_000, 10_000_000]
)
@pytest.mark.parametrize(
    'country, region',
    [('Chad', 'Sub-Saharan Africa'), ('Chad', 'Boo')]
)
@pytest.mark.parametrize(
    'priority', ['L', 'NON-EXISTING']
)
def test_validation(
        total_profit,
        total_cost,
        country,
        region,
        priority,
        mock_validators,
        snapshot
):
    # NOTE: we could've just mocked data to validate with a fixture,
    # however this way we can reduce repetition by using `parametrize`
    # and define only those parts, which are changed
    data = [
        # do not hardcode field names to save ourselves from future
        # changes
        {
            LowestProfitValidator.PROFIT_FIELD:     total_profit,
            HighestCostValidator.COST_FIELD:        total_cost,
            CountryRegionValidator.COUNTRY_FIELD:   country,
            CountryRegionValidator.REGION_FIELD:    region,
            PriorityValidator.ORDER_FIELD:          priority
        }
    ]
    
    # NOTE: we can further improve testing quality by actually checking
    #       that needed validator fired, but for given task simple snapshot
    #       approach should be enough
    validation_status = validate(data, validators=mock_validators)
    snapshot.assert_match(validation_status)
