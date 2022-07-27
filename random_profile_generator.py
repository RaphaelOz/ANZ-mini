import numpy as np

# Keys for the dictionary
headers = ['Candidate ID', 'Gender', 'Age group', 'Cultural background', 'Number of children', 'Most important benefit 1', 'Most important benefit 2']

### Building note: Is there already an existing function for this?
### Read NumPy.random_integer
def int_range(a, b):
    return list(range(a, b+1))

# Create a randomly generated candidate
def random_candidate():

    # Values for the dictionary and their probabilities
    candidate_ID = int_range(1, 1000000)

    gender = ['Male', 'Female', 'Other']
    gender_prob = [0.6, 0.35, 0.05]

    age = ['18-23', '24-39', '40-64', '65+']
    age_prob = [0.3, 0.2, 0.1, 0.4]

    cultural_background = ['African', 'Australian', 'Asian', 'European', 'North American', 'South American']
    cultural_background_prob = [0.02, 0.5, 0.3, 0.1, 0.06, 0.02]

    nbr_children = [0, 1, 2, 3, 4]
    nbr_children_prob = [0.3, 0.4, 0.2, 0.09, 0.01]

    benefits = ['Higher wages', 'Remote work flexibility', 'Higher annual leave benefits', 'Investment opportunites', 'Paid training and development', 'Other']
    benefits_prob_for_m = [0.4, 0.09, 0.05, 0.3, 0.06, 0.1]
    benefits_prob_for_f = [0.09, 0.3, 0.4, 0.05, 0.06, 0.1]
    benefits_prob_for_o = [0.27, 0.22, 0.2, 0.15, 0.06, 0.1]


    # Keys creation
    gender_choice = np.random.choice(gender, p=gender_prob)

    # benefits_choice based on gender
    # Create exclusive benefits_choice2 based on benefits_choice1
    if gender_choice == 'Male':
        benefits_choice1 = np.random.choice(benefits, p=benefits_prob_for_m)

        benefits.remove(benefits_choice1)
        benefits_choice2 = np.random.choice(benefits)

    elif gender_choice == 'Female':
        benefits_choice1 = np.random.choice(benefits, p=benefits_prob_for_f)

        benefits.remove(benefits_choice1)
        benefits_choice2 = np.random.choice(benefits)

    else:
        benefits_choice1 = np.random.choice(benefits, p=benefits_prob_for_o)
        
        benefits.remove(benefits_choice1)
        benefits_choice2 = np.random.choice(benefits)

    # Candidate creation as a dictionary of lists (for pandas)
    candidate = {headers[0]:[np.random.choice(candidate_ID)], 
                headers[1]:[gender_choice], 
                headers[2]:[np.random.choice(age, p=age_prob)], 
                headers[3]:[np.random.choice(cultural_background, p=cultural_background_prob)], 
                headers[4]:[np.random.choice(nbr_children, p=nbr_children_prob)],
                headers[5]:[benefits_choice1],
                headers[6]:[benefits_choice2]}

    return(candidate)


