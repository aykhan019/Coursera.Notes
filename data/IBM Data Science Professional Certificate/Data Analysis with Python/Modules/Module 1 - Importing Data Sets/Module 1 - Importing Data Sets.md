

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWXZEVGP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1Dhy%2FVOPgpPHcFkyknvGTTGplogL%2Bp7seezejjFzFoAIgcWhvLtsvcAcApeAiE%2BXYi9Fi27oLVqNogt1zlxXdjB8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEfayT8w2M1c7yRM3yrcA98g71BspLYW7voQaenoqxyimEUMfaFGgiALMGaBUNeHyuaANk5SLoR1exzlwHDlNy4HuYMPlus4I9UnxiY548GxaYotJaiFySKT5lTxNtVREbbUU%2FUCgKBORgPeS1xp%2Bn0250aDNXpPZCZ9CHlCb659wdMQreWXceOWlIU9G8Hvb69nW%2FJc2fjjfo5qbPhcJhc18eFLozO084y7IoJebzxcXcL88YwJWNyIvs2t2USaNznWcensRjhA2%2Fl4GxbO2kJ3rg6fbz2%2FDLM7KEaFgDEFcayJPFFLr4c6Vw9hAJ9JyKmbYoDwbNgLWIl5M2rwE3qZ5vkl29fLSe7ulzSxgU%2BqInVrEb%2Be9uT8en7QbN3hBSkdyj8FhOpMQKJz747ZPoXRqTjSTn609KYG2ce8C437kTCzEdGd3HQf%2F8J7PFtM3EKn5f9csGIHyGubbAN%2BXKtb9cncPTd8n53VygvVSqIbDnk%2FMtBlavC1J%2BSU3b1blxzC7tScDAHSYmgq6XS%2BPOkufiaUkG0LOPehzJuZRkV5S1RVBWpm6Soiqwf%2BCJiXKPdSEvQEXKk5vStXT4iJjvsoDGTBPhHlwVMvj8BV0CsWPQoXIcUzxj9iegsH%2FgDXhdxNd7ArtFZOvMzyMPHygb0GOqUBXNVMz9CzeN9zvVeDf883OHLUkVvcDeGRg9iTX82oGnO8LDWSaNUAlBM%2BpyhbMDqypZCk1aBEjPUCFvke2Hrxh7SX92l6t83bvHsQe52YT7R6mVKT9g7n3BW0c40o4zfqFnJ%2BL1sm5upXF8RqLDhpfd6UgKzzB9kBG4XYE4pe7Pwzy33ENOdR%2FO9xeWCu%2BIgj8UYMWTAFWHj3pZkJDjgCc5qFN8Bh&X-Amz-Signature=03bbdcfd8fc8091cbf717f32b2061df1276b08004f636184a719ab8b4281da34&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR2GF4VI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCy1lQOz9AHV3n84%2B5Rc%2BHg8k6dfEVCbdphVUIBefwhZwIhANtb7ziUTWv5sVdpUrq4aWgiVUHiolk%2BqA%2BqjUMJ5PQcKv8DCBEQABoMNjM3NDIzMTgzODA1IgzYygek%2BFgKa4Vk5%2B4q3ANhLRzDcEAOEFbH58jnYLMVj37IeV4RElEfL5836GwMEvn3rKgIQaeK9p2JM4FTXjRLADDIMwydY8Il5OMbHxh4D9shsgd38JzxKoXvKkBsDN89Bp4Ruho%2FDoQ2K21Z0XEvCMh0MPyh%2FYFqwDrA1%2B35LEvWCOSrJc%2BCiO7Rax0lan%2FkOgMn4pqvQ8KRw%2BUXJrUPqKLA72C2J9ILZkQTEs4Bz3eyKOAMu3i7z0H9lLgPuBN2PF%2BsbZBrGGo%2F03nLwuAy%2BiRwgQN6I3BwG%2FBf0PVqwVfZlmIX%2FPUZgZ1cGsvL10YZonNjc8qdyEJti%2FAcYoypFrEnPTebJ10%2BNbFq4FNzAHbETpu9zxl49UVzmXAAxyHkY0imDHZzHPe%2BpmZ%2FsINrKWugfj6TfObrEAol3XnjQ2OPEghqIsYVl%2FIGh84estOWNiw5s49Ex1h4bBM8s32Qwi%2BmTfAB%2BmQHhAx6F9Spr06VeqwyYVQdpPxbQmlPOvaih1YRCknqZgChMzqb6pdCEN%2BPR6Xy8xFOU2nnqgdPElQDc9juk6G5vH14ZfUzTyheB0Uynlew4hgyfVkj1OnuIrkyBXq%2BTtPC0eaz7D4G166MzuZxbiV%2Bu2TBD8gCtQce4hOHLLDjUHN2gDCG84G9BjqkAW55M%2FCbfWcS8wWYM454jOT1VjQDJBtnT6uXCaQ7rj3Wzc%2FQSXWYMVw%2FZlzeDJXd5dbYyrqQPh4M10zw6%2F3%2FEYB9i6%2BCbLYs%2BHW%2FW1geBKbv0lZ8fkF2KhbvjvuKRJdykkBiT4ymNW4hlVEZTQiUtNv%2F0iWAleiMkicbPoAPziSbbU33GPdaRvEkjFXrbUs6zSNqv%2BNfMDqOtH5MtE75WqX85DU%2F&X-Amz-Signature=b0353279b288bce68e22e5a50f74cb0d5a3c6a878fa3b65fbace7b8f66b986a9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR2GF4VI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCy1lQOz9AHV3n84%2B5Rc%2BHg8k6dfEVCbdphVUIBefwhZwIhANtb7ziUTWv5sVdpUrq4aWgiVUHiolk%2BqA%2BqjUMJ5PQcKv8DCBEQABoMNjM3NDIzMTgzODA1IgzYygek%2BFgKa4Vk5%2B4q3ANhLRzDcEAOEFbH58jnYLMVj37IeV4RElEfL5836GwMEvn3rKgIQaeK9p2JM4FTXjRLADDIMwydY8Il5OMbHxh4D9shsgd38JzxKoXvKkBsDN89Bp4Ruho%2FDoQ2K21Z0XEvCMh0MPyh%2FYFqwDrA1%2B35LEvWCOSrJc%2BCiO7Rax0lan%2FkOgMn4pqvQ8KRw%2BUXJrUPqKLA72C2J9ILZkQTEs4Bz3eyKOAMu3i7z0H9lLgPuBN2PF%2BsbZBrGGo%2F03nLwuAy%2BiRwgQN6I3BwG%2FBf0PVqwVfZlmIX%2FPUZgZ1cGsvL10YZonNjc8qdyEJti%2FAcYoypFrEnPTebJ10%2BNbFq4FNzAHbETpu9zxl49UVzmXAAxyHkY0imDHZzHPe%2BpmZ%2FsINrKWugfj6TfObrEAol3XnjQ2OPEghqIsYVl%2FIGh84estOWNiw5s49Ex1h4bBM8s32Qwi%2BmTfAB%2BmQHhAx6F9Spr06VeqwyYVQdpPxbQmlPOvaih1YRCknqZgChMzqb6pdCEN%2BPR6Xy8xFOU2nnqgdPElQDc9juk6G5vH14ZfUzTyheB0Uynlew4hgyfVkj1OnuIrkyBXq%2BTtPC0eaz7D4G166MzuZxbiV%2Bu2TBD8gCtQce4hOHLLDjUHN2gDCG84G9BjqkAW55M%2FCbfWcS8wWYM454jOT1VjQDJBtnT6uXCaQ7rj3Wzc%2FQSXWYMVw%2FZlzeDJXd5dbYyrqQPh4M10zw6%2F3%2FEYB9i6%2BCbLYs%2BHW%2FW1geBKbv0lZ8fkF2KhbvjvuKRJdykkBiT4ymNW4hlVEZTQiUtNv%2F0iWAleiMkicbPoAPziSbbU33GPdaRvEkjFXrbUs6zSNqv%2BNfMDqOtH5MtE75WqX85DU%2F&X-Amz-Signature=c7520a9d9f94f87d19ed83083b915edd354a5cbf9670dc5b02227904882926d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
