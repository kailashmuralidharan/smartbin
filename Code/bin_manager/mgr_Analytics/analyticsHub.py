class AnalyticsHub(object):
    def smartDecisionMaker(self):
        self.blockDemand = demandSense()
        self.blockDemand.getDemandState()
        print("Demand is "+ str(self.blockDemand.getDemandState()))

        self.trafficState = trafficSense()
        self.trafficState.getTrafficStatus()
        print("Traffic State is "+self.trafficState.getTrafficStatus())

        self.truckState = truckSense()
        self.truckState.getTruckStatus()
        print("Truck State is "+self.truckState.getTruckStatus())

    def customerAnalyzer(self):


#class binSense(object):
#    def getBinInfo(self):
#        return 70
#        #print("Bins are 70% Full, Good time to collect!")

class demandSense(binSense):
    def getDemandState(self):
        demandScore = 0
        for houses in range(100): #no. of Houses hard-coded to 100
            #obj = binSense()
            #demandScore += obj.getBinInfo()
            demandScore = 7000 #Hardcoded to-do , try getting demands from requests table
        blockLevel = demandScore/100
        return blockLevel
        #print("")


class trafficSense(object):
    def getTrafficStatus(self):
        return "free" #Probable improvement from Maps API
        #print("Peak Hour")


class truckSense(object):
    def getFuelLevel(self):
        return 25
        #print("25L Remaining")

    def getTruckStatus(self):
        fuelLevel = self.getFuelLevel()
        if  fuelLevel >= 25:
            return "Ready"
        else:
            return "Refuel"
        #print("Truck 304 Running well")


class transactSense(object):
    def getTransactionPattern(self):
        return 25
        #print("25L Remaining")

    def getCustomerSlab(self):
        transactPattern = self.getTransactionPattern()
        if  transactPattern >= 200000:
            return "corporateLarge"
        elif transactPattern >= 40000:
            return "corporateMid"
        elif transactPattern >= 10000:
            return "corporateSmall"
        elif transactPattern >= 2000:
            return "residentialLarge"
        elif transactPattern >= 1000:
            return "residentialMid"
        else:
            return "residentialSmall"
        

if __name__ == "__main__":
    decision = AnalyticsHub()
    decision.smartDecisionMaker()