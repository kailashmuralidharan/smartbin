import abc  # Built-in abstract class library

class pricingStrategy(object):
    """Defining an 
    abstract class."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setPrice(self):
        """Required Method"""

class dynamicPrice(pricingStrategy):
    def setPrice(self):
        print "Price Varies based on demand"

class loyaltyPrice(pricingStrategy):
    def setPrice(self):
        print "Price varies based on Loyalty"

class discountStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generateDiscount(self):
        """Required Method"""

class loyaltyDiscount(discountStrategy):
    def generateDiscount(self):
        print "20% discount for loyalty"

class transactionDiscount(discountStrategy):
    def generateDiscount(self):
        customerType = transactSense.getCustomerSlab()
        if transactValue > 10000:
            print "15% discount for high value transactions"
        elif paymentMode = "wallet":
            print "5% Cashback to wallet"
        elif customerType = "corporateMid":
            print "10% Discount for regular transactions"

class collectionStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def collectWaste(self):
        """Required Method"""

class compostWaste(collectionStrategy):
    def collectWaste(self):
        print "Compost levels brimming"

class recycleWaste(collectionStrategy):
    def collectWaste(self):
        print "Recycle levels brimming"

class generalWaste(collectionStrategy):
    def collectWaste(self):
        print "General levels brimming"