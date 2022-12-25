from pykafka.Customer import Customer


def test_customer():
    customer = Customer('1234', 'fred nerk')
    assert customer.id == '1234'
    assert customer.name == 'fred nerk'
    assert str(customer) ==  "Customer(id='1234', name='fred nerk')"
