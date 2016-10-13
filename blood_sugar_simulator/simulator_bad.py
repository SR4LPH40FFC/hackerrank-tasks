from const import CONST
from datetime import datetime

class Simulator:

    bloodSugar = 0
    bloodSugarByTimestamp = dict()
    foodRates = dict()
    glycation = 0
    glycationByTimestamp = dict()
    tracker = list()

    def __init__(self):
        dayStart = datetime.date(datetime.utcnow()).strftime("%s")
        self.bloodSugarByTimestamp = {
            dayStart: CONST.INITIAL_BLOOD_SUGAR # TODO: define function
        }
        self.bloodSugar = 80
        self.getFoodRates()
        self.tracker = []

    """
    eat()
        string foodType - type of food, need to define rate of blood sugar increase
        int ts - when action starts, default = now() in unix_timestamp 
                        (number of seconds passed since 01/01/1970)
    Description: Eating food will increase blood sugar linearly for two hours
    """
    def eat(self, foodType, ts):
        self.tracker.append({
            'untilTimestamp': ts + CONST.AFTER_EAT_DURATION*60,
            'rate': 0 + self.foodRates[foodType]
        })

    """
    exercise()
        int ts - when action starts, default = now() in unix_timestamp 
                    (number of seconds passed since 01/01/1970)
    Description: Exercise decreases blood sugar linearly for one hour.
    """
    def exercise(self, ts):
        self.tracker.append({
            'untilTimestamp': ts + CONST.DURATION_AFTER_EXERCISE*60,
            'rate': 0 - self.foodRates['exercise']
        })

    def normalize(self, ts):
        if(len(self.tracker) == 0):
            if self.bloodSugar > 80:
                self.bloodSugar -= CONST.NORMALIZE_RATE
                self.bloodSugarByTimestamp[ts] = self.bloodSugar
            elif self.bloodSugar < 80:
                self.bloodSugar += CONST.NORMALIZE_RATE
                self.bloodSugarByTimestamp[ts] = self.bloodSugar 

    def getFoodRates(self):
        self.foodRates['exercise'] = 1
        self.foodRates['broccoli'] = 1
        self.foodRates['steak'] = 1
        self.foodRates['cake'] = 1
        self.foodRates['coffee'] = 1
        self.foodRates['banana'] = 1
        # TODO: get food rates from DB

#     def now(self):
#         return '1234567890' # TODO: return current date and time in unix_timestamp

    def remTrackerEvent(self, event):
        i = 0
        for evt in self.tracker:
            if evt['untilTimestamp'] == event['untilTimestamp']:
                del self.tracker[i]
            i+=1


    def calcGlycation(self, ts):
        if(self.bloodSugar > 150):
            self.glycation += 1
            self.glycationByTimestamp[ts] = self.glycation

