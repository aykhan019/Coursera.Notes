

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NPVQ3MN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2FF0OJs5eleyhzB0ZR9We3isIDpwPN64dien9VbCePlAiEAyU6TrNEZQhqJQtzAGa4J%2BybATlEko2X6OBInMrIRgKIqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1cU8pHhjUmh3dswyrcAwGf3uvzT5%2FOa%2BSmGVEFovMZILlqXsKs1WR474laZs7mvGHUqj%2FQxVOxW0m5RgQryEegQjR1nU6%2FsgrtpRwO0o05d6WIjIoEN3wNqJsPcV%2B%2BLQO4Ag0SRO8XIm%2B%2FVndZfN9LtmdmnrmYSUO%2BLA%2FAifhGTG5uJMFBxtcUDXwBZUiUFwNAYIcaHIkougObFeQR5OmR3U39WozopQsrfRW8HLhbBNfCTUXVw3FYj1aVwzM9eb8xYWf5WDMB1Ym2oLrblyEi4JbPNuOS7szlq2sTMZNqObs%2FfOe9l4TqrSWGhaHnBjX1GRUr4rNeTtsNrnrc2WFzNFvuMyRuZvgkJ2Y8ciQzSYnJ90cCglYZTjKC0b3204GLDFnMOFNqb2b%2BLJ5LP8eQdID4h%2Be0ZezyFd2zLYpa7AcSPHliBwUcIymyiF%2FBxD969GhqeLIoDgSUKofLMnS%2Blz84y2iIGTRlIFbsOOz89HuQINihwOX0rTTy4yK12HAlJJwd9mvlSOhrIAeroYfuO7URxZVOnoLJOGnMLCmyy2jMJ%2BMJuvqKoLlLsqKqMf5vXsPLteKSMgkiidqQoEOhAm6ewHCmWTYhE9EKsg1fZX5%2BKFn4MSfpxpKglr6VwHnBdCeCjNVuVV8dMIiL7bwGOqUBM16LZs4DIgs%2BAkV0RdhMfdWQCLvNch67NW2eftvQ3c%2BbU3lFm%2BZ3deYlxExAM3XuYokVUTB%2BkTj%2BnwMtPS3g6F3r2oFZCMzSfBxjZ9lNMwfVmqe%2FNx39UNY%2BxEQs5nFDL8QY0Rpimfm5pJnFxqZycWUsjdDJyszODFxjPwKFAvtaWUq9hmX1ZXfb59hCy3kqedl%2B34XC4FMU4qyR2oLtltZ5N2sS&X-Amz-Signature=9a2fa1607858ad698b20561ae225f7b45bf4abae57df4a9e4acac18eb5efee2c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663APONAT6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjT6l2mIlkP13jY4fN3lJEJ8E02hg%2FBeKYnLhWnCRHiQIgHOZ7uAIZTtmmhP7nd6PSK6sMNr7%2F1u%2F7yYwL%2F%2Byp6HEqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBKqT%2FQveMfEpvW3SyrcA6UFIw8tFQfT5TTlAfWPjytj0nvePBhWaqdhPddQR%2B4cQt%2B%2BVNuu9ttZqC1yMzdnWHm%2BmXSjNxPETFefOxgWJns5hTgtdWyCuyDOl69YgLn13L9IcMSaHaXPb1NmO4WSt9uuMIedyeIAVwUcaXwrfmA6WBk6SZSb7kOk0qSou1MbB7recHiHXkCRe7ab4AieX5be29yMjPFS4z9EFGbsshZjub5Yqwj8RLtGrozAnKT22q9p03tneoiy4ueCu2zOVY0WjtXZ5%2BCPuo549RqkyzAmDKF1xzhT04NYmq03ty5kMcZqlaZpR2NO8rzM8Y3H5DxyRZtkhfepPPueZ6nyX5G40GOkn0K%2BP8Fx%2F2wrlbJqgnSBoMcVpOmJU8LHHS2alDJyVRHz%2BGaXN4a%2FLK6t9MqPzihsukNGh%2FCNO%2F0lldRPwnpCv5L%2B7M5V82074eQ%2FInHRkfxkKgUPUlYE%2FVvQsg4NdScGgpvcqbMUtfPvmTHyo7tPwQhrCuZpcHvjvOCxrRJEgVftOvvjbPPpG33uaB1yeFGLYs0XySyYNGcSkB8jg8mtY0M%2FQ6wMexeqthCRSQ9ei6urU9RK5ceAXO7vZiWvJjNuflNH9riP7INMxi3fB34KM6t843FPViFEMPmK7bwGOqUBIw0jmACfL7LqDlPUCgQJx1L0HUdL%2FaZ%2FM1PeyJgAC3RQjE5%2Bx7yVl890l3KWOj3r1kzkIJpRXXlAr9Ch9oFT42lxlV58mgnEEzKYgr3JLdQqIebLO04AvfNZuqLwF2%2BbwooeIdm0x4XCgmmJm36%2B38km3F6LxsnoFuctgwhSj7CDnDqMvgXXNDy3dMSqmd90Da8Mp8qqC0jBGAQa%2Fayfh%2BsLZAAa&X-Amz-Signature=e93a896d46d485960136afd3c9f5279b693130256350b0e8a643fd4c80c34643&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663APONAT6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjT6l2mIlkP13jY4fN3lJEJ8E02hg%2FBeKYnLhWnCRHiQIgHOZ7uAIZTtmmhP7nd6PSK6sMNr7%2F1u%2F7yYwL%2F%2Byp6HEqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBKqT%2FQveMfEpvW3SyrcA6UFIw8tFQfT5TTlAfWPjytj0nvePBhWaqdhPddQR%2B4cQt%2B%2BVNuu9ttZqC1yMzdnWHm%2BmXSjNxPETFefOxgWJns5hTgtdWyCuyDOl69YgLn13L9IcMSaHaXPb1NmO4WSt9uuMIedyeIAVwUcaXwrfmA6WBk6SZSb7kOk0qSou1MbB7recHiHXkCRe7ab4AieX5be29yMjPFS4z9EFGbsshZjub5Yqwj8RLtGrozAnKT22q9p03tneoiy4ueCu2zOVY0WjtXZ5%2BCPuo549RqkyzAmDKF1xzhT04NYmq03ty5kMcZqlaZpR2NO8rzM8Y3H5DxyRZtkhfepPPueZ6nyX5G40GOkn0K%2BP8Fx%2F2wrlbJqgnSBoMcVpOmJU8LHHS2alDJyVRHz%2BGaXN4a%2FLK6t9MqPzihsukNGh%2FCNO%2F0lldRPwnpCv5L%2B7M5V82074eQ%2FInHRkfxkKgUPUlYE%2FVvQsg4NdScGgpvcqbMUtfPvmTHyo7tPwQhrCuZpcHvjvOCxrRJEgVftOvvjbPPpG33uaB1yeFGLYs0XySyYNGcSkB8jg8mtY0M%2FQ6wMexeqthCRSQ9ei6urU9RK5ceAXO7vZiWvJjNuflNH9riP7INMxi3fB34KM6t843FPViFEMPmK7bwGOqUBIw0jmACfL7LqDlPUCgQJx1L0HUdL%2FaZ%2FM1PeyJgAC3RQjE5%2Bx7yVl890l3KWOj3r1kzkIJpRXXlAr9Ch9oFT42lxlV58mgnEEzKYgr3JLdQqIebLO04AvfNZuqLwF2%2BbwooeIdm0x4XCgmmJm36%2B38km3F6LxsnoFuctgwhSj7CDnDqMvgXXNDy3dMSqmd90Da8Mp8qqC0jBGAQa%2Fayfh%2BsLZAAa&X-Amz-Signature=3bafc6cb16e55a7a92d2ba06d9f073c72fe9d59a2528b7d8cb68801b71bdfb4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
