"""The project is about US bike-share data"""
import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
# get user input for city (chicago, new york city, washington). HINT: Uses a while loop to handle invalid inputs

    cities = {'1': 'chicago', '2': 'new york city', '3': 'washington'}
    city = input(
        "\nWould you like to see data for ?\n 1-Chicago \n 2-New york city \n 3-Washington \n>>>  ").strip().lower()
    while city not in list(cities.keys())+list(cities.values()):
        print(f"\t ({city}) isn't a valid city ,Please enter a valid city. ")
        city = input(
            "\nWould you like to see data for ?\n 1-Chicago \n 2-New york city \n 3-Washington \n>>>  ").strip().lower()
        continue
    if city in list(cities.keys()):
        city = cities[city]

# get user input for month (january, february, ... , june)
    def month_filter():
        """
        get user input for month (january, february, ... , june)

        Returns:
            (str) month - name of the month to filter by
        """

        months = {"1": "january", "2": 'february', '3': 'march',
                  '4': 'april', '5': 'may', '6': 'june'}
        month = input(
            "\nWhich month ? \n 1-January \n 2-February\n 3- March \n 4-April \n 5-May \n 6-June  \n>>>  ").strip().lower()
        while month not in (list(months.keys())+list(months.values())):
            print(f"\t ({month}) isn't a valid date , Please enter a valid date")
            month = input(
                "\nWhich month ? \n 1-January \n 2-February\n 3- March \n 4-April \n 5-May \n 6-June  \n>>>  ").strip().lower()
            continue
        if month in list(months.keys()):
            month = months[month]
        return month
# get user input for day of week (monday, tuesday, ... sunday)

    def day_filter():
        """
        get user input for day of week (monday, tuesday, ... sunday)

        Returns:
            (str) day - name of the day to filter by
        """
        days = {'1': 'sunday', '2': 'monday', '3': 'tuesday', '4': 'wednesday',
                     "5": 'thursday', '6': 'friday', '7': 'saturday'}
        day = input(
            "\nWhich day ? \n 1-Sunday \n 2-Monday \n 3-Tuesday \n 4-Wednesday \n 5-Thursday \n 6-Friday \n 7-Saturday   \n>>>  ").strip().lower()
        while day not in (list(days.keys())+list(days.values())):
            print(f"\t ({day}) isn't a valid date ,Please enter a valid date")
            day = input(
                "\nWhich day ? \n 1-Sunday \n 2-Monday \n 3-Tuesday \n 4-Wednesday \n 5-Thursday \n 6-Friday \n 7-Saturday   \n>>>  ").strip().lower()
            continue
        if day in list(days.keys()):
            day = days[day]
        return day

    # Asks user to specify time filter to analyze.
    time_filter_options = {'1': 'day', '2': 'month', '3': 'both', '4': 'none'}
    time_filter = input(
        "\nWould you like to filter your data with 'day' ,'month' , 'both' or not at all ? Type 'none' for no time filter \n 1-day \n 2-month \n 3-both \n 4-none \n>>>  ").strip().lower()
    while time_filter not in (list(time_filter_options.keys())+list(time_filter_options.values())):
        print(f"\t ({time_filter}) isn't a valid data ,Please enter valid data")
        time_filter = input(
            "\nWould you like to filter your data with 'day' ,'month' , 'both' or not at all ? Type 'none' for no time filter \n 1-day \n 2-month \n 3-both \n 4-none \n>>>  ").strip().lower()

    if time_filter in ('day', '1'):
        day = day_filter()
        month = "all"
    elif time_filter in ('month', '2'):
        month = month_filter()
        day = "all"
    elif time_filter in ('both', '3'):
        month = month_filter()
        day = day_filter()
    elif time_filter in ('none', '4'):
        day = "all"
        month = "all"
    print('Hello! Let\'s explore some US bikeshare data!')

    print('-'*40)
    print(
        f'\t  Chosen Filter \n\t --------------\n City: {city} \n Month: {month} \n Day: {day}')
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour
    df["day_of_week"] = df['Start Time'].dt.day_name()
    df["month"] = df['Start Time'].dt.month
    # filter by day of week if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        month_list = ["january", 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month)+1
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_list = ["January", 'February', 'March', 'April', 'May', 'June']
    month = month_list[(df['month'].mode()[0])-1]
    print(f"Most Common Start Month: {month}")

    # display the most common day of week
    print(f"Most Common Start Day Of Week: {df['day_of_week'].mode()[0]}")

    # display the most common start hour
    print(f"Most Common Start Hour: {(df['hour'].mode()[0])}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f"Most Common Start Station: {df['Start Station'].mode()[0]}")

    # display most commonly used end station
    print(f"Most Common End Station: {df['End Station'].mode()[0]}")

    # display most frequent combination of start station and end station trip
    common_trip = df['Start Station'] + \
        '\n To The End Station: '+df['End Station']
    print(
        f"Most frequent trip: \n From The Start Station: {common_trip.mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"The Total Travel Time: {df['Trip Duration'].sum()}")

    # display mean travel time
    print(f"The Mean Travel Time: {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of user types")
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print('-'*30)
        print("counts of gender")
        print(df['Gender'].value_counts())
    print('-'*30)

    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        print('\nCalculating The Earliest, Most Recent, and Most Common Year of Birth...\n')
        print(f"The earliest year of birth: {df['Birth Year'].min()}")
        print(f"The most recent year of birth: {df['Birth Year'].max()}")
        print(f"The most common year of birth: {df['Birth Year'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
    """
    Asks user to specify if wants to see the first 5 rows and if wants the next 5 rows
    """
    row_count = 0
    answer = input(
        'Do you want to see the first 5 rows \n1-Yes\n2-No \n>>>  ').strip().lower()
    while True:
        if answer in ('yes', '1'):
            row_count += 5
            print(df.head(row_count))
            print('-'*40)
            answer = input(
                'Do you want to see the next 5 rows \n1-Yes\n2-No \n>>>  ').strip().lower()
            continue
        elif answer in ('no', '2'):
            break
        else:
            print('-'*40)
            print(
                f"\t({answer}) isn't a valid answer,Please enter a valid answer.")
            answer = input(
                'Do you want to see the next 5 rows \n1-Yes\n2-No \n>>>  ').strip().lower()
            continue

    print('-'*40)


def main():
    """
    The main function which executes the program
    and Asks user to specify if wants to restart or no
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        restart = input(
            '\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart.strip().lower() != 'yes':
            break


if __name__ == "__main__":
    main()
