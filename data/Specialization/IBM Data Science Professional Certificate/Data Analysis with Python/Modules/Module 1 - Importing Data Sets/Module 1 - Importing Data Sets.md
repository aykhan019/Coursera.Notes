

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CHPA4XK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAODWccn0IZx4AT%2F8k4ea3gAR6duthm281y6tmqH8FlAiAdmjuS1xgrrfyVDcsjyBUWuyLMWU%2FS1GgcW78eFbQRqCqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIFNp96CCuYO4ZjCnKtwDkSmnAiyESpZ0dE3XNenfretCfvrz7FH2eQeD4xzVR5YnEVUA7Oo2lqzsY77rWDpV6DLL0uNxj2NSVpmai9e6D%2BvOXSIjAQWdQwaUWdAQvKWAzvEE1HGCy91MTqzuw2V3BqD8QisAbaMX9eGRywVkUfFT6eV1%2BaMA6YDV1daCMl2T%2FEbbpQ%2FVrMbHxMNqUTVpzO425ZTWenTJra4oGsESLr4D9SUMEhHj340SAa5cV%2BjYkjPdp7NT%2BroQy17RMKC7Cq1NSVPHQaP9tHclvSlIFpxbEYKMIbINIOjvn4fQalFbZ9k5Ho1lcY7Cq33y6Y7b1NFeSJOGSVIUGddzXkMNUsBm9ZFdFP0odGBL1wRqaOPsBTiBpFjV5RshW669C501jTB0hStm7ZIzEWiBFcQLJ0GjbP5Jwg%2F8g1SWeu5mS0yuKDc7vh3Lh9gH0d5yX5VCD6B%2FI8nd2Bnpvyj2sKtLaQKdPNTjl7BQE4piFBaTB2A8ccsvDHUtzCbsbxyqBshml3cFSq55ecPOZY0crJ0MA87MKu5g6rpWCcSXeVaLEH%2BGCXgHkRcjB6q8qYH6146KodBkirx4EGXlJLWhXMIRcpdfFvQSLXJxCyGTyC8CTnt4OvQkDt2ieV4qKZMwmKPsvAY6pgGvyhesi0mdNncI9Paj8aDnDsZQB7j5rfTKrOG1DxdKJInKEfEl%2BiiQHmbQtw1%2FgaObc9j1u%2B0aWJzUYF2pgsfgRsWEeZNwSv6T%2Fn8osXhj99jPs70kLbXK2sbDIOURKG%2BbZ4Y%2BugY1P8iJsP8Yl8zLGVDmytJhUAlgl90cpwvFV%2FOfC1YGc%2BSc5XEO9ujcWeLph5xZmD2dVvMMBpmhxkUWLvL4XPPr&X-Amz-Signature=49dcd4d42940d90ea53fb5ffe1ad60683f1e4f2b3ea29d125664eb3cdc70dfed&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUMXIIGW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEDlQQYfvteWImAnSRXG1isqJxmWRBkwWsrXvjDsE0SLAiEA8PpqCM0RTdYaRtJjSDkEy6R5VNAE1r8cABfC%2BeCsiRMqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHlwa65PtCDMsb8i6yrcA%2FF09PE1PT%2FzzNfnJqQKtxjav8GsHlsLzWPwYdEZ0ksI4XabWt6%2FrImpbGlONaU1IJ49mw6w5wIgwuKfbASxVTTA9tcNOLozLaPWWOCtZC6BrOzNAT9a1ip2EzYGvcHHI45p2B7GBkx1GfOWXrsdshNvtOCEfjO6ZpO6fZod8GW70yIs5rfXuHugzqtgk2iFBkUWXm2Bm0Y1xtwMV%2Fgli8TAHxsMRxr3EpvZmU3ejILxC6oEi7BIp9bbcuoS9eAf7NTJtEQ8Yqp0AOW4d5yQ9FVvUU2bzBH22OCX7V0MMzFNFWihCEku07zw4Yr1lW7wSdmfUNotYbjRs5D96hbiQAi7F7GoJ27mpb0KRrb5oDt5YXJaCxmbbKsREfhT9mPtR9oJPn2LcwieFY2wfdl6pprs%2BDQGCPwFgQek9wujUxWL%2FTM6hUjbvdPO%2F88KPePNAEIclIx2YyyNTY8EoTL%2Bxxb%2F%2BvtSO36OsA05Klcf374jGSC%2FPMolxng6avw0mT5ZkvBe6xHzwgbsemOgOQzMCBzX9cMck%2F1rqOTDUbfsw7QnALQC11MwPChr9w8CgPu2K4EHrjQ1uH7GVMBinzXHXQ8WYtS2hLKzohPTY4DKxpLOKx%2BIV0Lc8dExrRfXMOSi7LwGOqUBWSYx2M5eRS1%2BXLpJwAm5ABNi1KGvyM5pFzmSP3l%2FyYn7j6PHrneA%2BjUPjbe8bPWbyINnTTZDe8fqsdMPe%2BvZtlR8s2OpqDNf7uc2UFO7XNlm72FYK4X%2BxQJ9E0F3mfLK7Hs3uhbU3gGuGGa3ha9YV4cJyP7T8g4NywibkU9cyAADcyAUDMScI8nSjyP5pd4z9C%2FKdpfXkvdTEwvb3%2FSUU9qXP%2BoM&X-Amz-Signature=c37dc5af651b8e239c679a78646a0c04925fe6ba1f85aefe7f4a3f73137f0248&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUMXIIGW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEDlQQYfvteWImAnSRXG1isqJxmWRBkwWsrXvjDsE0SLAiEA8PpqCM0RTdYaRtJjSDkEy6R5VNAE1r8cABfC%2BeCsiRMqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHlwa65PtCDMsb8i6yrcA%2FF09PE1PT%2FzzNfnJqQKtxjav8GsHlsLzWPwYdEZ0ksI4XabWt6%2FrImpbGlONaU1IJ49mw6w5wIgwuKfbASxVTTA9tcNOLozLaPWWOCtZC6BrOzNAT9a1ip2EzYGvcHHI45p2B7GBkx1GfOWXrsdshNvtOCEfjO6ZpO6fZod8GW70yIs5rfXuHugzqtgk2iFBkUWXm2Bm0Y1xtwMV%2Fgli8TAHxsMRxr3EpvZmU3ejILxC6oEi7BIp9bbcuoS9eAf7NTJtEQ8Yqp0AOW4d5yQ9FVvUU2bzBH22OCX7V0MMzFNFWihCEku07zw4Yr1lW7wSdmfUNotYbjRs5D96hbiQAi7F7GoJ27mpb0KRrb5oDt5YXJaCxmbbKsREfhT9mPtR9oJPn2LcwieFY2wfdl6pprs%2BDQGCPwFgQek9wujUxWL%2FTM6hUjbvdPO%2F88KPePNAEIclIx2YyyNTY8EoTL%2Bxxb%2F%2BvtSO36OsA05Klcf374jGSC%2FPMolxng6avw0mT5ZkvBe6xHzwgbsemOgOQzMCBzX9cMck%2F1rqOTDUbfsw7QnALQC11MwPChr9w8CgPu2K4EHrjQ1uH7GVMBinzXHXQ8WYtS2hLKzohPTY4DKxpLOKx%2BIV0Lc8dExrRfXMOSi7LwGOqUBWSYx2M5eRS1%2BXLpJwAm5ABNi1KGvyM5pFzmSP3l%2FyYn7j6PHrneA%2BjUPjbe8bPWbyINnTTZDe8fqsdMPe%2BvZtlR8s2OpqDNf7uc2UFO7XNlm72FYK4X%2BxQJ9E0F3mfLK7Hs3uhbU3gGuGGa3ha9YV4cJyP7T8g4NywibkU9cyAADcyAUDMScI8nSjyP5pd4z9C%2FKdpfXkvdTEwvb3%2FSUU9qXP%2BoM&X-Amz-Signature=23581c79dd083a91dd9559f720fdfcf000285240a7441fc367e286e483d37b02&X-Amz-SignedHeaders=host&x-id=GetObject)
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
