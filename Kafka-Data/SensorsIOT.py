import pandas as pd
import datetime
import pytz
import time
import random

def get_time_date():
   
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Kuala_Lumpur"))
    d = pst_now.strftime("%m/%d/%Y")
    t = pst_now.strftime("%H:%M:%S")

    return d, t

def get_sensor_data():
    sensor_1 = random.choice([True, False])
    sensor_2 = random.choice([True, False])
    sensor_3 = random.choice([True, False])
    queue_length = 0
    queue_status = 'low'

    if(sensor_1 == False):
        sensor_2 = False
        sensor_3 = False

    if(sensor_2 == False):
        sensor_3 = False  

    if(sensor_1 == False and sensor_2 == False and sensor_3 == False):
        queue_length = '0%'
        queue_status = 'none'

    elif(sensor_1 == True and sensor_2 == False and sensor_3 == False):
        queue_length = '25%'
        queue_status = 'low'

    elif(sensor_1 == True and sensor_2 == True and sensor_3 == False):
        queue_length = '60%'
        queue_status = 'normal'    

    elif(sensor_1 == True and sensor_2 == True and sensor_3 == True):
        queue_length = '100%'
        queue_status = 'high'
    
    d,t = get_time_date()

    return sensor_1, sensor_2, sensor_3, queue_length, queue_status, d, t

while True:
  
    s1, s2, s3, ql, qs, d, t = get_sensor_data()

    new_data_1 = {   
            'DATE': d,
            'TIME': t,
            'BRANCH': 'Taman Connaught',
            'SENSOR_1': s1,
            'SENSOR_2': s2,
            'SENSOR_3': s3,
            'QUEUE_LENGTH': ql,
            'QUEUE_STATUS': qs,
        }

    print(new_data_1)

    time.sleep(1)

