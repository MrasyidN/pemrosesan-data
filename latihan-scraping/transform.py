# latihan tranfform 

import pandas as pd

def transform_to_DataFrame(data):
    """mengubah menajdi dataframe"""
    df = pd.DataFrame(data)
    return df

def transform_data(data, exchange_rate):
    """menggabungkan semua transformasi data menjadi satu fungsi"""

    # transformasi price
    data['Price_in_pounds'] = data['Price'].replace('£', '', regex=True).astype(float)


    # transformasi rating 
    rating_mapping = {
        'One' : 1,
        'Two' : 2,
        'Three' : 3,
        'four' : 4,
        'Five' : 5
    }

    data['Rating'] = data['Rating'].replace(rating_mapping)

    # Transformasi Exchange Rate
    data['Price_in_rupiah'] = (data['Price_in_pounds'] * exchange_rate).astype(int)
    
    # Menghapus kolom redundan
    data = data.drop(columns=['Price'])
    
    # Transformasi Tipe Data
    data['Title'] = data['Title'].astype('string')
    data['Availability'] = data['Availability'].astype('string')
    
    return data
    