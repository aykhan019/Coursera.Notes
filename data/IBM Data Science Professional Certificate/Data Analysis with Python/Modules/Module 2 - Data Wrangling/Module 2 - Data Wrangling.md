

# Module 2: Data Wrangling
## Introduction to Data Pre-processing Techniques
Data pre-processing, also known as data cleaning or data wrangling, is a crucial step in data analysis. It involves transforming raw data into a format suitable for analysis. Here are the key topics covered in data pre-processing:
#### Identifying and Handling Missing Values
- **Definition**: Missing values occur when data entries are left empty.
- **Techniques**:
	- Removing or imputing missing values.
#### Standardizing Data Formats
- **Issue**: Data from different sources may be in various formats, units, or conventions.
- **Solution**: Use methods to convert and standardize data formats.
#### Data Normalization
- **Purpose**: Bring all numerical data into a similar range for meaningful comparison.
- **Techniques**: Centering and scaling data values.
#### Data Binning
- **Purpose**: Create larger categories from numerical values for easier comparison between groups.
- **Technique**: Dividing data into bins.
#### Handling Categorical Variables
- **Issue**: Categorical values need to be converted to numerical values for statistical modeling.
- **Solution**: Label encoding and one-hot encoding.
#### Manipulating Data Frames in Python
In Python, we usually perform operations along columns. Each row represents a sample (e.g., a different used car in the database). Here’s a quick overview of basic data manipulation:
- **Accessing Columns**: Columns can be accessed using their names. For example, `df['symboling']` or `df['body_style']`.
- **Pandas Series**: Each column is a Pandas Series, a one-dimensional array-like object.
- **Example Operation**: Adding a value to each entry in a column.
```python
df['symboling'] = df['symboling'] + 1
```

These techniques ensure your data is clean, standardized, and ready for meaningful analysis and modeling.
___

