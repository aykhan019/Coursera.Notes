

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4RAEGAP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD8urrgkZUZ1uSepBNMoMNBxYFfoyFY%2B5EiXzpNr5RawgIhAPhHe7hIzYCeoPTZ63lZcuNpNdA6pRYETBf7U7sM63zcKv8DCDkQABoMNjM3NDIzMTgzODA1IgyqdTcHFORHSENrH2Yq3AM9S1D0YvLx1NXU%2FqNpvJ%2FWA6u46NzvJURgw%2FSXwOv17lYS7OLsKWDpBhpPOguMFoI1GWGbGBCHd3kdtYde%2FCIgPRcSunhxsQ%2BHukFB1HoAzDqeaJDqE%2B8yF8uhVHkCDPAeSQXqmgWwXx5n%2Fn%2BvohosmA3dsuFwGAShtVdfbUx02Xl4tqHca%2FqQ6IqqXpejAgUHr7p%2BJe4rtK6VgK2%2FyUZslEcXbPn35ZpsdPgX%2F%2BogJNTozwtU%2FPSawMiAeR0JnLMI0%2BFl6O3a8Hmq0fpKXP8xYImtUsG228FsBm4SYmTl1gyeeyhgK9OBO6tIFrXspRbsv7znvJpeA5flizkf1CbdJvqyj%2BKnUxSS17VwC8CVB4IjEeh2DLLxZ8b%2BpdvWqr7OlXSwGrUvt7ljViTEeBo%2F4Leo5epjNlDqIOplLFHIeGmrgFXH2laiB3NiyGZ9T%2Bx9Ynl8cWt3CjS0BeAnOgCz1XqF0iALyEvkF8nTkRIysVd2A5xwqAkhn0iJmBhyWlm1twE7G2arwLKkR5rPyNkJ93luU1KpGd1TAtgIW%2F8SRzYxnRUJ9UDzID68PyDqQemmoDuO9hoXP5WurTa0y7RqJ6MsH7MepdT0lexqqqU1ZLDtpY9V1jpBV3YSazCVzYq9BjqkASk9KmmYb7hfRiD%2BsjZfuUt2CphUL5xWMEmZuwI80MT%2FbxnTgJBcCZ%2BCrsq3CMOmq33jc54sgX82MqdvYLNIhFAuuy8jqkVMFlvNfElmKuErAaiR%2BXl8dYKCcVDEMc%2Fd%2Fn6XK3DHW7P5ZzH%2F%2Bh0MeWNG%2BVwDzhsq%2Fxat2xwRMIaEOnl861HfTHrG5BLudFq7LUL9APE3DgsyrOvGQreCkxUjWBrY&X-Amz-Signature=bbb94dae5430ca4aa919b875c2fe4ff2c816d3f5da6afbea215d54cc59fe142d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLG4LPPY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCICbBUV1tz9F46ag55YOUVgveT2nBIBITdMSnWMrzUwOSAiBLxBuL8q3oc2JLNGuqtobhKW44zN2UssRUWfAguXMP9ir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMDGm7P6FW%2Bf2BqR0aKtwDWZd7HMRjqQG9xEkhVqaGcdHJA6uvIebgEEqjm5NwhDfzeDFE4s5lB2ssy2y95MJ4budHT2sJK2pIsS5%2B8CIz0buvvwRQWScyjbIYG2m19SrYJ1RYCV1NVTEtsDABbOIdgmHk5QkXiDdmyHkbQk3YYI%2BWeXsnGS9Ii2HsTMfOWD2GfcCQUC2HGGxdkUfnNoqycM93J1%2BzpaoutJmuGY43pgFQjB%2BirgRML0OS1aXUnsLXCvt6qr6XLmDPBOHC8%2ByqhYxfu1SncNBz%2FVcMVVKA875%2BZ7J3%2FwC7LpJJupZlrhgnB18rhbVgrZDEi6WyAjmP2fqSLMtWeSWIVGy4CZ%2BRxOM9UOf3a7XBTs1z2kd7lQ1IOd9YsRcTOxx2JtW7RzZZ9HYJcRPRVEY%2FGM8mP2z4ecZYxqVVMXZDr%2BuBA%2BZAjbtBPVX%2FjibT7%2BPl%2BQu%2BUehA1uWcHeyjOUN4zepw0tC57IACMdhYfFdFAy5P3ZuqxruNLniRIV%2FckKE50GuwoM7JvTIANsnxJRR2pN3iJBRj6kc3t3sEzt7UDhhhgRTLwTgAyJnSlWUUX1XGFMR1ZqtQcr3hnIVp9d0bH9Tu6g8lMI%2B4ATasv1G7MS%2Fx1La0%2FTbQnV7txLrQwIKBbf0wmc2KvQY6pgESlTbYgyfkKLzMPTKq1vlhPQZMAO99kKyn9g9gqYvx%2FA2DKH%2Fz5NyQVAMJa3a7WbZarmTRZBPAH8e7xsLkUG8Tvy36yEkRGutT7kQvwaLdy7r%2FmSShZjEEWLygMxEjPpD6cigzfyqft6ndGjmHlfcAMHzVBTV1PVJ%2BTn3fGx4RKn6MlTmeIdr%2BWqV2yXzKHNkQUrA3MUBGzyNQKhme2XpT6Se39vPl&X-Amz-Signature=00f3f8493f02de7e9ba7dc89f9ed1b0acf8b5d8d0e2264a3e2a8ce86819d71d8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLG4LPPY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCICbBUV1tz9F46ag55YOUVgveT2nBIBITdMSnWMrzUwOSAiBLxBuL8q3oc2JLNGuqtobhKW44zN2UssRUWfAguXMP9ir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMDGm7P6FW%2Bf2BqR0aKtwDWZd7HMRjqQG9xEkhVqaGcdHJA6uvIebgEEqjm5NwhDfzeDFE4s5lB2ssy2y95MJ4budHT2sJK2pIsS5%2B8CIz0buvvwRQWScyjbIYG2m19SrYJ1RYCV1NVTEtsDABbOIdgmHk5QkXiDdmyHkbQk3YYI%2BWeXsnGS9Ii2HsTMfOWD2GfcCQUC2HGGxdkUfnNoqycM93J1%2BzpaoutJmuGY43pgFQjB%2BirgRML0OS1aXUnsLXCvt6qr6XLmDPBOHC8%2ByqhYxfu1SncNBz%2FVcMVVKA875%2BZ7J3%2FwC7LpJJupZlrhgnB18rhbVgrZDEi6WyAjmP2fqSLMtWeSWIVGy4CZ%2BRxOM9UOf3a7XBTs1z2kd7lQ1IOd9YsRcTOxx2JtW7RzZZ9HYJcRPRVEY%2FGM8mP2z4ecZYxqVVMXZDr%2BuBA%2BZAjbtBPVX%2FjibT7%2BPl%2BQu%2BUehA1uWcHeyjOUN4zepw0tC57IACMdhYfFdFAy5P3ZuqxruNLniRIV%2FckKE50GuwoM7JvTIANsnxJRR2pN3iJBRj6kc3t3sEzt7UDhhhgRTLwTgAyJnSlWUUX1XGFMR1ZqtQcr3hnIVp9d0bH9Tu6g8lMI%2B4ATasv1G7MS%2Fx1La0%2FTbQnV7txLrQwIKBbf0wmc2KvQY6pgESlTbYgyfkKLzMPTKq1vlhPQZMAO99kKyn9g9gqYvx%2FA2DKH%2Fz5NyQVAMJa3a7WbZarmTRZBPAH8e7xsLkUG8Tvy36yEkRGutT7kQvwaLdy7r%2FmSShZjEEWLygMxEjPpD6cigzfyqft6ndGjmHlfcAMHzVBTV1PVJ%2BTn3fGx4RKn6MlTmeIdr%2BWqV2yXzKHNkQUrA3MUBGzyNQKhme2XpT6Se39vPl&X-Amz-Signature=b7ab73fe10375d1a9028d630f7f1f13dd909eaf6ec171684bb0062f7832076fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
