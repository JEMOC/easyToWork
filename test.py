# from datetime import datetime
# times_list=['07:43','12:01','13:23','18:01','18:23','21:32']
# data="11:2114:4516:2018:2321:32"
# list='07:4312:01'
#
#
# # def getTimeSub(time,comTime):
# #     time_hour=int(time[0:2])
# #     time_min=int(time[3:6])
# #     comtime_hour = int(comTime[0:2])
# #     comtime_min = int(comTime[3:6])
# #     time1=datetime(2018,1,1,time_hour,time_min)
# #     time2=datetime(2018,1,1,comtime_hour,comtime_min)
# #     if(time1<=time2):
# #         return 0
# #     else:
# #         timesecond=(time1-time2).seconds/60
# #     print(time1)
# #     print(time2)
# #     print(time2<time1)
# #     print("time:",timesecond)
#
# # morning=[]
# # afternoon=[]
# # night=[]
# # time_list=[]
# # i=0
# # late=0
# # early=0
# # overtime=0
# # while i < len(data):  # 分割时间戳
# #      time_list.append(data[i:i + 5])
# #      i += 5
# #
# # print(time_list)
# #
# # for times in time_list:
# #     time=int(times[0:2])
# #     min=int(times[3:6])
# #     if time in range(6,13):
# #         morning.append(times)
# #     elif time in range(13,19):
# #         if time==13:
# #             afternoon.append(times)
# #         elif (time==18)&(min<15):
# #             afternoon.append(times)
# #         else:
# #                 afternoon.append(times)
# #     else:
# #         night.append(times)
# #
# # if len(morning)==2:
# #     time=morning[0]
# #     print(time)
# #     hour = int(time[0:2])
# #     min = int(time[3:6])
# #     if(hour>=8):
# #         late=(hour - 8) * 60 + min
# #         print("late:%dmin"%late)
# #     # morning.append('缺卡')
# #     time=morning[1]
# #     print(time)
# #     hour= int(time[0:2])
# #     min= int (time[3:6])
# #     if(hour<12):
# #         early=(11 - hour) * 60 + (60 - min)
# #         print("early:%dmin"%early)
# #
# # if len(afternoon)==2:
# #     time=afternoon[0]
# #     print(time)
# #     hour = int(time[0:2])
# #     min = int(time[3:6])
# #     if((hour+min/10)>13.3):
# #         if(hour==13):
# #             late=min-30
# #         else:
# #             late=(hour-13)*60+30+min
# #         print("late:%dmin"%late)
# #     # morning.append('缺卡')
# #     time=afternoon[1]
# #     print(time)
# #     hour= int(time[0:2])
# #     min= int (time[3:6])
# #     if(hour<18):
# #         early=(17 - hour) * 60 + (60 - min)
# #         print("early:%dmin"%early)
# #
# # if night:
# #     time=night[len(night)-1]
# #     hour=int(time[0:2])
# #     min=int(time[3:6])
# #     overtime=hour-18+min/60
#
#
# #
# # print(morning)
# # print(afternoon)
# # print(night)
# # getTimeSub("09:20","08:00")
#
# def splitTime(data):
#     i=0
#     times=[]
#     while i <len(data):
#         times.append(data[i:i+5])
#         i += 5
#     return times
#     print(times)
#
# def classtime():
#     early=0
#     late=0
#     overtime=0
#     times = splitTime(data)
#     print(times[1])
#     morning=[]
#     afternoon=[]
#     night=[]
#     i=0
#     timed=[]
#     lens=len(times)
#     for time in times:
#         hour=int(time[0:2])
#         min=int(time[3:6])
#         if (i == 0):
#             if hour==12 or hour == 11:
#                 morning.append('缺卡')
#                 morning.append(time)
#                 if hour==11:
#                     early += (datetime(2018,1,1,12,0)-datetime(2018,1,1,hour,min)).seconds/60
#             elif hour < 11:
#                 morning.append(time)
#
#     print(morning)
#     print(early)
#     i+=1
#
# classtime()
#
#
workday=5
wb_row=4
infostr2 = "\"上班\"&AF" + str(wb_row + 2) + "&\"天\""
print(infostr2)
