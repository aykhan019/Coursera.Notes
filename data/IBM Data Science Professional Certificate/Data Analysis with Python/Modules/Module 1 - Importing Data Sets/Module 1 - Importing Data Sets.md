

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ4PE7TI%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIAdMTpeiF21bRSruyFZbgYEbZ4wJSlqA%2BBgnxvIVjHhZAiEAg2A5YGkixLD1AAp%2Bk%2FuZNnLBK81tkIwfQmJ8RFwO4QQq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDBvl%2FxU9OybH8u7bgircAy7FbB38AOozV2IWzYCwSIQb%2B8CTeh3GdcSJx9I2flovA9AmXELk1Op9Xvvg7VpGI2wvfavU%2FO9A9EgiJIWPYyAkTM86VnKECH%2FjN2AVx44tBFHaEHkkXKV3onaqeGt5tVb43kW%2Brg3ovHKdVFxZI8gIIU5IPO9voFXuXw4pG%2FU0xSfMV8B6GYHXXiOmgyPDsXtO0XRGns4%2BHXWejZfhBrMbU5EcVWYR%2FKPFjEsS3Gg5UaE0oBtws1TysC947SFaf3DD7nrWOYr9%2BtCXFTLYBE4s3mWtvj65e2To5AQ%2B2FPcs6WglFOKFjs7Lz1v3TSKxlnKVktwJWBeXaTg9mUMkbnZmp292o4wQijJ4bqlxd3ZlUIQxbQh1xiwJkupw8cLpCmGImz5i4HNLQePW6fr%2Fh4zdoLkr5GxHcxwqppAf7QsOf0kJ32SSCEbO9fVKlbUqCkYivzvTuXqo3oUM88ed2x19MIQVbIWKdS0WAkjUzImd3MYfysqQFXiY4z5WyYkPfpcRyoxDKufldsvXOQKhHfn20zesy08xFh7Aa7asr1YmuKJVDC46GvvFpvKttq%2FLSn0Dgd5jqnsp2QYDrlayZvnlw8t%2BuwBY6T%2FncYgA%2FPXZPGHRZuDnNHsndg4MOnkxL0GOqUBv9KEh2hnENATdt3K9%2Ff4cuEN%2FFjjIkmq5fEYxcGXDhdl5joAyUWenywmk18UKnA1Kva4SuTOH42lwZkx2NmExjwm9b5ZSHZx7orVh5TnIhx6c18oJqy72k%2BKTEIfHqfPULZHOca29kj2IbGuX79%2Fm2ggw5dLkAsQRkXEZJpuEZ6oGo4roZprZ9ZGW2bYoNobCBgCWnl5G%2F%2Fjc5%2Bq%2FRD9yRu6%2B5mV&X-Amz-Signature=14008dc6f49889e51b00ebf74093a7a6a4b44f1c70b0a86797ab169440fb0387&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W453XEP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIGwxHquiuaBNnC3bwULQPrIe3TUZEP%2BVVyOFG%2B5PFC4iAiEAzANWk2d9MlWUi6gEBLDq0nmP%2BTndYxtBQsDmYrIFjfwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL%2Bf3fBqnXi2aYrIHSrcA6sHnGACu5eYHHktFLBN%2F1duJhSi1Ubm7wDBPA%2F6sy4MWwy7KzRMWVlvNplLvjITGjSNlRb42RiX%2Box2HAxhFmFhySHL5mnBuZnq18Vme6b8wGnVvJOCC4BM65cgLMSh7K58oZMI1%2FBudK%2F0S%2FiiTY3geEWAc%2BtB4zsG%2FMQOnjYi00TA0o4BUHFb%2BRGpKbFFrM7M3kCVEvA4sriK6SdTWMHf2WlVcroJMiXLLI5IJRllhzLsoLRExeX03Jwawc2VREwDXmf9Jg%2FL%2FPpjNFFCBfBIwuvNJPW36absoDtCwr1gOCZNlz6nzJWWrFseloipg6vqkmh3Ra7qrw%2FStxm9f9%2Bflc%2B2iTqiG9RbHfVQ3F1emrjeL7Xrknambx6u0W26tdxKJx9TNTAmq%2BB7ec3XkDz5FqwdMwD9WRMM3xiwsaIY0p%2FYL8gWmoLbdcKiPhMk5nhawcgzPWlQRUpkEpQDkwxd%2BbNplnMHmMz%2B%2BLDEyKyFf%2FhNYF7Zlp0V2uEAONfmjUaxdqRFyuqWVt9%2BypiTzLdTR2%2Bfo4AX9t6qx1OvlYOH2sYEVIlatrgwXmuEbjyRe4b4iR28D6M8g6vCoMj9eEjTXYrWd4rOwzVPl3X7S4ff7se3tmjtpKtYf%2BL9MM7kxL0GOqUB4wfxEeRc6RQBmN2QGAFEf%2BvhHSp8OcXpwSW47ousrGftGmXyqImxxB1%2F1aNlSNx%2FtBamRZnFWBUxxL%2FcWoMs3oc4ODSrwo5cZV%2BAfXBTDtLZIeQAVDOURgbAvG%2FxC5a%2BjGvuvpC4GYsoMuCn4OuEsnJjrX7t2F7IApLNX3HBlcG94fc9bdKHWh2DRhzrlIz0JkOGEL4niVBMH1RzLFNHPWtVQq4I&X-Amz-Signature=1b3a176d2e9ad30442815f9b6882e6cfe01518af34656e3d01064bdbcf73f8f7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W453XEP%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIGwxHquiuaBNnC3bwULQPrIe3TUZEP%2BVVyOFG%2B5PFC4iAiEAzANWk2d9MlWUi6gEBLDq0nmP%2BTndYxtBQsDmYrIFjfwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL%2Bf3fBqnXi2aYrIHSrcA6sHnGACu5eYHHktFLBN%2F1duJhSi1Ubm7wDBPA%2F6sy4MWwy7KzRMWVlvNplLvjITGjSNlRb42RiX%2Box2HAxhFmFhySHL5mnBuZnq18Vme6b8wGnVvJOCC4BM65cgLMSh7K58oZMI1%2FBudK%2F0S%2FiiTY3geEWAc%2BtB4zsG%2FMQOnjYi00TA0o4BUHFb%2BRGpKbFFrM7M3kCVEvA4sriK6SdTWMHf2WlVcroJMiXLLI5IJRllhzLsoLRExeX03Jwawc2VREwDXmf9Jg%2FL%2FPpjNFFCBfBIwuvNJPW36absoDtCwr1gOCZNlz6nzJWWrFseloipg6vqkmh3Ra7qrw%2FStxm9f9%2Bflc%2B2iTqiG9RbHfVQ3F1emrjeL7Xrknambx6u0W26tdxKJx9TNTAmq%2BB7ec3XkDz5FqwdMwD9WRMM3xiwsaIY0p%2FYL8gWmoLbdcKiPhMk5nhawcgzPWlQRUpkEpQDkwxd%2BbNplnMHmMz%2B%2BLDEyKyFf%2FhNYF7Zlp0V2uEAONfmjUaxdqRFyuqWVt9%2BypiTzLdTR2%2Bfo4AX9t6qx1OvlYOH2sYEVIlatrgwXmuEbjyRe4b4iR28D6M8g6vCoMj9eEjTXYrWd4rOwzVPl3X7S4ff7se3tmjtpKtYf%2BL9MM7kxL0GOqUB4wfxEeRc6RQBmN2QGAFEf%2BvhHSp8OcXpwSW47ousrGftGmXyqImxxB1%2F1aNlSNx%2FtBamRZnFWBUxxL%2FcWoMs3oc4ODSrwo5cZV%2BAfXBTDtLZIeQAVDOURgbAvG%2FxC5a%2BjGvuvpC4GYsoMuCn4OuEsnJjrX7t2F7IApLNX3HBlcG94fc9bdKHWh2DRhzrlIz0JkOGEL4niVBMH1RzLFNHPWtVQq4I&X-Amz-Signature=c831d2723d422b379239d3e4108aa32789d40239cc7d320560e7ad5b8ddfb052&X-Amz-SignedHeaders=host&x-id=GetObject)
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
