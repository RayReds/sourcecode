"""CSC108: Fall 2022 -- Assignment 3: Hypertension and Low Income

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Jacqueline Smith and David Liu
"""
from typing import TextIO
from statistics import correlation # Note that this requires Python 3.10

ID = "id"
HT_KEY = "hypertension"
TOTAL = "total"
LOW_INCOME = "low_income"

# Indexes in the inner lists of hypertension data in CityData
# HT is an abbreviation of hypertension, NBH is an abbreviation of neighbourhood
HT_20_44 = 0
NBH_20_44 = 1
HT_45_64 = 2
NBH_45_64 = 3
HT_65_UP = 4
NBH_65_UP = 5

# columns in input files
ID_COL = 0
NBH_NAME_COL = 1
POP_COL = 2
LI_POP_COL = 3

SAMPLE_DATA = {
    "West Humber-Clairville": {
        "id": 1,
        "hypertension": [703, 13291, 3741, 9663, 3959, 5176],
        "total": 33230,
        "low_income": 5950,
    },
    "Mount Olive-Silverstone-Jamestown": {
        "id": 2,
        "hypertension": [789, 12906, 3578, 8815, 2927, 3902],
        "total": 32940,
        "low_income": 9690,
    },
    "Thistletown-Beaumond Heights": {
        "id": 3,
        "hypertension": [220, 3631, 1047, 2829, 1349, 1767],
        "total": 10365,
        "low_income": 2005,
    },
    "Rexdale-Kipling": {
        "id": 4,
        "hypertension": [201, 3669, 1134, 3229, 1393, 1854],
        "total": 10540,
        "low_income": 2140,
    },
    "Elms-Old Rexdale": {
        "id": 5,
        "hypertension": [176, 3353, 1040, 2842, 948, 1322],
        "total": 9460,
        "low_income": 2315,
    },
}


# This function is provided for use in Tasks 3 and 4. You should not change it.
def get_age_standardized_ht_rate(ndata: 'CityData', name: str) -> float:
    """Return the age standardized hypertension rate from the neighbourhood in
    ndata matching the given name.

    Precondition: name is in ndata

    >>> get_age_standardized_ht_rate(SAMPLE_DATA, 'Elms-Old Rexdale')
    24.44627521389894
    >>> get_age_standardized_ht_rate(SAMPLE_DATA, 'Rexdale-Kipling')
    24.72562462246556
    """
    rates = calculate_ht_rates_by_age_group(ndata, name)

    # These rates are normalized for only 20+ ages, using the census data
    # that our datasets are based on.
    canada_20_44 = 11_199_830 / 19_735_665  # Number of 20-44 / Number of 20+
    canada_45_64 = 5_365_865 / 19_735_665  # Number of 45-64 / Number of 20+
    canada_65_plus = 3_169_970 / 19_735_665  # Number of 65+ / Number of 20+

    return (rates[0] * canada_20_44
            + rates[1] * canada_45_64
            + rates[2] * canada_65_plus)


#TASK 1
def get_hypertension_data(small_data:dict, citydata:TextIO) -> None:
    """
    >>> 
    """
    
    check = True
    for i in citydata:
        if check:
            check= False
            continue
        x = i.split(',')
        name = x[1]
        cityid = int(x[0])
        content = []
        for i in range(2, len(x)):
            content.append(int(x[i]))        
        if name in small_data.keys():
            small_data[name][HT_KEY] = content
            break
        small_data[name] = {}
                
        
def get_low_income_data(small_data:dict, citydata:TextIO) -> None:
    check = True
    for i in citydata:
        if check:
            check= False
            continue
        x = i.split(',')
        name = x[1]
        total = x[2]
        low_income = x[3]
        small_data[name][TOTAL] = int(total)
        small_data[name][LOW_INCOME] = int(low_income)
#TASK 2       
#def get_bigger_neighbourhood(CityData, str, str) -> str:
 #   pass
        
#TASK 3

        
#TASK 4

    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Using the small data files
    small_data = {}

    # Add hypertension data
    ht_file = open("hypertension_data_small.csv")
    get_hypertension_data(small_data, ht_file)
    print(small_data)
    ht_file.close()
    
    # Add low income data
    li_file = open("low_income_small.csv")
    get_low_income_data(small_data, li_file)
    li_file.close()
    
    # Created dictionary should be the same as SAMPLE_DATA
    print(small_data == SAMPLE_DATA)
