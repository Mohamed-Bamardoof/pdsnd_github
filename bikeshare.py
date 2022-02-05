import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# The variables Months and Days will be used in get_filters function to check the correctness of user input
Months = ['january', 'february', 'march', 'april', 'may', 'june']
Days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters ():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Which city do you want to see its data? Chicago, New York City or Washington?\n")
            print("You Entered: {}".format(city))

            if (city.lower() in CITY_DATA) != True:
                print('There is a mistake in the name of the city\n')
            else:
                break

        except NameError:
            print("The input is invalid")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nWhich month would you like to filter by? January, February, March, April, May or June?\n")
            print("You Entered: {}".format(month))

            if (month.lower() in Months) != True:
                print('There is a mistake in the name of the month\n')
            else:
                break

        except NameError:
            print("The input is invalid")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nWhich day would you like to filter by? Sunday, Monday, Tuesday...etc\n")
            print("You Entered: {}".format(day))

            if (day.lower() in Days) != True:
                print('There is a mistake in the name of the day\n')
            else:
                break

        except NameError:
            print("The input is invalid")


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # use the index of the months list to get the corresponding int
    month = Months.index(month.lower()) + 1

    # filter by month to create the new dataframe
    df = df[df['month'] == month]

    # filter by day of week to create the new dataframe
    df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month =", most_common_month)

    # TO DO: display the most common day of week
    most_common_day =  df['day_of_week'].mode()[0]
    print("The most common day of week is", most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour =", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_count = df['Start Station'].value_counts()
    print("The most commonly used start station:")
    print(start_station_count.head(1))


    # TO DO: display most commonly used end station
    end_station_count = df['End Station'].value_counts()
    print("\nThe most commonly used end station:")
    print(end_station_count.head(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time =", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time =", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    # Make a conditional statement since there are no data for Washington
    if city.lower() == 'washington':
        print("No available data ragarding the users' gender and date of birth in Wanshington")
    else:
        gender = df['Gender'].value_counts()
        print(gender)


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        print('The earliest year of birth is:',earliest_year_of_birth)

        recent_year_of_birth = df['Birth Year'].max()
        print('The most recent year of birth is:',recent_year_of_birth)

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('The most common year of birth is:',most_common_year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_row_data(df):
    """Displays raw data based on user request."""

    # defining the variable used for tracking
    row_index = 0

    # The loop is written to make sure if the user wants to see more data
    while row_index < 300000:
        display = input("Would you like to see 5 rows of data? Type 'yes' or 'no'\n")

        if display.lower() == 'yes':
            print(df.iloc[row_index:row_index+5])
            row_index += 5

        elif display.lower() == 'no':
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
