

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWMJEF2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdMAEgeIziZlulFNMOFyI4NVODVHZjhuA0w5rDY%2FgnzAIgDBUDIjTvr1ym61LOIcdFZWJ79LmC5EPn3Kdkfp96ad8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLWwOLU%2FrNE7JOmPircA4nAECu7J6O%2Fi9x%2FFkKPOZVCIV80jbIoIRJfqRcMkAQE7NXXUKhid4LBIDX3Fme6DGlLtCrHD2Waa4TL3I%2FNkg676C5vkh2p1EZK919aoc3fP2lgno3lEdBAeHl0P95uH8M1HcBpHVvCPWvN9vIlOnHLQblftDw5gVRBbyZade5dUHoFs1f60qubm%2B5uxJeKDtqfLmMKd5HcWBBS7tFEGQZgZdnyRNGuAhZv1jBM%2BjrCd6JPDW4k%2B9YmCHoZF%2Bj3C7EW9OdOkX2NPxwOcCpiuRooA5rvUKsX8pBdpgpb6482JhHRdOMuQG%2ByY1GxGKadsJHSzs07%2BcPqlw9v52o%2BagSdZp26Ei14TvZD99W%2Fg3%2BgbZzehILuG7cAbKs6xPHtS3Ihwis1i20nduiReyAWkaTp2ZCbOxPAQxUGRPzw%2FeivxnWPH1QMVIgSxtQ7fKB%2FklAoI8bCCnBA1ZEV%2F63LjaTUHWqXMtu%2FsvzHCCImgIMB1zwKpBOupHWIHnLEUy3FelWxGNQsNAG7wBaEN0et98fHLoOFTX%2BVWpagEZSZ0qPIi%2Bj3cXgNSgwWG%2Fobt5yFN5gAHvJBmlDo%2FFOmNEdKbRoSW%2FS7tRUD80PCwrRKDpu1sVLJJypZ2LdDk5%2B9MKKc%2FLwGOqUBakdtpeqlK893a5p0uimnyf2FoHf5sBylwaE5VZaKwKI41a5AOhbpP0g4PF2j%2FRwmkFf0xnnsDDOQpgaVoEs4rPyJShUaesAPQNUl4clreN8GOPWuiyrd%2FxwNSfRfgmBS%2B458ij1etFw%2Fmgh9cWuQI5roYwHAg%2B2j%2BNCL1bJVD%2FmA%2BhjiO311TgLg8DqjeC%2FdvrmMftac8pnBvHyhyePYAe23gkSq&X-Amz-Signature=9533a842800b7b93593c5890c79c6949eacb43600b840942b02fd2169f0355a3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EMAWOIV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2YtvMQAzIrlYb9Sk%2BlntIr1vJBLKavxgUse17bzCimwIgAh6B9abGszVfA4b6V4Mx8Cg%2FblIaQ2YeJupE8K6hrHoqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGSYXwLpshuILZ5sCrcAyDjrt8vxjWyr4kLxf2NH6rmYbfqMmyvHvIAsynvnbtDoAtaLMZsIBJg2QTdjubcIzlZ%2FHXqPgC%2BkEt4SXc4vdB3UBUnStEKFK31hESQC0JzrnLVd0nLxFx9%2FsI5gr29F8EHP%2FGOssxKvY1aWqihidmUOIkzIRN5qzmyS9jzPnCgWzZJWkEgG%2FHECA%2BhJGmhDWe%2Fx7%2Bpw30CgPgtH889PLdaqGdYc60vwDJrt0ZOFdwVApscPPt89N9p5quSIOQ526lLSy01tWSbtlNbuaT8eCgXQwBh95ZTXqjZYFTtTaoTeWRw5BZjti0Tb8L%2BFkBR%2F0W2aVffEcrp48WdOERksKOKF7gj1X1vCyWqe7h5S6m7RsF1PBtPx%2FlWRnpJDs4pTuzRlCyMJewInXF14f2gwjp3P80jsB1eLWkcy7SCDReSP81Jfkio4GHRMmQVddYTBoAYt5c0RKh88JleqB1flaWekb%2BHhR9pWMKDpXPzsXsHfl%2BSbCPjZfbRXqsSoJaxTJ2uhGb6UNrMsHTRFP4fSjUllqAE2ZmjtcsV9ipZbJZKIZe%2BrguisJNiZs60hkQh4qsG%2Fkdj0iM%2FxQd%2Frm84ch6T5WmyObN23%2FOqqIufeDMBupWxQrC19zAssQpGMJec%2FLwGOqUBuw9dt5kYR04Z78TeyFUcPq%2BTnZrSOmG4OrH9R%2FWhxcLa1RthufwIeE0stho%2FwsygNcLxtuX8F4nBeyC%2BYL8BdALcbsxJtCZu79BJHiHd0XdYj9vnLYXK%2BIy5Rw0ZqpNJ6nj1HGhqAKURySNCdunXwE4X7u3CJZFUJ0IM8CIIqtBkK4B2rgskijveiitjaxDxY7w6%2B4QztkGlFxhq3rHqKArznZcy&X-Amz-Signature=9b41c16a6e3c334d373137171478ea56668fdffae097e9807c3b3938715bb893&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EMAWOIV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2YtvMQAzIrlYb9Sk%2BlntIr1vJBLKavxgUse17bzCimwIgAh6B9abGszVfA4b6V4Mx8Cg%2FblIaQ2YeJupE8K6hrHoqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGSYXwLpshuILZ5sCrcAyDjrt8vxjWyr4kLxf2NH6rmYbfqMmyvHvIAsynvnbtDoAtaLMZsIBJg2QTdjubcIzlZ%2FHXqPgC%2BkEt4SXc4vdB3UBUnStEKFK31hESQC0JzrnLVd0nLxFx9%2FsI5gr29F8EHP%2FGOssxKvY1aWqihidmUOIkzIRN5qzmyS9jzPnCgWzZJWkEgG%2FHECA%2BhJGmhDWe%2Fx7%2Bpw30CgPgtH889PLdaqGdYc60vwDJrt0ZOFdwVApscPPt89N9p5quSIOQ526lLSy01tWSbtlNbuaT8eCgXQwBh95ZTXqjZYFTtTaoTeWRw5BZjti0Tb8L%2BFkBR%2F0W2aVffEcrp48WdOERksKOKF7gj1X1vCyWqe7h5S6m7RsF1PBtPx%2FlWRnpJDs4pTuzRlCyMJewInXF14f2gwjp3P80jsB1eLWkcy7SCDReSP81Jfkio4GHRMmQVddYTBoAYt5c0RKh88JleqB1flaWekb%2BHhR9pWMKDpXPzsXsHfl%2BSbCPjZfbRXqsSoJaxTJ2uhGb6UNrMsHTRFP4fSjUllqAE2ZmjtcsV9ipZbJZKIZe%2BrguisJNiZs60hkQh4qsG%2Fkdj0iM%2FxQd%2Frm84ch6T5WmyObN23%2FOqqIufeDMBupWxQrC19zAssQpGMJec%2FLwGOqUBuw9dt5kYR04Z78TeyFUcPq%2BTnZrSOmG4OrH9R%2FWhxcLa1RthufwIeE0stho%2FwsygNcLxtuX8F4nBeyC%2BYL8BdALcbsxJtCZu79BJHiHd0XdYj9vnLYXK%2BIy5Rw0ZqpNJ6nj1HGhqAKURySNCdunXwE4X7u3CJZFUJ0IM8CIIqtBkK4B2rgskijveiitjaxDxY7w6%2B4QztkGlFxhq3rHqKArznZcy&X-Amz-Signature=44b6fd2579f6f446d147411e0ab3e3ec1db77a1a86286238096c4edd486a3b05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
