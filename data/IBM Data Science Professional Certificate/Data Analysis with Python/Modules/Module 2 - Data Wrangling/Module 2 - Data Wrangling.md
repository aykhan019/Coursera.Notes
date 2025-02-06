

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635K7KLFO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCXVII6y4ETRM8kIowH1lSDPB0zxC4BRhdMPRDVsDvHaQIhANyJ4qj120DLDGiWVxyu2lk%2Bff5oIp7vsz%2FwvzNuhtkQKv8DCFEQABoMNjM3NDIzMTgzODA1IgyfsMjy89pnwToqxr0q3AORNMSCYGmAPN4LR83znrC547i4ddb3U0yvBigaMfKFI%2BLns6tMOFCftF9orMOgb5CqI9ecFpBVh5ptsYjKZeW%2F1J%2FpBQaF0ZzZtnF9cmVl4W3RmQqO2YP%2BEOrdJ0mkADBCPElNanl4gWoWdWaKFS8pFBBLmX3DjyPrH8wHNQrIv0tcH0ixfpf5gGxIy7fMyGe%2FiRjic2%2BD8HlXKW%2FyFFjrWyQmC9sdJ6j7z5ZuV%2FQ%2BcrxoDckp0%2FhYd4No3S4x4NQWSIKPsaSX0RQRBjghHYWxjKQw8sF3FRCAc%2FlIp4lg85oG8XQOJWTeLjkay1EJhKeYV4ZISOjyAH8ilZrfx1J8U3D2LHLRQmP7p44vnQ7Qfa%2F6cebpYEgUjtbykl1uNJ2rmeE%2B1Y6LVu34ooDYC26z3zaeYXuxgcbTRELlatJjN%2FdAMc3r10KHqvszhjXsEzAEX9Vrai128l5DmYLFNpzBxakeKZgoicQIojtsND0xcn%2FjHwS%2FBjTz8XF%2FBkwIj9dpa9oo7%2FCFPjdo%2FGDQaQ96LjGSA32rF63DnBCK90pyQs3G%2Fqq8Tm51bY3mgEG8MlHpmmhJqMFLWxee2l3KPJhIQW%2FQnKlcy7ivdUe0zh%2F9Qh%2F%2FNz%2Bqb0G9NMn5DzDz6o%2B9BjqkAU9SXM%2BlsE42rXBPWi7YGtIjPsH1Z9PTboBSNCn7%2B0PvSpvf%2BRQvh9VJ1%2BGVzsuFnRoDI4CTojX4qDBjCxvhhKSkT2DVO2G0kOgz54Uz6V%2BiGqsPhiT0ECOEnpFxVlg7HCSMZdU0XWr9irqIhEj6EuUjT%2FGwcUOVfMABH4US0DonMgEnV4fvD54zkeCEZmSYhyfg9%2FqpvfsC0aLKGRCanwjutPsU&X-Amz-Signature=1df3c564d567ae5ae2cada6a97419abe9d20e9bc104e696c1937ba78ccefc879&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ZCPBWA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQC7jH3fRvtfMYdni9y%2F7pJ9wKotgZ7TG%2BCEbivGE1r97wIgGt3eJWtEVqtyn1v6YLBJ9iBjRLeykNxXgyXYbUIbJXgq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIyB4Tlp5DqQEE20iyrcAyBUNr7PPrbYvB8mVTdUOFtQ32ix8FDDLL8j%2BrOj5Czg4fg0PsHIIhRMk3GaU3I1TV6J2%2FvzKPyeNEhcJzFHFeVlEbI8r%2Bkc43Avu7Pv6RGihRVKMdA0%2FNcuR5Cbt7v%2FQ6kVmzZRK12uXNb4I8DlCsR208stqXtGOhmniTt14F5Q%2FAzrUMj%2BDvcUwrPDDvzFwYfdjUHL0HdAdATY5FbGL4gZeQdk3F2IM%2BSr4Gp4UXAgMb3ALUcc1Iajrfe6Jz6VNcbI0VsRnz6I%2FbhHBiHo7%2F%2Bd11e08qf%2FGDSLm3guZWQPW9WCVjbxbn7q4qmR6SMH%2BH%2FA%2FnC%2B%2FrbLc%2BJyVRcd62jI2qaCDtoJN18xfs4R3GcloxtWLQXI3mWdz9sMosDOnFqiq11aJB4ezvhLcutk0bEOPWRX7%2B2tw%2Beo622K9JPBPvUFkjDAtv5nCFn5X3DAQDeN8vzOc62cZviUqnbh6PkFxKd%2FCgO70Vi69jRp5rczLgXEOA7q9dTOh1TKy5fK9GMnebHL8%2Bb6JrFwqlynLFJxd66jjOvoV%2BjYfwpzzOTP%2BprMoNvyIpmoHy2mj4j8QCrV%2FgGH62iadxkbE50xCLTuunM5q20dV7D2i4x8AbeIPEceZO5tSpdFN9ghMPvqj70GOqUBnGOcY2eT3MG0i1Xz%2BQr%2FQLbvYrbDPliQHZvrfnq1vCXaEHR4sUu6c%2BU%2BT%2FpdTH2lZHF7V7N%2Bzc%2FvBhkM%2FUsilUMoHfK0eRbVn7p9QexXnz%2FsEg89xa1Kh02TPoWu7FCvRhpM33ZuIlHobo2GthtQKF4IgG1lQr%2BWTGHeyKn6w3lwRk8ooKNc1W%2F%2Bh8ZaecjFcIA0GxUuqt8NaVoyNOCINRMZl9ev&X-Amz-Signature=82548f546d6edf52186d9a3b438b7f919c289fcd884e046790ae9cc1f7410aff&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNKZVS74%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIEX7AkNUdCVpF%2BlojIoGhXoh5KBAEd7XS38VNmlazv3BAiBOpgNpHAJ%2FszEZf8I2Hn%2B1VxRTDSYVH6rq4tmEWuyOUyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMl8qDX99KDooozXwoKtwDhBSr4X4TAYmYBej1beYNOhWscBRD5PIP1bkAUOaA1foU%2FSsueKJIcNz%2BgghwD%2FHViJqtgJVwJ5qDnazBH2MS1fqDxfL5QCWhsla9mXE1P9rWJX%2B%2BtZPwaFoI6vp6USHtcCpSsh0xDpJN11Bui6EH36osOjHA1rupe37XUiT52NwQAa%2FVWuVvsiaObNQ0UogVLEMzAC%2BBeuinIQjNbKcXkZg3UZU5vgZLJV67Y0yLuozadJh0jXnEyRVzQriIz%2Fnbr57hgRTK%2B4ssXaLvBj6y2SjYBDDLXwaFnJBwNgq73KP4NL0m3eWbl6wxqJ77zZI4IiQg16vbuzhhLHIaYDq80S%2BQp1tPnFcvrmvOx7KApK2pkDNvXkisTL6KGEr5uD6z%2BIPPlRcKEsMxLyJIu%2Fg6Pldc1tVUcPVRPYpV8KK%2FJfn4aMCiCSitvLyK2jYJbGelB1ZPff3rql40X2O3%2B44XCNQ0C2r1gBxoS%2FhNyEh9BFFMoKGjMafBwworE6%2BApX0GbTQnD%2FRTKAhg3PjW%2F43b9myJPa8uXXg92kxbttKnyl2vkUQBp0FSAGF0%2FA9VrpA%2FEuYLAutcqCtToIKBkU39DE7kihtwALOLBVXLak30HhTuJ4EPsqiVV3ALXq8w8OqPvQY6pgHMyq8aNbAWb9nRVuZnsyDchm5HsVcOeKCgUkaWdunsJiQVXws0zKVGbRLI4EZUjwXo%2F1sUcYIQWHOXRpHXdYiVJeGvLHqPmywoODAbTPj9o%2FaqSMfWE8Fl%2FCfjn%2FQGv4vYzR%2F2v0HnTnI6dw62rF%2BRQ7nbnFTX22IpIP3mja0quw6FK%2BqEH26MnW2d0APMtjzsrzSj69kTz9OpOM32iuMjkGxPXRGP&X-Amz-Signature=b1dec2fe8f1d5c305f1e7b951b7a2d82ba1220a2398a7c3b677d465cf5c3763d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA2NREGT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDyZCnT3L%2FffWvN%2BUGXdnbQxOaiTWZ9q6T03Gf4exqVegIgWgSuJnq37cblj2s8IkdegiFrqSnbfq8Np6NAfWJRTQkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDFiPjKjnyTl%2BGl8VfyrcA2%2BZJCokWY%2Ft%2BVCwN66wu97DK999bsftgRVnWaQayDhbBCA7ExwmURHN6%2Bk8WW8PnJTK2Fl9%2FYYgkoXMwP%2FYEkFtFe5IkwkYLai%2FzX0EVqnCfJXeDtiofelBUtUel0nfzQqnSBdpAfdfRcI6c%2B%2BkE%2BcEoKkiGi9IQ9qJAAsSQaIDP5YYbtNjDklXzxfwpHg%2B52yIO68MwfrPRqNB7PLaNjwBarVvF%2FTTP5cDsNp%2Bp8Bskk3nOQ8k%2B2YjBp5BQbUvwAzMzbe2cJUZkQYiccLjBpVNLwheYuwfjhlNb1mIPi7%2BXCyCV0m8cqxz17%2FYrX328KXoiz0Vx5LgGo8hK5F2zp4D7lLjuQcSJqLMyfCKf5sPcQCgbiH6QxS3snzISBYSjE6%2FxHqj55x2p0O9PvcBz4Ax7KOY7C8KaPEtsylKwHM7CcQeqPD7T3sgs5DiIsvH2HdLDuJcxQpSBS6miNHXkLdtu3o5%2FzFiuJ5xAMKQL0m7NItIsLvvUiGJ2rBtmZw%2BiN8cwbdypRh2%2BiRxgNfJzSWtfarkKtR0hSUlqIwf1O2q7xPW%2BoNEH5YtJM%2BB0np3uM5ByyS2cpBg4wrdb4f%2BC3w3OUHd6I%2BcWo9A3LoeLKnpR1%2FSVmG%2FFer4ZrBjMOXqj70GOqUBRELd5Tg7VsUAKPKS%2Fh4FcTimO6XSDFr3M%2F7JX%2FttoKja1T%2FymmjKFqLNyEtdeTideJhtdRLE1glQ%2BBb8Wil4SUujPNBEVrxygYIcyVMGWJtZxZELm%2FoBwHmTier5G5BfmsDUbG1q0b5%2F39Spi4DjvA1oHAdafWGvi47UzZR%2FgTuyz7Wonem3lswlFMS%2BWu05%2FiMSp8UrH9eYzs89IvOLzOzMHKy%2B&X-Amz-Signature=983cead5ec819014819681bc2f1b51dd429d5332beeea51881fe38bdb07fc6e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5NZX4H%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDYrfde4vc7t8u9uSF6HgjYtaEs3QtMpSIYJQdD7WVRMQIhALxx5a6gX2MKtwQuGIJv28NtW1fMeK6cbEoEUWBl5AFxKv8DCFEQABoMNjM3NDIzMTgzODA1IgwOVdvdID8BLc8fI28q3ANYjJIaknFM24AAGPZx4L%2FW5d5KpQ8881Egb3eOG0Pt%2FXnaHz2jk55Tz%2BEdOZTOrGLw53bfXL6SXcCZ%2BfQUw%2F9Wue%2BAZBSvLOgtMFm4EfaTjPg6ACEOWV2VSfDQIVfH7gRYEQorSK5gOGlA38y%2B22fB1Q3hl4yCm7voINN%2F4Ozt2w5b7ZKQyPU%2F6EP%2FmDuwD2gbiSIZCov5Ced7odQMsQvVFr2mqvNEAWfcroFF6uLe6ZOsJzVFNsaChLLmLnj2gPhvZB6g%2B1y1ndwddzraeg9hXK%2FRTHs%2FNWE%2BJqwyVhRadWICf4FVYwTJ8UDqVEJamkolfIOLVE2M0ZB6B95%2BZJNqCwEGExj9%2FLrnNB0F3W8yIEFtr4jiYd%2FdqF8d6U%2B%2FbRyg5zVxNrgRhfyxTAcrj6xC%2FKAwAHY3msAoVFHOG4fWYi2Ua91ACmLEb00AZyv5MaHHwXZKU9sseP6%2FkBUOm5fgJ33adlPvGbqzINU7hu4IpIfCdGHFEQz%2FSmSkW7O4wdj5lVUBo9WoWy6x%2FMKGlRyQQQDRSje%2B01Gf8pHTT8vyaBjM4Pl9o%2B7GTrSBSxoR36%2Bdc2stTyM9ea8ymlMW9EdP2JYNAesR0reIEK386FKs5xG5rf8zz8PIpnrbwjDm6o%2B9BjqkAWwoU3Kukahw9jqUBy%2FIKRl%2FFuvXfpe2GGYCD1xlOSyRVa8clnr6Gnjy6f9VQcKIDLg9kYni5iv9k%2BE6%2BrPRC8i507lGRveYX0lcDLXX4MPRvB79IgXihHXMCN0F5PFyaXYW%2B4h9Z6kBpoI7s%2BYMbtTbRJ5mHzioZFdPJZXBHeT%2FY%2FpS7iDiWcgVpG%2F0ECcvtmZiKiPiYYNSPrUqjFIc%2Bg6LLWUk&X-Amz-Signature=3ce45231404384bf8b63826682dc7fdee50db8737bfcb375b0a85e0754b9ea0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBUT45JK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIHbHeJf%2BE9EgLe8jdx916c8J5IApgBJ%2BQJ2owP9qIHxeAiEA5ZrYL5rjTT5z76PIGvnFKT7OpmPkRgq6zoh6IAIM%2FMgq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJNnBqQoJFGFetLM9SrcA6%2B3idReK3BXMtmk5oDUI2JUGwQy6q7%2BMwR9cp1KLqySSXBwxzunkw4tE%2BOfaiGZM%2FLSRikg6LO8wp7xDa7IT1fhQRYDAxYeIYt5FdpTsdg1t9oWkYITBRhkX0hvHUqgHu2CpYoa8yOd%2BvxWJnuJ%2B%2F1FjKsg4V%2F%2B8Q%2BXR3NwfCG05FvbrJHZezZoRnEA9mL1LqJDuqg83c1i08IVpUVmRWGiWV%2FLZrB1SvQongP%2FNctINA0CRpa37RBA8qdYH4wdC5x9%2BcW1vtZWimyO6rSD8DMaxaIRMneHjB7VioZDgCR%2FaiH3vbnwK8mdTNFZoiCbqe0UhToWGN29%2Bqy9ReT0ZD9lywFIDl7yYLc9O2V9iRN5Y1ZJo5E6qlGLowhdYkbrvgyWNLABkti9nQGWy5%2BXAvUs7EZlaePtEihfbs9dxAmbJjx49qYxBfXW6adrlkO15zyocRF45cDfxfePot%2FeA%2BFkT%2FkGr2YHU2Qr9gd8nHzaJzpvsYe%2Bn12iP1xBfIFSXdpV6oPNut1VJCIJ5GNKYIsafZMt4AeOrazBKrQhxjPDhp4rm9INrvyumQdTfWKx1iZPmb1AercWR4y2oIUS%2F4i%2FBImJrJf9HWF7%2BzPkagl5vLj43D1GpzwVPKsGML7qj70GOqUBnKuIGj0hguNF%2BYxXYK20We2zgPtgfxjuwhOUPRq%2FpoJzPMt%2FIWf5HhOpaI2JnvGyHIWuryP5s%2BFMVNEFlXZCB74kbR45Mh3QXL5ks2S%2BIUwo8nRUiiNLN4Ev0o17kARGO9cg%2Fj1pkuy9bfSM3UeW2KxRvOwlaoY7blawWdoAKT2nFcBY%2FzOTH6Y4q8DuvRbpy3vM%2B3T16ngk78uKxBWQA0zcJxYV&X-Amz-Signature=0e6b3b7adb7ca9926945469384df7e5ec0c0493081db9209083c3ecef5a10160&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGJSXB5A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIFrxbqaMKURch83a9i98oKSh1RxvQxYA8O8aiSqLgyAcAiAON%2F3Z2JB5AkbgH%2BIa2%2FmxRn8zqKlehrQI54dfrO8dSSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM3ydbgxqwBrW2mjGUKtwDLc9oCzH4p3HxOhmOBYg4H5FiXCsPOew3MzH6DiBaCk0jYBzMSxfjcAtR8FyUuIXG7%2Fx4lyT76DkYYZL2N7nc5b02Qj%2BKTeriryQ925a4hOTZ5MA3tzZqm06vKg2QNFwDrz2BDKYeL3H6%2B7kZYJipLAnp66jTOV%2Foqc79fpzM0ElsTcCkE5UMPl8NFeEmeUlZdwDdHq0Nf%2FHnF0%2FwKInegl7EK2r65HyHzt7PpcozHrmyWyf1k8Yy50TxuG%2Bp4ajRk5wwfy1BkYa7%2BrF%2FqCZWxAuLmFqn7JeaEi9U7FSWdFxL%2BTzd6JMoIoYtJ5HFRwfivhNktG1l4wGaWIoWEwCydxWUeABew6C%2F%2Fm0M%2FiZf2mFbMpBEytjjm8IlmMXNUYI9AJGf5YPP5tFYb%2FrlzjelVF%2FKYIqzDFctKNhLAtFAd8zfUMBXrsN4fGpha%2BRtUBhQkkKKQyjyml%2FBBUc38YhWNcmTFzGH2g0Lu8uQ3gQm%2BNETcIhcx1q9rwgGcWNXtM%2F97Vo4SEE8oMO1Wl1pCRWVKRwhFvK5nUtDN%2FZUWibG3owpS6PeeOgb2kOj91oes0mnlHcy0a99Vorcy%2BdSOeayjJVUyKvVGr62pX5P4lBtOEM0nQlNuehMmpmsr7ow8uqPvQY6pgESuNb1Rw%2FTd1cmJxq6ryG%2FadpG35xKQiZKWTP3vR5X3EQ94sk%2Fcw0bCbAcLB3MfdLo2WWjl9gsyu9rPfes3gPVnTfoUlIemLSNYZHRSX0KdybwT0%2B0vwCJUFP%2BbdnFsAAooOZT9DL3KeVTsb37DeDOKmGDWVqVs1fE6COGWx5Oi2K1cA1hFnnm3WfFSO0wQSU2inyHgdnY5Ov9CUFCamR6IutfN71y&X-Amz-Signature=360a63f1c49a892312e00a8ca080dffc964e0bd0b9a375d0135c0ae175349bd3&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPUITUMR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCICULjNYGBfcvCWVzMyRDjGHJkSyej4mqRkwJOA6S6MrmAiBdGv3olZVnJcOSe67PkmBpxC7KieidwCVlc03WegBTlir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMiPe%2FCUszV5PVng6uKtwD1lNrqHl5C4xT40oknApAMR%2FnXNCpbDzVbdf6IfXfNtoZZTDY7QQhs2cjCAyZqA%2FbY3T8V2%2FOayYA0kR4d2EA899SCCRahRQ1y0TEfTWIumISRHQL0DmwQJGNqlhHXjfuB7PmPkh79p%2BkGsGssUy9QICVlihyqFcILfBVnXSn1vcwzUpB3Q9TGWuszep5IilKPCIh78BwlYt43zo2zYvEWrjlYk9Zmr2E4Ps78lbx4q6o4lw4T50WgklaVQWJ%2BE7u1bawMvaVLls3B3oq6JxDjy%2BSCkmedsS7NZI8x20li1IkrYY8P9fJrTcZCXmdEe2V1HPi%2BWcgm%2F4N%2FF29FP3T%2FCa9SkkkipTkDTog5LolKwghJeE86CR0Dz7XYPkf9eHbGOU7MwR0wwYEdssKkboSr2GfViCoj3VLA6QJoP3kosgu%2FjalgVFXhV6UWbIS4bbopVgLFDDiH26CQHR%2BQphiBO0jIqWqY%2FQh9vqbCBM1DNQ41CmeiPACL9%2FE0xch6XNYhqGB3%2BnWBlxAoSB761K6NfW8VsjUX6SLChO1%2Bj0KuqvLHwjSm3xmOmqtPYgC4cT8DB78%2FxGZaI%2B8mj0qHTy%2BELo%2BlEiZzakeNpVWn0CaPf9nv60JUP05wGzQ2YcwyOqPvQY6pgEuIQ9Iu%2F65QBDg4jOD2KYwaWGVK91SDVfSI6EBpdh9%2FGTNG2eYBGwu0kzKfMpvBYXrHUq0izoe1ljUY%2Bh%2F5Q9TovWDRn814sfvPYLcYxEsVTGzCHkFjWpmbLqUFgj2PkQtNL8Gb7YgzWg5o390YHD9y8ILXK7Jtgoj1Nzoe84WMeeKuuWaEBx60WXAlPTrBJFB3%2Fc9tklIWlBPA2D%2BMo37id7CyaYb&X-Amz-Signature=37988a4e69ef79ebf7497278b73544927fc753bdfc8b7f29c158f8a7182e6965&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5NZX4H%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDYrfde4vc7t8u9uSF6HgjYtaEs3QtMpSIYJQdD7WVRMQIhALxx5a6gX2MKtwQuGIJv28NtW1fMeK6cbEoEUWBl5AFxKv8DCFEQABoMNjM3NDIzMTgzODA1IgwOVdvdID8BLc8fI28q3ANYjJIaknFM24AAGPZx4L%2FW5d5KpQ8881Egb3eOG0Pt%2FXnaHz2jk55Tz%2BEdOZTOrGLw53bfXL6SXcCZ%2BfQUw%2F9Wue%2BAZBSvLOgtMFm4EfaTjPg6ACEOWV2VSfDQIVfH7gRYEQorSK5gOGlA38y%2B22fB1Q3hl4yCm7voINN%2F4Ozt2w5b7ZKQyPU%2F6EP%2FmDuwD2gbiSIZCov5Ced7odQMsQvVFr2mqvNEAWfcroFF6uLe6ZOsJzVFNsaChLLmLnj2gPhvZB6g%2B1y1ndwddzraeg9hXK%2FRTHs%2FNWE%2BJqwyVhRadWICf4FVYwTJ8UDqVEJamkolfIOLVE2M0ZB6B95%2BZJNqCwEGExj9%2FLrnNB0F3W8yIEFtr4jiYd%2FdqF8d6U%2B%2FbRyg5zVxNrgRhfyxTAcrj6xC%2FKAwAHY3msAoVFHOG4fWYi2Ua91ACmLEb00AZyv5MaHHwXZKU9sseP6%2FkBUOm5fgJ33adlPvGbqzINU7hu4IpIfCdGHFEQz%2FSmSkW7O4wdj5lVUBo9WoWy6x%2FMKGlRyQQQDRSje%2B01Gf8pHTT8vyaBjM4Pl9o%2B7GTrSBSxoR36%2Bdc2stTyM9ea8ymlMW9EdP2JYNAesR0reIEK386FKs5xG5rf8zz8PIpnrbwjDm6o%2B9BjqkAWwoU3Kukahw9jqUBy%2FIKRl%2FFuvXfpe2GGYCD1xlOSyRVa8clnr6Gnjy6f9VQcKIDLg9kYni5iv9k%2BE6%2BrPRC8i507lGRveYX0lcDLXX4MPRvB79IgXihHXMCN0F5PFyaXYW%2B4h9Z6kBpoI7s%2BYMbtTbRJ5mHzioZFdPJZXBHeT%2FY%2FpS7iDiWcgVpG%2F0ECcvtmZiKiPiYYNSPrUqjFIc%2Bg6LLWUk&X-Amz-Signature=58af2821d29f256f544c2e6df187861e8e6ccc5891ef9102fe9abe891f4b27b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQYHUEI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCICJi4lmCBSduVuNfmWQuBtnfM0wKumbCZjsjsNnTrxQwAiANlxYKdNqwVXTqyYc9c1pM4WpyLaej8ueWKD2hWeEevCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMcRt%2B7OlGOyhViI05KtwDTGeEg5uAD7XqkaoyojTzmN4eAUi2Rhj8Wwn%2B2vxOOLFmBq40ucpMiHlhYlwEToDpJ63gOpSAuNketvuFwzLG5HhTsEIJilAQo44CLwtP91vI7WtCexzd1GNZzzAH7j4ODikSl0VyCFI2DhNAi48UXxlAciBnoDKGuBHNT5Fz%2FYyGt5ZPLVS0t%2B3eFwS1UUSwFoZx2QEt5Qbg7jWpYbrNSky3ETldLll8qHc%2FUK5WeFTZRee5rxh4fDvsksIdckUKd9CXt3v%2F0UHSGBraMvKysuTOdGMl%2Bqtj8O8y02mOrynDIRuhHoCUotKqSAIA2nddm9ljkVkUy5yBh5TB7PCR0NOX7fuBF3fSwVMrvS1ohyGnvdY9YX%2F4fZIwlOriOJoF5CNxEcvK73gN3AI53ASSm4YdyGkhHQOt9E87ZZig%2BKrAqi%2FK%2Bp2Lx8zDJ%2BY5mgu1V2oIEKZYZgUGhBZZomkaaJQIdVgBdXjVvm8ScVtD0Kzu%2BMgfQiEyE2wEpUEdLVeG1kVIGG3sWAR8crJ%2BgFe%2BlCwxdlCZDDcFJHtopTIl%2B7WRwekYDlBU7L%2FkASzHOQVTylN6nV5J5egtFLuyt7hJW27w4QOcGnVLQ%2BBPzNGhcMUp727NNkcPHmidiKcwlOuPvQY6pgHTbr9DWkg0CFcBxhU5owkQEt3OOV%2BQl6cv3Hve54%2FW%2FP%2Fau552jtUFsSq6o2xIjoSShhH6cVAHBxkPBcMDyflZX2U4UT7afseos%2BK58oKxoLEEWz3%2FjzWm42fosop296f0xOGrILmQ2CbQRbohYfadyVhlJyuNRnBYEcuzZjRpAMuC%2FJ7VuxYVpMbNODNnXpdOHQSU5B2WUOX%2Ba%2F7Gu2uOjoFEtG%2FG&X-Amz-Signature=47ff15b61a9f1cdf889d731e58ee5e197ca34abd1bcaa68dc14fb5bd1d1067b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEQYHUEI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCICJi4lmCBSduVuNfmWQuBtnfM0wKumbCZjsjsNnTrxQwAiANlxYKdNqwVXTqyYc9c1pM4WpyLaej8ueWKD2hWeEevCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMcRt%2B7OlGOyhViI05KtwDTGeEg5uAD7XqkaoyojTzmN4eAUi2Rhj8Wwn%2B2vxOOLFmBq40ucpMiHlhYlwEToDpJ63gOpSAuNketvuFwzLG5HhTsEIJilAQo44CLwtP91vI7WtCexzd1GNZzzAH7j4ODikSl0VyCFI2DhNAi48UXxlAciBnoDKGuBHNT5Fz%2FYyGt5ZPLVS0t%2B3eFwS1UUSwFoZx2QEt5Qbg7jWpYbrNSky3ETldLll8qHc%2FUK5WeFTZRee5rxh4fDvsksIdckUKd9CXt3v%2F0UHSGBraMvKysuTOdGMl%2Bqtj8O8y02mOrynDIRuhHoCUotKqSAIA2nddm9ljkVkUy5yBh5TB7PCR0NOX7fuBF3fSwVMrvS1ohyGnvdY9YX%2F4fZIwlOriOJoF5CNxEcvK73gN3AI53ASSm4YdyGkhHQOt9E87ZZig%2BKrAqi%2FK%2Bp2Lx8zDJ%2BY5mgu1V2oIEKZYZgUGhBZZomkaaJQIdVgBdXjVvm8ScVtD0Kzu%2BMgfQiEyE2wEpUEdLVeG1kVIGG3sWAR8crJ%2BgFe%2BlCwxdlCZDDcFJHtopTIl%2B7WRwekYDlBU7L%2FkASzHOQVTylN6nV5J5egtFLuyt7hJW27w4QOcGnVLQ%2BBPzNGhcMUp727NNkcPHmidiKcwlOuPvQY6pgHTbr9DWkg0CFcBxhU5owkQEt3OOV%2BQl6cv3Hve54%2FW%2FP%2Fau552jtUFsSq6o2xIjoSShhH6cVAHBxkPBcMDyflZX2U4UT7afseos%2BK58oKxoLEEWz3%2FjzWm42fosop296f0xOGrILmQ2CbQRbohYfadyVhlJyuNRnBYEcuzZjRpAMuC%2FJ7VuxYVpMbNODNnXpdOHQSU5B2WUOX%2Ba%2F7Gu2uOjoFEtG%2FG&X-Amz-Signature=8ae3beb0a51e17a9e6eb04fbe017795843ed55235768234da3b19a0ab423cb74&X-Amz-SignedHeaders=host&x-id=GetObject)
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