

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCCC74SA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvpG5Kx1wUhkDf7dK2jd%2BYmiRGZdjQKcNeCK35cSNogwIhAKFDAtOno%2FGFfczzJlRhJHeE3HkSiH%2BYZkkrE2V8JS3LKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0XRro9Pdsv4Jd%2B4Qq3AN1Bryiy0WgZYSmgK4zy3QG35AHg1Qta8h%2FIzZ%2FBiPC64PPNuxV6NXG3qtgCShEGgvCME24G403pOR3hzs47k61SL3h3%2BU%2BZGYncIyg3FGXDHe4bGHke7E8Nby0LNv3pt4v32LUOFL3YBgTJFeqMvzgoMC%2BdwwucvGikKcar786T1%2FT289IfnsBDC%2FfRNDHobMwLmLfh%2FB0%2FTN6QlbHOPJAm2r78EOh5smp2jh3aLl7ucpIMJSzcsruNq9kvPiriw%2Fu5nhtmLxgycHfAMFGd%2BbilEiux9I5DdgMYSVJMXeSYI8BKPYJ%2FtGFsOVOFHVtxt%2FPqRYwDzA22MNCwerkpH9T8k3XmVzKDu8qgHXoW6B%2BxoNnUL5JcHhgdZ0ToUNPdVtIdDdcpX1JV2U7qAf%2B5BcTa%2FjOeJiS7U605Qd7vFaULJetfSuhW%2BOltyQk2kBypPRaym1RFRufTQQtWnhzLKnKpkM4UdF7YI%2FusCts1tYtR%2FOrSDqqxZ5bVLCnK%2F6dByPq%2BOXCumuTTZ9au7p87QlHRLleoW6vMGNEfko7YfbiTzUtxXYuzYvpYCiG54hHfGWxPKzv%2FClO3kp7w1Uw52X1FHvMrVVDcjIpEgajM4TskjqCCwkdHci2mPGtNDDlv%2F28BjqkAZ6Teac2Cg2KTN8oj72qjGKUoOSY3rNn30PrImRiebZ5ifdW%2FKN5KeQuQReEynp4hCCJLJtKotHi%2FfTirKbqT%2BFTUTF671bd6ywqmcFkLzIXznmNws10mvD9%2FG0GTBzup0vb2UdQohpXN3GKYR4nTYUKJTAH6ylqugdz6DAxP7Vvh16ELUWoxSBbfRa0n%2BM7Rf6kCOlIuUq121ws1C7AgWKGHZt%2F&X-Amz-Signature=5a0928824bc2cd0f9441fea5d0a767f6c8e4abc6b046441cc780b1a150bf6215&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMBTFCC5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOv4O%2BxUiR7zqc4oG41ro%2FJiCpMCh3uDnCK9yFwyn4hwIgQcDahLhODjHXYLt43i13JNqqyS7AOddgn04wjFIsycwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnlOCxf%2FYhhywoioCrcAyGC4vKWQae9QHCRaSpbxC1LiGia6zHa2haezXmkllmkeZesBHl2nm1go1VHfzHs3mnaFBLUidLH43amMnOVP%2FhuNW7Vn1l%2BuLMs7zBwSBcxpW96nh370o%2B2E0CMvaXMqo4f%2Fnt%2FkjSOddvnmIpeGFor%2BxLwadZxE0KGxjw8c2xxuWQGDj8YO6pzoqXVN0T%2BxiydfjFZ32CdCSl3wHltiNNjLxxTzr7SMV9OB7ypt4UyRMLgY7VSq4ywk6cJOsvwfMmUJ9Y1q5lJib0NyS2DBkyjZSsE7jNekNg8TRhOeT7UlM70sAhK4LUhPNQBwIEOK4UHoViO4fP3eH7ymQH2IweRchIjt%2FvxCORuwzJq2T5wUgdxv25CVL5mMwbdb6P7bcEZJAQkB%2Fd9t8W0j8MhzRdN8QTUvkA75s1U87FU9uBH7Oale1HScpOKkieCVSqDTTFZ4LvupgND0OO1E81446Xk2izLVmXiprWjjDiv3E%2Bm8cL1rrRHzRdIepP6YoO1fSGd9RuI6nqj7Y92XwPainBmBoq%2BNrpsjRpCWEQN0j089ufPGMr9bmDVyPUqLzH5eS83jLadcwxM8eOUa6TfYwHcMXYJu5BQQi0JV2M1bnysMmndbmpcA5PadzTgML%2FB%2FbwGOqUBqjFNZFUieKf8DoPtWnB%2BSp5dlRZW1HSxnQau23u5asMyFPzcagrvyw%2BXFEbWzjtP2zIHH%2BH2cCUQZsqce6qIsap82ETCtvfzvoqjGlDCnKxuNxXFVtWi947ygJZnp5LvrXTVlNj65valm%2Fr%2BqS11HiJiVDyaJYfhaKKdQmWopWZLsi1YGQfyoE5IsI2cJMIeXX1Y3tyGqxq%2FhVwWS5FFfsfhfQz3&X-Amz-Signature=8e4166d891ff9c885012e9797cf6671ab60f8f79579ba8987f3d0cbf0e342e06&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ERXTLBV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8Jwt17uhYxKLTlvf9fVldA8Vkez5vYyWl2WBcHBm5%2FAIhAPIvGQ3EzavujjO0DwtSSOD7UF4jqP549M7TT83E3lpaKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwP2apow3T1LdCDzy0q3APrOD09z10GpM0T5B3BSffkGVoj%2BV%2BJgoJ6mIR54F68p4MAGPpWUvF4tHE2SZNCzORhfbcYAHHQahdf%2ByPvGsnyz2IG7U28ppJl1Qa4K%2FNybbYMWhUXPj57%2F6BWthgfoGCkCbNnpXl77uDvSYzfnY6aKB4gVt7SablIdHPYsCITqjOf5JKj1Cc9XEWqm1viqWROMgGIP0jLOsqgj9VD2FxS6ix5mUbMl6TIc2OMLUXwHuCP%2F40NB5CzNJxM86%2BaLVvrHtO3AGLnYWtlPgcANvuvqFdvyioCXTlx4mjkoQx9LmLMXSXOZ7j4TBzMKGjToAXA0uQ6GsuAP6J2cLdIbQxqMhc7JVkNHoewg6TyiCxLhOu9%2FacQWmbPXVFjDJ4OWEANIg4sYbc4HHVUVBAL%2B1U1fr9AnM3iWohO%2Fm4BZQfSlsACzg5VdjoD82IvV2B%2BnIDHk%2FTDER8IBuss8QjfHxnIBt%2FukFzDY9F8oe1c72tmjw%2Fl%2BlJ9XAlHS%2FOF5j8PkZtZT5uJd9ungVNud%2FAaW4O5eMnpo4eUPz2JU2nUpFpwZlqOOZfUNSteA1lDDiz5uFY1qHVppQrjaxNWiRviN%2F0etnSnqo0K2uUpeDKeCwOBUs%2FkNdFpVz0DCmUUVDCTwf28BjqkAaALt1sIkflRltf58Ac%2B%2BrTqDqU2fQD1ifLIebecOtZxusWkbEn3T%2BG8bpIIREZwuqr%2F34nTG9p3TpElhT3bVfF9rBRH9bAAb3r8sYeIyP8QX6VQp5xrKXRhFl4gZvDHg3SbMe78pn2dOY4lqX1cIAvAzm9zJ6T8LSnSPfMXp78VsN5uPVEWhFtADDFtqUKbRdRXp0qJiYIyq6IZzlPA%2BUcVpTjO&X-Amz-Signature=4e33fa3a243afa8ea5fd9ab0cf50b134cc31c90916dfa9b93c9755b6d1348eb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2Z3TIVV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8mo2uRt5Puj%2Fvs0qWUcqp%2Ffj1UeRIVNwRWUI2wzBltgIgURMfQKTPVhBHHCNcntxEUsuFVe6VYS0NZ1uz6cwjIkIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGuO%2BWgG3lFO03RNrCrcA0mJ%2FKturXNNlsp6DrCLTmfWZftbd4lb%2BJNgbS3ilVJip%2By61mBBLrivJxIXxb1WYSxAJD%2FdXLy4PBK4bQYjyjHnsco99dlLEZPAtLvHt1oStQs7Mjxn%2Ba12XMqKmHdmZM9laJT50d9LxTDGCKVG2%2FT19xsEgHTLbiFWyjZ2PRy%2FratsuQWNZUbo%2BoDKZfLDRz7dMkWzrFXI2MwrltfjZkRE4ZfMWOjSD%2FTvbkAa22mxDSnaI%2BsHunTabNYSeNF7fCntinrKSYl%2BlP9ZpINDE8L7NJrgQo%2FGvQBnunFKu6qYXclWhNPAu457fxUHtRBZXftnxADQJiqqRV5ps0LzhpyOqqYxgmx1OO5A8lRIKV5%2BnwMSginleftsk8wEF%2BkfC9uqlcoxpOltTq9VSSdB%2BwQnWVQ%2B%2FaoJBnoiFmgNeGT%2F3LinwRgt4mX5C2%2Ff262oJe6QEwWR5BEx%2FNE314n6Nzl8C%2F5jqIObGoli%2BMXhtkUjtaVbHfZwFHzMVuxXH%2B5JAFAV9%2FwB9%2Fpa%2BMumnXS2ocFe5l5C%2Fgly5qccJ14v%2FbWyq5EIpjTcCHTDZa1%2FxlNXlnaPUqeT5aWzmFMhM8gohJx6LlakbcN9TsQsH79OXnAIxKdbtNRFdUORgRREMLG%2B%2FbwGOqUBWs6wxPF1N9Qy8GuR3MgyNCgqfNYHfi4YO3CR8bmiQJsw1AeRsn3F2Zr0hruiwY5yRMLRHgePAb4GBKxUJFt578YlIoY%2BS89wy2gWSO1gr9Z7g%2Beme6LawWNh%2F4Fgj7wUj8Udm3Zlrl1EyASEHt%2FqSvklj1xED1gadUiiZgadOy4zpQWjNXhXztwVFVBrqKHDiMDDulm6KVE7caqu%2BqHHn%2BiuCbCS&X-Amz-Signature=f9c2295c3c12063348f7c1452bd3b85b3cf0db3348f6755f89ba287143a1570c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTNPYCUE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBx%2BKkpFGN7cPRH5zql8gPzPiCDw%2FP9yTFmBuYRJFHVLAiEAoTcPdynM%2FASvAydYw3A239Mf86Pb7ILoK0eDkVGtuXwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBgx2b%2BM9FHOhsMayrcA6F%2Be7N5hOdeyIXCgQH5t6%2FEUhX%2BBp%2Ftml%2BGNPKfVe6oksVQbIBhIaRhNWtmrIScyWO8aKgIUzyfBtJb40V7hjdn6U%2FFdrao9nt7wg2ndr2pDtY9wRrsuMKDDvwkkeY6LPtX9zBTDxQhZnPiHkscNzpzUZBJjo3va2f%2BOq6lKQWDmcSXTCJprga9CZ11v9wDnpddNnROyA4QtLdT%2BFIkaVe%2BJsm1C2I9ENmrppLEuWnD%2FsZcjpNO4jjugtbTcajPvQsg7em2ZlS9NJrnlZo3MAst4YG7y0CEDxE0UdU63ObHE6xwRH031j3Z6IRvj2js%2BBHqK2EcVQcsjX7GDjftouXaPW5cdjr0qKSbVTmV69IyBYTAXgWZ%2FHe9qQmQph%2BCsz6MqLJ%2FlydOMaXo70x%2BrVkT%2BS2Smq1XHO4QWFq4PRaB4mdwJEcakAGyIomCQ3Og8TofTmfbDcF0Dn9u%2Bh1HVgBBqKdE9YOvheLIlV1GSYcR4th0Mmp4BAE6qSHnzrongE7sVoVaYC5jK4IwPzJZ6KgmzdAMyBP%2F0q8ExnprLud%2FoVD1I%2BqklQlOqwfoHQ%2BCb5%2FWQ9uFCm72%2FnpBFfTT3zWuPELoIQF2E7r9eoWa7pGvqqBnfRk%2BF3s5pFplMM%2B%2B%2FbwGOqUB%2BTxPE1PErTc3QfhxaMRoe8PLq%2FEY4FpiE8UPKZOY62KsiFatU%2Fp9PnfqBaVx7wnUoxjW4n1W1ey%2BUZrb9Pludi1YZomep%2FUc0epxJrfSOBEQWZVhD%2F2r47nFo4Co3O5okmxBMefxbPxQ7HsYX1GgqBTXr2g43ObAFFVX1JeAlGG8NpomNMLc2yx%2B4pB6zaY%2BitiJdt31tYlSSRxuQYKLgUx5MDVi&X-Amz-Signature=dbbef3f1bb119b2b63ab26eb39925bed0e275b7f3fe437936b2ce85fbdc1ecbc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LSQRWEQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnJBz7Vkwbjt9AfRbJvGJkOHGiZmNFmoOZWCXtiRYfSAiEA9PjancyVUQkXgqPHJUpBDwtR7fO7JDmWLcBifiO7B78qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKAG5xzTk245a7SeMSrcA6ghs0PFSaru6VSNYZCHDiculOURF%2B6I3Esk4%2Bkkiz6QF4i0VTq73vcWQwrNJfUGwmaueYlXyBL3REOh%2BQCbNN%2F%2FWRfLrAgE5tCGhYUYe%2Fr0U%2F3zce7y2sumzyzNREXM%2F9wMb5ibsVChtL%2B3L4Hi4JFwTCCZooFmMkcCESE%2BuAf7f3uF2gZV%2F%2BE58KML8f5Z3kUJ7XHPCyakqT4KfJU4hQyRdHpMJnBwvKDuLh4PDZNO3VCHpdSmcZc4Cbm4X9tOcHS4CVXU9kD53WkyaDJY4IbV0XSo%2BCaHKSztOhMPKMz5lBF3ETAdBUB8IXKJs1esB0liBEqVVSIgTi6t%2FJMSp95hF1zNJDVruYTqt3NvkGTw6%2FBC3Hy86SkuzQ1Z5zzjFVl%2Bhvdwb8XvKKQgwGWJqeF5jL9O6Qypr3AZCDxQ6btojkIqHQWycu6wIdDhafv6cR8iIFLKSYLjMaoiZUt9YbZ2rRn%2FsB7jT3GoZ%2B2KG%2BzbxgEuNU6fLPrOD5An46dwS3HG2Qkbf42eZEjS1%2BUU%2FzsTNBqUZ58xuxXJS4bFDI%2BSfJj1Z7ywNWkZarPgV0ai9MTj3czdZtV080aBIxBfe5gAYc99FTrYO%2FXSZijhb5uMBPiAbcEgy2AFhvATMLi3%2FbwGOqUBWa0aVspjBRgu5HZWg4i4sR3oA2iwVzqQxT27%2Bpr5xmm2Mi1juj9fdUOiNnc7hlh1%2FGP32HMjw24akmwwg7aDjldoRdAsf8Ndx3zw6PCzCBnn1Rrnz3f7XA2rRZBSm%2BTjWW%2F8E2rX%2Fpc%2Fi4GXcxRVDX4X2eIH4boqRxCK%2B70sPe54CwPVQ0zKzMc3uOWnAz6S%2F6esTuRF3wZ1uWaaz6SyF5VOFdt1&X-Amz-Signature=3a40563b8047aacc41c62011cd2aedda0b629e225a3d56b3c4aac2ee899eabd3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6T3HCNW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCZaCd5dXQ5OK3nBUJquJR1y0qwGKYE5fO2sHxaBnRHQIgfT2WlHrSJS0hbyRS3P4rUWVIs6r0yuqIj9NQGWUs%2FC4qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCA%2BdniW5DytGWksircA14nH6oH8HczE8BvK9kOIm8DARxqmd786slpjEuoW%2Bmf6D1qGMVd564AFmFy7gZzRxsh%2FMI0ln3cXIDyyLvkZdjg2T%2FWrzALwgXUyqpTmvPaUHn8XXK4pLd61uE3fkb2jnNterEUS9Grf2r%2BVonn0MiN6CrXl%2BPNw5bQPMuIXZF8JRFJIEGyuFICvLH%2FG9KELXx6o9fxdqzKffzlgMkqufI00gJI44jQbGjWrWekoEYCqg49viuAiFI8VGScFOvejJhM6wXszFH%2F6o7IcMFW4OogaJ1VrMwAEd%2BxkooSFT1vARw4mq0RfRSAfM34dL8LtHFL0MQAD9Dn3p6z3%2BHxjSxLFnJWoKPtdaRwEzNnnv9hfQlJW8OhgScXt0qhznnAf%2BWbi5AdevOmAy0HtfuPVF1HAKjU1mZHLklAzsWzdrZ0Bym8xoGP7%2FZZ%2FqSGywZ%2Fg5PczJBDSIqNFFaLcL1PALPy2O%2FfaItLDxxlRp1Kbg2qei9uyat4jovnXFg0AjVvcplbMz%2FJzQc3Y50g3tKN%2FRKwJom7V3EjyKYtmMXqk8jBbY01jT%2FL%2FZeQ3I6jAK18v9wenhVjymxSfffeGw3mAhdjD64G%2BNRIDMyOfzqwbELr%2FjHrJMqxU52aJdGLMNu8%2FbwGOqUBE2kkx2XS06enu9QH7NX%2FPnzei%2BHUEfHYTICqopSKxfGekrDo4Nv2x%2FGKZSRM6k8h%2FTuPRDQtGyEin72vSF%2FAxQ1zfUGUXHffbBzkVOvcu8Z0XcH7jkFd790g2r6x%2BZi4j%2BsGj%2FTKTMlB4CgVVuria4ebhe2GO2tJkhBGFs%2F7ghmBK3n9vnevyWNMGBPOkkATw1MXiuslEX1XH4RNUH7AWP6sYnzn&X-Amz-Signature=8626f8c97dd0797bdf393248e5c3b7ae585de06291e8af1d294c3f876faabf90&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVHDUCSX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFO1pa2%2Fc2nxc9rvAALsG%2FTTgP6alT7TFoatDAiUiUSdAiEAsVeHrzNA2cko3Ie3jIhviuZaNlFuDq6bmYy1aD0izyAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNa%2F%2B0gtKVHocMd31yrcA5QwM9UI4WhZVZYoRmfE%2BIg%2FXXdsaF0NBLqnw1qehLv1KrEX8ytrQ53vgBUkAVb4UvRBrnjv2df4tClEXZwKgvajbnoI7ls%2BxEG534M%2BkljHu37pkiGcm7%2Bn5Mld0OUDdRuH2UYpAqjvFhUyA5sLCN9myTgK8Dqr60xpTPyeWCymxvvGkZzjOMAL7uBMSdMrW1nuQcxzVL8wDeqLUwKG2J4yXxq3bWF%2FU0mFwKVU5EbcQDmC0IIs0V%2BpjLo02stmVzOqTgthQKp3sgqQj5fFlrNhOkoMzdMZ5I1i1sSgNxRhMquRAF4A8eiQ%2Fm2xf5SC84d%2FqnoCpxesKZxVhsB2z%2FKOPGmG2mJblw7LODbI90QC0kWUJ36iw%2BwZ3B0t78U%2B7xfjd%2FaXTYMu1R15YBv46LVy%2BhxGHof5V198UtyrsKY1Z7EqaqbRYO9kKyehDGpLgvDBAOsDNXSMMjSvE0k0Hp8msLzGvBYtqlbgiAWEJ4geEOGgW6MjAn39g4uUBPc8e7KBQMmdmflprNFO7XQWwa6v2s3b%2FrX6h7SaC0lYBfr9kCOicafQKbljOILh8pzrZYD7Mb%2Fq5vfAbM9WDnvBI%2B0vXb3cBh0nt2knoH7cyBGtOkLpc%2B43l8gbPBqeMPa3%2FbwGOqUBIeMWp%2Fcy946tnp8H6ZebL3%2F7BH63058IgchFYPbbx%2BIFnji7hUbevQ8WUSJ2J%2FgwAhHG%2FkUwA11uyyQlUJwEhbv07AIkZBNxQKQzVYoJvNv5tTSvAg%2FuHaOGEZ2bAu6DPhQEHn9w749qDSg%2FZnAQXuLAi1C5cjXgZF%2BG3C4Ky2TTNxsDPlYQIxB2s1lSmkvi1vwMyOszVFRruYbo8NktVsDU9zuy&X-Amz-Signature=cf819828c1ff2a3fbd6016e67cbb96c0c9da1c3fad40e8ab31a17286a73f1060&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTNPYCUE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBx%2BKkpFGN7cPRH5zql8gPzPiCDw%2FP9yTFmBuYRJFHVLAiEAoTcPdynM%2FASvAydYw3A239Mf86Pb7ILoK0eDkVGtuXwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBgx2b%2BM9FHOhsMayrcA6F%2Be7N5hOdeyIXCgQH5t6%2FEUhX%2BBp%2Ftml%2BGNPKfVe6oksVQbIBhIaRhNWtmrIScyWO8aKgIUzyfBtJb40V7hjdn6U%2FFdrao9nt7wg2ndr2pDtY9wRrsuMKDDvwkkeY6LPtX9zBTDxQhZnPiHkscNzpzUZBJjo3va2f%2BOq6lKQWDmcSXTCJprga9CZ11v9wDnpddNnROyA4QtLdT%2BFIkaVe%2BJsm1C2I9ENmrppLEuWnD%2FsZcjpNO4jjugtbTcajPvQsg7em2ZlS9NJrnlZo3MAst4YG7y0CEDxE0UdU63ObHE6xwRH031j3Z6IRvj2js%2BBHqK2EcVQcsjX7GDjftouXaPW5cdjr0qKSbVTmV69IyBYTAXgWZ%2FHe9qQmQph%2BCsz6MqLJ%2FlydOMaXo70x%2BrVkT%2BS2Smq1XHO4QWFq4PRaB4mdwJEcakAGyIomCQ3Og8TofTmfbDcF0Dn9u%2Bh1HVgBBqKdE9YOvheLIlV1GSYcR4th0Mmp4BAE6qSHnzrongE7sVoVaYC5jK4IwPzJZ6KgmzdAMyBP%2F0q8ExnprLud%2FoVD1I%2BqklQlOqwfoHQ%2BCb5%2FWQ9uFCm72%2FnpBFfTT3zWuPELoIQF2E7r9eoWa7pGvqqBnfRk%2BF3s5pFplMM%2B%2B%2FbwGOqUB%2BTxPE1PErTc3QfhxaMRoe8PLq%2FEY4FpiE8UPKZOY62KsiFatU%2Fp9PnfqBaVx7wnUoxjW4n1W1ey%2BUZrb9Pludi1YZomep%2FUc0epxJrfSOBEQWZVhD%2F2r47nFo4Co3O5okmxBMefxbPxQ7HsYX1GgqBTXr2g43ObAFFVX1JeAlGG8NpomNMLc2yx%2B4pB6zaY%2BitiJdt31tYlSSRxuQYKLgUx5MDVi&X-Amz-Signature=00e851233e10f52cb0fdf5e1e8a45909b9d51beba0eebbefec3d3bfcdf37d9d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7AMSG6T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnVSn3VU0FdLSsOW%2FgKbNWQBtigTC%2BC4DZbIc9GQcC%2FgIhAKAxUgMabiFBNyWy96E1iIHOQeUGGavuaal%2FrXX1voUEKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGLyWWn467H9M6BpYq3ANxjlKuabSQbuiGF9TGo8ewUqap7sVoMyQ0WqfZU1noOxPAUFhFUe9lvXbaiDlxo%2BjQGX%2BKRYeCqgjtKVWGKge881MHIrD%2Fqg%2BHU%2B1OZodUJCJRyjUxCC6aNb68Q0zlhnxs01xQg4GSE2igVhWaM8M02qbnCAU%2BZxZir11tVXv71ODIZuWwCbE1gP9vJB17Xv5lN3pwRFC%2B09%2BxFRnLvJjjTp73BKhfaVvNMHAIdK3mtPTbHDMVYbuDM63GiPZo4DgnuiXji6fXPZV5%2FN5gnJv%2Bchfc1oPvrrXw4lz%2Byr3W5Xe1Ojpo%2Fq8SrBhfxPDXOxTRvZjr8VBE0WoljRpt8qq9RAs5YidQ1PEhI71GPz3e6S3NdGUMFc%2Bl7WRUUw32w3750zrHlLVIqtRzvXSkOk%2BlYIoPOUkHoUipcQp8EQRNqppqPhetbXxiuvv8YxEzYQiIPGLsnUdhFPfK03YhxwcwLGcgn1h9PE9zKuGMdswJOYjgO0uv1sq8OstfdZocQtxUUWFqn4TjzqY801wRyi60Gp9s4%2FINZ9MIDIyN79hgq%2BvDVvuFcrT7EtjVefvOE6D6UPlefxjbDyUb2qI3sGQNjhTP3r1qfz7xq55s4r2j7fNlvGFIK9O6785RmzCJwv28BjqkAUqdNOxLhxBtgVTa359K7bOf98phLUwwmjRp69n726byEoEtZXi0aAcPEOMjc5HPOi9h8K0ixxDdWPiGGsiTfEvTEehdVUavxOnslYtb2jNvbWPrf8fcS02IrTBBnjvb%2FXUlcdZbB30sSKx3E84iZQ4KLqhdaEqbqhTq8d3eN9JKNrxVKqDtxFwLamhxEM7KQEjX0GXtSSm7gmIinorZ0HnlZS%2Fe&X-Amz-Signature=cd96998863a239df6fbed8b597407d155592e68f2f6cbbad800c0171a414e878&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7AMSG6T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnVSn3VU0FdLSsOW%2FgKbNWQBtigTC%2BC4DZbIc9GQcC%2FgIhAKAxUgMabiFBNyWy96E1iIHOQeUGGavuaal%2FrXX1voUEKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGLyWWn467H9M6BpYq3ANxjlKuabSQbuiGF9TGo8ewUqap7sVoMyQ0WqfZU1noOxPAUFhFUe9lvXbaiDlxo%2BjQGX%2BKRYeCqgjtKVWGKge881MHIrD%2Fqg%2BHU%2B1OZodUJCJRyjUxCC6aNb68Q0zlhnxs01xQg4GSE2igVhWaM8M02qbnCAU%2BZxZir11tVXv71ODIZuWwCbE1gP9vJB17Xv5lN3pwRFC%2B09%2BxFRnLvJjjTp73BKhfaVvNMHAIdK3mtPTbHDMVYbuDM63GiPZo4DgnuiXji6fXPZV5%2FN5gnJv%2Bchfc1oPvrrXw4lz%2Byr3W5Xe1Ojpo%2Fq8SrBhfxPDXOxTRvZjr8VBE0WoljRpt8qq9RAs5YidQ1PEhI71GPz3e6S3NdGUMFc%2Bl7WRUUw32w3750zrHlLVIqtRzvXSkOk%2BlYIoPOUkHoUipcQp8EQRNqppqPhetbXxiuvv8YxEzYQiIPGLsnUdhFPfK03YhxwcwLGcgn1h9PE9zKuGMdswJOYjgO0uv1sq8OstfdZocQtxUUWFqn4TjzqY801wRyi60Gp9s4%2FINZ9MIDIyN79hgq%2BvDVvuFcrT7EtjVefvOE6D6UPlefxjbDyUb2qI3sGQNjhTP3r1qfz7xq55s4r2j7fNlvGFIK9O6785RmzCJwv28BjqkAUqdNOxLhxBtgVTa359K7bOf98phLUwwmjRp69n726byEoEtZXi0aAcPEOMjc5HPOi9h8K0ixxDdWPiGGsiTfEvTEehdVUavxOnslYtb2jNvbWPrf8fcS02IrTBBnjvb%2FXUlcdZbB30sSKx3E84iZQ4KLqhdaEqbqhTq8d3eN9JKNrxVKqDtxFwLamhxEM7KQEjX0GXtSSm7gmIinorZ0HnlZS%2Fe&X-Amz-Signature=43fc0ab3408396ec99bbb877fb97b1b633e695666aa0cff8b2755a25689f47b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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