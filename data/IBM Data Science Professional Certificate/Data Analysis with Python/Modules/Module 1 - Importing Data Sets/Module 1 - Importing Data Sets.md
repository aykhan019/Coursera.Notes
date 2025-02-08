

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ZW6AX3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIArMuZT5zylUeyZtvc67LTCBQYLeVeitNDwGpoPoTfpjAiBaAhSmIClYWtr7Q3Jecjgm4hwq1fArXrKOOiTksMcfpCqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeurCHhd4NxN1ltHpKtwD1Afow86p3O3vBbm7muTsEv77HVxQC0dp9%2BWbuQCCxDw2JH7%2BbU2sv5YuHsozTDPsBFdSr2o4Kk3eEj6hnO6cnYjfkRxOuoNfyX%2BFL97PZMmMsQ52lRJrBG1%2BrxdGlJuttr3lnlJ%2B2Gfr0zvVrU6OiFQ39lcyukkOy%2FuZImIfbLMgJ3QvM35nJKGI99am0LFW3Q4UsrSDOic8A%2BoLlpNagN75G35DRQj9VZdK3xSQK%2BYLFI8w57kBZfeTa%2FMqOnMCg6IuMgZJgwTeXffjH6TG%2FAe%2B%2FINge%2FeNDoI1CTCHcStg%2FGW%2BtSqhCw69Tmr19FlHKo8whH5D3XaEQSsH7PCMaS6kc%2FtRAqPihQOcygCTZ3r7WbE1VXd0ir%2BYffXmeL%2FR44xYQsmUg2Xa%2FPdirAQpe75Fo9ei8oIqFZUZXSgiNWPGNQrqxYmTcWc%2FYwtPcIyDl8XoonXpqO66%2FdchTdKEfPNTTcekl2y6mXd2L0Oc23KrdX%2FW4AWbndyEOqjJhNKqvBjnw7a8YPDqZlMQ%2Bs9lElNbaIbf5%2FIt7eZcL8IhMXOoVF42j85G%2BcXDl%2FhYMp4Na0XBCsffbZ1%2Bnn35m6tX0wF5Q7n2RMNonNWPBpTj4b0PHkM%2B2FW5MfoqXF4wjtSbvQY6pgHmAuIzDO1Xzxob869AuwVBFRMQIfotp1CL9PTar7cOQ0h9NNWJH8A1vutz9R06cScNliOgFJQn5pivZMy0Ybh0KYg1piKvy6mv%2BQ6Xiqza7o%2FIba5NNaisy9jQzLjSQgcNzvTr%2BlW7S92A5fqrbmnYHqs0QEA6xqUE%2FFYYVP%2BOQP4O6oiHssJ98pLyaYEQ7VEsaInW%2FVjv7dnW8YUSwRM1KCRbkoLi&X-Amz-Signature=f91f745d3fd2c04f7a49ec0428b2cd489cc453144b3705c2f5f9485d59812dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIMPEOWA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQDZnZaU4VEZ%2FsPtdwAc3sv27ryrQeTYhHIdzQb9cvijyAIhAOY885FMJLXAXZIpB7uYO4Tc%2BAAMOZ46RjMm7A5x7tgRKogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwokJRjUh9D2pdz0soq3ANnBtpoYDaM%2BmR76H2ErdkkKQPrPUxXhYD20dE7Ab98gy0lqPqhmiK87cZZNWRkPSFEki4OYOMG7riCFztNfSc%2FfpNXavLhklYgorJ4uO5Ef5r6wB0ZCzBN3pLNUo5zirAkD07fEJrPSVdRokUgmxv5o5k%2FUbpBC8ZTSjZrGRhAFchpHDvtBRKTTiaVIIZGQoK%2FOi7WfRQm7%2Bnf%2F2YrQVA3ensfdHEgim%2BTeIWuU3Uk%2FKb7vCWYznGI1s4OXKN9F%2BfopYVdxGWwHnOv49nmTRl07KwbE777lsh08fJq4G2Kwj%2Fiu%2FHL7162Vke1bADO5SsN3N2FZfn0IgspNXgzAKOvstZTJw%2FRgTAdFVTNsUQmPu5O%2FbMKx3fwi16pGT5vRPgG9zJTLwU%2FVTx4ADLMdHy4C8INQ9N8Bg87RDeNuuTQk9A8HpgM4wpj9fEpfiVWzVMnGZWbyV9xlw31DGf8mRdVEbtzi9kAvKcI388ThZnxelsJwCqxOMmTPaSsX9BxuqARIcESyfi0Lydi5D%2FOH%2BHfnv5Yuk5Qg9b%2BVsHJtNgYrkd4Ed20aMJaf01WlhI0NLxqHmxsQPzmN8dPSLqcXRhsw6EGV5ilAaLnixEvo2IMLsS2eRHu%2B%2F%2BKQpQgkTDL1Ju9BjqkAUXeVY4y4Qt5luRR2B1uv2Llrl923ONKNtFy8JJYqtwB5V8n%2F%2B0eyXjMYLuGFF99kBDJwd8VrEttmfsMKQlej%2BL9Vb%2FwK7pMOAZHeWNmOtOeqZiqo%2B05NaXxXjXID2cx8yPHMjZuPCq3jwH9Ry41RHE7l7Kky2es3noTNSxyNjVJWJvXF3U%2B2GUcIGbfWu1igFE%2BJJxFYyDGo2iMMR5XjQXn030h&X-Amz-Signature=09b29d0df979af56af4c335ed81c73e503ebdee33b5bc53d4f39443a089158e7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIMPEOWA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQDZnZaU4VEZ%2FsPtdwAc3sv27ryrQeTYhHIdzQb9cvijyAIhAOY885FMJLXAXZIpB7uYO4Tc%2BAAMOZ46RjMm7A5x7tgRKogECIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwokJRjUh9D2pdz0soq3ANnBtpoYDaM%2BmR76H2ErdkkKQPrPUxXhYD20dE7Ab98gy0lqPqhmiK87cZZNWRkPSFEki4OYOMG7riCFztNfSc%2FfpNXavLhklYgorJ4uO5Ef5r6wB0ZCzBN3pLNUo5zirAkD07fEJrPSVdRokUgmxv5o5k%2FUbpBC8ZTSjZrGRhAFchpHDvtBRKTTiaVIIZGQoK%2FOi7WfRQm7%2Bnf%2F2YrQVA3ensfdHEgim%2BTeIWuU3Uk%2FKb7vCWYznGI1s4OXKN9F%2BfopYVdxGWwHnOv49nmTRl07KwbE777lsh08fJq4G2Kwj%2Fiu%2FHL7162Vke1bADO5SsN3N2FZfn0IgspNXgzAKOvstZTJw%2FRgTAdFVTNsUQmPu5O%2FbMKx3fwi16pGT5vRPgG9zJTLwU%2FVTx4ADLMdHy4C8INQ9N8Bg87RDeNuuTQk9A8HpgM4wpj9fEpfiVWzVMnGZWbyV9xlw31DGf8mRdVEbtzi9kAvKcI388ThZnxelsJwCqxOMmTPaSsX9BxuqARIcESyfi0Lydi5D%2FOH%2BHfnv5Yuk5Qg9b%2BVsHJtNgYrkd4Ed20aMJaf01WlhI0NLxqHmxsQPzmN8dPSLqcXRhsw6EGV5ilAaLnixEvo2IMLsS2eRHu%2B%2F%2BKQpQgkTDL1Ju9BjqkAUXeVY4y4Qt5luRR2B1uv2Llrl923ONKNtFy8JJYqtwB5V8n%2F%2B0eyXjMYLuGFF99kBDJwd8VrEttmfsMKQlej%2BL9Vb%2FwK7pMOAZHeWNmOtOeqZiqo%2B05NaXxXjXID2cx8yPHMjZuPCq3jwH9Ry41RHE7l7Kky2es3noTNSxyNjVJWJvXF3U%2B2GUcIGbfWu1igFE%2BJJxFYyDGo2iMMR5XjQXn030h&X-Amz-Signature=899fdfbfb709aeebddb0eabed516f20c26302c6874d673d2eb7ea426228736fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
