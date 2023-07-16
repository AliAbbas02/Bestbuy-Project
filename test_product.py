import pytest
import main
import products

#testing if normal product is made
def test_product_making():
    mac =  main.store.products.Product('mac', 20, 100) 
    assert isinstance(mac, products.Product)

#testing with invalid details 
def test_invalid_details():
    #when name is not passed
    with pytest.raises(AttributeError, match='name cannot be empty'):
        assert main.store.products.Product('', 20, 199)
    #when a negative value is passed
    with pytest.raises(Exception, match='Error!! negative values tracked..\nplease check inputs and try again'):
        assert main.store.products.Product('iphone', -200, -300)

#testing that when a product reaches 0 in stock it becomes inactive
def test_checking_zero():
    macbooks= products.Product('macbook', 100, 20)
    macbooks.buy(20)
    assert macbooks.active == False

#testing purchasing quantity will change the amount in store
def test_product_quantity_modifies():
    macbooks= products.Product('macbook', 100, 20)
    macbooks.buy(20)
    assert macbooks.quantity == 0


def test_larger_quatnity():
    with pytest.raises(Exception, match='quantity not available in stock'):
        macbooks = main.store.products.Product('mac', 10, 10)
        assert macbooks.buy(11)
    
pytest.main()





