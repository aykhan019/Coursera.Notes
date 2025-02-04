

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AD3PUND%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIEz8Szm2beziPDcjAjfkkEbrpixM7QLyJwa6BbloKi2BAiEA6DxwPu%2FhL7W4mjY6ywmBdirK8NiZGjjnf41ccFZKRPQq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDEFR%2BLDkrrxW%2FYToFyrcA1JAUAlvJWmY2to4qXyqq39AoyMT4Dw30l%2FK2JcYNX5vd2DhkRF5OwjSaCsci%2BUplJUL0eunViqWWR8kRLjZA7Y7Z5u0GuhfOJ%2FW2rkzSlTDvR5U9RdfDUVGWh%2FLN16qADc%2FYkkjGfywS7pMrUC8RvG78J9zJcohI6q2yfeP%2F7WF62P%2BHHPYrDWoDZgAgeBKS4uF8m6qEN%2Bg%2Bd0AYVIQxe9YLaoLxlbmhmOvsalsrSvAsMcqVjFwj9afVTYC%2Foa402%2FhtpRutnHl3nVgAu8NEx5A9myXuh1JsGsDxHmFJjMDkU3mb3%2FBSOZJdoWy6iGeil9vZ8pvdMPCyg6qpQvglYFNb87uVMNlampHRXVt2PoLuiX4XnuQLBlrT7uT3lf7VXLOePKEFurJkOwChK9dfE7ni2Hz8hQmxEdr5jd29Gr9mWI89mGXoS%2FyMzgswY%2Brfaa72IsRfdxVMCQ%2BTSri5ROHNPFfOBnogScTrB6wD7H3%2FIqrr%2FzGlXzv%2F%2BHHaIbfcvif3EtANh9lnguge1VaYUjobbmV2823Q3hVNq%2FiYciQsxnoovzZh1TwG%2BLzzuffS2Wu9KosFsnSzAsc2H93Tbu%2FcaRVo6ONr89FPM9NWFS4acpNm6eHm3Q3ByhPMJaeiL0GOqUBDiSo6zxqctls2alJXVXlJbkbUTw6og6leOBUXNUl%2BebE3PjJ7i3P5Ni%2BZiYLc3L4cA83%2BoQw6HiZPprVFGJIJLxLGC97vJzAIfbsvIllNI3Jd%2FLzx%2FiaTY5wwM5zEIhhrZcL2BXqq25qG7wZofVwgEts8S%2BXADZfqSbL5zwjM%2Bhz3oWiYOnCWAmY5IKKN02UpeaHEulrVngvg0BFp%2BLsYoy8Scw9&X-Amz-Signature=f94613569f4225d78021008ce9ed2c61d0909fb17a04c8a3f74f9427e99842d3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654LPIUMK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCtztJL3skOBLlMTwQWRINJilExN2NMoTN2%2FZ1byoRxPAIhAMMgDK6oF5MG3EYwA6TfuHpB95oEZGIEyRIK1PKOTfY8Kv8DCC4QABoMNjM3NDIzMTgzODA1IgzjHUzYq6F4YVfDJ2Mq3ANhyaSuZ2W6i1sgC09eZKKCp0qFxSELn4RdgNSeiJ6WsZuPpnNUtf3gaLgtMx%2FSdaI9GC1acuHOAIaANVGjdTNfPcra5%2BfA5D3LLq0jJoyxDywZzt6%2BCKs%2FaWONUZyLZLV00HgcaX8fGauydnBQR%2FYR4adr0LO8rXbiIav%2F1VD4LxGyO9gRQu0rySG0xwgpHA9lPfVcLpF%2B4i22ZnZZnYa2Sx5BW2GW1HDFLegrOgKbifLGLFdvj%2BJ78Ewx9jG6zYaO91HonJ%2FGqaoVYxE85O8Tlmv13eH6L4WAH247zV1tIPapicBK8DeylNheluvbt1GRTO0NePoB9nEcP63m9JDCxrfBRoDy6s2Ib7qHoUflXDwSCQahz2qVTO4XE95MhIOeyKPbJVjQD2XNukWccSwIduPxHscHj0INOh3QzuG4fury5Us%2BHKGTfeDGAlG9OzH7FatqbbGLGi5Wlu76lgsBkBHms4anVoZ3lnY9CVkSMKkHYrYgapEFOw6SgRwyV1HW5iMrMwPhYD2rV7OwgUce24LTUJa0gb04W2huHAoStfIuLdrztuvJPzc4qYO%2B%2F%2FYVDtOXdRUSe2BJnNJDQQRMssGxP7nKgb%2BvLodCgRCd8xsGgZDHIcv%2FPWHzNjCYnoi9BjqkARJjOgFVSLHTElehi1jpFiz%2B5aQsCxrXF2bx8uylnFPaS%2Fgf3UCotEHFsYEWVssCB4CX7KZzg%2B9MMJWuSBWEPBdtI%2BjbuZ%2BMMvYuVCfa1ZDieTiLeZqutxDhKpWPXwqmB%2Bw5kT5RAeWvbOu%2B9D5egOmur7CpP31DATtMeD2O2dlDdkCVCd6bFSf82lx7UACQcyaqTWPgodydOngkZY1fQ5KZkSM5&X-Amz-Signature=4fb1fd00130e7a179914bb6698f73dacfcb91cde3764acd8942908c88de27740&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654LPIUMK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCtztJL3skOBLlMTwQWRINJilExN2NMoTN2%2FZ1byoRxPAIhAMMgDK6oF5MG3EYwA6TfuHpB95oEZGIEyRIK1PKOTfY8Kv8DCC4QABoMNjM3NDIzMTgzODA1IgzjHUzYq6F4YVfDJ2Mq3ANhyaSuZ2W6i1sgC09eZKKCp0qFxSELn4RdgNSeiJ6WsZuPpnNUtf3gaLgtMx%2FSdaI9GC1acuHOAIaANVGjdTNfPcra5%2BfA5D3LLq0jJoyxDywZzt6%2BCKs%2FaWONUZyLZLV00HgcaX8fGauydnBQR%2FYR4adr0LO8rXbiIav%2F1VD4LxGyO9gRQu0rySG0xwgpHA9lPfVcLpF%2B4i22ZnZZnYa2Sx5BW2GW1HDFLegrOgKbifLGLFdvj%2BJ78Ewx9jG6zYaO91HonJ%2FGqaoVYxE85O8Tlmv13eH6L4WAH247zV1tIPapicBK8DeylNheluvbt1GRTO0NePoB9nEcP63m9JDCxrfBRoDy6s2Ib7qHoUflXDwSCQahz2qVTO4XE95MhIOeyKPbJVjQD2XNukWccSwIduPxHscHj0INOh3QzuG4fury5Us%2BHKGTfeDGAlG9OzH7FatqbbGLGi5Wlu76lgsBkBHms4anVoZ3lnY9CVkSMKkHYrYgapEFOw6SgRwyV1HW5iMrMwPhYD2rV7OwgUce24LTUJa0gb04W2huHAoStfIuLdrztuvJPzc4qYO%2B%2F%2FYVDtOXdRUSe2BJnNJDQQRMssGxP7nKgb%2BvLodCgRCd8xsGgZDHIcv%2FPWHzNjCYnoi9BjqkARJjOgFVSLHTElehi1jpFiz%2B5aQsCxrXF2bx8uylnFPaS%2Fgf3UCotEHFsYEWVssCB4CX7KZzg%2B9MMJWuSBWEPBdtI%2BjbuZ%2BMMvYuVCfa1ZDieTiLeZqutxDhKpWPXwqmB%2Bw5kT5RAeWvbOu%2B9D5egOmur7CpP31DATtMeD2O2dlDdkCVCd6bFSf82lx7UACQcyaqTWPgodydOngkZY1fQ5KZkSM5&X-Amz-Signature=ffbabca33737994710dd6a75843c5f93d1a5cc20a42f381a457cb48b678d02b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
