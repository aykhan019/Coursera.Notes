

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4GVZ4QM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIDSnAkLsjEgazUOD7scM7Ss83KWfZa1SFuBzPGuA8esPAiEAuXhCZqzJF1nfaO3yatJMwMzER4%2BVAyOfAkcnjo%2BAPqQq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOJMogNsQAfBicaN0ircA%2FxsSWqaw%2F36K6%2Fv6IWoUwIB4kvj2RRTPfCP9sdziPZeTAzlwGqK%2FBN8Pf46DjINiN2x0m91XwPxnTT%2Be%2BSaWqAFEHWEUevIEupF6gI4UB4Z5ngv5yAl0hKkWcsdC91wTlIf85VhlxuB0sm1yZ2dBsIHh68uFI4KuKFYU69CsCA9HAiLyNqg0kIG81F0JZcVAFJCSA5qcvP6oOGjVMJKXPOuCilYOTH8b0mx5gAXkJJ%2F1dKYklR0Z4H4pdKrg%2FZV2iZm3sP1tq9ZFxL0jVGRP3SA%2Bt13ylzBhdKvXbmQb2gqG0%2Bc3mhCYwjDG8WNp1lRjg5p6fWjhYPzzF6vbvthvPOQjt0l%2Br%2FspWtGlIQvHSr%2B8Bu6xWpNRoFqxxpToysFOmb8px8DNTIXbkiMcxtPc1CfbZ6ld0Lcj9vivgRFpVBr%2BbrMedxVEZxQDlUrn5rtvjJJZC6NnLv7NC7Nl6w%2BhPJmAdEFgTwlaLkkUWyf36EcRHu9evxFseYZFDigYTrgP1lRj1M9v5BkWqfD%2FF0DaKoFqrmh7w4B1ynBmmmdS%2BUg0fX5WU4XfVAgGxtyNptpDnelPbTSMTMN10yZLSX3mG65a%2F7DCZr5%2F2yXkckVZoXbfpD2NnKFenXzPPR2MKuw5bwGOqUBhovHBQ709ZFehnh%2BxQpFJJjVFvMhGtCaTDJj1%2BCcs86iGUMdj8Qhqp9rRgGkMnM5ko9ozaBfT5k1dfdam4E%2BgPtqpb9ezEJiyawI9Z%2BNusUM9CwWsuCS86ccii7CtKaTYnZ3pSoEjp6MDCyeYLkYaor%2FTvFGSzzJeuDNlxN3YS3ovjq%2FOxDqg1%2B7wlaCb0a5ZE0whl2eRU%2FwKfpqWLbjpKUCULgj&X-Amz-Signature=8f688efdda7aefe638ce7beb5b8d3ba035f9effc248e060b59f41c8326dc6986&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PCG74P6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIADSGZgZQ37YY4XCN3NF038hWktVam5HZed0VApzvgpHAiAC7U1lHJAVPUEmWOCzjgrXwGllcUt5bW1l5KmlF59RTSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMlNIwaJJhQ3MmDKQJKtwDLNfh0WrXtakl2bcd7x4x4usBXgD%2BdYmyV%2BkAj0hZEg7tH7sWPfMzVKdhSthfqLWa2XOESsOJsunGdBxKPHtGVKwCRfZRgw7L631EJ3TXuxvp7pO9Bdg70iwuF5ChfEkAA3r8VJQanpuKe7HdSti6tqcXjob66u3JbkknfmVYl4eUMlCmSpBwkbGkNheKFjvulvmTxkJnXaDAiWWicOL1Z%2FlqBocEEhZ8pkyn2b0RVnr4aMNjzWM9efLdUsfroubwLIpDpZemvYuzGPS0t0NXlZfOplEw%2BbF5umrEoSKHTkxba4xCDbD0DxN6yOwR3uRPSfPhiVfAzNqdI98L%2BTap4W1T%2FL74szfGfk2dK4hxVVzenQk8ZOJAFRuwTMD73qDr%2FQaNFSQ%2FFKqE8bVYt89htwQe%2F1Ka%2B4Ai5kln6KzLE4ajFHbRbxVjaahBbjb45fbwzI514Yjjhxm2%2F5T2U9526W4zetvCWpDhJyGH1e%2BIJLIkDha2fqIJHvNy82%2BCM6YaSP1DMDDBPILxmyMocqZ%2BCkE7dAkFbClKN6kNfYBaLhVN%2FQ5MTeT9VEz2mV5XyH%2F%2BEx%2B0DPxwgfCMSI%2FIHbUxycXrPrL5Zz7vIKKFPe32L6T7Q%2B98E1JjKOp9N2MwsLHlvAY6pgFSl3P1YniiIRe%2FfT4Alh1kxZRxoEWgG6nlxpGWFmH94U2pmhw1Fmkffh8s7%2FzOoGHhJvgC6s7A6BZm14c%2B6f7OQd6o5yh%2BAJumsgUK3vFNJx787Kg8%2FBmTj4IywN4J%2BTX%2Fz30UUWAwST6Z97SGFL8R1%2Bmdj4FdPr0ZryCRArVBsvjukbkJdkVO25hMWOHj4KIZktrNM86CKR7UaRD70hE1Ureew5XA&X-Amz-Signature=e267e4f56f54ed32280118c4ac5ce004644bd4165aa02dfacd94728fc0efad00&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZKJBI22%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCAzTzDx1V9g%2BL6Un%2BhPz2z8rLjJcl0%2BNs3KJMn9JBXewIgGRikKtNtjso%2FsxLQ5n65aumxV09pqV5fe6bcWRU3yO0q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOp%2F68NBVUS8aYP7FSrcA%2Fd2CxadL2gvx%2BlTozFsXeF9uzjMN5UPB9gnGLb24dWIcivWkQECSXfJgREdjdflOWvX0B%2FzlUFFLZHw%2BVa8YnA%2BI5g4kHT2QMCQqz92ByKuldEU6qC8uxhCROMoNj18luHkCr%2F4%2F03TB0SkFq5O4XjL%2BJ1tf%2FdxSYrdJ5QGP8kPDlmcXbtkXDaJrYBR4CQFW3wiRy%2BerwTyNmjNSmnOmDR7j90pUkrGnBA9M3CUtJAtUNMDhakY%2FccOHiTMz6z2yV4CmoMZSBvHAt4T5oLBOUw%2FQ0sN2doKVpsQu6RhcYYrWGA1C%2B3fhkyqGpOMbn6iEHrQVr62iaxlU%2FxoXwlaJo%2BGW9iWpYn6NaW7HH3gnRjPwgtDmhhWVlznGzMjw7X4Y1KXKVi%2FLvOmfVofPhB5pVW97atG4vVPgsRkROB9vN3wf4WbTA8wzVqlGr0z3E%2FLjYIq48u9Wi1fjPz1Shdy3XfrJRwS9cb2tOMt82nXWh%2BNYGtzPdKwIyii%2FMHPkHtIuJJKFGz7tTDD34e17LpZYmIY0FQG1BzZ9TrTQbhpUWpqR5eUQLG7YqbYw4Vy3Jzwx1mcDNNzbpN2t5y9SJQyrMxLO8HgPe8Yqx2Z3ulA71ZTiWULcq8GMrgZlNPlMOKw5bwGOqUBjmb0uTo0GMXXkZNLjcjr90ooxL34TcDts2mvZNe81%2ByiM8dU7R%2FVlgp%2FXsl6AIIXX%2FdA%2FQWermP8difq1rZ1SfoSYtBPwwY%2BSy6mD2PLsd4ZLjBHHhR%2Fq7xhUFYV14AhfCo57delqndZjpjxWCdKMa0b5KrxBV9U0Cb8eF9LJam4FWWWwW1w%2FjLBS4ir3ELi3M0UonteSeNZ6WDNoTOTacHwEh2s&X-Amz-Signature=5f228d9a6a88eb20e268453c335b9b647153696daf974baec58cd0735791c1bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQMTLTS4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICJEtVILpXaLyr4FTgSMZ29xzIzRZF70wZVi69DLjEQiAiAwMOFFw5C%2FYmICBPBFrsAJMXIOzIjaR2FmgOdfB81fPyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMUYBb2nZo21w7TQfdKtwDWTWAD0d55UUu1xdK1wqmgAabrmQNmGJlm7IzgCq7rhy8m3wQ%2FyCxlJaqDg%2F9Mp3iPvdAp6TONuo0kVuB9YDySwqyyhJtx8nrbIQ%2BsBlR1Q0OpeMd%2FzNWzmeXJ%2FAve6Wd0Bk0KSA0dWVqKCiIzfU%2B8YFtWl%2BI9qk2PWXSs8%2BNh4noYJ01XohqdIGlFQXpRhlc5RiibupH9mKoyYCJB5VOkMPHfrx3MXHUI9Y2wYBCwhvFurSQAr2Ho6fuodsrcvxfxyR1aYBGhhHjZKQGqizCVzWg6qcdO4mPD%2BbY%2F66aHQ8nQ0bKxSkjys5xkptFaKwUeNg1NhFvR7ZJbC2%2BjUDM%2Bx8Z%2FfyNBGSJYPx%2Bbu74zuHQTblGxfZEVyVndTfV1LHD1eV%2BwPjQTTZUwBdN22Hdju5u5ZAf9%2FhoePCebH6FNfzCkxsZmGcU7drFIhNxQU%2BSFFEuUBFYY%2FGbxkDrPlDkDY14PgAo0GUGqo4CSS6px7qdypDZoiArxRrtdkwrrJSRbJ9yVN3JvS2C5ax2GDqzxH0Hi%2Bvf434wl8k685ftvUxFFZABT5xEo6Wiz2xdbJs06nKtvf%2FR2mZQH7HZ%2Bzugz%2B%2BCx%2FGZ%2F4V9zTzGBcjppEiwHnEumNkTKPWKWZIw97DlvAY6pgHjFc%2FHwjddzxo5NJ92R9roYzXve36F1t%2B2cU2dqN0Nw5sD2CtqRbUlJnGhlQPR5uQjwb59mw8ynogt6ayOPVf%2F33%2F7IrqvnlfK3y2zIwMGzJb2pd9Vdou5g21nKpoO5KxdNkCVmb7p7sJLzGTeTik0cdJ6PHcn03o9D74V9oZh7XOHdhMZTO%2Fc2powRMAS6eTcJipTr2crg6Pas%2FgHDgQ9rqyYu8YI&X-Amz-Signature=09bd5db469ac6861667c6e587b8be05bd3bd65917527014098081abd4a990ca7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUWCIL6M%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCICJTW64bRPVz1iYLfC6c5CgWfBruIz89jhY4biobbqGqAiEAteLXKAbA3H%2B77rG%2BFVzeQfRolVPetC0za2Wwk%2FxmRHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEqrVIt6T3pR%2BiNn6yrcA0ZgsmrWl7et9qhLT88%2Bj7naXj%2F7Ko62untgTQGbu4TPf3TGWTmOfx4BtUzzk84IOH0fx6jsesVfBkLqSwyoXlv38%2B5YoMNMspVt8VZqq3cshRfJapPFEyxN9UIIrE%2B0%2FKaS0PVS5bNRmVkYS2G66ZYchaZHfcmc7h6erQ3WObINoKWtv3XWO2M0sreTaI%2BI5FFgeyyYHxBR78ajl%2FFJO2AbWILvDhs0tA2aUq9CMUXjSjiN5JUJ2ZJmouN5fK4%2FVs%2BAEkEScWXogm0KKBDy8iIPhPyaqvodSn2ItlT1xMXt8NgmLeejLAzzWmfMdnmlJM6mL2drTpURIKeVQqiSR8K2CvEl9wi4G82Jjg3wVUpH5L2slPqXrSjyD47B7lJ0l0oeTbrOOfvTBMxhUlImdXTkIbyrbNET0%2FmjhB%2BFC5zmUc%2FbGOqduQn%2FUiFqhLOQMSIn0vVMrXcMInAA%2B4r15ASLYCV%2B7SjhY88hgrNyR6oH4OmqRymapas57KkXBcZpLL7pmDIZXNKO1NeLHyC7PnR4MKsj6g%2Base63Dc%2Fzpt2QQa%2FtewMIaBCt0WxyxUFujMl58QIWdDajF%2FThV1ly4%2BZtTvBcUPBczviZRHRUVFE%2Bma5PRejPA3pFjJnyMNuw5bwGOqUBvGWBcprd27ogq%2FUavMYzAtZBb2BN8qUK5EKaoUjpQYvy0pP0a9cEufmcr%2Fb0OHGdx2J3Q3nFLVKRCz5zVMQhng7QUmI74gLh%2FVX9UjZELpyWVFbMrDVb2eNPPGDJSq%2F0A%2BCze5H4qiMvQQI68l64nGIWYX2e1wtSGMb%2F0Ripgf4yJGbUBZ1m1yBwi7%2FGHsDBUlDdrPoXCrqk%2Bskf0u%2BmTAD20Uh1&X-Amz-Signature=d013d0fc6f3afaf74b30b16e9e77992936b46e42b7b0629cf3d47d41f0789533&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4N2DZZE%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIDJ6CeDHZ4xM59LrqIXsVA4MNNJrU1jjAlBPuoECkHx%2FAiEAqoKQIzEL5pksuuL3mnGriPGNcTs7MvzShA1r6DF9M8Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOeXem39s2RFIOQFpSrcA32s5c4v3a2tPOqFkPEkkEQQa2B4zhoteF9YOs%2FWGyLXE1VQRJe2meTauYSnpX0P%2FnQL4jPW8CQOSB3W%2B5FPR6tX10uqwVlW0VDWWcrA0pjZaFWBByQh66ftx05SzdeRf7wVtl0fLFATSSLFMSBQFTdLNiH6hMHCS9HBK%2FeQ4SaSjSZbJlhxl7qBkGpwwzXkJFPWX%2FsM0bu6seNXzOEz5gdKkjbNhCx0U64tl0uliXRHWpoVTjZ4c7o4QYQfvZ7mgncvKExjEAGFRayOeKezD%2BItLmgx%2BxFijCgtYqaXsEAwxp%2FdYDtpPBUuCOt%2BXQQLFM%2F6Pkxg7NST3r0IW58vbBEtpVHysGaaP6rSo%2FTu6X4oIjRQR6akeveNbxZWHaHyF%2BULueJxGIKARdvRs8oMR9R2SIaLTBSbGkc9DyJJFhMVXJ419M%2FNTuk0tNVL3YaBra3iVmo3P4fCNzenPlvcjko1KDwWjh6cXfMKK%2Fjsu1ca2shAycPlj%2FZF06dqobYWcEhDR15UdAbfZcoeaynAkCokjYwiMYtNXqMvmUS5cRPg%2F77KRji3OSKsWAeigmQjch7CUSEbv%2FwvdA6PL1o3lrb%2B4%2F2FpJROIi%2BLiOThlPPNNWp2Xm39iyKwOTbaMPew5bwGOqUBXq0mVh8oX5x%2FsPFOOZqHvrB%2FHvUO9xr9cxzn1Y2vKimiJioq%2BIEgbWLcrWCBCquxHAAgki2tc%2BILNFZpZrA%2BH2G3qC5sDGCKFNGoUUmqUPKBjVWMoM1NgcNTjgjLDbC%2Bwt7Y2YL2C4VWwoZFAFgEkx7gqUmHObXliqiZvEnI%2BzmNg4%2FV6%2FzPxQBIhLPnipJBo%2Fd0MRIShjGHAGtMDHEzV3DpeuCR&X-Amz-Signature=2bff7d2b6c3841dbdf0f4640aa0186f415ffc404bda3fe1391f8879cf3ae298a&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWSXKUSI%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCICaVPGUq28pWYf2ic9SJiWM4Io18xJcmgRakTI012BZIAiEAs%2BVGEwzI1Rumq%2FwaUKy%2FBKT3WmlvaBD9fs7Duh7yQgMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDAfFFzxH4eau5NBCPSrcA%2FVuUqMQh0ShZuor6v92%2BBhAzdBp6mjJAfsD46hrciiQe578n9gpdmU5VRzzEJTyiXRG3zPgDDGVpG3MwXMb8Wbmdfwf%2BLcSrCSik8sRcih6Wmhx89JaW97YUc29ed%2B9I7Hy9bj31Fpy2sKi2%2F%2FKeto9hy6w5No6%2Fa67pMFapIcFpgQNwPrQR7gPwRcOMqMK2DWhhP4HauILbEcoP6Qh8u85e0d%2FJE9yJs5C7GRJ407fDTqvaw46ZE1Bbg0KGiL1taKSTHgowYkm7%2FYc8PThxYkReCxZ%2BEhtTM6IGNdyWOBf1p5sz0PQxI%2FfJ3yCmL%2F6Ksw2nMmF%2Bm5UvdeUrzb4hi%2Fq0ZCveCl3IxHe56spHI%2BFVXD5Rcu1lHRCvC1pUiOjTZBTi%2BUB1meYyHMkc%2BS3qvRWZJ2GCpCMBY41z07a0B%2B1DnCDV7nY688NH5t0qT0jGkYHrgwivhrkxy28Ms8VMOyTPTN3b1Yvlu76mj1hYZTEPBF2CaKEguIzhyEWg0nzhviHU74k2QVfFykBF%2BxEYlF7uG3Xv4K7QvGIamio2vG%2BdxUKSBVZ7Cg8jkwx5g4fWKugwqrywH5UF%2BKS0cQ3Ymq69i6NuxBfRfos4Wu0os4vpBwFUomqPUM5LzxSMPOw5bwGOqUB60u4Hv1FC28SMkBYwHec7U%2FJf6xssceHGoaEFgZaiWKLR7KdNTNb1%2FtC4QTV6L50QkzfbL22YqVXXiz9jI31cts1%2BOFNjzBz1XIsYrJVedpeja8hLl4%2BJFyxLtO0kYY2xV8aBetsz%2BtpeHjDwnQ5Epo3SzDI3bFXB4sGZ1OHvNP8JcZA%2F8B64yfbm8T3GOg1LfhKM6GFnwUTo8FfSSHIpJfwppoX&X-Amz-Signature=94ce569ed1fce336f7fd2fd30d4d213e2833437ddba6b08ecd92ffce34fb6f57&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XPUYE5S%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIEpa8t2cpnJLmfOftjZ89EPeUuJefgaPfB1b8ayY%2F2pSAiBH5RH1QsnpJmLBxFpQSkxdh6yAiIOqZFBiR6gGhN6Pkyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMkiz%2FwPG%2BrkZDqSzfKtwDCu6sCGR2AgDC5fc8j9ANb0LeFrLztKUSbCx1Mc2lc3PHMYRMzqgA8ZxAv3%2BoVR%2F%2BmjMxwDkdO64VEV%2F%2BdeO5mwoyS9IScRMftW3v4B%2BZp8GF5m23MCvUvV4kqi7Wd%2BoO9qxphZeXQpbDLi3B1naWsFifMwNcnh5qsFbZ8Iy7xK7VRBQlFkeeOekMloZdsD6%2Bb5S%2B%2Fg9OIdPTw2QwHOWUijR1maqG7UM%2FfXXR1sQWJzcVU5eYsBsmpJE41jKhX%2FT96IKACrjUu1HpHP04Bz6Z2wPN%2BKQITLOZto3WnB6tOq%2BCiDLrt%2BKpCaz%2FPZkAWfGq3YdAo7O2L9mgrgsdWeCrUu7zWXzXXko0ndv4%2BbQ7uHDZUnDlSVn8CenteDOfwC67Be3RR5srReWo3iXVoa8apAUsOVNoxh%2FYnUtWmkT%2BoilYxvWEH77Zyvi9GoLknzVALOKjL5PbNiLiA7p%2BpLmswxvesINx0bTHIxS8z8aZDVrZbL8wypOxGGCG9J2iUhmj1aCpGeXW0ic%2BU2uNhVxss5hC5Wx11Ln6BH%2BaykTaeVV4qoAeV6ZRwwL9MMA0fVJ1crmwUHnhiaSPk0F2UQ4O3Vi29qZ3mK4CV6GwB9ITpnqKNQzFfoVDN2B%2Fzmkw0rHlvAY6pgGU92pDGFIQQ6%2BOzikApAVozEOWwv5so8fkKEpphwPIO37JLadwKxM5RpMu7POr4PkxkfxXFVX9mbD12yuiM5p%2BnYF4m8fwMwhRsZbFRD%2B5ZxGn0ISzG20qjDov%2BdxcLvzcUGPV%2FcxXOdY6EUZUxMe06S%2FUPt%2FDhFUeVtGsYnnH6uBdZJCDIvwTPiAtuDHWX0psAFNGfeJuzwVfe6ceqVEIjBtkGYTt&X-Amz-Signature=b4cbd82fb9181c4bb8cb00e448392673e81b7c16bbcef35670d9dbd4b1372d17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUWCIL6M%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCICJTW64bRPVz1iYLfC6c5CgWfBruIz89jhY4biobbqGqAiEAteLXKAbA3H%2B77rG%2BFVzeQfRolVPetC0za2Wwk%2FxmRHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEqrVIt6T3pR%2BiNn6yrcA0ZgsmrWl7et9qhLT88%2Bj7naXj%2F7Ko62untgTQGbu4TPf3TGWTmOfx4BtUzzk84IOH0fx6jsesVfBkLqSwyoXlv38%2B5YoMNMspVt8VZqq3cshRfJapPFEyxN9UIIrE%2B0%2FKaS0PVS5bNRmVkYS2G66ZYchaZHfcmc7h6erQ3WObINoKWtv3XWO2M0sreTaI%2BI5FFgeyyYHxBR78ajl%2FFJO2AbWILvDhs0tA2aUq9CMUXjSjiN5JUJ2ZJmouN5fK4%2FVs%2BAEkEScWXogm0KKBDy8iIPhPyaqvodSn2ItlT1xMXt8NgmLeejLAzzWmfMdnmlJM6mL2drTpURIKeVQqiSR8K2CvEl9wi4G82Jjg3wVUpH5L2slPqXrSjyD47B7lJ0l0oeTbrOOfvTBMxhUlImdXTkIbyrbNET0%2FmjhB%2BFC5zmUc%2FbGOqduQn%2FUiFqhLOQMSIn0vVMrXcMInAA%2B4r15ASLYCV%2B7SjhY88hgrNyR6oH4OmqRymapas57KkXBcZpLL7pmDIZXNKO1NeLHyC7PnR4MKsj6g%2Base63Dc%2Fzpt2QQa%2FtewMIaBCt0WxyxUFujMl58QIWdDajF%2FThV1ly4%2BZtTvBcUPBczviZRHRUVFE%2Bma5PRejPA3pFjJnyMNuw5bwGOqUBvGWBcprd27ogq%2FUavMYzAtZBb2BN8qUK5EKaoUjpQYvy0pP0a9cEufmcr%2Fb0OHGdx2J3Q3nFLVKRCz5zVMQhng7QUmI74gLh%2FVX9UjZELpyWVFbMrDVb2eNPPGDJSq%2F0A%2BCze5H4qiMvQQI68l64nGIWYX2e1wtSGMb%2F0Ripgf4yJGbUBZ1m1yBwi7%2FGHsDBUlDdrPoXCrqk%2Bskf0u%2BmTAD20Uh1&X-Amz-Signature=59514e2680ed55679a18ef13d18f28640273ce4a36a07e04a4f2f610e81667d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QET6FPOF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICuu2dbObgRvk73GCfd8L5m4%2FMWkpvYU9gZgtcu9fKZzAiBH9EJ2idpa%2BFfOvtdQxb%2F%2F5s%2B3DzJ%2F%2FC9Q%2FvNVF9kG6ir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMFo7dCVWeNLbBRSwdKtwD5CkU43vxU9WsktGqiZ8oe7ByKHxbXKa%2FX6qKs9EdXPe1Ki3Uu37WwSY5o%2BGXsB0HmaZU0lNQikM%2BcNU1zRpySWhAGnl7MitHGE6Zm4VM8axFVOhKY4YWIOG%2BF0SIO1%2Fcvf6o3Za4Sx20fDZ5sS8exztvLxlaq7XgJtkmWG60VwbUdveMWMkUIUIAdPWl9MtU8wSyLUpqZe1U%2BkO%2B1JdT6hKaOTnqAJ8GzxyiozIIQ17XzD9%2FXXjD62EbHMZM1wfZ9E84Ws0qEUs5flLnDv9XOGXMCpOKxBnE8JhqoSYbWqabT%2BYT5Q7kq8LmpycXgaSVN985zrQdTbMaL0HuDZls1ScCY1NXrCy6AxaR8t7NZdr6QPGWy0ZLao1suLAzgC2qhLC%2B18ApvqJMHjb19lNldHN34RfPa2jxNnJ3xegenrl4%2F5157ZmjXZDVyIbAOF%2FKk7lNOZUPLyNY2PU9DGm2vGEq6Al8l5k48bMNKHMnbewgvtaRq6c%2BCVV5xbaxJqQd5mPkrAU6f0glBlPdEjpzPzujlzFO%2BQrCBPW7NrR73Y6UoYFXJlv296JRROXaVpZfNC1wRqNbvNggzvZTQrx7P2PufiwhimUhR6PQ%2BI9uSFCAPk9rc%2FyCIiuivkUwqbDlvAY6pgF4i6ZS7kReLijPx38zq04rNGQFlpiE9m8UdnBFDT2nA%2BLGoW%2Fu2IrLaMbB90VakO8hDUisjnAm%2BgsklyVXy4W%2F3RoqWkq5uI8tT%2FETJL%2BcPsJInWx73e1YAxlDZOyrWty3TOpp8X8hqwwKyHJ3y4kKlByUVNrHZedEkc3Z3doecp%2Fz6tfxJyYK5ZrZ1K5X9w0v3V70477DbGxQwVoyfbyHGiAfbr2L&X-Amz-Signature=a1493f17cf9e0c01c4bd33afa69c7fbaf7a04e11ba6c5201f495571c60bda1a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QET6FPOF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCICuu2dbObgRvk73GCfd8L5m4%2FMWkpvYU9gZgtcu9fKZzAiBH9EJ2idpa%2BFfOvtdQxb%2F%2F5s%2B3DzJ%2F%2FC9Q%2FvNVF9kG6ir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMFo7dCVWeNLbBRSwdKtwD5CkU43vxU9WsktGqiZ8oe7ByKHxbXKa%2FX6qKs9EdXPe1Ki3Uu37WwSY5o%2BGXsB0HmaZU0lNQikM%2BcNU1zRpySWhAGnl7MitHGE6Zm4VM8axFVOhKY4YWIOG%2BF0SIO1%2Fcvf6o3Za4Sx20fDZ5sS8exztvLxlaq7XgJtkmWG60VwbUdveMWMkUIUIAdPWl9MtU8wSyLUpqZe1U%2BkO%2B1JdT6hKaOTnqAJ8GzxyiozIIQ17XzD9%2FXXjD62EbHMZM1wfZ9E84Ws0qEUs5flLnDv9XOGXMCpOKxBnE8JhqoSYbWqabT%2BYT5Q7kq8LmpycXgaSVN985zrQdTbMaL0HuDZls1ScCY1NXrCy6AxaR8t7NZdr6QPGWy0ZLao1suLAzgC2qhLC%2B18ApvqJMHjb19lNldHN34RfPa2jxNnJ3xegenrl4%2F5157ZmjXZDVyIbAOF%2FKk7lNOZUPLyNY2PU9DGm2vGEq6Al8l5k48bMNKHMnbewgvtaRq6c%2BCVV5xbaxJqQd5mPkrAU6f0glBlPdEjpzPzujlzFO%2BQrCBPW7NrR73Y6UoYFXJlv296JRROXaVpZfNC1wRqNbvNggzvZTQrx7P2PufiwhimUhR6PQ%2BI9uSFCAPk9rc%2FyCIiuivkUwqbDlvAY6pgF4i6ZS7kReLijPx38zq04rNGQFlpiE9m8UdnBFDT2nA%2BLGoW%2Fu2IrLaMbB90VakO8hDUisjnAm%2BgsklyVXy4W%2F3RoqWkq5uI8tT%2FETJL%2BcPsJInWx73e1YAxlDZOyrWty3TOpp8X8hqwwKyHJ3y4kKlByUVNrHZedEkc3Z3doecp%2Fz6tfxJyYK5ZrZ1K5X9w0v3V70477DbGxQwVoyfbyHGiAfbr2L&X-Amz-Signature=4d4ba2fefb44129896ee1c88979b5b8992bff87d8d7edac156647b76dfae9345&X-Amz-SignedHeaders=host&x-id=GetObject)
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