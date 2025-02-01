

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BL4VTOO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBGO%2BgzfST1pkFrAbOU1kFMovAz4aiarurGrM7APRU4VAiAmAF6imIQzGNF1YGHdOv7HkednBpkfAMLn8OMGv5QZviqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4CvJ2wq9HHSmnUjKKtwDnlrAXGqprjUWjx0etN8gEJnMkZ7RgkqKpgMBEiribMt1JS3grAtb%2BR0NS7oRA7sAk4mqmjsbFIMSAJswCUW%2F0yvFYPBcYNfqnPkjKBwcqgNlNpuf0U3OFkReu9pkcIe4d00VeRaU%2Fds5WueYJlHq7wb2qNtM%2F62Y%2FFqKVAwJJAFAlhEDHNdDpfhQNK4h%2BlgpT%2BTFbCwIGwQnBuNZjlLmI3P7LNSuMEqpXNjOEforMWnBiBUD4%2FkKGgkmpxVyPOq4iMA6re7sM8yQlIYari2iXt6tf0N7UGAJFSqEXBlWKi%2BIXNhe4vDRva%2FL%2BL2126OPb%2FIDkf8PslGCEMCEVCLwp9lFnAdjYJAv5A0sLhpciBoiFDRX%2FeOGx0d8dEVIzQQq22RztgBjDKObc6tnHyDPO3Ld%2B63x1dTdD6DbqpyeSounbyM2YeZNfn99ZNhkI11%2F37ozxr6LHvqNX2U1sjIZHbLfJlnj5OttOsjjhW11J%2FPaFsueBPSZjSy6ZexAb0MjEwLn6%2BNEb%2B35mt86729zfx%2FQiw301LZvBiSMBUf5%2BqPh9yELvxLRNGtvStJrQslFzwpAEZc5CprTctyd3cDHswyFPElRHljAFozJ6kdCdEI%2FSols5Fim%2Fv1vKm0wv6T3vAY6pgF%2Bw6qT%2FfkSob%2BOob1riZvCXRJqnKcv798DNRqkfqxJxlkEwKfA7xwkk1p8BqGmCufZ4U4IH97jMAXIrrjdqQM9OabZ2JoMI1Avup6tni2%2B%2BD%2F4cIZmWZkSUaF2KztiCXdn4tKYFIhU4ngy1CQzabP2%2FbJYfowngdvpDngHN3wXzcfeYVbK4ttpwvOZlOLxfQoenFuchJ2tGymgzzT%2BVQBMeS8xTlu8&X-Amz-Signature=4a113940322a3461db9608a7dc7dda53ec1e2cdf97422b39a2bf9dd517059f20&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RLJM4EV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG20KDqxEjXdJGG4AiCri%2FjLyDvhWP7m2prtwkGVdDwtAiAZpXX79H8Kfp4Bd%2FY%2BHngFXb40xswDSneQBhyb5D6pUiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaeIFnPBQxX8tko%2FmKtwDaIS5BJIo8poG0LqYsUv6ljVVMhK3G6FGF5SwXoc75qC6Szu%2BpF%2F0mYgWSeDVliWzWuogO0eFQfI%2BWtpxZmIUS9QpXirLotr17OZosc3aUm7OLHm%2FaIkK3x5NhBM86pD5zDpfeqEDpnjEnprZQ%2Bgkb5CSJfEIiYhExQG7qLoBPDeJ3KGJaBQDEWU93VwTp4bbUCBdRRpVdWGjyFh8wyhXglpj3VTpZ1GxaQHM%2BtxyN29lwU5yjdQaK%2FSvxD%2Bw9hzEbDwbJptyCrzE2esrRIE0Zref6Uj73hsquExgXWSr8jErSjMTB%2B5CJ6BPNBNfAikMbwCeZInp4Zy7uQH9X1szBh0kkSQhMZEmWwkBRIR5U3cfH%2FCHIcGbgCfnnvNuDeR0eZlhFMfxmcME8S%2FGehiPhu1ZRZgJeqcjS9QBiFMMZDIW5F5CTjrEdv%2FeMVZnY9Lz%2F8PW4koyyAiqRdryPI5uysUHSfyH30A2cZ7CbmUt%2FBBFkL58mJNAXQ0YOlmO6WpmmCPytzIog0Q%2BZP8pGCX%2BwvvUw7TIOR1JorHerK8E67fy%2FqBjEBN%2FAZadcdg%2FtuT8rCZDjop3Wg%2BB09R9WY6HQcCWyMYv23WOWP3RjHzdkBysNkN%2Fw9RPcM6ngqkwwKT3vAY6pgHa9oAtdzI44qYVuOzyLaO5W%2Fetb6%2F5wO3otnM9WtSokrYTFvr7S2B8bpIBXbL2o2Y5U7HjrMRIew2gx%2F6sfIfWdxEQb3aAun3k3bHtaRtvUa320%2BkZA%2F0oTK%2Fa8tB9qnxhlyaDIi%2FSJ%2Frsu%2FvTIFzr1VeV%2F04Rz0P4LIOLrjJGJ2mPjvGYroBqzHXGwBVwKmPkfYh%2BJEXCi8DS3diqlspc34aD4cvC&X-Amz-Signature=486c0217b28b7c5e500cc67143e64fb0f3014e30226000d55f3f7dac52466c22&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RLJM4EV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG20KDqxEjXdJGG4AiCri%2FjLyDvhWP7m2prtwkGVdDwtAiAZpXX79H8Kfp4Bd%2FY%2BHngFXb40xswDSneQBhyb5D6pUiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaeIFnPBQxX8tko%2FmKtwDaIS5BJIo8poG0LqYsUv6ljVVMhK3G6FGF5SwXoc75qC6Szu%2BpF%2F0mYgWSeDVliWzWuogO0eFQfI%2BWtpxZmIUS9QpXirLotr17OZosc3aUm7OLHm%2FaIkK3x5NhBM86pD5zDpfeqEDpnjEnprZQ%2Bgkb5CSJfEIiYhExQG7qLoBPDeJ3KGJaBQDEWU93VwTp4bbUCBdRRpVdWGjyFh8wyhXglpj3VTpZ1GxaQHM%2BtxyN29lwU5yjdQaK%2FSvxD%2Bw9hzEbDwbJptyCrzE2esrRIE0Zref6Uj73hsquExgXWSr8jErSjMTB%2B5CJ6BPNBNfAikMbwCeZInp4Zy7uQH9X1szBh0kkSQhMZEmWwkBRIR5U3cfH%2FCHIcGbgCfnnvNuDeR0eZlhFMfxmcME8S%2FGehiPhu1ZRZgJeqcjS9QBiFMMZDIW5F5CTjrEdv%2FeMVZnY9Lz%2F8PW4koyyAiqRdryPI5uysUHSfyH30A2cZ7CbmUt%2FBBFkL58mJNAXQ0YOlmO6WpmmCPytzIog0Q%2BZP8pGCX%2BwvvUw7TIOR1JorHerK8E67fy%2FqBjEBN%2FAZadcdg%2FtuT8rCZDjop3Wg%2BB09R9WY6HQcCWyMYv23WOWP3RjHzdkBysNkN%2Fw9RPcM6ngqkwwKT3vAY6pgHa9oAtdzI44qYVuOzyLaO5W%2Fetb6%2F5wO3otnM9WtSokrYTFvr7S2B8bpIBXbL2o2Y5U7HjrMRIew2gx%2F6sfIfWdxEQb3aAun3k3bHtaRtvUa320%2BkZA%2F0oTK%2Fa8tB9qnxhlyaDIi%2FSJ%2Frsu%2FvTIFzr1VeV%2F04Rz0P4LIOLrjJGJ2mPjvGYroBqzHXGwBVwKmPkfYh%2BJEXCi8DS3diqlspc34aD4cvC&X-Amz-Signature=924ec7f0a75464a1f7d0f85e91e25a80653631def7db56123ef018d480f7d4a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
