

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGFJ3RM6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEY9beMS8NE9ELe0VB%2FHWaRxkUwSiuyl5trvj%2Bb4tq9IAiEAnEElyISXyWkyxVVoZPMv8QhdX4D7um9Li1WRV8fB6r4qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLJsTrpttGLR50OqOyrcAwegaKstbO9tfkEo2MeB9xKzjnmBXuWKiNI6ZSwKhAhqZeo8vOwgkGHSFOYGbU37G6XFZjI2YjcOtI2Rz0IdBEfqSL2WXJ0eOMUDiQqL9TpVYUyH998GhdjegpfYta0vG8%2F%2Fyjc4i%2B%2Fzc6K99tszE8UlrlfYyw11xZ68jgwENivgAhN5nfeF32vI7PYupMpCBMNT4d5mAg902aY3D4LNremeOmWfVzwObAtLvhriCOkmyGMNREuco7PSZT%2FFuaC7p%2BJCNpVxNYPxdJgMe2Qa%2FY%2BkBfGDo6lHFDqPRRQyKborDfpog64LihF%2BXBxtcIZ7jCFY3ea5hwVTyzjMiIPqGkQ4c6KEUFYM7Aw7PRbubUx5g%2F7sUx4wyymVBKnmkllKhgznRGL3XW33Ix8xxlpkO2ZCAtGV%2B%2FFCkLQjcZMNL%2BjkiV3KgmUd8hVGcX%2BZucKsWEG3pL%2F9AiVNjc4JcklH8%2B2Iu0tao9pp4La8z5tJlGoxDPeJ0I0S%2F9oLT9FpX1Ic6wYrFCR5GrCvhkQL9T0lC80ovf6ahn26%2BlQWVry9t5ofYgv40dkrItUG%2FGdzJ2gv48tWn762bG4CxKkSipdmsERhsi%2FUm4aLyhCkjXh7kqAluZsLKqgCZ2%2BRzob%2BMOSj9LwGOqUBMRJIAxP00BCgt3gftl2QjLb7%2BLlE%2FfzFhWOLPMw9l1FUbH1h0ZjywbCbTWwsNUkhzsyB5dS4boXdAT1FpJEdgiBBbphcFzuLfeNz578CkC4DpquDVrvhx094UNntEHuIcOIDWteRhVgyXuhbQeruOhk%2Fp9ahiBRsgx%2BmuNtEnHuXWhmWujvsIp7H1Ryu2XAcSbOHw1McgLWdCbv96qiwihccSrJG&X-Amz-Signature=b1e8c6ece3e13dafb88465be26aab8d239dec21c8308ad59ee91bbc7d4fdf484&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWZ2N45F%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDT7PAez%2F0X4C3OSNfD0nxz61pCLTP2I94QFBd0pDWo2AiEAwEuzpgOUYr9pFTL0Bw5SHk5ztleFWMZoNtqWqm5FrUkqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSfYP1GA329fqhBFyrcA0QH9rHiFBBty%2Ffk4uQVMFjdiK70Q67K7%2BDyhUs6ksZG1eG6R8aspYgLX16fbJ4ks1POeoPgc4ZdLDQChrWasH2j3i3zTg1ukm5qlXhhpGzgZ71fgx9yg%2FDj048wdZ3aZgWxfGmJ7%2BR%2FDlIL0vKTM%2FLZGWx130x1QpNHuw6SzPkSv%2FaI%2Boq9CCxGGVlBMWySG1zhuQ%2BdQmdYvEzHUeembkmFMnbUTkMUyXyynwJMog%2Brsxce%2Fb8tHZIrP%2FgxQd7%2B5RR6hTB3RCe4ursHH49nox7w7gyDOIyn5vPT39fvVJeNXy1C%2FVAMUBfvQJpASGnr1GZoKvTF9allSPHPfjRSHcdcCgNQPaiRztuXDK7zGtcwcsu8i5F41eYwJ6mN2g0gLCVVtY1mnJ1KP6vUFFjbxNCP%2FzfA721ilMC%2FdDm8FJPCzrmf2oTLy9Yw%2F7FM3Zj1AfByYFku85%2Fm7UmoFu%2BHG7St03IgqNQ5VBo85fsef%2BSkSA1%2BXOua6YxcpmBLkFCwP%2BazTqnD5qH5v3XAUwYhfzHaj%2FCN2M22Uz45soY5NG0TH2J5tZmF1uiDOGc4Kg1abk5cnwU8LmOrym4%2F8M1fSNifbudJr%2BC%2FgW457HW9dx0%2FYJ1sAX2JdqUfVar9MIik9LwGOqUBIs2sGck7SHIlEfyeEIXIOXrR%2F9c5gAj1DiU%2B0S9uYebd6QUiri9e6WTN76C%2BzRLfF675SjUAsI0KCb2T5jpX08uYrpHkQGgl8Sg3Tl3Q8omTG3OhS2Yb847nIF75aY%2FCZPmE09c9PAIsTlFcm%2Bp5xYQcP66iQj7D8KChu1Ysr4FkI7euYwZPX2R0sK0wVmNN3XdqBMdEQmJWanZmaG3Z7PMZptys&X-Amz-Signature=a77f737f610b2cac72d2ee15115373a5cee19b81a6ecbbe51ad3dba80f464936&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWZ2N45F%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDT7PAez%2F0X4C3OSNfD0nxz61pCLTP2I94QFBd0pDWo2AiEAwEuzpgOUYr9pFTL0Bw5SHk5ztleFWMZoNtqWqm5FrUkqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSfYP1GA329fqhBFyrcA0QH9rHiFBBty%2Ffk4uQVMFjdiK70Q67K7%2BDyhUs6ksZG1eG6R8aspYgLX16fbJ4ks1POeoPgc4ZdLDQChrWasH2j3i3zTg1ukm5qlXhhpGzgZ71fgx9yg%2FDj048wdZ3aZgWxfGmJ7%2BR%2FDlIL0vKTM%2FLZGWx130x1QpNHuw6SzPkSv%2FaI%2Boq9CCxGGVlBMWySG1zhuQ%2BdQmdYvEzHUeembkmFMnbUTkMUyXyynwJMog%2Brsxce%2Fb8tHZIrP%2FgxQd7%2B5RR6hTB3RCe4ursHH49nox7w7gyDOIyn5vPT39fvVJeNXy1C%2FVAMUBfvQJpASGnr1GZoKvTF9allSPHPfjRSHcdcCgNQPaiRztuXDK7zGtcwcsu8i5F41eYwJ6mN2g0gLCVVtY1mnJ1KP6vUFFjbxNCP%2FzfA721ilMC%2FdDm8FJPCzrmf2oTLy9Yw%2F7FM3Zj1AfByYFku85%2Fm7UmoFu%2BHG7St03IgqNQ5VBo85fsef%2BSkSA1%2BXOua6YxcpmBLkFCwP%2BazTqnD5qH5v3XAUwYhfzHaj%2FCN2M22Uz45soY5NG0TH2J5tZmF1uiDOGc4Kg1abk5cnwU8LmOrym4%2F8M1fSNifbudJr%2BC%2FgW457HW9dx0%2FYJ1sAX2JdqUfVar9MIik9LwGOqUBIs2sGck7SHIlEfyeEIXIOXrR%2F9c5gAj1DiU%2B0S9uYebd6QUiri9e6WTN76C%2BzRLfF675SjUAsI0KCb2T5jpX08uYrpHkQGgl8Sg3Tl3Q8omTG3OhS2Yb847nIF75aY%2FCZPmE09c9PAIsTlFcm%2Bp5xYQcP66iQj7D8KChu1Ysr4FkI7euYwZPX2R0sK0wVmNN3XdqBMdEQmJWanZmaG3Z7PMZptys&X-Amz-Signature=b5e61e046d61dfde8f2d177d6fa5e05c1e5eed37b25c18cb8091b7b48f3e803b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
