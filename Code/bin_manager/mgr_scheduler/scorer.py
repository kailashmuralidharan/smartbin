# import manager.Command
#
import commander


class RequestScoreElements:
    _distance = 0
    _age = 0
    _weight = 0

    def __init__(self,distance,age,weight):
        self._distance = distance
        self._age = age
        self._weight = weight




class CalculateScore:
    _request = None
    _age_score = 0
    _weight_score = 0
    _distance_score = 0
    _total_score = 0

    def __init__(self,request):
        self._request = request

    def calculateWeightScore(self):
        self._weight_score = self._request._weight / 50

    def calculateDistanceScore(self):
        self._distance_score = (self._request._distance / 10 )

    def calculateAgeScore(self):
        self._age_score = self._request._age / 5

    def calculateTotalScore(self):
        self._total_score = (self._age_score + self._weight_score + self._distance_score) / 3

    def displayScore(self):
        print('Age Score :', self._age_score,' Weight Score :', self._weight_score, ' Distance Score :', self._distance_score,' Total Score :', self._total_score)


class ScoreRequests(commander.Command):
    def execute(self):
        self._receiver.action()
        print('This is the scorer !')
        request1 = RequestScoreElements(-1,2,20)
        request2 = RequestScoreElements(-2,1,50)
        request3 = RequestScoreElements(-5,1,40)
        request_list = []
        request_list.append(request1)
        request_list.append(request2)
        request_list.append(request3)
        for requests in request_list:
            scorecalculator = CalculateScore(requests)
            scorecalculator.calculateDistanceScore()
            scorecalculator.calculateAgeScore()
            scorecalculator.calculateWeightScore()
            scorecalculator.calculateTotalScore()
            scorecalculator.displayScore()
