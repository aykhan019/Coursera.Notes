

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPVXHHKX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDVEEd6zuaEQ9DzhE8h2kvzpWRPPQfATYA71Vg1kf%2FbYgIhAK5cvUnTu0ntfYYlexlhW6iF1q4GdfT4X%2F2rA%2BimKIegKv8DCFoQABoMNjM3NDIzMTgzODA1IgyOVIBFjqnY0YZpXHcq3APp5etUfb8DZiGXe%2Bl80Upr%2FFEsEbhr78tTvjLa66UAcp4axEWQOWnekH08pX8ni9wko2aZdY%2FoPcrJbliH2%2F%2BdlQ9tPIqdUTa7OaaF6zIaJZVrF6TIZoUCWy8zorw%2FM%2BuSaJ810smyvU91MKefurHaexrSZ%2FcpSjmbbhLUlf%2FaSY01R%2FC63dJASSC%2B3%2BlGqvGD7p9KtZ9t9Lp0m2Fr7Rd9ceyqKtl79Xb6xLJoryl0gceubDDjAKZynwKKskRuYcjQgBNiQ74ylfVea%2BJzrMnYdsBCSzzcpzdEfxgQaOKm9t6rlqDuO93pWj%2BOI7AeZDhYYjsCmm3LyR6A9G4moxtUUN7613XWeO5W3ry3KAp3Xw9Wllvo9VqYp12Z4Y3zHz%2BvrzrjSxH8id460Bx3oDXpuml37xAdNIlDx7RlPN5a5TML9tC1TUyFO7CWOIYNYM6IryNbjbNrvp%2FrK9S8xSe6WxhuOY3lzXOXN4ARxvDI4nL5FM74Jf6rHT8nQvPqWmdEZcTc3dFwIYDeReZbUFuD3g3J9Zd9vEQwF7MkVmYJfeOEqgaXxUQ7hfw%2BmIhUr37%2F5MbjS8Ch6iQvWYEdWNJ4kQ%2FoV3FP0riM7tknTLauai2DAvp%2BQCCSO3bjQjCb7JG9BjqkAefjL5nr%2BXHZrK1MCcs%2FBZRCz%2F0OIxG%2BX8vzLCko4AwrwNqQZhgObAblP%2BZhCxKuCbC5SzHv0wtEu7MF4kZp6Tv9oU6DK0rymgb%2BpYNXK7AIVXiJB6Oc1ylFV5cNx8Ax8cBh608dt2RGwZy0R8TWsC2bVl%2FAH88on21R95znrevyaQeQZAMaIO%2BN70X55snBetMnbf%2BaCbtqY7wWAOB9NgBzuAuu&X-Amz-Signature=40ec13af4fadc304795a595e1d0846c7eb0536e1ace6710950493817fd30c7a0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVRNDEKN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDWlMAMOOQdeh0hNoaWhRGhD7dVrgtngOpKnBeD9TTWAgIhAN7kmJQPMdnvwC0kzHK2gyNiUj8QWUu3FMD5PQgQhvLfKv8DCFoQABoMNjM3NDIzMTgzODA1IgzmkVYk8h1wDAj4MCkq3AMDc3c7YF%2F4kENZ1I95DKow4j4P73fkamdF7SbQM23WFzZ%2FZckp5N9eIXLTW6W8EBWpVYP4m5zKyV7GZl0aoTqGXpcj00E9evblbUD381yZYN7epjEHRZdTX2lGWbtj2qoWYlEQ0bRQ8gJvFr8vk8XL8mrOB3zFxwdyX4b%2Fj79GnWYobtDZK82Db1mxMnfBUQRDNg9Czxd8syLxR9BCzATqsGc6oVlxe5O69X57apfb5W%2FSBdCXwwTwoz2uR5D7xq7IsTCVtfBOMQJItdOrWEWH77AIqHsmFQo2aF5ynLN2RkOTNZq%2FYXc3w5XszCFc1zaKeTOCDCjsfcvbWjqLqsgvV5DwcyKuK4XSvZl73AVDb71i4nrScmogOm0E9%2BiKVucxa0KBuMbCpqLWV9%2B3B23W7ZTr2mS%2Bvd5Px3mFemHobwudai%2Bokb8wImjQ1G5yS%2B2%2BUAeoLmXdd99z3jReHCeaiMR4%2B%2BpKfjRNsOtXoEIGXd9fNLDv3wtVz5sPdQSRsl80dSbz82aCJbg1oNSx5AjPwymZpyvDUdt9z%2BMs0VpICGfO1lgGLwC665J8ij3rcQvXtnnyeMY4GtuLilLOLyvz36VSd%2F618I8%2BE6NhBkLL%2B6Vq70U6KJzyW8Uf4DCt7JG9BjqkASejstXFpJ5ax7YZVA6Hk2LE30QgEWoZc7KYPpZsUQVAiy0lsmfuoVPVw4f73DbzE%2FTr88FX5MlwxTgAGQhHupotqi%2FcDIKr%2BPp6sPVpCc8wzUgiaWon21qLKsqHBIskJFXdDmzKEJFurjj9ONpYkYMah34J%2FQa2we5RFhu5og0ZhMULEj8CyYLV7eLLLsvPl4d2iH6OrZ6jIYbPmHk6YSS1fcgU&X-Amz-Signature=c1b159d28ca7afae007906feafe53035b464061c77670d2ea76e65b8844bc2ec&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVRNDEKN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDWlMAMOOQdeh0hNoaWhRGhD7dVrgtngOpKnBeD9TTWAgIhAN7kmJQPMdnvwC0kzHK2gyNiUj8QWUu3FMD5PQgQhvLfKv8DCFoQABoMNjM3NDIzMTgzODA1IgzmkVYk8h1wDAj4MCkq3AMDc3c7YF%2F4kENZ1I95DKow4j4P73fkamdF7SbQM23WFzZ%2FZckp5N9eIXLTW6W8EBWpVYP4m5zKyV7GZl0aoTqGXpcj00E9evblbUD381yZYN7epjEHRZdTX2lGWbtj2qoWYlEQ0bRQ8gJvFr8vk8XL8mrOB3zFxwdyX4b%2Fj79GnWYobtDZK82Db1mxMnfBUQRDNg9Czxd8syLxR9BCzATqsGc6oVlxe5O69X57apfb5W%2FSBdCXwwTwoz2uR5D7xq7IsTCVtfBOMQJItdOrWEWH77AIqHsmFQo2aF5ynLN2RkOTNZq%2FYXc3w5XszCFc1zaKeTOCDCjsfcvbWjqLqsgvV5DwcyKuK4XSvZl73AVDb71i4nrScmogOm0E9%2BiKVucxa0KBuMbCpqLWV9%2B3B23W7ZTr2mS%2Bvd5Px3mFemHobwudai%2Bokb8wImjQ1G5yS%2B2%2BUAeoLmXdd99z3jReHCeaiMR4%2B%2BpKfjRNsOtXoEIGXd9fNLDv3wtVz5sPdQSRsl80dSbz82aCJbg1oNSx5AjPwymZpyvDUdt9z%2BMs0VpICGfO1lgGLwC665J8ij3rcQvXtnnyeMY4GtuLilLOLyvz36VSd%2F618I8%2BE6NhBkLL%2B6Vq70U6KJzyW8Uf4DCt7JG9BjqkASejstXFpJ5ax7YZVA6Hk2LE30QgEWoZc7KYPpZsUQVAiy0lsmfuoVPVw4f73DbzE%2FTr88FX5MlwxTgAGQhHupotqi%2FcDIKr%2BPp6sPVpCc8wzUgiaWon21qLKsqHBIskJFXdDmzKEJFurjj9ONpYkYMah34J%2FQa2we5RFhu5og0ZhMULEj8CyYLV7eLLLsvPl4d2iH6OrZ6jIYbPmHk6YSS1fcgU&X-Amz-Signature=7f0a697cbc7834edc1f49ebe970cc11cdb879bad676e814816e3bcf6aa0f3dd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
