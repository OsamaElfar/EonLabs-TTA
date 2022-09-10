import pandas as pd
import matplotlib.pyplot as plt

HOURLY_PATH = 'path/to/hourly/data'
WEEKLY_PATH = 'path/to/weekly/data'
MONTHLY_PATH = 'path/to/monthly/data'

def hourly_normalizd(hourly_path, weekly_path, monthly_path)

  hourly = pd.read_csv(hourly_path)
  weekly = pd.read_csv(weekly_path)
  monthly = pd.read_csv(monthly_path)
  
  #Convert date feature to datetime format
  hourly['date'] = pd.to_datetime(hourly['date'], format = "%Y-%m-%d %H:%M:%S")
  weekly['date'] = pd.to_datetime(weekly['date'], format = "%Y-%m-%d %H:%M:%S")
  monthly['date'] = pd.to_datetime(monthly['date'], format = "%Y-%m-%d %H:%M:%S")

  # Dropout August month from the data as it is not complet for whole 3 datasets
  hourly = hourly.loc[hourly['date'] < '2022-08-01']
  weekly = weekly.loc[weekly['date'] < '2022-08-01']
  monthly = monthly.loc[monthly['date'] < '2022-08-01']

  #iterate for each week in weekly data and multiply its value to corresponding hourly values
  start = weekly['date'][0]

  for End in weekly['date']:
    if start != End:
      vweek = weekly.loc[weekly['date']==start].value_week.item()

      # multiply the week weight to the corresponding hourly values in the same week
      mask = (hourly['date'] >= start) & (hourly['date'] < End)
      hourly.loc[mask,'value_hour'] *= (vweek/100)


    start = End

  # Last week
  vweek = weekly.loc[weekly['date']==start].value_week.item()
  mask = hourly['date'] >= start
  hourly.loc[mask,'value_hour'] *= (vweek/100)


  #iterate for each month in monthly data and multiply its value to corresponding hourly values
  start = monthly['date'][0]

  for End in monthly['date']:
    if start != End:
      vmonth = monthly.loc[monthly['date']==start].value_month.item()

      # multiply the month weight to the corresponding hourly values after normalizing them for each month.
      mask = (hourly['date'] >= start) & (hourly['date'] < End)
      maximum_value = hourly.loc[mask,'value_hour'].max()
      hourly.loc[mask,'value_hour'] *= ((vmonth/100)*(100/maximum_value))

      # print(start)
      # print(vmonth)
    start = End

  # Last Month
  vmonth = monthly.loc[monthly['date']==start].value_month.item()
  mask = hourly['date'] >= start
  hourly.loc[mask,'value_hour'] *= ((vmonth/100)*(100/maximum_value))

  return hourly



if __name__ == "__main__":
  hourly_normalizd(HOURLY_PATH, WEEKLY_PATH, MONTHLY_PATH)
  
  
