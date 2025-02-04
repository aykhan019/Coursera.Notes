

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR4G7TP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQC1TBcrAO3SQf70LXQiNROqQTs1i3%2FlxOuB3qtUYMC1igIgQY5k4U9L7vtVYxwUq3k7zY%2FRiSr48N0%2FNhVy2AIn26cq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDDzXDGbhz9fYn%2FTirCrcA5HDgwC7zekFjUaUgxfrB6Roh9OFhsHmQzn0WiD71locFBfFMEPD5ZD6K28oXEuhxk29DVzDdi%2BNL9UFlVF2Q83T3cczvolk163ak01L0yuUplez0d1j4%2FKXCFguEnHlqDVmCmC7GrFjtloEsVIRbIe%2FgHuAxBIVfG9z9Qogqq5lSX7XyeULsXBhHdXY7SYJ3l1wnjl7%2FxxDlL26ilkGUGPIbB4sRoRvV67G4IKRlP82pd1ghzqxiTm4tz7P3mi8wUSn6%2BicYRcbC0E2LmhGCztTBQmlz3c0J2wjRtDEOm5O6W23jQIRdX0qn2A5k3WZmdGez%2FF0rmmI8v%2BIXHxpcv9OaUcQbzvhcfiWsbC4JF%2BnszS%2BVMoM%2BL88Emw4zj%2B23Ai1G3eTkr%2FFhAX7G8lkX1lFTyWUsvS2XUBM0NmR5J9iP6TETqn5VxZ47h7G4m95%2F3bzz5rHZhcTWeMctBqn1duMFTQp7wJ1CMw5GwFgu6lsFKeQsEgAtyX%2BKahgTsBpR%2FaYPEOITq7fkTvK53Nje0mOW0AL7wee5mNgvcq9OQBbF5FXsiO5dNZLw0u1YjegtOgAvasjFiy6pu8tWfnedAECQTHG87tBWd0Gmy3a7ARk3nDhxaitNrAgmxFYMLvdib0GOqUBH3VoB8r0WqbV97dzYvXkaMkryFf24rAMUbZtnRT7u5YnvNeqVZD2gT4b5f1IZmO7gk7IuofH%2Fnq7iiPAnysTh8vCrTgxJ43V8RoKuJpTA4bLsJtPbXakYIYvQrvW0O3xri8%2FEqCZbM3PbCDf2okALb3py2RZJ6hnjtfHh%2BH1cYn35SHNkaV2wMPczDc0XKK548ND1qUodk8PvTdv7rW3QsFGXknA&X-Amz-Signature=dd1683a2528b2e4df53bb490741f37a6f330eafcf14c3183b729479f99629c62&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466636FI2F6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGaGkmgP4P63xu11jFye48INeccHW1DFbfaW9Bq2nWxnAiEA1A8ngzEwv%2BezA6yIR0NSSE2CL787ZKZiPEhdOoYPm1sq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDKdCgQ24a45QlbvXyCrcA%2Fh6tFcTVw5EayDFLTeOo3IwOPZ1xx9uhqPmK3kiu%2FCTd9iMhsCNcIv6AUKBfVJAi%2FNGOLK8KZVSTjjRbyHYH733A6Lqs2nkqa1Lt9dL2ObdoiFvCOY8uLCGDE8wSuaHJDgZyHBZjICNuUpwT4UUpt4QTjMUGw%2BStll3FIEhmd%2F6oz1O2Bumjh5F6PMJnNWK36WQnw4nz5k1Z1zfBzUJ7Daj5z8W%2Frh5%2F17Oqsy6TqOnE4m%2FaqtC86ro9F0N5PMxddSgBxmUNrd2kK51C1Ae1jeUzeTfTg7VcHKNcMdUoBrUbKE9srPVU%2B1uLzG3Gc0%2BMApAgtg8tBOEF4avSeONikii967Nl5Dpmy1MdDRW9WsFl%2FvY8%2F6KTmJ1h6uI4L36XoeKQO%2BkqaiEFM2PV7KCliC2QhmXwEj7tOzkBtpxO3hMJ4LH9OJhyOIzErdBKVedNyM0j4zuXMFscodNcLsdz%2BCrjMRnKOvzY2wlsQ6vM5Tu8qB34x1nfSmZAFmeOR3Zb0w0TPxKhattWF7rzky9Endh6IWmwOSxDTxMjRdTy97P9tOrppX1P%2F2q2AJTSczsV8oz3ONRelh%2F0I11goekMUVSshyF7Znduemgtq5qY0z8LvyvtzD8ENQdJ4YFMOHdib0GOqUBUK1tvEhP3sFUtcAZMFS4eDR5jBRbyb3%2BIZSebqmC45PvLk5ZA4bgr1dVJL9uFSb8qqNDgEVc4AnpUHENRbAPuN9sMhwSmgTWuXXET%2FLsD%2BOk04DUGoRVE1Q84IM8u27nBgbZo8khGPLIHxpid6zk3HytC7PsE5a9sERZYnatvnTii9y98jqRJoAIYq3aHbp%2BEmzzzqUvAk8N4ZQeRr1Bo0Gp9fIq&X-Amz-Signature=7b257ca874b5edd73a876f57a46e492da5bbd196edf9709d82e9e7d010428f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UHH66LR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDO29aO6n4SVXG0zxZ6fmH%2BBsXQHx7%2Boz2p6JejP5BL0AIhALEBitbCG6hG%2F7CTGlwfuM3OYlS0bk5na6Rd7xKiVKmEKv8DCDUQABoMNjM3NDIzMTgzODA1Igxo1hLPfQ1oSrVHD1cq3ANwb8ngHNM3bqd39guh0Cn%2FCgRmF9UXwECErtAlmGov9UWT7vyVqGTX%2FSFXc9TBWpx5A4%2BHR15ZE172TsQW7nNoVFUIQ3N5Sgjw%2BFXrvtnxvTf%2BLOgkDQLI%2BZodAnf4thAW%2BGGXFZ9rlcF0q2SCwaujZ%2F6TD3Owkq838QNEJgGLQIkxP6LQnGinS2bq2xiJgWUzz0kmca8dy9CyrKLfmocb%2BEa5jHtEIwepvPunl%2FvNH0%2BtA%2BBpNQgQlz1ZoDOxVfYdxzzK%2FQDLyPwcZfcM7LVbzNOrQJ1DKhjCOXSp2UGRu12LjiiEwIdeKdwgPuRKJyYXSoPOVLtMDa3XGEPiLlLWNE7AwpDVJgf%2FtElzLiomW%2F50aP0lcIhHClDpab7TDHPlYeQ4D4fZzGuggv4pcUOqZUpm27XDc1s6PqTo8fA%2FRwx84%2B3bsahJ645we%2FSD4CLvW0eWFExo682K7Y2fON%2BOdYQzUlZNzWzfUSRp%2BmQSEzW%2Btl5swUcvy1TLvkpUTbW0bm7zoHEWRkmR668Nr%2Bp7XzpqB1Hfpnvs9x7Qf5Nsg%2BW2sx5cepaHht3A5WLkRsk6cS9iwOCwZ6oJhWiChCgLzlZBqI2bw%2BfgTUvgBqo%2BnKWXWC3OdTr03h0AazDn3Im9BjqkAdOvTnN5Rm2W%2FcVmhkiA%2BWvOVGoqQGALucpCJcdZRUydrc%2BAM2U2lnwPQqShwUvTzM5xhNt9OdmErEwPWAa6NJ%2Fb021aXWka6721jnx2t0tI4fk1RsdsbWEMXB%2BwoltVDctY%2BkFg9lOSsNq6YQsqzwKTkMkItzgsqP9IPlOUczMJvlOy2S4eZ4km0%2Fdqg%2BY52MCZ%2B9G8gNiEUxSiEXSzAklLV%2F%2B9&X-Amz-Signature=594a93604effd5fd8860102ade3bc4c2bf091c5b293aa209f0904b7e0bfb49ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OPFZXC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQDz1UwEQYGJfelpHWJPNLjPc122idWTyuOaC5dw5jJdEQIgP3zL3aTTk2Wuunhd3RqijPCtmlDY3HZhNf7idFcfbagq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDIcAtcDvauOF1%2BcLRircAxQ0J%2FHjVT4AL%2FjLzQmngUyGf4Mb5SbmmPadqszGhchEkJgeHcF2LHW14k8wCxWA6KDM4thvr8QSdtpgB1nG8sFElwv4Gxz3%2BB%2FI%2BwrThlxWPI1GkdYZa6e21PDAn2MBexXKQ8j2U5T06%2FZANgAU21Z9i0QU%2B1ha5WYVq5iI4x5jdmE8p1ovpHpQjbuuXwU8AAKJkcpputqVrgiwAfgTO%2B%2B6If38e%2BbsR2fUQtJCGhnMqKXL34yOUgj7NQXT9hN%2F4j44qme6cOubGu1hWNsBOM6qkdA4cMONdJg3cd2VA0DQ6DqOKdtUinsb4JOIKEyx%2B6zVBdzSB3ggIzo%2BHPtbpNDlRi6zQB8iDZ6%2FtM7eNmFiONR1GbRD5H38liWh91U4YCbU5cVF6LNtyC0%2FKiTXX%2FtzowPJwdsU52HRs8Py%2BmxUPuTrxoSmzbjma4e3brebLlof7lH63xJGs9QhEWj2gQqvh%2FqO2lyBORE%2BbuUlnRetd9PddFD5HRQiZU58pkItzqr%2BUaFyi5SBv%2BzUSt5EVweizaZPl0B6myPXaD%2Fsdp3bmwg3Mlrncnu%2FC%2BFMgFp%2BHWXS%2F%2BRPXwjrgyIDsZe%2BPXJwJdEjpiIHZcYtgBAEjsbb%2ByWSa9RuXgdUJmJwMPHcib0GOqUBYPbYCsk1LGKgWRmV13KScZTn4w6vuiF0zb72rSRhQMJJJIhRkSyj6TNaN2GogJYKH8UVfKAD6iN1nOLamRnHPIEfJGTcz5c3p4G82zXv5u2kM2rkR8QRW4sxUtQXk3F%2Fer0vLE0PgKdOvGtacg%2FuoBxp5mAXfpkNxkwUMaKz8eDiXNBGce4cUOBz5PLYvsjtT8vE25MMTzsR5ZRIWQrzNeKW19Jq&X-Amz-Signature=9c3733ba0377fad9d4489f1dd20c3e1bef48d81055091b86c030cc2cce2947a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWEX3GUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDkc5Zw4naKT0aYjR1hPhQTd1Mtikl2z%2FqJer5uhaRS3QIhAKnJ3fPWvJJZu%2BNvwzSyZLjIDelZWDHD4FrVVCJPoXgmKv8DCDUQABoMNjM3NDIzMTgzODA1IgytZYpDm49NgSAQJx0q3AN%2B1rsFKdRFX2ewhR4NW5KZWvrvWO%2FYY8vrGzJs%2BWmf%2Bu%2B0Cs%2FqlS4WMW82ApepNQTQ7wFrg9LwpXRW5naAHrlH448giUc8OkAQKIxFJAvjqY%2BEgtwrAcN4oi16JdSmmrC1l8HRLNBtWs5I%2Fe2acan2JG8E4NPOxICa1Md7jxBM%2Fwsw5oec9RxMjeqn%2FDeY8TbsdEIBI0VLbwju93%2FM2x5dFsceZtSH8Fdd5I7brjXzNHy%2BOLB1dRnDrtXWZ%2FvL4Lbs9DuAGs8%2Fjk88oEP8OxJdqYALn7i13Lw1zN7cpW5ZxszqHbMApl6P4K1GvfsyJa4JHj8Rv4J96ZavF4cWd4UitAMwK6lv3nAdulOvo7N93mouwkq93WzmyJ1%2FKnGpDMgVAHywfG8JEFATCDhQPOSvl4tHmXfsb42aGRBilx81YN8eMK0kXaHol1sbqaeou5PEqN7W4otsv9FUHmta4CqmTFhs9kM5j4sZG91JGuuQL4nxr%2FhW4hhR8MZwTP0pMOhbp4fZLA85kIbeM7F0xsFHNJgNYsw2%2BlPmMW9UrJSQbGr3QT3AqKJTnZXvaVcf61aupy2Sk1Ww4W%2BKRwLixWUCdlKPbhxcjTezWDttm46zFlqLrhgOrgUXVyISMDCx3Ym9BjqkAaxmq8b3NERVmjRPQJcGbh87H8OFnwFUWXYpUukk4VqdZLB0CeTmeIxqe9Qml7jfAeKPbr7XJn9ZHTUUVcQX5BbaNj1dD%2BsY0q5JodaA3ggmDTM8FD9nP5rkzWHcujFxu88C8LnlcERynXx5LadAHvRg%2BavxetiWWe3UyoXEVV%2FJVYVlth2t6DLILT7ZN%2BjMp9parlnm5K%2F5aOAwmUWdFcCCyFY8&X-Amz-Signature=c3b0b3560d15efd53f8e84a7e5d1aed569b3a3e31d6a03b9b9251e7ae0d2d6fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUL7GBNU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQDP2gb9y7pYBicQcQaAwqZXvg9WV1XFN0BnaZ9Re%2BYFsQIgefa4I5915iXFwso9%2BOecklF%2B2NwvoW4HNaqDxxbHlC0q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDN16AkSN7HqLqXZP6ircA3bO0hr5wndhyEMnnofQykyJ0yNcFcP5xekFxQPK%2FEHnLUPtIoW2y%2FQSe1%2FJH9XzmmhcsVOHPmtYhidGtaihGzhinnokaOLrTXSOY4Ivj69I3LdtDa0bPXHraZsYhjsS4eIgqmgjtdr1I%2FaaSojQz%2FHdSjrtkF4MrDcIbF47RlH1mLTCwlUOvvbAa650I%2FBpA5gOx4fCYcDlXMjbLNTq3RURG6UKnrtS%2BOOHB36Fb4ZN1iZcmm2MTJ1JTD6hHD%2BItaDTAeVN%2F4EequZJe2OMeVXHmCXzJ7TE1MitdZo5hN8AjWYl%2FIQuK9I2IrDQk3Ch2irZlTpfncF6uJXKzWLdpr3I%2F8n7nAV4gQvYOLMFobm%2BjwG9Fxnt1OtnVlItOfqCbrTmxtlAXMU5qSPn7tHmdrOv7VDSkOTImMwzfavuaSylxY9aruuQUwhC1o5mDHDjs0Zipan3Zi%2F1LpFwn7HSeXQerK0PHT66HyNgSixu4%2FnsTisPg81OElfSWDNWPpC3uFAFmyRB%2FwVy%2F%2FXMN%2BhuYxRYdaE1ye7475vC%2FWRcV5sYq3zxHNE3ScKjKzWBdBW1fcrsFbh2NX0V9g4J62RiDzV58MBtbwRxUidCD3twIHuXGwwW9D5NmOqQ7YfaMKjdib0GOqUB899i6dQThfiM4UX3MwXH8gzFBCMPGsF%2FTmRjzW576Lvx4PdTGV5wpkv4DRs3sQQaKMufP6EOaXIuWf6huU2Ps33kas8MlCrMZyEOEdXVm9lZi38QxUswtL%2F7Dyh6uDqchEq47Ww5Reblp3e7JiUYP3pyrvCJrLc51MsukxbrhXWfaEgvFs5yKBKEQ2kkmqU%2FOFdhJkzRUlIHoRXEIrilpXVh3Rl6&X-Amz-Signature=f8789d3ca7b3548941175ca7b15ebdc07b97a89d8fc2a60adf50ea1d9864bed8&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ODHQPMB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDAXWqg1xUndnaQko6MFYy3DttHVo%2BHFNj886n31m1EbgIhAPFY1Uz%2FsLiWvf9NgMZPIqATq4yycCN03E3Lz%2Fc%2BxuxTKv8DCDUQABoMNjM3NDIzMTgzODA1Igy8Q1GEOcMlyQCRsgEq3ANgAW6nN%2FH53GQxYZY%2FP720HPSFl5%2BF%2Bzc9Ghfnt%2F6ZdVxYA%2B%2B1q2XiQIqpMXD4rQ2NrevzNDiyWrPzIRLbXSESKUGM789xXrHkP8y1YOg7ZBUfmbA9y%2FdxAtebelgO1W6GDDMylCDHAOKb9DL%2BaUCMVDnep%2BJsD34WjJZKcGwUJ8QKS%2F20s9U04nltl5wiKuFM3ZYSYpneeX3%2FlHD8%2Fkuh0prYU%2B1XSrwn9u7TXKrHgGjwKmcEIR%2BBobKG38C1v9jz7U2FqI5ZU7gkO1C1srmYhnXS%2FO4aRf8hFpeArwbz3JU%2BEfKAHceb9cNkVCMzg7ZJJZQrbfQ%2B5S2siMGgIGRl69sfYabCXTxvBWpqksw7zMbVBucDtpAy8pGoHfoSTKH59cEQn47bsyeW9TNL4UbFIRZN2fZVBLOq7hZPMHxOh%2BrVfTRgS%2FOu8IZo687ZHlJi%2BfGNsVS96DyFtYLwxoPm5D3t5mp0cpmtjo66IMCwAN0GFYRuyCzeZAs2Ng1o8FzYUysDSKwG59fNAg5aZ9qN7YmZg3wKCQwPzJkPA4bqnMVwIUVip%2FWCsH0SHWLasQ6qTgW9r63HqNT2JFAwAuTM7EzNhh6LcB0BLVrb7lh14moJtyxWT0VdXcONnDDg3Im9BjqkAbzuQkSjGPqmsVYrrR0cGoPqe1%2BoUEu8NOiSM6bhmIvStqs4uQs8ir4s5baNLjpUWX%2BEE9EEy5DYwwu1e%2B2Hp3iTJHJPA4IOTWxvFBdABFgbwJMWjhPqHsX0n00SWpOFkYLYdJsqziZoKHx5LjDNBhnfi3jRQ5PC5aYmCClKOnjHVkVA8jJhoV5kA%2FgMbMzS3JkyIdjJZFjBEBuLW2e2Y9p0GxYg&X-Amz-Signature=e09ea1efd04ac491016e4757652199825bb9a0c80d250f5fc3b264d1b01f012c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HPU3I3Q%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIEIxDXWCgQ0tC0fFRZHSs0SKXSHkEVzgCkvgpZWOMHuCAiEAyMI3onWQT3fUCpZlVHMQSOWP67wBOJOBt%2BQxuAASFF0q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDObePlZVMXm2F3xfYircA%2F9y6ezI%2FwVcY7uRSuUd5I%2B8J4ptTTSHXJjUdTZ2PZL9QTGzwm77x8RDFqEYk5mSYctSeYmvnENqdMn%2BDfpVCe6pX7i%2BL%2B7Gk30nwn%2F2G%2F5D4%2BwiBphjrNIMSQcnz%2FWQG1xEgaNBCluUWYoWEPePdPxMovEHPG3v44gH9SgMGcUCxfPsgGqE%2BdA%2FCIuCpYZo%2FQBvLd8cHQM8pgNIywoPvWbdreRlKjELSkw7N%2BoKb6APWaedSiZEsSscVHeO267N0XZSDAVTMFFKONQPDzAL%2Bgaq%2Fvgt9t%2BNMN54CyU5%2Bwf8DspV8TZpfwQRTMBtgCzWPtAvAWOATyWCmwng9p55i7oTdVjuVoxgOAXt6R9yfpTtsZ6cHASptNJnlgL8lgsCTfTg97hXS6XYj6fUEX4wGzF3ces96sVH%2FHV0r7GP4oXcsKki3T82HmckG2YA7VoPhi3VVjj61bquxlzAhDMb0h4EJ37js2q%2FQCLUIMdlsVYDlLgzFqQHysBcvZDQf24IEop9%2B5jJVAj77CxLDEmlIZGH5vgAU3N2Isvfh1Ps2LyRDys5JwpkiAQneXNLp6sCYUrjEIsgFL1jDCnLg%2BADvkbffi6zRXQKaFqUhhaqg7HQiktsNEFIcWxICOKWMOjcib0GOqUBWkfErWMabFFJz%2FTOzubSliMbygSpNMbKn%2B290%2FfWj8ORB5RGx47cL6T2VFHwKzP%2Bwi1Q4OHdEj%2FimKGTCU0AtqaszdnpCR%2FxAN32ARPEkndijpjzqS8B7CLX90Zzd6GoKGfFQLJjkLyhysk3vQcUFCy2fLe29TY3sKc2vRua4AjW5gBup8HywOaNC4wN6u%2B01r%2BF5VVrn2%2BINcd9%2F4p6EF4bvdAQ&X-Amz-Signature=c364a445647780370a00f339f4bc1c2b5ee6abda1cfb3d6043fb046526a90fdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWEX3GUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDkc5Zw4naKT0aYjR1hPhQTd1Mtikl2z%2FqJer5uhaRS3QIhAKnJ3fPWvJJZu%2BNvwzSyZLjIDelZWDHD4FrVVCJPoXgmKv8DCDUQABoMNjM3NDIzMTgzODA1IgytZYpDm49NgSAQJx0q3AN%2B1rsFKdRFX2ewhR4NW5KZWvrvWO%2FYY8vrGzJs%2BWmf%2Bu%2B0Cs%2FqlS4WMW82ApepNQTQ7wFrg9LwpXRW5naAHrlH448giUc8OkAQKIxFJAvjqY%2BEgtwrAcN4oi16JdSmmrC1l8HRLNBtWs5I%2Fe2acan2JG8E4NPOxICa1Md7jxBM%2Fwsw5oec9RxMjeqn%2FDeY8TbsdEIBI0VLbwju93%2FM2x5dFsceZtSH8Fdd5I7brjXzNHy%2BOLB1dRnDrtXWZ%2FvL4Lbs9DuAGs8%2Fjk88oEP8OxJdqYALn7i13Lw1zN7cpW5ZxszqHbMApl6P4K1GvfsyJa4JHj8Rv4J96ZavF4cWd4UitAMwK6lv3nAdulOvo7N93mouwkq93WzmyJ1%2FKnGpDMgVAHywfG8JEFATCDhQPOSvl4tHmXfsb42aGRBilx81YN8eMK0kXaHol1sbqaeou5PEqN7W4otsv9FUHmta4CqmTFhs9kM5j4sZG91JGuuQL4nxr%2FhW4hhR8MZwTP0pMOhbp4fZLA85kIbeM7F0xsFHNJgNYsw2%2BlPmMW9UrJSQbGr3QT3AqKJTnZXvaVcf61aupy2Sk1Ww4W%2BKRwLixWUCdlKPbhxcjTezWDttm46zFlqLrhgOrgUXVyISMDCx3Ym9BjqkAaxmq8b3NERVmjRPQJcGbh87H8OFnwFUWXYpUukk4VqdZLB0CeTmeIxqe9Qml7jfAeKPbr7XJn9ZHTUUVcQX5BbaNj1dD%2BsY0q5JodaA3ggmDTM8FD9nP5rkzWHcujFxu88C8LnlcERynXx5LadAHvRg%2BavxetiWWe3UyoXEVV%2FJVYVlth2t6DLILT7ZN%2BjMp9parlnm5K%2F5aOAwmUWdFcCCyFY8&X-Amz-Signature=52a6d7676649d18a693975f9092b379e4711be8ccfaed713680c6905726dab60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466345HZWPM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIHdnPHI3xRp5Tub4Y%2Bqmzh5qoUFQz55qG8qm8ZK7mwIUAiEA0KTV5K4zfj9Nl1uRRJeq4AX6ME7F7bopdLrSh%2FA%2Bzy0q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDJxcDTFpmuNiLIc%2FzircAyOzn5bLmkY4lGG6nOAJLIE9f7WPyUGbBZqdVvsxMn3NJ%2FYA8aYqwelbvIU9Ue0kNA0NnOos2mu%2B8Zub8Zw%2BW%2B4DV9yEAb7oegLED2XILGHyAxMGo6uNMZm%2FQaf7eqns23Y%2BH3tUnVVLQ4WoJuEztQ2pk9RZOG2l380La6MlePyDKVHkSlU5CO5vf0YejzGfyLKggNklc%2BkQxs4dRKTBCZKZOyusoyNfbXHKk0VaKL3YPugSQ8iXhnbGuM4saA3Nh%2BhYD2xHrTCOPQyEPdxwJmxjlXxJs5cvSTtpd%2Bq2cNdYLidZzSgXgq2HEcoYnXIQ%2F4duTkFeJ2D5C3WNTTQb%2BsEYY0ho9PRaKAqFihMWjcUJNbQzbRDQpiizWAh7Iu8acTVwNweYHbo%2B%2Ff5apKMkY3SLHD9p259kzXbL3SyM00yyNrYco%2FhLVMJrhiRH6QmMpD2D0Y8SWbYWFu%2FJyzvtUB6FSxOOxq7qnh631Cc56HTNbaRbebfDeA3K41XI5%2BuQnl6wDbAirvKObSaTsgY5FLifSS1Ifx1BFs6tSr0tJi%2FuXGv1l6dWM2AcsZi1wNPe3qD6DYe34JSOtbqswwgcrmNWPTHiFLmeUEDQ4JmxSy9CrCTBN4gfMYjqQALZMIPdib0GOqUBcgqWv1fWK1oxnUFEpznC6byrZI1g8ZwclSChiwrYuPUIafzGwLwfbpN%2Bi4m8GD2Deaq398IQNzWdCFC5YI4V2YPIBQ7s4PXRsgdB07vzVmMaJvrey8AnMzTc0SJSLq66U0sbcwcbW9kiCf2pBNnpKpp%2BeFHE%2B2MmCPlpW3Cu%2BFVWdAkFasagWekqy%2F9mmQPvDvKi%2F2WeeYi1cQyQ4e85aiI9NIZr&X-Amz-Signature=ef070da77f104aa946c5074b2bc02ddb91d3caecc2d4ccd3d2772754977a7a39&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466345HZWPM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIHdnPHI3xRp5Tub4Y%2Bqmzh5qoUFQz55qG8qm8ZK7mwIUAiEA0KTV5K4zfj9Nl1uRRJeq4AX6ME7F7bopdLrSh%2FA%2Bzy0q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDJxcDTFpmuNiLIc%2FzircAyOzn5bLmkY4lGG6nOAJLIE9f7WPyUGbBZqdVvsxMn3NJ%2FYA8aYqwelbvIU9Ue0kNA0NnOos2mu%2B8Zub8Zw%2BW%2B4DV9yEAb7oegLED2XILGHyAxMGo6uNMZm%2FQaf7eqns23Y%2BH3tUnVVLQ4WoJuEztQ2pk9RZOG2l380La6MlePyDKVHkSlU5CO5vf0YejzGfyLKggNklc%2BkQxs4dRKTBCZKZOyusoyNfbXHKk0VaKL3YPugSQ8iXhnbGuM4saA3Nh%2BhYD2xHrTCOPQyEPdxwJmxjlXxJs5cvSTtpd%2Bq2cNdYLidZzSgXgq2HEcoYnXIQ%2F4duTkFeJ2D5C3WNTTQb%2BsEYY0ho9PRaKAqFihMWjcUJNbQzbRDQpiizWAh7Iu8acTVwNweYHbo%2B%2Ff5apKMkY3SLHD9p259kzXbL3SyM00yyNrYco%2FhLVMJrhiRH6QmMpD2D0Y8SWbYWFu%2FJyzvtUB6FSxOOxq7qnh631Cc56HTNbaRbebfDeA3K41XI5%2BuQnl6wDbAirvKObSaTsgY5FLifSS1Ifx1BFs6tSr0tJi%2FuXGv1l6dWM2AcsZi1wNPe3qD6DYe34JSOtbqswwgcrmNWPTHiFLmeUEDQ4JmxSy9CrCTBN4gfMYjqQALZMIPdib0GOqUBcgqWv1fWK1oxnUFEpznC6byrZI1g8ZwclSChiwrYuPUIafzGwLwfbpN%2Bi4m8GD2Deaq398IQNzWdCFC5YI4V2YPIBQ7s4PXRsgdB07vzVmMaJvrey8AnMzTc0SJSLq66U0sbcwcbW9kiCf2pBNnpKpp%2BeFHE%2B2MmCPlpW3Cu%2BFVWdAkFasagWekqy%2F9mmQPvDvKi%2F2WeeYi1cQyQ4e85aiI9NIZr&X-Amz-Signature=3007b056fd09f91615d4c2c2f4c81d7a9936c90ab76bc6db5b575057832fab69&X-Amz-SignedHeaders=host&x-id=GetObject)
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