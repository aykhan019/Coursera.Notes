

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646QSH5PI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaWfPo7jQfnjTCwub0mgvJRmmncdp%2BeYtLPK%2B3FeK5vQIgT%2Ft0sKAasX9Pf0LolIwaNacWDk747czSlZvOB2s6HTMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADdZkEFlNgx%2FWb2aSrcA538gwlIY%2FvfDRfuzpPOh6xdiWToIP%2BdOd4y3LU1J%2BsHUoeLQGX4fsNPJ2ynzUzXLzERiIMpkTA7%2FgIw9wmHBNAllqutHU0V7NQWHxAMqwu3bKK30WpMhpyp%2FoFYn%2BKtNPPs0VK03aR4XWsKN8ppe%2BHaW4u2lPA%2BRxj5%2BhzN4ASA77VYa6X6mAEY2olZXXjEka1L6PW%2BkPzCKEJC1AZ27hJYgdDlXjETAbnm9HGcnKeXmIh064KUG6K2obQiaft9tX7%2FMuhyReTnRN97SOzHCUyxG%2B5E%2FvQVsglyW8Rt7pemVdMNKo88zH0CBqhSGlgGza21x3vPGWsNRVKPtqRHI0rjDjPzO3LSWpwMjOLFi%2FTdLo3%2Bs41omtG0MYGPY6mWUDbdhPRhSXmcOACMrmkhcLAhrSCQ4FZCy81PF8%2BoxwlWTGM59eQqrn9aWb91jVHrsri1f2l6yQUpIWy9ScYsX8w%2FezzrPYPTJ3h%2F2l34nDLnRCV4oex9Pu%2Bm0E%2F%2BqGj9R%2FtpykarWQxO4tsFshRciM0KAuBuyd6PqmmTYzwc%2B8CGtV9tSLlcpcrRohhKVGQJVfK%2BjYTffogFnopziIHktSZGs4zPtfiS2iLx98iubGWtuvFzrXw%2BEfx5KA3TMLTY%2FrwGOqUB7p7QMJopx6A0p44vKnhUs6A%2FUHZz6XES3tFuIcxIttUONqLkkfraMvqP1%2BqB8ngAQe5JvSk41aOPyl7vJonNBOubYOs380tkeWDJEXrTMAbPuryG6M1EScYLCwYI5SUzfwwT9c1wffo3fnK6RzP47dQlSPyABndycHjBVi1cv5r6w8Gpg62PYtw8SoU%2BIcPk0f6SoRJd8HHHteyJ2K6pbPZGjz3%2B&X-Amz-Signature=c7b41167d977dd99c42318a8b794449c0656e5aa6c942f71c0fb5d0c7f665fbb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVU2IJXC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDK%2F%2FLn%2BDuZqgjyUa2PbUVUIbC9QWs6Xd%2FRoNazyS8QhAiB%2FGn9hubUjFgCyRi2%2BsfODtogDTa4cPgjGsC5bL2LdZyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOCpSoYcVasF0%2Fo2JKtwD%2FE0ay0pyFtyDUwaK8xCJNFxnxtHGxRbLBYcq4r0Fi9XmVlo6awqoErVj5fZI24NCFVGsGpGvvtbjZry2DuxsKYlIkqkLIxbMtzv0kfG6ldW4AuKKG901mxPAgJjFouEPw56wdp7H%2BTR%2B3I34iLLdZEj2YZJzhEPqUpeOqNpet6lEQmGhhg5mL6i7L7AUXjJJaWROQ9WFAbdQwWFt7NT08Z9oIEect7Y3%2BzH3eKZbGsAD%2FsqOJfQ3RuvkisZVxTbVlhSSrkt3EtAFfIeNKYqA6ucM8moq%2FtANOHvwMMtaZ9bhCFfsmFk857cEbmcII35dS9%2Bx8lk7k1SPp968qh7z%2Fxhx%2B25p1z6kbeSpN4NzKTQgB0mLto6Mai2wzuCelv6ERgmc9VsvrmMTWjD5BL7TH14G3uuXnFgpktnqaURz6tc5P00rT354GVkFgglnE83Bi4ORSv0uQxWqSRIUhT8DyUn7OIb3R3m7%2FFZD1sN1N2TDkyMoffhdwIyp4P2PtWPVO2QxxEmIJ5TWMTADtg7MPvaI3v%2BrX9EQK%2B3IYesScy71ij0%2Fy0IWy2FfFW9p%2BAyseliAyJYn2k6do0O3Eg1FJdt1fRx1QSuSTCsBrF0Ixwe48JDTTtJXEckv9DMwg9L%2BvAY6pgGQlWbbRy5OJqN4NPfH02UW55dlhi5iHd25wdIfr8HJ7ahN3u5lFBfPNttigA1av0JK6sDpEtTgzmuHkkVe5NOwtwBchtzNhq5u81YABaV466GJPvFCs7if1qeUd24boxUpxnnBe9AJR2em8ZVEc8oVi41nGwC3AYQJQK0nRnP2hi84l7oN1DcRc%2BwySdJ7uXRXh3EAaw8a6FEf%2B%2BmJ%2FPTknROWwyxs&X-Amz-Signature=9271169a1a3b6d062225cbe09d5681f266a1aa16ede57ade8f57fb40825daf4a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVU2IJXC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDK%2F%2FLn%2BDuZqgjyUa2PbUVUIbC9QWs6Xd%2FRoNazyS8QhAiB%2FGn9hubUjFgCyRi2%2BsfODtogDTa4cPgjGsC5bL2LdZyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOCpSoYcVasF0%2Fo2JKtwD%2FE0ay0pyFtyDUwaK8xCJNFxnxtHGxRbLBYcq4r0Fi9XmVlo6awqoErVj5fZI24NCFVGsGpGvvtbjZry2DuxsKYlIkqkLIxbMtzv0kfG6ldW4AuKKG901mxPAgJjFouEPw56wdp7H%2BTR%2B3I34iLLdZEj2YZJzhEPqUpeOqNpet6lEQmGhhg5mL6i7L7AUXjJJaWROQ9WFAbdQwWFt7NT08Z9oIEect7Y3%2BzH3eKZbGsAD%2FsqOJfQ3RuvkisZVxTbVlhSSrkt3EtAFfIeNKYqA6ucM8moq%2FtANOHvwMMtaZ9bhCFfsmFk857cEbmcII35dS9%2Bx8lk7k1SPp968qh7z%2Fxhx%2B25p1z6kbeSpN4NzKTQgB0mLto6Mai2wzuCelv6ERgmc9VsvrmMTWjD5BL7TH14G3uuXnFgpktnqaURz6tc5P00rT354GVkFgglnE83Bi4ORSv0uQxWqSRIUhT8DyUn7OIb3R3m7%2FFZD1sN1N2TDkyMoffhdwIyp4P2PtWPVO2QxxEmIJ5TWMTADtg7MPvaI3v%2BrX9EQK%2B3IYesScy71ij0%2Fy0IWy2FfFW9p%2BAyseliAyJYn2k6do0O3Eg1FJdt1fRx1QSuSTCsBrF0Ixwe48JDTTtJXEckv9DMwg9L%2BvAY6pgGQlWbbRy5OJqN4NPfH02UW55dlhi5iHd25wdIfr8HJ7ahN3u5lFBfPNttigA1av0JK6sDpEtTgzmuHkkVe5NOwtwBchtzNhq5u81YABaV466GJPvFCs7if1qeUd24boxUpxnnBe9AJR2em8ZVEc8oVi41nGwC3AYQJQK0nRnP2hi84l7oN1DcRc%2BwySdJ7uXRXh3EAaw8a6FEf%2B%2BmJ%2FPTknROWwyxs&X-Amz-Signature=b542e8a8df0a66476488b6da830a1fad4fb634afef4e5cdc4c41552a9c3464e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
