

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SUQHFKO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcdRPHzVdcdc7KxOphR6%2FFzr0LrLu8hU%2BCuJhJcl5DgIhALvLf06o22nzkzCvKT9ijblVhlZ1LAe31Ns58QBsQ0uwKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE2HjRd11QHm4Y%2FbAq3AP4OmpuUTrjlWXs4Hp%2BJ1394REocdSUJX7cUEQiTpLgbwSd1NwazfTPpTiFv1L%2FhxFsVbxF%2FKVXtK6mn%2BIg%2F3o3NrF%2B5tEW23Xlhp%2FqTV6BkHSy82NRbIQ4jOLsx5C62iLQH2pEwKbEUduN%2Fg69F4u5nOwejpQBeWp%2F6yaXbBC0oDPoAg2sNo6T5IExc2zZLx7YszLS1jqDdZGgYHcYHBoMYhR3fLBHgnVdouy4V9uo3%2FJSD0Cg7k6E74Fp57dJqBKz8aDXSz3g6QGjQou1bs2qb07XH1G6TSjCCxQtJJPKfCKOoC5p%2BEEb0xfOUp7ItOkhbnutjZ6BMvEfJf1EUtTkOCys5xzsA15tDY5F5xrlvS21S8LPpx0UyR4unZL%2F%2BRN8NbTSugwtqlOzZSnewjoWgUy1c6sUnreTsmA6w9m%2FOvI4gipn9cZAiJ3n4w9SIIu1b65kpNF%2B2jkdZiXiQG8Toath7D7q2TJKvwvJUkNd59rCoewtHobsg6bJYF2YCtnoGcT%2FioTuf8MEVe571c1WzJBrl6xBuAJFtqluD9BZSlqx3xgLYNzjh1z9ELysLxONk6g%2FnXqRPRnFLX41WYxEX%2FOOG9TiXlEHRJd4oKp8azcyfo0SKxCro91WmDDS3v68BjqkASPzn5EtOkOndJdZF91ebsnVRN%2BMkoKlmazz4fEDQuMdXHmOwxPX2pVPKI22sVpph%2BTvjF94n06oDZC9Y%2BgWpbgwp0Lae2USHD5aya3ppnmRQhahsDnR%2BsMvMNcsmm8Uk7sZavusAOjFsRWPdHkz9vwpgmU5W1Xs%2FbT0vWbpleT8gA94cknREesDHaFYzfp12AFfyzqF6OtVDgtwRpa0tC7dyS6D&X-Amz-Signature=f7667833c5bc18a1920b8363c0df6b6d47f9363648bbf9b32b0d18bc84a84a02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B56HTMR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDSH35e7N%2BP%2FGWbV9H%2FLFyUlctfb4aBYvMOQYB0ikZNNAiEAvwuysvXAyXNsmESCb2dxQ5nGwdoAHfESV8qrsgh90ooqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNEw0dReQWOHaLt1mCrcAz%2FE2k0naBkL6TqCQ6nqr1niRzn9cJFWTmO%2FlJIHmnHF6A5grwbDWjFYppbmpiLrlt0UeMlgLZoogCcafieFh4rEVyV7qoZTOUKOe9cfKej5EOR3OdbPYeB1xcHaA0mNnR5V1QjxO7%2BSlf2bUllHnw%2FLgd7voCUm%2B2DdDAMYTHjyYFqzoSz6Gn6HbVir6jI%2F2nOX1Eoe5AQB5q9EM9a7XiDrJ3F4WYN3sQ1ShjcK%2F3oUTn5%2Fp6rLcaCngcPLKfuqqBeMIyo1Gt0Sf8mVKAnlirGv4DbNOQ1VWCq5w5Wi%2BxSupirUhcAcJWzpwEfKhcsyp2hm99nQpIiKD%2FlGNuW3%2FDXXz%2FIEYNbFGfA87vQF9tdzBqFLZM1Xc%2FTLisEAHPBh8nankSXqWAAW6XovE2oJp83IoxES%2F8M5vZrfc5xVnCMlbPznfzqkOigJaMWulR3FfaYxUHbr7C%2BF0xgMW7U%2BCVOOxL2J4ZhoD5PqA5dygzDW5USMSFhOmXLb13pjdBvGvQLGV2bzGrsZuxAwAroe9aq%2Fe50U29DCwFKdGiUjwgNkQlAiV4AaiNy0tDFY50J0iITWXf54NI9LM5lKXNxHTVChwJy63TYQ1L2TrA5fVAIlG4qf2heXLewM2ro4MLzk%2FrwGOqUBeviZQA57%2BBlh%2FEdnsKHSL2TpGBqWRw3EZ81%2F2tldIvrrMuKJ5sMTL252zeGhZs6zNQEs1htiYW4UdHDWQoiGGJEW2ofH0byhKv8c04w2k6oUiAiYxI0%2BFEkEc45CXwbuXaJnHlwDVg5e3SQp2HtMPUljbRTxEpE%2BBAH5IelCHgLYMaYhNEyMylXCV99eqQeWgkeXKMe5Qw1f0BDSkn8X4lHfBDL%2F&X-Amz-Signature=3eae22e63082a4198b6f8bf0a969a0c9a23fdb748d987b54daa9026588f1426e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTVHOSLQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAtOfopBbz9s6Q8KX9fgdBD3hCHtiSaQ6U10oiwDVpJTAiEA0d4IPB4SiCGa%2FJnvnIl4SkHdiBirHGuXIouTwj%2F%2BVPIqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYY74sRRSvE1H5GICrcAyqrc9emZQ4LblerwM6PYE8mpbhPeN%2BbNT0Om%2FHcKlDY8MiIAO4ke8AY38kqWIXB6O3NeEn2eFQj2KrDjP9yJ6ifu9798dPWK2eg9LQkXk%2BgjCpgKPI%2BZziGI%2BE%2FsqZzEiRxWRZRy7s2BLyGAuL5Mc%2FgnjZpQhO8egcXHki2jlLfqg8RJJnGLBtyMUOZH1L%2BRFeB%2BDMvsHxK%2BMbrfkDuALtGeLYivUyHAbH%2Fnr1HcL6CxI7lX41ZAnXsfq5Gou6BJX5tuqO%2F6%2FeZ84hgRwZ4KzROos8vhy9lOd869yB9dVUz0TbgJpbF%2BnXLDlLQ9ICK9berDb%2BTz2qGPTdaXXp0p86uOKwisNl%2BnluxQu9%2BLN12VcHcsoEO7UCsAKB6X4NwkOFYLx531um6djgucqPcOFeYF4mMa8Zc1Hy7w%2FVsw8QyfI%2FSiQWiqVP%2BDsHROudbYMzkhPC5oTPb0oFIDMSs%2BF%2Fr%2BN4draQu4YUz1f6Q74redrZV6x6ubSwlwGB%2FYIQscB4ALYd7LOJaRj%2BRD%2F56FQI6LhQchGK8jVkRP5BCTsmNs%2BOUFVkvhEt6CPdzd9ZZSqY%2Biaiz9SMRm3FVL9DU%2Bdxx8opjehHAdfLLxwK0nBoLQRx3ytyj8smXcAfZMJLT%2FrwGOqUBEqAO%2FeZcSFyQO28B4iIEBebk8ybCIu1SpjdzYztTEouAGP9e9hCSpcb5lKEHAhOSFAJ0DKV7juLWfTRJKj3Lag%2BVepneQeQE77%2BGfIzB8w3BoGsBnQ%2FET8cdBCh6bu8TiZD%2Bi%2BKQhse8mRVvT%2FRSIXRGglnk3KSRcovuRllbAxDfQghuDYXWnRV8%2FQXt0BDv8b2Pxy8OmQeLQfcRmZc3faUjjZ%2B6&X-Amz-Signature=d19bdff8f8eb8ec375b3be0b33b4595d91b1628558b86d7448e0a9e10c6a766c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6SZPUSC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjOn4w30KGiR5nJ39g03mDCqFi74KMlNHH2d7lV6FO6gIgPRj9Z1Y%2B9nXn5UWS4Q4x3BbKpMXNb7yIuXjf6VyU0ssqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLOfPRJJFU6VMshiircA0TJJczGUDLLnLXa3FRaktoTsRBTHLBPdpqEd698DcdFZcL0Sk2a4TTKRAMf7GeOS0HT90wmH83hRTPDjLjNsdIfyd9mrqCefWXryOmVO3R1Bli%2BKaOgbZMEUgaqZOOyjP9AkTPCl7Ecr%2FhjUcgbZ9t83tYh5N3QP8eyyRnsh7Qd0%2B%2Bnh2k2sT6g1sv4WP5WaVnuBuSeyvYXGakcMvQ%2Fv2412IhgKqylmQdVvlArn2UjaFf8fuy2C2yMjcbqQxelvE%2B9lV%2FPO3wnXuj4bq8B7QXDy%2BcWM6r6tSqH3cz1AdZoPlwQTUZ33vnfjnjwBbDj5ucuACERWmogSu%2Fj7Ry%2FqfAAH462w09vFKguzRiHFfNubi9njgn0DsWKKagaU8o%2BBAWGX9aeQ%2FmwkxY6TQf7E6hei4LRhuXLyWuB91lus6OYYEGL9LWa88Dl6F3zfDPwY%2Fs%2FDVH%2BdBZnQyZ1hkDrNDCCDmCKNApoT5lloXz5X4HG0wT9iSvCv3h5L3agOSDSchWcfnAEMSCN5YvnK%2FxiDbGl542XnLh%2Fr5xTcFXWwZQVvfdidrxDxIUcSrQrWllpGUuSntRONYSVMhl1axofBugDoxV5ujEIppsZVEaWe8koGMO6y4WalwjtT0uGMMPY%2FrwGOqUBI8aMFviTv7M6yjbPvsHECufJj%2FUsPEcP6mXsr7sxRfoSd%2BDCj20fthfzEW1jWheqU8SDpjCD9WSW68WE1mcflMutJ3Z9iySJmwlt69bWfe4WhAgVXq8rhKDTJE88TMUyFNZJjxe6gR4eZBnhKGFDZFpRu5QQPzkZSb%2FKJHkyr9Ph3JMd5k2q7BnNhoKHoMZGH3NftU4fjheiWOhYsXwR9%2BFV%2B2c5&X-Amz-Signature=8ce7a63d53ea4006e2e7729083cb1735704bbd09bcedcf050be3a57f14b665ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPESOCG7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIfynQOssfLl1tRIWOHju0BeF3nDSBSvEipBlfd8ZRWAIhAM6wIOHnVId23%2BFMHMRjh%2BJB95gQxg2Br6IPtMKNlqSNKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfkQfJRxbeNVQOD8Uq3AP8ymd9WCry2RQ9QhS%2F%2FiCtcZW8Oj5he9AsiVjmjf6KqNY0VmtIwewrkq%2BvtR8nlNLLQLwAISkUnwmwTDiR2Fqqcpotg4eg0QGQA24z1yronuw9cZj6rVtWUBuOFPEKY0%2BF5C1RjsN3DOL08l3gVA%2BONZAGUKAeEoMSHkWnharj9x9JG9u30TKdt%2FfRxKZbqOeB9WZJdKBS4P4nbISGVu6Zcobxu3WNS9rsQP%2BxOdSxo4Itxff1YGfCBT%2F3mD1fFkKvCRAZ9w5UpPWKzDnZ6YyksH51tEjDvfsyPKkfSjOkqGuc%2FAzxv5uJ8Hf0iL%2B7gd9fdb6fabN8v9MgOoDMJ%2BjbYHYRs%2FEESwC7I0w56qnauluTqq3QfrYbw%2FAJ39hp5dl%2FeOMKFTKxILtCR8CsuE%2B4o5HCG4aAERXkJqn6cIrK%2BpMQKm7Y4RtVdbWS40XxNay%2BSWFOK%2Fmpp9jINAyAW900IOryqFg0Ux%2Fo3B3Ri2oU89Jp8RypGG%2B57tFiJYQcMXBKjL8Zb%2BZYtuvMJszeMRFBYzXm4cl8AFEKA%2F6JSzy6EJbUhNTN%2BRJlXSBhjoN%2FpPJ2vTMmqFL%2B9TxGrWMOt1nnJeB0wVioVnYQITLl3ECNQpLb8tpp1gYQOaGEYDDY3%2F68BjqkASYaTjuhaPEq2gHbQVXNe5ktYnuCLt6eo11XQHh8pwpT9xshV%2Fm5Se%2B8Ml5Zzx0yotJFzyeToYzcT4UbBqY6L5F3SjYxiuj%2F1ba0hHepEvxmL3XuNDBcEJsij4E1XbsS75Myr3J8lyt4kicy4EOQAckxYYdhTCI1xvalz5xt%2FLE379yr6AJg%2FaEVD2JxZpb8LD8ZWuztHdhU1Cfyn%2Bneg%2FY1ERYB&X-Amz-Signature=6024ef42f75ae90b57c7183fbbab4a4fb6fe48cf091f8a59790a23dc6a1d51e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X66V3Z3F%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCByvIlFH6D%2FlPWVnIDHnzH0%2BvG1YkiYTK3ma7EcvN02QIgWMSzhmDYO7lMj3ZdwOp%2Fp3dCpOId705dmaEe7ee6iDsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGHNauJBlot0yzQPISrcA2Gql7wx4JyU0TQDmwGUSaPw1pIIU4J5aOqGfKvTRae%2BFuExN09aOTBVvcSOHmIy7MldtprLJn9YqDKUmr3f88pih86M2MEyS1N%2FCgvTl7cZMOLjiEzCWewPSXVnKZsfXWz7FytA0ugS%2Bjyo%2BQmEofZxcZJh3rx8D8IG%2F%2B1xlm0gnVU1crR4NNwp5OuUNWeLhjJMdMcqcqrZeiHfPSM8mYrIYVUqrMl0c0yoELAeepVCpvCV1X9yioU8BqH3Q9TZwglidqfQy%2Fz7Zu3aIOzdvDsa6vHVgG4ehyDnB0qhJu%2F5Tyhg%2B%2BJQhPVz10J6MMUselu%2FSIf5LlMCV%2BxJZlfOxOm2ZLoKcRXzbG6udOSKD3RM3QQGmnk31%2FhBrj3LP1gikUkRsu%2FTAW7p3T96WZS3A2lTUDUOz1PoF5Jis0SBu59E1O0VHc3%2Bq63JLxBesoxA%2BJjmyfqCyjmy5T90ZXY6sFAyb7VIdfy3aLRFOhxt8YYu9teLNBBzF4IPBITIexCpUxGrI8Qcrz%2Bh9KR6m%2FBqQXhckI4FtMNCbVwG1Aj7cIYTIBgSRFkA3suF4xR7jIQqKNvUrhMm38NM4ZaC798ad8rBAb6Y1z0VDuuoQGWxjI8%2FsVLs1GfJR21%2FP8%2BzML7i%2FrwGOqUBnyFXVdPWsSxDRDDi8bsTqo3A6TiEl7kwELGYaBl5KBj6Rws9vwccKyOHxOH3F%2Fb8rDXkTy%2Fw1ME5LXhzU6eHjybW50eXbxDPij8bPJuXs%2BfYLUIiS6mXVfHuccNR3JmUX8C3XTe5rvieJ%2BgsO0f9wZFJtEvJd1u%2BEyM1gwkEMNd6HuIEGaMla7kiQ%2FcqKhRML%2FS737iypGRTJIjJUI3MUgW%2BstnV&X-Amz-Signature=7de35897ed30c6e7503c21919add5a3a7baa639c70a27ebe3fb18f0b492f0762&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665A7XCEGL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE40xUrx%2FhrKUGQNS3cTz7FbtDG%2BviB3RaxsE2N7uiGUAiBZhQ13jWBbWgdpr8E%2FZx4sKP9eGIYy%2BDeUGYJ%2FXSU1LiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUOZ9lMQhqYi3D7GXKtwDAIboR6FwLEfXiT5wz%2F9r9dU4yd5bEUkbVnLrIiWQJ1xLNsf%2Fa5mx9171UHd1R%2Bu2fAv9I2JiwlzLj12%2F6ga%2Bg7dADsy62qic%2BPpD%2FblcrWff9PjOXOIhc8q4A0LjRrgdALx9VZkobbx6HTf%2Fh4N4pRBOTqGTfIEEnj99GPhnQB0oyyaMal9znLxIog4ycVIbcbyZqpQeVotWrOVgSegd04qyc6ypz8vtcZNBIJvm0bC2UyTJ8wIhAEutPOd6%2ByCgyfWW270Xzym0lMMXWP0B86pTxZzPIe066CH9V9E5Gp74t6RugiGonO8ILCX9x7rSGfGvGGvad%2BdNd2Mqo8q3mohfU9bYgq9f6P4kjfVcURZaestMdro%2B%2BXCugBnWWzswfWfh88NPtHG5TBd9SXWHpoOHQCS0IF55jQ8BWI5O2Xs5r7pygOZd7qdkOIJlxuodRO2A1DJCIcxNBhKmYZZQCtT9AQEAPWvW1pNfo4n%2BkLA39%2FQC9hvsSE3vs9HQyvCaD29d5PBlyPjLXb%2Fu4c2rAviYccAAa%2B8%2FkMzJj9CCB%2BhCYF0y%2FafCErvBoyzZw5obSUvgbReEA3DzbAlpNN9u73Ur82dPH83pxzMlWHo1gSuhPt%2FtzKRXTfcuWyEwytX%2BvAY6pgGt8pg916ZHSlcGWkvafDCdXEcMfCQkx3xWVBNTrddfXcpQMMZZnIswXLkWL0laVUR5U%2FZGvbk1yyl1KQ67LynEAkkDn77tG5cryYlUvkNPLGU8ZAw0FPhancSkYYGEfOasIbTI6Y7iDUV0qK4PkjVpx2CpBrPKVt%2FbkHzy39ucAp3K2Y47C6zwnRWG3gPZx5Gzl%2BubSLU%2Bexq6uBLINxjREib6WXIn&X-Amz-Signature=ffc375bba6b113d568cca4cb8cbb55cd210c6e42160b66436e183c796c93e094&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWICT7M3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBksridPi6S%2Fw%2FCw17U6u1HqxRWY6oD6oLx2vg4HLrowAiBGUtLsUb%2Fne7GJa7ilIEjrmY1dJFxPcgwy6Y1B59FyzCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnSBCiAYcP28dDYURKtwDAk7OxdvufvN41vH%2BrZJeURknRP9IM2aYQ%2FVkdSUaEYi8szQyu4Bty3l53jXh1yEZDNGDcNA54qrAHcupU81t0kgXZAqBZMiVwA4%2Bh103Pb78LfaVFTNPINjbxM7gENQaGpChvYt1EW8N61%2BWIl%2BQC8zvM03wkOE7PH20jrQWrupZaPgqjgg%2BKcrS0fDgVMAaBIBkWohZp3Xsb5O7IGwsj%2Fah7MMcnPelnzg9ttsMPvsPzGCBXbnIlfa0NPVuUhCbYzPmO2Ja3gV1gSSn5GxHaorOzPiJVai1eA76YdhRmmhnt8%2BKxfAqEkH0x8RdSEXZva0BZFpNi5qhuVc4JZHmFNF3j6bKNxG1eASQZsK2YO%2F47Jmt%2FgIWIenj5AVyPK%2BQctzuJN%2BXWgerJd%2BjowQn4oSjkj%2F1sG8pnyx2xC796No2R4%2BGFZdTGFemklJmgIJ9s2HpqiMN9Rfdt0aSM7mJzqMBM61aLVJu137nbBSvW8fTIei%2B4skLXZCIpbxEqZXSJ%2BEU%2BONI9xE52w5IejfEsX9bwIAytwGJvRJWRjjIN1gLM6OeEc1mouJAwepCLTjnAwO8oTERUJUekNIjDqfslgvWZy2WDJB9cZwMr8PoNjK%2FllqEQOfJ4Wt4QhQwz9b%2BvAY6pgGWgnPUDXcajrUL%2BxVGYdW34UZBfoqzOhOPQQVdEk4NJZ7m2ZaJK%2BZuijX%2F5j6NfDwlX27k8BXpbq362%2Fjyz4MtlOAypIVEUYAdFEifmATqRdozMtX%2BYlRE30g7Qfa7ChplKVSCpP9JOU1wjqOwhpNCzOWMT1HqQcczwt78IFMQADJ%2BeooDw2ZVcv2%2BvnSXWgeK7jH7whP0di3Qklvt6jAH69quyvyf&X-Amz-Signature=f7f55158944ebc541b1b00e8b787c2e8346be04b38e4f08c04ca7cabbf7f8f33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPESOCG7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIfynQOssfLl1tRIWOHju0BeF3nDSBSvEipBlfd8ZRWAIhAM6wIOHnVId23%2BFMHMRjh%2BJB95gQxg2Br6IPtMKNlqSNKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfkQfJRxbeNVQOD8Uq3AP8ymd9WCry2RQ9QhS%2F%2FiCtcZW8Oj5he9AsiVjmjf6KqNY0VmtIwewrkq%2BvtR8nlNLLQLwAISkUnwmwTDiR2Fqqcpotg4eg0QGQA24z1yronuw9cZj6rVtWUBuOFPEKY0%2BF5C1RjsN3DOL08l3gVA%2BONZAGUKAeEoMSHkWnharj9x9JG9u30TKdt%2FfRxKZbqOeB9WZJdKBS4P4nbISGVu6Zcobxu3WNS9rsQP%2BxOdSxo4Itxff1YGfCBT%2F3mD1fFkKvCRAZ9w5UpPWKzDnZ6YyksH51tEjDvfsyPKkfSjOkqGuc%2FAzxv5uJ8Hf0iL%2B7gd9fdb6fabN8v9MgOoDMJ%2BjbYHYRs%2FEESwC7I0w56qnauluTqq3QfrYbw%2FAJ39hp5dl%2FeOMKFTKxILtCR8CsuE%2B4o5HCG4aAERXkJqn6cIrK%2BpMQKm7Y4RtVdbWS40XxNay%2BSWFOK%2Fmpp9jINAyAW900IOryqFg0Ux%2Fo3B3Ri2oU89Jp8RypGG%2B57tFiJYQcMXBKjL8Zb%2BZYtuvMJszeMRFBYzXm4cl8AFEKA%2F6JSzy6EJbUhNTN%2BRJlXSBhjoN%2FpPJ2vTMmqFL%2B9TxGrWMOt1nnJeB0wVioVnYQITLl3ECNQpLb8tpp1gYQOaGEYDDY3%2F68BjqkASYaTjuhaPEq2gHbQVXNe5ktYnuCLt6eo11XQHh8pwpT9xshV%2Fm5Se%2B8Ml5Zzx0yotJFzyeToYzcT4UbBqY6L5F3SjYxiuj%2F1ba0hHepEvxmL3XuNDBcEJsij4E1XbsS75Myr3J8lyt4kicy4EOQAckxYYdhTCI1xvalz5xt%2FLE379yr6AJg%2FaEVD2JxZpb8LD8ZWuztHdhU1Cfyn%2Bneg%2FY1ERYB&X-Amz-Signature=de67beb19726992003817d8995a66c80ae89ab82f976e7e0d397f5c70818227e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBRVBDEP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDum0cClqAoh1hdmmlgm3wGyaIPxaJwNsbYazCWFN2kVAIgKXssMC4%2Ftz0APJDa%2Fhz%2BmbGeL5HyRsqbz1UWdeNWFyAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMA2Jdj8nBrqD1UaJyrcA22EKRddtGIfZkVM6gSP5Ljia69DfaorFF9tGf444l4I3F0WBN0UMjVDFrOW%2BL8sadAucwntADTDfhKnazAbI%2BJBf3V5%2FVBfVo%2BJ%2FZKd%2BJAR98iiLlVoisDwUXJ1alIsoWJ7pGc3p3dZ%2B1%2BkIP1JbivssbfeqgT5yYBaPEkYRE590ODbW1iUgiMhoqlvBopgJL%2FtQg23W5SmRnhE0tq9TYhwUis3jRixuh%2FOI0nRnTaqiirMYLaCg8N97VtaS0mDJXuOizwiI5KC%2BfjcsprjSF9jUECGg4qhvTfAdDLGm%2B3yCLbr4tsrTnYF33njzBh9C3SjydVITqmIzRMVVL9rNOIw3FY8yfS98ocKga%2FXVhgjSI%2Blmr%2FBfxdyTgedP%2FZxBCvYnNaky1pO9ML7FKidUNmgJLiCpL4IQszM20bdQXYqPBI3naJs4l%2BF2%2F1jvNQwCdF9NCmArV6xno2za6XDslzfnnmmEx4FFMFj%2Fn%2FV982o0dZ4FZJ5ljjtovzz6lzeNL%2BSOhjZw9hhVgV3HRroQKrP3MU3m%2FOm6e8PxBx2%2FAlIZujr5xh%2FmkgYBOD1xGz%2B8HV7N8Q7dotAe7B4AjPxLsFBn4qIr7OILMm1IucuQco249iOVDZxyTND5ZgtMJPm%2FrwGOqUBvPAFGgarvlAWFNGhaORGe6wEU6G7ojMvUrXNN%2BF5WpM3JP15NeLVvuSPn%2B5qGIzr6Bn2yATr9qA83%2FE7EpdAEdSaPF90l5ukqgXjAX2Dzok0Hm2AWH3sVPleb9ZNkOK8DtvFnrDPSIS5jtT6f5PUPtji0%2BfklEL716It9eXuFgZMUNuujP3Ljy0sMs3YomgBKdWopPwsrjTaF%2Fk9ZcRBMwvZWHcf&X-Amz-Signature=b57644ba2f64f0744c3791dc99c310ab51b3e92ae426f001fb4184257c671f48&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBRVBDEP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDum0cClqAoh1hdmmlgm3wGyaIPxaJwNsbYazCWFN2kVAIgKXssMC4%2Ftz0APJDa%2Fhz%2BmbGeL5HyRsqbz1UWdeNWFyAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMA2Jdj8nBrqD1UaJyrcA22EKRddtGIfZkVM6gSP5Ljia69DfaorFF9tGf444l4I3F0WBN0UMjVDFrOW%2BL8sadAucwntADTDfhKnazAbI%2BJBf3V5%2FVBfVo%2BJ%2FZKd%2BJAR98iiLlVoisDwUXJ1alIsoWJ7pGc3p3dZ%2B1%2BkIP1JbivssbfeqgT5yYBaPEkYRE590ODbW1iUgiMhoqlvBopgJL%2FtQg23W5SmRnhE0tq9TYhwUis3jRixuh%2FOI0nRnTaqiirMYLaCg8N97VtaS0mDJXuOizwiI5KC%2BfjcsprjSF9jUECGg4qhvTfAdDLGm%2B3yCLbr4tsrTnYF33njzBh9C3SjydVITqmIzRMVVL9rNOIw3FY8yfS98ocKga%2FXVhgjSI%2Blmr%2FBfxdyTgedP%2FZxBCvYnNaky1pO9ML7FKidUNmgJLiCpL4IQszM20bdQXYqPBI3naJs4l%2BF2%2F1jvNQwCdF9NCmArV6xno2za6XDslzfnnmmEx4FFMFj%2Fn%2FV982o0dZ4FZJ5ljjtovzz6lzeNL%2BSOhjZw9hhVgV3HRroQKrP3MU3m%2FOm6e8PxBx2%2FAlIZujr5xh%2FmkgYBOD1xGz%2B8HV7N8Q7dotAe7B4AjPxLsFBn4qIr7OILMm1IucuQco249iOVDZxyTND5ZgtMJPm%2FrwGOqUBvPAFGgarvlAWFNGhaORGe6wEU6G7ojMvUrXNN%2BF5WpM3JP15NeLVvuSPn%2B5qGIzr6Bn2yATr9qA83%2FE7EpdAEdSaPF90l5ukqgXjAX2Dzok0Hm2AWH3sVPleb9ZNkOK8DtvFnrDPSIS5jtT6f5PUPtji0%2BfklEL716It9eXuFgZMUNuujP3Ljy0sMs3YomgBKdWopPwsrjTaF%2Fk9ZcRBMwvZWHcf&X-Amz-Signature=51abf7b0dd7b19d796e8e2ce07a1dc03dd9d9d9ea4b35f8406840e2b7f79fa9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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