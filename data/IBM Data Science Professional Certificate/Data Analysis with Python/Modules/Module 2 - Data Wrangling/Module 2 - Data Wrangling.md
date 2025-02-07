

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLL5GTKV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCNj5L7KNBYz2RgGDMH0qb%2BRdKm4Jfkp7tjOWgjpiyLwQIgP241w9bPLJHHwCaDJFxI%2BO1NwMDI51keoD9dqnU0LqAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDAgKOvIeiCFGilM80ircA6JrNn%2FQJFovm%2FcuiOhXsogli3v5%2F5FDi1rcjZoxNRgVsccvZ2uj9Tw6EOl2m%2BFrgfRwVUl8AI%2BbHYGrsP3qcapA0Gtk4eCEC9iaJFOqghOa3n7clYGDZQlUTIDt7hc6MhGaZofft26Iz8DosFMFUmtXHgIios7atTAyJvYJCxzht9Q9QVLxhsvgJZhDSvKr4q0ddMJmLJlwKaTeCMiCZuEaDVtPlDD0Q8WNwJHuIUJ%2BjBB6sTiujLt7Ew1vkPFEdtUULX%2Bp71hiEx5vDfJf7mVDPgqdS69Wc7sKa24fpTSq1E%2BoLH%2B%2BniDdpQuVxiOdvfl8aPCePmWR5bTJEeuzA8fFALspAyuGMIE%2F2Sfx%2BcFCmXoeSypX1siZP83DX4K5dkWkQ2FyVNfRihcoauae0OjX6%2BQdfBaphnsT5KJdYsAaIikfxVqcZbJ1LcBigIUFhgVTvMqGrkp6Twm78%2FPDkadRlfis%2B0OQve0x9D95eBYGCg6dwIDKSxfsFkp9vCo6ojQrlvOnxfzVKjVto4VMDMXYnuTqBjVOJR3cLYAzos9KvoqBs2Fwrej9bw5MtN5xRRQY9IpYM6V3xldNjJIdFdeYeF61y%2FMKfFMnzB1wswKhhwl6oEBinFbO0f3RMIX6lr0GOqUB3I3BR88K4XXOzcRQsantIpIb7yDnuUTv2N6%2FbDwosL5f%2BjB5GE%2Ftxa4R5M7ohjjZf7W8ezbpcIqfHoS59Yjpm5GVxjfZDgMiHGm%2BsZ772sDFF3zP%2BPz3%2FNrXx9o0OqrC5dDBr0GYFJPGlqvGqo6w%2BIHDBtRezI4mu4cH5pR32%2BxZPZuSwjLZNfKEWlXZ0gm48yPMyY9%2FdmwkXLLXV9jfOvgui0HI&X-Amz-Signature=0ef3d9f9a390bfae3feb0fbb69cd60be077c0a4b784fe91d0eceee68a2f46390&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJ4L3PXH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIASNKNFof3vUQqPKge%2FobV9XFAtwl9%2B%2BSnXFkB3Lj6VrAiB0GHZviiBq5EYrHrpMPq2dxVe%2ByGcRRCbqs9vDYllgDir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMYtqlIHK%2FiUhqukOJKtwDR3FbgyB19bZPggv7x%2FHJTK2rI%2FHuhCn%2FbmbtMcJF93M9yk204Q7OE51yTjdxiUmq2ceitG42P0e1qyhJbXSwrLPAll9Tf7N8oitPZYj%2BkeK0sfw5LEEUhubdW6dY5mbMnqUzqiJZxbrHse7B6qqR1MBMVvBVGNUhQ6g8iPgXSI323w%2F4GJzA3yHHwqEqfo5jEXbBpC5Lw%2FhbXMNtyjENU0xUalXCuCYsChTvtqtVioN9hNtGcSndAkyAHWJl%2BHR2T2M1W0v8j0MFu8b6xMt%2B2rDo%2FrAwS17H5%2F53%2F5JRgYaK1FatSnsS8kcUsatfpTCMdnn0k5mEgFkdygOWPKA7jatIlYR0Q510fxy2Wk13f8p%2FPbdp3JLP7nwxQrCR03KDMAhMrhM%2B91TYp9PfGF3dBG4D6VXMKx20B0rQt3VSKxxaV5EzGPPemHjnqnR4e3YsC2JwMS51xU1rnYk0iv2p0j%2BlyrITeY%2BNJe0XIlyF92Z651QiIjJREKotLGMM4wBlLtdcIxUlWiR5yICcLljFlbpz5wfJYYx4nSgQY4JlvA0%2BKs3%2FdKOop7MYh2h%2BGB8I%2BgA5bZFJOAWuYDgtb3fsCNIneNmvQpVMj7NSewfoamshcdu7tEWQ9PaLc9owm%2FqWvQY6pgEzjlHQhSjFK%2B8z59uvodVImcintLu2CYKQ0pjo6980flpT%2F8dj4fEb%2Bhr32A%2FexM1jU%2BqCw4qqShqY2aujHXeggMQGqwnpuQw5Z4WfB7IfkKFYGm3PjG0gYpsb4w4GhVTO13AZT1lLdKox6tdQ%2BJwHKbzBKu2o6SrDOj2t8OhJ%2B4cvdDZlR7Qu9OERz3l6qjfL0d7Syr9xd45%2BFlMaHpnkXAwITZgy&X-Amz-Signature=0196ea410c0317e74eddbe4f2f886452171bb4003e2d75bea40bb0a70f412e51&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW63JYY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQC3Qxa2y06YJE5OzomJntpCyA%2BM%2BIyiseuQuEhk5ZsMuwIhAI3NilstpetuFwHXH4e%2FkSbb2yZVZ7ueEky4y1AMSCi9Kv8DCHEQABoMNjM3NDIzMTgzODA1IgyCtUH2vEoAoEy2aYoq3APY4V1QaQvtSXxkw6z%2FmNhphYelLpIWsBB%2Bn%2FpIl3J1UyfhhE2n%2Bfx6agB%2FF9up2ILVD1T19Mk%2BjmdztlLUbP%2BDvMpAWCrPsAfoZo1oNvjxBOy%2BsF6AzdPTKgMb1pSk1IRi7W7K1iKf3bWXFclEC3wWpn9AX%2B50rGlXkqP9149oLMJ3NxLnT17xsEFstVgxMI%2FgnRDIoNy30SMcLGd3CA7Q46mKncPqvxk5tsr9weg3YSV6AZ1NmuO2zEqEeCEa1YQMRlg%2FXcsVkBtrbZ4YNkt0onJ9EmNPbInIdfOxpim%2FMB9u%2FB0njqFP4IG9OmWNHynZSNuuB7skvCN8Gae0LLuPIco70M9r7q4S4xV%2Bp4tWpDo8E29luTcp%2B8d0R%2BSHgUDb2JpSG6B2y81N5x0cyIMFBBjXNEMrIroltl9SnXCmtQWRpzQEtsPFarnzf3x72ZTrbo%2ByjmloPc5YF9T6ifmEBQQeUdPBWTNfdgEAngY7XXRXjF51aCDvxm0i1qLhTMRrrwQ5VXxe%2Fe1hTuxYedyv5xFBoQT0cz%2BYNrOtnkAkcSgFLl%2FxdVFQRudh3GY%2FZ%2FNEmSoo5WdmZVeVaAFe%2FeXa5f2Qg7ERi0kHfOf8w%2BN7mw1UvU7h1iaYc70UFTDN%2B5a9BjqkAZPOQ0UwzgXymXWHbkoQM0xnbAEYm2sQkZ79mJkYhFGZt9YDWzKrPyOXCx8deGWpJ3itoVkKc%2FWXBomDu1aU72zlI%2BoPMvBBvPPgefJjrNtm3yiDMOVS%2FPWS7SkkEEGQrKHm0E45eEKI3CgJAfjcuCZiLtyL9LkZllcVu6avIYDE78RZonchasF3cPpLN1mMmP%2FNOa6L7I8M2IvG8P89Xz8dOipI&X-Amz-Signature=98c05700842395a5aae1916ecf4680b554ab6654e16ded3acc89be835fb6b952&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLU35RXP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH58vfw2h%2BiA0I%2B9us6Ok4z%2F1esH9sXpvs915cNTjqznAiAGFx%2FtWaJFzaIGzJwV1nni5NF7sMhDHkBuiL6ArBfEaSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM04%2F6BgGajESdFWJuKtwDTHpmiWqRvFS%2F3n4Rb54i639GVQoJaGsJ8qvnZzKp7ZJm19IYzZ4PCly%2BZfoOj5GoQq0Y823QzwMkG5NjwvkPEIH%2FlFxRFtsl12%2BAa4iuzaE9awWDWBSZosoHgUVK9H1I6yWW0GQKVQLfaAKn1mydZ36BgErXXDS8MP2FKvjmvY4pGr2i8D53Ca5GgksAiS4czxcc%2Fh%2Fiafr4J%2FOuRGpmrlVHu6%2BIHX0SqeuO52Os0x8NnaSiHHn1KEiOswxKWPr60xISrEbACijtw8fyfTCs9xQkoAn95WyE2XTCyO6TDeYvUU%2BOLPKZeJnBjBSN5KOyqGmOyDqawycG0oGZsm%2BqPM5dQxY6rOPhnfJLZwCjqni7C9S%2Fx0Ghd3D1Z%2BUAwINTfJQ28IfP1hMp%2F5ILMx8XLCkmCuCugn26miFRd4EVgIXWkHc93WY1pidpGEr%2BIldxbWbU7VwfE2gcM2I46wM34toilwjBCOAOtso%2FKP6HJhn7ZWwqkDwSK6rMlTzzDVrDbNunm%2FouZQNWcpMT%2FU%2BvSLlWiBHSX1ofm8o8%2BAth%2FtItDP%2F3qJySjJhVPCyzQA%2Bp75mzw3Gx5MujXTXVsB41rlQJQsEKJw93kSraYDBa133LtdAVWZEWTtXu7Bgwy%2FmWvQY6pgEsCzXrTbMtEhu98bQYp4stzSqNdzhV4QRioUDCtZPHID5W0i38LUyponHgtooNWuh2zsp%2FOCa0AQBjP0UrSog%2FYN9N4CpdIX7j1Vq4%2F2knL%2F7uHOdzI7JRX4w1%2Fy3vgWJNvXd%2BOLB%2B9FttI5yIpKLPNjiWu8oz6s4mnTlqWNQx1%2Bwz1mapyB3su0ggUaloNR0oM%2BUMLxzDrVUxCWTY3YY1ggrJnxct&X-Amz-Signature=a8f1dfa6af260af78eb7f1798e6087eae491bc278ab2f6c99c00671a753137c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3DZC6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIA2TrdK1JInbVjaa0ciB3JiQdwzxI2RDaB%2Bz8Dmf1s5%2BAiAHlyASxGIhHE%2FACiCAoxER8bTj5zbQUw8l994sl0fdqir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9qem7ssNBwznLmEKKtwDBpeFGpYxxiwLTJkrdVIzvpMigfy67rCARmAm9K%2F2npdkxKDQqfiqMiT8PgyqWUYCvSjSrV1a%2FokB7asHdXpWVuYYSoc8dNnkyb3Wn3%2FQFSP4ls7Az%2FCzcZpMz4zAihT0tDF8nsXyHOTxnR75ax3TtWxy%2BLAb2mtHCSANDkcJj4md6EJksBU1T7L0N8QxdaWJ5%2BdikNTbP3qf1md4qvvTenJ0AprHRKrqT7U9PhPxYSL02vmbEPS3ADZKQ%2BQOIU%2B3kUECAU3AfxJeFTtLBJgQXI9q8fOsCSHH3Di87Og2WuxwRkK5DGjaq8jrnOzfFhD%2FHQGTriMSe7cIK4boQw7UDBs%2FAkLr5T9ZrmOXhEo5Ne4j8KKmLYlIeOJNRVnawu3r3LsgAhYF5O7RkOo0ksCtFVVy4i7JnYtqpuRkBSiWVqAk8Ht4Teld72xF8S06WYEzAAiQyRJWqR5bhOb7Tb3z03VnjWJox%2BzWQbjY6B1TB3On8rv6iVJ2PjRjagB5jtj6mQVihaJmSzwy2bRCicP7RAvA9hEjlE%2FZ48JgOb1M8OYgzN1AGy8dVxTalDxemasfQR4NI0xEkmpvJ35Cb4JWR5CRjGXPvKGG58bSHDniO6tKeexzURj%2BMCdi5HYw%2BPmWvQY6pgEW96sA7wAdM7JIMXFAkFxh6APnO0ciuZcRlnXwwlZNXkwgrjv9sgzghqFmbp8%2BBQWhqMVyEILTVGFcfEYB%2FRNr%2FEa%2BYE%2FKuz9keqDC9tW6TtMmMx75P7CGK5R25OiimUiQr0zYAvZtqi1%2FX2uw03A%2Bt%2BHLLrYDVQJhTFsqLrt0%2FFzxfS%2Bkd4GfM%2Fy65y3t4qnvvaGEgwtckUDOpmutk6NiGbD8bBRL&X-Amz-Signature=ac41ac229cfbe6c8c9a99a78253078a7ce612c50155f76a3cb063427736ca096&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627ELILNL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDsTBAEgsWjp8zwpS%2FgSECugZGny2VgbXvMxFExm8HndAIhAPVWKIwRKEC7IRrCq9cbmFwbYi0X1Lkmxvytexfh2x6iKv8DCHEQABoMNjM3NDIzMTgzODA1IgyxSQk60kzDv6HKnSIq3AMKFHWdVlrjFmFV3GoQJG9YZm5XGyQlkcS1e3uYkPq8gXFxbx0KGcOCI2GJnicXHobqAQ6qPxDADVnaIYjQCCKfOxbFKhBoRPq%2BUmJ1o99OMSmpu1JpWqEFiB73oWLD6k%2FVqQzD37yidfgO5Kdl0BYT3FAlaOgX3bJUJvdhmGYvl0KbFfe0EM7zc1Z9ilq0afO8L7Id1kZ1rlftOWru1tfw3EBMAuyEoBXtydbCNCX89isnuShoSJwoDlPDAc9E2zZg2pTy%2BRRuM9kdWBwbwOagYieVSO5XfLYX3V6iPdH4L08kpcjVoBOBXkHhdTqMza7gLPmiNqMJveazNXWpcwp%2Ba28j37zr3u3CAcq2obfqS1z2icWZxNlJ96zTmrE3rAYHi4KHFiyVZ%2FgXo4LPcQ%2F3D3qZBtanSwyVDqInvL9KqaPokUdz4Th%2BuCMZzfVXvwygjGFhN%2F%2BgE%2Fplhp0TwnGPnWg5bUPFQHZib3HmIPluymoOWtbMZ19YTDfxN0aGEZ3k73zXxtd3IFvmq96wfJvx9NHoeI3lwdWYNX9sJ%2BmszBIKRHE6oe%2B%2F0olxm3%2FF3IMZtC8NAH88LEEYekTWxZRI2uQ4fmRKzxWjXvqbUUVEkrDbmwTo8oXYdb0wqjC7%2BZa9BjqkAcUpSiv%2Fc4ztKGnCAVZl85GngSGn9GWGtpo0ArWxY%2FVWwF5jz4KBgWzqCyYozWzjBtpoMSl9F3sUFzsCEzSWjM8lF1rFV51EY4TJZ9brWFvwYh7DkgLmWg3z%2BSFiC97p1HMTk4CzaKx1VRGx%2FvJHxdinEdO5qd4NwFtkHPuE9EckTSGwHa2M0BoyGJUUcq7aTDcHSti3axsn%2BIQp9aM%2BIvI%2BViRN&X-Amz-Signature=990774291f04c71af8fd88ddb0edf07c240c494dfefbc349d5b761a23c69e286&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDAXG6ZE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDbtVqoshhX4qWFVQE52TVh6Tl7I8IQ29wmS17ugOiheAiAmvpKqUQ8EEfvGvX0TgMbwyxeXwPUM00ngpO8WeIgegSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMTw1JoRoWQLsV0aJBKtwDzeCimneEvSmNwkwO5a%2FOzTG0zvsGXruBPRY%2FIey8zcMqMDVL8REisQiRh5lAEx2rJvT3rwbPVxMi%2Bgj8y%2BiCAZPnM3ucbLH23o1Dv9WNjiN2zr6BIdwIXJ0XrueXEH%2FVqSbA6iuwvd3nI06Gf5mJ%2FKUjIY%2B8dL5l8xiFGHoEX9E199izDbNxpE4h%2BQ%2FVOxwUvzwkPfQAgnc66TPTtDoM%2FIxqURY07Ft45xvS2%2BYLl7EqXHFNVGPbshVVdht9ZktUDzmfwZ4WM3H4oDcPlUroYW2CoJzW7RVBWzOWfmhYHi41UICRaP7S%2Fhsp%2Bvl0BkUUYDuy3n6ctJekCWun82%2BrXoV0cIjZuhoauImyksrRhmbjy3yUGu7GbpPGa61BKYmBV0jkXsCLJviFeiGvIQPFr04v5IvYPCvVWiV5b9drxZRecAy3REtJodZrrrEafLWHAf4eywWOeNO4vPUQo8eb44LqHtam%2BNrb2%2BS6U2%2FbuZXgWrOxbIWAGXlaTT1rFCoGplQgD9EZ74dgpMekaejIjVvty0sGPD5%2Fd5uz%2FY0HzmloHfGiulnZkOQqtwCYUwNf%2FUqYSnuL8clsxpZq%2BEEdBy2oIY%2B0BEESx7odxHTQ2FEKnHpowqbO%2FuiOsCEwv%2FqWvQY6pgGy8Xt%2F0KcyhB%2BnEqsLAxfdUvWeBBTudiDGRByweq%2BkEIPBExKThPZjENLq4qaP8zS96bEBbxGNbgZjYAZXVGwyMbZUUT7fu35QmE%2FsmsgVBmCIcmsvjC2tfuWiMnwxpElOiDKsNvUQ7CVLvgF5WiEs02SbgPAQFiQOxsnl8sKxS2ZaqTY2ZlAluOZFtCYun9eWgVtHXekqguTbajZ%2BDGB2BsIvKLfE&X-Amz-Signature=40ab9dd2c0d0aeb65aeee1a243d30bf56aaacd1fd4bd993902486c5c305ee3b6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT4WSQXY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDiBoPq2aBDyJlXV506Q7jqjce%2B2HVERclSdCsSY4bV1gIhAIIW%2B8h0aEGHDFD8vZB4brFXT4wg86OpAbwlMKGcFf8ZKv8DCHEQABoMNjM3NDIzMTgzODA1IgxZJyWpOkXv9SbCEgwq3AMUdV4o8OvdtbU0n2j4etXESR0SktYgT9ESipqYTApbz%2BZcBiIO3IddqLl%2B8T%2BB6byMwsUtUg79eqvX0Ny9%2BaCHVOAkr15P8RP11c6ZH5YlmBYZKpVCPkWUs%2BvXFjPgX%2B5wNi8bC%2BiLBPYp2w3E2XNB4JRKnwMc5jf80%2B6xE8oYXlpAhwsin8OGYLD1tNHMDyerDDKfRgUEVu6YV0q7ocCfb7%2BOH7hQbCqHUS7THow8xR2HwSrdzz68%2BLc3gg9XUaAJ5F5FvYKYu2pp6aqEKzVRJTSrE636hvrk5lOLIDtnkGmMrCSxTuAcB%2F9Mt%2F91LF5TFvXm6XE5mkgdHABBf7fb7Hs5gkdvjlqMsC3f8%2F41gSNOFzzVJy0q3vt0f15%2FecFjLHV1dhJtv%2FCH%2BJwHHrJS6leZyMdzDA2JyoTyzFG2j7FgZzXRWJ3O5GDucGyWVsgDzulmq4D6dPvb1dbPMPOEZIk9hXdT4SrSkK%2FHYZ4%2FIci3cDWshVdumavwRXCQFa7oEB%2BRmlL10qPPI%2FRACUZacXDWnD6hWuOyBQ8BUeytV%2BZNq08vqUfrShoir69ytuJ8jE%2Bs1hKJ%2FmMEgWDpc1MOMgbhZyIhDMia4f4L0kl3nMj3mEaqu0sAIywB6jC%2F%2Bpa9BjqkAZP8DZmXJoH6Z5uSNS11Tvu8FJYjsGePSPoS8sTrscdtQb66ihf7L%2Bk3KnL%2F32c%2FCj02C25gPvucoNaCrULUjOfGh0pHEzFdhd1NzG4FjIJai9V5qJXmCBCj7OOzyMXS%2B0fVaY2jZgF%2Bib5RUYl5XAKDZlozqMMGkbdSaH3mRiZZta9XhODWvwo81%2Fuo495CzR9uOZ0gOVytd3e1kjbmDOo7sS3S&X-Amz-Signature=02cd409b8f020b8f4be144c0ddc7abaecdc54eab59a6f1aa9cf2287bc5373cf5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3DZC6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIA2TrdK1JInbVjaa0ciB3JiQdwzxI2RDaB%2Bz8Dmf1s5%2BAiAHlyASxGIhHE%2FACiCAoxER8bTj5zbQUw8l994sl0fdqir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9qem7ssNBwznLmEKKtwDBpeFGpYxxiwLTJkrdVIzvpMigfy67rCARmAm9K%2F2npdkxKDQqfiqMiT8PgyqWUYCvSjSrV1a%2FokB7asHdXpWVuYYSoc8dNnkyb3Wn3%2FQFSP4ls7Az%2FCzcZpMz4zAihT0tDF8nsXyHOTxnR75ax3TtWxy%2BLAb2mtHCSANDkcJj4md6EJksBU1T7L0N8QxdaWJ5%2BdikNTbP3qf1md4qvvTenJ0AprHRKrqT7U9PhPxYSL02vmbEPS3ADZKQ%2BQOIU%2B3kUECAU3AfxJeFTtLBJgQXI9q8fOsCSHH3Di87Og2WuxwRkK5DGjaq8jrnOzfFhD%2FHQGTriMSe7cIK4boQw7UDBs%2FAkLr5T9ZrmOXhEo5Ne4j8KKmLYlIeOJNRVnawu3r3LsgAhYF5O7RkOo0ksCtFVVy4i7JnYtqpuRkBSiWVqAk8Ht4Teld72xF8S06WYEzAAiQyRJWqR5bhOb7Tb3z03VnjWJox%2BzWQbjY6B1TB3On8rv6iVJ2PjRjagB5jtj6mQVihaJmSzwy2bRCicP7RAvA9hEjlE%2FZ48JgOb1M8OYgzN1AGy8dVxTalDxemasfQR4NI0xEkmpvJ35Cb4JWR5CRjGXPvKGG58bSHDniO6tKeexzURj%2BMCdi5HYw%2BPmWvQY6pgEW96sA7wAdM7JIMXFAkFxh6APnO0ciuZcRlnXwwlZNXkwgrjv9sgzghqFmbp8%2BBQWhqMVyEILTVGFcfEYB%2FRNr%2FEa%2BYE%2FKuz9keqDC9tW6TtMmMx75P7CGK5R25OiimUiQr0zYAvZtqi1%2FX2uw03A%2Bt%2BHLLrYDVQJhTFsqLrt0%2FFzxfS%2Bkd4GfM%2Fy65y3t4qnvvaGEgwtckUDOpmutk6NiGbD8bBRL&X-Amz-Signature=6c8590f76bf0d3f00d2429c282396aea0a11be3b67a85827d8ea8fe82ede1c80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GXWW7K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDbnFwTVrvIW%2FvlBMmv1%2B21QuFmolfJXmX0UoN4C%2BDHLQIhAITExLqZlDidacrZ562YYo%2FGaOKzbxSZqr5TUNHAfOzgKv8DCHEQABoMNjM3NDIzMTgzODA1Igwolv3FtzdEKh6cVVYq3APwUOXYF%2FMkJj%2Fc8SFMjXax1VT6%2BSsn3KlqsvHna%2F8U9o0ira%2F7SfA2CegKJw9gnLpdZ9rpA1rt0vIGLxkkWfouTpfRcg1JjVLFxxUhfntJ8dZKz135wk9pDkI0hFdl5RF0ZHnhV9dRnzoaLkCV6zVnt8VOeeB3293cHtsO0KpHrVuRKnLaICHJqAhTp3i8Y1qR0mlqgc4JInCGJxKj1WmC2Rp12KMjxENvfZqUON72jqOZJmmmU2e0HhDzzdeCCB00ECiq%2FJyGl636AR6cCP9P%2FSsVJQg19dImLwpXw2fk%2B40DaO6GH4QM10e0F5WnrSDDXAxHGuqbsJOOVebSiyb1CIJtf0v1REy%2BCx7D2ITDWwv0a%2FGiJeOa7pX4ek%2Fa6Csks%2BixQK3UU58Bz7%2FflIkWsP%2BV8GF%2BY%2F8NOnJab%2BdfawAQVrxQGIRtczhMqk%2FcHeXpFXRpk6GWK3weau1xvkEgEb4hAs3hV2Vy0b1PF%2BBwhBYHLFe2ne5KKEmobGUef3y%2B3gxpRFoDO4xNLJgEkUvakIPsHa2yuNqQErQlSsBl7MpT9gQnHkGX516B80PR4X%2BDn75mRZE3WvrAvvlk3vISTMxvaFFYSxuiiBQtvvDVO0R0yJLcJ%2B20I10MQDD4%2BZa9BjqkASRizhQsLr%2Fqr3D74QkOXfkWT8lAQUCoW%2Bq5jtY%2FwEm097b8WhjkVqDhI9lrX9Gk0R2Y9VU7E7q%2Fn0AnYTQxV17Cp%2FX%2Fox6%2BB30i5Bin96VKP6sR7nTB%2FtxT5VT9nvPihxzmyiAvNObHk004lY1xptZFvaNbgsn4HHFm%2FaXHa%2Fv1wIYgLPXgz0gdJdNTyA9qkNRblxlme7hwjMJMRRAyKcR%2BGsK4&X-Amz-Signature=5360fb8a974e9d8a915ef27d7e58c4eab7a0d2a863b17ea208986c30c8c7c8f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GXWW7K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDbnFwTVrvIW%2FvlBMmv1%2B21QuFmolfJXmX0UoN4C%2BDHLQIhAITExLqZlDidacrZ562YYo%2FGaOKzbxSZqr5TUNHAfOzgKv8DCHEQABoMNjM3NDIzMTgzODA1Igwolv3FtzdEKh6cVVYq3APwUOXYF%2FMkJj%2Fc8SFMjXax1VT6%2BSsn3KlqsvHna%2F8U9o0ira%2F7SfA2CegKJw9gnLpdZ9rpA1rt0vIGLxkkWfouTpfRcg1JjVLFxxUhfntJ8dZKz135wk9pDkI0hFdl5RF0ZHnhV9dRnzoaLkCV6zVnt8VOeeB3293cHtsO0KpHrVuRKnLaICHJqAhTp3i8Y1qR0mlqgc4JInCGJxKj1WmC2Rp12KMjxENvfZqUON72jqOZJmmmU2e0HhDzzdeCCB00ECiq%2FJyGl636AR6cCP9P%2FSsVJQg19dImLwpXw2fk%2B40DaO6GH4QM10e0F5WnrSDDXAxHGuqbsJOOVebSiyb1CIJtf0v1REy%2BCx7D2ITDWwv0a%2FGiJeOa7pX4ek%2Fa6Csks%2BixQK3UU58Bz7%2FflIkWsP%2BV8GF%2BY%2F8NOnJab%2BdfawAQVrxQGIRtczhMqk%2FcHeXpFXRpk6GWK3weau1xvkEgEb4hAs3hV2Vy0b1PF%2BBwhBYHLFe2ne5KKEmobGUef3y%2B3gxpRFoDO4xNLJgEkUvakIPsHa2yuNqQErQlSsBl7MpT9gQnHkGX516B80PR4X%2BDn75mRZE3WvrAvvlk3vISTMxvaFFYSxuiiBQtvvDVO0R0yJLcJ%2B20I10MQDD4%2BZa9BjqkASRizhQsLr%2Fqr3D74QkOXfkWT8lAQUCoW%2Bq5jtY%2FwEm097b8WhjkVqDhI9lrX9Gk0R2Y9VU7E7q%2Fn0AnYTQxV17Cp%2FX%2Fox6%2BB30i5Bin96VKP6sR7nTB%2FtxT5VT9nvPihxzmyiAvNObHk004lY1xptZFvaNbgsn4HHFm%2FaXHa%2Fv1wIYgLPXgz0gdJdNTyA9qkNRblxlme7hwjMJMRRAyKcR%2BGsK4&X-Amz-Signature=a61303624a02be6e6936604dc1119b3e13563ed18593aa6d324b92642c7dbcf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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