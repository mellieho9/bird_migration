import pandas as pd 

birddata = pd.read_csv('/Users/Admin/Desktop/bird_tracking.csv')
grouped_birds = birddata.groupby("bird_name")

mean_speeds = grouped_birds.speed_2d.mean()

mean_altitudes = grouped_birds.altitude.mean()

birddata.date_time = pd.to_datetime(birddata.date_time)

birddata["date"] = birddata.date_time.dt.date

grouped_bydates = birddata.groupby("date")

mean_altitudes_perday = grouped_bydates.altitude.mean()

grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()

import matplotlib.pyplot as plt

eric_daily_speed  = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
nico_daily_speed  = grouped_birdday.speed_2d.mean()["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
