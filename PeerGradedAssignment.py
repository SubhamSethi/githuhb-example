{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Importing all the required libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting package metadata (current_repodata.json): done\n",
      "Solving environment: done\n",
      "\n",
      "# All requested packages already installed.\n",
      "\n",
      "Collecting package metadata (current_repodata.json): done\n",
      "Solving environment: done\n",
      "\n",
      "# All requested packages already installed.\n",
      "\n",
      "Requirement already satisfied: beautifulsoup4 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (4.9.0)\n",
      "Requirement already satisfied: soupsieve>1.2 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from beautifulsoup4) (2.0)\n",
      "Libraries imported.\n"
     ]
    }
   ],
   "source": [
    "import numpy as np # library to handle data in a vectorized manner\n",
    "\n",
    "import pandas as pd # library for data analsysis\n",
    "\n",
    "import json # library to handle JSON files\n",
    "\n",
    "!conda install -c conda-forge geopy --yes\n",
    "from geopy.geocoders import Nominatim # convert an address into latitude and longitude values\n",
    "\n",
    "#import requests # library to handle requests\n",
    "from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe\n",
    "\n",
    "# Matplotlib and associated plotting modules\n",
    "import matplotlib.cm as cm\n",
    "import matplotlib.colors as colors\n",
    "\n",
    "# import k-means from clustering stage\n",
    "from sklearn.cluster import KMeans\n",
    "\n",
    "!conda install -c conda-forge folium=0.5.0 --yes\n",
    "import folium # map rendering library\n",
    "\n",
    "get_ipython().system(u' pip install beautifulsoup4')\n",
    "from bs4 import BeautifulSoup as bs\n",
    "\n",
    "import requests\n",
    "\n",
    "print('Libraries imported.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### installing xml "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: lxml in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (4.5.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install lxml"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Reading the table from the wikipedia page"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M1A</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M2A</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M3A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Parkwoods</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M4A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Victoria Village</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M5A</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Regent Park, Harbourfront</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175</th>\n",
       "      <td>M5Z</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>176</th>\n",
       "      <td>M6Z</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>177</th>\n",
       "      <td>M7Z</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>178</th>\n",
       "      <td>M8Z</td>\n",
       "      <td>Etobicoke</td>\n",
       "      <td>Mimico NW, The Queensway West, South of Bloor,...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>179</th>\n",
       "      <td>M9Z</td>\n",
       "      <td>Not assigned</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>180 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Postal Code           Borough  \\\n",
       "0           M1A      Not assigned   \n",
       "1           M2A      Not assigned   \n",
       "2           M3A        North York   \n",
       "3           M4A        North York   \n",
       "4           M5A  Downtown Toronto   \n",
       "..          ...               ...   \n",
       "175         M5Z      Not assigned   \n",
       "176         M6Z      Not assigned   \n",
       "177         M7Z      Not assigned   \n",
       "178         M8Z         Etobicoke   \n",
       "179         M9Z      Not assigned   \n",
       "\n",
       "                                          Neighborhood  \n",
       "0                                                  NaN  \n",
       "1                                                  NaN  \n",
       "2                                            Parkwoods  \n",
       "3                                     Victoria Village  \n",
       "4                            Regent Park, Harbourfront  \n",
       "..                                                 ...  \n",
       "175                                                NaN  \n",
       "176                                                NaN  \n",
       "177                                                NaN  \n",
       "178  Mimico NW, The Queensway West, South of Bloor,...  \n",
       "179                                                NaN  \n",
       "\n",
       "[180 rows x 3 columns]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "req = requests.get(\"https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M\")\n",
    "\n",
    "soup = bs(req.content,'lxml')\n",
    "\n",
    "table = soup.find_all('table')[0]\n",
    "\n",
    "df = pd.read_html(str(table))\n",
    "\n",
    "neighborhood=pd.DataFrame(df[0])\n",
    "\n",
    "neighborhood"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Removing the not assigned values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>M3A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Parkwoods</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>M4A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Victoria Village</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>M5A</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Regent Park, Harbourfront</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5</td>\n",
       "      <td>M6A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Lawrence Manor, Lawrence Heights</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>6</td>\n",
       "      <td>M7A</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Queen's Park, Ontario Provincial Government</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>160</td>\n",
       "      <td>M8X</td>\n",
       "      <td>Etobicoke</td>\n",
       "      <td>The Kingsway, Montgomery Road, Old Mill North</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>165</td>\n",
       "      <td>M4Y</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Church and Wellesley</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>168</td>\n",
       "      <td>M7Y</td>\n",
       "      <td>East Toronto</td>\n",
       "      <td>Business reply mail Processing Centre</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>169</td>\n",
       "      <td>M8Y</td>\n",
       "      <td>Etobicoke</td>\n",
       "      <td>Old Mill South, King's Mill Park, Sunnylea, Hu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>102</th>\n",
       "      <td>178</td>\n",
       "      <td>M8Z</td>\n",
       "      <td>Etobicoke</td>\n",
       "      <td>Mimico NW, The Queensway West, South of Bloor,...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>103 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     index Postal Code           Borough  \\\n",
       "0        2         M3A        North York   \n",
       "1        3         M4A        North York   \n",
       "2        4         M5A  Downtown Toronto   \n",
       "3        5         M6A        North York   \n",
       "4        6         M7A  Downtown Toronto   \n",
       "..     ...         ...               ...   \n",
       "98     160         M8X         Etobicoke   \n",
       "99     165         M4Y  Downtown Toronto   \n",
       "100    168         M7Y      East Toronto   \n",
       "101    169         M8Y         Etobicoke   \n",
       "102    178         M8Z         Etobicoke   \n",
       "\n",
       "                                          Neighborhood  \n",
       "0                                            Parkwoods  \n",
       "1                                     Victoria Village  \n",
       "2                            Regent Park, Harbourfront  \n",
       "3                     Lawrence Manor, Lawrence Heights  \n",
       "4          Queen's Park, Ontario Provincial Government  \n",
       "..                                                 ...  \n",
       "98       The Kingsway, Montgomery Road, Old Mill North  \n",
       "99                                Church and Wellesley  \n",
       "100              Business reply mail Processing Centre  \n",
       "101  Old Mill South, King's Mill Park, Sunnylea, Hu...  \n",
       "102  Mimico NW, The Queensway West, South of Bloor,...  \n",
       "\n",
       "[103 rows x 4 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = neighborhood\n",
    "df[\"Borough\"].replace(\"Not assigned\",np.nan,inplace=True)\n",
    "df.dropna(subset=[\"Borough\"],axis=0,inplace=True)\n",
    "df.reset_index(inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Final DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M3A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Parkwoods</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M4A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Victoria Village</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>M5A</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Regent Park, Harbourfront</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M6A</td>\n",
       "      <td>North York</td>\n",
       "      <td>Lawrence Manor, Lawrence Heights</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>M7A</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Queen's Park, Ontario Provincial Government</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>M8X</td>\n",
       "      <td>Etobicoke</td>\n",
       "      <td>The Kingsway, Montgomery Road, Old Mill North</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>M4Y</td>\n",
       "      <td>Downtown Toronto</td>\n",
       "      <td>Church and Wellesley</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>M7Y</td>\n",
       "      <td>East Toronto</td>\n",
       "      <td>Business reply mail Processing Centre</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>M8Y</td>\n",
       "      <td>Etobicoke</td>\n",
       "      <td>Old Mill South, King's Mill Park, Sunnylea, Hu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>102</th>\n",
       "      <td>M8Z</td>\n",
       "      <td>Etobicoke</td>\n",
       "      <td>Mimico NW, The Queensway West, South of Bloor,...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>103 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Postal Code           Borough  \\\n",
       "0           M3A        North York   \n",
       "1           M4A        North York   \n",
       "2           M5A  Downtown Toronto   \n",
       "3           M6A        North York   \n",
       "4           M7A  Downtown Toronto   \n",
       "..          ...               ...   \n",
       "98          M8X         Etobicoke   \n",
       "99          M4Y  Downtown Toronto   \n",
       "100         M7Y      East Toronto   \n",
       "101         M8Y         Etobicoke   \n",
       "102         M8Z         Etobicoke   \n",
       "\n",
       "                                          Neighborhood  \n",
       "0                                            Parkwoods  \n",
       "1                                     Victoria Village  \n",
       "2                            Regent Park, Harbourfront  \n",
       "3                     Lawrence Manor, Lawrence Heights  \n",
       "4          Queen's Park, Ontario Provincial Government  \n",
       "..                                                 ...  \n",
       "98       The Kingsway, Montgomery Road, Old Mill North  \n",
       "99                                Church and Wellesley  \n",
       "100              Business reply mail Processing Centre  \n",
       "101  Old Mill South, King's Mill Park, Sunnylea, Hu...  \n",
       "102  Mimico NW, The Queensway West, South of Bloor,...  \n",
       "\n",
       "[103 rows x 3 columns]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=df[[\"Postal Code\",\"Borough\",\"Neighborhood\"]]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(103, 4)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
