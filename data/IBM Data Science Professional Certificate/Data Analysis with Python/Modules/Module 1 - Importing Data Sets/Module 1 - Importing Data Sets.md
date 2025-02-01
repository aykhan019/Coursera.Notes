

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CUVCAWV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSA3EP%2FJyaRT1Xv1xekzU24T0gFaRLljIalnVSsqM2AwIgMKPAzEW1JWIbui3ct6%2FvriPcHSqpBg5OxzWUtaFykQ8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPa%2BfXYVOOMSikwErSrcAy77hfBagV%2FIHSr8k0NbycG1sv1crFRIZRCg0SladsnSGeNrSGskQLI4s8qDFr0jHYTW4MiVcE1p270W5xr6d8IQRJv4nVmvV8XLX0L2WQy6%2Boyzz7AexWfD9SbiMhqCK8d76vvbJplgMe22LeWgcS85NvwDz%2BaydpB8qo9fgMpTPM16DvoOb%2BOZktGcmdEJKtktovgDRDrJBozSnmA6XRbfQEL%2FL64LW5HSUESnc6a9fMfHRN%2Fbl3pfrXm%2F04EglI1zXvm3rNl6%2BH3%2Fr2uOe0A7dBzY08xMa9b5IU%2FgIgEkX%2BZ5mF1PcAuF%2B%2Bad9y4j2l402McO7UPcxar8QJHAAG9VXL0EjYiNfDxb2P5cEvg5LA1ygKRr%2Bp29LPd51hqiiZOoRK9dGHR7W0Ualn4f9WG8tDwGxz%2BYeZRL7cP%2FytwO1x4A3fOn5x5ZoN9YddoNE1hkHA31WvWYyyihRtpH26RxkyI9%2FdgcdP%2Bg2QPdQqf3mk8R3QceNvsb4eLYFa8L3KcYTnUpTqcJzcnYyN4UDnMg3tBLlDpXIi%2FqUs9zF1Uz8Eh%2F%2BvcnCAYcSW83AxmFZcK%2BAAykYsNuTHUPxPc2o0YJwa2tQP3ihekQHxD2e%2FfXXiH0nI7eB1Uzs5gTMJHF%2BLwGOqUBBkXb2%2FVxtroNSUuuZL1sMPYBgfrjWmv9D6bRQW9sdDAwKK%2F5WqmbX%2FhR%2FFATLD29lpT77ZvSJPRP1o59PLpeCweLKXzs7qTXnuvxsZhDIagkDwQ8TOcrRFwuHTzA7rkMOFGHoxO5RdOjvyZ9q25Lwx4OmhscHTG4ncrMci4VEskYMR8MLJccZSpB3qOx9UixClA4Ie7oyIb7cto9aH1bPEjrQ7ZM&X-Amz-Signature=565982dce0507b0d7648b754cbe79db94c624daef953f56176516cd2e08151ec&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WETCSU22%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETKswLnnEpsf9tLifVitFN%2BP2X7bYFYbV8Ka7HVxRZoAiAsaDQPMeM2dfdRXsmrniSqWr9665qY9Xb8MawgCE13HyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp4kIpYbCprkMnHL4KtwDqB5G7d23Ft4ibT9BHZ%2Bjduv1v4dmsOhov8ny9g5tg94CRa%2BO55rN5FoMd%2BscqMp7YT1fWpkYnk3It2wiiup9DhH6XHR9jT9swC7OH9XlnTZ9MCMLqWYlI%2Fr2D9pXwyp9aslJqKcV4jfCoK1wuhg14Nrm6BINmxHet2W73Cp2aa6higxxi9Y0VZpBoWmpLupHhDLKFoxUMdUH%2F9zs3GGsnLVvDnFqz6SX29FU3msRjQ43ukDJL5nsDEpFpWHCOW%2BXTziOxkSKcyXXl14YlQt%2FFIo5YMB6DX88XSQ4Z2RvN1%2BiBeH5lnCoiACnap0W2DIvC3LlFiMO%2FPeDn5iQ9OE9MxCfdqoF2Rrp60V6lDxb8QxQ0RGcIxiLCrwj7YxpzTKPu84JkxMQSlig7TwqdyOZH8eERjz9FKdFkjfALncitpFo5XECMAEAuRhqbcKZuNH09mIj6Y4iNEIFfZZ7JL5uL4BOi%2Fqkb3PPZIslhx8Hm%2FPlmg2h%2BFvegaHcnZthy9qj8aa3QELO%2FzS047ht0dsB%2Fob4XqXo67sxVPLk%2Fs4g8gOThn8mloTI9%2FbpYdYYPLCs9yTUUu7bawHM3jZmV8KKUlpeMW8I%2Bs4d9xS%2B33hp%2FW8HUlqWiDhpYPEV0CYw%2B8n4vAY6pgHXeMBXPyNQnXYS1n%2B7m8svQPVaFFR0wftsBJlIF046oytKHroUN9fniJTJlSH3VclOl6qPiCZTUqttG5IhUcK3BsnTXJxMy3n%2BXUE%2FJ74MLSmkPUcTWvm0A7zClYfz8MxAoscTWO5nzy4LzscqUvtcpiVI%2FHsDmevNgksV%2FPC6hUahd8l4mKO%2F7tYCPLuZZB76Q9bvz4NUE2uemWk651MhbdepgIZP&X-Amz-Signature=26dbabb1a151995224f3bbfd4006ec6101d09e790f15c77ba6c4aec3c254d9c0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WETCSU22%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETKswLnnEpsf9tLifVitFN%2BP2X7bYFYbV8Ka7HVxRZoAiAsaDQPMeM2dfdRXsmrniSqWr9665qY9Xb8MawgCE13HyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMp4kIpYbCprkMnHL4KtwDqB5G7d23Ft4ibT9BHZ%2Bjduv1v4dmsOhov8ny9g5tg94CRa%2BO55rN5FoMd%2BscqMp7YT1fWpkYnk3It2wiiup9DhH6XHR9jT9swC7OH9XlnTZ9MCMLqWYlI%2Fr2D9pXwyp9aslJqKcV4jfCoK1wuhg14Nrm6BINmxHet2W73Cp2aa6higxxi9Y0VZpBoWmpLupHhDLKFoxUMdUH%2F9zs3GGsnLVvDnFqz6SX29FU3msRjQ43ukDJL5nsDEpFpWHCOW%2BXTziOxkSKcyXXl14YlQt%2FFIo5YMB6DX88XSQ4Z2RvN1%2BiBeH5lnCoiACnap0W2DIvC3LlFiMO%2FPeDn5iQ9OE9MxCfdqoF2Rrp60V6lDxb8QxQ0RGcIxiLCrwj7YxpzTKPu84JkxMQSlig7TwqdyOZH8eERjz9FKdFkjfALncitpFo5XECMAEAuRhqbcKZuNH09mIj6Y4iNEIFfZZ7JL5uL4BOi%2Fqkb3PPZIslhx8Hm%2FPlmg2h%2BFvegaHcnZthy9qj8aa3QELO%2FzS047ht0dsB%2Fob4XqXo67sxVPLk%2Fs4g8gOThn8mloTI9%2FbpYdYYPLCs9yTUUu7bawHM3jZmV8KKUlpeMW8I%2Bs4d9xS%2B33hp%2FW8HUlqWiDhpYPEV0CYw%2B8n4vAY6pgHXeMBXPyNQnXYS1n%2B7m8svQPVaFFR0wftsBJlIF046oytKHroUN9fniJTJlSH3VclOl6qPiCZTUqttG5IhUcK3BsnTXJxMy3n%2BXUE%2FJ74MLSmkPUcTWvm0A7zClYfz8MxAoscTWO5nzy4LzscqUvtcpiVI%2FHsDmevNgksV%2FPC6hUahd8l4mKO%2F7tYCPLuZZB76Q9bvz4NUE2uemWk651MhbdepgIZP&X-Amz-Signature=5e9cb41435bdb34be8ede31cd7b5382adb562f19737ac90ef2c96f87034afa4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
