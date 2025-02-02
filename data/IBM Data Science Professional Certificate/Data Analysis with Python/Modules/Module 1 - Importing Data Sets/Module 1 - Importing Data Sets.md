

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MM2J2JY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGErAxs88cFn9coR9IrC8d3mwPHVkufrWlZsHN7CFFMnAiEAwacAJliAhN3w6Fi84kULKmFA2FCmi6pMU%2F916GbEfkEqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLO%2BkeN9ayfKQ8ApCircA4a%2BWex01vQNDgBM7iGOnFlOaosc2uVhD%2BFWnIbyEcQM4X0KrsxmHWWP3fholpX7mD1q4ed4OCAGuQzHfDbbHWD%2Fm9w8IjtkagAO0bvcCiqT44s39PndsuCAFuWOi3ataKW7QwBGVPtIaSqkbKkn792dA4dXDYenI6bgjtOmRJdHhthTyCSfOev8D6VkhrhyqgW4%2FX2eD6LVLbAq7nAgmu%2BLj46tZQzB%2Fg0W0lgr3yQDpq%2Ba7CiERz7YZZSoYs88J%2FeD5MN2G3ClG0n9A7KdoWF8h8LHaPHgxDTEgOT2ka5DZZTgf1BZVTYkFANGBYlReYbgoUDNCABAaLfgGmq6dEi4ifn62jz0iceKx6%2FzitoOlrEwmXOUH%2BSR7SNuczFzGaxdc2yL%2F7NKACYUJ4eVhusM3J5W3Ovi8VA2DZtxdK5K5sBTfqY5THi%2FKkbrdjtiERfUUsL%2F48dj8dTcUydEo%2F5jr5tmWwDof3I1AX43lGprvwCWwVkvGhVmnRzL7GEL%2F7A8XKt6olAebTSH6GsMgf9z0f2P3meEeMVkiuRIIO2XSRH%2F6mI5EMmKBcK9BgBAnWCtG7DB%2Bra0Ir56vY2sbk99w3AXt06w%2BynA8vCwWxBZG%2BWBcS0SlVJlJhPQMIK7%2B7wGOqUBsdnfKKJgcu2ECGOzp%2BYRRZ6z8ld0WDwQVizTQT7ARlUiyPIZk1IgjQ81BrVwmVhH7xPuLFKXTdintNpgVHOpMsNru%2BdiVUA2bEv3Xb9oGN9fc%2B762bZrFdBafr%2BrARv7HS15nK1S5RmVoxKUp1XwFf%2BsNklJTqcpGTTkT%2Fyu8vcVi3D4nBoIqcz4INKSwtNcg2f093yblY0e1GrzsRCZgzBaV2wP&X-Amz-Signature=2abfafa84983315d5c353358124023616a6f10fcdaa81816d79b4c0784f5e3eb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RHX5YNT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGn57AY%2BSDbQfVhyVph3m3F8oPgkmOkPZ8AhPoHQOjI2AiB8UjUHpLDZiiV4taiU8PL9w%2FNRygmYaPh3xufF9j329SqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2Pv2CFsC0agiWLdQKtwDH1M3t2jWFjnz7mk9eAg6jmLy5nhS7gBOIjaHByfPgtN5WAm6JtUdipdr9Qh0Sxh9Bu2NRfQ9s7Lwg4biqQBKprQdxROa99%2FpzS9we53oqWexP4aay2flaByinIbjM8lg19XDl5JTzlro3rwcIVZJYEmaxuIsyCKjzL6mt%2Fm30Q6GUx1ootoN7CQU8neINiewWZFADCR9Wy9cRyCzomXvBw7VsvVLmDKD1u0S%2FMZM3HeIrt8g0rOUCnUIOolffzhKHBbtoR9wDFDL0Vz%2Bwjd%2FBWPzrUHH3R1%2F27mFJ5m7w0Agzb6VpuN5Mb2Z5nufaCqhEtAhtUYTlPgsJx0NStrZMmiyPKubvXIzqxIyca8L3DsyJT5e5rdxOnAFcvhE7LvLzylD0GI3SIJKqKARRa8xFUKnPAM4LJDQsb5%2FprZGT8r1mTvZS5hwXYOwTFkznHWBA3Sz3JSVlZdN8GGHsLVZ3Lt7a0oGH3qEtH292JWJavTuFWN5MtEl7xjB7wGVwLq5o2zC3dDd%2FnyevekF01fdzSsPEyO1mbMhbTPxxcTi3zwt3n7BauiSpYVz%2BsNFO%2BEZdxlEhKDQArvm3gPxSojuKEhBPDXzqAWNXMlTKv6iqQcJYM3KWAsfegMBp18wgbv7vAY6pgExpDfFKNXtzxEzNvFJD4WLHWMExOBeAbtjwFHKQRtdfPBq2wIycrVybra95ieOVlnW4GDzCvTv2v%2BWxOSMbLtm7Lo8blEV9VWUYzKT1hm5PCBKOS9sAtz53%2Fj9lfFdZhGiTjJugsvpuII%2BzT9LifvQOBvak8pU9EMJkKlKb0My40swcPf1g8cYggsKJ5g5U6aDk8ENZAAZWc7%2BsfXHkIT9phNTfLTX&X-Amz-Signature=4cfad03055c165481cce622f578737216c48798dee793473be7e3e3c9aa0ce24&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RHX5YNT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGn57AY%2BSDbQfVhyVph3m3F8oPgkmOkPZ8AhPoHQOjI2AiB8UjUHpLDZiiV4taiU8PL9w%2FNRygmYaPh3xufF9j329SqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2Pv2CFsC0agiWLdQKtwDH1M3t2jWFjnz7mk9eAg6jmLy5nhS7gBOIjaHByfPgtN5WAm6JtUdipdr9Qh0Sxh9Bu2NRfQ9s7Lwg4biqQBKprQdxROa99%2FpzS9we53oqWexP4aay2flaByinIbjM8lg19XDl5JTzlro3rwcIVZJYEmaxuIsyCKjzL6mt%2Fm30Q6GUx1ootoN7CQU8neINiewWZFADCR9Wy9cRyCzomXvBw7VsvVLmDKD1u0S%2FMZM3HeIrt8g0rOUCnUIOolffzhKHBbtoR9wDFDL0Vz%2Bwjd%2FBWPzrUHH3R1%2F27mFJ5m7w0Agzb6VpuN5Mb2Z5nufaCqhEtAhtUYTlPgsJx0NStrZMmiyPKubvXIzqxIyca8L3DsyJT5e5rdxOnAFcvhE7LvLzylD0GI3SIJKqKARRa8xFUKnPAM4LJDQsb5%2FprZGT8r1mTvZS5hwXYOwTFkznHWBA3Sz3JSVlZdN8GGHsLVZ3Lt7a0oGH3qEtH292JWJavTuFWN5MtEl7xjB7wGVwLq5o2zC3dDd%2FnyevekF01fdzSsPEyO1mbMhbTPxxcTi3zwt3n7BauiSpYVz%2BsNFO%2BEZdxlEhKDQArvm3gPxSojuKEhBPDXzqAWNXMlTKv6iqQcJYM3KWAsfegMBp18wgbv7vAY6pgExpDfFKNXtzxEzNvFJD4WLHWMExOBeAbtjwFHKQRtdfPBq2wIycrVybra95ieOVlnW4GDzCvTv2v%2BWxOSMbLtm7Lo8blEV9VWUYzKT1hm5PCBKOS9sAtz53%2Fj9lfFdZhGiTjJugsvpuII%2BzT9LifvQOBvak8pU9EMJkKlKb0My40swcPf1g8cYggsKJ5g5U6aDk8ENZAAZWc7%2BsfXHkIT9phNTfLTX&X-Amz-Signature=3ef1013b150de2a82afafdb769cec9ca1856ecf3728617ad957b93e829d3017b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
