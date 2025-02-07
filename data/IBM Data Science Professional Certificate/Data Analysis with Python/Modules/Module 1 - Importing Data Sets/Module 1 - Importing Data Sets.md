

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBJ2CKMB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFblTe2iGTybHh%2BcVJX1UlPCc22MpcS5kfQL1eUbdnpFAiBf0LHlybW%2BlgyYaScJYosksf9GtuxpSNh%2FuZScbgXHNSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMKW%2FE0eMstISJLJdlKtwD8WUz9LlJ8zEuJi522L6atlHJUFeMuyXiJV3tQ8B6boeZ3EODT%2FMtkpf9QoP6j3gtHgiIDpEnnKJnSWWAIHq961RXJpClwMGlCUJLXeY08FqUZ39B%2FUiMjzpK8ZJYqSt5MNOF8F5wOF8F3Q4gUy01jBnZIAMbbjRgPQynIhev3yOzWOPhIPb6APUoBShJOUnjgSlAfRMJFA13KP33f4xs51fDH1XbAwtRvN%2BM%2FU7g1DBMNl%2BnSjVNjHQyQm4C38PXIkm6za2Iv4s3jpSJ6wxUQSl9XqRsa9TjikDct67%2BH0aPgS6kqVr2SXYFnsR3BAnMu4yWXzkTJZGg3AxvW6Mwmzez8MQiSOzDAI3jC2ainku0nCups5WH1eJ04XjxPF9J17HoIsWLGst1zzxlUtyIL9rCqufKKm%2FQ2Kvz75QiWf4ntTg%2FxH288LKXuqUxEhbY%2BpS4%2F8Nj1yAEXnMHIcESiho0UJ9jRWAMrV76QosenrTkD9awobCMQJ6vpMltgRH%2Bax2GBGzmXr%2F9CgK%2FCr1jfvXps2sx6iRnE%2BH2397fcCkRPKEL2etvI5xgf7q4Ye69Xq8cUsx2c5JHinQmx9G0eG7dVrg8daxYrRX5AnfN2sVvS3raighrOOPlETUwqouYvQY6pgGsAPHnzEeWlweoStWgSFyfIKjvWoYjyWsNdLT%2BkN1EwYiTd%2B7Bh%2Fa6G9zMcFamfpJKejIW8VTYW%2F7kftpjbmnoVgPkIlqKO%2Fr%2Bo6TZdsFXp8to%2F31OxOIQB6MyQQgap%2FiT%2FRysZ8Tigqat8P84H6x0V1dveuSnjTG49nj%2BDPSSZxdA1XA%2BaxGVt%2B2yzZyO8aRt67Rtmk1qqrUnMlgIBbCCHYrfOOCD&X-Amz-Signature=d71b5def13edc39056e65ef8a4597e9c44392915cabee733e700604684448a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635ALIV2Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGxqI9SRSI95GIM7hS7qrCPW3PXifkX%2F5HHEHaXd%2FTmSAiEA9iolNWm77Tl%2BetbVjMdGcQt0KxcQMykivj9Lcui%2FXr8q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDFviiuda%2FQAFW4Ba5yrcA1ZSmhL1cd59AW8uquF36olEz3d%2BEfIq5Bbqj36MeAHVxeMAJH9Y6iS1sAEFJCyEEI5ZXJfenndZaOpXy45tgowhwdMQojIiOvMkMY01Sa9r2bmGn14Lr4XQS8jH5BLWo4k6WJFKPu837ZPZMTzsL4td7pU%2B2q69vvY3NY%2F%2F14P6ufUiDbu2A8iFmaoxOI4ZqlTHbbdVshsAm4g4XHF34ou0zxlVl1ipFyKhAsw7R871ESlH0WD1eiaFppQQ7vpi547Yb%2Fc1XAXR4qAJX2%2BbnkTh3PcHHy6xW2hH03ezMcvUXD72acL0BQJ3awLJGOruQ4B03U7XvVSB4AzyTMzKLhctx0ZWlkBUqdFzmshHFabEB6hDtzmr%2BpzxjBRchZESiMTc9fx2DmHS1S4RFzcJyRNavV3%2FT2SzKMzSlq1%2Bzs3%2BDJzPk3w0T8dd3EBvqbEpN%2FE3FqLEs1YxwCs1s1U30OCCvf9Sm6%2FO%2BDeMxzS2Ig0Gr6HHhsFnAJH0GKSbeJyWY9PNBRFioEDBbWE68OUHE%2F42tJlvcMYShiHjTOjbi5XSFVMYcQlEO%2F5eCjhbMOZGMHwzBYFhYjHkEIMfilZw07e5PJGiCXC9po5BsAuDzdlSnjD5dvBTyUX36bUtMIOLmL0GOqUByyc7mTzkfLwPc%2BKUZhLhhXXAeKMmG1O8UJS%2FNhwAxaKih6Ay4Z1CkC49fn6DRufKaEcS6Qr07iPmCQ26rzPYn29Sq0p%2BguoB%2B7oIPaaMQF5bIam4Qez%2F8fyoGKLYArHkZ6KNwuWOllp%2B0eeLXdNHIdz26bxZhrcyehjjz3jl7Ss9ZANI4g3OQzis56AOiTQ74x6azlPPWjeuz6aiEeNfgfc8%2FJk2&X-Amz-Signature=0afe2b9ebbd1bc00572dbbb7ddb2e1d0e6a67e7e9f9a631d9dca06a6d79b67e0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635ALIV2Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGxqI9SRSI95GIM7hS7qrCPW3PXifkX%2F5HHEHaXd%2FTmSAiEA9iolNWm77Tl%2BetbVjMdGcQt0KxcQMykivj9Lcui%2FXr8q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDFviiuda%2FQAFW4Ba5yrcA1ZSmhL1cd59AW8uquF36olEz3d%2BEfIq5Bbqj36MeAHVxeMAJH9Y6iS1sAEFJCyEEI5ZXJfenndZaOpXy45tgowhwdMQojIiOvMkMY01Sa9r2bmGn14Lr4XQS8jH5BLWo4k6WJFKPu837ZPZMTzsL4td7pU%2B2q69vvY3NY%2F%2F14P6ufUiDbu2A8iFmaoxOI4ZqlTHbbdVshsAm4g4XHF34ou0zxlVl1ipFyKhAsw7R871ESlH0WD1eiaFppQQ7vpi547Yb%2Fc1XAXR4qAJX2%2BbnkTh3PcHHy6xW2hH03ezMcvUXD72acL0BQJ3awLJGOruQ4B03U7XvVSB4AzyTMzKLhctx0ZWlkBUqdFzmshHFabEB6hDtzmr%2BpzxjBRchZESiMTc9fx2DmHS1S4RFzcJyRNavV3%2FT2SzKMzSlq1%2Bzs3%2BDJzPk3w0T8dd3EBvqbEpN%2FE3FqLEs1YxwCs1s1U30OCCvf9Sm6%2FO%2BDeMxzS2Ig0Gr6HHhsFnAJH0GKSbeJyWY9PNBRFioEDBbWE68OUHE%2F42tJlvcMYShiHjTOjbi5XSFVMYcQlEO%2F5eCjhbMOZGMHwzBYFhYjHkEIMfilZw07e5PJGiCXC9po5BsAuDzdlSnjD5dvBTyUX36bUtMIOLmL0GOqUByyc7mTzkfLwPc%2BKUZhLhhXXAeKMmG1O8UJS%2FNhwAxaKih6Ay4Z1CkC49fn6DRufKaEcS6Qr07iPmCQ26rzPYn29Sq0p%2BguoB%2B7oIPaaMQF5bIam4Qez%2F8fyoGKLYArHkZ6KNwuWOllp%2B0eeLXdNHIdz26bxZhrcyehjjz3jl7Ss9ZANI4g3OQzis56AOiTQ74x6azlPPWjeuz6aiEeNfgfc8%2FJk2&X-Amz-Signature=d240adda6c2fff641b3f6ac579be48085fb84bbcfbefe7f9666a5de1dad64e6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
