

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIW3I3KG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBUlodbXDzxCSWtQPJT9pXq9NTYLbwgo0CPWQol3tb%2BgIgWOuIbHG4suz6BVrG%2BaiBbdvZu4zGmrzlzvth1xc5IIcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRfE7OTNbtEkwGvDCrcA2ZwK%2FSTQTG5y4eRqABLXvNPWv3fyZ8b0s1F23MTk25QiOIbjf%2FMNd%2BgJigjuUvw7QaKG7qJZob88WR2hpUvnqHS1hRXQM4ry2U8q%2B49pQWm2vbbTtiHfDIHS%2BdPcU2gswd3aOONIe3opovSaCtl96RqnhHEI0UTbfiMtlOWs00BPgLn6KlaZKyM%2FacbLK6D2pueudlC3hSMQ7c8Fu7k%2FbJQ5Cf98OZn2XwannwOKOxxAe1S8kjFPG28X8kbFJ4WftAaC%2Bn4YSJlYugs6Zvw43vr4FxAPKyUKMskgmsoljXXZXBzhie5sb8yD2O7yCFOTZHKxDlrtdPcA%2FEeVk4EnDujOpmeCAA0%2FoxpwdSP%2Fb0r%2BR03VTOVw0UYriknjvfxUG7UX1eocrIrMoBt5mZ1Ndmh7uGvke96j65QpQzlPNkj30N0yGg%2Fgsum3EmKItl%2FoD%2B%2FpbtxXEDG3trXlG4fAM0YIb9TOr0%2B1vCvhYxY8Ecm6u8QCXTZyKSwyXSNwJwaJBDklmQZlslE3Bt3up4wSk%2BAtUR3a3Za8knnj66BD2aGb2b1fQCilb3vbVwEuBnAtfzhOqyzv8Aojxcr0S4H0iBlYezP7%2FqSMJlhLe1hvngPSuFd9Yj0TtCFNdjBMPXH57wGOqUBh%2ByyNlF8i0gFVpEyOR2yPi6tYEQyqZnqNeZFM44CH2Lv0U4uxhhykTi4iXMnHiHFv43BR%2BiNyAeMN22Ay1XaX5qN3ih6ZAMzEx2xA7KAJlbAKJxFCcuQMaOwauWhpPqTdcODfJ7lrkxttHDZFFWhyvzXXao5GOeBdVCyellFMQSuY7%2BRWWesuO%2FqvPJQil9uR0hssMyQmmBYnopsKaMicDHylnwE&X-Amz-Signature=3a97807869939d41702b2c6c0e5ed56127a06e180250fedf5ddb6fca2e15a642&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4A26JYT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9OOiMhjLETEGt8%2BbLm6NlL7lmkq5p65L0TW%2Fu2pdlggIgZPynPqE%2FRE3Fh0xRvHB9JyR6dHCFIEcoESeq77TD5hYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyie%2FWD7xq4HbfDoircA2QEDgoNbFt1MMqqt2yP6AbovpKAlY5IVxt2YztBGVMAp9mUWy1uqCLyrV3MZlGuttzJYTnMwLB7p%2ByWjCgiaR2KCM79BMRLyEmIEvWexgCtmgzgh8LR3SEzS9N6J1oQKOsgar4BSz1W47n6cCJeSvU%2BYDjvloWRgZRJe2vEK%2F4Bv0S%2FZyFwHeb7%2FWP43HkkEZ6%2BCFDzVKHAejCIh2EJq2XqmxDPkjp7TYWG5IaNigNMCOny5%2Fh5GoFAghWeJLNo0R9gMazH6nVYuErT6cg5rfDBiSCLYBy3QNOpYGHofdk22NqjqtoebybYvVxTTlWlsDrXyQgqzlTEHBifD51U7SjcF52oyf7CFRv2%2BmO3ATSsrSCjC1U%2BHU8hyYp79A%2B6tcf8df7x1Z0iJHLT6C%2FnJi%2BLNOjrWh2QySupI08SSTnRgjhtMfsfof2zBE4uyzC3Lbx7qoCstbzpf5w90T%2FmeEBgPKpfLVdKrA5mxQhjcoP7%2BD0RUNxb4w3hawJ%2FmTz06eNQLkYdkkyeWqcpchOWin85%2B%2Bo62zM5HubiuqoWi%2FUDkvi7JNCOr9QS1KQURBs1m%2F%2FK8nqBqG0ypD3jgErLRRMOCMXZ%2BjaXQ%2BjSAPUdyOTgIusWECBBLhp80fYXMOHH57wGOqUBRlTlEpXrB%2BpVRg8BPQ1o%2Bm6A6%2FlvpdJWbVDI7AgpQvfyX2sNIJeA2hmngUcccYaHJ8uP9fRMqix1fj4Na6a6vzGjkH9WZiBP28K0W10JGur2HxCdTnPwPpvC%2BARtIFsG%2BQNNdR3xOIKKE%2F6wn6txUNau6lzODY6Kg6MBhRvUi93actgtneQNL00inn3Gq4GmWGjKX%2Fp80%2Fxi85uoOH2BaUQT2fsd&X-Amz-Signature=2a122076955e8a65e2228bbd3188cdf7a3be83b597689d4cde9364a8fe473231&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4A26JYT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9OOiMhjLETEGt8%2BbLm6NlL7lmkq5p65L0TW%2Fu2pdlggIgZPynPqE%2FRE3Fh0xRvHB9JyR6dHCFIEcoESeq77TD5hYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyie%2FWD7xq4HbfDoircA2QEDgoNbFt1MMqqt2yP6AbovpKAlY5IVxt2YztBGVMAp9mUWy1uqCLyrV3MZlGuttzJYTnMwLB7p%2ByWjCgiaR2KCM79BMRLyEmIEvWexgCtmgzgh8LR3SEzS9N6J1oQKOsgar4BSz1W47n6cCJeSvU%2BYDjvloWRgZRJe2vEK%2F4Bv0S%2FZyFwHeb7%2FWP43HkkEZ6%2BCFDzVKHAejCIh2EJq2XqmxDPkjp7TYWG5IaNigNMCOny5%2Fh5GoFAghWeJLNo0R9gMazH6nVYuErT6cg5rfDBiSCLYBy3QNOpYGHofdk22NqjqtoebybYvVxTTlWlsDrXyQgqzlTEHBifD51U7SjcF52oyf7CFRv2%2BmO3ATSsrSCjC1U%2BHU8hyYp79A%2B6tcf8df7x1Z0iJHLT6C%2FnJi%2BLNOjrWh2QySupI08SSTnRgjhtMfsfof2zBE4uyzC3Lbx7qoCstbzpf5w90T%2FmeEBgPKpfLVdKrA5mxQhjcoP7%2BD0RUNxb4w3hawJ%2FmTz06eNQLkYdkkyeWqcpchOWin85%2B%2Bo62zM5HubiuqoWi%2FUDkvi7JNCOr9QS1KQURBs1m%2F%2FK8nqBqG0ypD3jgErLRRMOCMXZ%2BjaXQ%2BjSAPUdyOTgIusWECBBLhp80fYXMOHH57wGOqUBRlTlEpXrB%2BpVRg8BPQ1o%2Bm6A6%2FlvpdJWbVDI7AgpQvfyX2sNIJeA2hmngUcccYaHJ8uP9fRMqix1fj4Na6a6vzGjkH9WZiBP28K0W10JGur2HxCdTnPwPpvC%2BARtIFsG%2BQNNdR3xOIKKE%2F6wn6txUNau6lzODY6Kg6MBhRvUi93actgtneQNL00inn3Gq4GmWGjKX%2Fp80%2Fxi85uoOH2BaUQT2fsd&X-Amz-Signature=277c48c83704800cc4b940608f1b86dbce7ebc61045465d92ee751ed658b69e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
