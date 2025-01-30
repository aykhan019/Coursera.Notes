

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NX6PL7C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHPBqle5D9FQrTQLm%2FOb%2BPBbdxeC9w%2B972XeMrFcFt3PAiB3nPW7LPGv5WezBqpEHhiqDGlz5bNMXODvHSmkBJiq0iqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMviAhTt3eTE45ASy%2FKtwDyN0ebCBn%2FrHGyfOfL7W0GZ%2Bj4S8B4Znzh5CaIfNBxdieY%2BWK6gBA69R164tjMexqQAbxKha9o74lCgFlqSSyR6tnaZtFyF0WZqYUeRjV2uwt4YMisE7gkorWK%2BrtajSC9Fzkwr%2F%2FFSJJJqSzW3nAYJb8mFwmmE4%2FyXU5aIY9ITgizIh%2Bg4h4CVNcnnwxcF4xqdHqugo5ceDrnC7Bh3lWilXZC5OorIwkEqgd8E%2FiclzUlLRDHeFuUCbIYOse1XbclkyKF4ecbhiePmj1jROernr4TiUoYzTjaW6t5ZU7GOQmVvj5C0A51toYhl5dSjuiITGYGFQYCqiUl1ejJLtgV%2F6GdGWRKUrGsvg6e%2BSy7mcpL%2BVv3PEayvVxEUL5i3Pi9MZJsRnxqnMC%2BtuUUSOKwJTcp%2Bv4B2fBBCAveuyMbfMaul1Y6u27Rv1yzSIKseEQ20113020vVXwgwZ0747DQJp%2FxCfgh5GKUIcsCLVBC32bdIq%2FELSMByUyJo3qjaqUHmyygvfMc3nH47e10L%2BoOrhLY4U8CIT1uTMxpEf0nzQjG%2BeEPBcuBRWxexR%2BhPnRC0l9PGOXh9YAkuvcEPZojJAjjirjoGqXXcMSJOhHh2xL99%2FCQJHK6tuF3mYwrpfuvAY6pgGetarrgTN66W1SDdGVrWgjoeeZWoVx92Fj16%2FeWNPKU04QJbc9It%2BT8aKgc16L4s6Utz%2FxBSczz7IvnG6xZeFsNkGDL%2BINdtGmvl69r6XhJiKKkxJwLuKf69u8wYFK0t03WsynuhSuKy0v3CcECH2lV%2BMxZMNiNfn3cgNO4KNTQ7V4o4xyVuDaKk10WErcydYZdooqnH4445ElEW6LyigMWBE69ApV&X-Amz-Signature=37262cef43e8211b37900138ffef635939fba1b28fad470b77309461c2227769&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT6SM5II%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBKDkRQ6ijiQyFcfChcxr2isHWGw9qiqND%2FbCBff5mi8AiBAhRyKdguGQVj4OPbyFr1EePSd8Ad7TwuhrC9JiYLe0SqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmZhlru1XRGD1q%2FU4KtwDzyEw47yKbyTPuF0FJr2P1w7DpwEN5jluaEEnukJNz%2FNz%2FQwJ2ggrV3viIZt%2FTONfq9E6bo6Uj%2FVy0aoZdgWjSTbeRrTQ8%2BrM7vJ7mC81fA797N%2FcfGxtfLG%2BmOm9uL%2FvK%2FARBH5o28n2mqP1t4AeyTEmZK%2BWf6Uu%2FLZ2fvGU9dV6tFEEPH%2FFcfM5yzH0O2HY4WbGwnH86NkCfft9JN8pzxaATGBN0uCXOidgbQHtFiSzeFXzfR33Rt0SM7%2FLBpw8ronHvEKVIs%2FSrIGbp36a%2BhKahWNOPOC9UU%2FTC3wryABmBs%2BXDGzRZWfRABY53lZGIwdHLwg5nuFLrN13m4LaV8Ug4kLIbPETnqDuLdn2rJQDcKbjWrxmTs%2BC28Dvnaq33r%2BfJ7NG2augdQJDSLkeoREGye16CVMykPoDv6D4a%2BKdgH5s2RVyDxkWvKZDMmnGRPep7alLJAy0L%2BWd0%2BdVpPsMMlie1eNAny3P1E75v%2Fje16wD6RF%2FNPuAXmUgt5LA501vMVf8NmULxrXhA4ypJC0LgFihPSUWNmbIyznNP9dGvMvujwjiycnX1ja9TNpHYDmTPpMpp%2BBu8gDYaBD9vkn71P%2FBWc2weZ9Ea1oYg8trcSZpEKWm6LxyJ90w35fuvAY6pgGm4uPOVE2kJ4dx8sRgfXjc0j%2FV4oTHdcqRpC3SZtTS%2FWQXp59rEZHXKEe25yjeI2vFlEqjMR8orEO7XT0UiuHCxyMercXcHoLnq5y3zIVx681RStCbJV9qfJDPgo2OxLhlP0RwbNq2dkhH37rGCdIucfja0cfJ6LdnT3qzwH8SpVC4LxBUu2qmOIktXNyUfHH6rvTK74fNT1VkfSndWAZem0oJ%2BCgT&X-Amz-Signature=11211a1258a93036aa8acc18b7751860e50e77803058238b34a5aaae59f6d606&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6DFSA23%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEZYNn5%2FujTUKWfCukTaZcGksLD7MhcHtKHw9WnWxaGMAiEAgp6sr3flz5Y0YWipNUj9Q7sqA7BAt0tXrtjhz6yxi7UqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO19sFc9mntKmmvPircAy9aWT3Mx8UpxdBBhUu3hCUIurb35yJYDwKak4n6sSrAHPPUWnZMqtWWn%2Fo%2Bmv3pPG2Mgdltn4%2BnqKx9BSRLajGahkDiT9K03Zf3x%2FPvxPRxTkXlnqzrtzHhTm1S41mLG%2BFK7ri9l%2BYlVzFz%2FusVlfcuaPAKd0%2BzFsH9kmiCtBk5%2F%2FdHPwKCYqLJpDJlFJOsPWZE4P8H57RB6NRYUyQ3obmubVs9%2B2EfsMMNoGse71mrPfj2LkCArLxCYFz3zvx3uVhwa%2F6yYAOfKLlH31YFF4ZAzE8H2LVt4j3mR2z%2B93I%2B87CXKsHtDv0K6Ttb%2Ba35uOusR0Bn6wEmfs9UH3yJEWqvh1qQ%2FrJ53kgk4Tti9Uoe32HM%2FlW49MCw50symYpu%2FX6q8zjtCHQdrrfrdc%2BdBIigOOmC26trcq1U7bbfAYAkyR1icXzfybAv%2B8Qv89jmXS1v3vO1OiD2%2FHaVlQTZEfvBWgMFVVa1q2neVPcyVM7A1N2Z1FrzDPIKctwI%2BvGx9hqeOVVEx%2FjRYzxBnAP9i0KGrFx1YzZdIR9IfDmSFRk5GlSDgIdUy7in9miKyDS5kxKwwX1XPPblkOmaaOjNzeIwG%2BsYheEvOHy4ZAjxW87qatMzND0PRfpvziMtMJmY7rwGOqUBxK%2FGGHMTNrm8WYkPCV2s2lRuESC1Fv2qJdgrnBX9VO%2B5otFvRXo7hS9qWiE6uz9s8uP1M3UIxBmu8tRtnNIvxVtTOmiPC9EjXDcqygsmbLlWk88kagznP3lxysXe4af4kLoPE53uSTZzdvOnYzI5rY%2BOfixygMAEES1QtPZFvCgDm2hR55HZ7%2BUUpzoeUx0nY4Au4lUjTsiQ4unB2hFcGBrssk7c&X-Amz-Signature=0412284814d242b27214633171b251589c8b1df891eba49686d7421137196e27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BHV7KTV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHNV5Jg7kTBzPWmyGY6q58fkA7Nw9gx%2FIS6qir8HZsg4AiAor1wvnt37oXobGHtPfzlgRsBXJSipmwt84hI2MC9NdyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNEg0NG58ha%2F0pg2pKtwDtIQIrB7O5fmBPK55HdEMcan8%2F7NBxXuTFPPbg1d7DjEUjLEr6uXAa%2B0FXpXwzSxEZAi7IG8JHcB2TrzHInO%2BNQS6bWOoxKj7c1KKLfOM4Z5w2BW61YVAI9jKMy6Qrl3qfeS5nNtcLUe%2FkEAuZFsjhhJWLyYvb7NJ%2FkIyK8PPnrYnbxU39loCugLJ2we3Pr6EM%2FtJ%2BpKYygg2wnUgG4L19Nxw9MnrnYvaJ1wp2h7lYagsLsNOsY3xBMBhXuTw01NAnl5zQtP6bm%2B%2FeTAIk377%2BRgUbDD2tfOxjn65za4ZwtD9fGsBUUD7oywI7NxvM%2Fz2nRkmcJYbI1jvYbEGwoL5POIh74h5xeflF%2FCahTYT%2FbZ31NiOceYd8wLXyoGmZ2w7TnqWNi3Z5Wj0jHhUhmH%2B09OMhviCfh9yXVfwMllsRY73FW8tL1w3u%2B7jmRKK7JgHa6neeKlaKXjbr43NQ8VLQ7m9h2eMarmik%2F0D42k4Fg60u2B1HlBa3X49labH9ZhG4UlqDWgAcWcAH5lBOUXA9PZTKE1GE6SjtVOBlaiKfphxAuNLSxaz1EzIOm6a85PvkW0Cis2CKkHGa7YZNmlZh7cxc6fM4qPG9Y0TvMkMkFe59oMz1Or2AzFDk2Mw05juvAY6pgHeHriQArbdN125KTWuHtlPbXkIP2RwEcNG6AdZ3Abg7ccsQutZ2ejg6FKXMNlFFOd6ow8al2tLhI4bbQjWGUTXO4bMroWGXiAF%2FIphSnfCR0IzKYcBx9UJ51hhtlbqj4KHBymDqnfcpqtWAwJWNGi5MsZAAmrqdHIGzx1HejhAm8SJrSiGxmfyGcnDGEQM0QJtQn0PepxfACgmSrkRUw8erDsFVcEe&X-Amz-Signature=baf6204ab1a6d3ca5ae8c19a814f6747a49d9eb3b042d3a32bcf5e36ba2b1cb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466524KJOD4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICWfm5LZZ%2FOBPWzBUV7nxiUULEEcD2of4kFPUurZ3nUUAiEAoc7qv1Wmuq0ZWRnFvIy3JiK7R%2BcV3wPBetNFoeI6P2IqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA9W%2Fhl66Esgia5wgyrcA%2F7TpmY4oPcXaxDxlR3%2BkLOzBjf6CtR5MJnHML1mu076GIDpGNTvffxNde965wrFhlp7hmJlNvurSSx489mXgLD5yQFsGCJ4PFNnbojntEPk2TL36CSgLB4buQkvDVMo8dL49%2BeubaKRUYAlV04ZBZ16aTbde7LmFs05TL65AFXapKtkObPR9Tii0G0CgNpTarx2%2F6kCKhJgNr8jbJ0Pv3VpLhTojbZzr8n%2F6%2BEMz4iUwpnRNNjPpjB2VjsHzGbNNeDIqnxFEtlmjba3aiXpWBvpOOQaQDbmHAPVKkqK3MeHqpm1Sij5X2nZVcq2zY8CwcQG1sInFmxDznQclnHxlpKkTubtoadwnfWJ7AHgV%2B1mrD5h%2B2QonBHRHutckfL75TR8Tr1x6XYTvsLDiuDQA2vczLCnalUjQgZ%2FSTd2CzbUn5Pbxq%2BQN8O9zhn%2FrXfqFUEDn90eM02vknd%2BoTM0u92GFq0gU9y0uCyfGR7htah89EiZq1ZTw4wu5d4y1Gt7sm6hFWJhdXkaP9L%2Fp%2BbPnkJ8G%2BZHhTH9GSEfTgtTBX0RD5Mvj5BSaiDXKTq5WRt5XMKg3QaG745idyH08d3PWXi1H4KUw9yqEyCBXiWL50ij5oKCw%2Fe1vtyW5TfBMNOY7rwGOqUB1Q%2BjI6UgpFKTgp9Dj5xgaWaUDdX0aEDjSylosiUWA%2BRWHtEzR%2F6WBaqBEszbM0wME%2BbAarJ1anxOkWXh%2FpmSnN70dKl5hrhMUnUj7ho0P4HGutVGZHq8lymt%2Bw%2FI5%2BFWp7Tg3LMNiGoIfCy1Na0Ie92ZQHezZ4tpbFCwVr6MAm%2Fxs%2FtVwpybu95EFLLoAS%2BMB6%2BJA7XYKuSsYySBl3hslTiOVFOC&X-Amz-Signature=2e11f05a8b8ff250a22d3be33deed033e50d438e35e3f7709ddcd0cf6bc07e90&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJWQ4NK2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRny7Q2vbtZDeu0nnF62izJce0AjoDGn1y%2BErn8MkvlAiEAoL0eC1lE9TyLxCMZPtcgv5GWZ0LtPrQRnCZo3AGgEUAqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmAR4q6ddk7K88BMCrcA%2FnFAsfhr7fVqCKCiT3UXMsAV41LwEVF9x2VKAcgBIoKXd2sGX0Z42%2BNlWrt5BPXK1N8X40bnayqM7T6M3TzOT2t20lep7Me26yA%2FC4ueBrlz09yXcW5HEi5mx1GtTZAa4bJwueMOUM4qhV8xOHKEija2nPQhfKzsaTfVXGkLEJiMMAhu47c8ODhWuk43MgOxSn6kxePjxPZlfbfmgIMrw6fVImJhx2vKtDtLdVc2sJUNeCFdajn7%2Bb4NFsvFPVTpsbCgHUHXRsoGYw3GHhRnXxdrGW9rhvIkrs5fj0LiBjwji9LiScprUgN300apd5oS0g3blfcW4YJVr94RfcqJdtkLmnYByX24aU6JlQ2gYMyyhq7AeLvSC6FK%2BeqLX5cPuTOGM2jKfqhOjEDmX2DQT2%2BaBTpta4X3JSrkaVP1XERGx3iVv0n%2BneeM5KrKVYZqOl8Nlmb3MiGp3xqpKrlVo2oJ9b7xlvxYvDL9%2FqEtB5oCTHGX2Yy9pPgitngw4VhpH1zGmPUV9sLerNR8%2B61N7N0FGW59CsG0qr%2BmjUaSukjkzfQj4uVguDuzlL%2FUWOCtoCw74AJcqbuyzMo0G5R4coJVGy7yKflbAJhHoM%2BNowBltNxWfCxkzqNZLggMJiY7rwGOqUButCEqv0%2Bwaz9%2Bf4LG54stjj5qWht1uYkSkRJ%2F9ytVX%2BW43gDJJ8SzCQxnAA4BplAyDx6XrtBC3ryPp%2FbyUNOr8TMQ8dSEzi6ve2MEDY94EVKZ8x0D9FumAzVqKfybwpJdnPjDCUUNoLDniBbuzSs7%2F4GrMxWq%2FwhlxcD64fiFDNI033odnvsWWg6KyDO37aoyIFsEi5a0387obmU7wSsLQbadEBm&X-Amz-Signature=5ad32abafc7395f4c8ec4465dd9fb747737ff0131daa9e3f18c065bc553534b5&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7J3U6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7mOXBI8%2B5c%2FxsncsOOpbNpy7%2Fv6Lc0OWI4UoUFNxz6wIhAKGRmVE5XpzL2bSQ4b1j%2BddFQ%2FK82fc9qxcpBPwOEuOrKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1%2F0z1qmN1XCRfeXcq3APyUcledkeFeQDFF%2BsC%2BmE8iVkhS25yxA12htMK4Z3Ep5iMZBPKZ0mEBaNBoBvV77rnz4WKsK39k0DLQRNkEfprQ%2FcHXIXeM9MWN8DbzVrBduzseeHq6IPSqBg9%2FFeSxI%2BHIRBFb%2BYrNVa%2FLKtj1KXzyC2XqiZE8jNrtL33EuZg8vcTWY4%2BxihWmKPsZYUUbXZqgsiS2v%2BGxHKI%2FwEkEcyc%2FZ4wOd1a7AOM1kuGZdm3zUhIBrAYkOAXgQ5uz5ukfaaru7qvTJL8blb3ofBECConQjSFoAPYNOB8uHJkyg32Eq4yjZDaGrrDigFVuLn63YCNxw%2BbRJaRqu13rkDtv1zy5SsaOpKvhmsynRkDmx6%2FX75Jj0wI3nA2BIVFstbQs4aQhKsCb90nn6eISkQ74Uer1CKkIp7MCdBpI6OHKuvJbmico4O6Vchs0ToNz%2Frm13Dkasy3GtwwJBnIiwOJhXvD57izNaPhPKy4DZ9pyu3ZYfynvjB8lin0to5fJ4PU4z%2FFZOniwwMckU7NAynL%2BfdiEpw43Q951M0D7vvmWPYDuqiUBMfh8kS7VRaisVezh0A%2FJfUo2LAbl8hLNYDtPoGe4q5v4ZKc5wSVMyCal9O1MfTO7Gpc5OWckVdjADCKl%2B68BjqkAenYPoUHZKjXmeR3tDcMhVZEgsH16BMcI1sSyqKBvrya%2FBCCEGW5oS2ASj4iBfU2LwHtuflcguDIsZx7RBJjiJxxTmWgKJUCZXYxYI61oI%2FvEv9OsfCMAOrrPTyqdGuj5B8%2B8V%2F4YzhL6baUkvjBPgSmcHTKK8o3quCXYy7wnaUPX%2BEFgSEj%2FJVM649Odrnu4Hdf4E8RP1FZaePu0pflKGdrdx0n&X-Amz-Signature=fcb09e64e2e2985f1db04082302d6e855f175ba170c41b5ce97e2d575cb0752e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2AMJSMO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtD5%2BDY9ny1EVSj8%2FQj4cRPBI%2FIz%2Bl%2F5BKFWTCsP6ThAiEA0hx11P32N70IU%2B474YuKwVoKmyW1Q9f7esUPq9%2BElgsqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCk1wohTxf0GLzVJVSrcA5duaGNYx4LZ90XWeMO1AC%2BcXWyzz0FadtzovFIFjXRj4eD1QM3fk4jmh2DaWKk3MVT%2FUoQ%2BgRpvz4GRCUFWlLtvqu8HUFNIaUHOzeejfZtkoSIYf8xdn59zH2xUF0BvkYP%2BXGcfjf4dD5EI0C9svv0CSAtpU5FSct1MZvvrCvTwm88WRHjW8oPr%2FPXXMkzGdcGbLH%2Bveh0YcoNOd3MjtM90IM%2FCXIK%2BGDvctw0Ow9jy23CAUh0E%2FJMAmLs8bwceLb8586E%2BApisjgG%2FE2nKVxhz3QwxkevH0VvmZSSDl4%2FNn1q%2BUPswpDgeuw0lMF4dA%2BiOe5D6unUj4mzbySbVc6Eg%2BQKJ6pX3%2B7huer30MRCDhA8XiOMfoHS0P%2FXfQGmRpTHOKEejbXsRh1jjoHCSUliDePwHs4n1MMY33xgLtAEzY12N15vAT6iWeLlK77KIgoudKY%2FfkjEQ1MLHmTNDhYxE7oWiTfUYltONG5mcN62qCdIruMEYubvBytpPS96NnoFHSFdH7V%2F2zXNZvIFPhr2E6Lj5WyLk92HfKCUdYJDZfIiHlhlT91RBhXuLzDdsYXpxlpehTtX4KDbIPRB3DbjsadHm%2BbWu1AVzEdNXo3%2FLTYYmsdfd%2FMI7tahYMLmY7rwGOqUB4SzD4AD4cEg8zksDCmie6mJRIxXOobrQIjRPdgfqEblcvWv7LDmlvMND4s%2FQ8R2IHJvcarQcO%2BKJxmEkOnqOwcsAFNkjyOSxYx22YPObc1fzx8XKbNZWFARtY75iJAKmbN8q6ADl3466aTntJr7c53duKeUmSPjxLo5qynuhY464w3NR0edn4iikfLUQFKVNFu8%2BpML84wDkH4sCAJW7R8fFBhPu&X-Amz-Signature=aad46cf1290bd0dd49c3ee2df9f74a01b8cdd4a32c15ce6314841f16d93af67f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466524KJOD4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICWfm5LZZ%2FOBPWzBUV7nxiUULEEcD2of4kFPUurZ3nUUAiEAoc7qv1Wmuq0ZWRnFvIy3JiK7R%2BcV3wPBetNFoeI6P2IqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA9W%2Fhl66Esgia5wgyrcA%2F7TpmY4oPcXaxDxlR3%2BkLOzBjf6CtR5MJnHML1mu076GIDpGNTvffxNde965wrFhlp7hmJlNvurSSx489mXgLD5yQFsGCJ4PFNnbojntEPk2TL36CSgLB4buQkvDVMo8dL49%2BeubaKRUYAlV04ZBZ16aTbde7LmFs05TL65AFXapKtkObPR9Tii0G0CgNpTarx2%2F6kCKhJgNr8jbJ0Pv3VpLhTojbZzr8n%2F6%2BEMz4iUwpnRNNjPpjB2VjsHzGbNNeDIqnxFEtlmjba3aiXpWBvpOOQaQDbmHAPVKkqK3MeHqpm1Sij5X2nZVcq2zY8CwcQG1sInFmxDznQclnHxlpKkTubtoadwnfWJ7AHgV%2B1mrD5h%2B2QonBHRHutckfL75TR8Tr1x6XYTvsLDiuDQA2vczLCnalUjQgZ%2FSTd2CzbUn5Pbxq%2BQN8O9zhn%2FrXfqFUEDn90eM02vknd%2BoTM0u92GFq0gU9y0uCyfGR7htah89EiZq1ZTw4wu5d4y1Gt7sm6hFWJhdXkaP9L%2Fp%2BbPnkJ8G%2BZHhTH9GSEfTgtTBX0RD5Mvj5BSaiDXKTq5WRt5XMKg3QaG745idyH08d3PWXi1H4KUw9yqEyCBXiWL50ij5oKCw%2Fe1vtyW5TfBMNOY7rwGOqUB1Q%2BjI6UgpFKTgp9Dj5xgaWaUDdX0aEDjSylosiUWA%2BRWHtEzR%2F6WBaqBEszbM0wME%2BbAarJ1anxOkWXh%2FpmSnN70dKl5hrhMUnUj7ho0P4HGutVGZHq8lymt%2Bw%2FI5%2BFWp7Tg3LMNiGoIfCy1Na0Ie92ZQHezZ4tpbFCwVr6MAm%2Fxs%2FtVwpybu95EFLLoAS%2BMB6%2BJA7XYKuSsYySBl3hslTiOVFOC&X-Amz-Signature=5f62b86bdd7ffb12df4712f4c0bbda7c5ffeb9dfa58f82df9030f27faec2e8f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZAWWZLL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfW3O%2FIGqWwI8H9N0otPvrg%2F0rKK2lcnDgvKpMDz8UQQIgPqpOQHNm8SjEmKqY%2Fc2BH%2BAvPBNi370IaUHDTCatFusqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8XN%2B42aR6nINRXCrcA9X2ZcwuljplpjWaQbyRxqILzYYcjMevVGFSeAnH5RozD5NnxJE8%2FJbZz%2BvkzAhxei5VPhzUIXPGve73X5ETZ8WXky6oT3G1kQ2Xx638jRGQxExI92quSLU5LeQGbcWKa37SdIgbyl6V9nOywTFJB%2FBLvzkBkmjndoZqOWNZpjfj4SV7zqUpI8QwUFDvRZsAq6327wQRXR3oW6G7PVGuxrg9%2B2%2BG%2F5BqpMESYiVqylHH9MRkIBBvnQ5940yynISuiBaQqaoWpkqkstKHV3Ztqk8BnaqB%2F7smXElGMcnm0M7a%2BNipLB01F%2BjqzAOQbE306ZX1Qmd3STLVbstDa2N%2B%2B8t38HmLbSYDJyiuc7hK4FcdK8MjS%2FsCFZVnGvVXfgt5G2qYO2WCgmqMRsHTjJ0nk3ji3AULHFZbeB3vSnTMoMm7c0%2Bzgg4yHfoc5irlBYFpbhSTLun8x04idk%2F1m%2FgKI2XgYKY%2BZDGOhUTecWr2k2Dg8WgsPy1TrY29sg6JbRUP7LA50YWsOd8BH%2B0nMlM%2FLeDbASKi2f92I%2BqiIscs4XuvztMIEskkiAhXG1qYhF%2F5CzI8C%2Fiyn53yMgJDJLbog7xq4mILVjJpNZQx%2Fx5z%2Bcr4IPDs%2Br6PaoS1DEvbMJOX7rwGOqUBuVFABwEQ7bUjsX7f96P8ekpcIXzVAAcHM%2BaFqe%2BAkX4HACLpa6bj2VR5A%2B12t9HjcCCsL1HYUO8cogu7MOLAZb%2BSCvS%2FeMwUQFTVZYl4Clzxb1syMLfoWepp8iQrlzej1u2pjC9Jcv6I3XE9IBIGC3vyDJgPGktlsYF2YpclJC7sqBd1HZyftbVSlt6k3KMGrgddQ8UXV%2BMX9j9Q1T3zMeQXyl4H&X-Amz-Signature=3cd002c3147a4c97cc114fc32c17f525d3ba18e9dfafdea2b959aeb73ffcdb26&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZAWWZLL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfW3O%2FIGqWwI8H9N0otPvrg%2F0rKK2lcnDgvKpMDz8UQQIgPqpOQHNm8SjEmKqY%2Fc2BH%2BAvPBNi370IaUHDTCatFusqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8XN%2B42aR6nINRXCrcA9X2ZcwuljplpjWaQbyRxqILzYYcjMevVGFSeAnH5RozD5NnxJE8%2FJbZz%2BvkzAhxei5VPhzUIXPGve73X5ETZ8WXky6oT3G1kQ2Xx638jRGQxExI92quSLU5LeQGbcWKa37SdIgbyl6V9nOywTFJB%2FBLvzkBkmjndoZqOWNZpjfj4SV7zqUpI8QwUFDvRZsAq6327wQRXR3oW6G7PVGuxrg9%2B2%2BG%2F5BqpMESYiVqylHH9MRkIBBvnQ5940yynISuiBaQqaoWpkqkstKHV3Ztqk8BnaqB%2F7smXElGMcnm0M7a%2BNipLB01F%2BjqzAOQbE306ZX1Qmd3STLVbstDa2N%2B%2B8t38HmLbSYDJyiuc7hK4FcdK8MjS%2FsCFZVnGvVXfgt5G2qYO2WCgmqMRsHTjJ0nk3ji3AULHFZbeB3vSnTMoMm7c0%2Bzgg4yHfoc5irlBYFpbhSTLun8x04idk%2F1m%2FgKI2XgYKY%2BZDGOhUTecWr2k2Dg8WgsPy1TrY29sg6JbRUP7LA50YWsOd8BH%2B0nMlM%2FLeDbASKi2f92I%2BqiIscs4XuvztMIEskkiAhXG1qYhF%2F5CzI8C%2Fiyn53yMgJDJLbog7xq4mILVjJpNZQx%2Fx5z%2Bcr4IPDs%2Br6PaoS1DEvbMJOX7rwGOqUBuVFABwEQ7bUjsX7f96P8ekpcIXzVAAcHM%2BaFqe%2BAkX4HACLpa6bj2VR5A%2B12t9HjcCCsL1HYUO8cogu7MOLAZb%2BSCvS%2FeMwUQFTVZYl4Clzxb1syMLfoWepp8iQrlzej1u2pjC9Jcv6I3XE9IBIGC3vyDJgPGktlsYF2YpclJC7sqBd1HZyftbVSlt6k3KMGrgddQ8UXV%2BMX9j9Q1T3zMeQXyl4H&X-Amz-Signature=e480f2005903855e5e716f1ddddc41ee285870d40348fa7001bbf3cdaad2d9b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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