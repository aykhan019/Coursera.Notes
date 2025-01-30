

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EL5P73Y%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHzGpI2n9dgEgfoZPfT2rK9fAzBRhj0aWePhqnP6luWHAiBW1oGqtBSCJRYIwPrFgewZA1d5Lj8yqoqBDWBdYhAYLSqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7LPgNR64etm0Jzp4KtwDDTz0Q3ewWHxBpg8CJFoXjcQu9HsH9o4AYqVQ%2Fz2lPuqQLcq2ILrK2AyOvchv95KMns%2BeuflxpICP9QUJUnfaCBb6d7pmiUVmpnRPNL8CP9af1meeYu%2B1PWjmcFm7BpwUIh%2FplpUjXpafb9ktieWCU9NZO3u7YtFC09FZzEOMX4O4XTLZTEjbtZczDQRQxv3lZXnbkDtRPS%2B%2F5HXomlPGDiIuRv26btzaudz9JGoIR6bSlOp7TGYEotgSykaQQMHhP1xWTKYKj2qeQMP7xXgKAd5AtEc0TduiCBcDk%2BYMQ%2F0tEkRwIZ5O1mwfbW7ws5FjzXHQoKNETylNfgoh7wFWgVLNTSu%2BoYn9rHpawPXXDcbsImzGg%2BSPcKsPKv4pBAGD9lrVXHk1S81fl0kLJGeiNu8%2B0lvMS4D8smVCSi4Krs%2BRwwW3%2B5ZSyivQsaiAmq3rndaHmh9puSFmydN4eXMQsaqsrspEar2atElUPWuYj%2FKTJ5%2Bh9izQyvM6Xs%2Bk%2BHi7xeia10xuh7NQVrPY%2BTtiCJQ%2FTwCQTU%2FQTOkGtDiwl8Yp78E%2B%2FobF6EEyr74ozFcvkPH%2FXVqY%2BMpEx4JBJbBPLSPOAWP%2Byjb%2FPSjylJxh63EtIGnmVKDlwDQ6sbMwss7rvAY6pgFaDGjTDBTI49fvvpRX1gc1iFB6Al2TEMxJNmEalA%2B%2F5yQ3cJRGaoS%2F1%2BRJP9eC46kyD3NZ7yj94iynLLGGuPCPrK1yn5MXRorewiitU%2FVVIIv3mn7b1rxQQBuBJg9k9zmHdD24lXxQssRNhUqOHr9EFzyY0i3QDBX3H6JceH9ppASH65PvxVFxu8BiEdkJ1sIOFPYj2VHz7EbPilbz8jdz3UKEZgl9&X-Amz-Signature=0db9b3a2a32064e71525af03a2c88c0130ac60afd0f045965400f3d20de4b640&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQYHHYAY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2B3%2Bi7sPcSK4mVP4lthw7cMLOpDGi9QCIgxRfQ0B7Q0AiBeg1A73sssSrsDoNNhDRcWACgUiAsnlRW0jI2%2B6QkMoSqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ5OD82PASFJnOCpcKtwDfXaszAJ%2BpPkhjP7bh0JjkV8wq61EGtAG1wqyHWbt%2FB5WjPhXouf4SXUEbDdOvr9JaVnelSk14%2FlhL%2BBKl8hcfPJTjENxJT9TNfeUc0I69b%2FEgklQV%2B7nGWfUlRiR3Emeis0EvRKxXP0ozO63iPhU8Md5jI2p9%2BYDJA2WryZ1iRdhyKLs2nUZolc%2F7gYfJ9ImFyNCHrWdaKlC3jvKWu2p2%2FVKdtGzcTu37uwsxzWNBMua1kRqsfk8xiMVUQs24wN2Dcs1DM48Y263KLSU1YJqdXay4qLyeiKiijEFmeAU6vCvOjvqRREWquCQXsLrNzjgOY38n9hu%2FOdfvRDrZdYMh1USDrB7chS9dbvZCMD69OooGR%2BK4uPu6McXR0x9nj8O%2FVUlaubwEN88Rux4UfZBpsATGRUf5MABI5U7%2FCR6VPUCgTvpFkOifyYdmt8MEUimxG4k5g3Tj1YZd0uA0R87j7lyMyKS7Ec%2BlZi2KQRowSHsQiVW5qETs1htpw99FpfkVpljMnSkjjSZ023Zgot7bLjIxpLrL2dZQueDwwfl%2FkCuob%2BQGrFre6zEEsuTs6B1iWtF1vBBxV%2FnYPybaNduTZT9IVsskw6bufHJUtnRrpoLYW3J%2F7sAZCwTAqYwns7rvAY6pgF3ZXyVYUEplLgFPgqq8vBWrr3leuiIxk078ZjjQi%2FUFk%2BtjOyb1zmGP5VSrejzxUO7wVljYMPQu1wKfl4YmInDqWvi%2FItMlA7QRSuBc5xs6RJQxZzonksxRTozEAskmcNN5ipQo3MunVeT1warLYi3wK7Yb9eEBVuco1nhVgRH1XncsQSRweR4vrprk8YU1Eq8YL8GNhd%2BimbJDvlQNf4O7yoXmJTr&X-Amz-Signature=aaabcf805358a7c515d3ccb2619ca3bd5d15b27b9b02cf10c889426003412cc5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYVDZ33Y%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB7ShBMLDC3syr7u4DyyeFauLPRHj7cA6A9pnhgA%2FayIAiEA%2Bzni1TtZVFFkXf0aTbNfK7dq0XQiKiIc8Ofmk%2FbOFEkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB2DQRKaJJXk8eYEdyrcA1hQXUObiK7pcLorTGd3SqEZmZk6Ep9q8iJO7vj5bF7wAkdS45swCGJIv7uPh8A1dC95D6388zYLbAr5tG3Msit22c1QYt8Up6TNN9eaX%2BUguH0vrPmA2t53J9xaWXjbTnwTyxL4CPPYJ%2FxMXw0ro8ofQxz4PdxKV7fRpA%2FQ0th1457T6RLoJsymVxAQZImsF7SLKjxS5R5S49FqhRSf3tJEplWsdyRS4EKvoaolhZGpnhgpcilXVrKy%2Fp2i8ltk16tnTGy5Pm0uUqSViola4V%2BPCyi1PgruJ%2BE2xDE5DtI4k6nJ7E0Ulb%2BgZlsQDWgfosNsVW67iqY0OVVdjkTHDBkje4HkDKcpBQIHKWcp0cQne9gJD0TP1EoWXMm%2BDbH6Kun%2BpMN%2Bj%2FRDbEMSNTxL7yassV8S%2BwVFw2t1fxqVLy3iRnWSY8WaOkgLt81RNNJUuXYStuNrLU1TOMmZOfwj5jVHAlneycTMAP1ESdLXPTci8AXGcwNwHjR%2B3Tn0bsHZautcgubMJZpen3ep97WN5RrJwHswAfq2o85i%2Fo3IlwndNEUPXVagfuuigS6zdg6ozbSuibMBl0W7muH%2FGYUM0Mo26WjilN1HRm6WQ1EEOE%2FWUJpvsZOYEEaNDKdqML7P67wGOqUB4wHJAFyx5dZFOjWhnHDq%2FQZ7KMVj2jq6zpL7khuToH1iscSXhlyjyhf8MZr8TUPvTscGBFPxmrpUcspCJs3%2FhzXAobJhYCLccrBJ57zfF%2BGZrp1vpYe8yfLmEEVCB%2FfyPVEyEe1137rZ%2BQWXvlZf9CsirpA2tjWiLb4SoTS1zhwfbICnAK4uR9PlYlPSlGZ0ybZDlx0XcEBLtGLpbm7q3yiMURL%2B&X-Amz-Signature=3bebb6aaacefa707e8a67f661dafda8a7863203e9f07ff2b33e4a74e14f65907&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676QLGDU4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDufK1k60Vi7tOIeLdK9VZeilQvAYtZfAssSIbgCN%2FlwwIgV5oANIXzweAjXxpzMzwjVjA2X%2F9ruBhkIdePMRZ%2BCScqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAhcQ%2F7aFOXS%2FLPs0ircA8u42XWbSuysIWjwYffCKZBzN5215FhZuwgTfU05Lix2ULIzPBFJ3PbrpFtFT%2BlcCGIU7AaounEEXiwpr4q1IiaFtJeYpiseARhvmWKnCGHb%2BvfmS3%2BZtcX3Tkap%2F8QKlp2f49HKgd2ipEG%2B22q%2FNzhsC5NvjsFY9uRVSWbQMrpwyTnMWI7XngnjxYEAYWs8qDMLiJVDvM81mRVpQjqoOrX76oQdOyEtLLiOTtYx7wZSkjlSglFfZZZ6gGX8SYkwey7e9YyPaSRfHAgtJvxB%2FYM1lGAk8lzRL2M9VBynHUOC4StIT04VhPSyumsdFfchFk77CuRFSa9Q4FJXAM3ED0hbVpUuxlKoyeF85UJdrVugcHlN%2ByAEomeSbChogZ%2F1Kfxa8QcT1eJZZ6SfbbuI5xihHWf2xaL9eiINLf7pSrir1hAO5GeeJh94g%2F4zRagwpXuQYDRPWEX1bLTjSfUxA%2B4UEBkejOtpoFLal9j3xMxBdZPCB4qUx013GEf%2BPbdDlW4gFHvo0A3edzXkDxh%2BeZVDSPwdh4peVJyee5Avgc7i%2BvsIVIUFd%2FHtM2uMIb0ES6OTLBg6%2BNThLA7FuTxXNRAqHQR72zxgfocmW0hdQnYvKU3Eqzcl%2BiBI7i8MMMPO67wGOqUBdhqBbnlU9nx5QDa7yhxLukg3mCcRdXgUBMqW95gnCGNxtOnJJBc%2F9jGEi9V2vKSIfLASgbUh26YLN4aayeGxYiGTfk0ehPFE3usI2RfRUf4otLDrE8cdec75yql7ApPtxGOO49Lmz7NwMsxkPAuFinGnb%2F%2Fg2UxoFbu6W9U9RhuBfbsh5QxeGpIjO0MHaCDRdPmNdPaWRcgpoojcOcKDuoPF5JKh&X-Amz-Signature=7075d0f87a4705e39bd8f1f5c5a969fef7c0d8004d2a2bf2cc922808c5667951&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJYYZ7P3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgdbwCRHDYZ27HbcgkYpqjcIXkYpgmZj%2BR6TvKGHuUJAIhANQzOhTQvPZYPrBv56RxxNAQi4ZnDLzIOeHcHFEzFOFmKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzv7HNp7u9vF9th2mkq3AN%2BKTgpkNdQF91Xk%2Fe3CeBmfe9rPM2FpuMFxpc9Z3NKRgoPjfmYyFPtSUW5f6y2k0IgDobqgBAIAKT7hicXWq%2BQWWeQ1T2GSbbflIDJzEF%2Fp9IWHx79nJ7tbURfXihhIZtBtr%2BQIj7pwbc23XFAG8DyKxNQgZeX1rTJFIInnpkegeCyb9fQbm8FhK8GnunxRZPyD4CgvTUkt5P8paCsMEFJk9u2Uy7SFgLOy9Q3JffYUnPj53Pfy%2BELXzUZD3bgBTu%2BpYPCZh39g%2FvhJk0BKRiseINaaPojI%2FH4br4ndFmQeGQPNKmXTfMDnvJxHvffuU1FqVnNbzQXl6MVNqYrt0X0o85sK1D%2B%2FGG8Pb5lPH3c671RCLJ5cC7iGQat2brjJ0DvFc5pYdsBeeFowZ09%2FFFkOHN9glkdhDYHdSaD%2BRvjwKyw8Kfa9byE6Qs3JG1b19%2F11x6EDXJu%2FKA9i5xHwRiQNh2f0is8o0%2F9pvjDXHgP6YuVN1Z3Xhf3eOb2DpC8k8xcO6N8NPnx1WvWY6g0VcyCtR9rrvTaG3v1iTuqQ3v1A6xWBhiB0%2FRc55N%2FALJJWEzO0vMOnDDe7zMK3g9Gp3n2Ytv5cKgJP%2FN4Oul9G5Ny%2BQZe2i6y2iges5WGxzCUzuu8BjqkAaxq%2FXy9sVLnwthT8L%2Bts0ob5wlrM9Q%2Bw%2FWeMvdsLnj2htaiqof81iQZ6vWU%2BqxgIjWZJA30zujShuv8Cuwq7jP7SZW1ITEJXWOTn8tjMWelCNChZSIlPRhlRpUoWcwUxV3UaGNbjvE%2FTXWmh4vIn8obofJ9GiQSiUDxD%2FT3Ulme6nlowYRvI6iHwcR3ThSg03MIpXH2e4NEjqBex3kcDXRPIdxA&X-Amz-Signature=f4ce876c131d9c985adc19066d943478a522883b7555928d4ea8d92966a62364&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626IAHXZ7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9bZQmSY2onb%2BXE2xLcArniUHogQVTUWVJQzGj5YBaQAiEApH9Tg0%2FcjCPBBXuMBpzTD13satZzbtUbD9ChGJ2E4rkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNJOb%2Fysn0tFtBywRyrcA4HemF7lpRuAutLCl5Ctj8ia%2FqHFrqSCZ3RxKDBZP3BUR94IPjU9UiRjvYiZIrhO1js%2FhGHfs%2FJ6xRf2ymShqh7QX75%2BNxggebSRdd%2B%2FXmDf8LVKFwao4OOr%2FwLXzC70SuTcA0fUjQcfT12Dy0eyLxJLVsalqMhUlRZw5JwJa7gkBXbyL%2BSrvZeu1veNiYxoY%2BiCRaKgev1Q4aGOwVVG4MLGwCqSPtG5EZksYtevr%2FGQgHcVI2kfjx5lqFWXAVmLEBtkV0CSFIIYd6aSK%2FAIGTCWPGoNeSJXkJLHTEmBh77JKEQcy%2Fgq9%2FDAAWESPwEfbZ57HmRKTV6KeYAmAgfbYHe6HjrirpvLsjHgzhYiAKkLvo6zxbPvRaP48lSd%2B4UqF2PTraf8KaUS8PIniXJG2Ek1PMXZGygYAhMLWHXkHqB6WHwj3MTjHX49c2Q45mj9ueC6%2F%2BD80%2BDGprNtQ%2B5o3euLbRJappQAQLeQLiy1tQv5JvszINTuQeHXNaBD%2FXFf4XRqepthmODkHnwqJYWkTorDJRqr%2BiLo6qjJ0Jd%2FisL5Xay0e9QEGaBtq8k34wxXlF3RKwuPpRSfk5ZPMNg%2Bh3pTOgO3YyqxnCfTNINoIJgxeIO1CjmyO29yNWTNMJPO67wGOqUBtYzHE3yCb1RKqkYhCslPMq3IddkOV1ik%2BjMnTI2Zwajd5sCo3AhWAVqgPGjennQBXVFZHkWqK99lsrHmJKVEFbxXtUW5GOgXaRxaSMLz057XXu5Kifw7H%2FO5x2OEUdxrIKCcIxzBd0cgs0JWTK82iIVIjSbKnLf%2BJh1MG222w4NehQ%2BBwQ0LeRfvlxJcQruS9xtbpI1hG92byEgkaaYx1G7AYa1C&X-Amz-Signature=b35764224eadcdd4e5edc3b40d7dbaa04fefde1b99dd352af7e0b5bf1dc08489&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4A7NTX2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNyhXvlMGoQx%2Bnoj%2BW%2BEb9VRszqvzfBaES0JrxpWh2jAiEA23%2BMDLbuhJWzF367kdOozYqGh%2FyeH67VdE8iYOEcuNoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMcDiJj5qiAp1j7ZzircAyj5YetLlzNt9LgOlRBSGUg1Lx91yfp%2F5JzjzVcPBzAhkUaGKEO3mWNLny7gaAAVhZvBZRIhq%2BZSavrhlhKzRxTipk3nAq%2FVgxphPfsI%2FDac1eEJDxP4rUCzhHiQjsIEdois4yRYLRzmzNMIC6pz7ScSahthYWHLTsIFJX92zgOriV7J5gUKlQUYKYcBIW6YubjDytbFwCFLHmf%2Fh6Dt38R15j8DJMQ%2BJgF5iQeh2AalG1%2BYigLGl4SZHZvNq0Qb4JafQX0PZSjyFistcevs4db38srlo1TbQZJdK538xURFVZBx0YTCfd3no06mppF9prwFGoAPm1%2BPEpRiJ2DspAl9VxayTsj8QOI3AWaSgFFZzvYaZiMBwMGKA%2BIqjZLuRmuz3tWFzICsAbgrsk1UidiQC6Vix4P%2FF%2Frt2UPkSXlxEtQGHTLmzvIWCHKAhDcLcWkoSHf%2FoHE8yZfacDbRptryZ407VX6FuG2uNoQAEJf49qMNP4J03Ew%2BqWKKOGKpRiywKPKoMIuPRpVdrR2uUt7IksK9N%2Fi9Oxcx7zgz0ghOPV4vrou79A9pWxz%2B%2BKuLrSZkD7kXox60iByzlds2iWaSmLXcIh7sB%2BmFRONrrQYUKb%2FIVb6W5ap8hCRRMLnO67wGOqUB3JYg4Nz4PWDZ0PLItQY8XGWiUPIYJnpyThTlPr3zfKLmS9IM26HdJYSSFch6biCUB6SnAW%2FNShAkz0PEBZofN9zThrt2gL26b3qjk3kqTcbL1mVivHn5cIcXmsCi84chJkIog%2FcOd5BZMCEee%2F2Tl%2FmZMEqyvapEfpVYGPHKhF1ifi%2BO49AvMxFdWMgH216eKYuaTyg9ZXB5Up%2F44gqBYTqSquC%2B&X-Amz-Signature=64f255f56ebfb09702cfec6e0f0e18310a941512bb5a9ef8f8850e8bfa24a65f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3ABFXZM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9Yg0adDwnCqe%2BahPIZftjuK9k3PksF2KzAACvZVH8mQIhAIPbKKTDAr1PJ8nm6dGkSlH9b4jFpsjEjhcnEmUh4tjlKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzWqXxzpMhkDRwfw9kq3APd7x0hAprfi%2FU04QEflKGeo%2BWtf1ccIIE%2Fr3Vw1ZMI%2FV9FkAJqQUOHjzB4XesVD0CCxi4U%2F2IqVF5v4o%2FqA%2FZauOYFF9qabNlrWygP%2FpPmDJWc43n50GSAQnRgO2YayclA5YTG5jjRTQRr4KgY9lCUza6BEcY3uZ8D6Q7WW9REUuO2fQ31Ja15WJPZFzfFTfVTpk7Sh6ncnLvfJxtIXxvC53FI%2BxGo6wFLB8XWfCvBL9y4pQubqOiT0%2B3%2FKNekrYHrJ3qV%2B%2F96TAs%2FbM0gZp719iLwrj9e%2BZLjOQclsJ4Y02IOkD2dGuPMfnr5jiZkizjFjSBT6lJqYRe%2Fb%2BKwj0Swi08K7E4GfJilQ%2FYA8Pa8pGgiFdDAB3GPN1qUKmgRvb9hSDryvDUJXeus41elwRSoRv5uNTC%2BYKKQ8QtvwWhfXllDPLhTCQM0FJsY%2FOnuUnLIKuvIQuCB6RBtCFAvRL3AT1jEEmPRJ53jTNNOtla0MgXeM9cKrQUUV5%2FSbzs4CILM7PdKIOvGVrFSBtJ0NqQ9DETE0OZM64Cqt3KTL0eAlbcQE679W0PPfjY5k3Nc9y9SgBIJrURpDQaxB1j4qOsLJAIXpsGjVA7M12FOi3y7vXn4sRkL4IGD3zFFUzCQzuu8BjqkAX6nuY7M4upWGWwNfTOz2PhUS9SW2zdz6LMvUIUKWU%2BEUqtw1q%2FFZ%2BsZ1I4sl5QX1LcajMgGAk5kdUK9otkhNXYj8wRZY4flp9%2B0KCu1945yJ%2FVBGZnWkjjiSZ4IXtzMGslSj8swUL2XzVblfusjdj7YuoElIQsVv2wOHadZWsbaRT2kHBAD%2BUo47xiKylR6tgB80flXVLtvskkp86Lwj8c3hote&X-Amz-Signature=eb2a7a76a603083c41c3c3f0ccb639f38cccad7ac3b87e8dc2c395479e6723b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJYYZ7P3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgdbwCRHDYZ27HbcgkYpqjcIXkYpgmZj%2BR6TvKGHuUJAIhANQzOhTQvPZYPrBv56RxxNAQi4ZnDLzIOeHcHFEzFOFmKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzv7HNp7u9vF9th2mkq3AN%2BKTgpkNdQF91Xk%2Fe3CeBmfe9rPM2FpuMFxpc9Z3NKRgoPjfmYyFPtSUW5f6y2k0IgDobqgBAIAKT7hicXWq%2BQWWeQ1T2GSbbflIDJzEF%2Fp9IWHx79nJ7tbURfXihhIZtBtr%2BQIj7pwbc23XFAG8DyKxNQgZeX1rTJFIInnpkegeCyb9fQbm8FhK8GnunxRZPyD4CgvTUkt5P8paCsMEFJk9u2Uy7SFgLOy9Q3JffYUnPj53Pfy%2BELXzUZD3bgBTu%2BpYPCZh39g%2FvhJk0BKRiseINaaPojI%2FH4br4ndFmQeGQPNKmXTfMDnvJxHvffuU1FqVnNbzQXl6MVNqYrt0X0o85sK1D%2B%2FGG8Pb5lPH3c671RCLJ5cC7iGQat2brjJ0DvFc5pYdsBeeFowZ09%2FFFkOHN9glkdhDYHdSaD%2BRvjwKyw8Kfa9byE6Qs3JG1b19%2F11x6EDXJu%2FKA9i5xHwRiQNh2f0is8o0%2F9pvjDXHgP6YuVN1Z3Xhf3eOb2DpC8k8xcO6N8NPnx1WvWY6g0VcyCtR9rrvTaG3v1iTuqQ3v1A6xWBhiB0%2FRc55N%2FALJJWEzO0vMOnDDe7zMK3g9Gp3n2Ytv5cKgJP%2FN4Oul9G5Ny%2BQZe2i6y2iges5WGxzCUzuu8BjqkAaxq%2FXy9sVLnwthT8L%2Bts0ob5wlrM9Q%2Bw%2FWeMvdsLnj2htaiqof81iQZ6vWU%2BqxgIjWZJA30zujShuv8Cuwq7jP7SZW1ITEJXWOTn8tjMWelCNChZSIlPRhlRpUoWcwUxV3UaGNbjvE%2FTXWmh4vIn8obofJ9GiQSiUDxD%2FT3Ulme6nlowYRvI6iHwcR3ThSg03MIpXH2e4NEjqBex3kcDXRPIdxA&X-Amz-Signature=893dff01eb42b302ad607b6cb4c00abbc2673740939cb7384ad01025a035999e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BGOL5CM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBe%2BQzNO1jZtDV3lllXq%2B0wnFbUrdIBcWyv4DFwP2GYLAiEAuzFALENkmVytC4VxXHbG4m0kDX7F0NVK2so3qA7OLm0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCSBEElTSJZMWD0BSrcA7z8D9MKeDyQtcd0qf3ueMg86ZabaspgDaBVQM7okJWATGatJQrIuLJ1OYcIwd8F5YFbCJVVtXnMzaidppbzQOb%2BqVgixkEcH8QM9zmMszu7k0i8ln%2BkXflTLXlltP9%2FHeY6%2Byd9%2F9fqAmwqORd2XDB8XPp23nizT3ZYMkNfelj0ITHPef9jBCdrEUi1FFJGNeCEuz4kqVLip4TwDDblxp18ZmZ3HTW0BfwrhcM8FGlaNaXnmAmxQcDBM%2BcbBlLIsEE9buLg%2B0pCs6fQRsIAPQNnNUs5wZhHdSBeM%2FlhVEQv%2Fg%2FTJo6D1JU%2BRoGS%2BDuNgEm9YPqPOeAUvNB9XSwBJ94sfWixSR%2Fc2SD7j0ugkHhX5U1TDxuxz%2Fmk4oobaFbRZ%2BlOQtc4sNBdsJ11wMRBtsHyLc3VT8xSvS3%2BC8UL4VBZi%2Fr8Mld%2BrF5uYwh2FrhFFiRifVFdZA63FP4U7WquWCCyhWEgv7vpGIBbHGgS2Gadij8vNb8lhlHDfOL4zFM1nSKEwNrL6BKImmunMfHjcGwhfkdjQOi4m812wKvRit6Pj28MbRcaoswqH77R7RFmVoNWIrZnOqYvLQNA3c83iljxHNlGBr1OkdjCH%2BKjsMAQGMUTwCo8c0OdVteqML7O67wGOqUBttiXSZuppqqPFFebpHfyhNlnCDLPB3msIWoHMcDQ16gHYtBHgcAWwQ2yAUIwrBJLoGL1GKyLvFFjJnkH4HXPy7M7mtHdjotHpkYCZTlLBXlhci7d2%2FrrltZ%2FtjSic2sDXs4GNIVb6shTOsYsc7wyWGJNQLbMVSdglm8KhSl5qE2NOpMxQy9OpCmroyVZDA50Zdwn064kRJGATwDJSKbQFvCEVVFe&X-Amz-Signature=23352de7bd3a1944849672845bb96900f586376e139c913337e3b2e5a5edb511&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BGOL5CM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBe%2BQzNO1jZtDV3lllXq%2B0wnFbUrdIBcWyv4DFwP2GYLAiEAuzFALENkmVytC4VxXHbG4m0kDX7F0NVK2so3qA7OLm0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCSBEElTSJZMWD0BSrcA7z8D9MKeDyQtcd0qf3ueMg86ZabaspgDaBVQM7okJWATGatJQrIuLJ1OYcIwd8F5YFbCJVVtXnMzaidppbzQOb%2BqVgixkEcH8QM9zmMszu7k0i8ln%2BkXflTLXlltP9%2FHeY6%2Byd9%2F9fqAmwqORd2XDB8XPp23nizT3ZYMkNfelj0ITHPef9jBCdrEUi1FFJGNeCEuz4kqVLip4TwDDblxp18ZmZ3HTW0BfwrhcM8FGlaNaXnmAmxQcDBM%2BcbBlLIsEE9buLg%2B0pCs6fQRsIAPQNnNUs5wZhHdSBeM%2FlhVEQv%2Fg%2FTJo6D1JU%2BRoGS%2BDuNgEm9YPqPOeAUvNB9XSwBJ94sfWixSR%2Fc2SD7j0ugkHhX5U1TDxuxz%2Fmk4oobaFbRZ%2BlOQtc4sNBdsJ11wMRBtsHyLc3VT8xSvS3%2BC8UL4VBZi%2Fr8Mld%2BrF5uYwh2FrhFFiRifVFdZA63FP4U7WquWCCyhWEgv7vpGIBbHGgS2Gadij8vNb8lhlHDfOL4zFM1nSKEwNrL6BKImmunMfHjcGwhfkdjQOi4m812wKvRit6Pj28MbRcaoswqH77R7RFmVoNWIrZnOqYvLQNA3c83iljxHNlGBr1OkdjCH%2BKjsMAQGMUTwCo8c0OdVteqML7O67wGOqUBttiXSZuppqqPFFebpHfyhNlnCDLPB3msIWoHMcDQ16gHYtBHgcAWwQ2yAUIwrBJLoGL1GKyLvFFjJnkH4HXPy7M7mtHdjotHpkYCZTlLBXlhci7d2%2FrrltZ%2FtjSic2sDXs4GNIVb6shTOsYsc7wyWGJNQLbMVSdglm8KhSl5qE2NOpMxQy9OpCmroyVZDA50Zdwn064kRJGATwDJSKbQFvCEVVFe&X-Amz-Signature=7ece80aa4eab84a1b85fa5a7c4e34505e9f29eb33a747e25cd3e16df4801e1b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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