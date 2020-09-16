#Mindy Jun
#25957137

import api_methods as am
import strategy_classes as sc
import indicator_classes as ic

def print_header(symbol, tot_days, strat_input):
    print(symbol)
    print(tot_days)
    print(strat_input)
    print("Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell?")

def main(user_input, info, total_days):
    '''Goes through user input to return indicator, buy, and sell values.'''
    if 'TR' in user_input:
        ind = ic.true_range(info, total_days).indicator()
        st = sc.true_range_strat(info,total_days, user_input).buy_or_sell()
    elif 'MP' in user_input:
        temp = user_input.split()
        ind =  ic.simple_moving_prices(info, int(temp[1])).indicator()
        st = sc.simple_moving_price_strat(info, total_days, user_input).buy_or_sell()
    elif 'MV' in user_input:
        temp = user_input.split()
        ind =  ic.simple_moving_vols(info, int(temp[1])).indicator()
        st = sc.simple_moving_vol_strat(info, total_days, user_input).buy_or_sell()
    elif 'DP' in user_input:
        ind = ic.directional_prices(info, total_days).indicator()
        st = sc.directional_price_strat(info, user_input).buy_or_sell()
    elif 'DV' in user_input:
        ind = ic.directional_vols(info, total_days).indicator()
        st = sc.directional_vol_strat(info, user_input).buy_or_sell()
    return [ind, st[0], st[1]]


def print_report(date, o, high, low, close, volume, indicator, b, s):
    for day in range(len(date)):
        print('%s\t%.4f\t%.4f\t%.4f\t%.4f\t%s\t%s\t%s\t%s' %
              (date[day], o[day], high[day], low[day], close[day], volume[day],
              indicator[day], b[day], s[day]))
    

if __name__ == '__main__':
    api_path = input()
    partial_url = input() #i/e https://www.alphavantage.co
    symbol = input()
    start_date = input() #yyyy-mm-dd
    end_date = input()
    strat = input() #includes buy and sell thresholds

    api = am.get_api(api_path)
    full_url = am.build_search_url(partial_url, symbol, api)
    all_info = am.get_info(am.get_txt(full_url))
    info = am.condense_info(all_info, start_date, end_date)
    tot_days = len(info[0])

    x = main(strat, info, tot_days)
    ind = x[0]
    buy = x[1]
    sell = x[2]
    
    
    #print report
    print_header(symbol, tot_days, strat)
    print_report(info[0], info[1], info[2], info[3], info[4], info[5], ind, buy, sell)
    
