

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DCV6PFB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBPhoeKROuyfzWUxXN3rYeqSflDwQttHrF2Y%2FgbxPn7XAiEArJwiR0hMeFSoIy0s6gBeqq6PGnO45qJePos8d0%2Bwi2kq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDINxWfxKvpUga962syrcA9KhWvEZQDer322n4LgTgltrzGsQ9c%2Bo4MOwjrz%2F9TejlIqc3SUlWeeaVbuV2Ewro36GmseSgOKwmKQ%2BoVn2Q8mReZZCGWrAeekLzu83ANnsIgPaV61iS8qCzomQAz6FDKxsE1XRikiL3n9riMo%2FW44178l0kWqKmjaDVub%2Fk820irkvC3sd5kEslHtZvO%2FaYGVLR35dEWNoTtiRyRbwQxqTzXas%2BOx8yyPvGayY5fz5PMMnvCPk7elLz1ma%2F8NYqY2bYVZPgLKFax6dXojSbo43DIFJ93u7JpJ4Ez2LqGWxydWr7CkqL5DYasQ272WqGuWHibpCmdrGRS2gV6qObWx196yj02yUfSOQ0A5GKSuKwoBCqjxVrh6qIz2HU4svgghRRuIHGGMY0IncJCjb42HBI%2Ffm1StkzMWrU6xfDkI2ono%2BXwGAZH%2B1AqMHbb45bVdNaq%2F7Y5MXa0h5%2FxRSqGfEKkwpt9wbl2%2FC4C%2F6MqwcRwSMbvAV%2Fx7W4SRCo%2FOCNdtx9Q%2Blf1tBngvXwGEm05DENPSXLpH2%2BqOW8IG0oH3Q0mNMf4BLj16JxZtE1iic5e1ohc63LC3xq6on7bxRuNR9C00c7yGc%2BKlUYCYEyZqbf2T57NNvTSLavx82MIH6i70GOqUBJmR0PZRQz6NE0jVK3xJe47q294w%2BvAs%2FcIYUEvQRekKj9Cv68xIQvxwKUV%2FuQIL57woowxC3CtsMJumOKyIJjbr6Nt1goepwkQYX%2FZobHkEjkUAkBnt8d2CZipI0E7vJxpUrMMZhl2eangfVG1FHv3XbFkZ2PM0Cadw0Afhm5RroqglC5KP983Lp7scYAS51ex8n3nrZxHl6bdcFARENaCxEO6Bc&X-Amz-Signature=001da4e80bf7515bb53b203646519e3cac1ebbe4efdb389c4f1313ea0bd809ab&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRXHPYCW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBHPVFDLSIfRfgoIqr0S4YXVSQMfgTBLvm6%2BJGP87i89AiEA%2FGF%2FfhnkwflXW7fRNvWsoSqWUu%2BiJy1v80hBcQapV%2FIq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDPP7YydTYKWuoVxv5yrcAybrd%2BIAbOQ5l4%2B1ytMlQ%2BvNmJBP7N2vGqB3DBb4xFlF5vy80C9HY6uDAmQvtwcPbXC5FtXCTDYATq6rJ3UgPmahvdudw%2FYgOZIMsCG3dvJecg%2BnORrCXzqGScMWnmacbXsBkwsxSoyHQ4J7FkB2OMiiDdTj2514fsS%2BeHqFbV8I5eYaLZVnxhj%2BibX%2BMQzRLrLexVgp7GnOkVs5earQKi6oX0CRWWQnd%2BU389OxqUVgeUMtyi8VgUpbL1ehvVPf6qeYVdv3e0QGtpdz7md%2BMQlsF%2BsvZN5Cf%2FRQRjN5svrgKfU7VwqJ%2B0FJQ1kFkxu0S0VXxazw6Jla0MOrEzFK1gIqArVbKZsf%2BTBPDgUvNBbiVZKdeq5XEUGqv%2B%2BvwZGBearCG57fy7lQO5v5MeI1OokClAxpPbHa%2B9B9lqDOEFi8Zx%2FJv%2FYyx3%2FZkJsTNaMcsgAIXicqJoMiddOJI1bAoJpDHjy0xvIDHv8uYeOdKLgR4RxtENTSCfzAaRWzr61vazEne6dCQ1d8MlpqYROtW2l%2B9xmq7uMNyyhWKm06zY0xtg9hhbR6kd9OcWtx2YZON%2FwvPMHTuYWlyDIYo9tU3yKjtY5V91UiM8AD1nhtNARZ4b9GtuQswYxMu0WwMKH5i70GOqUB%2FqqKEhOrXBmveM%2B0Jnvu6qUT95H8l8gLdd8S7EfV2kxJFVQNSKav8onD7%2BPA0uYDvAyms%2F%2Fm%2FAF1ZkZdFaHbpqZmttWAd3eRry4mE78j1a7jdsdm4Z2MoWo%2Brw0QTrprsOthnt7SsjGi5EzEhwxBAUvmVP82V%2B2JM5wQyJzPIazrE25BPhorI2XfY7mTOLtjEDLk4YJgbc7DcR5s61cL5jYZUu%2Bo&X-Amz-Signature=5f487a320d60ee6d4caac2b62ea5968efe3fcff4984c6fdc68802719e36cedd1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRXHPYCW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBHPVFDLSIfRfgoIqr0S4YXVSQMfgTBLvm6%2BJGP87i89AiEA%2FGF%2FfhnkwflXW7fRNvWsoSqWUu%2BiJy1v80hBcQapV%2FIq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDPP7YydTYKWuoVxv5yrcAybrd%2BIAbOQ5l4%2B1ytMlQ%2BvNmJBP7N2vGqB3DBb4xFlF5vy80C9HY6uDAmQvtwcPbXC5FtXCTDYATq6rJ3UgPmahvdudw%2FYgOZIMsCG3dvJecg%2BnORrCXzqGScMWnmacbXsBkwsxSoyHQ4J7FkB2OMiiDdTj2514fsS%2BeHqFbV8I5eYaLZVnxhj%2BibX%2BMQzRLrLexVgp7GnOkVs5earQKi6oX0CRWWQnd%2BU389OxqUVgeUMtyi8VgUpbL1ehvVPf6qeYVdv3e0QGtpdz7md%2BMQlsF%2BsvZN5Cf%2FRQRjN5svrgKfU7VwqJ%2B0FJQ1kFkxu0S0VXxazw6Jla0MOrEzFK1gIqArVbKZsf%2BTBPDgUvNBbiVZKdeq5XEUGqv%2B%2BvwZGBearCG57fy7lQO5v5MeI1OokClAxpPbHa%2B9B9lqDOEFi8Zx%2FJv%2FYyx3%2FZkJsTNaMcsgAIXicqJoMiddOJI1bAoJpDHjy0xvIDHv8uYeOdKLgR4RxtENTSCfzAaRWzr61vazEne6dCQ1d8MlpqYROtW2l%2B9xmq7uMNyyhWKm06zY0xtg9hhbR6kd9OcWtx2YZON%2FwvPMHTuYWlyDIYo9tU3yKjtY5V91UiM8AD1nhtNARZ4b9GtuQswYxMu0WwMKH5i70GOqUB%2FqqKEhOrXBmveM%2B0Jnvu6qUT95H8l8gLdd8S7EfV2kxJFVQNSKav8onD7%2BPA0uYDvAyms%2F%2Fm%2FAF1ZkZdFaHbpqZmttWAd3eRry4mE78j1a7jdsdm4Z2MoWo%2Brw0QTrprsOthnt7SsjGi5EzEhwxBAUvmVP82V%2B2JM5wQyJzPIazrE25BPhorI2XfY7mTOLtjEDLk4YJgbc7DcR5s61cL5jYZUu%2Bo&X-Amz-Signature=9ba140d043aabbec278e661688732e1d65825fb21ed78a802ba3a133727cb0ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
