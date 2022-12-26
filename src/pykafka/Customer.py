from dataclasses import dataclass
from typing import Any

from confluent_kafka.serialization import SerializationContext


@dataclass
class Customer:
    """
    data object representing our Customer record
    """
    id: str
    name: str


def customer_to_dict(customer: Customer, ctx: SerializationContext) -> dict[str, Any]:
    return dict(
        id=customer.id,
        name=customer.name
    )
