

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKQAVKMA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIGfGFUtjtZ%2BMkxf%2FVPb3qG7cFJmFfcoa%2BMkLqrx3q7vrAiEAiL0jeBa%2BUdjRVgcly6smubFkgcjhAH1KA2E1AOTeFZgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDD8jlcJOpRFHQ8UmCCrcAx4pu7V2AhNQ8f9cOUnsFE7ZMS09jVD30%2BfIPKGi%2FW5vfW7y%2FMCFI0iEiZFpPTy3FkiVcZAqayR6cPZYGBAb6%2F3Ev5r20KdJUnZs8GFhd58whx9f3vjbTbTVQOOd8v%2B3LtmkoBkpImQ%2BcfMBx%2F8d3%2F4TZXaQiSoLWdIYUU5Y2GCYI8vvQiI8zB4GP8psUoSHTdrtuoEz40h2xQqce7KQ%2FafA2WjqWqR2qOq1siDIV3flKGS9HwjnNSn6REdphk7GOHwRK6yJiKudCpitCXxSxfSKAd7WjNWpFMikyfzJEpUyb4A8l9lN9nrEDg80hNa%2Bsv0rQWA4RAsnM9bXK32lNOGpzzhMXyJK0OqC1ixIRZTAZc0ofcwEGc6s98%2BGfxPVmQekic1H4tYBf0WhofGefNPLcEqH0oiKe5esGZsKyZSKL6y2QX7bOj5TpimQDCyJTLIb6CsmOKduGRkg%2F4pbuetTTUPkhO72WvIFjQ2lp%2Be1MTrA%2FExH1kkfPX6B7uOsXB%2B8WNGPxnavXahMnATmoyoHB2vQk48YRk%2Fs2o98xJLRitwQACerpBzxEd6%2FkPtwY%2BrfPW%2FQTr0s7cmnSzL9L4QqPxqa5bHTlqo62%2BPcg7EaBK1Fw1Y2kbw5i5e2MMz5lr0GOqUBWdHiHgTNq69zspipcg8Wv2%2F4i7YlttdIK0MUpeaeYxW8ToR48xPnu%2F6ghnzS%2FmfwFCTU6sVNYJlxlXUHl%2FchLN0OR6V9joAF0noZ75Yq5hRf4rEt4xde6SQudQxGpAzsGy6vnoqBCaQAoDKbnavhJ9nGFoia8ILGhUlvnok%2B3ge9EP1cT5BWrtnMKUYUGfyeNPsEakKIn9ldkwKZsnAR3HSmaqt4&X-Amz-Signature=b9960180281b3e515ccbb9628c75af1304a6d037178f0c00a46e353e11319afe&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMUWZKKJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDv4NXj6L9VISU42E2CHxRwDTtMkeLql2X4zOW0EQVScwIgJQStGehwrbynMpBjLxuU8Vr44E67glvrSja6Om1FeZEq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDD5V1vc%2BmpXbswrbfCrcA4qQw8gW%2F5s7kMXcKrEnOWFs2LmUe%2BHyxYTDfNBG%2BxtOKOKQTLnU9wbFJ8MtCC7Zp9nz1LwJFElFrHzZdoQddkIE%2FsAZjNpvxP3GGF1XchdDV8D0ipPsOHRPAnf9ZXdr9CIwkbb%2BoDEZsztwC4uAxTFVMdI45FlQAjlBb%2F49L4eeEEfV%2FF4QeGW9SyWuZCYS6wh3FhuhZyRMp%2FJLacZgkrkdaIZGqkxsj1Br%2B0KdCGCJQ1ibzcCbrU2wk7j1Z9YSFuqTEQmfjw9Pl8IjR2wTaHLG%2FF3qDGrGokln1GsfiQ4y44gFRIXAVR9dvxLcWdmwYN7D%2BS0WuH%2FURKENdBS8NLVmhaEIr5jLht38pVQ4KJiS7MRtShgJlXz1QRBRU78vtBV9RVfPc2UtsWIlFvt38kSqQ3qhFA2GtdWSIx1h5qt%2BfL8vy%2BTfV1Rcvhjseu2NIPr8x%2FVLDitDrJyyIff2RUbi9AOHZ1msI5QjuB3M0SMOWSEeD%2Foq0Bh%2FsFL6XbIoZvJcbmZby3bMhszLClcdfKV3IIS%2BOKK2vj99%2Bgp5uQnxGmWeriu%2B3fMLo5dqUDkvCVGU34IVc7eUtNmS60Y6ISv%2BJZnepda1WakSEiYKkePme0r%2FW14v3Ows9Q%2FWMMv5lr0GOqUBuaOyPtogcRrdFk9MjUs3ewWOqiyf0qcYfbTnEkKOhpySxOEFgpMgBmekSjdJ70kskxHWy8Y%2Fsu4UDlJYu4Tjx5A2POobgVYhUq0DJxHu%2F5VJAsK%2FeIWfKwQiomJDdb%2F5CBzT6Eo%2B47rCeSqze6yLQmoZ8%2Fo4i5lpsYvdja422yJZ3naJ5p2BoZ5MQKpLLHWRK8mEp56nwKu1KGaorAdUZFhdc224&X-Amz-Signature=571d15eae72164dcacaefb470f60dcd7bef76ef65ebe22e4e591e2670dec3612&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMUWZKKJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDv4NXj6L9VISU42E2CHxRwDTtMkeLql2X4zOW0EQVScwIgJQStGehwrbynMpBjLxuU8Vr44E67glvrSja6Om1FeZEq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDD5V1vc%2BmpXbswrbfCrcA4qQw8gW%2F5s7kMXcKrEnOWFs2LmUe%2BHyxYTDfNBG%2BxtOKOKQTLnU9wbFJ8MtCC7Zp9nz1LwJFElFrHzZdoQddkIE%2FsAZjNpvxP3GGF1XchdDV8D0ipPsOHRPAnf9ZXdr9CIwkbb%2BoDEZsztwC4uAxTFVMdI45FlQAjlBb%2F49L4eeEEfV%2FF4QeGW9SyWuZCYS6wh3FhuhZyRMp%2FJLacZgkrkdaIZGqkxsj1Br%2B0KdCGCJQ1ibzcCbrU2wk7j1Z9YSFuqTEQmfjw9Pl8IjR2wTaHLG%2FF3qDGrGokln1GsfiQ4y44gFRIXAVR9dvxLcWdmwYN7D%2BS0WuH%2FURKENdBS8NLVmhaEIr5jLht38pVQ4KJiS7MRtShgJlXz1QRBRU78vtBV9RVfPc2UtsWIlFvt38kSqQ3qhFA2GtdWSIx1h5qt%2BfL8vy%2BTfV1Rcvhjseu2NIPr8x%2FVLDitDrJyyIff2RUbi9AOHZ1msI5QjuB3M0SMOWSEeD%2Foq0Bh%2FsFL6XbIoZvJcbmZby3bMhszLClcdfKV3IIS%2BOKK2vj99%2Bgp5uQnxGmWeriu%2B3fMLo5dqUDkvCVGU34IVc7eUtNmS60Y6ISv%2BJZnepda1WakSEiYKkePme0r%2FW14v3Ows9Q%2FWMMv5lr0GOqUBuaOyPtogcRrdFk9MjUs3ewWOqiyf0qcYfbTnEkKOhpySxOEFgpMgBmekSjdJ70kskxHWy8Y%2Fsu4UDlJYu4Tjx5A2POobgVYhUq0DJxHu%2F5VJAsK%2FeIWfKwQiomJDdb%2F5CBzT6Eo%2B47rCeSqze6yLQmoZ8%2Fo4i5lpsYvdja422yJZ3naJ5p2BoZ5MQKpLLHWRK8mEp56nwKu1KGaorAdUZFhdc224&X-Amz-Signature=eddbe4f6d2a36afda787db317b89d1793a064008a99ab2ac582f1bc89f43fc21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
