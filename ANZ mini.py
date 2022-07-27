### Replace csv package with Pandas
from ast import Index
from cgi import test
import csv

from numpy import number
import random_profile_generator as rpg
import time
import pandas as pd

# Create variable to give how long the script took to execute
start_time = time.time()

### Create the df with Panda
# Dataframe creator
def candidate_list_generator(number_of_candidates, file_name):

    df = pd.DataFrame()

    for i in range(number_of_candidates):
        df2 = rpg.random_candidate()
        df = df.append(df2, ignore_index=True)
    
    df.to_csv(file_name)
    

candidate_list_generator(100, 'test.csv')    
# print(candidate_list_generator(100)  )

# for i in range(1000):
#     df1 = pd.DataFrame(rpg.random_candidate())
#     df = df.append(df1)


# ### Create file using csv
# with open('survey_result_2020.csv', 'w') as survey_result:   
#     csv_writer = csv.DictWriter(survey_result, fieldnames = rpg.headers)

#     csv_writer.writeheader()

#     for i in range(1000):
#         csv_writer.writerow(rpg.random_candidate())


# Give how long the script took to execute
print("Process finished in " + str(time.time() - start_time) + "s")









