class Iq_Binary31:
      '''alternatives algorithm for iqoption binary trading '''
      import random
      from pyiqoptionapi import IQOption
      import time
      import numpy as np
      import sys 
      Money =3*[1]
      ACTIVES = 3*["EURUSD"]
      expirations_mode = 3*[1]
      ACTION = ["call","put"]
      i = [0,1,0]
      sleep_time = 53
      strike_time = 60
      balance=0
      def __init__(self):
          print("from pyiqoptionapi import IQOption")
          print("import random")
          print("import time")
          
          print("login! :IQOption('arvind8198@gmail.com','%mG+H6vuvD_ETtC')")
          self.Iq=self.IQOption("arvind8198@gmail.com","%mG+H6vuvD_ETtC")
          print("connection to iqoption")
          check = self.Iq.connect()#connect to iqoption
          print(check)
          self.Money=3*[1]
          self.i =[0,1,0]
          print(self.Iq.get_balance())
          self.balance = self.Iq.get_balance()
      
      def loss_distribution(self,loss,n,get_profit):
          x = int((-loss/(2*get_profit-1))+1)
          return 3*[x]
        
      def reset(self):
          self.Money=3*[1]
          self.i =[0,1,0]
          self.balance = self.Iq.get_balance()
        
      def set_ACTIVES(self, ACTIVES):
          self.ACTIVES = 3*[ACTIVES]
        
      def set_expirations_mode(self,expirations_mode):
          self.expirations_mode = 3*[expirations_mode]
            
      def set_Money(self, Money):
          self.Money = 3*[Money]
      
      def set_sleep_time(self,sleep_time):
          self.sleep_time = sleep_time
      
      def set_strike_time(self,strike_time):
          self.strike_time = strike_time
        
      def get_action(self,i1,i2,i3):
          return [self.ACTION[i1],self.ACTION[i2],self.ACTION[i3]]
        
      def get_details(self):
          print("Money :{},ACTION :{}, ACTIVES :{}, expiration_mode :{}".format(self.Money,self.ACTION,self.ACTIVES, self.expirations_mode))
      
      def get_algo_details(self):
          print("Index :{}, sleep_time :{}, strike_time :{}".format(self.i, self.sleep_time, self.strike_time))
        
      def algo1(self,n):
          f=3*[1]
          get_p=0
          get_profit=0
          sum_profit=2
          loss_counter=3*[0]
          while True:
                if(self.Iq.get_remaning(1)<self.strike_time):
                   Id = self.Iq.buy_multi(self.Money, self.ACTIVES,self.get_action(self.i[0],self.i[1],self.i[2]), self.expirations_mode)
                   #Id= [k[1] for k in Id_t]
                   break
          print(Id,self.get_action(self.i[0],self.i[1],self.i[2]))
          print(self.time.sleep(self.sleep_time))
          count=0
          check_w =3*[0]
          while True:
                remaning_time=self.Iq.get_remaning(self.expirations_mode[0])
                #purchase_time=remaning_time-30
                #Iq.get_balance()
                print(remaning_time)
                if(count>n):
                   print("Profit=",self.Iq.get_balance()-self.balance)
                   break
                count = count+1
                while True:
                      if(self.Iq.get_remaning(1)<60):
                        # if purchase_time<4:#buy the binary option at purchase_time<4
                        #count=count+1
                        profit_t = list(map(self.Iq.check_win_v4,Id))
                        profit = [k[1] for k in profit_t]
                        if(get_p==0 and sum(profit)!=0):
                            P_arr = self.np.array(profit)
                            get_profit= P_arr[self.np.where(P_arr>0)][0]
                            if(get_profit is not None):
                                get_p=1
                        print(profit)
                        for j in range(len(profit)):
                            
                            if profit[j] is None:
                               continue   
                            if(profit[j]>0):
                               #bal = Iq.get_balance()
                               #print("W",self.Iq.get_balance())
                               check_w[j]="W"
                               self.Money[j]=1
                               f[j]=1
                               loss_counter[j]=0
                               if(j<2):
                                 self.i[j]=~self.i[j]
                            else :
                               if(profit[j]==0):
                                 #print("d",self.Iq.get_balance())
                                 check_w[j]="D"
                                 continue
                               #bal = Iq.get_balance()
                               #print("L",self.Iq.get_balance())
                               check_w[j]="L" 
                               self.Money[j]=2*self.Money[j]+f[j]
                               f[j] = f[j]+1
                               loss_counter[j]=loss_counter[j]+1
                               if(j<=2):
                                 self.i[j]=~self.i[j]
                               #if(self.Money[j]>9):
                                 #check,Id = self.Iq.buy(2*self.Money+flag,self.ACTIVES,self.ACTION[self.index],                                                          self.expirations_mode)
                                # self.i[j] = self.random.randint(0,1)
                        if(check_w[0]=='L' and check_w[1]=='L'):
                           self.i[0]=0
                           self.i[1]=1
                    
                        if(loss_counter[2]>=1 and loss_counter[0]>2):
                            #self.i[2]=self.random.randint(0,1)
                            self.i[2]= ~self.i[2]
                            loss_counter[2]=self.random.randint(0,1)
                        if(loss_counter[2]>=1 and loss_counter[1]>2):
                            #self.i[2]=self.random.randint(0,1)
                            self.i[2]=~self.i[2]
                            loss_counter[2]=self.random.randint(0,1)
                        if None in profit:
                            count=100
                            break
                        sum_profit = sum_profit+sum(profit)
                        if(sum_profit<-15):
                            count=100
                            break
                        if(sum_profit>5):
                            sum_profit=2
                            self.Money = 3*[1]
                            f=3*[1]
                            loss_counter = 3*[0]
                        if(sum_profit>=0):
                            e=[k for k in self.Money if k>10]
                            if(len(e)>0):
                               # e=self.Money[self.Money>3*[20]]
                                self.Money[check_w.index('L')]=3
                        print("sum_profit=",sum_profit)
                        if(sum_profit<-1):
                           self.Money=self.loss_distribution(sum_profit,3,get_profit)
                           f=3*[1]
                           # count=100
                           # break
                       # if(sum_profit>-3 and sum_profit<-2):
                        #    self.Money = 3*[3]
                       # if(sum_profit>-2 and sum_profit<-1):
                       #     self.Money = 3*[2]
                       # if(sum_profit>-1 and sum_profit<0):
                       #     self.Money = 3*[1]
                        Id = self.Iq.buy_multi(self.Money,self.ACTIVES,                        self.get_action(self.i[0],self.i[1],self.i[2]), self.expirations_mode)
                        profit_r = [round(a,2) for a in profit if a is not None]
                        print(profit_r,check_w,"ACTION=",self.i,"Money=",self.Money,"flag=",f,"loss_c=",loss_counter)
                        break
                self.time.sleep(self.sleep_time)