import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Insert the city name from chicago, washington, new york city: ').lower()

        if city not in CITY_DATA:
            print('You have to choose the city name')  
            
        else :
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Insert a month or type "all": ').lower()
        months = ['january', 'february', 'march' , 'april', 'may' , 'june']
        
        if month not in months and month != 'all':
            print('Please enter valid month or type "all": ')
        else:
             break


    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day= input('Insert one day from monday, tuesday, wednsday, friday, saturday, sunday, or type "all": ').lower()
        days = [ 'monday', 'tuesday', 'wednsday', 'friday', 'saturday', 'sunday']
        if day not in days and day != 'all':
            print('Please enter valid day or type "all": ')
        else:
            break



    print('-'*40)
    return city, month, day


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

# we have to convert "start time" 

    df['Start Time']  = pd.to_datetime(df['Start Time'])

#creating new columns (month,day of week, hour)as following"
    df['month']       = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour']        = df['Start Time'].dt.hour

# filtering by month""
    if month != 'all':
        months = ['january', 'february', 'march' , 'april', 'may' , 'june']
        month = month.index(months) +1
        df= df[df['month'] == month]
# filtering by day""
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
    
def raw_data(df):
    """ diplayed raw data upon request."""

    answered_question = input('Do you like to see the first 5 lines pls choose yes or no:  ').lower()
    pd.set_option('display.max_columns', None)

    x = 0

    while True:
        if answered_question == 'no':
            break
        print(df[x: x+5])
        answered_question = input('Do you like to display the next 5 lines pls choose yes or no:  ').lower()
        x +=5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print(df['month'].mode()[0])


    # display the most common day of week

    print(df['day_of_week'].mode()[0])

    # display the most common start hour

    print(df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    print(df['Start Station'].mode()[0])

    # display most commonly used end station

    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip

    frequent_combination = df.group_by(['Start Station','End Station'])
    print(frequent_combination.size().sort_value('Decending').head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print(df['Trip Duration'].sum())

    # display mean travel time

    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender

    if CITY_DATA['city'] != 'washington':

        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].min())
    
    print(df['Birth Year'].max())

    print(df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

        