### 1. Handling Missing Values in Data Pre-processing
Missing values are a common issue in datasets and occur when no data value is stored for a feature in a particular observation. These can appear as question marks, N/A, zeros, or blank cells. Effective handling of missing values is essential for accurate data analysis. Here are some strategies and techniques to deal with missing values:
#### Identification of Missing Values
- **Common Representations**: NaN, ?, N/A, 0, or blank cells.
- **Example**: The `normalized losses` feature has missing values represented as **NaN**.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXUSMEW7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF5%2BCVHGS8fum6a%2BLINJg5c%2BiwvFbzl6ZXjYdGIHqMvdAiBqdapCeU1ZdwHR42ubm2Liu0PLSIE6e6I8zU%2FZTroRuCr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMD1Z2F9iT%2FKnwtQxVKtwDdVY0xnASqAAX%2BZJMolxaxByZf%2FJv6Ilbg1q7IxAo%2FxxmTaAO%2FqACl0Ku9VKQG%2BKJYiPHj58hm7gHSDXLEjT%2FtD1R2sgSNN%2FrCDntChYASd7s8fEAJiux9Ug0Lkyge3exVDEtK0Lon1zs80RmoGngaWW3gRHUBZKfjw5ll8vvH10FlQ8tkVky4DLIxRIm0r9PEf7R5OJTdRYe6PJ7CvjOgs%2FHsNRquQjeq%2Fj1aj9L2muKSSKEtxas8%2Fv2tGsKmjVNrx7RCcgsPjt%2BbygHFHnBhXwu4XxzxOzTz8PPb%2FstuB9iVJ2EN13y2bGu4HkTGIUIfKpU30RRNx9XXx9cXdlc7pMHdphksJuzlez1AJ0EBraKuB%2Bws8QwLyKqSBqfKSG6yJSE9Y7d%2FSSP4cHtJLHBKoRqHMD6QrYv9c2W%2ByndrJiQxpJPnj5MWVuHqU6fIU8qywxJMlruT1fKQgAQl9mUJ98lLAQceHAvvH%2BahTW0hrO6xkUmCfzLtxcxscu7awRrZ%2BYXMHbDaJ5250TOdYrSizfWktMiIl8SOKmS4fSG9VJabp8v%2FG5Jxifg5Xzal7yzRn7tSR7EyJPud5Cp4BsHOpSmpxfFAVUo6aLFXt%2F5HPvJNcn%2Fms6lKBw9srYwrvGCvQY6pgHzeOb6ErK9WSWgcDYmLJu7k01rZHpcWb4boOlK3gPkbQSh7E0zyEWxpgRukB4E%2BRd%2F0INh%2FYVB3LFuM4FUE%2FATtRJKGSitRjsi4xxsOMRp1O%2B87wt7V1zoyefye5xbj2XRUkqIM2ZG%2F3%2BqYFrWZlrABts5AwEIzpn%2BG9ENfVR7VX7psnpFn3Eloza9IYRqQpMcoHXzAzYATEqVgsgIOmwlg4cAfkWI&X-Amz-Signature=2b974f8c6e007db39e6657c87171674b3d383ec2c4308f0357c2f62309756851&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR7MXQH6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb8CaJfJ7Bl1JU%2F3Wog%2FGKZE5C0lFXr2bbtu%2FR%2Fo7G2wIgIC68aKQuf0Q4pMfhbQNOuy%2BkY7Eqc9M94P341UoDOuEq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDJqDLZ%2BP4TvQuYDijircA9tfzAV%2Bv5jU9RUcQEZQTyQAOe1S9v5lwTatPEJhRi55rPPos1rTWq0K1plGUJDqG%2F6Nah84xCyOPC8pElW%2FsFtrGUNUknmGvq7CJOqxVVjAQtqdWvtGl7wsq%2BHYRUhl0podsPRtHEr7Lqwo28rOuqzLURKbHE3HUCR8XR8KPiZcCVc7b9r%2BQuludEdB0YatYIm6OJHIK6SLnPOrG4NYbGaDt3t2TC15wYBgzueKDW08n5RtP%2FNE%2BNPVvwxSiYgmFvYZf22zhk47%2BfXkoAxmGzgE2M0Z0PauVN4ZG5Ulla60cgYu%2FRvSUO3Zo5c7icDH7uXzuI%2F6tc5aG5YPJ8rHWQyQFGSYUoEZxidjAheqPnRJp%2F9wyli8mpyXpOFRU5hGiz%2FQs4C7JObPA3OtUimiayoKLkj2J1xkHDCNyHDOZjunzONxPD3iJqyiu65ESA25eWh%2FStYCgAtLw4J9WM%2FN2fyVfwi5zyw6hh1T2%2B87mTY1eCqVflx4nm6WWmG2Q%2BbJ%2BQRU%2FXo1TfcZFSHcY4XCadU%2B1UhMgzZ597MLf15fQYmLsAT5ARwNJpbCyw6k3oK8xo4j25yxfLB3W%2Bru4xmwf4f4BKck8WU62Xs5eRrA%2FoNCiYnDVplFqXv4bCKZMK7xgr0GOqUB5YQjzkgnFaX1Vfh4jfemFYmnhBANnEgsUP1XHNiTZT6RVNxei5PK6hNrJTj%2FEoR4yyyfdDeYgdZ5OCvkDJlj3pVCkBizfXzTM85ND0TA%2Bnto0pHjSEqBa7deeT23I4aYDfww2DNgoixQI7N%2FzEz4SjWEJo%2BPs0Y5DXzzr55U1t01gYZpdwQmfbCokOpv%2Fi6iWDsuqo19vxDQs%2Bf83z92ZXNJVMiC&X-Amz-Signature=ea0ca977ca06d7dfef4fd8c528c86576aad98e746ddc23eedbad30946af461b5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655WKHH3J%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICMR6VqdSsyRpSbEMZ9%2Bfvc%2BdVjBqQpKE38wG3%2BUHwhSAiEA50Bakk4VnNiMCQiwyT5wa%2BhiSg%2BzbNnyOgAMqseZEkwq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDJXrQbB%2FFGLeqXcBzyrcA4IHOE%2B5UEeTizOtyJXnEpRzu8VSLOjkdWy7tSxVQoJzan5f2cHNVVVsDJ2bSGY8ci12tGyVqRpArmCtP7i%2BpUaku8IDpQg%2FdRfva219Q5wBHrFNaEbxA53v4iKap9Bp6OPYOn%2FYNFUmA65oyOWOJJMqPWMrDYLaFYdTcaqB%2B8hFSWCR51HKMMT2jfOu8pcukI5OGoVAQSfFCTHfwfwZpcpxvX0m1wEMy5KhdfbDDBLw0RM4m7yix0MeNYiwOHuqb66A1zGRgYnd8g7h8lYr96tyHMVYRS7UVN1tRuI%2B7KjQfJIYMpDatyY55%2BGAlcPo8J1RVdrBUTHLNP6NXGSPzY256wTS9QeVkbrkHsz9lBBSybkfykgDpT1KUjIMV6pU2vtRDtEqvuB1qcSFDULjYS2wTNKJM07QTDXIEOrd7%2F8kkM9%2Bh%2FXwVg0dC%2FKqcohP24NgNHAE5nZh2D6bO%2FCjvsnpSa%2BiQjk5K9xo8rZCHzatfKYP0NBrb%2BoZaUeZgfn%2B9zCen1S3CiDBwoKeep8VD7HsEQkZ9s5b7CVXZIBHLScTqhamFEwWbREfdflHG%2FqSfHK7ozswQADCdBx82H2XUVZwIizaQbYa7sx3AYLnsWrKCLWkNVjv0u3AoOuoMIHxgr0GOqUBeSLyt8%2Fx6vgIvw0oO6mUvg1rIU6jqOcs0J3WJEsj%2BxBaGAaIYExnjuWstdJ6Iw04O9f6TWF12tWpX0fG6g%2FCKIs0C%2B9WUswkJYyNV0Cls7ksdmKCWZlNZiX%2Fy9YkqLWd5uZGJmjQ6z8V583c9sFZ3YTV%2BAktsSpJNyNDqXwhwNyN7FkSEqak9kOw9VGHOQwgC1lVbyFiPOr8A1aQKBSoXf4QQizU&X-Amz-Signature=4787cfdb600706ac565776d51d9a4604a07ab698f1e92ac787888829b863b5b0&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Pandas Method**:
```python
mean_value = df['normalized_losses'].mean()
df['normalized_losses'].replace(np.nan, mean_value, inplace=True)
```
	- **Other Techniques**:
		- Use group-specific averages or other statistical methods to impute missing values.
		- Example: Replace missing values based on the average within a subgroup of data.
4. **Leaving Missing Data**:
	- In some cases, it might be beneficial to retain missing values for specific analysis needs.
