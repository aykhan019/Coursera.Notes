

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ5ZISI6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCeXGjfxQDk77E7uzJtq5J9AnLr1M8BkSDdK1qm7sDolgIgSAdGetErQCznoOqggEQPyNQicHyc0%2BmOoCiIWrNUbpoq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDI7DIcIMDxLFBu7%2BACrcA%2FaZo3QpeGdK0MZXrJo5ccGnG3H1rFMky3SaQ13TGqWy%2FfxP5%2FYGKu7sKw5i%2Bfp2onS%2BXuXgqNcq6n39dMb1Tjg11EH7n%2F3EG1dKgYKiCakqod1Lb%2B2NovnrqrT3WO9z5Pfcdx1%2Fh9Q3ysPSAQPQGjCu9%2FObwgNve2r3%2BSE3FbX4T1FHK8HM0HJ2v9WFD89uunj%2BYcbDTMBaZ9Rt94jdRKSYMQjfrwt3%2FKY0rnpC%2FUXPc7AxYg1A%2Ba9BetVEhRFhhcWYivrRc6mgAyBo2XbFZuIFmsm8lNXCMDal7fKZEI23JMXcbZ8n6z9zYBxSlKzOZnJhpnuBaTt5kk4r34zE4RvkKmRKfXCOuCiu2GSUNSpNFdeCGAO4sd1oz1TDWdoSW10uZ1TZzS%2BikLbLIdWXmVZA6zRbdjx%2FINjMeEsTq62z8n9sXzpzCBAGG4vI41AZ%2BCXPoxbPhwuT8dEoAmE2w3wFAk3MS%2F%2Fg74hZC4Li0wCDg5s%2FL11Xseefg2OSdoVf2RnluklvDueMMAGGI8bc7q5CYlCnYAocAesyyhZBNr7YRfy8G8BGVFT%2B09g%2B84lic9iOWvfp5dO1L9Dc7xOoo35NAsTr91%2BzKdKnqZfPzDuK9WA5W%2F6ZmXtsXIEIMMzdi70GOqUBTf1XVj%2FvBGaQcXdcwcsrviN2cHFddwbaycuj%2BgUrJ3Lv%2Ffn4z2qg0HenmOtSciJJtpqgDnj5pqhs9faoZ5Xa71%2BHdNf4FkpLUgVoFh6qhM3tlJ7wzid7cepQdcyerUVseBYzPZgHqn4XA4E%2B8pE70VVby5Y0Ho3RalIYjOvPFGq2Pzfz3HzuIUrY6SE8cv7eLNHUweUQKuHPx7HDguHCd45mZDK%2B&X-Amz-Signature=5ae5f48fae68ac7fd5d073328d90a33fb4d12dfc4c980947c0f644e82f1be9ab&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTFPUO2I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIFPO6hbA9CKa6dJfKhlsRDsJ77E2yQAXT0VR9lp30YUdAiEA7w6PakwpFFB%2Bvys3VwCosA5BZZ3wlY4ge7HhIZ7zaDgq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDM1M088yaDPD6OrfeSrcA6GeABR9WQmdzPxeZ%2Bb5Ak2pcaAchT1Hh5GB7iCVf1Ke89G7ztPQVDEuQ0mF0TV%2FWcc4oe%2BEv9bawhKVIEu%2BRl%2FWIy3NWsrEuPOpuXdwrKxXUVW6tLYwgebcXXr5aSHGMf4FO%2BQBsNHZpGKd8egzQ0SrlRNgOWzWIe5Gs2St1nW7%2BEyVCj5qt3F2vmGHJWzTXohET3riNgA98KehG%2FMwWJwsQ8wSU%2FkC11PskcDwHpvVLwsWY2hRswaLQxoYxaEEuS3mjKwXTLj5Nlr4iXquUCfpz8iTeo65EeSEGXFY9avfm1FkteEclTrW2Af8QAXKuaCLMbbJIzE4jSnEqC%2BYTd3O1LJLsT2Xbl6OPqBrk%2ByhBiQq3318%2F3lDCAjdwuatXVLNSQmBaH9vBeCv1yutfbGntNJd%2Fd5bUQJk90HTW6LZs9%2BDrd9xZGL09xdZrkRyhMdFB3%2BCnkKuhHNkdyK6Woeakvdatd5jlNjkg%2FKUxUJcp2hXJlveboICWiJgZkOuXlXfJK4Nzsj6v0d%2Br49hogKtbAbFaywj%2FwiZguVaVmfrWUk5Eyib04T3LrGcIYmYfPbXZTzYiNNhqxeWfbEvgEHqsUs%2BAPbvfEVVfII5PZBOVoKLeunxo6PEBNxDMLfdi70GOqUBDELFssCprKi4ROL5SfyReAocT9fuNP%2FVH0inuSO2FxwDkmtubvqQweeO78bVRL4g2jWKKfJv9jscs7dlkyJG3YlzUAnA%2BfvNSHjNGbAp6DZVbRG%2FMEzylXCS8d5Yx3D1AOerAXflXp8pKFTWTtikbdRccjjyfyNN8fr78Z93FsT7v46m106nf2jzMTk8m%2Fl4VSX%2B%2FEHPYAbRwA4PdJl%2BBVI6rfgT&X-Amz-Signature=3c2ed3074765b929f68ea2ff530a1fd67b0c3f37312d0275cca518d7f3ac8f0f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTFPUO2I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIFPO6hbA9CKa6dJfKhlsRDsJ77E2yQAXT0VR9lp30YUdAiEA7w6PakwpFFB%2Bvys3VwCosA5BZZ3wlY4ge7HhIZ7zaDgq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDM1M088yaDPD6OrfeSrcA6GeABR9WQmdzPxeZ%2Bb5Ak2pcaAchT1Hh5GB7iCVf1Ke89G7ztPQVDEuQ0mF0TV%2FWcc4oe%2BEv9bawhKVIEu%2BRl%2FWIy3NWsrEuPOpuXdwrKxXUVW6tLYwgebcXXr5aSHGMf4FO%2BQBsNHZpGKd8egzQ0SrlRNgOWzWIe5Gs2St1nW7%2BEyVCj5qt3F2vmGHJWzTXohET3riNgA98KehG%2FMwWJwsQ8wSU%2FkC11PskcDwHpvVLwsWY2hRswaLQxoYxaEEuS3mjKwXTLj5Nlr4iXquUCfpz8iTeo65EeSEGXFY9avfm1FkteEclTrW2Af8QAXKuaCLMbbJIzE4jSnEqC%2BYTd3O1LJLsT2Xbl6OPqBrk%2ByhBiQq3318%2F3lDCAjdwuatXVLNSQmBaH9vBeCv1yutfbGntNJd%2Fd5bUQJk90HTW6LZs9%2BDrd9xZGL09xdZrkRyhMdFB3%2BCnkKuhHNkdyK6Woeakvdatd5jlNjkg%2FKUxUJcp2hXJlveboICWiJgZkOuXlXfJK4Nzsj6v0d%2Br49hogKtbAbFaywj%2FwiZguVaVmfrWUk5Eyib04T3LrGcIYmYfPbXZTzYiNNhqxeWfbEvgEHqsUs%2BAPbvfEVVfII5PZBOVoKLeunxo6PEBNxDMLfdi70GOqUBDELFssCprKi4ROL5SfyReAocT9fuNP%2FVH0inuSO2FxwDkmtubvqQweeO78bVRL4g2jWKKfJv9jscs7dlkyJG3YlzUAnA%2BfvNSHjNGbAp6DZVbRG%2FMEzylXCS8d5Yx3D1AOerAXflXp8pKFTWTtikbdRccjjyfyNN8fr78Z93FsT7v46m106nf2jzMTk8m%2Fl4VSX%2B%2FEHPYAbRwA4PdJl%2BBVI6rfgT&X-Amz-Signature=cc47a47173ba3d54e7fce2e9907629e188f810be278a2a6d33d8db60777f17fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
