

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IMRQPJ5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDo5LbDi%2FR1Nt%2BjlQ1q%2FOTzw4cQSQPCO%2FCinj0OAnRc%2BwIhAOh4UMi4dPYGWO4bBPYrUfHdBbPRUC4YMlZcfcyVOjJVKv8DCEIQABoMNjM3NDIzMTgzODA1IgzFr%2FhUZo4sXSwkookq3AODvRowrBYFDUX09VS6BVaFHKMi9r%2FnRv2FoZBZoj5lAgVoRy8QtcmQwz%2BRSUXROKfesXbqV6tYhBezebiE9QzAUDApD0X2wWYUUSNY4TnkvccXbF4RreztXi4UjHQ7RqXVUv7lIebtV97iMA6xNl4beANCt0X20%2Fuv9yAvGGo3GMGXkwHojOZjaK1WIak9toN9T4vhwTXOnFleJyU5%2FGC50dUlUGKWF904VlZUiIzo2lUNV8qQyLTJZVOFhJ5am82GjE8ccyNCMzVt7noJPdEHad4uSx8VA%2Bn4VRfhkp639u8pdgnzaAWhKVHc1CBHtt524GxL0tPSwtEbQB%2Bx8%2BBxdhV0llYh5u1KKgCQLQ863szkngOuP%2FF12zsh49NDUyWHBgunLnpNopdku2iH4EI6xX6Bzk0I55m0XIivnsoIZOxvVge1WSM4DV26iJPGQaKg5dLtS0uTJCeubqYqwHc4ZpWt1loGmGfYwMQvT1gyy5rkXKuQPf4vunyrOUIPtT%2BIYcIBMeOnI5mi%2FpaEbdnoLA3fHk7p%2FGFFJaMGamt%2B3MoQ79OGHFwMEbhyG2jbKmU%2Bh09FD%2B3UG60sq0otSMcAe1AqCaamaYGiM%2FkknIr9Gj8oevma5ScyjjSqVzClz4y9BjqkAaV3NorH49TaSrytknTPqFK5ZUutKcE11bPvkvBZwx%2BfYaTFAB6DdPxAegpS0iqvsbxkFB7YXILa5rLYwcuTsBfB9qprOChZBoKwFCsTLZfGnQGoS2TCnJnxamV243rFQsk%2BYAudtkgK2ZNps33DNS1lC7yApEsVcl5cPnkbevegybzpqUwyUsV%2FJe%2FI6iH%2Fm%2BmAppPN1A6Fd6cXHXeqDnwRzEYz&X-Amz-Signature=1922b2aaf222f07ac4d3ab6d646b69665e7a01946df33b92efe63813cda39919&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS4UO4TL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCZkHgqVDNKYkUMuO1eKW7H0uel6IEuniedjV%2FSOJiURwIgMNrDhJG1q3csL3xrs8auSC5%2FoBg%2BSMaI4XJSj%2FWCRacq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOx3NlGgLliWot3PlCrcA6RJ2BIcJHrlevuVlGyEsJO%2F1afACnfK3SFo40CVyiUQDswUIf8Exrm5jTH2eR5OIu%2BfPopqC59Of5o%2FK7W6ZaLXxPcwwhuOKAd7jHXiHIgXezaEWGXtz26Xx%2BvSAdM26cri4qGrAyY2hWHaR4QiXIQKFFPi4wRDt%2BHEPkFY%2FFDiQ9YvVgcyehChuzCg4LEWOkJOz8TZ%2BJLQ8WIyA%2BQawgS8Xqtp3t03tVhFSnDxQEewRfzsoY91pzpMGTB1HarhvxAQP77kdD0pAOQDhWzsGSpwsTboqtoeA5SFH3tjz0yaRw21aooNuwiGx9xOnGvL3bKFBZGqE6I2EWZlbA8tYuLEZpAFE64I%2Fja%2BPI%2Ftasd0yQDEhfReMiFum0VqUBUs1w925y7ZA5iJxxU0QvM7OdyZMPWttNfTzI1LBmMlbW9JrFtxLZ7rCaBDrca4n764I0%2B%2FM8b6DGWhjYGwsMD%2Ft4MgJJl2cVDP0JLT7mCTWe%2B90ft57blN64WU68vmPKovyd8rnfemwAm24Cf4vqDnxfhY15KP%2F0WnObskpdPui3KL2JSWR48kPsomZwKFonL37REfg%2F2mFF%2FF3%2FX3Ev6cL3%2BcOrE5hq5cxqfkZgCDAcVOT9uUual2D7FUbpV6MJXPjL0GOqUBFKuPxQ26sJrxXa5eckgPqnBu72uaLNkX9Yb2DtTSMVD0sgcSDqtjqcgOfNzyaZMFEzye7BAcxRLxJm%2Fa3P213Cbaf4KMiMYT3XdRx7He5GXGzAfCvcZINhfbOK1LZn5P8bvP7AnSAY49bosdDYWtLven%2BuUFWPWxKhMrq7JQbs6Q0%2BCqpF74c3vJI2EGeG6OebK5q3iMekVZgfAikso1IXDsD2sk&X-Amz-Signature=22fef65d133e22ba7da21bc6cbc5708d5ccd3be8129f83e1f0b09d399c77fc7e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPTMAUC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDmUvQlDqCGtArGfk%2F3b%2BL%2BEi8%2Flp0fvfhueQdpkLo4CQIhANc2xlvmsqYKEoUDI5%2Fp1rUV6UOZRrx9puE84itGqWcNKv8DCEIQABoMNjM3NDIzMTgzODA1IgyFkEyI8hZynaGtSvQq3AO87lNW146AXuKnci3nUrBaBPga%2BVmSpNDVjQCjvJakN5nsf5Qu4stBkwcy75K3zJfiNygzTyk0TM54%2FaTZNEAbvYCfbsT1HzHvFpO%2BV%2BNsnv1rbdLduKhqnLVEicXpFWh6qYL3dY%2B4N4EVvDHDIZI0jO%2BnMc0%2FM5v48sPFw5XB2ysSpi%2F8GyXsINgNLgpRV834FVwZGQekHNhUUquIItek9qL90irFEWauePF1lxRopqwolVRJz9aJbe%2BpGDtSgxkrzeA%2Bz%2BGMjf9uvs6QRNnN7WYhvPYOpBZ%2FcqHEe%2Fg8ETE43agZRnHtGZh54QwFxvz71Npg8QvhtJi76vQkXyb3PUpfCVm9pmuIqcrrSnGBgfLjxndcDS8datbCC%2BF84H0bAYKIQ4ejNuTV%2FI%2BphCNdscy0tDJMOl8QtNzIAhbn7BaxM1Kcx92AACPdi1nwKEjVl8ooNk5mcteO%2BTsq8PwZiTWa2gBYSorTobEJv7scmnpkuRO9%2B8FE5gGmKAQmwT5bj8kX3dN0%2FOqaFa%2F1dJhCYNCA%2FRVE%2FCWE34z2wZ8zegLNLL3vkAHRz%2BX6t7wfhA%2FkBmRkrExI5oKqXoWGwTz6Duj9CO1kozXi2r9HztSK%2FQ%2BI4wgmmlFBm3pGszCEz4y9BjqkAR2Eregy4FRcnYv3oR4JFPsRbjA57%2Bg06seUF65oJI5jRMOeiRixRkunMWRARXmJE0gIZPt2BE14R7vs%2BPHZzH%2BMBkkkYkcAzqlARRKyIEd0Zp6K3BYrx7nh66hVcre7qjor1Isgbxj4JpZK6lbW3LeXazVINeqhEmzyHVmTWdtwjq3Z8g3hkTBJ656FU5VUD0jRgqHG9mz5CTfD%2F4WC48d4BgBO&X-Amz-Signature=58c475ddfccc701d5626ab0e9d0276b6100dd3aff30c37e5dc7854405625705c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIOS6HPS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHvRFs0djTa2sXv2NnZlfa3PQAWB%2BglO4HDZxMFUeA1MAiAwVeBt2%2BL5TeUGvFRxTyKPCRLoaSs6eGDKaSSIqtvFlyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMjzai0bE4wcaTn06IKtwDnfX8Y7guPC9PI8Ym%2BkP8d028jYvTXtPZJciej%2BB3XBCFY4%2BFXTYKF2MlwA92NxyJz3glqJLFNEl6lLlf7TIurjQANEC3Ji%2BlrmUo40xpwbzDh3v7p3kZQ%2BnKn2XNdJ69hzEhqD%2Fa7a0zE2%2Fkv1LNmVTh%2BpNVBWYjYkSSri4%2Bvnl9CPMdqcQse81f15D37G%2FMLLn%2BWwCWmCKQCBG%2FbpJ87F32Bzy%2BvKpFL5ZYMRtQw7ocgEqVXmecQWxnP58RK13sb8bE5Hkv3E%2Bf9Ixjk7xK23sAwcnKGuNDI%2BDM1xbEIAx%2B32wWS50P6t3oDfhknh9tK2%2F2QCY6D67ZeEm7Hi3T9KH%2FSKXCnB%2Bqe8%2FwwfsjjPJHrI3Ro4vdjINTDpS3z4BEWnpGYY4%2FK%2FfRTjIE0HT%2Be3TdkBpo7MTscUh7WbfF5wdQv2WolBy30eQAzWBWedZnPngw3E%2Buoxo2DQoP8F6YtgWmne6sOEeSlAOZNCP0I7lj%2B4zlQTYySx898sk9jDY%2FrrNgtHDSMr89dBS%2FGrRk%2BedbWTE0Ld%2Fd27EIe5L60ljb6V6KW80sI1gpGHv%2FsP1qOhg5YtZvJKhJiik6uxwhzjdowabG2WjyGMKdTWt%2FMYn63KUwdWS3IUYy0iAwns%2BMvQY6pgHLxBmmqG8KAxw%2BpuswQTT%2BoJ%2FJ%2FK3G%2F%2BE9F5ITenFaXhQIO2HDpt%2FueSjMxsxMNGA3oTpY6cuMykB0k5eL3983jt5RROMXkvG65SzUdkx5LscOIbFixJqkaUBVEHIWuXTcieAJfXpux5hhUuxg%2FfymQ9GNmDR8YhKzfKtMxUugFXlv5ZF8ZTdiJtOPcF6Q209dP3JWy3AnbqVgUWykcACIK8nIg9ZF&X-Amz-Signature=1f7ffa1a3d244da81419724a50776957d1fcb9afacd9ee0b14eed0e7f24d4dac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL3QUF4D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDZw3j670XYR%2FAsJ0khN%2B%2BeLkQZL8eztiQ%2BYlCFX1tgkgIgYlEbMWg9yG6gDfx53glOOn9%2BitHyqlHos4nCA2TnVOMq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKLzvhcgdgPD9I2nNircA8sESdnWHlO1Dpr004YG1UUEeOLVij0FI3GEdVb4CeIxgZm%2F1wQtH9qQ6p%2BUyqu%2F1FRROuXI3i2uW6gmzijWGj9Ds6029KvLuw%2F2iU7JsKLxyYe2OEf2cVRnyuYGJBkT0vGcXcLWEnnTopcKC4djW088KgoU9uqBHUZ%2Fa4KcJfH%2FWlG3loRnj7xayCQX9QW0YVxdFANnF4e7M%2Bb%2BCPbcSwZVEehjUBs2K%2BRtkag7%2Fhbmp2gIm2Wcy%2Bhkwc1zxzBiX0vI4UUjNqDzDnn05hvnSWo85naYcA%2BmcwtpbJ09APZJfQnBle8wJ3NqWh5lAuBXNdAz8VPS%2F%2BVtXjiverQZoiJoU5oc31QG3VbpO%2Fij%2BtahWE7PfoPTLmbwLt6WwKHYwdg1EpbkuH7VGxA6imN5CjsOZViKHCrXVubY5hrT6TxIyHhm9S3ww2wscXF3RQ8cWyzavuV%2BNDmxXmo5Br17zn6ovSJQHrs4yhgHFlD8N6uFq84fgIWlQ53ErwS6MQVRjwhPfTsyJP25%2B9rYAnh459DJA10GFFC1QnOdnmJ9zhrv8XIwfo96L0%2FJba3V%2Fm9crfRbBzxgI4RPLfPzjSQ%2FpNwS88gfjOuUlKwVwuUUtrL5AC3EaPjs%2FVGbzXXEMILPjL0GOqUBYzRlNOw6GsdMk1s4SO50dPasuIDuC12QUXWZ4UF%2F51xAPcn91ZsDUh84tseiY1gzCZj3kXl5mps5TvQzOY4O9lSZl8Mu93dX36VPwn9BEEJO%2BBBVJKzNPYeUGP7O8YGSL0AClbEjUAD3MExyGR6UoEJm2BNXtfPX3Je1osAjEEOp8G6sgXiZ8x37Gh9Kj9TUqdFUXla7yo%2B4K%2BRnhlje57VEGxpX&X-Amz-Signature=69511549fe1fef40c94bb604df62196cb69bed14421f6890634b215342a2d576&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQCTP4PA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIDvnBIld4z6a9Frv6ljN%2FtOVmMnI3sGZmFffIJLgwv5vAiEAsu5EOjzxbkSeuXSMhi34aiw8GhdrKCfKDRLtJUbGjw8q%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDIZFxBTt1qqMOtWQyyrcAxENphqAxV3DF8K8KESd2c6Y3CwEeazBzE2HzxK5%2FcgaMWPHkYjnqsU0vgKjUlrvzK9TTwhixe5cap%2Fp%2BmKK6ZxjllCox3qc7uF%2BL%2Bw01qCJq%2BFAMrSppMj1XgW4iZrmwbd92miry7i64TL9624hitbarSpXs3KPsi%2Btq8FHSzW8JtInpj5w55bX6rc096%2FnrLblL3ryOA0Q8Vn5fbMaQEBmcJvL5eLERMo7k1PxxywgCixRAcSe%2BKj0rFt48ITwC6r0LP5JxlCnZXZVmJIxM5Kf4GI3nqAZINx21i94T44mgvRDRf3mbKHW12yyRPrlSsyUT0q%2Be8hX6JpaM0BMVbe5uW2D0t2UmlI5qvI9L2ZaCMO%2B0%2Fd2tkjooOmqPffyY0lGRYENHP2EfCtlBni519qIov%2BM%2F1C%2BhLL7huaMOTbqtkY1LS9xAk8XqCCmLzZF7tOmCVNnSgbSZ2jcFsHvdJ0w0QdYT9mmCZmEjxD2Cw8Smtyc6hPXBhqUUCs%2FjKt6VH30ZkJRUenxd9aaGwvT6OmznkU90sU5ZOJLzw8usi60bsqN5ZqYH%2FCuHxVZV%2F9dX%2FpE2JT8g0d1AQoWpBr4mNzdyZAriKtMNur6E%2B6apKnCRDXbpoMmAdkPo%2FBLMPnOjL0GOqUBPa49Y5bQdTrRneBiAMevqGA%2F0DOARkBc5AtPI5V6LNF060GR7F81%2Bau3IfYGAIxmWzeEjhyfDm6kwM%2BkW5VfLSa5XygunRy8kam8df%2BRDtbIhSHleU%2FFSMTZSYJUh1nnf6Wj06CaiJy9CbYzlOvw28jK%2B3z%2Byni0kVF78gxdaMxffwQ6abeaKoMUOgbEA4cS7LLiGaEv1QW5twETQfbZmHnwDtUJ&X-Amz-Signature=96d7fe948d4d07f310ee8dcef7fc5dd6813bf13e01855564cd462eeea0d07d8f&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QIBAPIP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIH%2FS93ooGaBFPEcaro8RmuXX9%2FlRJJ3%2FzGCEodraw9SqAiB0HcvsiTPoVE3%2FZ3U8xVrsm%2BHC1%2Fi5fPPmEPONK3V%2Byyr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMaLMncY25v6ux1%2B78KtwDnZCDh6%2B8N8omoYkg1FoF2HqToR%2FMXqIcNDf9VSelozgWQXB1abjqus27dU6frMw3LkZqwNWmzSp%2BRtxQeFUi46FvGJzcxs0h9V9NVyAh60kUgnFZCE664pi1ux1sUyQlkF0W9VMWBETwH%2FzdiVtERf5xyeRaETpGjjI5IPY%2BXcxfLE7JPkmWtsg40%2BLy1RAV6XLP%2Bv15YPEVdLg6ROxOj3DR5cXy9GTd9fZZT67WItHCleyXg9TFVIvLi9XW2gjoeJjdBQZeBpy3%2BKLQbeoP8iziPUNYgUpVrt7VQR5mRYxpQU85s1JD4v3qIbE%2BjcL9rU4C4OZS11iyJKETiqFUskvjH0lsZY2MhcN8Iu%2BdqtbqxrGHTi0P10b2RiTO5aCDcYIKbWRc4QSnHhkDX2rE9MsRHqqCGMl7GsKWQIyb8NYjsjE0kDXiZemGZpC6gTf1uJVO1U6KlnkgJEBKc%2FtFy4DIwl0sgYO%2BU8PAvZHASNQ7twlV03nRwcebaQLGm73R32C%2F7GhxSqs90wnwTAIO9lrGuMe%2FUBSyAf63kMZ7XHpGzs2on1wslhnhGOxMy%2B%2Ba08AI180AfyF5RftAwdTegMu6Js0DM64xgblh496clm%2Fyn8uwN8b%2Fvxx3QwMwx8%2BMvQY6pgGwS2IASQEzRW7AhuEUe5R55%2BTi4xzp%2BGG7zIF9P1xE31YdLCYH4vLlZueJmGt%2F1rW%2BAoXpHvod3%2B3ggng8mfM2MZGQAj%2B6oFyoKcteicZUBkVPmUxJgZeCoYsvEz9w4K9MlGvtUtiR46gWd3o0D99ttPQPLpJ43ojPhFz4wOC%2F0ZA30S0ccqutdZW9NUae%2B6WCjrrE1Zj5SWtXFdH9byHbFEFBNs5w&X-Amz-Signature=153b72c50d1a37bd6bf63a50e665f4c460483005a5a8361be9dece2a86898ce9&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR4VZAX5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCOFHTSJuYUWoobRU%2FDWaGwOCdMI90dHEnrrHRPGILxmgIgc56NyXRcr1iui5mqsib7SO2AbimdiYQrVTlIWi1d5MMq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKr%2B6ojuwMDXMtY8eircA6XVeDAkSVTqcTCEBYOmXrIqCEjI%2FM%2BJsHFsigaBtFh02n55v5Znh5G75nVcFDizrWL%2BclzhdCbPU2Nwet1HmnxGK%2BXYL%2Fmlpb39XqSUfQxgrny28ssVm2UjuPxslCbtC0yD6A0tK%2BcORuTeA0m%2FCLjGJue8mEdHZITO3rulW%2B8KeL%2B%2F8BAWaSLk619bBKP9LF5BzcgCsQJYLOXjLuW9Kgztu%2Bm9zTgmFYL2%2Bbgwu0tZZRYQ0fHsxruJwu6hVnlVGKBy1JgyUNx%2BbfZjdTvAGPSlhp8nltz%2FlglWkDM7OZ%2BqAml7hWmNqqXoi5uCC0dzvO16XsOQA16SoF1mqbXkP8Kpo0oR89lgDrJ07C3Uf6hLP%2FPBBG2JuOQ8rdXAcnVVOc33rfEE8biDxKdy%2FIu%2BubRPpgEke0tvw24FQ8ukKGlAK%2B2J434bJv2C8M7yhRokwZSKuSsZo5ih6EmuJEKih4k6J1T%2F2%2FlzcDZBWWQUdUAztNeJGA%2Bt9XNujq8%2BSXXjY0amHtmir9%2Bs9TIjItFSx33nAzdjBZLM4xXVRdxm6xgyuGp4kzIuGxPBkWSMobiKFT5647r0uNZ20VFkztnD96qj%2BKxF5L44%2B%2BnHQkCIacXFCiyc3lRpiVsKBJAjMPvOjL0GOqUBF45JUInd9Hih%2FPSFSrn089aGySNJ1opEtPZKjlSP3NLIkY0bLXcVdoeO5%2B2uHqsK%2BVSg0lswXPNE9RZTF%2F7pEIHk4pUqkh2avZZdrY5ldRli%2BdK4JVymMdmFVVlTVKKutveTlxT3X9xtN49kXs96A3U9uoT%2FrZyVyQjeZY%2FaGw1yIrwsbuQNosByas8fJ3OIcd8i6HtC9hHNI48%2BzvDHhXlj7lB4&X-Amz-Signature=e01bcb1116fb43b3eac7777e760bb1f5f34f1ab631b9c55b8c446efa10f7e03f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL3QUF4D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDZw3j670XYR%2FAsJ0khN%2B%2BeLkQZL8eztiQ%2BYlCFX1tgkgIgYlEbMWg9yG6gDfx53glOOn9%2BitHyqlHos4nCA2TnVOMq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKLzvhcgdgPD9I2nNircA8sESdnWHlO1Dpr004YG1UUEeOLVij0FI3GEdVb4CeIxgZm%2F1wQtH9qQ6p%2BUyqu%2F1FRROuXI3i2uW6gmzijWGj9Ds6029KvLuw%2F2iU7JsKLxyYe2OEf2cVRnyuYGJBkT0vGcXcLWEnnTopcKC4djW088KgoU9uqBHUZ%2Fa4KcJfH%2FWlG3loRnj7xayCQX9QW0YVxdFANnF4e7M%2Bb%2BCPbcSwZVEehjUBs2K%2BRtkag7%2Fhbmp2gIm2Wcy%2Bhkwc1zxzBiX0vI4UUjNqDzDnn05hvnSWo85naYcA%2BmcwtpbJ09APZJfQnBle8wJ3NqWh5lAuBXNdAz8VPS%2F%2BVtXjiverQZoiJoU5oc31QG3VbpO%2Fij%2BtahWE7PfoPTLmbwLt6WwKHYwdg1EpbkuH7VGxA6imN5CjsOZViKHCrXVubY5hrT6TxIyHhm9S3ww2wscXF3RQ8cWyzavuV%2BNDmxXmo5Br17zn6ovSJQHrs4yhgHFlD8N6uFq84fgIWlQ53ErwS6MQVRjwhPfTsyJP25%2B9rYAnh459DJA10GFFC1QnOdnmJ9zhrv8XIwfo96L0%2FJba3V%2Fm9crfRbBzxgI4RPLfPzjSQ%2FpNwS88gfjOuUlKwVwuUUtrL5AC3EaPjs%2FVGbzXXEMILPjL0GOqUBYzRlNOw6GsdMk1s4SO50dPasuIDuC12QUXWZ4UF%2F51xAPcn91ZsDUh84tseiY1gzCZj3kXl5mps5TvQzOY4O9lSZl8Mu93dX36VPwn9BEEJO%2BBBVJKzNPYeUGP7O8YGSL0AClbEjUAD3MExyGR6UoEJm2BNXtfPX3Je1osAjEEOp8G6sgXiZ8x37Gh9Kj9TUqdFUXla7yo%2B4K%2BRnhlje57VEGxpX&X-Amz-Signature=9ba13d810e47b6dfeb7c3a9e975fb8bb22b3584f29a359ef31e476cb4a50fa28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IZSPV6R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDr9ussYKRXqe%2FiLvUp5muKr3L2G%2B3NJfXXVHKFcApDpgIgPSWaGxs7UVZMvByuz9CqcZKftv3y5dUUphViygUciqgq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOWXxuaoynVYQFWTfCrcA2sfTpNKeAp9o6L9k2dhGVxvQElakXkynwcCI2MwAPTdfcB0o0MPeF6zNYYnVw1HdEB2D14Io3EzrEbUq5nTmeiAOFtMUKWs5bJNrjqmFcAioZd37j61PlzfnR3X%2BrrgVh9d3jl84Rw%2BzGu81KQZJnpurihignuq%2BB6lVzlpF9qPrdNII3%2BEUB43VVPhqJ1VPOVlwmyC71PQMfiPXpE29NeAGcSsNQSbU%2F4scxzsZtawBVQsMidg3roOXiwt8VajbNrJwKe88aBL5bekrOrLDFblgqiChAyhAvNw4yePKBb328Y6oGu84thJxFFgb4a7KAG6zC46mHGV68rXjp%2F8sSn7Ol%2BWFGRZ%2Ba4fGzkkwDzql%2BFvTbE2%2Fg2HecTfkaWUbMJ2OPSi6L0UybJAz6JVXtkcaOM%2FUjVA7ZqE0BYsyRuQ0TzFr5G8bfzs4QH6buYs0J%2FqgsSnyo1t1gU4tGu55hyPD3gsuJvxIurKCxjzZC1HEeI1VYivWXlqZnujFYvuzd43WE22pYDeSDWCA6lCvVHQVVMF0rPThXUrhYTI1mN%2BxTfr54DS9GAIcppcH5G%2FbRapMfii6zCFf92t6lcGvsXw09diuk03udIwpz8fY1TRpdUjYFoab9rh8SVPMLrPjL0GOqUBQ5IqekW2awLS0j5NWj1fsObyyrhpiP1gl0%2BeH3GfTm9aWhdUmGN3kS30YpYOm3RNawcu0FvlsagHJNSRzgeaEdiz4r6otE5S7id2Hx2h5uweLH%2BgzfBtMKX3ujmypt%2BAlnBNskXkPsl7xtqYfYoZqynYb0LngVII2aPgMsGJzv9mgH76qyrKqcbYjuqydUioFFCpiv07%2B1R4LjknR5Tm610BRdGM&X-Amz-Signature=171521fedf2942b4fefc1958aa32d1d1b2510a0e845114c9e7dda3b29aeb0af9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IZSPV6R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDr9ussYKRXqe%2FiLvUp5muKr3L2G%2B3NJfXXVHKFcApDpgIgPSWaGxs7UVZMvByuz9CqcZKftv3y5dUUphViygUciqgq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDOWXxuaoynVYQFWTfCrcA2sfTpNKeAp9o6L9k2dhGVxvQElakXkynwcCI2MwAPTdfcB0o0MPeF6zNYYnVw1HdEB2D14Io3EzrEbUq5nTmeiAOFtMUKWs5bJNrjqmFcAioZd37j61PlzfnR3X%2BrrgVh9d3jl84Rw%2BzGu81KQZJnpurihignuq%2BB6lVzlpF9qPrdNII3%2BEUB43VVPhqJ1VPOVlwmyC71PQMfiPXpE29NeAGcSsNQSbU%2F4scxzsZtawBVQsMidg3roOXiwt8VajbNrJwKe88aBL5bekrOrLDFblgqiChAyhAvNw4yePKBb328Y6oGu84thJxFFgb4a7KAG6zC46mHGV68rXjp%2F8sSn7Ol%2BWFGRZ%2Ba4fGzkkwDzql%2BFvTbE2%2Fg2HecTfkaWUbMJ2OPSi6L0UybJAz6JVXtkcaOM%2FUjVA7ZqE0BYsyRuQ0TzFr5G8bfzs4QH6buYs0J%2FqgsSnyo1t1gU4tGu55hyPD3gsuJvxIurKCxjzZC1HEeI1VYivWXlqZnujFYvuzd43WE22pYDeSDWCA6lCvVHQVVMF0rPThXUrhYTI1mN%2BxTfr54DS9GAIcppcH5G%2FbRapMfii6zCFf92t6lcGvsXw09diuk03udIwpz8fY1TRpdUjYFoab9rh8SVPMLrPjL0GOqUBQ5IqekW2awLS0j5NWj1fsObyyrhpiP1gl0%2BeH3GfTm9aWhdUmGN3kS30YpYOm3RNawcu0FvlsagHJNSRzgeaEdiz4r6otE5S7id2Hx2h5uweLH%2BgzfBtMKX3ujmypt%2BAlnBNskXkPsl7xtqYfYoZqynYb0LngVII2aPgMsGJzv9mgH76qyrKqcbYjuqydUioFFCpiv07%2B1R4LjknR5Tm610BRdGM&X-Amz-Signature=39828f27a904a19c467752f62ab12e5988c3d68faa9959032401216a9f7e63bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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