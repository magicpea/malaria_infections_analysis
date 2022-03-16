"""
Marala Berdyeva, Jenn Wilson, and Marie O'Connell
CSE 163 Final Project
Malaria Infections in African Countries, clean.py
"""

"""
This fail contains methods that clean the datasets by mergring the geo_coded
dataframe, the reported numbers dataframe, and the malaria dataframe into one,
all-inclusive dataframe. In addition, this file adds new columns to the
new dataframe including country name, number of cases, number of deaths,
mortality rate, if the country is majority rural or not, and the percentages
of pregnant people given IPT (intermittent preventative treatment)
"""


def clean_data(geo_df, rep_df, mal_df):
    """
    Merges the three datasets containing geo data, reported malaria cases
    and malaria information. Returns the merged dataset.
    """
    df = geo_df.merge(rep_df, on='Country',
                      how='left').merge(mal_df,
                                        left_on='Country',
                                        right_on='Country Name',
                                        how='left')
    return df


def add_new_cols(df):
    """
    Function takes in the merged dataset and computes the malaria mortality
    rate using malaria deaths and cases for each African country. Creates a
    new column containing the name of each country and its mortality rate.
    In addition, computes whether a country has greater than half of its
    population classified as rural. This allows users to look at the data
    and determine if rural vs non-rural (urban) majority countries have
    differennt malaria data. Also adds a new column with information about
    what percentage of pregnant people are given intermittent preventative
    treatment for malaria (IPT). Returns the newly generated dataframe.
    """
    df['No. of cases'].dropna()
    df['No. of deaths'].dropna()
    total_cases = df.groupby('Country')['No. of cases'].sum()
    new_df = total_cases.to_frame()
    new_df['Country Name'] = new_df.index
    new_df['No. of deaths'] = df.groupby('Country')['No. of deaths'].sum()
    new_df['Mortality rate'] = (new_df['No. of deaths'] /
                                new_df['No. of cases']) * 100
    new_df['Rural percentage'] = df.groupby('Country')['Rural population \
                                            (% of total population)'].mean()
    new_df['Urban percentage'] = df.groupby('Country')['Urban population \
                                            (% of total population)'].mean()
    is_mostly_rural = (new_df['Rural percentage'] >= 50)
    new_df['Is Rural'] = is_mostly_rural
    new_df['IPT in pregnant women'] = df.groupby('Country')['Intermittent \
                                                preventive treatment (IPT) \
                                                of malaria in pregnancy \
                                                (% of pregnant women)'].mean()
    return new_df
