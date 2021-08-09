from pyiqoptionapi import IQOption
import time
from RAS import RAS
Iq = IQOption("arvind8198@gmail.com","%mG+H6vuvD_ETtC")
Iq.connect()
Money=5
ACTIVES="EURUSD"
index=0
flag=0
ACTION=["call","put"]
expirations_mode=1
count=0
size =2
bal=Iq.get_balance()
print(bal)
check,Id = Iq.buy(1, "EURUSD", "call", 1)
print(check,Id)
while True:
      if(Iq.get_remaning(1)<60):
         check,Id = Iq.buy(1, "EURUSD", "call", 1)
         break
        # print(check,Id)
if(Iq.get_remaning(1)>9): 
  time.sleep(Iq.get_remaning(1)+3)
profit_sum=0
RS = RAS()
Iq.start_candles_stream(ACTIVES,size,1000)
while True:
      remaning_time=Iq.get_remaning(expirations_mode)
      #purchase_time=remaning_time-30
      #Iq.get_balance()
      print(remaning_time)
      if(count>20):
        print("Profit=",Iq.get_balance()-bal)
       # break
       # if purchase_time<4:#buy the binary option at purchase_time<4
      count=count+1
      if(flag>4):
          break
      while True:
             if(check and Iq.get_remaning(1)<60):
                check,profit = Iq.check_win_v4(Id)
                profit_sum=profit_sum + profit
                candels = Iq.get_realtime_candles(ACTIVES,size)
                RS = RAS()
                data = RS.ras(candels)
                ll = len(data)-2
               # D_diff = abs(data['+DI'][ll]-data['-DI'][ll])
               # ADX_diff = abs(data['+DI'][ll]-data['ADX'][ll])+abs(data['ADX'][ll]-data['-DI'][ll])
                print(data.loc[ll])
                alma = data['ALMA'][ll]
                low  = data['low'][ll]
                high = data['high'][ll]
                Open = data['open'][ll]
                close = data['close'][ll]
                print(alma,low,high)
                if (low<alma and alma<high):
                    break
                if(low>=alma):
                    if(close-Open>0):
                      index = 0
                    else:
                      break
                if(high<=alma):
                    if(Open-close>0):
                      index = 1
                    else:
                      break        
                if(profit>0):
                  #bal = Iq.get_balance()
                  print("W",Iq.get_balance())
                  Money=5
                  flag=1
                  check,Id = Iq.buy(Money,ACTIVES,ACTION[index],expirations_mode)
                  print(ACTION[index])
                  #index = ~index 
                  print(check,Id)
                else :
                  if(profit==0):
                    check,Id = Iq.buy(Money,ACTIVES,ACTION[index],expirations_mode)
                    break
                  
                  print("L",Iq.get_balance())
                  check,Id = Iq.buy(2*Money+flag,ACTIVES,ACTION[index],expirations_mode)
                  #index = ~index
                  Money=2*Money+flag
                  flag=flag+1
                  print(ACTION[index],Money,flag)
             break
      if(Iq.get_remaning(1)>9):
         time.sleep(Iq.get_remaning(1)+2)
         
