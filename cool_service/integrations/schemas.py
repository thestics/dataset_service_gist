#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danylo Kovalenko


from pydantic import BaseModel


class Country(BaseModel):
    code: str
    name: str
    description: str
    region: str
