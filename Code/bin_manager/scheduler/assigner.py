from scheduler import commander


# Mediator design pattern is used for assigning the waste type, truck and the driver to the trip


class Mediator:

    _trip_creation_status = True
    _waste_assign_status = False
    _truck_assign_status = False
    _driver_assign_status = False
    _mediator_status = False


    def __init__(self):
        self._truckdiver = FreeTruckDriver(self)
        self._truck = FreeTruck(self)
        self._wastetype = WasteType(self)

    def check_trip_creation(self):
        return self._trip_creation_status

    def check_waste_type(self):
        return self._waste_assign_status


    def check_truck(self):
        return self._truck_assign_status

    def check_driver(self):
        return self._driver_assign_status

    def set_mediator_status(self):
        if self._trip_creation_status == True and self._waste_assign_status == True and  self._truck_assign_status == True and self._driver_assign_status == True :
           self._mediator_status = True

    def get_mediator_status(self):
        return self._mediator_status





class FreeTruckDriver:
    _drivererror = False

    def __init__(self,mediator):
        self._mediator = mediator

    def assign_driver(self):
        if self._mediator.check_truck() == True:
            print("Truck assigned... Assigning driver")
            if not self._drivererror:
                # driver assign logic
                print("Driver has been assigned")
                self._mediator._driver_assign_status = True
            else:
                print("Truck has not been assigned. ERROR!!!!!")
                self._mediator._driver_assign_status = False

        else:
            print('Truck yet to be assigned...Driver not assigned!!!')

class FreeTruck:
    _truckerror = False

    def __init__(self,mediator):
        self._mediator = mediator

    def assign_truck(self):
        if self._mediator.check_waste_type() == True:
            print("Waste assigned....Assigning Truck")
            if not self._truckerror :
                # truck assign logic
                print("Truck has been assigned")
                self._mediator._truck_assign_status = True
            else:
                print("Truck has not been assigned. ERROR!!!!!")
                self._mediator._truck_assign_status = False
        else:
            print('Waste yet to be assigned..Truck not assigned!!!')

class WasteType:
    _wasteerror = False

    def __init__(self,mediator):
        self._mediator = mediator

    def assign_waste(self):
        if self._mediator.check_trip_creation() == True:
            print("Trip created....Assigning Waste Type")
            if not self._wasteerror:
                # Waste Assignment Logic
                print("Waste has been assigned")
                self._mediator._waste_assign_status = True
            else:
                print("Waste has not been assigned. ERROR!!!!!")
                self._mediator._waste_assign_status = False
        else:
            print("Trip yet to be created...Waste not assigned!!!")


class AssignStuffs(commander.Command):

    def execute(self,stages):
        self._receiver.action()
        print('This is the assigner !')
        stages.append('Assigner starting')
        if not self._receiver.check_error() :
            mediator = Mediator()
            freeDriver  = FreeTruckDriver(mediator)
            freeTruck = FreeTruck(mediator)
            wastetype = WasteType(mediator)
            wastetype.assign_waste()
            freeTruck.assign_truck()
            freeDriver.assign_driver()
            mediator.set_mediator_status()
            print('The Assignment Status is :', mediator.get_mediator_status() )
            stages.append('Assigner completed')
            self._receiver.set_error(False)
        else:
            print('Previous Stage Error!')
            stages.append('Assigner not completed!!')




# if __name__ == "__main__":
#     AssignStuffs.execute()
