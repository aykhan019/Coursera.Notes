

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSNQXNKV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeKDcSL8s1u5kUCHg%2F1bGKjYaL%2FoEfjvCgV1tTVfaEXwIhAIafF867QPXfzq6V2yAt8lVXL1%2B7Drey4nE0iS6TyoE%2FKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBfYBECrj%2FwrXY9yUq3APoqvkB0Tqr8xqk%2B4BrCypEOwZFFukxet1hVGFuI3fphR6NoQnADnaunONWgiJbwT%2BcU8Iu%2Bcf688yH3KhD5xRkIDTSmWpYNxDQAf6K9RoEoqNjlVmDL3PQwRVuzWmF9HjkGSHRlxV2eWc00S3MdfpQVggeg5h3qOM9IrzLsEUBEcEr%2F60x237t2WL0Trl6fF9PSfm6FWsrSolIE2iL3UiHMvgXWvFrfWVN9UVyYASmh9ruzBBVa6k%2BxXbOZP32v0bEOZGbgzMxUHlgiMhLO%2BisT4EbX2GywY9jHOWF6sVc6VuqyBIKm5o2R1vPSJTihuLOGYkQbWX7wb1uu39Jxum0j%2FBOUHDjLkTrMAxxy2RlsT%2FQuxAy5ro9CDdj0uLhw5j7wyjfPL7IHS%2F9HqvsxDMwyPk3hCaY%2B%2F7aBsnF6Bm6g16lI9tNORVoIz8ySbMajFDAChTQaYUHr3KjnZUOjg8YyF18iYJ2z5NzaxOlYOzmG3w0y%2BXDBQc8zUxpWUx4UZ2MwM%2BjhQAgEJU0DBmvy9O69ZoixHq9LYJrvlNvZ9ESws0myiT35QMBOzEBtIo%2Ft1wK2CbTh%2FGCdloQRCjlw1OxsUXLNXr11ZoI8N98WGsg2R29jaAqKI725muKfzCH0PC8BjqkAVow2n4CT7sE2hihZoF8FlHpkeCIBPLnNWbnKy3dZ1Fnz0UPaSg69%2F6LkmVb7jwuja18FkEkQXgxCH6Ex033A1V2klwh2vhleu6t%2BVn0tGfF9FktTE%2FBjNXbXFYgFi%2Bky313HI1eUsPDI8BZGdnuOLIjMHtCQoG2ctWKiElc2x0ugtiAYP3QIGhWEIJ5BxeiNwe1qIVmLsrgZ8b35%2BbAASIlx6Eh&X-Amz-Signature=57a2eebb14734be45ca53f9bebafbf868102c2d4e5f88ecc509b33f14df254c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXM4BXPC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIqaSPa7UwQ%2FtA%2BRh%2BsV1V4otWGctP%2BSd51CHQt1P2CAiBgTuIrMOJysRbkqKkEyVq4oZJU7p62CHUP3PVl0obgmiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqVSeHyzeCmBfEB6GKtwDKd8LYBKiHRn8uyjSzAUoemYJQegySxPhR1bAIoBfA3wz7zp9NNG0OAU%2BeQsu%2BDmlqbtF0NBEHhwTpQGffI5vkPMbVla0fChdVWCF3UtXeJ%2B%2FniCyoYhSUQvFQ8yom3Sx57tYXtUuMVxpK4KqeIaTv9%2BDIgBXubLsqFhUanrs4jQ6318O867XMMh2TSIRrfQ%2BBYWV3QnU2JjQWN5EzW5rrIHjO4xGL4bOiePyuqRZwTH5kHSJAvoWZB5CWWSBQir%2BBOSwf%2BGuPMUkVmQgwv65aWQkHdbtPW5lE7C8yAnjLoY%2BftpMboHeElBRlhVbYGbu3RlPKyRIlpSOxYcdc7EHCy9RJc%2BVL69zcCRzw58RqnuzFj86AqCc40cV9lJT7xbJdvbiFi8t6Lokh03%2BokPhMCC0Bniof0RS3%2FDQdOcwO3VCEHIotpvQc4SiZ8csRQ%2FNNs%2FuALmkxGtdlCwWjP39yD5%2FX5Dq%2BMKDVJ7eCn%2BNMHM2d4%2BoUMXL8qVwC6g6O%2BE4aeF3TDMBfOKQXqkjjdyvk1KrIv%2BgrZXbCHJYKypYmMRGsfKQSrUuc47GTRDU1jJsIHZDRs86nciv67C8XMNVbFHQoO13c6o9rUSeNJsoosyfUhTDVz5aOv1wq7Iwh9DwvAY6pgE5PmRGXWh59jFoHz14yjWkQRVHwmjlYRXu77qvCMoaoZVAvB8f3dK67LV27YhJl8Y7eeWfVx7Ymdd7WoALPEYAvkc80x23rKgcVRwlOxVpqZ%2Fl7h%2F4wz2LzEx0%2F1ItJzLpA2aDHTtZOPvt0xnb4OYLFyJ4nJOpSbGL0LejsqJVQyTlYyuUu1%2FGFsJMYtBG0IR8jDCFynnjgpZmqWYQAtpjzwo24GVq&X-Amz-Signature=c862d9b48e2f93a739e1fa03c6bbd402e3cd6f04550d0c78e5b10647e60d0485&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=5ca8419bb6edfd4ac4873775874cb9bf2319b499c79ace538e8df9384c8bdd16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637AUNHQ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5dRE9f9BMXdvsRAsWRZO7kAExT8g16Gop2Ze%2B3YfCLwIhAKgyy%2FeGs6BtXfOYNqiJD8MGyorRQxh47ippIaL12%2FiVKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwv%2FItdhaw9dDSpWBQq3AM%2B3bnFk7MNNuJGyR%2Fx8qiIzQD88%2B0GnQslmdI%2FmSgyY2l5J54IWXy5%2BT%2F5Q5a3YUhaEhDSScbFFdu%2FNR7X11bTvX0MuxLejr5xJhRIsIQp0wr%2FgFBcZgOM1jbj4yDVN1tIvdF%2BxjE1BS9%2BMwL%2FK3RRaKr56fXdLPpQxjDshVM3LwTcuCJEvz8czNBSx8vFIXWgHg7a3w4J1lUiW7trqkU9A2%2FhAW2SGHxAUs9qFZKqC3LPVU46KUBNz3nRKlpFtp8EqGBw5Tdfo9CjU6QUtsgiR7YuRMLZ9eNoUqqHaTS1YZj7Ulm5x8KwlfxwmV6cX21NS8ODf1%2BY3yOJ%2FsZ4gcakM%2Bjf8bzq1ui%2FMlXIkrJVOj4bRZG0rFMRC%2FSc83Hz3ghLZM%2Fx1VqNQG6FWtYWaST24QFDUl7z1u3drjgIHnCO5I9YJwVQqGjJPYVfI5ASq76U5b%2B8TETM3to3NGg4QwT47Z1yHThYipXHs6n%2B4KTRZL%2FjTxvjaBGeFHRSaFiDoKTYcU7AfOlBGBWKoI7mN1w3Jhm4zXsMMyVZcTeLQHjysph57S%2Bgi8r63kbjiOTag5Tja0bZ%2FRMgW0xQcBrQW1XH7%2BxN69BZ%2FP2a%2BsD9L5264QQQ7zeI5AfTM207rzCH0PC8BjqkAX4cnfOGt9U5gj7REIadbtdO4oN5S0ZEnDQBGyBj%2F4hgrdZYTpHAfAlsE6tDq%2FnbQG0e7H1sUa5rtuNenhaMTE91T9LY2EbUh9p6ZfZw58BZ1OLnyKn4bA5w5xaWkJNC%2Bj0NV1LvfRZsaUIiwb%2BhxdE8jYK0%2BeWnu5RFe3KAToC5VN6WtMb2nM%2BM0zwPcZ8NIuLPUAsuL8qsk5dgouyWoopvJ8qC&X-Amz-Signature=d66cb0cf1961b5ed9dc63b6592cd48ad619739696989f5ccdfb83d3817edd7ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBYAH3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICafSmm0cQxLQ2jIYydJkGKLbyMuxHwlEkyWLM%2FxIRytAiAL7wvzAf9VkR1GkM9T6CE1NemoBxLX3R83lNoicL%2FqqiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCWJKNVmyeTMe9lZcKtwDvT9kcCGT6yLgzd%2F0iL2F3Vr7a5mGLuv7%2BEIWoSMBvnCvQ%2BdAJktBPPEf2OyWZX5JLLLaJAlI2GmVTlXdiq35K2CD%2F4rQa7GXRtfkFbB542ssFk6S10WKzJCMOIx8dgUM8hV7vlpdbRpCHEKet9n%2FSg4TWHozBpwNQw4L83MZ%2FJfIqDEgXvnOsOLe%2FOsBfB3LglKnY%2BhjeWo8C3yAy9ZgStSJNEIfLq54uicBxrLDagFT3YWB1fCn%2F9JRtYyXOctXzv6L%2Fw8lFMiYS9o%2Bz4tXSFjOdOsBcd2ebMUZqQXCcxA6dP2u%2Fm1xDTsHPopnJaYoiqoXHf5kSkMw4hwLlxNChde%2FDA9MuBB3JIf7PJqpg5ELWgJFG6iCsXYfVa%2FQfH%2Fu8Y%2B3G4TsSUz7wP9VMULdApNQeedXttN5kmSijOwNDq2HP4DghcZQozgRbCQGpjYjqwNJ808FxP2Ov0pGF3n6FZlKJ6zkrLhy5RxMJgjPX9qsF6Xf%2FC1nsG%2Bb7s51K0FX4g0QNtn4y2jRDxGYZwgndGLyCnyEd2lHlKvpfdSTtzIT90Q%2BGRvXdxw6CzvF2MQ06z8oVX2YfVilEG56JRNmLsOoDxG5byKks1RngN8%2BUMLp%2F3ipuVHy3I4HPpowuNDwvAY6pgGPfm%2BZqn1fq%2BIaGgEnUMvmdEQn2htxwLpYMN8vqMYLoIXHnoWJxff5SSBOvQtic%2F7tKcfGQ%2FHZRjjEC73VjRtLjwF%2FIIfDcdb6DTIYt%2F3aeujHwB8aHxrtAsJv1wJ7ZsoMwuzAirdiu%2F7kdmmc3A2aZTSm8bi2cBO4Y9LRpP00yhGkYQzUUgUVPlb4%2Flfg8RI0hVTzKql3XWCHeV4oU2Bfu%2BrF75nw&X-Amz-Signature=f126dcd5d917cc9c3ef4abd190e5bac204df45652c7551f7a8bf84a7008fb2be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7JZHDGM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJ3suxQn5fm25nRYJ8c8Z8OgNgnShoQUVkN%2BR62Mg34AiBZ9jTYhMH1iOoPLd05BYYZyCkqlOnkgywig2Zk4aA%2FDCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQ8KmbffozOyHz2pTKtwD5axl21vfO1TtMYxS1kp%2BJ1ZDwNq8BGf67JDp7TyqMAiEUsA6aUVDhyyeG%2FMb%2BmzxQBAmB0vhbVrVUEAXPr6rftB2EWs4z1PTLOh8TmVBOo%2FAQky8vJD4RYlNP21b%2BlUoUpZWYNaH13j7VyDeP1JMe7A7TDeOXoeDX6dfdgpx%2FsiKj10t4TMZbp%2FAjMKuA%2FN06uk4qZPL0P%2FGpxzzQ3H%2FxUA28rKvYo1KqqxU3qsd0UnckN4J9hHLx%2FLNGbEj%2BPtI2SUDTfc7rIyBcYpeS%2BZrFhXRCbGZbMDE8vJAcm%2B3qlB9YELObmt%2Bfd5SaKg4FtsWldHTEAtGy6HeXGbwcKpczqWf1eLwDpiX%2BJ%2FS2vggLB3hDnw4TtYxT6cejdralQFqIkiwI9tiOsxSm%2BEE%2BrBfZfDYBif5kcL0gozn0r90MctVcl8C%2Befg5X8eN7nkRKSXiFPre%2Fi5HENsoOo1RcSbnimdR8lajrNvrRbYhutFhvppHSBCUwlCm0fOTTQfMvbIsPaAYhztI4hYNmFF54SnYbw8OaKqorDAPQcQ4nerS1HLEXdYp7Az18dgJ9Y4kiXEUrP4gjPTsRkkz8LraQbGoU1jO%2FBst%2FGb%2BClQhteiP6Ts4r82npz7x2yaA78w1dDwvAY6pgE0gx7mI%2FHpAaYumB%2Bc29EVj8jqLdguEPRiqrbwnPtoJ7Eae2Ku4l3bedRKNEaXB7VsoYmJwpzTNF6sVzVvcpPTrIcgKJxV0ZzbYnAkmKOqj5lAhznB8tYkPI%2B17GkFin1On4aj2upQZ0bx6B%2Bwf33kDLw%2BlgaNUoXKicbWoF0eei3i74Wh041UchcxTQOVHxrHcEaV92Q3F15k%2F4qJRr7H0rZm90PI&X-Amz-Signature=cd9df002075710aa4adaf83020e86114b36cc8450ab4caa9c2a8af0f733bace1&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XIU2ONS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0A8xCVAdYDu0XlMcx66IW0Ji0HMZI9I1CGI6VSl8gqAIgVpV%2BpJHV%2BZf90hVCVA6DwpeyRmOAEtPX7A%2FvHwP3l%2BcqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbQ04medM4y2zcefSrcA5kX1rmKGYiuyUgICRugSseUi4RvlQqyvCxQAqTUUTo7qxjILZSbMGKCw5PkDiCnr0OrPbWjuB%2FheDzqcyKCGs7oKWEvlkNUYHFryrh9E7xOjtWuR329fM6uf9re8G3kxXc2xtqqfCZKqz9Jw20Mr2am%2B8RHVWwK2lnZ1TYw5g4iwMxACco8YH%2FsbdSkgmPi44NANdO5n3pVX45XF0aVRcDzEs1fF%2BrdzgaBhEMTgwQE3kyyitpInxnTYLdA8l%2BYk%2BQfF9OIro7eiNH9EpMDFvAoBKuwHBE8XK5He%2BO3ztvtXwaP%2BtfTOKcyXopSWNIU8q6NImlTzfBvQ9a8jZCgTgsLXPfZZmwsO7zXpchvETgSyNz1dsxX0JIvbqQxyr8B3QEOYRogiXGwOUGDJwuDbMxULwmEFqvjbHRB4kk%2FUf0MTk7IIuU5jW6TrL1atRrxHLnv8EH4AhRUtTif11r5ppuzFmQSatJ7PIZl33MeWE%2BEgrpIjDWcLwfurP7XUPQPr5FkRcvh0ORfWMWbj37bSR9G0kLi14I7s97o0T5g5Xbn435mL1Ii1gNK6KTZGM6OWKv8oenjnhM4UUOlJStTThRj9E529wOz5QIc5I%2Ba4GCyY0OwhHz%2BK4YVYXxcMKbQ8LwGOqUBvjBm0jT3ZPdYCzTuQlPrBPziFoqOCp029y1%2FOJVaxIu6ASeCZLQjL10GVjZFj9qWSRbN7axUrkcRV6VM9k4pQNlzmmnItfXwpDfUkVQu%2Bfsm%2BhNpjyXMUTRRln2xbOQuqd2VzxFd2hVMptruLZlu9SP%2FZWh5Nj5b8jt%2B8kK1GC%2FR2%2B618kPsBzfIeQS1zbyb8wtATJIVhNKI24BJEkWDhfzxFHik&X-Amz-Signature=13bd20c05bff48801adf99b6e45e4322ea0b2a238a57cada796462c00ab8b6f0&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYPI6WSO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICvp%2BzqdJPEZszZtLCL2aqynDFWhRiT33%2B8LNNkWIBZAAiEAohDNqti%2BJiC2bM%2FYbd5DJEwTiu6RCFTAU8CtuhB9VcsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgCztfsjlmRE0xe3SrcA2UirnSytKkayny37ogEXfnXjPzTsyVbbOW2G%2BlQiH83OHviOat2RQ2ypd02tZOSY4JqIGwJUqC6T84A%2BlYfpxkWF5GwMYTHihe1%2B0Ku05LB%2BZwF1nrNsOtZR1N%2FbjX9M6Cf7oahXU36UMZOuBMdP4rVDTounvOdxQo8ZdIs%2Fz%2BeGCywxcU03ehhkYaTluWb1a%2Ft5ncDAhS%2FbDp0lNJu4f7lIUe4HlXJWBGQrVDZENqzBUZAUnnogBXOnCijar1pRYdU0%2F423g7ecsa053Qgf%2F1GTEYqgqVYZKLWWaw%2FlhOAE%2FR4caYDsyS8ITFOFOHnxxr81uuwxvlCsKS25%2F0z%2Fm9%2FiV7Z8IDPXpba4UB2zyOeAPU2b8kwzesZX1S1kQG7VGKDa4%2Fcn044AL8n0RyhzoTn47pgx%2FLnnEZ5MopWmHfce9IOP9KYm3XxKtX%2BaI%2FqfUV4kHz3%2BLoh6YtW3%2BmWq8p2twz9usT%2FIPX2f3d7N96mpwWMtOQrYdr%2FEFOSCStDZTz%2FcIFC44vjR9jj4XdRWBA0Q0XxH5delNGMUO1uKHo%2BeB%2FSzcOi8gv73Mu7eoAu5ogHmqxR8DuH4IkEhYkt3LdnjDbbAqCqNYrua6qg%2B%2Bd1ih%2FLyo0Svh2Mvr3fMOPQ8LwGOqUBtAT%2FvTTReU11KWsHHYV1s6%2FVyTXsVrPBIVce2js7Xpg7PnUTFFMGkHyGtmF13ojGZVwGDxL8NQ3n2%2Fxpj4Zv2dwZEGsKRMe601Zy1%2BFLpUiwPN6lJPJ3fKiJv%2BuA4D3oNP9SqLVcJQFfr%2FDBBia0oficHcfF2yQAPHj4rpNEHrgheBLvEccTQza7%2BJinORaGPNELJSPXbBRgRSehm4%2Fvm54KQed3&X-Amz-Signature=43bf8749ae876a4a712d89e7194dec566e21c0e1c189ceba820d3906bd9d0368&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DBYAH3T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICafSmm0cQxLQ2jIYydJkGKLbyMuxHwlEkyWLM%2FxIRytAiAL7wvzAf9VkR1GkM9T6CE1NemoBxLX3R83lNoicL%2FqqiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCWJKNVmyeTMe9lZcKtwDvT9kcCGT6yLgzd%2F0iL2F3Vr7a5mGLuv7%2BEIWoSMBvnCvQ%2BdAJktBPPEf2OyWZX5JLLLaJAlI2GmVTlXdiq35K2CD%2F4rQa7GXRtfkFbB542ssFk6S10WKzJCMOIx8dgUM8hV7vlpdbRpCHEKet9n%2FSg4TWHozBpwNQw4L83MZ%2FJfIqDEgXvnOsOLe%2FOsBfB3LglKnY%2BhjeWo8C3yAy9ZgStSJNEIfLq54uicBxrLDagFT3YWB1fCn%2F9JRtYyXOctXzv6L%2Fw8lFMiYS9o%2Bz4tXSFjOdOsBcd2ebMUZqQXCcxA6dP2u%2Fm1xDTsHPopnJaYoiqoXHf5kSkMw4hwLlxNChde%2FDA9MuBB3JIf7PJqpg5ELWgJFG6iCsXYfVa%2FQfH%2Fu8Y%2B3G4TsSUz7wP9VMULdApNQeedXttN5kmSijOwNDq2HP4DghcZQozgRbCQGpjYjqwNJ808FxP2Ov0pGF3n6FZlKJ6zkrLhy5RxMJgjPX9qsF6Xf%2FC1nsG%2Bb7s51K0FX4g0QNtn4y2jRDxGYZwgndGLyCnyEd2lHlKvpfdSTtzIT90Q%2BGRvXdxw6CzvF2MQ06z8oVX2YfVilEG56JRNmLsOoDxG5byKks1RngN8%2BUMLp%2F3ipuVHy3I4HPpowuNDwvAY6pgGPfm%2BZqn1fq%2BIaGgEnUMvmdEQn2htxwLpYMN8vqMYLoIXHnoWJxff5SSBOvQtic%2F7tKcfGQ%2FHZRjjEC73VjRtLjwF%2FIIfDcdb6DTIYt%2F3aeujHwB8aHxrtAsJv1wJ7ZsoMwuzAirdiu%2F7kdmmc3A2aZTSm8bi2cBO4Y9LRpP00yhGkYQzUUgUVPlb4%2Flfg8RI0hVTzKql3XWCHeV4oU2Bfu%2BrF75nw&X-Amz-Signature=0b026926770ec61d596acf5e8b25b125c7893ab47bab466c00730ca340c335f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAL2NC3P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJg0R9QpkAZJIRze%2FIfQGXKJHSwBc76B%2B%2FiLklJHUIxAiA6B4GuGj34hqgJhiZMWtgpBmZuXSoeRPyphHSN6iMESSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPNUyLfBaPDrY%2FcL4KtwDKE5PHmyF0qAmHbrJhusnJO5u8miXq99XEsZ490ZFwd6b8kJStHnetjpXsXJR%2FUlQwsuoF2%2Bg1WrDiCr9BMLDHkSABP8g9VXr5qjmhrCZPYpaBlj6bbJdjnwNltX8VYzQE0pbWIgXYW66tYN4SoUvaVKO%2BI2mLScIC47qhM2q8yKNxHixa1Wu0Y%2BV7gcWS5P0gy2p5eoBqfrktite6lCDKdLUBbm9QSlsAKNdYktbZP0UZpGh7o%2F6UiLRCIymyrW13TM3cKspuvXgRqQsTrDWnfCT11s5KtCza7vnxIlXOEucbxVNV5jhCQ8Aw98C1L17ZXjEZYwxxzjTO%2FdsnQ85SW50uICwEclCZEYbyozhG3Uq4%2FKIqiF6k5fRPtRdJ3YpLczmJU0SU5LZGelHtcQLeKxRG4q9iH0vhMuc98VOB%2Fb%2FZXDQiR%2FRwf%2FvBSF9frD5R%2B%2FTQFZYdxyZjaAv6pONco5t2PuTAmba%2FA5A0FfQ6I15hR8u4q1DkrPkbJenyVnh%2FjQTLCuKQwf1JTQghwxpDX6IwZRsqh3qWO6gYgZYvnWXDj2s0K%2Bms7gq9Vu9O28CXrwu%2BZhzpt%2ByV2RTKdcLpMx7uQphkpE%2FRoGWEl%2BC%2BAa%2FNDi3Mo5iKPf6r6QwiNDwvAY6pgHUBdFkIDzbLg0jITA%2BohklKzUAxCb%2B8YDgYEcTi8AhHaDm3gtNuaaPmWVMFriP5AbDShDydrxttuTr%2BLUlmzUE7n66plSYX4q2i7e%2F6%2B3tSZILfAESqtsARZRDTQbnhattn1Hml%2F5zBEPXPOztBdAvYriEgwDRi%2FG1wA72MnKVgKR7pg%2FZ0dDfMVnu938A6f%2FLdLi4Vsk6IOVqw4MH%2BxBmCSKGnHaI&X-Amz-Signature=6c6144571c68af30800a1358f3a96e1fa8403c0639812cf71443164b442c78a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAL2NC3P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJg0R9QpkAZJIRze%2FIfQGXKJHSwBc76B%2B%2FiLklJHUIxAiA6B4GuGj34hqgJhiZMWtgpBmZuXSoeRPyphHSN6iMESSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPNUyLfBaPDrY%2FcL4KtwDKE5PHmyF0qAmHbrJhusnJO5u8miXq99XEsZ490ZFwd6b8kJStHnetjpXsXJR%2FUlQwsuoF2%2Bg1WrDiCr9BMLDHkSABP8g9VXr5qjmhrCZPYpaBlj6bbJdjnwNltX8VYzQE0pbWIgXYW66tYN4SoUvaVKO%2BI2mLScIC47qhM2q8yKNxHixa1Wu0Y%2BV7gcWS5P0gy2p5eoBqfrktite6lCDKdLUBbm9QSlsAKNdYktbZP0UZpGh7o%2F6UiLRCIymyrW13TM3cKspuvXgRqQsTrDWnfCT11s5KtCza7vnxIlXOEucbxVNV5jhCQ8Aw98C1L17ZXjEZYwxxzjTO%2FdsnQ85SW50uICwEclCZEYbyozhG3Uq4%2FKIqiF6k5fRPtRdJ3YpLczmJU0SU5LZGelHtcQLeKxRG4q9iH0vhMuc98VOB%2Fb%2FZXDQiR%2FRwf%2FvBSF9frD5R%2B%2FTQFZYdxyZjaAv6pONco5t2PuTAmba%2FA5A0FfQ6I15hR8u4q1DkrPkbJenyVnh%2FjQTLCuKQwf1JTQghwxpDX6IwZRsqh3qWO6gYgZYvnWXDj2s0K%2Bms7gq9Vu9O28CXrwu%2BZhzpt%2ByV2RTKdcLpMx7uQphkpE%2FRoGWEl%2BC%2BAa%2FNDi3Mo5iKPf6r6QwiNDwvAY6pgHUBdFkIDzbLg0jITA%2BohklKzUAxCb%2B8YDgYEcTi8AhHaDm3gtNuaaPmWVMFriP5AbDShDydrxttuTr%2BLUlmzUE7n66plSYX4q2i7e%2F6%2B3tSZILfAESqtsARZRDTQbnhattn1Hml%2F5zBEPXPOztBdAvYriEgwDRi%2FG1wA72MnKVgKR7pg%2FZ0dDfMVnu938A6f%2FLdLi4Vsk6IOVqw4MH%2BxBmCSKGnHaI&X-Amz-Signature=a873e763f7a184fdcbe5856b28c6eb7310f968244878e4b48da05c2dcf9e2c3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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