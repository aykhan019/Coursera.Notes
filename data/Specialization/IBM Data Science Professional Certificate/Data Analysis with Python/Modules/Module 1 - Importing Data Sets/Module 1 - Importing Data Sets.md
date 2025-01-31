

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTHLUJND%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpLncowR3V9MNefI1jiQWFkg55fGgICg0U8WZ5HxkI4AiBfoZNHpz0Far%2F%2FEatSIgjWI9ZqGKmoS6SV424dq15gISqIBAi6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeqZEYVGou4C4bYOQKtwDVratBgKSXHdLI%2FNwfKxU0B7EfJy%2FueJUFJWgX28nqR2Sph1vY%2Fkiurs1pXwjUBuXVHqijC%2FYagC4Ij23mcjXvWnhn8bs00%2BFeDP4jprDIttBSYOArMdxrRvTdEubfb0%2BZw59ovrkxpkM%2BMph7MSHqhTlvMpuHFkN2i5hVWkCgUqg0TwiZd7aKWdpsPupEvPyr8Q%2B%2F3nzadeB2sdxqlHhUdn8D74dx5m9PcnTdDj5Hc31y7XIzXKcbPUsLjvBw1uJckGdXvJnTc2JtU%2BsrPzPqnrTDPYHtRUuF7c3n3N3T2C8EAS2MCya6EX2UwKj8GYdaG086qNh64G72UlQm8anq6bkL%2FHWvuqobchPsKQhXTJ0GR04rlkrIrsb2T6p2pRkn7XvXfhFw%2BEGiAHnML%2BgpNemIQ88%2BpcbY2g6cQSVYn7CMIR%2B%2BTQrK8zGPhvrZjPLbM4iV7BTHFbqjEDIBt5jHPEA3dqr8DOld66BIp1pK8HikE3PEJICVpQ0LaY3Kj04bMXawtq1kMiS5sQeF5dCvt51J8aYsxP1yUxhVGB9bAUyzd%2BOOAx%2BfV1c8Fcy12orWGkqaUhy%2BZJjsQff87WPDyceATx3wtuaD7zA4Blg6ul5ZQUg5VkqDx4nnIUwsJryvAY6pgGX3jwWBFw1y6T6xHfpjB4SxEYBMogGlvhBc%2FnEs7LCjcg1ZcU3xoBKBK1Zh%2BGl4ZBDPaRhGYi%2BxPi%2BPStRdHi2WuCqf0Y5N0TnedPzENZQ7NsvuT1%2FCcaP0CQpFHXZhkLzC5AWvR661k4Qmh7Jxrq8xrC8lWYSchqyVm0XiVgTDkmmn0bS%2F%2B390oTUR%2FOn%2Bd5kGmj0ltUogqY8zSMGNmEV8nM0ngJP&X-Amz-Signature=1228b26c61b9dc4363dc1cb29363b75274b4e01569ee6bc7c9e907bd778455b3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646XTZJGF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3MNBmwnT6lKw2rOfZdcpV1Th85mtMOXpAdNWjVp4SdQIhAMWxbYORXsRc%2Ff44Yki%2FVmqWoeVq7hbqltsmQf7hHh2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMJiRG10KK0r1%2BbOUq3AOVRn7cwBeqv5XbgSHGGTqtfFYmLT2PYzAvH8sgEVSaqv5fRqog0JCcHlpIAL%2Bhs3H57QRiTY9O5cDi8Dyo92APzAUivcTJ6xIg%2FZYBdz23pEphGpkRjPZ4Zk3zxpOXmow%2FNLPZAZSw1zuY3mc%2B71ctLZBTVmlRYa2pR99bPSFHX8RNZkTb5dQbKYQJgcjQN%2BI5E51oplYjcqtkB3SWIr7pFqrtfyldl0iVIOFDI%2FJcULuPDk4%2FrlZWigypipQxqD8zvkKPAxF7tL9L4%2B8EyWz%2BhMS8sjYAE2Zi4AJfwkrOEfR1EPnZYoHJ4QNoV97QUfwI4%2B2TWyypXkR2%2F4Ebwomxifof%2BzYS7WEmccN09lXZFr2VHlb%2BPMS2yF0WwdgI8i0hDTi%2Fzx9A1g%2FpuEemCT5bGn7GAcCLWsIKuHyjT3t0wXVRDkdyJvd9sUA8%2FFduVWOlN6yP5%2F0gGj1F8zkg1Sg4z7bRbLy7qfuX2%2F4eiChctHcX0EBADz42l0jJ0xcNt1AHXV9ap%2BwKQyQOzr33fH9JjtxQVDga4zC48XIQdz4XHSJgTQ79oCDlz82ElJI8s1AaFKWS9EREBCG%2B%2FrNShJT%2Bw61%2BVTW%2F7VvRCH9pUkZa4CzXzJwqxJ%2FTilYITDCnmvK8BjqkAZnbFbIwxRmrNzhXL5viV5IwZNWvWJcmkxAq5DlSntOMqg%2FbJ4pB0p2vWt4ANaHbwfK1JK99OxNBvcHb%2BjZy0I%2FQeTaK1lXthaIcAvCpTf%2F864JeAXvWHFhnwAPrHsWOcBth2hkE%2F2wi8m0nbsZKLF7gNOLVxehoN9jrZ5aX9XgFLbHTj%2BVbTdDDy6%2BGFGTxyBfRPjW9C%2BHlmWDI33XCnpjXInI6&X-Amz-Signature=2279e816457b806def0dca8f6e552b65e867ddd5694ad8b6b5506edf955ed7e9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646XTZJGF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3MNBmwnT6lKw2rOfZdcpV1Th85mtMOXpAdNWjVp4SdQIhAMWxbYORXsRc%2Ff44Yki%2FVmqWoeVq7hbqltsmQf7hHh2FKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMJiRG10KK0r1%2BbOUq3AOVRn7cwBeqv5XbgSHGGTqtfFYmLT2PYzAvH8sgEVSaqv5fRqog0JCcHlpIAL%2Bhs3H57QRiTY9O5cDi8Dyo92APzAUivcTJ6xIg%2FZYBdz23pEphGpkRjPZ4Zk3zxpOXmow%2FNLPZAZSw1zuY3mc%2B71ctLZBTVmlRYa2pR99bPSFHX8RNZkTb5dQbKYQJgcjQN%2BI5E51oplYjcqtkB3SWIr7pFqrtfyldl0iVIOFDI%2FJcULuPDk4%2FrlZWigypipQxqD8zvkKPAxF7tL9L4%2B8EyWz%2BhMS8sjYAE2Zi4AJfwkrOEfR1EPnZYoHJ4QNoV97QUfwI4%2B2TWyypXkR2%2F4Ebwomxifof%2BzYS7WEmccN09lXZFr2VHlb%2BPMS2yF0WwdgI8i0hDTi%2Fzx9A1g%2FpuEemCT5bGn7GAcCLWsIKuHyjT3t0wXVRDkdyJvd9sUA8%2FFduVWOlN6yP5%2F0gGj1F8zkg1Sg4z7bRbLy7qfuX2%2F4eiChctHcX0EBADz42l0jJ0xcNt1AHXV9ap%2BwKQyQOzr33fH9JjtxQVDga4zC48XIQdz4XHSJgTQ79oCDlz82ElJI8s1AaFKWS9EREBCG%2B%2FrNShJT%2Bw61%2BVTW%2F7VvRCH9pUkZa4CzXzJwqxJ%2FTilYITDCnmvK8BjqkAZnbFbIwxRmrNzhXL5viV5IwZNWvWJcmkxAq5DlSntOMqg%2FbJ4pB0p2vWt4ANaHbwfK1JK99OxNBvcHb%2BjZy0I%2FQeTaK1lXthaIcAvCpTf%2F864JeAXvWHFhnwAPrHsWOcBth2hkE%2F2wi8m0nbsZKLF7gNOLVxehoN9jrZ5aX9XgFLbHTj%2BVbTdDDy6%2BGFGTxyBfRPjW9C%2BHlmWDI33XCnpjXInI6&X-Amz-Signature=908fc582fc43359db1f8f33b271cc2a33206638f1d58ab46c0b6669a55c383a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
