

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675YE46OT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFx%2B32H0alqee1vV952CktIFo02FrSly5gqYtJZeiCroAiBuN%2BVynXr2t546zIc2X2Mtxq9D7OF6ViViNJQCjc%2BJBCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCqRa9xUznXB4XpVHKtwD9jEYdTw9%2BHXNYQhw%2FwJHJ1E6bFqzLmquG%2B8zork72%2BdjSSjgf4yXoPjnb5rYzOxTjirQAG98isWpDcbXLH6NX4pIJpBcFW%2Fn7SPKfqpWqD%2FMRc72B0DUg9BRMF8OKAWOAj4T8Fmz3GYcQAzCEkgnJlPPXbE9PYvXJIsW4h3YbihDeg%2B5HLypUkzc1ecYpn7PsiUsj4EvCe3j8Prsc%2F7Qx92jhH0t7M0nbtxEHVOwPCaJ%2B0Gu8vv17vgrAiiSI%2BpOJS7T1gk9XKGR84E0RhINANUR5ua34addYNLxcLIjkHfXcVKK2QfHHh8ygp%2BJL%2FGCuiu9Ymd3ZADXzuQD%2B5YJysGOzgbTBSZfhB2yAWjHuwfkryRWXKaBWAD6m1wLegTKaq2r8KgOTW0znluAQolMY8d1utXgURIplRFXnXVIQv%2FyxxaLNgaRAWdVtSJ0iv%2B%2BBg6mpKRbIef%2Frf5me75D0zvOOWWh6k79ortxogm2NDGdj2qsUziKuHbZWGvGFi4t9mRxB7nA4hoC%2BL%2FScKKcmDNi0LFp6p64WhQnWYtdXfLZi2yQbUe%2BNS0FY%2BHmeIwZnqTTZIL7ZyCjjw8oVM5fbjVoRGV7DBdbSXAJyh24jgqLn68YA3Fc36YA3Iwwjsj4vAY6pgFCxNZJFdeONmT5waHApV6K2Cpk5dr5aP2XYDvo%2Fnreq%2FzE7o5PUd9Y1HZVEkhxQKOrki3Jmb04WaQiqgbdBGnS7PIDNO%2B%2B7rEUGozjGlVHh83LYvRcEOUWV2Ge5jsWiqObdQ3wEGJdXOQuICmc7rJ%2Fcx1T4HdwnPc%2F32YAhAlrCUVfKGOZJpL3gYthQyygCf1htCYI04UzyH%2BomLBHdZ%2B0NvLaplmv&X-Amz-Signature=27e2deb715c0c4e4dab863a5a79c382b526e16e0318b5e9d03f12b4332052272&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656A55377%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICSWbMBDd9MZ44zUqdNXyYuvsq1r4AwrVvx6hjRBgBLNAiAbSZ1hhN3lv0JrkaLrdcbGtyjB9KTl6hNfubZVtXGh0CqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOef4r8tkhPKcoXLwKtwD3ymlDoshtkX5NhFSFloBFlhEH4qXj4Py1%2B%2BT%2BU7IyOlrHJE5u6P2bynkIA4Bv8zFCX1z48KB2Cbcy2ugezqISvTOxjZrA0KwYhf6bfDZUfsTNNo2vHB6Ml8avel5IM0VVml6GlFGGVoBbsBt%2FiMirRZeBo5IWWIWGiT%2BifzfP1MRPCWVUleYC0XGlzjP6q1ha3goamXbsOInNhYiOazDIH11BcNU7Kr9CRxx6TFjaWjrRTZtYjA5Re3dxZuKfJJYMRw0H7IZqQrHQDvXGQq36dXtd6a098ZWRMMS2hP1E34Js7%2FKM5Mp0I2yG8id0IO6WvLjRn2AOhZn7728iNgC32XSkGJOYyOpA6OAq%2Fd2LY0PbjfI5I3lyGhGuf5trIcuYCBAGPX2TUAIFzNrtQaGFo2G8IEcUKfozJhl182P46Blb81OVqQP9B7V2YhGi70QIxTwtu705%2BF%2BZANZQuW3QrXxhe5vS9CQC0EA83uE0h%2BIR%2FOMCFmAfln5XNLKUivS%2FK8s3lAVxxe2i95STZmw8AxtH1HbNoVVeM3QR5%2FTuWNOxh15apEcn62T5Ca9ETw8QmF5UpN8m0ivI9vhut5p6ABUi4znDntYrwjaJ9GySetEcOqCjrZ1Hys%2Bvzwwssj4vAY6pgH4r82CnORo56lupY0xm4NgKJcgApYI1k2CgiUsVh61qkQUu8rOtGY%2Bl0jLZlDmcZjemX2UWVJNNpdGvRcNfipKlREQAMlU7w2%2Fg0xGrtnzPDub69gTMqi9l7cD9htnA%2F2pnB%2Bih8VSTEd2m%2B%2Fss9I3V%2FisY2j6SHH6mA7PmgGY8wpwwscGEc1CvH2udhG7731RPrGhKR98PrQMLbxv5rp83Ox2mRWU&X-Amz-Signature=78f3691e9977ea685d98ae6004ca7b5457b70188a0e2da79b74ada5a4750d670&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656A55377%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICSWbMBDd9MZ44zUqdNXyYuvsq1r4AwrVvx6hjRBgBLNAiAbSZ1hhN3lv0JrkaLrdcbGtyjB9KTl6hNfubZVtXGh0CqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOef4r8tkhPKcoXLwKtwD3ymlDoshtkX5NhFSFloBFlhEH4qXj4Py1%2B%2BT%2BU7IyOlrHJE5u6P2bynkIA4Bv8zFCX1z48KB2Cbcy2ugezqISvTOxjZrA0KwYhf6bfDZUfsTNNo2vHB6Ml8avel5IM0VVml6GlFGGVoBbsBt%2FiMirRZeBo5IWWIWGiT%2BifzfP1MRPCWVUleYC0XGlzjP6q1ha3goamXbsOInNhYiOazDIH11BcNU7Kr9CRxx6TFjaWjrRTZtYjA5Re3dxZuKfJJYMRw0H7IZqQrHQDvXGQq36dXtd6a098ZWRMMS2hP1E34Js7%2FKM5Mp0I2yG8id0IO6WvLjRn2AOhZn7728iNgC32XSkGJOYyOpA6OAq%2Fd2LY0PbjfI5I3lyGhGuf5trIcuYCBAGPX2TUAIFzNrtQaGFo2G8IEcUKfozJhl182P46Blb81OVqQP9B7V2YhGi70QIxTwtu705%2BF%2BZANZQuW3QrXxhe5vS9CQC0EA83uE0h%2BIR%2FOMCFmAfln5XNLKUivS%2FK8s3lAVxxe2i95STZmw8AxtH1HbNoVVeM3QR5%2FTuWNOxh15apEcn62T5Ca9ETw8QmF5UpN8m0ivI9vhut5p6ABUi4znDntYrwjaJ9GySetEcOqCjrZ1Hys%2Bvzwwssj4vAY6pgH4r82CnORo56lupY0xm4NgKJcgApYI1k2CgiUsVh61qkQUu8rOtGY%2Bl0jLZlDmcZjemX2UWVJNNpdGvRcNfipKlREQAMlU7w2%2Fg0xGrtnzPDub69gTMqi9l7cD9htnA%2F2pnB%2Bih8VSTEd2m%2B%2Fss9I3V%2FisY2j6SHH6mA7PmgGY8wpwwscGEc1CvH2udhG7731RPrGhKR98PrQMLbxv5rp83Ox2mRWU&X-Amz-Signature=ff12d453420a8a7ff9501de712d259e08963659fe929c8c9881e25fa1b90e797&X-Amz-SignedHeaders=host&x-id=GetObject)
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
