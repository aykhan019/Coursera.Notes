

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USRUVFWM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH0GC0ErFW9qZk148qdOn8mfX2ItmBgvocvpshRuqiUDAiEA6wUlFlvJdvQGojiZ5G%2B43E7SRClhGUxcs0sGQ2z4FWcqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLdQVXrchnDgBl1fCrcA72BM73081Pk9JxsIla9XE5YJL0Uf5vLO0lUuP2uh7hoM0Uc%2FZ68iVzRovCYVtxmxXJ1B%2FhG%2BfywzfN%2F0YA6BycleM47AMf2hE0nYILdplhSuULSHVzDfLuX5EdtbuifdkssJ%2FaD0u9e%2Ft12ZIX6ZIdcGq8xO1HnvVjEGxs2Tr6X54CUFq%2BWg%2FOEC3SqTYTTpkGZM6%2B%2BCEEDywOqueMdsl5j%2F%2BKEgmJUM4%2FQkoig6GCJdkJ0Pmdhnqzu0u%2FKyp4JyfDu1paOm05cNbVLrirV%2BQGexaOF2%2BbUJq3K2bj2D1XlN9Ac0H6%2FEw9SgZDOePELCBXOK9hk6UVlFfH3UUMHQUH6rTSvLZx69DMxuRsGPOT8Hs0fomTC2x%2FmVokLbqdv9dyhuG3MvcB0TwPGEjOEgtFOwSOvrr8kgVfaqWmmV7ZUD%2BIMoYGLl4iiDX8z6F%2Bg9Ejr01AD0Mwlad%2B3MjzTLihljYQcZ9KX22qM5WPeYN%2B%2BG6IHI6bgRjlHoeCOkSwK4rTMWg8ynPvoS0d8rSARz95rQEsyjybHyQruGU5IvOcdJpvF%2FyBDem2Q2az38jm2kLAVGkHnNEnHnMmf4q3AE6MSLhgtwE%2FPzDZmfU0S7ZPhzxgErU9GI3fs2S%2B1MKiU%2BrwGOqUBTENEm%2FArR9b6REb9dTPVo%2BCu1M%2FncRVtTYhHOurpsn0DZ2xBt5ZJFboNcJ%2BNVQK9ucaA5k2WEnb%2BXkbEuD7P%2BNH2gUTzKJBNRd5c2PMvbKZJEzhrjO8NVuSdfOllRZ0N1a9QKcTOuW7SGFpPc0XtD0YD0sOk3xlySFg3PdS7eO7HGiut6ZJ3PguxJtBQAtv7nJhZZPggpYIot5TeziInwOocmUD9&X-Amz-Signature=3aa9a39ed03c09e11ccbafe223fe1cd068679639df585dda4441bef4bf4ad004&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWTFNXQL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKSViXN3qmr1j%2FcrpP3JdSQccw9QlhHVXPCQ5Oaz2HbQIhAP0si2lpsso8mIPPbmH5crSa9lvrcEhEdj2X9Jr%2FRy99KogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTpID3gcQpjpiNW0sq3APkBRo5gn5OW9N3j8ycwucVIZF%2FbnEwRPn5Fsj%2BcbkGE5GAvMqQfUY%2BxB19i7c0l%2Bb%2FjU7aG7Gw8eniCq3DBz8u0sKMGiRyqUJ5CIyIMHbqCNm5Nk27Ju8NICe50p4uWbbb%2ByVbCmV4D0QMDUkJAIGT1ylWzaL8b5iV%2BgUDmfnv%2ByR4ki4%2FUrjSdHhuKbNe6d9nDVWUCk8%2Fg0p2aR%2BZ7Ro77IsMcZkyHIM8DG727wbY4ufRYauGZciJ%2BZdAIRTR5LP%2F5gCzqJ%2BgVfR4v4M9dCVz8D1xa18a2BV4KCOfXV2vMSIqjE%2FR8crnXI5TWH9xIc8CPFAkhixVQl%2FFRZDZkPI5WtFzEFfcweTQUVPBS9Z40k9f5SbccbH%2B3pv4IwsKodz%2BqbVbUq8dlEcPcJKT1i68qjq9DaGcXYGJtQCW4gYLnCTY20Q6Qa2ZAOEEVWnu3v6zTpSnLXwP6BhmF9sdgFu9EMsgjjJn91sOXjWluXoEG7bczlytFMzB6k%2BQCmDA0PmG%2Frse3QYXbqTeSXIMK4bxFm9c%2BGWZOszJkIfycxhh7PcZQPDJoIgRdlCyObO1Vgjb6LAEimKksTiqXJ%2BaHuP7qC9p7X%2Fjo9bplbiAQ0Qa%2FkAb%2F2Skz1V79b5XxzCqlPq8BjqkAYh9A5ee%2F%2Bm%2B8wi9q6sUrEYTDD7rK4cBUSGpG2yEdpZdDij9sfQfV%2FKJgWgRzIZO0Bi2FEohu9sRkKE0EoK70ZlGMOjDwDAMkHJM65YMwV20K8NYnanoy5XPT4ogNlXksaOJESJKYC35qPwwS6TuKMrzv3VbkS585DvlgNtjTz7a%2FWqGx7CroUOXuQ4U%2BmrVVYhw7QObWHxD5Zdl5xqcNro57nCp&X-Amz-Signature=330fcee19250bb832f11d601b476bcc3ff5d0c14df138e97ab3382e021bb2fca&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWTFNXQL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKSViXN3qmr1j%2FcrpP3JdSQccw9QlhHVXPCQ5Oaz2HbQIhAP0si2lpsso8mIPPbmH5crSa9lvrcEhEdj2X9Jr%2FRy99KogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTpID3gcQpjpiNW0sq3APkBRo5gn5OW9N3j8ycwucVIZF%2FbnEwRPn5Fsj%2BcbkGE5GAvMqQfUY%2BxB19i7c0l%2Bb%2FjU7aG7Gw8eniCq3DBz8u0sKMGiRyqUJ5CIyIMHbqCNm5Nk27Ju8NICe50p4uWbbb%2ByVbCmV4D0QMDUkJAIGT1ylWzaL8b5iV%2BgUDmfnv%2ByR4ki4%2FUrjSdHhuKbNe6d9nDVWUCk8%2Fg0p2aR%2BZ7Ro77IsMcZkyHIM8DG727wbY4ufRYauGZciJ%2BZdAIRTR5LP%2F5gCzqJ%2BgVfR4v4M9dCVz8D1xa18a2BV4KCOfXV2vMSIqjE%2FR8crnXI5TWH9xIc8CPFAkhixVQl%2FFRZDZkPI5WtFzEFfcweTQUVPBS9Z40k9f5SbccbH%2B3pv4IwsKodz%2BqbVbUq8dlEcPcJKT1i68qjq9DaGcXYGJtQCW4gYLnCTY20Q6Qa2ZAOEEVWnu3v6zTpSnLXwP6BhmF9sdgFu9EMsgjjJn91sOXjWluXoEG7bczlytFMzB6k%2BQCmDA0PmG%2Frse3QYXbqTeSXIMK4bxFm9c%2BGWZOszJkIfycxhh7PcZQPDJoIgRdlCyObO1Vgjb6LAEimKksTiqXJ%2BaHuP7qC9p7X%2Fjo9bplbiAQ0Qa%2FkAb%2F2Skz1V79b5XxzCqlPq8BjqkAYh9A5ee%2F%2Bm%2B8wi9q6sUrEYTDD7rK4cBUSGpG2yEdpZdDij9sfQfV%2FKJgWgRzIZO0Bi2FEohu9sRkKE0EoK70ZlGMOjDwDAMkHJM65YMwV20K8NYnanoy5XPT4ogNlXksaOJESJKYC35qPwwS6TuKMrzv3VbkS585DvlgNtjTz7a%2FWqGx7CroUOXuQ4U%2BmrVVYhw7QObWHxD5Zdl5xqcNro57nCp&X-Amz-Signature=c6bd6849c69aba895f61e330e66f14b0a81c9806ee20a5fafe330dc36059390b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
