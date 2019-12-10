from strategies import pricingStrategy
from strategies import discountStrategy
from strategies import collectionStrategy

dynamicPricing = dynamicPrice()
loyaltyPricing = loyaltyPrice()
loyaltyDiscount = loyaltyDiscount()
transactBasedDiscount = transactionDiscount()
compostCollect = compostWaste()
recycleCollect = recycleWaste()
generalCollect = generalWaste()


class Policy(object):
    def __init__(self, pricingStrategy, discountStrategy):
        self.pricingStrategy = pricingStrategy
        self.discountStrategy = discountStrategy

    def setPrice(self):
        self.pricingStrategy.setPrice()

    def generateDiscount(self):
        self.discountStrategy.generateDiscount()

class platinumPolicy(Policy):
    def __init__(self):
        super(platinumPolicy, self).__init__(loyaltyPricing, loyaltyDiscount)

    def displayPolicy(self):
        print "Platinum Policy"

class goldPolicy(Policy):
    def __init__(self):
        super(goldPolicy, self).__init__(dynamicPricing, transactBasedDiscount)

    def displayPolicy(self):
        print "Gold Policy"  

class regularPolicy(Policy):
    def __init__(self):
        super(regularPolicy, self).__init__(None, transactBasedDiscount)

    def displayPolicy(self):
        print "Transaction based Policy"

regularCustomer = regularPolicy()
goldCustomer = goldPolicy()
platinumCustomer = platinumPolicy()

regularCustomer.pricingStrategy()
regularCustomer.discountStrategy()
goldCustomer.pricingStrategy()
goldCustomer.discountStrategy()
platinumCustomer.pricingStrategy()
platinumCustomer.discountStrategy()