

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEN66BHI%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHWj8mPzSJoc%2BqZX5KDirnghGGej4LGfUFko8XExF0mGAiBHHY9JYz%2Bvf%2Fr0oVQcTReomLp4llSCk5h%2F%2B96Xk0qTlSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMyfG9MCcSmQ1hxB7GKtwDFFT7H7wYlS%2Fwbpw87PzqV%2Bc1PKirZKOgpBcN%2BQJDBuQUQoVdOtnkeAIpeXDHKl9nNT0oeH7jaxVgzuYmcX4eol9a7fwcS5Xe4a2VndJdQmYE19hETzRtFDTkc2EnXHTx9%2FxT9xqiTAvvSomvcIUlk2lvQQ2WVNg9gSDTQcUEzZ1FT2NxWwM7X4v4UfiKhXLeeplaLc2yBmlq5WP29on1GNuruL5hQT%2FLtBhgWiqvYMQQJv9dYhH35vZxRjxGZMF7C7X5d%2B1FbYFRJoIhDmNoRk2pjJBalouuVC9REdfAoseZrZT%2FBA2S1DYrcvhqzxbjUlNTCBx6RnyoFb1GB%2BbC9qK%2BRqoxkXd7nJdNWCWod6Itvb%2Bci8oh08Amr0uZyHGgWXSZmbqCiRZjEyAFFdH6gLUtEBdKSFsWrNx7w5vfZHcWqP8mOjkMaOKyvyXztOH6wWlGpsm8CSrg3jt9uMyG2QAs9v3%2FgR539MTLmFE7JgFg3ZS1tlnRyU78vJRNLeEbf2FDPDKD804BC3liHGtIlX3y7H3AtcN%2B3OoAVoEDCz4zClkYqoyDxQENVZVnrYvoIOZ9KngMscb9KAFG5u77DxKHoGk5QyrMT7eLBpM%2Fx3EibdZMG0%2BcJkycE0cw%2FY7YvgY6pgGiuABC8mifURzBfLM9pSo9nAtgOkeqkl8rjf9iZFCknTjmTr9dWqa5iWySfhrJbBAW2IhT%2B%2FoOPCZ5fhAYyODiQ94y%2BaIQLW606SWrVqXCRDGdbFbYf8ugyimiJoYTaoBDIcowMxLN%2F97ID65KQ2mWz8LmPdTYTrpNNN2ehUiSoB1S9yjiU%2FyChteffDDk22%2BroCpIZvoM6gOEHpN5gWQdSJ2zpKaF&X-Amz-Signature=ea80efdac2b4f1946b75ba73d73bbfc8cbdb39c90287d8e032b8d323a267d3f5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Y3YFDH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2FMhVpt4rJKvln%2BCQ4qKE92i%2Foewe2ABsrt8PpSjjBAiEAqe7PnPt3hwJL2S8X9ltC2iQfZPPAaiuzLtSHaKgfQPcq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHO8wlt26BoCrYw8XircA7mCiT3r52B92MNYSDAGWD3QoAccqO4QrLja8leW%2B8lyNYznE8tE3Khugthoe4EMOIcQOyh%2BduS0XOVJtrs4AUabMBBumJ3bBXgTAepzfHCLNL0qhvXnGL3eZR0KAYApY8K44S5TqYv3N4daqYLG2wkEw%2BIJsgwuik1u%2FmOzUxdkqvRiJMEviWxGkOOErZCL2FltY7RsMN9zcw5RV8agIbysj%2B1DLf4qfUzVmw95EHJh857jsS6H%2FrFbfmjvWUU4yFtvS%2BdRnvqOh2IqQnsnr100PYEM3AHA5dYTPWat169IC2rTDSlgV9CA52Zm0nrfjATLDhCMKhW8sIzWHIL%2BhM7E6J10QqIEWVHp6BfeqEDDnfjoMYqkHYeF4vSxVbRea0pWSQAoVqI7lz7E49qusas3MMPq6%2Bmfhbawd1CscHncsI9YPgGkKeH%2Fognf7NCVOwBfwzVahNfU8ktQ96Sw7FDE%2BLoJ6ejrXmw6h%2FuR1RTMqpLB%2F%2FX5VYA99hbcWnm6ow2NjTxiLq9mDO%2Fhq7WbBB2a9RNmZqMuUkmrwhLcud%2F8TB6L7gapkfVKDcgNUFjA5sESJJ6gQhHKiC0cqosUCJUN6jbK0tVDqqP0xUEWG8Me4pOJoe3sCSQ1xCNBMN%2B42L4GOqUBA%2Bw5r9WbLQqEWqXTtPH8qO6a20aVppZ2K3oTmhcIBnuzVQEnnryfy55a91dYNZc%2FXi8IcOPL2JkThgquX%2FGXi7qe219kdeTybztuDhzNbM%2BC0CMS5v6ZLn8N8cC3tzCwuY3RXuqoLut7dD5S5%2BLCyUtt7bDHosBAtxNjjrw0ShmgiTapaMS7JwRO0xAK9YR2shSVT2%2BF%2FW%2BDbfItrD4tG31FUoO6&X-Amz-Signature=f648b5f180fd99687b04a71f0ea58e5a0cf166312b4fbe4083164310a03cc1a7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Y3YFDH%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2FMhVpt4rJKvln%2BCQ4qKE92i%2Foewe2ABsrt8PpSjjBAiEAqe7PnPt3hwJL2S8X9ltC2iQfZPPAaiuzLtSHaKgfQPcq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHO8wlt26BoCrYw8XircA7mCiT3r52B92MNYSDAGWD3QoAccqO4QrLja8leW%2B8lyNYznE8tE3Khugthoe4EMOIcQOyh%2BduS0XOVJtrs4AUabMBBumJ3bBXgTAepzfHCLNL0qhvXnGL3eZR0KAYApY8K44S5TqYv3N4daqYLG2wkEw%2BIJsgwuik1u%2FmOzUxdkqvRiJMEviWxGkOOErZCL2FltY7RsMN9zcw5RV8agIbysj%2B1DLf4qfUzVmw95EHJh857jsS6H%2FrFbfmjvWUU4yFtvS%2BdRnvqOh2IqQnsnr100PYEM3AHA5dYTPWat169IC2rTDSlgV9CA52Zm0nrfjATLDhCMKhW8sIzWHIL%2BhM7E6J10QqIEWVHp6BfeqEDDnfjoMYqkHYeF4vSxVbRea0pWSQAoVqI7lz7E49qusas3MMPq6%2Bmfhbawd1CscHncsI9YPgGkKeH%2Fognf7NCVOwBfwzVahNfU8ktQ96Sw7FDE%2BLoJ6ejrXmw6h%2FuR1RTMqpLB%2F%2FX5VYA99hbcWnm6ow2NjTxiLq9mDO%2Fhq7WbBB2a9RNmZqMuUkmrwhLcud%2F8TB6L7gapkfVKDcgNUFjA5sESJJ6gQhHKiC0cqosUCJUN6jbK0tVDqqP0xUEWG8Me4pOJoe3sCSQ1xCNBMN%2B42L4GOqUBA%2Bw5r9WbLQqEWqXTtPH8qO6a20aVppZ2K3oTmhcIBnuzVQEnnryfy55a91dYNZc%2FXi8IcOPL2JkThgquX%2FGXi7qe219kdeTybztuDhzNbM%2BC0CMS5v6ZLn8N8cC3tzCwuY3RXuqoLut7dD5S5%2BLCyUtt7bDHosBAtxNjjrw0ShmgiTapaMS7JwRO0xAK9YR2shSVT2%2BF%2FW%2BDbfItrD4tG31FUoO6&X-Amz-Signature=8ba5016887e6fa518163c8a7e142bd656503b105e2ae25dbc2d22e5df98c1319&X-Amz-SignedHeaders=host&x-id=GetObject)
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
