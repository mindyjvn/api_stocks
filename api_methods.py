#Mindy Jun
#25957137

from pathlib import Path
import urllib.request
import urllib.parse
import urllib.error
import json

def get_api(text_file):
    path = Path(text_file)
    with open(path, 'r') as f:
        api = f.read()
    return api
        
    
def build_search_url(url, symbol, apikey):
    query_param = [
        ('function', 'TIME_SERIES_DAILY'), ('symbol', symbol), ('outputsize', 'full'), ('apikey',apikey)
         ]
    return url + '/query?' + urllib.parse.urlencode(query_param)


def get_txt(url):
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response. This is taken from the API notes.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    except urllib.error.HTTPError as error:
        print('FAILED')
        print(error.code)
        if error.code != 200:
            print('NOT 200')
        else:
            print('FORMAT')
    except urllib.error.URLError as e:
        print('FAILED')
        print(0)
        print('NETWORK')
        
    finally:
        if response != None:
            response.close()

def get_info(text):
    daily_info = text['Time Series (Daily)']
    dates = []
    opening = []
    high = []
    low = []
    closing = []
    volume = []
    
    for k in daily_info.keys():
        dates.append(k)
        opening.append(float(daily_info[k]['1. open']))
        high.append(float(daily_info[k]['2. high']))
        low.append(float(daily_info[k]['3. low']))
        closing.append(float(daily_info[k]['4. close']))
        volume.append(int(daily_info[k]['5. volume']))

    dates.reverse()

    return [dates, opening, high, low, closing, volume]

def condense_info(info, start_date, end_date):
    dates = info[0]
    opening = info[1]
    high = info[2]
    low = info[3]
    closing = info[4]
    volume = info[5]
    start_index = 0
    end_index = 0

    for day in range(len(dates)):
        if dates[day] == start_date:
            start_index = day
        elif dates[day] == end_date:
            end_index = day
    dates = info[0][start_index:end_index + 1]
    opening = info[1][start_index:end_index + 1]
    high = info[2][start_index:end_index + 1]
    low = info[3][start_index:end_index + 1]
    closing = info[4][start_index:end_index + 1]
    volume = info[5][start_index:end_index + 1]

    return [dates, opening, high, low, closing, volume]
        
    
