import commander


class CreateTrip():

    def set_truck_weight_limit(self):
        print('Setting weight limit for trip...')

    def fetch_requests_for_today(self):
        print('Getting requests for today ordered by score descending from database...')

    def assign_requests_for_route(self):
        print('Assigning requests for pickup until weight limit is reached...')

    def update_requests_status(self):
        print('Updating the request status for selected reequests...')

    def send_notification(self):
        print('Notifyin customers of the selected requests...')



class ScheduleTrip(commander.Command):
    def execute(self):
        self._receiver.action()
        print('This is the scheduler !')

        trip = CreateTrip()
        trip.set_truck_weight_limit()
        trip.fetch_requests_for_today()
        trip.assign_requests_for_route()
        trip.update_requests_status()
        trip.send_notification()
