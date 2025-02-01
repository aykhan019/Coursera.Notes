

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663DLKTG6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3Kj4DL5Ix7SMIF%2BI0sSuyMIw%2B019NeuPVJF%2BQOjj7oQIhAIfGvGms1WFPXRx7uvfyfV2EfKwOC%2BuZL33eKlxJ3rvdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUBiaDGwdgoFjCgKUq3ANmCLHoZcEp0ZtLwg4nAGYOoZGgYB9Jn3EBZlt4IiQsX0ybSFxctFfN%2BClIgYUfkeQVXCohqlPYkJ%2B2l0owCHHVHxjVEvwpfcHKSEM9v6zuYru6eVWMfv%2BOrNcTrAA0oWvaFMiPr0OnpZuEqmRBglLSuwmKAWcjQ6zVMySSoHDokDOgm7m0jRkIyRpTlffJMScmR76lYHMm0k21dpCgxPy%2BYFC4IChqewqoWbSYHqD9xlFghZgfOiQIqlShESeZKwRm%2F8QVZweWk%2Bqu2xzv2s2faQaqVpya7sqXDpQpvcmB0InNyVkLJRDPfDKmP2DLyJy66v3fWB%2BR2FwilWKtBqtJvk4QOrIbKYB%2BeeM%2B5S2L21Qa7ifgDEGdaQ9E9MfrD2DCw%2BpV7DDjzQS%2BfNWB7waRktLPGEoDINUceYz%2FdSH2EHaCraFrE9zHEnUQuWJXwnlYTaPkEkJj2O3II0JoqYq9yHLSTuFhvvuJVy68Wi38auQzIXc0rVZG83p8m21PZV51kqu36uNlwvJm3VIF6f9rbVuKqKixSoxv2JoVy7fIfmqJPdjgkjCSpOuvicO9E1jIAHtZaLnAYTtL5t2PMcCHhwbsgKcrr7PQqLV515GgTmwbbipBdQQ4RGHW%2FDDSpPe8BjqkAbZ9PBkagsJHLuVcqLkFEx4wMMXtVN5OQdnd7DqOJuMsTXHMqXgbP1XSYomj1OOSDC3hrUcOnYxuJNbxfSdiNTgswhyE7vgaQ1Ed3USi3AUT4I8S8ut7Qm6vfQEjecUhSyYtcIw6RbOHidZ4tRUJP5DN%2FGk8bacNScfMOSLxRB5YYHUMmuMnQdKr49EOVh5pTnEFQxfB%2BBPvEJWzrCbTtreBirTX&X-Amz-Signature=d13d7c77685bb662e8bd7b8fd9b1c1146c3990c7a7c78cccdd0d3138ae9e2af1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675OHBW2H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFoVTc%2FZDdfkOJ7UP%2Fa7DoA3k1dXabOsqxzRUFBpH0iAiEAh1sQln4n1Ovgqx6VcaCnMmF7mYeOvjJqv7eUTD8li8QqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPUXLN1PzNNUgXFlUyrcA75790QyaolJp0I%2FYBpzC4eNmzZel6kO4E%2F4ZYFHFDDrm%2B%2Fj9%2B7P5M2j4oWjpZxBcY6Y0M0kqW4xuvTY8T%2FhNb7Z4jlGV1OeCW2vZtIC%2Bt9loejiHVDIIgkJYToE%2F%2BspU5sutPu7CV92Txij4alxahyPHpi0iATQmahKskCsbgpEuSfd28S1sU7zjVBqL2iTIdhYqNUJtQvM8CQZYxm%2FWKS%2F%2B5cOWZ8IAaMj%2Fo%2FO5a1hG4aTp4XEiqb3CEbyGjVGiDNw8Wr2Ijo2aFlneDD%2B5W1QjTVmfPKMhGxGYqv6nu7Vg5%2Ba%2BCvMON34%2FCVz9C%2FCgvjoogd8wTRodKbYRNoo%2BQBbMddVGx%2BiLm80H4aCkr2Iql%2BVaMo7aAuImH3cVwbMqjMJ1E1dR58xPpClJOqEQRWuNGtcX9VZeuAi4v1%2BLxY82dERKGLNVKUl%2FSb9QNc2Npu8jVj1OLLkzFYu71zrc%2BU7LqqadcpMIXB0VEnp4uFnh9%2FOr0AMzHb2%2F4p0bL64L5bHMa%2FNPZUqqPwmQ3x5aAZSxYfoRgiO%2BNC1e3jdAwYpV3WFHE%2B8Mo1B8qIlEGof6gcwmzCqLqDEyU8KA5TXDR7uc%2BqN%2F1A7iAOuPnV9NW38PBV%2FKfI0ns3exZZnMN2k97wGOqUB6llqQrKV1ae%2FhDDC7l0svW3RU1362NTY0rRz47Oi%2FCjttFAC7jeNXa9j3OGQd4ntrst%2Fn%2BdBi54AKyhYrSXLyzGWMQmXaT9jRPb4KG1mMTaGYVZJ63Fz0eTyagD0YbUlQ0zxUgnYzQv2sH52fl3QWFBisNF0GnMhhfBIHqtZQZb9YUPH4t61IQvgOQa1hGhEtFdgQAyqgICxCPmaOqLHrzBnKk9D&X-Amz-Signature=5954df14b990b2ed4bf572aef80348561e8ec8fc64b31f72c9eaeb1073f3ec48&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675OHBW2H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFoVTc%2FZDdfkOJ7UP%2Fa7DoA3k1dXabOsqxzRUFBpH0iAiEAh1sQln4n1Ovgqx6VcaCnMmF7mYeOvjJqv7eUTD8li8QqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPUXLN1PzNNUgXFlUyrcA75790QyaolJp0I%2FYBpzC4eNmzZel6kO4E%2F4ZYFHFDDrm%2B%2Fj9%2B7P5M2j4oWjpZxBcY6Y0M0kqW4xuvTY8T%2FhNb7Z4jlGV1OeCW2vZtIC%2Bt9loejiHVDIIgkJYToE%2F%2BspU5sutPu7CV92Txij4alxahyPHpi0iATQmahKskCsbgpEuSfd28S1sU7zjVBqL2iTIdhYqNUJtQvM8CQZYxm%2FWKS%2F%2B5cOWZ8IAaMj%2Fo%2FO5a1hG4aTp4XEiqb3CEbyGjVGiDNw8Wr2Ijo2aFlneDD%2B5W1QjTVmfPKMhGxGYqv6nu7Vg5%2Ba%2BCvMON34%2FCVz9C%2FCgvjoogd8wTRodKbYRNoo%2BQBbMddVGx%2BiLm80H4aCkr2Iql%2BVaMo7aAuImH3cVwbMqjMJ1E1dR58xPpClJOqEQRWuNGtcX9VZeuAi4v1%2BLxY82dERKGLNVKUl%2FSb9QNc2Npu8jVj1OLLkzFYu71zrc%2BU7LqqadcpMIXB0VEnp4uFnh9%2FOr0AMzHb2%2F4p0bL64L5bHMa%2FNPZUqqPwmQ3x5aAZSxYfoRgiO%2BNC1e3jdAwYpV3WFHE%2B8Mo1B8qIlEGof6gcwmzCqLqDEyU8KA5TXDR7uc%2BqN%2F1A7iAOuPnV9NW38PBV%2FKfI0ns3exZZnMN2k97wGOqUB6llqQrKV1ae%2FhDDC7l0svW3RU1362NTY0rRz47Oi%2FCjttFAC7jeNXa9j3OGQd4ntrst%2Fn%2BdBi54AKyhYrSXLyzGWMQmXaT9jRPb4KG1mMTaGYVZJ63Fz0eTyagD0YbUlQ0zxUgnYzQv2sH52fl3QWFBisNF0GnMhhfBIHqtZQZb9YUPH4t61IQvgOQa1hGhEtFdgQAyqgICxCPmaOqLHrzBnKk9D&X-Amz-Signature=9ff8badf03c96113a75dac7b85edc8c49aa7b5ce7d0e7e4e0d0de0bd57c91c08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
