

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4BASZG3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2FeFc3KcmneFw1evuZjwZTWmCtAOOQMg6YGTHyL%2BgI3AiBno0AHwcdQlVuOkBHXsxBxlsAereSHQ3BM39NUMXClPyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6ptSKP1GEPgFSd5fKtwDnbrBx3wFYxEyfM2NE55rDIId6r8JbQs1HA04LiDLwUwHQkriqmmFAKUdyddnE%2BFtUMZ9k7BBWBRIcRBjSVuJRgsS91Z%2FHIns4ZjD77S2b%2FRFNFaZLTtqQmjSPFSiLdqvdESTsPv%2B%2BlFtTAIAwSOpqpLPBvnj%2FEypE5hzZe%2BKp%2FK8%2BQr5u9U5%2FzJ0Cd80wzobMcBPJx4WxIdeJLR4%2B3agdFJZl%2BFIpsXkofikPjtFpNgDySVtOEhA9nGNMQS75YPi%2FUDCPD7TXGgWpEJ4rzUEhHyEIZQIOarH27vlbo6Min3QSfLIsMMgupiMZIhVZtXhTWz4yrvC0%2FbD7Wd56GHfuBINrAy9963BhDaoawBFNSKAUSV5qk%2FMAbVIwmYYltwV0vgOFDIbzdzLkqXBwjQDPOs%2FGM1Ygivedch6juXsHnOXrC007%2B1hElSvG4gvnEYo3Xv11gmtJ8ubscHsTD2AJpxj%2B2gRn%2BozR05FA778t85%2F34krozvAZeMlvRj8qszAXjnYmhHr0jqo1OIRxXlfvrlz53Bew8Uoqb0ScZjIwvkpJZ1ze%2BfpL8GpmChtI1kfm2aLvT0KJNcR%2FDpTW17NQP4SL6RF1YqZSVslw3uo2BUP6AYHH5a6mXoSUG0wiKX3vAY6pgFFGXthpxLcN3g%2B9C04xTSgGTkyZx5o89TwZ2ZBqq4Erd4hLMr3KHPauHt78eNy%2BYKvrNFi%2B%2B9QuftrTZR6WAUTGmfj8JcKsHghPbbTjznY7bV9DhcoB4Rp%2BbyPtUXhmw2i7TMyg6Qzvxy8QCQlq5iqkHQrsoiGBv8ojKkPMLWEfD6gpDb%2BN%2Ff6jQ3rCzN7Oe2kh7ZEostuZU4cErqfVrrzpaZL6V8K&X-Amz-Signature=1882d2a7734cb15f413ce1faf66f054f285803a85d11f236d735bdf8436fe1a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GOJ3234%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDOn4ie8TXkPXJdtP96jG1nJMHnRBahElhjSjSFBOTAYAiEArHtI2eTW8EJJP0xmjr7Xk%2B%2Bi24ifUnfN21cV3AZxNlEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVE8SWBLHNyiwpXaircA%2FRWPxh9Rzn88sLmaNhVhLT1Ps0iEK24wY0maiGud2TEn1l%2BQoXeezYHwFTa2dw64E0EhAZdXkfk6lkC0G0uRUXwqQ7NsSM%2Fu1Bqp6cJejEkE3a8mEwhg%2BiDmQJ9R610ugZH2Nr0cZyatqwnf8hIFY%2F%2B3iQsqe6uK67QYQABQv53OruYGAGInTPx26EIohkkDNSKlo0LdrCrEfW6QYXL4%2BLeD9oT3W%2B%2BSLdFkMyJW4W%2FWIDU%2FIbszGmmtJIYWrDwliPMC7MTR1nwL2s5VS0plu2yVIi6GqVeRHBHRvWt7BotA2CkGzZYxtxjbSRU4QEgmxpLCtWC3cJp6OoXwj2tcBhNhxS02ANNJnraTFqEgGNSr%2Bpk8OkknLClMeHdrWXRodV2JGE8Qc5NYQIMjnAkcxz1eqfBkP%2BljspTlZMD6dGjwYqJTITq%2FCpm8UmiiogAYpqSXBewD1TbDoV4ReN0VpZEY6Cnrq6rF2iX3eVLhemTG4TV%2BO4PzbP%2FiFjmt0u4oW%2B26niBFF72ZYRD9FpV3hyHuMjsD%2FgMOUYLy2s5auzbJHa92K1wyffoDXZhj6tE3gtb7P2T5k25U2sFLMljOjZsWfHJ9axaALjk72HR1b5tniYcYCpXjJqw5w6tMOWk97wGOqUBtuuKu%2BL33y77sGpDVQ4%2BHA5nd70N98aQ3G5nHP2uHoTq51ZUJT%2FLyHahPQZvf48cLKUwmIkPhXOMRoRw1OJ9cvUSHlHquE1Uw6mRFAjIk8DFFmvGX%2BnId1HoHqo5LXUJ5AbKxXKs%2FD3r7U77XRYnLjiU9afJsvN7LIO0FL24s308jTkuvOjMS6GjIJ93dHwrKOhNDGmET9w88v%2FYJQGTeGiwCfeT&X-Amz-Signature=4c5d1d76a4c244f5f4ed8bc51883f28729262895f409e04fb6d48672683cfd79&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656XDB337%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG4ZG0p6P55o%2FxmOXId3CaFesK86J8dyRMVYTWrEJoRpAiBbkNGWywPcoGiOQFb9vlZJSa8OF9XqSfczBsaN3QhlKiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeW9BL4fayjrClk9JKtwDWZxgjTqgNT75skAMg7Yzt0bsCxva%2BhpqGboYY5%2FdeBkLj64sY0eaKiAXG%2FwAOJ1PaPy34ga4rHyKNHWthMrX40CTIB3nRH2lWPqmtE6Fm9QOi4VCsKS3O%2BzE9AZCsiFtm9pkRpbVwCspnoQGjxWmKu4Lhq5yr%2FE43Z8SZ20EJR1knzzA2hweoj0xJTjKfxLaZ4Xtu0vB3VhWMBQF8lab9dMsWsLCopaymNyBPbMlPoRLEBLJ9RfjzXNyciPaVlAsCvq52fkYpmpYYY1cumZ4cpJG9m1MZvKwr3NP7vm8Nj4SOUnkUMS%2BmVvD5P89CTtOjIhJsUjyXhmvCfdMlJRePxlwvtMaw9XfxmaRjt4%2F3gWbLiyUltkMU4g2As7lsoBhX%2BUI0Iz%2B0lCEIO4Y6RE%2FUMaJukjoaoyyWLQyCxMSzebhM346AkK9%2FYenGusUqSMv70I%2Fse7BMBECyC7t7ZKCEWsTbYRsxbIhe3jEQayHHADuRMkXi2hNgn1k3DUwFAqAXq7FcdatZw7eKQd%2FWMJJZI7JfxwtwHjWTiPVYuDCs3j6lpXTdjUI0HWSrWuQknRa1mHkkdWlrSZKw%2FIwjgTOLL25WGVyhlcZyra%2FSR3kq2NzoS8D%2BFXWGWQ9pMQwv6T3vAY6pgHcu5257fNsbhkRsL8jPjHoMoQkjQ0ciC7KAH7ZX44M%2BiW4ap0fyhpXCn9XvOZ1PySTQFto1ocXzizjKXAh%2FJBUs04f41obRWk2%2FYqDYYE5K1te1HsKI1HAnTGKu0Hp7aHFMIDg%2FOn4IZoo1N7q02IvL4ugl151Dx2zH13myFnp8exDFh1ViNXGz3pmEph3XqY3oSaZbVdYTCATGEpAYbc7yaVN1KzG&X-Amz-Signature=35e85a3243c1af472e19ec63f7f4ffff416f3ee6cf248a44b80c5a6b765fc0e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JJ5NLUW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAi%2BHrdR9viP8yA2VUyJQEqfCMriDb4T%2FrCWOmcpO3e7AiBEHnzeTJ%2FcdVp3RnnuQrtAmvT8yWfjarEg5exkVlkw4yqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhYqu50f4uiS2qHuNKtwDxSm5RezkuCnUDE1mU1zQqOzgsEYVyGklRziCLhuatLPn%2F4dDSaxHFrTdQ7gJ%2BpSS5lmZFufronJSp4OAnlevjqPMNgqJC5BjQgqGitwejyhBbFpuZ1ClRx8w98QAPWm%2BlBE6BXyzaQ0p8MW43npTwGyUAAYF9C%2FzZptDjYyabyXx3cvlHYFvIZwsb%2FxFeVYEDqvcfN4LIWCnJ3pZlopqVwIZXx4maGAsb1%2F4WPG2zl4H0HGJWRlXTUbd05lh3lvw%2BF6oiR%2FluXZgxiBMJqMN3aHajA44q68B2a6miwj4LHiJ%2FSek7k1SjFtjYtW99FKWYCSAuFa4dcA1vO%2FgL%2FY4g9lUjk0Nv0zZQ8Jhdhb54TJu4l6jzGCfOrNGN9WvmLDIu3FZJZC1IYYx%2F9eezTRMMaPhkw0UcjGGWBoU%2F92Vu%2FnqjdMTsZkmvcRVrkjYBVw2ud6aLB3DJ12hY8ca3QcKrVJuBu6nHrn4LU25U%2FsklTrx63elJpg9DEpa4M0RpAFgcuGn2iieJ5y8ZQt3%2BCOxDnqLoUjBCRF3bCWrY8W5Z35CjuGk78R9EnD0jRid6POSc6hLbTgbZLJh9Qc6JelD%2F1Ed7ysFgVstpLlECeLPNmVjVqzTJWAoNKdrRkww%2BaT3vAY6pgGd9r1TbfNm8RdRerjDRqMynMqWDF%2BR3TvyTf8CNteXJeUOltyN2D7LU7TjN%2B2ZIRBxqhyvlldFcmxffHfn5ZarKiaecKrs1kbHe2sQ44r4SuZbfqV8BpIf2Mn9vuzm7%2FaBeUyl26quN%2F2gyZw83qlK9z%2BotXnQugIbYjyUy%2F0XO5dFgIaVFyAScMn5FGAy2VWyxWlC4YS30JfZQE3yGo0jL1U3mVAa&X-Amz-Signature=96a7d4384ff4be004808decbd724516d27bbb1e227f24c9c4f37897e15cb82a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673PH5NJB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmY9G7k16k0X1QZm9i%2Fqia%2Fs8gDdj4iOI5tUcgSviPRAiEA7oMUCacO6Viq%2Fu7wulnRTfwUViUheBmFbvcGQLkNq8kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHVC82hFdEuWKv0A2CrcAxpOcNh3qjsAMyy4OlbItc2zmyKyfGtdh46gCcQSUQhHB6rB2lJBTLSkb17XDFGgiPxyqustwsOMXFzZ7nqISArz9kBUJ6JiTfUpmTkNWpDHlLQAvV%2F3r6F%2FfSthipuTl4x0ngMhp4oBKL3ZTR696FO8otpS9bAcjtfLvwKLEuoe10a%2Bi4ySPFYicZ1%2BHpeqiO0TigCpaY29NvZFbwTvwX%2Ff0CQp%2FRKwlBz1T9UlYkylz9B99%2FQ1THlg2EF0vI6PP4ymuSceTvSYr6gRt3Fpg4dXtEsdQd8lWAse4i%2FC1Vlg8fnQOVxIt3muutedL%2BICgEXTLHu4TCkVsPlp3%2FQ3gviByEnaJVV1PlUqUd%2FKD2omG%2BuDUFw4Jkds66CvmkC1jLpk%2BXIlAD%2FBh%2FR%2BOGcKDn%2FK6T5w8kL5oq4efFVTKW64rze4k74Dc9LzneK1zI1rTZKROstMcPfBKlxV6yUck%2FpCfqP0KNpZ5r0EOPaxV5zTqFX2C4PEOJRhNlusNkVTd8VvKf7Hes4O2FltLIAVA1gPkmIHl%2Felt3OdqQ5X7%2FVaM5ZYeyQnq2NcaiFSMyldtU0Nx9bkOEq1u7BN%2F1vFo3eg%2FLk9F6piXKIXF3LrWL9aTv%2FNb9%2FBzdKD0ltuML%2Bk97wGOqUBFtvMHA%2FgAI8m0LhQdDn9Z2jM3nCpoP%2BkrT%2FBCKdn1G4Hghj9TfWmgy5a2hNiWrURS4cVAjomtbEfDeMYGmzZgX3IN%2FWMyb%2F39K7hyjAa4Yd%2BgbSz2HfNfrUVaVMmphFfm4jXz8epWBikw1swe01D%2B5h1US6HAVNksnmmqNtKPWswQAeT1GB40ZYg4BusUDdEMKd5nRKYBhzhED7kKTfKKRavOVM8&X-Amz-Signature=414b3ee5020d393ba04013982d93c1036b063568852dac327fb8b67de193805b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWXJRO3H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBx0hzJi%2F48HblXkKKRy%2BVmVdlIreDOocpnIsKdxw5ZQIhAJ4NN9ospUKB2k1kLlWJQ%2BfbENoi2wTZdT8kwpxFMii2KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDPLBmMYsF73FT1z4q3AMviFc11bW1O5Pl1EkjIFET%2BlsE3m3EcR5XefNkCtBdzrAoQ4jDMLNpdpAzy9Css9Jr1wmzyEHbx6I3wFAmKZA0VNmLe%2FBTrKAjVFfanL4ayvoxl0xRPziPlYXGbVRXy59LhKBg6NY2GVWIu%2BV4x5y1oYdbkBv2SVydr592boe%2B9dR8u5js9bMahHBXIfLuey4y5MAzFjFDYfCLr%2B8KehALAbuNESXmBH%2B%2BY8DK54HAzpiHeuPJfyyyXqYo53LT7I4BJObhxnoOLhXlVmvNNY3m%2FM93AFzq85ZLuTRiVGB2UnRo9ird8JEdfI%2Bqifby9Pf9WSsqguWSd8WsymiBkYWJ%2FVePs0lVBHrPXnMPA4qnQwhQKifT8f2l3pdR6LZOqSuORqk29DDQ%2FBIXdEIwwWoFsgzDH0M1yY7n8uCV%2FKh%2BKBlV%2FQcwr9hhYclgWDG6jMyNb%2Bkqly%2F3rJD%2B9C1xjCCLP9o9Sw3y2FtI5VEOaO5c3gMFXAum8suDP6atcSaTo3kehbTgtf3jD7C49sm8BpR1EkENqu9IibiQLproAW9yurAU3h4hOIEW%2B5T5fC9nqo%2FvVOziiOM%2FSKZjThRNTJnHJc8jXIOAGy%2BvbLu78onqsrIQKhVuFB4Zb79mazDbpPe8BjqkAX4Zcw0bULwbxa0RnzhdzB7LKG6eXS6atfgDZ6cSwQlr0hIIF4Mv9JVR8iux2bVDldaeKsAj7yWAjbD7TE5EzzHyYWpuZLl31hCkCISgCRjVlu5ZMCi5uFbULD0O3vgl9BxYAmoz%2FQ%2FbSUIcDawjpIyeSzew6dQyWUtMaH4TW%2Flf25B%2B9ofAvg4LV1%2BrziUQc%2BQgp4IBRbG2Sgb9wFTElq5emtUQ&X-Amz-Signature=efc767acad693567b9f68c1e545e4a86f5b1253c58f5100b4bff3ea853225f58&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMUQPZK4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHtDHGh37Fvwr4ERLbiz9EWO06VT543PutmYfFppmRMeAiEA1q0vJMe%2Fwzu%2FudbB6457I%2BKx3l2eTZpoRNDWHnt%2FPcwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL0qOIp3DSwNM6yBNyrcA51GyoRcGRpoho%2BJj20Pc09rczxjtS5ZX6%2FjjOjT6jEG%2Fe9HKGL6i3MafH0yV4sQuTun0ZJhLqKl%2FWJ%2BU4BBer3%2FGa4igaZhpzOggY2%2BURcfJF3aTS77wK%2FKllrNcyx3%2FmqsAK3kCZ6rVTyU%2B6uMLa7yrWxLWsqiRnCOq0JhRUbYuxoGZOwvoJ7ZVstVWX9C0mAdBwhlVpJ07LX2%2F7s1LUFaYNluF1J9l1E696HNoWBmn7ZAAy%2FZsiMyLCootxkmGms2LPnk6a89sCkss%2FCSYmyHBdvcFFuoFak6YPVtBr5wCWuGUBk3mEqi4WE0Wo6Le6KSQ2qOGRF1lhaN%2BJn84LRL%2BvPxF6AecmIMqiyjeAyGi08WstPF6Wr%2Fx0FoaBAp62TiHF5%2F8s6MFvrryZh7sctYaRslxfrk0v%2BvB4TsT6N77%2BsR9cRPtH%2BRqEDTMhorj7kBPPZVT5qZEhwmnA2EO3DsX5Eu0VQhVVy%2BPMPEzEQAPO03xlaY%2FMI938coF8NF2GcVnA5dYXigJCdFF1B9BK7jxeHcn9VzAYC%2FIvFTXQHJexLv0YSc%2FH4C%2F7oFAD601OeGzYWeqUY97ivBImaxD7lhQjIALXnHUq%2Fwo3PjOaMgDiQmK%2F0mkUaMlXy%2FMKuk97wGOqUBgoHdh4wyKi1u4sjPWNHf3zw12ecdIrhmVvKOwf4KVoSd3x2kaPxejDMMDH7ysa%2BnQf9w2rMdwClEm0S%2B4cPOqVk2r%2BUj0XR8lDrcD8v84PHgvfeWLcKiOh%2FhT7YxW597CT6mgJts%2BIgkQBjaqp%2BblAd%2FogOIF3T%2FerjzyMIYyviSeSmVkCwmZPGafAvP%2BeR%2Fq%2FWOD%2BaQyJLR27rdxXxQOiu%2BYMXB&X-Amz-Signature=031082e97e3c9000df4e86e40f1ad184e4e4b5805b2a9cbebc4d60e043f5130d&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBVT2NRZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGuElLUazE%2BzIrBr1zMZ7ipe%2B%2FJDgN31jjayLCL2DQWVAiEA0XZ6fO6QKw9i%2BX4FbOf6Dxj0T%2BD8o4u5mgWTzBz7594qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFKxAQGdVOnadmp8ircA1ROBjAS1p%2F6nwj1gi6GyOkEdlnYlWLmGgxxrisJ01kguVvBdI8PIk6widkxDfJmhkqepby5GOUoptXGLV1j57XTb3To%2FTCVIvVGtqxdJ%2FteHyHwh3fmYRLBg5yUmX2orpqlaFmj2MFl8MYEXBqjhtkyhMnC1mAIRoOPpvA2PHzLQXoituNwZEz%2BHCLk5DbnCeOHRtbRcD%2Fa2JFguoTGMEKxPFpVYPrZ3e0guNsyugs5KuiDqhrdVM1hvm%2BpJr0fmVD7%2B%2B0MMmF5serAQRyX7958uVDG6wNIwnI5aflC%2BSXrWjqB04ehsX9OVlrZge3UCgflnUzbblhBaY41pow0Udy7RR8ad64YVaMB8oDKW88YszDGYhGPgQzm8MuKcRXGh5JG950zE9UbhVorAvhQ451doiWdV1XaL45TU%2F8U%2FotYmOE2TQPWwZGcVh3wc8gtCaz8fphvUwKroiSKP9vHfu7N%2Fr1OorwzksZ8wOOyQcxb0m6p6CosI6LH0tt%2FjMsA060IbAS5fdAJjVJL01qoRR8LPl1Z9hUQqqKkG%2BpdHw5TYwuwL5%2BVAEjqQ%2BKwa7ZUUj%2BR18oD9qez4fDe3sj4s1AeQkRWsNQD0WMQrAHBjvw99ITeBJbjqZRJE0CqMN2k97wGOqUBmSq2T1964POZe5IG0MPp4I%2Fhy5AHmfgkOLiF2tz2HbwCmYAi0ksm1zloSFW65Yk3fm5bgQtBOv7J1BJqbj3jQ0Qx28LLeKpzJGFvX6%2FMz7L2sYBpAKKRTPcLxvVInaPrxuc8jBjloJy3GN2QAB9sCColm6DOjqMhWD6IpIq2fW%2BvTUm%2F9iReoFbiHaah22x2zQf3VYsPUV0BcivQIGM5rloFhM1a&X-Amz-Signature=f7571d4561457e15facdbc2d57dacace4389e59b586afab5bd8eee2fa3ef00fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673PH5NJB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmY9G7k16k0X1QZm9i%2Fqia%2Fs8gDdj4iOI5tUcgSviPRAiEA7oMUCacO6Viq%2Fu7wulnRTfwUViUheBmFbvcGQLkNq8kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHVC82hFdEuWKv0A2CrcAxpOcNh3qjsAMyy4OlbItc2zmyKyfGtdh46gCcQSUQhHB6rB2lJBTLSkb17XDFGgiPxyqustwsOMXFzZ7nqISArz9kBUJ6JiTfUpmTkNWpDHlLQAvV%2F3r6F%2FfSthipuTl4x0ngMhp4oBKL3ZTR696FO8otpS9bAcjtfLvwKLEuoe10a%2Bi4ySPFYicZ1%2BHpeqiO0TigCpaY29NvZFbwTvwX%2Ff0CQp%2FRKwlBz1T9UlYkylz9B99%2FQ1THlg2EF0vI6PP4ymuSceTvSYr6gRt3Fpg4dXtEsdQd8lWAse4i%2FC1Vlg8fnQOVxIt3muutedL%2BICgEXTLHu4TCkVsPlp3%2FQ3gviByEnaJVV1PlUqUd%2FKD2omG%2BuDUFw4Jkds66CvmkC1jLpk%2BXIlAD%2FBh%2FR%2BOGcKDn%2FK6T5w8kL5oq4efFVTKW64rze4k74Dc9LzneK1zI1rTZKROstMcPfBKlxV6yUck%2FpCfqP0KNpZ5r0EOPaxV5zTqFX2C4PEOJRhNlusNkVTd8VvKf7Hes4O2FltLIAVA1gPkmIHl%2Felt3OdqQ5X7%2FVaM5ZYeyQnq2NcaiFSMyldtU0Nx9bkOEq1u7BN%2F1vFo3eg%2FLk9F6piXKIXF3LrWL9aTv%2FNb9%2FBzdKD0ltuML%2Bk97wGOqUBFtvMHA%2FgAI8m0LhQdDn9Z2jM3nCpoP%2BkrT%2FBCKdn1G4Hghj9TfWmgy5a2hNiWrURS4cVAjomtbEfDeMYGmzZgX3IN%2FWMyb%2F39K7hyjAa4Yd%2BgbSz2HfNfrUVaVMmphFfm4jXz8epWBikw1swe01D%2B5h1US6HAVNksnmmqNtKPWswQAeT1GB40ZYg4BusUDdEMKd5nRKYBhzhED7kKTfKKRavOVM8&X-Amz-Signature=378c53ce2b1e1ffd9eef01613eb859597542702050535ff64f9f5521f656ec97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655ZYW734%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3zkelPF46FYrCvweql%2FnCIOimMPDc1BjMRNubwZSESwIgUg8q6rUnxuK43n1hVmr1a%2B4s%2FqUyz5rDGcN0qhgFC3kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLmo60KYuzpVASWXSrcA4nQukxBVh81U1zQ%2B2efXfmjf5aAt6Plp7R%2BM0e9A%2Fwmrtn0KrYFK2O6TNop6EymmH5%2BZGyjo7JX948sHUEnBfVeHTq%2B1Eh0UfZo3QPcrEd6T90C1WWskL6fR7NLaQjryKYp1XAu%2BYcyP2etefBnkyNzypqhKsQPJAahcpXNcnP9xmgC8i9WsBYOyUzlCpge7buvhaK%2FgB8zOs%2BDJq58iTAUogj3YeLYQLhUaxECVPLbPWKHBvx%2FqeL1Wjx0VJOR9wVC7gCVWrfxu5XwsL1wSzGiVIhANcVm%2FquoBi0g%2F7D0BwGCx47TsE6DLBNvwq%2Br0a8FRuy7%2FnKrOKD8rIMatcBBGgi4FmDicfdT4Y3CbO3tr41%2Fru6OFeTllFCr0WKKIwCGIEjSJKQreYySpIoyBKIBrXXIIDojxGLBQjYvA%2BhGrHInDlzItDxQQRRr%2FnKipJYVudm4jjgEU2yFI4mysjRSvnH9CSrHtKKFCWKr6JZEf6Qx2TqwdXRPLE51wlk3lA7RZrHy6gU5tjf8qW9whgbv4odZzaVOG1WD%2B46el2NX5bCfQ8GGivREFAnmHVjuA7pDdiHwNhwj3g%2BHf9153JRmrF3ZWt%2BZOwsd5emC0dhdPazfgKgP6EdYvVUnMMCk97wGOqUBUCX6uwrPm7eXYE28dBHc%2FO9i4DG3aSrJt9vG7UXaooOKTN2qmNjW2Py1joqHHx9VzBQWW5R%2BNczu1gtUpaS33VG1TeZkFTV3U9elntFRGveW%2FZEGDU6646KT3ozyoZOuprsGiyzmLKaULW1YaRk9p3JT7qC%2FMdUnm%2Fm6%2FnDLHYB%2FUpfBbiUhbsHdC%2FYDuqk4e7T%2FWK2FwuxBg4nuw7SwDwT0QHI2&X-Amz-Signature=e6a94d57b55ad2f54aff7b95b2702fb0b9cb599faf96263c733929591ff17895&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655ZYW734%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3zkelPF46FYrCvweql%2FnCIOimMPDc1BjMRNubwZSESwIgUg8q6rUnxuK43n1hVmr1a%2B4s%2FqUyz5rDGcN0qhgFC3kqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLmo60KYuzpVASWXSrcA4nQukxBVh81U1zQ%2B2efXfmjf5aAt6Plp7R%2BM0e9A%2Fwmrtn0KrYFK2O6TNop6EymmH5%2BZGyjo7JX948sHUEnBfVeHTq%2B1Eh0UfZo3QPcrEd6T90C1WWskL6fR7NLaQjryKYp1XAu%2BYcyP2etefBnkyNzypqhKsQPJAahcpXNcnP9xmgC8i9WsBYOyUzlCpge7buvhaK%2FgB8zOs%2BDJq58iTAUogj3YeLYQLhUaxECVPLbPWKHBvx%2FqeL1Wjx0VJOR9wVC7gCVWrfxu5XwsL1wSzGiVIhANcVm%2FquoBi0g%2F7D0BwGCx47TsE6DLBNvwq%2Br0a8FRuy7%2FnKrOKD8rIMatcBBGgi4FmDicfdT4Y3CbO3tr41%2Fru6OFeTllFCr0WKKIwCGIEjSJKQreYySpIoyBKIBrXXIIDojxGLBQjYvA%2BhGrHInDlzItDxQQRRr%2FnKipJYVudm4jjgEU2yFI4mysjRSvnH9CSrHtKKFCWKr6JZEf6Qx2TqwdXRPLE51wlk3lA7RZrHy6gU5tjf8qW9whgbv4odZzaVOG1WD%2B46el2NX5bCfQ8GGivREFAnmHVjuA7pDdiHwNhwj3g%2BHf9153JRmrF3ZWt%2BZOwsd5emC0dhdPazfgKgP6EdYvVUnMMCk97wGOqUBUCX6uwrPm7eXYE28dBHc%2FO9i4DG3aSrJt9vG7UXaooOKTN2qmNjW2Py1joqHHx9VzBQWW5R%2BNczu1gtUpaS33VG1TeZkFTV3U9elntFRGveW%2FZEGDU6646KT3ozyoZOuprsGiyzmLKaULW1YaRk9p3JT7qC%2FMdUnm%2Fm6%2FnDLHYB%2FUpfBbiUhbsHdC%2FYDuqk4e7T%2FWK2FwuxBg4nuw7SwDwT0QHI2&X-Amz-Signature=79eacd9516db4e4e0a92cb968c7aa511de60ae99a2f911c9f62e10f7fbf3e448&X-Amz-SignedHeaders=host&x-id=GetObject)
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