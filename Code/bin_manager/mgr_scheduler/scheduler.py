import commander

class ScheduleTrip(commander.Command):
    def execute(self):
        self._receiver.action()
        print('This is the scheduler !')
