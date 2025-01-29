

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YSIV4U6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQC9izfvCYE59jhKNGGKsF9Qgr7noPU3AWRWBtYkmudM8QIhAI9kcytnXyX95CSKN4qGwBTxgPhuTsltOWPD7zCvGJb%2BKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYusVHSfj%2FyfaRTsq3AOki6YiyzBVtNHyBCEblK5XTYgOjwAs0uDhSHMhtUn3AXxQVFhVza1HxIp%2F4X95Kur9nyQRjU82Xobf3UbY8mHDa37oWLTCrWQ8TbEWvpLm6RFNU4ynWAOnPJCi3ta7RNI%2BylkJ7QB7PnuIrMpgPIXVR0Nan2GJlJLShpM6MbUV6%2BY1qJGx73LDJ0d8e3up5eQnKQyA5xRZbn9TJWvyswsIst7AuhvHErMgTV0dg9zNCq6R0Po1mtMNAgnky8M8RHJmOA9ePyijFvRFVyu%2B1c0tZWJH2oWyDlX%2BtZoeFZBF9UWD%2FpywvCP8nLlqfVV8wcQ97NdtT%2FrepAB%2BS2G%2FhfPqn%2FJL6EZ6csYjqVal8s1ylQNCU01lofFI82N66x%2FpV7Q6siARh7%2BZHz7zGZ4d5NqJopOWmw8WjlA%2B%2B8cGaQgwJAkEgOA3U0%2FEIfgnDK95v3flp8jzq8cQMRHss%2F593LwXiRBbQ8WHkxIj576oSpHTC66yfDfwzkh0Qwn%2FC1btfzRi4zpaD40Gc1jJpxsyc%2BSXnzSrRNYCPub1XlvwPAwtKlqXhbGsfOv2s38fYq2X8PSS1I%2FUqLdgAx3xY0YuY%2Fr7v0b3pdh38SaFXBY81NeVZ3HdnoEQVKM7l4Gn%2FjDSn%2Ba8BjqkAWOUpo6QE9dvB2ZTxy49E7dniXmUoMhnGiTORsacRyIFuaSooJBuX51w%2BmhE64%2FGIZlDFSX1ozp9JdhiAywwo4sVBIkYQAgEp8aJrGqdpapxwYuNHnIQxNZ0eGz5r%2Fj7EjkRMq%2FXpSTlnMBRw2umt8o3Ja9Dpk19JtlTHulJZigIX1efnBLVoLf1jRGel%2FwYlis5vtK3Ygg4ndWxsjLmygoJjokj&X-Amz-Signature=9f579a873cc4cf7d6f48b0209662edb182ce2abb403db7c442e36e32e21c96c8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFLAJV4Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIFHeVobay0v4FgB%2FzPluOUDlylJMLOrDY%2FS%2Frl3VABrjAiA%2BvSFlosJnFdxWMTI2EWOMJmwJPaVopo%2FzygucWZSQzSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkkPDCrAlotU%2Bzsh2KtwD80uwz03ALXaOnU%2BaZG7J%2BTzQjEEmmF37H4GoqiyOtIJjRvpOAz7y9VYUbx40NM2ogXPKnsglTimvoguMGrY49b%2Bi1XNvG6GGUVjvUSAx5YLghC%2BhJLzpbZZ9gG8l%2FJbhq60lypGT4MNCT6dNPtXuyhaRkf0i8edFWMwmIADHswmdYaKJqX5kwcymc6Tk2yQUWcTcDOZw8QyC6WkdttkyApnvUzLD%2FfwtSUF5ytA7e6dt%2FDT0Ogk7rRJP%2For8PXJojhYR27AvI2TJwh940ruCmVB2jT3liHKBO%2FNNNztKR36%2FZ37SedFoR8IbrjfGqR9aV8GpxHqjS1H2qqq9czrqDfwT5BHhPLr6p69r7QPy%2FL1%2B8aObAqydKrZEHvUU2VMPwWxDjG%2FKoXsNy1cl7scjn2yOH1hBh8tNz6vqiHIsmJ8EY1I8U7TVKX9iImT3Q3nG36p%2Bn6WQokIJfgJJV6%2BW52ZPdKZlHxXfWTspUvRCNFWu4qIVKoz%2BVsgQ%2BUTTlXEzhltm%2Fhx0GViastFYBvnpt3dpax%2FBMjY9TFLTnwReSWodOuM8n%2F2zPe0kpnUkKaGTAyuX%2FDucMxIbCKsUB08dkjd%2BJ%2B5qGXPENQjPY9wi%2FD17%2FfEr7bQT3yfx9Dgwtp%2FmvAY6pgF46Fto45QpLjqnOsEo6Vkn5Q4XUDOyR34tAdlDNi658NaGAIICJQfpLTwzyHbN%2BTP%2BiZkPa27qwv01QQLQ8ritjM9evG6xwcXGiw7tI42Vh%2BQ%2BowlwWuWd8kJTm4OHcnMzpWPZCPqnRbElc5JHQLRIikWiyz%2BjILZCtf9l7PtgKfncmBKr9TNP8FAn8mWJoGyMFFAB%2FcRgF1dA%2FdMyzfKiF0aB9aNZ&X-Amz-Signature=b446826de146b17b2c057fb5c895806e466330be979b4bca7fc2d3068ce9f33c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFLAJV4Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIFHeVobay0v4FgB%2FzPluOUDlylJMLOrDY%2FS%2Frl3VABrjAiA%2BvSFlosJnFdxWMTI2EWOMJmwJPaVopo%2FzygucWZSQzSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkkPDCrAlotU%2Bzsh2KtwD80uwz03ALXaOnU%2BaZG7J%2BTzQjEEmmF37H4GoqiyOtIJjRvpOAz7y9VYUbx40NM2ogXPKnsglTimvoguMGrY49b%2Bi1XNvG6GGUVjvUSAx5YLghC%2BhJLzpbZZ9gG8l%2FJbhq60lypGT4MNCT6dNPtXuyhaRkf0i8edFWMwmIADHswmdYaKJqX5kwcymc6Tk2yQUWcTcDOZw8QyC6WkdttkyApnvUzLD%2FfwtSUF5ytA7e6dt%2FDT0Ogk7rRJP%2For8PXJojhYR27AvI2TJwh940ruCmVB2jT3liHKBO%2FNNNztKR36%2FZ37SedFoR8IbrjfGqR9aV8GpxHqjS1H2qqq9czrqDfwT5BHhPLr6p69r7QPy%2FL1%2B8aObAqydKrZEHvUU2VMPwWxDjG%2FKoXsNy1cl7scjn2yOH1hBh8tNz6vqiHIsmJ8EY1I8U7TVKX9iImT3Q3nG36p%2Bn6WQokIJfgJJV6%2BW52ZPdKZlHxXfWTspUvRCNFWu4qIVKoz%2BVsgQ%2BUTTlXEzhltm%2Fhx0GViastFYBvnpt3dpax%2FBMjY9TFLTnwReSWodOuM8n%2F2zPe0kpnUkKaGTAyuX%2FDucMxIbCKsUB08dkjd%2BJ%2B5qGXPENQjPY9wi%2FD17%2FfEr7bQT3yfx9Dgwtp%2FmvAY6pgF46Fto45QpLjqnOsEo6Vkn5Q4XUDOyR34tAdlDNi658NaGAIICJQfpLTwzyHbN%2BTP%2BiZkPa27qwv01QQLQ8ritjM9evG6xwcXGiw7tI42Vh%2BQ%2BowlwWuWd8kJTm4OHcnMzpWPZCPqnRbElc5JHQLRIikWiyz%2BjILZCtf9l7PtgKfncmBKr9TNP8FAn8mWJoGyMFFAB%2FcRgF1dA%2FdMyzfKiF0aB9aNZ&X-Amz-Signature=81679180ae3df12141099f29b74904cf27073fa1fcc7b63bd758b380129b6ddf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
