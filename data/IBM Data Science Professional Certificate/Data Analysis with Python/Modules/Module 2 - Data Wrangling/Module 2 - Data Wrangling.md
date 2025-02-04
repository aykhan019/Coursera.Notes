

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMBWNXII%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIBGQxPN4FzHR6wHDqJwgkHBJ3XOcWSbrwHnv%2B5qGew5lAiAqGhM%2BIlmnYRO2EBFjp7dUqa%2BxfpRR3RnIDwhljkcBuir%2FAwguEAAaDDYzNzQyMzE4MzgwNSIM5vOe0JB7nR6RzTGEKtwDeL7uSiNiQPSSBPz%2BQ%2FULstM3GMZoghWsF49NrSOuBrJ8HuXha4qp8HxwyL43P07%2Fi5kxmjaoeDa6FHDU1wDaVIo4T1XzwvtGR4Inq8MdYGiZGeHm8BJnjmOA2HLHR2DXHf3LSLk29ydpiN2Q5oEiMKlJIAXLVhHRI5Rermx6q3CPOOwrpWAvuEHPaNcjTnlyXXij63qvphYF6711%2BR7cszZMPmU30YI%2BjcXR19udx4FlX8inglRbOcUXviK17xx36LfXZ16bSzVUss5h8nNyA%2BoSPyC9gXkaiUo6V3N5p%2BC4XdkOdKbCtKTN8o6coIRebODto0LEKWQX2fCO3MUj3mgiSTIPPW2oIrCh%2BmcXJCD8n7DJp%2BYsdd4zP2SFX4flM882ZvdjKKrwXgMsm5qHcCxng0%2B6mBGINWSP6yetRPVGolIoQy7PCDEuMY9QDYT1nqVA7KcdfUetzTBz%2BWjiJzhukNqHuwgPJT1Sz9MdSs52uwFWa6K%2Fr5z7FDtpchDWAQWIkUmxg76jnMYuhjNdqhHSQKnrg2FIxR6vfVhq93HZfRtuR4cepB21tzGBtZUrxxoq%2Ff5wvHN1%2BYJkChgKitI%2Ftz1iAFA1rzKOrRorXvFUmz4VgwYpTE3VPXAwgp6IvQY6pgHMn6srW2D7WWkOSof%2FA65W0PjoIbG2KGia4O4Vu7NXyhOGZKMt%2BE8LEgzcOpOV4Q9LIDoikaQOSmx0Il06GAtFRxXmPXKu9ZSgZaqrGuDUuOV3wNGDFFRwcQ4TuQ10R7Lrk93XahTns0NifxhhBpLWih4eed8J5tOYAu%2F%2Bn7K5hNNU0fp6HTnSIxYOLwvEfNKsizS4HWWJAesg1sw14YOKRHU%2FIikJ&X-Amz-Signature=06f9385dcc56138aa1267d7dcbcee3a2e56ea2003c1ce1c9b13bf0422ea17191&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VFH7U6Y%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQD0m%2FRSdpVgapTNmeuGYuEr4YAou1eTVvEqWh9QhnccjgIgUU137sQwVeGVFgwFKR1vt3hgbUAQ1oZ4nJIclSk%2BMAUq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDK5vDH4xJyqAgQm4gyrcA5LS%2B%2BldHs6Vv58B51N7djOMzVav0anpSIFfl7Y77D9FdEMQq%2B00S2%2FBl%2BOAWVBncJGa8ZOJ9T3KYe4PJjiCXBStW4s8ufAnWmtYvMazDCdPpY04yvOrEIFqTmEUUBpXTQmoeR9%2FQ48f73yuf9zigdw8v7WkWrQr2NzeguIv%2BBIwNTzX%2BszW2h9Zpoe8Jy8M9B90UaNIwzGJVu8OumcTIkK5ImP5xRZ4vEiZWpNOdvGV%2BcXewm74n%2FFuA9edSmahk3m3y%2FnbHY%2FJj52%2BwOw36dl9PPVUyFNnCnUt2bf%2BEHpAe1MndEm9lHUvTDttXBTm12ewDbi%2BxXEQKbzUeDHhKNGoeWZpqb4HjVZSsECp0LPOs1yylr6mawHc6FqpoTfok%2FDSYMJdfccgwEQBxhdE4S%2BdRON9FqhmX5MBULbJGXySMVtq2QPX9dX2PVyfF5IHUvaMkMtHNNUxhVetpTayBT2Fsim3LVPdWVkJ2A0U3xm%2BKq7E36kTxGyebKHISQas14FSJiBHROwO52vqAV8NlvnJi3IAaKiT0Sx1IysQDy7ADgVIniAZWCOQANqA1soSpLLUGoql1MFHVuwy%2FpwuSaDwArpomVf%2Fp6A3hCbgOyqGIC3fixsL1%2BWpkTIyMJefiL0GOqUBbqyyMACiUjCdTqg%2ByOX%2BjMqyA0hT4Q9kY8wfI5p4UpNkbEkK%2B2JL9ifPkus9r1V0eSj1UciZzGQ1iaGzt8WiA%2F%2FpuAVlApQFunroL6D5l9MJgRkzvaJHvR4wBCuLMEiKTvRoqz0TCQBLT1XqckTTqOTQFwuZi1LoqXiYX4IxQ4v%2B9HY6Ha8qJv8X%2BoqmU8OLcnVeGY3Rq6X4CSseAVpg8BLhxFq4&X-Amz-Signature=2f771687f51d1b4ab54877a645dfaf5f90241d69318de3f838e796eb4df79ac2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653LZDC6H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIHdZsCsTxMbYYYYOssv05995mZorw%2Fub6C%2Br3%2FU8rL2pAiEAhxFWGQVXoOuUrIA%2BtE3l7wVOHkroaY00%2Farh6ygkzLYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDHotIeb0m3zKthpR6yrcA7wVUfOmvoxVtQA0O49YzdAxGhxFPvUKICdOFNLckB%2BpXvhG%2F8I8EA1Jv%2Bc9iwZU0VtCDlnmy7cZjyLnPdLsMDG3kDlYLu1zbLbw8FOOs68REa%2FS5wq6rjgWnR8dVu15XZDLMFErkkj4aRPm51VmfeuxIqRvSMihHrg9Af9VhEtqr%2FicE0XTl%2Bv4wFMGZddizrkHwGsIC2NF2V61DiOjynFpeKNTGoxN%2FUOCImRWmewAY7rIRcL4a9mF60XgsL8W9b%2FwPN9pdfUI5ecP0M6liFZV0aZBVP2fHqbLgpuKqbdZbgPmemoJ5F6erQBLML0%2B1xs6NtrtNoRyQgoRXIQ2CwRBkEl6Ig0ScQj50NeSAdWzkBVLISReINbz5cVSlsyhN5P2uTuBR9MI7wdHJPXVDjVA%2Bj0EK5R3AnafAZFAEC%2BbLBzpUqkuac1QeNj%2BO3AjAzSFaKBvQXWzoOvzr9hjidXiGlqkA19ubqPeiPGO5uX5I90T7CafE5tU5G7BASSuhYi06tSDoyYiqAlPD8wz3fNlpULkAuClwVsu6GSnY7rzrXTP4ShNPrgsBDftePEwMBtUsaPEqYrpq8GqLnUx%2Fiy8fbTFjadg%2FGZcMnW8U%2FwKmODaEnIEU9d4gsqJMLCeiL0GOqUBGeiU9iZ5jGQQEZyrEvGrwO8VqXu0fy5wz9xvhJhJZ0e9MfeEpDoQ%2FZF9JDo%2FtzjY91hMn4ty%2FECrnxsWDom8hKBoZ5kYnDvUVSHDiPIZCrzQu5VuwEkcKm7Jrlgf8blf%2BjruoXAKs5c2F2X6Uyw9nNtf%2Ftge%2F2zrMb2DakmX6CIuC0ldEdrkPcddBU%2F5P9iBL%2BpKLyMMsxzRoUxAgMB7jw6bUi36&X-Amz-Signature=67cadd1ab429111ef9bc9c79127ed09f17b711bdabe6ca06e8c47179f1139299&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZVSB6XG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIBDgxEeycIZh4NF6iOPR%2BeBz52GO4IOop52cQVTkMkoVAiEAlYOo2d7amZeNipx2C61DiU84nhyQagulYQBQ5j6OcNgq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDOzC5c1Dnfwa6lLwrircAz7D1Eu4dytPMRijl6M%2FeHezLpb6pO1u29%2BA%2Bsg9o%2BrLJVT3QpGnA0x7PkNuoCd9IeLMAF3mSZHXmDdy18KGEUt1fmP9ufGrNE5son%2B%2FjyF08k2vEVRFVY2lzThVhMg8O1R6XIgJTFpD02b1%2FJkxwdvDygwxEe0v6vL6wLuI898aaR%2B9DL1kR4W5pqVs8vWr6%2Bjs9C8XJP%2BfSkGHq0V0L0n%2B%2BgqRlQTouBNPShAWz1GcJP2iUxwE%2FCVDMT%2BSqYi4EFo5PBxF4w8QtLDGlmla%2FT4L1RdRhWwAJYIUN9k9YeNETU1bWBJ19x7M4v6%2FwCPtxQxiaqqgTCRAq7GSNTq%2BrOrQG76Yiz8QfClaSrbrXx3h%2BwgiQOBl47iD7UgyvCGNmPnzxi1hMibDASVRvojHOmppNeo2BLMeYT4FqVROPiQv%2FRHbcHmwYfnRqLRylL4Lbu3H6%2B%2FrJDWdP0NVC00lkoKNe33ruBVnSkXVl3ETwkdei8Mn6Bq1Cmn6KNqc73SH%2BkCrZ025tmr%2B%2BMz7cNbh4Ix9GIKbfjHdJzMuCVyQFMl5djagsCQHTeOa%2FkKZkzJ2HQj1RYXhwgQM%2BtdG0dfN7XF%2FaI56t0TCvPqFj%2FQgk%2Bw6Waxb5hOogtzGWE69MI%2BeiL0GOqUBhmrvkL5S2JvEt9FokU1MCMxSQqnyjPRpeXrJgPS3S%2Fy5nkwNkTUwgkGrPQe0pjoR%2F290NFSqzbwTMSlwQ3Xbq8yoYVcz4mW4qmnnbFFoVCWBVm2CDzfw2Y%2FsFh3M64NwKUaUJ9Nrg7bQh0PTqm5RyMpGVPg2x3%2BOGYpWgxKrP7vQbeSDaY6Do9OjizWkm4H5v%2BSLOLd6jvz08ivlWEsdhxrqwi9l&X-Amz-Signature=d0d235d3e78f250b16d928b612b7555d55cf27d6c0d019eb55af912af8f73500&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M3NSIAD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCm0vr%2Br%2BeErduwBrnwXYmxTm7Vhqbv%2Boj1vepvukr73QIhAJQW7b7xF3XDMbH84cWrb%2FM6eiJ6OdXT42LW6USQlgqIKv8DCC4QABoMNjM3NDIzMTgzODA1IgxspplN%2FQk%2FWlGksykq3APy2F0Mlb23GKTXxlXjbmOXO%2FNj54E7t4fEXr5D7tQRVqFQrZqYw3ZPYPwXcQE1DSUoayJBg7FoQf2%2FR%2BA6o%2FRvK1yddBCXqeYsUuSaUOfqwwg%2B4Zk4ZoG0LBbBkG6yKSyUWEoxKlzHdVnwj9uFQ%2FE2VTmy72EWmPVrqrRF%2BXDl26E2w3zEJf4CC9YJM4UquHksRN%2Fhs%2BnT8PWOsT%2B9hORuutarJ5hA0WA02nMqU4XTnQTK2EftlKq8oGHoy%2BTu0%2FBsqWI3Ro7MPDpMNTjTDB1eHBj7Mgz5Tyh9XxmJx5CRxTz2nqQCgAENhoUJDy20cpEnyBdCB1TnB%2BBp0mqNKtLOpPVDj3o2CY10HHixGCqmtichnX3G6oNN%2BVgu%2FxoSmHHe6v9xsz9YBfAJCPX4DIhwlEQWziBiM6m9SG3NYGk0E8gRQHbiyIKHR%2FpR%2FTQvs36YOJ8ZEV0MvwxaPzcQz3mZFsjo6a3b92EwkXKK%2BIVTtNQMRTaeyR4hwODxaKcg22rPK10HGkWtwYeA11sCFZJ4ZI4WCkjpxFD2Iq8VBQULpX509GVP0AyTAOmo2w7KL6bHgoKn%2BqgC3HrZttyk9nrN7Pxs2ROq0vFEs0gydruXayQju2EK6PzPVdYwVzCEnoi9BjqkASO%2B1XaLc91rkmWn6KbDoBAjaEhFgajsmFvBJg5sDMLFVf2nm6i8c39s79UHK4FRwiEopvM2gUkLOKUfm8MdW2IUepX%2FjPqejf6ooscg6mkIFnHP1UDgWNc9SVXcSgg4OV3Y9EF7jdyRBgsMaakaVnpz%2Fm%2B76cVVToJZBWnDRXeHCx59X8F7FTWaVzD8koprKw7EhXMWJk%2Fr8cuAyoiBeuYvdkD%2B&X-Amz-Signature=17f41dfbd9f708e9e08103539fc8aa4c33fdb96475a91056725d79c04aaa3dbc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHLAPQRJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDQeT5XcfkvIT0U%2BAAWG1L443eLmjWW4%2BEg%2F4SY0S2MrgIgMZCQNVYVCiZk2ouuFp%2BX6A17%2BSdf2bkxIkvTbrdr5L8q%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDDVUVfwR31veOJfS0CrcA9kYH49eofFQ6dlH6h8nNIzotICgk5WjDwsmynBn3JCEdm6UtfxJuZgPQ66DLvR%2FlfzMaLVNL1ux9cSf%2ByVoxnh6I9IU8ngtSR2JZVOJ%2FKPiLr0Nu%2FYVAmxaVxyFh7t91U1Uk8JKduZn0oC%2Fdp6TUz58QpHwbtW2fbpUb5VUEOvyhkTmQjSClSA0vEF%2BSOqoww%2BonZaJ7COVDbKxmRTlwe%2BkLpH9I52%2Fgo%2FbPRu6UvtvIIZRtcEBsxI7vP4PsKJo1IbkfFsXaisqGj7DhwGMlpD0ebE1GLK0G5FVIL0GrffesE0GmZXVAe6d48DR0vw6i%2BNNr3r3Uf%2FpA6rNIkp1MGPjxzeBBE6jN%2Bo81RtI%2BiF9q90x2ImQRT9MEX1PrZFVN5vEte9FK%2FPNrmvq2mlyXDk83fJQywuDQLF50%2FxgIYXPDk0wtBQfarbVGdXnUxdofxjVCjSeqGJPscc5fGziOtop7nsKlU1yeVmztImnD%2Bu%2BDNjqURTgYTbniE9Mcspel8ffRgkU1sxcdU1Bcouaz8fMydbWbAW46duuhPS3KAmP99s60OQ%2B8glJL89Fvba%2FD%2FzRNuWr2BBJLOp2vGnKbSzV8S4CKP4ZHYy%2BD3PLL1rDCWU92fPScwa4dACaMNKeiL0GOqUB6yi2EZIlryalmJDttJdT%2FR6oenuQWmqqIeIYaun6R7cY3ZZ9t%2FuoPeiu7aHsMuqjfIRxhLZIQPld67DeEvWhNHhE8MXmXmkiR%2FUaMTj96YiQKAXj2dihJ6JdVrAVlMhVRtYstnzTDkmrvB1efjA77g729Tys8%2FYmNim1I%2BUDDvxZLj3EvRi09Lwhohv%2B5V53d8VCa8KV%2BUiu%2BUg2lzP8lIkEYgqD&X-Amz-Signature=8b27330429d5b00e1a9371656ba3c57d248663971c35075a9c0fcbf7a1d21761&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHXHMCNH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIEHy7%2B8DplQ5ESmNrZ9NuVggjpw8AdmQz0bxr0IoNYHEAiEA2K7l1e%2F0Ng%2BRADhqr7eKpycC7NvxU%2BqJIUPBKTh5qFQq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDPYefQJG%2BsxEK7jYQircAyVlDidIqnS%2F4oG1Cp60a2UAPMo3lXHcbAypXQiKcBrE95LMRqd9%2Bc7AIpmx5pM68FZUivpbIHK%2FsSg1FDYwUyNfdHrxfHeWbHQQNyAS%2FfNL28scasLjGnsLRRdkGryqK7rLgwqAtKNG%2Bc4JTA41G3Q5oZmo2UkUaWvN8auMcTEjHpyUxiJeb4BQ6TvMwfBE%2F28HhPTo4o4r59YtlkjTCXxCJTsv42hQnUF8aL4zMlrBfgq94fC5MIiroP89JhIkqF5YyiasuZrZF9fH0qQcN1f1ATuQKxzCgoEOMt4gq4qCNlLswndMGExX4YKVwfxyxNJU%2Bb7ZFAzanitQJr7yuXiyOKwz7RjEnC1YEzXPyXoJUQ4ZddzIBckcREJYWPwPRuD9AIYudFTlNrcJR9ReSP%2Bo%2FSc1TC5PhuFLEtOkFd2J%2FjUAGUyCJd6hXxY781wBx9HBpyi5ho%2BKuHf8xtKLp1K1zUzn2Jo1WAqfoenfXvTULQfTYtN%2FhtnQ5hs2nlP1sCJeyWQqp%2BiJcm%2BJXjC2Pd4r4hJcfc5xEYx84a0yv098vYw7gz3k01EicEjQ8b%2FDXvaJyBwlx89cbpiePZqMrj1jgRO%2BbCagrsscQrhfEGUjz3sO0%2B0MmI7WYhvWMKSeiL0GOqUB%2FIG5H2cwAnDjsVf1VVwpflbI5w6My%2FiT9O55YrwB4HNPhryyyR0lvDmqSH4QCiEILyp9ZUaU%2B9LRNsIbLA6WSuv8hWpxdl3%2BZRvaP5%2BchMg8j%2BK2ZjadcNEQXD6O5r0UxcCDdv9q7XogqutkDjE7iBa4VTr7SFw%2FhvotY4Pvxw0oFEf5%2F25B%2Bt%2FGzmRLVeL%2BukgrzEvQ4zBT5ZLjrJUPxPLQTMlw&X-Amz-Signature=34d1fa603a54a9718b3adf365f30f40bfbec97838f33784fa93fcc5595b2f4c6&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674KMZQNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQDe%2BxyMegej99EXrqeTfpb2y23Zg8rudqobRRwLh1TahQIhANtUlwiXOZXx9k4fb0Fb2MaK5ZeF3qboTgJxqCtRK4BBKv8DCC4QABoMNjM3NDIzMTgzODA1IgwNCJvVizOzIqSmgmUq3AMWW5wONeudoAHOqA3t65YOTE3C9CP2a%2BePPR%2Bo5B8icBFUT7TQFziVCs1bCflI6oDYa8eO%2Bss1vAyA0wEESK3M5vGH0hRv5z%2F5S8PGxRqNYugA%2FnAmyZqOO1M86zUcqv%2FwTBS6aFAnGTmBAzE4YyQDnw92ArEsszzt91AGA04IzlyREjl9T%2FmNU66oBrqZA5agkK9XekJgmEcxRW1dipf%2BKH9lhGIr8i13Z3jVbktro4HA2g8FUiZbSmxJowQy%2BdZ8f9TdJr%2Bq9uyQyeRmkDQexw%2B8bwI6nodd4GkGVoF1OAFYKsJSsNprE5TLxlWzQ9zA0hdfsIwYm%2FjSQ0wqTehJIhaC5CVK6XRS0dmmL%2B4IjUuXO%2FoquRWU7SRHxAUxK1U%2FWEWDvE6xfNld1YJdwt7lcJ9C0ilD94BOvMgBpSHiJMOA1NoNsVZASmMOtoRDthbbaLXneqR6U6jmq%2BK9GQfJkHgaV9IThhimvjXwR16hecg9MmgaFgUfjUcyTvxsXsVwQCYTR4Xo%2B5MpIsT%2BhK3ex1QwecDGbgWue%2FvN%2FFGjNewYUk7rzTejSQQ9Ie3ZnsXm57fOPPjCgd6UFHT40q5HYVBNWie4Qzia28eJBry7aAmikSxkOj2a92F%2FrzDcnYi9BjqkARPD9z%2BWnqelTWdY1SM6ueuE708FmmQhRrmklNNr97WrCBU8XDiBfDYJWSRWJyTdwnzQJ%2FiH5k4J2OB1Wy0epsIqwMtkFCVRln42M1ZKvSfIrnLzwkm86g6q%2F3pUlBGVdVZdLjpN3y%2FrXm%2FPzS1dPWKfJqAEtEylr31txRLDyS7grzP%2F0fSIyaxB6cLANZto2lzy%2FHOj5V%2BTcu1phKavAMOOF1me&X-Amz-Signature=cbdfe55295190d22ba9f234beb0da20ffeaafb3826a0a882bfb462a1148b4908&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M3NSIAD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQCm0vr%2Br%2BeErduwBrnwXYmxTm7Vhqbv%2Boj1vepvukr73QIhAJQW7b7xF3XDMbH84cWrb%2FM6eiJ6OdXT42LW6USQlgqIKv8DCC4QABoMNjM3NDIzMTgzODA1IgxspplN%2FQk%2FWlGksykq3APy2F0Mlb23GKTXxlXjbmOXO%2FNj54E7t4fEXr5D7tQRVqFQrZqYw3ZPYPwXcQE1DSUoayJBg7FoQf2%2FR%2BA6o%2FRvK1yddBCXqeYsUuSaUOfqwwg%2B4Zk4ZoG0LBbBkG6yKSyUWEoxKlzHdVnwj9uFQ%2FE2VTmy72EWmPVrqrRF%2BXDl26E2w3zEJf4CC9YJM4UquHksRN%2Fhs%2BnT8PWOsT%2B9hORuutarJ5hA0WA02nMqU4XTnQTK2EftlKq8oGHoy%2BTu0%2FBsqWI3Ro7MPDpMNTjTDB1eHBj7Mgz5Tyh9XxmJx5CRxTz2nqQCgAENhoUJDy20cpEnyBdCB1TnB%2BBp0mqNKtLOpPVDj3o2CY10HHixGCqmtichnX3G6oNN%2BVgu%2FxoSmHHe6v9xsz9YBfAJCPX4DIhwlEQWziBiM6m9SG3NYGk0E8gRQHbiyIKHR%2FpR%2FTQvs36YOJ8ZEV0MvwxaPzcQz3mZFsjo6a3b92EwkXKK%2BIVTtNQMRTaeyR4hwODxaKcg22rPK10HGkWtwYeA11sCFZJ4ZI4WCkjpxFD2Iq8VBQULpX509GVP0AyTAOmo2w7KL6bHgoKn%2BqgC3HrZttyk9nrN7Pxs2ROq0vFEs0gydruXayQju2EK6PzPVdYwVzCEnoi9BjqkASO%2B1XaLc91rkmWn6KbDoBAjaEhFgajsmFvBJg5sDMLFVf2nm6i8c39s79UHK4FRwiEopvM2gUkLOKUfm8MdW2IUepX%2FjPqejf6ooscg6mkIFnHP1UDgWNc9SVXcSgg4OV3Y9EF7jdyRBgsMaakaVnpz%2Fm%2B76cVVToJZBWnDRXeHCx59X8F7FTWaVzD8koprKw7EhXMWJk%2Fr8cuAyoiBeuYvdkD%2B&X-Amz-Signature=2250ffc70bc5d9d5a5ef8e1046a056d89449780ae0a10c8011d63ccc29fcd3a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP7HJWDJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFF5uQFWKXiYokpkpqRfT7OrXJd1TzIzgxHQCS6QpVADAiA%2FXvorsuJ6M%2BRxkvqi92YrZr%2B3n5lUTHkBYRi1lLr3ACr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIM2rMlVPxxZvsyBYMrKtwDrijuv0MiBLn6ibfUCv37ONSPmvUFLypysq4dzPBrISTJ2sp%2BJDjT5AElU5jgmQYe648S%2Fql9zB7O3d3iJfJD3k2P2sP6GBNU8Y32vZfE7iZWt9UvoE237jaUVp%2B85cKz7848e7ebucjhwzPb8RZ4v28EOmQS%2FpS7khIj78aLNKJdQlIC7UPf2EAqovrzjTv%2FitpP%2BvTKhN5WOYjTxTjr3eGzOrjtny7RfrUCuhTdXmRwao5O0YEkdb9%2BsaMB4il0Wr%2BsIjBqu8m0ayrupB5LKKB1BdraQIGwc6Z7KpVkVZO%2F0EAZRKNdbyG%2B%2FmKZ4A4G3iENE2PuAhuOim5OKYxgcLIhI4XmymHNv0MewzbCepwonjbGDTUdyUt7ZXYX9T4VWTx%2B%2FKPnQF3UiT5czmjzrJ%2BC9lPJ3XV42lkPIIhaDxNxOrpnzR5qyhj3RHKPmGxgpWFoR6tzCbR0olVhaEEedKNGnvZASn7HPa2902V96XOT%2BHYjRnim8Xzm4wUNvxtiRKEKZbw%2F3Z5m0PGEOyQydH5lI9%2BCVRczYq7aVrYOwuMZN%2BkPSbQ2O%2FXWaCtuHr3qQRUugk2LXtKhL0xrzy9RPff4aYnVCUVWXckW6a3qaKzJH0MACyiDbJCpy7kwsp6IvQY6pgGOxlwa5O8l%2B4YO67gSNF6i09he03XsMKfyc6M3WlR597lpkOefN7ghYmmuqzyOMY2Bu99tCDenMs8cHIrMPkszC4psjVHMKsWpTmDz1484bsN49mW1y3HalGraEbpvFOguh6Ygomy7AZwJZbXX1TyUWaE2CodsoFh4VQ%2Bv%2B8m9jIDYvWemZ3Mcs1NSFLQ2Ivk7QgOrQxMNmP0dzrdDoDoKun28zu4I&X-Amz-Signature=e9a8035f34c597e1d357c51e4bd2ab427a70f31fc49a00f356f0c9eadc3bc177&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP7HJWDJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFF5uQFWKXiYokpkpqRfT7OrXJd1TzIzgxHQCS6QpVADAiA%2FXvorsuJ6M%2BRxkvqi92YrZr%2B3n5lUTHkBYRi1lLr3ACr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIM2rMlVPxxZvsyBYMrKtwDrijuv0MiBLn6ibfUCv37ONSPmvUFLypysq4dzPBrISTJ2sp%2BJDjT5AElU5jgmQYe648S%2Fql9zB7O3d3iJfJD3k2P2sP6GBNU8Y32vZfE7iZWt9UvoE237jaUVp%2B85cKz7848e7ebucjhwzPb8RZ4v28EOmQS%2FpS7khIj78aLNKJdQlIC7UPf2EAqovrzjTv%2FitpP%2BvTKhN5WOYjTxTjr3eGzOrjtny7RfrUCuhTdXmRwao5O0YEkdb9%2BsaMB4il0Wr%2BsIjBqu8m0ayrupB5LKKB1BdraQIGwc6Z7KpVkVZO%2F0EAZRKNdbyG%2B%2FmKZ4A4G3iENE2PuAhuOim5OKYxgcLIhI4XmymHNv0MewzbCepwonjbGDTUdyUt7ZXYX9T4VWTx%2B%2FKPnQF3UiT5czmjzrJ%2BC9lPJ3XV42lkPIIhaDxNxOrpnzR5qyhj3RHKPmGxgpWFoR6tzCbR0olVhaEEedKNGnvZASn7HPa2902V96XOT%2BHYjRnim8Xzm4wUNvxtiRKEKZbw%2F3Z5m0PGEOyQydH5lI9%2BCVRczYq7aVrYOwuMZN%2BkPSbQ2O%2FXWaCtuHr3qQRUugk2LXtKhL0xrzy9RPff4aYnVCUVWXckW6a3qaKzJH0MACyiDbJCpy7kwsp6IvQY6pgGOxlwa5O8l%2B4YO67gSNF6i09he03XsMKfyc6M3WlR597lpkOefN7ghYmmuqzyOMY2Bu99tCDenMs8cHIrMPkszC4psjVHMKsWpTmDz1484bsN49mW1y3HalGraEbpvFOguh6Ygomy7AZwJZbXX1TyUWaE2CodsoFh4VQ%2Bv%2B8m9jIDYvWemZ3Mcs1NSFLQ2Ivk7QgOrQxMNmP0dzrdDoDoKun28zu4I&X-Amz-Signature=2f785d9052f9157166459aaad16e1b7d3136e73656e4b88f77093ae26ca65c0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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