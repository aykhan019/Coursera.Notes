

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDKRC2YF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCXM%2FcZFAuBdO1uSJwhdGOFpYus1qWhF0Ftu139f5lf5AIhAJJ%2FyT5ITtEaoadEfLbhrmVt85QgVWm5DI3ylUxm5fc%2BKv8DCCkQABoMNjM3NDIzMTgzODA1IgxuMybJnTpMrN8aDEcq3AOrDdIqaIXX3sYljyVkaSG4dMgE1pSSh319dSKM5pkOhVLsMdaaS0tnv%2F2oALgNGEzlf1w8ITgq2IxEVoGVf8dqAhtvsoWjXR3jJyGwOfyLbEjaAL7zPKc4qv5XcTcOcl%2BkIRrToKA56qy7dpBzrj9IKpnO3YuLdz29YtZ4OUl8RP3j9RNKeWGGDjnC%2BHNGde6%2FU%2FO3oK0HE7zHQRwK1N2wBtUF7kOQns7KbvFjo34bJAVgv1sDHZQnGZCa0O0%2FYdGNQJDLGbceRxOKwiL2UWyIs%2BbiBEJFzwEwbhuQU3TCPlUc6orx%2BirTXn3gMXKuJSctiIx8CUNd5%2B5%2FnVmA1Vf1qlePZidQHKV8j77JKZiH1h3NcbReby8SJQHaMBaGiH3g%2BiqopTbzR4eJ00Ag7dtjuWyRxMRocbzdyL%2FYTx7DiBTGNmC0GcezX6rGmbON9qA%2FaxRjUnmCpO1UyPWJJipuF1x143mKfR3m%2FvaT7qc4QbMGYcpeZT%2FC462yai3ZohgPLaI1vEoGqjPXTNIjlK5l8KEPC00%2BKwAjpQgFVtVHzw7LVsDzjcDNl0G0y11LR3sYWMSaex3%2BMvsrG4tM1%2FhvCfWiXL7jNIpAsiUz6tlSQFJYN4c5fKqLF9HZcTCZkYe9BjqkAQXBlhRg5iKyrF1VzvITQg7FAeuPPuoFFWusTlvvNxb0cXkJg3Nbo8FBvz1HAIb3qE1jbT5NZ00K9AR3L0%2FHT%2F7yXbAD82gnHioZI5EFExvCnaYW86W14pXGsufMs3kk2iFvYD61aYSMb6X81SsPNb52JwIm3EBllkY%2BCBgLsrAb7zqszDspE7n%2Fa0N7RUrLJsPfbucq%2FWDIDz34Kh6bqjtM4ntB&X-Amz-Signature=75dcc353c4277518c3051fbb4726360b89e88cbca9f70fe70429db0ee9806851&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGVK2YYT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCaIX%2BI8ePhgBMHAR8xZ0KSy1BZj1s1nNfh9qstFO0BmwIgPCQspoetwr0E7VuK5gae%2BKiyB2Nh1EtfP0%2FVVydl12oq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDPA4tpJGefZkWfiz6SrcA6VlvOMO2T5lwr9d6B6Bkk8jIuSqP%2BKZ7AL38zrUMvSv%2BAWlLRiytCiCpXg%2FIhWoF09D9yw7tlH%2Bwbc7tmrl%2FCRjx0f7EGohMpG1Bsm3yqMW73hCI1FJUwGP9sCXcxMXMBhPyXsRi4VBWgLg8%2BrpeJA2p4wjWKcUrCNDRA6QOJHzju9WPWjUnXS3W6uwNXX%2FgSG%2Bi5ZbJrlZfYqyi2hkG3p5HWmZSvaeOcE8oP1dZG8DLe1chT%2FR0kFVUOtpB5HE89S9rax6%2FY7MuNobEEzutBDogk0I7ExdHrNcRHxL5m%2FlsDT2XpnwworNE98oHK3e%2FMjat11GBqSDHW3%2BTC0AhatxFJw3n5KdDTiOEEPbMaog72%2B0GseKTWOlYa5%2FfmnFByyfjWWsbbz%2F7lbX1IUIBv1mCLUAfbvkTCThV%2FsiCoTY9IpmvPCC16DQW0c7kSb2G2VI%2BO64aDZqQwC8mm8Zf3nf0tUwhOyZe1bjIuRaWvyMEDFPL0PMYB2IWjaqUrXX3D0c4WcQE0%2B4T0%2BUHmiFdr%2B8nNVhds0sXiyUfBBPUCFMu5q1zfvfj3Crekxctjd7hpfXMVODssRhudMQIc0qe4v%2Bn2tAdew8dg4pp2HBqBQPZiFC80wam09cHl0SMKaRh70GOqUB5Mp%2FX5SukPBqrLI5ztg8ucIIoCOTlIWxpxzJ8dZmBi9XoszrcDV2Cfa1rtShXhyeBAhPd4DeLml7SKgon%2FUNMq4VAjQtF7wBRNUO3BZaX9lJ7mnNKwJ%2FZG%2FOy%2Fvf8m%2Fbq9wdu6pgJourxN5FIPS2Cah9snmS%2FfeNs1MoXanowdy1bQODOVsLlM7EYzYHwoYa5S9Vuw4POS0Uu8lWQb8Af%2FAMdgw7&X-Amz-Signature=0ae227d75742b308c57f3c1c89729d82bd6c97b8d291992729f148258cf18524&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGVK2YYT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCaIX%2BI8ePhgBMHAR8xZ0KSy1BZj1s1nNfh9qstFO0BmwIgPCQspoetwr0E7VuK5gae%2BKiyB2Nh1EtfP0%2FVVydl12oq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDPA4tpJGefZkWfiz6SrcA6VlvOMO2T5lwr9d6B6Bkk8jIuSqP%2BKZ7AL38zrUMvSv%2BAWlLRiytCiCpXg%2FIhWoF09D9yw7tlH%2Bwbc7tmrl%2FCRjx0f7EGohMpG1Bsm3yqMW73hCI1FJUwGP9sCXcxMXMBhPyXsRi4VBWgLg8%2BrpeJA2p4wjWKcUrCNDRA6QOJHzju9WPWjUnXS3W6uwNXX%2FgSG%2Bi5ZbJrlZfYqyi2hkG3p5HWmZSvaeOcE8oP1dZG8DLe1chT%2FR0kFVUOtpB5HE89S9rax6%2FY7MuNobEEzutBDogk0I7ExdHrNcRHxL5m%2FlsDT2XpnwworNE98oHK3e%2FMjat11GBqSDHW3%2BTC0AhatxFJw3n5KdDTiOEEPbMaog72%2B0GseKTWOlYa5%2FfmnFByyfjWWsbbz%2F7lbX1IUIBv1mCLUAfbvkTCThV%2FsiCoTY9IpmvPCC16DQW0c7kSb2G2VI%2BO64aDZqQwC8mm8Zf3nf0tUwhOyZe1bjIuRaWvyMEDFPL0PMYB2IWjaqUrXX3D0c4WcQE0%2B4T0%2BUHmiFdr%2B8nNVhds0sXiyUfBBPUCFMu5q1zfvfj3Crekxctjd7hpfXMVODssRhudMQIc0qe4v%2Bn2tAdew8dg4pp2HBqBQPZiFC80wam09cHl0SMKaRh70GOqUB5Mp%2FX5SukPBqrLI5ztg8ucIIoCOTlIWxpxzJ8dZmBi9XoszrcDV2Cfa1rtShXhyeBAhPd4DeLml7SKgon%2FUNMq4VAjQtF7wBRNUO3BZaX9lJ7mnNKwJ%2FZG%2FOy%2Fvf8m%2Fbq9wdu6pgJourxN5FIPS2Cah9snmS%2FfeNs1MoXanowdy1bQODOVsLlM7EYzYHwoYa5S9Vuw4POS0Uu8lWQb8Af%2FAMdgw7&X-Amz-Signature=37c8e722d4eb0d5710305fd7182337c26fc20a9fdf9eea56b1ff314fdc2a79a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
