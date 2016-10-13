from const import CONST
from datetime import datetime, timedelta

class Simulator:
    timeline = dict()
    timelineTouched = dict()
    foodRates = dict()
    glycation = 0
    glycationByTimestamp = dict()
    dayStartTS = 0
    dayEndTS = 0

    def __init__(self):
        dayStartDT = datetime.date(datetime.utcnow())
        self.dayStartTS = int(dayStartDT.strftime("%s"))
        dayEndDT = dayStartDT + timedelta(days=1)
        self.dayEndTS = int(dayEndDT.strftime("%s"))

        for ts in range(self.dayStartTS, self.dayEndTS, CONST.INTERVAL):
            self.timeline[ts] = CONST.INITIAL_BLOOD_SUGAR
            self.timelineTouched[ts] = False

        self.getFoodRates()

    def getFoodRates(self):
        self.foodRates['exercise'] = 1
        self.foodRates['normalize'] = 1
        self.foodRates['broccoli'] = 1
        self.foodRates['steak'] = 1
        self.foodRates['cake'] = 1
        self.foodRates['coffee'] = 1
        self.foodRates['banana'] = 1
        # TODO: get food rates from DB

#     def calcGlycation(self, ts):
#         if(self.bloodSugar > 150):
#             self.glycation += 1
#             self.glycationByTimestamp[ts] = self.glycation

