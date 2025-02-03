

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAHDFTHY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGoB2bbrnvrR9065UfqPvKrhs40kvEEte8ZJitUFwAvnAiA5pfEsMMz9ghf72qcS8iMdHoE%2BnQL4NWTzE0PdWRcUoyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIM0fA4bpC41hWKXnkAKtwDSYp%2FxU4QHKAdfbiG9POL7gMMs432Dd%2FWBUUXMHTeQyWv%2BvpFxMZaJjaTe0fSY7aPVi8Aio5hSMXBbVRXsS4PLEyAw2scbLSTYFQmkXqQfCMbOy94Mr4V8aauBgkfksOzjyMia3B5G0qa9daA9ajcXy9Xj6PycovLsCSYMqwX6PxCacz9zcUswc5CktOnd1znzW2BZy8%2F1gPel5RpK6lWGYh%2BXJRd6xuLNwXSFSeaiG9aoOPizHQwgN79POQHk1J949ATzW8hypT27WdFXK1poXpKQStxDBrp00miCv3iodxpezBqwZn35Hu2pzMgEqwuP9eZbTg0H6r%2BvlPehroiooByG4n7mfBSaWjkgUD3sxhRkeX0%2B%2FrdJNEY%2BB0jZkjAQsG4TkUYFrs5njlklb2KGmfjnTXy9qLUkUO1o13QOBzd%2FbR9xwa2AeTYCJdNlHop%2FZZ1%2Fhz3xy9kaBF%2FjQJBeFMDXdCU7qU5NZ6YoloBbOJQeEbns4Z8oUVtOEEL80pH%2Ffu7zo7N%2BKvkTHRo7fO93msyhYfNBTm0EVHfknjyCVKW9G9vf1okbKzBqqFSx8IjganfGnHAwyCWFXO1CIzf9My4afEKHIYVSn0XnmObDLRn7iEPGKk06dKNEoEw8bSCvQY6pgHh3htQloj6uslR9epi9XsbhsRQbaoKP6vD6yBt2HlD9LSuOi52DGMymriO2uqljmu46jwcrSvSsQVrbqrqOMea93LSbipYMgBq54qLaW5bP0rigMbSbglfWsraI9RPTHHnxwYxkfd%2FZkzbzMGxbTzu%2F6o7Eb3973bdaJV2fufPgdrFazi6qSCMHz8FbiXfXdqjzei5rS7VoTRZDKHdTsCgLazrwspR&X-Amz-Signature=9cfa188cb5f2187d9a6688604e8a490fe7b21ca645beef002a7f50f9b39b86ad&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNZNBAHZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGFGcr4znOdG0LwreoRjONCBe6UAsMgJ9Fmz%2FcETJLHWAiAMNlXPme%2Fvz8CgDPVasraKOBZHs5X8eSrmN2%2FYZMnG3Cr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMgdwEvopj8kKm8AP0KtwD4lLWRFixsx52%2FEhYKwmh5JkNRWNPBNM04RmKAekipaGzSWN4zWpiBbC2f35eeIN3nxlj%2B7GVqgSR%2FVSO6x8JbAxSV2ZH2tGl6V2kVX4B0Gs7%2FqnXpB6L8mgHRAALFlnbcoXuIlQPX5BpUs%2BZfd0Yae5zVnZ2y3kIL%2F8IkV%2B5oCddhv7VxkQyfk%2FIjm80EfCtotqK2iSt75PqeiNb9BQIjhASo%2FlSLc8mkFZi9SixxGh11JXM4ClKZj3VQFGqjno7R2ONv6axRhCOaTVykfD5lmsvSLZNYZONAABsXEPDICpErkVuHLzrzU32USs93Yo6EMboEGv4aI%2FNcaTHnyK0vyL9KYvC58LWnSPsQPWO51or33xCoTsVXCbiq8tQzy0%2BMBq70ZqgdEvOOgHGrx4howVEcADBoOzOdCUBxORbNg5BKw0SgC1M3OgXh9PHOB2fwM4nDBnyhh5nJGIr5Sq%2B1XGXLih76g8TvA5290KXEbm55VQb0WmT1x2VTzMgWAf5H7EYr3NaV0Xk1FB%2F3zhJ6jBVndCkapcH4jRBJ9jdY5E9zCRds%2FhSeGtKnx06eMkkz2WNemkbRqUduFOa7800mYeAbbdwfRvk5h%2Fd8bm0dfkXyXakY2rNcbR3jxwwk7WCvQY6pgHE5zrZI9cGN%2B34FyWvdOzeuqvHfywfRNooOlEFM7lytBx0ar3R6JpoSi6nXknPG5zdNjZV6hlAz%2FWduO4AABXEGQ2xmuDU6P9jgdB9BCXgIIofe0KoKqVDJdaKqK%2BG74%2BE2kSOO1hnd31A4A6Z3bscvV%2BmNJPyGmjuujWWQjsHHjStf%2BX81YB8yakxgF3cOR2WdND75R30Y3JIDrucAkNclIG1VqFk&X-Amz-Signature=1000071eeef32f6bd88df8a45af0582478f301c332ffdd3881eb3d347a4a0dac&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNZNBAHZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGFGcr4znOdG0LwreoRjONCBe6UAsMgJ9Fmz%2FcETJLHWAiAMNlXPme%2Fvz8CgDPVasraKOBZHs5X8eSrmN2%2FYZMnG3Cr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMgdwEvopj8kKm8AP0KtwD4lLWRFixsx52%2FEhYKwmh5JkNRWNPBNM04RmKAekipaGzSWN4zWpiBbC2f35eeIN3nxlj%2B7GVqgSR%2FVSO6x8JbAxSV2ZH2tGl6V2kVX4B0Gs7%2FqnXpB6L8mgHRAALFlnbcoXuIlQPX5BpUs%2BZfd0Yae5zVnZ2y3kIL%2F8IkV%2B5oCddhv7VxkQyfk%2FIjm80EfCtotqK2iSt75PqeiNb9BQIjhASo%2FlSLc8mkFZi9SixxGh11JXM4ClKZj3VQFGqjno7R2ONv6axRhCOaTVykfD5lmsvSLZNYZONAABsXEPDICpErkVuHLzrzU32USs93Yo6EMboEGv4aI%2FNcaTHnyK0vyL9KYvC58LWnSPsQPWO51or33xCoTsVXCbiq8tQzy0%2BMBq70ZqgdEvOOgHGrx4howVEcADBoOzOdCUBxORbNg5BKw0SgC1M3OgXh9PHOB2fwM4nDBnyhh5nJGIr5Sq%2B1XGXLih76g8TvA5290KXEbm55VQb0WmT1x2VTzMgWAf5H7EYr3NaV0Xk1FB%2F3zhJ6jBVndCkapcH4jRBJ9jdY5E9zCRds%2FhSeGtKnx06eMkkz2WNemkbRqUduFOa7800mYeAbbdwfRvk5h%2Fd8bm0dfkXyXakY2rNcbR3jxwwk7WCvQY6pgHE5zrZI9cGN%2B34FyWvdOzeuqvHfywfRNooOlEFM7lytBx0ar3R6JpoSi6nXknPG5zdNjZV6hlAz%2FWduO4AABXEGQ2xmuDU6P9jgdB9BCXgIIofe0KoKqVDJdaKqK%2BG74%2BE2kSOO1hnd31A4A6Z3bscvV%2BmNJPyGmjuujWWQjsHHjStf%2BX81YB8yakxgF3cOR2WdND75R30Y3JIDrucAkNclIG1VqFk&X-Amz-Signature=175c2a8b10f8f19520c85dc6af83a2f01268fe2b770bf8389b51836cb04770fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
