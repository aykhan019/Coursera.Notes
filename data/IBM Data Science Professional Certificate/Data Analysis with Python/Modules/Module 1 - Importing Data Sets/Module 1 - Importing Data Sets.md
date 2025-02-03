

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WR7SV4EC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDB2sIIm6AQF%2FPp%2BE1iJUzPn6BppzoPIV6ZhvFKL3yAcAIhAMbUOANAzb01a3beJuGzPsF8G3SP%2BgdS5kf0GBXonc%2F9Kv8DCB8QABoMNjM3NDIzMTgzODA1IgyfC2QtRbP%2Fki%2Bbm0sq3AOvuuz9iTBSLqMEjPJ7g7%2Fgx7J6vetem60ks05T8gdJMXAXkqtyhjEEkGDnQaDmzWOjpn8rAQuS8iYQzk30zKsD9O0%2BCY%2ByCVKrH4SP7kaLaMWCw7QNsjdctgebhU7Eir%2BsP2%2FdtL8tw5WzV%2BCAZ0uxi4bortukGuYMJ7XbOHqozNrv13mDVJnglP1wFsFILjejCw8cXNr03r54K4WhcDDbmZCBKvAtRN077xerUAiifBQCPlMNTjq0%2B4LDt7o4oNuo4lwg1LG4htdAAfY1bV93cBFAAhJXhgoAcuBH%2FqtTpyEW7cF7AXeKh5k1GjxBzcjR9Tf7oylWWwb9dGWyNh%2B3i%2BmcygStYIiU%2F9L9HjAdK69sw6yADeiVfwgf9A78%2BNqn%2F4yMY79XiXi4%2Fbk0DEYkP8gQJogNJV9SWYnjbWriDz%2B3yUk6Av5rDo%2F2jfXuM4%2FW6dB%2FE4S3memOkBIwPBGouEQxZ4jkSkki80EDXaY9edVyhdk9OVJ4dqHzK4lazoXw6P9RTAca9V%2Fj7frHXeBVyw%2F9jqvawosdIIVDkJaGDwkcWDva910iZWXT1h6sScvH2dDsQpsw5EfKyHoXuOd4g19nQzPGUdfGUU614Xp34gstqT1PNjPnP7IiWDCu94S9BjqkAW8laG6iu6XJBXF%2BJCncoBA3cSp0Ilomi6M9nqAdrbU5ZB5JgYg%2FskXgntSkSZsERE9JVQQiBv9DKapDNSCbTxyOD7Me%2BDxIcxTm3NZXnblnpDJHGtf5Lird2285qzKFxS6sFmdjmw6c4wRdeOQ6F196eC4yMnFn0cSdwLFBcuHobnCIhCPjJRLl%2BkfqG3fCZoch3z4hXAGK3LaPYo4BbLaNDAuF&X-Amz-Signature=969ea54d4d5453a71ab779551d8850ed9f114d32dc72274f34da7dac4e962d65&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYDI4BLV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDQePUGWPVpxleFysQHvRlIGTC%2BB50vKd%2FebZyU9tmYNwIgacccQLfZwC54EZuybZrpkwB%2BPFiR4WmZmX6btrhoRugq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDBubRJe%2BoxJb0oLZEyrcAzce7QyqoB%2B2%2F4rLTtDtasTkdc8VlQqTJyoERl7v46sBhb4np1kz63NSWanC0AvxVStbnSuNxA3BWvhCLcpORzuuElMzkYDMEPqLxEtkGnZpfxveKp8%2FMf9icVSx1j%2B0%2BR3Xuu6EzH7iagYqCwuWfEODDwCOA%2Bb4v7ktQBYJWJFLXHUDaLPnofT%2FSwoDpIkmxKihyoas7XhXpZ7VCG8NTNwP16yDzqKtc5oWt5GGtzrxafTmVX8yaH0fdgq9VjIQ3ChjoWmq%2F8RQxnwtHkU%2BMVqIH1MW6EbxKYNxwHoMiHZ9cYn13pVa%2BJf2pVGgKkGTuGz0WWJS%2B59JWs89O4ETZRMSXJX6k59D%2FX88i4ogA2HXB43VUgKZ8tum5V8N4wTDTdL3HcUpgQUsuO0vmp7CPypdQcBVsnou1BgA0QJ9u3C%2B42RnfwTlMSR%2BeK7lLpRq9a1g8uwa3Jx22qkRbyxKMRahd1be953z2dNR%2B2LDU4wzSOAkvyCPLdr415iojAUzHL4ZCXFevHysch8WvBs083ATaXHIXAvyaU%2FYHHjM3v1QPXWjjA3leGOKFPE3Hz2WeM657ZDJgXEahOLsjlzxvHMFP8eMB6SRR4%2BomwCfegRrDb5ytd8zw87pG6ZAMPP2hL0GOqUBR2bVpZVwP%2B1wtUmcT5pwVzMkdybQYnKgZIYKqGUHAURq%2FzP1ILHod1kuEbKpRNivjArhUsbbMATgVvf%2FSAbz%2FpSRnlU93msKU8uZkJVQzXIgfrqBhw4pM9agnbjcKn5SYY7bSNBrKyREPxr4dYELpVNA%2BGZ9kmfDMSC%2FvrDTrq5VyRs1peDyA96QpidxzwzyIZpoHUed4rewv8Z0XcayLxwoU%2Bc%2F&X-Amz-Signature=268a4a4f8fa78db44a841517e9dc67dd4b42c1cf64d4fb3a6e72eb40d17a984a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYDI4BLV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDQePUGWPVpxleFysQHvRlIGTC%2BB50vKd%2FebZyU9tmYNwIgacccQLfZwC54EZuybZrpkwB%2BPFiR4WmZmX6btrhoRugq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDBubRJe%2BoxJb0oLZEyrcAzce7QyqoB%2B2%2F4rLTtDtasTkdc8VlQqTJyoERl7v46sBhb4np1kz63NSWanC0AvxVStbnSuNxA3BWvhCLcpORzuuElMzkYDMEPqLxEtkGnZpfxveKp8%2FMf9icVSx1j%2B0%2BR3Xuu6EzH7iagYqCwuWfEODDwCOA%2Bb4v7ktQBYJWJFLXHUDaLPnofT%2FSwoDpIkmxKihyoas7XhXpZ7VCG8NTNwP16yDzqKtc5oWt5GGtzrxafTmVX8yaH0fdgq9VjIQ3ChjoWmq%2F8RQxnwtHkU%2BMVqIH1MW6EbxKYNxwHoMiHZ9cYn13pVa%2BJf2pVGgKkGTuGz0WWJS%2B59JWs89O4ETZRMSXJX6k59D%2FX88i4ogA2HXB43VUgKZ8tum5V8N4wTDTdL3HcUpgQUsuO0vmp7CPypdQcBVsnou1BgA0QJ9u3C%2B42RnfwTlMSR%2BeK7lLpRq9a1g8uwa3Jx22qkRbyxKMRahd1be953z2dNR%2B2LDU4wzSOAkvyCPLdr415iojAUzHL4ZCXFevHysch8WvBs083ATaXHIXAvyaU%2FYHHjM3v1QPXWjjA3leGOKFPE3Hz2WeM657ZDJgXEahOLsjlzxvHMFP8eMB6SRR4%2BomwCfegRrDb5ytd8zw87pG6ZAMPP2hL0GOqUBR2bVpZVwP%2B1wtUmcT5pwVzMkdybQYnKgZIYKqGUHAURq%2FzP1ILHod1kuEbKpRNivjArhUsbbMATgVvf%2FSAbz%2FpSRnlU93msKU8uZkJVQzXIgfrqBhw4pM9agnbjcKn5SYY7bSNBrKyREPxr4dYELpVNA%2BGZ9kmfDMSC%2FvrDTrq5VyRs1peDyA96QpidxzwzyIZpoHUed4rewv8Z0XcayLxwoU%2Bc%2F&X-Amz-Signature=415a5a6e89d28b131289ec483fab386fd8102eb6aaf19ea7977c4e5af1efd33c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
