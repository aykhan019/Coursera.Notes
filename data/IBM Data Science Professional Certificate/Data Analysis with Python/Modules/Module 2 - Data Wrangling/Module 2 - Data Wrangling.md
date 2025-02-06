

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K6HRSBK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFXbYBWW8BPC13xxmtdBE51pK5qWGWpyqAQCcwBG69NmAiBSo7eJTIEHoc02g7BrLELP%2BWLLHBIKTIZCE5HkImHq3ir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM%2BjDu7KQZGke6ltZFKtwD8KSeCV1AMS5%2FjujcV8fXR0I0IAbblTdELep6qZfrxl7iXG797FRyi2dWS7ZidC12XkVxb4if3LP0486wyv2LX7KJs2UWQ03WogPVSuCYESrWPAjgg54NU2xWKzvBFcXswGl%2FE4HRMUuW18ePaxwCghbzVvyRH2EOG5GZjl7W4Dtr%2B3eEvbvbtGJzilYdRM8qCPoWGA%2FzwftWbJDkosouXMse0u6hNtDzeDqpichqBsAMwqlND9fZy150TUJ%2BcFqJ08bQLw2IUAgDVfBzPVvHTJeKSMtfbmbcJKnKsQxxEx9RddyCQd%2BvGxkeRfzbP6%2Byb%2FOUd%2FyExbud92R9%2BAiiSS7BBxSrKSdu7C7jeaviNC2pVQWEUd%2FRTmMXbFLDr%2BPPd6Cy2DTzBY%2FCBP%2B1asLQvMVTqaAq3d9vFUPabbkri35pGakPJ22GFlo0F%2BB2nH49yFUXC9abs7rrwVfcDGIQTae1anRaVdzIkrAPZQo9RjJbFS6YgtTgdASxU74HfhUZGA5GzeF2sH%2F%2FWYKPkIDKNd9wWfMqP4QdxCUW6DrUUSucMNXQSHlTqdkl4lV7wt5s6v0pmFtOgQd7oCNM1AZzuVsIngbwRiaH0I8eHrHlIui%2B2%2BXY5kCTm6xvwTow3OuRvQY6pgEvbZ3vTCy%2Ffso2VdnZNTJAhTrXnGV4ZfWv7%2FkzUlz2ohgxrk%2BsEv4PZK50n1DZu3Dg9NBgUVKJMZH8lo3Ew13ajDiO3Bmi%2FAPB%2BLzYMew%2Bp8DLemZBeaObDB3hwpsWemYSVdMrAT87qwaqgAIwQPRHWNVi3O9eo%2B35i6f%2F6fmtECNQNV2oCQIYvvu4VOPcHR9CUYOfTRys9sSMs6I6rtDxN5mbr1X6&X-Amz-Signature=6a7aae3e4281ff79ebce474f7fd058775f53cb7f4f0cf84dcbe924650e2df264&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCRGGNYQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQD5zPpf1Ya7Flx2j%2BUDfEQp0sPFZR%2BoSHS8Qv%2BXu%2Fpi5wIgKFSRXzOpekMQCI2%2BuWtV5Kj9XYluHnuhF%2BN3gO7PSb8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJIwVGI4rItY6sVe7ircA1KlOJznb9L2zp9WyRVXQO%2FQNlaQgIJqk%2FQ9SRZsdESnD03JwvlE5ErVSdUp%2FewXc1Z0wBLsfC%2BCLTMixW0Hi7ABYu0ZpI5%2FgT9%2FxUpiqmhy7P2lPWWAIDesnbvPbSiuMMIbM4F%2BE2%2BwCGxLl44zF3czUxLk4TzE9nA9wSMR8bMH%2FnKoQuos6XziMcJMpt3K%2FqijIfG6tNXlJw%2B12YA2E%2Fz7IPZciDp3GaJ%2BCJHgSmFgz3%2BRyUsz9izaD%2FZlURLhXiI6kfKdo6iNxMi3LCWIBuba%2By2RMnH4mjAEEtOL1NaN1pFvxWz2bcbhQ8vPRLAwlH9%2FDH4ZB6sjVrZq4zOej4zMeGX9ZbQS0Wg7fRmdB23KAjERQATWOSA6eFQNBwSjJ%2FkG3RE7TX%2FFIEoWhok2WPfxDqoHJH9vKwIsZFkrRzbc4vwotWX1%2B0GDQJ%2BcPf9hQBnFA0oQzkl04H4GmOSeBpnSOO7vXBCCImojy31y2idplUInIRxjD4Tls%2BEQovAMRZGr%2FkXPk18BT43ktNGw1ZHDCjTizvdchMP5CSsT7pCb%2FhEkrfIhaAymxEeionXQn8xiCcAcr%2BF87w1yOl0suzt0buRYHGZ2oKHlz64CS%2BNQWFd3Zla15NO62YnxMNnskb0GOqUBrupxRDlIX8KCuvkeIbppIEFmh%2FrW34E2HmIadpZ5tB5QQDno1W3oKRcye0hJA0acO5umVakw6zziz%2B4bSaKiYjzn%2FBRMm%2BmEBbuSo2MJ%2FcojN10d3%2FkQCqnF2RD5T3oHYZ%2Be7zSTqWVgkalBYtktMFGf5%2BmTQ8Q1JIF2gmEv%2B3awmz7lRd1eUXlf7if%2BJBVaiwROrU02NIPZKbfl40aBJ%2FVOmzLH&X-Amz-Signature=6ec5e65fa4b6596d56802bdb8504ffd594a1381f6a5de850d22eaa99d499a684&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LK6QNDL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIEvvNxMTWYooV40fQpL4CHyfaoNbDh0dxyhpp%2Fo87zyHAiA3k5mMUQ0CDrY%2Bh9sAC5hHIoATQ4yj470GRYTElcDbsyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMH9tHM2KXiB%2FuTbKrKtwDRknRPe1nkWA%2BKyiPNFf%2F1aN7Bn9T%2F8gkyRvQcR52rDRtoswLvYKveWWytHYpAC2FlrEqrzIDjCqwU3UX5rm330O0zpGRi2LRLx997uDZNBpjOwefv5VJ6hpMgT7MGm8lNIAlLp4MV4ySUjK68dbSq8%2FrqC3eaOzgZ8W%2FxwycY7FuCxv2jrRDsdZ2giXGbn6Xr3wxqt9bQAExhCFEHwvCX%2F9WMJNYAEoYIB0U1dTvZz5DXUkglIaTquqxIs1Gaho%2BBaSNxPi2fsLC1wPyWG90iEZtqQeyx6SLm4MRmMtrWGCDrNN%2BVRfv6ciZy%2F0aWyqDjAhqFW4Hj6wCY%2Ft8F9dlUryDrwJEXtFl3FVSjMNGCQTlkJ0S8jobwulmGn7KpoJKMRwn%2Bc356n6xF5bGYcDZSpbIqGKEQISSZd%2BK3MXHoB4buBOlpFI%2BECvJsTPyeg84yk%2FnK4Om0aLdsr7b3tUct2ruTk%2Bt30rn%2FFBD%2FiamjsrQhdDp0E46jmQN%2F7aBdUOnMMBJKcKb2fSTgSFg06ju%2BJZ%2FkqyykdtFFHRrfRUz9e%2FWa6w1Lsg%2FPWh8LtHBVNPOjiEFm6r0JyI0s9AOgVosyGiO%2FT09p1z4C%2FYcKP%2Bzxb%2BKNxPntnaULAKTNdkwkOyRvQY6pgGywk7UxHGk%2FWla23qb%2Bp8gFhhB0taavSMjan44ichYQq934sPKbKqQ7XBSU%2FJWBrE0ZzPz5W2H408TY6v1zo5gcWY3lYwlD4DzklC%2FXKntkSDkg8pmxbMdYZJIL0lJ2ZrtkAsPPUExiy0pijeJS4mWsSeiS6qOBsT5URNny2xHv1ZeW9ZjxCUkTYahpWLHW890wXYVDp1K%2FC%2FYISebYVTNBYfY%2BhmN&X-Amz-Signature=67a1da1aa436876e8f7b37e26a838be83da909c79eeb4ae30827039ebe458e8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EAYCRHH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDY4362wxrkw4JKvv5m9LxBhXQyb8hH3GFVYTrRxe8yJgIgVdojPrOngeMDV4ZobehMhwosRhhurRNWphGIsIUwlIgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDF1IbMyQVQuRP8PrVircA%2Fy9UxBnXPNi4mo27aZk7zfUGd8ywGgSOP6u0rvaAluLAfzJ9iaF%2Fh7MB88RV8VozQjD1jfTIFRC%2B8psCgUFCq287Ak5oY%2F9DpLjXYMLuPSJ7%2Bd0vj01xYZXJcNwiAk0PXtW0OpfsHPrf91NFimx9r6zW0GfscVrFIHcDgo6jUErL3yklpZMqtLEWDG18MTTpc2z6n1z0Ko6D64QcXsPnG3phcbTJQQCsA3LdUOFM0PEPSAvF4YHoQoxQIfbdNwWUZppvLlBXqTrXnuPFZFaGOfeuT8a%2FXkpqw0lWXcXeWkyMwBSnStosWrGsjlu6xZeruJpfxJ%2F5tnIvzVBofcW0J78o0TmD6DlQX3shlSQYMczUaLq3frcizPHJyWAVO8DUrnEmaJzImT5HuFVerjEY4riL8caLl170atFkWnD6RTma2yh5l6gqQzygf44b%2FowzWJ1oo6VAAaV6uPnUo%2FLFeN0BLp2oXebCl1eIw6b0sEr5%2B%2FyVGHJ8J7MhIuED4pQ06wYYmchQPNOxKN7sOAiiln5%2FloPHH%2By9KRZvD5uNShVb8qkhGRBuvLiixufRrY56w8CRFoJcvcXQFZyEjlwzzV8cEomzJNCdyLqoUsp%2Bn8xazZ8NwpbLiBC3gjBMJ%2Fskb0GOqUBOzpjxxLcvTv0SffsgoooTbzQlwkILkfW2vxJyCX72tN%2BOi6XVHmlIBcTWLFowrtnNJIo8ZfD4AH88RZmsXBdLcTZSKOurEH8QStZwEn4GOH9IR8oZ%2F%2FF%2BiXaY13RWQ3lP8OBigVBWyOWfz1O9Sckg7W6KgniPOvH3HjQGUB2azJ4RxSpf9cYPiG76PMhqTl2sWosu8Nt9ZPynw5u5t%2BQsUFNHf6q&X-Amz-Signature=59a96c945a4e8857e47e6e4b39c6bc83d5255400fc440318b9156c6ce8b36d79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZWZFYCL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIAECbYGuLcgHmrJ%2BlpM600zSW4oLINDnb9Z3AtcMRN3%2BAiEA3YODaqQViLKAIQZeJpsIoDvZ5FhCv%2Bqu0YbWVkqIpxsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMXbeTOLoYtiJ8%2FOiircAyTARr5t%2Bjc92DRAdVcFWVxqgzj%2BjVMkiO0ctL71KVTVqhyyhXAcMc%2BiSr1oBZWjtTFWoRqu9ovxNAWwSXPU%2BIMqYYMw%2BxZkuNLbStcKF%2F1ZhaFT01Ui58n1qr%2FdNBWBKSQf%2FR4uZuRSn31TpyaHVAIWpWFiGcDEygFER8qZ7naq335dpIgB3Z3ey6RCRER2huuKOXMJMn0LGvqYsWIJrP69Af0nYlGqc2tcgz40gjSrdh2Ef7936ETM%2Bv5eZnKrXOmZDoraejT28efv%2F35u8X%2B9wMrXyYQ3gEEnZL%2FVAHF%2B1xcmUJmFKooKtdSK6%2FviajEFAer8RNUZ6q30ThGOkkNytWl32ERBqP3iIyyRgumoh15eFyDlU%2FjqqnMjCpGo3L0bBWbplMvtkaoR4MN4OPdJgkjfSBgm1o5HK5Q5TuR1uXXZOg53EWNxY7KUie0%2FLr%2BnqHtV8r1hLx3%2BqCJRJ3XQr3ehdlj8sLMUX0Vg2l1mL8CrhInwIoFKelduzrtieRorOlvMb9vcqkz6uoTR6xagdb2xr958L4PtVBpdJCJAceRuq7RfW8BVvRvFD2B7Y%2BIUQsDLqVQEYuDt6JzcbhamWU1du%2FNoiWt9FWbRDGN8hG2DIN2uPKfqvdL%2BMNXrkb0GOqUBRwDdeQN9%2FV1ZEIRzUu9fjy8M2ktvYmTxZjUiIkbD4fvO1joyToOk6mCLsdEQz5F9ERXE%2BxQ4DWO6C44zINOjmNMnvYuD4sZCFwd%2BmpY8yhU8UIKjdSmHPaoE1pxMxNjhHVm3aXhAilCimQPden2v9YoIDWH%2B%2B1dMtpzRzxcAVAe1kGCqRKWikb7O8MFHSmeDTt3vjjNsagi%2BnxlzjGAkF3M73m88&X-Amz-Signature=dcb82e392f3fedf07dc74492795816ecc462a0db27cf7a7954b707c66ac020c5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666K25GHPT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIHCSt4RxT7T%2BEnDmAnz0r27ZHKUoIXv7IsrPgReuOWJaAiBbl%2B7Z56vT62BVk%2BfGA%2FCNSgxN9Lw9wElsLwRzDOG%2FTyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMTm1BGY4B%2Fsc%2FdFGFKtwDXJsq%2BKZx5cc%2BdBV7x%2FmZ9B7GrcOWZ0amzjvMZNsrtzSj8qTWup5XQ60l7nx9ybWvpQS%2F7n9X2zJxmUm6SZiJ5ZE3pzwXI0QvbyW19z36w39Dc4BvQFYSK%2BuOiFFRIzmx38NZvJ3FFtcwofmJbj7nxskC08PeGtdbppjiR7iB7PRitkWhn00rcc58WOafhTvf9Ym1dPLjg%2FplLRPKH0Km%2FH%2B3g4BV%2Bbh0%2BMjxNUKzwUD2tMVYP6UUwB9IPVT9KWL1E6Yg5Bfeiuii0UP9NJlR4M1P5DwogTakNxgdmb1soKdzT%2BMTD8JPKSXMb5xtNBlWUj4zynIg%2B4VahAnIXHUrQU725JgoWiA2Ce643z7itPF%2BPtkb1OcYM2S%2FnNV2jCYP%2B5ky6%2BAPxwf9V%2BWJiz4Hsrugurrm18qexnwxUE7I42pHBLvKMs45JUfn1mx1Vt%2Fk4FIHAuI388PN3WmTYMXJBmV%2BR1uRyTGBYAy1kNtxBDOd4t33Fh0EXOqSAlGKY6cP5tcA3JcrSdy5zGWFo8PU41WcRG1jf7yNzo2Ohm0lWHBq5n4nwFIJCXcLnndBx%2BGGMw1GQJUCKmv9PwATQzfQvadjZHqJrUo4fQG1N%2F0DhLTPWCTUNKgzc%2FoHXS4w1OuRvQY6pgHTWuVkl8ij%2Fg%2FSCfKCMlJf5P%2FsDOqi1kY%2FAsJG2d7ciWgUwRUt4PvwaVKNb9uuNjvZzsQ9%2BhzzYnf6iFUKO38hqDqjLnlhaq%2FVZWz1VFseQ%2BC%2BNopF%2Fe8pgIxY3u5hI7pX32fNOocajYmJXTdnYZKpiVyyHuUisQYMx9dn%2BDFD2u87svNeRrvinEP8k8ilcDFyjdSSZX7edqWB7fvAQtVCouGUsu9s&X-Amz-Signature=dd4894092ae179beaad949d635cbe5dab72b1273a5be3480dd3c5d61bda4c27e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF4LEYYJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDGXSRY%2FYzdofM5jz8dVgkeerT95zBTJfFRRh04uKVwIgIhAIOPpbY3%2BlJuQnE1cb1znJr1pUYEF8B7sf%2B%2B6ohf1zIkKv8DCFoQABoMNjM3NDIzMTgzODA1IgwOVuxxWAUXfNW%2BJh8q3AMPED0Y7Ar4OoqEB5v6zRbRzQxIfNljZpP4CncBnlT1tZ9OGBI7n15%2FQlQsAODf3NOry%2BbEEdjM6qTK3%2F71kmweDWUTYhPAIqUPNoMhSKUgGPlp5HxcINKLMPD0HUl74uun9d6KMWs70uXOsOLEvQy3mMQLqi6e34s%2FJA%2B4mcMX%2FAb%2FTksFBApS0Vh%2FQlSCCsONrfzUnHcgeHijULKc6iaoKqskYRJAxditESRtUV5r091m4w2A2pZ60xodlsHjH1xM98dQctRoL2wY4Ariyb%2BMhuhBN%2FaKLsOg5WL%2BTG6Ylio%2FPlpbBWFqnhfFDr92x41l4585N7Z2DOLIlyZhEKIvNZ5J5evqpUGOef%2Fqr8%2BnazmstJ3JeOQrWZt3xoeptj%2BVr8x%2BeflDEXC7uvAlZ4gjAdN9or78%2F7NZ9cUtgFDwQG%2BF%2F7B5uunlCXfVE4Z6AO1PCSkZs4rQGLSIli02gtpFnmdISeOrSZSJsgBfO%2BNDRhogVOcN6T07jXOChOjT2gW%2Bv5QGk%2FaIadj30MkpYsk57GzRw7oEdBO%2B5qgVGdtIAn3WXwdhayqfG9XBlB9DWzplCIBcs3PvrjkuI9wMSLTnvQc0lgAPQPT7MqfkHteKxoU34JA9uKuteRcxSzDf65G9BjqkAT6nhmQy2vcv1R1EYdUNWbFxtFgOBrWPPvtStw7VAwOc1NoMPzLatftKx%2FCsllKE2j9QNnU5xMTg2CMTzKkIg%2F5p%2FEmY8TuxKvhggbc92f2ymiDs%2FE7998GyGiQ6wo1JJAjcSU4KMiclxlUNZay7fvocKNQKlHfBEKKFYLaWWe44hBJByR%2FKR9Z2yv%2BVO3FvZVU1QECgXruSw1XCFdWQX%2BP%2B%2Fcwu&X-Amz-Signature=3e17ca5f0ac852d90a7945f849623acd435423344023b1876bc818c5ade38304&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P7BS2A3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDwuZE4IuehZYkWB6qdmcto9jNSxG1EyIOvz4NBUm55sQIgfnU4V8tBV6Sn5nNTv46BygqzKQJCAILgFp3stq1ZCtQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDIRQE1HHFjBcl6w6xyrcA90MfLoRXnFMeKSpsB0Q1HvziXvAGKFeB3NaBZhqd3pdoE2TIq6VQmXOL%2B7cLRr%2BLnXN6VHUqVuV2j07nVuTNJ2I5ajLTtHEw64uhCl90%2Fn8YC%2BrA1nbh2vg4PrAadesqApQDUaoUfX2iLp5w8U9sYmvHUs0US19UhNvOarl7OlLf%2Ftf9qSyDiyXIy%2Bk5bpYjBvxPL%2BCCvoSqmIW2PXCNEg4LSwt4JZAltOBrEjE4Mtld3UfA7aW2PnbnMmyP0HjdipHecrY5kIOHr%2BPI6vQRywlyVzloP2uQPKZP8fjcGI7YtpoRYUOx0d4IGWxMvvbfAJPIa5XddTxeldxfqk5nYanCBEMVzMqcE%2Fov6G0Hhfrzz9JClWfaP2vvugR7H1BMnDUbRTLcSuIzUdtB9yacMHjeVQZ5MvP4MrjsC2HRsorVyltcg0JAupGvjAJbNwDit4Xl6KMh31Wkxayne7BvAS2pvs29nj%2FGraEh6vL4E0uDsKTT7Zg9LcQikYCcR6%2F0HfgkoCareP3rCwsxGtFxnmMV2668zj%2Bqz3Iocm1KDuDi01QkKwoHfUZ4kV%2Bgsmfrp2MYa3zLLv%2BEqzUTLzDMSORrfr10acuZKYoSoAA66hkY%2FtoheXdMdDSjfm4MNXrkb0GOqUBM5l3ICQcMKa0rXXSmD%2FBhRCwiQ7iYZAb80PCVvuWx8WvWfg6meJUdPm5SmQuB6%2F6SjDs2lo1BvL9YGgo%2BggXuahhfX5SBLfQQcKZLVQi71BuwqHIRk0rYm8LS35JtbSXzNhyYgwm80oSUn%2BPW%2BzPgPs2D%2FeVE9kThFg7Cltlo1tQNlvju9EnWDjoxBirle%2FjliL3xC0HeyGksb3hpcTf4Ln54LpE&X-Amz-Signature=343930ba9476f1430f976b8dab54e05d9a624f4d43aa311be69f25f89fd1cd4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZWZFYCL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIAECbYGuLcgHmrJ%2BlpM600zSW4oLINDnb9Z3AtcMRN3%2BAiEA3YODaqQViLKAIQZeJpsIoDvZ5FhCv%2Bqu0YbWVkqIpxsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMXbeTOLoYtiJ8%2FOiircAyTARr5t%2Bjc92DRAdVcFWVxqgzj%2BjVMkiO0ctL71KVTVqhyyhXAcMc%2BiSr1oBZWjtTFWoRqu9ovxNAWwSXPU%2BIMqYYMw%2BxZkuNLbStcKF%2F1ZhaFT01Ui58n1qr%2FdNBWBKSQf%2FR4uZuRSn31TpyaHVAIWpWFiGcDEygFER8qZ7naq335dpIgB3Z3ey6RCRER2huuKOXMJMn0LGvqYsWIJrP69Af0nYlGqc2tcgz40gjSrdh2Ef7936ETM%2Bv5eZnKrXOmZDoraejT28efv%2F35u8X%2B9wMrXyYQ3gEEnZL%2FVAHF%2B1xcmUJmFKooKtdSK6%2FviajEFAer8RNUZ6q30ThGOkkNytWl32ERBqP3iIyyRgumoh15eFyDlU%2FjqqnMjCpGo3L0bBWbplMvtkaoR4MN4OPdJgkjfSBgm1o5HK5Q5TuR1uXXZOg53EWNxY7KUie0%2FLr%2BnqHtV8r1hLx3%2BqCJRJ3XQr3ehdlj8sLMUX0Vg2l1mL8CrhInwIoFKelduzrtieRorOlvMb9vcqkz6uoTR6xagdb2xr958L4PtVBpdJCJAceRuq7RfW8BVvRvFD2B7Y%2BIUQsDLqVQEYuDt6JzcbhamWU1du%2FNoiWt9FWbRDGN8hG2DIN2uPKfqvdL%2BMNXrkb0GOqUBRwDdeQN9%2FV1ZEIRzUu9fjy8M2ktvYmTxZjUiIkbD4fvO1joyToOk6mCLsdEQz5F9ERXE%2BxQ4DWO6C44zINOjmNMnvYuD4sZCFwd%2BmpY8yhU8UIKjdSmHPaoE1pxMxNjhHVm3aXhAilCimQPden2v9YoIDWH%2B%2B1dMtpzRzxcAVAe1kGCqRKWikb7O8MFHSmeDTt3vjjNsagi%2BnxlzjGAkF3M73m88&X-Amz-Signature=a8b22acabc6545df9826e6b3e6c59be5421b65f4d5960c827e5d1b387c616b4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P7BS2A3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDwuZE4IuehZYkWB6qdmcto9jNSxG1EyIOvz4NBUm55sQIgfnU4V8tBV6Sn5nNTv46BygqzKQJCAILgFp3stq1ZCtQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDIRQE1HHFjBcl6w6xyrcA90MfLoRXnFMeKSpsB0Q1HvziXvAGKFeB3NaBZhqd3pdoE2TIq6VQmXOL%2B7cLRr%2BLnXN6VHUqVuV2j07nVuTNJ2I5ajLTtHEw64uhCl90%2Fn8YC%2BrA1nbh2vg4PrAadesqApQDUaoUfX2iLp5w8U9sYmvHUs0US19UhNvOarl7OlLf%2Ftf9qSyDiyXIy%2Bk5bpYjBvxPL%2BCCvoSqmIW2PXCNEg4LSwt4JZAltOBrEjE4Mtld3UfA7aW2PnbnMmyP0HjdipHecrY5kIOHr%2BPI6vQRywlyVzloP2uQPKZP8fjcGI7YtpoRYUOx0d4IGWxMvvbfAJPIa5XddTxeldxfqk5nYanCBEMVzMqcE%2Fov6G0Hhfrzz9JClWfaP2vvugR7H1BMnDUbRTLcSuIzUdtB9yacMHjeVQZ5MvP4MrjsC2HRsorVyltcg0JAupGvjAJbNwDit4Xl6KMh31Wkxayne7BvAS2pvs29nj%2FGraEh6vL4E0uDsKTT7Zg9LcQikYCcR6%2F0HfgkoCareP3rCwsxGtFxnmMV2668zj%2Bqz3Iocm1KDuDi01QkKwoHfUZ4kV%2Bgsmfrp2MYa3zLLv%2BEqzUTLzDMSORrfr10acuZKYoSoAA66hkY%2FtoheXdMdDSjfm4MNXrkb0GOqUBM5l3ICQcMKa0rXXSmD%2FBhRCwiQ7iYZAb80PCVvuWx8WvWfg6meJUdPm5SmQuB6%2F6SjDs2lo1BvL9YGgo%2BggXuahhfX5SBLfQQcKZLVQi71BuwqHIRk0rYm8LS35JtbSXzNhyYgwm80oSUn%2BPW%2BzPgPs2D%2FeVE9kThFg7Cltlo1tQNlvju9EnWDjoxBirle%2FjliL3xC0HeyGksb3hpcTf4Ln54LpE&X-Amz-Signature=a84ece6dfbe22d5faf20e89e15706677ee90ae7099420f0f5ff6eddfa209e5f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P7BS2A3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDwuZE4IuehZYkWB6qdmcto9jNSxG1EyIOvz4NBUm55sQIgfnU4V8tBV6Sn5nNTv46BygqzKQJCAILgFp3stq1ZCtQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDIRQE1HHFjBcl6w6xyrcA90MfLoRXnFMeKSpsB0Q1HvziXvAGKFeB3NaBZhqd3pdoE2TIq6VQmXOL%2B7cLRr%2BLnXN6VHUqVuV2j07nVuTNJ2I5ajLTtHEw64uhCl90%2Fn8YC%2BrA1nbh2vg4PrAadesqApQDUaoUfX2iLp5w8U9sYmvHUs0US19UhNvOarl7OlLf%2Ftf9qSyDiyXIy%2Bk5bpYjBvxPL%2BCCvoSqmIW2PXCNEg4LSwt4JZAltOBrEjE4Mtld3UfA7aW2PnbnMmyP0HjdipHecrY5kIOHr%2BPI6vQRywlyVzloP2uQPKZP8fjcGI7YtpoRYUOx0d4IGWxMvvbfAJPIa5XddTxeldxfqk5nYanCBEMVzMqcE%2Fov6G0Hhfrzz9JClWfaP2vvugR7H1BMnDUbRTLcSuIzUdtB9yacMHjeVQZ5MvP4MrjsC2HRsorVyltcg0JAupGvjAJbNwDit4Xl6KMh31Wkxayne7BvAS2pvs29nj%2FGraEh6vL4E0uDsKTT7Zg9LcQikYCcR6%2F0HfgkoCareP3rCwsxGtFxnmMV2668zj%2Bqz3Iocm1KDuDi01QkKwoHfUZ4kV%2Bgsmfrp2MYa3zLLv%2BEqzUTLzDMSORrfr10acuZKYoSoAA66hkY%2FtoheXdMdDSjfm4MNXrkb0GOqUBM5l3ICQcMKa0rXXSmD%2FBhRCwiQ7iYZAb80PCVvuWx8WvWfg6meJUdPm5SmQuB6%2F6SjDs2lo1BvL9YGgo%2BggXuahhfX5SBLfQQcKZLVQi71BuwqHIRk0rYm8LS35JtbSXzNhyYgwm80oSUn%2BPW%2BzPgPs2D%2FeVE9kThFg7Cltlo1tQNlvju9EnWDjoxBirle%2FjliL3xC0HeyGksb3hpcTf4Ln54LpE&X-Amz-Signature=baeaa54546db30d608ba70d936ee0139ae1f4a5d4b59bb4dba9056eb4d2ef226&X-Amz-SignedHeaders=host&x-id=GetObject)
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