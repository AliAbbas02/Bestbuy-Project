import products
import store
import promotions

def start():
    """
    a function that displays an interface to user and asks for a service
    """
    print('''---------------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
----------------''')
    choice = input('Please Choose a number: ')
    return choice
    

def order_product(best_buy):
    """
    a function that orders the products requested by user, calls the order function 
    from store
    """
    print('=> When you want to finish order, enter empty text for product and amount.')
    #display all the active products to customer
    display_products(best_buy)
    print('-' * 5)  
    #cost for all the items initially set to $0
    total_cost:float = 0.0
    items_requested:list = []
    while True:
        #validating the inputs made by user and handling any exception
        try:
            product:str = input('which product do you want: ')
            amount:str = input('what amount do you want: ')
            #if user enters empty text on product and amount, calculate the total
            if product == '' == amount:
                #make the order on product list by calling the order function from store
                total_cost += best_buy.order(items_requested)
                if total_cost != 0:
                    print('*' * 10)
                    print(f'Order made! Total payment: ${total_cost}')
                    break
                #if returned cost is 0 beacuse a problem occured while creating order break to main menu
                elif total_cost == 0:
                    break
            else:
                product = int(product)
                product -= 1
                #add products to the list
                items_requested.append((best_buy.get_all_products()[product], int(amount)))
                print('product added to the list\n')
        #if user chooses a product number not in list
        except IndexError:
            print('Please choose item number from the available list')
        #if user enters any invalid input
        except Exception:
            print('invalid entry')
                

def display_products(bestway) -> None:
    """
    a function that displays all the prodcuts to its updated quantity
    """
    for index, product in enumerate(bestway.get_all_products(), 1):
        print(f'{index}. {product}')  


def total_amount(best_buy) -> None:
    """
    a function that calculates all the active product items in store
    """
    print(f'Total items in the store {best_buy.get_total_quantity()}')

        
def main() -> None:
    """
    main function for the app
    """
    try:
        product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        products.Product("Google Pixel 7", price=500, quantity=250),
                        products.NonStockedProduct("Windows License", price=125),
                        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

        # Create promotion catalog
        second_half_price = promotions.SecondHalfPrice("Second Half price!")
        third_one_free = promotions.ThirdOneFree("Third One Free!")
        thirty_percent = promotions.PercentDiscount(f'30% off!', percent=30)

        # Add promotions to products
        product_list[0].set_promotion(second_half_price)
        product_list[1].set_promotion(third_one_free)
        product_list[3].set_promotion(thirty_percent)
        best_buy = store.Store(product_list)
        #a dict for pointer functions for interface of app
        functions = {
            '1': display_products,
            '2': total_amount,
            '3': order_product
            }
        while True:
            #ask the user to choose a service 
            number = start()
            if number == '4':
                print('Thankyou for visiting the shop\nBye!!!')
                break
            #if service requested not quit  
            elif number != '4':
                try:
                    functions[number](best_buy)
                except KeyError:
                    print('please select an option from the services')
    #if name property/attribute missing while creating products for store
    except AttributeError as e:
        print(e)
        print('invalid input!!! please check products and try again') 
    #if any other exception occured while creating products
    except Exception:
        print('invalid input!!! one of the product/products was not entered correctly')                   

         
if __name__ == '__main__':
    # setup initial stock of inventory
    # mac =  products.Product("MacBook Air M2", price=1450, quantity=100)
    # bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    # pixel = products.LimitedProduct("Google Pixel 7", price=500, quantity=250, maximum=1)

    # best_buy = store.Store([mac, bose])
    # b = store.Store([mac])
         
    # print(mac)               # Should print `MacBook Air M2, Price: $1450 Quantity:100`
    # print(mac > bose)        # Should print True
    # print(mac in best_buy)   # Should print True
    # print(pixel in best_buy) # Should print False
    # #combining two stores to create an instance 
    # try:
    #     combined_products = best_buy + b
    #     print(f'combined store :{combined_products}')
    # except TypeError as e:
    #     print(e)    
    #main function for best_buy with promotions
    main()