#### Practical Implementation in Python
5. **Dropping Missing Values**:
	- Drop rows with missing values in the `price` column:
```python
df.dropna(subset=['price'], axis=0, inplace=True)
```
6. **Replacing Missing Values**:
	- Calculate the mean of a column and replace **NaN**s:
```python
mean_value = df['normalized_losses'].mean()
df['normalized_losses'].replace(np.nan, mean_value, inplace=True)
```
#### Conclusion
Handling missing values effectively is crucial for ensuring the accuracy and reliability of data analysis. The methods to handle missing values can vary based on the nature of the data and the analysis requirements. Using techniques like removing, replacing, or even retaining missing values with the right approach can significantly improve the quality of your data and the insights derived from it.
___

### 2. Handling Data with Different Formats, Units, and Conventions
Data collected from various sources often comes in different formats, units, and conventions. Data formatting is essential for ensuring consistency and facilitating meaningful comparisons. Let's explore how to address these issues using Pandas.
#### Importance of Data Formatting
- **Consistency**: Ensures that data is standardized for analysis.
- **Clarity**: Makes data easily understandable.
- **Examples**: Representing "New York City" consistently as "NY" or converting measurement units for uniformity.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVS73UZY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL7Mch46%2BjPxhq8pifJi%2FsRhX3h9KL8JHJZ%2BvWy9QeYAIhAKANfLA7jbMkt9xzwLahfIy7rOkqGbcGluH1xwG%2B7kn6Kv8DCBYQABoMNjM3NDIzMTgzODA1IgzfXLFfymvyzpgpWDYq3APMfrDBKvC9MYCn1XTVd7BKGF7cRpF%2Ff6D%2FQB6tA0RX%2BMMe6Y7NFWT5QkIHG7zR7FuAM3DqZ1C2nggGv4q8Ug7xKkdCLzK2%2FkaExE74AGVRbuzZgZ2PROGATDlVJ%2FeyvyIRw%2Bm2UrmynML8iNCXuILyNjj7Qu2%2FRRA8iVJ6cPzrhg%2FstaNkW3Ex1Mucq7v6P5mnSpTsZgPg8GCfWG0Vqn2eAA2cLZIIfLZUlwbKQBsDT7pNyfPHnVQltYzB0EdV9Uvj8PXzaCkuGcpFY3ZWCh%2F%2BOZFbMCrX3hPeye7qiblsAcApSEzwlZT0NYE4ztdbInOPgOJ7skHPml1RCNlitYdeydoEt6U8aAzPML2UVfkpvOmrPCYJGKDGKspMDYlA8NcxUChte7m0MPyVsXgE30M72LmUNB0XM2So0Y7B64w2BMsEHoa6w4VBJ6kokVBWd3Y9BApasLrOZ3UB47%2BsqGUXExMcjuO%2FAEEsCFvsoBPhVF4uCD0naCT%2BAz%2FihCwvXc1zSii7Ya2e0AaJaUhjtu0%2BNMb3ZhWFLr%2FobsOwbhyXxcwCg7KP%2FIhoru361mhrKRUex2VJCQUsUJ1PUohzwoRolAxvibTs1E5vkB3O7qejDuqY3D0LbfLi%2FNdrwzCq8YK9BjqkASg0nafbZ1o%2B70BGOVYF%2Ff0uAu%2Fw34b2IbWtuQLqkQTenqwA9Sdm5Ja9K%2FpzC6G5P4sYFu6a7IZBDtnfP8Lr%2FmXWXCuYQ2yzfQG%2BFhyYFThRHluMLC%2BrOSkohqoMwCori5nHUklrEryeH1y3eltTW%2FEj%2B4Nefy%2B0x4%2BGm4ay02XoM1M5QgS%2FH897bCy20tPh%2FImQ3lq%2BQFatT0jlNJqN136%2F3hjY&X-Amz-Signature=b5f037b0887f9da569190fdc059e348c4b30470d9c7530fb1556dc2965e67301&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Common Issues and Solutions
7. **Inconsistent Naming Conventions**:
	- **Example**: Different representations of "New York City" such as "N.Y.", "Ny", "NY", "New York".
	- **Solution**: Standardize these entries to a single format for analysis.
	- **Pandas Method**:
```python
df['city'] = df['city'].replace({'N.Y.': 'NY', 'Ny': 'NY', 'New York': 'NY'})
```
8. **Different Measurement Units**:
	- **Example**: Converting miles per gallon (mpg) to liters per 100 kilometers (L/100km).
		- **Conversion Formula**: `235 / mpg`
	- **Implementation in Python**:
```python
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True))
```
9. **Incorrect Data Types**:
	- **Example**: A numeric column imported as a string (object) type.
	- **Identifying Data Types**: Use `dataframe.dtypes()` to check data types.
	- **Converting Data Types**: Use `dataframe.astype()` to change data types.
	- **Implementation in Python**:
```python
df['price'] = df['price'].astype('int')
```
#### Practical Implementation
10. **Standardizing Entries**:
	- **Scenario**: Different representations of "New York City".
	- **Code Example**:
```python
df['city'] = df['city'].replace({'N.Y.': 'NY', 'Ny': 'NY', 'New York': 'NY'})
```
11. **Converting Units**:
	- **Scenario**: Convert `city-mpg` to `city-L/100km`.
	- **Code Example**:
```python
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns={'city-mpg': 'city-L/100km'}, inplace=True))
```
12. **Fixing Data Types**:
	- **Scenario**: Convert the `price` column from string to integer.
	- **Code Example**:
