

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS3IQMIA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIHbesXco15PK3UH7iVHVAsJlQM5OPGbxvwCZw%2FBteEOKAiB%2BJvCccejoQ86gAhbNCqE%2F3fnUGDQqWGH0iWWHREVnYSr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMWNZSiF1jpYKNPZDMKtwDzBaZ0W0%2BzhdUkXq1Npdyr4%2FezdLlhsdJLhOiA3jTsrLb8LHigCK68cMB0DSQ32hJljFeycUyhemSW2GyqZdOqd8TGZV77JzVTAOGb0zYxDre29P01qtxn1%2BP3oP3zTzqlHiNvt4qF2m6rTltflMp7bJ%2FGPyoC1v3M1%2FoZwyuMR9fVZQipTBTx4UdD4RYFPPvucvQlsqRSQ%2BNMp%2BTuygwsIfJ%2BPivAmjPwXK35uCVP8q0PSuFQ7QTbQZOnyk7YiULkYT08ink0apjl5Mhmh24id%2BXGunSp0kdj14k2vMCXIFaIrKq1o0gv2Cid7R6VdzxmeMNpmiBGMXK3hzNS448Ss9lqcXgm8F%2FrJ9tycQqcVakwZqnrd80iiTC7z9spzGMJP%2F312HrpfuVvqOaBFb8UKduYCnbMOMIw33kP23EEPJiPPiabd4K15N%2BqedGcqy0nQ5amD1rYCPn1CMMkikVgYdZ%2Bng%2B21BRGyS9a7te%2Bod2PdD6SFH44p2SQSJrgTZTcntglyaDoN6B8yraCLBjYQqO9CuHso5xD%2B4CU2PKBoTOsAOtZDvc8S5zXyinJwyZ7aS1eXWiJr0dhM%2F8rqH1OXDjH1u29x%2FkxlFMoKn5DF9REPpe2zLcQManXqIw84qNvQY6pgGVGBZcHGKVo7YMS1oXYhoCqYBcXiVtUjvaYMSZQg1v4GcOFIc91l6uyfClvNVsi71VZivmClDKXZ%2FOLBnNHKoIKdd3%2F3PJPDk%2FnaTwodqezJf1x7K0CEWUxMbiyEx2rsrsD61Q9nSkNIuG%2Feigm6tofZAhxuwAvkjqpx7grY8OcvgKobNtHwX3K80ULQb8P1l0o2Gkgv5YOcw%2FAnrTc8th%2BTvNoz9F&X-Amz-Signature=efc657c4611c7090c696b1d45ce351f2596b1e2a4f61c0512a1305b3a9d7a04b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO2AVIWZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFUXePHfFAfaIyvCQk7fDXlJduhTLJkp%2FLiiZvTIDvNtAiEAq8cKRcCvduZVW64devRceG%2BaNdDBr5igknKDUeq1ER8q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKe01%2Ba%2F8rzXpNOhGSrcA4tmJnakVJhLakzhgp75kVoB%2Fpl2BxwDlGcEcJDGxusdvfg85cIXCMXGntqtEm9v7A5fqH%2BC1mxYn20k1CSxmwKqulsLaqqM%2B6if1gl6nMdTPqsroJkmDBdM5hIRU23VOzoPpVQeADmV1x6%2FViC4w5KMfjMtA5h7H%2FSF7Alz5q13oe14TB1Xumdjh9o3gOxw7c478A%2FsbGWX80fz1TBPwaLyC%2BGYbC7ABg3uUyaObyeHvoPH0ndXPFMYyqRvMlxYENVehv1%2BYffL7RfOaC9xHZgNqbKNAnsUUIDncqGbZMOgAkGzWgtNOsi%2FTjNcCSXhdasJREruAu3xp%2BkQaL1jv2MKwyFJNfehJubppOCSxVSOBtv1Z5CJ7%2Bl4LT%2FFQcfMS5Ky13jPCLhQRGIQI0kaEi4PNU%2B0PhjUf4v%2FSMj5zRsK7CaRK0dxNjSQBOG2zXuS%2Fg7cHQB554c6IjBnPu3CZBgREpVuq82AYfRjJA7drD4E0UriW6GWXyTYS6TPHAXBgUB8xfmPah%2FllfSP%2FdEYRoLE9dqhEVlY8SXLmCkCTXGdZT3ynl2VECBoJ19yOA7run4Qr1ZktRB9O9ii71bHiBHM44KZ8n%2FGQmywRk6fOI1wBA4a7XffXOfcjL01MNKKjb0GOqUBYC5MraZqPeelIy%2FH%2BQjem3N%2BpceHfuxPPLbEBzo2OlAQ75%2FTl36Q0OfxKPoPQhvw2jDvhpPL75g21QD%2B9fOj1B%2Ben9zvMseDZzo3lqUmSdzPpuhkpzSbcx8p%2F3pqadyzdI%2BJAlHE7L%2FL0q8TfTubrwo9QPph4jtw0L1Iu1YfXKYg%2BOkoHOnimkEOAxqtT5mH2ob1GU%2Bg1IROqmBI3cXZR%2Bmpr0rF&X-Amz-Signature=3d53a93fcda2d0648e04ff68f15bbdb34689aa5bfa37e6f714d75e23bcc9bce5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO2AVIWZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFUXePHfFAfaIyvCQk7fDXlJduhTLJkp%2FLiiZvTIDvNtAiEAq8cKRcCvduZVW64devRceG%2BaNdDBr5igknKDUeq1ER8q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKe01%2Ba%2F8rzXpNOhGSrcA4tmJnakVJhLakzhgp75kVoB%2Fpl2BxwDlGcEcJDGxusdvfg85cIXCMXGntqtEm9v7A5fqH%2BC1mxYn20k1CSxmwKqulsLaqqM%2B6if1gl6nMdTPqsroJkmDBdM5hIRU23VOzoPpVQeADmV1x6%2FViC4w5KMfjMtA5h7H%2FSF7Alz5q13oe14TB1Xumdjh9o3gOxw7c478A%2FsbGWX80fz1TBPwaLyC%2BGYbC7ABg3uUyaObyeHvoPH0ndXPFMYyqRvMlxYENVehv1%2BYffL7RfOaC9xHZgNqbKNAnsUUIDncqGbZMOgAkGzWgtNOsi%2FTjNcCSXhdasJREruAu3xp%2BkQaL1jv2MKwyFJNfehJubppOCSxVSOBtv1Z5CJ7%2Bl4LT%2FFQcfMS5Ky13jPCLhQRGIQI0kaEi4PNU%2B0PhjUf4v%2FSMj5zRsK7CaRK0dxNjSQBOG2zXuS%2Fg7cHQB554c6IjBnPu3CZBgREpVuq82AYfRjJA7drD4E0UriW6GWXyTYS6TPHAXBgUB8xfmPah%2FllfSP%2FdEYRoLE9dqhEVlY8SXLmCkCTXGdZT3ynl2VECBoJ19yOA7run4Qr1ZktRB9O9ii71bHiBHM44KZ8n%2FGQmywRk6fOI1wBA4a7XffXOfcjL01MNKKjb0GOqUBYC5MraZqPeelIy%2FH%2BQjem3N%2BpceHfuxPPLbEBzo2OlAQ75%2FTl36Q0OfxKPoPQhvw2jDvhpPL75g21QD%2B9fOj1B%2Ben9zvMseDZzo3lqUmSdzPpuhkpzSbcx8p%2F3pqadyzdI%2BJAlHE7L%2FL0q8TfTubrwo9QPph4jtw0L1Iu1YfXKYg%2BOkoHOnimkEOAxqtT5mH2ob1GU%2Bg1IROqmBI3cXZR%2Bmpr0rF&X-Amz-Signature=1e8cc48f5d40a51cd619e55747442467f4b34b3cf4d61fec8d99aa99c229ca5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
