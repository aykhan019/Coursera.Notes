

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN32TPXL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEKChWvYu0np8QP6oXMaslbrBTn5C0JDAx8noGxlpR%2BCAiArU%2Fa63XuPYZZ1PaAssYARlcJmon%2FX3KxVDfawh1scSir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMfuVjc1vH86tgMv7%2BKtwDiUA7%2FQ49dHfuKuKn1A1ZWtsi%2BlBnVrh2zzsoTCvkPQe4Pxw0ZG%2BgXxAVwNtYhoN8SBIWG7jTiiIUprVcR%2Bmv7qEoF5z%2BwNxXUtWTp8xtm1wDl3S9dgNZfR5ls5msBPVTm419UsvdTzjwd1UWhuC0ssLqLk8wm%2BHjDMWVxRVooHxJYZGViS7MQ%2F6u4EunafvzLvwMeih9erImETRh%2Bk9ZHUl60219Bh%2BXhgIYRLo%2BAQ5lkW7EDrKNP1mAscM7eYXqrCuXkUCjJraLl3wKb4OlmdHO%2FGxCoXH5aVmdbusgANTQCoqvm%2FuQA2zlR9cFGX%2FP3VDNm1F2pLdVEKBom%2FroslcK3myDd7u5LpJkFkHp3Q239P1YlUUWmUsEjLm0H%2FAqtb6VxKpDXvjD7vIpuznFzSLK1eqdqS5WyGxbdZ%2FlCU4brCkN47Q8GQxEyrV0JSMpNIK3Cet0WUBiVC2IAO4l%2FhUjVog%2FvbiwYhia4qN3Y0YsqE6yN8%2F7gRWv%2BrT0RSeqH%2F0N%2F%2FUDaPofgZ1dARDGeissD6NOkoCB%2BOt3iUGthgGEjd8NTgYnVOEnxAQT5t0IlLP8Gyd%2Fv%2BzJXo5q6opqAUQc5q3jy3RuH8nBRSOxIcYPL1nGKugEDl9HjGAw09yWvQY6pgEFymnHEdP5LsrYUptbSTos3FDTmDUuQ%2FSn3vz7wWM7CfvM%2Ff3heN9jfE5uo1SX%2B%2BSlABZB754SYHsaKLDg6uWcwXCjQaYs3Pr2eZTCvbShIYH93MXAkftFDSp0GvcQ1%2B1y2W%2BbQgD2OaSA4AbKTG%2BuGHhRgdreKYK6NqMqzbdXgEc3yQQ0To9CObpn9pVkbrGhZHEqIguG4J3vHiOclCM29cIaa9Qh&X-Amz-Signature=609b54a64c61913475ed2228df72a4aad8c0198d250b70656f63db53cecfe508&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAXAP7TL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCL4Gl2v3YsW%2BRP3k6HjtCibRrYuzwUGpb5GmWOX%2B22BQIgPhbLhVKVTfKBkvOAoi1nVR2vugyURN0v6PsnRHXYx5sq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDCm%2BeEXVf7tn%2FRMo9ircA2n6xgFj62TBHxsaImjlnXA3Ai0EUP2rQk2AUdMzSvXxcjuLLkAWZUGM8K0i905ho8j4n7jG7qPSIe81p39pckB62bzZ50GX2LJV8%2BIXO%2FYjXs%2F5ZakGqvQRHl%2FKzDGTVzOxEY3Hv4HYxvZxWn7ldNy3y18iLpv8wo%2FIb8duHRC4r84gWKOcYDX8a45L5oe%2BFFhVMfO4fdjnHK5l4nIx8zf%2F%2FmpXak27m5GuzIZHzsFmK6YeBqJewYFClCo%2BBPPBCGllfYQZ6ULRwRF4sqYuUa5HNV4zQO%2BYXGg7pvJkqAR7ciYLw9cuaQkaRhz%2FvXgzjKf%2Bl6Mrwe%2B85ARop0GPXg4AnSgnAk1lo4C%2BjWY0s0137kc9mqc5SCl%2BabqEHXXdzLBh5RGdflDPqnwmkIEUOVLBnm5%2BVwtgFln%2B5aKVCQHYQfQopyoLD0%2FVbrUlRQ%2FUmGMvpJeml1lSFP%2Ft9S0To6Ign5jRLI8vkrreScqVd9m%2FvELG2VOxS6utgq1Q6hzYNM5q0BQLg1AgCGw9i%2FHObrgWrwH1vms4StBveJAXbxx5lfET36kDyxsc8kIZs5ZUJKE4QudfRFlsme%2B7NCY5Hxrz2WcLykmmTtCSk%2FqE1Mujv6%2B9XcMtRnZQiUlaMP3dlr0GOqUB4RMMydjCb2ifpug1IDqGisbISm3wh6hEFZIFygMTgBCgM8hXZHXTN2ju5MXkKBBevDZ%2FvJCHhdAqV12aiMl5CAsJ5GaKV3md1VhBFfNrXyKRZU%2By1oyoDZljwU%2FJwjqyi4aiCrZ365j1gtdZ7Flz0dqRAFlW4KdiDuj0oIhZFKQGyPx7vvC%2FKIf1UuegpFunOsk%2FrgJ42BjMqWLewKs%2BUE9ov%2B8F&X-Amz-Signature=c803412c331862fa2737c5ad86ee263afc94df77f4fd977f677977972dfb687d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAXAP7TL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCL4Gl2v3YsW%2BRP3k6HjtCibRrYuzwUGpb5GmWOX%2B22BQIgPhbLhVKVTfKBkvOAoi1nVR2vugyURN0v6PsnRHXYx5sq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDCm%2BeEXVf7tn%2FRMo9ircA2n6xgFj62TBHxsaImjlnXA3Ai0EUP2rQk2AUdMzSvXxcjuLLkAWZUGM8K0i905ho8j4n7jG7qPSIe81p39pckB62bzZ50GX2LJV8%2BIXO%2FYjXs%2F5ZakGqvQRHl%2FKzDGTVzOxEY3Hv4HYxvZxWn7ldNy3y18iLpv8wo%2FIb8duHRC4r84gWKOcYDX8a45L5oe%2BFFhVMfO4fdjnHK5l4nIx8zf%2F%2FmpXak27m5GuzIZHzsFmK6YeBqJewYFClCo%2BBPPBCGllfYQZ6ULRwRF4sqYuUa5HNV4zQO%2BYXGg7pvJkqAR7ciYLw9cuaQkaRhz%2FvXgzjKf%2Bl6Mrwe%2B85ARop0GPXg4AnSgnAk1lo4C%2BjWY0s0137kc9mqc5SCl%2BabqEHXXdzLBh5RGdflDPqnwmkIEUOVLBnm5%2BVwtgFln%2B5aKVCQHYQfQopyoLD0%2FVbrUlRQ%2FUmGMvpJeml1lSFP%2Ft9S0To6Ign5jRLI8vkrreScqVd9m%2FvELG2VOxS6utgq1Q6hzYNM5q0BQLg1AgCGw9i%2FHObrgWrwH1vms4StBveJAXbxx5lfET36kDyxsc8kIZs5ZUJKE4QudfRFlsme%2B7NCY5Hxrz2WcLykmmTtCSk%2FqE1Mujv6%2B9XcMtRnZQiUlaMP3dlr0GOqUB4RMMydjCb2ifpug1IDqGisbISm3wh6hEFZIFygMTgBCgM8hXZHXTN2ju5MXkKBBevDZ%2FvJCHhdAqV12aiMl5CAsJ5GaKV3md1VhBFfNrXyKRZU%2By1oyoDZljwU%2FJwjqyi4aiCrZ365j1gtdZ7Flz0dqRAFlW4KdiDuj0oIhZFKQGyPx7vvC%2FKIf1UuegpFunOsk%2FrgJ42BjMqWLewKs%2BUE9ov%2B8F&X-Amz-Signature=6ca35340696c014476d1de8fa987bf24c787fae1bb3c86f2f253729dc39f5283&X-Amz-SignedHeaders=host&x-id=GetObject)
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
