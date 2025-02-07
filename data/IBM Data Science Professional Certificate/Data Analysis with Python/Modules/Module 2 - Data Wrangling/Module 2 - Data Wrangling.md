

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5GAMRZV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDc%2FwqJU8TCMVh7PcF2DLJl4qBIHNcaQl1PMP9WmTuK0gIhAJMJ39WZ1BcJBZDdpC%2B4%2Fh9qS7mhBlWEwbeVl7H0GxcvKv8DCHYQABoMNjM3NDIzMTgzODA1IgyVvMha1f09cZ5NbA4q3APZARAF6azDX75Fl92VT2YNJTaTl0qZR69ZFr3cq2t77NZTqXvmXW623LT5e2UKuXLQw3Ye9YsfLeOoEYlm4ji1kW5%2BuG%2Bfpt4HOYb6IUjrGJvTPvsB3tjBDQMe%2BcjLirpvzNgmGejR5tD6xz846QByIsopBsnjq9%2FFCaVaW2FBa4l1xlOKgqHXrPUMnjCr6mrAm%2FlcSvzqY2vW6lP%2BgzWScOQ4dHqPKGhmaGgIKkiihKOSnbCrXDbMR9%2F8SepGfCyt33Uja8NkzCdLQ%2FvhZ%2FlGsjLPPOuptajO4DgL5BUUYWLCJU9xJNiDM9aFKLO8q8eKGXXbEtsZCK0cfxYZaVHMRaQQXMh%2Bc8BVPM1eNXbDJNLpIPIGcMvOXhkXpMACA6gi0PahKv7kL%2BX4rdudPqW8eY9Wze2gYzVBSGYDIaUWGmJ5MR4mqA0vFhjAg7EPYXOVD%2F%2BaIesHYUFaEcKyyFIWkbVksAjsU78X%2FGSH%2BBEi3CBhV%2FFBWwS7ONoO%2FSHernlNh5kEfqEOXMA%2Fb4ogAn7kVW0qDdnnwMR3c1krQaLENXVMW1FvT8pcLJNHwWTJ0WFRZv7Z7hzZ7UEA5bfkw9brfDKXXnwPfsN1IqjXwe2sHsn9mk6%2BI6tHughORzC7i5i9BjqkAbI8LBRayBWR%2FTtxf89Cl3hPeY56nN%2BnVR5Yojz9q42eE0x%2FLidCEgjKULExZZ3ZO%2BlzkqyAj4rXYNJqCHrZaCOtdQ5sLTYaK5j6Vd62O5r%2FrIYs1wnq0rtBf93okCFlF8QEDvD3M7L8NCNC%2BqMjZ08VOsioka5H0nVDydwR0PFM%2BeSgJBHn05DWBk14bRqMOGpNu0RnAfNEyCPnXz72%2BTErJDco&X-Amz-Signature=8ed8aff91c94ddf87fad172d45449e16d815914cfdf887d84c23f71156a106cd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN6LF3AN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDgygNfsYPFl3uqB%2FXf665lHVqsbsXoMV7SUR51dtSiSQIgU0kd0KSo2SqJLmnu03X%2FjhcNucngFtJoZUeZGIbfrYUq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDKmOygI4se7WPwiF9yrcA2Gn1nismYCiMwub9DDWGdk%2FmC6ydb%2FU4uosy6KKoRGiPbhDePRER0ZWkVAvHJhpN5KQAFEeqfjeKbr%2FOMjNj2owwkYHeBdSmAQKa5Qj0BWHKoWr9oXC3L8io0mTQpgFoKVGCThhll1v%2BV%2BJQvIXT22hpCeMzX5tQ5TjXdYh6BbqhNBLE0dJNCRAIgkCa0JE72EV%2Fj5GZPQuyj9r9475F0qLT%2BhlIwumy%2FAb49RRlEtHxAo2Q8QA%2FrO4TkGXxoZdQJpvN%2FxxYtv%2BYOjsF%2B9dFHF1Qc2BllBBs0y%2FYuZVJpM4QsB%2BNsMWPJM%2FyLip7meKssiKauLZqNNkohQjwrYAp7Q4c29VzVWwYGw11Ap8fhYBzmDdbdqRQJzL1XGn4DkqgZCG0zkphZr7l2qHFlBGZ5G%2F2Dd30ogi4CiC%2BW%2FPe6W%2BvPVttfAkqSgnC09xTmmI9UzblX0k9%2FPM9cesRFBBfJ9mKybtlQHHMG914pBHTAVD9oOW2ougos9OecooXXvJtaDqtEEFK8frU2gox%2FhMVYVpfePuGpTQonCgw2rviztXe%2BTGm4D%2FDy27jGpkLNaxs9f7AcAQPi9MiZcFj1du%2Fm5Bg9ZzdcAplpvWpEoN0wODvXUmo1s9fq4h2%2BdQMOKKmL0GOqUB0m0Fud%2B3sMqe68QTINaA4b55%2FSpT3Zb3pPagB8DFqs28Ko98wyfssvIu%2B4xQ8BWS1HR5LuOoeUn1czZ38LOvsTi7jROJAuIFXeSU37KnOwKokuxdgYG03IHY%2FVl2oPslbS9D0fe7uGPOW%2B%2Fwt9jF6oKHdRstptjHeSFdM56LsPXYySWaTyhYVd%2BbE59rV9OzyD%2BYvsUxC7kYpCqmjEOaZrxzDq2n&X-Amz-Signature=653ecb578c8bc76457c4a9b257f1def43c44a2085bb8dedc4ba1fd175a8166ff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2RBCQH2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGqBbpmJvP9EqfBfiEPH7eQcIIAMtJhGqR8Ste1PLDGVAiEAj%2Fvx%2BfJZsIRrLYQ9DnrWT1Ky94lJ0dpjTRgyICFKa4Aq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDPhF7uw7ciXX5SLx%2FCrcA%2F%2B5Ij%2FFy0tcDG9qjU5hLwzW6rAVbzY9n1YefP59Ht0EtT7YUVtpBHYVqW%2FpnZJvWx25LdT%2FEiK3OK%2B9F2UZntcXo4Aq9ru%2FmjUegSrGh8dvjCJ%2F%2BXNhnkZChPSQtiO%2FD2p0QOIBSRMVTt7muRiQ9F7d6SHZtHhlUH6LrQ1CTwjeWE0ts4mcjP3WPKZ%2BWJShtg%2BNUPOiMD1UIc6zERePK0ut7phRxtX4qBmmBNI80QlwhLdYUsET0ZVveAr0yoxVZ86pkgSr9J3ufBospS3onH6yc%2FG8VGHLELyvLqo6YOMToz%2Fr2agf5FFJPjfod%2Bsg00lsmqAQo0XfElTu8Yx8oeKRviGjHfVgOQfC3Oxx1oAxI77eGkh%2FmX83omleiIY4vJbyDwmI43gdYGP5w99Msh6HdImgS2DNsEWnpST0T5kM%2BSKpvawffwtTMhypxnQ78iTfdR2ENNpZtUPQyQxQlwQf09xwwV6LkcD6EhragVaQ58w7ZTHssHDN9fRUl%2BbmXzwZNZoWQJmgo8Lsh%2BHv75XeY%2Be5mmyKyFAKRLvJf3VFy6eOeqvsZ2sewBrGtlExTyRmubmSarC0NIlZYbfaQBGm4AvqGG7b1zDiGBQBZXIi0TZ4YnomYZn%2F27bsMOGKmL0GOqUBwt2KQXNCBS0i0%2BaDeMRltnHY6laBJDhKy4fRRQS24h8WacXw6vsJF1AITedUsYPjbNdadJ0ibFtRJVPVGPcUFMQKDGkkjQWMWNoAMKGSG2G%2BNHWaJNY67MuK%2Fx9%2FBrOnSpd5PDt8jkAr%2FcYMN4UpFnh%2FwTyq%2FqZy2uUS%2B6OG6m%2BXMQVmjZxXljKzcg5AgDyxPtUMWLDv9mUsQoJ0QHk2AlAOg9qG&X-Amz-Signature=24c537732097f125b6b5de6b23830f6b8343f73c056057b36807ac9d83e82312&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BRGGM2S%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIFloV1pTxz2ZD1vcYcxnwYk0ac2dyIBIpylx8aR3BmLeAiEArapkSGX24%2BSMt5PKC7E97LJHz8eUxp2GgkjMqOV9%2BCMq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGJBRgRhFiQgZwTvlSrcA0PQJgAhRy9lg4AN%2BfXQmdiqZteO0oA1mDyx43gvTtWTARiOefBEVNFsOIH43maNERBrvbqA4ypcm06rupFKrj156bk1lCTBZQNrQRBIUZjJ9stVBAH63ODryvKgL%2Fby3ygGLoK%2FvkaNQrxmBdB8OBsky7EH6H9fgA6ybLbxwxMzLmHkTRe2%2FLyvtgMMwFWOmJe%2FIew48BUYXe2HBHrrMjdRQX6XCOif3aYHWmCSYCrVqqWCiMtFtQC6CEKMA5mxD%2BjEJbiDaj6ZLRieehbEP4yVqa9eaythZt%2B3AsWbnsC%2FCM4P4SU4hXLmR2%2BoJbFpCLeRW5eXUpCss7y0v%2BzlPoLDjtUotyOiXRS6r%2FoLCr7huRVwVTpJ3gJN78LvlgG1QX6iIEa0FPmI2NRj6GCEC5yTrvqqaL%2FxO5OHla5OydidC3ERGeNHt5OKyJjHOlWZ2%2BtKnMPCoVwQ8GV%2FLswV5piKt6ufyxcmb6WIfoMp6jZM8XbmTUCtCB3wuWY8ZdRZWLTBglmLuY2zOF5Alga04BCcbhd63%2FYUmW66U6GA8SlOqeLayHRYoQm1NOaAPpbJCbrrW8WpxNN1zk%2BS%2BZTSzUNpi5fmxn2S3xp3c7rcVlfSND125iveIl8P3%2F6uMOKKmL0GOqUB0Wi2jGXdXPIi8Kvh0vG7Xl%2BgZZKYz3G5%2FtdHD9uhG9gJMQNpfgHxjFIHK1WgYXUeV45nu2XPyrUWXqJGT0tGsmuZzlnEsPM%2BLqFBjIlxynDRF5QQK26mCDIcr48xpUatw8JM4UaJ%2F1odteRWPUqochsyEylmUujlJvD4by3NzZhAz2MGLemJYnRkyxmRF6kL%2F%2FXwWW0QVSGjNBQU20h%2FJUW0DkUn&X-Amz-Signature=7c85faffd87fb5ae93c78c5e502e576aa5c7d2722686e1094dee318dbf3ed3aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2AGMH3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDOYsIU%2BBcpJI91REN%2FF8olWBtirvJkHBtEBlSOEEDHpgIge8gmtaz8uGQwJzLIx62R%2FTL2u4dcSRDV8InfF8YBN1Iq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDG0957I5OJunAWrFjSrcA6XFDD%2FJ0ByRrTZHrHtk7pyyDiGXO%2FuumJupNYWXZl7qISpRFu7ki1qn%2BmEu3pqt1lR5fpfl939MIkGNmdWh0lYVvlAPnlzDepaET4Ak6N0Ge8DoqJOG%2FZ8J%2Fv983lA31GQuSpB1M71NcpYKIVlNH%2F7sJNU0ZXmC%2Bx%2BVIuPECs9Ar497VNcMzXXAUGmdFOo5yFpjPvkgnl6QtrfvoV8G05T9C8MhnklvpUBPa2h3XOWpskqR2RJz7HFndymTl1RwdVt%2Bbbo2Ag1s0YEonSgYraA37B0mIhBvNSi5OuZysbFHXL91odyQQ3VwNl76GuZfSjqHoA9rLCwgm1mg7laYiVP6LN%2B9zDWQiASxFz1ueM9dDEM%2Fh%2BU8Co4CjcjpfB5b6eljJDy%2Ff5lIMZhOePza8cibJRjXAaAx0KVFR5eGzztmo9Ucj5dpz%2BQwUQvAEUwnL7%2F5LQ8b%2Ft8JEL%2B3kZXR0rk71vqY2hv13Yde4mKaTNWSXkJyic%2F0rGglrApH5%2Fd6R3WmglHMbb38ZVQh92KyrjQ1L9bWhoB3jxk9v8sj6JPA7%2Bzh2ieU0GnUYXZaEjsnfZgD6cUFQxqgX9X6%2Fuw07naM4zLAoUGNnEDdZXDkKJ0dncp0qlbAW1w2rlljMIOLmL0GOqUBzNcoGkmvg93ZfCiuEglvMNGkBQWgYXOpImjH%2FJhTnmPkQ1WPmCthBYEpu%2FW8o3ExOe7PMg4yszBLuHj2yNcIml3iyv3NMuiYh08R7U5UuI730lWHWsTs7fK46XROfck56CDdFJGq7xMKETJRgLIbURQ%2B53r5E8o1MhIY1lD%2B9NIrUvzeZurZlzrkrazcYRRBYbDIer%2BBmeykr1si2ZidRcRYLwW1&X-Amz-Signature=87839a97d12fb13fc0fb03cae5a9dd430042b2cb4ec5d57d6d14d5b51b7dc8e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V6AZKAG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDxeuqbrRo7VcbKpl860aGEIUcDrFNbpJcGUCq910s7WgIgFAvm79eOzzf2IHqVOmhaIbBE8GTeSdL41NT6UkZNM2Eq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDORaWPLcUNSR2fAA3ircAxApyvrSJgm4DlJ1swFtR2gu7h%2BuB5kpytisAEihzdkw2ObkoL5UgkHA3Rl8ei9B4FpaHR%2FTAXLOkbLTB4YnGVdSWNeM4BVgdflKXWtVOuerW9pXalKpY%2B1Vq3zBsrhRn2FSZYaHcHdvJireUbBbCofo32QKxAixmm9VOXJ%2FyeYX8q07RPY1Rz2ztFKgGFzGVz4HtahkWl4L1qGCJ3w%2B6OvSFBMTzfGcL2pe4H%2B5MkX6oxfTDoP%2Fu9O54j6Tq3jmm8WaYqRvw3jh0jaXzoF2Uf474qBxL1oHh%2FPhb6Zs0n%2FyE%2BKaVZmVnqojBxKrRnaBFlUI%2FYhw8cF3FosaTaKPMjdo%2FZLHqLkF6469OgRb0NaIP1ha8GQ5Dzbcvz3VAGBYwnaX2DMJlhpou3xGGo%2BqZggjLE4JxkiLkEY97KVefD0mPjIv%2FJh2VOBPjhxvXYCyqCRG2JFg04nWdoDNsXhnYx16PXGEPm8x6NsMsDyFSqevNzqWsJItqnWOqV63PtyGd1PbwouaUVyT6lUoKwMJAb1%2BvHpFAl7w%2BxhQSNg1KwjxvM520eyeI53ZAn%2FOjCOaIs1dFyohbw%2BjlIDcEpwx4P4FHMQibccFjFyInjHfCEWz7yyCRFUfvywmX6JXMMaLmL0GOqUBmIhDhp7R1S86xzn2HMlv89IMFPU0TVl0sXI7667fM9gjlLSF5AYsyJoVm6K7L1ZU4ca9mwqsEAehG5sUefYAaI%2BzO01M51wGA%2B5UF1YBNBbsn3kFi2zztCqMNZCvNZ8745Fa2grj7SXUenMLQmBVsTVzRkTk9AdZVH95x0fMpffH%2F9RpDAZHpnxcpscfanQSaLlO2%2F7On363JXhGbeyrV50PCPwC&X-Amz-Signature=06365ea8c0476c34d5e568db8409eec79a8b805b87d1c642c4efffbeb0ae84aa&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTXI3PJ7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQD1HgoWMC6XxNx3RtB%2FBsUzgcrv0QKweRkjT0fDtoAvtQIgc5E23PQ%2FW83OIPqE2Yb0PNYWc0MX0NhMl6q7k4XdKb0q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDLXMjx606LHMJaLa0ircAwHMS5q9VUWZK3SS2PQYmiY0W05AQQkxRJZIjLfl7Ix5pDQtRlAel4lAPHzqO2WNYBVqZlQQl2arGotv%2BceE2F33fagdC1ks5MDFQXOFeOjGsuH1XmhiL%2BKCM68DjQk6IThke%2BUL8l8%2FSlz7TIu1jMRzcDtQXK9kpQrbarqy3fXd%2FbJLDbEO28E2NmkknJCf6u31FFksVd0aVCl%2B5rtniTsph35GnIkhWmZiZEURMoMhqD8hUIQkXjBDl6yimTDL1MgmsLaQRhvnvZ5YtS7xwKC0FeS0gtH%2F0cxM5vmlPf9zFiFbRpe8NuM6YqSV7Zw1U3OJGB7JSjtOtHryU4ZBCVCxqL%2BkV3%2BhL1KGHqt4p0b2ShoWUQr%2BDLxBaIhrI1ENjMAanmomiKIgMXt7Jim9iUs7K0bV9yi%2BFV0zK1jelyoZjay%2BbjeLQiq6SlqpVrv1GgZV0HgAkylbjvBm%2FSquhasKgxsc4JKa4DThjODJlIVnpBzIsNDEgvOMu0B2QCs9XOhTIB7YAUgHnsRh1nSxtK3n%2B%2FTjCYhC1cDvWgaOqrB24mnGTmNujn%2F%2FoCU5xgRJIzW6ErozNLRWt28q1SrlIEzbKYPLpvlz71bbmnhhKFQkwkUY9LYTW%2FpqyazYMMeLmL0GOqUBLuDBnxHaDsNbNBY%2FHLRC7zxSSKpNqcrdGP1PoUFp%2BNBNLnP%2BBVNgbrU4zLN5P4QdD%2Fo26Eqp6Ojj5vt4pH2qqulk%2Bjm7iLMzd7XXNgGuTnjC4F6BtS1Py6fHIrXMei3AIv4K6XG61%2FaOdWgNxRbLYB0AAU7vi9aXwItMml42vrZPWjNd7cWKUa9AblvbvjK37HUWyntUNQ%2BuHk8K81UuLCfxDCWp&X-Amz-Signature=33b41c4828863f747eff10379bf5f835f7c85fa3e20c168b7ef2bb14c8c7265b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCT6DZNI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGqopXKOzkIQKtHKz26zNaMUXoYxVTwLNwYYkaNuhI61AiEA06UyeemTGdPKXzmmb928k0BEpgYcU2ZfnNo8MMSPRFYq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDPra2w3cRysBvduCeircA%2FiaCwzkw0FV7CMxlkgLr2uve9vnHThHK7bW9DPCuMPigzH0wRIrcfp6X8SxJFCYUpzlY6OLgPu475cIS7HtgkUSJZd%2FmCj8uTS86dijJl1W6CmYlMDeIU45v1g%2FsJeET%2BIlnCgX13Jkok%2B3N9medIXRkScnNYUKAHaym8cnXlgbJ%2F%2FbXodrsSldb7CsRAU3kfeHylKB0sDSw1KjMrTcaeuOTHPQ2O7RDyttoZ0nu0MEKoOvDexq8lKyUJckBnFpNKzITwGJHSO5zf2YchvUS7RBUCiifEqPXWO3RxLfBZIuLlkjKpB47ct3tyeoS05uI3hTWcjy802agfTTo2KeDtVIR3%2BaRUTZGJYvGdi1oPLGMF%2BrD9nVqY9St66LU71uifoYvUADAnUHJ0v%2FE%2BDR4ZKeEt5%2ByLDH7Bb04H4wmQFbsNZd4qhL2IJISuhBTyQzt9bxkeFfr1WzCjRxeqwaV2Z7IHe7vh%2FKpUPg0VXDza8J3DZu0CkmQCVVqIBxHRvgVtifgi82C0n2TjyWjEY492cE%2B8JJ28KviqoUChCSaVobNZotJSCNABwB%2BkVuzHzoxHJRYybrsiIhEjT495ZVqub8i3e78cvulM%2Bf78FHGUuCqJp6oKFRJBEUkP%2ByMKyLmL0GOqUBsS%2BIlWe8eDVzingVzZR5nytQWGNIH3Vpv7o5g9wN2IwmMNgtWTT3Dv1v5iwlRpgzYl7B%2FWVgtUknSoJVGGf6YtcgiMkPGZbLDs2409ypySeV0BH6GEh0YXq67Pwgvpc0zCsa8WzC2l5PC1t%2B9pIz8nroPp17xLSidT0eNHgHO9OdyHtO%2F%2BeZsBeRkK5i9o%2BNkw68VleRc5Ls%2F3erq7P1pk7NT2AK&X-Amz-Signature=2711463c3f4546d45621fc5edb0b035f6c3339f1cc199e3d3cecbdf3e18c15c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2AGMH3C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDOYsIU%2BBcpJI91REN%2FF8olWBtirvJkHBtEBlSOEEDHpgIge8gmtaz8uGQwJzLIx62R%2FTL2u4dcSRDV8InfF8YBN1Iq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDG0957I5OJunAWrFjSrcA6XFDD%2FJ0ByRrTZHrHtk7pyyDiGXO%2FuumJupNYWXZl7qISpRFu7ki1qn%2BmEu3pqt1lR5fpfl939MIkGNmdWh0lYVvlAPnlzDepaET4Ak6N0Ge8DoqJOG%2FZ8J%2Fv983lA31GQuSpB1M71NcpYKIVlNH%2F7sJNU0ZXmC%2Bx%2BVIuPECs9Ar497VNcMzXXAUGmdFOo5yFpjPvkgnl6QtrfvoV8G05T9C8MhnklvpUBPa2h3XOWpskqR2RJz7HFndymTl1RwdVt%2Bbbo2Ag1s0YEonSgYraA37B0mIhBvNSi5OuZysbFHXL91odyQQ3VwNl76GuZfSjqHoA9rLCwgm1mg7laYiVP6LN%2B9zDWQiASxFz1ueM9dDEM%2Fh%2BU8Co4CjcjpfB5b6eljJDy%2Ff5lIMZhOePza8cibJRjXAaAx0KVFR5eGzztmo9Ucj5dpz%2BQwUQvAEUwnL7%2F5LQ8b%2Ft8JEL%2B3kZXR0rk71vqY2hv13Yde4mKaTNWSXkJyic%2F0rGglrApH5%2Fd6R3WmglHMbb38ZVQh92KyrjQ1L9bWhoB3jxk9v8sj6JPA7%2Bzh2ieU0GnUYXZaEjsnfZgD6cUFQxqgX9X6%2Fuw07naM4zLAoUGNnEDdZXDkKJ0dncp0qlbAW1w2rlljMIOLmL0GOqUBzNcoGkmvg93ZfCiuEglvMNGkBQWgYXOpImjH%2FJhTnmPkQ1WPmCthBYEpu%2FW8o3ExOe7PMg4yszBLuHj2yNcIml3iyv3NMuiYh08R7U5UuI730lWHWsTs7fK46XROfck56CDdFJGq7xMKETJRgLIbURQ%2B53r5E8o1MhIY1lD%2B9NIrUvzeZurZlzrkrazcYRRBYbDIer%2BBmeykr1si2ZidRcRYLwW1&X-Amz-Signature=83facc2212ef72efbdfb98e7bb21ef32c91cdc6ac22f0873a6f596b98be36fe8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVI7INQK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDHgIMu79RhEQtxCT3JBD%2BssOelV%2Bho%2FArMnpDmtXwGPAiEAy0H8vVW8%2BomJwNOtTuUw6YvovcnV%2F6p2k75wl4WHE4sq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDFv91QN%2B%2FnBsbEsTGCrcA6f9uPXI1ljcyjzEvxCJjRbV7ny3B0GEHaFpz1Ea1wR8U9JPwi7cCU9x9oHZ3x2TSA0RPxptueNn3YNMX0cSvEKm34%2FM3DQvg5oCbbEMUMVpY%2FhxFauusnXzpRVQhgA50LuqhxBVSeyHA%2F3hvtNmHFUK7GO4OrajK6lmmLguDROkpR8Qs8DGIUQR2%2FPmlhODzugul6ntn1uq1uDmwGI4ToQGVYbc04zm%2FAgZFKBR71GGZsc5Fr4L35TsFnxctzxigEW%2FBWtIPUcKBIAjy34zPgwmeqW%2BXPRGHxaiUYJw6j1VDeqmvGQrQGHFBM9Vn%2Fdr78kB7hlCyQVvx8BGe1h54Dh67MtnEjh9dPOOmkPzMNZSvxU4lbdfNAtGcTGvlCWMSYDsvoGJ7lR0e3kh609beKqxdfAfaaTaWwcotQkqsgBo2I3iKTlcT146Q3O6ikkDkY9b6fPYehkSE%2BGJnr0mrS5%2F2DpoGbeucDAOGWFYFDRXZqiP00curDxD8aTgUpGnOFhYsJchwaOJOrzb8EE7WfkF5tnB%2BRBnCbrKG8OY2Iqrv6LabXMCMBmqxg0jwJH0HoR%2Bj1LmuFEK9fjmL8xBgon5DJnxIbhclP2CS2xQFF5ysEQuoXbPRmRkaUmVMOOKmL0GOqUBn9ommVJpM040fcWZI%2FLWjO5ne%2FrYlYm%2BVPWA62eLMFy5It6HFWSip0tlgXqSFtBjAbqeZwzY7Hco1QKnSSOU5zC1AmYrEtM%2BpyGQUwPfU332uYUFgsIK2X9D1bon1PkfkTwkGOzp8kaYm2%2B%2BxfQmcFdclDEXZJnmfJpylnchy0NkrGHGpckQBjNl6a0uish3urZh%2Bj9ZYpidRdvZHolVuZGug5fh&X-Amz-Signature=fc68c32d88757f5f204893b34f34d8adc0a1be43d912675ff1b5cceaadbc8fb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVI7INQK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDHgIMu79RhEQtxCT3JBD%2BssOelV%2Bho%2FArMnpDmtXwGPAiEAy0H8vVW8%2BomJwNOtTuUw6YvovcnV%2F6p2k75wl4WHE4sq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDFv91QN%2B%2FnBsbEsTGCrcA6f9uPXI1ljcyjzEvxCJjRbV7ny3B0GEHaFpz1Ea1wR8U9JPwi7cCU9x9oHZ3x2TSA0RPxptueNn3YNMX0cSvEKm34%2FM3DQvg5oCbbEMUMVpY%2FhxFauusnXzpRVQhgA50LuqhxBVSeyHA%2F3hvtNmHFUK7GO4OrajK6lmmLguDROkpR8Qs8DGIUQR2%2FPmlhODzugul6ntn1uq1uDmwGI4ToQGVYbc04zm%2FAgZFKBR71GGZsc5Fr4L35TsFnxctzxigEW%2FBWtIPUcKBIAjy34zPgwmeqW%2BXPRGHxaiUYJw6j1VDeqmvGQrQGHFBM9Vn%2Fdr78kB7hlCyQVvx8BGe1h54Dh67MtnEjh9dPOOmkPzMNZSvxU4lbdfNAtGcTGvlCWMSYDsvoGJ7lR0e3kh609beKqxdfAfaaTaWwcotQkqsgBo2I3iKTlcT146Q3O6ikkDkY9b6fPYehkSE%2BGJnr0mrS5%2F2DpoGbeucDAOGWFYFDRXZqiP00curDxD8aTgUpGnOFhYsJchwaOJOrzb8EE7WfkF5tnB%2BRBnCbrKG8OY2Iqrv6LabXMCMBmqxg0jwJH0HoR%2Bj1LmuFEK9fjmL8xBgon5DJnxIbhclP2CS2xQFF5ysEQuoXbPRmRkaUmVMOOKmL0GOqUBn9ommVJpM040fcWZI%2FLWjO5ne%2FrYlYm%2BVPWA62eLMFy5It6HFWSip0tlgXqSFtBjAbqeZwzY7Hco1QKnSSOU5zC1AmYrEtM%2BpyGQUwPfU332uYUFgsIK2X9D1bon1PkfkTwkGOzp8kaYm2%2B%2BxfQmcFdclDEXZJnmfJpylnchy0NkrGHGpckQBjNl6a0uish3urZh%2Bj9ZYpidRdvZHolVuZGug5fh&X-Amz-Signature=91e6927a68cb778870504e5d12a3efd886ed5d0a26b1932cff22fb49b20182d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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