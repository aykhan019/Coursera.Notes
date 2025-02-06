

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQDSE6V5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDHvAJpnmPYDwN7wHHh75QNv3crswIBM5jlwIzXwr21HgIhAI3aVUHFyeR1vYbJ1Vzc0ahLLBM89d9yTQdj07Td3BWZKv8DCFcQABoMNjM3NDIzMTgzODA1IgwY43dUXtYa1udL5VQq3ANOc%2Fznm1DVic%2FswZ%2B3TjtQimOW%2BqOYinU31orSHS5Efx%2F3ZkX3TKYXsZgcB047liiupPniZg%2BF1KZveQD4dZWKtxMZsyMMeL5Bvdh8eNGfMpKNZVglZG0LkzAoxGeeheXpQHT%2BFZO6Xs%2B2kvhNxIn23DvbqJTl4or2x6%2Bb0zR04%2BxJhiSxQVb1%2BRoNV1%2FoKv1u8%2BqedxDK7BpHFmKnFZrnKi1LE5%2BeZLcRN0sbbpn8bAibI%2FjEo7x%2F2ZEHYuSgSL7Cbpb51fOAswin1yelAeJR6gIgpKgBUj8ydniINX075vDmZnuIF2iB40MqgPIysU7gGTNS0Af7pSuffqb97N2Sal7NPgqYriHQMw%2FbNYG7j64pxvbquZCltV5aRVn6eT0sInJAFVN%2B%2BKKTGJiLJSYr2MrnIcGIh4crVo1fzAq7TToxepySxqYYKRQfidyBjfKHPJ0V%2B04yH74%2Bm0mYAvaVWX%2B8tRUWi0m38nGnbMwLzSjOcx0XTZWvg5GIZnfKAFnND3m%2BehuMkBlQQxNxKfbx2VEhzwRFoD5lRaUugXNffk8oyMaTAAWsWW7DGKr7qCzt0u2dhKHRPuSYT0exhgxCq9FlZjp%2FFBthaE0dJpJRp2sodICacBMEgkOyOjCnmZG9BjqkAXltb1ctGLCSzIRR9%2F%2FIl0A8dQsj6ZksPaf5LSVuDevEygEjgQRHJHRcpkGv68ChSzDO0Qq93qfZndtIVFt0iMyDACrwPTWSK8cBm%2FqpArdjLp8SA7JpB5%2FrKgkmmJaXB4IMp1v6iIX53OUz%2BPW6s1feXPDM%2FX4p2ARRy6zp3nBxrlwp86M20wB3dZvvHCwuJZWMfDaccwnHrpoknlDkLuPrWkLc&X-Amz-Signature=93b46e7f56516c27eb6f5e0438175268cb067824253ce467ca15062fc0f6b88a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDRWPJP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDY3tQTkNVYRJkWXcYypzczYN4C4kBf67OHg0ed5ZbVowIhAL6T7wCFJboRQDkXek52RYX5aean6BbNwxY0k9hARyTrKv8DCFcQABoMNjM3NDIzMTgzODA1IgxrbzNTxuwuovk5sDIq3ANg3Z1Lapn5LbtOycoh3%2BZWgjfTndIaeCZ4Oc9yO60KrgXfLhe4Gl%2FnPDSQnbVnlrUlFroZ%2Fo1B%2FTEyPVHPc1N0dEEoUlSWOFSASEZJr2CfpupbvKzM3N12vkKeB9gnHoVR6T0MGkf5dUDQYSgz1wdWS1TSriUlsS2USX3Cvc%2Bh%2BT8vSkhwpzsD3IYEpSI0S8IAA3NXQekyNh65WisRHAHvindfqvqpBUwskMEvVTc4T6Q%2BNR70mSPJArnXHR6KwtIukUS9%2BSqq1w4bVQmL7oJTcHG19mU2vQ5TacSYWJOqVhqTpil1Y2184gipKJfknleJIDTG4BoVNQXxdGN4TgxJ8YIBOzAuoTkH4Dw6k10wf1jwCw1ylJ2wrIghZMm0wbXAdKHVS1rx%2B5yBEn2HjvvB2s7%2FwxuogFVsqp3KBwCo9k35IS%2BJcTIggnmQ5IczCQ6JhD8dLnThkS1qwy5VJNsbJ9k%2Fp4SjDng3wHxfuq1kEz5cRAqLmcsoCUr%2BS%2FWThBGbq8KKKu4cqfEKgwF6QeS3RHyCw8AxHVJmCOqNg64Rduhip%2BXJ6V1RCPcAJlT10lHcFEQiorPjjvkg%2FcDi3nQptBebgu0CU%2FMk3xM2fjKkdiomR47m3s3GZ6PWEjCdmZG9BjqkAZS9W6RJ%2BbbtSLwMNMtMj2LsDZL1YpR9SW13WcqJLQYSKrwhoJRWHue5zOt%2FicnmGFC39Nzjd%2BTsFY%2B0Du3cA%2BVlsnazkwo2aAPpT6Cw1kdh02fbbXkWs8hIT9kBiae4MYYrn%2BtCzyKTzJS9M6fbrp6BVWINSmhMHLgaRuc3gfglFY1VES6O61acm9cMvm41L%2FRF919WNYj6nwkMjdWw0NmEgfsq&X-Amz-Signature=399b79b4137ef84863e200ea20e3fc07bda8560578db78cbf751b3dad0c4c149&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDRWPJP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJIMEYCIQDY3tQTkNVYRJkWXcYypzczYN4C4kBf67OHg0ed5ZbVowIhAL6T7wCFJboRQDkXek52RYX5aean6BbNwxY0k9hARyTrKv8DCFcQABoMNjM3NDIzMTgzODA1IgxrbzNTxuwuovk5sDIq3ANg3Z1Lapn5LbtOycoh3%2BZWgjfTndIaeCZ4Oc9yO60KrgXfLhe4Gl%2FnPDSQnbVnlrUlFroZ%2Fo1B%2FTEyPVHPc1N0dEEoUlSWOFSASEZJr2CfpupbvKzM3N12vkKeB9gnHoVR6T0MGkf5dUDQYSgz1wdWS1TSriUlsS2USX3Cvc%2Bh%2BT8vSkhwpzsD3IYEpSI0S8IAA3NXQekyNh65WisRHAHvindfqvqpBUwskMEvVTc4T6Q%2BNR70mSPJArnXHR6KwtIukUS9%2BSqq1w4bVQmL7oJTcHG19mU2vQ5TacSYWJOqVhqTpil1Y2184gipKJfknleJIDTG4BoVNQXxdGN4TgxJ8YIBOzAuoTkH4Dw6k10wf1jwCw1ylJ2wrIghZMm0wbXAdKHVS1rx%2B5yBEn2HjvvB2s7%2FwxuogFVsqp3KBwCo9k35IS%2BJcTIggnmQ5IczCQ6JhD8dLnThkS1qwy5VJNsbJ9k%2Fp4SjDng3wHxfuq1kEz5cRAqLmcsoCUr%2BS%2FWThBGbq8KKKu4cqfEKgwF6QeS3RHyCw8AxHVJmCOqNg64Rduhip%2BXJ6V1RCPcAJlT10lHcFEQiorPjjvkg%2FcDi3nQptBebgu0CU%2FMk3xM2fjKkdiomR47m3s3GZ6PWEjCdmZG9BjqkAZS9W6RJ%2BbbtSLwMNMtMj2LsDZL1YpR9SW13WcqJLQYSKrwhoJRWHue5zOt%2FicnmGFC39Nzjd%2BTsFY%2B0Du3cA%2BVlsnazkwo2aAPpT6Cw1kdh02fbbXkWs8hIT9kBiae4MYYrn%2BtCzyKTzJS9M6fbrp6BVWINSmhMHLgaRuc3gfglFY1VES6O61acm9cMvm41L%2FRF919WNYj6nwkMjdWw0NmEgfsq&X-Amz-Signature=62f8e8a5b1b54396ede8b1a12ddfbaa32a4aeb03c0196b04f042281edb73129f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
