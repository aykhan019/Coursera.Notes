

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OVI2DQN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQD7lOnqm2E2SI05i2ZwoX0HlrTDiPXs85MUtVH2%2FdBQIhALJ05b3%2BGre7wBlMSt8HiNtfeAVEesZ%2BN9DfkzaqtEDyKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxyjdfb2XUfFLWBxXwq3APIzKXjyqFPhjbL1YVDAdTg4V3Zo5gCT5Tky67q5y506FrS0Vf%2Bw%2F2Qwo9m5SKd6Jh3BmohGsdpfofqFaXh1ro29UquoHAThxz2nSQCZ7Z7zpTDkfbAe7kH90EJuMPXCJwAGRuPHp8AH2W3t5kGdsrbtP9pltH2kKMbzftml7i2D621XhsEMmCXybeEpy7hA%2BHhX46eCsoVHvjyBtorHTtslGW7ZjngBSCrAdlXStbRZHhLxlyeF3XU5ov4LMzQqzSIbBj%2BHjC27HyI8d7TSnC0ehK69WwVT%2Bs1OHda7WXllKq4lqajrDMtY3sOvzLuGaVaRKo9s6BwIZRmjPwkGOgfQ5Bj55vpMICIdtfotXbo%2B1O7zJk3YKy8J9DveUt7ispUEiQSlIpIjS7ysVHzS4XRi0nxPfYB%2BzhhxWwfdbQAOY2kwrDF7FlW9LZKZcf6TEZWloya%2F9ixh1hJGRyRnSVIUlHE5n9gxzKfam7gvc40lh9%2FrLkfRvGKtnBtrlOQW71C4sqLX8x5r6QZxk3vXv8mgHmpUxQ2dO1VhRM%2FXVru5paGx9KW%2ByIwZPjVC5PF%2FlsNIlUtMU%2FTjyV3ycAGhWyO0PgwlbB0Uqpc3lw%2B9Lk8c2qsuB5Dtr%2BGXaSftzCCw%2Fi8BjqkAWysm1wIU%2FNSSDJ4MCWfJtrHhEM7DAdyMQJMQfN0%2BXENQUhngqtlyr0KT3Lx87VxVTNSwoNrLjhL6YwqDAvOYn783mK8ECriuzJoOMf4kET3rxHzLXn0jzbLeB3wjVRwmW4wmav%2F%2Fcp69iw1ddRlv6mznzOqy12Q4XgrSejQQFEEolgmYVdUUaPjbDqa0Jizpq7kmpFgqfmIXNAVyvxofPc7bz6S&X-Amz-Signature=e6897259418233d62f16198763cd085e2a50615909710160a59d9886975f96b6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCJOYGTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAcM%2FM1uddkqT2v5gqSydtz6WVlgUbQ1LK36hyiXDtOnAiAnJt8ag982Vw5zQcaz%2BNhES3Zjq0XTaHUbN65ItZFthCqIBAjY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPU0WIr5DgbRODLsEKtwDX%2Bp%2FZ%2BIlyCkhW3XyThpRz6P6FSmL6jNYmElFWhpLS4L0wsqk7Mu7b3CWBQNVSh%2B%2BABn51VHyGdWftXovDzNaqExMNE%2B7iEYt6995m%2BW5OWEz47nfwVlV2W4etww%2BnwIr%2BjRPRLKsxlceyU4o%2BPnfVaAGYIf%2Bk4icVRGE190C%2Bxgmbo6%2FVhvNfKXkDAuNvh%2FzcecdFmLpaKWf90d4OXuJq5%2BBz7Gke6QTrQ4UQF7bt6uzMBYOrNvfE7aQrf9RBZ0ZtoEtpvpftmKHm%2FPvOSPV3xxdvmFYAU1wJVSLTWq7dmBMT%2FfEZHLxFYopf3HAifseffncUpmYOV5wzvNMl%2BXy9KJC0xQgEtv8fFxH9Ab%2F22dwvOiStXl%2B7jW2iGDfxwiQBDGjlOScQJPrcenieToVBIpx5HOGrE2X3aN8iwvAKO3Ve%2Fs2Jqfc%2Bov5meSHZpY%2FgjA6KX2TMTPYuusRah8MeaUIILbsSdA0UJ4BaI8zxnMIOrN%2FlbkRzD19eylZK3PeCHA%2FCTgy5hgN5Pq8B2llituJyv%2BrYE2gOQkVEL%2FNRNdJLQ13koL%2F%2BI%2Bfxw4srN%2F0dbTF6IDsK2cq9J%2BCUskbolwk%2BIDFB%2B9aHXr9BOjnVUo3qDHkVA0%2F1Lk3Fjwwz%2Bn4vAY6pgEarF8aHmkFMSVfiiRSI2xpCYKDN%2BiIV%2BpQJlld64vdGMn5PbQQrZGBzjCVtPxFBtnPQAcBaOX0aXAtXm0FPwtGaYgtZ%2BXfmNHRnfmS%2BfS8iT%2BiFBzCsJR4WwhtWRaVedLmvaHKR4fGDd2djcew1n9e3bu6OqjYFiDiDiZl6o7E3G5BApQUegxwh60KTQcfdzOCmNpOGgv%2FM1i8s829sLEU%2FCndQdt1&X-Amz-Signature=2af9f577060f46f3a6250c28d4c6d60ca2f253951482cc01b9db49d46ddd61bd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCJOYGTC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAcM%2FM1uddkqT2v5gqSydtz6WVlgUbQ1LK36hyiXDtOnAiAnJt8ag982Vw5zQcaz%2BNhES3Zjq0XTaHUbN65ItZFthCqIBAjY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPU0WIr5DgbRODLsEKtwDX%2Bp%2FZ%2BIlyCkhW3XyThpRz6P6FSmL6jNYmElFWhpLS4L0wsqk7Mu7b3CWBQNVSh%2B%2BABn51VHyGdWftXovDzNaqExMNE%2B7iEYt6995m%2BW5OWEz47nfwVlV2W4etww%2BnwIr%2BjRPRLKsxlceyU4o%2BPnfVaAGYIf%2Bk4icVRGE190C%2Bxgmbo6%2FVhvNfKXkDAuNvh%2FzcecdFmLpaKWf90d4OXuJq5%2BBz7Gke6QTrQ4UQF7bt6uzMBYOrNvfE7aQrf9RBZ0ZtoEtpvpftmKHm%2FPvOSPV3xxdvmFYAU1wJVSLTWq7dmBMT%2FfEZHLxFYopf3HAifseffncUpmYOV5wzvNMl%2BXy9KJC0xQgEtv8fFxH9Ab%2F22dwvOiStXl%2B7jW2iGDfxwiQBDGjlOScQJPrcenieToVBIpx5HOGrE2X3aN8iwvAKO3Ve%2Fs2Jqfc%2Bov5meSHZpY%2FgjA6KX2TMTPYuusRah8MeaUIILbsSdA0UJ4BaI8zxnMIOrN%2FlbkRzD19eylZK3PeCHA%2FCTgy5hgN5Pq8B2llituJyv%2BrYE2gOQkVEL%2FNRNdJLQ13koL%2F%2BI%2Bfxw4srN%2F0dbTF6IDsK2cq9J%2BCUskbolwk%2BIDFB%2B9aHXr9BOjnVUo3qDHkVA0%2F1Lk3Fjwwz%2Bn4vAY6pgEarF8aHmkFMSVfiiRSI2xpCYKDN%2BiIV%2BpQJlld64vdGMn5PbQQrZGBzjCVtPxFBtnPQAcBaOX0aXAtXm0FPwtGaYgtZ%2BXfmNHRnfmS%2BfS8iT%2BiFBzCsJR4WwhtWRaVedLmvaHKR4fGDd2djcew1n9e3bu6OqjYFiDiDiZl6o7E3G5BApQUegxwh60KTQcfdzOCmNpOGgv%2FM1i8s829sLEU%2FCndQdt1&X-Amz-Signature=8375cecf3f109ff192c5061713ab6ce51f3b736946e6aee0c226761beb86916f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
