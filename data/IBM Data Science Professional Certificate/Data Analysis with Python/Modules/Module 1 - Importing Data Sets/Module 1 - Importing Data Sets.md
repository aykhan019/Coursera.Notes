

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QZMM3ES%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCuSvvBz8UEe9iOLgtxdNhLEYeadCcbGMv0HtdrLc2qzwIhAMWl%2F4LWKW8ENAYK7YK9qRwsJrvX4IlZVUGGA4VplK63Kv8DCG4QABoMNjM3NDIzMTgzODA1IgwZbvyaJ%2FT0tRjYB4Mq3AMy2EiuYh4fJT9tqNHnTQQ4CC5FQ%2F6DQGmSRb2nhcaUq8s9gMK2kiaLC8YmnUM02TCCXqZXBHqfeQtDwHIxja4jfhhKrDrn0UN%2Fmn4XyFuFGDx%2BCy6M4zF7lxuzpB0AVMu2OM9XRFXBqrJ5hMibJ67bLhsTY5IR2VhbcfcRTPRYReDS1VRPUtHOc6VThhPw3cf%2Bbo4i75y%2BNoS%2BmS67u2Z4QScvyI9P%2F%2FNjQoeNVkfUO3EmSwnO1ANMX7fq7K1U5jURQKtZ8%2FnNCU0KLpcvZd%2FCCx5spo77%2BxNjAoWxRkfd1Jdi%2F4651NXDI4cepk4%2BHF1beJPGfUaoiK%2FHC2yRKDmpOeb5KUuxjzz68xm8MY9bLTXRoAxRHsB%2FIcu4i0k%2Bdp9%2Bo6gCGAUGBGQsZJmePeYFhFLKYJH8v5VcS4cK5RSkD2n76OSM1vfz8oreRk9M3o1HZ02omfTkzFjKfWPeEzBP7L%2BR8gaQRu4Q0110a3v8LiS1cWdOf2ZD%2FsSJdMUo8i0tRipG4kfMehCxPSZSj%2Fx3bR3RETBlnx7PuqrWKyepeIxTsNMdiq8OY39hL%2FRPRt8IowHmNrNzFf91lO0Kv8zvkx0PSTC%2FZG4SjzvbSesEIAUyasg9tcec0XN40jCWopa9BjqkAZjnvzLMXFT34JRXNB2de8WtTsxOw0Gf9LR1xgQjK0t9fOUtGhVlZcoDOhJ4qo0FC6ZKVEk8OlyrKhdqbr2F6PDgIrZYLz1NauVbqd%2FFnxGtbu6hLqM1pLEcGdsHK4n0JRjokgpGtqD0grkBUKMwNv03iRilPjOceZX8K8G9g7Q32PL8Mkeb7OB1LBa6c%2BJf5isaf%2BkKs2tTkvjT8fFl1VjrgKtQ&X-Amz-Signature=17a31cd67689f27276e8de2de72c5e243ba9378f1e818f260085c303d75aa850&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QLE566W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIF56Q9oIImiBZeas8Fg3LhMqr0HSMdCyAVqKX31ciMr7AiEAk80uxedx0a677DEgYP%2FGzbtfGPMHpLKUdfP9nme1rbUq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDKUC3PgWTeKDznYWeSrcA3MJeURpm0xj0aUKptOSKD6MazB%2FtX9vdtPncj2hFhoJpevNuAIl01B15zGa%2BFmQNk5mOBj%2FE9UTbmaTTOzhjlDi4%2BFpx9u3maKMqKBY%2FJ%2BJDYr1bAnIa%2Fn8vSS%2BybGl19fBcwGm37modW7WewZ%2FCcsI3jizbtODa7On1mc9Stt4kOLGErNmwWDt2sqjPVaxYZvmAO51Vffy4L%2FLiuCGLpfJGjrf7DN%2BxmpUAL8nKeO82DpZPbKe3hYZhHh0rJxoFGb5YtntqGTQZjv1NEeePvPnBXi9Ef4Henen214TvacbORlmlmr6ogs44l7CyD6MfhFVnkakxJ7OG2IxKdGV0BO12jYL3Qpw%2B70mdCejsMPFULUIbxVo1Y4jRkGuim9BgeAk5Q0hl4udPUCbT%2FqqMl4Xx06nmF55E3DZWcg6RUDBvaUqM9fiXoMnkWoslFTyCX13ont8e0O%2F76IP5tbAh7deZUvUJOHu%2FWvda8XPQy72BkzMcXsJnDmM32X8t1zgPb79ddSUOsc5otKR80rED1nfDQOXgTBLK5Z2qR3KPk59URaFK10YkV7a9f4BDefkPof97Ti2FwyccYrZPL7kiiL6ufrZ6CKS4ew5WJgUuK8ngrGc4bluWTFfzEahMPehlr0GOqUBKRjVww2XB9nEMMwb5VbPf08LaYjOMNpF1SURD4Sk9FiVEkMmkz7Bn6nL8my8gCtXA1mNzQMVJ7beJ5KVUfsdTb0njGxRdH%2Fd%2B8ImW05eOMyTYbmody7EWVb5RQGNjTZfBg5vJl1hNFelOMDlPBW639KAwaovhxxhLHN0du7foDbhgPpN9YXORGP0JGe6Gsn%2BISxlkBHTlZ%2BdlerXdnsyb9H1VvT%2F&X-Amz-Signature=dbbd21f826e314b1ec54f45d5a04ef1fa1ff1bd0cedbc885c26046da2944f2ce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QLE566W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIF56Q9oIImiBZeas8Fg3LhMqr0HSMdCyAVqKX31ciMr7AiEAk80uxedx0a677DEgYP%2FGzbtfGPMHpLKUdfP9nme1rbUq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDKUC3PgWTeKDznYWeSrcA3MJeURpm0xj0aUKptOSKD6MazB%2FtX9vdtPncj2hFhoJpevNuAIl01B15zGa%2BFmQNk5mOBj%2FE9UTbmaTTOzhjlDi4%2BFpx9u3maKMqKBY%2FJ%2BJDYr1bAnIa%2Fn8vSS%2BybGl19fBcwGm37modW7WewZ%2FCcsI3jizbtODa7On1mc9Stt4kOLGErNmwWDt2sqjPVaxYZvmAO51Vffy4L%2FLiuCGLpfJGjrf7DN%2BxmpUAL8nKeO82DpZPbKe3hYZhHh0rJxoFGb5YtntqGTQZjv1NEeePvPnBXi9Ef4Henen214TvacbORlmlmr6ogs44l7CyD6MfhFVnkakxJ7OG2IxKdGV0BO12jYL3Qpw%2B70mdCejsMPFULUIbxVo1Y4jRkGuim9BgeAk5Q0hl4udPUCbT%2FqqMl4Xx06nmF55E3DZWcg6RUDBvaUqM9fiXoMnkWoslFTyCX13ont8e0O%2F76IP5tbAh7deZUvUJOHu%2FWvda8XPQy72BkzMcXsJnDmM32X8t1zgPb79ddSUOsc5otKR80rED1nfDQOXgTBLK5Z2qR3KPk59URaFK10YkV7a9f4BDefkPof97Ti2FwyccYrZPL7kiiL6ufrZ6CKS4ew5WJgUuK8ngrGc4bluWTFfzEahMPehlr0GOqUBKRjVww2XB9nEMMwb5VbPf08LaYjOMNpF1SURD4Sk9FiVEkMmkz7Bn6nL8my8gCtXA1mNzQMVJ7beJ5KVUfsdTb0njGxRdH%2Fd%2B8ImW05eOMyTYbmody7EWVb5RQGNjTZfBg5vJl1hNFelOMDlPBW639KAwaovhxxhLHN0du7foDbhgPpN9YXORGP0JGe6Gsn%2BISxlkBHTlZ%2BdlerXdnsyb9H1VvT%2F&X-Amz-Signature=aaabd51e134a278d7fe63bd39302cb4bb23289711093904a41a54d06f5c14a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
