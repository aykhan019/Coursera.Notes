

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIQ4INWP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuG3WbsIgJZeHd1E3SUO9irKeIEfB3cM7VCEmLqJHzJAIhAMddLXvAsjUI6WHRJdmZWHLqqxDpRLz62vb3Dy3ZTyZvKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUbDI9QZCyh8HBvVQq3AMvyh0X88WSZ5LXb4jEvC1hbWh0RIrEIc5HJ%2BpxlCd4van%2F8fUZ9cvrJAA4W%2FgvR4ALkR0FLtbOiVmjvVM0yfyX8to69hyUcTa59%2BSt4z%2BlqvjR0RoglsDlwt%2B9V%2BiwHBnPfsVxqdpVlU3JFn0eHJSlwv0QvBjj5lIGenvzObSI5Xhvh2CReTwrfe04g%2F4Q%2F%2Fvzn9L%2FpOaZKHgXbcLt3pPZswZilQQ81LRHlZw%2FWU010sU6hCYo9mlHZ1xnpgszMdUjXbbwT7SLvNw7vk3XNRnDICkk5SLjkYrc1x1KAjTQGUp8Qlm2IfVam2upgeJ2VhcHa5kiQIhPJbF0Y5ddZvQ08El4gnXy9j69pFkK8y0GZgSZfW4H3vqTuNMvhAwNTx7cEJuhRIlxYixzQ3q08em5JAN8tvIbQtAI7eJgzTO%2B5febxACw0LDFbuFK5s9oW1XL3jk%2BBqgxnx%2By%2BN02f%2BNMu7Ho%2F6dpfmxQ5Ret1hOwLD6b4Zx%2F6%2B0e8hZKZSAl9Q%2FXICSxIPno4etxJkw5oBOBK01zv84XbQVuGDr2B%2BfcpHHkkMWGZGQadZRwlenqnp2HLMtp5LDTKtim5a4ce%2FDCM906xvVTypN74MArf5RyAKHCqDbi1AxGT3%2B7%2FzDXvf28BjqkAQNnBwYzh4w97OxZQtltsQup57%2Bq1eQF9z5XPXGWwDUhkuqGk1sZyqThcnTRju0bIG5sbryl7Y7GdKr9B3KlylxmQI2A3S5SpVsBdNUFpW5OVKsIRa%2FmIFEI%2BykcpFmFIMo7JS5Z1QLbECBOMi02w2C3VJqSZbxukAFtOw3e0tHSafWAu9SbtT5zDjZEdZ1fXfTdaUFUDPjYWkGzZZeac%2BBFhA0H&X-Amz-Signature=e1a1ec93383055b761bc1e6263e095c84e03560ad7998219c8181fc49e949b28&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FSI22US%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi1lYGNJ2G2mdfhtoVYY6uPDh1rwx5hI1gx%2FWhMAxEQwIgFKmDVkQezMh8%2F9kl8hWDQE1TIXpHVww8NGr2Ltj4RpUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEkSkvTw1Rx9pag9AyrcA%2BW8qDo9g5P6kHpbupI9D7SIK4coHPlbaRYNw6S67Z%2FkXq4hYeVUI9v7I34J%2Fr772yGQpD1fpX0uGU58kouz6NY9WfBQSilG9ovslyYF7ZvV0z2SY%2FiStzvkKpsSI3%2FtiKw56WueL%2B31d%2BG51Kq%2ByU9Iyy8UTCkzcA7R6f0%2F6xkgHkcXQQ7WQ5grXc3i%2Bhf%2FcTziHxDtD7XK7%2F08IPbuvaGN%2BiBgdKPGM3ymzY%2F1deezp8IVyq3d%2FGS887CevmK27nhl11cDsFxujNXwAW0FAK6dVFYTHr3rsLnI6B5Az7YdB0AViI%2FG%2BBJKhhjp9jq9nsF6AljAzWH3xOgD%2FBD3d0uLnUGo30V%2Fd%2Bunw5zALPA4Gzfi3ykWFqBljHQdmWLCvpC%2FyUIMs2HINQSt9bV%2BZRB6CBgUhUEbmOKHMa14zHv4oyWkABuqQCn3mrGa680m%2FLuJc6LvyFkI%2FhsRfM2WvSceSTba9u71lsmKAQ3GXhILkmXDkZroxJtS8z%2FE%2Fd2dfp%2BHvxt2CgHidMdNewegX58grCib3tRKnv19NFxvk5o0XGQ5LaNZGEbr4DdsWm6n4WeCKseKSMSGc6D3BM68kpsX71nJLS5oUOTp%2FaISkN1cBRbI9w%2BpRt8bb5tNMJq5%2FbwGOqUBCX7vRCcdDmHZx9aet8K6ozyYDYwfh23d7Un9xtW9StS1y%2FtAro1ZEOjigm0M7peQrU6Ac88EhYz3UiKFX%2B02%2FuWxOZPf%2B5QcswkqLwM1t2AZz0Iwwu95IphPvdxi%2BcJ%2Fy3yt9wds114IMydkdhcb32%2BjtQ9fLbowMEGpArYEUYPAlqHduzMiloKw7Ps6MW7wH8fOculFcJ%2BAoKhmNJOR37UZK9EK&X-Amz-Signature=118b9d152b7d7550e84e77e30da315f6746ca9dc112c988175350ceededda30b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FSI22US%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi1lYGNJ2G2mdfhtoVYY6uPDh1rwx5hI1gx%2FWhMAxEQwIgFKmDVkQezMh8%2F9kl8hWDQE1TIXpHVww8NGr2Ltj4RpUqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEkSkvTw1Rx9pag9AyrcA%2BW8qDo9g5P6kHpbupI9D7SIK4coHPlbaRYNw6S67Z%2FkXq4hYeVUI9v7I34J%2Fr772yGQpD1fpX0uGU58kouz6NY9WfBQSilG9ovslyYF7ZvV0z2SY%2FiStzvkKpsSI3%2FtiKw56WueL%2B31d%2BG51Kq%2ByU9Iyy8UTCkzcA7R6f0%2F6xkgHkcXQQ7WQ5grXc3i%2Bhf%2FcTziHxDtD7XK7%2F08IPbuvaGN%2BiBgdKPGM3ymzY%2F1deezp8IVyq3d%2FGS887CevmK27nhl11cDsFxujNXwAW0FAK6dVFYTHr3rsLnI6B5Az7YdB0AViI%2FG%2BBJKhhjp9jq9nsF6AljAzWH3xOgD%2FBD3d0uLnUGo30V%2Fd%2Bunw5zALPA4Gzfi3ykWFqBljHQdmWLCvpC%2FyUIMs2HINQSt9bV%2BZRB6CBgUhUEbmOKHMa14zHv4oyWkABuqQCn3mrGa680m%2FLuJc6LvyFkI%2FhsRfM2WvSceSTba9u71lsmKAQ3GXhILkmXDkZroxJtS8z%2FE%2Fd2dfp%2BHvxt2CgHidMdNewegX58grCib3tRKnv19NFxvk5o0XGQ5LaNZGEbr4DdsWm6n4WeCKseKSMSGc6D3BM68kpsX71nJLS5oUOTp%2FaISkN1cBRbI9w%2BpRt8bb5tNMJq5%2FbwGOqUBCX7vRCcdDmHZx9aet8K6ozyYDYwfh23d7Un9xtW9StS1y%2FtAro1ZEOjigm0M7peQrU6Ac88EhYz3UiKFX%2B02%2FuWxOZPf%2B5QcswkqLwM1t2AZz0Iwwu95IphPvdxi%2BcJ%2Fy3yt9wds114IMydkdhcb32%2BjtQ9fLbowMEGpArYEUYPAlqHduzMiloKw7Ps6MW7wH8fOculFcJ%2BAoKhmNJOR37UZK9EK&X-Amz-Signature=a0b2a8c8ade04ff1cf327076a1c6c3526de7fbdebc8ab1840a9b1163f625e693&X-Amz-SignedHeaders=host&x-id=GetObject)
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
