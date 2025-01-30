

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYZNIH4D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEW8STVpdx%2FPqMc8Ix9UO7jAL25ZAfnDPdeHMGmie5aQAiAJnQWSacUKC4jSTN6raBUsEp057QSJV2RFllNSQdsTayqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FxaqeISULoMXhH%2B2KtwDtXrYZh0fu0QE50OLNQz%2FJ1zX9uKu1N1zHOVZfr7CFvCpQNMC3xKhaSAIkLUBMuZQoOeZIt1oXbY423oYQpnejcktcolQQRARbVxH96uL38G3GziYGZSqBiSDs4ob5m%2FOEEpRwlGOdK2kHwE0tTwKKCJUVs958Zo%2FgPreFBD8Wcd7UxBF8f251t8Ya6r%2F43vmCUdPERRie3oahm%2BO1%2BvntPJCbyviiyGS2CQoqM6wwO06L9nnREbq3inUODkpUQ4WCQhYZIaVFcGmXwPUijGpuf63CzZektbVcrHUdx4LVEmfExihpG4TqDqKcknWbo0XeSdRmZD2ivaiPnNz9xJcgmUWtInQZrKS1aNfyvD3ovU7sorgIdu27LgK4Fl7XqSos2MTvNwW2Qipo%2BsfjrHmUwe1QtDaEZgIvp6bbv%2BIJHX7VtmHo1PjiTnu222XbBD4wGCQ4eMtUdYEyrxt%2B%2F%2BgXHaKmJmA3kVNyesnSsi2jd4KMAe5B2RPNn12lOb9%2FwougKVYexIquNloNmiiXLyRyI%2BHjrv2qcqph92gPDy5DJCRJO6TdrQDVLyTg6NTEMhQJfdys1TdCsohBg5xS6VHkcw1YnxM25dh%2BPq0BZFmfPkdGBDDRjRhLUOXvzMwzOvsvAY6pgEHUYcq%2BUdMEXxroIB6Pp4iSNr3%2BEOwTkIbNlQYfYbs5XgXCd7rWoaR8H7saqnssJcd0oHm8b3YYKOIgYnMiVR82tY6eAsuJvsLhhcaSogkBkvib%2FnSRuoIBDYEoGkmFXbQdEqRMR5qhLpUORyUWNTWiGGVDtPv%2BTbgkK%2FTwD6GUxs21dFBE0lNgYda0RDJuf1%2FTRpnib4%2BjsX9%2Fz0a7zpgfZdhLyxj&X-Amz-Signature=3b383311826e9facef3cea2cec1bfb9d22bc5e4cc5933ed4644279097d5679a2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL72F72X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEnIxyvPop0HkMv%2BsWp2e78VLrZHWlAVScvE81HaOkpyAiEA3i5I1sFcoMjqaTn50tExe0l2N%2BqOfVZ09NQObcmL4msqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNUW1bZwW3gvl6l7CrcA%2BOldQwmGCfVddNKvpeAM5RRi8GZfO7dmBZYsrR2E%2Bvtezc%2FmMdEMRu6Y3AcSkFW6SQa2e9Hs2Xe86hFBM7hP6Esmb6vj50N%2BcAUy4pmbVpJc9byzs0iDnv3ib4%2BDjdTv22kacLsd1R1LawcvTB9ZC4oAX5a8WRHhdwp%2FA%2Biu4sVXlBgxnga2bB3k3XFo4Ujw0M0LuCQHONsj4Up%2FXBBo6KeLjy7vsNI8pPlRc%2BNunsitncMkehPk9oFfL6KQ2qXMyZvt4EiADBMznZegXWpFtHWqIhcC8EbFxy%2BRaI5txK%2B2tLLlpO1Zopjpz81azsInGkTaT717wropCiohkM%2FOcdG9MX2TL%2FPjKfDDCdos3XyQfiQkD54i4JLrPhcJ2yAKaE%2BGdM88R7bdPXpjjAgvDKv6MgHd0bYBpp%2B8veEvTjDIDy6BetY0f%2BoYi%2FLxSICBCYw9n69T%2BYI%2BaEqM0%2BfrDZq%2BcOh52MdnSKzbK8xxxpXHLdR6F1R3jWb4SCa6ypMBYwYAozUYRLdbFWGT4177coC8KLtgDAsF6nZ2QJcyNFrIe%2FKwh%2BRHA9rQPl7dJ47LAtVsQE4X75qaEuj%2F%2BMvmT8oCsUMidc4Qghjif3sJFYBmEEhfBnUvi%2B9F3ZsMIbr7LwGOqUB6uFcXFR2MbsT%2FBpdhE1copoOzw1nRzrh7E0D1fetPn5R3O7qirPfK%2FWwDvazIR%2Fj5Mkpof4xzn9zlQBWpTni1ZAJnYsZBk%2B4TG3QExgMnADBEGklKrQWktJVGvj6DAmQgwxhZ55HpLFMZiGXb5PobIsnT96ZNuOEWgY5OPqBhc3Ans9Wix0sd3boVqQ3Du6GYPT0LbeFjKVIDaZxGovRzKqVaRmX&X-Amz-Signature=cdef68a35e55475b31f2a78d71e6ce9147a4e6d2ec987bfb47a1c3598666d316&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL72F72X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEnIxyvPop0HkMv%2BsWp2e78VLrZHWlAVScvE81HaOkpyAiEA3i5I1sFcoMjqaTn50tExe0l2N%2BqOfVZ09NQObcmL4msqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNUW1bZwW3gvl6l7CrcA%2BOldQwmGCfVddNKvpeAM5RRi8GZfO7dmBZYsrR2E%2Bvtezc%2FmMdEMRu6Y3AcSkFW6SQa2e9Hs2Xe86hFBM7hP6Esmb6vj50N%2BcAUy4pmbVpJc9byzs0iDnv3ib4%2BDjdTv22kacLsd1R1LawcvTB9ZC4oAX5a8WRHhdwp%2FA%2Biu4sVXlBgxnga2bB3k3XFo4Ujw0M0LuCQHONsj4Up%2FXBBo6KeLjy7vsNI8pPlRc%2BNunsitncMkehPk9oFfL6KQ2qXMyZvt4EiADBMznZegXWpFtHWqIhcC8EbFxy%2BRaI5txK%2B2tLLlpO1Zopjpz81azsInGkTaT717wropCiohkM%2FOcdG9MX2TL%2FPjKfDDCdos3XyQfiQkD54i4JLrPhcJ2yAKaE%2BGdM88R7bdPXpjjAgvDKv6MgHd0bYBpp%2B8veEvTjDIDy6BetY0f%2BoYi%2FLxSICBCYw9n69T%2BYI%2BaEqM0%2BfrDZq%2BcOh52MdnSKzbK8xxxpXHLdR6F1R3jWb4SCa6ypMBYwYAozUYRLdbFWGT4177coC8KLtgDAsF6nZ2QJcyNFrIe%2FKwh%2BRHA9rQPl7dJ47LAtVsQE4X75qaEuj%2F%2BMvmT8oCsUMidc4Qghjif3sJFYBmEEhfBnUvi%2B9F3ZsMIbr7LwGOqUB6uFcXFR2MbsT%2FBpdhE1copoOzw1nRzrh7E0D1fetPn5R3O7qirPfK%2FWwDvazIR%2Fj5Mkpof4xzn9zlQBWpTni1ZAJnYsZBk%2B4TG3QExgMnADBEGklKrQWktJVGvj6DAmQgwxhZ55HpLFMZiGXb5PobIsnT96ZNuOEWgY5OPqBhc3Ans9Wix0sd3boVqQ3Du6GYPT0LbeFjKVIDaZxGovRzKqVaRmX&X-Amz-Signature=7b911d3f7eb43ad97c53140bb58bbd8f383b61e1f91ec862c7b3326aff36c5f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
