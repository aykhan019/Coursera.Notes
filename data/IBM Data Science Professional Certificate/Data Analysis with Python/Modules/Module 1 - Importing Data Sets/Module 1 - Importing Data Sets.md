

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T735YPAX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfozWXJ395N%2FczxLT7WdwBQoppsEiEWXZDsKymfZVSEgIgdHhxJwPz3dLDCGdGvOiizm1CZtpLwVlqrxz1kfXe%2FEUqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXvU%2BwC8G7XJfIgNyrcA44OsGJ8kYM1NABGoq2mI5pszEl%2BkjDpmdDZHFix7tr2CL5Lc0qUpWZgZXWOxUtJOYxvlbeX%2BXoVb8lhpMKStBPP9WtfUzrVgYPZ%2BdLhEvi53wZgDDc%2BbMo6%2FWHjof9hGQBXzSxziQsYkA%2FEkdsch0wV8Kg4uC6rMrvbBy6VOxYDV3GlL7l3DE%2B6%2BK6xTndgHJcz7kcP03%2FmF%2BvHyUmyiE6rxDYlelY%2FWj68AuvrrROWidaFAqvbj7w4AA6m2%2B6hsx0z0P88rWvv6N3QeTKMctxHvaPQcvU3h5P1QJnWdxVvHkY6vnatJAyr56RVTOYJEg9S4a1nM1tr35KNLs2aXtwL4%2Fq51cnI8fo2IRy7%2FN6P9nVzQU5GpcBL93UYMfOjXHi0NoV%2Fu9oVrYTCQVdT3qNsbB%2FGCsjClLz3zzHBkIKAJz5OeW68WzdxEs6zape01zjXYqFhOUmbzxlUauh7O6099WJaOAMm7fRmuTozoaBwz%2Fk%2BFFmaZgeiHfsDQOjPQqdwqGtxSgBoh6LT80RsJU%2BWLvmbMWe6AWXH5VpnqMq2ftpDmF8LGAgeydCDZdeE0XKssWrLohSv1MeMQWkSm9GHfldgj77B6Yhiev7soxGJid7mx6F%2FYCMEGePXMPvJ%2BLwGOqUBtWg5pUnUedI2BVKjewxwydvuD5UUiO1asu0%2BpRTBUC8CuPAQ5LG9Eoh5qYPiH8WVVXlMBCn6w59o%2F29Jljdwg4zS0K37tw7BtU4x2qkTBXMPX36QFDwcUThb37VPhj68ZdkiUvhFOtb5j2BC%2FYbidfNzxp6LVK0%2B1VhxC84WtqFoXT02pTt0fjuLe7vCKw8s1gW7dPTcymDOdBDwgE%2FLtzMz0qlO&X-Amz-Signature=af5d85b09fac025f1f1556c15f927abbd99c6c9b94000e909281ad2ce16a9054&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZ56EQK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEE9XfOuK32%2BH8RzE3Y8FxiOhH%2FUHet0qKhSHb2H3meLAiBHRvpVuJAgOYhvXr3Eh8MksdZi8lWTE0%2BYNUOasTgyZCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYK6c7NfRzFqqFmGMKtwDs%2FlG1dsBj64kisZJlRsvgxHY0MRY6KCeQMmas4RpWrCKQdRBzWbUJFWwnOBeLZ%2Bwdl4yt1K33dKNq%2Fc7Au5r%2BJQ7z%2Fx5iPCKIqWHe82UTAqinNH5at8eecLLmJTVb9wCKTKdMIk4domQRk0%2BkxexmSy8mUII0n1FnfqUXBQCOwXpLdHMljr%2FloeMVRPh8aFEMKcS29wnZ1kNApy4kXcydW1tE4UCeDu0WNQ0BZ%2F1GtIzOyoAVNPNI09Np5FghudreHzFowLRdJO9wuXHmhJII7URsBbUNKGVwiU6SqKZH%2B7kLhYPogWwTSDlcCzYhMjdyAFXSuuNQ5UVHV%2Bf6HspWTl%2FJeZ%2BUcfaQiAmg5Ahl0aMO2oz78tY%2Fwo3YxO0b%2B1Qv5AaxGgXNBLW02uweUkjczuriEI69Ym8TjYkrfsn4nxeOBPAkvzTT1ku6WgCoCwbc9CvSIwSZbb6AJNMh%2BLyOH49ta1hez%2FSorx9uuqV9mUTuB3Vf8YFyPu6AuyZRVt8BWvabIED4x%2BCtRpXS9JXs361GuGoSb5EL2TW4lp24xFVxZp4f%2BrTt%2FVjyF6Bc%2BLGtq8FiB2mgyjxpTX4Mf827fhW24rMjbIutOgkjP1clFW1eI5S49UOPTWio34w0sr4vAY6pgGE3AKkaOAVkdli1WMh%2BqWDUyn3d%2F8t6L14bIl3jFaepxFrwpkh67zr6KfUq5h078N2nxeH%2FQCcKV91O1yjqscuMpa%2FinKrTbCTsr4sxXnouGTEzEZp%2Btj2KXlgvMCnE%2BQlyZ6Ma4AhXrnszWUdYnlki2jVgkjn8LDS%2BeBvjNpfV9x%2FTyut%2B9fqvNoPLjdtHfDmoHewjGmjJYw2uzqGlGaQNbsmH%2BQb&X-Amz-Signature=5ee8c7643bd9228be5b3b42e49bed4f41fa09fabdd0577d508828c86f5c682c7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZ56EQK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEE9XfOuK32%2BH8RzE3Y8FxiOhH%2FUHet0qKhSHb2H3meLAiBHRvpVuJAgOYhvXr3Eh8MksdZi8lWTE0%2BYNUOasTgyZCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYK6c7NfRzFqqFmGMKtwDs%2FlG1dsBj64kisZJlRsvgxHY0MRY6KCeQMmas4RpWrCKQdRBzWbUJFWwnOBeLZ%2Bwdl4yt1K33dKNq%2Fc7Au5r%2BJQ7z%2Fx5iPCKIqWHe82UTAqinNH5at8eecLLmJTVb9wCKTKdMIk4domQRk0%2BkxexmSy8mUII0n1FnfqUXBQCOwXpLdHMljr%2FloeMVRPh8aFEMKcS29wnZ1kNApy4kXcydW1tE4UCeDu0WNQ0BZ%2F1GtIzOyoAVNPNI09Np5FghudreHzFowLRdJO9wuXHmhJII7URsBbUNKGVwiU6SqKZH%2B7kLhYPogWwTSDlcCzYhMjdyAFXSuuNQ5UVHV%2Bf6HspWTl%2FJeZ%2BUcfaQiAmg5Ahl0aMO2oz78tY%2Fwo3YxO0b%2B1Qv5AaxGgXNBLW02uweUkjczuriEI69Ym8TjYkrfsn4nxeOBPAkvzTT1ku6WgCoCwbc9CvSIwSZbb6AJNMh%2BLyOH49ta1hez%2FSorx9uuqV9mUTuB3Vf8YFyPu6AuyZRVt8BWvabIED4x%2BCtRpXS9JXs361GuGoSb5EL2TW4lp24xFVxZp4f%2BrTt%2FVjyF6Bc%2BLGtq8FiB2mgyjxpTX4Mf827fhW24rMjbIutOgkjP1clFW1eI5S49UOPTWio34w0sr4vAY6pgGE3AKkaOAVkdli1WMh%2BqWDUyn3d%2F8t6L14bIl3jFaepxFrwpkh67zr6KfUq5h078N2nxeH%2FQCcKV91O1yjqscuMpa%2FinKrTbCTsr4sxXnouGTEzEZp%2Btj2KXlgvMCnE%2BQlyZ6Ma4AhXrnszWUdYnlki2jVgkjn8LDS%2BeBvjNpfV9x%2FTyut%2B9fqvNoPLjdtHfDmoHewjGmjJYw2uzqGlGaQNbsmH%2BQb&X-Amz-Signature=17e2d96d2e86cbfa38add6c672cad48162acf9d127e0d7c4c3a8c20b95e7f0c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
