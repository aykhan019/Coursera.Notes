

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGJ3UX7K%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFgvOTJNssAEtRzegd28nRSL9rclSWzQZ9PskOWxuw1AIhAKyCtZWKWxQRpJ41WOMb8ZRDznAIlIq%2BypDrHi%2FQcy%2FcKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQH8alc%2B47ntXwze0q3AM%2BZ63hsj%2FUT5tiiFB19H6xaxUdB2qn5A6iFgRphnIwojCBa5m6tquk8YSJ8gIvP8C%2FzaK%2F3vS3SK9sYrmgao65K6l7pJ5iNN6yik5l7EV1EFA1bIscdfLnVSgp4s6FAoYyzQY5uqc5AoTkW0pt3rVrIaxFwGEcfEyDpcThCiDm5rNZ3ZDgQeUP0Pnf0dnMh64BWGzbf5fDYGXe8ujIFDupZPI1mccex2b%2F1kUEwTwA26lI1m7oWJpZqZb%2BP6%2FywKvTddTJbMib6n6Hnnrk4x40uyeDso4f4fy36Fc4StSZmFyQm46YrainwhXMVQSsVBY%2FyNsjd2CGKnkssEmxh4oN%2FIgZqbnNBY6%2FjRIfE2IyI9%2BEfCDTO60Wy8SND8f4fOiUuW830Hg4%2BEUtGeZHPnAh8gziU%2FQGNajuLBoUb3zmoPQ5%2FaaIe0CJKjqZV0qVSPM9ft2tOFCTDrZHBP4qcwHEWLX%2F4qCPuR%2Bm%2FaupI6VLXBrxaydSP%2FuaCJt0AaCVb5WF5uernuw%2FXOBDqYObQ2WtjcJgz1ueXEYsujhADMI9HQvnvSDboe%2By1X9ymxdXgS5xCUBKZQlQi5fU2JPj%2BazoY65Qj%2F2xg5guRTLx1GpYcaEcHOeGQZvIs2dZYzCdwIC9BjqkAUgYL2%2BukJNY%2BJwTvXID%2F7CvRzhL6VX%2FKgSEGbKNNagBBrB0bImquMcBldNM0zu955orErRmkWbfOEHPSvsK8c4iXc8TFW9FBESBAftmpoHj4TTkWrAKVcdUpZ%2FvuSSvjT25Mch%2F3S81ymOt54AaUqxX%2BaMn4mbkZ9%2FHRem6wkeaRUu9yEAu0b2txFLicPZM5tUboGkpxullY8XRAofW%2Bp52pXTo&X-Amz-Signature=708421cca3bfdc6191206540147c40ad449d604a7ab51651ce6fc28ade1727e0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUVYX3C7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH8Fu3Nh5XP8KqUhn0thAKb%2BFBGobcIeXOP1sDRZ44bNAiATEV4%2BKg%2BD3eZnm7trUn6zT%2FmDuKdeweycvSDlo5M%2FHCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyZLMDyew7djSpczEKtwDcTv69pI1QE%2Bf3MmpF1rsHJfLL3GFQikUqCpnt%2FeVR2AlBZr0aKum%2Bke6ComJIa%2FP%2BKcfTZcUPr1XA0%2BOk0b49d%2Fwf4tOTlmNZ2EfHq3LqJxMEm4nF0jSr6ObGicwY%2Bc5GHYa%2F7mFvkLqq31Pmq7lNJO7ziiNOTF7%2FtjtVVgphYgvwApDIGxcMLu%2FW9mJloh8CArjOitsgvHDczr6qui%2F6IK8eACjSt8i6R04S91c44IJVA9wklt7gwkXIbjeAsDKIdfEuuJTWLI5ajmTtNo9QxQ1Z%2FudkTXCEoG5BkSrlNRyVFx%2BhToFvQ3SAO4QNSWR2SRXwCDCGnerq2WOESUqBG%2B70MDJp6pVWjmQigfHBe49Zdvn32dUq92y9zkN2c%2BFeevOO0SR1RRcUlwQIuVa%2BeE982nxmxhQy6JgyHL49RwkgIbETJOX68w41VyzPi%2FWdtJ%2FzqNrtphYLOq3T%2BRt0Ljpk8fD%2Bg2k5Nst8JsrpcGcvUSKmcT2U1PKAnZs5UDUPKLbNBTzLUaW0XMTLpY2Gr0FTh%2F46oG0WCMYMrAaDiAgTXADIe32635ZwibvN5%2FQFLoQFleW7sXuP1JVjtpkbJwOUMOzPKK7FRuzDVSx5PFVbt%2FyJJ9qBQhGVPww8b%2BAvQY6pgHOFx9KStR18yFZRjkb2oNcNBuR2oQDRV5dEOedR8kyEXFmmeehXXjDhMLRSVtXeDwQRw4QPxD61WB2wNe%2BOA45z5%2BamMJx2tB%2FMu%2BcaGvdwiarh23mfOZHNF1Fn%2FRdShWIXtsVc9SYhOBbHjNZ%2FeSEXyYG4qLTdKov8IoQ2Z04WIK%2Bd46Nt33Qc9%2FCEmmuk6aKBewdkCgNvds1fvBPOrgRultNgsdu&X-Amz-Signature=aaff9063f903cef2670a5d64bae3716edd5a48a5bf5b8f166b0a9fc7f8853fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FVSZD63%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYe0c1miPBa4ShK8zI48Mp7%2BJ1rC%2BS0x9BZ6iJEEOsWAIhAKaaXNWdLqTFtkBMDqT0QQWE5jF7ul8%2FHVaNxz08ZAAZKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgpcpuZbrRJBUp5HQq3AMgeIUl%2Bx6BH2g0jX4FkdPYk9%2BNrPE39kLWhDd7TbUdHmYbv80haIBzwKMcl%2Bu%2BgnBh4y%2BFqomvjA4aH7GRjv7oe40bvAm1NPzcWhVO2hWnB9KsAPYac91JfF%2F%2F9zSf8FKnLNM%2Bws2U3swoVHX8MSO%2Fg39YERV8to2BgAXQN5uKCGIT2ncKs%2B1nGUD0bnaw09TmfW%2BEAwUVjLlBrJd544BQlPKVVxZfvdQP9r1VCMk%2FRmFY6iJXyc0YnrM0a8kkOiVkSmQxKVH67IbUXoWfrA%2BkwL03%2B5k6e%2BXzmZ%2FxBIZTMzddpXNxxdQWLTrUPR4Qyz2n6TwrhLCnDecjJ9hh0WQVBcAwngVC6mihIlE90KAGPaMg9pEnZe%2Fbrm7S5K6o9V9us0e%2B6dmdusL%2FyRHUtAZfAFVdtKlrCzvWvub25JbhXqZ9QvJRg4qfqt77NH7vdgYZipxTl15%2BUPV6MkpDKPMMtPZ%2FK2PjtvrlxfFwyalzjAiuLxqh9GwxUSQqtF9vq21tR1ZdO9o9JPZOrjfkioUsUkzluyOmKGTeSrDplPOoTIzjH3h2tFLoNByIAkRDj8UiGbKr03Clm0Du%2FL4Mk20ngSMCXS4vguYYWoatQYSehQNz2ECbwrztdbXn9TDvv4C9BjqkAbGHVd87QvUItV6nB22CX1U1V%2FXJSR%2FZBH6%2F17%2F6sFYxEj%2F9UKIFkL6g4aMMjx9aWW12EFD69Z%2B%2FI9G47MMY7csYYBitGfKH1teDmb7yjPbzZPR%2BWZn%2FAFBgB3XaRwJyOX8U7LN6wLEpHA6egD9hMv6a9xi1Xqig6QHpjcgjZ6hYoABHiEnkCh6SVum6UWqtYSfemKyVNqmGWK795DVcHz3Fj9LX&X-Amz-Signature=52a20bfeccdfd3d379e0c3c2a4ddfb3308009f613d443ffbc87f2a6e7297a725&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3T332AK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBA%2B75RlAXAKDrcm3MoLymF5ZxpTrsWpnE73g7GIuUs8AiBPzrYj6SVyfQXvLQdYWs0tI3BPZvNK%2FLZR0peLuDJxtCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXnL3Z%2FHKIXpjienTKtwD%2BIVS%2B4fo%2FJQXKFxiU2Cm5BAX7Xc6BZzs5mY5LIAQSIEnVaHZR8vfWSSiCNu3GtF%2FtM6ISTus3OCq5EQMD3nBNzFyX7qpmeCUS%2F%2FRltrwLUOGPwqqE8pIqIIzk4VitaxBaZ3PK2q0%2FE%2FmIfldMAyEaFBPpOuLvSVSsdSEydkx5n0JfckFvS%2BnQMmAOP2jp9rZEU7S8P38YlNTqsKHjCzoYLGOme2y6UmVTteBnpvhR%2F8ngmMx7f0g7gPeL80DH%2FEJw6nsL%2FQxi%2BjKKGQNVqzwdVBGDGY%2BkgjSJuLvvQl6bEvO1VrznIvhDCBUEQPi2aX8p1ZUKJrkvlL9%2FKJUKcK1H0HSgHkp4UNcGHZG7OXJ5aHKglDFMfR20Jy9ueEwPx%2BdTvG6BHRlS1XVNbKZ4Qar%2F8pWmg5fLu%2FcQd%2B8X8bPtuKjYnNB1sSzqZPLHfbscs3LudskavXAqUQHjrvO7GkkJ6FoHITx%2FTnJ9ynsNmd69Q46iZ2UCBdtFRzKIVg6TtxwN3tdbIqLBO9CbiSWM%2BhkMzIi%2FRwImzXN5AriWRVOwQZCXVUvEgj5%2BGhDY38%2FeXUQ75WrG6O6Z7Uh3%2B5GHtesvbrQEcuxZtQhnWzbScc0wg90PNZQ7AwZd5KtGtUwv7%2BAvQY6pgHbDeQIcMdVZXJsXFCq7GfUQsWWcBmg4zssEyCgfkF8UT7MSMO9PSCUS2UNN%2FvnKnsu8O%2BgjheF6vQbDNzuzKywT3Nsw9rwc4w4knrQGaolQptQ1qfQ4GIfupn9%2FF%2Fbp6F3e3dDy8BxgMUNWJVKgFRa%2B1RmZ7tt%2BdWh5lWMfKNvxIv7QOSTkVV%2FJZBWLaBYvGKPgQn6RyD4b4IrPsTVudtvVpzKihdQ&X-Amz-Signature=abd93c60d726fbe8f556cbee68268512502a9084d1fa30d4a5c9ed13042745c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWPZUGDC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2%2BoWjojytCEp%2BHmfo4PzQUPHWOMwvJzP5KweEhCYreQIgJ%2BD4GI1wPPlRZzj9ady3241EQlRzW7cCcGA2tYTpXoIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFI0oTNY2rTNTyboWircAzdBjFTaTTk8AExFAZdeg2NIDAMQSmFKTiClySB5Ny5RnrA8DnrSI6UFsrQUQNXA9f2APpBDsV2Ho21vEyhDnDV6PTBHZsWN4kRIs7xbwVlFGJyWh3HRQ%2Fi%2Bdy9eanoRhNJuGOXWHTG08CoXts80Am2Qzdxlc54qIpKDyLhoMGxcLagRHtJ9v781Wum%2FN%2FsIiXvd%2B3gv2eumYJjLMXfV%2BvkVKB8ui3GgVxum3PCwOrhwBh5SQFFmXuMDyeQijhG8V9OZin7b5sZ5bpjy6OOAd7yiAqNtkWHrlWat0WGMOcU87pmCSRgZ2T7m%2FHPP%2FYwMJh5CQ2WgvxJWJ0r6M4D9kj2FJKzzs5gb7pZ39VfoUdISEqqVmXvfYHedEZaChasdhJ8q1ZtesYaD0EcPs2Fq%2F%2FBwrSL15COj4F1%2B4fRGpjm8%2FQL2GlXlM7x3lheGx5%2ByuJqLth89uEz1s6u8hUYt5g2JLY85mKejvP4Je4lJAOJN4HacF0YzdXnevBO2rKuZe7eZen0q9ciQco96a9q9PUMp8wwJeepRnIl4CFmGHmTA3FPgmIH9DYZ976DpyDHRuFyNNFwREVHknhYJ0f07iL5c7U%2F0m%2FO%2F%2BH4eCjWcd%2BzIxRX45ej8fNCd5R8sMIq%2FgL0GOqUByfWBYkq6xn2jXeY%2BYBMfbnAzDvmJP5bWbglT9jGz1HzC9R0%2BTtiuqsM4m23yCjtZnNCiH00bk3BWCEBFe1pI6HimV8%2FGOG%2BmelC0BXCxxxyGBRrmnM5nS6cu8AirJd%2BoND9ZwxcJekhAJn%2BBH3ymiKJnkLKXthmzgwCHsbXAkCCZdTURVhTl39JXZgdWU2xniBFzk2H1Md3BV9h8DRWFxeXutI%2Bs&X-Amz-Signature=b53f871d84425ebc7ace535079a088887eab7bb2ce251b8af506606c700af0a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GRBQLQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIHlHy0546pSgA39s%2BprpCXZwXBci%2Bf52VBwn8yYawrc2Ah9h%2BkUq5gBFJlsoQ7PuDYGzD8%2Fjo4vUyV1tJSy3TygHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVoKiJwkxVXowd44q3AOSq3LAn03NVJkSzMmipn%2BM%2BCWwVBbVt%2FuazZR3ZtoFLIS27QRy0SnTfa9TDVoIQOIgRIqWCCjcMB8k0YqLOzflW08EToi0uSoth10fLSkvTewS2EUH5OKs1%2FMEZEmsngM3z%2F1pPwCMZzkIoxLK5M%2Fqw0iXY7WVcIjiIXkAPgjA7xhnN9tihGh6nktAh4eR%2BPt3D2SIctZo2tW4T%2F0Onlb%2FltxOFYOVDRUuoqYimV%2F84I9F58WTMxqwjoKRrkl3o%2B5w6xvHQ%2FBAnUCCsqlwsxu9jSQ6OoYhlvRelEpZaEEf1jl2f6cObSUoUa%2B2XmoDS77LKu8RADlWdcvxF7V92%2F64p%2FMmK6ncRE3XlOIeRSn94%2Bd%2FSNOiHLHg8EGQl0WX86dbF9V1koVQsmGkS%2BGzSbCoDmfeejkuTCIdOFz72l59Zzxo7YFrPzLkOCCAanGZy5ZZ2FD07ArqgfQ3rA92vZU4xAhJbJ1avGFlR04Q9H8hoFLrgKPriSzhoRrEVAtIP1%2FwUSeSJhhFmJGZdKrFNAAdTVZlRcnUjn7qEs0FMJllB1snLfj0%2BIaOP6kmHZnHBG9lyjl3V7WlmSt8Loe%2B5rW%2F9IyQqs38slDXGMLDrLlEnkffWvZax5nMmZoSmTCNv4C9BjqnAXinwz3d7IQ2NlOCwBRqUmqb%2BoNEp8X7FOAL8maJG%2FIE6bzwf6EmXtMwY8N2hGYUNXcuGcVowEC%2BwUkiam4Mly0VIZYC8qA6Gghr8YvYX39AaGQD1%2BfAKyKHwm%2F2jUWdGJNVUr2b4Ry1dRairlf1IzJONcFm2nWIxIp3v2mbaZZ7s65H8%2B%2FVfKRgMkydzZW%2BEy6KerQJQStnuPItpAT%2FO5%2BHWW7PatmJ&X-Amz-Signature=83dd33957553888326beea973b7b71465664258d4947410acf77176874c98bf6&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRC6QUOU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDr%2FopISZ9H5J9CExnDHSrJrBIgao4xTY7%2FsXCtdI83wIgNcqIqThu2BdQQzDalo70H8I%2B4m9JqzdIzMAjnLHyLlUqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB0x8xkLBL%2Bv%2B3ytaCrcA6Vtv%2F1LhnSwriZVDCORACpjjU8wrQ4IvVmxnEiAUXkl8QS3sfWNopTxK1s2LzNlVeMHukbqr5Blv0jShA3QVxRrVVoP81Db5HL6eI58NCmwM3ugB8f41oau2Nwz%2F2qf0nGrVjBNZ%2FU7C22FScWscmARwrEKY4bjJi0blj0joeY0wCDgZmVZQYpITCezEkEf2NkjVJt7Eta9ZPqoEvszTuX7mrcZ9%2FOECvfje%2F0fDDOjDX8TKSswz6pYkcu4s%2F%2Bny32zu%2FJ4goYZUOasYImGaZubeHC%2FiSsWSAArdJyI91iRA4wM1d%2F41WKuSyy6DWfgPZN60%2F9v5ypIaFlfT50lcWRVFNj9u0OYEvLxs1zYSV61QgaPWedHGREG2P9BBHVw5cH%2FvuwWkZIdVHP%2Fq4D2lpUg9ZoQ6OLFEUiQyHlOf0iIJvjuS95WoTLfnlXHN4kHKXQG%2FkGrJrZniNUMBRPyJWBEC4bzgLoHkpR7p%2BEYxjmOrHghkNynAgmRedqrVM4vU%2B8PbgaivNjbji6QLtwewTNZLbvhfrdHk9tmkMlHwh5%2FSLrklqVwbroHPPInt1ZNw3tMLa6W7y3OlMCZAmIhTnobrW8wT5SU29wCa8SOkXjyDnbQq5Rmrz6ekYMYMJrAgL0GOqUB8DpNJc8ECQ2gSDYMdv9t29IrjIh0BcGZ2glo7hwXrXDhCOQKgZmf8X2TdEktygU%2BJjea5vUK7yXjTzgagdpuYMhEXLW8rKdixnyeumsQ6FSNpvtgxbNyzsKnbGi2TyjwyZp%2F%2BDi4vA4TtznKkmBOgm%2FDT3g6CICH%2FeDyWtgVk31QEzvQ6gaTjHB%2B6cKk40zYyLZsxcLC6MiQ8EkRy9PcOhIeGpiH&X-Amz-Signature=6f3c6b42752ed7e81d62352d56bf98bce9df02a579b123fcc686c61fad8c87eb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QW7W566%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCplj2GoXztCILDnGymzheRHgBgPTeh%2BoWshBtTTeh7AAIgC0Et%2BT32U2B8Iw%2FcqwZMS3oSxPQBs06003lR0nE87CEqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwv2KE73djsKWgl3CrcA%2BJOvSkTb%2BCIRwD%2Bg8zbfPEZeAyeL9GengFyShF7kZovb26KhVFTHzTVRbHp9498MsdgXNJjSmvmjQl16ta794JkiqGNcw8fJ5xACzANflzXpodZszj%2Bmr4GdAB2PWWgECKYQGCplt5wXgI5YNE2sTA926nxNdjlSjMia%2BhGHgwDwvejdSvGz8ohNTPG5wYN6hEkmG1xD1i%2FO8erCM2rs95Cxpt39A37ShIwngSr2TaQoiYHBVGWW9kh0bpqKMzvWS%2BVZOeqrGrjdCyDUOiO2AXC4E0W02pS3hrNt3s33a8Za2Urv2tmeZlrLdolyTu4cvmRF35Ehgb%2Fl2VE1i2NMFRMk77JlWvb9921lfVMzYUCalFvG9Ts%2FTD%2FdxsIRKbYJBqbkpJn8XhtJEeK%2BzfHp1q4u8uPbDVjcb6xmKWs9WJfEloiXPqG%2F5ROu0Dff9Gbo3QehywrTe%2BYk69RLjXFdWKXNEdsV7IBHTqBmoBF4WqaX9hD%2Ftyd4VatrqCiIMR8K2xa0gCLIq62p3%2FFe7%2BMLS3vqVBJiP5W67KHjHvR%2BjSBVO7eDNROEA5urwH0rw7452J4PVO9SJXlwBke3HOlnIu1P4TgWeyo%2B%2FOupd60fLkVrc8aYsRSxnHDn9ryMMC%2FgL0GOqUBdrmN0bsSEYThz1QrEuyWumxKG6t4nvI6r95TN2cBdv57zCx0%2BMcQewjZC8yQ0kjGR1htfZ8TZKWs63P5xewvbpVeJXaztWd6WWCGjppq79P%2B82fHVlh56l10P%2F20gl4jPEYLpEWzvhsnqzAIlZ9kyQqNAinZWDoBaV%2FLBWWjWcfEkCtLgQY1bVHcPn0%2FDCNYUUc2g9PNuR84BgZT63HPXnuV8T2B&X-Amz-Signature=6cd71a94d9d14ed04fb6b7bf8bb72fc78f138f68a562ea837f0fcbefc7aa60d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWPZUGDC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2%2BoWjojytCEp%2BHmfo4PzQUPHWOMwvJzP5KweEhCYreQIgJ%2BD4GI1wPPlRZzj9ady3241EQlRzW7cCcGA2tYTpXoIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFI0oTNY2rTNTyboWircAzdBjFTaTTk8AExFAZdeg2NIDAMQSmFKTiClySB5Ny5RnrA8DnrSI6UFsrQUQNXA9f2APpBDsV2Ho21vEyhDnDV6PTBHZsWN4kRIs7xbwVlFGJyWh3HRQ%2Fi%2Bdy9eanoRhNJuGOXWHTG08CoXts80Am2Qzdxlc54qIpKDyLhoMGxcLagRHtJ9v781Wum%2FN%2FsIiXvd%2B3gv2eumYJjLMXfV%2BvkVKB8ui3GgVxum3PCwOrhwBh5SQFFmXuMDyeQijhG8V9OZin7b5sZ5bpjy6OOAd7yiAqNtkWHrlWat0WGMOcU87pmCSRgZ2T7m%2FHPP%2FYwMJh5CQ2WgvxJWJ0r6M4D9kj2FJKzzs5gb7pZ39VfoUdISEqqVmXvfYHedEZaChasdhJ8q1ZtesYaD0EcPs2Fq%2F%2FBwrSL15COj4F1%2B4fRGpjm8%2FQL2GlXlM7x3lheGx5%2ByuJqLth89uEz1s6u8hUYt5g2JLY85mKejvP4Je4lJAOJN4HacF0YzdXnevBO2rKuZe7eZen0q9ciQco96a9q9PUMp8wwJeepRnIl4CFmGHmTA3FPgmIH9DYZ976DpyDHRuFyNNFwREVHknhYJ0f07iL5c7U%2F0m%2FO%2F%2BH4eCjWcd%2BzIxRX45ej8fNCd5R8sMIq%2FgL0GOqUByfWBYkq6xn2jXeY%2BYBMfbnAzDvmJP5bWbglT9jGz1HzC9R0%2BTtiuqsM4m23yCjtZnNCiH00bk3BWCEBFe1pI6HimV8%2FGOG%2BmelC0BXCxxxyGBRrmnM5nS6cu8AirJd%2BoND9ZwxcJekhAJn%2BBH3ymiKJnkLKXthmzgwCHsbXAkCCZdTURVhTl39JXZgdWU2xniBFzk2H1Md3BV9h8DRWFxeXutI%2Bs&X-Amz-Signature=59c755f4e6b943c3cf84b678836ba34ab56e3cd1e295cab9ed91af22fa4002fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN2PG2NK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPszOmv9dpNMOh0MWpCZo9OkHDbUpY%2BnHhVeTN5oBkPgIhAPNG9YysKHZqoS1XegrMWmzS1AnrZmLpnDj4HOjqiZg8KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrRw9RyyISBFx27fEq3AMv2x0eBroVPWLtVoiutS40Ivna86Y1Jhhk3YtfXSwAY%2Bfgrknxg6TbU3aAUm4xk9q78OtQUycknP2Fe2RumbaTH2%2Bp%2FT%2FS2Yx1VaYIsY88uDMs4CDDnEEnb6V6Dlx%2B08O9QMqZIiwNfaJhiyxuxV%2BCJb54RHYRwx2tsR4r%2BQJwTVEyKOuzl4EAZrq80G759LKeFcT5jhVPYDIh6wGMtlYsoagjEhbO3woEubNNrbo3DiaEQSIqkH%2FZvjFv7HTZYczLHsjxs2Lnusos4ffoBOd6NNnWGuiuJD0o94WQRwLCnFwU3%2B6HwaTXTD%2F48qVRsr%2FkisZMmt1CfWL9PKp4JCEtVxXREDVD%2FAvZjUwyGxJ8ncJFiIfXrDmF0Lp3J3%2BQAkGGA15wDzXlvJyDmyFSPUakNDJ646Vcd9NRJcHV%2FFHTEGmQGkgU9Te6cIaNlnkU7rpVgEDycXnO62ei5LNsdllu9uznYxX6G1rFrDOoLsE7p0pj1pev2yUFGRWhYDSqNFbFhj%2BYYUNF3DBl%2FYZizC4dIBRpIR9rJYYB3VvV4C3ZZPY6jwCjHTU%2FWxT7Pp6rW5iN%2FW4dydwuTComKCk2l0rUuZgsp99zEBs9ILwpQiRR7Z1rbK3zyo7K%2Fn2JLDD7v4C9BjqkAdIyp6lKYFainU1UYsMxFLwN8kvfmUdrPEr3t5VtxjhyeaikaFgYqZ2PLNqTbisFSGcxEg2V%2BwkvQpQL83QwsZQOP%2B3Q0MTm83b77PHCPyshFG4hozxhxPVrwHiboXTNDDLKRZh%2FhGNIL8cdWrbRTnlCBmbb9aqBCNXekUrYAo7Y9trmt1gr2uhmmXegJAaLF5Be%2FmvgY2%2F0XGCn4WEawgofwcp%2B&X-Amz-Signature=d7986bf522601bbf5305084b4abc8010b74927f6bb7137a941964effc2eddd0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN2PG2NK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPszOmv9dpNMOh0MWpCZo9OkHDbUpY%2BnHhVeTN5oBkPgIhAPNG9YysKHZqoS1XegrMWmzS1AnrZmLpnDj4HOjqiZg8KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrRw9RyyISBFx27fEq3AMv2x0eBroVPWLtVoiutS40Ivna86Y1Jhhk3YtfXSwAY%2Bfgrknxg6TbU3aAUm4xk9q78OtQUycknP2Fe2RumbaTH2%2Bp%2FT%2FS2Yx1VaYIsY88uDMs4CDDnEEnb6V6Dlx%2B08O9QMqZIiwNfaJhiyxuxV%2BCJb54RHYRwx2tsR4r%2BQJwTVEyKOuzl4EAZrq80G759LKeFcT5jhVPYDIh6wGMtlYsoagjEhbO3woEubNNrbo3DiaEQSIqkH%2FZvjFv7HTZYczLHsjxs2Lnusos4ffoBOd6NNnWGuiuJD0o94WQRwLCnFwU3%2B6HwaTXTD%2F48qVRsr%2FkisZMmt1CfWL9PKp4JCEtVxXREDVD%2FAvZjUwyGxJ8ncJFiIfXrDmF0Lp3J3%2BQAkGGA15wDzXlvJyDmyFSPUakNDJ646Vcd9NRJcHV%2FFHTEGmQGkgU9Te6cIaNlnkU7rpVgEDycXnO62ei5LNsdllu9uznYxX6G1rFrDOoLsE7p0pj1pev2yUFGRWhYDSqNFbFhj%2BYYUNF3DBl%2FYZizC4dIBRpIR9rJYYB3VvV4C3ZZPY6jwCjHTU%2FWxT7Pp6rW5iN%2FW4dydwuTComKCk2l0rUuZgsp99zEBs9ILwpQiRR7Z1rbK3zyo7K%2Fn2JLDD7v4C9BjqkAdIyp6lKYFainU1UYsMxFLwN8kvfmUdrPEr3t5VtxjhyeaikaFgYqZ2PLNqTbisFSGcxEg2V%2BwkvQpQL83QwsZQOP%2B3Q0MTm83b77PHCPyshFG4hozxhxPVrwHiboXTNDDLKRZh%2FhGNIL8cdWrbRTnlCBmbb9aqBCNXekUrYAo7Y9trmt1gr2uhmmXegJAaLF5Be%2FmvgY2%2F0XGCn4WEawgofwcp%2B&X-Amz-Signature=8a1fd399c2ed22d38d3c669283c40f8deaba53c4b8b2111baf335f31f18d1673&X-Amz-SignedHeaders=host&x-id=GetObject)
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