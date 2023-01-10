"""CSC108: Fall 2022 -- Assignment 2: Carbon Emissions

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Sadia Sharmin and Michelle Craig
"""
# The following lines define the type number so we can use it in type contracts
# for functions which normally return float but for error situations return
# integer constants
from typing import Union
number = Union[float, int]

START_YEAR = 1799
END_YEAR = 2017
EMISSION_FILENAME = 'co2_emissions_per_person.csv'
POP_FILENAME = 'populations.csv'
G7_COUNTRIES = ['Canada', 'France', 'Germany', 'Italy', 'Japan',
                'United Kingdom', 'United States']

# Missing data entry in table
MISSING_DATA = -1.0

# Constant return values to be used in error situations
DATA_NOT_FOUND = -1
COUNTRY_NOT_FOUND = -2
INVALID_FORMAT = -3

SAMPLE_POPULATION_DATA = [
    ['Canada', 500000.0, 512000.0, 525000.0, 538000.0] + [-1.0] * 215,
    ['Finland', 800000.0, 815000.0, 831000.0, 847000.0] + [-1.0] * 215,
    ['Poland', 9000000.0, 9070000.0, 9130000.0, 9200000.0] + [-1.0] * 215,
]

SAMPLE_EMISSIONS_DATA = [
    ['Canada', 0.00733, 0.00716, 0.00698, 0.00681] + [-1.0] * 215,
    ['Finland', -1.0, -1.0, -1.0, 0.00341] + [-1.0] * 215,
    ['Poland', 0.0452, 0.0489, 0.0494, 0.0502] + [-1.0] * 215,
]


################################################################################
# Simple functions
################################################################################

def convert_population(population_string: str) -> number:
    """Convert population_string to its corresponding numeric value.
    When the population string is invalid return INVALID_FORMAT.
    >>> convert_population('76.6M')
    76600000.0
    >>> convert_population('76.6m')
    -3
    """
    pop = population_string
    format = {
        "M" : 1000000,
        "k" : 1000,
        "B" : 1000000000
    }
    for i in range(len(pop)):
        if pop[i].isalpha():
            if pop[i] in "MkB" and i == len(pop)-1:
                continue
            else:
                return INVALID_FORMAT
    if "." in pop:
        arr = pop.split(".")
        if arr[0].isdigit() and len(arr) < 3 and len(arr[1]) > 1:
            pass
        else:
            return INVALID_FORMAT
        comma = pop.rstrip('MkB')
        return float(comma)*format[arr[1][-1]]
    if pop[-1] in "MkB":
        temp = format[pop[-1]]
        return float(pop.rstrip("MkB"))*temp
    return float(pop)
def get_year_index(year: int) -> int:
    """Return the index that <year> would map to.

    Precondition: START_YEAR <= year <= END_YEAR

    >>> get_year_index(1801)
    3
    """
    year = (year - START_YEAR) + 1
    return year

################################################################################
# Data cleaning and reading
################################################################################

def read_data(filename: str) -> list[list[str]]:
    """Return the data found in the file filename as a list of lists of strings.
    Each inner list corresponds to a row in the file.

    Docstring examples not given since the results depend on filename.

    Precondition: The data in filename is in a valid format.
    """
    country = []
    file = open(filename, "r")
    x = file.readlines()
    for i in x:
        i = i.strip("\n")
        temp = i.split(",")

        country.append(temp)
    return country
def prepare_data(filename: str, is_emission_data: bool = False) -> list[list]:
    """Return the data found in file filename, cleaning the data accordingly.

    If is_emission_data is True, then the data in filename is emission data and
    should be cleaned as such. Otherwise, it is population data and should be
    cleaned accordingly.

    Docstring examples not given since the results depend on filename.

    Precondition: The data in filename is in a valid format.
    """
    pass

def clean_population_data(data: list[list]) -> None:
    """Clean the population data in data, replacing the strings representing
    the population with a floating point value.

    Use the constant MISSING_DATA to represent any entries where the
    format of the population string was invalid.

    >>> small_sample_data = [['France', '29M', '29.1M', '29.2M', '29.3m'],
    ...                      ['Mauritius', '59k', '60.7k', '62.4k', '64.2k']]
    >>> clean_population_data(small_sample_data)
    >>> small_sample_data[0]
    ['France', 29000000.0, 29100000.0, 29200000.0, -1.0]
    >>> small_sample_data[1]
    ['Mauritius', 59000.0, 60700.0, 62400.0, 64200.0]
    """
    for rows in data:
        for i in range(1, len(rows)):
            if convert_population(rows[i]) == -3:
                rows[i] = -1.0
            else:
                rows[i] = convert_population(rows[i])
    pass

def clean_emission_data(data: list[list]) -> None:
    """Clean the emission data in data, replacing the strings representing
    the emissions with a floating point value.

    >>> small_sample_data = [
    ...     ['Canada', '0.00733', '0.00716', '0.00698', '0.00681'] + [''] * 215,
    ...     ['Finland'] + ['']*3 + ['0.00341'] + [''] * 215,
    ...     ['Poland', '0.0452',' 0.0489', '0.0494', '0.0502'] + [''] * 215]

    >>> clean_emission_data(small_sample_data)
    >>> small_sample_data == SAMPLE_EMISSIONS_DATA
    True
    """
    for i in data:
        for x in range(1, len(i)):
            if i[x] != '':
                i[x] = float(i[x])
            else:
                i[x] = -1.0

################################################################################
# Data querying
################################################################################

