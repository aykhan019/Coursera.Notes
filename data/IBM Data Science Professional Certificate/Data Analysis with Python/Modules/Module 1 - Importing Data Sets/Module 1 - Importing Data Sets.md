

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7ETQR7T%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIFnH3v2qnmUEDn7kIuEbG2eT2z7G81asJsYc3YtkEhiqAiEA4e4ZtbB48Rtp3%2BBJgGhvXAxLNK7511zGlwGttfdB4VoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGG6gd7vv%2FWD5oASmSrcA0JWYy13EMQt5CPmNpdcq5aGvbOctNeUVRP6j%2BswmueWjATs9kfczirs8SoIy%2F1a6V4NZjgl6LVf7C9eweLyEHWrQSDJaHerseK9ut9RX%2Fcu%2BrEpKhn2uIuYPcJFTnwaArLzB1K7pic2FyLpWxmYwYiZp9o7BteVM8DVdodWkubondqLiKwHLlr3lV0cfA6C6VC8yXwc7hplSHr3EWvLCcDXE2lL6NHj8gijkngOnxPQkJq062hMxjfYYAVkIz1C2ugOZLjtsYrL0KhnjUXtzFrLf%2F8GWovkSz8t8G7Njs1SeoZfKFiC3HE0TPnMqnB7sq14iUPLrzGDSvWMzyc3fTD0seu5NYXts7DQA8TUWfkpFQ2FVLBkXI5kDU0U65JeyloIP7QW%2F9hiUPXrof51uDrKctATPpM6JdIvvOVR6saO2kBCpr61McN1MoX6A6CxtFiSzn9PaOABChbNbuUtjR0OtZOb7g8h393CaI8A1LFtejak2uRP9Q2AU07RBXVWmCZi%2BF3RxgBnT9EoUd7xeG9cYja%2BHHOBErWrPd%2B0JLK0BPSkqDS8RC00JfjcTELt8%2BiS5qwrDJVUrDU8%2Bj9rtci3TiD%2F9DUizbHS0kXcKe857DUmEEhfOvRrzfC4MLWFnb0GOqUB90zJ%2BP55o4vDrC1Tsk8sljQZ7QPw7OdIJH7y9357xHBb8if0guHK7ApYSbrdRF1C3Zm5NEpa76BjIeb9vteqm9HVXucz76PvKVPvrOJpmQUufFn%2BM6cM9XGbmYPTTpiNaYuKV78W2j2Zzqr9xBVM64WIAvnV21qCYYqMlNkvFzIWLfeN1V9BIaGK3qQS9TGJZaJ6vNzQmMzv4wMU22fIPExEdHQ1&X-Amz-Signature=bae5ad5dd2c2f9d25f1d3801671bb22f8c8f046f522abc7a873f42dae14d6658&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y45SD4PE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIAV9drXTDyi0k6C8oZ0%2FDPqAMvZFvUIGDgePPOF18i8yAiBFew7FEp7L4f38SdkfW0pvx%2BWWXmuN9MNbV06kI6Vu7yqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmlIr4YfiyZ6cgHutKtwDphlCjm0zH6yjKr3Q0jSVXMkWvNtyvFpYcyy4oTj3BUhJzjJbzApg6qhYpXOeDtWdNdNfurwYCZNfySACu24prWvbLmCqzxY4Gmu1XzzrBA7f1C5YWUkbKwsqkmTNRbAG7UMAqJinxU5EiKP2WOcFDBDduTcSDuvxQe9EUHzO0u7tPyynLAkhtnfGf%2BumLONYW7jlNA4r1fNDs%2Bwv1z%2BMKLLgqMjuxOKSDw3FsZ%2BN1MnqkegUjKKjEYMW9OISslZfI8sJRxdURmADCGsgTqu6ZENcJAE3N6sdpFhzU9Nfp3Epi3praJR2fjv9f%2BfLMbIoNKzl%2FQXrfN2jmTqKLsCLhTslgliug6hgXSWz1m%2FfD8%2FIVza0L27bvgWW2FcKuulMnu%2FNM65u629Wu5CUI74gCt6cJkK6uD2e8BsFW2bvhIhvMm4%2BMuT43K4YTma%2BMQUB6%2FmkELJtcrja2lUDmvEL0mxq3yuS5Ikg2Jmi1Gm2xladFJhjMvMY56gYWLLF15moy2SqKGkLBAd153a41LofhmHGJ6xRyULDFCc6ax%2BufPP7yUxvwGCU2iAFqeTxD4BbVPgPqt9AfGGxu%2B8Ib5J%2F0EmZZoumSWPi6MNMfFW4oVgTIiKNERJiFN5qfQMw54WdvQY6pgH4H2KMSmNcaXNGiWBPIz19qdrmRMQ1Nc11PtMNbEvMr7kCwaXprcrlE%2FGMI1HJzYZ23Kqs4FJ%2BbcZA9FBsEQsp1QljDjg0Sq7W1%2Fp9E7hfW1ZJGTz1xHz180sp6T1a36V%2FxKv8qg7X5XlFiJHmLw%2BM7ajuWX6Rq%2BLEfFkyewmRnZaK5iv9B3UyyurEAsAfrxyVAmOOPP5i%2BjJGvl7wmZQKcsIW9%2BG3&X-Amz-Signature=66ddd84ab6b5c360dabe9ac9999bdbb6e3175d41f0da0e7d5c0a62e6d8ae3c54&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y45SD4PE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIAV9drXTDyi0k6C8oZ0%2FDPqAMvZFvUIGDgePPOF18i8yAiBFew7FEp7L4f38SdkfW0pvx%2BWWXmuN9MNbV06kI6Vu7yqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmlIr4YfiyZ6cgHutKtwDphlCjm0zH6yjKr3Q0jSVXMkWvNtyvFpYcyy4oTj3BUhJzjJbzApg6qhYpXOeDtWdNdNfurwYCZNfySACu24prWvbLmCqzxY4Gmu1XzzrBA7f1C5YWUkbKwsqkmTNRbAG7UMAqJinxU5EiKP2WOcFDBDduTcSDuvxQe9EUHzO0u7tPyynLAkhtnfGf%2BumLONYW7jlNA4r1fNDs%2Bwv1z%2BMKLLgqMjuxOKSDw3FsZ%2BN1MnqkegUjKKjEYMW9OISslZfI8sJRxdURmADCGsgTqu6ZENcJAE3N6sdpFhzU9Nfp3Epi3praJR2fjv9f%2BfLMbIoNKzl%2FQXrfN2jmTqKLsCLhTslgliug6hgXSWz1m%2FfD8%2FIVza0L27bvgWW2FcKuulMnu%2FNM65u629Wu5CUI74gCt6cJkK6uD2e8BsFW2bvhIhvMm4%2BMuT43K4YTma%2BMQUB6%2FmkELJtcrja2lUDmvEL0mxq3yuS5Ikg2Jmi1Gm2xladFJhjMvMY56gYWLLF15moy2SqKGkLBAd153a41LofhmHGJ6xRyULDFCc6ax%2BufPP7yUxvwGCU2iAFqeTxD4BbVPgPqt9AfGGxu%2B8Ib5J%2F0EmZZoumSWPi6MNMfFW4oVgTIiKNERJiFN5qfQMw54WdvQY6pgH4H2KMSmNcaXNGiWBPIz19qdrmRMQ1Nc11PtMNbEvMr7kCwaXprcrlE%2FGMI1HJzYZ23Kqs4FJ%2BbcZA9FBsEQsp1QljDjg0Sq7W1%2Fp9E7hfW1ZJGTz1xHz180sp6T1a36V%2FxKv8qg7X5XlFiJHmLw%2BM7ajuWX6Rq%2BLEfFkyewmRnZaK5iv9B3UyyurEAsAfrxyVAmOOPP5i%2BjJGvl7wmZQKcsIW9%2BG3&X-Amz-Signature=b8f5bf5b8cf6387a748f3261fb4e6fe33d15645252f8a4d049eb6e35731586e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
