

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQCNSCQZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICeM9hwKHYlIQzqPe1MxG7aYbK734WPhgL1q0WqXjvZiAiEAx1nmNbmLDfn66%2BNyLrTKmmJkYd6cBwsghD8TJAT1%2BFAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOK6nz26WVh1%2Bf3DLSrcA0CVaEYPVYyHqryJJQhwbyKliSd9Vb1oOUcb47g0Jzgywm57z0QEws0%2BVhTA1FknIyf3B0ckIet3GOge%2F4wa%2BdkV%2Fdhk1eTyEZy4zkVGHJz1yPYZZiRIVmCB1xYuWWrzbQxr3o46ywUnmoCOItaj5hPbHP2hwyRc0vknYlNnxFt%2Ft%2B%2FNP2mPycwBtuex1bEsCkAGlV1UzsQgl%2B1%2FUAPaMw%2B%2F6ylYumJKmduEGeC8q3fymG7PiyF8FDjNnAVZZQfixYWhN2lQtCANtjDgYlcMI8U8jcY%2BXqOKAHdNuPALs%2BVAN2WTQIg0RQP46fy57RsZm005JCG%2FHRoM8%2FhBtP9rG2b1AxNNTTCxKQtYWQ7Z%2FGaqHn8j%2F1UaDid3Rib6HvsWPd9wINfNCC8LHWShAAAtHElEp%2BKtjGROZyd9QtC7xE5wp3c2LvlWU4o6adPj2BnjpS3lVP1UQbLzAE6jGW%2FtdlgEKDkRdbRueS6B9mYurPlt4PJ8XX6kXONsjamX%2FNNRcHFjiZt6aHH3dSG%2B1ObKVSlpgx1KpG2arBkv61qMpa%2BjZo4WSDX0qrN0lXGIxmCzZnipjDJCtfP63VS7iO66pgpGz40R%2FUTGReUpRqe2cJdIK09fxmZxN1vmOy5RMPS65rwGOqUB2UNvMdQFM%2F1m5JQEPczMJcta8sjwDlsVScsU6bXfu%2F%2F%2FscImhztwY7JL6d2f3ZVleVlAHTTVzge7cikw8H9L0sq%2BRRbRtLFng4uDBsC7nbkKaJQ06NqhTkrIvCBPSXPArf8EwiDmKHJV2r2JXcQLHaSb18OLFBSOqk920iXRyxf%2B8f1t9NZv3ZYxKn9LFtIXWxjVsVMdZxu3Le%2FoImbzSAemuWWM&X-Amz-Signature=4ca0b2d9ca0f8e35b26f8b0520c71f472c8c95fa17f32ca4274336fdd346c073&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOMAXXLQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDAk%2B0ZMQ9KWChNWYZBGCBpz%2FaHk1ENnaiCDjtD4WJUuAIhAL3RbUf2G8rFhGJt5qfVST7vOX8yPpF0%2BdmHNNZfu%2FSeKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx14Wu5tG6QsqV24Bwq3AO8Z1oz%2FwcOg8NHSyv5R06uQTv1495geLLgCGOD5lWWVbenDannyQZ0MMhuGnsPZSP%2Fin%2FLjJp0PcYZK3SDi2fkcCKzJeS8bJWFRe7cSpyFB6Jk%2FHjCTH8ztpGy75tqmhFydWuwumVmGW7J%2BOTnJznw6mP9VF75pWrYUhJbQkmw8GXvpPpZBJsibpq5Qm13FcptAax6lyy8cZOHymsPO5rbdMQCsSbOPVdgVvOy4Bv3xwJgq3ynrmqo3E%2FeDdLe3uNbgQwUOPzd5RcPsYJiILGhsAobmV9dLui14QeTAdRL4wbPtzXqCKVkmOilT4YK1f1tDbFzpZVctmKrY4nFgjkZiVoWCJK%2F9mNKb8V20kAjqMEu10H0GWG7HZncjl0xWauv3IJQ7ppFPthmGhypsEtN5u7TzdfZ0Ueo59Z56EFew%2FuZTk65gXfOL%2FwUX8fi5jcc18gcsZsSJDUxkKVrr%2B4qCQQZp9HxDY2CPCej2jXLpWpYRsU%2BkQ4gIyKF5CP81SsLUlW4vh8i85UdaeUE62D9NS%2Fx56GYpdCK4jonFAWn1%2BHxX0eA7nHbuQuVyZ2IpPLqxsCBNaMLz%2FQv1%2FM2XGMcFK9pgiSt3kJO4B7pKE7bk1yNYs2sU7%2BAE4cwoDCRu%2Ba8BjqkAVNBnPWDPalwh7eLWi9HVCYV8b5NTELu8mGJjoeKsDut85Ek9lBv4f5SfXM35A6gGdg2JNHvC6ZfyHYtT13zkVJQskji9v%2Fu%2FcEm%2BzYRwZZcr7d3h9%2BEPVzFb9pcsS3LGvKqqI0M%2BtH0k9FoapkVcp5M6tR7cmbAderZgPWzreIWo8lX7UpykcFfDVXC6izvU9WDlCX6nXhGjgEYf59%2F0dtl2sNU&X-Amz-Signature=269361ae834da8fef71d336a93261b2efde1c90fa899c208f45c606e6f2dc671&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOMAXXLQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDAk%2B0ZMQ9KWChNWYZBGCBpz%2FaHk1ENnaiCDjtD4WJUuAIhAL3RbUf2G8rFhGJt5qfVST7vOX8yPpF0%2BdmHNNZfu%2FSeKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx14Wu5tG6QsqV24Bwq3AO8Z1oz%2FwcOg8NHSyv5R06uQTv1495geLLgCGOD5lWWVbenDannyQZ0MMhuGnsPZSP%2Fin%2FLjJp0PcYZK3SDi2fkcCKzJeS8bJWFRe7cSpyFB6Jk%2FHjCTH8ztpGy75tqmhFydWuwumVmGW7J%2BOTnJznw6mP9VF75pWrYUhJbQkmw8GXvpPpZBJsibpq5Qm13FcptAax6lyy8cZOHymsPO5rbdMQCsSbOPVdgVvOy4Bv3xwJgq3ynrmqo3E%2FeDdLe3uNbgQwUOPzd5RcPsYJiILGhsAobmV9dLui14QeTAdRL4wbPtzXqCKVkmOilT4YK1f1tDbFzpZVctmKrY4nFgjkZiVoWCJK%2F9mNKb8V20kAjqMEu10H0GWG7HZncjl0xWauv3IJQ7ppFPthmGhypsEtN5u7TzdfZ0Ueo59Z56EFew%2FuZTk65gXfOL%2FwUX8fi5jcc18gcsZsSJDUxkKVrr%2B4qCQQZp9HxDY2CPCej2jXLpWpYRsU%2BkQ4gIyKF5CP81SsLUlW4vh8i85UdaeUE62D9NS%2Fx56GYpdCK4jonFAWn1%2BHxX0eA7nHbuQuVyZ2IpPLqxsCBNaMLz%2FQv1%2FM2XGMcFK9pgiSt3kJO4B7pKE7bk1yNYs2sU7%2BAE4cwoDCRu%2Ba8BjqkAVNBnPWDPalwh7eLWi9HVCYV8b5NTELu8mGJjoeKsDut85Ek9lBv4f5SfXM35A6gGdg2JNHvC6ZfyHYtT13zkVJQskji9v%2Fu%2FcEm%2BzYRwZZcr7d3h9%2BEPVzFb9pcsS3LGvKqqI0M%2BtH0k9FoapkVcp5M6tR7cmbAderZgPWzreIWo8lX7UpykcFfDVXC6izvU9WDlCX6nXhGjgEYf59%2F0dtl2sNU&X-Amz-Signature=0b67a5eea54d6f7f91f3a5bc8fbf2e13b18d5fc63996172a2064acd4756b7215&X-Amz-SignedHeaders=host&x-id=GetObject)
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