def get_country_row(data: list[list], country: str) -> list:
    """Return the row in data that belongs to country, including country's name.

    If country is not in data, return an empty list.

    >>> get_country_row(SAMPLE_POPULATION_DATA, 'Canada')[:5]
    ['Canada', 500000.0, 512000.0, 525000.0, 538000.0]

    """
    for i in data:
        if i[0] == country:
            return i
    return []
def country_with_largest_emissions_by_year(emissions_data: list[list],
                                           year: int) -> str:
    """Return the name of the country that has the largest per-person
    emissions in the given year of data. In the case of a tie, return the one
    that comes first in the data file.


    Precondition:  START_YEAR <= year <= END_YEAR
                   len(emissions_data) >= 1

    There is at least one country with emissions for the given year
    in emissions_data.

    >>> country_with_largest_emissions_by_year(SAMPLE_EMISSIONS_DATA, 1800)
    'Poland'
    """
    max = 0.0
    country = ''
    yearIN = get_year_index(year)
    for i in emissions_data:
        if i[yearIN] > max:
            max = i[yearIN]
            country = i[0]
    return country


def emissions_by_country_by_year(emissions_per_person: list[list],
                                 population: list[list],
                                 country: str, year: int) -> number:
    """Return the total emissions for this country in this year
    based on the population and the emissions per person


    If the country is represented in the data, but the population or emission
    for the required year is missing, then return DATA_NOT_FOUND.

    If the country is missing from one or both of the data files,
    return COUNTRY_NOT_FOUND.

    >>> emissions_by_country_by_year(SAMPLE_EMISSIONS_DATA,
    ...                              SAMPLE_POPULATION_DATA,
    ...                              'Canada', 1799)
    3665.0
    >>> emissions_by_country_by_year(SAMPLE_EMISSIONS_DATA,
    ...                              SAMPLE_POPULATION_DATA,
    ...                              'Finland', 1801)
    -1
    """
    pass

def total_emissions_by_countries(countries: list[str], population: list[list],
                                 emissions_per_person: list[list],
                                 year: int) -> number:
    """Return the total CO2 emitted collectively by these countries in this year
    based on their populations and emissions data in the appropriate year.

    If there is a country in the list that is not found in the data,
    return COUNTRY_NOT_FOUND. If all the countries are in the data, but
    none of them have data for the given year, return DATA_NOT_FOUND.
    Otherwise return the total emissions for the years in which these
    countries have valid data.

    Precondition: no table entry for emissions is 0.0

    >>> total_emissions_by_countries(['Canada', 'Finland'],
    ...                              SAMPLE_POPULATION_DATA,
    ...                              SAMPLE_EMISSIONS_DATA, 1799)
    3665.0

    >>> total_emissions_by_countries(['Canada', 'Finland', 'Nowhere'],
    ...                              SAMPLE_POPULATION_DATA,
    ...                              SAMPLE_EMISSIONS_DATA, 1799)
    -2
    """
    pass


def country_average_over_range(data: list[list], range_start: int,
                               range_end: int,
                               country: str) -> number:
    """
    Return the average per-person emissions for the years between range_start
    and range_end for this country in which we have available data. If there
    are no valid entries in this range, return DATA_NOT_FOUND. If country is
    not included in the data, return COUNTRY_NOT_FOUND.

    Preconditions:
        range_start >= START_YEAR
        range_end <= END_YEAR

    >>> country_average_over_range(SAMPLE_EMISSIONS_DATA, 1799, 1800, 'Canada')
    0.007245
    >>> country_average_over_range(SAMPLE_EMISSIONS_DATA, 1799, 1800, 'Finland')
    -1
    """
    pass


def peak_year_by_country(data: list[list], country: str) -> int:
    """Return the year when this country had the largest emissions or
    return COUNTRY_NOT_FOUND if this country is not represented in data.

    If this largest value was the same for multiple years, return the latest
    year the country had this maximum level.

    Precondition: If country is represented in data, then at least one year
    for this country has valid data. (I.e. not all years are MISSING_DATA)


    >>> peak_year_by_country(SAMPLE_EMISSIONS_DATA, 'Canada')
    1799
    >>> peak_year_by_country(SAMPLE_EMISSIONS_DATA, 'Nowhere')
    -2
    """
    pass


################################################################################
# Data mutation
################################################################################

def create_total_emissions_table(emissions_data: list[list],
                                 population_data: list[list]) -> list[list]:
    """Create and return a table in same format as emissions_data but using the
    population data to determine the total emissions in each year.
    Years where the emissions_per_person data is not available have values from
    the constant MISSING_DATA as the entry. The returned table should also have
    MISSING_DATA when no population data is available for that country/year.

    Precondition: countries are in the same order in all three tables.

    >>> table = create_total_emissions_table(SAMPLE_EMISSIONS_DATA, \
    SAMPLE_POPULATION_DATA)
    >>> table[1][:5]
    ['Finland', -1.0, -1.0, -1.0, 2888.27]
    """

    pass



def update_country_year_data(data: list[list], country: str, year: int,
                             new_data: float) -> float:
    """Replace the values in data for the given year and country
    with new_data. Return the original value or COUNTRY_NOT_FOUND if country
    is not in data.

    Precondition: START_YEAR <= year <= END_YEAR

    >>> small_sample_data = [['France', -1.0, -1.0, -1.0, -1.0] + [-1.0] * 215]
    >>> update_country_year_data(small_sample_data, 'France', 1799, 0.05)
    -1.0
    >>> small_sample_data[0][:5]
    ['France', 0.05, -1.0, -1.0, -1.0]
    >>> update_country_year_data(small_sample_data, 'Canada', 1799, 0.05)
    -2
    """
    pass




if __name__ == '__main__':

    import doctest
    doctest.testmod()
