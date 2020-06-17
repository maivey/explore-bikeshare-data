# Explore Bikeshare Data

# Background

This project makes use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and WashingtonThis script imports US bike share data to answer interesting questions about it by computing descriptive statistics. The script takes in raw input to create an interactive experience in the terminal to present these statistics.

### Bike Share Data

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

### The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core **six (6)** columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

# Prerequisites

#### Bikeshare Python Script](bikeshare.py) Dependencies

```python
import time
import pandas as pd
import numpy as np
import datetime
import json
```

#### Flask Deployment

Import the following dependencies for [app.py](app.py):

```python
import flask
from flask import Flask, render_template, url_for
from flask import request
from flask import jsonify
from flask import send_from_directory
import os.path
from bikeshare_flask import load_data, filtered_choice, time_stats_day, time_stats_month, time_stats_hour, most_common, station_stats, trip_duration_stats, user_stats
import pandas as pd
import time
import pandas as pd
import numpy as np
import datetime
import json
```

Include the following tags in the [index.html](index.html) and [graphs.html](graphs.html) pages:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/superhero/bootstrap.min.css">
<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
<link rel="stylesheet" href="static/css/style.css">

<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/5.5.0/d3.js"></script>
```



# Steps

## 1. [Bikeshare Python Script](bikeshare.py)

### An Interactive Experience

The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe to do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit. The script also prompts the user whether they would like want to see the raw data. If the user answers 'yes,' then the script prints 5 rows of the data at a time, then asks the user if they would like to see 5 more rows of the data. The script continues prompting and printing the next 5 rows at a time until the user chooses 'no,' they do not want any more raw data to be displayed.

### Statistics Computed

To learn about bike share use in Chicago, New York City, and Washington, this script computes a variety of descriptive statistics. It provide the following information:

**#1 Popular times of travel** (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

**#2 Popular stations and trip**

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**

- total travel time
- average travel time

**#4 User info**

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## 2. Flask Deployment

This repository also contains a Flask deployment of [bikeshare.py](bikeshare.py). After a user choses the city, the filter, month (if applicable), and day (if applicable), the user can choose to click "Get Statistics" or "Show Graphs"

#### Get Statistics

![Screen Shot 2020-06-17 at 1.14.53 PM](/Users/morganivey/Desktop/Screen Shot 2020-06-17 at 1.14.53 PM.png)

When the user provides input, the `Get Statistics` button displays the statistics described in *Step 1*. 



![Screen Shot 2020-06-17 at 1.14.53 PM](/Users/morganivey/Desktop/Screen Shot 2020-06-17 at 1.15.05 PM.png)

When the user clicks the `Show Graphs` button, the webpage displays the statistics described in *Step 1*, and also displays `plotly.js` graphs of the following for the user's filter choice:

1. [For `day` or `none` filter only] The trip count per month in descending order
2. [For `month` or `none` filter only] The trip count per day of the week in descending order
3. The trip count per hour of the day
4. The top 10 most common start stations
5. The top 10 most common end stations
6. The top 10 most common trips from start to end (i.e., most frequent combinations of start station and end station)
7. [For Chicago and New York City only] The user count for subscriber and customer
8. [For Chicago and New York City only] The user count for male and female
9. [For Chicago and New York City only] The top 10 most common birth years