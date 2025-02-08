

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZH43RAH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCOqhpIW8e%2F2F0ohx28gWUrB8YGhuaWWyP1DFCVJ3utdwIgCLXTl33KV9Dvu%2FOOXyQOMZwgRybjEgW7qr3EtmCNBVEqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDDxLfgtHHrD7FfycSrcA8iDzgpvHN3FgLR0QON%2BSP%2ByK8Jgpcqm5zB39x7v056QIGVPoCSeeleoDGOpDfvnWVA9Pkwjiaqq54lWimsQ8iVJHtuaI5put8jjy8gAZRvy4%2BDCsQ%2BwQWtn%2BO02njrmymwvVDDHMbLN07H6ZczKyTvGzOySHWsotS0pRcTzFc4QmVfbHtbrDYZCSawKJQFUDYFgvGmZr9DPldRMYSjqcvWA90Zwy0yl3A44lt3NP4O7jDNfCS4WPa2MncM2QYYEZvWke20inQleXlfWmAhSkclxXM5a7o0kq%2BAJoshLSoq7VVbWo7Ucdac8KP8l5PyV1Js08A%2F6k%2BZt7bZ6y19uPF6Ag4Je%2FoKEpHJ9FR%2FdawrXhd4ho8clNc%2FIqZhvAMsxSU5wQ67X6dqQvGDAmsNqsWZ9c4pWF9%2FyJClETbRPI3qcHLvQ2tQXlrCHhhsTASbBYWsaLWsL7yQAYgyRM50XV1sZqmjzr9HbBfx3f1qZvsGfg9KS%2F%2BMUvYhk0EDb%2FrbnI%2FM%2FLGLoVrObDwuB1SmQS2Xi3SJsBWpnCz48OErOF%2BFnSeoMVZ%2Fvt5mi9sNB7zlx4rxXeO3AIqGcLT5f8ao6wgFT%2BozVma8fqz%2F2ZDLuHvFfKJN3mweSNG%2B5OCBxMMeOnL0GOqUBwMg8Kc76Kdn%2B65cZ0at7XZye18GRyVO0a8nYTqjFKKzygoe3SGDQMIhaG%2BCCOJcbcnoWwIF0mRoR2Sm2LqEpHYiQ9OGkXmsa4bL%2Figvt0m4dbOHhiUryFiz9jDfuGdstVUR3KxPrHb8F%2Ff4mTOqOGSR6sEHelMsiSRLdJAlRptnhRbPtv0qKdgrIrj3yG4TDayZ8M7tkDXKtVW60SebV8DYvv8h4&X-Amz-Signature=5c1d03b9ddb314712bbccecd96270ad13fdec4228fe61053f54f92293cf102df&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHPZEMDF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCD6bF39MHlTycfmvIhNrfeq05yS9MvGkiwmvVHnZNgyAIgZbZQ3rgGlp8wB6b%2FF%2F%2FKq26OxQd9shDNVKcjnKBbRT8qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3wJ8SQWA3sq%2F5%2FxSrcA7QaCJ0cYFWvl9Bo44nehjTbzhYL4ZuHSWK%2FXq%2BzZST0coXiBgaeRr180dNKQ0AGo29OZaev3JQqJbeBWleshi7OiD%2Beeue8vFGoLcGw%2FUv6jET3Pi4Y%2BxByEGlFwimK1VOnYhTRAO2QtTVVAIDMS33Zifrf1f%2FDkFS668sw7JZwM58m88s9ybG%2FGExKCKhVZE2aB%2BdLT%2Fh%2BTCHPXqcF3%2BT5ldTXDa4lcfAPZGGL0SwEhKMi5bQp2BnHT9W4QTcu8ed1i2t0ybcHglF6yRYH8G8SJjJ702NmF7lqiw5cUfYSDuJjY7U7xd1b4PGQzOcbKnQKQipgJImhYTEpkVrkBk5EyX7EtNVVB7x8VDgpYYx23I3M4CDilJ%2FhaVCHm%2BB8WLuqpmd0zaHZldgyn3RtH9kxc%2BSBLFfLuY8QjQEHcqZK5rrDVPXAxv4r%2BqKMoxlmPLMfABipNIwgue820ZKk6s3Vngg72yK5Qwp7MR0DYobhUTFsVvf9ie4bFhlHjBksrPxbQv0WLw1n5vUijY8c0sKf6Bqybc8bJbpzlIuP01CRpYFUq%2B65HfEc2to1FKvLyOG9DSytEg3DtG31nLfVPgCka5mPLjxaoF2fFkfXrMrHD4H6aHfHFFCBQ7v9MImOnL0GOqUBXphkkwg4FKfVxhxMrCtkMv2wu7sl9BdMGYZ%2FSnf%2Fpkelf%2FJeZZN%2B1uV9DZUiDVNIDeUNld6TEdTpFg1rU58Og7b9SDTKOr9ot8TufaMKey9DEQPjb2Sn2QmwIrm%2BGrHZfu5s2owQD84lHi%2FdbOGjeWfZjDTT1ZhD0x7lzGroIvknEl2R%2F6E9CUZeBnal5qU%2FCoSJNMiENDjxGw0LKSl86Q7j%2FWlV&X-Amz-Signature=0acbb7a8e62e31cfeaa1302e6acac70c3c2ab9125262efbcceda2b61a7c9c6f4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHPZEMDF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCD6bF39MHlTycfmvIhNrfeq05yS9MvGkiwmvVHnZNgyAIgZbZQ3rgGlp8wB6b%2FF%2F%2FKq26OxQd9shDNVKcjnKBbRT8qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3wJ8SQWA3sq%2F5%2FxSrcA7QaCJ0cYFWvl9Bo44nehjTbzhYL4ZuHSWK%2FXq%2BzZST0coXiBgaeRr180dNKQ0AGo29OZaev3JQqJbeBWleshi7OiD%2Beeue8vFGoLcGw%2FUv6jET3Pi4Y%2BxByEGlFwimK1VOnYhTRAO2QtTVVAIDMS33Zifrf1f%2FDkFS668sw7JZwM58m88s9ybG%2FGExKCKhVZE2aB%2BdLT%2Fh%2BTCHPXqcF3%2BT5ldTXDa4lcfAPZGGL0SwEhKMi5bQp2BnHT9W4QTcu8ed1i2t0ybcHglF6yRYH8G8SJjJ702NmF7lqiw5cUfYSDuJjY7U7xd1b4PGQzOcbKnQKQipgJImhYTEpkVrkBk5EyX7EtNVVB7x8VDgpYYx23I3M4CDilJ%2FhaVCHm%2BB8WLuqpmd0zaHZldgyn3RtH9kxc%2BSBLFfLuY8QjQEHcqZK5rrDVPXAxv4r%2BqKMoxlmPLMfABipNIwgue820ZKk6s3Vngg72yK5Qwp7MR0DYobhUTFsVvf9ie4bFhlHjBksrPxbQv0WLw1n5vUijY8c0sKf6Bqybc8bJbpzlIuP01CRpYFUq%2B65HfEc2to1FKvLyOG9DSytEg3DtG31nLfVPgCka5mPLjxaoF2fFkfXrMrHD4H6aHfHFFCBQ7v9MImOnL0GOqUBXphkkwg4FKfVxhxMrCtkMv2wu7sl9BdMGYZ%2FSnf%2Fpkelf%2FJeZZN%2B1uV9DZUiDVNIDeUNld6TEdTpFg1rU58Og7b9SDTKOr9ot8TufaMKey9DEQPjb2Sn2QmwIrm%2BGrHZfu5s2owQD84lHi%2FdbOGjeWfZjDTT1ZhD0x7lzGroIvknEl2R%2F6E9CUZeBnal5qU%2FCoSJNMiENDjxGw0LKSl86Q7j%2FWlV&X-Amz-Signature=b74a292c3b0e79c891d051e59b1b861173102b50b793b2862f22c7408579f187&X-Amz-SignedHeaders=host&x-id=GetObject)
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
