from typing import Any


class Product():
    def __init__(self, name:str, price:float, quantity:int = 0,active:bool=  True, promotions:list= []):
        if name == '':
            raise AttributeError('name cannot be empty string')
        else:
            self.name = name
        if price < 0 or quantity < 0:
            raise Exception('Error!! negative values tracked..\nplease check inputs and try again')
        else:
            self.price = price 
            self.quantity = quantity
            if quantity != 0:
              self.active = active
            else:
               self.active = False
        if promotions == []:
           self.promotions = []
        else:   
          self.promotions:list = promotions.split(',')

    def get_name(self):
       """
       a getter function for name
       """
       return self.name
    
    def set_name(self, new_name):
       """
       a setter function for name
       """
       self.name = new_name

    def get_promotion(self):
     return self.promotions

    def set_promotion(self, promotion):
     self.promotions.append(promotion)   


    def is_active(self) ->bool:
      """
      a function that returns True if a product is active 
      False if product in not active
      """
      return self.active

    def get_quantity(self) ->(float):
      """
      a getter function to get the quantity for a product
      """
      return self.quantity

    def set_quantity(self, quantity):
      """
      a setter function for qunatity which determines wherther a product will be 
      acitve or it will be deactivated
      """
      if quantity == 0:
        self.deactivate()
      elif quantity > 0:
         self.activate() 
      #if negative quantity tracked return False   
      else:
         print('negative value tracked...!!!')
         print('please try again')
         return False 
      self.quantity = quantity


    def activate(self):
      """
      a function that activates the product
      """
      self.active = True

    def deactivate(self):
      """
      a function that deactivates the product
      """
      self.active = False  

    def __str__(self):
      """
      a function that return the product details
      """
      if len(self.promotions) != 0:
         return f'{self.get_name()}, Price: {self.price},\
Quantity:{self.quantity}({[each_promotion.promotion for each_promotion in self.promotions]})'
      else:
         return f'{self.get_name()}, Price: {self.price}, Quantity: {self.quantity}'
 
    def buy(self, quantity) ->float:
      """
      a function that gets the quantity requested and checks if it is available 
      in store.
      """
      #if negative quantity requested raise an exception
      if 0 > quantity:
        raise Exception('negative quantity')
      # if requested quantity greater than available quantity in store raise exception
      elif quantity > self.quantity:
         raise Exception('quantity not available in stock')
      #if quantity requested within or equal to available quantity in store
      else:
        self.quantity -= quantity
        #set quantity with the new updated quantiy of product
        self.set_quantity(self.quantity)
        #if any promotions on product while making an instance of class
        if len(self.promotions) > 0:
           total:float = 0.0
           for each_promotion in self.promotions:
              #applying promtion  
              total += each_promotion.apply_promotion(self, quantity)
           return total
        else:      
          return quantity * self.price
    #greater than >
    def __gt__(self, other):
       return self.price > other.price
    #less than < 
    def __ls__(self, other):
       return self.price < other.price 
    #equal to ==
    def __eq__(self, other) -> bool:
       return self.price == other.price
    
    # #property method for price
    # @property
    # def price(self):
    #    return self.price
    
    # @price.setter
    # def price(self, value):
    #    if value < 0:
    #       raise ValueError('price cannot be negative')
          

#class for nonstocked products      
class NonStockedProduct(Product):
   def __init__(self, name: str, price: float, quantity: int = 0,\
                 active: bool = True, promotions:list = []) :
      super().__init__(name, price, quantity, promotions)
      self.active = active

   #overriding buy function for non stocked
   def buy(self, quantity):
      if 0 > quantity:
         raise Exception('negative request tracked..!! please try again')
      else:
         #if any promotions on product
         if len(self.promotions)> 0:
            total:float = 0.0
            for each_promotion in self.promotions:
               #applying promotions
               total += each_promotion.apply_promotion(self, quantity)
            return total
         else:
            return quantity * self.price
   #overriding show function   
   def __str__(self):

    return f'{self.name}, Price: {self.price}, \
({[each_promotion.promotion for each_promotion in self.promotions]})'

#class for limited products in store      
class LimitedProduct(Product):
   def __init__(self, name: str, price: float, maximum:int, quantity: int = 0,\
                 active: bool = True, promotions:list = []):
      super().__init__(name, price, quantity, active, promotions)
      self.maximum = maximum
      
   def __str__(self):
    return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}'
   
   def buy(self, quantity):
      if 0 > quantity:
         raise Exception('negative request tracked..!! please try again')
      elif quantity > self.maximum:
         raise Exception('order over limit please try again')
      else:
         self.quantity -= quantity
         #if product has any promotion
         if len(self.promotions) > 0:
            total:float = 0.0
            for each_promotion in self.promotions:
               #applying promotion
               total += each_promotion.apply_promotion(self, quantity)
            return total
         else:   
            return quantity * self.price
    
      



   
     
    


  

      
    