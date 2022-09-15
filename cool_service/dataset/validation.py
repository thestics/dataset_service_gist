#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko

from abc import abstractmethod, ABC
from collections import defaultdict
from typing import Tuple, Iterable, Dict, List

from cool_service.integrations.services import get_countries, get_priority_codes


class Validator(ABC):
    """
    Abstract validator
    
    Factored out as a separate class as it is assumed that validation may be
    both row-wise and aggregate (e.g. sum of all values in a given column)
    """

    @abstractmethod
    def feed(self, data: dict, row_id: str):
        """
        Process row from the dataset
        
        :param data:   row data
        :param row_id: row identifier. Added to ease developer experience while
                       debugging
        :return:
        """

    @abstractmethod
    def result(self):
        """Get validation result"""


class RowwiseValidator(Validator):
    """Row-by-row validator"""

    def __init__(self):
        self._errors = {}

    @abstractmethod
    def validate_row(self, data: dict) -> Tuple[bool, str]:
        pass

    def feed(self, data: dict, row_id: str):
        valid, err_msg = self.validate_row(data)
        if not valid:
            self._errors[row_id] = err_msg

    def result(self):
        return self._errors


class LowestProfitValidator(RowwiseValidator):
    PROFIT_FIELD = "Total Profit"
    PROFIT_MARGIN = 1_000
    
    def validate_row(self, data: dict) -> Tuple[bool, str]:
        if self.PROFIT_FIELD not in data:
            return False, f"`{self.PROFIT_FIELD}` field is not found"
        if data[self.PROFIT_FIELD] < self.PROFIT_MARGIN:
            return False, f"`{self.PROFIT_FIELD}` value should not " \
                          f"be lower than {self.PROFIT_MARGIN}"
        return True, ""


class HighestCostValidator(RowwiseValidator):
    COST_FIELD = "Total Cost"
    COST_MARGIN = 5_000_000
    
    def validate_row(self, data: dict) -> Tuple[bool, str]:
        if self.COST_FIELD not in data:
            return False, f"`{self.COST_FIELD}` field is not found"
        if data[self.COST_FIELD] > self.COST_MARGIN:
            return False, f"`{self.COST_FIELD}` value should not " \
                          f"be higher than {self.COST_MARGIN}"
        return True, ""


class CountryRegionValidator(RowwiseValidator):
    COUNTRY_FIELD = 'Country'
    REGION_FIELD = 'Region'
    
    def __init__(self, countries_getter=get_countries):
        super().__init__()
        # NOTE: while this particular validator needs only one external call
        #       it's not hard to imagine row-wise endpoint calls. If so,
        #       a better approach should be proposed. Possible solutions:
        #       * `ThreadPoolExecutor`s task per call
        #       * async calls. Requires a lot of glue or async web framework
        #       * full read and then calls.
        #       * caching, as a simple mitigation
        # NOTE: we do not use external service directly to increase decoupling
        #       and ease our testing later
        self._country_to_region = {
            country.name: country.region
            for country in countries_getter()
        }
    
    def validate_row(self, data: dict) -> Tuple[bool, str]:
        if self.COUNTRY_FIELD not in data or self.REGION_FIELD not in data:
            return False, f"`{self.COUNTRY_FIELD}, {self.REGION_FIELD}`" \
                          f" fields are required."

        country = data[self.COUNTRY_FIELD]
        region = data[self.REGION_FIELD]
        if self._country_to_region[country] != region:
            return False, f"Incorrect {region=} for {country=}."
        return True, ""


class PriorityValidator(RowwiseValidator):
    ORDER_FIELD = 'Order Priority'
    
    def __init__(self, priority_getter=get_priority_codes):
        super().__init__()
        self._priorities = set(priority_getter())

    def validate_row(self, data: dict) -> Tuple[bool, str]:
        if self.ORDER_FIELD not in data:
            return False, f"`{self.ORDER_FIELD}` field is required"
        
        priority_val = data[self.ORDER_FIELD]
        if priority_val not in self._priorities:
            return False, f"Unexpected priority value {priority_val}"
        return True, ""


# NOTE: other validators are intentionally omitted, implementation is
#       straightforward


DEFAULT_VALIDATORS: Iterable[Validator] = (
    LowestProfitValidator(),
    HighestCostValidator(),

)


def validate(
        dataset: Iterable[dict],
        validators: Iterable[Validator] = DEFAULT_VALIDATORS
) -> Dict[str, List[str]]:
    """
    Validate dataset against a set of validators
    
    :param dataset:
    :param validators:
    :return: Errors[row_id: List[error description]]
    """
    for i, row in enumerate(dataset):
        for v in validators:
            v.feed(row, f"row: {i}")
        
    errors = defaultdict(list)
    for v in validators:
        for row_id, err in v.result().items():
            errors[row_id].append(err)
    
    return errors
