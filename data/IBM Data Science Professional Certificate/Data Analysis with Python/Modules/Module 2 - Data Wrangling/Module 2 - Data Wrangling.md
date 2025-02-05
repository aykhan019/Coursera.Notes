

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V5HJZRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCeyXfpYF8cDpT%2BvZoZu7Zx0nyvieaBdjAxwovUkLl%2F3AIhAO8kTbj58ZKvm04gXGgjG8xgF9r9ZGM35dq3lyOUMNwYKv8DCDkQABoMNjM3NDIzMTgzODA1IgwxMNNN0iVksI2blM0q3AMoxenpGQ%2BSdWfyhJ09M8R5vjVXi%2FQYRzRa6rDLxmJDVhF%2Bc7Rsi2NOOCnO5tcDl5NX8ixlfqtCmo6dPEMO7EgjH62c3QN3WSjl34di7VBv0eU04eEfucAPNIrWHsv2k6GEe5i%2FlpLhvNbZl%2Fp%2FX5zV51PLjYAxZ6FgYBG%2BWAQ8%2BjE%2BaxuWBSY1yMGzEtK9WpqaOSQFdqLWd4LFp%2BBtwvzpsM99zfaUCz8Lc8%2BzksbbXzCmKwqf9jm%2FflGOn0RLlnXlKCMc0GzuRohNGLo730tkd%2FDQb1b%2BRUumN7x9pkpLW4Y6Ka8pP%2BKfh31Aj%2BiXQvlqpV%2F%2FbJ2n9ZaxA43EMQ%2B4Zij%2F%2BdEeFTMyGM%2BrvlFNS2dt0jEmrLv74IDqWgWAGgzYIhEfP1Qp5bAZ3MHUKI0IKjuoS1UDllXy8EjFo5SbhUK7iY5es3WEhH8csYIs1puPQa3fm36CtmIWUUhEuuBunTG%2BR%2BFSpmXf7bKjaTdl8AMhOE4lPmj%2BUHHOEV0wPNTeec5hHamgsMRxFMEjVfnXNXQeI2Bu5mcv5zwNRFL1r2BV9CKBEep%2Fx8jpr9L07NSiJfKwqavXGeU7YVpPdbY6Fle2lwuJtTS4yEVKc4FAgW44QTEUGkioVENq%2FDDnzIq9BjqkAQ4ZZBCy%2F0klgFnEGQZhKV%2BCy4fedZIAAh8RxUsOxOtChR2M3QLtzJHKdIkbkiQyI3W2E844IH9HwlxwXJ2fQu6zaQnGQmhv0Xy%2FC%2BRGRFDX5ywgUI%2BuXuKXWMUJf19vFokm03ptHby693lcc3FnaZDEFQyMdM%2BUw7gQ8ehuuZ6CsjiXwuSCRPsuGyVJyhSFeEXse%2Fh6mwgLWzmuzYyVWncswjtF&X-Amz-Signature=2ee026617e5a005e6bffdc67c2ecef944c81a528c9a3d3607295c511cf0acb15&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QBXBWQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE4W7uI3s1VV40LrWQDWK2gCUAoRwA5Mh56K%2Fnk2RvopAiEA%2FM8RO6wb7zFI67s6XKQ8Qizgv3UJgNBU6a%2FTY3B8VBUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDE3zlR6L7pii5jLUEircA7IMsL%2F%2FvAkJ8t0iN7IHJ%2BUzH5MtoiRkOP3PQSI0tFg4N%2F1MCC4yHSSQEXJLgkb8njUN%2FEhEdwyjd0M3%2Fd1Vcq2wf9TyqwBJLbfgyjsLkDS6Un1zw9OaV4E1XLQDv%2BsTUkmb3nxG7vSbDBryKzk9i4%2FabxLk1YdjKJHY7ZpnJ5SrzcH2mIELh3HGB9yxU4znoz%2F6uAu%2F9T0DBzUey6AW6sMFMp6FhDWYLZB8iIFi9ZfQcHv894azlHYaZpDjsOAVGOgFpSIJPmiTl6zW2WHTiA1TOzIG1DjHw6edOtrNHm7KYJ4ZB5y3qd5aUlcg0jGwDoDxzjrXZqaKR2NGofKs0%2FKRQUd49HDdlO61tq7sVTUxhgwe%2FHBdnvLu4JHl51iQSmnVjWnUOikicJ0ujCqccwvRJT6p4pRuaL1YY0sEUczDBa04OOQDrRptXadYcMVDGUlc9llZW3YD52PAjqkDB9PgLHrB9jRx8m%2BDJKVG0rGZFu4N9rsUUPagxYkm6XneSEfmHT4MNeGiKsQ1u3Zfdtxq8PcrWz4ZVz4tLJEHUlIoEaZ6foA4JOfaF6esPnykUBX%2BqeKB6nLQUPH3mamgs6z4%2FaW40GlbDVr5II28xLCjyB5ey%2Bu%2FJ%2Fr4CeWwMPrMir0GOqUBqBrKHKhJv459wm0G9ABsdQhwZrgb3maabKIpiBRIjqJe%2BG3Z2y%2FNNsHysCp9Qym4N6rwXzjTIbozJqkB0zYQCCaikpPjWO7%2B9aKEmotHobnLqoXxiLkvi1xM%2Fy9w32I8MHROnFIq8Xh%2FkVDhJ0D3zTBO6CfRGBS6R3wLgMGLbCz%2B0fx0fKYrklVldH7zimWVLL%2BTKmu5vzboCUQOn9mulpT%2FeJmb&X-Amz-Signature=5d80cd28b622d78b9625980708b253e38c4d551ff21e9427a93b1aa7d1c862b1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKJUURUM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFoD40ho%2FTyhxJIBQGw1XBdyEJ6mVGTJnmBJuo6Gtmz6AiBntjZL3gt%2B9VaAeImb4BWrHTIDFL0kehs2dYrxEAiLnir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMdAmHqNP9a3HZE7JIKtwDG7xY24lb%2FbIJ2%2BhMyxkzJG0gzSA02niKpLA5cBhz4zQ9wZO9XOaj6rOD8g%2FEnXqh0o51GtYMN5UixGGkFgDOrekht3MtTR98mkUraBLNf5SOA51gUvE3Q7Kh80DLHKowzle%2FHrIjVS46hKNsTi11KqTkSfri5DE42Sn9vrojoPDL1bQrdv8iRi%2FSX67ee3c7tfbvbRFzNRB7XigJAJ9mvXNQXouRVKGRMduPcj72id5%2F18CJILUXdv1u9VODFOqqD4mrKORHihM8Lj%2FQE2nRaFCzwxGbEpKNRHSXtpnqpFhAYyrWC%2FJD1BC7GZ%2FHAmwbW1WhYpDHSTy%2BM%2FHr85G4DTRVurbJatjpxAm%2FkFVyv8G0yAfKCt6f3QJrAYoFXDZW6pFfBxDLQx2ZRZqndWwDyXWwPChRO0%2BsDyuMRmXyan5pvggYfGhKR9P8gf8LpOPZWkvzhUG1lq05yab2ZdVT2ve3zAB6NUSuldBj%2BdMrgSJ3K%2B8h5xtJwXw8WM64KGgmeHF8IxvEOf%2BtiQp57sHtX1q93ffutEX3EUqr7K27CJw7P7bmBPHowLgQZfTMJN5k3dUsApjk%2BXvkWNlOOQOHEUwaBYLBrNdzgM5hdQ4breQzMwwWdPUs2oJKHTMw1M2KvQY6pgFdNWA4f75sqFVRVfB1IfsgsSMVAjmLMUC%2BOyOTFKuzWJBnvBZP1AEMlSf0DLJK7djy2bdd7uYaPLYYbhJ1Gtkx1qrH5jtqUEdp%2BPtuCqFBr5JNXS61PJCnlfV%2Bq1FJo1jHbvBKiKnKqv%2BpQJgyiaD850nYLcKr6Njzl0JLgSfygImy573NHAQriZ6YGC16U0zDRG%2FsSET%2Fo8xORWtxawehlWsUEfRN&X-Amz-Signature=098a5f166211db097707fc432b887d85a5bd6d74ebaf78713fc1d6e143acc4e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGX6UHGD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDoIzALsgu%2B5eMXipUeArFryFYtC2uScx87cBnhLbpGIgIhAKmGY4Hm2Jw0u0VTYj%2FJjPTw60QpL6VmZ1JkorR8CbRmKv8DCDkQABoMNjM3NDIzMTgzODA1IgxV2SAVYmurpdCGSmAq3AOuyB3Vjk1h3n%2FEPdazLvjZZkct6vk33XhMfe5GjSsOtshUFIRenVyWY8yYrXDsLn5oo9Jc4TMLkVyHw7u%2B%2BE2CilWcwVBExJ6PFVToFLJD7BlMqH%2FcKqafgqgzHMahF8FckGvPZYSyual%2Ft6XsZY%2B32v95nxJc%2FssjTR28K1HazJqZ04xOSlyscUy1XFZipS5LcuWnImH1xcFzOGhGoger%2FLa8TH3xXwq6fvsw3%2B15AoljgZC%2Fhbd9GWLZcSuMCb%2BQx5D6XSPHySPYMO3qVYd6aIFa%2BCUQJ%2FyeAY1O6nfXRSVM8geB9l936xEQ1aX8bsaktE%2Fdu5aB%2Fo5W1k7C%2FiRBZ0GHathmoSQGc4Z82JwPw7vmvtwr067qS0RP%2BwQycuC1hglH9tHyv0uiTeviPL06%2BQvPDVckN0dtWRUzVvWby%2BtmvppSHFvDJz8oYJHqiZgHY38GFoWJtiwDx0LQ3sIgDqV5JhQCWWhddLPMb05ogQ5FYgAx4inRs1htXT6Mor3UMoRzetfkke2214%2Fox2jbe0iIOeNsNZLDqUi%2BfV8S7uxF%2F4G8Lm0G42fAUZDuqspTjjlDtvG%2BRK1IrDW5wh3Z6oz8imzw0ZoNn4YF8NzYbKiiMuAY8NcyR34T5zCqzYq9BjqkAdJFnjeo9amNKZ82T%2F1PZP7SCPH1JIQncQ7niJHtVm%2FYjuIM3J7OjCQt752Pe%2BffZX91YdJ30Zs7i4RwrE0B7YYuUQkmZ2buz5bc9jNjy%2F1%2FPUShBTKW%2BVKDFpIoiWKBW1RJEh3ajFYYux%2B1Oeug7p6xuoKOrKOWqwBF%2BSMSXEhtzEYZ25Ai6WD4OqcV3hfKXQ0shiL2%2Fb2XVWZtV%2BeuwhxpPWgG&X-Amz-Signature=1247cc5a322eaac82548246de164825727cf7b95e6e789b0bdc19b6129531d4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AX2RYOJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIH7rWyUKuKgyAxaFyHH4%2BAVibC3JbL0tNgXvkc58nESSAiBHKRY0U0XrThJtjadJvZ7UuVeCpA14ZAl43G3lvVn9xyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMOzToJglQSF0E%2BethKtwDh%2BP2Im6R4U1TkMWyAyFwUMWpJHl13ph5fmb%2FYZl5yv4kpWEpa9ccziTY%2FFfJvqmo7HVxoErK6EBaKyAJpaapxhbPcx8QtgR%2ByJN7%2Fai8qNxicPOIztTwqglQNSiE0GDOMIOK1KDl6B%2Bb2FyGF7cPHUaSNA2c15mb%2FI0en9EAaBulnkJfupAD95Xw%2F8V4%2Bls%2B4IiASngGRE5o21uqStJHjSkmRS%2Ffb%2BEzJslM3MwhH9M5fqUWWMcXReTYtb5vgqHFuYoDvjC5awzrJRhGl%2FG%2Bk3Eim4SfZ%2BIcW9iUxBm5ocsq4xijxj0VatfHPMrdXaRZ937Roy3SqbYT6weyuAWs%2BJVUwMDtv2V9Lk%2F%2BfyssmOzt0aCvF9bk3cpi1bt%2F4%2BZeyTr5t7m0w%2FBw6sJpphU7Z07pjg4Dvzeb8HIMWv%2FqD2jLLAe%2FyWODb5HydIO95mvPjZZX2KvxqrcAJZ0r53slD71lRtxmENZgde10BOprOO7ZDFQAtNdNKueg6XUKKl%2B9tY6m05FUAt1li2xsEHdamrzBMezS1h9LMmc2Z9Fw1Ao4qiYWjL0D608hXDs%2FPJmS6H0H7rR0YKKQj%2FtFzfACdGHF2y%2FsMt%2BpNGyGt86Eiyato42W4sQdQYoUjvMwxs2KvQY6pgEwbBCRU%2FyKeiGTYRIwZo3aBnNM%2FQ9yV88G0ruTWQFPPxh8kiMmvSPkvDsesJkWJmpAnbSB4wqj2E7QutPGS4udFJkY9TJLFltCzx5i%2F9G21cR1EgdIumHYL07qRd9mq6Xi8wNU%2BOywEU%2F8trvbhmpuGGSxHM9P9QSW7AKX7KAYqfIoqD%2FaXjfq1AKVWNjDQYQ%2FBkeFrBWFsS9Q4%2FmPAtoeS5nCWip5&X-Amz-Signature=70ef7498a1003c558cb1b89055a0ac9fc50580c45bcbf946be7931edafee1816&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK4JUAVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCICMk3gugAQXiV4M7qA4sEt9KrLPI1pyE8fQjgqfXF7MkAiB8mSuyAH4gbcnvWvTwp1Lf2FI0V7jbG1KfSHs38txEsCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMlS%2ByV%2BZqN1Ew%2FyIWKtwD9fdzjoCAMPPDcR3JfP24BWBTYg4PJGhsH%2FgRL5MrYJNWxsEIb1a6RUJPSnkrrVBxYW5%2FBtZ%2FpowAQgWhMdyFECMCdDTuXbvwheE%2Bm92rui6xX9l0uLqQkz3lObzeEP%2FU%2BuefSAfXTT7Lm9xyGhLTaJtIJ9h9ZjfkEtK51YZF5oKjapOUrlSBLyLzaCmO2TjbkIchUs4B9mnxOUOL7NrYu7gs%2FTRfBqS%2BSdKLVpVVgMTGWcgKD3%2BFkqW64%2FAXjHRLX3mMOn5W24IMPJAfNYoITsDHuTra5PCwu03uLkBP26r0eATADellhQeYbRgHAmAR0%2F0%2BPeAGtzeuyz%2B4RCSh1GS1nZesDa%2BfWTfEZuLToato3%2BDvg4NtImLzOWCah1ZkSA9gcMx9p4Kth%2Fe3OdptOa9H8kSmr8yIV0%2FQQ%2FYdonKBzt4nlqkZYnm8pYg3JdiUoAWO6GDTyPrwVC5bOSW4WRUwfsBM0cEjRFq989UGPip9WRQDcO5H7bxr%2FJnnMsdiL2F51km6%2FILqABHXilI%2BTeXJHHcgTcU7S%2FRmWH8eYXfXoP9LlbAAgxKKkuOLJdq7EReqjo8mj1HghDBXHEjUVs10vYDzbODQI%2FdOwZOAul%2BrHYTJT5%2F42XfJBOswk82KvQY6pgEao%2Bb33ZMwOtvKG032ylHTiyahX%2F0oe1o%2BSqNUzGL6fXXuWD0hKMPdNDnmNApcAIDpE3g397mtZbglpqu01n16dSWFjtqvKNVsGJYdAThxLeIUeaIDK8PPPYl0Pgr6GaXcCM5tOA5oQHokD6cEecBz6p0i6cpJqTvlZlU0gS7xUtC6V%2BJDYhBmjJdfpeA%2B2DNRy1PEiz%2FtBy4Ty6GotbkO9njUyOld&X-Amz-Signature=fd72dd92d042598523fe16129f5b10608ccaa82c01ce370012c9f81eaddc9bba&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTFGBKAC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIAwD70PD9hsWPIkpMmzL6Ve16ZqtZ0lJ6IwEBpFFFFw8AiBxtTpFLW97AVrU2EufIVGdaYfYhFoJtyzxhCFpJAzcdir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMJZfLN5B%2Bl4QOt%2FK7KtwDD6aj6uhoxtVoiY4nAlcYsZrsDPe1cXaK70jPrVFKuLHIktiSmQtkjX1XVvH7fPX0wvINteE9SPeIh2rdK%2FvBQp1oIETIVHVz7WutCj0Zwu6jYNfagVrfgLq2zjoWD6iubfWWmOl8T0Oy69SNFpMSdziq5hVridOqztCcRxteiTsBwDkQ1I%2B4amdtsBk07iXUyF9Tj1JZFgvJDiOAXNqhWqqRJWP5GiF1QmMi4VPzV9dZElXqNPXKVCON2tA8ww7ktDuuddMIG5ssmqPHUp%2BftykTinG7%2BcYmQCzst%2FsXIU9krXOpGTCP6Cm%2F7lsDdWxBdbi3rV83nhENg%2FARHggdCE8F4VGTTmZjfog7O2Rsc7SXbUVNAqlAET8cSCqxIIB9JbAuIsTMYmEF%2BluNtOlbuJ8XEOKBo8cN1jZ%2BWHZcgcFt1oblBOzGsWKW88%2Frbs4C4vCfwZGDbGsaSQjwHq%2FZz%2BTQZztGy58a7kOrbe8kAbRbvLRsPWZhTdV0W0qplvj121CynMhgNrlYJEbgmI3p1Zb%2By45P4oDNnlzkIwvBQN%2Bx0DWXK%2B2I9RZc9xB659W2EGyFlDOqEUHOPO3lD6c6UPpLpCx%2BtTynx7frtX5x%2BxUXBCY%2FkQUMMMGAK5ow%2BcyKvQY6pgFFjJBxHhK%2FOo%2Btx2iGkhJhN4cG%2Fn4l2H5NtTlbzVmf04SL4AYqiI0bdOwSXWMIS8VE65mfBCHEIYLK%2F%2Ffa1%2B3EGuW81ZZhsQVonBHsDRWffdwLiH9831sV6ckx%2F%2F3anX6uRHsiHsX1mDhIkApIb19%2F1PTAw3uwm3dpT5iJdLB34l%2BtzdHXdmF4p96M0pbxbCj51L4IS8WtJqVUltwaS4DnwJSUxjBS&X-Amz-Signature=e879028629a6d35c333a9d19cf06758c522a539038ebb27340e5e33b5b413e00&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMERZZG5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDtBoNuBuQHdg7HenSxBEN3GLplmkwM6PYIoY7euuS%2FUAIgDBUYF15NNUVTAqYvL3XH3aCYbVZiGqORToCKP9Fy4xcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBv35FDurpzxXB2T1yrcA7FdgzEHOqxp4mlIlPFmIYEqrNxasdXvKTv9ZtHtw2ktQbT5LKxA0ti1ZtI0tQ87BYR0uiSwFVrh6G8vPWgCMSBk8IN3z4IvLUWn6xqjD2y9rbt8d3TZn%2FEfn7lXPfnt0%2BAnkms5Ur55%2FMl%2FBWloxiKkT6LUTg%2BKIbDy2hLxFUNXrvUTuUujkayYem5bxQD1Um6zDIIcSaJczOsVdx4ik4P34cTxJxE%2FdGL2fmmWZ7JvljRgwE%2FhJo%2BLGBNXDzg75qCkMx3qO2tH3rJE5Y1WQfYbr%2BwDzfdBfS92ieetXXa3u7EjLLsEgAxuRcKliD%2Bn%2F%2F7D5CCcIlr%2FLB1GhFqlfF9hMobylSDo02%2FmMNzbb6DFVU%2FZ%2BXVk6ZEjl98Dl%2FBKmvESqECrtJJ%2FhSqIzJv6NWvUgZFfIU08wSuGpOF%2BgdTksnMgBVymaNks6UOmh01nfu0HM0pscEly3i6HOWWAwSsxU2p8joMHM8rUFKYK8HDn3euaVHan99UHroDQpM6qyrbKFiUGnCyu0JNLaqWHBmgLmhNr80DV7blsREbElx5y5uytqwCwrD8uB2TOvBX7RTWnHuJSnc1pHsoQKCIO68xPMQp4DL7SPgsqAll04AL1JNt0rcp%2F3dLfPm%2FSMJPNir0GOqUBA9ANzReowACSI78ZtqRXVouHb6FwDAdJi9TJmDfmCR2Sqe4wGV%2BdZKsk7mEL7j8WZxXbqSIJ32EyiI1wOrsmI15r3YvmRa8BOXT%2FXboOtMaCJfXwdTCqaMWlQ06YuE%2F5qXrx8QVe614T3R2aIDAKLgPZs0xG6kg2GCFLo5dW504fzcPFvZxeOWqr6u7cnt3xjpEdaMO8kaWCNXEOl8%2BDgmjfOn7a&X-Amz-Signature=b69fdad2cbea7f0367a300e311d28924ba2df130a9a17d3ae622c3b2de291543&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AX2RYOJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIH7rWyUKuKgyAxaFyHH4%2BAVibC3JbL0tNgXvkc58nESSAiBHKRY0U0XrThJtjadJvZ7UuVeCpA14ZAl43G3lvVn9xyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMOzToJglQSF0E%2BethKtwDh%2BP2Im6R4U1TkMWyAyFwUMWpJHl13ph5fmb%2FYZl5yv4kpWEpa9ccziTY%2FFfJvqmo7HVxoErK6EBaKyAJpaapxhbPcx8QtgR%2ByJN7%2Fai8qNxicPOIztTwqglQNSiE0GDOMIOK1KDl6B%2Bb2FyGF7cPHUaSNA2c15mb%2FI0en9EAaBulnkJfupAD95Xw%2F8V4%2Bls%2B4IiASngGRE5o21uqStJHjSkmRS%2Ffb%2BEzJslM3MwhH9M5fqUWWMcXReTYtb5vgqHFuYoDvjC5awzrJRhGl%2FG%2Bk3Eim4SfZ%2BIcW9iUxBm5ocsq4xijxj0VatfHPMrdXaRZ937Roy3SqbYT6weyuAWs%2BJVUwMDtv2V9Lk%2F%2BfyssmOzt0aCvF9bk3cpi1bt%2F4%2BZeyTr5t7m0w%2FBw6sJpphU7Z07pjg4Dvzeb8HIMWv%2FqD2jLLAe%2FyWODb5HydIO95mvPjZZX2KvxqrcAJZ0r53slD71lRtxmENZgde10BOprOO7ZDFQAtNdNKueg6XUKKl%2B9tY6m05FUAt1li2xsEHdamrzBMezS1h9LMmc2Z9Fw1Ao4qiYWjL0D608hXDs%2FPJmS6H0H7rR0YKKQj%2FtFzfACdGHF2y%2FsMt%2BpNGyGt86Eiyato42W4sQdQYoUjvMwxs2KvQY6pgEwbBCRU%2FyKeiGTYRIwZo3aBnNM%2FQ9yV88G0ruTWQFPPxh8kiMmvSPkvDsesJkWJmpAnbSB4wqj2E7QutPGS4udFJkY9TJLFltCzx5i%2F9G21cR1EgdIumHYL07qRd9mq6Xi8wNU%2BOywEU%2F8trvbhmpuGGSxHM9P9QSW7AKX7KAYqfIoqD%2FaXjfq1AKVWNjDQYQ%2FBkeFrBWFsS9Q4%2FmPAtoeS5nCWip5&X-Amz-Signature=44645f4d9df37f9af8a8182caffd86a6c72be51bb8daadf69e14cfeee80b13e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6O7RV5Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDJljHcwuUDuPEEX3qJlmL5Kg%2FZJlcFVZVKI%2FFn19v9cQIhAPXDmDkk6zm66lBF0Gq5FZTms4ywtdyhGaraM8C2CITJKv8DCDkQABoMNjM3NDIzMTgzODA1IgwIy3jv9S2t%2BSr02JQq3AM2%2F4b5dSaby4EbVJUmyvsEMnm9FuF5y13AzsvqDDA8eLP81iGBgo488unYricdNw0YmktZ%2BCV2kGfc7XwgvRE0ZJFVG5MaNR90NQMsJfUZrOZh53%2BNzN7qr3mT%2F3KGLI%2FdpzmvNMfGGRurvfSS3kwC8TKJiCf0JgA7GPoVA3DaKHlIwna0%2F8a%2F6ML19K%2F8HAZSZCV6vA7Yq1HvIVdO0F75TaKG7mU4EvsyuYkMFjt4VhCKS%2F5vveyrBKq%2Bnr5wFYPhNwkwQ05nkeEQMsVxBzvTXUNGnMt8JUQTKij2EQ54uLy4FjA7N9F6yiDmZBqWFLMHSBWSbvM0zym4MQqkqcjwmwznZw1VFo0ZQJBEVWA%2B9KCTSI5RRX17zNxe2BHXcKhGR5ZK5LO0b3wFgKmWoD3vbYKr1rjpmv6vsBLV8Km8n0sQBAi9VENbbLVkO1MdLuGQf2%2BO2IvAUVgeR1hemWttR2GxGhOvBc6T0g4Tau5bdS6Fl86BtWK20y6%2B8OFHXs3qzIa2HvUguUK%2F87YDfiRQA7%2B8boMwkIaOrtd4AiRYQTURYQNfsvS%2Bid45gm%2FF%2BnJ8kxKi44krznUeMNLLW2PaC6qdlfzGLdV5Tivab8U7kJekV%2BbxOPDNaL3egTDyzIq9BjqkAVBcdagUayxVLuVzL%2FytEHrzriVKW0pQyDHFSuE426sGKy3%2Bn5BuiuY1Qoj9BvzESUPboKwnJVDUBRD4zr82fURxeGvljyEEhh%2FbWlmNcmggz8KVSzjgAwN5XuWZohjraFOkFHh24KGoOTVnEFudO%2FbvjToVlzrRtL3hV7doPMC3bva6YJuREeSVuXgZsIUr9OBB4k38vjHngLPlyEUhv2uZpEhZ&X-Amz-Signature=c1cf2c696cafddff8833213d75fb774e9a226359ab77d64e973503c4a98f30c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6O7RV5Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDJljHcwuUDuPEEX3qJlmL5Kg%2FZJlcFVZVKI%2FFn19v9cQIhAPXDmDkk6zm66lBF0Gq5FZTms4ywtdyhGaraM8C2CITJKv8DCDkQABoMNjM3NDIzMTgzODA1IgwIy3jv9S2t%2BSr02JQq3AM2%2F4b5dSaby4EbVJUmyvsEMnm9FuF5y13AzsvqDDA8eLP81iGBgo488unYricdNw0YmktZ%2BCV2kGfc7XwgvRE0ZJFVG5MaNR90NQMsJfUZrOZh53%2BNzN7qr3mT%2F3KGLI%2FdpzmvNMfGGRurvfSS3kwC8TKJiCf0JgA7GPoVA3DaKHlIwna0%2F8a%2F6ML19K%2F8HAZSZCV6vA7Yq1HvIVdO0F75TaKG7mU4EvsyuYkMFjt4VhCKS%2F5vveyrBKq%2Bnr5wFYPhNwkwQ05nkeEQMsVxBzvTXUNGnMt8JUQTKij2EQ54uLy4FjA7N9F6yiDmZBqWFLMHSBWSbvM0zym4MQqkqcjwmwznZw1VFo0ZQJBEVWA%2B9KCTSI5RRX17zNxe2BHXcKhGR5ZK5LO0b3wFgKmWoD3vbYKr1rjpmv6vsBLV8Km8n0sQBAi9VENbbLVkO1MdLuGQf2%2BO2IvAUVgeR1hemWttR2GxGhOvBc6T0g4Tau5bdS6Fl86BtWK20y6%2B8OFHXs3qzIa2HvUguUK%2F87YDfiRQA7%2B8boMwkIaOrtd4AiRYQTURYQNfsvS%2Bid45gm%2FF%2BnJ8kxKi44krznUeMNLLW2PaC6qdlfzGLdV5Tivab8U7kJekV%2BbxOPDNaL3egTDyzIq9BjqkAVBcdagUayxVLuVzL%2FytEHrzriVKW0pQyDHFSuE426sGKy3%2Bn5BuiuY1Qoj9BvzESUPboKwnJVDUBRD4zr82fURxeGvljyEEhh%2FbWlmNcmggz8KVSzjgAwN5XuWZohjraFOkFHh24KGoOTVnEFudO%2FbvjToVlzrRtL3hV7doPMC3bva6YJuREeSVuXgZsIUr9OBB4k38vjHngLPlyEUhv2uZpEhZ&X-Amz-Signature=39756b664715690ea65474db4cebf7826312052ea830d4508e093eb6b2bdc34f&X-Amz-SignedHeaders=host&x-id=GetObject)
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