#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Payment:
    def __init__(self, category:str, price: float, description: str):
        self.category = category
        self.price = price
        self.description = description