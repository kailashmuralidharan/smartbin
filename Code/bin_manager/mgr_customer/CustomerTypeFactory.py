"""
Factory Method Design Pattern implementation for Customer Type
"""

import abc


class CustomerTypeFactory(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def _create_customer(self):
        print("Default implementation for Customer Creation")
        pass

    def some_operation(self):
        customer = self._create_customer()
        result = f"Inside CustomerTypeFactory, {customer.customer_creation()}"
        return result 

class RegularCustomerFactory(CustomerTypeFactory):

    def _create_customer(self):
        return RegularCustomer()

class GoldCustomerFactory(CustomerTypeFactory):

    def _create_customer(self):
        return GoldCustomer()

class PlatinumCustomerFactory(CustomerTypeFactory):

    def _create_customer(self):
        return PlatinumCustomer()

class Customer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def customer_creation(self):
        pass

class RegularCustomer(Customer):

    def customer_creation(self):
        return "\nCreating Regular Customer.... DONE!"

class GoldCustomer(Customer):

    def customer_creation(self):
        return "\nCreating Gold Customer.... DONE!"

class PlatinumCustomer(Customer):

    def customer_creation(self):
        return "\nCreating Platinum Customer.... DONE!"

# Simulates client code, this method will not have an idea which type of customer object is about to be created.
def customer_type(customerTypeFactory: CustomerTypeFactory):
    print(f"Inside customer_type:\n" 
          f"Invoking the appropriate CustomerTypeFactory, but I'm not aware, what type of customer it is!\n"
          f"{customerTypeFactory.some_operation()}", end="")

def main():
    print("Regular Customer Creation")
    customer_type(RegularCustomerFactory())
    print("\n")

    print("Gold Customer Creation")
    customer_type(GoldCustomerFactory())
    print("\n")
    
    print("Platinum Customer Creation")
    customer_type(PlatinumCustomerFactory())

if __name__ == "__main__":
    main()