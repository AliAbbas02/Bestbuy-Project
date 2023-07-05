import products

class Store():
  def __init__(self, products:list):
      self.products = products

  def add_product(self, product):
    """
    a function that adds a new product to products list
    """
    self.products.append(product)

  def remove_product(self, product):
    """
    a function that removes a product from product list
    """
    self.products.pop(product)

  def get_total_quantity(self) ->int:
    """
    a function that calculates total amount of items for each product 
    """
    total_items:int = 0 
    for product in self.products:
      #checking if product has items more than 0 in store
      if product.is_active():
        total_items += product.get_quantity()
    return total_items

  def get_all_products(self) -> list:
    """
    a function that returns all the products with details
    """
    return [product for product in self.products if product.is_active()]      

  def order(self, shopping_list) ->float:
    """
    a function that takes an order from buyer and checks if 
    quantity requested is available in store, if yes then calculates
    total cost and returns it, if no then raises an exception
    """
    total_cost: float = 0.0
    for product in shopping_list:
      #calling the buy function from product to check if requested quantity is in store
      try:
        total_cost += product[0].buy(product[1])
      #any exception raised will handled either more requested quantity or negative value   
      except Exception as e:
        print('_' * 5)
        print(e)
        print(f'Error! cannot puchase item {product[0].name}')
        print('_' * 5)
        total_cost = 0
        break
    return total_cost
        