```python
df['price'] = df['price'].astype('int')
```
#### Conclusion
Data formatting is a crucial step in data pre-processing, ensuring consistency and accuracy in data analysis. Using Pandas, you can standardize naming conventions, convert measurement units, and correct data types efficiently. These practices help in preparing the data for more meaningful and accurate analysis.
By addressing these common data issues, you can enhance the quality and reliability of your datasets, leading to better insights and decisions.
___

### 3. Data Normalization
Data normalization is an essential preprocessing technique used to standardize the range of independent variables or features of data. This ensures that each feature contributes equally to the analysis and is crucial for computational efficiency and fair comparison between variables.
#### Why Normalize Data?
13. **Consistency in Range**:
	- Features like length, width, and height might have different ranges (e.g., length: 150-250, width/height: 50-100).
	- Normalizing ensures consistent ranges, facilitating easier statistical analysis.
14. **Fair Comparison**:
	- Different features might have varying impacts due to their range differences (e.g., age: 0-100, income: 0-20,000).
	- Normalization ensures each feature has an equal influence on the model.
15. **Computational Efficiency**:
	- Prevents features with larger ranges from dominating the model (e.g., in linear regression, larger value ranges might bias the model).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XMOSKBB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFLVnqiUu3KXO1BO4DMfWLzoCg3s9ihg6NLk605Mg7RAiBS9%2F1JjswHijBvbDgk%2ByShMZDJyqUB0VINUOIbcr%2FskCr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMs0D%2BiLU60qKd1LbXKtwDmU2hD8BT5mz2l%2F3DwQoYX0oRleOiYpiScGQxrH1PG1u0rGTJXYRWlpYTPQLVERKjFsQqyttopOpkEC6P6ru0k4jZMHwtF%2BJL8oQPkWroKKswn7hbJLoUzlaUqgIITz561l%2F57tE7NR1lFz8rF9YTLOTg0KodwmbPJw3TctW51Qs5lqp5Sx9TyYmRAa6StUevpxDqDU20vDC8nCLZ9Dl4kWPjqVRt5uIoeyZ0Mdgc%2BtYiNukirkDAaESZAy6H9Ij6t8lD2Jx3XFIHsbnCYHdnvMjRgUNcJDqsSKVWO8dUCf7ct9QCqqIuR1C4BndngFx4q7luYwNX8z0vmgxU2Pwg%2Fo0Tf62nXL3Q6o8R0rBHdB1CtXMvpFKJnG5F14K35If%2BkiI5MIMhqxsD3EUoOoFPEVOyina33tUcmGDDDDrRGgBZVoMTVGBX228RDCkSwSkSIQvCM2WPKEa0Z2TPUcc0jJPP91jh2QfYb6cqW2WJgk6ew8b5QeyqJl6qW4PEZCWjNmrUqFNWx4EmpXhKNiRN4ZpR%2BLvylufagzU5129fsUXSJuNH1i6ozZLZzqV7829xL8oqJxNTFTci6K3d%2BJTUKQoF6of4n5YM0A2wCnEjV1x4D0Lpv1%2Fz6KVqEmIw5fGCvQY6pgFffhWIBdkG2I55dAkVy%2B3qhfAHeAmWZfwsvkBOjjPUuPNyVkr%2Fa9qWNEhr66vQH%2F0P%2Ba3IzlS9xhRh%2B4gI8RdCYdC1xlXbbGXhD8fARf3qRp5ee4x8054TceEz0PQY%2BfwnMXz1HRQ85zAyTUpfrrzOVjoTfTBR%2Fj5ZdOEgK2L46q%2BuYbDB3v96D8JCShWpLXQ5hFSUmrJUHNqAyxso8BFHQWI7lbCS&X-Amz-Signature=f9edd4aef9913f0b442bf7b7f6dbf9c1d64a070dde013ae4abc21adf30bc4b9b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHJVHI3N%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDK4PCL77q5OV%2F6y0e7gNkGm3Q8cKTnNtVKIyhHInVtxwIhAMMnFXkVDkm2%2FujBosQMmQVPurUOVA63GFJ4m7ZJD3PKKv8DCBYQABoMNjM3NDIzMTgzODA1Igz6ZHr5Yfwh%2FNmXdGwq3APsoUHFFUcPjUngV8pATBBqp%2BOXm8UpRrdBk9O%2F6RMGuorzG1LLLy0cA2W28IcTrlUeloAHuy%2FtsIIsGhELHsub10FO15yCkVi33AFwoZpT7PG7NCBFiE%2BRQYAUyp06PUPkt06QyLMJ4TAZxrHS%2BLrFmIkir6bwgm%2FevXOD0oSvNOXdPP30iYl6sadG%2F0gQ6lSOlUFJCX78oXiJ7GbQ4F0ZVy%2BK32mQiXWlf%2Fp3FYonBxgm38KLHBaS2jJiYfYwdmrT20fF2KY6j8EezwlWAoySGG3NTtZSEQgW5HPRDDf9pqX2G8kiQp5ojGX9JYbtGEcxoI95kbdvkE25hRihRXYWP6LVEsZl%2F3cJAh8aWg9uoav08TK84ymNyIEHeo%2BRHUdDdOgF%2FPwjPnw8vxTNkrOGjVkdRXFId5indnSxJws0iS3g0C84JQ2kA6yfUeg8%2Bn3R2fLu0BcLW61bm%2BSNVqRIEt8sqYhn0vgdwf0ubS1Um0%2B4dYEem2yju8qRS16a6MdyVC9DydZvzkGMluEiQFiSrvBi4Yg4OSitj0fEGhmwC1JpF8JwpCeavBth%2FG0hseUWGIJ5CwXIF1ax3goiQvHtDg15%2BXmtyMVd%2BJ%2Fa6WZiv%2Bfkdrmg4EoOJ2pRujCW8YK9BjqkAV5JRlCB50u%2FKDaHsC31R1owGdn%2FxB0CLca2NIw6FyTIdn3nAUkoZpeyOWz7dEB%2FSZu3qvmze3D6PnO0Gn40TkGc1wyQ4SoqLW90zFlKlCnswZeJCmv6Ds8w4poewo05ufjRj03GqWqNW9UoKRwJIWSyqV8QRpojEdQSfVi4OBqEBxxzJDL0TXEtBg1WssVb%2FuxFpDNA3mhKzgkyx028uYAlczcZ&X-Amz-Signature=46d1c10831758a006f318a910dd2a7bebd6072e1fdabca9c9d1d6580bc6a183b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXTMO6NA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhTPac0o6szUcTLSU%2BwmyzanmnbH%2F%2FoPOOhE%2BmMOYkCAiEA0ARnU%2BtQUJWX3moGjlfKUkcCB%2Fqra9QXUsKG4iNeISUq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDFXVYTraZBUJwDwOBircAxi1fI2f5XAc9L3QrhzZgSEtwCOlkSlII%2FFwlUqqx1oTLT48t%2FHWW3TPgacLuF5nocImo9q6w7XnQmnjjsxPCRw%2Bu7GhDNcg3K%2F4JtZWjEctk4aX92LlbKnwauM3oKo0oseZJhUYwFQ7DG4x%2FF0MhVwyDSdmRbdieNYJYSR%2FR%2Btfj0LD2tvojfG2cL%2FveJ72NSQhjvhCcDcnLYYqMgOrnPgwEBDkqrenyUjOg26cB3StEPPgxwg3EPu9AMrWempGLoldaDK3Evoq6uxGA7%2BiibzezjpGZZrGEpXxseCMqR4eZR%2FTmPXypjCe4liuz2fPFPzjAWcWMDhWtBRlqiPmtJaS1eZyADWltv5b5cMu7uYD3L%2BzHZGwK%2FJeW2d6G782ZhUe%2BqY13lMLnRfNxshwMRw4kLkdbYR5DOTOxR3u7p5w1Xgvo4rxKXcs8zWEiAAk1ZMJcc0iCR00nrpqOM0oCSdukK3sK1ntmCOEjYei%2BHMC30HoCOID%2BYUmuRAh36EnqFpZz4pm4kvUvcN4XFN7J8pDP1AbketaWBE6laREFlOkaVNl0jpctYhDu5pJYyotrihu3LMwUvqWNFu1zE%2BJ2Iov8NSPDBfTrq4i5XbVNZ%2FqCC6hJdwGlzZj1EY%2BMJPxgr0GOqUBAJ9pr0PkHT%2BNLe9D7A37fgk2wT0ElH8iltblR3oe5EIKt5FvmZKSRcqD9Q993CcfFPrjW6YSEfgURyj6bLHsL99k7s119K94qGHeC1cjj%2BbJHTjDHmbN%2FeaMkcYEx3iJ21cZaQnqqJkNwLR9zPzKdy%2FXnbeJWIuZM2SYxnIEgNGnWbIVY1qOpmnxRDaT%2B8RHTx79RQiLAOAgS3VLmOKhbGfnxYNG&X-Amz-Signature=7630bfd4a28877124c54ecdc081816b6892e9db09259657d2b58403f036a3cf0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPVJL4V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BX6dw1CEbPM%2BdUXtn43yMoT5GJXyxiVucl6XV094kEQIhALEvA88eM0d%2Ft2EvJx8UkBrgqUv%2BZkWuntxYm3obztknKv8DCBYQABoMNjM3NDIzMTgzODA1IgzWX%2FGleCEd3n25Ck0q3AN1QrSe5jcOjKHCGuS5wFF6pHFNwK%2FujUxomi4njCuGZLEjcU8g0pRjHjDVXHFi13LtDhC7Q00tWrR3UKUWDGP6UdWIzkz7A5oG5PO4OH%2FVvaamI%2Br7bohTYoRKM63mFqux5sQaCZGyZc2xP4%2BpUvnz8c%2BwIsujlad1U%2FK1IxlkEvGa3%2BIRNPYmHKAVjVyjzw7Wbrf0fP%2F3X7rPoDfUg%2Bgb10qvJY8CNBG6rEw%2BPTsPUNcwrb43K%2BlpCHBdCBnGBb6KIH%2F9Z6C%2FISEaB%2FV7lziVIUIlMnAOMK2klIf6lrbU3Usy3emRCHhDphtfuFSxkRgBXIJ6BJDf6gmLPTqa55Nx%2BYYi9lxu6zkPm5hKJdjARnFUo1TjopMVBpKasC9fL3AJ64vL5knJ5%2Bqbs7QaodRwxE%2FB5Mg%2FhkPPm9mORfZhnx0z0aJDqovRuZK%2FTRxTHu7%2FGywd72NWb8tlnw1KnBLmM750TrDPIU3xn6v%2BN4ijUGGG3kvhS4YmsF9ZaV31n0zzkuJhGIEUi7w6%2BP8RHwZMpRqACLyEgBxE4%2FZe6n7vHlEcJZJzHFu6SovmmBfpZUdFd%2FAum0JPQAgEdnCUaPcjtlp1z2geUHAAuVFWwBXcRP3VbAwAhJVVC3p51TCw8YK9BjqkAcWPZ8UC0b14%2BXNlekVCZIOZ%2FTJL00X7%2BO84EEinh5InXq%2B4YH2iB7v%2FR4oDbJnZjijE%2BqRcAzoc3sl32K0CAQo9R5vL9TvW8jUGj5NydW5HVpYsqwlH1dhvuhb1dFYRjAyngKz7q%2B1QUkyTIvlwBjjrzaRtYZTKuhi4qtKqFFx3c7pF4tLqfTzFTlHovfnxPK9H6elgm1U0h%2BKQ%2B%2FeiVycLiIDR&X-Amz-Signature=17da1e0d7ad6538817b74161a32e1aaf72ae54d8815b478e06ced9ccfb80afea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Implementation in Python
