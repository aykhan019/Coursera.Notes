

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GWG6EPP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD35mybD%2Fuba5EQlaPWhd63oPc%2Fk%2Bi2kibLywK1dIIELgIhAIq%2FnzrBTg1NHMLN2kaE0wTN51wAjytVgJkP2isDXoFxKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqQcpQTcBnHDcgXIgq3AOhUj6TvYDf35sKVePYcCck0NwSE7hnhJOuUv1NxgxS7l3Th9o8gRpzlsHp1Cyo2QkfkB02Vh%2FA8JCJJBXbyMUdAEQnEJ5EiWd%2B8vOVE9T5z1y0F4GPQ302Fv%2FI6%2FKpLoTWkMb0ULH7ylnGVHjM2xK%2B4DzTCH6qPbb7oACLQrxmV4DVlOSXJ6hKwegTyDufsodspN4Tf834dR%2FC5%2BSlH1vc%2Fe88GJSZ3TT7x8Pr6ilQotflPKZncTJmaVE5D%2BuuzrvHNvtENF87UC%2FuscVKBMp8fF8Ow2AuA7dG4Y2LUnl%2FoJvllQfZPclXxa22reP6JJP0IP1%2FZBWCvmTzZ%2BGAqw4rDPY3DO8EzjOq6m8HFJZuxAziT%2BRrjW%2F4q%2FwfauC3mAg1qd%2Fc5yfT2Epwhpq7o27dnsSEllT%2BCCP303NbVS7NncdPBIHEMkIsy6GoeFnEfeSXNmAsvGGVDZF5y9xpgxLgTyYrJO1qMthSmmF2JWfuWzxZ%2F2Pj4vqa3C4lXlu1lb0%2Ftc41X5HKaLymDR2TQiZrRXArV7uVtTll7UUZR6OyWbIJY1%2FCrHmQ8EyCnq%2FcDQi%2BB5b%2BdmLvP99sI%2BToZj4%2BYyP%2FoVqzwypwqg4zL1vL8XhhL%2FgeNXsw%2B3Vy%2FDC87PW8BjqkARCCx6U63xlJOMjj92b91aBAaE1dDsNQHxwyi3vLBm%2BIdg572iefXhuYOpGNULSbrDyWP5Bknu6hbn7YBFoTweRPn37TXUcP%2BiNG4J1HNzANthkkp4KAWUHAy%2FqG9rmSJFBtGwfWxmAsyw2P0fxYTcKTCrRpyN8HlUkY0ne7DOQ%2FDUOzWnZwjG65qLeVNlsy6BoDZ25vSDoT6B3QtP2lgU%2BfRo9e&X-Amz-Signature=e7d028c9ef4fa1ca27e9195a031a964f7d254a1ec998ac4ec624ea517a600d88&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7PBP3X%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6%2FIBZbbPbCKe1MUa2LD4yYWLosw3ZNd6I0k7GmByy7AiA7GTsqbSYxAaoCUJwA1dHI3om68ZHjibn7jDbySagfNiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnUCeSYZWBY%2B9ag2iKtwDCLyD1Q55A5UGiG1T%2B2OHeK6cfcz0MWkU5HMtsHPW9C6WQX05%2F%2B9jYqiwEkJEd01yPz3I4Tbe6dhc5zLwbBQXtIoSXL9uNBrAd2is6rH5AWwcIKEERYtBWQRX4P4g33F91%2BbNQyIyzXgVhRsmS3QeFVMkNBwxzXy5VMuJQkRv3oOiDc9tu961ntyNQ%2Bm05%2BurCIvfdMbJUawGcNh2cNl0QjNvJcBsg082ME2NstAg4YC3aVCb1oQifLcbjb55a2DdDdyQKGW4f7gKtltudNAyYS7axbwa0CqKYvhU35Ytd5J%2BjJ09qw1rKKxzdJkmCyBSfTSNB7Fzc32Oq7MVKyMXy46%2BjezO4YEujEt%2B%2BT4%2Bc6JoIWhmew8CgScQIkX4IVBU7hLo1F4JW8zh7mm7A362V%2FfaaZ2kS2zKVWQ80mNMDHx2mxPjVa83n04CSBKwtvJPKnh5P46XNco3NzabFgwWJb5qg3kw3JmRxfHp%2Bxc%2BPsw3BCxwaQxa2VqaoPV69Qk%2FAuXxjFb9y23kLXvEStMobCzihtWJ2GvEHrhdxO5%2FOk2DnhGLkBuKjWm55exFn2Va%2B1G3uKUhNw6jqr%2F1Dr6pPeMsFh%2BchbBAJ9liGhByDrQYm0OqXhtkYmX19jEwz%2Bz1vAY6pgFeimFp%2B7VZRpQZg3yaPHfQP5hCnASNdNI%2Fix2t%2FTcHJYlddC%2FqHMvZIVFC1goFYdV8fMP2s4oBhvcqEzi1Q3JLT6dajF%2BEs5o8bbrCHMCsyfw9gmxUgUHVxlLN9JsTHZhcF25RCilWOyuPVlkJeVYL%2Fmcoaa65xw8n9HA%2BVHRn4Djb%2BRFJ%2FMmb1dgCgONPb7JrSNxZngGmMxJ%2Bk36MUz183E6SoZDa&X-Amz-Signature=0a5734449bda064964d68a9a0b3cfd739d2cea29cb519a8993354de66435ec2a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEJCY726%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDwvcbSfTrH8%2FEDoPDuXzfDdZtO8zlBKR8sgParYvtzAAiAWy0lBc5D60Jh%2B0xd%2F7bXgctWnnH35hUKEzvULIHp66SqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIw9HgGNjBszG1apIKtwDeYqIw4TpqO4AOpeVvlXm0SmDrboHOx3%2BDf%2FA83sQu5%2B310UgVUPEpRBKPIoyD%2FCietDFmT9uwA3UR8TazvMB6ZOL1quvpLi7p1JDtjXv0jAkNjSkIklqdu0AZml17lF0XFjYEWvoBft6s6TCWjy39uD5XnuN3tYSl7sTkYt7oDCpGzdDI3fIn09uA2g5xDhffFaiXojCFKwlTZJTtOZb1jzOBNnMTRH%2B2qLoFMUrnSN%2Bt9paTlj0%2FeLs6WJg%2BVtjtKQIVYP5WGcme%2FJ7knU81Amo5Iwiyvuuc0Culr%2B9dQUxYfTHPUf%2FydgICwDFWzpNrHlDY4o4AjWPu%2B6wEZ%2BLaGcfEx1wuFi60FBrfr%2B1342%2BKFcmgz%2Bmo24SSBLVAuAvwS2h%2BSGi%2BRea8LIthC19wJ9bNyopbmLXTeIOWZuVNRpXVOFTJYdkgypDRXmkGiexMjSfsociVEo9NpQMLxv43tEleqmNMarME%2Fr2ZZN80%2BiwZoF0bpGeThuZ%2FBgWE9smnXI8f75ppp8AT%2B9gihcKW1w5%2FaHYeLo6faghQ4KO1p8PzYeytJGHi0sVXz9ljmD0L3OL0k%2BI3Y1VXoQrxAgKZdeEoiTaR3hX9VKyXCI9sjhoAs0qUEWeexX7Yj0wt%2Bz1vAY6pgF8gPOHm1I6BsS%2BNFwaNtiP81w7VBpV2jMbN71G8RCc297EbBRIW7DnHzXbl0AWi9RUZxWO8D7u6IMkDymj3Tj%2FsXIVaZJyGszy2u4GtvTdo%2By3fmdEwloDCYAmTvkuvXH9oW%2B5pvnHGxpKU%2FIEV6k4EZZ8fsNb456Bq9mo2HrxWziQpp7JE%2Bho5ng3nNtWn5fZYpRHrFeeMKZxpHmRrs5bFFnGmyuG&X-Amz-Signature=bd1cc5d64f3d85d7a7748a730032f29e27d2344948bca62a250b3efe3376409a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672YTZCNK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsotKxgRlOF3siq72lh%2F0j5J%2BvXlHRiurUY69iP29H1wIhAODKTi1zB8cVdv9uTGDdCc%2F4a4m0KN1sfTWaVEp71mvDKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc9nBQK0DjPvEzJ2Uq3APuKhmCvS5n0UNN%2Fw85RSdxrvsTkQ%2FGlwNO8ad9BwiG9%2F%2BArKoBnoqsPscuNa3z%2BjK8JCYiEOpDKEIB1u2YRKzlZ2ukOKu8UQJ%2Bfqf5ushwbeNwRAW68T%2FRnsosQkmjtZ0ZwSpFeBADDvb5VVt4cK8i03X89I4awkzdGVfTDl2mKvN0ogosQGLkA0QgWXcLPm4GipbYIeKmFSLBKZE41MDCqG9JWayysqac%2BgeLC96vOAVrGmrekLnFyUxN3tUK5QVZb%2FhBMxhNEIGtEJ3qEJCHwiIUpy%2BRMm5PdJXgwr48CVGA%2BWa263BoBS3mewScibgrX7HupGOkdURsNzFLo7OegDaUMj7tjhkjFA8npNVnDT0mj%2BY8lc660phie0Of5NXELo%2FtN2f48VtxG6X5655%2B2sHLBL2k6AYAvu2Ny%2B%2B7mLwDNeKgl2TDQfAHc9HEGt922CodMQa4hr7ToaY%2BennmwxTgiKH4OHk5LzRWkGJgwJL40Q5LdI8c9aMPxM4b%2BVsihrk90Vh7I9kL3%2BRVpjFgUDqI3UjA%2FOZ7MEIrVRLLZgQBCwl8KkO9b4s5sVQC4Zme0pwma%2BlHYjWJDYJ2vPwnv0AWNTrU%2F4uy1aE3omECcueTe1xVHLNINqlRVTDc7PW8BjqkAY0JuJgCF8LSqSaojD1eL3VV%2FWUgxN0G33j7CiMmIqrndvfrBCUKRY5EuUipOA2Et7bunyJmFbPQ4LmR3KIWqAOK56Wnl2TyZsMs532skxL0PiNbvNeGFVb32gYAzuwGmn6Bk5gwThwnZt0v9Mstt8wYBHFUvr92npXO8Sidk5mN8KA4yMbuUlL3XnKXNwLEaN982Pc4yFQa5x1B0FIk9VEyRZIe&X-Amz-Signature=0e4d6c40389b27a1a4296632dc830408bbd6f924449fc6c9a363850d71686656&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS4GID2U%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlBSnV%2Bar5WG%2BBsDDOld4euz69dqv8qYN0nJIGNmSL%2FAiARtBWwHs29L03v1tCa64NlZ08VkMNowhoijpucmYDaUiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUvOJSorq7HmFnFIKtwDzitPjk%2FMZqBujdFCIU0gwUORKHY9jTXYLRwMtF0kOK9aJZlrbKH2E3l%2FIio77vOHM0EnRdCwtemxEzKuZQjkC23dfIT%2FdW0HZBq2bDteu9wi%2BhX9Sh4GljXh3mfbK%2Bmv92namVan4Cy1XnwHYH%2BHmogx7GFmCr%2FDDMJqrCRdeE9phdG%2FiVcfa8ANPAtVie2cvegmSz3Vp6KKT0LDTFgpQF9ADv2p6cmoZibQR0%2BKUwRNVFSy62vPwKdwrxeCfd2V5pV8Mypyf8JXTmgJ3%2BkamseYdivo6kRGaUbtjWVQ1u9btxXOux6XpE7t9NlQhi6OZ1Wfte2SARKmjipNXK1r0o5aOTK7LEZqOrVNoQvLGs5f6kQj3kaBkmBriEZWmo0K6hCjwdqk7uU1hibiIVKWEU3b1ftvf2%2FM20teuw96HfRA271dAJVKwka7vh5%2BkEsCBWOAmRkLH90rZdKYoR8FtZhVUxAnxGn%2BvJt11WsG92bsCTFGbp3YcI41prgZExb7JyxCxNMLHsaDAhegOH1YhI6SHyMaRkT%2ByYxsL6IPw51HZJPmomMnhH8DZUuuNeGaGKSs%2Bz6Y897E4zKuCRiCfd8p0fb7J8GuANKmJ%2FNzMrSqT9b7ocR4cBY%2BgVUw5%2Bz1vAY6pgEHojJbqBSxHMcmRumBj0cdG0kiHX%2BsMcy2H7Lbb0hDOzbamEoFLXHZa%2F4dUbzs5yIX7zUBOsapK4uXZurfsl0tn5lw0TQMSUhTGLj5VoSuOpyOOf1ezAdq3zJCXXpa%2B5ghpSnRzmgyo608PUO4yWM%2F47nnSOWTTMX9Azfnbj21cmW%2BbXdtS%2BgS3rXfpqvxSPpHXcS3onpdMsTBuvHOyLadHmhxTgXW&X-Amz-Signature=4fa228a0645fb66514dd43cbfe3b886b0904e100b0a6d7ed0930784361c67c8f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFOYXF7V%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBq7CqWGyZ1hGzWR70pnGsxofyCzmhGQB7fAu6DmjilbAiAmBCigAKZzF8Zg6ASX8527R96KjFKAaFeYsT2nqGxBxCqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJ%2FBTizciW5fDczddKtwDCzAGnN57HqSz9rMzHRlK%2FCIdb9wZE08o99MnGtGqGRFBgXAnEGgpebaadQz3NZ21aMFx9B%2BVUsTX5YF58e619kIsO7u0t8BZH4NQJbHNdXv2YqAaaKKwVowkGdLAFSzCV9Dv516e6V0KTDEKHWOsF3NRsb5CkBqiQVhofiwpoviHo9CEMfaYUm68P8kKPfrPQwmPBUY2Yz%2FpdfKv7NaYfiI8QP8U%2FFsGK8Nb1R3UbRsNsp%2F%2BbpY6WUoDmHyg1bwQFTZ2b7OjEeBgpNo%2F4udxYKUl8jsbnL5kVCkLQcyEtNicTwgK2Pzb6uYfVdYA7RWt2kzMbOAaY7Wp8G2eZHBEr1MGDfGUdPbWw35N21ZihQc18SzQxTBq%2B5xK%2FcNnanCzX7rdfF2ji1LmYuLhfjTub8e4yGBwBYIDU46%2Fgo%2BIGmK%2B9Vne7vCwTDn7ZTNw1jToMmSh9qAW2xTTuAffbz5gBrbtwsLJ8cRofEtR4vldOK3WMQ5gBkbs3l6TRdBSVLr16iLEqYfbWuvZxClxmcFb0gPoQVBpGY9ptoTJtnxWy3v1atOvZsGQxg%2BRhxFKoRD0ThGw%2BA4CUN%2B2SyOa%2BEaeVk%2F5%2BlNsKdrTAAhtn59QL%2BOBsg%2BUizTWs2HDBzAwu%2Bz1vAY6pgFpul6BvQZvGtat3GIUqqCBozagX6OnpzEg3FEtCm46eRGUUt8fBc4LzX15138K8ywVFjsGexTI%2BHg3uF%2BLzEjPYm%2F2KuKA3rvsA2sm0BFSSdE6sHdh2uCKS0094etgkyvQj8OGqIkx4se31%2FZiNV%2FkX%2Fn49uA0nLFos5dd0WRzEghiku%2Bkug6RduLhSZQd02s31LCZP%2BqFaQGJO3fohVpSV3yzDcd1&X-Amz-Signature=304a01c535a53a50bc881af7ec24c2edbb144c14819e93300628c93188da9487&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RCVOSXY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVy35k1yjjY%2FWBgX9LQ%2BkTjrr2G44Bztk7FpMyBZg3dgIhAK8fpOdFVlYNhFR%2FHPqmSoYxRZOXVXb6hyPujFEcnDQzKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfDxVEFCDz2SUX2C4q3AMWm99C1TEbBr4CvYZnherF7tP83BY%2FbhzaDs9Au8b46OVF4n%2BGHzBhiRj9KWOklC44fK3RzBsEqbAQdjXQsRGt3hk8k66CVRm2iu%2FD0qssVKaOuzKyvmNhIVeAqmB92236V7Oft%2Bz4CyOG0Dpt2XwaZJXRH%2B3EKxIzr0belswrNMQbdObj6uYC9w2LCvOWCKwNL1wBafaUXOoa9vYLAKCjF7ifQBFRDsRd26OTYxDeBpcWttbysbtl7T9ZFDib3VFO5PPV9D52Lex%2FCgmbJ6J1HuCFA9lmyAa6IZPGaS%2Bs28Yuc66qnA3JhEjhsxMICaI%2BshIuIlvDgDQyNQAB2kaH%2FElewjWEl3NV3w5rYW%2Fw%2BLcMdHa1l49eZbs2MEupxBLBOdjktJgYJnkN64smaaMOC1FaVUHbcXxFab9tQDTmDqSP86CHNLIOGVnoiZiGK8CSO20M3wLXeb%2FjQrbzEHvE68U%2B2unQokKk78ikr%2FZbItoVPXaZZ9nz4mao8Wvz7OeivFVif5719BfMspAFBZ%2F1ePNijevBWpkr7YPK8fIYu3jamDMWyk9gtP%2BSWAGU05QQtSPlpjxy1aAGrvtuLI1sZ%2BLaPmERVxBvT%2FBzFvh4UA6%2BnYf7Ez3Q0IPtjjCp7PW8BjqkAYEb%2B2gqsjrOGcvmXcFHiiVTpS3zL6NcsFbvsam99Vn%2FF7adnAVzpghNACIVLQ0FR%2FYMGFRGTm3oqOq%2BNFt3bq9uAVKBCFZuoV0qnJDbjbpU%2BOFqyHaJRD9g626Vs4aaQvvlHA0Q4oWZM9hlImnowfdLGvZdPMSjPx3wV7iVctg%2Bc2yL%2F7%2BCXtOW8pm9xOT4Iq6j1RPU%2F%2BHMPzdKmYN9KQhi%2BZqg&X-Amz-Signature=0a59e4a60a9bd6fe53c91e90acd0cb003a3507c90184a57ca941a3c3ccac5880&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUECAA2S%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICNAWG14et7llotX5SEnQj%2BahwIKqGVmfpm%2Bn5JqlujKAiEA0pHVpDnk4e1gkK1Blf3p5y35%2Bx%2Fd29rC4VR%2FTBa21z0qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbgIZc22zcb9DmzhyrcA171zHVCHcVOIWpiFCLwH44MUSakyKk1v%2F%2FgopG%2FysoyXpBr1UmnFI0gy%2BppRGdzMeLXYQo8nPFcUbSBuJObDKekYIfgayrLfLIt0PHxBQSmZNnWgexKJBo5FNXIfi%2F6M5kblGObMkWaCjbhpTixvbGaC%2BJ4%2ByhUIfhU5fLK2I06pFw83JZ1rk1kEbvw4GhjkuWT61svOM%2FeHX%2FCVNmNnqkTOMmcv8Uqaw%2F%2BOY11eeQcR9O7LLwtHxYoJOtomHCjq2XShi9zlnAP4ThImBpi2ZTcO5z6AAK64KQTrDmFkMtriXzF4Dxf9ZuGlslLPDvl13VXepyLPx9i7V9aQ6oMC3bZkXflKdmWEpaIBOJ1agvb5FgokVUVu52OvfsApIJczRxgx4dX3gRhAhcWK8qGwejyDXH%2BuVuBkW%2FJ%2F4THCz6cjvufLNSof4k7FqcJNiVYOfeX1OamF47aZf4WGiNXRIfQYlAJS6ao6hYuFjXwYA1EJrfq076UGLhg7v1mVaosksHXIE5lfPpZke0U%2FwIruWJ3WjW1t1frokeOTUPdwa5H8UnbSND5Le%2BlMqNe%2FGDszSzDwRit%2FliRLimAggqH7c0wyrTuQgtyIl%2FeTSgO%2B3TrBn6qAdjTAmlc%2FYD7MMbs9bwGOqUBmmMzGP7FclNfFsLIE2Sfzq69FTnxLR1mfo00ithSnAJOKF2mfBB8OMGCdl4FkRyglrHAfNipUNmBsEMabkWtS%2BuLU9KmMdOrHRQKMLpXz7vip%2BWPEgAbqF0kB6opY63AdjYYVWVHS0mD7W%2BOpG1MQsmv36ouBa4r%2BeNkVhErjO0W%2FNzQcSBvLPJ6zewLBCDPIuKpABuP%2FfxLpwzpISppOXsgkb%2Fq&X-Amz-Signature=528552114003c20f11fa6b872b4198d386c0ea5ecfbb031bd1b6877dadc22616&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS4GID2U%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlBSnV%2Bar5WG%2BBsDDOld4euz69dqv8qYN0nJIGNmSL%2FAiARtBWwHs29L03v1tCa64NlZ08VkMNowhoijpucmYDaUiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRUvOJSorq7HmFnFIKtwDzitPjk%2FMZqBujdFCIU0gwUORKHY9jTXYLRwMtF0kOK9aJZlrbKH2E3l%2FIio77vOHM0EnRdCwtemxEzKuZQjkC23dfIT%2FdW0HZBq2bDteu9wi%2BhX9Sh4GljXh3mfbK%2Bmv92namVan4Cy1XnwHYH%2BHmogx7GFmCr%2FDDMJqrCRdeE9phdG%2FiVcfa8ANPAtVie2cvegmSz3Vp6KKT0LDTFgpQF9ADv2p6cmoZibQR0%2BKUwRNVFSy62vPwKdwrxeCfd2V5pV8Mypyf8JXTmgJ3%2BkamseYdivo6kRGaUbtjWVQ1u9btxXOux6XpE7t9NlQhi6OZ1Wfte2SARKmjipNXK1r0o5aOTK7LEZqOrVNoQvLGs5f6kQj3kaBkmBriEZWmo0K6hCjwdqk7uU1hibiIVKWEU3b1ftvf2%2FM20teuw96HfRA271dAJVKwka7vh5%2BkEsCBWOAmRkLH90rZdKYoR8FtZhVUxAnxGn%2BvJt11WsG92bsCTFGbp3YcI41prgZExb7JyxCxNMLHsaDAhegOH1YhI6SHyMaRkT%2ByYxsL6IPw51HZJPmomMnhH8DZUuuNeGaGKSs%2Bz6Y897E4zKuCRiCfd8p0fb7J8GuANKmJ%2FNzMrSqT9b7ocR4cBY%2BgVUw5%2Bz1vAY6pgEHojJbqBSxHMcmRumBj0cdG0kiHX%2BsMcy2H7Lbb0hDOzbamEoFLXHZa%2F4dUbzs5yIX7zUBOsapK4uXZurfsl0tn5lw0TQMSUhTGLj5VoSuOpyOOf1ezAdq3zJCXXpa%2B5ghpSnRzmgyo608PUO4yWM%2F47nnSOWTTMX9Azfnbj21cmW%2BbXdtS%2BgS3rXfpqvxSPpHXcS3onpdMsTBuvHOyLadHmhxTgXW&X-Amz-Signature=d5e298e275d0141ed79d2c24be2e9888ead4e9e8961cda1fac0beb0d6f56656a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TK5VORG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMe6nrC%2BKm1O2bJlB%2FZ8R8G1uLcGLXQi6XgpV9tMyuyQIgDgPm1S%2Bt%2BtOAjWDKxlrmHEg%2FkMPwZkwsWagsa06gH9MqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMfGme4nsbMeVJWnqCrcA8RE%2BzTDgSObA%2B8Q5ontLQmv0Xwhh4IZkm7KPwoiq5IAn0jXgTzzCgFJ5RQKr76d6nNGjanj2QhHfXMZsVmHdbo1Xs0KZBW%2FawdArzm%2BhDVNlzbLpAIx3YrQTcG6wl1sxiVInZdaoxU6pdyja6QD%2B9qo4XjpcPtQdNS3pOBdn5UHesecns7gf2onVG%2FOhmm3cFrf%2BEo%2Bt6IlFlE3wf9wrOrgOq8VF4WHy7lgPmesErD7ux8RKhSUCUIbryU4kasNMnLQYaCG0QK6QaDuvG4Q0CLu370iRho%2FwM%2BZ%2F96gJN%2BBf%2Fr%2BBbvhd3%2FVckkJsUiGPzX9ZYY%2BnRNvgFylzIBN5SQEaN%2FxIGPWUHD2s%2FguqKJYTNLr2B7P%2BsNxyWHMWdneRSwKk2t3fd3TBR%2FvdNiV33cx2NqIAHgJU8Gz80xBTfra8dyzH8d8th441WDQSQriGA98Y9O0Drl80R6lWMRFx3NB1yifeRiS1Wbm8eRcZQ1tyePCcWWLz171bf1fTWGAiPGO3zoozt2xy4j1%2BZ8qORdKVZAqXSKL8fOaD1dlQqUTQALvBC8BSJJQqsqjUfLg73n1kuSmvlpTUCubjJdrFQegYV5AYlrFVXbdTu71rup%2FtxtSHcmEX34DGW56MMbs9bwGOqUBkRnQhpWXoaroFz%2BsXvBioJF79sNPFk0Tl50jSZClSSOuWmEs%2BmGWQCq519pM2txv%2FSJEA97lmHRBN5ZESK7GXeTLNgxzBFu1UGaZi0lTBiyz%2Flp5jLVrCRDGpTmKFpVmYNrrZu68iBOLtFdv9JvRfWe8Ith7WdUKlkDLhVVZu67G5VH2qVXR8zQxJu%2FmxSIf5bLldo5Nn6sxL%2B4Y9yFRkT%2BwKRkg&X-Amz-Signature=2ac13ab114d57e0d97604d154d1297e84825e59cbe15469f8bb6ce9c4b95296d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TK5VORG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMe6nrC%2BKm1O2bJlB%2FZ8R8G1uLcGLXQi6XgpV9tMyuyQIgDgPm1S%2Bt%2BtOAjWDKxlrmHEg%2FkMPwZkwsWagsa06gH9MqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMfGme4nsbMeVJWnqCrcA8RE%2BzTDgSObA%2B8Q5ontLQmv0Xwhh4IZkm7KPwoiq5IAn0jXgTzzCgFJ5RQKr76d6nNGjanj2QhHfXMZsVmHdbo1Xs0KZBW%2FawdArzm%2BhDVNlzbLpAIx3YrQTcG6wl1sxiVInZdaoxU6pdyja6QD%2B9qo4XjpcPtQdNS3pOBdn5UHesecns7gf2onVG%2FOhmm3cFrf%2BEo%2Bt6IlFlE3wf9wrOrgOq8VF4WHy7lgPmesErD7ux8RKhSUCUIbryU4kasNMnLQYaCG0QK6QaDuvG4Q0CLu370iRho%2FwM%2BZ%2F96gJN%2BBf%2Fr%2BBbvhd3%2FVckkJsUiGPzX9ZYY%2BnRNvgFylzIBN5SQEaN%2FxIGPWUHD2s%2FguqKJYTNLr2B7P%2BsNxyWHMWdneRSwKk2t3fd3TBR%2FvdNiV33cx2NqIAHgJU8Gz80xBTfra8dyzH8d8th441WDQSQriGA98Y9O0Drl80R6lWMRFx3NB1yifeRiS1Wbm8eRcZQ1tyePCcWWLz171bf1fTWGAiPGO3zoozt2xy4j1%2BZ8qORdKVZAqXSKL8fOaD1dlQqUTQALvBC8BSJJQqsqjUfLg73n1kuSmvlpTUCubjJdrFQegYV5AYlrFVXbdTu71rup%2FtxtSHcmEX34DGW56MMbs9bwGOqUBkRnQhpWXoaroFz%2BsXvBioJF79sNPFk0Tl50jSZClSSOuWmEs%2BmGWQCq519pM2txv%2FSJEA97lmHRBN5ZESK7GXeTLNgxzBFu1UGaZi0lTBiyz%2Flp5jLVrCRDGpTmKFpVmYNrrZu68iBOLtFdv9JvRfWe8Ith7WdUKlkDLhVVZu67G5VH2qVXR8zQxJu%2FmxSIf5bLldo5Nn6sxL%2B4Y9yFRkT%2BwKRkg&X-Amz-Signature=4a5bde2e469eadd3856c7d1471642d689cf763796585a0f79afeb0aca1d6e859&X-Amz-SignedHeaders=host&x-id=GetObject)
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