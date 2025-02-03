

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF2G22OC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFT%2BOeHZgB0nD6HcqtfY156Sz%2F8D4tcj5OA2muIX6Y6ZAiAL0OvnVaslAfdCZhxI7lFbGehSMgvnEfzT%2F5gcEvjDwCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb9jJxcIr%2BZ%2Fa%2B2o6KtwDaGn%2F9ljUvDxqIk%2F1TzR4F8%2BDycTq5Y5Nx%2BUwL7XZVSCUV7xo6cmw8%2Fz0g8eKHtJLvqh1n3lbfhShm%2BTrIm6fjn%2FjM%2Fy%2B%2BxJ6qh4iDJh5mxCDlWtdc9mbWWvu4O9pUYYI0tF4iwJ3NeFrXzSIZms3q9PMSHO6AtCipEwuKn%2FYDY%2B8re0CMkbrBK7Yp92z3A%2BOuBrwS%2B3zDvyxrKEIlRGDA0p3R50N1QVlrvJYvMhgb54BEgwHzbrJheaOY7qWCdFQ19zubN6ClZ5ds%2BD1r3ERqtxsAdslhcW2hjEcrEO0Opi%2BwiolItg8m3i8XUuZInZFlkHqvmzQpohxfoDi%2F8DzGCyQBXRK0f5dQhXNd6t3fYChUVw70TQHzM9xfDp3QThVXsQ%2F8%2FahiW%2FAWIebHwkBim0fXJNgpb2N6DDF%2FQlI6uAAeow92IPJObmkmTlGCSkLjrTyf4lOgF%2FY%2FzHRcU3L6jaCIZMFTA0i4w3geLJb3F%2BDE%2FK2NukE1n6CaDDRjXkMnNGQGwYCclJVOz3OkKEBlZQRm4Xr0qKTY7hdyr4uipbArmxQRSniBzz5bjoYsubST9ymWEPriLjV%2Brob7tjbn0Iafu0qndlWez67WGneymd72BrspRzJ4cA3OuYwu8CAvQY6pgFlFJU%2BBfVHIFjImjlqF9%2FCiOKzialdUZ%2BsgyO7u0LbeSfUoP%2BnY7mKi3EUK3XKwl9YPDr50t72Rwse9ozU03KMOCle%2Bcv8686kb2GPfjLvKevqY1o11BumTtkc8Qj%2BmAd7RlG%2FP%2BVeSElcgGMZr9yaj58byLeJqP6ZtHK5fSzrKhV07IjC6k%2Fxqm5ok%2BOlzOuu8hl0d%2BXV9%2BO%2F7yOK%2BXx9u%2F7cjIPk&X-Amz-Signature=372560e42e6f5f5f711d5e7181ec228b9a4013d1221545a98399893e69859c1c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCXU23XA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBBPY2kXubKUrFjZLB8uuaCFRzdu72n1ajgW7BupEPp7AiEArpWQUB5RDLUJO%2Fd7CgeaS2sQAQR4owKLKp%2BcMIbSUWYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIjSSggiH26T0Z0hBSrcA4Pf3e0DNzo7tD%2B%2BoPOCdnjNsERou%2Bc3qJCy7Fc3LhruKncCHf7lge%2BRVanfypDogEoghBMob%2FvZ4aedPD8gv%2F12zdO%2Bl63GWVzE1EsjFkuFTSfUPw2aCERMrDTiSH3oOBlqzZ4vg8UtKJiUK2J8KHN6MBW8cpi6l1gaB9m%2Fx5z1kK0L%2FqARM%2Bg8uzX64qMqgGZNT4KGbOpzSX0%2Foq3tr%2FxY%2ByrsKDchZApHK%2BPhU40W0yqm69HHpX869EUYnqs4FfBsF7wjI14LA%2BFhToBMNUC4WaVqfGqEiGGW6zA7xI5TkSAYvZ5C1UKwaJc3vxHwxWHJdSjTQq6eFrBEmizAdnQ643c5cWDW8UL59k0ebc2RRWZSnKjCwPet3biNY4U4OzEufUeMduYzEKbXJtw%2FOLwVhahAQL2lRdk2%2B%2BTQSbfBOLKeOtJJq3a4AKRHgvMf9V34nRFxBLV%2BQUm1KGgj01C%2BVmXi20Q5NY13Mk6KYe05CIufcYxzo3J0HL3WEeuHqBTjkfJLS0ZScZMPJP3rvD6Tn%2B2KJ2gbMgZSm2cJ%2FEE52PaVN%2BRAR1cyW3fxseraGLI6O4oAr5T%2FLDp%2BC1CJRT%2BsXbM5F%2BhDIhmlrPTe2OjiOjvQCqtwIfYP4XTpMLe%2FgL0GOqUB0TgHiIcjKHF3dPXPcerpNRRdh%2F65gNH9PM8%2BizhsTi%2F%2BoKFFL9IGzshGTI77yOjlwCHTGIEbGC1WYnNsJHxClF%2FlJg2lNhnuHbiHdXIoEblDKYHqe8MRq%2BNkV9xpghEFxoQWv8iu1S6itl2vEp8ZwTkRTZTsbM2aLF47HL%2Ft7iy8nvBriFjUEVRfL%2BnWtq8t8PhabzU7lONYGQnu0TufXQG3TrWq&X-Amz-Signature=4b27b8b358e75bf759bfd740d46e6d29ce918e19ae1d88978c9a907651c3a0e4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCXU23XA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBBPY2kXubKUrFjZLB8uuaCFRzdu72n1ajgW7BupEPp7AiEArpWQUB5RDLUJO%2Fd7CgeaS2sQAQR4owKLKp%2BcMIbSUWYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIjSSggiH26T0Z0hBSrcA4Pf3e0DNzo7tD%2B%2BoPOCdnjNsERou%2Bc3qJCy7Fc3LhruKncCHf7lge%2BRVanfypDogEoghBMob%2FvZ4aedPD8gv%2F12zdO%2Bl63GWVzE1EsjFkuFTSfUPw2aCERMrDTiSH3oOBlqzZ4vg8UtKJiUK2J8KHN6MBW8cpi6l1gaB9m%2Fx5z1kK0L%2FqARM%2Bg8uzX64qMqgGZNT4KGbOpzSX0%2Foq3tr%2FxY%2ByrsKDchZApHK%2BPhU40W0yqm69HHpX869EUYnqs4FfBsF7wjI14LA%2BFhToBMNUC4WaVqfGqEiGGW6zA7xI5TkSAYvZ5C1UKwaJc3vxHwxWHJdSjTQq6eFrBEmizAdnQ643c5cWDW8UL59k0ebc2RRWZSnKjCwPet3biNY4U4OzEufUeMduYzEKbXJtw%2FOLwVhahAQL2lRdk2%2B%2BTQSbfBOLKeOtJJq3a4AKRHgvMf9V34nRFxBLV%2BQUm1KGgj01C%2BVmXi20Q5NY13Mk6KYe05CIufcYxzo3J0HL3WEeuHqBTjkfJLS0ZScZMPJP3rvD6Tn%2B2KJ2gbMgZSm2cJ%2FEE52PaVN%2BRAR1cyW3fxseraGLI6O4oAr5T%2FLDp%2BC1CJRT%2BsXbM5F%2BhDIhmlrPTe2OjiOjvQCqtwIfYP4XTpMLe%2FgL0GOqUB0TgHiIcjKHF3dPXPcerpNRRdh%2F65gNH9PM8%2BizhsTi%2F%2BoKFFL9IGzshGTI77yOjlwCHTGIEbGC1WYnNsJHxClF%2FlJg2lNhnuHbiHdXIoEblDKYHqe8MRq%2BNkV9xpghEFxoQWv8iu1S6itl2vEp8ZwTkRTZTsbM2aLF47HL%2Ft7iy8nvBriFjUEVRfL%2BnWtq8t8PhabzU7lONYGQnu0TufXQG3TrWq&X-Amz-Signature=9e786ac50b594ca172ebfe90ce5f991ce8a86d4937560c65f2ac04d77dabf606&X-Amz-SignedHeaders=host&x-id=GetObject)
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
