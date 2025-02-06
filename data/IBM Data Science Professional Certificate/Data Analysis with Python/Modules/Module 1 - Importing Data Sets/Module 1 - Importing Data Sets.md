

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPDVQJCI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQC0HYfeV8HN%2BW1pTa%2F07re8%2BA9iKpqP2kdBjIyIIwL1%2BAIhAL1t9aL%2BAg8Eez4qVloELhdWkB74Y1KfDOeIBxMfLKWqKv8DCFEQABoMNjM3NDIzMTgzODA1Igww5wUxeY1%2Bdltnzcoq3ANuMQK5Z%2B94ejnp%2BsP%2Bnn1QTqW%2FCKiszB2Om%2Fb0m36krk6V0zxJpJvYAxUH1A171HOzNn0RnvD6uzGMGbBBnp%2FtEUfl1TKLQ7zEIKmX4lddDI8ztVc3%2BQN%2BE0jMwIVUQj1sy5ghnDp2HQ%2FZrkbL2pcO1ad%2BT%2Bvf3taDGt3S4kerzt%2FnGFmDEZdmbutFV38OElFMcjXpA0z3FpQPdMGsY6x59z7CBkQ9F08488UPWFblf8VdhbZwrhbih7np0qd2BEvUdnzIwUeM5aK35AKklJg0hqwWFIev5nDO%2BVSdz6Ru9fquqrv6qaQvi5ZsXNPicUMSVUUYRx4unXSwv87S1Y3GlY7yQgQZWoeXcNk4da6okeZtM893%2FKA6ooAQVvhL0DTrIi8h0TQUIh3rtWwEvcQeXjCN00%2BehpbBIwJhfY7SVB55V%2BIODbihx9yKHE3A%2BQ1k9cvCoPW1MOgGfBGQMG1TVmR5TbaFagvJozKzY3C%2F8FSXu2VuIsqgvnSXu2FVm%2FwS62HYggYAUfikipKhSHwjUrMVDWldffiuNgW48vjYyRExvAPCCXWxi2%2BhmQkkq7S8s9uwiu0J9Dv1A04qGwZq0OSAdzqM%2BA2POg4DH62No5%2B8BMESEQcf8X590zDp6o%2B9BjqkAb1t68tPJggYUEamu%2FLcCvaX1fFgI7ks3aFtrW1b%2BVePr7UfJitnNcSWZTgfBiCzdY9%2BoVErR%2BBlW9MyBb%2BG1BiRjd4MXKAtH6GqdgWEd2ljeQRaH7FobbxRSplTYmXqKyl%2B5pCRItU%2Br9Kp7%2FiCLweSqrOctDf8xh7CNtrUQmcbD0iXK9bqmvhNiqp3XSNMKI%2FU9tw27pt4iOMQdj9ESyvso4YJ&X-Amz-Signature=eadb00fcfd1c39d088ee0b5b7d3b2d312acca5f140479bf5046c38338e2995c9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JNRZKW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDURUt4JkRCp1ZBNjJOnzsrH9Po1GXqPnV%2FE6DjioAhVwIhAI6ibg31B1yV129YKeegoATfSi74gAt0cROxVvmyZTSvKv8DCFEQABoMNjM3NDIzMTgzODA1IgyklF2P%2BRDxjffHgLAq3AMiti3%2Bai1M6HwtBjExreBaf0F3u3PtocTeegQ6bV0gJq%2BFFUzJXhiZ6IAiVhE%2FH0ZT20p9ZMmZSLetaCI4btn6hmflhfjwXIRdAyI6BjYzlMnOgcrBAiJ2sDY2bxkffy1iCVRiJwe5lJ6lU3XQ%2BkYPfgz7RzPUe3P%2BFcZVeVJ9MSHn4c5qr6IqjkrW1Uhmw6TQC2lIHTqlIcIpIlymoi82ob8mCaOzB%2F8BR%2FIBtMHE7zsEh3Tlc80LrFM1P3YwjsdpyFMH3KnHZhj%2Ba5xozZYf7ag8EQQqEil5Dy%2Fn4kNbCFCaMdRa%2FMxVo%2BXS4L%2BDCfdeMJqBx5q2UKLahk6FnxJBNj2Mxflbx6H9b5%2FZQEVUbaKBAqk4Bm3wOJSnTWZmoHV3SvsGEcHlQkigNaip6VN6iKRTIE8gE0Rt30J3FMFKqg1hMsSnObJH3Uc9g98PIRsHzQGfJFdDA%2Bixy9OJ6Ml8ARbgMpkOSsEjDYgosF2x3UNB6XUdZDC6LXdDmEdSqMfHCYcM%2B%2FB9epqc4%2F%2B%2BxdPPtr%2BFY8rSwiGkAufZ4jSVVizxcWACNPmySXbW%2FNbP8tP%2BxZYNB0odRHdiwB%2FqTUJW7DEQk%2FMw5XD5SbJ7Gg%2BWYcPENtKJoAgeXioSODD46o%2B9BjqkAefIz6qMYrtI0WubHEPJnzjNvkoGx4KDvzy118Fjb0cayHfHSQnTdKXJrTZoCMcI5fDQx2aGf3nel7rEjwp3Kr5q%2BI651DOfpqC5erQUOAoA0Hr2G436nCsQ06JoL9W6Tp3L%2BtPLl%2FHrMh6nM0FE%2Bi1WMcI0U%2F%2BJpJJnHbt%2FPpmsh4%2F8Aerufe8dGaaiNkX4S7Z3R1t19h3V%2BCLznjYbtmFysK6Z&X-Amz-Signature=34b69fb11c3d9ec1d639c46fc20a2051e043ef22bb64871113a8ee21c0e601e8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6JNRZKW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDURUt4JkRCp1ZBNjJOnzsrH9Po1GXqPnV%2FE6DjioAhVwIhAI6ibg31B1yV129YKeegoATfSi74gAt0cROxVvmyZTSvKv8DCFEQABoMNjM3NDIzMTgzODA1IgyklF2P%2BRDxjffHgLAq3AMiti3%2Bai1M6HwtBjExreBaf0F3u3PtocTeegQ6bV0gJq%2BFFUzJXhiZ6IAiVhE%2FH0ZT20p9ZMmZSLetaCI4btn6hmflhfjwXIRdAyI6BjYzlMnOgcrBAiJ2sDY2bxkffy1iCVRiJwe5lJ6lU3XQ%2BkYPfgz7RzPUe3P%2BFcZVeVJ9MSHn4c5qr6IqjkrW1Uhmw6TQC2lIHTqlIcIpIlymoi82ob8mCaOzB%2F8BR%2FIBtMHE7zsEh3Tlc80LrFM1P3YwjsdpyFMH3KnHZhj%2Ba5xozZYf7ag8EQQqEil5Dy%2Fn4kNbCFCaMdRa%2FMxVo%2BXS4L%2BDCfdeMJqBx5q2UKLahk6FnxJBNj2Mxflbx6H9b5%2FZQEVUbaKBAqk4Bm3wOJSnTWZmoHV3SvsGEcHlQkigNaip6VN6iKRTIE8gE0Rt30J3FMFKqg1hMsSnObJH3Uc9g98PIRsHzQGfJFdDA%2Bixy9OJ6Ml8ARbgMpkOSsEjDYgosF2x3UNB6XUdZDC6LXdDmEdSqMfHCYcM%2B%2FB9epqc4%2F%2B%2BxdPPtr%2BFY8rSwiGkAufZ4jSVVizxcWACNPmySXbW%2FNbP8tP%2BxZYNB0odRHdiwB%2FqTUJW7DEQk%2FMw5XD5SbJ7Gg%2BWYcPENtKJoAgeXioSODD46o%2B9BjqkAefIz6qMYrtI0WubHEPJnzjNvkoGx4KDvzy118Fjb0cayHfHSQnTdKXJrTZoCMcI5fDQx2aGf3nel7rEjwp3Kr5q%2BI651DOfpqC5erQUOAoA0Hr2G436nCsQ06JoL9W6Tp3L%2BtPLl%2FHrMh6nM0FE%2Bi1WMcI0U%2F%2BJpJJnHbt%2FPpmsh4%2F8Aerufe8dGaaiNkX4S7Z3R1t19h3V%2BCLznjYbtmFysK6Z&X-Amz-Signature=0835c3a2156293afd2e0fe5604f67ea845545e23cbabebdecaaba9c44e7e7640&X-Amz-SignedHeaders=host&x-id=GetObject)
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
