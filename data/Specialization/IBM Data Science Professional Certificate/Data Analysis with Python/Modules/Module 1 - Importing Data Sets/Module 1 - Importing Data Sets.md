

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K6ENX4T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCAOtqzylVJWWW1tH6orjH0H6mgYd3R7H%2FUxVFRBV4X6gIhAOiQ5T4tiCeDclJ9XvGkZDBFlJZ13T6Y1YCqXqgses0eKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwIW70j%2BNxoZU3JSwq3AMQW5Lrd9AfSjQRqQn4vl7YdwRbaNTyOaUVAhdYWepx52shQbYicObSAOW%2Fa6Wr%2BRLQvhWEqWEQgPaeIh2LqbeQhs4Jtx4k4wJRo5mJLtZNurKuzGyosoTFX592z2xNmJzKTTIDRYSpPM9pJKckT%2BaEy3RFVXjMoPIU4MgQra8xS%2B61aY2eMbYqpjDGZ7IkhySmydnAkE3gWdk8r%2BE3pBYdYbZKL0osYTKhQJklNmsHvaGHelP3N5WS43aO1aoK0rwoXKvQ0lnP1Uo6VrdLsp4YBr5gItWJ2C8Q20p1J8sxQEKWuzO4xv7GRvRwMygfJUv1%2BphsVNsNVvgCaM0FTjs8ckTeWIOReXEGryta1ozXL2sYx97bp6MDJZYBnk5iqMa1BGgfQEE0Qm%2FEtAQMF5Mzs54hcFdnzHyoyJGu1SOWn%2FV%2FPIqgj2vcOWWYdVblR%2FFm1XA0q2cnuTZw8DOCOXHtftX4tLRXwlOoHwtjI2Ufp6m5heMOpVazASg%2BnTEFeUdlo7EZXbs2SlSsemF3zPGIdTtfhuTXPFMU65laTzheWIy82hjlSuc7Z4ql2%2FGbg8iZ1k9cooJZf%2F7A1L6j4ItbBslNman0RxWCy7rtNZyd1xuBr0uwKP7UN5rw9zD6uua8BjqkARq%2Bg2cFSL0aKo%2BUxERUIBrm0PemZVbpUlE%2BcSGPLNc%2FXHU0Z0ldVQqvhlqY9FMtBva1P%2BodltERJY%2BzAIzWrNJ4W9vEBzn5epaTHGG8fDWb8d8JWKULWf%2BQZ3FIfkFcvIA9LKbJevKkSdwCTekVmSVzTW45t82Ze8aAMB%2BnXorzw23IoliUPushkDbIaTvJ8msQLCliEGWnWP9M2zOpC0Rc%2B39y&X-Amz-Signature=70ea2199a680be573f9d400d6aed597e24a4758c3f94d619fb698125f76d2459&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAEEGDJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGeUm5zzcZdES6CR%2FIwjMBvesY%2FCwBb0GR7M5NpntkFbAiBaCm6DGZ3h3pm7Dp7usP7%2BkVGocYcNHHFy2ybw5tFHfSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuhzpXc5llxiqfGtPKtwDUyQqwCSSn6mgkgbdjWOmefCdLfS6AEP7N7lqGl2%2B82TVy3%2FwuiDauGDG4bI1CHXawMl4E8gFgpNBd%2Fbilk%2BYYqA6AgBOvrMcS5QJkbeWvxc%2BcIz6AEncVtLTUuZ%2BMqodzcQDYEbX4i%2F%2FpqnFcRL%2BO9zyX%2BBRkACttnAtTEImeihvpUs7k35uOEOXBF2T8E5I1Jr%2Bbb57yV48vobCeHtLUEnoroY53GDauCihwKJkto6RjLEuIEnAFhNSmwbCpnizNB7MNrx7jqmp8kjeaPTomR4YFWp8T9V6mCDMbnQkzG4Q41vyOdv2XT8BPb3qQAP70rqUIdvree9CDNekfFZ950pErjGiBtxcVYMcYcwoQjJpnHuqnbs0qS0aTMAF5qeK4w6vVY3TQfbCL0b%2BWH1KZfD5oA9HxqHFyCMaVehmsQC%2FweUhlhW4NR6P5%2B%2B5tHzofrj%2FZSmXKXlimrquXUPKlRjw5do%2B0EHikJ7SWmBN%2BceNU7O57qEMrrW4XNCfMie2%2F6otuuNr4OCPtBXTUym1aVqi%2Br1fuEIbaVa7N9QdGSVKNhb0RJCqYei0JJx1JKZOJE7zbrX8fIGscdiGgiAqB1tfZumGYf9%2BJRQS8VESaFhgoXbBdUw1A7XpAzYw%2FLrmvAY6pgH48H1K3QcNx7W2oEIzAI%2BZp5Bv76RI1C6WK%2BXcjNkdSZ4TOpiCciBzNTn1mUv7mERaLPBewY689cKz%2Bj634s7fCsCowMSQt6fYAFFT7gsPLL5zwg5LaeJEvrOyZHE5%2Fo0cJWOyD9Ky13mprwm28drdTfeMTHTmaNv4HaNEu2SN84Gir3lgkVb1kCK517A6vIyQTLWpLHCGU3giGujrymzM3wQFbK3f&X-Amz-Signature=88f974a6ab3dfdc547750178aed05dd6a88752364a1674ff43dca69a3b80336b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKAEEGDJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGeUm5zzcZdES6CR%2FIwjMBvesY%2FCwBb0GR7M5NpntkFbAiBaCm6DGZ3h3pm7Dp7usP7%2BkVGocYcNHHFy2ybw5tFHfSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuhzpXc5llxiqfGtPKtwDUyQqwCSSn6mgkgbdjWOmefCdLfS6AEP7N7lqGl2%2B82TVy3%2FwuiDauGDG4bI1CHXawMl4E8gFgpNBd%2Fbilk%2BYYqA6AgBOvrMcS5QJkbeWvxc%2BcIz6AEncVtLTUuZ%2BMqodzcQDYEbX4i%2F%2FpqnFcRL%2BO9zyX%2BBRkACttnAtTEImeihvpUs7k35uOEOXBF2T8E5I1Jr%2Bbb57yV48vobCeHtLUEnoroY53GDauCihwKJkto6RjLEuIEnAFhNSmwbCpnizNB7MNrx7jqmp8kjeaPTomR4YFWp8T9V6mCDMbnQkzG4Q41vyOdv2XT8BPb3qQAP70rqUIdvree9CDNekfFZ950pErjGiBtxcVYMcYcwoQjJpnHuqnbs0qS0aTMAF5qeK4w6vVY3TQfbCL0b%2BWH1KZfD5oA9HxqHFyCMaVehmsQC%2FweUhlhW4NR6P5%2B%2B5tHzofrj%2FZSmXKXlimrquXUPKlRjw5do%2B0EHikJ7SWmBN%2BceNU7O57qEMrrW4XNCfMie2%2F6otuuNr4OCPtBXTUym1aVqi%2Br1fuEIbaVa7N9QdGSVKNhb0RJCqYei0JJx1JKZOJE7zbrX8fIGscdiGgiAqB1tfZumGYf9%2BJRQS8VESaFhgoXbBdUw1A7XpAzYw%2FLrmvAY6pgH48H1K3QcNx7W2oEIzAI%2BZp5Bv76RI1C6WK%2BXcjNkdSZ4TOpiCciBzNTn1mUv7mERaLPBewY689cKz%2Bj634s7fCsCowMSQt6fYAFFT7gsPLL5zwg5LaeJEvrOyZHE5%2Fo0cJWOyD9Ky13mprwm28drdTfeMTHTmaNv4HaNEu2SN84Gir3lgkVb1kCK517A6vIyQTLWpLHCGU3giGujrymzM3wQFbK3f&X-Amz-Signature=5338bda17a37f1ea4c56731287bf59dfd31bfc5fe7f487903b7d333024037893&X-Amz-SignedHeaders=host&x-id=GetObject)
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
