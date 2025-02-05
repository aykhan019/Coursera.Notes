

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GCYBBYE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCICKOVOczD3ZNZWjHt0fdwpr3sFGdbCi9ApPEel5HGrq1AiBmxnYgkdFchEAEeiWGk0G7Y4%2BRBMIbf7UQVfSEdAwaWSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMbwgaBbTGD0BAQ4dMKtwDPs1Kg6Lub5kntioPXFpp3d6btTwpdEd6lNeOb3%2F%2FDNmDMVkt5WXiVUv4a9q8PvxxAr%2FtaD2nUW4QRlbq9upscTHfjIC2X7ud5j%2F025M9b7H2k%2FKihhXjxCJLOpANQMIIqH1eUoffxL6BTiK3BddcqSaVZYU%2BQk1xgx64u22NalPrsAFxIDCoDT52y1OVkFL01px8F7PLar%2B7DX33s%2BMslyvw6F7aD8ju2GJh1QbxTFoNw1a5WMpf3CAzm4Tip9DAWSn8I2atlFVRfwBhvWO7IlslzDJtv49umZPuusKfl%2FttqIs7ExVbJdhsBmKysuYw1sxWwThljlFva8zFj1Lp41MJU1occUrNSkEdKgaFKvJ%2FX7szsTIED9Wzd8JDjLVK3egih3gc5wAFSDiIoOZDwJui2y8IqEyEOgIGiQeK9680Pd4ulNv2IK93NO%2FyWgEf9rrX0AMDqGEj0Mte5fPERhg8K7hIDftT2jAPUN5bMo4FnpxQcC5O4xAX8NGQQNsEF8VKu9%2FX%2BBu7f%2FCHX7V%2FadUMAYiJ8kLE2KofaKVySOexh8DijGgzgnSQW1F7vJr8kwV4NDWybwlrPCcn3L8VAud83leU%2BgzO8jk3qcrFnIxUcNUctZz9%2FOnH%2BewwnpaMvQY6pgGrEh2kDYDgXQA15fa2zSq%2B84wTzk8g825lRaQ2YwtSvDsFICuF8xQDiFcWBfm7D5YIW5bitfGAcn4pHxdmD1%2BCdEEzRDlbEh%2B5F2orf7uBQ7R2Vt0Z8e1AhxAf0vFTgIQRWXV1nyn0E%2B5g1GMRUtnQ9qJAhBuDpvnmzitxr8EAb5FyEn4AFRFi0zHTFx%2FuxynYGKaWNL%2BqElWpJrP2KpDaMwQLHlHf&X-Amz-Signature=5cfbdddc433f0292142394c1656aad39ad1ff99013e291b51c411672bc020b54&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OURMV2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDB0vYLxoDKsZ8LHFQdM5uDob8WBacYPTROBp9ubSstPAIhALZsQmD81ZqbLTVW%2F1jkMZiuRMKTvvSWPu8wVdBRxMYtKv8DCEAQABoMNjM3NDIzMTgzODA1Igwsuf3HLK5Kpq9EqC0q3AOB2SnSdRbYwN9HRu245WQvblze3gRgvGwKVLZc6o6ZD%2B%2BEmjRoGhjfcx5%2FJ1GSebSrGC%2FffEdw3hoBRhmCHDSLucd%2BBvB0BflHI%2FPYlZFq6UA6QdNTt6%2B0NuiKgXzN0qdRlUpxJNPHnm0icNR0veteRcT7ZRzEWvhdPDX9E32ITnBZvXyxIurampbkv429mSIOY8Zu0Nt%2Bju6pzi5xBSqLGwPXJEOUHguKcvO3fWWC9xRzywheV7eHLK%2BUE%2BgUTcZumS%2BwTxg3ofn9dKcTIdP7Uu1Ldho0mJvUuPwhOmAAEVgH9766xxVR3Efk59GcB%2FwBEMzu4%2BQQyhy2Qqvo5fQuKBaajspXbKfYlhNG0cF%2Fv38JfLUr4R3%2B5n7Hv78rSe5K3SmvXlk73z3YITqwPS8ulDWQzPL8iSZclwO4%2FpxMm1BETtFcSZXOac%2FclhCyZs0%2BqeL9K1d28%2Bon06Xfu0URRrrzXkiHzP8%2FhsnfBQhN3nGWSSedcO0L5X%2Flyp5%2FodStRDJHXDjTgTEUPxRnDVHkki9HupcYRFnxTcjy9ghIEMdBx%2FhTB4vgA4904dnY%2BSTEA22155KNkqBPBDRHcCKsqZ%2BFqiVT4UuLWIFlm4Na5DULGzuSZvWq71Pj%2FjDgloy9BjqkAcICFrniZjmllRakB6LEZL4YiYAKTgH2J4dEch5x%2BlAV1iGp00TGv8HLAhQV4%2B04MWCOLDlbM1PzQ%2FATEAXt5NXNoxGWIQw8kKyEoacDij41GoeLzH4HW%2FZ4rWa20CUySBKtsda5ng81oiDAFlNhBZ%2BDQd5Y1UEwKYTOpZqOP1YGDzShiZcjIhagtxULOD%2BXqLt0%2BzjoSsiFyMryQX9KHiKG0RMx&X-Amz-Signature=62bd8856ed408f3adfd0e78a3027ae6bbd5e940548c70261805875c008453a69&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OURMV2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDB0vYLxoDKsZ8LHFQdM5uDob8WBacYPTROBp9ubSstPAIhALZsQmD81ZqbLTVW%2F1jkMZiuRMKTvvSWPu8wVdBRxMYtKv8DCEAQABoMNjM3NDIzMTgzODA1Igwsuf3HLK5Kpq9EqC0q3AOB2SnSdRbYwN9HRu245WQvblze3gRgvGwKVLZc6o6ZD%2B%2BEmjRoGhjfcx5%2FJ1GSebSrGC%2FffEdw3hoBRhmCHDSLucd%2BBvB0BflHI%2FPYlZFq6UA6QdNTt6%2B0NuiKgXzN0qdRlUpxJNPHnm0icNR0veteRcT7ZRzEWvhdPDX9E32ITnBZvXyxIurampbkv429mSIOY8Zu0Nt%2Bju6pzi5xBSqLGwPXJEOUHguKcvO3fWWC9xRzywheV7eHLK%2BUE%2BgUTcZumS%2BwTxg3ofn9dKcTIdP7Uu1Ldho0mJvUuPwhOmAAEVgH9766xxVR3Efk59GcB%2FwBEMzu4%2BQQyhy2Qqvo5fQuKBaajspXbKfYlhNG0cF%2Fv38JfLUr4R3%2B5n7Hv78rSe5K3SmvXlk73z3YITqwPS8ulDWQzPL8iSZclwO4%2FpxMm1BETtFcSZXOac%2FclhCyZs0%2BqeL9K1d28%2Bon06Xfu0URRrrzXkiHzP8%2FhsnfBQhN3nGWSSedcO0L5X%2Flyp5%2FodStRDJHXDjTgTEUPxRnDVHkki9HupcYRFnxTcjy9ghIEMdBx%2FhTB4vgA4904dnY%2BSTEA22155KNkqBPBDRHcCKsqZ%2BFqiVT4UuLWIFlm4Na5DULGzuSZvWq71Pj%2FjDgloy9BjqkAcICFrniZjmllRakB6LEZL4YiYAKTgH2J4dEch5x%2BlAV1iGp00TGv8HLAhQV4%2B04MWCOLDlbM1PzQ%2FATEAXt5NXNoxGWIQw8kKyEoacDij41GoeLzH4HW%2FZ4rWa20CUySBKtsda5ng81oiDAFlNhBZ%2BDQd5Y1UEwKYTOpZqOP1YGDzShiZcjIhagtxULOD%2BXqLt0%2BzjoSsiFyMryQX9KHiKG0RMx&X-Amz-Signature=1ac44db06eb59acffc17e62d98063f0282f7d687dc38c0109ff72db5c11c953d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
