#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
from kata.payments.models.payment import Payment

def get_payments(user_id: uuid.UUID, month:int):
    return [ Payment(category="a category", price=5, description="") for _ in range(10)]
