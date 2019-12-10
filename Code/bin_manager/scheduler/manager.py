import abc

from scheduler import assigner
from scheduler import scorer
from scheduler import scheduler



class TripManager:
    stages = []
    def __init__(self,stages):
        self._commands = []
        self.stages = stages

    def store_command(self,command):
        self._commands.append(command)

    def execute_command(self):
        for command in self._commands:
            command.execute(self.stages)


class Receiver:
    stage_error = False
    def action(self):
        print('Starting stage...')
    def set_error(self,error):
        self.stage_error = error
    def check_error(self):
        return self.stage_error



class Manager:

    stages = []

    def startWork(self,wasteType):
        self.stages.append('Starting work for '+wasteType)
        receiver = Receiver()
        stage1 = scorer.ScoreRequests(receiver)
        stage2 = scheduler.ScheduleTrip(receiver)
        stage3 = assigner.AssignStuffs(receiver)
        invoker = TripManager(self.stages)
        invoker.store_command(stage1)
        invoker.store_command(stage2)
        invoker.store_command(stage3)
        invoker.execute_command()


if __name__ == "__main__":
    Manager.startWork()
