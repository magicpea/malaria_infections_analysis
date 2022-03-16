# Malaria Infections Analysis
## by Marala Berdyeva, Jenn Willson & Marie O’Connell

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
