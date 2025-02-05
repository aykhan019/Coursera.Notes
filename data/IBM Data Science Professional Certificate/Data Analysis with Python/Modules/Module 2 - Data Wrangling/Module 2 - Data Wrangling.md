

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYRSJJMY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIEFGE40fAxRH1%2BibQf1WE%2BZV%2BEjVYB%2FS1CWFJe7G67UwAiEAzcmpeZUhJGp2nM%2FJVr9qz0pF5wTqhFmbnaYa5VgMk3cq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDKJeUlPVDqMEeFVXUircA5JQsU9P8bpeIs0jYcp72y29T%2Fv1764uC1jqhyh65NIwc3nD%2BURMIXXOLrMepr9V%2B03MGu8Crt8YN2VoAIGJDoFVd%2BlbIDeipFQ980v4k%2F2y6dNSq3Ipe0PEMcpem2i%2Bcgt0CtlivBOFURvrdiRE736k9%2B%2BH%2BJ9glNVosuU5N6VKz%2FGKAW5HHII8OMTwaXGMpiHl6Sa2R6z0tXTTXjdCBU2Xb22MMFEQ%2F%2FI5b5VfXWEoNizAkQZ12TvPctKEcF%2BW1FljbhY223narQf2IQHRQMJy0U78f23YICoOWhNnsVGdqurmE%2BKJrG61q4BD0eWF%2B5sWVtMya648OLOzFPun15X49%2FRGkEc9%2FYAzEOwGN%2BG8dYsYQCxCxu%2BQQEN%2FXk42LSib88FMbzOnajkqb2Pwz59yo85OnxzztanBwXHk9BD%2FqJLW284lC6Qhmt8cH%2BlBtwPH%2BNroR%2BVvtVmjb%2FQid4s8EnI5ldjZub1Pa41E%2FkMVp6RotYOLBjF%2F4rxbe9a7fNZBAxuqAlc0w4kgUe1GRJwMujobCUElrspOUV6jLFSzEX6l%2BE2UcVoAvOluYgz6DeGDPanfgCZSy0ij6QD8yDTewQfTv4xYZV87ztK9VMdl%2FgGxUTKNFK8RFKsyMK3kjb0GOqUB4fsgIUnwAmf7B0n5BM4C%2BzUBgwVCECh7xKjMh4Gn%2Bf2k3N5HjKb1pw5oZ4On%2F57sIBS2uT3rz0DUdYOYahQWjOfsVHxXqxIcJ1ypEtlpkKoXPQGq9EeHv3Hphmw11vEpEcFyeSYieVhKTpPmogiwtshHAKPosxrPmU4Ythw3lmIVabP6EvPVhpyywgvr0O48xEP7XksMNw08H%2FpFTGKkRfLKNKA1&X-Amz-Signature=8e4eb1e330d0ac187f2641b278759577c78272bac0393bd762cb0b1cb5749b27&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CDUWFMR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCpG0ve5ufJ%2BSlO8tVXhKs7fI6hgnp31BZx%2Bsx9aKYnxwIhANnAJp1IRyShI394oqcq%2F9bgbDcCdTPvWE8N8svfELuAKv8DCEcQABoMNjM3NDIzMTgzODA1Igya%2FwZp2yYfYGeuw14q3AOLvJoXJqcMAyatEbegNKI2QJ6dxnYw4va4xfxy71CkLwaltObKF1bKiLmy0D%2B4xZANJM5A7jrvjpKf7BLrn2qcLIj%2BQmREn0ZKheUG4bb0Fjog7abqvP5vk0nI7ahst%2F0sffn4CMthej8fAvXw2GMfBywdTBaXJZZTF5fiaipBdmD8CUtdnmvnm%2BR7x6WAME7grd7pg31TDwSlMJYH8xGg715MS1E3DcKDajU7d1Ug4jo0vNrcUjGr2b%2BcYbDLfdzzEqpTFDt3yKj3w2OYphHwN%2F%2FRyCnQJ2FQSz58RZCP%2BmTseyyMEQGRoGVo14%2BAmiDt0WbeAS8ExOaSHoXuzFRRZqcFm6b4%2FuE%2F9VsgtC9baIGX0hfDYm2HPEGg1pv489ixgpaKOMpz4Ce2vBUELxB6UNA%2BsKY5wWiwFgFJWHsHPnhzWHc2YksKZuIvW5zbF%2FOF1fEUjCsaaKSOAdBnojRkKH95TwKIY5ZncaxTRFVxngdxtahSWo5IJJO4SKVJRxf83Pnqz47p6NJxchYWPEGukUVZu2mojURPnn5dTWo5jZ0xgFeUDY4VoxalsyKRCo1pizx2rYW8meGxEkyXlnYlugdL%2B3ONZc7UCdmYUueNrsBWEE4bHfjnJthFODDD4429BjqkAc6kmYlKwe95rnrOr7gR9Vbc9o4My5pHE00WeshG5YXacg8ty9xOAwr6RmPkF0fQyONUN%2BjyWZllFYgqcmo%2BKhZi%2Ba6B1piRSGmsaNNrtZsiWb8YnhLSZ15vvmx%2F9N8U2yRzFj53RmIPOQGStM479XgKzqdA6k8gdtXAXFnk6K4QilcFErH%2B76lPaL%2BKAFGQiM6CS2opQX4B3Ol8uZQFxjpRSco%2F&X-Amz-Signature=c6c3c7feb5b49598e368295d009e49af15f5dedc76abb261ba338dff46fcab83&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ3SSFX2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQC057ptRDSQ%2BbC09gIGjKFHOSaamqwR%2B3bK99eQLpv4YwIgGZUochptX1hIYlKWUgRpG%2F2DH%2FsiFHH4VzdMGRIyi8oq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDGcGqNjXJC8idslzvircA%2F3GtTxkcOp%2BLG%2F2yEFyDI%2B3PeuM%2BDU0ywKfhZ518AI4uHud0ePBYZ7hUvfoa0Ge5AtfJWN5djR40UegxvbZTXiDyQ3FnXEmgQj21rq4YftYWe5uLHxJXN9BnFoZhYIWWm%2FFasbxv1usF8eZ6bOPBTQdlk0xilrxONOOzaDMn3ovKYGTs0KmLVX7Uny4qLFWXjKMzI2MCeovFOxw8zVzqJkeWJDglN4YsZ6gsuk9gdk5gWZ1Zh8hMwY2LVIxcTO%2F5mReneGaTLTj8lU1ZS3HgZ4ls58V%2Bbu0whjxatcm5%2BHWAW9lCRzdX2oqZ99XkpxEgQ0ywi9MQX1pvlmQGEniHIsPf5D2%2B9UOsjH6YGryFbVSNXV9wHndnxP3VK5featoNjyCvtVSAy5w6L%2Bo68%2F%2BhP%2BhkheZ%2BQyeHk2uTvew2Ug04F9Ykk0KMSerGasCsWo83vYvPQ8LreoZKeA4xu1dHCDPV5f34ZBBTxWeKEHJ75TtIxhcjuxlaxYciW%2BveodGSm1xdJtdDlnulNvpq3KPeMmb%2FzkWov8%2BzT3tfKldlW%2FRUV%2FnjzJK5d8xkFVPjwGQn8Arcsb4oxLSjIE4eEnsrt0EEdXahF%2B1u%2Fw0JhBYa6dDjhTVXPME4C6h%2FkgdMK7kjb0GOqUB4erbd%2FFv2MwYTEbfaWlozMYwVxlPvC6pAvprjn928xUa6b8H1IJy0vsSdLQ3xwLQBDryI3zhkFUL1cKXx2c6879EpZfA7JtsB0wba%2Bq6KH9lHStn38a%2FXTGvFv4n1G2DKEVdVGiZLEfWP9vViB5F%2FXnMjqRGxbq7rXk6kxKDupbhyGuY1dzbyBadHQa%2BCjcnzFNcQpqIo5gvFw%2BiK3YlHkm5bHv5&X-Amz-Signature=117166d30befbfdb3e8dd2bc719db1bbdc08575b4986d34383db2c94b65d5b1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WMUVET6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQDy%2BCUnRQFJJ4f3%2FeKpxpCCzyf1Qmm%2BqgiAzgQzmh%2BiMQIgbdEA1VBVJMF%2B3mmgOXYLcBYCJC1uI2XPmBlsZnVpuH0q%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDHbmWrnRB2nmNjtlnyrcAzCO%2FaE1MnicYI2jxyGgDzM7we8CneNhAyiklaFeobbn7m6m3nlh%2BuT8Dc5leXQQE9lixiaU1C6JaQMX09Z2qXEC9tOPqnPPBwikazYJHG0fcbcqfWqbTwXTq%2FNjGZZeiGvMt7DzNEC2%2FOUmsFv1mIGApJfokcRepkAuh9UUX7zZ8nNg3vQB%2BT5T%2BesCKLjN6ikmrhyouUSTPwpg6sg%2B0W5F1H0T1dfSXsKAbTkfEcD8VtpGmeaWf4sURfgt1hoo2edteutEI%2Ffpk646fw37jPtCmR2crFs2MyuS7%2FcTQ4UjLCg40ldfiPW%2F2jXbwZVyZMzoF3Z4ZK0b1SWyYv0K8cdGdrEnnjLh4bV3u9o4bhedwFo6KOnVOaYBzM2ybiNReaIYzNjT7KE7F6O0KKZ0w7RBOUzxH%2FuXY05PddZ%2B3yWawZfTec%2BpH%2FardBUE3ZWhQQIcSySjNVdfca6SCFnBkqYhrAjCInIuM6LApH998pIigJoRarF8XbPcftS%2B6zZR8pdx9t4XJNI7IjxmRz86BEsK99W36axFSDEFU0ntispCNX7t%2Fq5cyNne%2BCUEMWHPfweQ1V5yZhkvfnumD4n%2BstfWWP%2FVXCQ0oR1HcxUegVm98TmUBPJwSa8gM%2BKfMLfjjb0GOqUBCKlpNepCSepWlx8J4iC2jS%2FA2aWjffYxaznfwP3c7YBpgYk1Vlt9rIYbfj0UtBnVwMyWeuui9dBvn4r21WGlju%2FOtGjpvInuFICF8pibN62CSQXCjNcC%2FgZZ5v8ewfx047fcQlBsOWAoxNymUKuQeIwOD%2F3IS4ETBE8Jn%2FBs1XPik3veCSqEQRnzQ0Vaq%2FFAYWWKcTFUOG0grLV9xq0m3bvi3Ole&X-Amz-Signature=f61db3a51941a69d50616bddd7237b0334953273e56eaace5988f05db930cea2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2ZDMXY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCFwwqNvXRPqLa9QvrrF2fjsY27njelpBcq51dn2AhwtwIhAODoyJqQg6HaL1b%2ByUJpC5QSDDf1GUjsPiC6zOaOsT1gKv8DCEcQABoMNjM3NDIzMTgzODA1Igy%2Fgm7Z6m9%2FnoroW88q3AONCjtdZ59jmz5E5GXNNawJJoo7vJ5zf%2FrLAl3JOifqAb5MsrRztyLqTZaIil52PCtLuRlCoQHDyJmeh98Me1i1U9PzSD1zGG4R0id%2FdjbbeXZ8mlzt6IsOUqV%2FW%2BjvrZ96U06u3%2FbFT2EJvrmOZ6wEJqxZ844mCzqwP1k9PXrfQJvLrRbpyHmMTBw7QIWW13AhnGK4zQqcWLJd6Ck7wqCJE2fXyRj7ICMkw923HvKXRdnLfU3uf0Xriw7AvJw7n7uXFkwUmA4A159lOfNlSRMdXKN1FOggJp3h9vLPCLXrdCrbwFaKQNQiI31762ql1xs3%2BFPft73UysakyMLhWz4HhMFo01HFnOzh2C3wIpaMdkpHkxZ7ymKQ0eztOeJc7gvS16vxYA%2FqSdRDGLJc42GIrDvd3mitSU8otYey9YSjwbJ3qCtSgPFbJBz6BagDl4Q8u0z1jWU7k9%2FecLCTyNinOH%2FG4VLI3OSSrMc7fSUOj8YcRUfiJGuIE6L2T3fkwXGuxT01U1eeCyLfcW3OlKQ83E8DQ%2Fdd38cc6YowWwXw93QAHvR6bZ1ZHH2YfwDCi84DTFmDZJOCGvwcHTuP0peOk8m8%2Blx%2FrWiZ4aEN2IsNx612FJHyWL3m6vbZ9zD64429BjqkAY1GbEN77nuNiS9w%2FyYlZcEaunT2VNAl8X1UPQ0pWwwFYMj89MJ0vOF5l0vpSoo6ceKKEAGQObKGmr62XnrySP7WiuHBlO%2FkVD1sewpXzvyd5aV0P9Zq3T0H%2BDjzLVD10Cw1NAJkM%2B%2FqViDezG9A9%2BdSOQcEouWoKXzv0VRtsyMM8MruzuJik7RBG5Ce6dYqVKhvkQRzTqCxJm6885jTomUVDzj8&X-Amz-Signature=1d5f2636b1929a0ba731fa8ce846d94355ae4feffe527db98f34a242279a9732&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WH6CVAQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQDVKH25G%2BbGT15e2ISotJxYQRUa37RbKpYbh7RWKAFs%2FAIhAK%2Bp2tX5k0ZKN9khLFXnaaRUahW3KJBRzjOGj8fZMW2DKv8DCEcQABoMNjM3NDIzMTgzODA1IgwshTh8EYGCoO1lQSsq3APrZ0JLKJA7XuIfmUK%2BX1n4IV6YMnFsS2DiEQxjacCh9fd4AEctpGHpraSZ4nIXNFFt8qeeZWltowg4Ah54ORaf90INOOFmJ8Kc6pb86S3xYftJnN1DkktLwZM1RrHp8bNmt5xF34OziidbEC74Ewuah%2FQfZE731mI56dhM6MQTlZ%2B7go7NSt1FXo7iQ3lsGCuTyBecNoqnA6kIh505Nrh1xQHlv09g85c%2Br5Y8sq1VLz5oitnzGVGi02BMysSxDc8nyrYU3pnJoKW%2ByO%2BCrwJFMYKgOjFG3n6mggD%2FMQioIycvnJfIGNMDrwNZKOubtLQKCIw7Hg%2BCEhqVUrwnxafIXp7z6HLXgcxkpG8ad1u1JvnGe8hN%2F46pULAEmSSRjt3af9wvWOuxlClIBAtK8WKmitvIPDDqRz2uzBbPww92ZtJ2eTXsyFGiVK%2FEADdFKnxUi8B%2FyKthIFcmQEFkh0fuOQs%2FlFtW17V2yDRLZZUXLiUVDYdk5rKuyQR8n%2FidOARUTsbW3TUyRtQu7U%2BxukzO9K0W0wEUy53FEXQhFji%2FyKPwbxKKcf9N2icvmbJFR%2FyK%2BktvdQ19BsuUIR6ZgNz2JCIsKjO0aYADOE9x6cqsbqHyHI9PNwzNZJEQ7TDQ4429BjqkARf8CYBTTkkX0mQah2cNq3KCVyTeYzpdoBTqnYHeajWQnQrQVh5eFyz6SdeSfQnHlSBp8ABu%2B3SXtvXOYbirZMT2%2F864s1l0aTjKT%2Fm2CYdtT7zxLn4Hzfv1YkXKQjtO1m89M4J2JMll3FCq6k3VBIPjfOMbdjVKiQe4ifAIyVo%2F%2FOdN%2Bbg8L68w0Bc1ZN3N1ihNZa8nG9unxe%2ByI5u1MjTa5NC2&X-Amz-Signature=65e9ba4b2cfadceb475cf2b273cadbff199407da1d4bd3af31510d38f7497160&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665A4ZUV7Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIBBCVUY38ADB6H40O%2Fq358Cgsxw4S5TDefGqrXe%2FoSuaAiBPPphUILJzhWtYL5w4SOKyjddxWeJS2dsSlpiPaHp1VCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMkQrcBe5rQ%2BVhfPiVKtwDBNmt4kfBOa0LwyzcuF0doraaRn1G3idRA5pwpHEMj0FpmOtqJHJVlfr4SDU2qpbOeQVDq0rMYIXsUjA8PvAqxLJPaLEZkLAdC463k842u9KR7yX%2FuiB%2BzSfbbodGMTikYHdS3JZuAxhMWVQxU5xq1yWpLC3aTQSrEERrZvO2rexAplw5nHM08d3eKh1oENFGTV7cRG6FKpNuRRPz7%2FO4vbyaGpy8YKbQdZMCKCAMwBTdXuGOhAARouUz8u31fe5XPA02hxPmUCDlsJTkG58XcyUOrOgS7UJgoP%2FDxTWJSWqfEE%2BwK1TVucmAOg7plQxCppVYRVf1DLGXz%2Fk8CoJK9VLrAFyjnBiCFnUL64wU0Ry52Rzt45UHHt%2BecR8DzPv4t6%2F4q4SOJ00STrxtF8t5CLDZmaeRmIv11KxiByABHwYgHuq2Y0kuLpasv3rF3VqAbCGXTAFKxgYbxSwhWZoHljblqhzXGhQQlItIFbHqc%2F%2FeNIlZfGdcgmQ%2Fnx62cW%2BSCDxwvG%2BHzAU9kOQfDxO%2BHzTdtr9n1YEToVu5cqdbFFx3saoIB9ssY0i0nj4dq8h7mYHUeqJi5tTLDY1TwyoezJOAeXe5i%2FQiD8hgzrrb5DaUyzK%2BVFUzSFRCn1kww%2BONvQY6pgFtzkR%2BfoDlWfOUzlQttVtIctbRXOWnoI2%2FTwjgcBmNCtlpmGCxnmecCnuDv3bxiOpvKaGgqT6hs78AwZnx5LUCcvbZDQCKCt0fm617g2kBzXHf3Xfbr0vbuBykv%2Bb%2Fif8uM3K1nAVsPYyfKk%2F5Fo3jzHmi17HXSu2z9dH7xOZc4BahhMur6654knp77TlRSuv8zhsjBhBMUTQ1WEjAzJWc1H8rz0Z%2B&X-Amz-Signature=4b41ad76e1f29e98e19cae9c15482268c217b66336be75bf25dc0440d05ee84c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTHV7Y7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCx%2BmXTJwK%2BCV3SNLN5aB4KAw5H64TCmdN3beR2zqZsegIgFwdPp%2FuaQePN8X%2BB7OqN90niCUn0wRs5YkLeVeulc0wq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDCEHf7qUuYugMXY1LCrcA%2FdbG0Q6EKOAaljO7Yk%2BqMZLayJ%2FGLZJVHFmj2tUHbUbYprZ3sn2p4hdAq%2FIxDZKaUCTJLWeP%2BY%2FwJNStPwB8ezY5Uvcv7tFDSJJMqiA2qirlDHV3Vc9CHL6vOrBrp7Z4xdQHMa9GJAGnZ%2B8hsNpYAKvDXO8%2F5gatQXUAI4TrBJdBYkDmSYAWBiOBbIgbB0FVOH6zDrL3uAuXIp887tE3hhPJRrx6klCfo07bFjDdqnUYDuoysoUhfd4ndHsirhHwpeAcNGLsZr7PTjyourQvJom%2BsAL4wYyky7VrcyZmNXlOcHWMFe2Ki4QKaAgitdRk4ELVbT5vRkPp0FFrbiwH9HdQkbmi0UhfyH9FfnWuIq2MPCJMVxJDLEdi3RTLCvGyUot69nCeEyiNEyX5B%2BRuyh8kx923JPHxKKU%2BpKbkM1ktPpLuB3k4dhdT8N0OqzsX0VtWOb2o8GT3nnNjhX8JkWBpuxs2viGfNQnlvtIgZshHxjVyKUkcu2yfxdkL1FvmTaxHg0SdiMSFgCrT0db6WEDi65y9npZEFBRj%2FbISDQdVzGvHMYtutuWJxxods1t3naFDNCmhFJdDH8uK1qANli3X6Q3%2FsdoWTQrqO1kuU%2FhpcTb3Fsy%2B%2Fg9LizVMMmAjr0GOqUBBb1yQGjVIGjUPOwmWi3m7smOG1cFxN%2FOEanQS3FucSxaxh5C0e4R2QfXn5S%2BLDSAUPB%2BaPcaixwvrDE9Et6ozkeVtskpqFYj0%2Fi1dp4FIRVwxgK6iCinwZn9cmVYQ%2Fuit3O2%2FpZE5ZttOUwueZaL9qvOYA1T5ewmLAYezPbL8PLILQ1YoxI3nMo6aWlAIHBl9lVPibUfDDRsE2T8jTY1uN45uSpi&X-Amz-Signature=8e7e6820f789a98dbe048407ba6150746eea0698070c9e47bea80d2c107ffccf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2ZDMXY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCFwwqNvXRPqLa9QvrrF2fjsY27njelpBcq51dn2AhwtwIhAODoyJqQg6HaL1b%2ByUJpC5QSDDf1GUjsPiC6zOaOsT1gKv8DCEcQABoMNjM3NDIzMTgzODA1Igy%2Fgm7Z6m9%2FnoroW88q3AONCjtdZ59jmz5E5GXNNawJJoo7vJ5zf%2FrLAl3JOifqAb5MsrRztyLqTZaIil52PCtLuRlCoQHDyJmeh98Me1i1U9PzSD1zGG4R0id%2FdjbbeXZ8mlzt6IsOUqV%2FW%2BjvrZ96U06u3%2FbFT2EJvrmOZ6wEJqxZ844mCzqwP1k9PXrfQJvLrRbpyHmMTBw7QIWW13AhnGK4zQqcWLJd6Ck7wqCJE2fXyRj7ICMkw923HvKXRdnLfU3uf0Xriw7AvJw7n7uXFkwUmA4A159lOfNlSRMdXKN1FOggJp3h9vLPCLXrdCrbwFaKQNQiI31762ql1xs3%2BFPft73UysakyMLhWz4HhMFo01HFnOzh2C3wIpaMdkpHkxZ7ymKQ0eztOeJc7gvS16vxYA%2FqSdRDGLJc42GIrDvd3mitSU8otYey9YSjwbJ3qCtSgPFbJBz6BagDl4Q8u0z1jWU7k9%2FecLCTyNinOH%2FG4VLI3OSSrMc7fSUOj8YcRUfiJGuIE6L2T3fkwXGuxT01U1eeCyLfcW3OlKQ83E8DQ%2Fdd38cc6YowWwXw93QAHvR6bZ1ZHH2YfwDCi84DTFmDZJOCGvwcHTuP0peOk8m8%2Blx%2FrWiZ4aEN2IsNx612FJHyWL3m6vbZ9zD64429BjqkAY1GbEN77nuNiS9w%2FyYlZcEaunT2VNAl8X1UPQ0pWwwFYMj89MJ0vOF5l0vpSoo6ceKKEAGQObKGmr62XnrySP7WiuHBlO%2FkVD1sewpXzvyd5aV0P9Zq3T0H%2BDjzLVD10Cw1NAJkM%2B%2FqViDezG9A9%2BdSOQcEouWoKXzv0VRtsyMM8MruzuJik7RBG5Ce6dYqVKhvkQRzTqCxJm6885jTomUVDzj8&X-Amz-Signature=b6c1b55cefd3912bcce2ddc5772cea46c56ad917f35f7eabeb481cc131e9f464&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXXXTW2P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIBmZNzx9ttn7jTjxlCEPJXH5e3j1jvZ0sHxjWx0xDCcGAiEAzxOB20m5H8ZdfsXKriMVz4MqnYAtgR0GD7qpNuXfd0Iq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDDma4hQHRSY03Fyy%2FircA7KAKYVNgSiFPhcgbQMFRpzX6hoPBrWvKGxAxvTp7EKxWUc4qTsdRppJSTsgp4Nwum1bvt4cdL76DkXKLj5mW8mXSmNS8IwHmIgB%2FkTVFGMKnNIkdFMwA4bbeR5TVwQDgjDzynZg37iGwYXFSVGV0PqCHgsjT13fgv2YS0XJSXYOdHsam2XX87KCQLRUmm98RtW955Bne6ap%2BU%2FjbcD%2FroRdIpNDQyXNyGv3mqmuob1anq71zpAHD6y4cYB%2BBc0DDRaQsPNWCTo2w6lqoPU3o8a1gWn%2FdeShRtgh0t2YiPdTpEolm8Vww%2FpiE8HcJU37zIzQCYzhTqjFjoWQ6Xb92UTWm7VpVW6%2FNJD0fxZyJAUgMR%2BBIn1gneOlKCGV6Jg58mcJwSK%2FqPBQsBlsSJLuM5DHTLDE52uRLHv3dQwPOnUOVV%2FiGHsxFrvE9StHyur9RSgTdUZLu23IATV3zvjuvDpTi%2F9rycLG5ptz8BCdKtYVdonRZU4m1M5%2FFwI7uvcEG48i9QOvLUZgutr51bPPvTaXge3eSgR%2BTFYvwopYy%2BoZxkhzveOmSVd4jiax9KntYE46X2Co5%2B0D%2BdxEkY5w53PyLnTXZgoh80Y9PHwnY%2BBPCMuE%2BW4ySo6vmQdMMK3kjb0GOqUBHwQ4fK19JPdwLR51o7gVdfVpG7BixOWuAAu82ZyBn5Xwlkp8DJ9KMPF6rbxkBQs3keeNdUyUaWGSnGROGxrpjqDIJduA3fJm6YFJ2EMA%2FXR%2BIuYAfjtAWb6FJOsBPtu8l5xyuB6dwMrOuC4rxcnmA3nIk01XGOGzoRYhSLCNf6m13jCY4Wtgafr2ubSP%2BFyYhEldjCpEcPWXWWWIzostkLj4a%2BQn&X-Amz-Signature=4eeb64a8dc010279dbd226a46dc5070ebb2a09cae01efde6703178301bc280a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXXXTW2P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIBmZNzx9ttn7jTjxlCEPJXH5e3j1jvZ0sHxjWx0xDCcGAiEAzxOB20m5H8ZdfsXKriMVz4MqnYAtgR0GD7qpNuXfd0Iq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDDma4hQHRSY03Fyy%2FircA7KAKYVNgSiFPhcgbQMFRpzX6hoPBrWvKGxAxvTp7EKxWUc4qTsdRppJSTsgp4Nwum1bvt4cdL76DkXKLj5mW8mXSmNS8IwHmIgB%2FkTVFGMKnNIkdFMwA4bbeR5TVwQDgjDzynZg37iGwYXFSVGV0PqCHgsjT13fgv2YS0XJSXYOdHsam2XX87KCQLRUmm98RtW955Bne6ap%2BU%2FjbcD%2FroRdIpNDQyXNyGv3mqmuob1anq71zpAHD6y4cYB%2BBc0DDRaQsPNWCTo2w6lqoPU3o8a1gWn%2FdeShRtgh0t2YiPdTpEolm8Vww%2FpiE8HcJU37zIzQCYzhTqjFjoWQ6Xb92UTWm7VpVW6%2FNJD0fxZyJAUgMR%2BBIn1gneOlKCGV6Jg58mcJwSK%2FqPBQsBlsSJLuM5DHTLDE52uRLHv3dQwPOnUOVV%2FiGHsxFrvE9StHyur9RSgTdUZLu23IATV3zvjuvDpTi%2F9rycLG5ptz8BCdKtYVdonRZU4m1M5%2FFwI7uvcEG48i9QOvLUZgutr51bPPvTaXge3eSgR%2BTFYvwopYy%2BoZxkhzveOmSVd4jiax9KntYE46X2Co5%2B0D%2BdxEkY5w53PyLnTXZgoh80Y9PHwnY%2BBPCMuE%2BW4ySo6vmQdMMK3kjb0GOqUBHwQ4fK19JPdwLR51o7gVdfVpG7BixOWuAAu82ZyBn5Xwlkp8DJ9KMPF6rbxkBQs3keeNdUyUaWGSnGROGxrpjqDIJduA3fJm6YFJ2EMA%2FXR%2BIuYAfjtAWb6FJOsBPtu8l5xyuB6dwMrOuC4rxcnmA3nIk01XGOGzoRYhSLCNf6m13jCY4Wtgafr2ubSP%2BFyYhEldjCpEcPWXWWWIzostkLj4a%2BQn&X-Amz-Signature=668b9aaa4bd40eefe03a6dcdba3fba06840c4596d12872f85a67a0645e63440d&X-Amz-SignedHeaders=host&x-id=GetObject)
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