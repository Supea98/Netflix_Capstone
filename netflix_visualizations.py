{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks = pd.read_csv('NFLX.csv')\n",
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks = pd.read_csv('DJI.csv')\n",
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "..        ...     ...  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')\n",
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2017"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Data is represented by months in months for NFLX.csv and DJI.csv while NFLX_daily_by_quarter.csv is reported daily.'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Data is represented by months in months for NFLX.csv and DJI.csv while NFLX_daily_by_quarter.csv is reported daily.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
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
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns = {'Adj Close':'Price'}, inplace=True)\n",
    "dowjones_stocks.rename(columns = {'Adj Close':'Price'}, inplace=True)\n",
    "netflix_stocks_quarterly.rename(columns = {'Adj Close':'Price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
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
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
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
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Quarter</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-03</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>128.190002</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>9437900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-01-04</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>130.169998</td>\n",
       "      <td>126.550003</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>7843600</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-01-05</td>\n",
       "      <td>129.220001</td>\n",
       "      <td>132.750000</td>\n",
       "      <td>128.899994</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>10185500</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-01-06</td>\n",
       "      <td>132.080002</td>\n",
       "      <td>133.880005</td>\n",
       "      <td>129.809998</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>10657900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-01-09</td>\n",
       "      <td>131.479996</td>\n",
       "      <td>131.990005</td>\n",
       "      <td>129.889999</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>5766900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
       "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
       "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
       "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
       "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
       "\n",
       "     Volume Quarter  \n",
       "0   9437900      Q1  \n",
       "1   7843600      Q1  \n",
       "2  10185500      Q1  \n",
       "3  10657900      Q1  \n",
       "4   5766900      Q1  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dowjones_stocks.head()\n",
    "netflix_stocks_quarterly.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjsAAAHFCAYAAAAUpjivAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAACSP0lEQVR4nOzdd3iT5frA8e+bpuluoZtCW/ZeCiKCMmRvZAgHFRDEiQKiRzn+jriOiMdxcOLx4AIRkCUUlD1kiLIpsi27UGahu02e3x9pAqG7JE3a3J/rytXkfd88751m3XmmppRSCCGEEEJUUDpnByCEEEII4UiS7AghhBCiQpNkRwghhBAVmiQ7QgghhKjQJNkRQgghRIUmyY4QQgghKjRJdoQQQghRoUmyI4QQQogKTZIdIYQQQlRokuy4oG+++QZN06wXb29vIiMj6dixI1OmTCEpKSnPfV577TU0TSvRedLS0njttddYv359ie6X37mqV69O7969S1ROUWbPns1//vOffPdpmsZrr71m1/PZ25o1a2jZsiV+fn5omsbixYvzPe7w4cO88MILtGjRgkqVKhEcHEzbtm2ZP39+vscnJSUxcuRIQkND8fX15Z577mHNmjV5jouLi2P48OE0adIET0/PAl8fluezoMucOXMKfZyW16u3tzcnTpzIs79Dhw40bty40DIKUthr4Pjx4/Tq1Yvg4GA0TWP8+PEcP34cTdP45ptv8sR3/PjxUsWQnxUrVtC1a1eioqLw8vIiKiqKDh068M4779gc9/bbbxf4vNuL5TG/9957pbr/rc93UFAQHTp0YNmyZcW6//r169E0rcSfI45miaug95G9/fbbbwwePJgqVapgMBioUqUKDz74IH/88UeZnL8wn332mc17wi0p4XK+/vprBaivv/5abd26VW3cuFHNnz9fjR8/XgUFBang4GC1atUqm/ucOnVKbd26tUTnuXDhggLU5MmTS3S//M4VGxurevXqVaJyitKrVy8VGxub776tW7eqU6dO2fV89mQymVRwcLBq3bq1Wr16tdq6dau6fPlyvsd+/PHHqn79+upf//qXWrlypVq+fLkaMWKEAtTrr79uc2xGRoZq3Lixqlatmpo1a5ZauXKl6tevn9Lr9Wr9+vU2x44aNUrVqVNHPfjgg6pFixaqoLe75fm89dK4cWPl4+Ojrly5Uuhj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zbJlyzAajTadHfNz3333cd9992E0Gtm+fTsff/wx48ePJyIigqFDhxbrXCX5JXLu3LkCt1ne5JZfepmZmTbH3e4XXEhICImJiXm2WzoWhoaG3lb5YP7VpNPpHHaeFStW0L9/f9q3b8+CBQswGAx5jmnSpAn79u3Ls92yrbTz2VjMnDmTrKysEnVMvpWmaUydOpUuXbrw3//+N89+S4fsX3/91Zpk3iy/bY4QHx/Pq6++yl133cUff/zBBx98wPPPP1+qsvz8/Jg0aRJz584lPj6+yOOL+3oNCwvj9OnTxYrhxRdf5OjRowwfPpycnByGDx9e7PjDwsJo2bJlkccV5/PAMvChsLgrV65srRF95pln8j2mRo0agLmT7/PPP8/zzz/P1atXWb16Nf/4xz/o1q0bp06dwtfXt9B4CvpcujXxGDduHDNnzuSnn37il19+oVKlSjz00EOFlu3h4cH999/Pzz//zOnTp/NN8E6fPs2OHTvo3r27dZu3t3eez0DI+zm4ePFiUlNTWbhwoU1N3e7du/ONp6Q1R6Ghofj4+BSYoN/6eWaPmmNnkZqdcubkyZO88MILBAUF8cQTTxTrPh4eHtx9993WXwOWJqXi1GaUxP79+9mzZ4/NttmzZxMQEMCdd94JYB0FsHfvXpvjlixZkqc8Ly+vYsfWqVMn1q5dm2fUxHfffYevry+tW7cu7sMokJ+fH3fffTcLFy60ictkMjFr1iyqVatG3bp1S1X2ypUr6d+/P/feey+LFy8u8Av/gQce4ODBg2zbts26LScnh1mzZnH33XcXWttXHDNmzCAqKooePXrcVjmdO3emS5cuvPHGG6SkpNjs6927N0opzpw5Q8uWLfNcmjRpYj22JK+BkkhNTWXw4MFUr16ddevWMXbsWF5++WWb/2tB8ktSAA4cOABg8xwUFH9xX689evTg8OHDrF27tsi4dDod//3vfxk3bhwjR47k888/L/I+jlC3bl1q1arFV199le8XOoCvry8dO3Zk165dNG3aNN/XQX61IJUqVWLQoEE888wzXL58uVgTRf7www82zf4nTpxgy5YteX4stmjRgjZt2jB16lS+//57Ro4ciZ+fX5Hlv/zyyyilePrppzEajTb7jEYjTz31FEajkXHjxlm3V69enaSkJM6fP2/dlpWVxYoVK2zub0kubv48UErZNLcVR0Gv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YMAAlZqaaj3m66+/VkCey+TJk50XuCiVop5vy/QC+V3WrVvn3OBFiRX1fKenp6sHHnhARUVFKYPBoKpUqaL69u2rfv/9dydHLkqjOJ/nt5JkRylNKRl37G4mT57MBx98wMqVK7nnnnucHY5wMHm+3Ys83+5Fnu/ikWTHTX399dckJyfz3HPPodNJ162KTp5v9yLPt3uR57tokuwIIYQQokKTFFAIIYQQFZokO0IIIYSo0CTZEUIIIUSFJsmOEEIIISo0SXaEEEIIUaFJsiOEEEKICk2SHSEqsPXr16NpGlevXnV2KKIA8hwJ4XiS7AjhJCNHjkTTNOslJCSE7t27s3fvXrudo02bNiQmJhIUFGS3Mu0tPT2dyZMnU69ePby8vAgNDWXQoEHs37+/zGJ47bXXaN68eZmd72b2eI727NnD3/72N6Kjo/Hx8aFBgwZMmzYtz3H79u2jffv2+Pj4ULVqVd544w1unmotMTGRYcOGUa9ePXQ6HePHj89TRocOHWxet5ZLr169Sh2/EI4myY4QTtS9e3cSExNJTExkzZo16PV6evfubbfyDQYDkZGRaJpmtzLtKTMzk86dO/PVV1/x5ptvcvjwYZYvX47RaOTuu+/mt99+c+j5lVLk5OTYrbzs7OwS38cez9GOHTsICwtj1qxZ7N+/n1deeYVJkybxySefWI+5du0aXbp0ISoqij/++IOPP/6Y9957jw8++MB6TGZmJmFhYbzyyis0a9Ys33MtXLjQ+ppNTEwkPj4eDw8PBg8eXOr4hXA45y3LJYR7GzFihOrXr5/Nto0bNypAJSUlKaWUWrdunQLUlStXrMfs2rVLASohIUEppdTx48dV7969VaVKlZSvr69q2LChWrZsWb73//rrr1VQUJD65ZdfVP369ZWfn5/q1q2bOnv2rE0cX331lapfv77y8vJS9erVU59++ql1X2ZmpnrmmWdUZGSk8vLyUrGxsertt9+27p88ebKKjo62Ljr57LPPFvg/eOedd5SmaWr37t02241Go2rZsqVq2LChMplMSiml2rdvr8aNG2dzXL9+/dSIESOst2fOnKlatGih/P39VUREhPrb3/6mzp8/b91v+X/88ssvqkWLFsrT01N99dVXeRZE/frrr5VSSl29elWNGTNGhYWFqYCAANWxY0ebWCdPnqyaNWumZsyYoWrUqKE0TVMm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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.violinplot(data=netflix_stocks_quarterly, x='Quarter', y='Price')\n",
    "ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')\n",
    "plt.xlabel('Business Quarters in 2017')\n",
    "plt.ylabel('Closing Stock Price')\n",
    "plt.show()\n",
    "\n",
    "plt.savefig('NetDist.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjEAAAGxCAYAAACTN+exAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABB7klEQVR4nO3de1xUdeL/8fcMt0GE8YKixkWWVCDvUApmWil5q7S26IZdNy1NXXe3MivNasm2i+mq5Za69jW1NnGtzKIyLz/tooHrhqaZCiqEuAmICwhzfn/M1/k2gsogCAdfz8fjPGbncz7ncz5n5my8/ZxzPmMxDMMQAACAyVgbugMAAAC1QYgBAACmRIgBAACmRIgBAACmRIgBAACmRIgBAACmRIgBAACmRIgBAACmRIgBAACmRIhBk7Z48WJZLJYzLl9++WWD9Gv69OmyWCwNsu+aGDhwoNvn5O/vrx49emjWrFlyOBz1vv+SkhLNnDlTPXr0UFBQkAIDAxUVFaVbb71V69evd9U79f1u3bq13vt0vurrOy8qKtLzzz+v+Ph4BQUFyc/PTx07dtR9992n7777rs7392vvvPOOZs2aVa/7AM7Gu6E7AFwIixYtUnR0dJXy2NjYBuiN9MADD2jIkCENsu+a+s1vfqOlS5dKkvLz8/X666/r97//vXJzczVz5sx6229lZaWSkpK0Y8cO/elPf9IVV1whSdqzZ48++OADbdy4UQMGDKi3/deX+vjO9+7dq6SkJOXn52vs2LF65pln1Lx5c+3fv1/vvvuu4uLidOzYMdnt9jrd7ynvvPOO/v3vf2vSpEn10j5wLoQYXBS6du2q+Pj4emv/xIkTatasWY3rh4aGKjQ0tN76Uxf8/f3Vt29f1/uhQ4cqOjpaf/3rX/Xcc8/Jx8en1m1XVlaqoqJCfn5+VdZt2LBBmzdv1sKFC3Xvvfe6yq+77jqNHz/+gowEnc7T77c6df2dV1ZWatSoUSooKNCWLVvUtWtX17oBAwbo7rvv1scff3xe3xPQ2HE5Cfhfc+fO1VVXXaW2bdsqICBA3bp104svvqiTJ0+61Rs4cKC6du2qDRs2KDExUc2aNdN9992n/fv3y2Kx6KWXXtIrr7yiyMhINW/eXAkJCfrqq6/c2qju0kLHjh01YsQIrV27Vr1795a/v7+io6O1cOHCKn3dtGmTEhISZLPZdMkll+ipp57Sm2++KYvFov3797vqffHFFxo4cKBat24tf39/hYeH6+abb9aJEyc8/nx8fHwUFxenEydO6MiRI5KkvLw8jRkzRqGhofL19VVkZKSeeeYZVVRUuLY79bm8+OKLeu655xQZGSk/Pz+tW7eu2v0cPXpUktS+fftq11utVf+zVVxcrIceekjBwcFq3bq1brrpJh0+fNitzooVK5SUlKT27dvL399fMTExevzxx1VSUuJW75577lHz5s21Y8cOJSUlKTAwUNdee60kqby8XM8995yio6Pl5+enNm3a6N5773V9Hmdzvt/56VatWqUdO3ZoypQpbgHm14YOHeoWvvbs2aM77rhDbdu2lZ+fn2JiYjR37ly3bb788ktZLBYtW7ZMU6dOVYcOHRQUFKRBgwbphx9+cNUbOHCgPvroIx04cMDt0uMp8+fPV48ePdS8eXMFBgYqOjpaTzzxxDmPC/AEIzG4KJz6l/+vWSwWeXl5ud7v3btXd9xxhyIjI+Xr66vt27fr+eef165du6r8UcnNzdVdd92lRx99VH/+85/d/rDOnTtX0dHRrnsFnnrqKQ0bNkz79u0757D+9u3b9Yc//EGPP/64QkJC9Oabb+r+++/XpZdeqquuukqS9K9//UuDBw9W586d9fe//13NmjXT66+/rv/5n/9xa2v//v0aPny4+vfvr4ULF6pFixY6dOiQ1q5dq/Ly8lqNLOzdu1fe3t5q2bKl8vLydMUVV8hqterpp59WVFSUtmzZoueee0779+/XokWL3LadPXu2OnfurJdeeklBQUHq1KlTtfuIj4+Xj4+PJk6cqKefflrXXHPNGQPNKQ888ICGDx+ud955Rzk5OfrTn/6ku+66S1988YWrzp49ezRs2DBNmjRJAQEB2rVrl2bOnKlvvvnGrZ7kDCs33HCDxowZo8cff1wVFRVyOBy68cYbtXHjRj366KNKTEzUgQMHNG3aNA0cOFBbt26Vv7+/x59pTb7z6nz66aeSpJEjR9ZoP1lZWUpMTFR4eLhefvlltWvXTp988okmTJiggoICTZs2za3+E088oX79+unNN99UUVGRHnvsMV1//fXauXOnvLy8NG/ePD344IPau3ev0tLS3LZdvny5Hn74YT3yyCN66aWXZLVa9eOPPyorK8uzDwc4FwNowhYtWmRIqnbx8vI643aVlZXGyZMnjSVLlhheXl7Gf/7zH9e6AQMGGJKMzz//3G2bffv2GZKMbt26GRUVFa7yb775xpBkLFu2zFU2bdo04/T/+0VERBg2m804cOCAq+y///2v0apVK2PMmDGusltuucUICAgwjhw54tbf2NhYQ5Kxb98+wzAM4x//+IchycjMzKzhp/V/BgwYYFx22WXGyZMnjZMnTxqHDx82Hn/8cUOSccsttxiGYRhjxowxmjdv7tZfwzCMl156yZBkfP/9926fS1RUlFFeXl6j/b/11ltG8+bNXd9V+/btjdGjRxsbNmxwq3fq+3344Yfdyl988UVDkpGbm1tt+w6Hwzh58qSxfv16Q5Kxfft217q7777bkGQsXLjQbZtly5YZkoz333/frfzbb781JBnz5s076zGdz3denSFDhhiSjNLS0rPWO+W6664zQkNDjcLCQrfy8ePHGzabzXWOr1u3zpBkDBs2zK3eu+++a0gytmzZ4iobPny4ERERUWVf48ePN1q0aFGjfgHng8tJuCgsWbJE3377rdvy9ddfu9XJyMjQDTfcoNatW8vLy0s+Pj4aPXq0KisrtXv3bre6LVu21DXXXFPtvoYPH+42wtO9e3dJ0oEDB87Zz549eyo8PNz13mazqXPnzm7brl+/Xtdcc42Cg4NdZVarVbfeemuVtnx9ffXggw/q73//u3766adz7v/Xvv/+e/n4+MjHx0cdOnTQyy+/rDvvvFN/+9vfJEkffvihrr76anXo0EEVFRWuZejQoa5+/toNN9xQ4/sz7rvvPh08eFDvvPOOJkyYoLCwMP3P//yPBgwYoL/85S9V6t9www1u76v7zH/66Sfdcccdateunev7PXWD8M6dO6u0efPNN7u9//DDD9WiRQtdf/31bsfbs2dPtWvXrtZPutXkOz9fpaWl+vzzzzVq1Cg1a9bMrf/Dhg1TaWlplUueNflMz+SKK67QsWPHdPvtt+uf//ynCgoK6uxYgF/jchIuCjExMWe9sTc7O1v9+/dXly5d9Nprr6ljx46y2Wz65ptvNG7cOP33v/91q3+2yxutW7d2e3/q5tXT26jJtqe2//W2R48eVUhISJV6p5dFRUXps88+04svvqhx48appKREv/nNbzRhwgRNnDjxnH2JiorS8uXLZbFYZLPZFBkZ6XYJ6ueff9YHH3xwxmBy+h+uc10SOp3dbtftt9+u22+/XZIzVA0aNEhTp07V7373O7Vo0cJV91yf+fHjx9W/f3/ZbDY999xz6ty5s5o1a6acnBzddNNNVb6bZs2aKSgoyK3s559/1rFjx+Tr61uj462pmnzn1TkVfPbt21ftk3e/dvToUVVUVGjOnDmaM2dOtXVO7//5nMcpKSmqqKjQ3/72N918881yOBy6/PLL9dxzz2nw4MHn3B6oKUIMIOdNkiUlJVq5cqUiIiJc5ZmZmdXWb8g5Xlq3bq2ff/65SnleXl6Vsv79+6t///6qrKzU1q1bNWfOHE2aNEkhISG67bbbzrofm8121uAXHBys7t276/nnn692fYcOHdzen+9ndtlll+m2227TrFmztHv3btej1zXxxRdf6PDhw/ryyy/dHs8+duxYtfWr6+upm4bXrl1b7TaBgYE17k9duO6667RgwQKtWrVKjz/++FnrtmzZUl5eXkpJSdG4ceOqrRMZGVmn/bv33nt17733qqSkRBs2bNC0adM0YsQI7d692+3/Y8D5IMQA+r8/Wr9+5NcwDNelk8ZkwIABWrNmjQoKClyXlBwOh957770zbuPl5aU+ffooOjpaS5cu1XfffXfOEHMuI0aM0Jo1axQVFaWWLVueV1u/dvToUQUGBlY74rFr1y5JVQPSuVT3/UrSG2+8UeM2RowYoeXLl6uyslJ9+vTxaP/14cYbb1S3bt2UmpqqESNGVPuE0ieffKL+/furWbNmuvrqq5WRkaHu3bufcTTJUzUZMQoICNDQoUNVXl6ukSNH6vvvvyfEoM4QYnBR+Pe//13l6STJecmkTZs2Gjx4sHx9fXX77bfr0UcfVWlpqebPn69ffvmlAXp7dlOnTtUHH3yga6+9VlOnTpW/v79ef/1116PCp56Uev311/XFF19o+PDhCg8PV2lpqespq0GDBp13P2bMmKH09HQlJiZqwoQJ6tKli0pLS7V//36tWbNGr7/+eq3mRVm3bp0mTpyoO++8U4mJiWrdurXy8/O1bNkyrV27VqNHj/a43cTERLVs2VJjx47VtGnT5OPjo6VLl2r79u01buO2227T0qVLNWzYME2cOFFXXHGFfHx8dPDgQa1bt0433nijRo0a5enh1pqXl5fS0tKUlJSkhIQEPfTQQ7r66qsVEBCgAwcO6B//+Ic++OAD1zn82muv6corr1T//v310EMPqWPH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iAEAAKZEiAEAAKZEiAEAAKZUqxAzb948RUZGymazKS4uThs3bjxj3ZUrV2rw4MFq06aNgoKClJCQoE8++cStzuLFi2WxWKospaWltekeAAC4CHgcYlasWKFJkyZp6tSpysjIUP/+/TV06FBlZ2dXW3/Dhg0aPHiw1qxZo23btunqq6/W9ddfr4yMDLd6QUFBys3NdVtsNlvtjgoAADR5FsMwDE826NOnj3r37q358+e7ymJiYjRy5EilpqbWqI3LLrtMycnJevrppyU5R2ImTZqkY8eOedIVN0VFRbLb7SosLFRQUFCt2wEAABfO+fz99mgkpry8XNu2bVNSUpJbeVJSkjZv3lyjNhwOh4qLi9WqVSu38uPHjysiIkKhoaEaMWJElZGa05WVlamoqMhtAQAAFw+PQkxBQYEqKysVEhLiVh4SEqK8vLwatfHyyy+rpKREt956q6ssOjpaixcv1urVq7Vs2TLZbDb169dPe/bsOWM7qampstvtriUsLMyTQwEAACZXqxt7LRaL23vDMKqUVWfZsmWaPn26VqxYobZt27rK+/btq7vuuks9evRQ//799e6776pz586aM2fOGduaMmWKCgsLXUtOTk5tDgUAAJiUtyeVg4OD5eXlVWXUJT8/v8rozOlWrFih+++/X++9954GDRp01rpWq1WXX375WUdi/Pz85OfnV/POAwCAJsWjkRhfX1/FxcUpPT3drTw9PV2JiYln3G7ZsmW655579M4772j48OHn3I9hGMrMzFT79u096R4AALiIeDQSI0mTJ09WSkqK4uPjlZCQoAULFig7O1tjx46V5LzMc+jQIS1ZskSSM8CMHj1ar732mvr27esaxfH395fdbpckPfPMM+rbt686deqkoqIizZ49W5mZmZo7d25dHScAAGhiPA4xycnJOnr0qGbMmKHc3Fx17dpVa9asUUREhCQpNzfXbc6YN954QxUVFRo3bpzGjRvnKr/77ru1ePFiSdKxY8f04IMPKi8vT3a7Xb169dKGDRt0xRVXnOfhAQCApsrjeWIaK+aJAQDAfC7YPDEAAACNBSEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYEiEGAACYUq1CzLx58xQZGSmbzaa4uDht3LjxjHVXrlypwYMHq02bNgoKClJCQoI++eSTKvXef/99xcbGys/PT7GxsUpLS6tN1wAAwEXC4xCzYsUKTZo0SVOnTlVGRob69++voUOHKjs7u9r6GzZs0ODBg7VmzRpt27ZNV199ta6//nplZGS46mzZskXJyclKSUnR9u3blZKSoltvvVVff/117Y8MAAA0aRbDMAxPNujTp4969+6t+fPnu8piYmI0cuRIpaam1qiNyy67TMnJyXr66aclScnJySoqKtLHH3/sqjNkyBC1bNlSy5Ytq1GbRUVFstvtKiwsVFBQkAdHBAAAGsr5/P32aCSmvLxc27ZtU1JSklt5UlKSNm/eXKM2HA6HiouL1apVK1fZli1bqrR53XXXnbXNsrIyFRUVuS0AAODi4VGIKSgoUGVlpUJCQtzKQ0JClJeXV6M2Xn75ZZWUlOjWW291leXl5XncZmpqqux2u2sJCwvz4EgAAIDZ1erGXovF4vbeMIwqZdVZtmyZpk+frhUrVqht27bn1eaUKVNUWFjoWnJycjw4AgAAYHbenlQODg6Wl5dXlRGS/Pz8KiMpp1uxYoXuv/9+vffeexo0aJDbunbt2nncpp+fn/z8/DzpPgAAaEI8Gonx9fVVXFyc0tPT3crT09OVmJh4xu2WLVume+65R++8846GDx9eZX1CQkKVNj/99NOztgkAAC5uHo3ESNLkyZOVkpKi+Ph4JSQkaMGCBcrOztbYsWMlOS/zHDp0SEuWLJHkDDCjR4/Wa6+9pr59+7pGXPz9/WW32yVJEydO1FVXXaWZM2fqxhtv1D//+U999tln2rRpU10dJwAAaGI8vicmOTlZs2bN0owZM9SzZ09t2LBBa9asUUREhCQpNzfXbc6Y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a6bw8HBNmDBBhYWFbm398ssvSklJkd1ul91uV0pKio4dO+ZWZ+LEiYqLi5Ofn5969uxZpT/Tp0+XxWKpsgQEBNTFR4I6kJqaqssvv1yBgYFq27atRo4cqR9++KFKPc4teGL+/Pnq3r27a8bThIQEffzxx251OKdwvlJTU2WxWDRp0iS38qZ6bpk6xJSUlKhHjx7661//Wu36r776Sn369FF5ebk++ugj7d69W3/+85/197//XYMHD1Z5ebkk6fDhwzp8+LBeeukl7dixQ4sXL9batWt1//33u7V3xx13KDMzU2vXrtXatWuVmZmplJQUtzqGYei+++5TcnJytX364x//qNzcXLclNjZWt9xySx18IqgL69ev17hx4/TVV18pPT1dFRUVSkpKUklJiasO5xY8FRoaqhdeeEFbt27V1q1bdc011+jGG2/U999/L4lzCufv22+/1YIFC9S9e3e38iZ9bhlNhCQjLS3N9d7hcBixsbFGfHy8UVlZ6VY3MzPTsFgsxgsvvHDG9t59913D19fXOHnypGEYhpGVlWVIMr766itXnS1bthiSjF27dlXZftq0aUaPHj3O2e/MzExDkrFhw4Zz1kXDyM/PNyQZ69evNwyDcwt1p2XLlsabb77JOYXzVlxcbHTq1MlIT083BgwYYEycONEwjKb/3ytTj8ScTWZmprKysjR58uQqv4rZo0cPDRo0SMuWLTvj9oWFhQoKCpK3t/M3Mrds2SK73a4+ffq46vTt21d2u12bN2+udT/ffPNNde7cWf379691G6hfp4ZSW7VqJYlzC+evsrJSy5cvV0lJiRISEjincN7GjRun4cOHa9CgQW7lTf3carIhZvfu3ZKkmJiYatfHxMS46pzu6NGjevbZZzVmzBhXWV5entq2bVulbtu2bZWXl1erPpaVlWnp0qVVhurQeBiGocmTJ+vKK69U165dJXFuofZ27Nih5s2by8/PT2PHjlVaWppiY2M5p3Beli9frm3btik1NbXKuqZ+bnnXao9NgGEY8vX1rVJeVFSk4cOHKzY2VtOmTXNbZ7FYqm2nuvKaWLlypYqLizV69OhabY/6N378eP3rX//Spk2barwN5xbOpEuXLsrMzNSxY8f0/vvv6+6779b69evPuR3nFM4kJydHEydO1Keffiqbzebx9mY/t5rsSEynTp0kSVlZWdWu37Vrlzp37uxWVlxcrCFDhqh58+ZKS0uTj4+Pa127du30888/V2nnyJEjCgkJqVUf33zzTY0YMULt2rWr1faoX4888ohWr16tdevWKTQ01FXOuYXa8vX11aWXXqr4+HilpqaqR48eeu211zinUGvbtm1Tfn6+4uLi5O3tLW9vb61fv16zZ8+Wt7e3Lr30UklN99xqsiGmV69eio6O1quvviqHw+G2bvv27frss890zz33uMqKioqUlJQkX19frV69ukqiTUhIUGFhob755htX2ddff63CwkIlJiZ63L99+/Zp3bp1DM02QoZhaPz48Vq5cqW++OILRUZGuq3n3EJdMQxDZWVlnFOotWuvvVY7duxQZmama4mPj9edd96pzMxM9e7du2mfWx7dBtzIFBcXGxkZGUZGRoYhyXjllVeMjIwM48CBA4ZhGMamTZuMZs2aGSNHjjS+/vpr48CBA8a7775rhIWFGUOGDDEqKioMwzCMoqIio0+fPka3bt2MH3/80cjNzXUtp+oYhmEMGTLE6N69u7FlyxZjy5YtRrdu3YwRI0a49WnPnj1GRkaGMWbMGKNz586u/pWVlbnVe/LJJ40OHTq4tY/G4aGHHjLsdrvx5Zdfup0LJ06ccNXh3IKnpkyZYmzYsMHYt2+f8a9//ct44oknDKvVanz66aeGYXBOoe78+ukkw2ja55apQ8y6desMSVWWu+++21XnX//6l3HzzTcbrVq1cq0fP36863Gxs7Ujydi3b5+r3tGjR40777zTCAwMNAIDA40777zT+OWXX9z6NGDAgHO2U1lZaYSGhhpPPPFEPX0yOB9nOhcWLVrkVo9zC5647777jIiICMPX19do06aNce2117oCzCmcU6gLp4cYw2i655bFMAyjdmM45uNwOHT//ffrk08+0fr1613XoYHzxbmFusY5hfrSlM6tiyrESM4vb86cOQoMDNR9993X0N1BE8K5hbrGOYX60lTOrYsuxAAAgKahyT6dBAAAmjZCDAAAMCVCDAAAMCVCDAAAMCVCDAAAMCVCDAAAMCVCDAAAMCVCDAAAMCVCDAAAMKX/DzjojOEizeZPAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "\n",
    "plt.scatter(x_positions, earnings_actual, color='Red', alpha=0.5)\n",
    "plt.scatter(x_positions, earnings_estimate, color='Blue', alpha=0.5)\n",
    "plt.legend(['Actual', 'Estimate'])\n",
    "plt.xticks(x_positions, chart_labels)\n",
    "plt.title('Earnings Per Share in Cents')\n",
    "plt.show()\n",
    "\n",
    "plt.savefig('Earnings.png')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiMAAAGxCAYAAACwbLZkAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA+XElEQVR4nO3deVRV9f7/8deRURFQTAYTFCeczaQUyykTFbX8aTcrZ63rkFoSy9RKG1TK1MxyyKtCk5pdqls5JOXUoBUKao55Q/QaaFqBaYLA5/eHi/PtyKAHtS34fKy112p/zuez9/vsD8aLPZxjM8YYAQAAWKSC1QUAAIAbG2EEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGApwggAALAUYQRXRXx8vGw2m31xdXVVUFCQHnjgAf34449WlwdJNptNzz77bIl9Dh8+7DCPFy+XGn+tbNq0STabTZs2bbJk/2XJunXr1KNHD1WvXl0eHh4KCQnR0KFDdeDAAatL04wZM/TRRx9ZXQauQ65WF4DyJS4uTg0bNtS5c+f09ddfa/r06dq4caP279+vqlWrWl0eLtPYsWP10EMPFWqvWbOmBdVIt956q7Zu3arGjRtbsv+yYsKECXr55ZfVrVs3LViwQAEBATp48KDmzJmjli1batWqVerZs6dl9c2YMUP33XefevfubVkNuD4RRnBVNW3aVOHh4ZKkjh07Ki8vT1OnTtVHH32koUOHWlwdLldISIjatGlzzbZ/9uxZVapU6bL7+/j4XNN6yoqSjtuKFSv08ssva9SoUVqwYIG9vX379nrwwQfVoUMHPfTQQ/rhhx8UEhLyd5UsSfrzzz9VsWLFa7LtvLw85ebmysPD45psH38PLtPgmioIJsePH3doT0pK0j333CM/Pz95enra/2orsHPnTtlsNi1durTQNteuXSubzaaPP/7Y3vbjjz/qoYcekr+/vzw8PNSoUSPNnz/fYVzBqf4VK1boqaeeUo0aNeTj46O777670Cns2rVra8iQIYX23bFjR3Xs2NGhLSsrSzExMQoNDZW7u7tuvvlmPf744zpz5swlj09iYqLuvfde1axZU56enqpXr55GjBihkydPOvR79tlnZbPZtGfPHj344IPy9fVVQECAhg0bpszMzEL1PPLII6pWrZoqV66sbt266eDBg5es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zZs3l7u7+1Wpu3bt2tq1a5dD28GDB3XgwAGHgNGzZ0/NmDFD1apVczr0FPwP9eJfQG+88UYpq74QAGfOnKl3331X48aNs7cvX7681NssyrWo/Vrp0KGDVq1apbVr1zrcyLty5coSxzVo0EBPP/20EhIStGPHjsvaV3HHveCpkZ49e+rFF1/UsWPHdP/99zv5Tkr21FNP6cEHH1RMTIzDo73ShZt4x40bJ3d3d40ePdreXrt2bb3//vvKzs62z+WpU6f0zTff2G8ulWT/IMO/3uD9559/6u2333aqxuLOePXs2VNr1qxR3bp1+TyiGxRhBNdU1apVNWnSJE2YMEHLly/XgAED9MYbb6h79+7q2rWrhgwZoptvvlm//vqr9u3bpx07duj999+3j3dxcdGgQYM0Z84c+fj4qE+fPvL19XXYx6uvvqo777xT7dq106hRo1S7dm2dPn1ahw4d0ieffKINGzY4XffAgQM1YMAAjR49Wn379lVaWppmzpyp6tWrO/R7/PHHlZCQoPbt22v8+PFq3ry58vPzdeTIEa1fv15PPPGEWrduXeQ+GjZsqLp162rixIkyxsjPz0+ffPKJEhMTna63QGRkpNq3b68JEybozJkzCg8P19dff+30L40jR44UutdGkqpXr666detek9qvlcGDB+uVV17RgAEDNG3aNNWrV09r1661P1VS8ITKrl27NGbMGP3jH/9Q/fr15e7urg0bNmjXrl2aOHHiJffj7u6u2bNn648//tBtt91mf5qme/fuuvPOOyVJd9xxh/75z39q6NChSkpKUvv27eXl5aX09HR99dVXatasmUaNGlWq9/nAAw9o+/btmjVrlg4fPqxhw4YpICBABw4c0CuvvKL9+/dr6dKlDh8cN3DgQL3xxhsaMGCAHnnkEZ06dUozZ850CCKS1KNHD82ZM0cPPfSQ/vnPf+rUqVOaNWuW05/t0axZM23atEmffPKJgoKC5O3trbCwMD3//PNKTExU27ZtNW7cOIWFhencuXM6fPiw1qxZo0WLFln2gXv4m1h7/yzKi4KnaS5+qsSYC09HhISEmPr165vc3FxjjDE7d+40999/v/H39zdubm4mMDDQ3HXXXWbRokWFxh88eND+NEdiYmKR+09NTTXDhg0zN998s3FzczPVq1c3bdu2NdOmTbP3KXgi4/333y80Vn95qsKYC0+HzJw509SpU8d4enqa8PBws2HDhiKfPvjjjz/M008/bcLCwoy7u7vx9fU1zZo1M+PHjzcZGRklHre9e/eaLl26GG9vb1O1alXzj3/8wxw5cqTQky8FT6T88ssvDuMLjntqaqq97ffffzfDhg0zVapUMZUqVTJdunQx+/fvvypP0/Tv3/+q1W7MhScvevToUaj94uNc3NM0f30y5OL9/dWRI0dMnz59TOXKlY23t7fp27evWbNmjcOTP8ePHzdDhgwxDRs2NF5eXqZy5cqmefPm5pVXXrH/3BanoJZdu3aZjh07mooVKxo/Pz8zatQo88cffxTqv2zZMvuTLRUrVjR169Y1gwYNMklJSQ7HoEmTJiXutyirV6823bt3N35+fsZmsxlJxt/f32zbtq3I/m+++aZp1KiR8fT0NI0bNzbvvfdekU/TLFu2zISFhRkPDw9Tp04dExsba5YuXVro56+4OTXGmJSUFHPHHXeYSpUqGUkOc/zLL7+YcePGmdDQUOPm5mb8/PxMq1atzFNPPWU/hgU/ny+//LLTxwXXN5sxF31iDQDcAGbMmKGnn35aR44cueK/uocMGaJ///vf+uOPP65SdVfP888/r6lTp2r+/PkOl2iA6wmXaQCUe6+//rqkC5fGzp8/rw0bNmjevHkaMGBAuT/9P2XKFKWnp2vMmDHy8vJyuOEYuF4QRgCUe5UqVdIrr7yiw4cPKzs7WyEhIXryySf19NNPW13a32LhwoUOT6EB1xsu0wAAAEvxCawAAMBShBEAAGApwggAALBUmbiBNT8/Xz///LO8vb35GGAAAMoIY4xOnz6tGjVq2D9gsChlIoz8/PPPpfpyJwAAYL2jR4+W+Bh9mQgjBd+WefTo0UIfUwwAAK5PWVlZCg4OvvS3Xv9N9VyRgkszPj4+hBEAAMqYS91iwQ2sAADAUoQRAABgKcIIAACwVJm4Z+RyGGOUm5urvLw8q0vBJbi4uMjV1ZXHtAEAkspJGMnJyVF6errOnj1rdSm4TJUqVVJQUJDc3d2tLgUAYLEyH0by8/OVmpoqFxcX1ahRQ+7u7vzFfR0zxignJ0e//PKLUlNTVb9+/RI/CAcAUP6V+TCSk5Oj/Px8BQcHq1KlSlaXg8tQsWJFubm5KS0tTTk5OfL09LS6JACAhcrNn6T8dV22MF8AgAL8RgAAAJYijAAAAEuV+XtGilN74uq/dX+HX+zxt+4PAIDygjMjFhoyZIhsNptsNptcXV0VEhKiUaNG6bfffrO6NAAA/jaEEYt169ZN6enpOnz4sJYsWaJPPvlEo0ePtrosAAD+NoQRi3l4eCgwMFA1a9ZUZGSk+vXrp/Xr19tfj4uLU6NGjeTp6amGDRtqwYIF9tciIiI0ceJEh+398ssvcnNz08aNGyVdePR5woQJuvnmm+Xl5aXWrVtr06ZN9v7x8fGqUqWKPvvsMzVq1EiVK1e2B6QCHTt21OOPP+6wn969e2vIkCH29UvtBwCA4pTbe0bKop9++knr1q2Tm5ubJOlf//qXpk6dqtdff10tW7ZUcnKyHnnkEXl5eWnw4MHq37+/Xn75ZcXGxto/6O29995TQECAOnToIEkaOnSoDh8+rJUrV6pGjRr68MMP1a1bN+3evVv169eXJJ09e1azZs3S22+/rQoVKmjAgAGKiYnRu+++e9m1X85+AKAkf/e9flcb9w6WHmdGLPbpp5+qcuXKqlixourWrau9e/fqySeflCS98MILmj17tvr06aPQ0FD16dNH48eP1xtvvCFJ6tevn37++Wd99dVX9u0tX75cDz30kCpUqKD//ve/WrFihd5//321a9dOdevWVUxMjO68807FxcXZx5w/f16LFi1SeHi4br31Vo0ZM0ZffPHFZb+Hy90PAABF4cyIxTp16qSFCxfq7NmzWrJkiQ4ePKixY8fql19+0dGjRzV8+HA98sgj9v65ubny9fWVJFWvXl1dunTRu+++q3bt2ik1NVVbt27VwoULJUk7duyQMUYNGjRw2Gd2draqVatmX69UqZLq1q1rXw8KCtKJEycu+z1c7n4AACgKYcRiXl5eqlevniRp3rx56tSpk5577jmNGTNG0oVLNa1bt3YY4+LiYv/v/v3767HHHtNrr72m5cuXq0mTJmrRooWkC9/b4+Liou3btzuMkaTKlSvb/7vgslABm80mY4x9vUKFCg7r0oWzKQUudz8AABSFMHKdmTp1qrp3765Ro0bp5ptv1k8//aT+/fsX2793794aMWKE1q1bp+XLl2vgwIH211q2bKm8vDydOHFC7dq1K3VN1atXd7ihNS8vTz/88IM6dep0VfcDALgxEUauMx07dlSTJk00Y8YMPfvssxo3bpx8fHzUvXt3ZWdnKykpSb/99puio6Ml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jh07KigoyL6899579j7p6ek6cuSIfT00NFRr1qzRpk2bdMstt+iFF17QvHnzeKwXAABIcvKekYIbT0sSHx9fqK1Dhw7asWOHM7sCAAA3CL6bBgAAWIowAgAALEUYAQAAliKMAAAASxFGAACApQgjAADAUoQRAABgKcIIAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGApwggAALAUYQQAAFiKMAIAACxFGAEAAJYijAAAAEsRRgAAgKUIIwAAwFKEEQAAYCnCCAAAsBRhBAAAWIowAgAALEUYAQAAliKMAAAASxFGAACApQgjAADAUoQRAABgKcIIAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClnA4jW7ZsUa9evVSjRg3ZbDZ99NFHJfbftGmTbDZboWX//v2lrRkAAJQjrs4OOHPmjFq0aKGhQ4eqb9++lz3uwIED8vHxsa9Xr17d2V0DAIByyOkw0r17d3Xv3t3pHfn7+6tKlSpOjwMAAOXb33bPSMuWLRUUFKTOnTtr48aNJfbNzs5WVlaWwwIAAMqnax5GgoKCtHjxYiUkJOiDDz5QWFiYOnfurC1bthQ7JjY2Vr6+vvYlODj4WpcJAAAs4vRlGmeFhYUpLCzMvh4REaGjR49q1qxZat++fZFjJk2apOjoaPt6VlYWgQQAgHLKkkd727Rpox9//LHY1z08POTj4+OwAACA8smSMJKcnKygoCArdg0AAK4zTl+m+eOPP3To0CH7empqqlJSUuTn56eQkBBNmjRJx44d01tvvSVJmjt3rmrXrq0mTZooJydH77zzjhISEpSQkHD13gUAACiznA4jSUlJ6tSpk3294N6OwYMHKz4+Xunp6Tpy5Ij99ZycHMXExOjYsWOqWLGimjRpotWrVysqKuoqlA8AAMo6p8NIx44dZYwp9vX4+HiH9QkTJmjChAlOFwYAAG4MfDcNAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGApwggAALAUYQQAAFiKMAIAACxFGAEAAJYijAAAAEsRRgAAgKUIIwAAwFKEEQAAYCnCCAAAsBRhBAAAWIowAgAALEUYAQAAliKMAAAASxFGAACApQgjAADAUoQRAABgKcIIAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGApwggAALAUYQQAAFiKMAIAACxFGAEAAJZyOoxs2bJFvXr1Uo0aNWSz2fTRRx9dcszmzZvVqlUreXp6qk6dOlq0aFFpagUAAOWQ02HkzJkzatGihV5//fXL6p+amqqoqCi1a9dOycnJmjx5ssaNG6eEhASniwUAAOWPq7MDunfvru7du192/0WLFikkJERz586VJDVq1EhJSUmaNWuW+vbt6+zuAQBAOXPN7xnZunWrIiMjHdq6du2qpKQknT9/vsgx2dnZysrKclgAAED5dM3DSEZGhgICAhzaAgIClJubq5MnTxY5JjY2Vr6+vvYlODj4WpcJAAAs8rc8TWOz2RzWjTFFtheYNGmSMjMz7cvRo0eveY0AAMAaTt8z4qzAwEBlZGQ4tJ04cUKurq6qVq1akWM8PDzk4eFxrUsDAADXgWt+ZiQiIkKJiYkObevXr1d4eLjc3Nyu9e4BAMB1zukw8scffyglJUUpKSmSLjy6m5KSoiNHjki6cIll0KBB9v4jR45UWlqaoqOjtW/fPi1btkxLly5VTEzM1XkHAACgTHP6Mk1SUpI6depkX4+OjpYkDR48WPHx8UpPT7cHE0kKDQ3VmjVrNH78eM2fP181atTQvHnzeKwXAABIKkUY6dixo/0G1KLEx8cXauvQoYN27Njh7K4AAMANgO+mAQAAliKMAAAASxFGAACApQgjAADAUoQRAABgKcIIAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGApwggAALAUYQQAAFiKMAIAACxFGAEAAJYijAAAAEsRRgAAgKUIIwAAwFKEEQAAYCnCCAAAsBRhBAAAWIowAgAALEUYAQAAliKMAAAASxFGAACApQgjAADAUoQRAABgKcIIAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGCpUoWRBQsWKDQ0VJ6enmrVqpW+/PLLYvtu2rRJNput0LJ///5SFw0AAMoPp8PIe++9p8cff1xPPfWUkpOT1a5dO3Xv3l1HjhwpcdyBAweUnp5uX+rXr1/qogEAQPnhdBiZM2eOhg8frocffliNGjXS3LlzFRwcrIULF5Y4zt/fX4GBgfbFxcWl1EUDAIDyw6kwkpOTo+3btysyMtKhPTIyUt98802JY1u2bKmgoCB17txZGzduLLFvdna2srKyHBYAAFA+ORVGTp48qby8PAUEBDi0BwQEKCMjo8gxQUFBWrx4sRISEvTBBx8oLCxMnTt31pYtW4rdT2xsrHx9fe1LcHCwM2UCAIAyxLU0g2w2m8O6MaZQW4GwsDCFhYXZ1yMiInT06FHNmjVL7du3L3LMpEmTFB0dbV/PysoikAAAUE45dWbkpptukouLS6GzICdOnCh0tqQkbdq00Y8//ljs6x4eHvLx8XFYAABA+eRUGHF3d1erVq2UmJjo0J6YmKi2bdte9naSk5MVFBTkzK4BAEA55fRlmujoaA0cOFDh4eGKiIjQ4sWLdeTIEY0cOVLShUssx44d01tvvSVJmjt3rmrXrq0mTZooJydH77zzjhISEpSQkHB13wkAACiTnA4j/fr106lTp/T8888rPT1dTZs21Zo1a1SrVi1JUnp6usNnjuTk5CgmJkbHjh1TxYoV1aRJE61evVpRUVFX710AAIAyq1Q3sI4ePVqjR48u8rX4+HiH9QkTJmjChAml2Q0AALgB8N00AADAUoQRAABgKcIIAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGApwggAALAUYQQAAFiKMAIAACxVqm/tBQAAF3nW1+oKSu/ZTEt3z5kRAABgKcIIAACwFGEEAABYijACAAAsRRgBAACWIowAAABLEUYAAIClCCMAAMBShBEAAGApPoEVAP5OZflTOiXLP6kT5RNnRgAAgKUIIwAAwFKEEQAAYCnCCAAAsBQ3sALXq7J8oyM3OQJwAmdGAACApQgjAADAUoQRAABgKcIIAACwFGEEAABYiqdpyjqeuAAAlHGcGQEAAJYqVRhZsGCBQkND5enpqVatWunLL78ssf/mzZvVqlUreXp6qk6dOlq0aFGpigUAAOWP02Hkvffe0+OPP66nnnpKycnJateunbp3764jR44U2T81NVVRUVFq166dkpOTNXnyZI0bN04JCQlXXDwAACj7nA4jc+bM0fDhw/Xwww+rUaNGmjt3roKDg7Vw4cIi+y9atEghISGaO3euGjVqpIcffljDhg3TrFmzrrh4AABQ9jl1A2tOTo62b9+uiRMnOrRHRkbqm2++KXLM1q1bFRkZ6dDWtWtXLV26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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "\n",
    "plt.bar(bars1_x, revenue_by_quarter, width=w, label=labels[0])\n",
    "plt.bar(bars2_x, earnings_by_quarter, width=w, label=labels[1])\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = ['Revenue', 'Earnings']\n",
    "\n",
    "plt.legend(['Revenue', 'Earnings'])\n",
    "plt.title('Revenue and Earnings per Quarter')\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "plt.show()\n",
    "\n",
    "plt.savefig('NetRev.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Both revenue and earnings follow a postivly increasing trend with approximately 5% of yearly revenue constituting earnings.'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Both revenue and earnings follow a postivly increasing trend with approximately 5% of yearly revenue constituting earnings.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "# ax1 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "ax1 = plt.subplot(1, 2, 1)\n",
    "plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])\n",
    "ax1.set_title('Netflix')\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Stock Price')\n",
    "\n",
    "\n",
    "\n",
    "# Right plot Dow Jones\n",
    "# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "ax2 = plt.subplot(1, 2, 2)\n",
    "plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])\n",
    "ax2.set_title('Dow Jones')\n",
    "plt.subplots_adjust(wspace=.5)\n",
    "plt.show()\n",
    "\n",
    "plt.savefig('NetDow.png')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
