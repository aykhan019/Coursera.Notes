

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUALWLI3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQx%2BDp3t%2BD6%2Bvd5RI%2B5rZTyUbMyTnxQjh2HeNOI26LaAIhAO9Swj3jzZuaDSF%2FgcCYaAoivKGe5v8v2qUNfE0656bPKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2Kqgcs6Lv6GvnQloq3AP%2FrBAe6%2FFake%2F5GDhp%2FcQrs04bxdL6nG%2B4KwPt48GgqLGOfWDqrSHkLd9D1bObHzcbaDPhfQnwNcgETceJrYHdYxShqJldQy6wSzUiwxpzGX1SB03jZSWn6049FHVvh5sNOgZcPpiee962k%2FLYhgIeIs9sa1FhMs1LUF%2Fp7hXGeg2ac%2BB2a%2Bb5%2BrpaoR7%2FSGpmtMNHWpC58l2hrWlJeCmHfAEOSAyGzwBYYCOepXyUfoomMsWWMd2%2FTs67lMo1rwGM%2FoWdLEDcV4dbFIi2qUhm9wHi%2Fnerv5%2BrzWZJsdD8XSo5qJ87Klz7uh%2FOnFvLax7XM9OPE323qn%2BUSX4a66FwzPB2hWFtgNLOA1QnFDKh5k0Ro5VI1K%2FpS%2FvC3Zfbhd87zoGRqUlEAf0ZUPu2biv1pAjD5pQ3PHxYB3m9ZgEhZ%2Fz8FRgNbV0m3F5TZf2qlz6xUfkE%2BWTONeX7HH7Z5s%2FJ6uXIwb95fbStA%2Bpu90tAubOMleAldIQ52ZlpsNd%2FCgSHhqT%2FhfZMiZph%2B4TuCoPJQwXpGaBmGcRabTa55JGagss%2B0F9DGEqzwR3qL%2BhmHXj3N5XbrFZwupJCgYkhDb9k%2BSOY6j1%2BOcFfDNPglS1jm7c%2BPXgb2Ex5ZokfhTDmpPe8BjqkAcZX25x865ovt3Uhq8HeZzqBMWCoOMX4zEUWW4Qv9iiIBhPdagUyQqNLoySGAlmrPDht6RfdUYYsx3jJM%2F7u7bXxim8RipJNLjGL%2BW7VpgPbR8m2wRCIbk5nkdq2Ua8YeqBOjUnulYr9lLtA4XAlxdh0OdKlb2KGkbmmJf8jRoLD4FnL7O22Crxgnmw0npa1lbHl20Rxdg%2F3kbdej5bso6pr7rX%2F&X-Amz-Signature=cf39569d44579758a404aceb1ae9a9fcbda2026e3d0b6693ba035efdd5e98a9b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6DJRZA7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpCqclBnEHpsGN19GjtN7oiUd8XxOpBpJvvX5QWDNRWwIhAMeueIE84yn9ptFaf37KzHzdEp9TQskTVR3Q7NGTzBNjKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZ%2FPeYbogCWz8Wg0cq3AO%2FGKF9zZfD%2FGwDA%2FMAR%2FWvcoF41gUoYQKy9izFw1vdUHlF%2BmyClYCANALtGqH%2BuMWMYy5SxqnBXqVzQnWvQoGmzaU1PtTveCHXcI3zs8Dd%2Fc46bjkYCkLZfGwgTPOj7uBT4u06eMWD2yJyhrdMpH5VOApHWG1SpGHbRk2zRpjUEVZXKyRc6uW%2BsMPmliqEqRMHFa%2BHEatvlxH%2FS9%2FKdPlmowAZ1ylSAVZD54BOqet%2BthvHL2sSl0pYm2Ig8RQhaVbUDJa4Af%2FojBVbTfF33aQk1Kn9HVEMcijFLbECLdOt6hy%2FNloqExrX42ep9Cqp60%2FFwMy8KqTGF%2Fjx%2FMYj3VJOvTBq1besEqN7dgrc%2F%2F7%2B4mNdSrFz1pm9u0qYWfvjz51aIY2rW%2FhcSJMiGte83nG1WBcIFKAXgKJFS0979gRAGtjwCHS9Hi7sFY%2F%2BKYtqHtKnDhjsGhGhcVpvykVepMnWmbkxh5ep3chfwuvjJpAsgvEb2Kj%2BcL1OHYlATSrpuxXZ2%2Bh7Dt0vVzj0VI0ZiHvHXAiOrksbXRVewQtlTVcAz6nlKZEvgf4bi2GSp%2FsfXzC413WkbjEIdAZKCkpjiXK7B%2Fmgyov7wEH%2BojDMhS7V%2BK%2BHk4IHvf889loNgDCOzPe8BjqkASK%2BITMsAXSm3CykI%2FPAadA%2BoPSA4GeChSsA7Qd8IBae5ZBcWrO%2F9xwTukT45uFVQNPN4y%2BYjeuSdQIfAKLiPEdzOq9n3xRfCbhC2bNCD9PERZBf6OX1tXLfOAJzC4bIRJFxAVf7m5iobOxoGQKmDkWZiTz%2Bc%2F1iWlCaS8ctn0igim9mZgCltVUkXWWPZDWLPOvOC1TTJEadMFdNZ5SmQasQwmHf&X-Amz-Signature=7f036e7815bfe4247de01a7763c279b046784453377606be050becb3fb780ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJHVIOSF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAs77YdA886bYS90i4gc1gW1pzilwsZ00qXmkJlTa3NkAiB5TAIltp71G48o74oAJj2dgQ120s5K3FnyI8jEHCOajCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1vsQYkBH0DsNycbMKtwDvJmiR9%2FfME141XEtL7X1NstNbJBKB1rHgrhpDIqIKRgdDWrXEpxI1SxSzvF7xU%2BQdCQVsDP4jqSVUsSvof4oJw9nxTMo0kpk7u2Fajp2YnaArkLh4iQmIven1pRZPlRMk0OqiDUixE7wukeMHmdzQ3xY1nuqZscIGSnTN3JxMUxGGlVoIZYsPvR1a8wnfogQnGczVvtbHPgSyFWN1bBNulZfHlqQZ3sYvcG8ir5IhUUtBY7R4ajgDmR45OuS0qbS9erL2U1HoegsXPajCFiUCZBOTU7QWtTiRix0Rs6jbmYLESFnWbm2XMSO3halytUOdlvGQXddq%2FItMuPdTWynATOhICKjwnaFH4biyQefPz%2B%2BuU9hiQ6mDyaBVw1xreHGJ98an2OwbG%2FKuX1IYEU0o%2FeNAR3bHrvxT1NM3OoGhKGq%2BS5pkoB3stGHkXxYUgviKC0L2ColPuIdWIuPeHKh%2BK%2B0akolmNCZBhuyLOsa2Sc1nK55UU36J7eimI85ivDs4YB3iDVKVPsQja9pgMu1XCUjCwVvCDHcj6USP6iZhESC8knfcBuaJwsjpRqBZhqpcwqxBDpmisbDGYJf9RWA9UAYRG0suY7UYOErDTurDKl83MYm4JyJm0AhLgMw3aT3vAY6pgHEJrVWpX87J6UbYnFkPdUQ%2BlE7GL46132%2FRvDQLb%2BD6PTxaCLRv7k7Mp7qy5vwr87hT9zuQ%2FFhYM%2BkBwSyFcLsi3ev4GZEzu0z5w8Oz7f5Q30vek2LBjrQqSPcLVBHGCtjTPEa%2BcF49sDXqhRCeo1Kx98SlypSrwqHw57zyekUInggoiKoSY%2BjX6j21RkYivCXKoAitWb1%2FS3AsmqgQNWtPcyCLfHk&X-Amz-Signature=c6d7328f8d410b019d2588955953db6cb474816ee12ec6eca0cb7df49d92baf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2WCLKCA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCGU0XW3N9c9%2FbArnzeO95ZY66tXUJlK7gDJZD8O8cEMgIgMmGOJFrywdyIAVdz7lzoDMwCxIZZvYKZ3PMnlmfgSzsqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJNLjh%2B2hv81bBOGGSrcA1tfjVVQFpF8fFtkqBbpSQR9xOTIX%2FcPUXAj9aSObuJHe01pr3TxOKV5%2BgcKUd5wyOIbbyYmHePHM0oVzgG%2BrlQ4nRA6kdA5LX7DK6vNCmdQ8%2B31Qt2vwbfXscEJCtKFY5n%2FCB39QB%2FXQ9FAk%2FHVIPqPK6sDidZBM0BiKFVx843dNx49IZR9xrwK8BSDrVSX%2F%2FAx0GcZQ1aOhNuY%2F%2Bd95SI4o51cUPxNmX5fwXp1V3BBnXtBhzEHfrh3ASX3vrjx9H%2BL0ESpzX5gxFFj7R%2FyBio17vV9AgUBLNQNHdA7rFDeOd%2Bx%2BEi%2F3J1dEtJvUG%2F7hK6fYZsY5mCtd18usvjpzF8y8%2FNiCZzYtNrmITR37vtV05j%2F0IDVrJq01aBJj9om2Q1bJaeQX0fMyGHOMZzq2p8I4aM3jpq45uRsAMd0V8GR4AwoFaseGY5H%2FeKez6clBMMHujD0pOb2VXA7vvv9DHpRnxLlRLQeM%2F6KjaFw2t7h4bL9Z3OB%2BOu1pGr40a3Z64YcC0r7VqpYB0S%2BtE%2BdqWyvbe%2Fg%2BpTelGIDkoJsVNJbzO24j6%2Fi%2F4gP1FtsuFB46Ymto9onfL3%2FV904q63m6%2Fax%2F54ieikOyJWrCEBOy%2BsPGoRSWvND%2BeJByWihMN2k97wGOqUBSAwo2ktaUCUg%2FzO04u9ZK73N0rJCEbaMNo4qvcr%2BSwa7Xy1YDfG9OCEQc0Sswnm4lCIEju1eufl9lYlFtQLgPGz3vdw%2Fd5IhfPpoALHnMi0Kaxb85un8oBOcLW%2Fu1t1Lm1%2FG17A5YJRYM%2BRQSiU5hI8kxExL1gMZ9fmpgT%2BcZwPcx8IIGUeRelXEpGXhrd3orqSaDVMYIQbfJo%2FIoNJa8rIp0fZ6&X-Amz-Signature=9f6e658110451f9fe6670d57c77548f1c4e67e62952dab27259e9a7b60c4d70b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6DJRZA7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpCqclBnEHpsGN19GjtN7oiUd8XxOpBpJvvX5QWDNRWwIhAMeueIE84yn9ptFaf37KzHzdEp9TQskTVR3Q7NGTzBNjKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZ%2FPeYbogCWz8Wg0cq3AO%2FGKF9zZfD%2FGwDA%2FMAR%2FWvcoF41gUoYQKy9izFw1vdUHlF%2BmyClYCANALtGqH%2BuMWMYy5SxqnBXqVzQnWvQoGmzaU1PtTveCHXcI3zs8Dd%2Fc46bjkYCkLZfGwgTPOj7uBT4u06eMWD2yJyhrdMpH5VOApHWG1SpGHbRk2zRpjUEVZXKyRc6uW%2BsMPmliqEqRMHFa%2BHEatvlxH%2FS9%2FKdPlmowAZ1ylSAVZD54BOqet%2BthvHL2sSl0pYm2Ig8RQhaVbUDJa4Af%2FojBVbTfF33aQk1Kn9HVEMcijFLbECLdOt6hy%2FNloqExrX42ep9Cqp60%2FFwMy8KqTGF%2Fjx%2FMYj3VJOvTBq1besEqN7dgrc%2F%2F7%2B4mNdSrFz1pm9u0qYWfvjz51aIY2rW%2FhcSJMiGte83nG1WBcIFKAXgKJFS0979gRAGtjwCHS9Hi7sFY%2F%2BKYtqHtKnDhjsGhGhcVpvykVepMnWmbkxh5ep3chfwuvjJpAsgvEb2Kj%2BcL1OHYlATSrpuxXZ2%2Bh7Dt0vVzj0VI0ZiHvHXAiOrksbXRVewQtlTVcAz6nlKZEvgf4bi2GSp%2FsfXzC413WkbjEIdAZKCkpjiXK7B%2Fmgyov7wEH%2BojDMhS7V%2BK%2BHk4IHvf889loNgDCOzPe8BjqkASK%2BITMsAXSm3CykI%2FPAadA%2BoPSA4GeChSsA7Qd8IBae5ZBcWrO%2F9xwTukT45uFVQNPN4y%2BYjeuSdQIfAKLiPEdzOq9n3xRfCbhC2bNCD9PERZBf6OX1tXLfOAJzC4bIRJFxAVf7m5iobOxoGQKmDkWZiTz%2Bc%2F1iWlCaS8ctn0igim9mZgCltVUkXWWPZDWLPOvOC1TTJEadMFdNZ5SmQasQwmHf&X-Amz-Signature=083e58e27d81f3192a5f9a39d55ad1ed7bde4b35f86e610b376fb89bf838e191&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466766ZRLOD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJ8y2c097toPzH4Sp%2F%2B8rw0bcBCjrBMDyH92zV5mkfBAiEA07GJ7F%2Bp1JRcdkw7S%2BJTBg6xf1CCT22yZb1ygnaCGFwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK61BtlsNq6k5MtnTCrcA49h9mQkU1wcf0o217uhw8FU6wBU1DqLki6dgQ%2F6CBqjnZ7sFzOiHl8U4xf4YdI9FfmqmMPl5%2BSu%2FdEgfsyLFmBszqhuPyqbewK2PGRwz3x%2BSUzp7jAJrluhEhAoi3hHju4TJXVX%2FQ9LYKLl9Sv%2BcChSYID5ZXMIa3A3DH0lx9M6NrlrL9Tc18nkXO9Wgjdcq5nz%2B7zryEBbEGI9beWjd7H9ENb41FFk%2FdCv5KQv1CL4l4CNjqwSmmzDi7mYqYpFFCF%2FNblTkmnddSAfuOp1gVPH1X%2FTGGLjQSi2RFHIQzEYhq6rw7d6Gbsvl96WABnUiFcfZ3c0He17JRyB6xJbCuMrWjkah79v%2FFlJe%2Buojyv3nkoQ1Ee0h2GLMf4FWDB11zb1hUXvAp%2Bzj69R5sUSd4JqLiIMR9bsYHsbG%2FBwe1HnG3ZaG96NUQeFxKOIhqaauzNYkXSjJ9vN7iMqAoViT%2FbOjjHm%2FV%2BiMVNmR3yKwn5kjRnuvIB4B8QbQoOY6P0UURdzCUTHCqXrPvSTMsJ2lY2qbKcOmE52ziBCUvlnAAiEaf4llvGpZ%2BaSx%2FSqrG%2B3Zc29rvIqluOvJX5gB0QzH3LXOTol9dwL1ZFg925kAz0efceG78nrI6tRwScHMOak97wGOqUBhR7fpYt6dAVXvgkxCQiI6aziWR2Fd%2B6LWDK5hsBSVI1DhRHlIsK9vtw7FfL7uARfR5LUdpmELNOUEV7vmmFEeqMBRLtbm3K%2BfFdxO8rhvXGtYTnwl5rr5%2FYSsvpAUYyVDdXK9EehCh%2BLEClKuCBzHsSkG8wcG6DAMpscA8pByP9TyZP2ARdJTisWYIhLqJKZCCXSui46W9X3Wf0BkugkvhyGMNXY&X-Amz-Signature=31fdd48e24533a5a4f537324aa4f9c359b7d958b384d60e12cc85f490a2641b4&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEHFTKBE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3o0eITc%2BDVj9C0aMN26zVuBL27PdMefEExi%2FpQvoElAIhAO4jREbibKIGQ2LMPopPeUJtmaBrFtoD8%2BHdHdejBomhKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igymc8Br%2B5ZlqJnKwWoq3AMcsZUCB8p8p37nYCqVvVjamZYhz8Zez85XSCRi0NFow7wTH7k5wcLrC3vtpG6EcXU%2BtF%2FWlkp%2F%2BPV70e8ciTsFTFx8hi6B8DCRbIBst%2Bfd2wrWxqElLbwO1jxfIu4qhQkFSaVoY%2FQfkdP5kTZtiXb7quVQRavmm12tYjHIrip1u9i550ghyOuN6muhIQcZ7ONovMJiic1VAuqcwwKVlVcT5sBmc%2BKMb4zwepCYDCntuAjxPDClfLZvVMOwz4GAl2FT217PZdy3EPVhpA4Dsm9Hty2wfKablq%2B6dV%2BiyDxBe8qFyNZxr2sVOFZAfY9ALUVnmgTxijQG84%2B8XiXSboFTk1meyaaiFjoeCsFe3I6WhLE0Rph%2B1ikRrFJR6tnAPf42JwiDFbCGn3zfmglvXgFbk%2BUJaFM%2FEroaoz0aWVdttilqNBWFR7QLlJGpP2XovycRBc3K%2BU4BC49bJMLLE0bJsIBcx0Hf0GS8vvGqhkT3IL8l%2FQYcNrFU9rHNx1oYsfpnoEITVaGmG4QDWPa58WuvthL38jUkkfdZq9gbzgXXOvKekXJK4SfI8a3R8%2BvVJCWicYqJFiv6fMujTM8a6Ub7F%2FA2ABl%2BkNvqFsmIQGGXeKhXLDEE9kv5fWD%2FWTC8pPe8BjqkAT9YZ8C1T4aJAuzRHA7h2bQeh1D3aUu%2BzmMuyVKAkp%2BESUA%2B5Ia0GuWPPloTSnIrpjhvgRQoiC5goSko62zDeiZ1XPW8faGQKeNZ38dPDl2mbi4C8%2FgPaytIxbSZn6a1uWM91nh7D403zkpdvFCQEPy3mvvM3UcvznlMcvbzQUDE2d7ULg1gu2pfV%2BMIljgPtJpVw%2Fv3O3UT1Y%2ByfjSXg63oxoLP&X-Amz-Signature=af1426587375d3c99b934c7295ae8a69e614a44488c98b95832b552d98e0876a&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVZPGXOV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTmBy0KXEr%2B2LeoKJm3cYC9DrfMUtlZ46Ar0d%2F8weKIQIgAk4HcNM6uprvk%2BHEkfEPwT5158e4n954ki05BQ3n02gqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIdOGHk1BgbbWMHk0CrcA4TJLITZvLH6KaO1bhVPb%2FVtBoyxW%2FxtFv8wR%2Ffh2UOhSIajc4LNMIh%2B0Rgc4sk8%2F2kw44F0jumRkKsFq%2BnZqHuYgcEgDmTe61RqWFm34oBiF7iRzo4YrP1D%2Fe3p3KZmOUVL7fHh4%2BRMih6G0fY0Csxl03Bzw4R8ScDqYTAFuWyoUWfBm%2FANv2ojxcVMqEn3iokgbJRvtvOvjuTR4bzpckg1rDND4Jl7vhn2f0THMmk5VtK0ps51PQLq9NFNLTZ8L9xS4%2F3mHFCm5isujl6FGAVf7Usoio%2BXZT9TfN%2FNXgXnyo9HgziJffUWXwX5FKGOCGGcHp2p1ChYUxSLzppuRdokwRUb4Dklx1H7jvjcEyeHVA2xN7DcFUXDON4QlU0BJcAhvHaWkFhl0IaXUwge3T9mexIUtq2Ue%2BcqyCW8BD0HSZJAbyui3h%2BIEk%2FK2z4ToUQvBPert%2Fvro%2BCff7zm3Abw3irToGpNFotLJAiejDmKxU5%2Bfi1BKr6AqXEeV4qyGBcI2zSUUDW3qI%2FS6xEpfaZOXDaq7qgKN1k1z1nUzT9BNgyfSnkeYtaweHU2245l5F4p2oebpkYur57f6qJYIrSydINTY6R5DXKylE2fgHnmLF%2B3RW2fbgADzA9SMOak97wGOqUBZupU2ifNf3rCfKCBx5ZXj7u8RjauB74J%2F8sWvW5i7jkhysQNwwQewZ8n5Sh7eGwyQFCGi15WQ6QfUlhJ6XhlJG2HBqpq5Xc0Q7jSW7Tu%2BGb5GRYYNu482ehKKpDewqodOH%2Fml%2FFzF%2Bur2Yuf%2BLEUfn9gNedUrZU1rL180%2FJvgW3X2KNFagAhWhko%2FH3DVTcxoVC8%2F4hzjRZn6lAVj4EbjZfzaAUH&X-Amz-Signature=767ff916f56807010fd679d7956cf36bc29f72ea601fdb7f8486a5292451a930&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6DJRZA7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpCqclBnEHpsGN19GjtN7oiUd8XxOpBpJvvX5QWDNRWwIhAMeueIE84yn9ptFaf37KzHzdEp9TQskTVR3Q7NGTzBNjKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZ%2FPeYbogCWz8Wg0cq3AO%2FGKF9zZfD%2FGwDA%2FMAR%2FWvcoF41gUoYQKy9izFw1vdUHlF%2BmyClYCANALtGqH%2BuMWMYy5SxqnBXqVzQnWvQoGmzaU1PtTveCHXcI3zs8Dd%2Fc46bjkYCkLZfGwgTPOj7uBT4u06eMWD2yJyhrdMpH5VOApHWG1SpGHbRk2zRpjUEVZXKyRc6uW%2BsMPmliqEqRMHFa%2BHEatvlxH%2FS9%2FKdPlmowAZ1ylSAVZD54BOqet%2BthvHL2sSl0pYm2Ig8RQhaVbUDJa4Af%2FojBVbTfF33aQk1Kn9HVEMcijFLbECLdOt6hy%2FNloqExrX42ep9Cqp60%2FFwMy8KqTGF%2Fjx%2FMYj3VJOvTBq1besEqN7dgrc%2F%2F7%2B4mNdSrFz1pm9u0qYWfvjz51aIY2rW%2FhcSJMiGte83nG1WBcIFKAXgKJFS0979gRAGtjwCHS9Hi7sFY%2F%2BKYtqHtKnDhjsGhGhcVpvykVepMnWmbkxh5ep3chfwuvjJpAsgvEb2Kj%2BcL1OHYlATSrpuxXZ2%2Bh7Dt0vVzj0VI0ZiHvHXAiOrksbXRVewQtlTVcAz6nlKZEvgf4bi2GSp%2FsfXzC413WkbjEIdAZKCkpjiXK7B%2Fmgyov7wEH%2BojDMhS7V%2BK%2BHk4IHvf889loNgDCOzPe8BjqkASK%2BITMsAXSm3CykI%2FPAadA%2BoPSA4GeChSsA7Qd8IBae5ZBcWrO%2F9xwTukT45uFVQNPN4y%2BYjeuSdQIfAKLiPEdzOq9n3xRfCbhC2bNCD9PERZBf6OX1tXLfOAJzC4bIRJFxAVf7m5iobOxoGQKmDkWZiTz%2Bc%2F1iWlCaS8ctn0igim9mZgCltVUkXWWPZDWLPOvOC1TTJEadMFdNZ5SmQasQwmHf&X-Amz-Signature=9b7dc4b8fbcb5079a81ad9a727789ed3186b842739877c6496b7f9d345469bf6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GOJ3234%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDOn4ie8TXkPXJdtP96jG1nJMHnRBahElhjSjSFBOTAYAiEArHtI2eTW8EJJP0xmjr7Xk%2B%2Bi24ifUnfN21cV3AZxNlEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVE8SWBLHNyiwpXaircA%2FRWPxh9Rzn88sLmaNhVhLT1Ps0iEK24wY0maiGud2TEn1l%2BQoXeezYHwFTa2dw64E0EhAZdXkfk6lkC0G0uRUXwqQ7NsSM%2Fu1Bqp6cJejEkE3a8mEwhg%2BiDmQJ9R610ugZH2Nr0cZyatqwnf8hIFY%2F%2B3iQsqe6uK67QYQABQv53OruYGAGInTPx26EIohkkDNSKlo0LdrCrEfW6QYXL4%2BLeD9oT3W%2B%2BSLdFkMyJW4W%2FWIDU%2FIbszGmmtJIYWrDwliPMC7MTR1nwL2s5VS0plu2yVIi6GqVeRHBHRvWt7BotA2CkGzZYxtxjbSRU4QEgmxpLCtWC3cJp6OoXwj2tcBhNhxS02ANNJnraTFqEgGNSr%2Bpk8OkknLClMeHdrWXRodV2JGE8Qc5NYQIMjnAkcxz1eqfBkP%2BljspTlZMD6dGjwYqJTITq%2FCpm8UmiiogAYpqSXBewD1TbDoV4ReN0VpZEY6Cnrq6rF2iX3eVLhemTG4TV%2BO4PzbP%2FiFjmt0u4oW%2B26niBFF72ZYRD9FpV3hyHuMjsD%2FgMOUYLy2s5auzbJHa92K1wyffoDXZhj6tE3gtb7P2T5k25U2sFLMljOjZsWfHJ9axaALjk72HR1b5tniYcYCpXjJqw5w6tMOWk97wGOqUBtuuKu%2BL33y77sGpDVQ4%2BHA5nd70N98aQ3G5nHP2uHoTq51ZUJT%2FLyHahPQZvf48cLKUwmIkPhXOMRoRw1OJ9cvUSHlHquE1Uw6mRFAjIk8DFFmvGX%2BnId1HoHqo5LXUJ5AbKxXKs%2FD3r7U77XRYnLjiU9afJsvN7LIO0FL24s308jTkuvOjMS6GjIJ93dHwrKOhNDGmET9w88v%2FYJQGTeGiwCfeT&X-Amz-Signature=9a1c2feb6781b3219f943373da32e6bced83017b06e6dd2f9efd1eb5a20b84fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GOJ3234%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDOn4ie8TXkPXJdtP96jG1nJMHnRBahElhjSjSFBOTAYAiEArHtI2eTW8EJJP0xmjr7Xk%2B%2Bi24ifUnfN21cV3AZxNlEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVE8SWBLHNyiwpXaircA%2FRWPxh9Rzn88sLmaNhVhLT1Ps0iEK24wY0maiGud2TEn1l%2BQoXeezYHwFTa2dw64E0EhAZdXkfk6lkC0G0uRUXwqQ7NsSM%2Fu1Bqp6cJejEkE3a8mEwhg%2BiDmQJ9R610ugZH2Nr0cZyatqwnf8hIFY%2F%2B3iQsqe6uK67QYQABQv53OruYGAGInTPx26EIohkkDNSKlo0LdrCrEfW6QYXL4%2BLeD9oT3W%2B%2BSLdFkMyJW4W%2FWIDU%2FIbszGmmtJIYWrDwliPMC7MTR1nwL2s5VS0plu2yVIi6GqVeRHBHRvWt7BotA2CkGzZYxtxjbSRU4QEgmxpLCtWC3cJp6OoXwj2tcBhNhxS02ANNJnraTFqEgGNSr%2Bpk8OkknLClMeHdrWXRodV2JGE8Qc5NYQIMjnAkcxz1eqfBkP%2BljspTlZMD6dGjwYqJTITq%2FCpm8UmiiogAYpqSXBewD1TbDoV4ReN0VpZEY6Cnrq6rF2iX3eVLhemTG4TV%2BO4PzbP%2FiFjmt0u4oW%2B26niBFF72ZYRD9FpV3hyHuMjsD%2FgMOUYLy2s5auzbJHa92K1wyffoDXZhj6tE3gtb7P2T5k25U2sFLMljOjZsWfHJ9axaALjk72HR1b5tniYcYCpXjJqw5w6tMOWk97wGOqUBtuuKu%2BL33y77sGpDVQ4%2BHA5nd70N98aQ3G5nHP2uHoTq51ZUJT%2FLyHahPQZvf48cLKUwmIkPhXOMRoRw1OJ9cvUSHlHquE1Uw6mRFAjIk8DFFmvGX%2BnId1HoHqo5LXUJ5AbKxXKs%2FD3r7U77XRYnLjiU9afJsvN7LIO0FL24s308jTkuvOjMS6GjIJ93dHwrKOhNDGmET9w88v%2FYJQGTeGiwCfeT&X-Amz-Signature=00a4136dc9620ba763329c3333adad3ee49611dc3fa859250af8096b643ce12d&X-Amz-SignedHeaders=host&x-id=GetObject)
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