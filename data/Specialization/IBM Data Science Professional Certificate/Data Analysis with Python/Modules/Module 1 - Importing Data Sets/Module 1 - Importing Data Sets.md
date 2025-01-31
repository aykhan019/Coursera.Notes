

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJGOIRH3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmT5pgsESK6MCYkYD%2FJAUlJ3StCT5glsB3M%2BO272MmUwIgLmcCv85LIUBgKE718WEO8hKlLF945tweCTv7BI5EdPEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhQG%2B5guSyWg8oGeyrcA5u%2BAXcgXTLor1g5LC875e%2BAnerBocEtxLDGih%2BMDm2mhYamGRpRlK6Ew%2BSFRe91%2F7JpU0NXE0ELkIcEvblWtx4SM7Dsa2aDLXVDdjlUyCy5yhkJUu%2F2Riy%2Fc9WZ%2FqTw9%2BQVllj4MUmOTmC3%2F7baa%2BhZn5TW%2Fw5TOnGdYzI%2Fah6BH7NO5SSQ71XJYJEZ4MRJd2w0NF71Ui5FwEYIoaPK4YUq017TtyWjhZXXguL%2BGQ59vWwa%2BFfWdGOcRZ9VJNN3aIK3bc3CKPlRcFc%2F4Cd1I8AQQecYnOYKxF0Ilk2e0DOWpi6voUN3%2BP6w9BkVUj4xrwC3WKSjNOD%2BVNecztqDF%2B3cmndZUyiG3aIKsNS2ursekDdkjHL%2FDQ5D7g1mJHnrRZWMtSXDruI8jyyEb1pFUJ38am%2BLL2GVwZcTJFAmoaRx%2F%2BJ8n3vIOHz75LKsAeKLuN6KqhVvXSFYV7w%2BumLhQNksXR%2FAD3xXdqgABTTJV97qrUXSRjhVj62RB%2FPvxrJtgpCYe%2F6XUdos8TEvl4DdjRZKHUlz0ZZnT4y%2BDB9kjPk0eyWyp3JkerI4jmMGAgIS4ot3UbiaRwduMpD%2BrKbdONWU9LypayAIcsre5MLgjwK92tdgC2hjWDtz9uQdMJnQ8LwGOqUBffJ9xZ8xG9cy0irgePWVNOKkts2krLsesHh%2Bw%2FSjU%2Fhb%2Bey%2BaQJPkxH6OqX7MkHguMJyTwDeo7bqXgjf%2FtvAYAL1r2%2FQNJg0lkhcbrzqNIHyNe0MgqEPQ291LHzxDt5QJU0s6YOkbRHbrWSconQnOi%2FLjku%2F2PSl4rz%2FxL1e%2BGjnPICev5EWCB%2BFXzeT6kfSpzRqlgHTVWDXorPIp%2FIQ6OMxUCci&X-Amz-Signature=712c002aed4b9866422a60d01795791801e9b1207739cb249836e6dba011098f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UC3PQ44%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdih5UlrJGhrO9NtgSQghlR2PIrTcD0ml8QUmBiPZ9FQIgb2R9J1iyB41K6FRMZ4DbxmaHi5%2BcmuNNK%2BQyn%2ByQviMqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwpsVGMRC5JBP8CeCrcAy8JtH1RZPqSlmY328CWvdvYGyda%2BSbJGjtbF94yb2Rxuj5gX01SlLeeftHUTwmi%2Furhv0MDsgxiWLqYKgw4pXhLsLQme9qOTpsDO9KJFsIZMiXhVdPE%2Fvz6dyqnS6jl%2Fp1ZmZb6kfULyW1B2llNxDAfmyuM2ye2RDLoq87SJM7JHF5DziC1KU8E9P8crCENIBMtVOaaNo%2F9G8AHMnzc0x6s3zxw5UGq32YnDgAnYH2rz%2B2kExRirI9iNHDr1zv91cH%2BXcHJrrmgNWjkz6bJBty96RbiF%2Fw9%2B3woSo5EqT3Prw5dzJJiWqXjVJTdfPgt9ND7cvgt5UY%2Blw0ls3F9rARYLWB75rmtJajUoOIv4vpmp8K%2FIfYIsG6gFKP5JGadOVoyyB2tNxhKkVOx2VZ5OwJ2HKTeyAQJwIgA2uh9bMZzV7QRR4oHYnXgVMELGxUHo3iPokTr9SvLi1qS8Z57plYkSw9hxEr3DSPDIfb3WGw9hKuHdxuyvWoupIcFccT1N9OWEsbq%2FQy8PzCjwxScwPco6tvVAhmTtFBUK9onTFJF7A4eJc%2FqYaoB%2FW5CRYZZ6gveaEs2ehsiodPmOUFpPcdm9HwPepFEg8Q90lZTW2mkY6PH0B%2FfPC5kO3O1MLjR8LwGOqUBtPJ5bNMLF7HQ63shFlLHEpL3zZAs0cLaSwy8EzdIgdg%2BPSKG4lgjRtbg%2BTcdfEVpFbS%2BFeonQLsMhP8B%2FmOSzdHu7V3w14q%2BSxHh5tD26MdcaCyd8uv67NtMUwaRmPyZOMEbOFJp%2FBt1PswzJFs7Ei5kI9FYu6XqTDbZnrUstYA0Hph3JP432mTVwIHmt9rE0DHYON0H0kFiV61hOuO0KROihDP3&X-Amz-Signature=14ac24fc37792d7d39267e03d5ea206d929512d8dd53b930c48bfdcfdd671ce3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UC3PQ44%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdih5UlrJGhrO9NtgSQghlR2PIrTcD0ml8QUmBiPZ9FQIgb2R9J1iyB41K6FRMZ4DbxmaHi5%2BcmuNNK%2BQyn%2ByQviMqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwpsVGMRC5JBP8CeCrcAy8JtH1RZPqSlmY328CWvdvYGyda%2BSbJGjtbF94yb2Rxuj5gX01SlLeeftHUTwmi%2Furhv0MDsgxiWLqYKgw4pXhLsLQme9qOTpsDO9KJFsIZMiXhVdPE%2Fvz6dyqnS6jl%2Fp1ZmZb6kfULyW1B2llNxDAfmyuM2ye2RDLoq87SJM7JHF5DziC1KU8E9P8crCENIBMtVOaaNo%2F9G8AHMnzc0x6s3zxw5UGq32YnDgAnYH2rz%2B2kExRirI9iNHDr1zv91cH%2BXcHJrrmgNWjkz6bJBty96RbiF%2Fw9%2B3woSo5EqT3Prw5dzJJiWqXjVJTdfPgt9ND7cvgt5UY%2Blw0ls3F9rARYLWB75rmtJajUoOIv4vpmp8K%2FIfYIsG6gFKP5JGadOVoyyB2tNxhKkVOx2VZ5OwJ2HKTeyAQJwIgA2uh9bMZzV7QRR4oHYnXgVMELGxUHo3iPokTr9SvLi1qS8Z57plYkSw9hxEr3DSPDIfb3WGw9hKuHdxuyvWoupIcFccT1N9OWEsbq%2FQy8PzCjwxScwPco6tvVAhmTtFBUK9onTFJF7A4eJc%2FqYaoB%2FW5CRYZZ6gveaEs2ehsiodPmOUFpPcdm9HwPepFEg8Q90lZTW2mkY6PH0B%2FfPC5kO3O1MLjR8LwGOqUBtPJ5bNMLF7HQ63shFlLHEpL3zZAs0cLaSwy8EzdIgdg%2BPSKG4lgjRtbg%2BTcdfEVpFbS%2BFeonQLsMhP8B%2FmOSzdHu7V3w14q%2BSxHh5tD26MdcaCyd8uv67NtMUwaRmPyZOMEbOFJp%2FBt1PswzJFs7Ei5kI9FYu6XqTDbZnrUstYA0Hph3JP432mTVwIHmt9rE0DHYON0H0kFiV61hOuO0KROihDP3&X-Amz-Signature=7d6f8f6f16a3fef2239a86350f282049923d8331dab6cd0a9e021318424f2a6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
