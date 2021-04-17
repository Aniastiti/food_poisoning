import pandas as pd




#~~~~~~~~~~~~Acquire data frame from your local folder~~~~~~~~~~



def read_csv():
     
    '''This function returns a dataframe from a csv thats already in the directory'''
        
        
    df = pd.read_csv('food_data.csv', index_col=0)
        
    return df