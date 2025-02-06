

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JKDAQQX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIGeLl3s4pPhMQ9ax%2B8OZ%2BZwAIJPKvcRzvqhmWbjReU5fAiEA9GYT2vW0J2KBWkrHY%2BUkzHXzzhC76MfekDimKNmLy9sq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEMFqNOxgErngLUfsircA4kE8ZgXB0WyxnmDVLf9nw9r4JoPuN3z2T1wVET1HwZI96YGnfkVGl1ZP0XsKI6ePm3saaaKjs8JaxhGuITg2X7s4%2FuYuJdpLsDo6laWJbp5GTGp2JYkf3J%2BEM6HN73PoamsrBTAIqDuBHc2LTTGz9QMilV9P8768VTVJftPWvEnwDwPYnvI011Jzx12rk0sVvXXWx%2BTFLZjNpWKorw4XPpLTD03IvxvloSmp4ZW0TtKUzkspF3r9nu%2FvDHUFs6fTlKTVbhlQYNYRWatu7%2FXnHD%2BhgCX%2BewiJtxZv8%2F3Pd%2ByCFmuZoJqkdg7mBSNwibK34zhT1Y0G4Jical9orTomobG78LlOWsELhGrCqloHHzEbSWcfpw60IuRHKGBbdoTdnlRTNWgah37mZhS%2FGjP01Ohh20cNXVo1CYjWm0kexMh79IAxF1F0S%2B1kG4YI%2BELjLQ6x1UtiiF0vfNKolUeE4Rg7boNFS2h9iIs9tcBcekJ8SuIQAWNXMT9SlZ1NeRFiDtlqYrOzJQcpYwjiEr2bLcaGc6ZaoMkh8T5URHlXK9Fw%2FTe661rM4GJ9E8K2NzYKmzefjtvwQTRMTsSYjYWWVghcRargnf%2B8P23pt4sn0bjQ%2BqOJp0DL6owPCsqMPj4kr0GOqUBIbyi6bzsWqKGhBmG2AWTyGSHkYppIdU4M4bAs%2FMx7ab%2Ff1xAwi5ejOGUDkPNw1EQiOnHoeip%2BiwhPsvhRkV91RAdxeLfdOExqnJGavP5ONBdkUFW1cDfmio5C9u4NAJ1f30aS4JAwvwSs0oQtqw5BUbwgDIOvqIH%2B3BrHKL3%2FIHdeIGCsLIdwXWFUjtGbIvsL8zhJ80YElHDxCGuGu6eJN%2BlCjwc&X-Amz-Signature=22fe76f4c988d2062b1236c7df17f19a579402defbb724625be14bb8455cc8b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663N7NWTMR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBBTcQpnOXsgNqesXjPBXOHi7EdsjzCwRbCE2p8ws26%2FAiEAv6n0bxLNxYnJm6UhOMgHIQrI97DH6p22qLZC%2BCbzwRwq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDBl6KyVoap7o5dmgACrcA%2BBD1cJt1Hu1kxvZnSPmS2G4S38roCWtwcWR3XAtLqpAdMlqCtyej%2FBk%2FOhIzHVdujNg3BgIZw87idNtbUcG4cmkmTvP69EM94uKqiIdHpHOaHQ5LW422UQgXz1SWopk1vaBY7eTx5cIvAwex%2BZVfvRmKS3y6%2BcW98tmH2Lxebl5waS0EEW6B5h4v%2FLkH2IFf0hOq1b4DQgnhxKNlN1Bz3pHIkNu1ZM7L3oEa66c5eNpyfUAHBhdGxiwKfU4qDFEKhRCBQsNYbgLuhf3yYgkpwsPCOcQy5opv3WIkohPaxS2e2zuDYofzXJ0%2FW0rvleJC1UM5ML%2FfqCqJZcsv68pauNUdNGhUIqJ95VnmHB2vZb21Ie6mIea5qXoHZ6oZKOrFeqKQXrrAohVE1ny%2Biqu2lMPCotqB6YkHq0PHd%2F%2BByEL9wPpcu%2F8PHgmjW1jc1rXnja8%2Bi1ClJ0NkZoTfbyS%2BeXFXh0EGWO9aQzaKdp6%2B4RsdbkZz3bCndoGQ7J7TJmYh5Z7bHuUiBatbRdR%2Bbq%2BQSzwhcjVdcEqjv9PY0sx7LPEjlENb8bZSAx0FJrcBax7%2BumAZSqCBXzS%2FERqjZbDGSWaTluqbXFcu8paaMVN6GKzF3AloeFXPSAKgP0ZMLP5kr0GOqUBOftbfWRaaFR9er5QGPlfUnOsRTEXEOOwi%2Bh%2BkJUnLSR%2Fts4EXdgq1rYOjgBVuK4%2F6MKqIKXbamIizsbAuljPN%2FrRJgF68UL%2BtZCw7idLje51aecWZyX1p2%2BHrBstbjZBBsb8zEVNKY90BKogSVG31CKeuKYEjf1GgMZwiDGCceAcrXBZJSiJ1958UW2OM2QaUSkAcaF6dD1kVZTtWalT5CVmQdZ1&X-Amz-Signature=6c46968806133ac4524d851f0b71942c8e996d4efde012e5dd664aa329756d24&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643MMNQOE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCTXF6txwWMsJuIV3PY0PIA4FkNOgzAi6aalgRyK0TrGwIgC9Yjn6Y4ZoAg8xajMlZv9BdU2FxrE4D99jfLAjEnikQq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDG7v9ufh7Kp496dGsircAy1xWZL2wV%2FWfgKYRPSEl3FzhdP1qxQ3okLn9BXA%2FgvL1mkdNSJxuQEraTnEvMMYnFXr22WAUYoKmABRkF9T%2FEbtcrxdEkD1UeXMYPSpw5cByA49B9efdvyKNsAd7UxEJD8%2BKozavUrDxpIiE%2B4dNcPKnRppgk0ra9FExTXOoH9%2BID%2B9sxSreVYxB33b8YTxgwOvcOc3mQbay38GsJDLJDzpBC1AO15v0ddmO1i%2Ba%2FJPoltpSCVv9TRb%2FvJURDMj6IaiSZS9vPr3mIp7tPtEFiL0484UJnWtWmx3pTZtXJhNAd2nNlf9SY5mdI0IsYTF%2FqPYrmSE2wZpzfIEdWDYDqmvifSo1n8da%2FF5%2F3slBP8FKEbdN6bQTnxMkSuGoTx1swye3CkNeYXk%2BMl2IAk3EMcvT3nx33JPW6GEdRJz%2FaBabqs6eVtFgXdZNwncTjM%2BOrngkF92nWyiBdfvQ63meiLQ5Uhjks9MDxMRRJrylaPqvqQnxJMKGUov%2FonkPwtCAhNbXdnDsc8b4CyggIZ%2FXQAGA3XTiLRw%2F7n9XuF%2B4CIxdglsguR5tKWdGq7B44oLZXINeajwMrlVF6rSQvN70fO0iu47wBJejvGuzQ9iQWRJVBtB2eEXBH08J4VAMPz4kr0GOqUB8xusZOm7lYFvUkcVha5C0LTp7n4JSpu%2F0%2BMAzT9QO%2FytRWLgISfydMOpIYuj8M0L4EaO8lEa%2FLZcAdwEWEUR%2BXp1Reudv9GQx3z0PjAXpmC3W37QShNs3Rt16LyPZaEC3CMR2eFZHELVtsFVah4Z6DI8X2sebJ6zqIUhgvO1rDYgl8peypA6dAZzacn84IgKZP8yfFDuERjMtG6gIZtpfssecygI&X-Amz-Signature=d8f240c82904189167509bb0964ea8cd617b0d3546704a092ff6f156e224c28c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433R22ZP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCkTeR0od5IjhrHySEvC%2FZicAjigmMkKeXSfisESbrRjAIgRDjCI4b%2FpU0l2wT7UZL8XfkvX76RA%2Fj9x%2FLcXn%2FH2Kcq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDA7g03WzyzSrh40uvCrcA1ZI2O5Ta314QuseY9Xf%2BtQZrtoATwbxmemL8CAWEXBRyZXTKICDipqANTm9bWFgnB994lRFznNQB8LNYxA5rtUleRBxzJKFyqEkN80LapvKkYuB9NGo8d0Up3viziRqs6p5fOcLQarb9n%2FWRoL1oqbYQ1rm4yDNsxJyNheX49jVp6YWpqkXKAlOqUEDqxPlqXtiPmMlds1AvVYIpTEycxydb8HgCs9DbSU6D2BUBtOfRTvhvURqd5%2Bv9R34LhkYxhd9eiIQlk2dzjx1OiSO9riQvA77cNjePTRyxw3Bwm8VV9tL8dZIaWkZKl6cLSyyUJbOz96lVtp3BmYjRxVbYJzEbGQSOmnlIYU6sqV0%2B34uwtwKjsHHuJc7bFqeyExksyO%2FJQXUbIw24alJBEWfsssQn2G6jhGI%2FcMWzYFWVZpv00VoPxAFQn5CckaCareBqqIcBIVB6a8uSkTpejaGV7KJjPuosk%2BgNkri5T%2FFwTcNuWcQ1qVmS3qSeFN%2Fv37v8bRRz5IRmDtbh7AFvMhyo%2BAMEkqKXVbdcOjOLuJET6l2ZJX1nqmhw4JrYHpzEJNQlM13CBGgycNTZCBHa0NOzYSF41Zm271UerSCxyB2ebv%2BhZZP%2B%2FVT7UXPvMXVMND5kr0GOqUBGSEqeCZf7gHuFPIwBnLE7Rlg5HvuSqq3aRlzQUInuoG0v9NIa6ZtVoWjXgosX2UP0LJSZWrN10cTMzmu%2B9bGUYFootqK%2BlUuHUgqEzv2oPKp%2B1RZ3V2kaUmhk351j%2Ba4qF9aQmi8x9jZNtsPZf7lHX0io%2FRVh8ukS5Ce5n%2Bazja1YATNj8bVZH5bww3n67xudPDOn%2F8lUVJfOfMXCUiSK5nGmY9J&X-Amz-Signature=39db3425b015fab42a5495f0141dc5c7136c8e713e0a36a3b5a96fcb29adefbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32YH6G6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDmuE8c96hApognenuetqH6AzctVRoVnL%2BDR%2FitQkt4BwIgQ00adhOpyAC6gdaNItAzI46BXQ5qEuzVr0ESp5QKv%2B8q%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNjj3cVfIc0zP6wy5SrcAx%2FBmMgqG3lIBfnDKZVF2OSJYI%2BXdISOJvoxrBMnxHr%2BSQ%2FzohjvANXxQRprysQKMQcl2NvEbEGjB8HiAj2rm%2BAYF%2FRgSn%2BEteVaVe4zZjLyEN%2FILgH%2FsPkxfPWn8K36EIMFulMQsQRd80lkTJXqLurgMiGrNGRaeYU4dwzL6kmpDTthSspw9oAyEK7Ci8ninL2DAXEuQFjcMJws3lqPmnuOMulFJB%2BZET0GpwyxTPtHV9HEWl3FhLBrvHtPv9xH%2BrDkoIQjj2M36jaBbK6%2Bu7YQvwLn7etH3Yy9r2Nbhz1mSILX7adQXCAj7hGZcsP2X2MwdKOKJnSUvy7SSeIF0AjCPwsOu1Xi17ZTSoDC1K2mIQznNdzUOKjTpPdCL7Ju6%2FM2MZPU7OZdJb7yPhtifEuvkeszZSHI2H2kG8IcxS5QIPmHw7rEzpoyjjFqx%2FcjsVyZz2n6Gk%2FZfb9TCQ3ndgnRBy28EOqMp2MpCtYmhRQ5kFJSXI4Qtb67LYS37yQbC4cxGnShaUGJsx5srFnBYo%2BOECPLqjx3lZT2BL5qupF%2Fd%2FjcX6jGpvtR%2B8fqYj9hJXWUnAhsuR2vXtWzWpz0AH74knDEy0TMCbtu%2Bn2smKD5jLO3qzItaeEHJyVdMPD4kr0GOqUBo3T9RtIemYbGRK4LBQNi%2BCrd9Ggf%2BHM9Z8FjU4VrnZlx3pRJZNngPi3%2BN9eskY58isKokoWD9HBTPchXPzAOcxghsGZ44Rqpnu%2BN%2F4sv7qAlfGJ%2B%2FX86zNKpWz5o%2FL%2F14dxEzw8WTOd%2Fe4WApf01ViUNpfDeCs%2Fipn7MZi9s0NGSybw8NSCmkIhrXm8hBX5x5Vet%2BqVzgdLPbV7LvONTEODYrZoB&X-Amz-Signature=83661df143807ccfb82a083b40a92e3853b083cc3ebd5d663aa07ba3547155b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YP7KUZR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQC%2FpZAQKWwG6VvDzeEA%2FiHlvD0xddMouGaZqP2DF20FFwIgB40yB%2B9ObPAX%2B2caK98GgqgQyyaUTtWD0S0SRNH195Yq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIfShrmlfQgmdrxtnircA%2F%2BNWzKn4gHHql5%2FDWkmUu2jq3VwUTiwO630C0YYSxannpQxOGwpHAuSiA2w8OiKrM%2BGaCYgY5P3KrXH2uevIW4aIrCU0i8sfe65xQzta0IyUvXrpmIoaoKDL%2B1YgzEkqhHfU0u3GhZOro1NXylxzUNqj5mDywtxtE2W2a9lQgK8zGr7RYRZDtbXtPsuYQRvaXJgouYrz5uu6BhkSMQgIpAdhXQ%2BZZV96WaBhpmo3TqXeSU%2FobAfGnO6VBDqzWZHXgbHrwzN5Po3R9bI90%2Fej%2Baeyfx%2B%2BC5Wb51TcPHiCPfX3t3rGjAkxFyyc8NrmZ9e0kL4D6Xgyr%2F49An%2BiQv2puEEpOYV7%2B4ntIMI%2Fu5AK6MkU5XkL7SOptx885AderyoWwC3VoWmmY2u1Uvn87wMVBjqSRWpk73fXn2MH8uVd6k76QmlTc8vUYlKBPItDK7CwqPKyoDTt8l2qZU2sYupeLEtX3GJvB0qwPn3fG3nLM42JlTza4ifCgleFQh8x%2BH9nVpUkH21vEzRpwMTpPSiHyFv4v9C9l%2BekANnSdeEvKUeehr%2FRo8Ag8%2FXII8uBUXSL37DLAYTFZIV0f9C1qghKgqYG4RMqmMy0MBVoNenIZE3oZYGQBsneOiI7tVUMIn5kr0GOqUBxWtMLAnRM9j%2BKlza2ZVKUEHIJUdx%2FQ5wQkcnuxeWCG%2FcFrvXZRupJw1hz1a5iCpKziAVTuuxmu5wkydXeNOR2vUt9ODe98tEQ8krKYyYtCGG%2BhUYEU5w8yZJYh5bVeNSNpAd%2Bb8uAQ5A%2BtlYbylhci%2B3aFTTSnOB900GBAhomfiREAX00OnURUVjLXLhT8CZF5YGDQLGT271MS0N2tsfU%2F0NsQwy&X-Amz-Signature=1c8a31687e093b7498917dfdfbe634d4d2db057e9e3d112a84f798b49d13e6f9&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNYMNIAX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIFiLeanXZPJXplKULoQHuDENFeGeeiO9G81ppBCOv5JHAiBjYbNQ1MTeR8cv5%2BRVmPTE9sH%2BSoQJIFXrT1rQXssFICr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMUSuqxtH2D4fRLKDKKtwD%2BoRQ6vITC9txXdpma8QUA7EWYEf8ffRiMN2TwRb4qSaaNVJ2DhJuwFBp3937TEIeMGr%2FoHvnpDqJWvugmYdcLoAe2a4tVLS2P%2BZfBatqenG6ABKC%2B1%2BSxxmgGJ9ClWyAkmJ7bAm167sc2c2nT5RcX1KZDm7hSfTmvaH9YARU1ZdMXdPv%2BlqMQ2TsazXIGuBpO%2Baeo3b%2FCnb4tBTBHCKLZVCBi4qfep%2FIEIBUjcU%2B98T%2FBOHavnZXCrV0KcaXrnlNo2Eo48TrBmobzBkgYVVV8Wyhx6l7gqTakDPGvOcOyZHcLgbBGGrfx%2FnsAOeFRyXuMJJv%2B%2B844t0%2BbCuKmshn5HegANDMmGEigF1lpclA7d84iNve%2F3qfpkeBDrvpbva0me9phDUf84W7hpI%2FkHUG%2Fp26fFJ7qlAgmR2U7L9xPHlfN4VUOSYsYYjnHS6RC0xtEB6y2roz3snLPb4t4FejlRVnjZcCzM37wy7pq1%2FCSoCC7KBjhuuz9dwRue2H%2FkwdMcFCkGEuSSDMXpuwnqCJPP0IhtR6rWy7rskw6z1tj7vV8zyvd4RRxYQuKPSV6FaGEbdlfirEgZqdAIavG9YWIoi6gqObILzHj%2BNDakBuZOgn%2BwjDUsSuKhcqBvMwzPmSvQY6pgFPCIO7LGxIAknE%2F9sRVopeL3yLTK%2BepiI3qA9wH20F8RrxGJhEsGbGKRHUCX9W5Gx1cbamT6rTBxY3h6dZrHY8cJlwfMQswC8g1MEV5hjfMxEDR56Ye%2Bz999sVbKNnn6exdyLmsUE%2BbLY6C7jzC0vH%2Fw71eYHCy42%2BQGQPdlGzHeQWc40o%2BChc3KDYfKoH34kma%2BpGywlqdw89wwEh15qtyk2aGNqi&X-Amz-Signature=446367b88bfbabd5534e4a29187cf5e9c5892d09a371dbe4fb9009dc6c78f946&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5OTWLOM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCpB1SWshohoAcNVD0W1%2FVRiV511HgQV2Nvxmh6yJ3WwAIhAO78fUBaPerqR7zZeysIXZP%2FObndNdz9K8yiA9gDqjjwKv8DCF8QABoMNjM3NDIzMTgzODA1Igz9OD4trtHS5EzdU3Qq3AP9RyG%2FpKpeOCm74%2F96zrItH3flIRsg5gl4WqdDvMz38wmtHs%2B8LPWYRtBnPXKOw5WJjPBS35OBxubd3ujKrXEH85NkayMkb6p8ziK6MLCMOYailMOewo7tE7HhTL%2B3GGQRdrTyLNkAHVjf%2FWM5Cc%2F%2Fui2SJ7sUjoOcmvhMGUGW%2F%2FtrE6r3e22Vajm4u7Ve2QZKDJKXIBFW6ozxzG0u5ZyRYSsoGVVFQLRScNVI3nFwPP2VsKofgqW8hjCvinUPGJSSNMAcXUJ7HKHSEqekI6sNi%2BC7X0gr%2BH1mRxsWR4mBTBDMXj9g9bnJW9tjRqZnjMvl2U6FGSGs8k6NawBgWIzaUU0trGi0nhDPtfv2VAplawO1MN0dUdJnFsQU2Nv%2B5FLx4wd5YdmCat8zzZv%2ByM9J%2F7JQ5FDQaqUzGJNUkc0WpjClEDDLt0Cj0FI6h4GpYKGwBBZUhce5qcbQS0OyU%2BlboRfIM7gK3nm7bu0IlfmubJYdsoxf9un9qLE5N3ClkXmYCWGR9jZmjUFpqR1RS%2FQZv23kWPgnQIaoO485w%2BAJuBIHVgYSV%2BEAlymR9MMfqfIekSDwksK%2B%2Bc54JO5%2FVxOUYlJ%2BH%2FlqAGkUU%2FTPG2S1eoOj6eQ1pINlPs6M1DDA%2BZK9BjqkAZLGehMK2AOQj9q0cA05MDCCMQ%2FkDJFVoOviJmtyj%2FPe6ZYI7mIcuSOpczaUA4Gp5HL1L0bFCOhiDfBs9%2F1b1HnhIJbCINMg1hweaZr%2BYD7hZCj0wTLlOuvZrtaApl9BEy9UgSBQQmE2Lm6s44QMTkrQ4QunbIltY8wbMETG3s1Owkfgbet%2Bx%2BQi%2F1x%2Fbc8QMACM6je8iNDLAshYT0jCiNHeKCPu&X-Amz-Signature=a1dc3e80e3f7581a4436fb71213d81af4cba37a5cc9e353b2aea6d6f5ed08c92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y32YH6G6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDmuE8c96hApognenuetqH6AzctVRoVnL%2BDR%2FitQkt4BwIgQ00adhOpyAC6gdaNItAzI46BXQ5qEuzVr0ESp5QKv%2B8q%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNjj3cVfIc0zP6wy5SrcAx%2FBmMgqG3lIBfnDKZVF2OSJYI%2BXdISOJvoxrBMnxHr%2BSQ%2FzohjvANXxQRprysQKMQcl2NvEbEGjB8HiAj2rm%2BAYF%2FRgSn%2BEteVaVe4zZjLyEN%2FILgH%2FsPkxfPWn8K36EIMFulMQsQRd80lkTJXqLurgMiGrNGRaeYU4dwzL6kmpDTthSspw9oAyEK7Ci8ninL2DAXEuQFjcMJws3lqPmnuOMulFJB%2BZET0GpwyxTPtHV9HEWl3FhLBrvHtPv9xH%2BrDkoIQjj2M36jaBbK6%2Bu7YQvwLn7etH3Yy9r2Nbhz1mSILX7adQXCAj7hGZcsP2X2MwdKOKJnSUvy7SSeIF0AjCPwsOu1Xi17ZTSoDC1K2mIQznNdzUOKjTpPdCL7Ju6%2FM2MZPU7OZdJb7yPhtifEuvkeszZSHI2H2kG8IcxS5QIPmHw7rEzpoyjjFqx%2FcjsVyZz2n6Gk%2FZfb9TCQ3ndgnRBy28EOqMp2MpCtYmhRQ5kFJSXI4Qtb67LYS37yQbC4cxGnShaUGJsx5srFnBYo%2BOECPLqjx3lZT2BL5qupF%2Fd%2FjcX6jGpvtR%2B8fqYj9hJXWUnAhsuR2vXtWzWpz0AH74knDEy0TMCbtu%2Bn2smKD5jLO3qzItaeEHJyVdMPD4kr0GOqUBo3T9RtIemYbGRK4LBQNi%2BCrd9Ggf%2BHM9Z8FjU4VrnZlx3pRJZNngPi3%2BN9eskY58isKokoWD9HBTPchXPzAOcxghsGZ44Rqpnu%2BN%2F4sv7qAlfGJ%2B%2FX86zNKpWz5o%2FL%2F14dxEzw8WTOd%2Fe4WApf01ViUNpfDeCs%2Fipn7MZi9s0NGSybw8NSCmkIhrXm8hBX5x5Vet%2BqVzgdLPbV7LvONTEODYrZoB&X-Amz-Signature=fda8f1a0c1d6a518b47ca461afb2bc98de9d728efc8981b66bca709115c25d58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RKTDL3E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDJjkqS0Y5gEM7xq1uQpLpjdTkufaQfO3Th7S38pL0W0AIgbpXefw43JpIBbD9ILidLWIjGc7ziMuXdIGlfVAWwahQq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNR4Q1ylaD%2BmVJGFqyrcA7H4cyJlhXfJNIgxpSQ59jyuL68YzV%2FvJbfS1k%2FywqzoedqvdysG%2F%2BS6xKNjbrDIHoO0yoqQHtXDwa3qgW42ijxk0De7PLpFf5gzk40lvd%2FmX5LXM17XspF7hYSXpU7xok8mgmrnjMXsR6pcNqCheEYCl%2BrJJUUHYKZJrdxrm%2FDMkb91%2BBAUeiduYfXlHj31BIZI2SRpEG%2BEXeHo5K8prNXpA9%2BV%2F4F3D1Vhvhxb4Hcz7eluLk%2FyLroiCDc4ncTBVyVdOL0q66PdEO0N%2Fy62T5Mt5mA3m0zV8WdKxG6fM0jl0AtFiEQ%2BMe6lZmkeC%2FSmuZq1X4DCpwNRcpZUeYq9iFmVzrmKDG4y%2BqaO3apJeGuwA%2FcfWPdfOE2X0UWkat5rjAuujdX1L3gx%2BdFJT9m9%2BKmjEqAGSd2cRCvxgtd9fkc38jf40bKXtkGJMRB4WGLPlCNzn71cHAcgf%2BNOufg6AAKSDW547Nbk3HRU0Lmh2EeltdJ7KPCwz%2BBWVe6kwj8MNLlSVCsoz2un%2BF%2BStsBieCnTuILnJwOdpzvVR77v4FQCPU5rsegzj5OlLYpC1pDgT98nC7Q2SS0zZFGn1M%2F7Dv2%2BwdUzTIURFhcas%2BtSWxlRdD1C18eW%2BTKVrcNwMMD5kr0GOqUBT5nL5Yehn0i20ARd%2BNZJ5NcB5fkBJHtBx1OQYr6jOC%2Be1pMtVesCYeCqxEsB8rUnarZ8G1bhb14gehqR3oK%2BMrY8ip9Fxyga70p%2BIy1C0kjMiU4LDIuNPqwaLCM72pX8CnGXnFTKdr1sCR72h2rkvIZ4Bw2smIz3vwbnS08HaLwiJfAo2i1r7IEff9OkOm1zfxFtgz6WOo7vndAbVFSoNu5%2BsC7T&X-Amz-Signature=536e74916db60805f93b20df61591b4918e7172c8b0fbdaec24e9dcbcdf7a0c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RKTDL3E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDJjkqS0Y5gEM7xq1uQpLpjdTkufaQfO3Th7S38pL0W0AIgbpXefw43JpIBbD9ILidLWIjGc7ziMuXdIGlfVAWwahQq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNR4Q1ylaD%2BmVJGFqyrcA7H4cyJlhXfJNIgxpSQ59jyuL68YzV%2FvJbfS1k%2FywqzoedqvdysG%2F%2BS6xKNjbrDIHoO0yoqQHtXDwa3qgW42ijxk0De7PLpFf5gzk40lvd%2FmX5LXM17XspF7hYSXpU7xok8mgmrnjMXsR6pcNqCheEYCl%2BrJJUUHYKZJrdxrm%2FDMkb91%2BBAUeiduYfXlHj31BIZI2SRpEG%2BEXeHo5K8prNXpA9%2BV%2F4F3D1Vhvhxb4Hcz7eluLk%2FyLroiCDc4ncTBVyVdOL0q66PdEO0N%2Fy62T5Mt5mA3m0zV8WdKxG6fM0jl0AtFiEQ%2BMe6lZmkeC%2FSmuZq1X4DCpwNRcpZUeYq9iFmVzrmKDG4y%2BqaO3apJeGuwA%2FcfWPdfOE2X0UWkat5rjAuujdX1L3gx%2BdFJT9m9%2BKmjEqAGSd2cRCvxgtd9fkc38jf40bKXtkGJMRB4WGLPlCNzn71cHAcgf%2BNOufg6AAKSDW547Nbk3HRU0Lmh2EeltdJ7KPCwz%2BBWVe6kwj8MNLlSVCsoz2un%2BF%2BStsBieCnTuILnJwOdpzvVR77v4FQCPU5rsegzj5OlLYpC1pDgT98nC7Q2SS0zZFGn1M%2F7Dv2%2BwdUzTIURFhcas%2BtSWxlRdD1C18eW%2BTKVrcNwMMD5kr0GOqUBT5nL5Yehn0i20ARd%2BNZJ5NcB5fkBJHtBx1OQYr6jOC%2Be1pMtVesCYeCqxEsB8rUnarZ8G1bhb14gehqR3oK%2BMrY8ip9Fxyga70p%2BIy1C0kjMiU4LDIuNPqwaLCM72pX8CnGXnFTKdr1sCR72h2rkvIZ4Bw2smIz3vwbnS08HaLwiJfAo2i1r7IEff9OkOm1zfxFtgz6WOo7vndAbVFSoNu5%2BsC7T&X-Amz-Signature=2c84853110d185bc41ec2cdffeb7c958727f858e2f35b9fa95aebe6bb8b9a684&X-Amz-SignedHeaders=host&x-id=GetObject)
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