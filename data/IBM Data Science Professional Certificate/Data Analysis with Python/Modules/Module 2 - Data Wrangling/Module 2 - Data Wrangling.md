

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWUCXSPT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIEp%2BAsEcGn7R2CD1Tpc7QUT2%2FXnlpEa%2FWaqD5AZ%2F7UBcAiBqemGbNqrtYA9IMnB59MI9xmBSTylHqin7vPyw%2FcPUkir%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMQTI28sLC1XHHFaISKtwDuAW9p0m%2BqP8Ojpq8wi5QiCJkMH1McSx1zIwZQUMUlQmITEEg8JQ5H7n6P2SJvA%2B1m7%2BJlUwKaR3iGRpJ%2F2I3wwHdDcg1lETohDbjeibgG4WNEZhs8XxWe4iNCaMA1YI%2BM6pewxQP4BLAJTuQsxZCzXgfVRirWux9a3jjWLrqlhnGANAeCux%2BN8DX0FDdwCT6yWqtgahXEVkkiCwKlebRyD7r5vhs8jWDeZR9URhWAv04ltCzpPrpMFBfMnbOXbsfZ5elPG0IrLOtmw8rSY5Xgm8eOAJluCfmzmCpNI1V2YbER1%2FJLw03%2Fs8YxtwYt2%2FFnWh3VsgDjRiFwSrvO8Pb2Qj6%2Bwe0CBBrQYm%2F4BhXkfUf0%2Fnw3estwz%2BXaAsNbA4Ea5%2FU5Bi7jkgZJUIRmOQSplT98zQRrskNfu4bWuMQDKh4lJxHmHVU2gX28IeNwyN1yIgpHly4UCzL802rJW7uR8x4008WHiMP%2Fx12JEwLiaQWRjw8mwecqQ3VtVh528bXTgEcEteqV0DPD%2F7ScaohbHLP%2FuawH8%2BJukZXzuuTxE%2Fphmf0BTkyKphmsydjvMJwHvzDyDehBCkwDaHc4%2Bfqrn5k9GaRx91%2F029ww0etgU6vHGyDIZ4G5alIaFIwvN%2BQvQY6pgF5h9BYnoJaRG83iEhuKQGLZKbtCyMO6rj0YknGkvCv5YFNM9iSxaV6utbkLuR3vWRUCmlI6u322%2BmEIz7IddROACB6%2FstOjzmhJXgMmQumhpBZ6V705Gc%2BVRHOmzhT%2FfjAcrfAI76kVmRV2RB5Yw4Kw6ww46rniELVgYUaZULjmms2720J2SDNOMu2Vh1CREruxNNKPwRDbBSf9GBi2Q%2BtexqEbU%2Bv&X-Amz-Signature=451313d5ffeab04306b3c4c6df25e7d35176e13c30ba1c6fce71c8a7c4a0eaa0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UQWQOGC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQD77c3HhKA6xKsIBHj7hOHlQPtxyp7MLOdaYPmrCak2mgIhAI3BoMCspQ%2FTXGopnwztD4fvdZqTTSOh%2BI%2FFpPjuj%2BNYKv8DCFUQABoMNjM3NDIzMTgzODA1Igx9hXaKYrI0Rv9seLQq3AMX40pYYmIw7eS9MDHT4kVMnMHejtiidfQfwWMDNVcBc6L3bNhAw69Lcp8ZymfIQkYfSd2Qfw7JkEQ989QGatED5oR1YQoA9lsIEz8adzT%2FjMJlcnV3PVJMULx7btmWDuUcG%2B3iESByvQbDCwZfbksSkI9q9Pg1wsDJnY9wtcVCZHnCFhFDZXEDoIZcQ0xf%2B1ntbtUepvv2mLpQf4YLIKYU0Vj5QUXFVx1qo7vZ4WZy8k6RwnfQqQwMVfyKc4Q1tNZgph0vQB029qMQTFKREFBBlkTGCJry2QkKrUsneDxliJgVcmknyRCBg%2BCEKjbveZPlO9CtWiGDIdkrDBMt2O115BjNjjTlTLxKX9tB4nSg75DpReevgYo8n7iEm9Zf2Zi7mCoobMPNM392roEWfcvBGt5aRJ61bg7pNJRcxGnSrs76Tqyi7aUk9kDY%2F50%2BDHCPSdoqiDBKA9QBWrZno7tYdCkVm74WZrP9D8KzvdqFJfVVETsDVNBdSNKCLp7T%2FQMGjMzSLa%2FnltM7HSxwD%2Bu3lLy1fMYwloqCzpaue%2BqGDRfvVZMWxMOW6s6%2BJJNKZybJEaOVpfHjHFifYKbUM96njRnmvagCbXpW0OauoPvKXKjSVLxNrBwJNsNb0zDo35C9BjqkAR9ERhdeOWXeNZExOpOwUMaSDJpVbpQbPewWeipLHCIVufjbB03MlFvHSOYTagypKJVBlmjSMEyTDVXtsHOxfCnHYlHQdt1g0DWoN80%2BwLAuNjTP1ldtQyegkvdTmTwr%2BJ1vkPT014RuijDkNnmg8rkQclIrSVlGNNVpUnumRmmqVTvDtG6MDtnww5b8wc4YcBP1rfulBE5c7paX7ck0x%2BqDTKDs&X-Amz-Signature=7f2e86a225c1995bd1b1904bbd1cafc1cd6739860d3bb4009fe6fc155c6e2c49&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBWP4TST%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIAeVdhjYUryJwc3%2F5QD0flHkE0eVfQysT7320ZNY2IDFAiAaTq%2FBNEnmXyu4%2FFCwTSngJRNvPO0bC0TUYgO59nxeUir%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMaNwAMDj5NDKMfp9eKtwDZ8QFt9MlcxctcwEAVC6B1Qo8vRcVkfL2D%2FN09lP3%2FKwHIVFNqq7b08dXqlGDGjst3hqwCbB1gtuEPhVY44l3VrU3zlI0Ve0NACi3SU76nqyNw5X70sBqW3vK3mN1nlUPup2C7WDQ57A9KvnFaARO%2FiTD6H7bVLeWIRoeCxkxxMMxNkuXJPedZsU%2FVwTSIcK5Frl4Y0X7G%2FGZk%2FZ4S8sRnl63zPzlv%2FYo0BH7g2rWlCICUC8I4zzF8PMuWBXSe31BUueb5A1fImjf11G4KhCiCKUNUNWNHA%2FVlkNRu42P%2BliPNVtzuJz9umWk9FsCIUXbu8ciIwEPstHZRkS%2BRGXtHvvzyipBpqXiC2aWsEH5N2jwoD2GJAiHHUpi6RpWcGankDUXvRZn4D6wRxaVBdfp7nL%2BDitv4WLYQT0mXIeD8u7khL7K2Hg1zhDGouOYHKCUR7B6QKdj6sd37RaHJ%2Fk334yfBAxhRB4gnkPyYFE%2FCepH2I6DEtnHZyBH%2BB0WJrmd6xrq3PObpu0kInhXm4Yk4LVwIyc2mc%2F2yIfptVboPGDTtTG%2FcA2Q1JrW4%2FuWVhw4gzAWVFDyoe8nPAOkTfJ%2B6gxpcCniWtZ02dGfw1YkwO5y6Z8sCBLJayU%2FG1kw6t%2BQvQY6pgFndM4ThEbOvhv1OtZT9PI8m7cpENK%2BfkeduTycIqktq%2Fgt4p3tNns0W7GHReOLT4RrhlAD2rVuEy%2B%2FDzlzA%2F9kZmev81%2F83oEnwzzl3MM02qzpb5BtOSRdFGReBo%2Fl7iz02hKSutMu6TzvCVPI7rVIYwRbtDoo0EFEYGsIta6mPq6dOfxu7zgQ0sbPBRgSNUJKrwrZYFRjRuEXt1Bn9yuifRC2TijQ&X-Amz-Signature=2f0e7d7f44c80c336f0aa83effa457dcbbde7c8ceda9b920d7b2a15ade26afe5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVK5CY5Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCqr4FwHS759%2FSxly4lWhOqSnE2xsgd%2BdWroIxTVn%2FiLAIhAJPBi%2F7mmeYdYUjhJhNPymsBbU955nmy8CHwXIHnB%2FNJKv8DCFUQABoMNjM3NDIzMTgzODA1Igxu9xE7%2F4mvP8iwiGQq3AP3djDZpx7tjs1u9Kuo5ZeCGIMp0%2FoGWS%2B1r7DPQ5hTshnDPri9FxCWliPb39yztjowYuVP5ZIzex6fGJn2M3ugzVlpvyAL%2Fp49RUIJKotow%2FML5R5euFe1MYiMZCKtxxhjTDtv%2B2%2B%2FSdqy3Q55Aq%2B%2FII9hgdreh14LlbOtlbsS%2FH8NvPc7imSnll9wDucLD3Gde%2BUguivuPir44oVOWBIXYKta4EEUE4na%2Fs32qcOwZzgct2OXmVeUG3GKp1a8FZ7DP%2Bkt8L91OftXlGR%2BpozWK4H4FBmCaXXeBPiBkRmaFId5fwCK%2Fsf2BNumhN%2FayIAMtwsSlwoZy4NhBfns%2FuBUXjdJFUrQs5Ju4I4E4Z5DF%2BkR%2BwwcvBsORVLDimP5gRUCflXB8YTtKEk5yKgYkv4mfgH1Exa3lqa%2BlANiz%2BeABKME2bzI2iOuhOOXz6xw%2FmCpzJjcyYixOMobM1OuK5i%2B60f0blcRHClo9Jj8YTYaQhDIPXfhMfW4aZH93tr0vHnqsura%2BVIuqQhOAskXrtwEJdMeiyNWf6o2oYmlLTrF8p9u52LXcjlgHexlG2XAeNElG9fRpaC2iUq1GSgmla5TeDpDMg8JKUmrET8vov%2FA9MB23K0FVNHqLJU%2FYjCs4JC9BjqkAayF4pTUoxHfq0tfB2J1%2FoUYOcbMBzlGYXM8%2FHAHZiWTtYqnsyJTjH9FGCCHV%2BEXZEagijMYDGqthPZln1OWjtOpiUhnqYVHwNjjg%2FdSJ6nJsxH5vQnumN91blbKYRttvciDuUXbD%2BSe%2BdTT9eKTssLe7SzwRnHJTELxhCgI5TsRCJP%2FWMjLv%2F9DRa1IeEiivSK2SFW9Ldyy%2BJqOTps76EUeupOV&X-Amz-Signature=dcb9f2b79bafeb239e037a5413105b20847cfc30615daf6a5c0ea6f0fa6ae231&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PL7PAOJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIBXn3XcpvZqYXLe3PIYifmDIADfBVelKTtQxmWPRqGwFAiEA76TtJdyrmEkSFLWoQVbpbEV9CT0HCAKQuStypz%2FNdisq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDCxg539WVfj%2FCTWeSircA4pOyWMRbVjzTFMz%2B5jkoExcBn81PHmamTHSkNfjXLR%2FNcBKoA6M6BhBbhrqZLa3hTUdap6gZTA%2Fu%2B0Q1JQa%2FMjxfOKQmfL50HdKSeNKBtuIm5595CMuSJIRnsOC9UMukU2bx%2B7YyWE%2FRyEnsXSUDFkuWUGaTyvk7e4HCeUnxQP4aduMMo2nB%2BK8zaWjPi4JAgxrXqvtBYAx9wKsQ583YthFUGTnS%2FHEgjQO9Dvoaoa9gAuzhKx4%2FZDTb4nnFn0YYnz61gzcwWZgQyA4Ibz4TYKz0GZyDrWR2Z7O3jXQnLdgovdEVFzct714O%2BM%2BW1Sf8DHUNWX6ijnvKaFfSSocYjJyMKU10vK9xBx%2FfrLiirm64EtAbU5fqVGdivNgC%2FmNjOlviI0dEQDkJhbbp67RqMD3KSPTIjSP6F74rcZJwehHviddiTlQXNB3f1g1Jn9b%2F38BrC8cqj263SJnD8z2ledGxacvCcbVHadTiRhE%2FZ8eJEmmirph4Qw8c94nmq2U8zPM9g8SvjGtlGnczBmrjnyh5laO32YDYBEQYuYLC4sgik%2BZcS4dODymEi0Bl5W5YyCvIFk9Nh7l2Qp373WwZ4FY8q6EU6GCmdblpzc5y2sGnw1CePwo4ZX2WGRbMMnfkL0GOqUB99DqFWH%2BTs0Drm6fo5xUqS9YY7bOjAA10qHaEc6reMSdk8q8nM2ADzch%2B6p9afZ87d6%2BHRtEv6N2LKdY3oSOoZiwEtpw9Er4twp5MP%2FzcbQJrlro2UCrBDi9paA8%2B6mc8e9oK0Nv2szFdzSq0c5jykGgJLzko8OqdpS5EWamEmxTcagYeEa4IWlQWWJjGvvialrLcrjm1U3eMS3W4udRoSS8BGub&X-Amz-Signature=3b089ba5f49c23189c08c4c02155651b9a18ca14194e2a5add3d8e274f7ab7f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBMUYVA4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIHOls9MvN9S7tkcX%2FN3Bd91Ynvk9crFK4rYTlphsAVAGAiAef%2BECRuGkp9p2Dyk2gdQi9uO4N9pEx7t%2Fv0KVjEvmqyr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMsQrRQXdxlSeLwoDmKtwDhp9s%2BQshxiqgQeDIVvmKIRUfRWR7OhkPmzfiD45If2ixGTwvbzdYKqoEELcLZSTauZrM7EzfxmOlc5PFEtE%2FUm0vkHIVC%2BZJ8mTAt7slvz7s%2FITXulrmp%2FsivQoYxSjRW7KUZtDRVHypdJClJgjmOfR4wql61EEEN97LB9hReK%2FWZZAxCdGFhpqlmz4z%2BzZoGuMwk0Wu3rbZEqqZmZOllo3Kk4haLw%2FyRYqCYNCIimpT5dr9eSms%2FLUE6YZL%2BhdDjNtixRTPbZ3gKcT01C8ilweGCFntLZgmJV%2FMds%2FJCd28lLS9V4OP1n2mQ0TD7WfgNAw%2B6kopZfTUG4t0nFa2KTi6VWlB0EiDfHVjkv8poxO%2FOD0f5ayTHnq6rXm5mlVXbqTmOIWCAgZZ6XRzqyz9Pzb202cNpnWDruUC56pUrSO7Ri47AGC10dOxLYlrAkD9Tl1nsiXPxtXhLs6iQjNAGXq6plPNPfhFSn4cNhmZDeNBwr6qjU18%2FW30mJk3MgSFmURWDYYSu5Q1rK2P2elJZqwzRQYEDvAwxLXIFB09sdwBBYA0tGbXr7P9F%2BDVajBAmGHfpPhDotDqrwZBArIhO2wEwRwd%2FPcOkg4AH9VYZMgpG9f9zMZXRcpTEu8wr%2BCQvQY6pgF%2F8%2BYK2a8ViSP5%2F3xR7IS6NZiK%2FrredTrghClB3d%2Fn0tJGpOuw6RHBpRsVBMhCp4Fg8jsyoIYc99%2FRvKzs770thp61GEwwamzuxpJDLIRjZ6Qx%2FErYklyFnmYJvt9FlmAhGERQFtnYDGNnIhsT17HVQnS3F5%2BYJnr7wB8els2qjxrkUvg7kPNBVpib3MlXYbnO1Kh9gz7g7%2FWS%2FPQyMbLDS3fxM%2Fs2&X-Amz-Signature=18e9019f19e739b1d30cadd9fd44f96ebe640ff3f24626a1e4b7543cd2b17583&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466675VVPR4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCK%2B%2F%2BGf4oHchmBoBAViADEFF%2FJZhvghbKXMxFFVLvlcQIhAN0uSssXLjMk5dd40Cfm1unoaHFreM2RlbsLKlh9CztTKv8DCFUQABoMNjM3NDIzMTgzODA1Igwm4tgcf8le%2B28xQ0kq3AO%2FV%2FgVoNBMaPJyLyWeN1zdmkyerUC1HCBu4os0mAFW6NplSxEwCvsmccfIQJWQKpcSKvQ8Oa%2BueBjHD99EtrT1JWCX32u9wfu283oIjagiA03ETZYCQoNvU3WEfH3VoazbeJLHfEf8mBgvM7DGZKMbu%2F7MuSVWRg%2BgF7qwjbKmgjw7xhiAxp6id2EpcLeGsdQEjL3c8T9QjML9%2Foh%2BZ7lQRjTs5So5EA75sRx3gz%2FeeGlQQMfJrv9DZtob%2FueW4HMjP6pa6fPns5yTexgi%2FxuRfN2KFGQXuqquS5nxrwBGalHTN5A9FI%2BP2HUBfJbRZeDxbPSYUjDxN1kTUVhwudGDCrc5RiwjQYVBOBSmUyCbq7c9wdEKCeYBD494ZeO9f7MDT%2BscDFn8XUJQgPagUFpY178LN2BBARr1zaYIZcn%2F5tW0WKgenuKwkaI6yKaWgwry8PV746ihpedVV7eSXBvWH2u3oIyuaOdcQ%2FMeVBO35vUrE20%2F%2BjIUk1lqdHpzoiItay6zypR5HV7JSvEan2y88aVl4T7LbXTRnZwuME0XvfGBYsgiFf18mqa2g1iwxn4Q6YxoZmkpAbc3rm%2B5plwnj6A%2FS9dnqwWX6e0MYQTzcjreelNqEipBl2v5pDDY35C9BjqkAcofu4aRYoxwJw0eupHoRMUzE8byTSxgvObMVwXd64NAXWnvh6OfrA%2FmY614Q3%2BDnC3uFGI4UF6tAaab8n8phQa1KthJZzufhTLVG80KmslV%2BkAy4bGhnGnS8HPkEe2wnAL6D4d8BT5wnZfstT4R8LlQ4iOMefngZQ03y%2BwUAVCbbVTDQJe0%2B1AXyA4z0nOG86GY%2F%2FGjXaDneFccVJjDs50PQEro&X-Amz-Signature=a4aaae10e78d03066bd63e36915c8f80428ccb581da79acc336e50678f400ea1&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTVDZRZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQDBISLqWrBfIEJQdb92lAVAVJ%2F%2B56nQatgKfDB83P5VpgIhAOwN2Fb0W2Cb0xsyfmTTYHexsVvFWsrEaooRDhMmdGQRKv8DCFUQABoMNjM3NDIzMTgzODA1IgwjkbLscSN1TyBOv3Qq3AOeO3BNbdTBF48JhP4CCuaRe%2B%2BkloP3Vra%2B%2BoDUmf%2Bx%2FeWXSsMsZHZ40zJJ%2BwPYMVKqyVr07KMWZuzdwstWZDLJ8qs0HwrqkK%2FfqjnXKkcr48J71isMwm6H7wau%2Bj7Uo3Hr5PRo%2FEtnP3iSnMpfaXXWWwOgosffZJyInUvjL6HNrSz5%2BM95YA9AjtCI2Sz6csE40YUBwOxybSckAlvxQ9Dpdsu4D7uFx56GCAlhs9yUZhgGE19%2Fd5QXkXqaFD%2F70wjKlL%2FcSXmb%2FgD0q%2B5S7LMrvYz6%2FR89vKg1xqktH8jamSAMe0KwofgQ6m8ggUT5bSTPpAdyGvY%2Fl2nCM%2FXDlOmH3k1W2gxFAclllWeYt8iIQP1XsTfW5gs%2BG5iGEIoWWiuyV31kUoF13VWa0GheePp8dzI6bGK7AaFnl8VbEEPEbAaq0YNuAo%2BuqiNb0a7DMehMzRJ5YJM7luVkQgx1%2FP1orqjhOtvECZk3Zqy9%2BRLc8wfCVJhRnT2XeXSf1mYQX0Ku9eiaP5aa8VuEoVnNX8VUjzxhA3FvCrxpMRJO2swbXXmldvoez6A1nAx3wx%2BtcnRVYeA8tZ36wT1yBNE8CNzQXQQOX8gdda3ENMJ6zELjCsJtr8hK5E%2FdPeCv8jDr35C9BjqkAQOJFgtZwj2%2F%2F6M4dne2rlCmGLsCpXp9bSa1Bbvckcr3An5dmpix4cwnb8CffT2%2BrGHg4J5eaqzWvUMDIF1FcD22tCF3qFWhzzwuGdxLqAHTiOnFrIyrXsZfPDscafnaEHlzyqSQNBpxGZjY%2F9oj67AX%2F%2FGqMv8KNf%2BxDIxpsmBrqyNyqNwHQHTaSqPb6CtbVMC9A7y876XwJrBfXQIJUq%2F5Nq%2FQ&X-Amz-Signature=9a61b36a75483e3c0b8dcd59a2e5d5c365b30f15d06d30befef3668a4c7d1176&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PL7PAOJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIBXn3XcpvZqYXLe3PIYifmDIADfBVelKTtQxmWPRqGwFAiEA76TtJdyrmEkSFLWoQVbpbEV9CT0HCAKQuStypz%2FNdisq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDCxg539WVfj%2FCTWeSircA4pOyWMRbVjzTFMz%2B5jkoExcBn81PHmamTHSkNfjXLR%2FNcBKoA6M6BhBbhrqZLa3hTUdap6gZTA%2Fu%2B0Q1JQa%2FMjxfOKQmfL50HdKSeNKBtuIm5595CMuSJIRnsOC9UMukU2bx%2B7YyWE%2FRyEnsXSUDFkuWUGaTyvk7e4HCeUnxQP4aduMMo2nB%2BK8zaWjPi4JAgxrXqvtBYAx9wKsQ583YthFUGTnS%2FHEgjQO9Dvoaoa9gAuzhKx4%2FZDTb4nnFn0YYnz61gzcwWZgQyA4Ibz4TYKz0GZyDrWR2Z7O3jXQnLdgovdEVFzct714O%2BM%2BW1Sf8DHUNWX6ijnvKaFfSSocYjJyMKU10vK9xBx%2FfrLiirm64EtAbU5fqVGdivNgC%2FmNjOlviI0dEQDkJhbbp67RqMD3KSPTIjSP6F74rcZJwehHviddiTlQXNB3f1g1Jn9b%2F38BrC8cqj263SJnD8z2ledGxacvCcbVHadTiRhE%2FZ8eJEmmirph4Qw8c94nmq2U8zPM9g8SvjGtlGnczBmrjnyh5laO32YDYBEQYuYLC4sgik%2BZcS4dODymEi0Bl5W5YyCvIFk9Nh7l2Qp373WwZ4FY8q6EU6GCmdblpzc5y2sGnw1CePwo4ZX2WGRbMMnfkL0GOqUB99DqFWH%2BTs0Drm6fo5xUqS9YY7bOjAA10qHaEc6reMSdk8q8nM2ADzch%2B6p9afZ87d6%2BHRtEv6N2LKdY3oSOoZiwEtpw9Er4twp5MP%2FzcbQJrlro2UCrBDi9paA8%2B6mc8e9oK0Nv2szFdzSq0c5jykGgJLzko8OqdpS5EWamEmxTcagYeEa4IWlQWWJjGvvialrLcrjm1U3eMS3W4udRoSS8BGub&X-Amz-Signature=e8c5e81b01e2baaa2ecb5a0c0c1f95e25da09069d7141a329dd0583c20abaa6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA3LWHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIGKRS2sGBp%2FUdiVzG9JMu0xJYMEu5bvI7gQQ%2FGgYh81uAiEA91TlvzTyUIPt2Sa65tWERUoHSAt0o8g4YXAfdcqI4IEq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDKps0ZS0O0hQ4bgNSCrcA3d5tH7ODU3h52LYGSTDfPDBubKIUTcScbhjarV4M9XU0EWwT8GuxOA8Askdyc9V66bRB0RawfkRrJYCe7MgIn1R3N7XhAWKsiAQ9JokUMLAK5XRDr8lGPWN8faTReje9S4DfltEMjGRHkdVWGxGqd%2F1HghrR9HhFuJ3lDYeCHtXxNIzfke2NOjOlX3evz9PKocbsPnhX8o19hjMu8TFaXZHMttfUCGzHo4sg5iLg1EH3UnCZEHMVvBAc4jHY%2FHDFCCgmH%2BO0kZnu1A8ptoHxBNOupvwEWofwP90zH1OaqCZPyK8%2BPLBWKaxsVgNayAlE2804I7as5%2F7HE1gKP8CzVFqLaM5DD8EESXCoGJUjpReNaEVeLzDlhc88EIflODx3uL8HTD%2FH%2Fd8z3mB0xp%2B%2F8euh8e7lXBSJ9tv3TIYLgnOZFEEXCWjytQBSXhBhHtFwjP69De2oymAGO9nzFZALfpP1LzNz9%2BFrx%2BFi4pddaUujg91v6l3fv1OxC6Ms2mfnx8PBmT2c1fkzG8e0DBOSwXmt7cvMF1ZqmDgXFOtmbXmimvL9gntqXg6XpcyIkSDHrcSVsMMNf5v%2FYUfaoFPwKu35jON%2BHI48v7r6T0y7Mdo9NuFVu7wEbrIwu0bMOHfkL0GOqUBFbeWTFFjAMMhFao%2FORVZ4J6TuHMXsNUnBpAWiOvAoagH%2FuFAHULopaEnMLtPmv%2Fhmpsf8dLY8U0DGmHVkwh8avv4Oox%2Foo16aalHdmIztYaPLg1jMIeFklnTI%2F8lMzmdpIPq1hFujFWu6dT3kd%2B2IehJRb9flHAxefE98WDfLWZlKBLdkxZuFEwNXGw7gXO1Nim04NgHnEp0NNQxbz2I%2BTvu%2F9S7&X-Amz-Signature=d33dcad1d3f24a3f26a1c5e151e1c4baeb8c16dabaa11bd108ea06c5e8e639d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA3LWHS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIGKRS2sGBp%2FUdiVzG9JMu0xJYMEu5bvI7gQQ%2FGgYh81uAiEA91TlvzTyUIPt2Sa65tWERUoHSAt0o8g4YXAfdcqI4IEq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDKps0ZS0O0hQ4bgNSCrcA3d5tH7ODU3h52LYGSTDfPDBubKIUTcScbhjarV4M9XU0EWwT8GuxOA8Askdyc9V66bRB0RawfkRrJYCe7MgIn1R3N7XhAWKsiAQ9JokUMLAK5XRDr8lGPWN8faTReje9S4DfltEMjGRHkdVWGxGqd%2F1HghrR9HhFuJ3lDYeCHtXxNIzfke2NOjOlX3evz9PKocbsPnhX8o19hjMu8TFaXZHMttfUCGzHo4sg5iLg1EH3UnCZEHMVvBAc4jHY%2FHDFCCgmH%2BO0kZnu1A8ptoHxBNOupvwEWofwP90zH1OaqCZPyK8%2BPLBWKaxsVgNayAlE2804I7as5%2F7HE1gKP8CzVFqLaM5DD8EESXCoGJUjpReNaEVeLzDlhc88EIflODx3uL8HTD%2FH%2Fd8z3mB0xp%2B%2F8euh8e7lXBSJ9tv3TIYLgnOZFEEXCWjytQBSXhBhHtFwjP69De2oymAGO9nzFZALfpP1LzNz9%2BFrx%2BFi4pddaUujg91v6l3fv1OxC6Ms2mfnx8PBmT2c1fkzG8e0DBOSwXmt7cvMF1ZqmDgXFOtmbXmimvL9gntqXg6XpcyIkSDHrcSVsMMNf5v%2FYUfaoFPwKu35jON%2BHI48v7r6T0y7Mdo9NuFVu7wEbrIwu0bMOHfkL0GOqUBFbeWTFFjAMMhFao%2FORVZ4J6TuHMXsNUnBpAWiOvAoagH%2FuFAHULopaEnMLtPmv%2Fhmpsf8dLY8U0DGmHVkwh8avv4Oox%2Foo16aalHdmIztYaPLg1jMIeFklnTI%2F8lMzmdpIPq1hFujFWu6dT3kd%2B2IehJRb9flHAxefE98WDfLWZlKBLdkxZuFEwNXGw7gXO1Nim04NgHnEp0NNQxbz2I%2BTvu%2F9S7&X-Amz-Signature=a8853fc4c0ff7209eabd9bdf211d9c0737cdcafffe622a451b72056e7d36f780&X-Amz-SignedHeaders=host&x-id=GetObject)
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