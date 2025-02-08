

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LLTGWI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIFJXStP95LZQCka8DQchhHFnCEF%2B9xPKDXI4rCeabJL2AiEA2cp0WNjJPq4YrLwvi%2BFMoMcsZYc4WlnEV%2BSGEBFGlJoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCQCuIO161yEMk%2FidSrcA1VAI0%2B%2FcroG7YyfyCnaPgSwhtNOzp5XYiDDk0plW2NiE0S3y8J%2FtzXmBbrBqEQMm%2F6E%2BSJLSL9HMUxxFg2xWNliYstzTgE1umcDKBkKXGeWPvN73kFimUCpDwUhphWvlX%2BRJ0E5TYcTFWOGecVG8%2BQZOeZ7tGpx2XAy4NQq7oNLb%2BIO8p%2FeChozIiO9mcFcd0FxeDHkZSgrk5X7Ci0mfF5XgI1cZoSenCNGl%2BR9QhuqWE2BaQiKOj3iMLV5%2BuGmZ%2B2ifS3EuPyvtbzpv9uWD3H9%2Fg%2BWDSJo6YzcyJ2RLdpzO2pDfy90kKVTnvg%2BvYc6FWrnoHavagHz5aXFbyN926c4b8N1dmnBQpMmmzn7AnqrORpzapDOZL2R0S2VWk4dgFFG0Bo0Li8c4PnHoIOuc%2F%2F6%2FvLw%2BPCLMDNwA519Bomzz9w%2BpNK%2B5lVS4DuIm%2BdF%2FaRWN78l1q%2FixfYRr8EMGwjqkWkjfCkFg6YHXw8oN%2BiH5gl8Bnz8JiXbuZTyVqyc9JI%2BefFE00%2F9WI1JA5jvSr1IS5Cg1KFTBLLc6nbtSNf7QUOfTThjpie%2BDDQnf%2BOHo5jTQRzCW9rdBdlwUM73hHuwjXgIt5yUV%2Fe4FQghgZlUwmAV%2B%2BUyBmWZSPaMMKuOnL0GOqUBh%2B9tXgho4g28ylGLEuRawl55DzZF5auz9Nl%2FQikzign%2F%2BNsXc9FXssGdI1%2BYE0WO%2F5maL18DGlGN5PE3GtvQ5MirVe8TKiErXc5dFMEWfPVp7FMR%2BOGgLL0Fp7eI64baAfNNnDKNcPlacxr9Vy%2BmbArczBO5j6CYJwd1r5X53aJk5FS4VmWIhnDCnTZkKO%2Bn4I7LHaIk1ZQhPiKZgU0nT7OZIs9r&X-Amz-Signature=4f14cb2901ec6bd456b23c87817c0e08468189e6ecedaf2e9653a1c2cbf9568c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466323BWP4D%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIEVpRBvlNGhVxhjMqQz9At1KOgLIOg%2BP%2FnI1%2FsJIUSa4AiAP7MLmAnpNGRf%2BNjjSTccJKGAj8b7EcLBHa2vsvhBMGSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMu6gZ%2B3neOYAyOz7YKtwD%2BS3pWH6CJGtWWArcfKCHru9CqNmk1YIZ5j1uKsvv2XJjH%2FZ6n6wdacA1hItbxVOZT3hRohMxLmepeEwsXsN2CSjNMDsW5fxZnqCiROT%2Fw4FBmqV89slqa2yM1NNyVTNaASjvKGzRU3u%2BVATt5%2FBHnqmPd4lA0erQYaR0ojK04rKoewzboNVfilsYOUde3exPxwqypE8Gn%2F0tCwX1TUywfpzjrGf%2FnUkDujmdruKp8jusUvrp57ISokU8d6LiwyU681yVE3smQTi9QFF4yWSzZOdUt8kjSNiizufhnSU3j5mwCH5jJ4P7OU5j9Ph8Xpd0IALBsbOkBDaBvi0ld%2FbFNgS0rTwQhPNiG2tfmKvDpNDd4FKZDFiMlgcZRSB5TLE3ZUJvIqUwM6cFI3%2FqI3M4UgJq0rzPLXZtYrG1DoN9dMGmvYHKYRqAjf3bIkoIWCgLOGnHYZRNuKqSvO7X%2Bn26Q6rcZYx5VfXGxRdXKKhqi5IVJrVOndpb07Ju%2FlzySNK65LqOVAcoCMvBcDdH1x%2B3C4N4hIuwvhdONqn1Fykf72eRClcElQ%2BNq2UzPnz6YN9r%2Bq4c8XNJYyKuTCdQJD8Ue0BKM7LOmJs6YMuWuhVuEvl0802WCEs542Be0YYw6o2cvQY6pgGAbRJCO%2Fc9Qy19L3hibOd79Neptr%2FXEMFrrFOdf39E95oj10XOG%2FRX2MrHL%2BzLNpmnJECCXKkJlmeX8z5H3L9E8tTJIsJq0dEQ0SQtCVrTGqaBS0tigN736WCbxM%2BrbQ20VO0zfnOR1l0bTUd8MG2WKWqdZakaAz49d1t%2Bs6Hd0dTO2MiJbHvOTb72OLf08cJrLDaOhuFQWZ8CjQePkGJSby7P202v&X-Amz-Signature=0ba216a69c2fdd96365400141d4ed21c5d8e9f797a259ba8ef7da50037edd14c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466323BWP4D%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIEVpRBvlNGhVxhjMqQz9At1KOgLIOg%2BP%2FnI1%2FsJIUSa4AiAP7MLmAnpNGRf%2BNjjSTccJKGAj8b7EcLBHa2vsvhBMGSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMu6gZ%2B3neOYAyOz7YKtwD%2BS3pWH6CJGtWWArcfKCHru9CqNmk1YIZ5j1uKsvv2XJjH%2FZ6n6wdacA1hItbxVOZT3hRohMxLmepeEwsXsN2CSjNMDsW5fxZnqCiROT%2Fw4FBmqV89slqa2yM1NNyVTNaASjvKGzRU3u%2BVATt5%2FBHnqmPd4lA0erQYaR0ojK04rKoewzboNVfilsYOUde3exPxwqypE8Gn%2F0tCwX1TUywfpzjrGf%2FnUkDujmdruKp8jusUvrp57ISokU8d6LiwyU681yVE3smQTi9QFF4yWSzZOdUt8kjSNiizufhnSU3j5mwCH5jJ4P7OU5j9Ph8Xpd0IALBsbOkBDaBvi0ld%2FbFNgS0rTwQhPNiG2tfmKvDpNDd4FKZDFiMlgcZRSB5TLE3ZUJvIqUwM6cFI3%2FqI3M4UgJq0rzPLXZtYrG1DoN9dMGmvYHKYRqAjf3bIkoIWCgLOGnHYZRNuKqSvO7X%2Bn26Q6rcZYx5VfXGxRdXKKhqi5IVJrVOndpb07Ju%2FlzySNK65LqOVAcoCMvBcDdH1x%2B3C4N4hIuwvhdONqn1Fykf72eRClcElQ%2BNq2UzPnz6YN9r%2Bq4c8XNJYyKuTCdQJD8Ue0BKM7LOmJs6YMuWuhVuEvl0802WCEs542Be0YYw6o2cvQY6pgGAbRJCO%2Fc9Qy19L3hibOd79Neptr%2FXEMFrrFOdf39E95oj10XOG%2FRX2MrHL%2BzLNpmnJECCXKkJlmeX8z5H3L9E8tTJIsJq0dEQ0SQtCVrTGqaBS0tigN736WCbxM%2BrbQ20VO0zfnOR1l0bTUd8MG2WKWqdZakaAz49d1t%2Bs6Hd0dTO2MiJbHvOTb72OLf08cJrLDaOhuFQWZ8CjQePkGJSby7P202v&X-Amz-Signature=b45c1ab3f71bdc2f2dcd2b9398d942ecda7d5113b8b6a72142bf07040c9885db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
