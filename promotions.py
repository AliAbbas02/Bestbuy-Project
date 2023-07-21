from abc import ABC, abstractmethod

class Promotions(ABC):
  def __init__(self, promotion) -> None:
      self.promotion = promotion 
  
   
  # a method that returns price after promotion was applied 
  @abstractmethod
  def apply_promotion(self, product, qunatity) -> float:
     pass
   
      

class SecondHalfPrice(Promotions):
   def apply_promotion(self, product, qunatity) -> float:
      total_price:float = 0.0
      #half the price by multiplying it to 0.5
      half_price = product.price * 0.5
      for items in range(1, qunatity+1):
         # each second item is half priced and added to total cost
         if items % 2 == 0:
            total_price += half_price
         else:
            total_price += product.price
      return total_price      
            
         

class ThirdOneFree(Promotions):
   def apply_promotion(self, product, qunatity) -> float:
      total_price:float = 0.0
      for items in range(1, qunatity+1):
         #each third item is free 
         if items % 3 == 0:
            continue
         else:
            total_price += product.price
      return total_price      
      

class PercentDiscount(Promotions):
   def __init__(self, promotion, percent:int) -> None:
      super().__init__(promotion)
      #if percent invalid, raise and error
      if percent < 0 or percent > 100:
         raise ValueError('Invalid percentage please try again')
      else:
        self.percent:int = percent

   def apply_promotion(self, product, qunatity) -> float:
      #calculate price of one item after discount applied
      price_after_percentage = product.price - (product.price * (self.percent / 100))
      return qunatity * price_after_percentage