

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWQNH72R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDhNE0wqpE%2BRuxsxBc8tJNqlhBh%2FYlqkRYiGqWf6fJegIgEgjkkuSbCJHSmubsvcDwHsQ3tdcYTfR7WH2qyXypPiIqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI81lltt6ntK1mLarCrcA3Pdxd5CzbwtmsBBRsVK%2F00n6lEod86%2BajiLwA1XPS3%2FcN1aqDI804Veta%2Fhszez9KwPIVdFfeXL0O3XdXeoh5REEKdyPz9kZagWNTI61UcwlDTfTYNhzqF3h6wQAv13RT6JS%2BrVYQfCsquqNH2Xmes0UPo6vAQh91TTcoa7dgm8gNGXx9scNxCMN6vTiUmCqtJNEI13HipvENHeMR43hrohyfHns6bWY%2BiQh%2BcUuhcRiUZkpcrrvd%2BDTKRQjacsgv5dT9vVgA6puN7XyKKZjJAYXlWHkxtJVXDQG2kDAz7B%2Bnazc8LI6GNPKidkWcCTeUiVxCsgdjSdFDPiIcrQMvSV%2FHfNf6vkigdpc3J7O2%2Fel6vley3Zw6SY%2FET10jQl2vyi8IRScYuyI8DI5YqlZM1EzAG6ernjspjwCv8cCZAKDAP2oAy51P%2Bd3QQ3s1teMKVM3uqatHRUpnuKk45rkZVxWevlI%2Fbi4C9jLOHj3hkKGvML5t%2B9EHIOBMUkXfByhxST2iGAemBL7IOhhwLnZPy4KH8lBnyoiqkGhXGCGc9J%2B3f1rr5DHfVJxszjcaZaekWbxlXcXd2iyM9Gn8Hh4sWAAtuwnU7%2BvQ9dbN9DzDI1lfVtY1ZhxDoHfgzcMNPn6LwGOqUBK%2FGv4TElvcZZDKVz1W6prwvb5XRKC7F7%2FzKX6sWluX5CAqZPbHm%2B3xz6qpdcxnWnrIH70dxi3jXBZ%2BrY0KWo8MWEmTuhUzGL2%2Fa%2Fi57pJxQa5Ae9n0c1U8N5k%2FAZevBNs5kEOQTC9QoK4GkS4cugxwZlHZQJbKdlCguQHj0zV4HfypDf5wS9EJkjbQWppCVDnYbXfOw0e%2BHnRtRrpyOJ%2FV9HSoDX&X-Amz-Signature=53d93c7b9439cf8126c7255f8d0f86bb58f28365cdc85393d2f36e3f931c8796&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAFAGIVW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNc7i4mGInU26vHDd6FCM4FEdIu78UaD8hQDPY9IdnVQIgbNjAoqAECSDIspDfRdr6nIycvk76n15ojMDNBoFX%2BSYqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL6SFp864Y30H2J6kSrcA1zGgwf%2BYBmSe5ML%2Fh8wM455V29%2FoVSujXIzivFd%2BZENrcrA78B3OTreD0bR5e%2B9C99JkPYSoeAPveiojk0g%2FcDzFyZLeChu%2B2rFg3bBwcN%2FZuOPn6O0eRERaUFak6LKoBso%2FoNWLGh04yDQfrO9MM1lTCIzQ%2Fsbb6UKOdI5sx7Q9kuC84138E26zo3uQvVqKyHyQf0vG5tj5vwMnhSTVdPoSBKifmD6huniAmSSyHiLDS1MEPqw93XbSjuiljZ40ZUAgxKMov2z2tS47CE5wVkTY34ggTmYL5GYlLa2nYvEJ2xokBfz1ghXuXAaCIUd3F12uPwGxwTevjK2tpvEGoUKJ7rBCo2d5j7MDf3olENm1Qy5HeKvWsWoTqLChQwERwwy%2FnbutWLK4lxptBME5%2BIAYzfIdUrjFg2Irpodx363S9ibgCx5RSWFqKke8OpFGs%2FXaQ7FKmvygFR3HFF1CHn4k6BkNxs7fYMh8WT%2BAmLLRYKAwgcVRI7D6kJVsUYiNfpNOcQSdW9Hdc2KRPL8cZyAK4Ppao9OPAdeb8gOxHoq1vgtzRyAVB4KId6RylgVO2iJ0o37Mj2AcplVql8bcbKjG9lSbT9AQsGyhKJhZQRVPxNoyElKbyQS8GpaMPTm6LwGOqUBnhUfKFv2pywFivn9tGNnnHH5MHChe61cihP6ic2ukcDRn04Jaz7Swes58pJLpcTPZOz3DQ5CT9%2F6%2FqWlO4fYZMKEJpiSoQ%2BiHLDWGeU8tsloWsL8xTBotNrF9MqQSvN2ciVsQMcYlzeQaQOt9kCSglYT7aWU5SZTAwJ6VsMd7fXVloERTUzgCTzDmSa3hucr5xCmmrzXOEKpGHLe7cn8xXb1LGf%2B&X-Amz-Signature=5c9d610902df5612935a858fad8b1ef995a03c79c5fca46d630511f332a83dde&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAFAGIVW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNc7i4mGInU26vHDd6FCM4FEdIu78UaD8hQDPY9IdnVQIgbNjAoqAECSDIspDfRdr6nIycvk76n15ojMDNBoFX%2BSYqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL6SFp864Y30H2J6kSrcA1zGgwf%2BYBmSe5ML%2Fh8wM455V29%2FoVSujXIzivFd%2BZENrcrA78B3OTreD0bR5e%2B9C99JkPYSoeAPveiojk0g%2FcDzFyZLeChu%2B2rFg3bBwcN%2FZuOPn6O0eRERaUFak6LKoBso%2FoNWLGh04yDQfrO9MM1lTCIzQ%2Fsbb6UKOdI5sx7Q9kuC84138E26zo3uQvVqKyHyQf0vG5tj5vwMnhSTVdPoSBKifmD6huniAmSSyHiLDS1MEPqw93XbSjuiljZ40ZUAgxKMov2z2tS47CE5wVkTY34ggTmYL5GYlLa2nYvEJ2xokBfz1ghXuXAaCIUd3F12uPwGxwTevjK2tpvEGoUKJ7rBCo2d5j7MDf3olENm1Qy5HeKvWsWoTqLChQwERwwy%2FnbutWLK4lxptBME5%2BIAYzfIdUrjFg2Irpodx363S9ibgCx5RSWFqKke8OpFGs%2FXaQ7FKmvygFR3HFF1CHn4k6BkNxs7fYMh8WT%2BAmLLRYKAwgcVRI7D6kJVsUYiNfpNOcQSdW9Hdc2KRPL8cZyAK4Ppao9OPAdeb8gOxHoq1vgtzRyAVB4KId6RylgVO2iJ0o37Mj2AcplVql8bcbKjG9lSbT9AQsGyhKJhZQRVPxNoyElKbyQS8GpaMPTm6LwGOqUBnhUfKFv2pywFivn9tGNnnHH5MHChe61cihP6ic2ukcDRn04Jaz7Swes58pJLpcTPZOz3DQ5CT9%2F6%2FqWlO4fYZMKEJpiSoQ%2BiHLDWGeU8tsloWsL8xTBotNrF9MqQSvN2ciVsQMcYlzeQaQOt9kCSglYT7aWU5SZTAwJ6VsMd7fXVloERTUzgCTzDmSa3hucr5xCmmrzXOEKpGHLe7cn8xXb1LGf%2B&X-Amz-Signature=8d24c08ed9f5b44820f3de370ada5e1e5cf0d71d438353d997346cae55c27e47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
