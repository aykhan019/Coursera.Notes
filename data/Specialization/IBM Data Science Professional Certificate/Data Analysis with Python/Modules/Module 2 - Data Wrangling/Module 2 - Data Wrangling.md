

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJP4SMGS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFXE1i8mlKZ1CfLOvOR9U9pLrgZdtESnifVrTpt6VnntAiBJGgMYqX7eAYglSi2vSRptPKWivdXR1tR897mG6%2BAcayqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR89BvozZyvSBLlyHKtwDuHe2FM8vi4V56OT8NokM4vqkwSlgfrxcH6HTdnF%2BWL%2BqX2M1Sdq1tao3MUfKYIRtuYiGsj5Z3tsLuvffpOi8qsBgvcZmx03G%2F%2BOYLvRQCYG%2BOaN%2BKwM2d2rGV3OIZSmMMrwY25ixli2lRENHdYtR65B9QwnLzOPevFavlX4myDiDP7HzpXWwei4XKnExMn%2ByJ68FhuUiIHX7RSC0SGppQp5u105ewNlxanjk0UQi47xZVWL867wwkIWbryDS7nmbjQntnL3ZNZ6nyTn3H%2Bt%2FO1NjM%2BmvRjhIE2fIrukvav5qh5gzsiI%2B9ilHsV6pdEu%2BI9VFTI5EjR5JtqDA%2F%2B5opVQR33X4bw8N85%2FERpzYq8ZVgLAa%2FF%2FKu5%2FssO1YCzVJGTiVi2VPxhTk6xH6dMYgPSlDLqpPYR4d1fV8bfm8SB7IJk2Aq6S9e5mvveaPOvnEEbnsaviAw0aorW6Radx8eFhheQdV0TYpaVEukx6LNlx6TQpKJXmWyQms4pnkOI0wKXgRlUiIfSb%2FwkZqRDKbVt%2BuUbXX66OVkMpypyLjDtOrYqlJpmNvzVUZNbHq%2Fq6rIPPEB%2Fbkz%2F8qsF13hnQH6bRP%2BuffrB%2FI%2B0E4VcsrLitCP%2FpCc3kncNppph0w2tbuvAY6pgF95tMkOIvQjWF83jzeSGbG0Bp5oXqFVUvdf%2Fo4Dwgwx6E%2BGlvYa1dVep0770Yoxe%2F6BV2eyS9rnivWgi6Wwqf%2FhB7%2BDymieAps6lu419oAwcirqnSIrbcdasYJMVhbbwP3WVUvbctUWnNu275DsMYBJJ0r%2FQ6dvnMdCesNsktlLt0Re3V3%2Ft9rZRYHAr29bukxpHeFIoKZKn6XQAhzVVw4ryPmtsAN&X-Amz-Signature=edc29de0b844cfb1ec34a6cd627a38e2b51a64cb6f0fbcc22568bf197fc1223e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHMTPN7C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2Mr5ku%2BafBJrzUhG%2BvYlC0dHJr1gjY%2FKtqsUFAlteyAiEAuSOv0bZjnR0jVWxii1etavzDP9cRoCNAiJ5pwrtU9CoqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOQ5mLOsTiBErdYP%2ByrcAyZjRPfns59%2BWcAZtPdtbN7mxeTSW%2BUCN7CnRcpZLXrMpp6iu8iKZ9FSbr5tKP9T7sRyAJ7G%2BZsql3IJ4t6xv%2FcoqT4XBeqo5eETeqkvjSERMHKqXA9jTgdMTr0IiiuIVPqAp%2BdGCTweupw5I2%2BxHT%2F9jVg6tHzHgB17eDu2L%2Fuujw9eVncJxFLmwHDPBBKZdUzlkOfAgoYR267JAN%2F1wotqTSdxKtyuhEC3k5FltXv%2FpQAMXIdw43mBlKBAd2PXNUh82EBzYPVhSW00F4k%2BW18EQhiw24%2BN0qEbCsEZgeS6Ro%2FicHq2%2BNIRWK969elaVSgN6164IAdO9pk3fsn%2Bp%2Br0hyU1YXHmN%2Bct4CpOumrt9dCfR13RnOxBWRfSz33Ifuh%2F%2FOIpl8QrCSMf3yvV9LvQzorXHzdRLue65l5QLJEfRXTNnFstffZRcIWhA0efeOjpgv6NJg63KJn1%2FDdaEC%2BLdLHOrUi%2F%2BGp7uho7JCCehEfB3x4O5gmunx6hF0bkWLxWgDURUlf5vTZDw%2FBFWQCLSL3x35TP9ybgCgrZYQe3APxt96aMgeO%2F1EsjE23O%2FP5Bg0imNRbjok2JoEEieE8%2BCCsQWxZvj8t4g%2Focq1ah%2FRL42zv7lPge9%2FvAMMfY7rwGOqUBlFKQetqtSQymKxyimfVVYxGOQQ5VMpu1B%2BHQVJDJr77FYnVpw2%2B2omFLVS%2BjYiP7JZ%2BfhHP6huteObw3Jawr7qRCrO19n17GZVgU7%2BzyA8tFplMt99q7qe5mqZNDKmrd1hQjaTnYNqGpsWAT%2Bv72KzlurIjtw2AufrOnatkmVYPDN4k3vpJ7uSLZ2XpNXse3CrNjSrip0%2F0zU2bjhmxt9u%2Fphp6V&X-Amz-Signature=adbfb75dae615df8a6585a51c4a40b1fcbbae7671bf2263e42213be154ef1c39&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5VHS46V%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCp9ezSSuKjyf0ukRBeBpgz1nRj31nFJm68JT8qAk5QZAIgdncTLdO0ULkAWfpQMAenXkgz5yiMkYWmp4CYJDNTzJAqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7r18xWyDSHNDg5LyrcA6hr243h3G6IPoeI0oczzhP4ELs9hKY4DDwU1HI%2BnXOp72CQX6aTWt5GfTaotISimkzy6wAmZALa6Je51dKYbgZsAKPP5ciyP969DFbe7OMDA0EKQch1U3vaYsFdvVlmuNThEEqFXGvCVJZouYwCR8YZVeAZzRzpG2AqRWDKHuVuBu48WlZ0sLRM7Tq1bQA%2B2DLOqorv%2FSauEQnZ5wyVI1QPdbCzd%2FevWyxjsMKymgis%2BqmV1nHmV4rYoiCSLK9%2B3bSZ%2BILahZKYM9Yx6k7TRq%2FCvLigmoglPzt%2BPyArSyH1saXrzx5%2FTzevFPAWdG8%2BFdItm3pPQ6T%2FOPFTZ3Zym7DFi3VFJSgMdbfFIv%2BzGZFdV%2FmKqa0ezf7CwmM3uqqd2Zac3ipqL5KiMFIL8P%2BcAKLH1aIv%2BbL0UyvBwZtv2E7Hq7RZ2DuWQavHOv0EpDQ5Rvs8hfrky6QUow5QuZ4DiMbyw3mJAvVi%2BmD7aqbsudYZs%2FnNkIPcyom3QQbkGCfJeCZ6JBYrAUbUecNwgbQsplEIfmhyESaCD4t6S3bYGC36L6P%2FYnIl%2BotyGNDnriHNMKlAf2jdfacwUBsAI4HVeEZbr8ELpP8vczcV0DhG8oKpUOq0%2BhqNXAxC7%2BJuMNfX7rwGOqUBOP03PH1D6FYQzmR%2FYBoKisBpEBIiP9RS%2Bz%2ByOexhsqWTVY6zKCsBCBdf5wN3Ps%2BC0eTSq5mPh8LXHXv%2BQNgrv83hwvrUneXbGQZaxsIo6%2BRGcOUc9wMoJjir2nwXhD3EfeSpwXaCYZCjt8Zpk6OnBeCDBIbSS6t%2Fu6r8ej5xMbYlNosbJ4rPuty%2BjN1Gj3Lg5Th2OWrut2fsREN4uYYQuQ7xqBiB&X-Amz-Signature=2ea08b76a042a9f0ececa5ae4828cd4cc9f777d17b6ad0cba63255bfe6d22bb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DOHUFJF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmQQuh1LJefIq4wYGalp%2FBd2XcieD%2F8UwxMBv%2FvSoPUwIgW6fKIz1m01pOAqsLCDBiaKPNA1j6NsGDVrnJJBiE4o8qiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD62PJiPOxAgTRtNRCrcA8gCPbwehAhbuIjTCSjfMRUkeiL0XmU1IHbmAa5L4xVjBNh%2BcVtt3uV4kjEzyxSkuoeZp3AOkWs3la7tpNsEIijW%2Fa8STc2PhOBtMisdx6Z2NEPIF%2F6DTPkbuUYYsNBWUY4l97f09U%2Bq%2FAW46nwk4nAIxuKCojK%2FpQPnFkDciSWl7GutbVipHbK1hp33UqWUrLxS1ZzqcYlb6MKkVkWl%2FYPoWrGwg%2FdEFnhz3I3HZHY0VIvaJbHtUtOxx52uW%2F2i9aS6SjyMwikKXAMUFwCi2S1l1EARWyt8NODQz07c5Y3uKYZGZIagHbEHr0e2A9weIG4U8IpESLKkLNaCRN4ySh1Oz4KK21BVZQaRd83Kuwm4jhi0QtacQL8DRPpXq3cQer8y9qfwjSByW%2F%2FC81ChFyrkEUg9H2lDR8ofzVauSYObP6JIKlnIyV1clYhAS3dSbvmtUF%2BZUFm2sj7hPydN1HSSpDijX57jmyoGKUc%2BSu0fPJ%2FTRfQ2vrHRk%2B2JXzErx3e8NTjllZ88HdpD9mWoCjvwY7ZYv5jHRCs7LwFVRqNh1HVgeJRhAAvcUi5A%2BFPBmktopg4JPB1c%2BErHrjKety8Gvw7xi1Mwzjk4zaPByrfmuZDqT4qpNyDPyVAvML3W7rwGOqUBMjgzTCP3FUAw8Xp0kby6HLLmJbEZXzOuBFFF63GyOmAtDBgbJTD0DQPSV88bhYdZTr3twxksHBGQi%2FmAlkQ8mDFeGKsw%2B107PP%2FqSRNgWWC%2FONP7zCjrFydwU8i3L782nkehcaH75C59xzAYTQbOyggNEMaWeTzHBG%2F077XM%2BZ7h7aIHYRUymQ8oxlKz0kYy6YcwqJrV%2BHSQwIl5vnQRL0bTLOMG&X-Amz-Signature=dde62728e5cf96ad118da6d4bff4b4ed19f86da4c249ff1df8198cdeafc5b22e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677Z42ZS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZRjDPZdC0GmcdesWh1np3EnrPW%2FxKZXKQ45v78vht0gIhANbKff4xViR9FHOcSHGhhfA1WJgvUTQyv1vemWEkCWMQKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIJhRkqqJvO47GbYAq3AOT%2Bl5VD7091phSikFohrFMi98GTSIjj5U5KSIZ7WlTteYBVymAYIVZIEPGJOv80LaqAzu3wGE2BSzl58VxqxzOXX1qYsNWMWVfsmwUfGSEe0IZtloL6EORyziwshX3HvFAbVGOuCOWXrIO%2BH39J6adOuwjBPWY3gKDRcXa2uLROZ4sorKt7dwaIK5T5LzdUNMyoLstnjAjJhgcuL7ilbkbAOx%2BBwJ7dGB1TijCP2wF5qYZjzrsOFdFP2Pr6qdXzCT%2Fzvk4q2tD6JPpqSRa4RQiS5imZoHKi8c8zdb%2FiDMND6MdaPI4bEdSuTFP570EkW9kKdN9ZqPN6%2BEePH7Fd4v6hUB8wANP2va%2BemyeeYONyc3YXD5dibwwd5wLIte6WjIKqSDtNGsYX3OEDiE8Eg5JdyXKs1S9QEm25hzi%2BGXxZc0irQQYkb%2BMTGv%2B%2BJlu0Y6McVe4nDh1b2vYoT4FlVF8F1xGmcPMJW0FX8yu0TBe3YqxSgDJj%2FQa%2FWnsNqSF33PdHV%2FtLnV405yPrynx5p8394j%2BeVMwiRoZ7tzeofqciwXHS7mQk7%2FfdS%2FDExQ%2BgRfbrtJ%2F%2Fq3MeiGCPWnp%2FFzrVuIIscWZaZJYT4GwIpFvd7lU7f9m6938rKo3QDD%2B1u68BjqkAZE%2FrRcAuJoX7sHURl2BL7u1%2BNcx9H1ftxPdIji3z12U4PRPgCJdk%2F%2F9Mao8Lj7TxgcJrBTnefDmef5LVRf9Sq1bx18rrAUExNsVeEolpOCE0krJZNNC0%2FdwY8zTl2ngcikyb9HR8dlEtaLxi4GRU1Pph1t4JpF8H94MUqljTvsR7xwswp9n6q7pBxNWX9ivK7itd2LudDWaB0Jlj3L6ULEhhJFt&X-Amz-Signature=a09713ce0d621dff8cbecd02e279b7398cf5590f0c3f29c8d4d9711fea1c1c7d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD2Q5WDQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGGBRQVbJMd%2BC7GzJbse9AjjUL71POdXXVnoUuTNyXyOAiEA39g0yC3KTFq0uKDtYeR422SYpK4zLaPkKoiPd5cp7UoqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDqyyUr%2Fv0z3D1RMhSrcA8O20L6FVuF6tLyezaRB8Eq%2BDzVC%2B8yXi8wcwoaq6HO7HB%2FjVDK6RzmuK0AUhDmg%2B1mbW1Sgk0PMXWBcqSuYOgqgmqK5eMcZkBiYgtkXSfCkaR70ptPFyVX9JFkXnWsuS1%2F30cNuRhQsG4I6yApRgc9w%2FBFZzTdfDIPn0BklxH4LAb5bY%2Fx3Mq4RoDgbdyukS45knXTbFc%2Bl68CeQYGZSnnRCB4GiaGCW7hMEu9YAkWjjS5Yi3j%2FRCerzzOhX4uzEkpQ9uMaJjZPCMAuDR2QcQKaMeWZA6PD98sUEfRbymkix%2Bv4W%2BLvyNj8PES6EQZvCUUo4hCYCopsnvBZpJ5mpsTlAz4DiXIAlsB9jNhCHhb%2FgHE9nvPRgCroiF3qKl1WQgN%2FzlGDiVinXlVbMDysN%2BK87vm2tfJ0UfmRRRxIrKfAJ5YWtS61ZzATvImF5aWhhm7t7A%2FABJPVlatqlxydigqxuFi2ccvIb6dvmxrXyeJJyRBBPdoMDS1kHPdXBBLXnau1SEHM0d8mMb32Lqhf1H11NZhAkDjbxdqZBKAghX9wU19FluCAnn7rAVzI0ZOddFsGc625PjEm5F0p5Oa52AJRfCpx%2F%2BEym3QLOUCT8EGAgXgmlGaauLKYFCK9MInX7rwGOqUB74FmRQ3DS9nQQMtLqOnlGjZicaqI6O5vc%2FP6Is8h%2FRLlykgocXFM7Zi9t6vOcYIO%2FMREs5aYy6AMlNdnVr807hAoU3P1bn4qKFkTBx2dUjPunkiTlvBt7oMsheNp4ZZTqAB8ZrYlNiPwRfRqGAHx5VTjY96s950zNh0l2SiB0sq8aoUaFrg7cXGqQ41bYmPTB8QXtbSu5e626IeY0oGhLaZAr5V6&X-Amz-Signature=128dd999f23e5ebd795140a1732723c930fa0491455bbc67bcb93ce39e604019&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQXEEAMM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPQFlcuU4kJYOuC6P0nPWjpjWBsL5Yoaf3Eh7nidNiaAiArXXdJ7rxhraEujR1QWwheYm%2BMfjQXKih7SeJWIq5uBCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BwgcvwSbz%2Fp61t2sKtwDaq8zxUWdSfA8Z4bcTM8Y37FwtYpDxmJfInWBwTB6rh4eKRcYWJRFpe73ORWfOrM1JikiT12%2BPBrH8EKW7JEaMoD9o1zW2MZyURKZb%2FBbxBquQsTyRGszjGyI4XEGnJQ%2BlgXELTcgdkYtNy7uti85Pb1nJobYUR7em5Py8PkLgl1yQUcGekEZ8wlfWRKM%2BQoSP9lQQ%2B82YL1QiN9YhhYRuv2mDgMoC1qUVf%2FuJBrGgpZNgPYsvHt%2Fm0AqHt5kXeK%2FlyloAYNE1hRSAxWSoeQ1H%2FCpRrieDSafQGvVE9wnvBQmCLCrMmyz6xHAdDeMYkVGFxVJYynT1nck1Zze7zKc9yrpl4Yx%2B2WvIgQP6W2PVmilf0ek1O0DKczuPx%2F8NtzdYXXqii2nMM16WrWEKfMtxv%2FQNZw8cElsLQFMdn36g8Ffps%2FoUevIDLOQ2fESDlfmr80LLxcj3LXMyLXbV1%2Fnhsfv9apw0CX15ylFE1nio1D8zBRhsPyAIELgd7IdadEsm1chPt2WxWmO7TVbj2C0ofIF2hmw1%2FlWDLkU2auhTxv0InC9XxBN%2BLR9hr1%2BnzMuHGcXgcY0%2FgS1ls1CYqahe1qRDSjF9I9rphMsevyNZ1e2StUqtupq%2FmMx2MQwhNfuvAY6pgHxxqncdN4FiU%2F%2FAJ0hfFU%2FetjzNAiPoE%2Fxe0ok905Awuyb4UTuHtlX%2B%2FGo6aTH0bmab%2FlZ%2Fbg97ln31TOPj3Rgaq5IkaXbBJjkls1ViWB64EEZbbVhi4vPId5JUVSIGvDSxMbdQmmtjxMjJChd%2F50Y95Nm1cvSDh5vyijLUcU691zrGj8OeKIawiNCkpdUtB5qKtIkeYi7sofhwZsXa8jRd612RGUz&X-Amz-Signature=505475325d41b509811e7b53d2511d05d1803fcaa38c417ad7b02241d7159460&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2RPGYOS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGjbOZq%2FfPD5JGvvhp5R5RNY6iqAWYPBXKCM1Ys9fF2CAiBfZV93y11Ta%2FYPMDiCM7CxoqHtXk9jIVHwpOgW9Dkr%2BSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX%2BPZChgxNBg6HhPCKtwD%2Bf9XV5KKsxNrN0DJknhN04veLbshy9AsyEi2%2FfsgoUgc2vKdHO9M7S8m5WaWc1yq3HQ9w9WSCRf%2B2Fye%2FSYFEHQ7dDATb266dl%2BDjYsmv5%2BfQ9PtVcKrxlcXvxVqMisrqcpGhnw5oq5Re7PMUHxgYAq0EaPBKJrpixjJZ648to5cSS1eRHPNU1WFLQ9OU2CRrQ%2FNVizlrjLiiwJBjuzjEdjiyUSBmQUXgkZ%2Bg9I3XPel33bVnfyj9JvNDOWPoMrDUSI%2FFPrGpu7ti0iMUKlUcaJ0MvkOjNJ8dvYT%2Bc30WzMttdEEW1vA6T%2FD3wEJ58D9GW%2BbjKcUzeS5Bn%2Bsd1L8%2F9I2Riew%2BGVt4ipSOf40p3v4lQf%2BkeTjUXt6aPZcS9zA%2FEV5k877wG2Rb%2BJ00NKyGolr3xirKpv36Pft58HyBI%2FiVYbiHjF%2F3BQWlA2ePrgi8mwuFJGc301XCunY%2FbCaYRBzGk36bTDh%2BdfYDKT2IFf8Uawlh6%2FAhGfSxn%2B4pa%2BQl1dfofygqQppjFkV7x0vEjXVqp9bkQD0KxXahuGg8%2B43vM6p1lJUKHoTXz3uzRZjcjQ4W47kR72bm0oJxEPh2RZSbmJSmTm1s7TMdDCCl2b69%2BKYKURm0KiVqvUw6tfuvAY6pgHCx3OiukiAypCdrDmfHIjFa%2BZuQBYWZ5yd2XfhUEL6niF2edX%2BNBzWhKZvvLnmISPM9cnV%2BlZO3i3p6WdFbqbsiuvByklwXQLJz6w06UOAuu5U04dlc6nIZXyfMRh4ETRt7puv0x%2FkIqjor1tGcZUSHqFbIIy2m94EJilydFuQdC6WQvKxPzvBstwVWiRfGB%2B%2BWLwiH5GL7M9ibaGpTKHCNDH7fYAe&X-Amz-Signature=a640d3bb6ad87415b082631b65a6d36fc3029cefc5267fb8cd2f326782a8a273&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677Z42ZS4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZRjDPZdC0GmcdesWh1np3EnrPW%2FxKZXKQ45v78vht0gIhANbKff4xViR9FHOcSHGhhfA1WJgvUTQyv1vemWEkCWMQKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyIJhRkqqJvO47GbYAq3AOT%2Bl5VD7091phSikFohrFMi98GTSIjj5U5KSIZ7WlTteYBVymAYIVZIEPGJOv80LaqAzu3wGE2BSzl58VxqxzOXX1qYsNWMWVfsmwUfGSEe0IZtloL6EORyziwshX3HvFAbVGOuCOWXrIO%2BH39J6adOuwjBPWY3gKDRcXa2uLROZ4sorKt7dwaIK5T5LzdUNMyoLstnjAjJhgcuL7ilbkbAOx%2BBwJ7dGB1TijCP2wF5qYZjzrsOFdFP2Pr6qdXzCT%2Fzvk4q2tD6JPpqSRa4RQiS5imZoHKi8c8zdb%2FiDMND6MdaPI4bEdSuTFP570EkW9kKdN9ZqPN6%2BEePH7Fd4v6hUB8wANP2va%2BemyeeYONyc3YXD5dibwwd5wLIte6WjIKqSDtNGsYX3OEDiE8Eg5JdyXKs1S9QEm25hzi%2BGXxZc0irQQYkb%2BMTGv%2B%2BJlu0Y6McVe4nDh1b2vYoT4FlVF8F1xGmcPMJW0FX8yu0TBe3YqxSgDJj%2FQa%2FWnsNqSF33PdHV%2FtLnV405yPrynx5p8394j%2BeVMwiRoZ7tzeofqciwXHS7mQk7%2FfdS%2FDExQ%2BgRfbrtJ%2F%2Fq3MeiGCPWnp%2FFzrVuIIscWZaZJYT4GwIpFvd7lU7f9m6938rKo3QDD%2B1u68BjqkAZE%2FrRcAuJoX7sHURl2BL7u1%2BNcx9H1ftxPdIji3z12U4PRPgCJdk%2F%2F9Mao8Lj7TxgcJrBTnefDmef5LVRf9Sq1bx18rrAUExNsVeEolpOCE0krJZNNC0%2FdwY8zTl2ngcikyb9HR8dlEtaLxi4GRU1Pph1t4JpF8H94MUqljTvsR7xwswp9n6q7pBxNWX9ivK7itd2LudDWaB0Jlj3L6ULEhhJFt&X-Amz-Signature=9c524b17b3d313b5bfa43bcdcdbd4c339d7a8cdeb608579cffcc4da0b7b0a74d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663URGFSC4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0nB8ugra8l6tTDYNeXfdE%2BgfY0IF8CKilI9tqEMluhQIhAJsWWBD5kV0YWo1B7S2%2BU8n13Hzu1LKA7dl%2FZX66i2DMKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgLoJ0JmTuKaFtEIgq3AOIYnvgPFPHY%2BvIMThClz2f7muLpmZ84um%2FoC6hLutFs%2Bks5ODjr1YRCVzPOYEoQeFy4oeMjVxudBCTmq2sdZqtmfHqKxcycO1loHFelKOVGB9HsY1gzmeNjXTFSvg7Kn0Uxc58sCT6NRoJ8zTcN1g2L4i%2BSYyixwadKgkNux6Z9CfAsdH1g87hjpaPGq7YrzpBQ%2Bh6f5dEGkIQ6LNg%2BsPb%2BhbTwHWpBdx%2FBYtniUxdLqk3WJchkccY2hHhExTMyoM6obNtzWUeggqJYzJIZn17A0wtZXiSz78xQsHimPMzaXOQiqBGy0OcD3tW%2Bro%2B1bAhQuE71YTlXH6tlcHa5gpwBDYe1xQn5VG1wNbJ%2BPN4S82ORiRCguiUZp9xVPbW7jtgxzTE13A4PMISESo9LZfPPx3kr5k3z%2F2kyRBxu2%2F7HByEXKecjICKveZOi6zPpotzD6zJ8BzSDlkK%2BC%2FuYPSxXxWSVVFCVpM%2Fc1MT8%2F%2F0MEnHKqsnbimEz%2F3%2BjDc%2BerpeP54f%2B4UmWZnW%2Bc6s9n7F%2BUQHMQ3q%2FHo5rwPtbyXWShyB25WGnHHGTE0QlmFB%2FATC3EOuXEkpfpiKWPcJC8AbrT15NzkExZuHAgfUUtC7Q5vk7rFcK10k1Ei1TzD61u68BjqkAcdogpUv1o1htWsTPIaXLLqQEIEEdYVqUky46mfJcC%2B%2FKxLRoZMgPY%2Fshd5kKkhzpktH4DV9cvqwisX9bN8H%2Fx3eR3Me7SD3m9e9z98q8eq7PU%2BLVJIc3tTOkVaL%2FBrUpqalltEygZwl5kHjCHQgKUmn8OJQ8wRu9oxMXL3RvEL1Kpyip90gUPDKuhQmwqPh8ga3TUDWuPUq33vpPG9z7GLun26O&X-Amz-Signature=c713afb7656c37686c00fe468ee751661e3d09ee3954d0fb687f4df97a9642e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663URGFSC4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0nB8ugra8l6tTDYNeXfdE%2BgfY0IF8CKilI9tqEMluhQIhAJsWWBD5kV0YWo1B7S2%2BU8n13Hzu1LKA7dl%2FZX66i2DMKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwgLoJ0JmTuKaFtEIgq3AOIYnvgPFPHY%2BvIMThClz2f7muLpmZ84um%2FoC6hLutFs%2Bks5ODjr1YRCVzPOYEoQeFy4oeMjVxudBCTmq2sdZqtmfHqKxcycO1loHFelKOVGB9HsY1gzmeNjXTFSvg7Kn0Uxc58sCT6NRoJ8zTcN1g2L4i%2BSYyixwadKgkNux6Z9CfAsdH1g87hjpaPGq7YrzpBQ%2Bh6f5dEGkIQ6LNg%2BsPb%2BhbTwHWpBdx%2FBYtniUxdLqk3WJchkccY2hHhExTMyoM6obNtzWUeggqJYzJIZn17A0wtZXiSz78xQsHimPMzaXOQiqBGy0OcD3tW%2Bro%2B1bAhQuE71YTlXH6tlcHa5gpwBDYe1xQn5VG1wNbJ%2BPN4S82ORiRCguiUZp9xVPbW7jtgxzTE13A4PMISESo9LZfPPx3kr5k3z%2F2kyRBxu2%2F7HByEXKecjICKveZOi6zPpotzD6zJ8BzSDlkK%2BC%2FuYPSxXxWSVVFCVpM%2Fc1MT8%2F%2F0MEnHKqsnbimEz%2F3%2BjDc%2BerpeP54f%2B4UmWZnW%2Bc6s9n7F%2BUQHMQ3q%2FHo5rwPtbyXWShyB25WGnHHGTE0QlmFB%2FATC3EOuXEkpfpiKWPcJC8AbrT15NzkExZuHAgfUUtC7Q5vk7rFcK10k1Ei1TzD61u68BjqkAcdogpUv1o1htWsTPIaXLLqQEIEEdYVqUky46mfJcC%2B%2FKxLRoZMgPY%2Fshd5kKkhzpktH4DV9cvqwisX9bN8H%2Fx3eR3Me7SD3m9e9z98q8eq7PU%2BLVJIc3tTOkVaL%2FBrUpqalltEygZwl5kHjCHQgKUmn8OJQ8wRu9oxMXL3RvEL1Kpyip90gUPDKuhQmwqPh8ga3TUDWuPUq33vpPG9z7GLun26O&X-Amz-Signature=08d2f4822a2587ccf6ac10be122442de52b45e64b8602554e76ee56a8c58caa6&X-Amz-SignedHeaders=host&x-id=GetObject)
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