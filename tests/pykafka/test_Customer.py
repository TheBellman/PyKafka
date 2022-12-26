from pykafka.Customer import Customer, customer_to_dict
from confluent_kafka.serialization import SerializationContext, MessageField

import pytest


@pytest.fixture
def customer():
    return Customer('1234', 'Isaac Newton')


def test_customer(customer):
    assert customer.id == '1234'
    assert customer.name == 'Isaac Newton'
    assert str(customer) == "Customer(id='1234', name='Isaac Newton')"


def test_to_dict(customer):
    result = customer_to_dict(customer, SerializationContext("topic", MessageField.VALUE))
    assert result.get('id', '') == '1234'
    assert result.get('name', '') == 'Isaac Newton'
