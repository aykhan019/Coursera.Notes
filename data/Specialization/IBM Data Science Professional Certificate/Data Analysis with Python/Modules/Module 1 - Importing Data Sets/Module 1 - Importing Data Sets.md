

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW5AFMNR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoQxwpoOppwUuVM3h%2FUh1tqRsLbuZFBQgWvo%2Fu7KvptAiEA6SpUomaMWT5V%2F8Y6qRPAxOWHQZZvH5lBmxB8ExF9S%2BYqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAaegERZuRL1VNU%2B4SrcA%2BJo2KKmH1W%2B8f0pFD2%2BzbzrDge8yfDAVFTHeDjAlMxvSGOKUNE0pfXi5FC%2FmoWuUbjRA%2F7S5Eon5Fgg1%2FPNhiOn9%2BOuQYFQ4nJgr42r%2BaNn%2BB07V3HeqqjNx92uXj34IyFPWTgobQbOQ82rKb%2B%2FZV7SIex767pLXU6Io3UrXgceV3LJjaix7qRDAijarYhjKsPXTFIusvUWEFFSt%2Bep0P8iVuX3kVZW0LGeVzHVTBXK0%2Folqdk3yYwB1DINXlQ9hgABRI1lUE0xcaQ9zA0NrljvWNDdIFG9JM2WCMTvVxATnO9D%2F%2FlZ7ly28Kpl%2FXjNKT7uVJwY11oK3yJkRFtpsFr%2B3VBAA%2Byco7CZRiFFzcZsWXp5PUSKGCJxootklGAOK4nZDtBZ0oNXrLbAptpopce5N3Jy8S5qj46LPaDSORy77JReA2blhU3VqHiY3R%2FX%2BDQkPvQCOZ0liP98pzAqua%2FbmSIY7WiJccC3xsfgxBjeOLa8IGtzzOhKFIU8dnd3mpu0Q38RFUupngXwo23OZYrSdfZDoQyKXz9mtv6qVm%2BxPQJxZNfMu%2F8RDzUYAidiQASpxOqCCbs0ruLJJgJ5iDXQmTFldO6zXxk7UPgwcQo6AUazNmYtE6JcqEL2MPHi8bwGOqUBanokrtnKml%2FuAwhxe1qDFXgtN%2FnKc0AG27DFO%2Bm4VEteQka0UEj8pm86n9yKvHcB9bkSmokxFIIPxvbGDvjwxN3fTjWfpFQTJKDKVp1JPzZQiMxiJUYv%2Fo5oMOTXh5KbKvVfHpIjoi0K9oUE0rH9bWMj%2BL3UTtyFigm1XCfpiu14%2F8Z5r4hrCIJUV%2F0sVgjOgHbDl70TD97xvhopsEM8NzZDkeB4&X-Amz-Signature=d48806c87c17b39b24678722b0f2af86c5245d41a679b808e68e6a554f07043a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622DKIN5L%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSxiwE4%2Fx5xGF0OVdqz91A9113L2nW4G3Emyug9aZYmAIga5yXsGflzXiPDdmKhiszk30MVAlozYukvjTbVoCVH%2FoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI0bq9hortzQPsfdeSrcA1dPbSZxVK%2B5dL042VvKL3N7QnvsZveU1IwF%2BpgIe7ix7CpkD8BYm75n1jHxEoHcQSA2uXYZ65tHO0EBrLa1Yp4XnLbWIW64FeRvfN4E1ze50GSU97kjAlc8%2BmafiDqxuAoJVctj4wp%2BLiPUTfNYipxacXisv9a6E%2BdcyZfN%2BX5qNvI2w6adDA9ZcQyn0norraQ5%2BAoIJPPAXpTVbQoNoAFGzO2iMtPNPWKJckCvUg0tJwdQ1vahqHoJAunzSjxj9pIWIh6zwP2WX8CiZ2rn1vxLA41w9hPPeVFZNfwgMD30kp8%2FhGiS7W5NhwHL%2FJ6AUwBe3WR9kQWYoxuussNb8NHiDWrfYaX14bDMHpUZqb3GYPsbBq3xy8bv%2Fi8D5YlJBtDn%2BrhqgB9YarDFeacYIh0hyRXWwUfe9Fh6PR0r7zyBGoJ4OIcBi9AlRGrTI2Kj5RZaiYO2e%2BM6OJ4E3VrgtBfAI7enoq3girv0pznFZVDej3sRKxBH%2FN5PJps%2FY%2Bzz28wujuyhDoMeCO07sZo0bQe%2Fuve6p26bE2Kw2qBSu9JKX4aUnDVLXuXTSkth3s1a3wq0sLLZlepEZzXCrSdezDVjZ9YAfTXnwlriZUO3xomvQ3Fl7F2D8mg59PS5MPTh8bwGOqUB4Hix3f4nErcY02VzGxmBT8JF8J4pkUYhyjXIHoevpuf84%2B79zT9W4%2F7bm%2BsqLpcHq3j%2FsIWz8PDQBK95i%2F63FSmHeJhIXVjQgvsovySiDJxliFtRA2W3rXJLqibYajed0tXrR7b8%2BIAPJ05hvnfHWlOxQWvLL2Tsx4DHa%2FIfaVp9Zcc9dwYg9P2rkevPLiZAmzoeEH3eiAQloslq%2FjS3FIag9F6k&X-Amz-Signature=ec30936695d4fe3816f5a85522bc4d4dcc46f2a293905315ccad036de5e4b990&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622DKIN5L%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSxiwE4%2Fx5xGF0OVdqz91A9113L2nW4G3Emyug9aZYmAIga5yXsGflzXiPDdmKhiszk30MVAlozYukvjTbVoCVH%2FoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI0bq9hortzQPsfdeSrcA1dPbSZxVK%2B5dL042VvKL3N7QnvsZveU1IwF%2BpgIe7ix7CpkD8BYm75n1jHxEoHcQSA2uXYZ65tHO0EBrLa1Yp4XnLbWIW64FeRvfN4E1ze50GSU97kjAlc8%2BmafiDqxuAoJVctj4wp%2BLiPUTfNYipxacXisv9a6E%2BdcyZfN%2BX5qNvI2w6adDA9ZcQyn0norraQ5%2BAoIJPPAXpTVbQoNoAFGzO2iMtPNPWKJckCvUg0tJwdQ1vahqHoJAunzSjxj9pIWIh6zwP2WX8CiZ2rn1vxLA41w9hPPeVFZNfwgMD30kp8%2FhGiS7W5NhwHL%2FJ6AUwBe3WR9kQWYoxuussNb8NHiDWrfYaX14bDMHpUZqb3GYPsbBq3xy8bv%2Fi8D5YlJBtDn%2BrhqgB9YarDFeacYIh0hyRXWwUfe9Fh6PR0r7zyBGoJ4OIcBi9AlRGrTI2Kj5RZaiYO2e%2BM6OJ4E3VrgtBfAI7enoq3girv0pznFZVDej3sRKxBH%2FN5PJps%2FY%2Bzz28wujuyhDoMeCO07sZo0bQe%2Fuve6p26bE2Kw2qBSu9JKX4aUnDVLXuXTSkth3s1a3wq0sLLZlepEZzXCrSdezDVjZ9YAfTXnwlriZUO3xomvQ3Fl7F2D8mg59PS5MPTh8bwGOqUB4Hix3f4nErcY02VzGxmBT8JF8J4pkUYhyjXIHoevpuf84%2B79zT9W4%2F7bm%2BsqLpcHq3j%2FsIWz8PDQBK95i%2F63FSmHeJhIXVjQgvsovySiDJxliFtRA2W3rXJLqibYajed0tXrR7b8%2BIAPJ05hvnfHWlOxQWvLL2Tsx4DHa%2FIfaVp9Zcc9dwYg9P2rkevPLiZAmzoeEH3eiAQloslq%2FjS3FIag9F6k&X-Amz-Signature=c8961aca9d9217c92bb96582985a00ce2f8b9524ae2d4d93ebc60d8bb427b30b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
