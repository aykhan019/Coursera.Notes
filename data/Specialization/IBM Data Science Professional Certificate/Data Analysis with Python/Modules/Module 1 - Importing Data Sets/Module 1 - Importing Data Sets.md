

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPPSB6L7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCifqNtrqAXI0A2OdrYc%2FXw3WAvsP5zNW8pU8a3lqWkbgIhAOgg0SF8B%2B3QsR2O87rq7HKHSqQGkmkn1jasbii2qEV%2BKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPBMdfsOcIwo8N0mcq3APdKLVHcDBcPDPNKDKzXGnIA5s8cf7hz6v42HteM0o8E3sEO4MLPQu8N0IQpELcqg51pEr%2F17BB4titiD9Ac7Y0I4yCRQigzUjmEpfMcXsmI9r45ECCPwrRUiNK%2B7FQSbz2pm2BO2TMROP9e5i1yDq3dU5jSX2H%2FeAHVbjgVtu%2B4RJJSx7N6a3aqsZY1Ai3QGW8egq%2FuIszRdWgCkP1FJBOH%2FIl8E0UqCobhukBZIYHMCPUTKhAadW3WZC1mOsPSh%2FV5E3PE91A6x2QTGpt0G%2BarVMjvtO4avq6mrnHhTSml9d%2FKBXJzvipxzsr2OEomvksztnlUA3qgaQGjftV2Wqp3xx%2FFMd3iARf%2FC2QvdiS1dCtEKdSNWc2LO3AnxPksneq721jBAIWOXnkiUVS%2BOcGrLMeuOT3iKgtG9LZtWhAB2v6angsb%2FLXHFx3pyBT0pWomwNSU23lsne4Ldg6nehLYVrx3RyWzUpmxF7KGvNQoVhiPHsK7qVa%2BxogSkfUOE57dm1HiZ17evM7iAcKitMy9rK8ZDrC9N1Xl1jkAwEUooFrA3TS5G%2F476K6%2BIhAiobTNLkUJN6h1pC%2BhNxPLUBNHGrpUf3t0BVrMlYs22%2B%2FjI6T1JWnLOTaQsYJDzD1%2FfG8BjqkASEG82OMoFfUODMVWKJr0QxOxiMDq2SdsjIdQOHy%2BdMQysWEzl9TFI3JIxPLkxjpaOU6gcZaNZaToaavbMh4h9OJeoX7fzWfyuhJHtwbIs28zSm8noZgaBYuzGvLHLhkZkoQ%2FH7iq2SNAU%2B%2FjHwc93upPNTWp9%2Bzfo03brhRci0YUMyv38Qb1A7Bxxm474YZ%2Fun6CSvBmZkbd2NGlcti%2FNgJBY3L&X-Amz-Signature=1902311c67669da0f216feaf47cbd445edd94459938aa62c2318fcf43ecc42c7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLIBMHAB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDC1haPn3KsLveJJkhI8v%2FNdLcqGK%2Bhym3FVw6ansb4TAiEA377dR%2F8XyoYEynqRMmcrp5cUa2iniubBRKeeDv5B3SQqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGOuv0eOreqFhauDCrcA85FVPbxDEHDgudEgNp0cvBaCJ2xLqOcQFwcTRVV8C7k4Ox2tC9mf%2BpHecTuFZXhVpjC1z0KPIle1mKcwKrC34eIQIipvSGIRMZSavXdU6%2F%2FkKN8XzcjvICT1Kv9FSyFvgfwRT6FrB%2FvmL%2FGQSqbNgRCqUDjB%2FMBZ1re2ZpcGOx71fCGEOtLAgKG7UV6XiMKOvPOxAie6ekviHlkXjL8Got1P80JDgHYwlLkPv67RcfPA1D8kb9gHhkpy1TK5zQMEiTlkNPPnRNuub%2BQsSw1Ni6VrTXEgiOmFyQWsYFahjzFIFra%2Bfe3P9ulrGQFN7AucKYxZ98z8oHUsbPAz5q8HBTm7S89w5AQFBCILWM%2BeR1cP1CpWIxTyg%2BjulkXrA4pNS9cdt2OmFWtjk6xVGW%2FMHY7AoNq%2BPwASYwIG9BR0dB2yuZdlyCHDr5iDR8WYEKHz%2BA0zZMedIcfqdkoM3iq57X1fnhqdKZYXrcabyiZzRuAucqFQ6930mUEEiPcbk8i%2Bi8vigCqLqQvEzMQil5TbRrx3HVWRF%2Bu4b1KirJPzdmaLY9gIVoKDhenkek6ExJ072RP9StLEBptWU0VnxS6eLyAnc8LlAcEu9mjOpFEem%2B6jaZHNDt9yo%2Bv%2BtgWMMr%2B8bwGOqUB6OymB1ltfLeW88mhoPnyVDwJpG0XrQacpAnFIxG9jZMsSjlGulAkmdptXLru%2Bo9BSZkOUzL17Q3XoslRKTny8bjqVsSDYBkNF%2BPpJE9cSHmIOVXN2Uk%2Fm2UHsK8XGLWhwRIitidkmoETCZbyOMk7FxdSL3xWUFNhwybhmT4zbdABw3Agf49J0w42r6%2Ff0S8y4WOhpTiUOfVXSqlFlIrbCsfE%2BWcX&X-Amz-Signature=a85c97d83d27622f22279a083acde2d778f60bea29f2698c806d3151f389915a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLIBMHAB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDC1haPn3KsLveJJkhI8v%2FNdLcqGK%2Bhym3FVw6ansb4TAiEA377dR%2F8XyoYEynqRMmcrp5cUa2iniubBRKeeDv5B3SQqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGOuv0eOreqFhauDCrcA85FVPbxDEHDgudEgNp0cvBaCJ2xLqOcQFwcTRVV8C7k4Ox2tC9mf%2BpHecTuFZXhVpjC1z0KPIle1mKcwKrC34eIQIipvSGIRMZSavXdU6%2F%2FkKN8XzcjvICT1Kv9FSyFvgfwRT6FrB%2FvmL%2FGQSqbNgRCqUDjB%2FMBZ1re2ZpcGOx71fCGEOtLAgKG7UV6XiMKOvPOxAie6ekviHlkXjL8Got1P80JDgHYwlLkPv67RcfPA1D8kb9gHhkpy1TK5zQMEiTlkNPPnRNuub%2BQsSw1Ni6VrTXEgiOmFyQWsYFahjzFIFra%2Bfe3P9ulrGQFN7AucKYxZ98z8oHUsbPAz5q8HBTm7S89w5AQFBCILWM%2BeR1cP1CpWIxTyg%2BjulkXrA4pNS9cdt2OmFWtjk6xVGW%2FMHY7AoNq%2BPwASYwIG9BR0dB2yuZdlyCHDr5iDR8WYEKHz%2BA0zZMedIcfqdkoM3iq57X1fnhqdKZYXrcabyiZzRuAucqFQ6930mUEEiPcbk8i%2Bi8vigCqLqQvEzMQil5TbRrx3HVWRF%2Bu4b1KirJPzdmaLY9gIVoKDhenkek6ExJ072RP9StLEBptWU0VnxS6eLyAnc8LlAcEu9mjOpFEem%2B6jaZHNDt9yo%2Bv%2BtgWMMr%2B8bwGOqUB6OymB1ltfLeW88mhoPnyVDwJpG0XrQacpAnFIxG9jZMsSjlGulAkmdptXLru%2Bo9BSZkOUzL17Q3XoslRKTny8bjqVsSDYBkNF%2BPpJE9cSHmIOVXN2Uk%2Fm2UHsK8XGLWhwRIitidkmoETCZbyOMk7FxdSL3xWUFNhwybhmT4zbdABw3Agf49J0w42r6%2Ff0S8y4WOhpTiUOfVXSqlFlIrbCsfE%2BWcX&X-Amz-Signature=436fa79ac996693390e78b8ffe60292e9bf2bf8526bcd2bf35bfc2b866189baa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
