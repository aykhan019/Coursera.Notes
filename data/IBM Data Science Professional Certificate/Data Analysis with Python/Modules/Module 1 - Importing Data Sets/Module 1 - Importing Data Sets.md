

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DQRXRJG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQD%2BqWwg8DQ6FOHh8eQFEt1nD7CChuEgXCROeNoBH8E%2BoQIgMPKg97akzF4XWIGbm%2BSbb5FCF2Xo81QwVWe85US%2BgFcq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMLR%2BB7TxxLtp%2F6cVSrcA2DXQfvpkjtb242DCghpayrm90XvtBety8aN0Bx65RhTPdxCrVFZDhTS5gOAd2TLqh70wk2ApS%2FGp%2FJhrPTz2HxFa%2BGFF2vMWPo5NesXms%2BULgrO2aCEog4IW49FIfQYKfe0s9pYXEPTIqBF0JxbQcUEsS6nld9m7yy2f93cTwUrPdBzCvLgz7qy%2FzVCGJcuh60nNjOQJwoLlrVp6UEM0qIeOav1xIjXcD0LmqelzGQWg81F4bC7yy%2FGaulqL%2BU3hxYvh%2FrydFdxQfbEYUJIZssaMc6jJYYPVMnuk6SuQSshHJRLB8KsTW01xsfeu3qLsHHtNBo7wwNofPqoNzXTxSSd1rWoRYEtKz%2BlosQWR9PEFiBEZWdLIG%2FvNvBTOOz8iZeNOMt1ADY0eQWi18ciSQYIDjCq5uCWEQxYX9%2BhoJ47y1%2FReQ7L0oB9pGPe3WK9L0C8ucmER4ekEA%2F0U%2FUckO%2Byh8JuJYAEX80Ae2OdzgdXgLfd%2Bq8PJ5oxdAu9dosGyguAxlDyPSOw5QvOwP5ffM0WSwjc%2FB2VjiMAze%2Fs7ds928ATdEf6Sv%2FWES9Snr7yHKAYUj%2FS612wGyYWD0sVG%2FR90ii68DoI6aZRxFuT%2FcwRaHGUt5Cni0OkXb27MI%2B4lL0GOqUBrh9CguVJsOi2vAoQgzrFqh6lIiZ4TClCDogLH0WVpARyFZjq56NhBPmj9lnY7sRXWvFNLu70iXcGLmr1KffT8RZCa%2FpT2QaEIpjqj%2BturDFX%2Fc1wQhvPXyEwl9b8RBGb7vARLuPJjJ9X8137gI4oJgTW%2F%2Fq5An6hvd1GROIRh8pxGoEcXwumDUovbyL2m%2FiTmmhpGB0S0xZbSL4H16VlcT9SF%2FAQ&X-Amz-Signature=d8604c346ebc12977bb892767adcfe7d407f5377dd1bd6844408305add8b6d80&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDGZTUTX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDyCCj4nRAOWabcvrFPdwr89%2F0sLg2zqDfKpMc8kjRGlwIhAOHcis6F%2BaLc6rnq7%2B4xssOC5k3gZsTDtElgY9lN2pLjKv8DCGYQABoMNjM3NDIzMTgzODA1IgzLWxgNnkYxzAJF9lgq3APbXS6Z%2BHIJouA8vdi5QbMgJP6jm4hFSfAxHP%2BfxzfLdIgvutARLIhf6CagAkgJit%2Bu6T8CXkpe05KtgGAgJGRQ5cC%2FO8YiXJFuSiUlTjActrpVrbGwuhd7fOtgM9O%2BhmKbgU97DoMxI2j9UOJkf1nQfAQ5Vxm37DyIQ06NolxDV4uJgrnPi2KcXVH4Vl9ahY5OUFFuIZ%2ByDJEZfac2vc4HrR46zeRVMpv5WfyS87hpwZ9kM17EtS220GRo6AfprWROz2KIzNNQ%2Fbg1B987%2FqYlNlJYj0I30O9DvJaa4lpWj%2BCKViwickfAAkZPZswyRgfMjGVzGauoxAKdIlZENb3o7s92fvHFc8zuTOyc31A2f8Drurk2jnPjv2Dxwc%2B2WpMGwov9cgUhNI7WpTD0MiBDizdqjRtLKA7ZxPFXQtJopv70KzoSIMyKPkVdR%2BWmpRHAsq0g95ioscEIFrKc6FLx%2B0%2BehJQv1ocrBk4m6R365v9xJyzqcwppCkMeue5zvK55lXOjECcw8uVFMcj4VJpU%2F%2FFw6uf6bn9zVQ73T5n4qzjHoy8Yf4gaaJjxJ4vXykP1H0MYcCTFjl6Vo9KtpNl1vvy2iWA0QTcuiEJTMm%2FaSgYbAPVF1dJrQ3fmOjCmuJS9BjqkASlXUBJyvISFkQgHY%2Fs8Cr2DfBeVyTcV0BO2yytjOr%2Bzwnyz8h23HWJp0sdyKQE9ivGviviwMjTDa2B%2FLbi8duytYxCdH%2BjpAl0%2B9t24mOOQzh2qJ5UcIC0H1J%2BvzwODFDXhfePkiOIX2DpZBo%2FxeHQ8wDyUYP9KMr7YNwnE3C%2BhkLN6AC6Mong2BOfPfjZS7cBfCVobgONHftYyMFKRuzB2A%2Bvy&X-Amz-Signature=545ff158d42512f21f1c99e41d5a0d9c15d2acfa73b8d6e18c0b6de1998766ae&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDGZTUTX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDyCCj4nRAOWabcvrFPdwr89%2F0sLg2zqDfKpMc8kjRGlwIhAOHcis6F%2BaLc6rnq7%2B4xssOC5k3gZsTDtElgY9lN2pLjKv8DCGYQABoMNjM3NDIzMTgzODA1IgzLWxgNnkYxzAJF9lgq3APbXS6Z%2BHIJouA8vdi5QbMgJP6jm4hFSfAxHP%2BfxzfLdIgvutARLIhf6CagAkgJit%2Bu6T8CXkpe05KtgGAgJGRQ5cC%2FO8YiXJFuSiUlTjActrpVrbGwuhd7fOtgM9O%2BhmKbgU97DoMxI2j9UOJkf1nQfAQ5Vxm37DyIQ06NolxDV4uJgrnPi2KcXVH4Vl9ahY5OUFFuIZ%2ByDJEZfac2vc4HrR46zeRVMpv5WfyS87hpwZ9kM17EtS220GRo6AfprWROz2KIzNNQ%2Fbg1B987%2FqYlNlJYj0I30O9DvJaa4lpWj%2BCKViwickfAAkZPZswyRgfMjGVzGauoxAKdIlZENb3o7s92fvHFc8zuTOyc31A2f8Drurk2jnPjv2Dxwc%2B2WpMGwov9cgUhNI7WpTD0MiBDizdqjRtLKA7ZxPFXQtJopv70KzoSIMyKPkVdR%2BWmpRHAsq0g95ioscEIFrKc6FLx%2B0%2BehJQv1ocrBk4m6R365v9xJyzqcwppCkMeue5zvK55lXOjECcw8uVFMcj4VJpU%2F%2FFw6uf6bn9zVQ73T5n4qzjHoy8Yf4gaaJjxJ4vXykP1H0MYcCTFjl6Vo9KtpNl1vvy2iWA0QTcuiEJTMm%2FaSgYbAPVF1dJrQ3fmOjCmuJS9BjqkASlXUBJyvISFkQgHY%2Fs8Cr2DfBeVyTcV0BO2yytjOr%2Bzwnyz8h23HWJp0sdyKQE9ivGviviwMjTDa2B%2FLbi8duytYxCdH%2BjpAl0%2B9t24mOOQzh2qJ5UcIC0H1J%2BvzwODFDXhfePkiOIX2DpZBo%2FxeHQ8wDyUYP9KMr7YNwnE3C%2BhkLN6AC6Mong2BOfPfjZS7cBfCVobgONHftYyMFKRuzB2A%2Bvy&X-Amz-Signature=fa57ce6f1020fe880b21938296a8bdc35daacca5375631d3d67d4371693c2323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
