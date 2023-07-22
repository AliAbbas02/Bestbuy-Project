import pytest
import main
import products
import promotions

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

#testing that shop throws exception if more qunatity is ordered
def test_larger_quatnity():
    with pytest.raises(Exception, match='quantity not available in stock'):
        macbooks = main.store.products.Product('mac', 10, 10)
        assert macbooks.buy(11)

#testing limitedproducts
def test_limited_quantity():
    with pytest.raises(Exception, match='order over limit please try again'):
        macbooks = main.store.products.LimitedProduct('mac', 10, 1, 10 )
        assert macbooks.buy(2)         

############ Promotions testing ########

#secondhalfprice test
def test_second_halfprice():
    macbooks = products.Product('mac', 10, 10)
    macbooks.set_promotion(promotions.SecondHalfPrice('Second Half Price'))
    assert macbooks.buy(2) == 15

#third item free test
def test_third_item_free():
    macbooks = products.Product('mac', 10, 10)
    macbooks.set_promotion(promotions.ThirdOneFree('third item free'))
    assert macbooks.buy(3) == 20

#percent_discount test
def test_thirty_percent():
    macbooks = products.Product('mac', 10, 10)
    macbooks.set_promotion(promotions.PercentDiscount('20 percent discount', 20))
    assert macbooks.buy(1) == 8

pytest.main()





