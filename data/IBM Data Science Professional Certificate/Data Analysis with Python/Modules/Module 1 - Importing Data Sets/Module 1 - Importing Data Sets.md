

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZA33PQ5X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANhD6awpK%2BdxsVvi2KorJqx7oClF%2FiXMyuVuCruksQeAiEAiDwAx7r3Fhl4MzAEFKXzO1uWwFn5M0tpS0WGXf0DcOYqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBCVmTyXbhs0iqkzqCrcAyNw0RGlW%2Bxu7M8lnsfZTyljZEIzidIHRx4otKdIGPPKh5y4%2BhAyQEaQ1raav0SyRlef3iqVdD5hGwB0PKhOELqx9zc6fZLAMFGWdZqu8VdLW%2FHe27%2FaCw%2Br1Bgw13osd4aM4BFOLAw0LA4UFiVG74nneFdt92qWmztlx6YFcLlFwURFXSxdC65PZr7DhDEvpr%2Fa%2FgrcL8w5bWoHih45uGnOKV%2B3hp6wtLR98ja4vTJGQz52JlgY7umWyG3ObzRXD26%2Bj1GTctYaQzwG2fHqAzVurk7HvIdK93IpIUAAClNKcMvvVHBae0ZiQn1VC936msj9U5%2BDsQmPJenizJZvt0IrENKf2uuNljw7RwwATUnLylFP01GsH%2BKh4ohz5LP3XX%2B1xCjx6mYCHCt0qaGGEcB2vqRrSp3ZxgRJc8uwp2oaRimsE0N3RHQxi5%2BJuqigf03sUNKqttCzVRxV7irBzUdwrmh7YxzZ1rJvAWcDykBJi83t8PPaOpqf2iNFAL04TfOnAottmWEJPtS52Vlrfjtbj9YmTGWsIdDWgkWt4JD56cdvYuZVAad7R5IabNt8o36Ngo8A5Hc0YWUcKt2Hg%2FpbSs8r%2BM7yokwYBXz8qAGQ1YTWfM5RZrDj%2Bgj%2BMKes87wGOqUBWygsHnMC%2F9QsU3Uvl6QwuD179TyTrARL4FgSuDKDjH6MAdEXenUmtGUp1POTbY0q0zlXK%2FesKtYtYxw3Q5JOegW05VTEVV8Yp7U1SZJWsUIjjDqH5QgxcGLQ2%2BHgfhDPI38iail3%2BFuQsebpKYq4tYhZHBD42zSGhDTZlLTOFAV0ev18Ba00XrnZBXagENSKwMuXTZqxotXJv41fBSVm3PVigTQb&X-Amz-Signature=77f04ff2bdf8377d704af291698f51c39186c40aebbb35dfc11fc0d406084bb0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XZXSUNT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7GaQuM%2Bct9T0g5LPq8jcYs%2FWpl3MGeb5rt964a82jXAiAxolINTqJ277pjTgGUPwg4gk2MDcESBhJcZoIKrJr%2B3yqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcMvaN2ZDGTqRWfpKtwDUYyTn8YM2tWwVk0Qi61zbpx73pXMnOn98dk7LsghygH76sP02MudsfbCYfi3AbGRtodTe23mMojFNxhy%2FarehRDeOhvtg8KdPq3h6BeZT0hsZukrkt0kOac0WYGvq8QnSXqme3gixlk%2FxFDvMkJyRwc1MZuFYeJcljkvR0hcM5KeEwpDH7huoM%2BhoTn2SiYmuc52ByfbvsPOD3hTNfnwZGezHw4ygx5pWcwSRcdxoVViVzIgjCXIS2qRxOZ4OpL1tj6LeoiGQ8nUy5LaRUfYnLrozjkihYqPdgTRXEByHlPLBRpFCnkNr7vBdj%2FLuKuI3e5RjBRLc1zMGm9Mf%2FEHsVVhE3xD7scqAzdvs8OUy8zPkL2m4nPcAONrN8OYXNvtKDgHyOrnBOMqvwiGo3oBd9cNHALvhLigaHxPFMxPxQzTsDitV3Z0c8E037%2BL5ILbBmATmZH7kFJRQFuLyK55WG0J3ekdH3OLUemUecldZFuITMgET%2Bj%2BwtGZIZumX11zOH7g9%2Bf%2FytxI5LGTMNypoaiVr4iDdVhb9MNtmqHnZN8O91fFERnsOvWp6V4ggXOBy4nRa3RXXiXMv%2BJ5BA5Fd2DoWTFNdJ7%2Be0poI5DdXYhbq18IUc3M9%2FXYRdkwsKzzvAY6pgFaaRXk7crwaXIkpm0w%2BWUCsondg4LYFs9bAXhXnruM6aE%2FTJUvhBsyCHcrggqljLDiaXB3EkkpVjPKe04mj8%2BqKHJjfi60xm%2FKWLgkJV8n2o9PiwnLUr54doLh2hpYwZN8RNhAlPcRlaSbyfMWIyhWxxauTucM6oN8L9mleREt68HDhnyiJ8%2BJ2BZuiEQaZNmhojw1tDX8XRcMQWI0Wfk8pmOKy5Qz&X-Amz-Signature=700063b077e74ccb9ecb037c007b6332c7efc96498e2b69b0b4bdd1a73fddc32&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XZXSUNT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7GaQuM%2Bct9T0g5LPq8jcYs%2FWpl3MGeb5rt964a82jXAiAxolINTqJ277pjTgGUPwg4gk2MDcESBhJcZoIKrJr%2B3yqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcMvaN2ZDGTqRWfpKtwDUYyTn8YM2tWwVk0Qi61zbpx73pXMnOn98dk7LsghygH76sP02MudsfbCYfi3AbGRtodTe23mMojFNxhy%2FarehRDeOhvtg8KdPq3h6BeZT0hsZukrkt0kOac0WYGvq8QnSXqme3gixlk%2FxFDvMkJyRwc1MZuFYeJcljkvR0hcM5KeEwpDH7huoM%2BhoTn2SiYmuc52ByfbvsPOD3hTNfnwZGezHw4ygx5pWcwSRcdxoVViVzIgjCXIS2qRxOZ4OpL1tj6LeoiGQ8nUy5LaRUfYnLrozjkihYqPdgTRXEByHlPLBRpFCnkNr7vBdj%2FLuKuI3e5RjBRLc1zMGm9Mf%2FEHsVVhE3xD7scqAzdvs8OUy8zPkL2m4nPcAONrN8OYXNvtKDgHyOrnBOMqvwiGo3oBd9cNHALvhLigaHxPFMxPxQzTsDitV3Z0c8E037%2BL5ILbBmATmZH7kFJRQFuLyK55WG0J3ekdH3OLUemUecldZFuITMgET%2Bj%2BwtGZIZumX11zOH7g9%2Bf%2FytxI5LGTMNypoaiVr4iDdVhb9MNtmqHnZN8O91fFERnsOvWp6V4ggXOBy4nRa3RXXiXMv%2BJ5BA5Fd2DoWTFNdJ7%2Be0poI5DdXYhbq18IUc3M9%2FXYRdkwsKzzvAY6pgFaaRXk7crwaXIkpm0w%2BWUCsondg4LYFs9bAXhXnruM6aE%2FTJUvhBsyCHcrggqljLDiaXB3EkkpVjPKe04mj8%2BqKHJjfi60xm%2FKWLgkJV8n2o9PiwnLUr54doLh2hpYwZN8RNhAlPcRlaSbyfMWIyhWxxauTucM6oN8L9mleREt68HDhnyiJ8%2BJ2BZuiEQaZNmhojw1tDX8XRcMQWI0Wfk8pmOKy5Qz&X-Amz-Signature=c443d182737cf9293a0a0cf4b6dc8ff9276712f410e34f3c0296c595a4562853&X-Amz-SignedHeaders=host&x-id=GetObject)
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
