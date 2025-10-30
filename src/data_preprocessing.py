import pandas as pd
def load_data(path):
   '''Load the dataset from CSV file'''
   df = pd.read_csv(path)
   return df

def clean_data(df):
   '''Clean the datset (remove unnecessary columns, handle missing values)'''
   #drop index column if it exists
   if 'index' in df.columns:
       df = df.drop(columns=['index'])

    # drop rows with missing values (if any)
   df = df.dropna()

   return df

def get_features_and_target(df):
    '''Separate independent and dependent variables'''
    X = df[['duration', 'days_left']]
    y = df['price']
    return X, y