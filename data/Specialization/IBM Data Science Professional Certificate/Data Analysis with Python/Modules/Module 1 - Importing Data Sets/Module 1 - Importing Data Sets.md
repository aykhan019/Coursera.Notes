

# Module 1: Importing Data Sets
## Data Science with Python - Key Libraries
Python libraries are collections of functions and methods that allow performing various actions without writing extensive code. They offer built-in modules for different functionalities, providing a broad range of facilities.
#### Categories of Python Data Analysis Libraries:
1. **Scientific Computing Libraries**
2. **Data Visualization Libraries**
3. **Algorithmic Libraries**

___
### Scientific Computing Libraries
#### 1. **Pandas**
- **Description:** Offers data structures and tools for effective data manipulation and analysis.
- **Primary Instrument:** DataFrame (a two-dimensional table with column and row labels).
- **Features:** Fast access to structured data, easy indexing functionality.
#### 2. **NumPy**
- **Description:** Uses arrays for inputs and outputs, can be extended to objects for matrices.
- **Features:** Fast array processing with minor coding changes.
#### 3. **SciPy**
- **Description:** Includes functions for advanced math problems and data visualization.
- **Features:** Solves complex mathematical problems.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HAGCUPQ%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCSjFQ0IS5kpjotYj%2BDhXdk4lgYx6Pv2C4wlVgjUXL%2B7AIgYK0JxTlFgEd%2BKhdX6u%2B1lD8nXSnKJDbPrtLmxH1qyloq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDPZH5OMT3U0HQYyPgCrcA1F%2Bt%2Be%2FoDUtmkBpaBx8ie3VM1HlCSSjaDav2jD5RCt2k5Cwl%2BPdlunaeOB05KmwYDqEQxOfw38Bs2OnbCdEtXKmQkpornyhAaehzV3Mi902diOjhipYHY%2BGckar6pZdD2CT331YOgbe%2BD6BPhrCmlhDAo6mOwkUyI0ZQceDT2IV8YK7gW%2BZ2ttXCLjrgH4IXkLHWxIWYrET3HHX8OkAHTtPS0tcJZohpXNJLu0oCL%2FchcLuw3oazmnYQtA%2BRET2OTgE%2BKDvAdEOQrLhjQXgggmaS%2BlFMElyqB1dHCExuQ8CDRVL2caMTkRdtRsQ5tIGzqMtGkVtQgUrzTvqY9BxfhZlLxRBysa0ExtiJibufXfe5%2BR0oeKDE%2FEU2ymBReThgDuJSxEliG4PIph44uCMGIN1%2F5S6p8JX%2BvXPGwqcmqh7WFM1TFYh0kx%2FFKbI4hD50%2FpVGGNHlp2QyVy4e71DAJkAhWFgzgUkCigRJa7o2tFTGc0y6%2B2UdubVi21ms18P4Dg%2F2Hs7eSsaLRusUqEehFehaYQCf7uktoIt81WT9tzZUwAsdM5rDAkqYzipFCFQTu56mAa6182n18vNYH%2FnIdK3Rb1WZi6SkU5SUZuErvDkOpYYT4Kach9CrGv4MMiU5bwGOqUB4VVP58VMtwKaypQi2wZbfK5cZdV5th%2FGzxx1n9xFbnPGMfyHNX3El%2Bdwur3IMU1QVgI7gAQ7qj9f1g9Db46iz58s%2Bg8EwL8vQWL34szs7K4tok0umqL1EqVewR1dJM2pFs5gnVrfV8YLfCYn%2BNpt02ys2vxMMhknWO%2F8fL2NpOsD%2BkwJd6v%2Fxujd71Ni%2FL%2F%2FWM8MNs23ey7EmzgpjGMRo5UDqDWj&X-Amz-Signature=70410c2f333d6fe27d703db0fa5cca41404c774a65b9c1023f31dd39c80673f6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRQ7LJAG%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDFIKrVg0%2FQUiRPwijD%2BCs8G0JTa%2BMNsXfPrDVG%2FPfduAIgRGQ9PPa6k67uAs2W%2FnhVQPV6oYNUu2yDle0BXLvAD7Qq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEquwf6JSeyp0IF8NSrcAy65bUAEY0mOTqkSpfq7%2B11It2adK9AZlfzFRxK51PThLww3%2BtgzirmK1YtRDneF6cUR6PCWV4vfDjpiOcKi4eJaYMbFlEH8AkRBvHGbat7RmBC8rGp80I%2FNWstsjTlhsefP1kOZm6NM46zg65XR%2BItCsPXmu7nCg55ahs2Hxm576gBFxl4%2BWjPfgtvM66eJKxm5HOOcgf2DmXYN8O4MN29ZJ5AAyRMLVXjLYPfZo0W3EG1EbPrdtS%2BS0bHdkxgJlDr%2FfkGNaa0W7qg9JrduxN1gEWp8PnfQ6oV0vQ1Tzj2hIa6stWf4D03%2Feu9Siiw9S%2FpGiDpTp0S3znkA2xrgbuKabCSLbhpj2kIuKTsCOOdDP8xh%2FYyIeP%2ForFwplqBdtHzge%2BV6QihCZy5rCCF2q2Pbvq9C4sLhYbihS6hdQjtwOAC2%2FtPvDSA%2FM9Uoj2zgE7Vrn8Y3PRTQws8pa1LLmnnxNsQiGqpQtzh9tEIdwvT6LGm6CXNdkMscPBjzZJ0Kp%2B2xcv4CguZPiK8zWaD4zuhj%2BuHSl527KZwZyInbfMfJluvvyLj%2FiryxcYs6dWR0NiVlazWipD323y%2Bbp3uDT9%2FpjltBexEIgxtxEqbvQ80qyJzVhciCGoIouTSYMOqU5bwGOqUBVLBXclNX5ZCFWfHjuLPipuTmE13YRAGErsGU89H41HWKwxKT0R1uX0A7CYiIL1grYlaAWjIIVEbaHmlJWbhTGR7hjVLzfAvxCMbZRaNregOrUze82qK9opz%2FWv5tQD6D1gjGKKU4cIx101%2Bpwt68dKoh2fwOQy8J9b0sjdy1i5vHL10TIrYThj9uEjSLyBRyxOJp8jbIPqXhfiNMDli9yh4dmoFQ&X-Amz-Signature=715321304d9559dbe8c5765bcff77ca0fbd1348e841e7104f4bb39ff8117515e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRQ7LJAG%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDFIKrVg0%2FQUiRPwijD%2BCs8G0JTa%2BMNsXfPrDVG%2FPfduAIgRGQ9PPa6k67uAs2W%2FnhVQPV6oYNUu2yDle0BXLvAD7Qq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEquwf6JSeyp0IF8NSrcAy65bUAEY0mOTqkSpfq7%2B11It2adK9AZlfzFRxK51PThLww3%2BtgzirmK1YtRDneF6cUR6PCWV4vfDjpiOcKi4eJaYMbFlEH8AkRBvHGbat7RmBC8rGp80I%2FNWstsjTlhsefP1kOZm6NM46zg65XR%2BItCsPXmu7nCg55ahs2Hxm576gBFxl4%2BWjPfgtvM66eJKxm5HOOcgf2DmXYN8O4MN29ZJ5AAyRMLVXjLYPfZo0W3EG1EbPrdtS%2BS0bHdkxgJlDr%2FfkGNaa0W7qg9JrduxN1gEWp8PnfQ6oV0vQ1Tzj2hIa6stWf4D03%2Feu9Siiw9S%2FpGiDpTp0S3znkA2xrgbuKabCSLbhpj2kIuKTsCOOdDP8xh%2FYyIeP%2ForFwplqBdtHzge%2BV6QihCZy5rCCF2q2Pbvq9C4sLhYbihS6hdQjtwOAC2%2FtPvDSA%2FM9Uoj2zgE7Vrn8Y3PRTQws8pa1LLmnnxNsQiGqpQtzh9tEIdwvT6LGm6CXNdkMscPBjzZJ0Kp%2B2xcv4CguZPiK8zWaD4zuhj%2BuHSl527KZwZyInbfMfJluvvyLj%2FiryxcYs6dWR0NiVlazWipD323y%2Bbp3uDT9%2FpjltBexEIgxtxEqbvQ80qyJzVhciCGoIouTSYMOqU5bwGOqUBVLBXclNX5ZCFWfHjuLPipuTmE13YRAGErsGU89H41HWKwxKT0R1uX0A7CYiIL1grYlaAWjIIVEbaHmlJWbhTGR7hjVLzfAvxCMbZRaNregOrUze82qK9opz%2FWv5tQD6D1gjGKKU4cIx101%2Bpwt68dKoh2fwOQy8J9b0sjdy1i5vHL10TIrYThj9uEjSLyBRyxOJp8jbIPqXhfiNMDli9yh4dmoFQ&X-Amz-Signature=3f37cf6d81138bc613d40f70a106bc9c26c18c46b45c9e416d43bb965c818623&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Reading Data with Pandas
Data acquisition is the process of loading and reading data into a notebook from various sources. Using Python’s Pandas package, we can efficiently read and manipulate data.
#### Key Factors:
4. **Format:** The way data is encoded (e.g., CSV, JSON, XLSX, HDF).
5. **File Path:** The location of the data, either on the local computer or online.
### Steps to Read Data with Pandas
#### 1. **Import Pandas**
```python
import pandas as pd
```
#### 2. **Define File Path**
Specify the location of the data file.
```python
file_path = 'path_to_your_file.csv'
```
#### 3. **Read CSV File**
Use the `read_csv` method to load data into a DataFrame.
```python
df = pd.read_csv(file_path)
```
#### Special Case: No Headers in CSV
If the data file does not contain headers, set `header` to `None`.
```python
df = pd.read_csv(file_path, header=None)
```
#### 4. **Inspect the DataFrame**
Use `df.head()` to view the first few rows of the DataFrame.
```python
print(df.head())
```
Use `df.tail()` to view the last few rows.
```python
print(df.tail())
```
#### 5. **Assign Column Names**
If the column names are available separately, assign them to the DataFrame.
Verify by using `df.head()` again.
```python
print(df.head())
```
#### 6. **Export DataFrame to CSV**
To save the DataFrame as a new CSV file, use the `to_csv` method.
```python
df.to_csv('output_file.csv', index=False)
```
### Additional Formats
Pandas supports importing and exporting of various data formats. The syntax for reading and saving different data formats is similar to `read_csv` and `to_csv`.
___
## Exploring and Understanding Data with Pandas
Exploring a dataset is crucial for data scientists to understand its structure, data types, and statistical distributions. Pandas provides several methods for these tasks.
#### Data Types in Pandas
Pandas stores data in various types:
- **object**: String or mixed types
- **float**: Numeric with decimals
- **int**: Numeric without decimals
- **datetime**: Date and time
#### Checking Data Types
Use `dtypes` to view data types of each column:
```python
print(df.dtypes)
```
#### Statistical Summary
Use `describe` to get statistical summary:
```python
print(df.describe())
```
- **Count**: Number of non-null values
- **Mean**: Average value
- **std**: Standard deviation
- **min/max**: Minimum and maximum values
- **25%/50%/75%**: Quartiles
**Output Example:**
```plain text
              0            1            2            3
count  205.000000  205.000000  205.000000  205.000000
mean    13.071707   25.317073  198.313659    3.256098
std      6.153123   26.021249   90.145293    1.125947
min      5.000000    4.000000   68.000000    2.000000
25%      9.000000    8.000000  113.000000    2.000000
50%     12.000000   19.000000  151.000000    3.000000
75%     16.000000   37.000000  248.000000    4.000000
max     35.000000  148.000000  540.000000    8.000000
```
To include all columns:
```python
print(df.describe(include='all'))
```
**Output Example:**
```r
              0           1          2          3       ...      25       26       27
count   205.000000  205.000000  205.000000  205.000000  ...     205      205      205
unique        NaN         NaN         NaN         NaN   ...     25       25       25
top           NaN         NaN         NaN         NaN   ...     value    value    value
freq          NaN         NaN         NaN         NaN   ...     10       10       10
mean     13.071707   25.317073  198.313659    3.256098  ...     NaN      NaN      NaN
std       6.153123   26.021249   90.145293    1.125947  ...     NaN      NaN      NaN
min       5.000000    4.000000   68.000000    2.000000  ...     NaN      NaN      NaN
25%       9.000000    8.000000  113.000000    2.000000  ...     NaN      NaN      NaN
50%      12.000000   19.000000  151.000000    3.000000  ...     NaN      NaN      NaN
75%      16.000000   37.000000  248.000000    4.000000  ...     NaN      NaN      NaN
max      35.000000  148.000000  540.000000    8.000000  ...     NaN      NaN      NaN
```
For object columns, it shows additional statistics like the number of unique values, the most frequent value (top), and its frequency (freq).
#### DataFrame Info
Use `info` for a concise summary:
```python
df.info()
```
- Shows index, data types, non-null counts, and memory usage.
**Output Example:**
```less
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 205 entries, 0 to 204
Data columns (total 11 columns):
 #   Column  Non-Null Count  Dtype
