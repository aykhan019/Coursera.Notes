

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMBPSOQS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFqZM2ItIIGmU%2BySuf6RPFly1gjG2jMWj8XDYHPRvXqXAiAK5nkRU4eiPRB1jSyjwWzcSTH1Lv6iAvXgGztcNRblwCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPVrmaqPiAq3mY58MKtwDVPtOvQgygP3WnqbKey30Q4WeF%2Bc44tCjJeWPJs8XKszD8SR6hb6AGGseOUnSTJHutZI6L%2BwFsyvE%2F1MibqCvQK%2FJhuHL2EzLGHUlXftZDyOnlS28nhhnmrFGtpLOBqkpmMAdn%2FzVTySzNuc6gYqPfBGeiYMjWb9gYPW5WJ%2FzT9V9sbMulzR%2Fzs7ibmlwHfkhNvJLp0sGn5CXpJfT%2FcVkpR2f44Bp5zI9YvYjc7VQR7jlQXGagPecxJrL%2BZ%2FDopgnT8Fsom0QzfWjc0CBj%2BMZeXwfXcbeekKa7En8h6sfjXnAtqwzdm5NIUQ4xhw6vUwtdUf2aZPdcpgMyPMhYAMM3iN1d5RI2fbnvGe1eyaisAVs2urfKG67IsXci6B2%2Fr2mAvirhVmVAD0Isw%2BFdANrMTNcPYp7tss9KxVEYRKiCKxjzfM8YpTKlX23%2BN1e%2Fvg5dHlRxtvUXg1ooxso6aK9DGXhBsuIOLoDVq%2FvcKtl1n7iGbEavOhUK5Co23ws%2BfJRkqMFMRn2iY9g0obarK9Q%2FTqQn7ahWJjFjuM879r7Bpix0kvzahWKxBiDBSdH%2BtVKcnehngrmO67HtgC%2FHsPwJ31yx0i8JCysQ97f6PN4ELAcXPtYZposvIg9KvgwyNDwvAY6pgGz3Jnk0t50wvI%2B4KsoLUprWIdk%2F33a1nQr5JZZ%2F9RfZhcUW7dMOdlm9yhDoLCJChKT1MpVtqIamG9wlATZYkWwlAgLg4VWjEKyuNHG5ePbkBDR5%2F5lqwCIXACQVyH2gyucUDjoQ437TVVs98oMBQyz%2BvMyhPqRP87WfVyFhMUaS6uQ31BjVpCqR0seefUWvYFJrDyGUrrrDAiUbCNpTPdlRwYLqcYM&X-Amz-Signature=7356ba7b92c63e1e54ec89da092ea1d00edcc389b36dc9853d83cd6fd0d7958f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKYBZZC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA049jXOJAbAUyzylSaPONt8rac7nVZYkNkDKRVbswo4AiAeOLQwUuLlVaB3c8qhA1WB3g7mDlAr8MFiuQJAZkb6nCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoJ1KiKzaAXwhg4bcKtwDPP0b8qmZfR1GW0cG%2F%2FYB8QHGvci8IAo7ViLqibUschx5Vd5VKc7K8ySOwBSrTkkefCVfVNpVMb16vZ2%2Bp9tJ7TSykYq5riWLh%2FA%2F%2F699tIiGImSZaa2kK6s2Wr3QwT4vKA2lR7P%2FZpBeWwLeoESOcxZp4eRazIKpnRoQtYDKc5U%2FCBwRP0O1WeNPn256I8Di2yX6zR5dF7SGuZwUKOGoCxl%2FU0ZBJqHj2zCGQ5%2FxNsuVvlXPkfgwiY8SXGYA8Bw0A6nxissDtaTUTQX0OcSCeq%2BXZ4J7cjIxR6fUbcM1GmaamLWsrpt1c929xsx86vQBUX0UUNjcSgnPOwmzEGSN6tSyLOe50r3iU54qrjWxzONI%2FY0qL7hfW6FWgNL2dPOip6v5uexwl3C5ZoYECCCWCln%2BxDW2ijYZY1tMFzqRJnaAmDsBe0dxMT8jcT37WDCSTsF4YTK3sKBVopS5IzAPNXNwckaEU0ivbHLMwIIhbiaSKovICcVGe%2BawT5JHkeq7v9DQNcKFQ07qyRi4j78uQlM%2Bofi3YCj%2FeNm%2F4nHpTbk6EPCiEO4yzcNS6ys6jx0BR%2BpWYJ7wEUa5PKkkqs5XdkxrK3LYBTYw1HWOyCwHbTpC1Rf1i7QaT%2FuVOhAwsNDwvAY6pgFAv934EBkPDbwu0o9bFT22Cc0YtbZNjxibW4Qj%2Bj2%2FJeHFhXdsF13%2F83ZhW7kxzN09Ul1ZVBQkgWN%2FrHlQ8oJOm4EAiXXU2M277UAYlvruHeQ1AYrfDuwVdkneuWxiqUv2sTgu6Ww5uukP6Ogw6UoM%2F1OuNIdTSmxT6HUwbbHT8yl7%2FzpxcgPhv4bGIc%2FNXnyw77oMXSn7ASgfksECvIbe%2B8ssJgVC&X-Amz-Signature=1c4ee0da90082e434d2cc301d078ecbbf8556ae01ab6c1a19d358b86d48912e8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUCIHKOY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB6fo7BTLgthLmNNW8Z%2F%2FGEl8p%2BT9WmaTmHjuSdP9cd0AiEAifZL%2Bc18cVuPUrFoR5NhAKJSfNFio792epk5aPG2zcoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgG7XCBTFQtIpK2NCrcA9WK%2Bu1BsO1nI5KCJk2k2WQY2IsfG1lOqluCTC1cTnBAItCWo9dKqXwBRO2CYVqWUKRV7E3VSMIF1W06D1A%2BPs9g2%2FnSxMPw3shGNmC4PgkRO0Q1dNmuZf2yyasQQTFGcSB%2FxI7fChxHx%2FECuz7ogfEeTH9aHVD6thVr%2Fup8ve4MjiIIpXA8rXUTcTF2bBQiL4mIOElJeHvZBsqL8FglwbSnY7muD6SGmPmFsVvzM%2FlWIRi1imxy%2FN7gtK1LiLDnKjkmSRHPZ2Aig9%2FsZuQNo4h%2Ff1FDo6phDlP2MaBMdV0W%2FE4Ylv7PTWwwpWZdKRB1W%2BBqtcyzc93wf%2BpHilnbsTxK43bF3h%2BsqylXYcTReP7400KAqxFGfB6u9uf5LvVnfbTmsLpUdPCbGDf3JvPrMlW19NIHTNTD%2Bz9HmoxWsliKMaEv1jz8Mf7kR7WnR3YGYjNORyvEt7qt5t6rzU0JA90g6dkgJpL3F9RQvMlCVd%2BS0Hx3nphptWuEYK%2BSWn2AbyybIJfq1Hx5%2BiUZr7nvbn7LI3psErDUQEMkR4gkOMOEBsFiUT05tIdWA8Bh85gyFM3KmVLTFEpEs01Rra0MG7%2B3qNibPDQkJ%2B%2BxJEWBv%2FUSbQQolqXro83uUeYDMJrQ8LwGOqUBj8eAj14J%2FbyoL4WRxRd%2FsZvqancHy1CZb4ilUMCcrXLF3GXN%2BzLdU9SaMb2e697iiZ3jLMPlsaIvdPgm5G%2BOJFLSDyCkpgkka4EkmciLQqyHINaejq1iMdfOFHjE8riVfwyaQ67USvk3FpNUy5Dmpe%2Fu5l9ksKPB5So%2FDyoemf%2FSS%2BQqwuiLrXTMuYk0fAO1KLVIyJJ%2F0%2BZm7i0LzVU1Z0R87KXw&X-Amz-Signature=2a5b2e8970d675183e8eaa06374ec0aa5f3360688898d1b8d585c79ac3675616&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWUO4DQO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4urrDJE0AuvduClfh8vUr%2BxsdeeEpH8MFlFyOZuJXWQIhAP2MZb3j%2BUNshDAgAJOEBQuTu7lt0Dj2hLvWjn77lAWFKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igza0g%2BCXVXClqcM8m4q3ANQ%2B5Rct7oISecjxXuVVFBrnR7orYwPzMMLIVcFKERWP5%2FeOLSh9Czj%2FJ5Tp5A8Q5%2B3o0ns%2BFyKu85UmgoNPwXsy%2FkmgaroodH6rNNX3IBd8Vzl%2BSa9d1oJgXu7VwFoJcy75xz%2BoXZCGzTYsM%2FzwElc9ZKzAMJ2d1qsQsz4Frc24G6pKQjUI9wJFDQXa%2FyCTfTleYtq8%2BZub7ddIAdKpkQVB5kMozztUDqxXNs6ywnkvDjtly8wLEp2r%2B5aMQ6aeisW9n%2FAXnNJqpr%2BS1Uy108mdsuv%2BS0EnOnNTMyvwSRMP9reXwtx1zzWQ5IN2OT8mggpNrKZAlb6BqOS%2BTyy%2BWJNm%2F%2F4jPNgzivpQVaTKNDB0LaRTZxCZuY%2BYBZ%2FhB%2FR0fp6SkibluNvwb5NP00jOYi7c8HTyRigAkWIsGIqBjZi%2FiZ3rOtapL2CWzdA5c7bzShiAyW8gcL5Ka6qiafw31pZaNG9tyybqtaLEJkgXNkbUKQ7FhsPjUyY%2B1kE%2FJLOMpoXdG7z2toACcqdEUVw00f%2BPEBmoG06S6N%2BO2lplhUUUg2nQGOg%2FVzuRHCHlHUkbJm87Qp%2BjPJnC%2FpuOEwL2%2BmB6y11IP0JfWGlWb%2BvQMm5bEEqzAN7z8Nr9a4bczDi0PC8BjqkATdu3jWzhlp3%2B3hUpUirBtyPg%2BSAnIo0v2z8jPhcmu6jBe7VjNyrx1I5m7DARzDdL%2BCFhPZkZmHS4KAzPm5kr96AKRn4iNLT8XC6PKpq7cigNgm5hBQ1hSj%2BVRbGLetzlVyVIWBY1kxQVvVidBjliVnKmP9%2BEO2zpHWuJl%2FIS%2Bo4a3ZAuT%2FCgGl1y7nS6ZfpPBa%2B4XxeYuLB1suAe%2BUSitZNTf1h&X-Amz-Signature=41c44984cdc9cbd486ddac43e9c0037f8ee91add16b257585091bf8a176a9c97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS4XET6S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtWrvBFSsILVc9Yb4haNVyh%2BKBu2m%2FulUWQG2%2Bk0ar9AIhAOJCyG%2FTF4i2i0IH4gb7HWY4hEfB5Vnr0YkvRZmSFiKeKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDgrUEdFf8OXRBjHgq3ANTVgCU5GxgdQd53Uyy2XYYX5Z4L6r5mS5v1ORLHSC%2B4x1xrNQL8nWV%2BF8l0AZSoYqApMWBO5oNP%2Fe3LMpqJQ%2FpslOxChcgOF4o0axZ12NJVZrQHsgMr0aIYwYU2iWWA%2FuRXDvSuncIRn%2F%2B3iduHR8%2FhN6FlVNbag2BaIUtqR5vjIDdh7F4cUCFA6EOgGh%2B2Guov62%2FzuvBpBoYi9cgH412FGuhp8EMxhYL15acpbJd3LgSkr%2BZVb%2BBnn2iDvO3CnhDTK9yseuaYqeW4Qb8pr%2F2lE9VkvY3qsFko92FN9vJNEZGi%2BYA3I5Sv9yvD0i%2Bh%2BVzMRKMB4AXN0zzCNDi%2FaFYNrHO9N6SJuc6IncuXyz%2FOd9QpMvQ6YKkHi4vQNWD9O7sZu0hWuicWPjP8rOROSrV4ORtbNLHyAT%2BFBqMY5yKZaZ1SlqfLSAKwu8hYhhgojRNnCoEeCt2zWXsMjLNI%2FYqFNfkniSnETvWyYBi61vJlB5h9FbZ9N0UoT6zdOECKxKfrcuIWq4kxGERXNGawAZrcbhhh9Q1CYlWnN9hkf794edPOkJF0hzDjRf6%2B%2FcDIUHGtMse1luGZX23ZZ4yGST4tV2Y09bihYJSsXWb79BwaAVwb2TEsdXPDYwPTzDJ0PC8BjqkAXF4BHct%2BaFRMLwAc%2FBzoSxAi%2Bk8xe2Tjxl97a9g8pShWOHZ4gGYIICiMrepk5gKDIYGAujavXtTxsmN93n1SJc6SEt%2BDSBdcuFQ7rLVXi3gHFbatMA6nb%2Bhf0j6mSMEGL9U5vEAZ4CtB%2BLq4iT8bCOzjwTYe6EKOws4ikcEa2vCn%2FfBd8OPCGRsVh0agUwx4rWZgtcpjQjLUW5iG9S8NCuOa1LD&X-Amz-Signature=a89919fdb56f5be2c534d0684ab3d0a995c3cd3203bc56989eb2907e7efc2c1b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVU55SNK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDusZb%2B%2F8TBgoT%2ByI1XQh9ZOAbNSwrlgUqGKm3vYyrmIAIhAMOylGUkTwpChvWVgUKxiuEJy9shqZHtDJgOf0L2h20vKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlXiw4eiKD2MSwaY0q3APwtaWUncD%2BtHWZqr3b3t1kPKtofh4TCCoL8bBgFH6Qwg5DSo85OB7G%2F7k%2BH4o7KuxP36C8WmBBhe2vABcicv8editYY6BVNgYwloABgP8HhdmpQHyHsoQHBnb3t3eHkOhUpMyirL69vaEwJTYpoYNs2wd5YJpbzOZIyUQQWS01a9dpK%2FtlqYYnjIYBzPxLdPNonPs697agFzphl2g0GbSAGOZThZwonbt%2FwHRFRW4aTPc3eq0tCf1Bn6HRZAp68U9u4jMWzKd%2FGUFyQG%2BqRuQYlXsmymokkca40jj0l0IFmGvuw7eXnZRcULtt%2BfJ1OiH333s61IkO6IiXRTVULSFF07qHCXOxkSKrIACoIZY3CeD3Blk9SMYCwOMIMYykL1sI3KJf6AmIN%2B43WHgQ5AV%2FwNR92ZoPjc72LlnOox%2Fu66jaZqrad7vu69jrfnz5KqtmSOHgzgUw3wVpmRNMU5qHgamZSVJ70mmLafFBZnE3Am0o82HRDAXp%2FsVNqDvJt4gDpCuC8AXYJJehFXqhDoUzjGb8i4JOPsk%2BWYUV2Bv83Qi44Sd6shGJuitkUgKrqfOeGGMMkFNfGMAtC4Wg7xlGOyFdMODjs93MSmt35BthPNOWO1s1uw1Tz0TSYzCz0PC8BjqkAVWwr%2FkMM4kHgMUxuvqzfoqo8fnkL58zMm8aFp6XYM%2BFszLFUuVBYJ1MFrDPtgrw2zT6NxRXrEElvuTQi8EKoVb2IA2Lv35WT44VAc2P8g3RYNBfunso10Kc435ycELmH9oxqzr0r3%2FQB6pov2LeOnktCmLzRjonfPenDq2lYNRnMtD5A09fAsWgmBL9ogNWV6Z4%2BtYD2sJlmoB59S3ocON%2FTS2C&X-Amz-Signature=505640d25d1005c6a3fe67c60fddf7e80b69c9d47e0e4208b28a1e6c19c0d7d4&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMC6GWRD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICx9IxkBd4CycIV%2BQHRiaJ6EBC1kZEzJvIRDauE9oL8jAiEA2gJ2e6RJuSyu3lPbr49kHWL%2BNqPz8an66tT0no8dGKcqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIjHa6OStoFb%2FBfj1SrcA0mTSlH9wwgXiT%2BiryVL4pB0%2FQhe06TGVtsDo7ZiRww7RTM78cSNFRV2eyx%2FoY5Ymu0V%2BIADVdFg6ntxMbEPoXPJOLgILEtui8O52KVzeSPeXF1VJ%2BD5MDssl4dYIuw5%2F0Wn0TIcqhn82IRq6vBveDejrHpDjJRWmL7zEu6gpR0NGcL%2Fw0C3HHNztm9sZYTefBbyZGXcTf3%2FHJVggvx1H5ba2C4KqlvBnnsnR3Bn9lOG2BpHU5OQ0110p%2FFXb2sv3adJpliuzlhzNyBlgeHQnRLNpcpQ1p6MxvvkCqwynu3Oql74U5zZydwXonZsPm4atDvWoEMfqfTOIc%2BYWFnyAsVihw8%2FAbveFKoxrLodi30SluomiNOzIDIcXm1MHDjT9fl14dtqFJFNzfZ9IQm%2FAX36GgwaGg5L6TmgFdb1%2B9wqJKX6T5WhHNNkn6URy8%2BPqP2c%2FoHgddx7a%2B5JbzPZVl0cIvynQ7D4jUDfWGLwnN%2BHRmSLlga9TjeBjnQ2QcbEfmWXMXNlMY5uIFC17IxMoMdHRhvZUVRCDQ3dVaNxTpdD7cp2Mhot6PPEPrRG1yx2h6%2Bfe%2BWvcRIrsV6pkYWtP6PVUNprWgN3fKC9od8n8XDafF1Kw0lE06KGGzrcMIXQ8LwGOqUBdPeIELjGQHR0mh46YKF0EsSXI66qcPwV8hP9muI0Q4CqMxc7OTVSJCSZz5avFh5P5ogKRhcUlhkQqZCqemX6J%2Fl8uBG6tcEAKgFTiBVaOC1IzUoe8gHZYjScQhGHLTW0e94oLbMt5D6eUhCQQ8gFqUVDZoPWR0hezxtofamkCUqcaECk9HHQrsDXcU7r%2FK7OCLnllnAQnmNhRL%2BGh2tmC6oFybkL&X-Amz-Signature=1b659f1b5c756f5239b5e33eae6ada664f547105c9f65dd54ece4c69d335e55f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6YHGF2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWUoQLTDP7cEQwtsQf8bJPf3xQRboFDfuj5kmJHVR6swIhAOXYHZlo85x9zAqVNeXEOTdaZbcTHU%2BOzlcf%2BJQJ8ra4KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUXLJ6EnzSLZGWRNsq3APQ72Zce5Bjx7o20tSde%2FXW0cj5TM%2BDKWVZvRfUlbJ8FD4MJ%2BuoUiFQMq0Z6M%2F8vjUUginplcGDlR5qXJ%2B1750alWl105DdHN6kZsduigjbRd0YPHPLpfSUjppYFm2QhTsYIP0RC1x1H2vRdYl%2BaeRSS3gYAWW12J0txc1up2Kk20j3tNarEW7bwQOgUD7Ks4lIjJqswAx7h%2Br0H0PjTJfi%2BUPP74Vpe6fiLC6Tp1KHpYU%2BStCy2%2BGLLO3I5EIyQDnkU3Ku2oLKVkAduKjd51JkUp869jSh6ZgrjPtCz7PGnEhN2KlSss3oXG2dFseif1TqGQloGs3TS7QhErPmDrvgplV2rU9qbe54NHtYxZdQSrmIXpEx9KUr5htr6P8YMROm6vCKQieXhS2tqGze%2BHHT1mLkiNvN4uhsnZeMn1glnWTpT0CLN8R5TEh6cOq63QLf0J8V8qi0xMMp3wB5pKfn%2BHhqeT6%2BAog588acFN%2FaLOkjDmL8uCCp92Ec9KCkRCdb5fS%2BqzeUNQk3iLDp6YoU5b7s4FVeZRxdNvv2LFiRVZ26eQDIoCC4So%2Blw4GRuBnGPGCyCAuwQ2zCgI%2BLTCJ8WB770j5uGKVMOq0q8MiAYJAPICkAE2kz%2FCrwCTDI0PC8BjqkAcrj01VTY8LC1uXZiYCiD56FRUxOw60qVpy%2F5zopFDQxKRZ7WNZIMzjptCJ2bL16aBhwrSxSLfTozW4TRdsw8LcxNlMYpQZBFNVRo5Zcmi8oUN1s3gbYbhxNBkHg730kdMP6vc1my2%2Fl8D%2Bgse5XQMUSqRQ%2ByD8aiVORioNgM1jjcgzOVZ0ENVhpMvVDS6wTuyh96Ob8x2ecXuLlEZdqvSLTw5Dp&X-Amz-Signature=c36b9c637f3cd770a985e3d413959267845ee53228a52543b900c6ef0e4f2a7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS4XET6S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtWrvBFSsILVc9Yb4haNVyh%2BKBu2m%2FulUWQG2%2Bk0ar9AIhAOJCyG%2FTF4i2i0IH4gb7HWY4hEfB5Vnr0YkvRZmSFiKeKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDgrUEdFf8OXRBjHgq3ANTVgCU5GxgdQd53Uyy2XYYX5Z4L6r5mS5v1ORLHSC%2B4x1xrNQL8nWV%2BF8l0AZSoYqApMWBO5oNP%2Fe3LMpqJQ%2FpslOxChcgOF4o0axZ12NJVZrQHsgMr0aIYwYU2iWWA%2FuRXDvSuncIRn%2F%2B3iduHR8%2FhN6FlVNbag2BaIUtqR5vjIDdh7F4cUCFA6EOgGh%2B2Guov62%2FzuvBpBoYi9cgH412FGuhp8EMxhYL15acpbJd3LgSkr%2BZVb%2BBnn2iDvO3CnhDTK9yseuaYqeW4Qb8pr%2F2lE9VkvY3qsFko92FN9vJNEZGi%2BYA3I5Sv9yvD0i%2Bh%2BVzMRKMB4AXN0zzCNDi%2FaFYNrHO9N6SJuc6IncuXyz%2FOd9QpMvQ6YKkHi4vQNWD9O7sZu0hWuicWPjP8rOROSrV4ORtbNLHyAT%2BFBqMY5yKZaZ1SlqfLSAKwu8hYhhgojRNnCoEeCt2zWXsMjLNI%2FYqFNfkniSnETvWyYBi61vJlB5h9FbZ9N0UoT6zdOECKxKfrcuIWq4kxGERXNGawAZrcbhhh9Q1CYlWnN9hkf794edPOkJF0hzDjRf6%2B%2FcDIUHGtMse1luGZX23ZZ4yGST4tV2Y09bihYJSsXWb79BwaAVwb2TEsdXPDYwPTzDJ0PC8BjqkAXF4BHct%2BaFRMLwAc%2FBzoSxAi%2Bk8xe2Tjxl97a9g8pShWOHZ4gGYIICiMrepk5gKDIYGAujavXtTxsmN93n1SJc6SEt%2BDSBdcuFQ7rLVXi3gHFbatMA6nb%2Bhf0j6mSMEGL9U5vEAZ4CtB%2BLq4iT8bCOzjwTYe6EKOws4ikcEa2vCn%2FfBd8OPCGRsVh0agUwx4rWZgtcpjQjLUW5iG9S8NCuOa1LD&X-Amz-Signature=177a3d207b86bb1f7f837fc194a89d4a7bacb05075c94cc025bb8e0a9b57ec41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZPMTNTF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI1j0A%2FFPdhNGbuBDafJDYZgorgwSpP%2FGQ1j3PzN1VeAiEAmB2sT%2BqCUxUv4CkjGtYBrGvqD9cMhNNnUW2fa%2BY5S6kqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBCvzydQ8yr8TXY%2BvyrcAzAfdCfhURiOZfMXNrq%2BQTlIO3FHMsXDttlIh3v9plYmcsT4rLs5nderhwFRHxx9vgWI%2BziIU%2Fl0jLFzkQq3JaGaoTkv8ZB%2Fu%2BW2UxaG5EzY4uKU1GFl%2FtKzuLmixe9wNvTjm4WPCr6M8c1QjH2cRSZeshs7Ft%2BdHV1bJGFTlUFkpsIugfdii7awASFyGElBakc8PUFVmqT0WdZNdAjUCW9VcWgN1hbKPqpYVG3DcK3IP4dBfh%2BfbX%2FgGhGgliqffHL82yZdWOG3aV9Q81vByBaooSiqehsgzbe0ehT7wkM6yqylmBHxMtRvP52BrPIfEUsgUjHmSIAWnLJWQcbFijBZgpNwO%2FAgRqK9CZ0HP6zunHoHDDhzQq9gDoBWIttHJ9bkRBZhSUkEAf0TykpHitlzV9NfDjV9dIuc2ZaNZfO8frBCz2a8EA9C7ynAY7kQNPjpMDAwe45PfZIgGBAedGKyKVwlrRheJIYXuIQCXtcVyf1OtD%2FMw0q%2FrtKox5M1eGchxKJNCKGv9A7I220CU9eFjAe%2BlfSwYtGNd6QUy8bmhlzOMBQnGc0y3pEhMuA4mDkK9yFSK%2F16bo%2Faax%2FYVxEgCawUgqbG7%2BxAyvMgh7iTfH3R7ANNjtx3e2SQMIXQ8LwGOqUBY1RNG%2FqpPgvbKpikHZZfBuRjeVcVblgOAHpAA2sQ4BRtFGAKMaAay%2BkCU6qhFiQBRDmuir78dwzXcmrtT2E4PXIFiVhPehDpfeygQdzDIOBA%2BtWDYPkL%2BmHLCSyaqiDO37Ghai90rz6jL2A%2FTWpL8a5LHMX6ptL6H%2FpZuzPf9Rx0aVHnmv428Y4qIJxT5nYgVSBgMFCSOjzu%2BaA%2FdwCdioujGz6T&X-Amz-Signature=dc610c9e068df71c0516e3bdd5d28927d00eb9db2bc9133d1f56eb5efa626a4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZPMTNTF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI1j0A%2FFPdhNGbuBDafJDYZgorgwSpP%2FGQ1j3PzN1VeAiEAmB2sT%2BqCUxUv4CkjGtYBrGvqD9cMhNNnUW2fa%2BY5S6kqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBCvzydQ8yr8TXY%2BvyrcAzAfdCfhURiOZfMXNrq%2BQTlIO3FHMsXDttlIh3v9plYmcsT4rLs5nderhwFRHxx9vgWI%2BziIU%2Fl0jLFzkQq3JaGaoTkv8ZB%2Fu%2BW2UxaG5EzY4uKU1GFl%2FtKzuLmixe9wNvTjm4WPCr6M8c1QjH2cRSZeshs7Ft%2BdHV1bJGFTlUFkpsIugfdii7awASFyGElBakc8PUFVmqT0WdZNdAjUCW9VcWgN1hbKPqpYVG3DcK3IP4dBfh%2BfbX%2FgGhGgliqffHL82yZdWOG3aV9Q81vByBaooSiqehsgzbe0ehT7wkM6yqylmBHxMtRvP52BrPIfEUsgUjHmSIAWnLJWQcbFijBZgpNwO%2FAgRqK9CZ0HP6zunHoHDDhzQq9gDoBWIttHJ9bkRBZhSUkEAf0TykpHitlzV9NfDjV9dIuc2ZaNZfO8frBCz2a8EA9C7ynAY7kQNPjpMDAwe45PfZIgGBAedGKyKVwlrRheJIYXuIQCXtcVyf1OtD%2FMw0q%2FrtKox5M1eGchxKJNCKGv9A7I220CU9eFjAe%2BlfSwYtGNd6QUy8bmhlzOMBQnGc0y3pEhMuA4mDkK9yFSK%2F16bo%2Faax%2FYVxEgCawUgqbG7%2BxAyvMgh7iTfH3R7ANNjtx3e2SQMIXQ8LwGOqUBY1RNG%2FqpPgvbKpikHZZfBuRjeVcVblgOAHpAA2sQ4BRtFGAKMaAay%2BkCU6qhFiQBRDmuir78dwzXcmrtT2E4PXIFiVhPehDpfeygQdzDIOBA%2BtWDYPkL%2BmHLCSyaqiDO37Ghai90rz6jL2A%2FTWpL8a5LHMX6ptL6H%2FpZuzPf9Rx0aVHnmv428Y4qIJxT5nYgVSBgMFCSOjzu%2BaA%2FdwCdioujGz6T&X-Amz-Signature=17b443553382f08c066cf6f03f861ba5c9aef5821be71f6df235d8f04798ed2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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