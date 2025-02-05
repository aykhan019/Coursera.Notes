

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XAZIJDH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDTFB4x4IO8B7QkRg0veiDuWh6zaMMhKnJgDQB4%2FssdDAIhAPjHgLZ6sB9Bpw%2FOBDqVGXDrJPCK0wOI24%2BmT8RJoiCFKv8DCEoQABoMNjM3NDIzMTgzODA1IgwJesTbklAVhg4Hppkq3AM3hO%2FAJYQUzOMnNalWiUWnXJ%2FQhm9cBCHd%2FUS0sACneSx2Jn0erJkjzOHmav18wKhkcuqDVowwsoYY1FPivZ24OVeXaoFPhvS1DlkcNbv8Tj47zB2dZSZh8zoRFnIFWDpsGUbyYMySH6GkwKGmVKaCaIHA4pXSzxFb0%2Fp%2B7SesaySMMwpViKpTYrc8j8LVNdXgdNubTY7vEOkDLPcQAmi2XknSpD%2Fwl%2B3eVD4qCu9wtWdtkqwZKCnLE2kXsctrKRtRAHPHYu4j9aw0OiEijGBEA1dgAN0P7VeCNE4esfi5y4liGDSbfRUGx22xI8bY85fbwNnqHrWgIIy0aUF8DChFHC%2BvqaQZX0yeXUKJBr3ePPTU6S2ZR%2FYHsj2Oir0qUqdaa72lYa9NXHZEngjiErIE2O3alWACYX579pojybtLxkCigHRcr%2FIAOZFT1j3%2FtEQWboi%2Fry5BTGfD6wG5arcmiVoJvW1y8pQjnjvnDILQukxLKu1ePSEQhAAKDax7GSWBtnPLYCW5naa0oWtoxzmSF3hhZ%2FqhJ2y4y4TCAgOQ3tJWESFIkQCeExdpcBS5FGgeSkP7qBmYr6L2EjoFzEbJe02ZMxN1P%2FrXSLUe%2BeErgq%2BVQ4RDjYFqerW08zDnuo69BjqkAWrnjbQVUiwyJzVD%2FsQLI1MRPECex5qTGqQ7JMJpt3KdWp6e3WetFIVnUB4YEJJ7BCYcVS4P2QIL%2BiTlcPrbKR8YC%2B0REirE3xVGUVnPPF2ez8paDJNGpvbTOXWGhIccTt6eZdjMzTlsVmbuRIR%2Fe78N2POr%2BJH%2BiexD84D%2F1mUJ92b9yQdU0e5hfuLO5YoHDENTftFHqyKsiKmWrGlWo53WqHZ%2F&X-Amz-Signature=96603bc081e550f5e27e79ac6081e75e2f1678bff85fb0046ec9e041c72e3e98&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6H4FW3U%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIEmWue1Yv4%2FDqeJ1V%2Fe0cc%2FvRW9%2FNKLLnkGOiKMVoZVjAiBJJvBTw71aChB3RPbRe%2BZsnoGFZiN0JyaHTXLdZUXfayr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMdYw4X5OcNHXa%2Bqr6KtwDlwjBD3nGm2bCfZs%2Ba1PwYmUZOIUJ15j6PL6%2B02369OPMadVBoJ4SWRtV%2FYO1qD09M%2BZkoVV7ZWF3%2B7ppJoe5iK15A8foYZaybFelJF%2BgGgD98PH000T3gBUpCw1Z1MqCQigImZ%2B7O9cj54eink5XlDO91vc8TATadWA2Mh05o9dDTrITi8azpyz%2BXbxaIBYfUMKoY2ljLAc1i9n1TuMdSZHiO4ye%2FbSgz88ZmdUORf%2B9Ph4TUwJsUKNy%2FaHnJvfHANZgslEpbFSWKCt92y571wWHDKoH2TPGUIXLcet36d9JaKwgzcScvj2qkdiDJhnmK6rbruMLTVpl%2Fq6rvWGKWcZlH3jIPj1duAU3cY1UkBerO12z2H3oy0s%2BHfHqqg0CK6E0v0mb5gltDmMmO7Q5%2BIfotXIThCBI5UYH0fZ2x%2BUtBtdP%2BuNdFiF95U%2FmvR6Z47Hu5Q3WSAo2323AMLngBw3fTpM03dY4Pd%2F4JnFrh9%2F0ESJAR4g%2F33r24hwsoMml2O13CV1rnGkwIJF7pF5BTfhs%2BQOYA5RpQl4Qw%2B%2F8ll%2FWULggy0noRPEj2SQwVYAcDWSTUeXE2En1IqPi3GxD2Cr6oDLcmH0f0e73oSAWuGOCCKNdpET7T2BsYqowrbqOvQY6pgEI%2Bc8LPDDaEtUX7iqC64ToccKDU0Mau80MsT2gHGRoeIq%2B%2FWHtW9XUO%2FlNz9TQYl04VYZJvLWtSkKoKypzeccx%2BDDIl8BsI3t3x4zdduMTChOC0CtZ%2FZHPaRo47ML9E469g1HvHP2np6qK%2FvasxKnYHSF9yDQLeCF5DKpPMYFmGGxvXlJxrnZc2i9SmDY9hDDrFkhEibcVL2mFOfZFEa4cY2AavL86&X-Amz-Signature=9822a6d083c6d3a987b0e7177c4b6896317870d0c2aefb36ef1441efea4c1414&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DLZRQ22%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCvBW5jpObUIgp1z12i5tLlLm39sj2Scv3xodQuPD3smgIhAJmStdgiyErQnCVqtO5hWjmuM7liVm6G4ugT%2FE13wOjSKv8DCEoQABoMNjM3NDIzMTgzODA1IgwDx%2BJCfaxjI5cKt1oq3APdRMMaFe7ZDtJ3oU%2FNX8tHvL7sl6uu7WljVGgkTy9eEL2nJ41NBTf4IYFXt8xiSjoD0boMfmxs%2Fcbf8CXXLuDhupDlGbvLP9dHX1C5FA8vp8Tvw1aiabeRX0kTtgOyIEokLAe69RragwZAuvr3rqlERjVmGWMYXWkYNfkXlZlFBQ30aNwAQmXkirozllF7C%2B%2FiAQ1a3weCUhDvcS%2FEEPdC1oKo%2BzYT07H1CFKK8TIQxOqv90aXroJUNZnkY%2FC65nweSC0SqGP2LcnZ0%2FEHzBvd%2FSDL6YVPkL1HiPxd0VZCEiLFnTOuyLEi6n2bmXZydUNVwW9Jatjp9MQ3ZjtRlOzEcVhEj8NJ9aMFRIpSOtJtpg9xv0elUAtq8CuW6%2FiUnYE4KcHa9LB6rWr09%2FtxDwqoxTXogOUiRvVNpv2SWZGwR0aRPja5jLs9X5xVOx7jo5FQaThJgFz%2BW61gAnooptpzKI%2BepA59Ghb0I6K%2BNeERi5Xz%2B8Za95hFNeWsWrcoFbZDwA9F9RMWnjakK%2BHpl9JagzTbbLB%2F9nL4buk6dA5QFGPezfWflxRVKXNeZqGaYG%2BuBmmTATxvi0N4SYls9Xp1NN%2BsB3yQ51RyCPlvvNV3XfY0wFdE33nljpDQ0zCKvI69BjqkAW%2BvFaczQRGwhi3e%2F26k08PG%2F1QQ5KGeinMcHYamWcUxTrMBnMxZuruuUBwQe8cqxKw0TXYF3N6igi8iRKcDaWvBWQfvQ7Lo9wfCk5oM5d%2FVWX5nV7oLUXcHpJ1OBl8j%2FhRNFzx4X2D8BKav4u9ap7j1Fd6z%2FtrB05m8PGybD1tKEnUNEicuSyw0mvLU50ys3CzR2R%2F3LhAUicMW3Puj7R9dtHdG&X-Amz-Signature=717ffb61e534c5be2a4821f640f0b22b608a43ed173f47de2a2a8b178e4bdec6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6FYS6GB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG7orhxw%2Bb7m%2Bsnyo5tQoCKuef%2FK23X%2BeWvFI5G1bGqLAiAmOVKAic2VXtiOsb%2FRwqAVkpWZKTznkXrTfIxvLVqOqir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMLSimmiZeTx6Zlx2NKtwDs3rr1n1uOfciuI5%2BpmjmbyyUDblcZiOixiVf%2FVNNI0Lycv0BFVKJsEWlu1%2BLlA3qcWQea2dqL1b2l6YyLEIhms6PaMbvQQ1jZzNsPziFX4WdalGqGU%2BvsvmDwoJlTZLE0%2BUFiAE0UkhDGi%2BSDB0KtKjsklbHHKghUtEnUA58%2Bhuu9yp66sRNzW%2BhG4t5NnRsancrZj7aeU2D7PyfjgHSFuVJ%2FmwDDn9wj29VpqdgK8Lt6ueosTLbGh%2F%2B35hU1DvTg9AmrMNlkWX0rDH4UawKlWSYduO6xt%2F%2Fa%2FxkeAn0QBLboqwwPCByIJTLNMRrggIXkmOLZmqhiZulXINuTiPHeeSj4sxMBDkybgk5YVODsSmT2dvuy4Iz7RAofcGhADWjtpxoSTn5MFU9Y6MYW7OQw%2F%2BRBZRfeMhoGABcmXLjWdFWDzoa5lKJMNXUhvSdsCp7IRabuYIgUTHnXElPMZppLxLPegQO5AJ%2FTrz%2Fg9RMNroJJEbFO6cKM4rM1tZyx8IlEfpkacDbL5jArPpz%2BU7bhV19fpYEjypNlrF%2FeUlCm5Ej2NuSAPwCVav0UTisnMFN8P2f%2B5gNjsZlKIBCl18wRLeTJr3P2P%2FcgAKpL1hK3%2FyC665iM6IP3rNkPOYw5bqOvQY6pgHNJG36eAiFZa7Fl18LbC%2BgUqq6BSOh%2F1jIpVPkZUzfSRIWy2bmWMVTTeMag5aVoNQKr8inJCAaAp%2B8powab3MLAHTB0ZG98ENBgF3XzT1KCL8fd6g6kR%2B%2B5kQ8T7ftNbYIUv4wGxCIE%2F8Og4VlID%2BoRRP5of13t3nEe89OU2KTa5DOikJMoPhn4OE80QyLastU4cR6wJAvGSGm9Q%2F8%2FZ1fVM7rYsUQ&X-Amz-Signature=b43bd975f511d365468505bc2bbc309a57ff2dfbf2601c0fdf73bfc2ed714e58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOGEWILY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDHwe6MKxTGpW1Vz8s%2FPeOApaUMtYOjgIB%2BReMwhymO9gIgPunRVdBehXVCgrpQYPI8C%2BO39QVQQEP9bxxWtTmJl7Mq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDMGZ2%2B1MaqKw3cNxFCrcA1xmuBOXzvm7pzvMruwPnzjPEuxMQ8cSHCHB2SxQBePUNTRTa7NJB%2F%2FIcDT%2B18uUYAkSZLMw5E9Eu6jp5c8NBNWoxuSWVBg7TKmqHfRaOXGnmEtZNcli5qDOmCXE9avFx4QedcFSh5tYvbvGIfjF%2FZ4WihaAgi1iKPC1fimJetU6I3sQkfyoI1tLqMKrMSXvq4pOvSQekkq0tAHT9GyWUYtdQpBlZtYpiXEvS97S3BZ66c0%2FTvmoC%2Bo%2FeRzqs8QPEefh60siixzcdwCZWAJHpb7MXkfxXZL%2BD3hrWmMEJzUwfYRq%2FvLDPkyIIb5hdxa8QuYTvd6foj25rQQV%2BohkwbPVZggoFIhcKWjASOMkKU74zI3uK%2BT4qY91rh1h34fSfBMu8IXTVFu%2FU%2B8O4YxMVkQUl11oZmz4RbQfwSe8U4futUIozPYV8Db%2FhRdhgpR4xJZdDNqtu0O8GlsQrxVw0SH%2FOcF6EiCWPNgPc22SyhiKBjm3AjTYTpm6LpOuOxBY5YCYwqKmdFDCzGBzll14zmAx08%2Bx54lnFI1yj9b%2F5Vp12OCdmUiIJmTt6PpTmX%2Bj%2Biisr6yRovaJgMzkx1xmvhUpb84P0SFWyNUJsTtdLfEnwr2iT8%2B6BzubP9vhMK66jr0GOqUB%2Fz%2B8GYiO5VEq6849lcAtQPqV3jEEoDEz2MCY28NlJVysoHPF1bY4agAZggvaT93uXruYhEwXSFwPANgePH5I810bnKVKDNAzpaGspNkzgjxjcnrecmh4gjKpza8sCbrLLM9twBG6762CE9CzELJZPm6KuOBQHqBsyUAEPIShNRfzDhR%2F82zaSl6VTWy2f4vAiCTxNBWMn8K3FLC11EqUoL9fmeIg&X-Amz-Signature=cb96dc6d0cebe625e82865756916cc5e0bf1ec38c4dd27b98ca9c24370487c3a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN6GG7UV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD%2BmEJfZ%2FjSgEYOSeX8hLnTJfMWT2zMsUINeBE5af5XxQIhAJyrmoRFVsD53F5Y3EODPn40Zf46zXBrOtJeqS9wAzb1Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw949np2CcBDLp%2BKzIq3ANYveyDMjHAGCrnA0iM6nl%2FW%2BWvvOyKDT95XTpon88lP4tQVHAOKPuvKw05uaJGmjg3ZIl5gAMASrc16gYAmgOO222uN2GEXWHwcG0AlbDrfZ2q%2BgVrlTRX4R8H1BQzUtmk6N6L689jfozq2o0CIQIIqg3Bai52ddgoVabYe2obnVRox9O%2FbnEv7MvnWMENyBUqp61UEH4WCsjcVfRbHu4dsBst8eTc36fCMg5tiEUSlZmcW8%2F7tffjD07NoSx4kQjLXSMxyqD3j6hQgvSLdr5Eu9%2FGDMK31tdo3nQ1o7GtZR5vSybmj%2BGGvr0sySJIGdYqBN2gNyPu4a96SC%2BRMGE2xhTIy6dC%2B%2BC9y9itYUh%2B0A8wnEkJhDy3viRFt4mm%2BWoVKn8w4Hm%2FGY61lAUOglKPIwztIM6GTsnQYyYpwXDvNCn1wxPwGqaR3OTdA39XK7s1bfQ5Jbk7gdq%2B6vhEhozOF7DXPoRZUTzJ41ScsaK8dyXi4ccsT9Hz%2FGQirbokgn7ogN%2BjmxKf2rjF%2F7Hj%2Bp%2B91Yto%2B7xsrPLHrTATEMMmcH%2BDACInuVz22I4ljCSIx9zZliBetZ2l9WthE%2BvE0cxroKEz1gn65UGNvmqLJyStFTWdsVuHQmvxKb1FPjDcuo69BjqkAfM3g9rLguK4LlMtcLvGmT8VBje7auRbbinsVax%2BPKGOYNu70iMOubUZ3YAc6JevzNPh5z%2F9WvVrvqrCa5p8kZcIMKdBij%2BEUnRYwsuE8I6qciPq28jFhN3zjzMvoaFvrX3rW4EN9wmigc4qDhZ6904jsTSaqCd26FNSSABEF9bTWE3Q%2Bn0P%2FI%2Bh%2FOTJIwn3lMogwMvCFeKzV4MPC0fyqoYFAjTN&X-Amz-Signature=2cff367e194b8bba583e6d2b0f3467e78068435cbe032637639a54ea951bb7dc&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SCQCFS7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCxRQTdyyDGc0KWRFI61T25SQQ6Oakenu1tEiLaF4srTAIhALduGvaj9p0UyIud1vwAZ7BoWljMbaZrn5GpP1RgqvTtKv8DCEoQABoMNjM3NDIzMTgzODA1IgzY1d8y0UQNc325h8Iq3ANiBA6tYMIZdji6yLOPeQYXWVNxk0bf7kfNFOd6Qiqe%2FS4Ab6mtOhpQPNHeeIQ1YNqrhufQOT4FR2w9NPoqqJ1Eevo9TCIoO5yeK6WZp99XUjpWYFjiNPe%2BSb8MUzVTS2y7pY1IwP311i5mx29G6c%2Beh1GiQDo0oyB97ec1Q8ascSdr3n38T95ih99WtImHtmu0aZH4Dbs1c02kSml5ZPQR6Y5Y7nrAxOCY3ARRNMKU7bSQT%2F26EU0HI0erNxTqMvHb1aBJMcQkP4DREi7MyW3HXDlXA58xFdyQm0zzTO7TQD3gNsDXk%2BTUSitLBN8FKN6VgFz8SatzgPD0z66guJ%2BM%2FSS5cQ6%2BbUIFhf8NYGjIHXvpIrydiw8%2FXJ815fnigk3WpgBh%2BjlSSDJ28aI1EMzZREtR%2BAWPgxvEZa4iDUqfU0N5ilJzscBtddYzjKbjtPo7ViXHaDnHZM7j2ja1%2FsLL0ZExY8PhRhaSGcMIgunp7PkRYacQV7tvFGyOas09XDCwjdZX2kKIoeyQQaWbqaICPMDVVttxwsy%2FrIS2msbnZU%2FcJn8HdexM6DVbJXI3G%2FgSK2rem4yw%2FdL0Ja6mgZrblPLZWhEjWOtk8cJfu7qBlxGfcITTgosF3lhG1DDDuo69BjqkAfkJKIPamvBDACVnn6d0dqkuTfIKFncnKXgzvyugTqLbFd7T1jwEUXYeg5HvuA0ipDvXy1MG6FJoal059VObqmioTdONoKMNZZkHRSj0EDYe08WwxO7S%2BbUZD9a4%2BHi72xktGCCA5XWQuZgjIns2K5fMHTepQrIjH0M%2BZU1tskhCfxXLTMkNiJ4GoDrk9TgEJFKoLxs34ZsNj4WxdXTA59YuUJqY&X-Amz-Signature=1f6319d70bf2e4464889473a44112c103e2e81fc9e84953b382d4fe41a83925f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXV3SNQB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDFmX1PnxwcCyg4Rb%2BWOejtyreLA2yFxn2PtfE11OVUkAIhAOGe0%2BBzQRJSXcIWhdtDCsb4OX2zY%2FBZvSMqCvOEXR68Kv8DCEoQABoMNjM3NDIzMTgzODA1Igx8%2B24IoMQvKJkc1bcq3ANx5HTjZZLSQhDhfgngqxMqg2xDsxFdfBvOBT12UFzDRPysMIsPltLjP9vEZQi297f5r93uXO%2FpT3JRYTdPEVb2BG5SL1hLYEpiCcr9onmkC0Q8qHDx1UBDv9l8JVUWTyo4GRoY%2F2EAI95P7ashVkxjkV8M%2BsTFMZY9ja%2Bh9s5wUKzigpjhTs%2B8H%2FRwk%2FsuuvLvqztTIGfFYKtlp4cvSwX2vl7IQ87d%2Fj1LqQiiLkE1W65Mkv2Ay2%2BIV6sVP1KxeK9dbCdh6IEoV1pV5ylb%2Bxe6UiIGdl1GGHQUwYo3TKGRUECqXPUbbfNVzEJ9ByWTJ%2BGGKZFJv6mDF7qf1eX2AMEwKEzPXqi%2Fn%2FwLloH5zjVAdQSIUL1fsW6hHoP4ruI2BqvBqEVfIPDoDt19fkBudId7kU9OQu1yBGiyUNxY5LzGpptbFdMOiBbh8xKtq2%2Fq3Vjavfwx1%2BNvLIAslCF0Sfd3UiZyKPdr3F5XkC7fR9Pk%2FX6SzsuPLJMLcq2bdezbuzHY7BuYocEoev62Vu2At%2FQIZD%2BQ3Klvq%2BJhhXwb2HFjXyLhJPmRksRVkdyLwAsArZcmGhzU1B71i0ZZSUIphfLmEWoVrxX%2Bte4JjofCAWenBmwLdBX8ZVMFay7oezDSuo69BjqkAVj77y6WQrNjmusFmb2R96ae4w9dVfUtrcmLdjcVDRmwAdLLZXz20bi3lbtU7NP382gFv07V%2BIL6UuONcceX%2Bo60O%2BjA%2F4ntxBEe87DxX50MdHJ%2FVqWyas5s1VAUEdl8hvGnIoXct%2BJioDRdPF048%2B6J7uMvKmJwWgJveZK2DFtZoOon6e3qDYGKRVwE2g%2Frl1rmD7BHtbo1fXbDOPZYtmv%2FY2I3&X-Amz-Signature=f40e6ba02375a4c808506f2c7ec1da489926ee3a5037e84f81ccde47c7bdc8c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOGEWILY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDHwe6MKxTGpW1Vz8s%2FPeOApaUMtYOjgIB%2BReMwhymO9gIgPunRVdBehXVCgrpQYPI8C%2BO39QVQQEP9bxxWtTmJl7Mq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDMGZ2%2B1MaqKw3cNxFCrcA1xmuBOXzvm7pzvMruwPnzjPEuxMQ8cSHCHB2SxQBePUNTRTa7NJB%2F%2FIcDT%2B18uUYAkSZLMw5E9Eu6jp5c8NBNWoxuSWVBg7TKmqHfRaOXGnmEtZNcli5qDOmCXE9avFx4QedcFSh5tYvbvGIfjF%2FZ4WihaAgi1iKPC1fimJetU6I3sQkfyoI1tLqMKrMSXvq4pOvSQekkq0tAHT9GyWUYtdQpBlZtYpiXEvS97S3BZ66c0%2FTvmoC%2Bo%2FeRzqs8QPEefh60siixzcdwCZWAJHpb7MXkfxXZL%2BD3hrWmMEJzUwfYRq%2FvLDPkyIIb5hdxa8QuYTvd6foj25rQQV%2BohkwbPVZggoFIhcKWjASOMkKU74zI3uK%2BT4qY91rh1h34fSfBMu8IXTVFu%2FU%2B8O4YxMVkQUl11oZmz4RbQfwSe8U4futUIozPYV8Db%2FhRdhgpR4xJZdDNqtu0O8GlsQrxVw0SH%2FOcF6EiCWPNgPc22SyhiKBjm3AjTYTpm6LpOuOxBY5YCYwqKmdFDCzGBzll14zmAx08%2Bx54lnFI1yj9b%2F5Vp12OCdmUiIJmTt6PpTmX%2Bj%2Biisr6yRovaJgMzkx1xmvhUpb84P0SFWyNUJsTtdLfEnwr2iT8%2B6BzubP9vhMK66jr0GOqUB%2Fz%2B8GYiO5VEq6849lcAtQPqV3jEEoDEz2MCY28NlJVysoHPF1bY4agAZggvaT93uXruYhEwXSFwPANgePH5I810bnKVKDNAzpaGspNkzgjxjcnrecmh4gjKpza8sCbrLLM9twBG6762CE9CzELJZPm6KuOBQHqBsyUAEPIShNRfzDhR%2F82zaSl6VTWy2f4vAiCTxNBWMn8K3FLC11EqUoL9fmeIg&X-Amz-Signature=40797efe1cfddaceffc95ee741b225128ef916f9edf32349bbed070ec9ad01c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXZP3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHcazyWjH3lO%2BNXTavhswZJk5opCZGfvRKuPMgFrQwvTAiAVg96qtwdw7Amp8euFbfCzFxISUt49v1HjxsY%2Bte7cwir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM5s%2Bc%2BN6RzZXku9XXKtwDN3fe2Y7dR9IeeJ2IAiW1DfxGH02s8QJ%2FnbS23N13vc3J3anpxnaDTXD4BepG9PwLnQsQS8395elErKJvFPWV7cnBP4O6edxawYx6cAsJJ9AuY4uClyPzZvRhiSheSWQMQ7pPsnh3j4zyI19S0sC%2BX2Er1MvNA7Fym8secHoQnZHA3KxrC%2Ba98MaU4CM7cSVbx2BtLqfQryI3bVTwO7WjOSnNX%2FXYeNDU2OkWQST0Ac6Y5PVWnE2WdVKqbNgGF2sck%2FTh8qxkoPv5XGVBQWPx1wUgm9jyPTD095e4jHEeLnsDqqmo4LCwvPwg3869k4ZqDolR1rDHbC9LDSAKTLCIGuv01xSq%2F0bEiv%2BPrzGSblLxGfam%2Bbc53jW%2BRZOJsTbIBorOvGYxcMjol6NuS0xEVida6LtF7ezMx5nV5GJkrwGqaL%2BWg13DaAJzytVfP8byOPKNIN9tNgXhegA5v2lfXpDjtzuMI65ErYXJmLEw3TQm0Qvrq59DsRByN3t1a4LSls5JtzSelPIBASQNtUPCHfwnFpSA9clEWImZ9ACJk3NJ03jtZV%2FXdA9Br4BWDNh39Zu3x0AVuckLRx6yKRJl3%2BBuL0mjZo2%2FaUqYlg3kTXOvyE7iEI1wKbRZduwwz7qOvQY6pgEXw4A%2BRPmGooWDLtQ4kpOJZ6bqkAyLiF41SuIqIMDVxxMrPrw%2FYLdtaJoR%2F01n4cYKWtgu1Q4PHrWJrx68JLnquQ8EVGR%2BmPSEtf5u1cUMmFTAPWT%2F7lV6pIm70iITWZbIscucY9cNImNwhNucYDTLJoip5r6kNloyJrvuppmwKCRAiuPVeJLzUBW%2Fo6jlcIYYvBL2pmnaBb4klMt%2BhHxzYoH1VGJm&X-Amz-Signature=36fe3578944ccfb8eb6ce62081e2b690ef26b5005c78c200f4251191dee16f6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZXZP3E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHcazyWjH3lO%2BNXTavhswZJk5opCZGfvRKuPMgFrQwvTAiAVg96qtwdw7Amp8euFbfCzFxISUt49v1HjxsY%2Bte7cwir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM5s%2Bc%2BN6RzZXku9XXKtwDN3fe2Y7dR9IeeJ2IAiW1DfxGH02s8QJ%2FnbS23N13vc3J3anpxnaDTXD4BepG9PwLnQsQS8395elErKJvFPWV7cnBP4O6edxawYx6cAsJJ9AuY4uClyPzZvRhiSheSWQMQ7pPsnh3j4zyI19S0sC%2BX2Er1MvNA7Fym8secHoQnZHA3KxrC%2Ba98MaU4CM7cSVbx2BtLqfQryI3bVTwO7WjOSnNX%2FXYeNDU2OkWQST0Ac6Y5PVWnE2WdVKqbNgGF2sck%2FTh8qxkoPv5XGVBQWPx1wUgm9jyPTD095e4jHEeLnsDqqmo4LCwvPwg3869k4ZqDolR1rDHbC9LDSAKTLCIGuv01xSq%2F0bEiv%2BPrzGSblLxGfam%2Bbc53jW%2BRZOJsTbIBorOvGYxcMjol6NuS0xEVida6LtF7ezMx5nV5GJkrwGqaL%2BWg13DaAJzytVfP8byOPKNIN9tNgXhegA5v2lfXpDjtzuMI65ErYXJmLEw3TQm0Qvrq59DsRByN3t1a4LSls5JtzSelPIBASQNtUPCHfwnFpSA9clEWImZ9ACJk3NJ03jtZV%2FXdA9Br4BWDNh39Zu3x0AVuckLRx6yKRJl3%2BBuL0mjZo2%2FaUqYlg3kTXOvyE7iEI1wKbRZduwwz7qOvQY6pgEXw4A%2BRPmGooWDLtQ4kpOJZ6bqkAyLiF41SuIqIMDVxxMrPrw%2FYLdtaJoR%2F01n4cYKWtgu1Q4PHrWJrx68JLnquQ8EVGR%2BmPSEtf5u1cUMmFTAPWT%2F7lV6pIm70iITWZbIscucY9cNImNwhNucYDTLJoip5r6kNloyJrvuppmwKCRAiuPVeJLzUBW%2Fo6jlcIYYvBL2pmnaBb4klMt%2BhHxzYoH1VGJm&X-Amz-Signature=e81410efe1510b0d1ee68f2df1a30a2f1f8aa7d93085eaa6e4ecbe15d5627301&X-Amz-SignedHeaders=host&x-id=GetObject)
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