Given a dataset containing a feature `length`:
19. **Simple Feature Scaling**:
```python
df['length'] = df['length'] / df['length'].max()
```
20. **Min-Max Scaling**:
```python
df['length'] = (df['length'] - df['length'].min() /
				       (df['length'].max() - df['length'].min())
```
21. **Z-Score Normalization**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
#### Conclusion
Normalization is a crucial step in preparing your data for analysis, ensuring all features contribute equally and improving the performance of your models.
___

### 4. Data Binning
Binning is a data preprocessing technique where numerical values are grouped into bins or categories. This method can enhance the accuracy of predictive models and provide a better understanding of data distribution.
**Why Bin Data?**
22. **Improves Model Accuracy**: Grouping values can sometimes enhance the performance of predictive models.
23. **Simplifies Analysis**: Reducing the number of unique values can make data analysis more manageable and insightful.
**Example**:
- **Age Binning**: Grouping ages into bins like 0-5, 6-10, 11-15, etc.
- **Price Binning**: Categorizing car prices into low, medium, and high.
**Application on Car Price Data**:
- **Range**: The price ranges from $5,188 to $45,400 with 201 unique values.
- **Binning**: We categorize prices into three bins: low price, medium price, and high price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XMOSKBB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFLVnqiUu3KXO1BO4DMfWLzoCg3s9ihg6NLk605Mg7RAiBS9%2F1JjswHijBvbDgk%2ByShMZDJyqUB0VINUOIbcr%2FskCr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMs0D%2BiLU60qKd1LbXKtwDmU2hD8BT5mz2l%2F3DwQoYX0oRleOiYpiScGQxrH1PG1u0rGTJXYRWlpYTPQLVERKjFsQqyttopOpkEC6P6ru0k4jZMHwtF%2BJL8oQPkWroKKswn7hbJLoUzlaUqgIITz561l%2F57tE7NR1lFz8rF9YTLOTg0KodwmbPJw3TctW51Qs5lqp5Sx9TyYmRAa6StUevpxDqDU20vDC8nCLZ9Dl4kWPjqVRt5uIoeyZ0Mdgc%2BtYiNukirkDAaESZAy6H9Ij6t8lD2Jx3XFIHsbnCYHdnvMjRgUNcJDqsSKVWO8dUCf7ct9QCqqIuR1C4BndngFx4q7luYwNX8z0vmgxU2Pwg%2Fo0Tf62nXL3Q6o8R0rBHdB1CtXMvpFKJnG5F14K35If%2BkiI5MIMhqxsD3EUoOoFPEVOyina33tUcmGDDDDrRGgBZVoMTVGBX228RDCkSwSkSIQvCM2WPKEa0Z2TPUcc0jJPP91jh2QfYb6cqW2WJgk6ew8b5QeyqJl6qW4PEZCWjNmrUqFNWx4EmpXhKNiRN4ZpR%2BLvylufagzU5129fsUXSJuNH1i6ozZLZzqV7829xL8oqJxNTFTci6K3d%2BJTUKQoF6of4n5YM0A2wCnEjV1x4D0Lpv1%2Fz6KVqEmIw5fGCvQY6pgFffhWIBdkG2I55dAkVy%2B3qhfAHeAmWZfwsvkBOjjPUuPNyVkr%2Fa9qWNEhr66vQH%2F0P%2Ba3IzlS9xhRh%2B4gI8RdCYdC1xlXbbGXhD8fARf3qRp5ee4x8054TceEz0PQY%2BfwnMXz1HRQ85zAyTUpfrrzOVjoTfTBR%2Fj5ZdOEgK2L46q%2BuYbDB3v96D8JCShWpLXQ5hFSUmrJUHNqAyxso8BFHQWI7lbCS&X-Amz-Signature=bdd287b9f452133e648a2169fa73e13509e1a66eeb392afde9b1bc7bd42edac4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Steps to Implement Binning in Python**:
24. **Determine Bin Dividers**:
	- Use NumPy's `linspace` function to create equally spaced bin dividers.
