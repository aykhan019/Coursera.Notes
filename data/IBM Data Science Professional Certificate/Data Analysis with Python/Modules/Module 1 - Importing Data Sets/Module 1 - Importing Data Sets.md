

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWSLVPWW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIXs2gDH4%2BDAY8o7n0l%2Bu0dE%2FqOraPhiwtQD4Gt%2B5HZwIgUwxpyqqbpFVDTltFiXgjNkIKBQ%2BqwotcEt%2BjyXHUzVcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvyzf9b13K2KHDY5CrcAySZZ2L3UpxVcjGhpynwQOpowl%2FR1OVyjtpKls6zZ2r92yhSfACQD4kpNMXRZaZWbNU4m78AH0AJiFVL70CXgds%2BVxF9MeG9deKDf%2Boa8B5h5DnzCB%2BaI8%2FJ%2BC79RPt1gZlFI22TFWVPeZzLJ3gMyAriT%2BDmf%2FSMzjPwPAtZFYbtNE2QXAhA2FsNzSrhXBZjs9x1erkPeB%2BLaZssOVR7MnK2mPgqyMk6tY5KSSqeRKA8gUs0Vs7%2FcCxBx4dBF4UMkW5dkxHlb03qy8tbeNbUEcVxrWYW%2FulbYdV6%2FRRPG7TTXfs3x0xpyx1AZuVSw7RHNQ8WKfl%2BlFISvSnk%2Fzdpdsj1ZI1kd%2Bo%2FfkVFsQsJKXxBP8zkwkg4Mz%2FCsrPSR0WfNUc7xhrAm%2BCu73o8lA781%2BgLwaJD9IKQT9MGaPJuWsLt65ODCaXl7KS61wE9aKHClbxZ759JYAGwIBVm6l%2FPe0qXO8niUVMG8TnykcnKZxL5sKYE%2FIUOx3SPMYRJANuSMrL1Cw5WAAVWdMHvPCE3Sv4LLM2Jc8mGJvA52taaA5lWQ2%2FcTjoKaS%2B0rSh2jwGY7Rl9AeJzSMUCOtkQfsN1vTPlyq5LfljY8CsxqIx6mxdYxvP0omvAqoihkwJwMLX49LwGOqUBBHyuNUCFgn3SwuzLuoOpyh1kgtX6NVq%2FmZUXQgKsP5cHyFesaqZH1l9larUcmnaprLPnD%2B%2FMrZbuQtFT3N1L%2FTlhgXnP9%2BHEStV%2FI2ZntqtlAmeHcSVP%2Fynbl3m%2FDPnFqREWzB7aF7JkyPTkdoot3zqCVvKSbgYiDjsRUqu08qVmET0jeQocnV71K21SeOCe1wptSRZFZFW4O%2FXmYMGbKy5bnWfs&X-Amz-Signature=4d4ad27787a29fc8453912dac4614a0cb483250163976af14e7c9e53ee78b7b3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI3EMCO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8SeVuGSF6W%2BjskJyeLPJ9Aa9F43taXX6oY3XSDLR5SAiEAoxEBs7tws%2BpUpjypakNmSgGAfNOAfKAXGEEVdnBT4ToqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJDJ%2FR2F0Z0H0RSRFyrcA9%2B3lJhRBdzjjm9KAZm8C29vgY1U5GH5IMB4%2BxmMNNECyxLTcfFkJ%2BmThNveodVsyyZRdgLwgnDSKWJKMc7NXW9wvxyCCP2F%2FYv5NQgAVMDtsG2IO5%2BijYpen0P%2Bqj29UV5ZKehm5xXpeFcmpDwjLJcjy2kCdl6RW0JAZoRH2dq8eX3dN6IyiaHTgiGo1iZ5gwwxXlqK6GH%2BZYJzYR5xih9xC3YkKXHtzZfcLk1FvhNS7PUE7ReTC95GN4ieMcVAbz4b8tEf5qjUbpawGHB8llmIVJeRCf1CJ6oyGYI%2FfT7UqL0PkinlU2C8sS3EvBHRFcMyaZNuHpFe4HwxBfVOsgf2ixoml3PnNYTFTjES0tB7M3TQeguCXIQs0WPN2d5UOxkEdizC0LrKyGl8Rt136xMywJnXwMlMro73mAmHZq%2Bs341HNfvHKsR8s37xGj92yJ4xJFjw406j5xNNd%2FQ4EinDC6U8jnOo2EaAloY36ee85S8QOoRrBaAIhCnEYBdVYuF0yekZoYmzjYwsKe5fDpJYiZlJIZ0H%2BwrMI63n3xKYokH9BPT4nAn7kxrpb9x3Ey%2Bv4uUoqfLmPfs%2FP06j5bx%2BceCVdkYsUhZLCikotxSPapZoa9hdLgO3ZigSMKT49LwGOqUBxoh0XnZt%2B96TieF0VyEXR1hN3G4Tr6jvZjA%2BWp8KkBofr5Nlq4nz0lgwycGE20Y4EIOANl2JXse%2F00I97pyiR3%2BUwj%2B5fUJ%2BbXNljVH6ni5Xv6PAFw%2B8qJaimEEbuK2OhM2eW3PMYi4r%2BGzUgnFFJDquKFsfnC5JHyHnWL%2FNqppOTVsIGiHHd7Vu66eab4sZwq1rnQpPxJSsnWBd3dIv8xU3%2FXNi&X-Amz-Signature=6fc1afde809f3445d6f582691764533d054d5049ce9dc86bca65b6f28effcc0e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI3EMCO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8SeVuGSF6W%2BjskJyeLPJ9Aa9F43taXX6oY3XSDLR5SAiEAoxEBs7tws%2BpUpjypakNmSgGAfNOAfKAXGEEVdnBT4ToqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJDJ%2FR2F0Z0H0RSRFyrcA9%2B3lJhRBdzjjm9KAZm8C29vgY1U5GH5IMB4%2BxmMNNECyxLTcfFkJ%2BmThNveodVsyyZRdgLwgnDSKWJKMc7NXW9wvxyCCP2F%2FYv5NQgAVMDtsG2IO5%2BijYpen0P%2Bqj29UV5ZKehm5xXpeFcmpDwjLJcjy2kCdl6RW0JAZoRH2dq8eX3dN6IyiaHTgiGo1iZ5gwwxXlqK6GH%2BZYJzYR5xih9xC3YkKXHtzZfcLk1FvhNS7PUE7ReTC95GN4ieMcVAbz4b8tEf5qjUbpawGHB8llmIVJeRCf1CJ6oyGYI%2FfT7UqL0PkinlU2C8sS3EvBHRFcMyaZNuHpFe4HwxBfVOsgf2ixoml3PnNYTFTjES0tB7M3TQeguCXIQs0WPN2d5UOxkEdizC0LrKyGl8Rt136xMywJnXwMlMro73mAmHZq%2Bs341HNfvHKsR8s37xGj92yJ4xJFjw406j5xNNd%2FQ4EinDC6U8jnOo2EaAloY36ee85S8QOoRrBaAIhCnEYBdVYuF0yekZoYmzjYwsKe5fDpJYiZlJIZ0H%2BwrMI63n3xKYokH9BPT4nAn7kxrpb9x3Ey%2Bv4uUoqfLmPfs%2FP06j5bx%2BceCVdkYsUhZLCikotxSPapZoa9hdLgO3ZigSMKT49LwGOqUBxoh0XnZt%2B96TieF0VyEXR1hN3G4Tr6jvZjA%2BWp8KkBofr5Nlq4nz0lgwycGE20Y4EIOANl2JXse%2F00I97pyiR3%2BUwj%2B5fUJ%2BbXNljVH6ni5Xv6PAFw%2B8qJaimEEbuK2OhM2eW3PMYi4r%2BGzUgnFFJDquKFsfnC5JHyHnWL%2FNqppOTVsIGiHHd7Vu66eab4sZwq1rnQpPxJSsnWBd3dIv8xU3%2FXNi&X-Amz-Signature=702b09ed4cd96a0e02330ebdbc59556a3ed5e7108ee589f99847b2407ffb9e71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
