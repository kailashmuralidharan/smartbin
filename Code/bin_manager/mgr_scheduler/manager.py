import abc

import assigner
import scorer
import scheduler



class TripManager:
    def __init__(self):
        self._commands = []

    def store_command(self,command):
        self._commands.append(command)

    def execute_command(self):
        for command in self._commands:
            command.execute()


class Receiver:

    def action(self):
        print('Starting stage...')



def main():
    receiver = Receiver()
    stage1 = scorer.ScoreRequests(receiver)
    stage2 = scheduler.ScheduleTrip(receiver)
    stage3 = assigner.AssignStuffs(receiver)
    invoker = TripManager()
    invoker.store_command(stage1)
    invoker.store_command(stage2)
    invoker.store_command(stage3)
    invoker.execute_command()


if __name__ == "__main__":
    main()
