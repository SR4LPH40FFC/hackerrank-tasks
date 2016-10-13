from simulator import Simulator
import json
from const import CONST
from datetime import date, datetime

__debug = 1

"""
jsonData = {
    // sorted by timestamp
    'events': [
        {
            'timestamp': 10000000,
            'actions': {
                'eat': ['broccoli', 'steak', 'cake'],
                'exercise': ['exercise', 'exercise'] // can be potentially extended for various types of exercises with different rates
            }
        },
        {
            'timestamp': 10000001,
            'actions': {
                'exercise': ['exercise'] // can be potentially extended for various types of exercises with different rates
            }
        },
        {
            'timestamp': 10000002,
            'actions': {
                'eat': ['coffee']
            }
        },
        {
            'timestamp': 10000003,
            'actions': {
                'eat': ['banana'],
                'exercise': ['exercise'] // can be potentially extended for various types of exercises with different rates
            }
        }        
    ]
}
"""
def main(jsonData):
    # extract data from json to dictionary
    data = json.loads(jsonData)

    # initialize Simulator
    sim = Simulator()

    # sort data events by timestamp TODO: this operation is optional
    data['events'].sort(key=lambda x: x['timestamp'])

    # for each reported event
    for evts in data['events']:

        totalRate = 0
        for action in evts['actions']:
            for rateType in evts['actions'][action]:
                multiplicator = 1
                evt_duration = 2*60*60

                if action == 'exercise':
                    multiplicator = -1
                    evt_duration = 1*60*60

                totalRate = sim.foodRates[rateType]*multiplicator

                for ts in range(evts['timestamp']+CONST.INTERVAL, evts['timestamp']+CONST.INTERVAL+evt_duration, CONST.INTERVAL):
                    sim.timeline[ts] += totalRate
                    sim.timelineTouched[ts] = True

#     for i in range(10):
#         print str(i)+"        ",
#     print
#     for _ in range(10):
#         for j in range(0,10,2):
#             print j,
#     print


    sim.timeline[sim.dayStartTS-CONST.INTERVAL] = 80

    for ts in range(sim.dayStartTS, sim.dayEndTS, CONST.INTERVAL):
        sim.timeline[ts] += sim.timeline[ts-CONST.INTERVAL]

    # normalization
    for ts in range(sim.dayStartTS+CONST.INTERVAL, sim.dayEndTS, CONST.INTERVAL):
        if(not sim.timelineTouched[ts]):
            multiplicator = 0
            if(sim.timeline[ts-CONST.INTERVAL] < 80):
                multiplicator = 1
            elif(sim.timeline[ts-CONST.INTERVAL] > 80):
                multiplicator = -1
            sim.timeline[ts] = sim.timeline[ts-CONST.INTERVAL] + sim.foodRates['normalize']*multiplicator

        
    for ts in range(sim.dayStartTS, sim.dayEndTS, CONST.INTERVAL):
        print str(datetime.fromtimestamp(ts)) + ": " + str(sim.timeline[ts])


if __name__ == '__main__':
    jsonData = '''
{
    "events": [
        {
            "timestamp": 1476072000,
            "actions": {
                "eat": ["broccoli"],
                "exercise": ["exercise"]
            }
        },
        {
            "timestamp": 1476075600,
            "actions": {
                "exercise": ["exercise"]
            }
        },
        {
            "timestamp": 1476079200,
            "actions": {
                "eat": ["coffee"]
            }
        },
        {
            "timestamp": 1476082800,
            "actions": {
                "eat": ["banana"],
                "exercise": ["exercise"]
            }
        }        
    ]
}
    '''
#     jsonData = '''
# {
#     "events": [
#         {
#             "timestamp": 1476072000,
#             "actions": {
#                 "eat": ["broccoli"]
#             }
#         }
#     ]
# }
#     '''
    main(jsonData)




