

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6OZWUCX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHqBplMVFCJBvP%2FhtJYV%2FH2CymUXBDKpabgcUdTwEGBWAiBEEc7Sfj%2BKQEiaAUs4qHxguwC9RC3NNjzl7kvtfIQfvyqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKrzQIMqJu%2FQA%2FUbaKtwDbVWtXHc6KwG6l2Z0C5kAw8m9oNOhmlIIPl%2Br0k7PZMWwXj6kxgIHfrFIPSyPnhBNRNxfv9gvkLWUlJhm%2F7MiKo5D7FSz7baSok0UkoMMRLHxjOUTYbJHTKepBZ48nUJPXyHrZOVoqyXk1bOZz%2FgeQ2wy7rZTPQSlxWJO9JelUvmwHBffcMBH4niLuvBHyYNwNXOPsso7ipKMRCXoKbVLwG1SG%2FcbikXxz07Xa5hsRVmI74tprRUHWtcg2Fm60QIuivraBhTXmtiVHvWpH3ciH3B%2BXXzy%2BXHQjH6XrfIzzfSg1%2FZDJigO8gRrHJi6a%2BTppE82JMhhY2WfjTGrS%2FhI7dbggOBHQu%2FRspCYokm1QcK9QDT%2Fk8OLjPJFocPy7o8jv53fVTkTqVN6bkHvU7MjF%2Bx8jQZqZo04DUtIJYd8CZT6e%2Fnsg6J5OTsZxYh4GaCGNbaOpGG%2FIeRw6CXtPb9llIBX%2Bs4DoBgNRdW0vWn1WKSnNR8QKuN0v8qaw2lVdEOqrWqng2xGF0L18lzKMPhz5gu1DAt4glV2kEcY375oq92A7jWL5Qyni%2FQM956P7dUzS%2BP%2BOHDxC1m6KdkDIkIh688B%2BwdrD9ICGj3v4NLXnn9aoKaemy%2BLWXlALWww1OrzvAY6pgGb%2F1TSIXA0dxBS%2FTqcqPCLdmmBxDUTOGxMibc0nxrVzz%2BdWFd0jobRPeTLpO5LFdefqV2r%2Fn%2FYlatt%2BM2%2BLgW9XBQ%2B1UjPQLPTCPhJxNmTaBKoMGKyI%2B2QYPEED43v35GsLnK0%2B%2FJq0JzGLWUchNA8ZTjsUnwMB7te2FqTNMI0O8Zedb9MIjdlehSYibJJpY6iazT1qBJYET%2BAlvuaIDKlDLXbFJON&X-Amz-Signature=d952fc6e14b71a2e0e31ced34529ec626a29e7700715a2c21b1958cbcbc39823&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKISI2GD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBUcwpEXrzWSY%2F4qBl6%2BoHpjx5EC%2BqZQrAhOuG5eX2C2AiEA6OoZF890JNCJz1y3C9u6MIJV4dIe0Prf7iDnYtLGtkYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjApLsryDhzKGAYwSrcA8J98w2Hp%2FF3%2BctNVwInj6Vcc%2FRd7iGOVJUM4D%2Fb4w%2F8Ut1meIJ%2FM93l0OB4ChgceaBDuS60ZvhAYiDpOXyn6o5nDNhnRyZZyIzx28cvBnnW4NlczhtkvC5BFWO3%2FJ9T3GeEjd8vQDzJ%2FEeoa9TSyOT8QI7owXzlkiCx34hXCrnzrJmlQ4ytL%2B5kjYqxn9xjbusFdF%2Flx8sZBLegWQjEhHi5rq3S8fuIpexOUTTt3GBQV1DwUcUy%2BR4jCrKFTQ0%2B2EdRW88f8nq3M%2F%2BgKqnXiBcsumJuZYhKz6%2FeFWtMQuW6wedUFmUA%2BDm8nU%2FXdRi8j9nY73ryVBTrezyTQStYq89lxdjk%2F8rP%2FzXnelauES3JMq5kFmr0cCOvojrClT5V6MBvI4f2Tm1tEV7KV34a44Iwl%2BbQy2gkOIZgneVxfypMmQ%2FJsa%2F8y0nvqVh38DNSPH0Uv%2Febl%2FPl3QSCLIFQWCQO64YGKchWLXb%2FIS8oan2vVxvXzcPRLDR8wfLCeQltN47TmylwhBExeB3D55Hysgtl28cDvRhdbVzOuwT3bxCKSZkrxJq5vdjAix8I3YyEmjVqtovKZ4QNXK6WwKj0Eib9PQxjvlfEJzsa0WLfYbq91sZ5b80OuLUQoMJ4MI3r87wGOqUBTvOiBH6Oxkd2asN%2BI%2BN86clpL3zXONSPMa%2FtInsRDNr0X0Kh%2FHgdGzHcnQp4kgtbZZQTkW8EU5U5h0V1gQnETu76%2B0gDrMxXDwqSVMs3%2BFMsGPFqImxpLdbUDL1kXVYTakKlSsqm63KWLM%2BxNJ5hSrIHMdkN4y4GRveW0dFPmOCX9lH5Ste%2Fo4pCjQ7iZjBAZbGs6dtkcW%2BCX9VkMHMYI4lEJ179&X-Amz-Signature=5f92ed2e6064cefca6ca1b6a497bfa5551b9899368ad1fc1fee3fac4da6c132d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3MGRHYK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGuBCVn9DJoxVyf3%2FYNlGy5ml1baxSYBL8HH3EvVsLDYAiEA7i8Wo0E3GIwKwCFNEbqPqB1IAHCPKBKoG3b5rBpEg7wqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEawC8iX499tAk9vESrcA5rdRzdR%2FFPGKWBlCoFba83yAvyGWHaE0GmqnC4g7BAM72Ic2WwJYoIPo%2FTgGZnmni4BcGF2TLNm7AAM8vpAPobIWTeA8XpJ75QrfYP4FMi%2BtxIlG%2BXuqiUnHL5d%2FkrySILSMd07GNe59wdwwZb3HotP0gPiIUGO%2FEAqubFX%2BIecdVReOO9O9mkP4u%2FkUuUv4lAzJt55ipPMahLUhqI43EbWUZZvCG0vJ2ewZ88M687yY77BDlCAcCuIJyZwYFAOiIFkk2Qe7E0tbh%2BJg8vdQEDoVu0FqgR5CTuL7CHHnY4vX296tgeQ3J4bSq9DUchI2fqM%2FiOQd3l07ic6Wstw1X6ecXHmgv%2F3AVmMuuJAugD6NOaWdF6g7LhyfTs4u5gzFqHHg9C3Vg1hzpgtnOiKs9uhiO2duBY3hSZNtp5HMLABxfWIWbk4fhjQI7zAQ4Eh1u1dvQKClgCrhVE0bY8Dj%2FUjNSzPNGv09bNUVKCqhjef8HCv7KYoJLW91bSg6PPwvAroed2kXf6Xz3oZ%2FVXNPIvyKJr5hQtuUwpVPsK06eOd69VYRfLgcZWXDUKBuOGy6NpV2rMdixu397ibn1fe1Qo6GhAh0psbeF1hIqT%2FQqu%2FSKJkmaHRMpMg9sk2MJrr87wGOqUBWetLFeCb2QftBlJJwFjN%2FJRwUUkWg7aIz7kU0moFyYPjX38NvWxmB09XWmPYPlD21Ab7vNpo%2BzuQL%2BqMnJiiyQ3WANhk8P5H0fEOavwgmKPJIWsKCWTvnPnxaWZbV1iqW2R5FAEIMvuUlqNb0peOTCbaAqf4VZeaeryHdDPNy1OFXPzySkC%2FecpRd151zwhxNnDAQFVXC9%2BVtLx8JaSrY1SnKS%2Fw&X-Amz-Signature=0dc67c415827f5896fe88d91c3e1cd99b4ceab8bffba84d8321afe932157f04e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WPXJMQF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTkjYcAiT%2B7wdKvwlfGE9RS0IUrubEA3pzDM4yXxVgsAIhAMHvdfii3TDKHxjguVVHoSX8g6kNiVbcCyuYkVjsndwXKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgztic7SsCWMuurLcq3AO%2FFNDNuPEGwQ3RBzaZpbEflVNgNq%2FlFQpdKtafoOSN1Ps1jG3%2FaY8AGT2dqlT9wRs4ZnqdYgA%2FiNXkndZ0vuTju41SLRng9fIzMXL4P%2FGS1n6Jg0XoXO9zbF%2Fdl7aRA2%2B%2BHyuGVgNg3DdBQtSpRLsI7PDoXBmvXizoq8Mt8k%2Bi5V46LC2dz6Tyi9bkm4DXYhVPG6rBBAikxY%2F%2B%2FiWyI5yfocpFrUJeYfgr60d4JrjiiuMe4%2B6m9wXpamDyt7Fl8NPRjDPEZPwMLSDCbF1%2FcDgCK8qnyPweND%2Fw%2FuVspfT3wJ8hkFffizT3x8glQWHJvdI69nkFiqPrfZHxKngMskxOfbJekpmdPjVI2QACYbWHe%2Bu1fVR5V3iWsYNxsI11uBhKyQmr7w2W528MkrWlqeOoErFxJ79nIfGQ28xz0K3akSNmXNzU191VCglkQDge0veetyWVKeADW9SuVTsKP12SN0A0FtMg95vTjewO0cX6u8HzhW5NIs5aO9rvxtCW1vWRaSSxswayKQLFKZ3DFTAwTQBfcjD3q2CNBKzJVYN4z3dkaGlf7kuf%2FPQeLsUuE0p4MsRdnSYxTAJZEzZXFGluioQDRBJFvU1K%2FVnvgT1224vNsP%2BFh9fvA8mo%2FDDWh%2FS8BjqkAYDaY4VsqTcak8NW7rdTBMSYQEM9pV7et5CynfFIyfGb93XlLtmCTZ9oFA7OxlvFthjwcsi32SCUdEs245EySHmUaZHkx%2F7bg6ZD4hMbe%2FXvFzihvhs0tDcAAdaa0xAfyse%2FaWa3e6i4kaXZNU%2B6Jvxz%2FR%2Foqlizqvi2MB9DbIBQvo3XK3ywCVvtYQ6bVmbHSixuXrJIpHf9RWC0YNJODuTtB2mk&X-Amz-Signature=070805a319f93d814fc209be59d78920e9fc4a6ff214f920ff450b587cbd9712&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UEBROJK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUSD6U%2FSNczRpLuK3V8Wrer8yj9HjKelfrDi4uyQq8wIgAucLiqmJ9AmdbESm5D8zq%2FWbd39q8kPXyygQD2NnLMkqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNruezmSrpBjUFMHgyrcA%2Bb17GVgwASfcGlxbdc5RVrGk7xpmPIrrfuHC%2B4g0gcZrbi1qE0Ku9iIw65dZmEk6ENq0dbOqG9adPFo%2Bk0TxOVCQjhxdwkhWThZ52%2B3%2FHAl8OcplKQy8cXbomh07Wqg12SxVbkuYhn5KeUBlrlGIUzSPoNIbA5quzAv1y9OPDNL%2FzPYz3gGRHAs%2B5QMblgZo8pI%2B6l44%2BjkA4UMwZLXwsJuktBhfuoxQsRXpp8KuFOEiyDbkoTzSZiEkM8lYPQNoEXZ%2B82XNbdxwCecBFpEJJvEsVG4WmRCwfre4ok7FwVenGAqDAW7ZpCt%2FhQiFfqMhcqxyP47dP2p0DSA2aUUgy0Y%2FsMxgCSPjuwp4heLdkWBzK31aZOo9EkTwiYPyFps7UFhV8QfxzY5F5yRmyA09OXqyJvW%2Bsqqz5cWqPL3%2FXvTxfvysD%2F4nUWyCiM8aYSEarekJSlzZAhhWLFYiqAuWLoxUM8vOaiC0jcr7PECUjEEi4u2NMG4Rw3PVqwk9aKKaivfQ%2FYMcLB%2FfvXLudQvd0awp2rSJYhas6kRCCE8la1sJA30VX%2FXpWDOpAJqUxwF513JWzDQ%2FJXujZF67QIRg0R2oNIf59OEneODA0WxyV6x7wvuY0JD6qtuXJzEMOaH9LwGOqUBj5ObF15OH9%2FSmrsVB8uv9F03VdV3zzEmCfv4j5pcLUOE7Yl2OAjfAS19R%2FogGExMEONTBeudko1blp2M%2FHdbgTX1lbwvf0Hq2ZHbz%2BZ%2FoNpeXz%2FPBv9cRROYXo672LA7yQjdWT1zaIH33q2y0nyygUC3ZRpK4aeKB3fvGgE27ux%2F1O6TjHQT68hqVREj43cTvcLa9b4VJe%2Fv18D3ZaJjOZrrSaBv&X-Amz-Signature=3dab69cca565a1b6985ee51a27411243ed9764ab1ac7af6b407d0918897d76eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2W3K3XV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIw7NLtcyDTA4zvVZDZbyIGAFeGoib8KQw1epR2OgowgIgX8emJjMIb0WwW6hvSD6jU%2FHOZ3g%2F8Spwdf4S13xYHrwqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNSZBNYvbQ%2BcuXKGSrcA%2F99RnrtmhvrvLWtFnTHTKjV%2BcaZrbcVdbUYOT7uQjreu2cd58OCxr6cOFDJxBcxA7lK4yU%2BaO1B1ev%2FWTQPLImCGZVECjjhA5G2F3JImvmxzx4eXgUFOZTqdC7fxlMOMlBJw5%2FYtXzXYKCG%2B8h9uBKpjwQ7LOHkiG2RTRMGgkWhY9BZ2dCacv0Td6UqrpTtZACIFCTD9uMHMpDyvN6NbxjgMI6f1tT1KY0TXXxEaocVoU9r9m7Bo%2B8e8z5iJwsp3w6gKCCyUTJMMvfFKHpMLDyJaYVuwHCWDjVC0hUkr7zo8spotNPuKKOLXpj%2F9UJ6yokQurOi40xDzFtjpg3sk88Dqe3jUeC%2FNtdN4E4rGXwFpp5h%2FJui9NajESa%2Buier8wdKxXPQBAFxMkkhqSbmPdPnSBOagFrvb45kruRSeUHkdOwRcRly8cEULjzxDGzNmXPRTDfkp4zdNY5qd436Oq6%2FUOjqEcwshlEdtcqW8viFn8rDZHTNtNYqElHyGUzepPRCzej%2FP1xPpXKADnwneUlkpyXwnPPmkFgv7tJ%2FDqHIhqBmOcH49uKmesmN8N5ar%2FWE1SCVSN%2F0GT9sZhLDNpXJEwvgF%2FnazhZOMjlqu8yQsWvTCDeT83N3v8DnMIbr87wGOqUBPpBcP%2FOJWMXmmOto1gYAjXBzM5Q9Qr8t%2Boh4L%2FMnIlRt1YkT8zIHF%2FBI80fjSOf49V%2FGHGFQ33Od5cH4o2Ai5Ie2zB9%2FCKnPEPxWnLBmrEO%2FkWVzxIvlTx954BAzgw3a7COULJoD7HHk3YLiaq0gykdUW1Sssvy6WK9eGOvm5zGtnXmK0nl2OPTIE63iWDxckh0U6LP%2BILwZ4w3iaRtdYIqUGlIO&X-Amz-Signature=424acd73ac652f03f4acd9aa7887dcc8f6fe4ccd9b967ec08b97e401a92d7a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK5IHYBA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoZc8THRyK0T6WUwzgqoZ%2B9qOyrHlwoZUrXcCyZOqGWAiEAgT9NNMAI%2F2ApUwaH%2F9xXCsXL4B9euLGqdqzdTKYQxyoqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOokYdRy7MsWiUU2TyrcA8%2Flfd67BOazyTpZPCxLXrozXKUr3Ud3M9w%2F3P0N%2F0ucO4a5aAEHS3YtecdjSIdWkDfLf4U7IXQ2hK9SJbRxuQfwyBMkia8u5C9H0QpSkKLrTYVCnJSngTCTZB51CjJLVXfeM1p47wHOt0HvSsF7Ll%2FS4LluMlKMxVX3h9qF%2Fbbre75t4Y%2BpqkSsj1hZfIPQRF2GyqNEhRfP6wTdmv9H35nKvCo%2BUHYoEcKHqI3wx8%2BiIW%2FDEIBHibp%2BwIyp5PEsZFltlmPG8mjoJfXuQ%2FIEMjKDtEueNft%2BNU86SR4FlcZJjQbc%2Bi2%2FltEEJ1FqHH%2Bcuezje%2BawBirom6U5bL6nFyMVih4X0DZdCtlxYR9jdPA65vGBMepCM%2BYhlPBd64rsn%2BsA%2FeGeRvmUqBd3qVLiyFo0xXsJ6%2F68WYzN%2BqGBD%2BBlsnjO7NMf%2F%2FiS80hwZTc%2BQCemAhgWzqFwD6AYVFNBH2R%2FGg6qqhPA%2BclF%2FwECralOAlpK888muILHu0cD6trT5%2FnDnTo%2Bb7VY8LLAJ80mFIV1Em0LG2Px6arziWlVI5xZx809qdNP7q43s9CP9rWe%2FN3VZKLF9qTQaAfTmUxEEhrjRGIfILueiEAtjzKkrkrkUT2ILfUFrTFddxPnMOTq87wGOqUBoz2KCNv%2BmQIgKTKUfRNmhrE8%2FOtBYgc90UdOrCn2FORoM3%2BA9jmzlUNl5Rg%2FqW19TO5CMyRCvaW3CQeX12BRpVHZb0MLZiqWyMQXQnT0zSkx4NZ0xg49EoQVegmOfDwt3F5EfI4Wrk8rV91HUd2HDy6ZxAC6wt8sLyQK%2BPNF8pKVZLV2jNpDxLfdzzpwJQnuD1%2Fj8s9G%2FDVMx06Y52tAoSdbbLxI&X-Amz-Signature=0f58a34085c7f656f9427826ccdbb086f9b9235dc457c068938ba85c404ac314&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LBJMCQZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHjab1eAA%2Fv1UvFoZ7ZXC2cb9QqsMBATq9aGZ6CSjI6AiEA9oEbsN1MB4MX0eYr1B%2F%2FlAB0X2SMn0QuTz%2BQPXqHKi4qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAvqcnA7nNm2e6L%2B1SrcA3z%2FTxO0Oy%2FLsqXw%2F0Np0OKBtpzGgs7fs4%2FLouRu1yPvQXc%2FlinxKQBo3ZlHB7xm6L9TBHobfccV5A%2Fil0gOjImM7Y%2FcjbduIcDIOjhGXeAuEuXiXKwY1QmRkGpUQtoyUDBhYmWt%2F9DyQZrhVejROGOLkmC7aavqeqJglHyxRN5cFEffEq%2BOJQVko8f0VR6Ez6qODMe7Tdu%2BYo%2Brxb92Fh18DasCDf5tXzIukCgqvrlfa1nNDhDjlrVy%2B1nJjOs2uOd8qGSfphOz6sJUptsoaHIEXiRBFT3quEWU%2BQUGD9WOy5%2F%2Fm3j6Zd0qTHcjh712L%2F%2FnqpW9V7G%2FOn5JHj%2FPFpwfjFZ0sKvAND0KNozj0gDRHSfaaEkY3CUhUS5q6h0l0rjQmREzA%2BDisVctq%2B0ING6jgdrOMfjILqvHMoRLNeuAMwYSRcFqSV2KWMy6gethabOhDjq1YDsLewsPVFdeSjyqIZeCU06%2FI5lAyiMTuq5naRZEDkTIrUxL1UY3pgfZEM8bw4gudFS66yJo8LXkcdUzUuDwkcVdrXW6HrtYhb7By9S8SrcSPOI%2B2wGy0e%2BRwUoKNWb9pe73TV3viFqCGAcRS77vPO5VmKQ7HN6boHwEikoNntMAT5K1jTLWMOSH9LwGOqUBwgSUE6ISe5Xhvk8nuW21bGTQYlmQDxcdRrux5FAMG1nTlA9m4WFP%2FfBMfEiU1smSbsAnF8HBMcYFH1OaCsG69ZpfEkzGzMf7PvF49pDRTSxjq%2B3P6LcpjT%2B6zeWv0l7LKL6vqljAR6YMIMZOijosm4sbhwd0DDioWBEkJwnpNhU%2FPOedBbpTKngHqAyTHBcN6x%2BYXEz7a2UQkriClerkgedmaefp&X-Amz-Signature=46b936e014640c63d20ea037767cf341a042669e44dc1287e09ba08e7747045c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UEBROJK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFUSD6U%2FSNczRpLuK3V8Wrer8yj9HjKelfrDi4uyQq8wIgAucLiqmJ9AmdbESm5D8zq%2FWbd39q8kPXyygQD2NnLMkqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNruezmSrpBjUFMHgyrcA%2Bb17GVgwASfcGlxbdc5RVrGk7xpmPIrrfuHC%2B4g0gcZrbi1qE0Ku9iIw65dZmEk6ENq0dbOqG9adPFo%2Bk0TxOVCQjhxdwkhWThZ52%2B3%2FHAl8OcplKQy8cXbomh07Wqg12SxVbkuYhn5KeUBlrlGIUzSPoNIbA5quzAv1y9OPDNL%2FzPYz3gGRHAs%2B5QMblgZo8pI%2B6l44%2BjkA4UMwZLXwsJuktBhfuoxQsRXpp8KuFOEiyDbkoTzSZiEkM8lYPQNoEXZ%2B82XNbdxwCecBFpEJJvEsVG4WmRCwfre4ok7FwVenGAqDAW7ZpCt%2FhQiFfqMhcqxyP47dP2p0DSA2aUUgy0Y%2FsMxgCSPjuwp4heLdkWBzK31aZOo9EkTwiYPyFps7UFhV8QfxzY5F5yRmyA09OXqyJvW%2Bsqqz5cWqPL3%2FXvTxfvysD%2F4nUWyCiM8aYSEarekJSlzZAhhWLFYiqAuWLoxUM8vOaiC0jcr7PECUjEEi4u2NMG4Rw3PVqwk9aKKaivfQ%2FYMcLB%2FfvXLudQvd0awp2rSJYhas6kRCCE8la1sJA30VX%2FXpWDOpAJqUxwF513JWzDQ%2FJXujZF67QIRg0R2oNIf59OEneODA0WxyV6x7wvuY0JD6qtuXJzEMOaH9LwGOqUBj5ObF15OH9%2FSmrsVB8uv9F03VdV3zzEmCfv4j5pcLUOE7Yl2OAjfAS19R%2FogGExMEONTBeudko1blp2M%2FHdbgTX1lbwvf0Hq2ZHbz%2BZ%2FoNpeXz%2FPBv9cRROYXo672LA7yQjdWT1zaIH33q2y0nyygUC3ZRpK4aeKB3fvGgE27ux%2F1O6TjHQT68hqVREj43cTvcLa9b4VJe%2Fv18D3ZaJjOZrrSaBv&X-Amz-Signature=0bf5a2b7d7958377d7fab647ea8455353b172411390d2b9e68a55b08aa90291d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NADD2EU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCnW8KWP1KfZMtgkmF4iCUn%2BOnhoj5wJXNyGjHHXBAvAiBO4zGAURisIOyNfRT5frWRNZA5mfwn39Ff3OO9mDIZ6SqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpdE%2FLHE941FlryiiKtwDFVJZ5lvmQbM0tMHvQKau24bpndVzPnq1HLaZkAXAgw1b%2Be84UREAA3kctoDuA%2BVxJsgYzoNJlBripvylQN9vWisrD62%2FIZU3cxGkpw4ES6X%2F%2B5QUKs0Qenjc5ekcXstOUqnlnJpOClgkPWYo3b1ATIsfgwwLhOg1KXyt%2B2ICSvyLaDb4On8AXdrTF%2Bg3g8Erlnph4NSCJXOxm7b63iQGt9XJWaik20AWygYVTstJYVbbKx8wXP0kI6foMx22Zqv62fMHicawGeC2Ye2lFNOL%2B%2FhhAk4GUgexvNsp20FsOnH2%2BQaXtkUYAu%2B%2BhhcPV%2Bv0nW6WAAXB%2F%2Bzqfk5HZm5TmxIdFHqdBvOd1LrkZBOCjdXfHUBZbRZtlCpdW70vdSSKUSLRsVcIkfgfmpz5czbM%2ByL9RPD5Q%2FDIHJGG7BHiY1HdhdmOpXYufGQlR6Ue5TU%2Fa2PD1J3o7OD0mVshrnHQ5MXke1E1aK9vA5qbhNNRH9Om7Zwh9mbH9Fs3Nu9jy%2F%2BsKYSaCBTBsjNgr132hPNVV8LOTKOOB7FnpHR2vmdPv0V0Tra3ifC32I%2BYXnNsSLPDGoJ1oZ%2FU%2F8BGRysBUGVe11VI1oArz5sJCqonVyQfCROWHIio5pl7WL79DyUw5of0vAY6pgGr4oG97HFj%2FX%2BAp3%2FT871l%2FfEYwoIpOvi5waNaHpEXJyyp28cRRD82vn0dbd3GFDg4qAXZchfk76FOq9ICyreVsHF80tZhI1f9Ki1QsKPLHAJ0IhaDzixeJRXcNixr%2FYk3BJVVfSGsPJOrw0VcEdl9TUCFbdm1lsVsOZGqSOIRWVlCL9geOhUTHFrFByTR6xClb1upjfC3iK6ZNHguzGFcnXiaG0o3&X-Amz-Signature=a59abc1c8dc207558ebca752355e4ba6e4bb62b668e65a8630d04689b7c2c3ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NADD2EU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCnW8KWP1KfZMtgkmF4iCUn%2BOnhoj5wJXNyGjHHXBAvAiBO4zGAURisIOyNfRT5frWRNZA5mfwn39Ff3OO9mDIZ6SqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpdE%2FLHE941FlryiiKtwDFVJZ5lvmQbM0tMHvQKau24bpndVzPnq1HLaZkAXAgw1b%2Be84UREAA3kctoDuA%2BVxJsgYzoNJlBripvylQN9vWisrD62%2FIZU3cxGkpw4ES6X%2F%2B5QUKs0Qenjc5ekcXstOUqnlnJpOClgkPWYo3b1ATIsfgwwLhOg1KXyt%2B2ICSvyLaDb4On8AXdrTF%2Bg3g8Erlnph4NSCJXOxm7b63iQGt9XJWaik20AWygYVTstJYVbbKx8wXP0kI6foMx22Zqv62fMHicawGeC2Ye2lFNOL%2B%2FhhAk4GUgexvNsp20FsOnH2%2BQaXtkUYAu%2B%2BhhcPV%2Bv0nW6WAAXB%2F%2Bzqfk5HZm5TmxIdFHqdBvOd1LrkZBOCjdXfHUBZbRZtlCpdW70vdSSKUSLRsVcIkfgfmpz5czbM%2ByL9RPD5Q%2FDIHJGG7BHiY1HdhdmOpXYufGQlR6Ue5TU%2Fa2PD1J3o7OD0mVshrnHQ5MXke1E1aK9vA5qbhNNRH9Om7Zwh9mbH9Fs3Nu9jy%2F%2BsKYSaCBTBsjNgr132hPNVV8LOTKOOB7FnpHR2vmdPv0V0Tra3ifC32I%2BYXnNsSLPDGoJ1oZ%2FU%2F8BGRysBUGVe11VI1oArz5sJCqonVyQfCROWHIio5pl7WL79DyUw5of0vAY6pgGr4oG97HFj%2FX%2BAp3%2FT871l%2FfEYwoIpOvi5waNaHpEXJyyp28cRRD82vn0dbd3GFDg4qAXZchfk76FOq9ICyreVsHF80tZhI1f9Ki1QsKPLHAJ0IhaDzixeJRXcNixr%2FYk3BJVVfSGsPJOrw0VcEdl9TUCFbdm1lsVsOZGqSOIRWVlCL9geOhUTHFrFByTR6xClb1upjfC3iK6ZNHguzGFcnXiaG0o3&X-Amz-Signature=3f16ae0363a6e3a5288fc78d30be0ef2d4156ec125652f5db592c4059618fac7&X-Amz-SignedHeaders=host&x-id=GetObject)
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