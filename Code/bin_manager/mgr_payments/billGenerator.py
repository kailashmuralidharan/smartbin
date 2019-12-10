import abc
import enum
from datetime import timedelta
from datetime import datetime  

from django.core import cache



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



class PriorityFareCalculator(ICalculator):
    """
    Add responsibilities to the component.
    """
    priorityFare = 5.0
    def GenerateBill(self,customerDetail):
        # ...
        self._billGenerator.GenerateBill(customerDetail)
        print("from priority")
        customerDetail.PriorityRequestFare = customerDetail.totalNumberofPriorityRequests * self.priorityFare
        print(customerDetail.PriorityRequestFare)
        # ...

class TaxCalculator(ICalculator):
    """
    Add responsibilities to the component.
    """
    taxPercentage = 10.0
    def GenerateBill(self,customerDetail):
        # ...
        self._billGenerator.GenerateBill(customerDetail)
        print("from tax")
        customerDetail.tax = ((customerDetail.baseFare+customerDetail.PriorityRequestFare-customerDetail.discount)/100)*self.taxPercentage
        print(customerDetail.tax)
        # ...

class DiscountCalculator(ICalculator):
    """
    Add responsibilities to the component.
    """
    # isDiscountAvailable = True #will be 
    discountPercentage = 10.0

    def GenerateBill(self,customerDetail):
        # ...
        self._billGenerator.GenerateBill(customerDetail)
        print("from discount")
        customerDetail.discountPercentage = self.discountPercentage
        customerDetail.discount = ((customerDetail.baseFare+customerDetail.PriorityRequestFare)/100) * self.discountPercentage
        print(customerDetail.discountPercentage)
        print(customerDetail.discount)
        # ...

class BaseFareCalculator(IBillGenerator):
    """
    Define an object to which additional responsibilities can be
    attached.
    """
    baseFare = 10.0

    # self._customerType = customerType
    def GenerateBill(self,customerDetail):
        print("from base")
        customerDetail.baseFare = customerDetail.totalNumberofRequests * self.baseFare
        print(customerDetail.baseFare)

        


class CustomerBillGenerator(IBillGenerator):
    """
    Define an object to which additional responsibilities can be
    attached.
    """
    isBillGenerationCompleted = False
    customerBillDetails =[]
    # cacheKey = "GeneratedBills"

    def GetAllCustomersToProcess(self):
        #  customerTypeArg = [customerType.Platinum, customerType.Gold, customerType.Regular]
        #  return customerTypeArg

        customerDetails = []
        customerDetails.append(customerBillDetail(customerType.Platinum,"Tom",5,2))
        customerDetails.append(customerBillDetail(customerType.Gold,"Jim",5,2))
        customerDetails.append(customerBillDetail(customerType.Regular,"Sam",5,2))
        return customerDetails

    def GenerateMonthlyBill(self,customerDetail):
        # print(customerType)
        if(customerDetail.customerType == customerType.Platinum):
            TaxCalculator(DiscountCalculator(BaseFareCalculator())).GenerateBill(customerDetail) 
        elif (customerDetail.customerType == customerType.Gold):
            TaxCalculator(DiscountCalculator(PriorityFareCalculator(BaseFareCalculator()))).GenerateBill(customerDetail)
        elif (customerDetail.customerType == customerType.Regular):
            # customerType.Regular :
            TaxCalculator(PriorityFareCalculator(BaseFareCalculator())).GenerateBill(customerDetail)
        else:
            print("Invalid Customer")
        customerDetail.calculateTotal()
        return

    # def CacheResults(self):
    #         if (cache.cache.get(self.cacheKey)):
    #             return
    #         else:
    #             cache.cache.set(self.cacheKey,self.customerBillDetails,500)
    #         return
    # def GetCachedResult(self):
    #     return cache.cache.get(self.cacheKey)

    def GenerateBill(self):
        self.customerBillDetails = self.GetAllCustomersToProcess()
        for customerDetail in self.customerBillDetails:
            print(customerDetail.customerType)
            self.GenerateMonthlyBill(customerDetail)
        self.isBillGenerationCompleted =True
        # self.CacheResults()


# Using enum class create enumerations
class customerType(enum.Enum):
   Platinum = 1
   Gold = 2
   Regular = 3

class customerBillDetail:
    customerType = None
    name =""
    baseFare = 0.0
    discount =0.0
    tax =0.0
    PriorityRequestFare =0.0
    total = 0.0
    dueDate = (datetime.now() + timedelta(days=15)).strftime("%b %d %Y")
    totalNumberofRequests=0
    totalNumberofPriorityRequests =0
    discountPercentage =0
             
    def calculateTotal(self): 
        print('Setting total') 
        self.total = self.baseFare+self.PriorityRequestFare-self.discount+self.tax
        print(self.total) 

    def __init__(self, customerType,name,totalNumberofRequests,totalNumberofPriorityRequests):
        self.customerType = customerType
        self.name = name
        self.totalNumberofRequests = totalNumberofRequests
        self.totalNumberofPriorityRequests =totalNumberofPriorityRequests

# def main():

#     calculator = CustomerBillGenerator()
#     calculator.GenerateBill()
    

# if __name__ == "__main__":
#     main()