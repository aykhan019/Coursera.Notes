

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WXPFYOW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEz3UoPEHln1WZsOgXJpfmrqI7IYsqF8b8BMZ8krOKFQIgdJbgbJuO%2FKSKqEXOeiSaPgYFOLN%2BN6US1UiwVam%2BfdoqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKdOLt4BJA2MjjisxSrcA8leUBxvIaXIHXmhtWpJLpwLqWSVvHSgTgSwPo6LPFMMBKyF6SMs580E1U4IVihqcFoiEZxVL9f7aY7KSu0W2YzNiEtALbpr0fTUeP9o%2FSLZ51OjS%2B4Ociw2%2Bin9HNQkTYbmo8wzIydiTf%2BWDL48KaM6UkxSsMHfA2j9kd5z0jOSOQbpeCurE5ehDSG%2FzXapupPl3BZftWIzmcaFwdPvLXBaBghbVoMluq%2FUPic7x%2F5iFtakbE8O%2FQagJlWbIE71WadHejF9fohqinOtegr9%2BaZRiQPurDnTyaxExSRC2Uh7jEBiDzoXP1cieSyeBwITiy9tyrtbsRcKTjUqOMJmK1wJxEHz6LC6Cvr7ZRyI7bF3XX2dVbOpvCH%2FCjZn%2BqfF3Ll8cMJ52ZhXRoBFd5%2FDpuuWT0rgH4Wfsh%2Fo2i9RPg%2BSP7TSJ4I5tAZZziMpic3QuBegMHG%2FJ8MdV3%2BkY5QM6vb2Of4P66IbnrHGuEeOuTDCliM642BIPSqtTkBUfcn%2BrUDQVnqHmE0eVd2seDsDQ7N4%2Bx6tuJeuo2UHQJzDX0j7oEJgRQ02hhI9M950bYFIyI22qdgdBmkH09pX8HGRRF0r9motYorqaIBHLU%2FgsMC9MzK%2FLH4rqldvBekOMLPF6rwGOqUBIDWF16pMsoN0OAp2%2B2rHhqPR79XEqkD2ancVuMXwBwWPhKr4RIJSDUkloLIwN4A0AgrQBYqrEvRBS5jhK0sg9EI8udJGRMWLBf30yIGudWyIgf5y5wD46gCaayK5OzPRqx94%2FN%2Fyv3DBptqJNksxaxJYK1Mh724JaGBDkkaGCG5G2E5FATOHHtPPqqgmTscZNAW9JE6lZZbyvmWpJ7Gqq8Gzpj9F&X-Amz-Signature=86389af6c464fa0afe9aad7d4bb7d0f6f8d34eb03010f26ef6d0bbcab64bf4c0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2MJNSPF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDie5jOZVI5saUVD4CKQoPffv93exJtxCL7qEs%2B3MmI7wIgXlCd2QEsoxmpIm%2BX8yRnatxP%2BsUzUbwdhapmRFxWBpEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML1iYo%2F5rp5h1vTaSrcA3EjLLQDhzToedFhp3ZfIF3FhEE0pxwe%2F16zG%2Bb0aNN%2B7yqOHU%2Bk0oxt47q7E5OoTkeRDVFA%2BzZ2Ca5fGxCOzEw%2FGwej1ZXo4UudQNkm%2FDXKijzPlwYZCxxO2Wtd45fcKcMeSUcv53uXztBaABiFECds7xftWEwWVLXpZWXS6baN2kqOl0lCiMljDn7cZLG3QKoWwdosZt7BhovUi6mVq3kbxO3XzBFQiA1Lu6b5UOqVjfPrU%2BC7XHozGW4TprI0cAadu0zrGiEBMVUXyPcFc58OhGQ%2BCuPpZyt9d4lnPRqR9cdCDraGKCnj2DIZj3lOJJxR34cWqnz44Ao%2Fe33E0c6oR4zyVhnmrn6c8mwMPbe2vClS%2BMKNV0RrF65u6z1lgNaVghNlFOzjTriU%2FU52yjJlhow9Uh0jTGC0iuTvfwar9LJfYUlJ31Zns7BuBxXeb1YCnOzKX6GKpRj3wsQDB%2Fdm8SoIJX2BBC1oFUivz57dH%2B%2FTzDExjZf%2FNiI%2FYYe6t%2F7qOicP9Bm9HStpCTaIyZfqu2nx9u75PtFIbR6HQwfBdJUoccsJp3wJQ2svvN2tc7GFqtZ7j%2BJyDyWEqOdPxM5NHl02SPtDcNMtAnqbLrqbgRYYxM5gs9B%2Bw7YkMN3F6rwGOqUB%2F3aqQC5ORl7iFQapGCqZ5MIQ%2FUZWRarQwuEqT9FPrMGnLWQspp1pVx82820Gm7kTPfD6Fn7LBXseZ65erLNDiqH1NLfeV1xyjggPOXq8AJmNxFKnoxVQUnCw7fE432HiNK0BYSQeZNGNlVpz9eJJBZnNFkILxo8MMnBSt86YazA9EzWVNfGzFSDdO4nSR4d6HB3xSi%2Fk2MTobKGZu8SHwHvvj9Bw&X-Amz-Signature=9121793a9666e1d321e66efb0c210223730396f650e3f2473e5a052655bbe682&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2MJNSPF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDie5jOZVI5saUVD4CKQoPffv93exJtxCL7qEs%2B3MmI7wIgXlCd2QEsoxmpIm%2BX8yRnatxP%2BsUzUbwdhapmRFxWBpEqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML1iYo%2F5rp5h1vTaSrcA3EjLLQDhzToedFhp3ZfIF3FhEE0pxwe%2F16zG%2Bb0aNN%2B7yqOHU%2Bk0oxt47q7E5OoTkeRDVFA%2BzZ2Ca5fGxCOzEw%2FGwej1ZXo4UudQNkm%2FDXKijzPlwYZCxxO2Wtd45fcKcMeSUcv53uXztBaABiFECds7xftWEwWVLXpZWXS6baN2kqOl0lCiMljDn7cZLG3QKoWwdosZt7BhovUi6mVq3kbxO3XzBFQiA1Lu6b5UOqVjfPrU%2BC7XHozGW4TprI0cAadu0zrGiEBMVUXyPcFc58OhGQ%2BCuPpZyt9d4lnPRqR9cdCDraGKCnj2DIZj3lOJJxR34cWqnz44Ao%2Fe33E0c6oR4zyVhnmrn6c8mwMPbe2vClS%2BMKNV0RrF65u6z1lgNaVghNlFOzjTriU%2FU52yjJlhow9Uh0jTGC0iuTvfwar9LJfYUlJ31Zns7BuBxXeb1YCnOzKX6GKpRj3wsQDB%2Fdm8SoIJX2BBC1oFUivz57dH%2B%2FTzDExjZf%2FNiI%2FYYe6t%2F7qOicP9Bm9HStpCTaIyZfqu2nx9u75PtFIbR6HQwfBdJUoccsJp3wJQ2svvN2tc7GFqtZ7j%2BJyDyWEqOdPxM5NHl02SPtDcNMtAnqbLrqbgRYYxM5gs9B%2Bw7YkMN3F6rwGOqUB%2F3aqQC5ORl7iFQapGCqZ5MIQ%2FUZWRarQwuEqT9FPrMGnLWQspp1pVx82820Gm7kTPfD6Fn7LBXseZ65erLNDiqH1NLfeV1xyjggPOXq8AJmNxFKnoxVQUnCw7fE432HiNK0BYSQeZNGNlVpz9eJJBZnNFkILxo8MMnBSt86YazA9EzWVNfGzFSDdO4nSR4d6HB3xSi%2Fk2MTobKGZu8SHwHvvj9Bw&X-Amz-Signature=12ad8a21ff5797064eb954eec8bd322d8e28c0864da933d1f4538430cc8a522f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
