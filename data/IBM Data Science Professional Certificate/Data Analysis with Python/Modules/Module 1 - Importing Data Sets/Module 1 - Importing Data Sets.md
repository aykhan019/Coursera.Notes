

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBO5F6GC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTCxkxXvUwbBdhmxBz%2F9O5jIWJSkMOG%2FlQRh%2B1S9cl5QIgU0JLb931GhX%2FySvy%2FkbB7%2FgkHlXMmOYlfHbNFddA4qYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDNSIrgwk4q%2BNBGNusSrcAwlbiS1YnFrO2ayzJSCxHcFw1HwUucKabjRFOO%2FwWh2o0i%2B0MGPB48a9e5GT2ForzmmhkyWRD4c6nK0HUwTj8Q%2FI5YJb0Lj2a4LQkiCJ0It79qMoiIqfRxX2RXq1ZhBPHglmobfO32M%2Fc8n%2B93bfFOU2EaWLfv4qGMCfDqh%2BnooSD0s71TqI51WDAHyStyyF3UT4%2F3KbVfPITwUQgKkZ4xGWhgXlUsRV%2Fa0Zx8Dt6%2BSGnGYB8vVX4hU1Uo7E8J%2BH6SkClxulsUgKKkigF1ZC5SgzxIkzoT8DILymEHYGWQT7QBIvebcoVoqmJ00tuXhrRcGRB%2Fa1%2BzpkT86p5eWQGpHU%2BXCbRDZQS6Jv4AiPITncN%2BLpl%2BmATNPwRRSPRM%2B1unAO3omI75vwzw8urHj%2B2xOvBUv6100DGOewk7KqkbXM0ADqVbRhwaPN8NCio2zq8DHICWpCrAcHb3Wbe6pDsYy7ycMiwlgxDXZOla0R%2FB0%2F%2BDDRjyqUc0xaup%2BEdh7VBd0kRIHbfq3zdc6bN2Zr8hz84praiMsj7%2F8TwHbwCLCl0nTF8fOVGzmz2QcVQy9J3EefHJnb%2B%2FcNnvpJTNtHN%2BJKd8RlKAZ8B8r7gTAuZl04AwiTRbJHzTYHpGAbMJ%2Fzgb0GOqUB4RPZepaO6ocvYXbajbJ3x9OdrHjpuaH5LXiyyRGM2oBuwITFwFfEG19LoIudp8puZ38526uaBxxOK8t%2BOVq9Te3Z63L%2Blto7b1OOwo43MtRUT7%2BNGmg0uWZqC0lhobXqMUJhq7aw1HroP2PX33qKZt2UutsQk5nye5c9XHMrRnBmT9sK5dWVtiFhxZb37CUmZOkAXhtknisfXd1rFskkG1Xrb1Xt&X-Amz-Signature=3276ade06a6e0a6d79342164cc94a9d592ffe06b0853c081ac37386e692873e9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BNXPDK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClAifpneEsOk4MirtGsutHU3VZrUtasH3oltrvHkqUiQIhAOmN9nZRgnw11zXcvIOhoYU9YF0lvQ0BWi%2BqHaL2wE9IKv8DCBEQABoMNjM3NDIzMTgzODA1IgxVrFw7tYFJkxQkdl4q3APdGguugEofkhewkicZKKUFwUGjnbvyHQeMOSFjkzu37w0NCfaYXmkt4x7oHRcjdWMSp9F1KeUCGUdArhT%2FXLzLVysBxJFICjc1QeAaIaHBZFo8hjASNDXeFvziJ647Nx8wWEISTCUK7eC8bWvjkRqZjzzc2J5%2BcsMIL6vnsJhP5y%2FP3oRLYZllZ80KZIuMDhlI8cq%2FPKWtyADQB%2F2MX%2B0TQ0HCgWiZDl4NvLeZvitGgXSVgm7uOTN9W%2F4KnXF00pH1my8gKxZRrGUV1knQuv7rS9XGXDxDDvEJ5iRE%2B8R6iu%2FmyBXA2O6YLQlY1ChN%2B8vBNaoQH9YsIGwSX9edGzRSy15Ucg4e1yshqFIpVkrZW0hIp3fuJ21XuCnN4ODsGmJ5WRStIy2tkLxKdq6py1OCdAbVHFHJIwKkBjJGCC8N0EIOCIwEbcY%2FP4%2BpTql4fZnmoOAezvZh76k0rRuRlH2XxqKuUr4te62XRFFv0%2BlvG%2B1nLhlaZKfBSlgfkkyiOnx68fpUHf%2BWOasa3wRHKjtGI6UEqtxwOQ8347Cc3yXxCwr5W0ze4PjzoRVj6oRc4pxJ287HeWGtEHceGwVVQqPXwn9dwur46hxjKrpnKv%2BtLgsCtNmuP4issdp4%2BjCt84G9BjqkAU6Vaj4pMJMQecj6Vt1IZDJHfSbMVWtOgL3%2B5hLR%2F99Z8HdzJr2BJCZycdz7Ym5Tf0FNYBmzqxLp7VPxSawn%2B%2BNmNYUl6AMARF81tSUs5obVDkPoZiTl24xVrnQvgz4Vfz6pWOLyBeFbogf9RlP2W%2FbV05zI9ax7PQ%2FrnhDsHFq5pAYA12Tq2LzwYczynBdEtiRQc0pOgnro2xl5xyppxS72ejcC&X-Amz-Signature=cbfb6a595388a5d0a21029314f2aec1d66a9bd4ed275211a43ef71f9c562126a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676BNXPDK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClAifpneEsOk4MirtGsutHU3VZrUtasH3oltrvHkqUiQIhAOmN9nZRgnw11zXcvIOhoYU9YF0lvQ0BWi%2BqHaL2wE9IKv8DCBEQABoMNjM3NDIzMTgzODA1IgxVrFw7tYFJkxQkdl4q3APdGguugEofkhewkicZKKUFwUGjnbvyHQeMOSFjkzu37w0NCfaYXmkt4x7oHRcjdWMSp9F1KeUCGUdArhT%2FXLzLVysBxJFICjc1QeAaIaHBZFo8hjASNDXeFvziJ647Nx8wWEISTCUK7eC8bWvjkRqZjzzc2J5%2BcsMIL6vnsJhP5y%2FP3oRLYZllZ80KZIuMDhlI8cq%2FPKWtyADQB%2F2MX%2B0TQ0HCgWiZDl4NvLeZvitGgXSVgm7uOTN9W%2F4KnXF00pH1my8gKxZRrGUV1knQuv7rS9XGXDxDDvEJ5iRE%2B8R6iu%2FmyBXA2O6YLQlY1ChN%2B8vBNaoQH9YsIGwSX9edGzRSy15Ucg4e1yshqFIpVkrZW0hIp3fuJ21XuCnN4ODsGmJ5WRStIy2tkLxKdq6py1OCdAbVHFHJIwKkBjJGCC8N0EIOCIwEbcY%2FP4%2BpTql4fZnmoOAezvZh76k0rRuRlH2XxqKuUr4te62XRFFv0%2BlvG%2B1nLhlaZKfBSlgfkkyiOnx68fpUHf%2BWOasa3wRHKjtGI6UEqtxwOQ8347Cc3yXxCwr5W0ze4PjzoRVj6oRc4pxJ287HeWGtEHceGwVVQqPXwn9dwur46hxjKrpnKv%2BtLgsCtNmuP4issdp4%2BjCt84G9BjqkAU6Vaj4pMJMQecj6Vt1IZDJHfSbMVWtOgL3%2B5hLR%2F99Z8HdzJr2BJCZycdz7Ym5Tf0FNYBmzqxLp7VPxSawn%2B%2BNmNYUl6AMARF81tSUs5obVDkPoZiTl24xVrnQvgz4Vfz6pWOLyBeFbogf9RlP2W%2FbV05zI9ax7PQ%2FrnhDsHFq5pAYA12Tq2LzwYczynBdEtiRQc0pOgnro2xl5xyppxS72ejcC&X-Amz-Signature=cdb689b4a9958594a8c9f3182927d8b4696002bed18b2cde98787e30a2e865b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
