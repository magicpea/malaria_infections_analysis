"""
Marala Berdyeva, Jenn Wilson, and Marie O'Connell
CSE 163 Final Project
Malaria Infections in African Countries, test.py
"""

import pandas as pd
import geopandas as gpd
from cse163_utils import assert_equals

import analysis
import clean

"""
This file loads in three different datasets, tests
the analysis methods and the values of the merged
dataframe, and contains a main method where tests
are called and plots are produced. Uses the cse163
utils python file to test using the assert_equals
method.
"""


GEO_DF = gpd.read_file("/content/Africa_Vectors_ \
                       database_1898-2016_mutated-point.shp",
                       sep=';')
REP_DF = pd.read_csv("reported_numbers.csv")
MAL_DF = pd.read_csv("/content/DatasetAfricaMalaria 3.csv")


def test_unique_country_names(df):
    """
    Tests to ensure the dataframe has all of the unique country name
    values that are going to be needed for analysis.
    """
    assert_equals(['Angola', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon',
                   'Central African Republic', 'Chad', 'Comoros',
                   'Equatorial Guinea', 'Gabon', 'Ghana', 'Guinea',
                   'Kenya', 'Liberia', 'Madagascar', 'Malawi', 'Mali',
                   'Mauritania', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
                   'Rwanda', 'Sao Tome and Principe', 'Senegal',
                   'Sierra Leone', 'South Sudan', 'Sudan', 'Togo', 'Uganda',
                   'Zambia', 'Zimbabwe'], df['Country Name'].unique())


def test_num_unique_countries(df):
    """
    Tests to ensure the dataframe has the correct number of country values.
    """
    assert_equals(32, df['Country Name'].nunique())


def test_find_top_mortality_rate(df):
    """
    Tests the find_top_mortality_rate method from analysis.py
    """
    assert_equals(('Namibia', 2.7965770087956585),
                  analysis.find_top_mortality_rate(df))


def test_find_top_cases(df):
    """
    Tests the find_top_cases method from analysis.py
    """
    assert_equals(('Burkina Faso', 253849262964.0),
                  analysis.find_top_cases(df))


def test_find_top_deaths(df):
    """
    Tests the find_top_deaths method from analysis.py
    """
    assert_equals(('Kenya', 3939342946.0),
                  analysis.find_top_cases(df))


def test_get_mortality_rate(df):
    """
    Tests the get_mortality_rate method from analysis.py
    """
    assert_equals(2.796577,
                  analysis.get_mortality_rate('Namibia', df))
    assert_equals(0.174647,
                  analysis.get_mortality_rate('Ghana', df))
    assert_equals(None,
                  analysis.get_mortality_rate('Palestine', df))


def main():
    merged_df = clean.clean_data(GEO_DF, REP_DF, MAL_DF)
    new_df = clean.add_new_cols(merged_df)
    df = new_df.dropna()
    test_unique_country_names(df)
    test_num_unique_countries(df)
    test_find_top_cases(df)
    test_find_top_deaths(df)
    test_get_mortality_rate(df)
    analysis.plot_cases_by_country_by_year(REP_DF)
    analysis.plot_deaths_by_country_by_year(REP_DF)
    analysis.plot_mort_rate_by_country_ipt(df)
    analysis.plot_rural_mortality_rate(df)
    analysis.plot_ipt_rural_levels(df)


if __name__ == '__main__':
    main()
