"""
Factory Method Design Pattern implementation for Customer Type
"""

import abc


class CreateCustomer(metaclass=abc.ABCMeta):
    
    def __init__(self):
        self.customer = self._create_customer()

    @abc.abstractmethod
    def _create_customer(self):
        pass

    def some_operation(self):
        self.customer.interface()

class CreateRegularCustomer(CreateCustomer):

    def _create_customer(self):
        return RegularCustomer()


class CreateGoldCustomer(CreateCustomer):

    def _create_customer(self):
        return GoldCustomer()

class CreatePlatinumCustomer(CreateCustomer):

    def _create_customer(self):
        return PlatinumCustomer()

class Customer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interface(self):
        pass

class RegularCustomer(Customer):

    def interface(self):
        print("Regular Customer Created")

class GoldCustomer(Customer):

    def interface(self):
        print("Gold Customer Created")

class PlatinumCustomer(Customer):

    def interface(self):
        print("Platinum Customer Created")


def main():
    
    customer_obj_1 = CreateRegularCustomer()
    customer_obj_1.some_operation()
    
if __name__ == "__main__":
    main()