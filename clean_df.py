from datetime import datetime

def convert_datetime(string):
    string = string.split('T')
    new_string = datetime.strptime(string[0], '%Y-%m-%d').date()


    return new_string

def clean_df(df):
    df['time'] = df['time'].apply(convert_datetime)
    return df