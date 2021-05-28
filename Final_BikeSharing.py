import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

""" created a list for each selection"""


months= ('january', 'february', 'march', 'april', 'may', 'june', 'all')
days= ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all')

#block 1

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nPlease enter the city you would like to analyse on the list below:\n-Chicago\n-New York city\n-Washington\n--->').lower()

    while city not in CITY_DATA:
        print('\nPlease check if the city is on the list')
        city = input('\nPlease enter the city you would like to analyse on the list below:\n-Chicago\n-New York city\n-Washington\n--->').lower()
    
    else:
        print(city.title(),'selected')
   

    # get user input for month (all, january, february, ... , june)
    month = input('\nPlease enter the month you would like to check in the list below:\n-All\n-January\n-February\n-March\n-April\n-May\n-June\n--->').lower()

    while month not in months:
        print('\nPlease check if the entry is spelled correctly')
        month = input('\nPlease enter the month you would like to check in the list below:\n-All\n-January\n-February\n-March\n-April\n-May\n-June\n--->').lower()
    
    else:
        print(month.title(),'selected')

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('\nPlease enter the day you would like to check in the list below:\nAll\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n--->').lower()

    while day not in days:
        print('Please check if the entry is spelled correctly')
        day = input('\nPlease enter the day you would like to check in the list below:\nAll\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n--->').lower()
    
    else:
        print(day.title(),'selected')
    print('\nCity selected:',city.title())
    print('Month selected:',month.title())
    print('Day selected:',day.title())
    print('-'*40)
    return city, month, day
    
#block 2
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = pd.DatetimeIndex(df['Start Time']).month_name()
    df['month'] = df['month'].str.lower()
    df['week_day'] = df['Start Time'].dt.day_name()
    df['week_day'] = df['week_day'].str.lower()
    df['hour'] =df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['month']==month]
    else:
        df = df[df['month'].isin(['january', 'february', 'march', 'april','may','june'])]

    if day != 'all':
        df = df[df['week_day']==day]
    else:
        df = df[df['week_day'].isin(['monday', 'tuesday', 'wednesday', 'thursday','friday','saturday','sunday'])]
    
 
    return df
    
#block 3

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month

    freq_month = df['month'].mode()[0]
    print('\nMost frequent month==>',freq_month.title())

    # display the most common day of week

    freq_weekday = df['week_day'].mode()[0]
    print('\nMost frequent day in the week==>', freq_weekday.title())


    # display the most common start hour
    freq_hour_day = df['hour'].mode()[0]
    print('\nMost frequent hour in a day==>',freq_hour_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#block 4

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common start station is:',common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station is:',common_end_station)

    
    # display most frequent combination of start station and end station trip
    df['combined_station'] = 'Start Station: ' + df['Start Station'] + '\nEnd Station: ' +df['End Station']
    start_end_station = df['combined_station'].mode()[0]
    print('\nThe most common start & end stations are:',start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#block5

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_trip_duration = df['Trip Duration'].sum()
    print('\nTotal Duration in seconds: ',total_trip_duration)
    

    # display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print('\nAverage Duration in seconds: ',avg_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#block 6

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    freq_user_type = df.groupby(['User Type']).size()
    print('\nHere below is the user type count:\n', freq_user_type)

    # Display counts of gender

    if city == 'washington':
        print('\nGender and birth year info are not available in the city selected')
    else:
        gender_count = df.groupby(['Gender']).size()
        print('\nHere below is the gender count:\n', gender_count)

    # Display earliest, most recent, and most common year of birth

        earliest_BDY = df['Birth Year'].min()
        print('\nThe earliest birth year is: ',earliest_BDY)

        recent_BDY = df['Birth Year'].max()
        print('\nThe most recent birth year is: ', recent_BDY)   

        freq_BDY = df['Birth Year'].mode()[0]
        print('\nthe most frequent birth year is: ',freq_BDY)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#block7

def main():
    city=()
    month=()
    day=()
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
