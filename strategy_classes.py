#Mindy Jun
#25957137

import indicator_classes as ic

class true_range_strat:
    def __init__(self, info, num_days, strat_input):
        self._info = info
        self._num_days = num_days
        self._strat_input = strat_input

    def buy_or_sell(self):
        tr_obj = ic.true_range(self._info, self._num_days)
        tr_list = tr_obj.indicator()
        
        buy_list = ['']
        sell_list = ['']
        closing_prices = self._info[4]
        temp = self._strat_input.split()

        buy_sign = temp[1][0]
        buy_threshold = float(temp[1][1:])
        sell_sign = temp[2][0]
        sell_threshold = float(temp[2][1:])

        for day in range(1,len(closing_prices)):
            tr = float(tr_list[day])

            if buy_sign == '>':
                if tr > buy_threshold:
                    buy_list.append('BUY')
                else:
                    buy_list.append('')
            else:
                if tr < buy_threshold:
                    buy_list.append('BUY')
                else:
                    buy_list.append('')

            if sell_sign == '>':
                if tr > sell_threshold:
                    sell_list.append('SELL')
                else:
                    sell_list.append('')
            else:
                if tr < sell_threshold:
                    sell_list.append('SELL')
                else:
                    sell_list.append('')
        return [buy_list, sell_list]

class simple_moving_price_strat:
    def __init__(self, info, num_days, strat_input):
        self._info = info
        self._num_days = num_days
        self._strat_input = strat_input
        
    def buy_or_sell(self):
        smp_obj = ic.simple_moving_prices(self._info, self._num_days)
        avgs = smp_obj.indicator()
        
        buy_list = ['']
        sell_list = ['']
        closing_prices = self._info[4]

        for day in range(1, len(closing_prices)):
            avg = avgs[day]
            if avg == '':
                avg = 0
            else:
                avg = float(avg)
            prev_avg = avgs[day - 1]
            if prev_avg == '':
                prev_avg = 0
            else:
                prev_avg = float(prev_avg)
            closing_price = closing_prices[day]
            prev_closing_price = closing_prices[day-1]
            
            if closing_price > avg:
                if prev_closing_price < prev_avg:
                    buy_list.append('BUY')
                else:
                    buy_list.append('')
            else:
                buy_list.append('')

            if closing_price < avg:
                if prev_closing_price > prev_avg:
                    sell_list.append('SELL')
                else:
                    sell_list.append('')
            else:
                sell_list.append('')
        return [buy_list, sell_list]


class simple_moving_vol_strat:
    def __init__(self, info, num_days, strat_input):
        self._info = info
        self._num_days = num_days
        self._strat_input = strat_input
        
    def buy_or_sell(self):
        smp_obj = ic.simple_moving_vols(self._info, self._num_days)
        avgs = smp_obj.indicator()
        
        buy_list = ['']
        sell_list = ['']
        vol_prices = self._info[5]

        for day in range(1, len(vol_prices)):
            avg = avgs[day]
            if avg == '':
                avg = 0
            else:
                avg = float(avg)
            prev_avg = avgs[day - 1]
            if prev_avg == '':
                prev_avg = 0
            else:
                prev_avg = float(prev_avg)
            vol_price = vol_prices[day]
            prev_vol_price = vol_prices[day-1]
            
            if vol_price > avg:
                if prev_vol_price < prev_avg:
                    buy_list.append('BUY')
                else:
                    buy_list.append('')
            else:
                buy_list.append('')

            if vol_price < avg:
                if prev_vol_price > prev_avg:
                    sell_list.append('SELL')
                else:
                    sell_list.append('')
            else:
                sell_list.append('')
        return [buy_list, sell_list]      

        
class directional_price_strat:
    def __init__(self, info, strat_input):
        self._info = info
        self._strat_input = strat_input

    def buy_or_sell(self):
        temp = self._strat_input.split()
        dp_period = temp[1]
        buy_threshold = float(temp[2])
        sell_threshold = float(temp[3])
        print(buy_threshold, sell_threshold)

        dp_obj = ic.directional_prices(self._info, dp_period)
        dp_list = dp_obj.indicator()
        buy_list = ['']
        sell_list = ['']

        for day in range(1, len(self._info[0])):
            dp = float(dp_list[day])
            prev_dp = float(dp_list[day - 1])

            if dp > buy_threshold:
                if prev_dp <= buy_threshold:
                    buy_list.append('BUY')
                else:
                    buy_list.append('')
            else:
                buy_list.append('')

            if dp < sell_threshold:
                if prev_dp >= sell_threshold:
                    sell_list.append('SELL')
                else:
                    sell_list.append('')
            else:
                sell_list.append('')
        return [buy_list, sell_list]
                
        
class directional_vol_strat:
    def __init__(self, info, strat_input):
        self._info = info
        self._strat_input = strat_input

    def buy_or_sell(self):
        temp = self._strat_input.split()
        dp_period = temp[1]
        buy_threshold = float(temp[2])
        sell_threshold = float(temp[3])

        dp_obj = ic.directional_vols(self._info, dp_period)
        dp_list = dp_obj.indicator()
        buy_list = ['']
        sell_list = ['']

        for day in range(len(self._info[0])):
            dp = float(dp_list[day])
            prev_dp = float(dp_list[day - 1])

            if dp > buy_threshold:
                if prev_dp <= buy_threshold:
                    buy_list.append('BUY')
                else:
                    buy_list.append('')
            else:
                buy_list.append('')

            if dp < sell_threshold:
                if prev_dp >= sell_threshold:
                    sell_list.append('SELL')
                else:
                    sell_list.append('')
            else:
                sell_list.append('')
        return [buy_list, sell_list]
        
