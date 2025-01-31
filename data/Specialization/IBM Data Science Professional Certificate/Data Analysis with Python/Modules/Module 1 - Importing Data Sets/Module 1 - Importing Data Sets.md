

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO2NUYGX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBUPZkIAjQ4DqcEgQP24Y%2BCXtaUFPQ6BdT%2B0S2dxpsaCAiEAzhQk%2BLpo5%2B8HDcyN1teLWSfEt%2BPsCVHCi5SL2dFKMNIqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwyaD97VVvMvhOhJyrcA4UkwVjrUTbfFj9jyOrR4tKAS10beW2t4cM7UeK9DnN48XQwxoONjCdu8Iu%2BrE2ZeJkC%2FYhq%2FqS3W27yADvMQGoZMcMD6MyI8r7HyHZyb%2F70f7P1glXbhy%2Boh0DKFQXQ56ETDGb9Ci20XoLK9iXAzWXfui5SL1GM2Ng4e1k%2FJEFulz%2FObhRO5XllW8Hw%2BX20eQuawcYKsOc%2BbYDEfrY1oTARAO56HtNMTTG84IZAK9G%2BxSXxCgtvvM1v%2FfAeNrTiWn3FSPZvPwE6BbCp5p74mq90wF%2FHQRn1A8gFrE2sAbdpNUGAMDj%2FraRaFFR2uvKNvdIQ5kZyb29%2BCwsBDCxGSQ%2Baej2Kfht6I8L9E8s0SLIPM5zjtA3MI%2BXbTjj%2B5i4tZtWPZEXvt7Fk1HVh4kuYkpfW16KSOgFGDPMDPC7%2FzHQGwQ8d2mPK9M5HEN4t2EBn6XF5W%2Bogq7rZyyXYTa8bnGxG17jbReTeRCMhtaM707clr2gGzefyqm%2BBXxJykIQ11JYnCJb1fLywijrco7EOlSCSjcU2irEgYY1GdqqD%2BFUkZTlaGE4w2FHHaCAKR6%2BpYYZK0VSYVgZWNwYzLOSGftLJCZr7QZyDNm6bR%2BihC59Mz8E9HwxVcqp2iCtlMMDW8rwGOqUBztv3SaoWI9U%2BGHvUSUwnfFiTqIMgAKCPa9YjpiarUf%2BsjFfW7IVr%2BaVQqhDLivz2h8WAZfuf38Qlv7dwPKHy33AX6fB82WgVjTtEOxQJaOv0PbbepZEIijwBDn1cU369LVBhZ1UI2lzAcYbu3WrA%2BX1Xs5CeS6kSpH%2FrXGoJAwFfeJFIIuKa50mQlEKCm6zFygqUrmijRuS5lgS4DnQnZ2UmjkGz&X-Amz-Signature=25bd8cb9a02add95955991616a216f8a8dea079eee9e9cf34de3b13115c15f78&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHJCOXY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbS%2BuYJoCaXVxTGl9SoZelPE3uXpOYHKLFnHg%2BDhyQRwIgU%2Fs3Rl%2F43zEqFzF99PqlT3G2sJosfVWRenlbECSjaZ8qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCj8K07VI2nJaDL7uSrcA%2BmJKgyL%2FpOJrpK9ZzZbI9Q6zzot3lJyLDIAeYTTTd04XXkS4emlAHP%2BcMY7MNm87BadEydGbr%2Fsf6jIFznOnSyGY%2BbYjrSOjDQMv%2FuaIkWUTc3VQF2XIMzvWPMYRffcloQ5ZTAq2KH43cK2GOx5M3LmTZwCYUlmnUjHlE3MYt5DmU0PMhrlayVkwMCp0ZhNnjdfXpxyCWcypl5VTRGRo72ULq02naFDbe%2BtIEgEa%2BzmNFnG3GYuOOSTvwEzm4SkZgwk5UzDWoXxno98Hm974t8VJwxtzR5sNalqDwOzezV6zpqYYNESXMWNkOR1iX5OLW4q0%2F0a6RmQ9jtGtQy7Ko%2F9c0iRtYu6OV%2Fmh04q2kOpvsoRy7F6O%2FYbXIv3fq2dRh4jvL0n6epH1%2FjdIfBP53nCTBh2VOYAxv1LUJmIzosRprOgrVeugML20yJ8uYdIH1fW55iAfqxSO2ToNJIQFr9vE2gcvyPYPm8QwraxwpfhPKs8133whaWt952u6hIlCDX7tcvooKuMzZ1k1%2F4%2FVpVvD31j581Wr7JOPOK86m2tiGCQK1dgjM4p3r0AnKzCYK1szHoEl4PjoaS5HANttrX6oSLaCddDN7EaaMmgMFPaCVEKyuRBR0ECR5MWMI%2FX8rwGOqUBAfHOGOARycKSiecxHKO0WQl2D55K26HWEhoZfdXnMMpnmWv3NxAmPJ2gXo7mTdACiwZ9hZi2Ejx%2FEUv6enJb2wCmd1w9LIkR5A8uGu5cEEDuftsRpKUfgitizXfeahIzYEMTCkNPdswuuQoP9RtsY74gj0Hb2PGy6j%2F%2BfzcDQVs3NckqXQYuW5hA1h6pliZBEQURENyq6qjZR%2BSqi9SG1rh3Cywj&X-Amz-Signature=2ed9a95878125ea0ae00bcf78edd0560918a8c7afe2a320c700f18d33e027e1f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VHJCOXY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbS%2BuYJoCaXVxTGl9SoZelPE3uXpOYHKLFnHg%2BDhyQRwIgU%2Fs3Rl%2F43zEqFzF99PqlT3G2sJosfVWRenlbECSjaZ8qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCj8K07VI2nJaDL7uSrcA%2BmJKgyL%2FpOJrpK9ZzZbI9Q6zzot3lJyLDIAeYTTTd04XXkS4emlAHP%2BcMY7MNm87BadEydGbr%2Fsf6jIFznOnSyGY%2BbYjrSOjDQMv%2FuaIkWUTc3VQF2XIMzvWPMYRffcloQ5ZTAq2KH43cK2GOx5M3LmTZwCYUlmnUjHlE3MYt5DmU0PMhrlayVkwMCp0ZhNnjdfXpxyCWcypl5VTRGRo72ULq02naFDbe%2BtIEgEa%2BzmNFnG3GYuOOSTvwEzm4SkZgwk5UzDWoXxno98Hm974t8VJwxtzR5sNalqDwOzezV6zpqYYNESXMWNkOR1iX5OLW4q0%2F0a6RmQ9jtGtQy7Ko%2F9c0iRtYu6OV%2Fmh04q2kOpvsoRy7F6O%2FYbXIv3fq2dRh4jvL0n6epH1%2FjdIfBP53nCTBh2VOYAxv1LUJmIzosRprOgrVeugML20yJ8uYdIH1fW55iAfqxSO2ToNJIQFr9vE2gcvyPYPm8QwraxwpfhPKs8133whaWt952u6hIlCDX7tcvooKuMzZ1k1%2F4%2FVpVvD31j581Wr7JOPOK86m2tiGCQK1dgjM4p3r0AnKzCYK1szHoEl4PjoaS5HANttrX6oSLaCddDN7EaaMmgMFPaCVEKyuRBR0ECR5MWMI%2FX8rwGOqUBAfHOGOARycKSiecxHKO0WQl2D55K26HWEhoZfdXnMMpnmWv3NxAmPJ2gXo7mTdACiwZ9hZi2Ejx%2FEUv6enJb2wCmd1w9LIkR5A8uGu5cEEDuftsRpKUfgitizXfeahIzYEMTCkNPdswuuQoP9RtsY74gj0Hb2PGy6j%2F%2BfzcDQVs3NckqXQYuW5hA1h6pliZBEQURENyq6qjZR%2BSqi9SG1rh3Cywj&X-Amz-Signature=79dc5e26564735c74b6c5358a562de58b816bee37271535f391343f18a914b91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
