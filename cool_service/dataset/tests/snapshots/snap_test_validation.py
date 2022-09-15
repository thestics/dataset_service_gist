# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_validation[L-Chad-Boo-10000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000',
        "Incorrect region='Boo' for country='Chad'."
    ]
}

snapshots['test_validation[L-Chad-Boo-10000-2000] 1'] = {
    'row: 0': [
        "Incorrect region='Boo' for country='Chad'."
    ]
}

snapshots['test_validation[L-Chad-Boo-10000000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000',
        '`Total Cost` value should not be higher than 5000000',
        "Incorrect region='Boo' for country='Chad'."
    ]
}

snapshots['test_validation[L-Chad-Boo-10000000-2000] 1'] = {
    'row: 0': [
        '`Total Cost` value should not be higher than 5000000',
        "Incorrect region='Boo' for country='Chad'."
    ]
}

snapshots['test_validation[L-Chad-Sub-Saharan Africa-10000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000'
    ]
}

snapshots['test_validation[L-Chad-Sub-Saharan Africa-10000-2000] 1'] = {
}

snapshots['test_validation[L-Chad-Sub-Saharan Africa-10000000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000',
        '`Total Cost` value should not be higher than 5000000'
    ]
}

snapshots['test_validation[L-Chad-Sub-Saharan Africa-10000000-2000] 1'] = {
    'row: 0': [
        '`Total Cost` value should not be higher than 5000000'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Boo-10000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000',
        "Incorrect region='Boo' for country='Chad'.",
        'Unexpected priority value NON-EXISTING'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Boo-10000-2000] 1'] = {
    'row: 0': [
        "Incorrect region='Boo' for country='Chad'.",
        'Unexpected priority value NON-EXISTING'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Boo-10000000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000',
        '`Total Cost` value should not be higher than 5000000',
        "Incorrect region='Boo' for country='Chad'.",
        'Unexpected priority value NON-EXISTING'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Boo-10000000-2000] 1'] = {
    'row: 0': [
        '`Total Cost` value should not be higher than 5000000',
        "Incorrect region='Boo' for country='Chad'.",
        'Unexpected priority value NON-EXISTING'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Sub-Saharan Africa-10000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000',
        'Unexpected priority value NON-EXISTING'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Sub-Saharan Africa-10000-2000] 1'] = {
    'row: 0': [
        'Unexpected priority value NON-EXISTING'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Sub-Saharan Africa-10000000-0] 1'] = {
    'row: 0': [
        '`Total Profit` value should not be lower than 1000',
        '`Total Cost` value should not be higher than 5000000',
        'Unexpected priority value NON-EXISTING'
    ]
}

snapshots['test_validation[NON-EXISTING-Chad-Sub-Saharan Africa-10000000-2000] 1'] = {
    'row: 0': [
        '`Total Cost` value should not be higher than 5000000',
        'Unexpected priority value NON-EXISTING'
    ]
}
