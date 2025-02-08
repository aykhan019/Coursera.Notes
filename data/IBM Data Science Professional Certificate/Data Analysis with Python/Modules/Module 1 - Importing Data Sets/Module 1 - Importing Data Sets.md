

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KRKJCTJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDG0DFWukVR7a2DwIl2I7gUKWKj6xP5NKq3e49B%2BKtfgAiEA%2Bj9gWLp1UFZEIHdK3NU2%2BiXweYvMRam0D1sqXIQ9N90qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ39SCJhnI7ZkHwvOSrcAw73IQTQgXxDA%2FOljeDZfau%2BqV2rCTuPvo73dKl8JROjVFAxxdTp1rEBQL3Mzo058W16YR3mAkxOln4qw4CnRm%2FQHa754f3gcZmShZ%2BJ1FVibM1TLDEA1d1K%2BfRBLF3Gblbk0q8sVoAS5jZcE15QNPUJ5vvSgj%2BS7cw4eVpYA%2FPKrP1wZJ8AR%2BfFhyPodZRu98p2JaTKC9KB0PUPkcg1IX7QIb8h4zJN5MW6TDztjAfCYAwlC0FeRk00jnthdjt9DLzBttPKoiRZWBP9S7aV3UbtVK5hINea0jcBydpW0PnHs080hac7JmYjjeckWlFpQEDRuoknQCOxVcJY%2F2Ds2p3i7mebmrjBe39kkNt%2FmDhrwikyYsXE5p%2FhgRvr0kU1C7jkANbVmRV%2BeNcQPMMIfqG9INtmOgACT%2BsCQ%2FljhhmlQRD%2BUHwciGQ6Z033GQefdROvO4vwy8M%2F5Yw7Q2VJ0QajYeC8XXf3NhSwLmemoP2NsdDqHIsr17RfYRVM23%2FnYy0bvckMJPWmY1fRGpPPp0LtC6U6kK3AKd%2FY6TW0h6zdYj8ydkNCxgQ73N0mo0b8y7%2FtHdMLCi7wFtgXT0Tte3ZAGeAI9I5B30J25QisiuFj0eChdXVu4oJrPt%2FXMKyFnb0GOqUB75DEJm7YUHw5lG6BQJfGBjVu1LzZrJ4WIW8gYDa39R1ehtvpPK%2F%2FjBIhefDVU1SlXSNcoWqOxMcx4WetbO%2F5Std6rcgsqFeetCV%2F68lK4wGjH3MV%2Bzs7X%2FjGvkjGVymCumBFcxfDdhGIrLju9FPn8FO0QSMmKw%2Fn1JSOilfmz2rKtJI3jQyx%2BHtaxG6T2lNTOd5aA2YCsHYjzKd3fZn0u8l9SzoV&X-Amz-Signature=116f81a098d9fbcb45d39ba6095170820445a0f0905c0b9170640905b870f32e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RXYXCPE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDiUKlVv4e2ZpfMqJ1WAMc%2Fi7O4qX1tMj9uZP%2FYF5lslAIhALUVfRHvUmZ%2BplydTMmWx%2BNaSsDEbXRC3uI8Wj99mScVKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgysLsXkgR636KsH2aAq3AOq5YCn9he5W01mJOLD6HbuTJzZUnv7yZsiBDY8Yc6i%2B%2Be9WUnWUBCcx0vzocH%2FcJm9BqCKWsNfHmgNWKA%2B%2Ff6QULyQAWRt%2Flyey%2FrW5sl4I7kk%2BGEo%2FvnOIAPmbgBnuWTUgIl9oyHbIXChbWy%2F7cLt1uK7WKNeiJnx1cKd%2BaDKq9U1vInuSi8cGgbJNm2VEg8FFC5gtwkdmLD2oCmP0xJPrU%2Btj87jBGpFMs3sP2DvnbJOMBTupWOOPMKPWZDp6ejQYXDIjmunZVyD289E4ObnD%2BIVTlXPTFZr24Ty0zjqIpRC3gRycT89hK4H0zNHDz0i03LTojGhnbPPAVNmLsJ28MfuD1EvyP9IMbZi2yIPNDq2EFfUNcqFZjufh1uo8qn97LX2WLzTwAxATpwQibZbV0j83fibFc90iGt0E7TQXA74SdZRaacJVf0eQ%2FdWf2%2B7R%2FCgkzrseS2T5vfiz2vhtxZq%2BrJ4DcXtSBnckzAT1wX3FegrQvNA5mE0HJzYkY5r5o5XJViMHop7EMzyPZ%2Ft%2FIjP1axf7KWZVjuajA2zhqERhl%2BkY4pQvfsSL%2BWNwZWoWU9%2B2Z64LwraorlIEWjC5rH%2Bd0QcdA8epO52ohbm8IQYhf1ck5Uuy62mejCrhZ29BjqkAQUb9QWpKYAAWLdAqpNxVShdErxCY1AYoemE9DquPn8Vb%2BSHR%2BNSwuMQ7M2NWjsF70LFKgpDAZoa3Fl5h7etdHhNxx1pgSUkCPUgl876NmG0WjdLmH%2F0GFBIAg0MEjrTfzNJoEfrpreTTpqW5Kt5Pn0Bt6kcpY%2BwAaq65Kccmm1G5PhsaIJdMBVzzs4mp1f0hc5Pv7IG31yonGDozr67A7V42ksw&X-Amz-Signature=b59e8281cf98766d67ce24332f3f962050701afa13a57beeaeb1ab4d540f55fd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RXYXCPE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDiUKlVv4e2ZpfMqJ1WAMc%2Fi7O4qX1tMj9uZP%2FYF5lslAIhALUVfRHvUmZ%2BplydTMmWx%2BNaSsDEbXRC3uI8Wj99mScVKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgysLsXkgR636KsH2aAq3AOq5YCn9he5W01mJOLD6HbuTJzZUnv7yZsiBDY8Yc6i%2B%2Be9WUnWUBCcx0vzocH%2FcJm9BqCKWsNfHmgNWKA%2B%2Ff6QULyQAWRt%2Flyey%2FrW5sl4I7kk%2BGEo%2FvnOIAPmbgBnuWTUgIl9oyHbIXChbWy%2F7cLt1uK7WKNeiJnx1cKd%2BaDKq9U1vInuSi8cGgbJNm2VEg8FFC5gtwkdmLD2oCmP0xJPrU%2Btj87jBGpFMs3sP2DvnbJOMBTupWOOPMKPWZDp6ejQYXDIjmunZVyD289E4ObnD%2BIVTlXPTFZr24Ty0zjqIpRC3gRycT89hK4H0zNHDz0i03LTojGhnbPPAVNmLsJ28MfuD1EvyP9IMbZi2yIPNDq2EFfUNcqFZjufh1uo8qn97LX2WLzTwAxATpwQibZbV0j83fibFc90iGt0E7TQXA74SdZRaacJVf0eQ%2FdWf2%2B7R%2FCgkzrseS2T5vfiz2vhtxZq%2BrJ4DcXtSBnckzAT1wX3FegrQvNA5mE0HJzYkY5r5o5XJViMHop7EMzyPZ%2Ft%2FIjP1axf7KWZVjuajA2zhqERhl%2BkY4pQvfsSL%2BWNwZWoWU9%2B2Z64LwraorlIEWjC5rH%2Bd0QcdA8epO52ohbm8IQYhf1ck5Uuy62mejCrhZ29BjqkAQUb9QWpKYAAWLdAqpNxVShdErxCY1AYoemE9DquPn8Vb%2BSHR%2BNSwuMQ7M2NWjsF70LFKgpDAZoa3Fl5h7etdHhNxx1pgSUkCPUgl876NmG0WjdLmH%2F0GFBIAg0MEjrTfzNJoEfrpreTTpqW5Kt5Pn0Bt6kcpY%2BwAaq65Kccmm1G5PhsaIJdMBVzzs4mp1f0hc5Pv7IG31yonGDozr67A7V42ksw&X-Amz-Signature=8f483e0c8ed9aa1a74c890a3d3b244c5faee8cda406b4133b1724cedca91cee4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
