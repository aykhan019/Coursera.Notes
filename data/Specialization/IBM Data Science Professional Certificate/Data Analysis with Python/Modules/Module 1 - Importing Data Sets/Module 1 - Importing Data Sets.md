

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TX5M7RFP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGu4L%2B9hKZ921MCUrgFU2T2w4bk2YPuKsJHVeLaobJitAiEAp4acx1JF0mZSNPILUdBGC9ogrGiz5TB%2B8%2F5YTPZo2NAqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF1biO7yMJCD4GVywSrcAzhO7A5RD8VhThX7ddmP5M4Y%2F2qBSgy9%2F%2FhdUXP7hyWluosUH2kGaB55d2iM7TPRku5lATllTFjwr1%2BbugyD6D0t%2Bk8jL37DYcC9NxFvOQHRX6OOlA5%2BfPlnGjk5yniwbOpjb2zOwTrGdiL1MgWXTwZ%2BgsCMKyK7wy4ay43UyfLU70BHCSCS4pKTu2Wot9YTWVdvymKUzTzfS86%2FSg3ERILDMdeW85hi7W6G60Q2rsWczYp8T1i1DfOY7xXVtLog5%2FCgpZE31VV%2F7THlut1fCPUL7dEApt7JyZMo6xi4yy7OU2V81g39LQ04BosmcC7ILNFzRG2DUDTmhzXoMufesOBqPv9gUbVWDnM6VY0PDtcAxwaIIWBO8TqBzQ3GxtC%2F55PHFfyjdLdqBcWdXlmTpLqtPOYjn03%2BefCiQH1%2FWrTmUDDicqSre1beBWTwn2bXB98zBK9LtPT32yArPX3G7USV0sO0cYMkJLAle1bewN%2FPJFacRoGh04gz4ZtTYqqpc7TfVnqkGkUTplQLPvaIV3snG%2BT87r9ua%2F71izy4PK5v75Pc1JSBShVAI3Zdz624iilIlMj7AHBHjFPN%2BAZX1jqMLYUHnfY6LQxXfG%2F2l%2FXShPU0Tsld8AXxN3TYMI%2Bq77wGOqUBE47FF9tgSFJquQpo7l%2BwEX3eU8D%2BN%2B8IJ8lnWJQVwgvUDRDK6FvDq086b9tiu5BfGwbijIOwP79WNJmbV3jjn5Amsgv47mWPIqLjVe7495y2JqhVIjrnCobDnp3PcM0vlRRkYcSuXbyVx8hpWS2ZCX5d%2FTy6uxSfD%2BVpc2J6pLi08bVaBsPzaoJJhiveCtN6O0ioo2XwHy4hPaOQLOsuVotpk6HE&X-Amz-Signature=31d6d5ac63b2300ae30e2204a39012ab823a4c80c25d1ee6a8dbb6de27f31886&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJEV6R7E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFfOpRhlssnbIjDK%2B2afstqBJvBv5F7Ps5PPyNu6agY0AiEA637PB6UhtPJHA1ucaow1fogXWMNgPBK806I7DQTlhroqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6xwe4y6QfOuOMBSSrcA4wJCfGSaiYXJp7uM0lBeu%2F4dwWrGctV980J24OOPAgVIlGtbu8bUbbIco4ocgEnvVA%2FH7opwNx5bMSp5KkAZxPMCxnSqTGzGxbOiixsJ6L22olh6ZlhiPK7dKUq7jpCnwhy3Cko5bDCs1hp2rzqShlL2jL30HZ%2BZdDJDkuKvwemmg0Q5G4SfaEPAu8V8me0gQz%2FYgYA6jKMUc7gls4zG5zS%2B8QjLtkl%2BgmQoZ%2BAy7wVNHd6j%2BFPYnUUpdJ92awL4A427j4t37hsD1%2F0i083IxuDxZkpst2%2Fa5GjHA5HrUe2xD2gH5SPC5OzKOIV34vfhFZyh1r8W5Sp0%2Fe8fEsxoJ4k7UNrgZlWbQ5r009y0b3ggO882Nm1A0%2BBA%2F3U7o2jVZwXBMPm9fitLCZQqB%2FxRUo558PXnJrtrX7CmVw8NvFV5gWZmKevveTR8XmtxRRQvi0LNcH8u3cYKuZ2DJj6p6EBeIKj3ou8mYN2dkgcqPPzFfSIEi%2BqjA5zA2XqdtxRRSCyW%2BHL4OQ9A%2Fj0BYnm5r4foNIASpO3BIXI3tzzCFr2wekSBds3iUODciN7Iw2CKnPGLc%2BaIFX%2FbiygWXt1jktXMTD9rmhj7LoveJL7a%2Frq5Ah3do2AzQiRMq5kMIiq77wGOqUB%2BOqCwStIVSgUwfDOf8u7MkP%2F%2FNU%2FUX8rxPRlmZQd7%2FlEGVrKOyGV2Cie9hImpE5thNBAJSAFLpsHIuqS7ki16snC1ZJB%2BmgTFFmEUoUQZj2F1Xzfs5MkOEy7DOXsdMROze%2FqYQTjuaomCel3WX49QbLJ%2Bx1F%2BRKm0XOl0NgvS7%2FQSVtcsfhjTtK1JlFEGYEJy3Ep9lauTo%2BsjtnxftVmoX8cIviy&X-Amz-Signature=ddb6511b11d4fdd9079c0041e5aaaaecc8a53dcaaa4dae8161435decbafdaefb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJEV6R7E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFfOpRhlssnbIjDK%2B2afstqBJvBv5F7Ps5PPyNu6agY0AiEA637PB6UhtPJHA1ucaow1fogXWMNgPBK806I7DQTlhroqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6xwe4y6QfOuOMBSSrcA4wJCfGSaiYXJp7uM0lBeu%2F4dwWrGctV980J24OOPAgVIlGtbu8bUbbIco4ocgEnvVA%2FH7opwNx5bMSp5KkAZxPMCxnSqTGzGxbOiixsJ6L22olh6ZlhiPK7dKUq7jpCnwhy3Cko5bDCs1hp2rzqShlL2jL30HZ%2BZdDJDkuKvwemmg0Q5G4SfaEPAu8V8me0gQz%2FYgYA6jKMUc7gls4zG5zS%2B8QjLtkl%2BgmQoZ%2BAy7wVNHd6j%2BFPYnUUpdJ92awL4A427j4t37hsD1%2F0i083IxuDxZkpst2%2Fa5GjHA5HrUe2xD2gH5SPC5OzKOIV34vfhFZyh1r8W5Sp0%2Fe8fEsxoJ4k7UNrgZlWbQ5r009y0b3ggO882Nm1A0%2BBA%2F3U7o2jVZwXBMPm9fitLCZQqB%2FxRUo558PXnJrtrX7CmVw8NvFV5gWZmKevveTR8XmtxRRQvi0LNcH8u3cYKuZ2DJj6p6EBeIKj3ou8mYN2dkgcqPPzFfSIEi%2BqjA5zA2XqdtxRRSCyW%2BHL4OQ9A%2Fj0BYnm5r4foNIASpO3BIXI3tzzCFr2wekSBds3iUODciN7Iw2CKnPGLc%2BaIFX%2FbiygWXt1jktXMTD9rmhj7LoveJL7a%2Frq5Ah3do2AzQiRMq5kMIiq77wGOqUB%2BOqCwStIVSgUwfDOf8u7MkP%2F%2FNU%2FUX8rxPRlmZQd7%2FlEGVrKOyGV2Cie9hImpE5thNBAJSAFLpsHIuqS7ki16snC1ZJB%2BmgTFFmEUoUQZj2F1Xzfs5MkOEy7DOXsdMROze%2FqYQTjuaomCel3WX49QbLJ%2Bx1F%2BRKm0XOl0NgvS7%2FQSVtcsfhjTtK1JlFEGYEJy3Ep9lauTo%2BsjtnxftVmoX8cIviy&X-Amz-Signature=43413d403ef69cd53d914ea261c2382d8065842b5f68127dca272794e1a7081d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
