

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GV7QYFT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7CoOHyXpYLZxV9bGZeHVx1bzaksID2AxOOQ9p%2Bq6fiQIhAMBSYeUnzVaf7FzIiaYuyB7eL%2BvwAU61Sc72qLy7ikxKKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxaNJX09QMr57ikk8q3AMY2qHUGslIQgKuPnA%2B32cStLbPkpOAfiTWyvBX9dYNBSkwQDRYzPNnTlX8Vd2zwAyMbcnbNFk2ckQmemsasKu4XYg49pvLvUiC8Kl3Yg6oxPSCSstf5l%2BANmZ%2BPkQ17HDbmwsiE6uhVf4DSlVBj6iB3xCFFxeRbjnnuBhyOPCJ8MctwITj8njJHwTAB9Ex1zEf24KBD2%2Fvah1%2FPwW272ABRiZsTuw04HV7E3ISogdEWRvXY1CrNAHAqnf39oeVh6Ac9Gm5lltYnZ1IQgfkLaDH3jBVtNdXDm6x4gWN4yonRr%2Blpt5suhwAEyzdELf7z%2F8LlJBezYDAojzRC%2FOV7jCkRNIIBzHUB1%2FCX2QO18rzpp05bhsqUXw23%2FlZeZtJpsGInMmO7Ke91klaBA0Krx9KqTe2UqdXNeNqDxCMpXLEejRrkDmEYRtPiYcDvmsF7X4ubqNApHRdkkX2f7lPGqP07oBwhIz7J99rreHzgBnVperKZF%2FOREUskK3uG55rO4AvzvD%2F9JUh82NgQQcMHMgi2Q43blikJsWKSSvvxiP7GTH6mQazJsOAjusiekIeNFViZg%2BJkLb8NhREzFXT7dqglfKCgChG49t5EaN9gi2hoOuVaJ%2BDVwP%2FCZ58ozC04%2Be8BjqkAcJ9NYDYPZRGzSdGtvmSMzFmaYy2IpghcDwNP0bXk00RtoiaddbBITtoJdZ8FjkGAj%2FhQIsl36lZrfrnKfRNf1Hs4RXorg%2Bx9BWMiZGF69K3HbS%2F8%2BCyhQ%2FJOXDfod%2Fnz5zz94grbNGRKkymzKimQfzJBwYSBfJKXvpFUEKetd5eyoB1ZK0KCbkmFuImPHUEIcjbPQNVSx1CPIcoJZFphIhv8tpc&X-Amz-Signature=5abfdfc00274f06043e21f2508984c852082d7d43127843d6264c7f4631c4e62&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSOCQLS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICQLafw%2FLhF11uMaa7Ag029ueG66rHmw8F6EenFu9l1xAiApjMQF7V%2FCrmpv0mHvxBqgvBrwLXYdgQD3t0JIVm137iqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrKEUd9FZJ9vLhkmZKtwDNGHRy2vGt0g%2FidtegTlI0qZV5CsPEVB%2BFX%2FvrwyZMRF%2B2gDZukKODO1NWoY4%2F%2ByIYevGkw0iuD0jFWwjWhh6UyZ8LpyrzSsj2hvkQGsUQmOb1rQ1SJe5ibMiu62cYyeWxhoIBiogzx0nNaBUD4W9sklR91B3%2FSL2qIzcv26nOCT4ak8iBY4a9G15n%2B68xonkbgIC4Uqte9Ofk73hdzUawwz1rlnlshC7evyCD0jRtHo0iaunufxHryEfpX6XKl3cU1zXJ2QufK2dOEf%2BrN%2Bctz8MGvJc8n%2FciljQowCOoXgGEVJYgfRptpgYBJwQxqJ%2B5%2F89jPeE%2BtwadBc%2Fkw5GNaO6NdVRXBWBXNHbpgc4MHOmgpxHKlNWgw7m16GCLlJq7JmohttCs1cQ0RVHCkJnFREOUv0KIRhd%2FOfT6CTMrKxRDrH%2Beecpes89hYsZytGkIy7u4cRSPSx6MVy8eiqUe3zSrmCHs%2BkUEQ9UF6%2FmmYVyoa7TLbKrbpgxrrgNYvXh%2FihvwZMFTXqn%2BDoyK3tYePOHmqOEy860Ep0qOZ7VCmCv3AIzxedGXplmY3d9Xk0T0hQ9nEd990CZGA6pmasBrkVflYq2ShSDrqP7r0KmrW%2BYj7vioCMYe6QwtrEw1f7nvAY6pgHYe7jJfeNz6yfDMnpRVlufZ%2F5%2BAW4oMWkxCCLTGyKQJPytrt7Y4PpUK%2Bt93L0Ec0uBacWKdTZlle7oup2U2Jsqcpy3qsXiR8mP3CsISTSY9mh9Gvzr4SWKsJvnWoZpdAQmQnogQAvRA2uW8CuDuj1An2F%2BGMpyQTOUXbeXlE9Wfi1QfVepkAQUdv0uPT4LPDx9I%2FKZXZ3hrgZ0alrc0VMuz83Ix%2BAT&X-Amz-Signature=8ec09cb03055538c42da8f803476b41a597801161a76b54974f17c3f9e5961bc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSOCQLS3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICQLafw%2FLhF11uMaa7Ag029ueG66rHmw8F6EenFu9l1xAiApjMQF7V%2FCrmpv0mHvxBqgvBrwLXYdgQD3t0JIVm137iqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrKEUd9FZJ9vLhkmZKtwDNGHRy2vGt0g%2FidtegTlI0qZV5CsPEVB%2BFX%2FvrwyZMRF%2B2gDZukKODO1NWoY4%2F%2ByIYevGkw0iuD0jFWwjWhh6UyZ8LpyrzSsj2hvkQGsUQmOb1rQ1SJe5ibMiu62cYyeWxhoIBiogzx0nNaBUD4W9sklR91B3%2FSL2qIzcv26nOCT4ak8iBY4a9G15n%2B68xonkbgIC4Uqte9Ofk73hdzUawwz1rlnlshC7evyCD0jRtHo0iaunufxHryEfpX6XKl3cU1zXJ2QufK2dOEf%2BrN%2Bctz8MGvJc8n%2FciljQowCOoXgGEVJYgfRptpgYBJwQxqJ%2B5%2F89jPeE%2BtwadBc%2Fkw5GNaO6NdVRXBWBXNHbpgc4MHOmgpxHKlNWgw7m16GCLlJq7JmohttCs1cQ0RVHCkJnFREOUv0KIRhd%2FOfT6CTMrKxRDrH%2Beecpes89hYsZytGkIy7u4cRSPSx6MVy8eiqUe3zSrmCHs%2BkUEQ9UF6%2FmmYVyoa7TLbKrbpgxrrgNYvXh%2FihvwZMFTXqn%2BDoyK3tYePOHmqOEy860Ep0qOZ7VCmCv3AIzxedGXplmY3d9Xk0T0hQ9nEd990CZGA6pmasBrkVflYq2ShSDrqP7r0KmrW%2BYj7vioCMYe6QwtrEw1f7nvAY6pgHYe7jJfeNz6yfDMnpRVlufZ%2F5%2BAW4oMWkxCCLTGyKQJPytrt7Y4PpUK%2Bt93L0Ec0uBacWKdTZlle7oup2U2Jsqcpy3qsXiR8mP3CsISTSY9mh9Gvzr4SWKsJvnWoZpdAQmQnogQAvRA2uW8CuDuj1An2F%2BGMpyQTOUXbeXlE9Wfi1QfVepkAQUdv0uPT4LPDx9I%2FKZXZ3hrgZ0alrc0VMuz83Ix%2BAT&X-Amz-Signature=795a3fdd54dbfda4f03553a1584b97e539516342456965febf811aa00bcd6678&X-Amz-SignedHeaders=host&x-id=GetObject)
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
