'''This program calculates ADX and RSA values from candle stream'''

class RAS:
      
      # init method or constructor
      import pandas as pd
      import talib as tl     
      from AlmaIndicator import ALMAIndicator 
      def __init__(self, df=['time','open','high','low','close']):
          self.df = self.pd.DataFrame(columns=df)
          
      def ras(self,Dict):
          # insert values in the candle stick self.df frame
          self.df['time'] = [i for i in Dict.keys()]
          #self.df['ask'] = [Dict[i]['ask'] for i in Dict.keys() if Dict[i]!= {}]
          #self.df['bid'] = [Dict[i]['bid'] for i in Dict.keys() if Dict[i]!= {}]
          self.df['open'] = [Dict[i]['open'] for i in Dict.keys() if Dict[i]!= {}]
          self.df['high'] = [Dict[i]['max'] for i in Dict.keys() if Dict[i]!= {}]
          self.df['low'] = [Dict[i]['min'] for i in Dict.keys() if Dict[i]!= {}]
          self.df['close'] = [Dict[i]['close'] for i in Dict.keys() if Dict[i]!= {}]
          
          # calculate ADX, RAS and thereafter decision #.rolling(60).mean()
          #calculate ADX, +DI, -DI, and relative absolute Speed index
          self.df['ADX'] = self.tl.ADX(self.df['high'].rolling(12).mean(),self.df['low'].rolling(12).mean(),self.df['close'].rolling(12).mean(), timeperiod=14*12) 
          self.df['+DI'] = self.tl.PLUS_DI(self.df['high'].rolling(12).mean(),self.df['low'].rolling(12).mean(),self.df['close'].rolling(12).mean(),timeperiod = 14*12) 
          self.df['-DI'] = self.tl.MINUS_DI(self.df['high'].rolling(12).mean(),self.df['low'].rolling(12).mean(),self.df['close'].rolling(12).mean(), timeperiod = 14*12)
          self.df['ALMA'] = self.ALMAIndicator(close=self.df['close'].rolling(12).mean()).alma()
          #self.df['ADX'] = self.tl.ADX(self.df['high'],self.df['low'],self.df['close'], timeperiod=14) 
          #self.df['+DI'] = self.tl.PLUS_DI(self.df['high'],self.df['low'],self.df['close'],timeperiod = 14) 
          #self.df['-DI'] = self.tl.MINUS_DI(self.df['high'],self.df['low'],self.df['close'], timeperiod = 14)
          #self.df['ALMA'] = self.ALMAIndicator(close=self.df['close']).alma()
          P_DI_diff= self.df['+DI'].diff(1)
          M_DI_diff= self.df['-DI'].diff(1)
          True_change = (P_DI_diff*M_DI_diff<0).apply(lambda x: 1 if x else 0)
          self.df_DIP = (P_DI_diff*True_change).rolling(9).mean()
          self.df_DIM = (M_DI_diff*True_change).rolling(9).mean()
          #self.df['RAS'] = (self.df_DIM.abs()+self.df_DIP.abs())
          self.df['Decision'] = (self.df_DIM<self.df_DIP).apply(lambda x: 1 if x else 0)
          self.df['RAS'] = (self.df_DIP.abs()+self.df_DIM.abs())
          
          return self.df.loc[self.df.index[-800:]]
          
