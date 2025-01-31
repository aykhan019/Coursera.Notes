

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622ZNUBYQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrdzIC0ek5ElvtrqYv1YJrFfetL9pA28aP4hB3B%2Bp%2FTAiBRtQJG7ruOhSocD%2B84yeVcNTZghxhRlnoyomfzom725CqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRVeR7PImL5ytbMxYKtwDqYG64a9DwFmU4NQCkxsmra4ksRbnsdUtTdQhWf1FcNkZCY0tyqICpgLC6paxxWOzV0g2CzKoTlFTNvEn35QxhTVC19D5gFQ0MgcQqKnAAkF3dmpnIwlOdF1ReDDpa0sqsR35QoivvlDO%2FwmgxPbutovLL%2BhtsPglamnILrkKqXLjzC%2BLCAvuhW8LC2L9MXAukLkICpttE%2FBsuT0vp%2FK7VDxw1kynueskETl3K%2F6nFX%2Bx%2FKvLbspY%2BZ4HfcUEEb7BUR%2BUvb%2Bs089XT2XQclix4YZSwybS2ng%2B8WBTck2dGFmAHrncn6DnAgTA96y0RDW8Ck%2BOMZH7A3cKQDmLfeL15dxgkvbk1ZqcGtxbkeZSMKOr724y74zBon5CNenSoo%2FC30cVXgTaXwf6s2B%2BEYaFsGK8WACMOzP1VQrtzR6vTTDLy8vBRlWJ7%2BafQLkdlzua7CT6PFj34gcpBIO4RaCxtOzb459YTB5NvgISI%2FRtIcPkSpasmIwmFl1g6hmagdyeccxvT8gqSYyldbdhf7C49z71sCFwSCwR7mtMuXgZN6hbQZ8rfCKT1w7n4BQnip%2B%2FezPHHFk5VG5prR%2Fr8PKzAmc2t0sbZhlKmxYZbQTcTbF8fsg2p85XA2B5UsYwidDwvAY6pgHkXr9LIgD9KgiAi9WeKoWu9zELOiu%2FcFmxg3lZ30ijOyatHiHAuaUiTOwcbsMGso4ddF%2Bivd2pDP55BbnFvJkfX5bJfsT1lukgX7lSfBO6FOvoS87QYI7VbL4NhHYth9Sh0S5D%2FwkUInNitq6IaShu0e10H7E1dEdHP55RY8zQqXY31Jk95oFrdWat1RwI4bqCqUWHalZQBkayVl8aVBuAQ8Rx07Na&X-Amz-Signature=87790190656d6533d8042cf72d0c70f9602281d44dee7d6bfd8276be2acba57a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG7UI3JM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC86jn86RJWSi4wEwpC1qCy0ae9qfjLLMBTf09YJidsFgIgajh4jxmhYmTFW2wH21SII%2Bs9xwHqtndHjZzCxiBof58qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNIPfYmiepna9Jy6iCrcAzrJibasPS%2F%2Fk9HYnEye3i6pRAD72KmHEi76dpZcb923DttyFwIU7jBSRurzcKmqzdG987EjTMfbdi1by8kBKr59cqR9pngIIYDhIAYbocp0EQDMIflXOh8C6W1irvG%2FSNNVG1sqQhjY9KLVDM8MFQEMlLqKKjE6%2FxcslD7pyXu%2Fxf8KlyUyglJtSCU3rsN%2BvhwvnRVq2PK22P9Yz%2Fs3uelXvEECN6LuBWx%2F7ox%2FzG68MKudbxm%2BD5m%2Bsq9C%2BwVHxA9ysYTbEmE8xCms2C%2Fp9WO605IBLOKTLqSu0I7VzSUBcUiIwicFqcUFuo1vY7WhtYqFpMJ5YLdwNOinV%2FV2sKVYC7c5A%2FabaseIWvYnBY%2FBnmE6cSno0DheaXDjyw%2BcJ1LUIikpCdKzEMyhdLXWUyGM9A%2B5OnigLG2yw%2FaPEZ33mDAZDt2xMwKON5k4kUKWZmAklgDPV%2FKBYpsvn9oZBkhFJZFvJQtHEXykzAyTuSLXYJJbD%2FEvDlQ1rE54z0gdflq5bdHyMLag1LSRTsZ3bg8UzEjl3h1qbJIKRs61WAncHyJgbxum%2FutHLtfWGjT8tPBeC17x5hgAxM4P2qz2RKN3BQfh2T3dRGYjqA1KlSSEzr%2Fk8u0b3jlKB4XeMMXQ8LwGOqUBb8n5dFWubTDel27X0f6kZH4%2BE00i6xuDz9BHbgg7IRil%2FNRRou2edgEkUQx1ClYH9Tx0E6CaxmrRyLkGzksq1kxGL%2FAuAZJhzJUYmyNfKYYvsBz7D0iUmMK6ohDFmv9PQizHtmhqz607dBleApMXt%2F%2FAnAU0YRwztf%2BgFXVPY4o0DrkEuAFNnjKMIl8y%2Bh7Lcv2Dwb%2FZqDgT2P1Lt1xDAHrsNpNG&X-Amz-Signature=e4b406db1e8fb85255c61b03d3d06ab1eb0d6b8cb6c5f27c19aa95725db525c9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG7UI3JM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC86jn86RJWSi4wEwpC1qCy0ae9qfjLLMBTf09YJidsFgIgajh4jxmhYmTFW2wH21SII%2Bs9xwHqtndHjZzCxiBof58qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNIPfYmiepna9Jy6iCrcAzrJibasPS%2F%2Fk9HYnEye3i6pRAD72KmHEi76dpZcb923DttyFwIU7jBSRurzcKmqzdG987EjTMfbdi1by8kBKr59cqR9pngIIYDhIAYbocp0EQDMIflXOh8C6W1irvG%2FSNNVG1sqQhjY9KLVDM8MFQEMlLqKKjE6%2FxcslD7pyXu%2Fxf8KlyUyglJtSCU3rsN%2BvhwvnRVq2PK22P9Yz%2Fs3uelXvEECN6LuBWx%2F7ox%2FzG68MKudbxm%2BD5m%2Bsq9C%2BwVHxA9ysYTbEmE8xCms2C%2Fp9WO605IBLOKTLqSu0I7VzSUBcUiIwicFqcUFuo1vY7WhtYqFpMJ5YLdwNOinV%2FV2sKVYC7c5A%2FabaseIWvYnBY%2FBnmE6cSno0DheaXDjyw%2BcJ1LUIikpCdKzEMyhdLXWUyGM9A%2B5OnigLG2yw%2FaPEZ33mDAZDt2xMwKON5k4kUKWZmAklgDPV%2FKBYpsvn9oZBkhFJZFvJQtHEXykzAyTuSLXYJJbD%2FEvDlQ1rE54z0gdflq5bdHyMLag1LSRTsZ3bg8UzEjl3h1qbJIKRs61WAncHyJgbxum%2FutHLtfWGjT8tPBeC17x5hgAxM4P2qz2RKN3BQfh2T3dRGYjqA1KlSSEzr%2Fk8u0b3jlKB4XeMMXQ8LwGOqUBb8n5dFWubTDel27X0f6kZH4%2BE00i6xuDz9BHbgg7IRil%2FNRRou2edgEkUQx1ClYH9Tx0E6CaxmrRyLkGzksq1kxGL%2FAuAZJhzJUYmyNfKYYvsBz7D0iUmMK6ohDFmv9PQizHtmhqz607dBleApMXt%2F%2FAnAU0YRwztf%2BgFXVPY4o0DrkEuAFNnjKMIl8y%2Bh7Lcv2Dwb%2FZqDgT2P1Lt1xDAHrsNpNG&X-Amz-Signature=ffc0860f4dbdcc38827f5543b9d07fc5ecb5344054ffc659c3d77341be730a99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
