

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MP3BXRG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIH4kvqHp%2BFzlQLiVq3eRsIJ%2B7q0rivxpJNZbLNRKktACAiEAsrNIeUeC9quQSwRXrXXeh6o%2FXw%2BN45g1CurdAy4qlZkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDGo3%2F8lVlKeLh7AgISrcA%2B%2BJvDDEbMydWlg%2FJNISijFddMxhmrEpaLUSM2mBbKI0mVP6Q1WR3UyXiuCa5SjKuDi%2BnDI0ZQHiLmQm5hqozr5g%2FtPK0kTjnx7G%2FddDvPtwmqxDf%2B7EZ3C5nLUtO5dqp5HgrtI6xsAAeYO5YizTmzNHy9UgyHFGDOXvhBUhtfLDBIM%2B%2BpbIoQaE5b90bilR6HjzKgWd9K3c5F8jIcbbDLBj%2BolIaW%2FSTeJ40C5zpUlfwSdWPhovXZTRUM1aFU88dP1%2BMEx8qxu6zoZK112RjIGQSizPw6LLWUhnYb%2Be78%2BrOMhG%2FAOp3c9RWhG0f%2F8ETVy9dUXf8%2BdgIl75VyH%2BCxykncO%2FDYHhyArR3CPROce%2BkRSVSjRF7e1w0SUmmILCV6kTeBwVVe07hK7u35Yh%2BaduJdp9Sml0fNNHjucGQli2a8gwhAs0%2Bh5C9KsGYLymkYDXUYZcwFXs6CIYoTUFFknpIN9G4yjsUiCo59WVzZ76kYf%2Bn%2ByLzp4eOMJgcFiPddBNwZybiZsphyR2su4bZbnW6ZIWfwQFCm8GAY2Yx8WIStvn2VMkSS2c2ioNKY%2BQNoGKXB%2BGWaZPiCYfIdZ0MXMUxdo499Nabeokwu4AikCSE91Z5C3uSoEAezKqMMW%2Bhr0GOqUBVY0pgnolgokq7quujnwdX6KXQ8KdEF3L2Kc6VIpQ6VQLFMglVchVfu9TKT3%2FI6SfsQcB3Dr5Z71wGIEBBmB0D511san8l2EHdO2Aax89BYEgwadfnZVaV%2FQtrkOk5IT0edmvBApSxmxxY0j8wFirCGf2FkfMHw1uINDeZUYlSxcSQ485V0KpdkzHeB%2F9Wl4u8aE7XMAoK7PyDMEH3KAPlcrtwbsQ&X-Amz-Signature=f10bf6016c37fc66422f354e85a87932739e8436b620c0dcc50766523b17843e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q32R6LUB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHKH5vjxpkkS2bc8Ewg2mpwRBQN6xrEE80JbkKZztxcGAiEAvBAIsSBcfxH0s%2BYqZMEEEG6MSyoxXYEjZBDjkRy0ZbUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHLiqM5mn2OpnDVH2ircA9YDLKsOvnmYhth1soqKEl3H%2FeESqzkrk9DssKi6r8CwAgfq%2BhINiPgbjN6poVItQHFipL21cqjUe4bQx35L4IwYN4ub1cZFtKBHGf6FBFNNRoPyvHpr0SNgebhh4XP5WDyznNc4bXMdQifta%2FLSKOAwxDAh3ec56x5B4nmp3%2FUtWpFk%2FzvK075f32bNXMCrNCC7aWHaJs4UhFTewWyuWwMRl6QyW29aG1d8%2BA0vwqTg1FcM8vcQ%2FaY0kharkp%2FCp7rGOQ8BmL0oLcQX45d3sIvTI%2B2A2F%2BTvVAij8iLFIsi%2Blz0ak5Xscb%2BwuWMH1Of6w6lZ8EcEJN3NTZpZmS%2BgbJnCIspGvQzkEqt4UpoVHNjHKZRccxCaRrymn2s%2ByHGJ2OJEokHUFQ65nFH0cSavuwgHzhlXK9auCfbzYrcumg1n865saakBFQ5ZkF763FhxCgadr7ViD4DGm2sa7dQLfLBLweKoSHTYQ905N%2BhGrw1wGOidEg0Is9rWx8eOvVJDVlL3zQIDZ1tumb3ZWOLubJkGduZ7iKumzROfaPhRaH6zn5CWWaL7oGuZL8t7xUPTt6gr5V0lxWz3beM9fJz1EaBygt2tIDA8JgmLGA2CwN%2FN3EMvZcVZT7G3RV5ML2%2Bhr0GOqUB9daH0vkLgsOzN5DaG2IqPmg%2FTpQccHaU%2BkV6KNik0IGT%2FwfOLIWq1spRPUPQjD%2Bh0%2B8sRufSYn2CCNP4EpaOzTWYb4KBr7AYcPAuSsv4ertesRaVnVszwDbeu%2F%2FwFXykMhPzmsRLUwb8FYyaKTPgSGohWEQXHDSh3psPn5LFU4haccafp14SM58cpXZ1Adco8PtKhqFRklLrVoebsap9dmHcgS11&X-Amz-Signature=876718a6933865e24b4e41adccefa2a5918d78d9e242132e286d6d0ee28fca1d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645SQWVIU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIGca0HqolQQbWqrylilQlXj5RYTHt281gcIUJJmnMpf2AiEAoSou3SpGEal9zyXof7c4cJBpyA5f%2F0nFViaG6xgL7gEq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDN%2BTH06cvGKLOTUmTCrcA5TewKYCr%2FA9CjaMFJ7y%2Fr39%2FeCZDFGiekHawv7JqigE0UogKKDCm2cNSfV0qqrgBVUOPPxSIzfu%2BOBsdUZ9okxDM3F%2BQleao08K46wLHeW%2BYCg0mtriJXOhd9B72SHGpX2R430QNEMqkgJwJ6FwqSjN8q127KeB2kGMlbjTpWQ0EzFDTigP72GxniuvDc0Vj018l68Hz%2BGmeLzHmn7PMRNRFo36K3ZXVZTgDUCtOEtQeLPwaFQK8NRX8e5Pk7y0PILNSWI9Y0bO812KPqan7asqr1E9q51tRKwJ6mucTTxzYfJdQwrG2BkiM8uXHhNl7tLNt%2FlLdnHBgzEXMoxv8MEhSoVar3UGMOCnSyWOGXa7e%2Bk33LPi6w6Vi98Xbk9PrMyRHFZxnUaJdvYaMJlXctGRAyPDeC3Sb6egtZRNxLeabBYwRfRFg0yF5R8IcU%2F0TMfyF30zoboEBugEpSMEPxcH%2BC4%2FWfi3vvIL%2BVxrl5hWSw8N8%2FYDcKLbV2tniR%2BcfOt2TqBpywzhH3N4ClhEOk%2BCjlAhVCr860b%2Bl%2F8THPAnbPStvw1OsBlj%2BEn5H23mVFcG%2FXXyuZuAGgPiw0E3iTp8h%2FMJIxE1Vvzykg8UN%2FlYd84z0zCoQP5v5iuBMLO%2Bhr0GOqUBgRgqfvaU5WCauNcjADFdIlTKIDDBJDzfHuc9ykDffM8iyJCuhesFXV%2B7sVafURxBS2CHWJPb9Ct%2FJT4wAIq90EDS0JFG0c7ciD4iDojwojenjPhkNMyoP1qeqbPv8%2Buq9WMFtmbrMId%2B5SL3Ywv5sWJxPJPv8iWCwpMzFFHRallUHhGDN100C8oajatgrf%2FuFulUUEiS%2FBUhsoAkTopRFJTRQrV5&X-Amz-Signature=f6bb518ca964e0852fa6c0194c10b532028df9d80c039caed002c1e1bf52a408&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EDVD667%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDZ3x9Q%2BX3umKSCJVt1P8FzA6%2BO6fQDKrxicOPQALgVvAiEAnlXg7WWp2ZGCZkkrR8fogb0XVhG4BE9q0WIgb41QGaMq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDKjOm6jH3SsxyGpcmSrcA7TvW0nvOsPGf3Knhs%2FTqTCpBmWZMTKw2dwl1EfOPqqkwMFDThA82A4SIGwgsQG2kiHEA416C99uu9rwWYXRBC9R221l7%2F9Hqw0k2oPMVSSbqOnwo6dhffprQ1DrjweOPISK82fncO6aa0a3g0n8Vg4An9ofbg4%2Bp5ZOHu4YuLiezDytgwL0RTiQ0MYMblb8U1T5i2j5uzlQVzT65fbqOLmcfi892StaeGmrucshD2MWkVvkE3zRhZn1IytL9cxbGPdWVDc0vNn%2BvLN176iYPCJC5FVUOldDrCmUcvtRpMvUFNFjdZRnixRlaHZkACDX5XpqRcnt7Bh4OTHaiQgdYDTBX6J6uVpbTIcqIo0fdm9G6taLyyNAWumcDhcS0ZsZFOjA0dbJPzegs8PNp4%2B47VCLfgzNqUnlIE0VZTkfnKpERTeKAH2QGdrQ5YdXCff%2FFNXpUpGpnuBsBhuZyzkF6FkfxFwELiv9W%2B2wLYLmqernT4fJ2EFfYL%2BzG6o80tpeCSLmf72kwMc6F%2B%2FYTZdV1oS7BHEX7firv0p71iEKqtyPOKFACfjF2Z0htsc1WX0ND6cKPQZdYAcsFlHM937Yh3oNmkAvsJOc5%2Fv9zKrjjcJWA2eUJWLcXnPCeqoRMIm%2Fhr0GOqUBTsRnx0DjcpJLax2pb4Q%2FyY6F9IUHX%2FCZlOtcyKfvx6L7KH7pB1qQfKgy9Ok8aaLnpIJgk9JQvVn5O3T5%2BP1Slcj3e2c9nmZN2gprpJjkK3AfHAJxt6BDCNfxCdUTGR7rm6SNASGNxxQAoxxNxYpkLR%2FL4lnJ6Hr75GWIlI384FoeUZDMor9VJPKgEyVFaM1tGs4D%2ByD6HDQ2uq2lJOEsRLTLjpYx&X-Amz-Signature=593a6d8f56b80dc59ba2fab15ca6c0cc069012fc4abd3f867b66d95c0e29587b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JEBDA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDbBF1myMVcE7pMZPKnaTmVjDUuU4%2BQxZRg8wM7NcmDQAIgaKfIUgBj0%2FrzZyooKROmHuLCAWIa%2BnzTwHhNsxChMkUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDPsenEevNcDOz7vVJSrcA%2FI%2FLQmpP67PU8vwufrJKxaUfbcdGw8C4bSGn%2F8jSRwEWMtIpDDQMcDR4EcvN3xc1tiMHYxl4mb6OavEDJQ1nRvX%2FQM94xHmig3WkHgxjktNBVZg5tglLdm6bkWBCAJI0LmfFhFgbNsSxs0Ikk98NAAY3T%2F4aLiy%2F1wiCx9VoXmqrZDj6LnlXhcWwKxhc6va2QSn2twoOhaQmmp%2F7G8tSuiiV2%2FyhCWFNdZjvBdP4OI%2FFXMvH%2Bu%2FnGixJEZfrK0o4wF9fPa%2F9mZPKFTCRtQz5ffwDuevEGiAKb7JvA3ce2ZKpWGn5WT5IEPxJ3pS%2FyD99FyqHVNYwxOzqnpOhz0qDNkxWQtxc%2FoL5igE0hXvH7J7YDlBQWu7EqvHmlAROPqK9P%2FC%2BrSMuR0kZ39ALNCwyqKa1wWyIF9RUsQdI8UobOVbYiV2bbRDwZ19z98%2BVFuoMFRViSryi%2BxkcuDfaKCgMskaKeR2bqcX8vHZUOHkQocbCizkS4SdDHuNBXm1sc0dfHI8Z8lGRbkuwqUtQRZRJlH7fK1EMXJVkF7ulDB4odtPE8Fv28K18NO50tj%2FvD0CI8CJ7k%2BlKJgY%2BDLwZOA4fcNT7VLcbX%2B790PYMW4cFvoXT2kpZW9i18TV%2FxOCMN2%2Bhr0GOqUBPMwmD98bWeXz6qPDf%2BPzdDiplGMV07FNMyU43PNMmxQmGhjxB8SLJOBmoXzNv1NHgSTdGZHlKT5N4Mn7RG1StbQCyrBxuqnseC8%2BCXe%2FWpWrBmshGfex%2FweKHDqcTca4qcbIYjjMkIEMHpEiUBM%2FU6bI98VvvbtRZrYQgzcYOrtY1xo22Exq90HTuG5gJRo9WfrHFRtOvmml50kJ0IbEiyBF%2Biu3&X-Amz-Signature=63ba2d9331d02f5fc0d208ee68014a05cc8c393b41ddfe9912da1b844d6f8a50&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCEEBXZG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDnjhZod7McRratPdPjAvoI59g5aCPt3arP2ONlTQ9zEgIgZNKty9pp0aliKaFYfQsqyM45BZj0TOK%2Bb3hAqGm6e4Aq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFwga2BOgBGDvxG7XSrcA4W0e3GQz0c%2BjAzmIYQwqMtnb4Px918YuaWiYsEKGFNhd%2Bp8Js9baWj47siott%2Fag0jCuFi4gOEhJVdvELRA7ZwWamCn15C7Rfxbmmcv%2Fo2wG%2BHI8qgEKsH0LMe4tssfNTLXG6QnOGsIVBcJTH9XLoZopOzjHgPnFolTgKe64BzkdJuc4nZ3JnKLy6%2FFNK3mClCi6BiVL81rH5j6ETcrwEY1s8YGIdIlIPhx8WXNzo40IKwaDSkgTf5f82X7%2BOmMWap5f%2FSsbDHNGBNXUFeaRX0LGSqfychEpwJ6EDs6WGiYY7LUWqMCuzSAZ3PLJ414mHGFES5wnBLyxrfVaZjZk8g1lr7rUklhbgtDjue%2B33YYkTeR1UcaQx5Sna%2FUy3nwITK2UPZAixPauHvcr168lJ1wcK9vfz8uje1ZqEXsBx57W%2FBUzioi%2Fp6wmd8EPzL6OdZ1BWU22ovs2sFed2wQC18NnjUX3%2FIRAf4wpJwTeFKj8TeLpjWj7fdHqEOQ0GLSjMiAkNCTP8xid8jEb8P4mFr7UtQNm9gGGRNz0owRe33cfpOBnT52maxJNdYxnXs7YI%2Bq%2B%2BLb4EObwwfhvlfmCg%2F7vLSD18TLTVTmTIyARtBTQiwJfpN%2Fxd4%2BYAB0MMW%2Bhr0GOqUBIHTDdlVdZt5%2FB%2Bb3J5R98bDqVo2ubmU4rg90EmKVvtmI%2BymEk%2B5UmH2NaTKjR%2FM9pfhITU9CBbIFKzgQY%2FUJ1YY9bMlXinE2vjtXiRals6v7SKipEfoP%2BC%2FQSaEQowEoDFiO9HgofD3zJkcwya8NzUlY075yK6bt0Q6QtjZS9SLhZqsIAqAl6K0bm%2BL10LL5k9%2B35UmCMi0gEwtXvs9w29fhoQFS&X-Amz-Signature=ef521660993ecfa2a109defd701df0d761e2b546753fca97ed93a9d5d0f8b99d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNMKW5A2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIF83a9xf%2BAiCYmgt%2BnogpjoC1Mpup6vIt8RFdvF0QIUHAiEA7bikBTtXyeFrgFV7MnMoR42WdZy0xPZ9qcydupRHSm8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOCoVhWX10BNED83JyrcA%2BIAJWPppced4u7FUiIIoFZRrPk56V7GdNDelmbel%2Fm%2FG7FzvSUjZnyY%2FA8wwhNVICzgbMwngKwiLmjddXjDg6Axv62TEGJv3EbL3SUi1wo2uxYw%2BqOzxBRy3lRJ3CC7nnmtyjckH3j42r%2BLDGbe28v18A6%2FdTBg3sQc7R6LT8kuwbm7EaiejH80q2TCnElcNXO8P78SlxthRp0nJ5XLx2bQ9OmKyY1WJHEA9jMRaizihlVZeSSsQLv%2BLTYC6DLG%2FGNb3TY4Yg622aye6aOPIafvps3YWV1c4swi6qNAalICfLzZ%2Flobl%2BHY3WwGq35nntUDioOcCJenBOa0WW%2FPMr3fvagidGKYyPvdN1pgrrDjMY1oWFwovN54iCsi517%2FN%2BsgGI2WznWJ2uyojbpvDmXXLNzk76%2FwG%2Bb%2FeFPwSWC5wD8ejqinAKc9aPUR95jzMRf9uDsZgin1rvtrVVDsayNM2%2FRWQEhmThuFnPIobfuisN5CXfGasixNqbQtHuvUV2mKGi%2BjJzVmln0MexKZu72VMR%2BolMaAsAK6%2BJuT%2B4PLWcYAcgqWhsm5Mh1bFTmBrbGfsc32TThJsx5HNVivNvh6QMFpESUv4kOgrLAfXpu28qBcFdqxp1CPRfa4MPG%2Bhr0GOqUBzk1w%2F4xYPwcVcNYntC4SuF65I%2BxK0xljJZsIP45hfFJsww4bqET0CMs1no%2F5j2atyE2MO5r%2FzBmGA0phV%2BDCk5tWjhntCwJzZi8bZ5DciOCayUUjndr1V2K8c3hdbZWOdXDAOtNZjd9pziuCTO%2FcJKbm4jyqrIfLNpYls3JrqmX3w0ZvPtasZhct12TAb56iLkSH6qBodUe8iplqpG2v8k3C9kG7&X-Amz-Signature=b62958187e7250814587aad8439c09c8e19c5485c87ba18083468cebdeac7c43&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNHAR72V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDfZvNoPrrueX02nDXae7GWYVLFGE3xMEuh6GOf2H3rNAIgYC2nI2hsKVpwVdivwUhw7hVZDBrxSpzWtWb6J3brBKkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFkPpyTkFahWQfeh6ircA%2FC7K98vDKTww7EQdyanoJCFxWPDJjfPXCvM4ELAiQffRges%2FEoWoVqis0bMBuke1EPCCh9o8ME00PEx1nUnSbY288a7fUUxPKFqbCICNTukgJozVY3ipzfWlfa0GzCqcZKZNBTmQ26W487s%2Bx3vY1TnpUWQEBcizoCTzt26tKhykjIq3IgxUkw%2F8k9XOzxS81rfiU8Y%2F82OM1La6iDsw%2B%2F69gvHlqkj0GYxED5F4g3bNdigB6z9u1tu6fYw7Z4JPjVqBeJafCXp8To%2BaXRgmpbd%2BqgaLjIMumk2aZDevdrE807MYq5hJvEfN7L7pE3t0t0cDjvH%2F5BzK7ZnXVy4GnqLSTun0lh3A066o8%2BCF62cAUAYI4jfozcbm32HSz3oVR8l%2Bea5hHtCYlO%2B0mWI15sTkKYUPLdW1hcDpLGzTZoSiSlikJE2gB%2F9pHUknNDFQ1DCporMA9%2BfJSySccvdc4oNwSvwHhwIwKPFMbJvtpKF4Tie%2FoMU5i9QF1Skcges13Y7KLwS8PKUYTuPWbZXuK%2B7HOKlABNeaWzOhCtoNBm1luc8rxBSuOJSE5XBwn2UnhXfuCp3uiwOJm7auw4W4HQn1c2Dj15tAateDc79QJWQ5FnmUGvES5tsTH43MLu%2Fhr0GOqUBsg2P5CAEf63%2BCzaaV8YYIej1Xg2NG%2FN73Q5FncZebqf6v%2BzWOAca0OAB%2B0pT%2BVwBgZdRQkBcT7%2F13p%2B03a3dWhGxp5AFPW3paqDGFC9ni5%2BBJFlrKS8onY1761mYI7irGxf4a9CdV83fzpViaaZ%2FuDQqhBsta1Qpu%2BowGXveS16xhbmEIGCGKbzjzWYPPPHADyPcfBv%2BL6%2B7zqBFQHqtPZQsQVDI&X-Amz-Signature=a4ed0202b0cde396256626ac131d22d9a1b1c7ba0f9243d1eed8be9772a9b7e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JEBDA%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDbBF1myMVcE7pMZPKnaTmVjDUuU4%2BQxZRg8wM7NcmDQAIgaKfIUgBj0%2FrzZyooKROmHuLCAWIa%2BnzTwHhNsxChMkUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDPsenEevNcDOz7vVJSrcA%2FI%2FLQmpP67PU8vwufrJKxaUfbcdGw8C4bSGn%2F8jSRwEWMtIpDDQMcDR4EcvN3xc1tiMHYxl4mb6OavEDJQ1nRvX%2FQM94xHmig3WkHgxjktNBVZg5tglLdm6bkWBCAJI0LmfFhFgbNsSxs0Ikk98NAAY3T%2F4aLiy%2F1wiCx9VoXmqrZDj6LnlXhcWwKxhc6va2QSn2twoOhaQmmp%2F7G8tSuiiV2%2FyhCWFNdZjvBdP4OI%2FFXMvH%2Bu%2FnGixJEZfrK0o4wF9fPa%2F9mZPKFTCRtQz5ffwDuevEGiAKb7JvA3ce2ZKpWGn5WT5IEPxJ3pS%2FyD99FyqHVNYwxOzqnpOhz0qDNkxWQtxc%2FoL5igE0hXvH7J7YDlBQWu7EqvHmlAROPqK9P%2FC%2BrSMuR0kZ39ALNCwyqKa1wWyIF9RUsQdI8UobOVbYiV2bbRDwZ19z98%2BVFuoMFRViSryi%2BxkcuDfaKCgMskaKeR2bqcX8vHZUOHkQocbCizkS4SdDHuNBXm1sc0dfHI8Z8lGRbkuwqUtQRZRJlH7fK1EMXJVkF7ulDB4odtPE8Fv28K18NO50tj%2FvD0CI8CJ7k%2BlKJgY%2BDLwZOA4fcNT7VLcbX%2B790PYMW4cFvoXT2kpZW9i18TV%2FxOCMN2%2Bhr0GOqUBPMwmD98bWeXz6qPDf%2BPzdDiplGMV07FNMyU43PNMmxQmGhjxB8SLJOBmoXzNv1NHgSTdGZHlKT5N4Mn7RG1StbQCyrBxuqnseC8%2BCXe%2FWpWrBmshGfex%2FweKHDqcTca4qcbIYjjMkIEMHpEiUBM%2FU6bI98VvvbtRZrYQgzcYOrtY1xo22Exq90HTuG5gJRo9WfrHFRtOvmml50kJ0IbEiyBF%2Biu3&X-Amz-Signature=d6edfc844077c7f406887944a0c3bffd382cf090e62313d40ba47e1dc218ea11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625HOVVUL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICNjdxl2YXeTWJMXJWBI3naLa%2FJcPEAvRueqqhH3zc7hAiAa0YjSrMyTmsuA%2BjrLtUs0M%2BmtSZSX%2B%2BMLerMi2gnapyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM3YzITvCPOwUGQoTjKtwD2NV%2FeiKp5A%2FYB4q1l33OHlKXtPXQz%2BNjOtMCtnOuueqzBwwhOk1%2BRF70SqYa2rHv83edufyCw10Nqe1WSf%2Fz%2Fk9TB68pwDVX7cuOphb%2BdoW6AFwtAePgdq80NkmtNBwdK%2BPcgtsEejOi0jcFiqgA%2FmI4xmDyTTR2TRwf5zfTJzZ%2BLgnuNBBONq6ICchMonX7T7B5sXK4k5BhRAP%2FzqbcDefwwVRIflBTHdG7paZgkktE19JbcV9RulQ83RbXYwZEnIk58fbZ%2B2f3mv35niHtSwqw7aqxhQY%2F6vN6Zk6fDt24lVKLLMFhgejHQNHBfCIgfVOfnkszcA4fGG7KIVS%2BrR894DtyYdEYCxjyY7QSMx%2FSOfT5eU1Qh2njcpp8q4NN4x45FtYe7POK%2F1KQNhK9ROGJk7Zwl3yH5JIqSzpt8svhuISkHs080hD6wcuqJGHT4wibvvGtDEVXlB36b6EmLXx4qvmP90sAxwQWA%2BlQDByDrzo6LZkQLH%2FsZGLyngSZdCvrnFIjcJCyF8pt6bI8HGEv9TsS5eHHzNY7fHcGa1pyDBX45k9IDykEkoro92VbdpK5s%2FA2gXOvhZNY8Zeq1nmcfEhNJ7Z5M7Qvh3BuY8pAb6hckysusvwN6Gow7r6GvQY6pgFLLV9yhzYslYyl0a0JITQxYfEyAJKNNERmc0fB%2FTMVqlqYSU4jW2LTr7ldcNBm47Pve9Nrdn10JMt9lNpRgegdbx81lKTHUS8FgDHj8QQ%2Bwn6NvneFDbP3kLJZmlJGGQ4Gs0628moWv4P%2FX5OUF4uBbx1GdC%2FySlM0Xq6dbnMDHysG4VRAizPk2x1YE7h5kpZlgYEI1xzh7%2FfAWW9TOXqZvud1T26y&X-Amz-Signature=b6d1c14bd4b7145bdd1e9a895a485843e01360b4089a98edf6d5281eba70f1fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625HOVVUL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICNjdxl2YXeTWJMXJWBI3naLa%2FJcPEAvRueqqhH3zc7hAiAa0YjSrMyTmsuA%2BjrLtUs0M%2BmtSZSX%2B%2BMLerMi2gnapyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIM3YzITvCPOwUGQoTjKtwD2NV%2FeiKp5A%2FYB4q1l33OHlKXtPXQz%2BNjOtMCtnOuueqzBwwhOk1%2BRF70SqYa2rHv83edufyCw10Nqe1WSf%2Fz%2Fk9TB68pwDVX7cuOphb%2BdoW6AFwtAePgdq80NkmtNBwdK%2BPcgtsEejOi0jcFiqgA%2FmI4xmDyTTR2TRwf5zfTJzZ%2BLgnuNBBONq6ICchMonX7T7B5sXK4k5BhRAP%2FzqbcDefwwVRIflBTHdG7paZgkktE19JbcV9RulQ83RbXYwZEnIk58fbZ%2B2f3mv35niHtSwqw7aqxhQY%2F6vN6Zk6fDt24lVKLLMFhgejHQNHBfCIgfVOfnkszcA4fGG7KIVS%2BrR894DtyYdEYCxjyY7QSMx%2FSOfT5eU1Qh2njcpp8q4NN4x45FtYe7POK%2F1KQNhK9ROGJk7Zwl3yH5JIqSzpt8svhuISkHs080hD6wcuqJGHT4wibvvGtDEVXlB36b6EmLXx4qvmP90sAxwQWA%2BlQDByDrzo6LZkQLH%2FsZGLyngSZdCvrnFIjcJCyF8pt6bI8HGEv9TsS5eHHzNY7fHcGa1pyDBX45k9IDykEkoro92VbdpK5s%2FA2gXOvhZNY8Zeq1nmcfEhNJ7Z5M7Qvh3BuY8pAb6hckysusvwN6Gow7r6GvQY6pgFLLV9yhzYslYyl0a0JITQxYfEyAJKNNERmc0fB%2FTMVqlqYSU4jW2LTr7ldcNBm47Pve9Nrdn10JMt9lNpRgegdbx81lKTHUS8FgDHj8QQ%2Bwn6NvneFDbP3kLJZmlJGGQ4Gs0628moWv4P%2FX5OUF4uBbx1GdC%2FySlM0Xq6dbnMDHysG4VRAizPk2x1YE7h5kpZlgYEI1xzh7%2FfAWW9TOXqZvud1T26y&X-Amz-Signature=d173b9ea79be2440ee694b88a586646584b86cba38b77ed1324101f80fc5419b&X-Amz-SignedHeaders=host&x-id=GetObject)
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