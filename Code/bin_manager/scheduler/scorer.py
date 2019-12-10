# import manager.Command
#
from datetime import date
from django.db.models import Q
from scheduler import commander
from django.utils import timezone

from mgr_database.models import RequestDetail, Score, Customer

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
    def get_requests(self):
        pass
    def execute(self,stages):
        self._receiver.action()
        print('This is the scorer !')
        stages.append('Scorer starting '+str(date.today()))
        # stages.append(str(timezone.now()))
        if not self._receiver.check_error() :
            req_today = RequestDetail.objects.filter(Q(pickup_date__lte = date.today()) & Q(request_status = 'New' or 'In Process'))
            for req in req_today:
                age = date.today() - req.pickup_date
                distance = 3 #this will come from maps


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
            stages.append('Scorer completed'+self._receiver.get_waste())
            self._receiver.set_error(False)
        else:
            print('Previous Stage Error!')
            stages.append('Scorer not completed!!')
