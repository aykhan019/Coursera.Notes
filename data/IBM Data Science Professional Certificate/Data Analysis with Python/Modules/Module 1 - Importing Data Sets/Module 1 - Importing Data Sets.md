

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RSDRRR5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyWMG3G5wkHpg%2B45CKfUUqjYP%2F9A2lyulr2mtG3awymgIgcf34t5vg56Fj81LEZK1glwd1huEqJgoHgdDRlFPRZtIqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIXfB8TdeWCVX5uFircAx35iR57TIyPTNW49iZjzEofEy%2BKujWrqk3h%2B%2B%2B0cz0JHUE04aokT2wP78PTg2bFmna7X27CkJasQdwL4WyAoxER91%2BtSayEQQDfFgdu2%2F0oU%2FwH48CoKMkzja5aaBJh%2FIrJ7u6V3T5IISi6kI3BfC2FEykKiMcSvF6IzMPM0UTAalSD%2B8mi%2FWqPqQVd1Vy65cq90%2B0%2Fsp3HdtgPzmXDZYZ5dfnJmwxzE0PCv4CPkIOrXRz833ePUJKAZSsHxOVDV32Jgvj61LVow59JJUl7IkbxlqnEbjVYLfDl3qQAQqCIQCSd0%2Bjzebi8xL%2FVx3Ztmy%2FZYYxpzMzlR7s7G5GOd767gDHaoat6FPlx6rq5zVG7bUWwW8oM0ZKs57lRUDl6DeZUywkZdOAvIDZdu7kvweA3mhqb%2B%2B7P%2BBxyKCqTVbISTXVH6PaU6yAe%2FpfyNdIXU4xryHqQPWpIlLUHw%2FrsZaHJIp1fnN%2Fj6djuOKYJgBIAp8l2DA1%2B6%2FJAmWHKj%2Be0qj%2B4LjEJZDfg2E2Deqwu7i1D3YOlj3qweD7awUgFSUrtwOtQyWR%2FfCRywZzjhdXIeNLWc%2Fve1gK3jFbvkGgzGbDrfezMnHpmciamPaTjbaIPcfVZd24hbTPwKfwbMO%2BT9bwGOqUB1AvJcB7%2B2LFm3%2FeSeuG4gePZz3ey0YnhdfKaLjM2UEgFdc118yRZK1Mn8sQ0LdRCMjiipCP33yqGouOQfcHNBbhzXxJTFbkEl6R168%2FxkebbmZwBpEQFKaWplTf8jWuBlVmQ6K6MuPyOZZt3ZYEKtt1xjQ4IvvQFmJB1Drrj5gqlMjHLrFS0lZmcqPzg3eqXl255BLlTv9lblOKd0hxhWRpx%2Bw%2Bv&X-Amz-Signature=3bab69f8858ed1d3be8b4e12c906f7d8ad6ae4d18399d9ae18885543b28e4309&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M2WIZVI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhWYN64XNP9tvLnyiP7Lrwq9D3JQNh5mVsYnA%2Bhl%2FhHAiEAspZblRW3Jhnf8W51XbSNFaFKKS0l7Ov%2FV%2F5tueX2O1wqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEKqeMDKhr8vlaYgvyrcAwZCZXEYlz%2BTOqKgxNnBPO6oRQ74b%2Fd6i6XYjIeeu6W61MVShSg2Ee2LC8UgoZiwNrkTi81yPBsUuqLCJNpMKCq73dN48R3J0A%2BtQMgXakcR9TyRIvFFUqIiNVjJ4Bej81ddOlgk732OLfOJyPSi0rW%2FrUO6S5ktZ1nrhcVfq25ALyE3XJG1LUyMdCkZRzINQDJOyGFGErAXDYPcRTN4jtd09YFkAM96P%2F2w04a72J5DJ0hVUx0vzselZaWcB7UKiTy9D71wtSaaqedre1Y0DfJkE9r4%2Fo1p%2FOsMKjlrWFap325fZafZvnkHrRxxjzME%2BLfeB1HQ6louF%2Fk6%2FE40aQVSHOS9mJrV6tZHql4he%2Fod11kPfWQmnpOkI03LxGM3hYGBFwL%2F6LwznIZzJbqtRUW4gAuEz%2BZ9W5cJyD7ZdIl9%2B0VffDMT80WXMdUf505H14OH8PgF5giL6%2Fy3aitvUmWXrsYjk1e1ESWroJUdewMVxDwuFtBUyNaC9Qd7bYmfC6R3GqFScVxu9RUC8P8hk5BbUC9gNCYUTHhbLXk39iB8oHFajw7hA9Jn8x00JmI2kalLudmdMSZmv6NhE9yMKEGEEqK4aq8WAoY%2B%2FMgIGlFARzmsLzHjV64JVrzjMJmU9bwGOqUBoaGnemRipsqGqtts6%2FTH9eU3rpB6s7w1rXkIwxxGbO%2FNFkG20YtIii%2Fs5nKfegWcNyzCN34EVzipG%2BnXGT9pLxVF1QsaQXIiOLZssko66TmVDy3okDAAhHhOqqCCdsOlQeAMVGke8UH0GkAmkC6cT21KPv7YfTMzbDFa43q9G8h9Llszb739vVDqqtULW5JT9%2F6h7s7ucmNvqh9AxAcQNK%2B2OT75&X-Amz-Signature=6d176ccefdafd5542941c5761e324cdbca0c1882ba50179e6d80711c3f9ff08a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M2WIZVI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhWYN64XNP9tvLnyiP7Lrwq9D3JQNh5mVsYnA%2Bhl%2FhHAiEAspZblRW3Jhnf8W51XbSNFaFKKS0l7Ov%2FV%2F5tueX2O1wqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEKqeMDKhr8vlaYgvyrcAwZCZXEYlz%2BTOqKgxNnBPO6oRQ74b%2Fd6i6XYjIeeu6W61MVShSg2Ee2LC8UgoZiwNrkTi81yPBsUuqLCJNpMKCq73dN48R3J0A%2BtQMgXakcR9TyRIvFFUqIiNVjJ4Bej81ddOlgk732OLfOJyPSi0rW%2FrUO6S5ktZ1nrhcVfq25ALyE3XJG1LUyMdCkZRzINQDJOyGFGErAXDYPcRTN4jtd09YFkAM96P%2F2w04a72J5DJ0hVUx0vzselZaWcB7UKiTy9D71wtSaaqedre1Y0DfJkE9r4%2Fo1p%2FOsMKjlrWFap325fZafZvnkHrRxxjzME%2BLfeB1HQ6louF%2Fk6%2FE40aQVSHOS9mJrV6tZHql4he%2Fod11kPfWQmnpOkI03LxGM3hYGBFwL%2F6LwznIZzJbqtRUW4gAuEz%2BZ9W5cJyD7ZdIl9%2B0VffDMT80WXMdUf505H14OH8PgF5giL6%2Fy3aitvUmWXrsYjk1e1ESWroJUdewMVxDwuFtBUyNaC9Qd7bYmfC6R3GqFScVxu9RUC8P8hk5BbUC9gNCYUTHhbLXk39iB8oHFajw7hA9Jn8x00JmI2kalLudmdMSZmv6NhE9yMKEGEEqK4aq8WAoY%2B%2FMgIGlFARzmsLzHjV64JVrzjMJmU9bwGOqUBoaGnemRipsqGqtts6%2FTH9eU3rpB6s7w1rXkIwxxGbO%2FNFkG20YtIii%2Fs5nKfegWcNyzCN34EVzipG%2BnXGT9pLxVF1QsaQXIiOLZssko66TmVDy3okDAAhHhOqqCCdsOlQeAMVGke8UH0GkAmkC6cT21KPv7YfTMzbDFa43q9G8h9Llszb739vVDqqtULW5JT9%2F6h7s7ucmNvqh9AxAcQNK%2B2OT75&X-Amz-Signature=a559804994d484d005ef2571cd81a9ecac7bcba4911e349121e8ced93c560576&X-Amz-SignedHeaders=host&x-id=GetObject)
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
