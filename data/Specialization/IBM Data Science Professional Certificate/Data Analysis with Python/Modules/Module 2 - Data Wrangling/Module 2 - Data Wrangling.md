

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE6U7X5J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQC%2B57ekZaCcd969BxHWxC1xaPu%2BcOSwHMP5%2BJ5tqKCYxAIfc1l0eIdorVMXYxmoajR%2FE8k1iL%2BwkPAYRR6JkGW8OiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcr3yYgYWTsxRWgLGKtwDqAXha0BRkK3IqEd9UA5a5Zt98PI0%2FmCOgPF8NdpyzZG5mtt%2BaNWh9Fazk67wb2a6DNI9uwcLnFRkZMAsek%2B9XVcrOjvW8MhSnrSryvoEui9PAQVqsQ9SODPOedzFU1v%2BGilObz4QXm%2F0RSKbFMeoaXtg%2FPeki7bxVl3D1xM37FmQ5WUgctmdZmOgzvU6wQTSfrm4Bz9vi8g835ogB%2BU%2FwRQI947DEwHTkSxP81dY6NzLzHm3ckNEeHCERxled0wxkY1xpT%2BCiF1Y%2FtCvjcLsAGCi8TUmtjauwlBKhLAAU72WOWhpaYPPX5RSV66Dla7QHDG6hGFtjrAavJ6XLH9U2A%2FvH4ij92DbQJy%2FxLuz6X7gbMjtm7k1vyNOw4gYkFCjYl6ZY7673LLdKVRZdLweTe6NIB6SeSrsG4f8t6nx31SBRzsA1IWnN%2B5m9vN2J%2B59fuu79ZrfSo%2F7uFDRDl%2BP%2FCsORBI2NDcArXiPaCpqLZQfvrlXP9LWWhwN5pW04EqhrWORoytGK3AjsEHqPkHT%2FSM1RIvMpBj7XRQPAGcV%2BX7KwFmvnbkNbmR2WJTNXpz2B7AWH1hhUSAJS3HBF0y%2F34nBSsmsxOKl36mPXbRc1wc3%2FNGqMp16y5D9UnMwnKPsvAY6pgGAdr9uGUjyO6DeYJUQH4blTmGEz4VrwbCfdrSyxxbnH%2FOv%2FEsDGT8US3%2BHPmIZgqkOeVF8M3WTYRvSHm4dbQ%2FN4TW%2Fn5Ib4UlwzAQHoamvOkhXvAM4bZw92klwPoAYyla3L6Ibo4gcVi6g6QqWVkTPSSxYmVkaFn84f8twuWnUhscbIjShZuHvUshyO7o50oUb5Ngvg1YZNmgvmnI%2FGomH7iSioTTz&X-Amz-Signature=f2b400273113be97cc9e6f085f08618471af0434c5835215107aeef2c1e838c8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IWVMUP6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyANzlZQqwnwDhR3amtgRAaGWyr%2Fr3McbDRTe%2BnJ%2BJ5AiEA%2FQexjFIA993TW7%2FGxvj7S8oJDf7FLs%2B3n2ZNYi5ytjUqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDRnr2QYsS026fHafCrcA%2B%2BNbspxyS0zbh6AJ1cA%2FZxPxALSrep7d2NlaOKoqtgDSt06HpqwAN2qu85T8kO7rhwBxtL3Y2inITUksVsYtcSidqKt%2FLQqYRtmgGeYcf4K8RP2cgfbH8aNFLFWKPJX2p1IKdwnM2ZuSg7o7Ib8KQSWwp2Gpy0qM76IXo5HtTdmGMhilmP67QgG%2FQyqWwaKDl4OM3PJTvlWvof5lvofWPXT7EtvHvWfB9Nx0%2B%2F%2FhtKz%2FExXLz9UBlScURi8qJ2z60CFkXOE6VtdIWqJuuk%2FZTukCzrhEpH7ubYUbid0igW%2BfKBm1yudbhC0kOOscGlDrjqO59GohWZjsvEqKgp6GwkQiWEuBppfMIRBaRhd4SIcMl%2F%2BUMj0Pc62o25FA8nPALbcPRe8eOnpTl0zTN0MsO%2BWKvoy4J%2Fn3fIpX%2BU7k5tMnEQCDCxzCuADpZIN8P0%2Ba25DmWzezKXfWuOnWr7PKeV%2BVQTjpdY2I874fEPI%2Bgc22g3lEGTEf5psQFILxBj4016SptzJOgTZzwCXXJIAOTpLKmwbPfh6%2FnyCYNU%2FgGR%2BST%2BAGbYM7iOZ4mQVNK%2B%2FR2iNEqky5AhfORGvJ%2FQdtB6K%2F6m5JbE8fMIC5aEG5h6Zl%2BqnbxDqWJwHySIRMMui7LwGOqUBHkTrY1JldrLNY25oQSyCpv8fgiWWjJY%2Bl%2FLj9PrQ%2FDSfom0XG%2BG7060MSlIgScKnabBFsbKxGm78pOJitvye162WRDO9kSJJgyBrM1lJiLdVwApyzWJ0ME9Kre3vVuPfOQ31OHlH5pr9%2F%2BPFv52E6KKcgKIz6QHe2gOFctrKsj4EfRWeZoVqLhWmGvcgkLhrSRcS3%2FuNTc%2BmSVhWlf5ya2f8auBG&X-Amz-Signature=38dfdc5c147ee50d1d577aaf0fac7ffe741b5cf231d22cf851589b96ae58c86e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI7HOMHV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcKsJr4vfYDFP8rsOjTylgcceUEKt%2Fxdr5cr3VwSKmKwIhAIO3TQquaf0FMYJRomHpCR329doVd3gBsEcyggmCm3BtKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxk8FKigXz6F2yDdtcq3AMRlVhnneGdMS%2F0jk70BMtYsv09shgCIxBPkyePJo%2FRv3srTvOvpjsr4VNzV9ackgz8mQtmO2kx6SxssJD1RZp%2FEoyeulpwyIVEys65Ci%2BPpEu3DOE8RPUZDEhltxXNnCGzGHEbx%2FlFxehP3Q4SYhy3TRTHL5oDo1L%2BuM1H628zzIm7Xxldyt%2FfpfuKGrUK7TZfZ34UdzA6HP5i1dDp%2FcDcWNDhQ1GTDe%2BgFl%2B%2Bs0yf%2Bt8J41a%2BkxzTrq3Rqz5Wrl%2BMG6RL%2FzpWT7lUXgvGyEgHttUirLVucAwqly5o5ouPyCabfdl6bMLNP6%2FfmtGMnO3m9WsF1IAyOK2UkjsvyVvril7Vy13ry0Tf7TnOxT5H5AaCFCmhr4oYgKb3xXPgSf8dn%2F1KJ2S2yNS0cTFsg4rX%2BlR08U5TLg7eiY2Cs1Kb%2FNbZXbBbKDKsx7Od0ttCmhFJ29x4ZjDTvWVsxWDzAauS0HuuoBm3QnFRlQFinSkHmMQPn%2FJ0OlW4stQ5J8s8w2uZsUo5SfBVbjpfENZfdoGJpGUJkeu1k5ZR%2FZORpqyAVeoeIXC3%2Flpt2ZDBYFVhqJ5K06y1q7dGv109sVrQiDYRQm4JEh4AARtW1Q4OAnAi2kSxn1jdB1NJyaXWpzDOouy8BjqkAT1alo5KT9PBjps5fqIJx0JXUhAzuzmtjquJic3%2FpTPCc90j%2BUcKzWEA7eyOIlUnCf9mlg5EZ6LWaRSQ1kE5eGW63lCDiWyav2oe1sXODOwPSlA1Dhq1Q%2BmcTPg4l0Zv125%2BSJXks%2FpDU%2F79CubWCTP5nbLStuGv1uad2bS%2Ba7dqKWK66W7%2BcI%2B42%2FEnYlzOUsW2TwvMuOFVgnusL6mQEL1fs3Sa&X-Amz-Signature=fe00230b5b3811caf183b0f1e037d891280b95d25c858fa1f4566f0ffcacee62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6CMKQAB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIene%2B%2BJDx0WHeal2X6nHah9b2ppjqlJrtg56L1hqrIwIgexbiFfOY1mjAqVHuyjvNZFODfTDCcfc27Ul3pm2RlqwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5zMjSh56djvjC1DircA%2BOGbKzbj6hhKNbhS495GiKQT5CH0TgAHqwEULvtnd4c250ZPQppuf6q10%2BcwLs6V%2ByPDgShhGtRwa6PKlfyDlyP4OUd5%2B0Vu1i7j8z9gWQJUhHmBeIMgdjKXQIRBRaY0wMRpBX7Or7j1xh6JvnM8VZ3ll3y42m15Xzv1OBZ30TqvD2OKZI99FKJvsNaxS7NGhH4HWZeXFHghj9iMTXZ8e%2Bo%2BzIN%2FubFRe8%2FvMV10%2Boghq6OgSILrVikFGf83r%2F%2BBxS0eKrBnmeeTuYmbyvVnuXQUVWPhcfQyrByLHd88x%2BfoYyhcYeuLeb3BfuMBVcXWBJQ3msbriNUjS3aYEg%2F%2BOoePFA6w68UydN1QFEShxlksFDJU9yfIpnv7yMppHBIEtYnc%2Fqx%2FWa0J1ol3XH6jpHTyv6wpVc8pk43oPZ2XgMYqrXsy4NZ4iqZvO35oCNckPR9AfeTWhMtxiQ15OzqNbBaCZTBuO4wryTfKZVt0z%2FPeBRK9bXVHNcfXHOYFFeuFn2eTRczauVWiDo%2BQ58pv4POZYFDFFGBxmv2j%2FcdUSWOI1Qb4oHgZqGLt5VsTxR%2BUC%2FD9SeBEM3xd%2BjRa9KbU8CLFxR%2F7i7Aq%2BCaML9LOnjvMcN%2F7nKWeEhiCvl8MNSi7LwGOqUBP20Q9xZSi%2BoEif2nxT%2BlboYM%2FC9NOjZsXjdJV%2F1HAC9NOkOcNrONGv3FAPCnDzZGzKjfomjgz%2B%2BlBZyWTXb4BGIvtfNWnzlMUA1VofDdwYB7bhFIsBkuf4zcPSr4Zjt%2BsVhL3mrOAKUqXF6yB%2BsIBWYFnhK2zWWj7gR0qsQRM72SwJGCfoJMg0hQ%2FbzDXrwPFaG1DoRu%2B9f114JthU7mROY2UPIl&X-Amz-Signature=5481bda6841e2d37a71f702adae3928e62bfcd2152e4e1fe3b8aa52bf514340c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636ZWDEGA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcOU36Th6CG2Y2%2BzKeyX%2BAHMxMTOxxOXAfSRzZKtPWZAiEA9Zal04WQ6nshrFwJ5s6UcPBeQZ9JRciv37rVKPoRLesqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2c2OQKFkPbbwUplyrcA6JDZoHcMiggXbt0XsiKUaGS8SSfu1fR%2B3xw6UnG10PmQDt44gDWDmODAbdGoNgmGGzLGUcTAkas6vsFbWOYE1p6uv2tXPJ4hopnLlpo263K3BzXc4v%2FhX%2Fys2DK5m19L3at%2FppZooOe5EwrIn1uoO%2BUgfD2tajnrozqrHALob%2Bdt3S2LlIzmYYAIwmGdX56w53DcxYIHr95yjb3wnDHY%2FlbKavwO6hw%2B%2BCxgyPOWXX7zqkyKxdx9mlEVXuIjpGF%2BrXlQuAlFFeR6%2FfxeVlVKGyBtnXcJFVlzfm80xDhtqQ5EWRrGIJc9gvku7MxMEKQn2MGJKt%2FR7FljqNMeD7loS7x%2FAMWlnqcdSO0U%2Fd08fwtL%2FiL189kJtfc1ZCfA1C8%2F%2FhCXRUEsk2UH6JUlCJwvB2W%2F0s%2BzxuV9z5H1BdAC0o9IH%2FW1g1hRNbWDll6QEmP3LlsfcsStJndKwfqdE1%2BUVDB%2B6sA4DJA%2FCaBZEL4hsVRYVDAb1ov2oLmk9SHxlg%2FRT%2Bim%2FbeIPLhFyr4ti9fzpy58Ja0X00PxOSCkb3KApR7aZmE9P6NzhesA420hsx1y7pg%2F9Q%2BgdOFLg8Lt%2FES5RxkBeShLV7fYC%2FOw9IjRV6%2FQmqdAwoOzjt5%2FvcZMMui7LwGOqUBN75clDOv4tSzRmPLzDFvtKV%2BulGLvmxl5aCw1QVA%2FwfkGNrTAjUOF5dwEhCHXU%2BiBbPWMse%2BZDUIFWUbUJyD8pOoBC6BGm6jAzGg%2F0H9PTP%2BsWJevc5ql6dp0H2L5yc%2FSs88F10OuxhWM3joHXIRE0OMXO5gJeFaVcvzGLatT50r8MYIjSGimF34NViVPSJI%2BbgIIytz%2BJFi%2BntTdUXFGDC1Kqpq&X-Amz-Signature=60b34f353c261e05b1f43d5af7658c98953f9463b5d477f9764ea8e9bbe26626&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SK4UEHI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYv7%2Fzd2Lo87WJ9qzIPxMhFi%2F6lwlVwtBwcgwYB4RpXQIgdqPIaAW%2BCPL2%2BbgKAlDjOPjQbFOd1O1hZD2w7JlOamUqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPM3l%2FJTFsTNZ9Q1QircA3aKeKtgR8vGXtSg2GVKmPNmcJHFryWEfPVISgco576VqMLB8xdQ%2F6WLjYbP8CnQkbOxD8TBgptykxJs7cjAPID9bHQf6oqshsfFN41hDveLveMhvtNrnfCbGV4rlpLrAOD442pgXhNQARpGMng9yoPy%2FYQSlPENdCo8nbA%2BWIjEQjjU0gGmWzWaIm0ZSyfQmXklGwUa88nVrzbs1OT5t322mIpPDKjjfo6bkJgM7ym2iz42hbB9UYUH8NkKRZkU4RRv5YG7nCvTPv%2FqWHqySdBbb2gg8fmftJStWU4jAeFv0m%2BxsRbgRzENPCQubcI8Igv3kOfkMS3Z0x4Alhue6so3ybhEKXlYhGu5rloHxNr4xtEsMXvcrJ772KfbIwF3d9fvZgxmLBsBAU7JSD5d7Ix8Uk0lp1GHquAGt5Cz53tLYYtkMTjpsOyoLnGAmc5kqzXmeF%2BmLgpB7guJrRZ%2FPdElZ51nNxIbfAZg5d3P1zde%2FEuJqMmVSkwpiIDXNzVo3bCGA2kdNPZDd4OvK7HPc6B5Xp1%2F9us%2BodxRePgtUoQVQV8B0OxU21CduS3WCF3QViP9%2BYKBVjpfeIwcvrJzdzYxE2PCWtG0gV2%2BiAy3a0GXy%2BWhXaRO7SWp6V7LMKSj7LwGOqUBLG9i1dd%2Fn0QXCst%2Fe8Nd2OS1%2FjTS6pZmfJCE9Fm%2Bl1pYW1HErzTcFJjCZxyTyBumdS4QdiOn2KDilFgYv%2FgvBSOob%2FPoPjBRjxp1WCiZbnwIzIFMxf98oBOAHy%2BKF9aLzFIVf3iVGL%2BhvreIQaCIpz6eQQm2jxWavtR9N0tXMO1fTJjT0mipiDEQAUq5i80IYYs9HG9mQFeRU9mfUNOAh7qEWNu3&X-Amz-Signature=9eaf83ff1597433d5bb7b7d0a794a66dfc09a0f6465946820c1ea3e85cb63638&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W64JMGB7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQD1G82JVYCNvWNxxi4qywdheKfdPNErlFQyPojqdjaQIgCC3y0B9RHM9SYok7kKeCN%2Bb2F5bHHuZgbDshox8dBKkqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA8DDPmTqVDcn%2F8BQircA9zO0tqlGLWZwTipZLu1RYpUR5sOe9a9INWrGK2nTTob2KIxZyj%2B110nEIbTbaL%2F1mS5NHAzPXjLtHk9ulenirqtwXQkO9lFw8tf9USoDDRLMuL2eoWoakd7%2FEXUysu4ugEWX7liI5sW%2BdPu2kWVDYqAV94tGPHZ73Ma4g25PqVbOyV8a%2FoFWhv96bihn1E9NcBRZR8jzlqEgT27hLu8Kpmkkg2DlBwZnBN4XA9E86l3dN8sNOVoq0wdXLrrcoFFtv07RBUmFZpNed26jmu6h3iWvkAIFHrALjUfjXebxtFLZ%2BndLjWg98qZhJqYb4%2FE0F%2BlKbYmpRH3VdVwF9Ut9Il6kSwErOGdaXQpPZnJ6OEAfDEi0XfUoUQYS3lZVDZK6s4gIQxzBmhUYd3TQYKEpbV%2B3u5zZHKGTQADOPjexq7VXvykiFTMJUm7p%2B2wPJCCz5Mbaz7c9h97T2ly1TvD8ImrgWzpljf%2Fn37Fzeb%2F7qZ60Q1THwAzF6W1kNyrlTMlY8eL3%2F8h9RofoFVEcZ2PEKjxEBOW%2B9vIOmtzvChr4XONLZ2T17ulgbxBSoeor6BcJ00Ud4ikZGT4iJTDsc5nSyqzkJeX4RBy8D4VlUstpBsYdOTQlQudu%2BRrLUjrMIWj7LwGOqUBhcielwBo2qQ6YdRacaa5ng8pwe24QPw1GEwN8R84MLUGp4JBKSW5YJLfI6swcE6Ss9VSPjEGVB2dYqf83VxI1B8Ry9GxfR1r40rMXcoITrlGQWcvdu%2FT9x47wLCOuHnh3Odto2%2BrBjJ7kdLbPenxfoWUzaU%2Falc0QN2tMmj2uNKCtRgnWVNdAVpF9QUMSxpVTc6ajyut9C0ztZ6VdDMbdL8E8uuj&X-Amz-Signature=21b4d3592a799e919aa9cc309f686c06787d18dcf9e4dd1d1a45e2afa7810248&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DNX3SNI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZJePrT8c9MknhX0SVv2pAfCVelL9AWxX6lB8gyo%2B6NgIhAJ529RkHSn1C7aD6JbGK8XBWLKCIdHw3oyc4t2uN91JiKogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwusZuVxG%2FVG41kRDAq3APVFGayQnVbXeD6dsHPA2DopoOVeRiR8hYJ9gK5QLBtjKSXhcBHClj4HB1iNzo6Mi2QORAdyEPJ0gXCsHjl5yVhV%2FM0HSZbD2LNdif3WDwdUmkOnABl5LVOsk5tVZHgkszcjAa8bKT6UTasE%2BP%2F2xr7m9YcDTj%2BpmE84%2F3F64x7eqbtgx2IXCVjAxC3hDOLVg0Iyw47OBSYuccQoxhbhzPWFjqx9cFfVqt34X1duQAVuQSITJ4VvWDv6ZV6HCj%2FOrR8H1e%2BYAC2hUgpgrWaYA1w18yljCB90D22lRLlzzyGpIQtx9f5KZx6jf7r4sFOJOy23Aq8hyt1chk8qxaz0zePuCaWz3ljkUinkCWHtHwSYPH7kz8IFfbYf2Jl4eO6ikz%2BkIdSTXX9e5DXYRM3UThq4OszCQJEhJd2YvD0kQNrZuiEjz16iMmJAPCND020Otg1Fb%2F14derMEwwH7lOgGbpml2vWzzz1I3Z6u%2F1VxNTfGk2U9pOkEFqVmJ03uBpbTQj3lQovJXYgGe3eYlbYFgXvcyLVEJGIFwEX7DgNb%2BFBedlE0BXrX2ipgdYpd60v2Rq8JVUhCsGbgU2RJq2PgJvG59SWYUoVMcpnPh%2Fy9ZnZK2LUIV6zal1zzjigjCBo%2By8BjqkAbtBr5OuSmx9KYahs5P0TIAVoTNILAaAcjLgeKBN8rPEfi6C%2BYiDX99CZvF7q1kfa7zJHIHAI%2FRCji2XlGDaPgfxp9zVSfeWTzosIHZ7BYFmd74O4D0%2BJTIIkoGEfmHD7X%2FhuZ3o6sSoivKeCAVyv8L7iS2WttDCI8hYIxTzwgp3zSZcW08TKX2nLqGU4DfcYO%2BaCFUMC0mghqpra5GE36llE%2Fl7&X-Amz-Signature=7bd381fb36569f7c874b11855cdb10b11248f3edd36a9097991e0ea36900227c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636ZWDEGA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcOU36Th6CG2Y2%2BzKeyX%2BAHMxMTOxxOXAfSRzZKtPWZAiEA9Zal04WQ6nshrFwJ5s6UcPBeQZ9JRciv37rVKPoRLesqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2c2OQKFkPbbwUplyrcA6JDZoHcMiggXbt0XsiKUaGS8SSfu1fR%2B3xw6UnG10PmQDt44gDWDmODAbdGoNgmGGzLGUcTAkas6vsFbWOYE1p6uv2tXPJ4hopnLlpo263K3BzXc4v%2FhX%2Fys2DK5m19L3at%2FppZooOe5EwrIn1uoO%2BUgfD2tajnrozqrHALob%2Bdt3S2LlIzmYYAIwmGdX56w53DcxYIHr95yjb3wnDHY%2FlbKavwO6hw%2B%2BCxgyPOWXX7zqkyKxdx9mlEVXuIjpGF%2BrXlQuAlFFeR6%2FfxeVlVKGyBtnXcJFVlzfm80xDhtqQ5EWRrGIJc9gvku7MxMEKQn2MGJKt%2FR7FljqNMeD7loS7x%2FAMWlnqcdSO0U%2Fd08fwtL%2FiL189kJtfc1ZCfA1C8%2F%2FhCXRUEsk2UH6JUlCJwvB2W%2F0s%2BzxuV9z5H1BdAC0o9IH%2FW1g1hRNbWDll6QEmP3LlsfcsStJndKwfqdE1%2BUVDB%2B6sA4DJA%2FCaBZEL4hsVRYVDAb1ov2oLmk9SHxlg%2FRT%2Bim%2FbeIPLhFyr4ti9fzpy58Ja0X00PxOSCkb3KApR7aZmE9P6NzhesA420hsx1y7pg%2F9Q%2BgdOFLg8Lt%2FES5RxkBeShLV7fYC%2FOw9IjRV6%2FQmqdAwoOzjt5%2FvcZMMui7LwGOqUBN75clDOv4tSzRmPLzDFvtKV%2BulGLvmxl5aCw1QVA%2FwfkGNrTAjUOF5dwEhCHXU%2BiBbPWMse%2BZDUIFWUbUJyD8pOoBC6BGm6jAzGg%2F0H9PTP%2BsWJevc5ql6dp0H2L5yc%2FSs88F10OuxhWM3joHXIRE0OMXO5gJeFaVcvzGLatT50r8MYIjSGimF34NViVPSJI%2BbgIIytz%2BJFi%2BntTdUXFGDC1Kqpq&X-Amz-Signature=e7f6eac5a77ffaf9c1b40ca680fe363e8fe906616e20bfcb75ba12c00efeec8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RYJNWZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICxTDt0L0Egx5MB8djshCDCX1BsIrWd4eS%2FocD7TNNn5AiAve%2BlK2UvHkorEs7vWNw3DCRJqnat07U6fqQarrd5c1CqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPRxzKb4022cy6jm8KtwDXd9YLCDeJXYAtIN9iyB67Xgi46vcWUh%2BmDQDBSc3YmWPDpRbnFNMrKZtoypJYYeKOC7j8XetHSbBWaz%2BhIyr95ofzz7nDG5OWD%2Bi8MiBXsy0L3aRjrXJHd0%2Fw7NNgYVDDbhdzhrnZaZh9B0Zw07e1fIy3o0EY48yQ9Hd6slgoDxTF5cA6cY5Ty%2BEF9FLq34ONOaCpiomkIUPlEDeBppbCxPNoPVrq4t8LHSPRPvxNndGs1AaCJHCOGqY8YtQ3Y2cEIoMehL2AHeeui4iB4e6kugjFtukpp7wYAukho%2Fr%2FmqTtAaZnqMVKRB7GiEGRkfzakobQdPAIdcPvfWOUvrhSkFNRk%2FL6L%2Bfrt1SG0ZxYBJ37IPNthdn4Au92dY0Vfkpq6QPLLgwVYyz22%2BiGCU%2B8nm4LuuZHMOH8heq3OcoV%2BNF2teowjO26RTOjY1vuN5%2Bc4WZwpW4vjXvBW80P%2FPwOKBl5y%2BMaTAy2Rr6ZacyXamBJ730KkQwuWk4p%2B%2Bg6QA34kCEAGgizCGjuxmhHkYCWV44dDqdiqb1VrgoO%2FtwSjnymPesTPwcgzaXIArQmahBUkGWKWXsCFAb8FbZ%2BTVr2QjNrOYLEGqkEMO2MwaK%2Fwh06TOFwNABG%2B%2BJ3OEw76LsvAY6pgF7Pzq93sbRaK9DGMfFF%2BK1ylTuFrEV9jI8hcl0jeU718wUIuEIv1dP%2BeTv92f4mSIqJTx0RHNQCFJhfRKf3PbNCje3yeKml6HTENotRH6vxpoy%2BCjnq9b2Vxjl0mLKszaAr%2B1N%2FAOGR0VAslaQk5QY9lUESsCjaP91k1nY6lLVxXAjGBKXCioVhjgMMZ0tNG7SfAIKwN0HwTRjZdWVUekiIWjRWzR2&X-Amz-Signature=f62210b6a2ed545eece930b0fa58de33db0a43a3efbe8ac38c91daf21698d998&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RYJNWZT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICxTDt0L0Egx5MB8djshCDCX1BsIrWd4eS%2FocD7TNNn5AiAve%2BlK2UvHkorEs7vWNw3DCRJqnat07U6fqQarrd5c1CqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPRxzKb4022cy6jm8KtwDXd9YLCDeJXYAtIN9iyB67Xgi46vcWUh%2BmDQDBSc3YmWPDpRbnFNMrKZtoypJYYeKOC7j8XetHSbBWaz%2BhIyr95ofzz7nDG5OWD%2Bi8MiBXsy0L3aRjrXJHd0%2Fw7NNgYVDDbhdzhrnZaZh9B0Zw07e1fIy3o0EY48yQ9Hd6slgoDxTF5cA6cY5Ty%2BEF9FLq34ONOaCpiomkIUPlEDeBppbCxPNoPVrq4t8LHSPRPvxNndGs1AaCJHCOGqY8YtQ3Y2cEIoMehL2AHeeui4iB4e6kugjFtukpp7wYAukho%2Fr%2FmqTtAaZnqMVKRB7GiEGRkfzakobQdPAIdcPvfWOUvrhSkFNRk%2FL6L%2Bfrt1SG0ZxYBJ37IPNthdn4Au92dY0Vfkpq6QPLLgwVYyz22%2BiGCU%2B8nm4LuuZHMOH8heq3OcoV%2BNF2teowjO26RTOjY1vuN5%2Bc4WZwpW4vjXvBW80P%2FPwOKBl5y%2BMaTAy2Rr6ZacyXamBJ730KkQwuWk4p%2B%2Bg6QA34kCEAGgizCGjuxmhHkYCWV44dDqdiqb1VrgoO%2FtwSjnymPesTPwcgzaXIArQmahBUkGWKWXsCFAb8FbZ%2BTVr2QjNrOYLEGqkEMO2MwaK%2Fwh06TOFwNABG%2B%2BJ3OEw76LsvAY6pgF7Pzq93sbRaK9DGMfFF%2BK1ylTuFrEV9jI8hcl0jeU718wUIuEIv1dP%2BeTv92f4mSIqJTx0RHNQCFJhfRKf3PbNCje3yeKml6HTENotRH6vxpoy%2BCjnq9b2Vxjl0mLKszaAr%2B1N%2FAOGR0VAslaQk5QY9lUESsCjaP91k1nY6lLVxXAjGBKXCioVhjgMMZ0tNG7SfAIKwN0HwTRjZdWVUekiIWjRWzR2&X-Amz-Signature=05f925c8e186896d1676544c11dc0f8439ecea1cebaa9565cc383a770ffbcaee&X-Amz-SignedHeaders=host&x-id=GetObject)
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