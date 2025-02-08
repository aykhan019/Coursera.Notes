

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5D7C2SE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIQC7mEr8pkxBqZByEKASx6BbEe4C%2FJm3s2tw%2FtPT7HP%2BTAIgeqQPfH7Vid6k0ORglUtnmFlEVqA3914T1fgwXnPbZEcqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEqgSXl8tlmielRLPircA739R9ouTEQbmLXTxi3ek0WHkx7lW%2FwaUQ%2F0C5PDzkJ9k%2FRj4IKuCej2Fid8oe1zuKMfYKp81h0WMFopLhn3BUgJBO3g4AgJCeqr3HRs3vwrikX104tyr02uS0rEbxD6Qpm18Qzzoi4hu5AK5N7sHK750bmP%2F2MHpJFjqMHgFrk7NlfHIJnRx%2BAivBv7IY%2B7ctGlrkAeYkjtbZpkxxAKRlKlqdlSDWppxlH4DkdbLSk0hGz5gcYEybn7a%2BNILSzVE4JU20yPoS92roc%2Fxo%2ByQf%2Bieic%2BrszG8YRXr0%2BFcY9eRPbqVwxEJuGj1ztT29hGGUI2jFH%2B36qpcDZPZRZp3Da7SMS369F0JekbJ5mxZU95LWxUQYuszBeQ913YiJ2%2BVDnA1goUsdNit8wo7W2YqK4lbJS5mhQ4si2%2BNSU8Q0icZAX4Q%2FelICb5QsjJmQJ0d2wONWQ5Db4hmfZQtfQDyirdkEeateknc7Ra7WM80ARoFqccltMFfBlJnNubFrH%2BYmNMNz5BQhLkqVQhAz%2FN196y7uukkWKz5YZl96CBVJ46nTdDOlpVZYdAAS%2B5hO8idHDZUGGKJa4GMd50Y5a6El9DsuPG1tmCnU1YVF%2FHj2AVuGmYfPRINH%2BvDgdBMO2%2Bmr0GOqUBgrmjra%2BHYiTetU955ojmzfsSfSaCwQSVKuJwK4ifdUhgKfLsfC0GdRQUmrTSNOxt1fzo4sMF%2F0TdD1GZ8miDiEvpmOJjBBICy1D694%2ByYYNVd5ZW%2FFFG1bQk1kScn3GClcBTyA1U4xTUsX%2F1djuAVFBOE4lP9idfqN2xntZ2Vz2JHGr0KjsLLqSQE0ZlWFKIcFm6MJMr6%2F5rsrkAGAvxL37uYco4&X-Amz-Signature=1d8ccaa2e3fca7b6d8255900922a7084df7a760c95dd6bf2ee88a1b0ca994291&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466454MWUZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDyoac2ahqIaNU%2BwwBMGOsJb0N4%2FoSbLL9ZGeAIgZ%2Bp5QIhAIwHpmjbHA0PYsSzYNdZoh9QcsZ89hSguSwADP%2FtB5GWKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxD%2BJui0kPHrFOq7icq3ANdxjdFbj8NTDzdnX%2F3N%2BGky%2BnrbxNguv6lh0Fsg%2BBDHonK1TMvcPlfIhXwtdz8jINAtAzzYB3reKpbcRkK3JVeIipmeB023%2BJVs2j%2B1awv%2Bdw%2F0xZAwypddIow3DwUQglB5x9DTLFlSrc%2FBl2EZSP0QfymGLzT6awWwU%2Fz1V5%2FnYOc7bZJzF%2F%2BmiC32NT41Uoi4XLjvCu%2BowAd7fHOVLU%2F11eqjZrQrgvJ2B3VsXy5tQUxrDDke1%2BmiKwlor2mXuv8KgJ8KcwMsDkG7tn2u%2Ffn%2BM2aTQSLv2Va00sLNUBNu8zi4NQNQHsfb0wYUnTKMTIgapjOoBUOcW989FqBBd%2BOunSnJAReqrXhKkNqirsFaGn6jUg9cRyno1QV2hGPztUY0XdifqS18ApLjfsKbXtrkGrhKc0C6UoM1L6nuf5coY5gWe5WYU%2F5KvSXQjA3YmmYW%2Ffdj1utzzex2YRwoUXeULzt1OA%2Fto%2BLuAh%2B2pQIIn9GEKXFocRNHgKLGWRrqS%2F6OjuNZ3t67%2F5bm8ZSZ%2BJLyk9SxkFMbKIuGq7nb%2Bu9%2FTwTdIlWDcocmWIvrof%2FepVUy1ifWhmR2D34wtqXWQO9FBlc5YHtqoLs%2F8H8V4k0hZJeOxrINt45c1d8%2FjD3vpq9BjqkAe1NwPWFr2pESUUzJy4kGM5IeAgI6OZf3Nv9t4Hrn%2BAp7lPfLj%2FOt5fcwkGNuEjH4joDx%2BSAmdv1nra21iS4zqZKVyJu1%2BpuAr8tdhiJi%2FKGOKSoKuWMhAOfhvcJNtQPK1YVeDQ%2BrQ3uCNuYfq6KXGyfxMq5NVpadFULchVrhw0sqY6U1r%2FyX0M2ClAyXZjAvg7NH6eZ4rC4fbE6x1PLSZOMydeT&X-Amz-Signature=ca4147672c0752f056be69291e05eca414f2ebabbd79091395642e4c5b281d66&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466454MWUZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDyoac2ahqIaNU%2BwwBMGOsJb0N4%2FoSbLL9ZGeAIgZ%2Bp5QIhAIwHpmjbHA0PYsSzYNdZoh9QcsZ89hSguSwADP%2FtB5GWKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxD%2BJui0kPHrFOq7icq3ANdxjdFbj8NTDzdnX%2F3N%2BGky%2BnrbxNguv6lh0Fsg%2BBDHonK1TMvcPlfIhXwtdz8jINAtAzzYB3reKpbcRkK3JVeIipmeB023%2BJVs2j%2B1awv%2Bdw%2F0xZAwypddIow3DwUQglB5x9DTLFlSrc%2FBl2EZSP0QfymGLzT6awWwU%2Fz1V5%2FnYOc7bZJzF%2F%2BmiC32NT41Uoi4XLjvCu%2BowAd7fHOVLU%2F11eqjZrQrgvJ2B3VsXy5tQUxrDDke1%2BmiKwlor2mXuv8KgJ8KcwMsDkG7tn2u%2Ffn%2BM2aTQSLv2Va00sLNUBNu8zi4NQNQHsfb0wYUnTKMTIgapjOoBUOcW989FqBBd%2BOunSnJAReqrXhKkNqirsFaGn6jUg9cRyno1QV2hGPztUY0XdifqS18ApLjfsKbXtrkGrhKc0C6UoM1L6nuf5coY5gWe5WYU%2F5KvSXQjA3YmmYW%2Ffdj1utzzex2YRwoUXeULzt1OA%2Fto%2BLuAh%2B2pQIIn9GEKXFocRNHgKLGWRrqS%2F6OjuNZ3t67%2F5bm8ZSZ%2BJLyk9SxkFMbKIuGq7nb%2Bu9%2FTwTdIlWDcocmWIvrof%2FepVUy1ifWhmR2D34wtqXWQO9FBlc5YHtqoLs%2F8H8V4k0hZJeOxrINt45c1d8%2FjD3vpq9BjqkAe1NwPWFr2pESUUzJy4kGM5IeAgI6OZf3Nv9t4Hrn%2BAp7lPfLj%2FOt5fcwkGNuEjH4joDx%2BSAmdv1nra21iS4zqZKVyJu1%2BpuAr8tdhiJi%2FKGOKSoKuWMhAOfhvcJNtQPK1YVeDQ%2BrQ3uCNuYfq6KXGyfxMq5NVpadFULchVrhw0sqY6U1r%2FyX0M2ClAyXZjAvg7NH6eZ4rC4fbE6x1PLSZOMydeT&X-Amz-Signature=0852577a136e2ba7d30dd5328fd3bf0884435bf3b1ceec8ea275495e9bf7d24d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
