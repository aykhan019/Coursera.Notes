

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S3EOUAP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD4Tj%2BDgGyUN4Ar8yVeMx9p7zEG12%2FxZf5znK2dOkmy6AIgKtwyADX68PiYCBTEEEpUHTQw9l3bstnU3S1npBekq0oq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDHl1m992sCSppem0%2BCrcA1UwZbfgO8k6IGfitVCOomhG7P8IDnpCdJN%2Bg8WmXO3hSOs%2FHiT%2FpOtcZeHOivnionUdrnQSlBdsZJxb5t34yPYN7lLK9dGJlPQ8vkUjsAiuo%2BqkuQSS5ctCOvorAJdnFT%2FATXOTgoPWlJ2%2BDnd5J6nDd%2Flxco9SmjFWuoCuIOT%2BFnZg9pi2A9UIMQE0SNL%2B41pPpNfIc13QwrLoZ5EBKDcDWcSM14qllqEo%2B89qpMr522p5SAeWJf1XvsMmY%2FU4LaZmsJw9PDJ6D%2B00pcvPnWqf1vu1dXuRWJ7MSZMicWliOqDW7kQvV1v2Sqc3mfLptMw9sxO1YggJSaybF9CaEb80dJQZK7hIvpPixsFK%2FfYZHom%2FHW%2Fjid9hcqIHr7Y7rUjKws27L9E5K64ClGju2ETcXnYyk3IaBv%2BStscK5RrODQkJ7FhZe8A8SxkZAUinGHzclGb8V%2Fj9kXt5ZX6KOEbsffap0ca8KYVDWxWQhx4vrCWfvAXQ83%2B5vHu64gNh7a%2BJcMsE2ueTX5dgMA0hDHSNXziFjVKIrR7tHyp24QuMiLKW4SV%2B9v0dUol7F7UTpJkKtBFb1NdpIKOvllnFLc932e%2FyMNuKf9r4orKMzWj406Gujqsc320orkJ%2BMM7miL0GOqUBFGyV5nSEt1Way4zRt4MaQCJcng9XqxhUHU1iIhZSFdgLQTv%2FrB08duRDQ73vIFCfc71%2FqrEIbHA%2B71xN71zFsbiyp34jhFVwgTRrJFLhS6juZvetWonSUoHu7I%2Bf2Ebwi%2F6iL6pI7avdCn%2FaRLi0Kmle0FuEj9MNeZ36nN2oPL%2BK1j9LoZFo4xGqhHrLUQcDdt6hFvjMi2L%2BITaSq9%2F7Ji1QNsKQ&X-Amz-Signature=053b448594eac77dcd7db2b601440c043b0c5bf20fdc47698550efbebc463386&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJJGSHSQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIGZLUF2QgUJg84jUdr96NHD1UBVFpz8k2IzwYbEXnyx1AiATYXidPgylp9%2FTwip0SmkUu8aSrU%2FrEfmx%2BKEyjL7Whir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMbbo1qv6yYRs77NayKtwDs0cv4Yf6Y0MrGaSbdb9owcVDupmUWMT7LJICNQTklyu0FcjadXfGkDAjDg9J94se8829PwBB2uBuIED7yUygO4kMnlhaZcG1hVgPODQkT4tNsTJvBQNKsPcNmk0vFElXoKPxy7GkEqNZy%2Fp8UuZuP%2FLgRaubmRMUScX%2F7lXG4tciLQGfrl%2FyY8r1y5ewo9s75qMcB%2B2hrkgjd81yqA%2BevIC3iUWeGZB6gciLB8Ve6skPmbJ38FDxI%2BMjYoU80zdP8GbpZagdrktoSh7%2FgK413UYXjtVDMEacJWg2CBYEGYQa4SvVd6zWQ5jF3Kd0hvfCSq%2BF589NfEstlPfis2%2FuyYrIfVEdBe8ZL6WVfe80Yttu8GkWgnHPtG6X%2Bx%2Bj7kwicPv6tjgFqxfeBsR2%2Bsqlaj6khhJgpnOdEQeGyYkSMVE17atvifdJZxnK3zpKgKtdlxMjOLSKpRlTNGjn5AL1iuF4uLced6RXigqU%2BOwOQTx5QiXGCMEV5SI5R02KpBo1vvjSH%2BC45ygTsnunVNaiTr4pWdeMSHQd8DTlno0zfDXhA3hq%2BsywJmruYfmNbSnokbvb%2BLE9p%2BuU3L5Rlg4WZkwd4jlSQH6%2B0JDjbsX%2B4tTn93T1C47Y9OTaTrMwg%2BeIvQY6pgFXK%2FyoqifEKKSz8rIEDOHmO4crdj9zp3BlU7FppSax1q5xKcwHi7CTojMMD3m75W7qOnJjHfDvH4aNJy8aQc%2F%2Bj2vRAAtYCEPufyW7zfUD6XRg1%2FeTWfD%2FNukel8DcIVkEdBkNmPhUoXiPmoucfUfqdMQ6mdqMG7Kff2UkYjiapozmtJwuUIimWJ8ray2qwZB4AWgDPxahtj%2F6pV2rkTNmHWW0tGE0&X-Amz-Signature=6f52a4f6f44456fccd213946f5ab835292de708f36e553cfffc5ec3b6d74e871&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJJGSHSQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIGZLUF2QgUJg84jUdr96NHD1UBVFpz8k2IzwYbEXnyx1AiATYXidPgylp9%2FTwip0SmkUu8aSrU%2FrEfmx%2BKEyjL7Whir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMbbo1qv6yYRs77NayKtwDs0cv4Yf6Y0MrGaSbdb9owcVDupmUWMT7LJICNQTklyu0FcjadXfGkDAjDg9J94se8829PwBB2uBuIED7yUygO4kMnlhaZcG1hVgPODQkT4tNsTJvBQNKsPcNmk0vFElXoKPxy7GkEqNZy%2Fp8UuZuP%2FLgRaubmRMUScX%2F7lXG4tciLQGfrl%2FyY8r1y5ewo9s75qMcB%2B2hrkgjd81yqA%2BevIC3iUWeGZB6gciLB8Ve6skPmbJ38FDxI%2BMjYoU80zdP8GbpZagdrktoSh7%2FgK413UYXjtVDMEacJWg2CBYEGYQa4SvVd6zWQ5jF3Kd0hvfCSq%2BF589NfEstlPfis2%2FuyYrIfVEdBe8ZL6WVfe80Yttu8GkWgnHPtG6X%2Bx%2Bj7kwicPv6tjgFqxfeBsR2%2Bsqlaj6khhJgpnOdEQeGyYkSMVE17atvifdJZxnK3zpKgKtdlxMjOLSKpRlTNGjn5AL1iuF4uLced6RXigqU%2BOwOQTx5QiXGCMEV5SI5R02KpBo1vvjSH%2BC45ygTsnunVNaiTr4pWdeMSHQd8DTlno0zfDXhA3hq%2BsywJmruYfmNbSnokbvb%2BLE9p%2BuU3L5Rlg4WZkwd4jlSQH6%2B0JDjbsX%2B4tTn93T1C47Y9OTaTrMwg%2BeIvQY6pgFXK%2FyoqifEKKSz8rIEDOHmO4crdj9zp3BlU7FppSax1q5xKcwHi7CTojMMD3m75W7qOnJjHfDvH4aNJy8aQc%2F%2Bj2vRAAtYCEPufyW7zfUD6XRg1%2FeTWfD%2FNukel8DcIVkEdBkNmPhUoXiPmoucfUfqdMQ6mdqMG7Kff2UkYjiapozmtJwuUIimWJ8ray2qwZB4AWgDPxahtj%2F6pV2rkTNmHWW0tGE0&X-Amz-Signature=dfec042a5c8c1a094eac44eb2f5b68f7b4fae0560e76ea513fcc45bb1e84c0ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
