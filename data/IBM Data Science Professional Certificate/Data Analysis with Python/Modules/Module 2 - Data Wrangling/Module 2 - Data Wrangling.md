

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ETO3XPJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGY6C0%2BCaBQ%2F0KsYT5rtJ7WYzODwXNa0hftL6OdSqgZgIhANb0ubNDVkhkF%2FuIr7G8s%2F6RJfJlHxGzfho995JlENYQKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxycxxfBC77%2FiT5Q4q3APKowv%2FgVu%2Fqpm6EBCm19d%2Bqj%2BI0nJYZ7oTglsmJgYmNy95XdqjI9yoXYGpIEJ54oUDMGUc5Aj5CMmWJ3YZ%2BJwKyLTsjevVj0M%2FUDCTN8SsjpdPxCZPuwRcN%2BzApEZvbWD8z5tTMUpWw33ELkR0I4mfFUqQ7QlCJPTIDSxpvkEtIxolb0ZtL6UbpjP%2BbDq5pskyUd5V4%2FtmVFbYokq%2BQWxSeZQ1IeZ2Hojh8jUQL4ZODa3EZo6N6Cntp1PQxrJVWZVbvF4CaV63RMa4tTqcq4uCeFgt5hrgouLTB2ehlrqZbf1ZLHreoax4T81c12EWeZ3lRu2qoWIIhAaM6vOQISqQX9GF3OMzd8Iy8DsIhy73GTY%2FjJXgJCDQf98XXGS2OKrsYsvdj%2B75df%2FTZLVtDTcVwEtHZAit%2FTYri6y4voEPldb%2Bhghn3PlV7g1yt6zWP%2Fzy3UToouFcoiVJxTgBxeFFZwtYjO1FfPYg3y%2BRdJLw4mCxzDB3UzpKUhtdxwIjrysMpQjIh2Wn03jeICjmslpQYr%2FAeQIqph9L8n6kTaT2I%2FiVVyNNTA%2BQf2CSZJYlbCvf85MtwZW%2FljSkGYlgSG2Gs3hEEjwRZttf5WbhT9tqsKLeMaXnh%2BwHe6mVkTDmk%2FW8BjqkATjyLseWeoI3JeSWYDUUdfSqUwzH%2Fi5ICC%2BCLeACyx3PqAz87iuGnYfAw9v7mxN1RjU2y1TEIGru7vEIYjnTo43mil7UpH4xAqi%2FyV7Qaa9atesSCoU%2FhXv0Oebc0p4SpoQ2HYC6l0ZVXsyMsAeHGceke2OKlQR5y71vfcunlvmb8F0KfULlxiFYgZ%2Bbd%2Bshku2KRRy2ad%2Bu7CSoy6Pa1eODQXdJ&X-Amz-Signature=1f505ccb055ae1c883d492f582e5f0af154cf5561ba6cc9aff2bfa29ad8b78d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOCKMLFF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH6nST6lg8ed%2BdVr1ZyYDQS4fC%2FB0eIHBm%2F5kDnwmBwqAiEA5V9UvYwSGjHicy4anHKzkGWAwjB4DIZLB3zWk9K%2F9ZUqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDSGbmPa%2FfgPH0esTircA1eVzrNHT7MsvLUIQb83ZRjaubUDn%2FOpB6ztot82oj2simmG%2FrjX0G%2BTD7gf%2BXs6oUb8WHutyFxyVpU01lMFa2quxbv45Nmf0lcSq84G1g7k8XqpEKUa9LkjrmnBlvz1EWjwTG9yRqNau27fcvI0GfdYbuOxTCNCK6WMPy6P%2FWI9CNHrliQFRk1DQCKTVWA34gnONrIXdRfP54HVsqKtMlnSikuYIHkw6UJR57TcnmLEltLVx4Z%2B7OX6TIQZfWFtltFcm5x8fQeDQydmPTkKHVBRzjkfn%2BZcHbx%2BOF6JjfOYXKtD4tLvQrrkzxlAT5gFIXG4Cf1BVzk2EQSXq943SbHzJOzSU6VB%2BEq%2FUmw5AbxLwrtrRCoe3BQZxKqaPqafvywztdNN0ofMJS1UPZTb7289RCVQa2AYmh2vfszDBUyQ%2BE3jp3%2Fsb3pInTr6qLNjpEQQ4m4WziB4TOeoevoUE6sAQcsQ%2B1U%2FxchtefOysapaaMRTizoEskhT7ERKKnBuDvud8ut%2FAtRRLumw5qncHJkEW6GeIzKn%2B%2FkJKAOqJjLEOoKUCnlIK0Vg9ey6xWBHuCPiHxi%2FpWtNKsfQ%2FsIYNF6PnCJZbZ7%2FokzsKhM4veCJNVNHvS2sirCfBic8MNiU9bwGOqUB%2BNONhXxJgzCytgHNyds0MESt62tolDGLicWNlm0GJwHyO7kJwqkqOEr6DUa4Mra5ZcaOk8KplDW0u5DjNfiadSb1pWG91aD3Y6zbKLfl%2FuqsoKl7Mjj5CTmb2fDuHC54W9COLemkLpTQPruPxZBY58Jih%2FI789YQIiE%2BrRVBqpN0uMWfrBkvI4OP25Y7jBMojcN55grApsB8Ix%2FhlGtQn%2B4YVCxo&X-Amz-Signature=22f96c7cf3c930f9321ab8553dd0b815545afc9a415bc0af8423194cd10c0b0b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3PCEKDR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWfiLGjFK5fIU%2BAABQt%2BUyPLhqlMmKijh%2B2cICCXq7%2FgIhALA0sknZHfJ%2BGIIo%2FrVIpmPfdFMGocgxX7%2F2dsyrwqfzKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx5Sxxu%2FwYDCcIvFt4q3AOZHo%2BlZ4GHMUleaY7H84AL8RfcD14h9CDaG6sFDfDzPmOkvAla3n99DbO9vDkKRE0qBFAyke5muBI6UtJF8%2FJbdla%2FGV%2BMGz%2BnkyHjTRNdoEOP4TNmKt94qE6hKZyNmWV2fpS9C%2BzN9Uy9ejZFAwu3GNTOwjEsPeQZGnR4rlK2zqgXtm44%2BRqJ8GfEU6h%2Bl63NpjlvgLX6BAyXzYV48p9eaXXRSyR1OD4CdXW3GWzVJyfz0fzJFTTrPj6ApHdteYzBj23k9AubSvCh2QVRprOdZEs7aNrvEcLLSSJacxXDd3VJse2HZC9wDaNB3FjPGiuvWB48jBU%2BZzo0qT6h10UHpMNtCCuBIHn%2BgG4ncuEfO1fCcr61qT9hsd%2BBq7SN6Sha%2BAFHx0KB9N2E4cd5hJLMxT2P%2B4dkjBtUyREg5kji2knLhFlTWbayEAw2UEdPdo8o7KzSUXGDM0uShYDyoFg1q5LObVMiUDKxsghIL4BaFfhi%2BuJqzuJhSmRmFo0aQiWR8gR8jRVNLr0Ja8JaPeBp7K8K7%2FQqPqD7h%2B%2BkN90PzQM5LNDBjd0dK3tMnOu5JYiz%2Bi2JXCqlEPFyYtprk%2FR62yH0aO1zgLy3Jfn231OPUkQeErDB4Fk%2BR2hHXDDkk%2FW8BjqkASM9q1Ze25EBC7nz5%2BYsXiy9MXv3Cq4MerKKfySJ13EknOOBh7rmiDBVAZGA2DZbe4yAHZX5DjipYEicbayDoyiSLZYJCNfJdsrWQEHYdOnnLeZqLMQZprCw%2Feqj2QaugB%2Bp%2BES18ndDoFIZjwV9IuA%2BaVVgP0oj1lMqO7%2FQlKYvUzf7M2xLdO91I8%2BySDTmAPDfmCflnydr53fb8O6WcHhYlfEg&X-Amz-Signature=6423167bd77b0a772056fdab30af3595c8fd388ce06291a137978676c1fb12bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YAJAT4J%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZwiLSXBi4cuFctQH5pRO04eQIG0ecpfQF4q%2BCiwBQAgIhAJcmmgPoyNfiUrvYQr%2BJD5qHAAKpwJ%2FMSm782x3pkS0kKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySlymNhnYF1S9y%2Bq8q3APz6nJAqW%2FyZv3k3WpHDLh3Pwob0FUq44Vm%2BNhV3ZyDDPkPW7upxz4YGYmI9nyZFJnc5X25IFjAfZAW2dD%2FmIslhHEG3VmlwjX%2F3r%2BQShQ69VGlH4SUeJ9z0YGFZsfxjuMm29MskrSlwVhgWHea9diJCvYXuX%2Bjd%2BG126EQSup%2BqncZ56fBEr9om8TYqK3F0kTjAmSawvUm8frPuxLtXcvFDN7%2Bfi6oVV9vcDaMd7sB6Zuix5tzkZn4qCUv4XRLf%2F4ByBxZXuh%2B4NNkGRLbPg%2FB%2F3Z86hQexypOyKkur8Ll0r6IeA8ElLrUoRdbqEERvEToQleanrriHdkHqN4uMcMq0ClHHuLFhUHJpn98oEGU4Qdb%2Bp6a337SYKD6gQxuTb7XHfc8STmZGh9YZoaeaAmXn55dfwZ5P5FNvAt3H9gTZIpX43YJMJ0fznM%2BiWomRdInUNaXTMX4f%2FbpLMYJ7VXlReHgjFxIgJL9pz5AyWKVHEal3pBF6%2Ffq8AuZW6x4ozvt6f1iPZMhONcxX8xvALiJGE2h0n%2BX0jGRAyM5UtKOstnJEr1trz7pDIAeeHT088D1aFXcDgk8wd0oYumgJS8bfdWF9eNJU3E3WU570EhYT6d%2FtDSNocIDXi2YGDDUlPW8BjqkAXVOHwfEjII0ed4v7DJp4T%2Bv%2B9rI5%2BPqBMvj5WwzDFoh6jKwd%2Febgqso8zcO8EB7%2FzLboSc%2B5TEq38LZBjtXOe0Xr73W2avY72tuosV48%2BLsUiLLbVbsmT9WBraH0Ih8QS2dclR3O3tVQiy7454FX3tFcTqOkR2B46tAVF1kLovJJndt%2BJ6%2FgFKmVlqp%2F5GuBPtEAKntjJRFSVCuk50MdsRoALaH&X-Amz-Signature=66b2047ecccd3afb1cee1bf12fe7be2e0708acc2484ac96a792b9ed791362dae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNHU3A6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG01CcBv67eL6lrvBBVQE7q47ZICm0erDoOl8E9RJ5oGAiEAoLaNGC6w6V2OTBG0VrYH2gF9Snl0rvmDocbAXeBmWzgqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ5yeQb6lYyXT95zuircA5OTuQAxcgkNSA7luOlRgEW48RbY4WeGnxnxZyemQsypx4sZmJFHscXOtX2mQFzHXdP8d2uYBeW8emhqjSNqejyeEB2rzPBUzHOuZC80U7QEEEpkN4dO2qtI43HPOwWjTmTw9MbZmjFYVqFR3qbOsSHfEAG6CN1%2F7fnmoPoI%2B3GLj6ay0g%2B3Numk59Q2Um0j%2BdgGMYW5Y5ruSrmeGmCtTslhudl%2BNg0MNbwNuy42Yzxe9f1hAn69jjU1ugA9CqJkSywFW3Wem0qyGPLw9dQFYYPFbBBemy8OvpZ5eBuWRlVFAmoAvDg0Ivb15vPvhkDtkv70bC%2F5r3zRlvT%2FJIykcXhC2T25FPRzLMgBwKtv0iZ6AmAUCSfEAvtUTB9CtsF3%2BJqYtPRfKTfaXjlfpl6GKMU2OKKkrD3Z3TRYhNq5uwR0PTqPd5%2F5vw3x2pXLoJFXqruUQjLzcewYCr7L1FzPiQDoi2Ddm0r%2BC5UoSP6LQRe1EsFtFUlYbha1ejXLwPq25A%2FjpxAEsF5Zv2uEOg5MvisI%2BmwBl%2Fl1IyZ%2BXwAYPSZ%2BtdiKYHDUD61uzbXL7omMDmA%2F7UYrI7ChktJN5vDyuJHseccKC3R9uEsn9yIlaMyq4YHAQTVuKCVQleVHMO%2BT9bwGOqUBnmKXYh4jTe9hl7fMoRN6sbcB0DRDH%2BdhA%2BbwMelCg7rb4n8NM%2BxLlEC2sVlorfFfGt6rHjCgGCO5QWxIrsYBN6sAWZhMN3slNEsLpONPTJxwHutdx0d4SP0pyDKMS3AIaMUu0kdVS5e3SxU9fZ1EvAT0%2B4OkQ4%2FvpebAXvSI8BLXFrDWlS8EL9ctNQMT1OyDwbbMU%2Bo4IfqA472VCgec6p2bOgNX&X-Amz-Signature=861c6816cc500d1f01ae5014b89a78b50a1545cb2b50c987b791e884bcbfc764&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5TXPXGZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSWH625%2BB2uYbmy82fMKvJV4P4sjOAjERJ3dgz9X5J4AiBZUNgJc4kVUV5HN5heGfWp7FmtZjCSkYfww6LeT01CpiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzLZrv3KGsXdUvsvUKtwDtVpnzGdkACuBkPj36gQOzU%2FVtY14uWFFY9iM0MT7qEXQ%2BjG9SPMD3zQwTvUC1b4A%2BYZh7HoncaBHsCICB1JpfGTV0ozoIPIwyiLcTpAx58kMM1kMQO6xro68HFiq6uSBOitRZ5WJWOCKsdptO03QxA50JwL2kYaTwn94%2BaCi5CT7jjupZk9byspmmlRqQgvYyXTYoDlCcvUXaJq%2BhdHEuIF8oAy2ZoQssWmEBOxwAe7MJxRz3bXvxVYkL7%2FyDqV4NNpJlPK1jVCQIc1awTtHAc7z8i8DwddTVZDSa%2Fv99P6GEj4GnswoNx%2F64gDBeuj3xRRCByixf30MX0MVg9ivL64v0YTni1V44Lr3%2BLIkE5cu1MCez3zDYLLDbUJU7Bp059BbqJtwBecl%2BbrxhWDYLAql71WMt05c3ZkcYdZmvP2ca26pO4CHd8zb18Mm9aH4nV9BLJp%2B%2BN52s80grunjLEFHaVPNpPekpxaJ2wabO2jvEfTH1nzklxo5vbo2VweF8exMigXe5d%2BLDP4mOxVRIgYg69xa7niJ23GLBZojQJUq4RpEmNBkoCzVuJa926FR%2F43OLLjJkeodeXzgbsEyYapnU%2BCbO4ZD1Rn2ED%2Fuhzk85dBRDuEWON15zFQwjJT1vAY6pgG5I4lE%2F9%2BKf8E%2FR2ZRaSSJwSNvL1MoHK%2FhZSVm1jQOmJ%2BHobfVb8Qy90%2FS3lC4xtESi64ziM5XfjGnxlGiTIaxM9owKo5rMPr23nDHma5fWpbXTL58fLSDmkLW6wI4F6WL9PP4cizerxw25eqtA5DUQ4zCiXcWOAV0SbpowPNssJLkQCuHc475t%2B9eUVvwhHfgyc8WQxY4SwIJ4DiNIXi%2BINO56fI8&X-Amz-Signature=36c92acb6cff01db4b4000d56ed16c308c54dc8583acfc88e95a763d449384b3&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJKAMD4Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC2tdOf39JD86Cs9t8RAtHwFw8gguDEEzLJ0PjEheqawIgT5iNq5IZ73%2FuTdv42Wy%2BZTuMoCVr5vQ6Nj5XJNadT4kqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNu3ricG7tBmBVXNQSrcA%2BhE%2Bsul9Rb2znyVSF2nQdeVGA086FMH9K1kUjrkYBtp0iDLm9T6k6Jn%2FiU2qo9HkdhHkpBIXaZsJmq4rGrKwOaYUohWWvMqFkXvY5S8U8MzAl3PX5of95wgU7hCuN7eceSO3OQI%2FQoNuLy6D2B8R8TIk%2B8ROM4bbAKkXpnM0GsXa90A%2BICAmHUwD2aI89MhlSw9DhXX%2BiSZ7yV9BjzIsf8Vv55MormU5w0h8f%2FNp9aQ3bCmaCbMG6gJbFdvLw6oWrAYWLfBWJd3YcJs%2BXPQKZh%2BS3MCy23QivjpV8%2B2lue3QoHQjVm2CDerZVGdhKLS2%2BbrW8FoIyPKkWQaE8mPPiZs642%2BGAXqVQ4v0ti06wwcfGyPXcT7o5MsC8vvBw4ToH%2BLCfuCiDtN1tFSI8f69o1OJwe8HyUjx8PxRwywPXbpxFGxjVnoHkLcg2LNm8UcVNk9w550VqwB10wZEzTw4kpmuOScDJNb0r2YmKdIeVHWKDFX8CklTBdnk32%2BDGvNKZi%2BMpCwdm4va8KDAQZvaKFWgI3XDdb0V9ojuzmrGORGyqsP%2FPdyu1pUqxTBsddcZqnKh94iFEYVd6EgmRty2hcReqWpeA5dufgNrzGgLcLyKKvHD%2FG5t7qz8RvlMOSx9bwGOqUB673oQJ12yiTSw23wodpuOJgiYvRnw18xUrunIp9elI6pTvjiRYaUK%2FCTc9gjK6Qh49%2FeAHBcfCnO28%2BjLmVaHR%2BWe0lwS%2B%2BAW3aiem5wB9pdJteEbsx0ohEaMI5avCccrsKc1GSiZwnwyZ9JilCAIlfF%2FRymksF%2B3RE9wUR8fkQRihzzlNuglsJkxvyyCbF%2FMupHKB9HVZSMnZt4G014hXF6K1sA&X-Amz-Signature=bd0ba3a48034127e541490e672d0bf1d2f91b182cbd757a57525ce4d6845621a&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PLTBSG2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlfeMdRdPbB%2BgU1acThjjwxoBu4s5D97N1iwRNQUl%2FlgIgaHlWoqnuU6Ufb8rbvq0rGyo5XlIXHiYc98zdsIbWCZwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz%2F90a46wqXnWG9MCrcA%2BdfCcKw56dYZWyVM4k8%2F05AB1j6rtRfhyEznIBATrb1Hy%2FaOsQloLf8nOdQH0SsguWSvCJGR%2F88MDZWWa2BuKvs3A8ruJuJzCqJVsATaY3GIxHVyZWBEDzgdmCVI0Tmte2gMPPawfB86VnJfjvwMVDHGU86bDlO%2BFMdlV71mMb0Nhc94TFRBs0DYQXrGcug53RDZVF1DtwtxY5XpO1RwKxzFIhYESeLBzos9KEY7Djc9LLtLgXB8E1Swz3fzEtwPmRifwjGwiGHXa0o%2BRNSJGFW%2Bv6dPw106XGEyLaPorqgn5NsaSrrDCslVhJATRO2Ka211%2FSjOgdpjP0vUyDcqJuyMaBr5xju%2F66LEr8Z0jmLPwBQBoPmI3zf4o8WyecHJiwelruNi11E26mzr04QR%2FDzsU88aocDX42D8i88cFVSDX9zOWLtVRzFBjP%2FIK0W7DfmxeNfIzQdi5zmR2O13GqbJfocMo3cJDzypBTPw2Qw%2B7qT3nGtvjTxgng3m6%2F7b9veLWAx0Qxa8LQZRE%2FYSQZc3eOoEnR2tpYc3jx0y9Jbq7%2BEnXpGuZrw2688FXROJ8dyJSTArij4dZv4Ot7dmESUlUM%2BTKDS5%2Bn4QrcCp2h7jBdenbCkjIudUDAZMOWT9bwGOqUB2Mh6VpTBIlo2CwzH0OtG4mDIwjX9x7gDHx5SVRRjkgwKlh3srN%2FB2%2FaHlXfGjZONIbI06PWv5UThfR1ONaVi2Pfmf1n6er1yZ%2Fzm8mmuQVvqtvXeNZ%2B71qWXmcS4HHgAvMN2DWmghfMwqdIk1j1jkzNyqU%2BWrcRNarKlCgyA5h31LifrgT25pLOsi%2Ff13Rtw%2BcnTEnAfKqpk4b8Np8meUOQljH4v&X-Amz-Signature=a6ee315871630e8aa0af2b0c7cc1d59b7cc51536c03860164d65f1c1e849aed9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNHU3A6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG01CcBv67eL6lrvBBVQE7q47ZICm0erDoOl8E9RJ5oGAiEAoLaNGC6w6V2OTBG0VrYH2gF9Snl0rvmDocbAXeBmWzgqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ5yeQb6lYyXT95zuircA5OTuQAxcgkNSA7luOlRgEW48RbY4WeGnxnxZyemQsypx4sZmJFHscXOtX2mQFzHXdP8d2uYBeW8emhqjSNqejyeEB2rzPBUzHOuZC80U7QEEEpkN4dO2qtI43HPOwWjTmTw9MbZmjFYVqFR3qbOsSHfEAG6CN1%2F7fnmoPoI%2B3GLj6ay0g%2B3Numk59Q2Um0j%2BdgGMYW5Y5ruSrmeGmCtTslhudl%2BNg0MNbwNuy42Yzxe9f1hAn69jjU1ugA9CqJkSywFW3Wem0qyGPLw9dQFYYPFbBBemy8OvpZ5eBuWRlVFAmoAvDg0Ivb15vPvhkDtkv70bC%2F5r3zRlvT%2FJIykcXhC2T25FPRzLMgBwKtv0iZ6AmAUCSfEAvtUTB9CtsF3%2BJqYtPRfKTfaXjlfpl6GKMU2OKKkrD3Z3TRYhNq5uwR0PTqPd5%2F5vw3x2pXLoJFXqruUQjLzcewYCr7L1FzPiQDoi2Ddm0r%2BC5UoSP6LQRe1EsFtFUlYbha1ejXLwPq25A%2FjpxAEsF5Zv2uEOg5MvisI%2BmwBl%2Fl1IyZ%2BXwAYPSZ%2BtdiKYHDUD61uzbXL7omMDmA%2F7UYrI7ChktJN5vDyuJHseccKC3R9uEsn9yIlaMyq4YHAQTVuKCVQleVHMO%2BT9bwGOqUBnmKXYh4jTe9hl7fMoRN6sbcB0DRDH%2BdhA%2BbwMelCg7rb4n8NM%2BxLlEC2sVlorfFfGt6rHjCgGCO5QWxIrsYBN6sAWZhMN3slNEsLpONPTJxwHutdx0d4SP0pyDKMS3AIaMUu0kdVS5e3SxU9fZ1EvAT0%2B4OkQ4%2FvpebAXvSI8BLXFrDWlS8EL9ctNQMT1OyDwbbMU%2Bo4IfqA472VCgec6p2bOgNX&X-Amz-Signature=d942dbab96dc272fee16478cac0979825b11f73f10769eaf5c5c40b8fd0681d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4MMUMDG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6qyBpfNUzKJ9akhdy%2FRgzQQEUKPDRt5LiK%2B1SnEKltQIgcrLaCs8duUN%2BcVAUrNVI0sS6XzuRU0jM8Qhs3lGtILYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMxhjzHE9Q6yIAGksyrcA3bVaLp8vQ1aKzrFCnfGVJCCWO70cYENrBFGQIF6IPMwe%2FMfpADg20clgSITtfUDk1zVxbIqFXu5NYf9VSV3w%2Fdj23O4pTP2HyQ3JuMRcWkuBJYX7PSz3L4mjV3FP1ag5ZUlG4S8B49Vt2O8hnsJwjvLWmV6Aail1i286%2FhTnB7akUlQvVEqQOJuXxx4qBaYxx3CDp1ZuFEH5lE2w8x6X6H9JjyhPDmoWXYor1sjNfHtgeebuoMYZb9RS6%2Fuh6%2FwKS43t1WtnQfTZuK2wIoMRLMGYXYnxT7SiIWNkLsshN9XSsIbmyizrSINFmcEtaULarhVcRX5VgDW%2BxwMqDJ%2FtPbdNrm1GmBfdIpYOoYnTST%2B4OjfMbFVClQUaPc89Bqdy6ktHqQ0NuAFZSj3P6iq4f3tdrgdJhxW7IZ5c5CYnCDUoOdkqKpl5Ob%2BzdfYgFHzAweoOx%2BJiSR2RJfIrI5%2FQgJsG8RF%2Bj4Qtr%2FQVC0RVZg1wYc28yrqe2zJ32BVKXbKP5UHgw9hed8ARL7JNqWtp33EdgOgEvmpNaT0rQxNy5qV8gqbfPME5Z8dp2Zvkly8yMFTiqNmNOZnrkTOB5%2BEI05ABamkIk1xrWjOs7YfhOYgdhcBBrlr9ymF9jvTMNOT9bwGOqUBMEveDVtyt9jGkKFmA49emmMgF29E9h%2BvmZMLFr8p7Yuozf9%2BEqLYE2zqMVdu5kFgwFMv6xrIuSYWEPXlJlMz67HuN9ibAd0yc1XcIMWXBriyU938kHWS1CtmAugw%2FIl2ayJKJLPFqhwWh9dV0wXhn1WnL19Doad5XQ2OgGWwed%2BQIU0TlNzOpINJrX1s0fnkqI8UV5ew69wJyA%2B%2BSjwzOpS5z1rx&X-Amz-Signature=7fb7ddd1627d1d2c3fc66dd3fd35d2425224c9b314f536d4f6e307a5b1c6e0fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4MMUMDG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6qyBpfNUzKJ9akhdy%2FRgzQQEUKPDRt5LiK%2B1SnEKltQIgcrLaCs8duUN%2BcVAUrNVI0sS6XzuRU0jM8Qhs3lGtILYqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMxhjzHE9Q6yIAGksyrcA3bVaLp8vQ1aKzrFCnfGVJCCWO70cYENrBFGQIF6IPMwe%2FMfpADg20clgSITtfUDk1zVxbIqFXu5NYf9VSV3w%2Fdj23O4pTP2HyQ3JuMRcWkuBJYX7PSz3L4mjV3FP1ag5ZUlG4S8B49Vt2O8hnsJwjvLWmV6Aail1i286%2FhTnB7akUlQvVEqQOJuXxx4qBaYxx3CDp1ZuFEH5lE2w8x6X6H9JjyhPDmoWXYor1sjNfHtgeebuoMYZb9RS6%2Fuh6%2FwKS43t1WtnQfTZuK2wIoMRLMGYXYnxT7SiIWNkLsshN9XSsIbmyizrSINFmcEtaULarhVcRX5VgDW%2BxwMqDJ%2FtPbdNrm1GmBfdIpYOoYnTST%2B4OjfMbFVClQUaPc89Bqdy6ktHqQ0NuAFZSj3P6iq4f3tdrgdJhxW7IZ5c5CYnCDUoOdkqKpl5Ob%2BzdfYgFHzAweoOx%2BJiSR2RJfIrI5%2FQgJsG8RF%2Bj4Qtr%2FQVC0RVZg1wYc28yrqe2zJ32BVKXbKP5UHgw9hed8ARL7JNqWtp33EdgOgEvmpNaT0rQxNy5qV8gqbfPME5Z8dp2Zvkly8yMFTiqNmNOZnrkTOB5%2BEI05ABamkIk1xrWjOs7YfhOYgdhcBBrlr9ymF9jvTMNOT9bwGOqUBMEveDVtyt9jGkKFmA49emmMgF29E9h%2BvmZMLFr8p7Yuozf9%2BEqLYE2zqMVdu5kFgwFMv6xrIuSYWEPXlJlMz67HuN9ibAd0yc1XcIMWXBriyU938kHWS1CtmAugw%2FIl2ayJKJLPFqhwWh9dV0wXhn1WnL19Doad5XQ2OgGWwed%2BQIU0TlNzOpINJrX1s0fnkqI8UV5ew69wJyA%2B%2BSjwzOpS5z1rx&X-Amz-Signature=fb741f5f43811e7c1cc58677a1294d19d6a971a599c061b7199e986a30aeed36&X-Amz-SignedHeaders=host&x-id=GetObject)
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