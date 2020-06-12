# Import dependencies
import flask
from flask import Flask, render_template, url_for
from flask import request
from bikeshare_flask import load_data, filtered_choice, time_stats_day, time_stats_month, time_stats_hour, most_common, station_stats, trip_duration_stats, user_stats
import pandas as pd
import time
import pandas as pd
import numpy as np
import datetime
import json

app = Flask(__name__)

# Home route
@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return(flask.render_template('index.html'))
    # Get the user inputs and pass to functions in bikeshare_flask.py
    if request.method == 'POST':
        city = str(request.form['my_city']).lower()
        print(city)
        month_day = str((request.form['month_day'])).lower()
        print(month_day)
        # If the user wants to filter both month and day, get the month and day inputs from the form field
        if month_day =='both':
            month = str((request.form['month'])).lower()
            day = str((request.form['day'])).lower()
        # Else if the user wants to filter only by month, get the month input from the form field, set day to 'all' for no filter
        elif month_day =='month':
            month = str((request.form['month'])).lower()
            day = 'all'
        # Else if the user wants to filter only by day, get the dat input from the form field, set month to 'all' for no filter
        elif month_day == 'day':
            day = str((request.form['day'])).lower()
            month = 'all'
        # Else if the user wants no filter, set both month and day to 'all' for no filter
        elif month_day == 'none':
            month = 'all'
            day = 'all'
        # Print to console to ensure code works
        print(month)
        print(day)

        # Get the data for the user filters
        df = load_data(city, month, day)

        # Get the user filter choice
        filtered = filtered_choice(df)
        print(filtered)

        # Get the statistics on start, end, combination of stations
        common_start, freq_start, common_end, freq_end, combo_names, combo_count = station_stats(df)

        # Get statistics on trip duration (total trip duration and average trip duration)
        total_trip_duration, count_trip_duration, average_trip_duration = trip_duration_stats(df)

        # If city is washington, get only user type stats
        print(city not in ['new york city','chicago'])
        if city not in ['new york city','chicago']:
            if (filtered == 'Both'):
            # Display the most common start hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count)
            elif filtered == 'Month':
                # Display the most common day of week
                common_days, most_common_day, day_count = time_stats_day(df,filtered)
                # Display the most common start hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            most_common_day = most_common_day,
                            day_count = day_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count)
            # If the filter is 'Day', display the most common month and start hour
            elif filtered == 'Day':
                # Display the most common month
                common_months, most_common_month, month_count = time_stats_month(df,filtered)
                # Display the most common hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            most_common_month = most_common_month,
                            month_count = month_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count)
            # Else the filter is none, display the most common month, day, and start hour
            elif filtered == 'None':
                # Display the most common month
                common_months, most_common_month, month_count = time_stats_month(df,filtered)
                # Display the most common day of week
                common_days, most_common_day, day_count = time_stats_day(df,filtered)
                # Display the most common start hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            most_common_month = most_common_month,
                            month_count = month_count,
                            most_common_day = most_common_day,
                            day_count = day_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count)
        # Else if city is NYC or chicago, get stats for user type, gender, and birth year
        else:
            if (filtered == 'Both'):
                # Display the most common start hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count, m, m_count, f, f_count, earliest_birth, earliest_count, recent_birth, recent_count, common, freq = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count,
                            m=m, 
                            m_count=m_count, 
                            f=f, 
                            f_count=f_count,
                            earliest_birth=earliest_birth, 
                            earliest_count=earliest_count, 
                            recent_birth=recent_birth, 
                            recent_count=recent_count, 
                            common=common, 
                            freq=freq)
            elif filtered == 'Month':
                # Display the most common day of week
                common_days, most_common_day, day_count = time_stats_day(df,filtered)
                # Display the most common start hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count, m, m_count, f, f_count,earliest_birth, earliest_count, recent_birth, recent_count, common, freq = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            most_common_day = most_common_day,
                            day_count = day_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count,
                            m=m, 
                            m_count=m_count, 
                            f=f, 
                            f_count=f_count,
                            earliest_birth=earliest_birth, 
                            earliest_count=earliest_count, 
                            recent_birth=recent_birth, 
                            recent_count=recent_count, 
                            common=common, 
                            freq=freq)
            # If the filter is 'Day', display the most common month and start hour
            elif filtered == 'Day':
                # Display the most common month
                common_months, most_common_month, month_count = time_stats_month(df,filtered)
                # Display the most common hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count,  m, m_count, f, f_count,earliest_birth, earliest_count, recent_birth, recent_count, common, freq = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            most_common_month = most_common_month,
                            month_count = month_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count,
                            m=m, 
                            m_count=m_count, 
                            f=f, 
                            f_count=f_count,
                            earliest_birth=earliest_birth, 
                            earliest_count=earliest_count, 
                            recent_birth=recent_birth, 
                            recent_count=recent_count, 
                            common=common, 
                            freq=freq)
            # Else the filter is none, display the most common month, day, and start hour
            elif filtered == 'None':
                # Display the most common month
                common_months, most_common_month, month_count = time_stats_month(df,filtered)
                # Display the most common day of week
                common_days, most_common_day, day_count = time_stats_day(df,filtered)
                # Display the most common start hour
                common_hours, most_common_hour_str, hour_count = time_stats_hour(df,filtered)
                subs, sub_count, users, user_count,  m, m_count, f, f_count,earliest_birth, earliest_count, recent_birth, recent_count, common, freq = user_stats(df, city)
                return flask.render_template('index.html', 
                            myFilter = filtered,
                            myCity = city,
                            most_common_hour_str = most_common_hour_str,
                            hour_count = hour_count,
                            most_common_month = most_common_month,
                            month_count = month_count,
                            most_common_day = most_common_day,
                            day_count = day_count,
                            common_start=common_start, 
                            freq_start=freq_start, 
                            common_end=common_end, 
                            freq_end=freq_end, 
                            combo_names=combo_names, 
                            combo_count=combo_count,
                            total_trip_duration=total_trip_duration, 
                            count_trip_duration=count_trip_duration, 
                            average_trip_duration=average_trip_duration,
                            subs=subs, 
                            sub_count=sub_count, 
                            users=users, 
                            user_count=user_count,
                            m=m, 
                            m_count=m_count, 
                            f=f, 
                            f_count=f_count,
                            earliest_birth=earliest_birth, 
                            earliest_count=earliest_count, 
                            recent_birth=recent_birth, 
                            recent_count=recent_count, 
                            common=common, 
                            freq=freq)

if __name__ == "__main__":
    app.run(debug=True) 


