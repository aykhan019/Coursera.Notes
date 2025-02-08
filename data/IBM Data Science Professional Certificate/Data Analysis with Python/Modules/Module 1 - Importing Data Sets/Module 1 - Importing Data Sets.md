

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVT2ID2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCaglxEtpXMDtTDsiEPLwoFVvYFerArlz%2FvkpWgXxf3LQIhAMupXkwSDai0NCSB80qs7%2BKpoxQKUbeb4whY%2F%2F2k%2B804KogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBlUYgksp7cP4yqC8q3APFix%2FwOxixMxbn1f7rg0rHddvBRFHMlMHYD%2B%2BNOWcimMMGTYgGl02TMsw%2BSr%2BduMCMOgTuMjjb%2FVPj0X2oSEE8kW7VTza0VC9JYF6KdRk%2FR8UgOaZ4rYOkp5HnsYGx7tB1nnjKXejm%2BfFHXmHvT4d%2F7KoJePFxxZvDCel5t%2FHvz1oWlxuRy175nqZ0nawgyFTUOhjOmQcQH%2BukxQQtheeurqNchdeskkg6YaLoP8VJZK9MqZPHsmsJ2F4ElxOIqDtpuHQwjwLn0OahQ0WxMbYeo8nHZYt65NNxV82ZsmnWUVlLqSckI1WaZznOavknP6DL7gk4VLW9Q4rchxvRUGdRVhUqYtXmsAiuRAUj2nR24AUrrLEgtc4mxO%2BQC8XIP8WBcq%2Bw69%2FaEP8CSJHO%2BIbDmlJfMTANztJh83h3gt8FJtOzuFvJEbtUQq0LwjXqTct82duKoAwu4yeD1rWdISpIVt8rt%2B3p3wEJ6uwF1CUkuBj74hV4ll%2BKEgCV3OvjGnm5%2F1mxFcBSP8Be2XMa7gztz9teYJ3JO8HJmiziwt28Z1UujMhf%2Bst8anFfOFyvOuJFxc7t6J8Gqgj4WTIJ5cZCPs3dRgltxMziyVkqy3z8TaOMCIV3VYoir3TyfzDWjpy9BjqkAVqyZvQ9deWYLiUIRr0Mnjr2HgUtRNJga3akeclVnezzwz7xDzgwzfigZ6vqaqjSXmbMUnjTbuuP6y1RDLaLLEb8%2FsyprX%2BZwma1KtneVR08Ne8ds%2FuIBCdEtixz%2B%2F6sxAlXmUl1pxnP%2Bbn5jL76ih2i%2BJ3Wx8z3jRaj29%2BWeG38OpIIDvDOozaAb4tYp%2BvuGf%2FXgtf0zGavxIZiXdff82mgI%2B3h&X-Amz-Signature=a62f3119b001b5021fd335cf702de794ae43a9758a314ff2ff6c5bbb669d6c1f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L5XQ3IP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYQhOjlK%2BGa8ZkPUSi%2Fn1hrEZLo1kUI1I9GNJThosL2gIgbDsAe28YRdYcDfka2P7z%2FcwfjfAudSvBesFQyc%2Be0UwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOQIjSBjkb1fWffDaCrcA1yrIYf4tRbak2JQlLd3SeXRKZERjWZBytPoejjH3biOEJk%2BZ8qg94EN22KPtZ%2FpBt6Dy8vSEUvfR7OuMWbDyT1HqD6l7SMuSaB%2B5LaEUV9uFzJn%2FawpjnVZ5pBAKWURcVZiIMuLaI2stir7g44cUAFLPBLCeYjMFxdoSWYHTQbEaqKE64JCmFfooYmwvGUmtv%2B65iRHEDwkbfoEaBb6eE9Pl%2B8Rh6SFCYBj4PTrxQRbLj0Ai5413Yv%2F3s4RVcymlMfNF5b491w4d35d0LnPGMJ8Ngrv7GmYzTxeEAepGGUEO%2FBjRzLJkjXHHBu5tN1KicXmDTagp3YOlftSzyIvRgXcNYAag3YPsUkwGUnXeGvfiMBM2U2OTXTZBjSJyInlvP97XacoH4uG6j8kVF%2F1ZyaS2jKzQc5olsNO9rRBg75lFVEe%2BXEJs8LYtsLt8LG2CjRYwp5uB0FMZhs83nNJI8RZ%2Bia7hfbgffdntudJV9LfmJZrbEiklykDlHJCZPdL2cgvzmf8SMY9Bta3xPvLZshXoKaCQeYxMZuryA%2BYsAL6b70K3XTw9GZA3fUAhorfuW0dLOKqW3kuDjhec4xGsPZnvfMPxfhR01zJ384O0Gm4I%2B3%2B6CZht%2FzUoNMkMIGOnL0GOqUBIx6I%2BPKWJfC1vm6uwpSndCF4eupnSma6FssEpMy1C9ZL5d48dKxUPZ6yP%2FncBfZe4hiJ571NIDU6MeJtKusIM2QS0Kmd0%2BY%2B4j9arArHAKg%2BMD6Avxsj7cQY2D0f4WQjWMgbJilxv0gw8kAkjF9a0T6cdvpj%2FYsO%2Bd8oQBVtKQmQ%2B0Mn08heHEHp725Fmnjx9U7nDE2YZkU66kv%2FSgS6v%2BOTr7mu&X-Amz-Signature=14259e38120d46834f6ade5e5f99ec05eaf7420b6131a11d767f6d37f4f8f7f9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L5XQ3IP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYQhOjlK%2BGa8ZkPUSi%2Fn1hrEZLo1kUI1I9GNJThosL2gIgbDsAe28YRdYcDfka2P7z%2FcwfjfAudSvBesFQyc%2Be0UwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOQIjSBjkb1fWffDaCrcA1yrIYf4tRbak2JQlLd3SeXRKZERjWZBytPoejjH3biOEJk%2BZ8qg94EN22KPtZ%2FpBt6Dy8vSEUvfR7OuMWbDyT1HqD6l7SMuSaB%2B5LaEUV9uFzJn%2FawpjnVZ5pBAKWURcVZiIMuLaI2stir7g44cUAFLPBLCeYjMFxdoSWYHTQbEaqKE64JCmFfooYmwvGUmtv%2B65iRHEDwkbfoEaBb6eE9Pl%2B8Rh6SFCYBj4PTrxQRbLj0Ai5413Yv%2F3s4RVcymlMfNF5b491w4d35d0LnPGMJ8Ngrv7GmYzTxeEAepGGUEO%2FBjRzLJkjXHHBu5tN1KicXmDTagp3YOlftSzyIvRgXcNYAag3YPsUkwGUnXeGvfiMBM2U2OTXTZBjSJyInlvP97XacoH4uG6j8kVF%2F1ZyaS2jKzQc5olsNO9rRBg75lFVEe%2BXEJs8LYtsLt8LG2CjRYwp5uB0FMZhs83nNJI8RZ%2Bia7hfbgffdntudJV9LfmJZrbEiklykDlHJCZPdL2cgvzmf8SMY9Bta3xPvLZshXoKaCQeYxMZuryA%2BYsAL6b70K3XTw9GZA3fUAhorfuW0dLOKqW3kuDjhec4xGsPZnvfMPxfhR01zJ384O0Gm4I%2B3%2B6CZht%2FzUoNMkMIGOnL0GOqUBIx6I%2BPKWJfC1vm6uwpSndCF4eupnSma6FssEpMy1C9ZL5d48dKxUPZ6yP%2FncBfZe4hiJ571NIDU6MeJtKusIM2QS0Kmd0%2BY%2B4j9arArHAKg%2BMD6Avxsj7cQY2D0f4WQjWMgbJilxv0gw8kAkjF9a0T6cdvpj%2FYsO%2Bd8oQBVtKQmQ%2B0Mn08heHEHp725Fmnjx9U7nDE2YZkU66kv%2FSgS6v%2BOTr7mu&X-Amz-Signature=0d6ccefa6f279caeb9eb5274ab67cb1e52576eb354ddbbde202f857df91c64fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
