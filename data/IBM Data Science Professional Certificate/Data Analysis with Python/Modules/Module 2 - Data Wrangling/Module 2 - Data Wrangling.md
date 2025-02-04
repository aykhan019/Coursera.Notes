

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OEOSBAB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC%2Bktwu%2BJG8t77gOTKfayuCXpUpt%2FA3lHgR3j%2BfImAjNwIhAPqRkBVojw75ulQeGJpRoRXUXz3oLwXzmX7jW8S2J8QlKv8DCDYQABoMNjM3NDIzMTgzODA1IgwWzYyK9qcF81nUpY0q3APbjEhlWR7y92n3tNHwN2Z%2BrY1i04u%2FrCVrIolrel%2F8waFY%2FnPM9O%2B4hPjiczz6ZX%2BTTk7lP4RCiBMst9Fe9wQZxtkpE%2FR7nPaEXULHbiq%2B6diQnP1PVUcO0lVNPq8CvnSB2yqQ%2FQFRz102BJ6e8U6utiSIMPB5tPkKHipJDwt229olrHE0mNKOdx%2BEzGnAz%2FzAyNXQTBNk7owkB59eFfoa62RgVRATyd9ZDlvnMSuMhJWXm60%2Bt%2F0A4HP2VU0YVfI7yZbSE7CHT6SNbhHDAxH2qBslC4n64bpeA%2FVSqktpp5iklxRQ27GO67ldpe57YhdCY6bSqKrIt78ay4GF5dCpWnghUgbx63rmbAP6%2FDK3ozE%2BY6oqhjFgsOALzEZD3xfJIFNjEFkX8lc3%2BY2DbsDIOWCPO%2FoPGwnQfPWBqEdZ6QCoom9dxI3x7toBWmERgL6yDTOIH0PfWCpODCiKr4y2xHo7CqNYVvWsc6KScoOD9zxjYXlaSogDxlaDlSmZeM5GO5aWwrw6NoTWvzs0V1ZNIhx4%2F31KsJ2PY5KNQwKmA77MhDuCvV568nQoO%2B8SioIr1%2FkWDkuT2UVe15Pfvp74LhGfKnkLUAqJtn9tHpU9zOZmUAitgtV2OoXTzzDX%2FIm9BjqkAQJggEVX8G2AcKoQQ%2BFiJcgf5XdKlNQK15uwYEq9Q1J6m7%2B65p73ap4Kq0%2FqpMBK4IKH04llceaJiV20x%2B8%2F%2BhMPvAA5j2yF0eu6g3lN6dENZeQRslJZQPQO%2BjteFmh0oMSrOKa%2BiAwN6b9lkVVbVEwqYNL%2F0m%2FgUlpJu8Q5XEC6L9bpkf4BWMur8KUilNHv2itMF%2BXF80MglB%2FyDZeZhuW4Rjxa&X-Amz-Signature=3470dd06b9361990b144a4d56167f5cf798cd075504ddd3aac662bfcec7a0e3b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2OKOHYT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCop2XwQrPZexTpdhebS9gGnhxuJcUjRYk9YIBk1y5nEgIhAK8SiVnBRaY%2Bq0dROxcPAtptCqcULS4KCaC8%2B2csDTj7Kv8DCDYQABoMNjM3NDIzMTgzODA1IgwgUJn8%2Ft6em8J9zIAq3AObKa9pEdxyTzEL0%2Fi2fuGD5LkcEdhfe3cdyII7W48TUHuZDsY2ABJ0n1tWY7bLjwsHSQvYMSulyw2obpbjYc7FAyFH64L2HF85Ka0UhHUCqRH1TwmBSLv5ZEdNHtVbIIaDYDatSTPb%2Bx0GhSApHzUKrtcGEeh%2FS4ggL0q7P%2BKHyXnDS3Exx4XlbxDMl2fInmYUcielv88sqX7%2BNjAxqRZ7kaA8S2Tn2DFsoWD82rxbaIyhI94AO%2BMDA%2BnfNmuYs18nRXMbezBmb4hbOsea0mn2vpEG1icBLdnuGeJb15ZxF1VM4PxEFaq%2FEJIg9GIy7BLtBKcR7gaRr29j00U3JXXlNTGvi1IqxGLZHg2xm%2FM3aavbPj2ed0Ru8h0Ko9bx4eL2RDHZqpWWxZjtfHb2mi2GQr%2B0JqV24pST9GuZw8ffOJbZUfhHgcABHTw%2BhZ1u9MVyOkpCgcUCLtKKb%2FOONwL8aO9ESx1e3n1%2F2%2FwEqzMCz%2BfWkUWPuuV7LU67msrThcL8KK7ND8NAd2ulWk6mD52mjuagLP5b2zWop0omUdQBBCTndlWt6wTrTQLvG7ZvJO3VjpCc%2BEaavBdCaUNF73RA8dD%2BCRUxAVptETm5oN7FDl%2FB5L83JwSOEhWDRjCN%2FYm9BjqkAZr9ZUrcFpc%2FCDdC%2BIFfGZDDbYNB%2BQZFgRwVDmvIWQmAmH%2FJI7c8qvZJ0cqwgO6qsTkPV8FsWG6SsBfTbJ2ks7WZh2YiRC%2BwLaehcUJxM5UAJ0LTkxaD3Wf1DkTL7%2FswhwyrcGcP0szTHns%2FkmNrg%2Bonyra75atgiq7XH3CDhuQrBPR4HHJ9Q%2F3zDEG0ePY1k%2BQmRdAQXC2xZoefBvNDXGDknMHH&X-Amz-Signature=39df10e521c837b1b3257aa747eda678f03b5013a1b376ca6c9d6230b9cfb505&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466377BJZLF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQDJedjh2fJrmRNN5XIDGoF9oB6lIgKFWVwdRA9BMbZsoAIhALth6RWa%2FFjcQNo2dp06kDs2xoe%2BUy9%2FuUO5jwB5YTBeKv8DCDYQABoMNjM3NDIzMTgzODA1Igxga6dziET0hYDZ%2FB0q3AMF3rkLz05Bng%2FHWP1lTl1XveJ6RdlkYNiJfKYmkSnyfNSvBE66%2BRcfLlso73FKCK1kWH9agCe8RwQDwcClY5eNXRBFYAawkNTnCQfoad9ophpaXc4O62b89hIZsMLIBSGzh5pbfs11V9FMPg1XtRaNFyGEv%2FTyWb0FlmnGXJR4J7hGjJIzwBwviHYjai%2B9jsxanLXDXENCKSG78i51XRov6e7RN3fu4XG268Eb68jn4kR9PTWao%2B3RqH62cG9V4vPNHCUU0PS9piEEcJaltI4Q8HByDuEbLFhzWrIMEsbRsApQ7IENDNMKJlzKjijOtA5Y%2BsaD%2FDEvfGqnJ4phW%2F13PEp%2BaRFG9FvRcEvw9i8JCfqnOf75hiOsrLrmCYRKkZ2ruEfTXIMUjy8aVfjYfjTXYPCYh4DcL1QXrmXTjCYbdbYndHhLqpuzQH9xsLgblAIdPGRG7lzbPvI4S8Ad7CanCib%2FD02VQ57PRLbPDNxisJLJts2K3hoto9T6GNkNwBNpHoFk7TbIpQH3dBxPLuvsMca2zDll1bryw2dukLuyWiVwAPXLmgLyHmuGzenTSJkrDEaJCifvZkGg0GcZgKSZi9lV%2F0k6ph%2B%2BtqclBHXtE1reTLOB5n5rIbKIgTCV%2FYm9BjqkATX1hzm3s9QCcLCmCk1Mlm8nvrDYbWy388s1GsNM2AxY1gIgzhbvAXrr1FcM1F0BMMb2c5CC343RKsICJ1kc6zXCWPAAyfoJKEB9rxVk8CuOayi1hvCv13sxK3IbArXBiLvYyirrmIi0Eyl2pM8W%2B%2B2z7jIgj7x9RIUjBlSuXvZfNYKzD%2FohUYNs394%2BmOuD7mF9yq%2FTWzz7XjvlQJwPf2Ivr8Xe&X-Amz-Signature=b1a64e007bbd219e8ba0c1bb516e0fc13199bf7b2fcf8ebc67c19f359ef3961c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664EOAXU5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIDWd9fdiv9FBxhSBuROEntKai9IpiSAF780wtZSE79DHAiAX%2FHPqK0TCkIcTFp4VTlnm47c2SGeEmsjNgSchtpzn8Cr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMa84yPtGIEpnakQeZKtwD%2FFIHO2KkiJamnFGA20mofSE4hZEr1%2Bu%2BZfRQOcAzNRx6i21v5CqF9r%2BB2y3eJzd9Lnuo7MJHch3OCLigSxV%2Bnq0CeSpUwfPEG4KB3BogCqaGU4faUe2CENSi5sASdsgwccfAFt5%2F4EBpPGvmi5GzhNRe3JrPA08xcCYeBH20zZDXw4vj1JMWPd41PZ72ZhVcie8VW%2Fff0KH7%2BAPV6IykZaWc1p809%2B6QDO1eItSLv8m4QqM55Dxo1tTJ9duS%2F2BmjEtq44%2FhfKAHr5dmfAvMHt%2Bb2amC4MqPjyfvVLUF4AZjr5q61qIhyrmCJDRgIs5bmcj8taJbTsPVZD8nkux7s1dxFZN%2Ff25lslWEIbVDvvUa78%2FBxoq%2Bv4P4V3jH8cnyxVZktl8CJtbqGeB6NNn%2FwtvkcofrEfnxzvCZFL9%2FwEEJjfKyjQcsSBFJhWsD0qyZ7z6A5GN9lyia6H97H%2F%2FNXH2OJj9FU2Ko3VHQCedbFw%2FTpkcOxFYVC5cxqBzIRdnoW440%2FISoMnTmzZf%2BXMJ8QFDyoRMIeo5RebasY07kO8ysbqMlhRxNgmKsiH%2BILKVetqCbghUNQJOyoRF%2FCv%2BdqnLltfT0SWkPBeV74d%2FqC3a0I%2BIpk0AUITYS9JAw4fyJvQY6pgGpmkLwuplwzc7R%2Bx8QrG6EdlZpFdtMiTngMdQ%2BpNwXTybUHZAwDCpOMDXMAij9TUQpvp6SL%2FiNgPGeO4GybjVuzL%2BUstBjPUS5ZbYbMz46dpG3XN1NIsojmXAPV1A6mGc9e1%2Ft2Cb0%2B7VRW45rb01JOE5fK%2B68gGLU62DYivbjCpWpu2QgFg0F3K4BkzN3nj5GBy4UQ%2Boc8Dyq4RXvw7PMsZ656KY3&X-Amz-Signature=7a2673b05e9b5737d9443a9779f703f6fd07e115863abaa5f25f0246ff151bfb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466556YWUNK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGwniJ8kXs9xncuP1vZvEZgP5CxkTsHPzSz4Kn%2BD33u0AiEA3aNCHWM2F36DqtkieAjhr%2Ba3ENGYxdCSDtksnrOHVGQq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDMCBlxTd4BGbp8xZcCrcA47pfwY6loJ5oGDxGiaJOoq8syF%2FJrUnl%2B30FdzSuBl9PY5dVv%2FCquHFe2KTCnnZdGj7OunLMBUfu7JkXSYRrOIJgKycTTvRGejsAEpxrrUk71NzW537%2Bbn0JsCD0WoKVtyi9J%2B%2F93xjEurI6YYFW%2BWMde%2BORnC1u2PcbcvfD6xD5jOhcYKdEAL6sdx4R1kBvNgAHhVTzwpkulq34xZ9P0I4FG5PF7pqXtzArgU%2Fj%2Fm8DvWyORLJmSa0QpPbeiYf8PwCT2O8i34ltnWg5UUs6wJikuveN2rWY3vA7j4U4vibl0Uuh%2BT5JjaSJW8mPMJ7W2fvViX7AjVTEudx%2BuJQahF0f4PbNZQcL093o9I5vOYB4tUNX9HsNMTIf55kxavciKKqfjU7E2Vj2JwcawNkzZxe%2BeLPXKoTlsP0HmBVvHP2GMfLXLhKM%2FIsaz81nqt%2BbnUYUTxlGivkm3bLp%2BoCIfh%2FPWDx4C5etzPeKEvT0LOLpOpHV9zc%2BHU6DI5UpI2LmJx4511hXjjE8dSE3vrZV0%2B625n6PpVM6Nabg5%2BoHDfg99sugy4qyRRac7DekPgLAoP%2F087mgyDBsriDNYog5wGBA3NcZL8A5G1AmZk03p1dvBfIvqrJ6zD95OB8MPj8ib0GOqUBCKJ8micEVKTGqmi1ky4Tq8nFpWsyOcXdUUar1bVtpmGI1eB6mqHUXIdFejkoYk4fg70I%2BC2DpZORSgqLFxlFAlC3GVq6a0qlgP2VUJQLJTr6UFsO226qO3btRT4L4gU3O3fqiqfC8zk2WiPP3kySUzPVlG9ucIpdbQR6Br57LKjdtXhDwdKtGjCc0Bx7VPvOnuG0KOSTcvyxSQIITnZINqfQCcq3&X-Amz-Signature=6822b0fc1b08e127cc1a7a54da60b27e3e2c36113e4873b070ec294a15f6fc7a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVQ4WYC5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCigj8q%2BLi%2FCy2Fg66La37tpA0UvnRRay4gxC%2F5FGJJoQIhAJH52jbIUsPfDMoj2J8foNj1aRlp429abJAvCLxSV2pqKv8DCDYQABoMNjM3NDIzMTgzODA1IgwMYd%2F1GO%2Fybb9L1Pgq3AO9yNhc0fjPlfJFBmrw1TCHTdV%2FqYxQc7TVEr43PKzrmSOKyVX3VLhG5QSCwasK4WQmnZfpBdEcn0NN%2FEZaWcwBVQfoU%2FjyI6zp7JVdZ0QGUcQUfADURtYKCHylcduo4EFEZMlMpC7yAMpLRe91HAd%2BUelWEDcgJA81hs6rPKjfbenvbnrWGFNXTcRFFouIiW%2BBKFI0uOWLlifQWCpz3VRnxxvIBJ4muQafYkVAgsFd9G%2FAauuPDgchNE2y7i%2FSA8VUwlYsROtd3GIiWuL4QvdTdmZ0lQPHTvEMQzdMSm5oh6ZTQAiVdhjv7VziQrRxZN04XGu0Au3bmIbY6VfPNBeYhkwmpPC3y6TkP2j82%2Bkd%2FjeXEkvmlcQDAs9q4CYPYLYMsLCWIg1xjgdZKUGbR35NS7c2dWgDnzcVir6h27Frn9Rl%2B3IdWw7%2FNHlYKAHy%2BMkUyLmiXr1M6wGzCF2Pa6Q0%2BRptyRRNlKreg9aDFLgb18BpoT9IkKqQhgx8ldGM9TKya3BUbKCnyixykCfsc6VtJA2B0gZECcgggaScw5D65QmufIpEDVnOip9axkU0NA6zF%2FnFgZNbfwIKLTmk76ofqRYlJ2xfNaaNM1C9V5BkUX6t5RW6PHVydsMByjDN%2FIm9BjqkASwtkqx8YCoaiBjXbD%2FVyRJH0l62BHqTvMla9ZbsUoVbs492BgOEV7RtXeNWMc3Xvan6Rm4cSv%2FN7BcSk%2F8fzz6wbV5wsTQ01qBiFy0OfGfFH3sgA7doGICP%2FgxM6kPLfnxWRof2e2OgQ0qMNnFufCIVXSf4i0SK8nMT1VLmRMbscxRpjUyCQQrjHzbbnOd1PK4uXF9GwjJcVnpG4oA%2FNh1WcxF2&X-Amz-Signature=813b7b73ecefd8b1146b6d727e317adbb47e25c10052837dc5a2e5c4984a7813&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWGPIZI6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQDSEOjJc7wYMv2oYwI67aii01EB4qcxjmoo29hbxqPHUgIgb4%2BNOvrpmpHSPXb5uC1gKWmoKbwPQNoxYe8VoV5ZDwgq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDJzKwM4wuVqf1OKEyircA2J%2B2K92O7QeKHmDhlhd36hxReHc2EE2yj8TlLvVfOod1TAwYQXwrt52123npv07XK2gnIYRs4MAwVlWjopi9CQ8Y7mqxSjYu2xuVFuVDzclHCSv%2Fbm32w6Vzb%2F1tkgRDhLhNhvivMKaGMTIXVX6cqfWB9Bu8EgAz47rDOLlapuTalfjkriXGIzASWCMQErSfcfx4IlU3Xe6hzCdIy2JkPSwAsCN2vAvWdAfFT1VSGKysUzNhAPTwm8owy6jS9YHZavu2Gsf14HbAP2zPiDpLfiJoXohTb0P2m6Bmz0uilx%2F02QTYyinEonG1P821CHdcaOIV1eW7f%2Bj9cAkResRatax72bqv415ccVM6z3FBI3RlhmlQZUDYE8SmPKmjZuTZKkZBYd7y0j5OO0rD7DQJCR27lD3vcmNNvFg8PmK79zy%2B8GsNob4dqUXcdkH9WH9%2B3Vi06PUzP27u58%2BzNa0W71doSiiV1TPsLUYyYMAYf2uBIlv0YerN66XKiB4e6KLzsmX4inBluKc%2Bs2Otjtl2cUvXoNimrqBDiSaKB4b1i%2Fv0O%2F3WvNp0X3cHrINE823yKZlATXT1ngq7gEt74VAJCVQtZvVAD%2FejSo311E9ZNkw6TK6naIhdKNCgplYMOn8ib0GOqUBi3R1V3lXQuYs1rxQjAM66NhQLISCSG2xTv%2BYegffeKFBB9sn6bFVrX5VnK127fI6jvqgx4LN3o7o5ucwMwM1BlHs5jvtIDMqPu1%2B%2FUu8cTT9tbHT5vpjONVVywUm9gdjey2exbEGsn%2BfT7bVm7MoA%2BMvyzhIh%2BRi8ns%2F65L497kDc2RsmqdzhoDcbHfrtn9z8aJ6suIHFjYVjX4Yp%2BGIoCVxBPcd&X-Amz-Signature=377c4863c00de173d3822e32eb9e5aaebb552e0c24301ff0646dac11e70cbede&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W65YX6B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIDNrjg0208lab3IcsMVVxqmM45cDB9aJVQgwm8Gvw%2B0eAiB5%2B6cBC0RZhH0c24u%2BjLMdICV8heMCfS%2Bvv0z4K3WZrir%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMmp%2BhM6E%2BHYm6wQx1KtwDTUROUMjKE6kUybat%2FtTi%2BDmsg5HGzM1LIWp1yQdI9Srip2v%2BALo2dZ3Mk%2FoWIzP7apnv2%2BYXIcHcNGHNF8aebc7T%2Bz2sVJUQ0ZRbMoDqlm6dz0kg3nnNJm7lg4V3VtdgZm3t%2BmfN3BtyDBl8VGYis3eRNs%2FC43PzN3FCF9pm47EP2B%2BA2zcJ9k6t33ISGq0OxCYKKpIDvnhnlv%2BzWejpxm%2BVaYBbXLdoG%2FDVEfB6KvZ9JzeY28DntT0BDAi%2FRL2aXfSHPgq15mnvvoKXww1QwfZgoezH9MUWe81HGnV%2BPvlf8kwbl0y2vOAUM%2BoaLoMDt%2FqxpBd2p1aUGArRDpNJrlmZ%2FnHTtpZelC2XiTNBCoAN6GvXK2hGe%2FBQPs5gAHOrXhMZHdCS4XsvYS38xCNIo5ur8uuinBQ%2BbLt8OQyYZuUxyUtFYN7bQ%2FndAHRJNuYR3Dw%2B3ZKi1vjcVlv52i6AC30iM01lMcJJcJ8fckQT9jLQD3YjDczlR0NFTugOfz3Z44rhS%2B6IgWNQzlhyw6ltcJRLT9DwxXgQO6ypYDhBDZah0400qttrZsnquuTxIY4%2FyWjJs3kyNLfj7TID5onwrW2ggibctvihMBjozXwpl2Utd%2FPwNy0SRPtrWW8wgv2JvQY6pgGQhHC5lRaUi%2BdfOZkFME7vAy%2BD2O2h%2FZ0NzZK7j44DqQfBT5LkvyYUe5Y1RVFoFsFKxLkjFMlseZqPLX47EvTWyC21IJaAGWtdBaYcaUfG8IiLwDpzWLFkZgu0eKvvPMDnBPxgnFi2mGx%2FGlr8MV1D7uMRdzuAWJiyEz72zhgaYd1QiHSVebEp2RTxRYuam2gCC4ATmoBgIvXhGcSRGeG1srSVO4jP&X-Amz-Signature=1fed52a659e0154ec02628a279ebf8b429a620414761dddd44ec165e77328d5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466556YWUNK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGwniJ8kXs9xncuP1vZvEZgP5CxkTsHPzSz4Kn%2BD33u0AiEA3aNCHWM2F36DqtkieAjhr%2Ba3ENGYxdCSDtksnrOHVGQq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDMCBlxTd4BGbp8xZcCrcA47pfwY6loJ5oGDxGiaJOoq8syF%2FJrUnl%2B30FdzSuBl9PY5dVv%2FCquHFe2KTCnnZdGj7OunLMBUfu7JkXSYRrOIJgKycTTvRGejsAEpxrrUk71NzW537%2Bbn0JsCD0WoKVtyi9J%2B%2F93xjEurI6YYFW%2BWMde%2BORnC1u2PcbcvfD6xD5jOhcYKdEAL6sdx4R1kBvNgAHhVTzwpkulq34xZ9P0I4FG5PF7pqXtzArgU%2Fj%2Fm8DvWyORLJmSa0QpPbeiYf8PwCT2O8i34ltnWg5UUs6wJikuveN2rWY3vA7j4U4vibl0Uuh%2BT5JjaSJW8mPMJ7W2fvViX7AjVTEudx%2BuJQahF0f4PbNZQcL093o9I5vOYB4tUNX9HsNMTIf55kxavciKKqfjU7E2Vj2JwcawNkzZxe%2BeLPXKoTlsP0HmBVvHP2GMfLXLhKM%2FIsaz81nqt%2BbnUYUTxlGivkm3bLp%2BoCIfh%2FPWDx4C5etzPeKEvT0LOLpOpHV9zc%2BHU6DI5UpI2LmJx4511hXjjE8dSE3vrZV0%2B625n6PpVM6Nabg5%2BoHDfg99sugy4qyRRac7DekPgLAoP%2F087mgyDBsriDNYog5wGBA3NcZL8A5G1AmZk03p1dvBfIvqrJ6zD95OB8MPj8ib0GOqUBCKJ8micEVKTGqmi1ky4Tq8nFpWsyOcXdUUar1bVtpmGI1eB6mqHUXIdFejkoYk4fg70I%2BC2DpZORSgqLFxlFAlC3GVq6a0qlgP2VUJQLJTr6UFsO226qO3btRT4L4gU3O3fqiqfC8zk2WiPP3kySUzPVlG9ucIpdbQR6Br57LKjdtXhDwdKtGjCc0Bx7VPvOnuG0KOSTcvyxSQIITnZINqfQCcq3&X-Amz-Signature=8b48f74e91bcaec8605f85bd2bbd61b242dca359e7e38d13fbcfb719c8fdb39e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYT5SJKR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIEGjXYGdTuyg9vUOAK%2FmRUY5cUMZiOkDvHoIyMFZ7CMvAiEAq9AAZuZTGX2GflnM%2BHrqj8dW9Cny6T8ptkyLMlRnHKYq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDJ9qbS2B79E95fURByrcA%2FhRC%2Ba8EH5SmWBh%2B2RbFu3zdrD4Xv3%2FdeiJyooyMPg3bZwzBg5YnZtIp9%2BqCFQvNmUzhJOvIOzehzldCKLO3jWItAnCbYWX8czP8gln%2BkADyySA0mTk0J7HVhEtrhrHKOaRvq5i%2BYhOYAmajOgpMrhZVK%2BrVtQNn3emqhFHQ3tmBSeiwNIV%2FBVpXXJ%2Bi1lRKDCe6TwpFGQn%2Fo9bHexvd94LPIsCr%2FRpiX1rdOSQ2bZ7Zwuj0lzTCyUGpsTxrhNkUJCI%2FZ1dKw7L2P1Nm8a3v6dXQbs5FSwStEoQUpMawQXTwnTPImsLjXp5QEsFJyBA1XePzrK%2B7pTp3XhKHa4yTgHIxE%2FoE6PZrZlgIzCQ2AAxOV7riqiSQeXfDkpnbLvv4820kxbXZVDZWLr1BywJCoK4pbIJ1y1p%2BpgckTiBAq49oTcRZ1RId2YdJC0cjUrN9EQREoeDZpnPIVPmA738%2FjbVcKekB5r%2BiezisMWWPc%2FzqHrmPBTlY1Nj6bWGf%2Bn5oOzVLQYKlMw9jH16QBgUPngt3ot%2B7MIFZqXwtkiCCRPZ26aKgKFPEuXkklEZuxNXozvx1bKmlPpoPfsF%2BvXCgP%2BEo3WTAuVoi37HMxFrspXTRiwO1Av3rwXyim8GMJP9ib0GOqUBKimM5E7A18iv%2B%2BBFpDDg9Ws1beHtBfJqqzJnV5FyzK%2F5JLM3WzUpX615PBtoilbNuqbDYTb7SGnkQYD6bsuh63HXZd9QSIT07tXcAmSLbJWST3JWFebO4qBYe%2BnSy0FC0ITPQm6o6zgQOI7DIR83QfqD%2FU2I%2FRhpQOngdVnFq57bGkUCrsSmphfVPnQKvBTjhIxqfroNPzWv13byH9vRoI0I%2FTTk&X-Amz-Signature=6f8311b41f51a81d8156729c98cea052409a33f0ca690f2b90400dafbbf9c107&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYT5SJKR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIEGjXYGdTuyg9vUOAK%2FmRUY5cUMZiOkDvHoIyMFZ7CMvAiEAq9AAZuZTGX2GflnM%2BHrqj8dW9Cny6T8ptkyLMlRnHKYq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDJ9qbS2B79E95fURByrcA%2FhRC%2Ba8EH5SmWBh%2B2RbFu3zdrD4Xv3%2FdeiJyooyMPg3bZwzBg5YnZtIp9%2BqCFQvNmUzhJOvIOzehzldCKLO3jWItAnCbYWX8czP8gln%2BkADyySA0mTk0J7HVhEtrhrHKOaRvq5i%2BYhOYAmajOgpMrhZVK%2BrVtQNn3emqhFHQ3tmBSeiwNIV%2FBVpXXJ%2Bi1lRKDCe6TwpFGQn%2Fo9bHexvd94LPIsCr%2FRpiX1rdOSQ2bZ7Zwuj0lzTCyUGpsTxrhNkUJCI%2FZ1dKw7L2P1Nm8a3v6dXQbs5FSwStEoQUpMawQXTwnTPImsLjXp5QEsFJyBA1XePzrK%2B7pTp3XhKHa4yTgHIxE%2FoE6PZrZlgIzCQ2AAxOV7riqiSQeXfDkpnbLvv4820kxbXZVDZWLr1BywJCoK4pbIJ1y1p%2BpgckTiBAq49oTcRZ1RId2YdJC0cjUrN9EQREoeDZpnPIVPmA738%2FjbVcKekB5r%2BiezisMWWPc%2FzqHrmPBTlY1Nj6bWGf%2Bn5oOzVLQYKlMw9jH16QBgUPngt3ot%2B7MIFZqXwtkiCCRPZ26aKgKFPEuXkklEZuxNXozvx1bKmlPpoPfsF%2BvXCgP%2BEo3WTAuVoi37HMxFrspXTRiwO1Av3rwXyim8GMJP9ib0GOqUBKimM5E7A18iv%2B%2BBFpDDg9Ws1beHtBfJqqzJnV5FyzK%2F5JLM3WzUpX615PBtoilbNuqbDYTb7SGnkQYD6bsuh63HXZd9QSIT07tXcAmSLbJWST3JWFebO4qBYe%2BnSy0FC0ITPQm6o6zgQOI7DIR83QfqD%2FU2I%2FRhpQOngdVnFq57bGkUCrsSmphfVPnQKvBTjhIxqfroNPzWv13byH9vRoI0I%2FTTk&X-Amz-Signature=ee16388cd91e1fc64ef7f869cdb45be3c2ac910c807c67920a052af9aca1cb73&X-Amz-SignedHeaders=host&x-id=GetObject)
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