

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L3YYXI7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC9eokTNjqWloClyDT9yYabqkuzaiuDvgHGg8hYkEmoMAiEAiZ6OgGzuYGnUuUxWAMfu9glMuMCSz9R7s%2Fm3OqiPOwUqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHeam2riFPibS1YNdyrcA5mVaSUNSdBrF5pnwXdD7SDkIzwYequx1wn%2F%2BriIF0oFY4m6Xx4ecjcem8gQJo%2B0fUtts1Szkfm1Vxv%2BDCjVvGCpJ7UKIN8aSCiOahfLnD1COZ5%2FHewN9lw8AwiTbxj6dGEWbUUlBhtlT8sJE4uxMA3DUXqvryGtz9yey%2B7Ofq37aDjFPQ2RZV8GozuskG9woK6LM%2B6enOcKPmYa2lsZd6rnUzsaZRnGG4mM%2Fp4p9%2BGezHrCccYzIKtBRCtGDgR8lxbOwCZ2HOr1HZkTao9RbntK3s9D%2BIxWV4I4MB1QJQ%2B8qGLd6JYldDZxpi0BfsSRK1YliPQ79jL5diWGeXkk2lStZifKBVwFrgHKKT9Y2DGrWa53H5zK8NZ1Abje%2FjttWgwTE5jBG77qbe262mrPGY3%2BIaHbskyKlKALLi3oj5dyl4yeAH9Co2R6LpWB%2FRhlxuqIDD1w8ZwLzwitMKaTsPA9ziZLmhqGseh%2Fg%2FjhREnML96HW2OuTWCwHahi70tzljxUrb%2BN8n1Zb1dmjZEfH18xDzH2wvqt21QNd5yFIythJcb2FfqFreWXK9qbT%2BbgTiqyQcOJydKXFNqZOsHHCNXhDHdJldMEYMLsohQy6SkkHrT%2FLr99tZ3TiXzWMNj2%2BbwGOqUBldCrsnc5EW37lR4AKzeHLFGB8pjgx37jbFr17KV1DDjgfa21pXEIizqPVmAhDnrVPt%2FUpWZwUHW35oGnRzgP9UN%2BpNSSdzKTK5CyO1oRnSpSQjiZnQyI9Z2aDCQ1gp20qJ%2BdJJszkhDMZ%2BW51KJsVHt9G92HsPK2q8U5Ghjfrh71RIaGFAgRN7XKfUQDotgkrFg5xQt0bZ3kAWwnzU5cIjopDlcd&X-Amz-Signature=2c9cd255baa98eec9c4008337da576f14a8b2f8725214fb2d49810a04300606f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QN55ESV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDg7RXkUMqCLLeztzPpKxP3HHHbP2ccz7bcP78YxLOUAiEA8CHXOP5VTqdQzFy6t3sSfr1nji2AnlNpvu%2BptjjuFXIqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJLZvajIZdZiq1KkdyrcA5%2BXbhQXbpL%2BUrAeAjd%2Bk0YlYIvRp5dTaXNYkY8eU%2FBXtPZYm21JyTe4bAFpFgOmcQggI4iJyPxxNZO6YDd81x4wm6mcU6JCNT0u9XSmOXu%2BLG1XFETeJcW5mWbJbwbZd8NUdolzAtr78FfEyxeeGWMzj9diL7HAqoC6%2B8CbU%2F0Z%2BaglYmoWt4xHJIWrXBIO4OhTcv0xpO3VqPygmrBfgNg7zXS51z%2FUxc4maV3t9zntFXKMt8zWrxZM6FSS2L0YKkP5igdWJ%2BZwW5kE2p4MjKk3pFbZqOQNRPUPmoNpqKXJerKAGzywQn8%2BP5NTQbhwM%2F0PRW0Ic%2FPcqhbz25XIsqlIIfrMnEr87W%2FR1h6JWEsI3C5CvzXjpVmIlu48RSr2Z95%2BAkN2QV3IpFdxB6PwfXk%2BPRrMltnWXufboGonBnPNzQRKvPkmetN2OrFrBogiDNGn0pM2jxRBJ6ciSC4GInYGRrEZAd0uDUjo3F3foCqH6vnv0uazELHI9mmwwmyNbnyJV4X8ba%2B1Oipy%2BZZdCbmnEe0YGnbcPbFNBKnbHSv9njmYgMkajMkKvqA%2FbgMQXM9nvhrnpwNa0DGfTWRo8zB%2BLMPp%2FQC7qqqbqw5LfYceguNOwOIT8bXMJdGvMK32%2BbwGOqUB9aVt1InL0eeem7AJ%2FeiEfDwm8zzG%2Bmgo%2F%2BhyEQyZdS3rIKl9nIDEyvj10Aii1UgXWRBrPA4UNfdMYiHAxs3Eq8mcLLol9PZPgHQh%2BDn8ZK0wMCjhCyg91KcQB9n5qieSQvTJZDrGcu%2B87Qlts40OjlzcrLfk4zz7OrWb0zIT8hji8COkTUEZqFH10f%2FsIGlycusfNHcX33%2FTTY03JpdIktIfLDhP&X-Amz-Signature=3cd864c786765754d13f458688104fdc375e3c5298a139f9fe40b0ab08808c86&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QN55ESV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDg7RXkUMqCLLeztzPpKxP3HHHbP2ccz7bcP78YxLOUAiEA8CHXOP5VTqdQzFy6t3sSfr1nji2AnlNpvu%2BptjjuFXIqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJLZvajIZdZiq1KkdyrcA5%2BXbhQXbpL%2BUrAeAjd%2Bk0YlYIvRp5dTaXNYkY8eU%2FBXtPZYm21JyTe4bAFpFgOmcQggI4iJyPxxNZO6YDd81x4wm6mcU6JCNT0u9XSmOXu%2BLG1XFETeJcW5mWbJbwbZd8NUdolzAtr78FfEyxeeGWMzj9diL7HAqoC6%2B8CbU%2F0Z%2BaglYmoWt4xHJIWrXBIO4OhTcv0xpO3VqPygmrBfgNg7zXS51z%2FUxc4maV3t9zntFXKMt8zWrxZM6FSS2L0YKkP5igdWJ%2BZwW5kE2p4MjKk3pFbZqOQNRPUPmoNpqKXJerKAGzywQn8%2BP5NTQbhwM%2F0PRW0Ic%2FPcqhbz25XIsqlIIfrMnEr87W%2FR1h6JWEsI3C5CvzXjpVmIlu48RSr2Z95%2BAkN2QV3IpFdxB6PwfXk%2BPRrMltnWXufboGonBnPNzQRKvPkmetN2OrFrBogiDNGn0pM2jxRBJ6ciSC4GInYGRrEZAd0uDUjo3F3foCqH6vnv0uazELHI9mmwwmyNbnyJV4X8ba%2B1Oipy%2BZZdCbmnEe0YGnbcPbFNBKnbHSv9njmYgMkajMkKvqA%2FbgMQXM9nvhrnpwNa0DGfTWRo8zB%2BLMPp%2FQC7qqqbqw5LfYceguNOwOIT8bXMJdGvMK32%2BbwGOqUB9aVt1InL0eeem7AJ%2FeiEfDwm8zzG%2Bmgo%2F%2BhyEQyZdS3rIKl9nIDEyvj10Aii1UgXWRBrPA4UNfdMYiHAxs3Eq8mcLLol9PZPgHQh%2BDn8ZK0wMCjhCyg91KcQB9n5qieSQvTJZDrGcu%2B87Qlts40OjlzcrLfk4zz7OrWb0zIT8hji8COkTUEZqFH10f%2FsIGlycusfNHcX33%2FTTY03JpdIktIfLDhP&X-Amz-Signature=22d1ddb0c9dee657dd2b9352b5b8b797488ba3f446b32f8da1260ba15e8c96ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
