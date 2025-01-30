

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD522MNF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC83dGbDrmBarVbw3KGkol23OVRvvZACfTEBRqtrpVVFAiEA6Vv6Y1KmDojzqk2l0X3UcRhN2VEGqWy9aat5BHwCiIkqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FHEcPXbllw0ip0%2BircAw5h9Wby3OHSC6ldmbfLENgs9ZmpyGzkQUgMoXKv01nHVJGj2e26IhQUcOdZyLFZymL0AI75gEcRdy%2BpjiY3218NC0actLhSkatrKNVmrYvJMP3vjjcDbgR0R93HLgJnheN2sROpbVIFIOArVLpWj3mI0l2j68shf9MxF%2B8ZondQ%2BfJKxO7Goobst%2BTa%2FcX0cIm4lO9%2BYg835sVqdzSV4AyMh%2FkWVlpVVEc49yWHFLABOr522fKSM3MK4WpqttNNGgiADg7JX6ya6wjOlnZgDZmbrsOoWY7NEQonAme25vR9pl4X5XfCp6RSvu6ONo3PEYJ7v7E03tMECTl6p7e3LN1Sz5JO9rXeFiPS8CStcW3PWR811T6Dlf8LO7M%2Frw9962XlTV3QUeLafAkpBFMykBtqLBydjer67o4g0YrAUeWIbwrJGYQlI8GGsSUyCDESQWBI4DrWcfw%2FL8xRnT8pWfg2Pr%2B03n2Q%2Bm%2FZaCyrNYuM%2Fs0Vy5O31sYMpLZSM25X2XiNFcz5%2BRy0oIRfmKVCbYjeu21vpFI7ifhW3CWjJCBDFJBUlNNLn0qow%2F5f%2FwaOJLTRp19%2FUJG2AOkhmAM92dDq7lmnDaGPaB%2FO%2BGDaDoeFl4n8kV1ERGb13xBcMKCX7rwGOqUBpKkorthsS4BWoxyKu28JbFnELNXQQOqPFuMPvVQY9i8k%2Bxc8YJJKEQemV6hd0t8Xv2gMNdhTAUvAAoHiQAiisVVOvD1c7hter%2BRP1%2BOtLN30%2FoMPGsoTTJb6bTI0XMfToOjpMMV6x7pOOs79OypO0gMFyatIRLlMhZGlTjyaeInbGjgpp6BvvisiIyrrHqk%2Fa4MfkcEfX%2BQjMbQ37pfOnl1XvGKc&X-Amz-Signature=0a39d4374b8db39f18ee4d5bb73c7a801b7b4f736572245074d65b8b60238c97&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VRQPZ64%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEX%2BKLtCL7kaqVHUMFgOZjZUA792EXuQ7lJhODEWKaLsAiB%2Bw6PnOUJnUr9uleKzZoUfjaBvfdn02ORJKO63Sl7W5SqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQbW09bv5lTPRgL3jKtwDr6mP6E41IL9sBjNWBB0H0TsX9Nat7E8es%2BvgPO3VRazCVAhUgRiluJUjYbhCWM2sboF2c13MgwDfLFjER9nQoQh8nTMpxCKHjMJVmDEsR8iUNJeZKgEJw4ggWrjw2F%2BIsJe%2FDsskLks6A5FGz2%2BKlsJkojp%2B0uR%2Bdl8J3wv5DTQD9fB5S36qz7LrTo5FWOsjcAy9UdaJ6K4eFC76x4O%2BZfD4Em8DKIyux21Vb8HgT1xQnvsEcaMOat20R2sqLOhbtqFXBdb9oJjTKMOLVRpDkN0NBZILmfO%2FvoNhbFEdSG2v59lX6YD7%2BxB4Y%2FyiC9nfAuS9p4uvsnDWzoRL8j0bjKAagdntMKsnlGHne%2F8Ii%2B77oVhQislsFFswQ3zItAy42wAmiabT%2FNDzjyZomIg93EOdXWjNKllTovFGu4UXfTBLPnpByZJWw0lztk1iUkxcvV1mrdj8aTuPfuiW14MRpEGJ7B%2FeSSA8YtgbIe63Jh8VKGgFCDPdnIbLQERuuBNNU6jyZtc3GgCfKqJ2CRo81LEn0M3rK3wDmwlO1S0y9HkltHHZlvw9SKKFbE7ttS96adWeEurmmeoNaYMAMpFjN%2B7UcOssooFJjI5B8FJ36CnGXwvHqcR51KSG3lYw7pfuvAY6pgEUnLF%2FP9AYxNyp%2BcA8zemTQ%2BxnBhEM%2FXxi0qvLXoiheiB1uF15RlMKns95fauNgBjY0QyVfV1eZB%2B0E%2BysvW1m77JUg4e2iXVEC8m%2BQPmnd8BTiElJHYYD%2FsMhgR22ANPyg5wJwDngDu1yEH36lr9myiTjEOU5LFcCrNqv3pGrkRGDofYbsyc0YZFIT7XIJDstkna30K4GmKJgGFs9Qosxzwyx%2Bl8O&X-Amz-Signature=3f2b73b97fddca9950e5b04bc226624a3e433cb6a9b1464a871e73da44c2f95f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VRQPZ64%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEX%2BKLtCL7kaqVHUMFgOZjZUA792EXuQ7lJhODEWKaLsAiB%2Bw6PnOUJnUr9uleKzZoUfjaBvfdn02ORJKO63Sl7W5SqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQbW09bv5lTPRgL3jKtwDr6mP6E41IL9sBjNWBB0H0TsX9Nat7E8es%2BvgPO3VRazCVAhUgRiluJUjYbhCWM2sboF2c13MgwDfLFjER9nQoQh8nTMpxCKHjMJVmDEsR8iUNJeZKgEJw4ggWrjw2F%2BIsJe%2FDsskLks6A5FGz2%2BKlsJkojp%2B0uR%2Bdl8J3wv5DTQD9fB5S36qz7LrTo5FWOsjcAy9UdaJ6K4eFC76x4O%2BZfD4Em8DKIyux21Vb8HgT1xQnvsEcaMOat20R2sqLOhbtqFXBdb9oJjTKMOLVRpDkN0NBZILmfO%2FvoNhbFEdSG2v59lX6YD7%2BxB4Y%2FyiC9nfAuS9p4uvsnDWzoRL8j0bjKAagdntMKsnlGHne%2F8Ii%2B77oVhQislsFFswQ3zItAy42wAmiabT%2FNDzjyZomIg93EOdXWjNKllTovFGu4UXfTBLPnpByZJWw0lztk1iUkxcvV1mrdj8aTuPfuiW14MRpEGJ7B%2FeSSA8YtgbIe63Jh8VKGgFCDPdnIbLQERuuBNNU6jyZtc3GgCfKqJ2CRo81LEn0M3rK3wDmwlO1S0y9HkltHHZlvw9SKKFbE7ttS96adWeEurmmeoNaYMAMpFjN%2B7UcOssooFJjI5B8FJ36CnGXwvHqcR51KSG3lYw7pfuvAY6pgEUnLF%2FP9AYxNyp%2BcA8zemTQ%2BxnBhEM%2FXxi0qvLXoiheiB1uF15RlMKns95fauNgBjY0QyVfV1eZB%2B0E%2BysvW1m77JUg4e2iXVEC8m%2BQPmnd8BTiElJHYYD%2FsMhgR22ANPyg5wJwDngDu1yEH36lr9myiTjEOU5LFcCrNqv3pGrkRGDofYbsyc0YZFIT7XIJDstkna30K4GmKJgGFs9Qosxzwyx%2Bl8O&X-Amz-Signature=c41770b16e7336d361212c650ac0680a35aed509a7781e8ac8326508c9fac542&X-Amz-SignedHeaders=host&x-id=GetObject)
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
