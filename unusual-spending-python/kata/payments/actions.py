import uuid

from typing import List

from kata.payments.models.payment import Payment


def get_payments(user_id: uuid.UUID, month: int) -> List[Payment]:
    return [Payment(category="a category", price=5, description="") for _ in range(10)]