```python
import numpy as np
bins = np.linspace(min(df['price']), max(df['price']), 4)
```
25. **Create Bin Labels**:
	- Define the names of the bins.
```python
group_names = ['Low', 'Medium', 'High']
```
26. **Apply Binning**:
	- Use Pandas' `cut` function to bin the data.
```python
df['price_binned'] = pd.cut(df['price'],bins,labels=group_names,include_lowest=True)
```
27. **Visualize Binned Data**:
	- Use histograms to visualize the distribution of the binned data.
```python
import matplotlib.pyplot as plt
plt.hist(df['price_binned'], bins=3, edgecolor='k')
plt.xlabel('Price Bins')
plt.ylabel('Number of Cars')
plt.title('Histogram of Binned Car Prices')
plt.show()
```
#### Example Code:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({'price': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]})

# Binning
bins = np.linspace(min(df['price']), max(df['price']), 4)
group_names = ['Low', 'Medium', 'High']
df['price_binned'] = pd.cut(df['price'], bins, labels=group_names, include_lowest=True)

# Visualization
plt.hist(df['price_binned'], bins=3, edgecolor='k')
plt.xlabel('Price Bins')
plt.ylabel('Number of Cars')
plt.title('Histogram of Binned Car Prices')
plt.show()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJZ4YDKA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEWi8CH4ca222RkkkrhxuonGefUg3xWqB1sWLZY8RSPEAiEAv2GnWelup9%2BJBnJOTolqkx3fnhSKw%2FfrOh3BKHfGBsQq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDOoE0yhi9EIhLaYfkSrcA66b3WGYzSFkHcGnJSRCDn%2FJ4pkDnieCMd75vrkzxhWwnjylG1AhIHdnGXnWju%2BuqsQOVyPKzlrVlBe2t9goFnHjZSLXLACLxNqBJ9thqwNEgY9I7PXRXsconSAsOSgqkJN96sqhY%2F958CbyjNj3Jq8WKA8oCD2mZb%2FTsIN%2BkjyXOqJeJz%2FIUAIe5MTYzx%2FfkOpe4HWWzuGBxtj95swj8VENR2qZOA1ZeCKrwv6J%2FlfZlqW4UJ7jfmb7jyx5%2BhGg77Hcm5O600LSPl8%2FD2UhIBEVGEvNRJVnyJWJwMojvjOEyK%2FkYpzVqa58oqxRM0XwRVgdU1iJ%2FAF2017dSm7tSIt%2Fiv5e4SzDjCd%2Fm2W5ztPPK7o%2Bj0Yjz2FVEgZWh3kQKHrdohdkIp7UL9%2Fz1xaaUHtBvN7iUWKWPFgIGnq%2F46m%2BS%2B2RMACB%2BZ7ciswPwG4p%2BKgFeQEkgQv5NlXWQm6ulwzK22ixoQ4uQVT3mmPq5sEOZe2Q41itiu0fGV8ERbM5ssmf3XSihSjzRUsGYKmi%2Frg5mHBIJRwebBeSJCtpuY8IrVDF1i2T5UqqOkpWfTeYOCZF%2Bg5%2FeA4kf79gTkYrwznnxjGG1hqEmom1vzgIXo7ro173PNogpwheMVymMKzygr0GOqUB0KH2sv1hgLSQS1j9I9eLQb6inCPDCAQlV5zH1qU1dchvcH86gkZ9nRcHlSWL%2FQwXOeA9yRBgFHDCiNwfLBlfISiaB2k6ON%2B%2BCpWc%2F%2FK5qVqEJzbFbl9%2Fq%2FyApMq1POiX2rtVfDtucvZ2xl1O7CT8T2z9d1RH%2FVelfMYq7FnLI9lWuovqgIPXdsNy7jwg67nfJGoQKGQDOH%2B2MejIa74QHeamgOQM&X-Amz-Signature=bbb3f7ee70fdc8462de4e2f9fd026419eddfce5941715450a13afe5903a3c346&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Conclusion
Binning is a powerful technique for simplifying data analysis and improving model performance. By categorizing continuous variables into discrete bins, we can gain clearer insights and more effectively leverage statistical methods.
___

