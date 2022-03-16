# Malaria Infections Analysis
## by Marala Berdyeva, Jenn Willson & Marie O’Connell

### Research Questions :
#### 1. Do countries with a high rural population (50%) have higher mortality rates?
- We investigated the difference between countries with majority rural vs urban populations and calculated their mortality rates. For each country, we wanted to see if a country with a majority rural population has a high or low mortality rate. The results for this question have shown that there is no clear correlation between countries being more rural having higher mortality rates.
#### 2. How has the number of cases changed over time? How has the number of deaths changed over time?
- We investigated the trend in malaria cases over time (between 2000 and 2017) as well as deaths over time for each country. We wanted to see if there has been a trend over a recent time frame of 17 years to understand the impact of recent improvements in medical access in African countries. The results showed that most countries’ deaths decreased with the exception of the Democratic Republic of Congo and that case numbers are trending upwards across the majority of countries.
#### 3. Do countries with a higher percentage of women that have received intermittent preventive treatment (IPT) have a lower mortality rate?
- We investigated the difference between malaria mortality rates between countries with a higher percentage of women that have received intermittent preventive treatment (IPT) to see if the treatment affects the mortality rate. The result of our analysis shows that, on average, countries that have a higher percentage of women that have received intermittent preventive treatment (IPT) have a lower mortality rate.
#### 4. Do countries with a higher percentage of rural populations have a lower percentage of women that have received IPT?
- We investigated the difference between countries with majority rural vs urban populations to see if countries with more rural populations have less access to preventative medicine like intermittent preventive treatment (IPT). The results show no clear correlation between the two variables–regardless of rural population size, the percentage of women receiving IPT is low with the exception of 2 countries.
### Motivation :
Although malaria is not as widely spread as it is not, millions of people are still affected by it. Countries with low access to medical resources are facing a crisis when it comes to malaria rates and their mortality rates. In 2010, malaria “caused 216 million clinical episodes and over 655,000 deaths” (Why is malaria research important?). African countries face one of the highest rates of malaria, which is why it is important to focus on these counties. We want to investigate how malaria cases and deaths compare in different regions and countries in Africa. We are interested to learn how rural vs urban environments and access to
preventative treatments might impact mortality rates for Malaria by country. These investigations are important as understanding malaria is essential to many countries as more service personnel can be dispatched at higher rates if malaria is still prevalent. With our research, we can bring more attention to the current problem and bring more awareness to how we can address these issues.

### Datasets :
This project requires downloading the following files :
- https://www.kaggle.com/imdevskp/malaria-dataset
  - use reported_numbers.csv
- https://www.kaggle.com/jboysen/malaria-mosquito
  - use Africa_Vectors_database_1898-2016.csv
- https://www.kaggle.com/lydia70/malaria-in-africa
  - use DatasetAfricaMalaria.csv

### Instructions :
It is important to note that that second dataset, Africa_Vectors_database_1898-2016.csv, must be converted into an SHP file in order to use the geo-coded data to be read in with geopandas. Our team did this conversion using the following site : https://mygeodata.cloud/converter/ . Make sure to upload all of the files with the following suffixes into your data folder in order for the SHP file to be read in correctly : (.SHP, .CPG, .DBF, .PRJ, .SHX, .CSV)

In addition, these are the following installations that will be needed. If pip is not working on your machine, we recommend using pip3 :

* Important library for many geopython libraries
`!apt install gdal-bin python-gdal python3-gdal`
* Install rtree - Geopandas requirment
`!apt install python3-rtree`
* Install descartes - Geopandas requirment
`!pip install descartes`
* Install Folium for Geographic data visualization
`!pip install folium`
* Install plotlyExpress
`!pip install plotly_express`
* New pip datapackage
`!pip install datapackage`
* Import geopandas
`!pip install geopandas`
* Import pandas
`!pip install pandas`
