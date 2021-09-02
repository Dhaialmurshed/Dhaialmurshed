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
         # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities= ['chicago','new york city','washington']

    while True:
        city=input("please enter city : chicago, new york city or washington ").lower()
        if city in cities:
            break
        else:
            print("reenter a valid input")
        # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','all']
    month=input("please enter a month {}".format(months)).lower()
    while True:
       
            if month in months:
                break
            else:
                month=input("wrong input so please enter only one of those mopnths {}".format(months))
       
   
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wedensday','thursday','friday','saturday','sunday']
    day=input("may you enter a day {} ".format(days)).lower()

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
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
    
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        

    if day != 'all':
        df = df[df['day'] == day.title()]

      

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mostCommonMonth=df['month'].mode()[0]
    print("most common month is",mostCommonMonth)
    # TO DO: display the most common day of week
    mostCommonDay=df['day'].mode()[0]
    print("most common day of week is",mostCommonDay)
    # TO DO: display the most common start hour
    mostCommonStartHour=df['hour'].mode()[0]
    print("most common start hour is",mostCommonStartHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        mostCommonStartStation=df['Start Station'].mode()[0]
        print("most commonly used start station is ",mostCommonStartStation)

        # TO DO: display most commonly used end station
        mostCommonEndStation=df['End Station'].mode()[0]
        print("most commonly used end station is ",mostCommonEndStation)
        # TO DO: display most frequent combination of start station and end station trip
        group=df.groupby(['Start Station','End Station'])
        mostFrequentCombination=group.size().sort_values(ascending=False).head(1)
        print("most frequent combination of start station and end station trip : ",mostFrequentCombination)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        #https://stackoverflow.com/questions/63229237/finding-the-most-frequent-combination-in-dataframe
        


def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        totalTravel=df['Trip Duration'].sum()
        print("total travel time",totalTravel)
        # TO DO: display mean travel time
        meanTravelTime=df['Trip Duration'].mean()
        print("mean travel time is ", meanTravelTime)



        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df,city):
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        countsOfUserTypes=df['User Type'].value_counts()
        print("counts of user types: ",countsOfUserTypes)

        # TO DO: Display counts of gender
        if city != 'washington':
            countOfGender=df['Gender'].value_counts()
            print("counts of gender: ",countOfGender)

        # TO DO: Display earliest, most recent, and most common year of birth
            earlist=df['Birth Year'].min()
            mostRecent=df['Birth Year'].max()
            mostCommonYear=df['Birth Year'].mode()[0]
            print("earliest year of birth: ",earlist)
            print("most recent year of birth: ", mostRecent)
            print("most common year of birth: ",mostCommonYear)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def show_data(df):
    """ this function shows the first 5 rows of the data if the user want to"""
    answer=['yes','no']
    request= input("want to see 5 lines of raw data? (yes,no)").lower()
    
    if request=='yes':
        first=0
        last=5
        data = df.iloc[first:last,:9]
        print(data)
    while request=='yes':
        
        ask=input(" do you want to see more data? ").lower()
        if ask=='yes':
            first+=5
            last+=5
            data=df.iloc[first:last,:9]
            print(data)
        else:
            
            break
        
    
       
    
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    	main()