### 5. Transforming Categorical Variables into Quantitative Variables
In data preprocessing, it's essential to convert categorical variables into a numeric format that statistical models can process. This process is often referred to as **one-hot encoding**.
#### Why Transform Categorical Variables?
- **Statistical Models Requirement**: Most models require numerical input.
- **Improved Analysis**: Converting strings to numbers allows for better analysis and model training.
#### Example: Fuel Type in Car Dataset
- **Categorical Variable**: The fuel type feature has values like "gas" and "diesel".
- **Goal**: Convert "gas" and "diesel" into numerical values for model training.
#### One-Hot Encoding
One-hot encoding involves creating new binary columns (features) for each unique category in the original feature. Each row is marked with a 1 or 0, indicating the presence or absence of the category.
**Steps**:
28. **Identify Unique Categories**: For the fuel type feature, identify unique values like "gas" and "diesel".
29. **Create Binary Columns**: Create new columns for each unique category.
30. **Assign Binary Values**: Set the value to 1 if the category is present, otherwise 0.
**Example**:
- **Original Data**:
	- Car A: gas
	- Car B: diesel
	- Car C: gas
- **One-Hot Encoded Data**:
	- Car A: gas = 1, diesel = 0
	- Car B: gas = 0, diesel = 1
	- Car C: gas = 1, diesel = 0
