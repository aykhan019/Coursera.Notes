

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJ5BTOXX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDVWtSSqa03xCYA9EtaG%2FG4EPvvXPnHiOCatGnMEmvzWQIhAPNFo1boZcEiZvsV8naSrJDfgEKfPjq6waTS2pFhmM7aKv8DCGkQABoMNjM3NDIzMTgzODA1Igzj%2BL6irA3lrWkwFMsq3ANRv01TPL1karYy1nZZpxs%2BQ8RF%2BYhWY35sGf9cS%2BstbVXLqbxZsiSAUVEh7cZwr9ctmomaXXBzbElWM5E5X1Ai6pPnM3TcCEXmgV5dh3KwRY9CA2NF0jB5Mp5P46j3b6eEw1uu7YUn4ttOgTDNdVwodPB1H64IzEhbN1aJvxP5rBuLPFNC%2FTfwReTf0xLun6LnSu8W%2BuVY6E13J%2FH1ZId%2B3y1eolFeDBmgEGC1oHS2NEsPoSx5JhHBb73QIE%2Fo2842iu38XyfGuL6das4daIexVJ7UYbGEuc2uuUmwkHQX1eGHn3CUimW6g8O6gBNjlxxtyOv%2F51CnXSf3kRSoIrOfCYUVji6V%2Bn4kJWpYTR%2F7sXVlchm1PTgvAaArBHFHgULGeVzRs2BqeDoLPGNRvsyLq%2BOibLcbq9egbZ2Yp7CrUUylY3hMBeNjeFPsvFc7WG9Tp5zmCkvtUJ92ds306%2FTarDiU6IyZUbyHNYHcrLAvuCK5WZnRBPUz40oBe3RjF4iuwiU8nW0Zyx8UJ4YsfHXMh5v38g4vDtPmAzwca82FSs8Jqr0K8J28CUZjOO5%2Fx00w2n8Fa%2FUQWovkYXMUbn9fPuFHyYMpd6PH6XC48TssRslGqRqeS4yaxN%2BmKTDkmZW9BjqkAWDodLWVFdYwt6THaWo7jfk78tAGwsNkxmYaWy2tUhy%2BEHK88p8B7a6rWh83FFhdlr6Lh9TarcTSxEeZrne%2BueeJ%2FndGelAnH4vdKmLGe%2FeRR59YgP5OlWj%2B0MvdVtKSf3ftM38c%2F84VLFzOzYcrEHdx3xh30Rw%2Bb6t6jFlS6k3ffqGgo1d0NX2KJjMIFdCQfb7llk3nLlsdQjJp%2B1nfmNbOve4X&X-Amz-Signature=898a497cb0d2cedd700d451649d30892ef3586799e020d0c08915e860e636f67&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U2FH45E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDzL5S7zQuHrgTjtlCYjIy0lnpUxxzVMZ8oMbtvI%2BnFIQIhAIwsnsaZbLJ6HWxJkIvx6V0IjyPn%2BpN%2BUbcBGZZzsd88Kv8DCGkQABoMNjM3NDIzMTgzODA1IgzW8UwDcgziFbllPr4q3APz%2FjYBk6WwNPuoQ5UFULxrm2O4e60SzMXr0RUHqDMxTJbzxgWifQqwp%2BYIk7ncYmqhVaps0ndmUyd4Dw%2FNjm0MvUN0HccItzxGeeuSv3hXjhYUv%2BGbXXIvwqCDSwJMbyryXpbmIUuyyS5kh3O498Ke4bqk54iA3lIAQoIeqRj4NJYIAcIzTobfCrmNKlbYDT9Eu2BDspkRZjiGMz2psy6pQJa1xqfsWPuKOh4Hlv35fkMm%2BQcWZMk14riJSkvLBZwIG%2BlulG4PmCtZBQGlGi2PYD5e8afVU5se8Kc2wOmQ6mO%2BFpxX%2BFNCjjoMtvS0lI7nOW22gfS4TviWSoMDMN%2F%2BysC%2BKbfYRrvPrzkvdgH5WrxKzC1pEMWztPcAJojHIxmuqwUIvLeSHAsl5S7mH7Sd3P9EkSxJWK%2FP%2FVddTdyPRW5Ux4O9zUtVT23fxusBhlzC3%2BfUq3txIRGyePXOrkkjVrmFXNz9zo%2FgB%2F3PaCOq3%2Fz2D%2BJddYK64vVfX37lj%2FDRKr4srZk0Bvgv1bl%2FgJQadDyM1fjXqllZU%2BgWfwjz5y%2F5%2BroDIpOEZoql4%2BIAjcyeIuzzKtlbeuPRQp8HbE%2FPuFyfQgZmarFRK6LVgRfxN4m9%2Bf77FJxE2cXPtTCjmpW9BjqkAS01pwe7sJR9AR7laPOx7FCpgkJOe7XZyiq0vAHmk2JQ90Baq3v5PlIgPhpgRmSE75si9SCHDrY4coMgMR8fGugOGUM50mD%2FNFOLu%2BrwerZ1wc33ZYCybGcK5nskWrHR%2BiKbk1V%2BXzJOmkgZXLhcfHWUC3TpJrkzVUm4ja%2BVBBAkSYKjl4lSQ7XVV6SjZi37mBgEMEDANQXOMkTZKJXSmjZ9Z51N&X-Amz-Signature=936eeae71d60f8182ab639fd8f511426e5055b796457979ac7e34f645772fdee&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U2FH45E%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDzL5S7zQuHrgTjtlCYjIy0lnpUxxzVMZ8oMbtvI%2BnFIQIhAIwsnsaZbLJ6HWxJkIvx6V0IjyPn%2BpN%2BUbcBGZZzsd88Kv8DCGkQABoMNjM3NDIzMTgzODA1IgzW8UwDcgziFbllPr4q3APz%2FjYBk6WwNPuoQ5UFULxrm2O4e60SzMXr0RUHqDMxTJbzxgWifQqwp%2BYIk7ncYmqhVaps0ndmUyd4Dw%2FNjm0MvUN0HccItzxGeeuSv3hXjhYUv%2BGbXXIvwqCDSwJMbyryXpbmIUuyyS5kh3O498Ke4bqk54iA3lIAQoIeqRj4NJYIAcIzTobfCrmNKlbYDT9Eu2BDspkRZjiGMz2psy6pQJa1xqfsWPuKOh4Hlv35fkMm%2BQcWZMk14riJSkvLBZwIG%2BlulG4PmCtZBQGlGi2PYD5e8afVU5se8Kc2wOmQ6mO%2BFpxX%2BFNCjjoMtvS0lI7nOW22gfS4TviWSoMDMN%2F%2BysC%2BKbfYRrvPrzkvdgH5WrxKzC1pEMWztPcAJojHIxmuqwUIvLeSHAsl5S7mH7Sd3P9EkSxJWK%2FP%2FVddTdyPRW5Ux4O9zUtVT23fxusBhlzC3%2BfUq3txIRGyePXOrkkjVrmFXNz9zo%2FgB%2F3PaCOq3%2Fz2D%2BJddYK64vVfX37lj%2FDRKr4srZk0Bvgv1bl%2FgJQadDyM1fjXqllZU%2BgWfwjz5y%2F5%2BroDIpOEZoql4%2BIAjcyeIuzzKtlbeuPRQp8HbE%2FPuFyfQgZmarFRK6LVgRfxN4m9%2Bf77FJxE2cXPtTCjmpW9BjqkAS01pwe7sJR9AR7laPOx7FCpgkJOe7XZyiq0vAHmk2JQ90Baq3v5PlIgPhpgRmSE75si9SCHDrY4coMgMR8fGugOGUM50mD%2FNFOLu%2BrwerZ1wc33ZYCybGcK5nskWrHR%2BiKbk1V%2BXzJOmkgZXLhcfHWUC3TpJrkzVUm4ja%2BVBBAkSYKjl4lSQ7XVV6SjZi37mBgEMEDANQXOMkTZKJXSmjZ9Z51N&X-Amz-Signature=9f24103dc3dfba62793746aeabc7a73a977e7b169c2f357b19ba264369b8af79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
