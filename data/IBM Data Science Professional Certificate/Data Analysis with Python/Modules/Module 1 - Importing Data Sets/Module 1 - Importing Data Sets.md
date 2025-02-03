

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW2MV42%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FNeCsBtwj3ZiBSD8jPYx6UPLkr%2Fybc0SG7ciX8Geo1gIgedDq%2BoTgfG4z6MKymKudt4uP9UA4grIOuOC5TR3nqZMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJaB3vM846JIvq6nmyrcA2FJOKbjNkKyP3FjM%2BiAyinK0eRLmEfuUB0fdsp9FKpVnW6rRn15%2BKTqHalxlKy049ajdf%2FwvWhVgHqpq0IjiV04covi6B8mU%2FNSqD%2Bg84AyjoWQNfUZedqN%2FnQXlHQxvOqSAr76j16mlatOgLUFmHPYoeUU7sHjqZcwO2O44HPXCdf8S3kTBr3jzXg8EsW9BAOS8xuKgRGxcfcutf%2B8f%2Fj%2FuyfnDv6BTPJYZgyrsKgJwwpQYuGCLOrWT9XoksiQ8w84coDvR%2BcVYJYx6DwSpaDu7YD9iGY2pPmVzjYKU5Bp8puV7O5A21HqeGqXYhN4uTqaYAqk2RMJKWSI65OCe5ZIQ3jem%2B3niKWmQfpbs1OC%2B6r2d1j4Y%2Bf38me0ZQY%2BCCmIDQzR4HDdFfp23xKwqqWT9jkivh%2FKWdq9Grs5YHFAQwkcJ2CfCXOtCg4ckh2k0%2BsGwSax1PDKI98SAxDb33r%2BDHPU4Gyd3F0wA7y4Ch%2Bscg7bdr7bTuPLm9DcKBd0V9hZGnA9oTiztMV4tqOddO6%2BNOgdxeVq95%2FStV4AUfrDr03%2Fs5yELB%2BHmMII7nMo%2FIvJKKwM88A2sKjlb8ByW5LBpgOGM6V1%2Bh2awwHYPGk%2FzAeebcFFAcy4UD2oMLXzgb0GOqUBr%2BGl7F%2F%2By1aHc%2FFs7Q9qoBhsNuzoGlZjfXTi1M9IKUJqt0u7rYOXJaSWYLeAPe4%2BG15E1VhJyPx9zHwI2vXNtuGs3WO%2F32wJlkswXxUmI296Zd1W71Gqs1hIwXhm6vS4BBKDEvpUc9QQj4m8ljWFTr25UYoNQRTrFUoNDT7CPEWxLN%2BFux%2FqTxE4Wt5lBUdImX%2B%2BN%2FUTnM50k01O4MPVpwB1ZEbl&X-Amz-Signature=5c597c7160ed6e6db621a8f060fad85a22dab00441e7b491168cd5277aabbc20&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4O4JCWG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6TSNxx3TIYlhYMBEK5GwQ0d3Ezuy%2BFsoMbABKmS7nmAiAaziRs3t10PFmu58fD0uhviK%2BrRSQej3dm2G%2F1IEpUBCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMwyr3RPkAHOI9c6CVKtwDfag6wS%2BVKXZa0kbX8tnucodiubVGOCJu3kGi%2FXZPPIEoE4OwgFvH7%2FyN5z9fgcBxxmUUAmPu07SYOzhEJ10KuiHXbBog6djAn0E1yKvxXTn9rV3mSu%2Fzs55Y3H40pFDkyN4aW9JqbCOplpycJGU33giTbc%2BMJKHpNcoCdsz8i6Mij2Em1gKIMGkBvLizjGTRCStxAVvepnbFzAPCpDi%2B2BNJT9GL34v84vYXa8iDw4ZcUtUrp2C1%2BNXabSjtnTl3b7U5NrknONzi9hIjAsaeaJIkjXBqYsZGjUzFdrLM3QX0xPfbTlOU%2Fr78uoRR9QqRjmJJwoxCo1PdS0Tog19uxUsdWJ%2Bhzq4z3Q8wCuN3l%2F6i%2Btjt0TkZI4H3o5nCr0J5biRFyR1r4jM1Lj5MdVoQWo8Sa0bUNSEdvAdwyXvtEPc1EOGRENgnVvIURBJ0Z5Gco3zudwvwnxXOSBTFz%2B9f2If0ymQb2DXVJYoyBPIYp1%2B4lgkipy3LbACFC7cqG6dlHoQDSq32dxteG%2FNzp3r6FjkEbtWiY97gdHL4jf%2F0OSZPKEZXApoglpONCnaT1kd7rG%2FnvIh7GXYD6Rg6lSffeOcG30nZ01QABp07SRfpv6J7phXMx%2FQC75KYCgAwnPOBvQY6pgEIcPhsiED6ASmOMCDn7iFQ2tqI7uwilz8idbi4pVZReUpruFvYGkhWu6NTYNqFL9noFya3JY6xuPWNQZ8hVcv3N%2ByK7HFP2Ynt84KxgLZIpmbgXaO3F3x7HrCT2RCYM6xU7oxyTNYLR3t2j%2FYzKKhsngzxQ1ZPeqfQKLmGXU7CJTbdqaG3LahYm38mRNRvgU9ni%2Fs03xGDYE9JXesICryQmh14bd8D&X-Amz-Signature=ad65067ceb32b7a8fec105da3e4231847ab379fe275e96bca680216b7833aa6c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4O4JCWG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6TSNxx3TIYlhYMBEK5GwQ0d3Ezuy%2BFsoMbABKmS7nmAiAaziRs3t10PFmu58fD0uhviK%2BrRSQej3dm2G%2F1IEpUBCr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMwyr3RPkAHOI9c6CVKtwDfag6wS%2BVKXZa0kbX8tnucodiubVGOCJu3kGi%2FXZPPIEoE4OwgFvH7%2FyN5z9fgcBxxmUUAmPu07SYOzhEJ10KuiHXbBog6djAn0E1yKvxXTn9rV3mSu%2Fzs55Y3H40pFDkyN4aW9JqbCOplpycJGU33giTbc%2BMJKHpNcoCdsz8i6Mij2Em1gKIMGkBvLizjGTRCStxAVvepnbFzAPCpDi%2B2BNJT9GL34v84vYXa8iDw4ZcUtUrp2C1%2BNXabSjtnTl3b7U5NrknONzi9hIjAsaeaJIkjXBqYsZGjUzFdrLM3QX0xPfbTlOU%2Fr78uoRR9QqRjmJJwoxCo1PdS0Tog19uxUsdWJ%2Bhzq4z3Q8wCuN3l%2F6i%2Btjt0TkZI4H3o5nCr0J5biRFyR1r4jM1Lj5MdVoQWo8Sa0bUNSEdvAdwyXvtEPc1EOGRENgnVvIURBJ0Z5Gco3zudwvwnxXOSBTFz%2B9f2If0ymQb2DXVJYoyBPIYp1%2B4lgkipy3LbACFC7cqG6dlHoQDSq32dxteG%2FNzp3r6FjkEbtWiY97gdHL4jf%2F0OSZPKEZXApoglpONCnaT1kd7rG%2FnvIh7GXYD6Rg6lSffeOcG30nZ01QABp07SRfpv6J7phXMx%2FQC75KYCgAwnPOBvQY6pgEIcPhsiED6ASmOMCDn7iFQ2tqI7uwilz8idbi4pVZReUpruFvYGkhWu6NTYNqFL9noFya3JY6xuPWNQZ8hVcv3N%2ByK7HFP2Ynt84KxgLZIpmbgXaO3F3x7HrCT2RCYM6xU7oxyTNYLR3t2j%2FYzKKhsngzxQ1ZPeqfQKLmGXU7CJTbdqaG3LahYm38mRNRvgU9ni%2Fs03xGDYE9JXesICryQmh14bd8D&X-Amz-Signature=69413c998c59aedfde7f737ec032915463177d2dc6705a3a20a2327316b96192&X-Amz-SignedHeaders=host&x-id=GetObject)
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
