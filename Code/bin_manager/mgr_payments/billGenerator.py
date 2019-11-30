import abc
import enum

class IBillGenerator(metaclass=abc.ABCMeta):
    """
    Define the interface for objects that can have responsibilities
    added to them dynamically.
    """

    @abc.abstractmethod
    def GenerateBill(self):
        pass

# Decorator
class ICalculator(IBillGenerator, metaclass=abc.ABCMeta): 
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, IBillGenerator):
        self._billGenerator = IBillGenerator

    @abc.abstractmethod
    def GenerateBill(self):
        pass


# class BaseFareCalculator(ICalculator):
#     """
#     Add responsibilities to the component.
#     """

#     def GenerateBill(self):
#         # ...
#         self._billGenerator.GenerateBill()
#         print("from base fare")

#         # ...


class PriorityFareCalculator(ICalculator):
    """
    Add responsibilities to the component.
    """

    def GenerateBill(self):
        # ...
        self._billGenerator.GenerateBill()
        print("from priority")
        # ...

class TaxCalculator(ICalculator):
    """
    Add responsibilities to the component.
    """

    def GenerateBill(self):
        # ...
        self._billGenerator.GenerateBill()
        print("from tax")

        # ...

class DiscountCalculator(ICalculator):
    """
    Add responsibilities to the component.
    """

    def GenerateBill(self):
        # ...
        self._billGenerator.GenerateBill()
        print("from discount")

        # ...

class BaseFareCalculator(IBillGenerator):
    """
    Define an object to which additional responsibilities can be
    attached.
    """
    # self._customerType = customerType
    def GenerateBill(self):
        print("from base")

        


class CustomerBillCalculator(IBillGenerator):
    """
    Define an object to which additional responsibilities can be
    attached.
    """

    def GetAllCustomersToProcess(self):
         customerTypeArg = [customerType.Platinum, customerType.Gold, customerType.Regular]
         return customerTypeArg

    def GenerateMonthlyBill(self,customerType):
        switcher = {
        customerType.Platinum :TaxCalculator(DiscountCalculator(BaseFareCalculator())).GenerateBill() ,
        customerType.Gold :TaxCalculator(DiscountCalculator(PriorityFareCalculator(BaseFareCalculator()))).GenerateBill() ,
        customerType.Regular :TaxCalculator(PriorityFareCalculator(BaseFareCalculator())).GenerateBill() }
        return switcher.get(customerType, "InValid Customer")

    def GenerateBill(self):
        customertoGenerateBill = self.GetAllCustomersToProcess()
        for customer in customertoGenerateBill:
            print(customer)
            self.GenerateMonthlyBill(customer)
       


# Using enum class create enumerations
class customerType(enum.Enum):
   Platinum = 1
   Gold = 2
   Regular = 3


def main():

    calculator = CustomerBillCalculator()
    calculator.GenerateBill()
    

if __name__ == "__main__":
    main()