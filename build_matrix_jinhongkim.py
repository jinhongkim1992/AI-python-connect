import numpy as np
import pandas as pd

#data read
movie_rate = pd.read_csv("C:/Users/USER/Desktop/파이썬/부스트캠프_머신러닝/pandas,numby/3_lab_bulid_matrix/movie_rating.csv")

print(movie_rate.columns)

#강의 정답
def get_rating_matrix(filename, dtype=np.float32):
    df = filename
    return df.groupby(['source', 'target'])['rating'].sum().unstack().fillna(0)


#내가 작성한 답안
def get_rating_matrix(filename, dtype=np.float32):

    pivot = filename.pivot_table(values = 'rating',
                                 index = 'source',
                                 columns = 'target',
                                 aggfunc = np.mean, fill_value = 0)
    return pivot



#data read
product_transaction = pd.read_csv("C:/Users/USER/Desktop/파이썬/부스트캠프_머신러닝/pandas,numby/3_lab_bulid_matrix/1000i.csv")

print(product_transaction)

def get_frequent_matrix(filename, dtype=np.float32):
    filename['rating'] = 1
    return filename.groupby(['source','target'])['rating'].sum().unstack().fillna(0)

print(get_frequent_matrix(product_transaction))
