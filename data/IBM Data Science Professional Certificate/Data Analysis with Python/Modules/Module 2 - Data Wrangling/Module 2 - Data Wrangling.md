

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2MN3F6O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFs1QIzmw172%2FwfT1oxntQRoALX50KfCuIW6RheFknXHAiAbKaPAMnYy5mH%2F4KZxmSN8LXnIta17aKYvNHqziy2IwCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVICzbID0G%2Bp%2Bg9V8KtwDs0PlB0lWREPShK1wZnuqsVRAz%2F7Z69xGE32jjwTAGYTsKtQ5NBWGhEU7sznpaIWpN7oCxVb8fxByQPVGJhT9YpQ7rVuhW6rzq9NSawKd9CSyLh8y20lgzg7y772F27ARbEf3tbHcIfHH8SOubZm063KrMdy6GcQKfVZRfYLkRYFqQtNOJ4JAbPg2sR8cegrUO9xt7eLz7NjfGAVV%2BbNoG14uAj%2BUAIRMCWrTZ6iIi6rKOB8FPmaoCOhytpx3aN3pXs4gITva%2BRiLE58R4C82gVJkb1WngJBY91iz3JsyGlE9zfpWiotYc6c%2BHrGtV8JQgFzPDbAaddrLNG6bsYWqvLJTWESjpbe1Ns5UbnNhescs%2Fm1%2FvT3vjGrAqKjg9b7V4CwO%2FmiBVp64TYmMFbf45MGxuZFoCemT6yxcIVwjrR2xa4ht2KDH2r%2BKjPrpEuT58QEsickGkduVf%2FncXDizaPsSdBfrGJqAagm7%2ByP9mEojywJwPAzdEu5TNhqGwj7qoempHsYaVbesORGE7fINikL5D94D6UiovBuTOjJQR%2FSqw9YzP7PqD97nG5pXgBwu%2BQWQ0H5u8AEd8Rviy9wHM9XqU%2F1JsHFeTRjx%2FiNPf%2F%2F51zs28eGTV2NN8nAwrZz8vAY6pgFazDPcupUshRPQQ5TEuLh61okROZ9I%2BzrnJIN1xG7P0aj8pee3hed0POgzd7bKqGVcf6394R8zuimZ8PMF6ckft1HNXRkHRu4nqjVCn8xMK3pZR45PnH1XY4T0AdJOoLKpBlG90yCpJkAzWNNUKxKbEK%2FG%2FO68K%2By1%2BNhzLfIM35vwelVfLVlsZm9DwQK%2BlPRiUg8B1W%2BknESzd57gBKSZMLbfejue&X-Amz-Signature=8f73a56d26d4b9ff1ce7ec7f953cdcfadec7455cf863c26a541c954ae7d389a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWYMQSZP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0tKYlGqJqt1k7FJtax%2BYrdmpKDOvwt2B6ZxpG5NqX%2FAiEA9V2x5hqVEMebdKYa3uzEHV1PhRkrQPozqovSXrV9abQqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtYgNwlED%2F86BtGgircA9h4yVvZe38t57QTEV1lzMCKvPVGfW5%2BQOui2xHEE43TIpQgMDFSq0427Nli8kt%2BRuayk7ZbaLciDbSYOPVcQQiv8ezuecW7Z0VBr1j%2BH2KWfLFL284UhMm3mYOFXUp4jDmJ9Z2incHUQG0UPJ0y89NPbfDi7cWNACiMKbO6srkaI5L%2Byu3nPalHqW4T3YOMbR2imp0WIexLAZwh7TjuPCKfmUy7KrmTaSqEhcosD6G%2B8jnHMJz59NXN85MoiKcAk5uxc0d2%2B3F40u99pzdS5SpDoUSHREfiHLpJCF4qLiop%2B8Z9KZx7SuLHn6eu1PJMM1nGlKo2Uft%2F3OWlRXFIYXpWnRJ4u3cWzFP3pkxjgFtw3oH%2BH3Bxsf%2Fq9WoPtppN6TN3OOo%2FLi1tr5pdLrw%2Fse4k3c4MpUVO%2F6nPmfahpfwrOH%2FXpnNi3CDA9%2Brn7JpBTzmZF62M7zloDPIXZZzhAWExDTO33BmKw3xTsncBGJ0t7KC0d0YtWOvrdi2D2ZPheZ9zEmyg2IDN6NSRxIg7%2BM1wWD%2FDZRZa8fWxnvcon60A9lgd7dc%2Fne4AiQzYKZKbeewHjV2T78ve21PLZtWAhUuh2yby3Pvc9loz8s6GAmNamRvmHUEXbbN4%2FddMMKSc%2FLwGOqUBGbednxQvWv7OzPpsIOTCIhr%2FPNVob6LdF5IkhBmMq%2F4LM7TyUlM2oLXS3sSyNbTv3D1mf1lf6YPHd9jtbDR46vewCjnOgVXECsyEhKVyXLyRCaSbgmH%2B8yjTY4EBbEKCxBeUxP9hM%2B8tkgZ7iyJzmtBsKPKA8nQFRfglrG8sL%2FGyTxtBLMr%2BToof8cDvQpZ9jUkISrus6KVwrGu7O5Fbj%2BlMyqcI&X-Amz-Signature=a7323e6341cbfeb9a9dc1c446857b90ec492b998a3b79030b7c9f597ed67e84e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4ULKYEJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRu3f9cPW%2BKNtlY85KJLDc9C9ILc1EPIgxPZvpfA9avAIgNmJ5IcCZN0j0Nb65Nsz2RekjGmPa8vE5%2BKuIP%2B7DhMYqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEHOzEPOUYLYPgGyyircAwxwUXrxwJ51D9%2BHtw%2BfsnYQnOCoXHO49UUvPKmREmQYf9DkFD4aAR%2FD%2BB%2BVXNSNzdSCQruwh2tdHGVyww7mTCPhjOKi5RORi79F3JourvPYE6IRMOgimPCcRwlSQoCZ%2FyjwWQlGy8HqsAKJxBRXSQepxKgcDUPBUQAfI%2FTDVMOQ3wMvZNEliexeD7L4qdwcLsgM5Q8Re39982Xu12jZb9jC3cfvOdiDPJAekces0oCXC0k7CaI6S3mOwHY0Xx16lJRVpLdDKl2SRYi1h6173O7B37OegUic8LlpYfdhaqDRWh5TZpI4N2oewJPHoWSKpQgR7eVUHFLlNXFtCYpOMcGGAQvdvZ1CzxdFDcJ7iqWnCUw3%2F%2FvMhXXB0QFWaqH4Se0X%2F1MLIXy%2BFrD9Jy%2BqOq7BKhm1NdcFfhMJdoOK5qIsqRv5i2dwJQsA90J%2BX%2BYrlcFeX53fossDW4WYWprwDC6UhAXebBB9wI6FpxKcYyn4j9Grx9wS%2FxrHe6Q0ZjTAIIbHUB4Uc4ZI8KVJhBVjHjDFDGzvAeNC8GHxWp9BJKaeQL%2B7M4dov8Ry6OumfcNLHAqr3R%2B6wfNbKoo9tQz6sYLGPJ5SRCOM3%2FiB7%2F9yZGiM7JD63spw%2B0WZ3C%2FFMIuc%2FLwGOqUBd3IzZkS2T1%2Fq5tsfgDc6zZAgsoj7HZwKyW%2F9hQeD03mQunAbkCPBALiudxTClPZDGXfdsHfp3hN%2BRfFCXJ%2BLZw2uFVXt0dryXahKth4MsjVelT6hxYlBg31bKMWriQxzQU1gBUry6w0y42tAB2jAxo0gOXqrRkBqyNB%2Bie32ORJGU0vdF0Lp7xjbcqpGkxOX4mKi5gV6U5NsnY2ta49%2BNvMNoc2m&X-Amz-Signature=7c74a7850f58e7766670deab96024441d7dfc768c93c54abe670608aa968f582&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHA6IGJJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPjrx5x3alGZZV1uj0BIoYuE6sMBjAcxlRO1qsjJhjVgIhAKGflzt0tgSSLiZbRRRQDVOo9KhNmI%2BVWArKr5u1anjfKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTGQg2RHWaafhXol0q3AMiM1762xHyxpKrvPqKxs0Sq2c7ZHLS3Kacu5LLtw7Okmy%2Bw0v5Th0duvTyoj7eaJw3BeA0YZ72CI0Vq%2FjB6KZ%2BPXtWJMfGh5CQIOcAt1XQtOKxy0H3AGHQTuOesp5jsB3d4%2B2tyQlehBiZP9qhd5cvZykwr%2FdAUoSgDOVH3cc3mV8c2EZYcEZyx5O17%2FV5f5l1HGyyBhNFk2cx4cMeTwTjv9tBsMYlo9LGb2XBQXJ5oORMaDKXyKlVwUyopEl7JMhsND%2FVdck3dCJ04t0wealqPkfw3bmNkMhbqKKOM5fUee4GZZS8mOkWDyBfhx1Szkmt1JGOyW8eVAp1tvGX6Fre0gZFVyOqK2fDZUV6RPEDiZXT%2Fnu%2FgEW%2FzI1hFaTlqGhNM%2F6ydjKL%2Fc8o1Po7YVgv1pSeB5X1ZITbj1f%2Bqf88lMM0nRtkol4ax84Hvexh7D0iv6%2BWi10aggChisQH%2BmAQWduMCpqjv6JYuN834YcD%2BhE1ilQvRUfwQ5yvdjcFsuddaQnm0jE0BARW3hrkqSVeAEdOga4m1qQWCMR%2BxWwn6N9ghUMLQhXU%2FbYPA7WGXxRJ3%2F8z8hNUB2ii1CPQSDs1HxFF%2B3yepW7o0tOnRLZ0QS1XmRTQYcyCU8MsTzD2m%2Fy8BjqkAfe3cp6PhQQ8MVueHvmDuw6AzOqD2OO7zV6FM%2FPmL%2BJjZQ4b2FIpMoumbOGXlggeVjvQU%2BjGAW6wm9RbWedt3wBb2DrVqnxplptuSX%2BRPb%2Fvsw9BGh7SEv9RWAPKrtoRNPW48c1NDmPAWRLHw6JayLiu4HnbR8rNJWskuJwMVaJpqd%2BjmHc16K9js5ZPx%2F37kY4j%2FNVhq7Xu73BzWRdJ81UhQP5H&X-Amz-Signature=8e62a708c0e4c2244b8ebbbc9f964bb6236ab4501d8fbc40445cea58a1b71962&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS5FLH6R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5HLuVNxKZICayM2nRdt7Tn7VBP8dyaOqgo4iehq6IQAiAJLBe2Cwz6%2FB9zX0Ks9Vk5%2BllESW2scIyfC3TRWu%2BUqiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtxlQ2PQr7xIFB%2BYdKtwDK9VbgvXAz8Co1k%2F124zt6M5f56HC6kM9rViBjvlO2UgthGz4m7vRA0f7gvTliLitA5n1AaBkesGcXPMUAvP%2BwY%2Bpp54by%2FBidWbzXQ21fqbzWUFe6KKoSnrYV890qz1qTUSI91qiScog8pz5xkfana10qNT6lRrU8mICLkQItvLWUbUF89jVCBSwOPlksBq5QcmnmlcAyfNrpT%2BwSis%2BXeiREeDr062qLYuRjsNiQildv8jwJMz7x6cdX1ZAgOsTqL1plAtrwt66BbrlpYAnPRWTrpRmEp86zgpd9Yy5BsAm4ORCxCSAw3IkHLTBF%2FQU2JS5C02vMULzj9ItQjhd2w8hph84itv5syW9d3VE5tJ6UUlWgJT%2Fj1u%2BX4oz6WWrQ7LiGrrs%2BSr%2BX8kxyMlzFOsf0gFIApW3%2F14TvN%2FDMKrdJwF7dcXrbOxChoM30CpxXjzltBsILU0zO7hHAYgx%2FuGWFOEx6V236JyU2hPfOdnt67IU7eeiEABCIdDu2bLt6CEQ50KvNsLegXPoF0ARhAGSzeeUgUSg6PfGbVAB4YO6Naqle5mNBtbKBNb1gp%2B0It4tAgBAOKntUcfjqmzRcqzSDB2RO%2BQhO671ZdQCOwtI2ec%2FQPnrdJb1sS8wlZz8vAY6pgHARisLzp3L2vBb46mAvod4L1aZbFI9QSdZZrwDGez2zlSG3uxPzyvpzgUa2BBORBisao0nXROuNHUK%2FAEC1qq%2F3soUAGLQv1ZNsb5kU9wrcTwJXXPaTxUjO307V8JDaPUg36bZgpdOR8f02qOQsftZ0ic6L4NFCG2lF7atU9sicqoZdr7QHchWIRrilfIW5LYPHQWopxsJeCP6b8DoqZNEua2D9IR0&X-Amz-Signature=3c64faa976187dfc16b78e447bdc31764e0bea7d484187004fb3d62cce56e551&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIX6P77C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlCrgRQyUQUXmuitik69x8%2FIMcD1MxXJ7gYuuymsptQAiEAuSEd3EqxnSw4NYRE2FoWnVP3nmRiGlBp3dyCGopTzAkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOowcYE9Z7mKtM9pyircA07FWBFDSQin%2B45kr2RjhqqhEaHOl1X9AOHDfwcj93%2Byc7pjvrC405TW3OO6WeaTeBr3HS1JZRM2Ru6tk2hmBFN91J0yuiNnWXX%2FtD3unj7%2Fy4ABAKJrB%2B4VPHprD0HitguiQdzWiu4%2FLwxzJmqNPwPNaM6MvM%2FP4FPUB3P2EyoO1YSagqgRiq9GRwnsV3WEd40R5hbMYB1UjMVwa6xmOtq2h9hnAI%2Bh9sdAMCmE%2FZmVdLmwqLAX2Dlxj5v28DTVgNHLCxDq%2BFxxmheW8%2FqYJ71HwtkU74NGRIe5ClS%2FwMHIOZEVcmwm8nnvL56D%2BpQ2zuxqAX6c9Q9cJdq2UaAUU6N%2BcOyQ8Gdn6NMeov6l4zvxN%2BtsNrmnw5ccpImfD6QY%2Be%2BKoYoQ4mHr4XJhB6bjuyBeGmVJftePpA6oyQ0Vc1jqvzPleDM7PNiSRnYHcESvS7f1cEVV82XehegqqSqsg2jh4BaO%2Bt9a3TAmRWeRHRYv%2BinCD4mjQsTfc3eKST%2F3Z5hyFIFXjI6NFSu6M9THwlGBQ6Y%2F2yuOsUai3H%2BFED8iBB5VMGf8eLqCg0N7kQ9wxVRzkoUGjMQ4ZE7uUSKZNehAeEexlZ7oCmClGw5lq7leAGHyyCSBvrAqw%2FmnMNqb%2FLwGOqUBQcxeLNMNew0Ntl6f06rknIfkhv6SJ8eAVwq8o%2FHAjT%2BjojUQa8jVGEJ77qJ%2B8GzZfGy%2BDbqmCK%2BtXkj3II4M%2FHlrQ9txVXXLYjg%2Bfh1DclsECpma8dhdqeQuANci8N6thzCTLzBIKD9SBuE1v6ujzBW4btdzG1yun2tZ2ychQKd04TP2ofQhgN%2B%2FwhVaXhv%2BTHHHtCgzZf7%2FboY9%2BZt0qg3XtBj9&X-Amz-Signature=7a1d641eddc7e40bfe8209729d7aa27f69af2179e198124edcba1f09de3f8780&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DSOBNHN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB36YsMSW6q6PVSzH0ZuHk4TyWGIXklMVCtYYT8N2T82AiEA4qCKLB%2FfCk9DbihkU2nztgcFH2M%2FaGpcX%2BgrABvqbZkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiibrLywjhl5CYJCrcA8lznX87gpOVL%2FvcI28lrz57rk4yhugDyqENE3Tc11XW7LiVxz69f6p3MzZD9PKvoLs5M%2Fwm8KmRKnJGY%2F8i7Z5lfJAhLUqrLRrW6ZQgsI2UR1XWq2x5GeORNcgm0ihJqSd%2FimNWQGcp1AQkV78YK0boOTOpc6xRuNqSLUi8QdCXBu3u3W6rXPsoFpVi2NpcUHrXNkj6IChYtdPrejxBIar3dg3nwXi8Mvz%2BFgeoANR2Qh845f%2Ff1z%2B4CZUtmJ2P2AD7JH2OXr3sQOYqy%2FC39MpjErmZReFg%2FEFJSqGqeEGa%2BFXybGwV%2B6Bx4PYvnu60p2M1%2B9seMPDQwAoJxnSzcTJ0ra05t%2BfqEmx79Vobnd1stXNS3v1v1yIxhqDDFCzsu00TNEZZW9SaKw33BXtE0O5TPuqTouTnv%2BILBZVlyW96LecV007X1cNdmpi2sYpdlPplfwtL6oaQ3QS%2FWt4ILQYMjl%2Fp15EtzFtH56WXxHZhKIwCZsolZ1y7qnzcC6KXFVVzXzN%2BbHZg%2BcO3AAvcyhcHI4Qa7ZpvszYQ0w5%2BNIR39%2B5czdWilPa7IJf3ejVH9%2F7wToT0tILM3FhliAAEkXBjwJs34oTZk%2BB4wTmkr9kw1yK59EIHjdVCu%2BspMNyb%2FLwGOqUBEH8EEtAvya6ylzfXSY3bcT8sWP2iI506S261SMYQBAfhKe5pzmM1ab%2F3u1oOL%2BYEojmDBd9hmEOzdDGT3wYYZ2MrNwax2pDpDAIBFz%2B7cTkGlxEzsuvIrdohBiEMmnNGCItR6MfW%2FO3iCtt4zm0XUMOYbYKA2D5vK7lzSAEOIkBhzbE625Wcgpg4zOtV%2FBtujBxz42NxJLXhoup6%2BVZ6BXeO65Ye&X-Amz-Signature=9396823a524a3a4fd7844a6760f1ea9bae3ef4625793b25a5a4fe7239b5005f0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SLQ5KTJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS7%2B147G3spVYuTPMBfoBiMWhIGlr7KdzMI6XBNbthqgIhALp%2F56U2QikGXqZudEGGLyjJThTY9N%2FxZDFIsiNX23JrKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytSed6eR2F7gxSBtQq3APTGyjQ4X2mRQm3UplRw5od%2BKdjSxfQi61GiBo2j845rsLluoTIYdmEIYEfNwuQy%2BrOjEE7VeiHvaUxLdBe5vJAh3whE84PMeYVqW1xj1vqNiypgVthiUXLioImYdFB1anqnfMcFAqFIbxDoJh69YLcex6DdBANJEW3nf7J3P5iKY7C0OjROKrHNDcadl%2BnU7av2vr%2Fa6SHlp2s%2FJd4rOGRs3vzkrzvX236rzciYNt6apwOMHHHl7Vz87aS0%2Fcwtm3YsDH8VD22NTSGwmkqtarJCM8Fmg3qHQ5VXL%2B5%2FlccKCxKBWGjEEguCswf%2F5mn7Q6avJ1SNmxGsOCoG6Igceh4GR7a259Cc%2FAY7ly6bn9T9NsOubHO9R0%2FYvNcqjgQTvV%2Baaf6RlzdecIF8B8XXxOR%2FYudyP1KvclCHPsuLa%2B2hgKF%2Bqk8dustdltWNCQn6%2BeTnNOK6%2BYN7hHsL7VibhAx3sfgVFKTqiSteifIwVqWVbQ9AZJYOwcnHWGb3l2RE66wDqDv7XIhmqcQ14dbrN7OCFPd8ecswWQz2kKNU9Y6aY67EIZBEZ1SgRxP%2BS2re6c00e8BXPw6Y54BoEi1kwV3KKhWzGTUGVWX%2FJ6fHmoGqEcS01wprfctfh3RgjCmnPy8BjqkAcmCMkHwTnXfghQTDb6UhFg8pqMJvn9IR77IGS7qh5R6M1iyqN6i21%2FR2XaoD0Geb4j4vNwSaP7eFSdvx71bspzxZJUvDTEwXFM%2FdgwhFiEvUTOIt18zYIYRjcKukXNf2Zq%2BKCrpJ2Ri%2Fgg90qH9lAQNGUbyIiq3VVLQJxHpUs8%2BBRzjGEzK2NYVBwbPvQsgbxr7RAkXcl1jgMVzEHpRPpzNTe6V&X-Amz-Signature=4f1beaee0890bc7a3e27611a61af44813e422168f9ef8d62dc9c921939406700&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS5FLH6R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5HLuVNxKZICayM2nRdt7Tn7VBP8dyaOqgo4iehq6IQAiAJLBe2Cwz6%2FB9zX0Ks9Vk5%2BllESW2scIyfC3TRWu%2BUqiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtxlQ2PQr7xIFB%2BYdKtwDK9VbgvXAz8Co1k%2F124zt6M5f56HC6kM9rViBjvlO2UgthGz4m7vRA0f7gvTliLitA5n1AaBkesGcXPMUAvP%2BwY%2Bpp54by%2FBidWbzXQ21fqbzWUFe6KKoSnrYV890qz1qTUSI91qiScog8pz5xkfana10qNT6lRrU8mICLkQItvLWUbUF89jVCBSwOPlksBq5QcmnmlcAyfNrpT%2BwSis%2BXeiREeDr062qLYuRjsNiQildv8jwJMz7x6cdX1ZAgOsTqL1plAtrwt66BbrlpYAnPRWTrpRmEp86zgpd9Yy5BsAm4ORCxCSAw3IkHLTBF%2FQU2JS5C02vMULzj9ItQjhd2w8hph84itv5syW9d3VE5tJ6UUlWgJT%2Fj1u%2BX4oz6WWrQ7LiGrrs%2BSr%2BX8kxyMlzFOsf0gFIApW3%2F14TvN%2FDMKrdJwF7dcXrbOxChoM30CpxXjzltBsILU0zO7hHAYgx%2FuGWFOEx6V236JyU2hPfOdnt67IU7eeiEABCIdDu2bLt6CEQ50KvNsLegXPoF0ARhAGSzeeUgUSg6PfGbVAB4YO6Naqle5mNBtbKBNb1gp%2B0It4tAgBAOKntUcfjqmzRcqzSDB2RO%2BQhO671ZdQCOwtI2ec%2FQPnrdJb1sS8wlZz8vAY6pgHARisLzp3L2vBb46mAvod4L1aZbFI9QSdZZrwDGez2zlSG3uxPzyvpzgUa2BBORBisao0nXROuNHUK%2FAEC1qq%2F3soUAGLQv1ZNsb5kU9wrcTwJXXPaTxUjO307V8JDaPUg36bZgpdOR8f02qOQsftZ0ic6L4NFCG2lF7atU9sicqoZdr7QHchWIRrilfIW5LYPHQWopxsJeCP6b8DoqZNEua2D9IR0&X-Amz-Signature=53610914d262b6182608e1bbbacb281b65ca848377f08fce4b2f8b95cb06014a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUMSCPQJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDa04DfT43nu3uygirsO93yk%2Fo9ZdqoVAH%2F%2FOeaRhbKJgIgdosPyBVyBLqM0NsDkFN7c6utNHtM%2BsCSjScgkizXOU8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC4NWWCy0AaeernCayrcA3%2FUKnd8c9uAyVL2ZK7FAdznFEPaUle3R1OOP7yPHREn1rCug1gmRuNezmbvX%2FQzAVvsHGyBXHD2%2BBCC8kxl8%2Fs%2FYxyhuz6r5HqT9yjxOavSAL8SFOdjgluPLSEYkHnKsdraTCNLU3C2CRnRg12FixJIpkjNDQh2V2LOMvsezm6Psh%2FWyq5nA7U57N%2Fh0RGE9iB3BgJFSNC348LGkDT499sep8pijQm6R9PN5nxwFkFJqBNuxMyowW0us%2FF3415Ir4UAhWKiqQdi5Vgjzo5GsbcIF0tSeqV3KqT9A1FiJbqoDaKT7t85P0wDd8Q4WBrbfx4pO%2BRZ%2B5As9IMMDbCWDYh0V6nAxwDgx8uDa0EnZfnOjbe%2FNu%2FU4%2Bx9t1z%2FaDu8GqGs9YKAZACXY4jowJ4tePKuk4tSU2UaWRb%2BJxmDb8nqLgXny8D7ZMxe1Mr4Qcu6jC37MnwNbPgxNP7MruWoVT%2BD8I074qLDfvnjGEKzliC7tbZ3KqoCg2KEcxgqxykO0VgnJDKy%2FH2rbkVdW6%2BCV%2BH9W2ap3wooDKiUVtdRYwb%2FuIufsagB2VuN2RFlvxaUIP25U1gg0rhg3bH%2B7ezco5uTegicapINh%2FzAcu9xrSWX4z1BQP4pH3Am%2BmEAMKKc%2FLwGOqUBCqFk6MjWhz3kv4d9ka3aFWctqCJKhRPIdpB5jvfys7B4ySuynUscIpZ3D6w6%2BlNMNXDI4zU5kbocGY70Hl3BzqE1aMm79KuVK8khVR6GR%2FvzKtt1jGDTHKurk9S225uIwEnGqwGQYAkiZ3VbpUALsa4yJyY7dSVGQ3FSzI5qIUQkiojm%2BDqPIDdIp5uCFrU%2Bq8guKu%2B%2Bd5I42YJbWWS%2FhdC8KEGu&X-Amz-Signature=8530e78e6a1b2b676b2cd714437bd95e9d7e3541e1bd977707a7645ab6afe9c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUMSCPQJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDa04DfT43nu3uygirsO93yk%2Fo9ZdqoVAH%2F%2FOeaRhbKJgIgdosPyBVyBLqM0NsDkFN7c6utNHtM%2BsCSjScgkizXOU8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC4NWWCy0AaeernCayrcA3%2FUKnd8c9uAyVL2ZK7FAdznFEPaUle3R1OOP7yPHREn1rCug1gmRuNezmbvX%2FQzAVvsHGyBXHD2%2BBCC8kxl8%2Fs%2FYxyhuz6r5HqT9yjxOavSAL8SFOdjgluPLSEYkHnKsdraTCNLU3C2CRnRg12FixJIpkjNDQh2V2LOMvsezm6Psh%2FWyq5nA7U57N%2Fh0RGE9iB3BgJFSNC348LGkDT499sep8pijQm6R9PN5nxwFkFJqBNuxMyowW0us%2FF3415Ir4UAhWKiqQdi5Vgjzo5GsbcIF0tSeqV3KqT9A1FiJbqoDaKT7t85P0wDd8Q4WBrbfx4pO%2BRZ%2B5As9IMMDbCWDYh0V6nAxwDgx8uDa0EnZfnOjbe%2FNu%2FU4%2Bx9t1z%2FaDu8GqGs9YKAZACXY4jowJ4tePKuk4tSU2UaWRb%2BJxmDb8nqLgXny8D7ZMxe1Mr4Qcu6jC37MnwNbPgxNP7MruWoVT%2BD8I074qLDfvnjGEKzliC7tbZ3KqoCg2KEcxgqxykO0VgnJDKy%2FH2rbkVdW6%2BCV%2BH9W2ap3wooDKiUVtdRYwb%2FuIufsagB2VuN2RFlvxaUIP25U1gg0rhg3bH%2B7ezco5uTegicapINh%2FzAcu9xrSWX4z1BQP4pH3Am%2BmEAMKKc%2FLwGOqUBCqFk6MjWhz3kv4d9ka3aFWctqCJKhRPIdpB5jvfys7B4ySuynUscIpZ3D6w6%2BlNMNXDI4zU5kbocGY70Hl3BzqE1aMm79KuVK8khVR6GR%2FvzKtt1jGDTHKurk9S225uIwEnGqwGQYAkiZ3VbpUALsa4yJyY7dSVGQ3FSzI5qIUQkiojm%2BDqPIDdIp5uCFrU%2Bq8guKu%2B%2Bd5I42YJbWWS%2FhdC8KEGu&X-Amz-Signature=b18e1353e615fb771fc817cd11c3909d81e8b56c2457e92088e496187be57e8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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