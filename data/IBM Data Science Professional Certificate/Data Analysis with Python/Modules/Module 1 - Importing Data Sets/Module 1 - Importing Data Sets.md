

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3CRBQVB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIEWPAcCddCpGFwvdXWVuMKLpFfYwcE5I%2B64Gq026ccaRAiEA6roDQYjFz04TxuMxJkh4CEI2kOIODEZodT1bcsmjUfkq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDNBQMHFtA0L%2Bsa4KAircA7mV8SujhLV7Meh9GHRy7gePbs8SZp7cK0erEMtLVhYmfI182YrZEzclbChSe4UMgiowK%2B80IEvkoaWQQPdmQBQWxWWCSKK%2B5xmBTExEnDWniVbspvZW4wIArfr4z%2BH3sVazvzH%2B%2Feb5lrCIhW5j7rx2UincEMNztQV5d4%2F92wPj9kADO5y4bkhYgQjYLj0D79Gof3dI%2FVPew9GFcLDoEdangrHIdLgUAlLpQ%2BdAR6Q4KkhDSf6WDiq%2BvgPJdFkRNErjyXy5KJNF7kJd18HdE1a7kpRD27YjkXn9eD3qyjZtPbRd6t1jv6JDRQ0xKGT5JP7q0Wy6ldbOGsk5zz05JWhk9fAI7NRWm14KecHz%2BuRorX94MlQXvqbsX%2BmpFhWh6B1Z%2FINeKZ1TO%2FK6eeiGidHC7gvsDRnHGrWa7NXlBGA3bvuEeeCHkR%2BSnwvBlDor31WuDIDdX5d%2B33HMdriZm%2BxrBuWZArjmHV76ejFTQooDEJHRTfJB68687wn%2BZZ7s5eIJSqGxL4XYtH48owKbuziVDROJGm8wOQCegzlN8yS8vUo6n5jZUOJEQ5AXps08vQurh0nYFUDuzRvT4N13JJM0Skjzz0My74nzql%2FeJhBL4BGeNtSzuHPiejK1MLrEmL0GOqUBlRimU4Wtupplv4f7tYQ889mZ1pcImbpqMw74ecOwGfWvp26HokkDEqiAtFbloPnkbbKPQnS3cQyzSucOe13Q9jcNS%2BaSV9l05Lv5fq%2Ff9Hhwj4FjqDuymuSglu36yUMmoEheU6RjFvN72cLMR9qFB3uBLoq8App1kSAruS56r%2FSpzSdV2VAX3XUUNMxx%2Fjp1qYrbyRBW8V80%2F1YSLdiRYhpM4I5o&X-Amz-Signature=bf88ff13b9bd2b118076dd67259ceafcfc9d98ce78d27c1e7ede1cf64ed2b8b9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRSEAKK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGdYZRQI9lXfGu3ynLZRG4ARkfNQ80VSmP1LrSOXP7nVAiBIRzoJsQOXDvS78PItaNDJWF%2F8ebYR0tetPh0fkDFjwCr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIME31bl9HsPVTkiNEEKtwDtHkr87Rg0nNo7J0r3r%2BWrVDh027s7447xYSLE0M6OPoCRwuun%2B4ZDGKnPxcDjD%2B72k8%2BQrbm9xFElQrlXJ0tfxiC%2FIdZM1RG2haSMFdbqi%2B2r0JiC57O8uRN9LJ4e01sHEm2nUvDGBiFu0skJ%2Fbno32GVyLoPLuXvN2WUI5rSLIogiKv5nptGQHE0pnlCKrYLHrY7CYrG5VeBxuVGLYI8k41xSZGxbPpMTv81N7cEFS9fxChmMrsgnulQBxUycwzPnGJUM%2FOkB5QzKcbN%2BhRAzYPKOC0EW9aANOcpUWiWk0gtURza0gCV5W4EHvTajYLI9%2F0xVKZCCpE3pXbQbB8400IVE1hRJ5dsbtYyDAWU%2BlZ9rICzGGTOuCPKxBvKDynGa9j8FASjSYAFB3pJBwCNm8pfVIgNCgMVgefiloGEj6%2BH6ojybpU82aBtU%2BqD%2BkkNJe4SFv3NaFnq6TuLEVhXU5TYfzliHdkH%2FDl7Z7L7bRthHWniT0zsgNH2%2BQiE5l5S%2B2JbQxWlYBNM7H%2BgLfZPf20L9oNH4I0MOdgUglmJ5deEGvUi5wSAs99HmC22iIMj1WsD8YT%2BdbaNbuOY5AcargyKLjwYMWO%2BJzbXKY0bXBUCuYw8vsyKm7vmR0w8MOYvQY6pgHn28AeZ5dxZBUKDiQOn4bEaLWHJ8v1%2BxR9cmxw7rRY7o1ER%2F%2Bbnfb%2FuREvFcTBDG2rtqHPIul%2BoHY9t7xT2o97fl0O3IAr68YcAquaRrMkH6eTINEwaCwAoy6rGaPWv4NV7hIiBOfBclEynjfhiQOaM0vrzJBaxhZJF6X4emKUYLqqxTE7QhiVjsTCb3vj%2Fq3LIqyKhcrDuDy0k9KGwy6FaylWcjzD&X-Amz-Signature=c4f9778befafa71afc7cf059b85dc701a9fe7ca0892c0968a2ea6efe5ae989c5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSRSEAKK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGdYZRQI9lXfGu3ynLZRG4ARkfNQ80VSmP1LrSOXP7nVAiBIRzoJsQOXDvS78PItaNDJWF%2F8ebYR0tetPh0fkDFjwCr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIME31bl9HsPVTkiNEEKtwDtHkr87Rg0nNo7J0r3r%2BWrVDh027s7447xYSLE0M6OPoCRwuun%2B4ZDGKnPxcDjD%2B72k8%2BQrbm9xFElQrlXJ0tfxiC%2FIdZM1RG2haSMFdbqi%2B2r0JiC57O8uRN9LJ4e01sHEm2nUvDGBiFu0skJ%2Fbno32GVyLoPLuXvN2WUI5rSLIogiKv5nptGQHE0pnlCKrYLHrY7CYrG5VeBxuVGLYI8k41xSZGxbPpMTv81N7cEFS9fxChmMrsgnulQBxUycwzPnGJUM%2FOkB5QzKcbN%2BhRAzYPKOC0EW9aANOcpUWiWk0gtURza0gCV5W4EHvTajYLI9%2F0xVKZCCpE3pXbQbB8400IVE1hRJ5dsbtYyDAWU%2BlZ9rICzGGTOuCPKxBvKDynGa9j8FASjSYAFB3pJBwCNm8pfVIgNCgMVgefiloGEj6%2BH6ojybpU82aBtU%2BqD%2BkkNJe4SFv3NaFnq6TuLEVhXU5TYfzliHdkH%2FDl7Z7L7bRthHWniT0zsgNH2%2BQiE5l5S%2B2JbQxWlYBNM7H%2BgLfZPf20L9oNH4I0MOdgUglmJ5deEGvUi5wSAs99HmC22iIMj1WsD8YT%2BdbaNbuOY5AcargyKLjwYMWO%2BJzbXKY0bXBUCuYw8vsyKm7vmR0w8MOYvQY6pgHn28AeZ5dxZBUKDiQOn4bEaLWHJ8v1%2BxR9cmxw7rRY7o1ER%2F%2Bbnfb%2FuREvFcTBDG2rtqHPIul%2BoHY9t7xT2o97fl0O3IAr68YcAquaRrMkH6eTINEwaCwAoy6rGaPWv4NV7hIiBOfBclEynjfhiQOaM0vrzJBaxhZJF6X4emKUYLqqxTE7QhiVjsTCb3vj%2Fq3LIqyKhcrDuDy0k9KGwy6FaylWcjzD&X-Amz-Signature=ca6aed732e004e68e51b186d638b2dcd70f4d6a48c722c7baeaab806163a14fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
