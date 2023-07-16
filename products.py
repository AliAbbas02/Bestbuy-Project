class Product():
    def __init__(self, name:str, price:float, quantity:int, active:bool=True):
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
               self.activate = False

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

    def show(self):
      """
      a function that return the product details
      """
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
        #return the calculated price
        return quantity * self.price


        
  