#### Implementing One-Hot Encoding in Python
Use the `pd.get_dummies` method from the Pandas library to perform one-hot encoding.
**Example Code**:
```python
import pandas as pd

# Sample data
df = pd.DataFrame({'fuel': ['gas', 'diesel', 'gas']})

# One-hot encoding
dummy_variable = pd.get_dummies(df['fuel'])

# Combine with original dataframe
df = pd.concat([df, dummy_variable], axis=1)

print(df)
```
**Output**:
```plain text
     fuel  diesel  gas
0     gas       0    1
1  diesel       1    0
2     gas       0    1
```

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJZ4YDKA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEWi8CH4ca222RkkkrhxuonGefUg3xWqB1sWLZY8RSPEAiEAv2GnWelup9%2BJBnJOTolqkx3fnhSKw%2FfrOh3BKHfGBsQq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDOoE0yhi9EIhLaYfkSrcA66b3WGYzSFkHcGnJSRCDn%2FJ4pkDnieCMd75vrkzxhWwnjylG1AhIHdnGXnWju%2BuqsQOVyPKzlrVlBe2t9goFnHjZSLXLACLxNqBJ9thqwNEgY9I7PXRXsconSAsOSgqkJN96sqhY%2F958CbyjNj3Jq8WKA8oCD2mZb%2FTsIN%2BkjyXOqJeJz%2FIUAIe5MTYzx%2FfkOpe4HWWzuGBxtj95swj8VENR2qZOA1ZeCKrwv6J%2FlfZlqW4UJ7jfmb7jyx5%2BhGg77Hcm5O600LSPl8%2FD2UhIBEVGEvNRJVnyJWJwMojvjOEyK%2FkYpzVqa58oqxRM0XwRVgdU1iJ%2FAF2017dSm7tSIt%2Fiv5e4SzDjCd%2Fm2W5ztPPK7o%2Bj0Yjz2FVEgZWh3kQKHrdohdkIp7UL9%2Fz1xaaUHtBvN7iUWKWPFgIGnq%2F46m%2BS%2B2RMACB%2BZ7ciswPwG4p%2BKgFeQEkgQv5NlXWQm6ulwzK22ixoQ4uQVT3mmPq5sEOZe2Q41itiu0fGV8ERbM5ssmf3XSihSjzRUsGYKmi%2Frg5mHBIJRwebBeSJCtpuY8IrVDF1i2T5UqqOkpWfTeYOCZF%2Bg5%2FeA4kf79gTkYrwznnxjGG1hqEmom1vzgIXo7ro173PNogpwheMVymMKzygr0GOqUB0KH2sv1hgLSQS1j9I9eLQb6inCPDCAQlV5zH1qU1dchvcH86gkZ9nRcHlSWL%2FQwXOeA9yRBgFHDCiNwfLBlfISiaB2k6ON%2B%2BCpWc%2F%2FK5qVqEJzbFbl9%2Fq%2FyApMq1POiX2rtVfDtucvZ2xl1O7CT8T2z9d1RH%2FVelfMYq7FnLI9lWuovqgIPXdsNy7jwg67nfJGoQKGQDOH%2B2MejIa74QHeamgOQM&X-Amz-Signature=92f83ea32048fc727a443903dccb9d730658607d6dd7c76b864ea7a32f93aa68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Indicator Variable
**What is an indicator variable?**
An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning.
**Why use indicator variables?**
You use indicator variables so you can use categorical variables for regression analysis in later modules.
**Example**
The column "fuel-type" has two unique values: "gas" or "diesel". Regression doesn't understand words, only numbers. To use this attribute in regression analysis, you can convert "fuel-type" to indicator variables.
Use the Pandas method 'get_dummies' to assign numerical values to different categories of fuel type.
#### Conclusion
Converting categorical variables into quantitative variables is crucial for statistical analysis and model training. One-hot encoding is a simple yet effective method to achieve this transformation, allowing categorical data to be used in numerical computations.
___
## Cheat Sheet:** Data Wrangling**
### Replace missing data with frequency
Replace missing values with the mode (most frequent value) of the column.
```python
MostFrequentEntry = df['attribute_name'].value_counts().idxmax()
df['attribute_name'].replace(np.nan, MostFrequentEntry, inplace=True)
```
### Replace missing data with mean
Replace missing values with the mean of the column.
```python
AverageValue = df['attribute_name'].astype(data_type).mean(axis=0)
df['attribute_name'].replace(np.nan, AverageValue, inplace=True)
```
### Fix the data types
Convert columns to the specified data type (e.g., int, float, str).
```python
df[['attribute1_name', 'attribute2_name', ...]] = df[['attribute1_name', 'attribute2_name', ...]].astype('data_type')
```
### Data Normalization
Normalize values in a column between 0 and 1.
```python
df['attribute_name'] = df['attribute_name'] / df['attribute_name'].max()
```
### Binning
Group data into bins for better analysis and visualization.
```python
bins = np.linspace(min(df['attribute_name']), max(df['attribute_name']), n)
GroupNames = ['Group1', 'Group2', 'Group3', ...]
df['binned_attribute_name'] = pd.cut(df['attribute_name'], bins, labels=GroupNames, include_lowest=True)
```
### Change column name
Rename a column in the dataframe.
```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)
```
### Indicator Variables
Create dummy variables for categorical data.
```python
dummy_variable = pd.get_dummies(df['attribute_name'])
df = pd.concat([df, dummy_variable], axis=1)
```
___