import csv
import datetime

DIR = './dataset/'
RAIN_FILES = [
    'RainfallHourlyData2012_Part1.csv',
    'RainfallHourlyData2012_Part2.csv',
    'RainfallHourlyData2013_Part1.csv',
    'RainfallHourlyData2013_Part2.csv',
    'RainfallHourlyData2014_Part1.csv',
    'RainfallHourlyData2014_Part2.csv'
]
TOWN_FILE = 'TAMBON.csv'

def get_thailand():
    town = list()
    district = list()
    province = list()
    thailand_csv = list()
    with open(DIR+TOWN_FILE, encoding='utf-8') as f:
        c = csv.reader(f, delimiter=',')
        thailand_csv = list(c)
    town_ids = set()
    district_ids = set() 
    province_ids = set()
    for record in thailand_csv[1:]:
        town_id = int(record[1])
        if town_id in town_ids:
            continue
        town_ids.add(town_id)
        town.append({
            'id': int(record[1]),
            'district': int(record[4]),
            'thai': record[2].split(' ')[1].strip(),
            'english': record[3].strip(),
            'latitude': float(record[10]),
            'longtitude': float(record[11])       
        })
        district_id =  int(record[4])
        if district_id in district_ids:
            continue
        district_ids.add(district_id)
        district.append({
            'id': int(record[4]),
            'province': int(record[7]),
            'thai': record[5].split(' ')[1].strip(),
            'english': record[6].strip(),            
        })
        province_id =  int(record[7])
        if province_id in province_ids:
            continue
        province_ids.add(province_id)
        province_thai = record[8].split(' ')
        province.append({
            'id': int(record[7]),
            'thai': province_thai[len(province_thai)-1].strip(),
            'english': record[9].strip(),            
        })        
    return town, district, province

def parse_town(address):
    for word in ['ต.','ตำบล','แขวง']:
        if word in address:
            return address.split(word)[1].strip().split(' ')[0]
    return ''

def parse_district(address):
    for word in ['อ.','อำเภอ','เขต']:
        if word in address:
            return address.split(word)[1].strip().split(' ')[0]
    return ''

def get_rain():
    station = list()
    rain = list()
    rain_csv = list()
    for rain_file in RAIN_FILES:
        with open(DIR+rain_file, encoding='unicode_escape') as f:
            c = csv.reader(f, delimiter=',')
            rain_csv = rain_csv + list(c)
    station_ids = set()
    format_str = '%d/%m/%Y %H' # The format
    for record in rain_csv:
        station_id = int(record[0].strip())
        if not station_id in station_ids:
            address = record[2].strip()
            station.append({
                'id': station_id,
                'name': record[1].strip(),
                'address': '' if address == 'NULL' else address,
                'latitude': float(record[4].strip()),
                'longtitude': float(record[5].strip()),
                'town': parse_town(address),
                'district': parse_district(address),
                'province': record[3].strip(),
            })
            station_ids.add(station_id)
        for i in range(24):
            try:
                current_rain = float(record[7+i].strip())
            except: 
                continue
            date_str = record[6].strip()+' {:02d}'.format(i)
            current_time = datetime.datetime.strptime(date_str, format_str)
            if current_rain > 0:
                rain.append({
                    'station': station_id,
                    'time': current_time,
                    'fall': current_rain
                })
    return rain, station