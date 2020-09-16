#Mindy Jun
#25957137

class true_range:
    def __init__(self, info, num_days):
        self._info = info
        self._num_days = num_days


    def indicator(self):
        temp = 0
        high_list = self._info[2]
        low_list = self._info[3]
        closing_list = self._info[4]
        tr_list = ['']
        
        for day in range(1, self._num_days):
            high_price = high_list[day]
            low_price = low_list[day]
            prev_closing = closing_list[day-1]
            if prev_closing < low_price:
                low_price = prev_closing
            elif prev_closing > high_price:
                high_price = prev_closing
            temp = (100 * ((high_price - low_price)/prev_closing))
            tr_list.append('%.4f' % (temp))
        return tr_list


class simple_moving_prices:
    def __init__(self, info, num_days):
        self._info = info
        self._num_days = num_days

    def indicator(self):
        avgs = []
        closing_vals = []
        closing_list = self._info[4]

        for x in range(self._num_days-1):
            avgs.append('')
            closing_vals.append(closing_list[x])

        closing_vals.append(closing_list[self._num_days-1])
        avgs.append('%.4f' % (sum(closing_vals)/self._num_days))
        
        for day in range(self._num_days, len(self._info[0])):
            closing_vals.remove(closing_vals[0])
            closing_vals.append(closing_list[day])
            avgs.append('%.4f' % (sum(closing_vals)/self._num_days))
        return avgs

    
class simple_moving_vols:
    def __init__(self, info, num_days):
        self._info = info
        self._num_days = num_days

    def indicator(self):
        avgs = []
        vol_vals = []
        volume_list = self._info[5]

        for x in range(self._num_days-1):
            avgs.append('')
            vol_vals.append(volume_list[x])

        vol_vals.append(volume_list[self._num_days-1])
        avgs.append('%.4f' % (sum(vol_vals)/self._num_days))
        
        for day in range(self._num_days, len(self._info[0])):
            vol_vals.remove(vol_vals[0])
            vol_vals.append(volume_list[day])
            avgs.append('%.4f' % (sum(vol_vals)/self._num_days))
        return avgs
        

class directional_prices:
    def __init__(self, info, num_days):
        self._info = info
        self._num_days = num_days

    def indicator(self):
        n = int(self._num_days)
        closing_list = self._info[4]
        dp_inc = []
        dp = [0]
        
        for x in range(len(closing_list)-1):
            if closing_list[x] < closing_list[x+1]:
                dp_inc.append(1)
            elif closing_list[x] > closing_list[x+1]:
                dp_inc.append(-1)
            else:
                dp_inc.append(0)
        for y in range(len(closing_list)-1):
            if y-n < 0:
                temp = sum(dp_inc[0:y+1])
            else:
                temp = sum(dp_inc[y-4:y+1])

            if temp > 0:
                dp.append('+' + str(temp))
            else:
                dp.append(str(temp))
        return dp
        
        
class directional_vols:
    def __init__(self, info, num_days):
        self._info = info
        self._num_days = num_days

    def indicator(self):
        n = int(self._num_days)
        volume_list = self._info[5]
        dp_inc = []
        dp = [0]
        
        for x in range(len(volume_list)-1):
            if volume_list[x] < volume_list[x+1]:
                dp_inc.append(1)
            elif volume_list[x] > volume_list[x+1]:
                dp_inc.append(-1)
            else:
                dp_inc.append(0)
        for y in range(len(volume_list)-1):
            if y-n < 0:
                temp = sum(dp_inc[0:y+1])
            else:
                temp = sum(dp_inc[y-4:y+1])

            if temp > 0:
                dp.append('+' + str(temp))
            else:
                dp.append(str(temp))
        return dp
