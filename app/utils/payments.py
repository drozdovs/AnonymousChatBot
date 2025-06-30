"""Payments utils"""
import random
import logging
import uuid
import asyncio
from yookassa import Configuration, Payment

from dataclasses import dataclass


@dataclass
class CheckResponse:
    """Check response class"""
    is_paid: bool
    amount: int = 0


@dataclass
class BaseBill:
    """Base bill class"""
    id: int
    url: str = 'https://google.com'
    provider_id: str | None = None


class BasePayment(object):
    """Base payment class"""

    async def check_payment(self, payment_id: int) -> CheckResponse:
        """Check payment"""
        return CheckResponse(True, 1)

    async def create_payment(self, amount: int) -> BaseBill:
        """Create payment"""
        return BaseBill(id=self._get_id())

    @staticmethod
    def _get_id() -> int:
        """Get random id"""
        return random.getrandbits(32)


logger = logging.getLogger('payments')


class YooKassa(BasePayment):
    """YooKassa payment class"""

    def __init__(self, shop_id: str, secret_key: str, return_url: str) -> None:
        """Initialize the YooKassa class"""
        Configuration.account_id = shop_id
        Configuration.secret_key = secret_key
        self.return_url = return_url
        self._payments: dict[int, str] = {}

    async def create_payment(self, amount: int) -> BaseBill:
        """Create payment"""
        bill_id = self._get_id()
        payment = await asyncio.to_thread(
            Payment.create,
            {
                "amount": {"value": f"{amount:.2f}", "currency": "RUB"},
                "confirmation": {"type": "redirect", "return_url": self.return_url},
                "capture": True,
                "description": "Balance top up",
            },
            idempotence_key=str(uuid.uuid4()),
        )
        self._payments[bill_id] = payment.id
        return BaseBill(id=bill_id, url=payment.confirmation.confirmation_url)

    async def check_payment(self, payment_id: int) -> CheckResponse:
        """Check payment"""
        provider_id = self._payments.get(payment_id)
        if not provider_id:
            return CheckResponse(False)

        payment = await asyncio.to_thread(Payment.find_one, provider_id)
        is_paid = payment.status == "succeeded" or getattr(payment, "paid", False)
        amount = int(float(payment.amount.value)) if is_paid else 0
        return CheckResponse(is_paid, amount)
