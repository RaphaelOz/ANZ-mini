from ast import Index
from cgi import test
from numpy import number
import pandas as pd
import time
import random_profile_generator as rpg

# Create variable to give how long the script took to execute
start_time = time.time()

# Dataframe creator
def candidate_list_generator(number_of_candidates, file_name):

    df = pd.DataFrame()

    for i in range(number_of_candidates):
        df2 = rpg.random_candidate()
        df = df.append(df2, ignore_index=True)
    
    df.to_csv(file_name)
    

candidate_list_generator(1000, 'survey_data_2020.csv')    

# Give how long the script took to execute
print("Process finished in " + str(time.time() - start_time) + "s")









