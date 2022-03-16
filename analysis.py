"""
Marala Berdyeva, Jenn Wilson, and Marie O'Connell
CSE 163 Final Project
Malaria Infections in African Countries, analysis.py
"""

import plotly.express as px

"""
This file contains methods for analysis including finding the top malaria
cases by country, the top deaths by country, the top morality rate by country,
and the mortality rate of a given country. This file also contains plots
that examine malaria cases by country by year, deaths by country by year,
mortality rate by country regarding IPT levels, rural vs urban morality rates,
and IPT levels in rural vs. urban areas.
"""


def find_top_cases(df):
    """
    Finds country with the top total number of malaria cases in the dataframe.
    Returns a tuple with the country's name and the number of cases.
    """
    temp = df.groupby('No. of cases')['Country Name'].first()
    cases = df['No. of cases'].max()
    country = temp.iloc[-1]
    return((country, cases))


def find_top_deaths(df):
    """
    Finds country with the top total number of malaria deaths in the dataframe.
    Returns a tuple with the country's name and the number of deaths.
    """
    temp = df.groupby('No. of deaths')['Country Name'].first()
    deaths = df['No. of deaths'].max()
    country = temp.iloc[-1]
    return((country, deaths))


def find_top_mortality_rate(df):
    """
    Finds country with the top mortality rate of malaria in the dataframe.
    Returns a tuple with the country's name and the number of cases.
    """
    temp = df.groupby('Mortality rate')['Country Name'].first()
    rate = df['Mortality rate'].max()
    country = temp.iloc[-1]
    return((country, rate))


def get_mortality_rate(country, df):
    """
    Finds the mortality rate of malaria for the given country in the dataframe.
    Returns the mortality rate of that country. If the country name is invalid
    or not in the dataframe, returns None.
    """
    temp = df[df['Country Name'] == country]
    if len(temp) == 0:
        return None
    return temp['Mortality rate']


def plot_cases_by_country_by_year(df):
    """
    Plots a line chart representing the number of total malaria cases in each
    country by year in the dataframe.
    """
    in_africa = df['WHO Region'] == 'Africa'
    africa_df = df[in_africa].dropna()
    fig = px.line(africa_df,
                  x='Year',
                  y='No. of cases',
                  color='Country',
                  markers=True,
                  height=1500,
                  title='Number of Reported Malaria Cases by Year per Country')
    fig.show()


def plot_deaths_by_country_by_year(df):
    """
    Plots a line chart representing the number of total malaria deaths in each
    country by year in the dataframe.
    """
    in_africa = df['WHO Region'] == 'Africa'
    africa_df = df[in_africa].dropna()
    fig = px.line(africa_df,
                  x='Year',
                  y='No. of deaths',
                  color='Country',
                  markers=True,
                  height=1500,
                  title='Number of Reported Malaria \
                         Deaths by Year per Country')
    fig.show()


def plot_mort_rate_by_country_ipt(df):
    """
    Plots a bar chart representing the mortality rates for each country and
    the percentages of pregnant people who have recieved intermittent
    preventative treatment for malaria in the dataframe.
    """
    fig = px.bar(df, y='Country Name',
                 x='Mortality rate',
                 color='IPT in pregnant women',
                 orientation='h',
                 color_continuous_scale='Bluered_r',
                 height=800,
                 width=1000,
                 title='Mortality Rate by Country Regarding IPT Levels')
    fig.show()


def plot_rural_mortality_rate(df):
    """
    Plots a bar chart representing each country and whether it is considered
    to be mostly rural (>50% of pop rural) or not (urban), and the mortality
    rates for each country in the dataframe.
    """
    fig = px.bar(df, y='Country Name',
                 x='Rural percentage',
                 color='Mortality rate',
                 orientation='h',
                 color_continuous_scale='Bluered_r',
                 height=1000,
                 title='Rural Levels by Country Regarding Mortality Rates')
    fig.show()


def plot_ipt_rural_levels(df):
    """
    Plots a bar chart representing each country and whether it is considered
    to be mostly rural (>50% of pop rural) or not (urban), and the percentage
    of pregnant people given intermittent preventative treatment for malaria
    in the dataframe.
    """
    fig = px.bar(df, y='Country Name',
                 x='Rural percentage',
                 color='IPT in pregnant women',
                 orientation='h',
                 color_continuous_scale='Bluered_r',
                 height=1000,
                 title='Rural Levels by Country Regarding IPT Levels')
    fig.show()
