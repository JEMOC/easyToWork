

timeList1=['07:55', '12:01', '13:26', '18:00', '18:27', '21:30']
timeList2=['11:23']
timeList3=['07:56', '12:01', '13:17', '18:01', '18:22', '21:31']



def compute(timeList):
    morning = []
    afternoon = []
    night = []
    for times in timeList:
        time=int(times[0:2])
        min=int(times[3:6])
        if time in range(6,13):
            morning.append(times)
            continue

        if time in range(13,19):
            if time==13:
                afternoon.append(times)
                continue
            elif (time==18)&(min<15):
                afternoon.append(times)
                continue
            else:
                night.append(times)
                continue

        night.append(times)

    compute(timeList)
    print('morning:', end='')
    print(morning)
    print('after:', end='')
    print(afternoon)
    print('night:', end='')
    print(night)

