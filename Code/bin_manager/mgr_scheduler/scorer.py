# import manager.Command
#
import commander

class ScoreRequests(commander.Command):
    def execute(self):
        self._receiver.action()
        print('This is the scorer !')
