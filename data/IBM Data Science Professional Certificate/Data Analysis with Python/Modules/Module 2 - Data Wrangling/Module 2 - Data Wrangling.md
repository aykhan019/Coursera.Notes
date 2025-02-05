

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQOLNBSP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG0a98hrVtOS3%2F6I0b3VA1c8JQMxNt6HpJnydMYhTpVbAiB3VtZaSUFkLkqfamKeT7duENhwtlPJ6SpMW8k25276Vyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMU2I4crjt3oBpDZ26KtwD4GDILwIMxPoXsIZ1jmN%2FPh%2BexN0lIAchyhIZGeIFc9i4RVB9OzmsumFUgzRoXCQlfRwLhe5E8C4PFUr16itOZfGQRwPzZVX5KM8Njw1vCgnhiANX6MNpgxUcKulZrRdBrw1WnHSrj7n7BsdIndRPApKXWHGt1EmK5Sy20S5c3Er5FepddAXo5L%2FV21Q7pr3r%2BcWYeiF3UfkgYNHC%2F0BX5ploOuGJe39Qa%2B38%2FY989mwWLorJu%2B29qnh%2BdY54doJg6KNenUFGUKCqe%2Bku%2FEOd5cJu%2ByDrB3kBoO7IvzU7EJtKrfN9yVwyu08DadL4EZUW3QrjdFfLAl2%2FTJOyrGHTrZi3Vu7kPN4V1s1ypi82FMI%2F6U0a1GUeTv4RWr4nPrUVCwzlI5c12D1bbo8Pk0HY0N%2B5r180%2F6bV78gzT9DpeTCrgya6GoGSf89nRL3SUps%2F49EE5nit9n%2BofFSYj5mnWrTF7cCftpuR8sTEfxIlhLjbw9upLwdvSsDFxcxdBAhFCCTrZQpV4Kncb3ETYTqqE%2BS0K95AdTEPY%2Fg9u562rm4LnbMSVuJPMaaYmDwViyLIz%2FR8Pr6y0j1nIm711Ls4xoiCx%2B1SB5mNCLWHcmy8sIPrh1yKsMct8BdLlDAw87qOvQY6pgGfAtyn4HMpseXn5%2BfKu3342Fgb3PYAWtcSvF224BEdY3KkpQXumXfF2owQGGAx3C9rm5CrnTf2j57urrwJotQ%2F%2FMLtSqV1liEB46xmfgE8XIcZKVvSt0CinURInXDlXHD0kOYL03%2BFBKQXVNZwWJZQczh05BqquRv9vDPviIHKxoMl5xB6o0Pb8Xnutd0vF%2FE6QcHyeYTfqUzBfzUuVAEDiIiEkXvw&X-Amz-Signature=e760f2b2f1e4ea482d852082de677383bfb07f26633f76c1a42ed8da89111f32&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYKR3AL3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCXv5HKsckIs%2F4rLe6Bbao4ded3%2BfecsBqyxpqbG2rluQIhAIVF6YqFkqlsFlIWCeNSNoIpKUh2RlHCl2iAK1vOZorKKv8DCEoQABoMNjM3NDIzMTgzODA1IgzPZkI6lgQgm0wfjnUq3AMkpI%2BI0o7qVFJzGajuQI85Ragu8RZz%2BmcyW8qUZynYHyYZyYsdwfAmeaVTrlGHJvzmu7GOKv5juA1aOa3pn1jpGtPF1c3YnoW0j6Gg7fO41dc5Vf7JgxgWRBog0bGZtLykOdETmng7EMt%2FP5rcJGv9dg1GlgkstGEOWDg8R82F1RHONgO8QPvvyzw0Tzg0m17Q47D2XUSlWGKlyUsS5PFLgOFq6sEu25dwNtktWN5DbCHAisQDNoBriTkSQLNf93Oxek3a5vFlxtwWrqP9qXJikG1dwQnGj9LxvIkqjEJSLfrrfItQHjpIs5nKv%2FGoxUZIeeZggQVlPwpTNI7SUOMBNNsWdcGfMVIyBOy2tV77FUsmk8FsC238gpBozAp2LO72mI4vuhFYeU4HX7aW%2FIFJac%2BxIzrC8lBxgsVJeMajJ78DIaOgVzpYdi7Rnv92Hy9bvMwFExKks5z%2BRm80Pxtp4M4RlT3C0atLRyaOmGpGD7bW45dWeelBzLc5ohvOJLcGFQK5f1AseI5unmXs7mJlpH7jGmUiabaQsCnsvCVUEn5E9q3XM17tZNDI2Evh4fD1gDYjbIrOSrnSU4ZJHbGiKYZ2bpEfCWbZojCbodgXj%2Bf4DRawsP3SIUYezDD1uo69BjqkAZBEznwvvx6IA4MsAOZwiBDzQQfz2Kcprg2%2FILslHy8SSla6YQ%2FVexMwmhnfQgenqgD6alWEAuvEZrryq12y%2BK844Nu%2B5tvItYMB4vuybRXQlAhfYr2AGLmzgu75IIy2sXKEF%2F8T8Wq%2F%2FQJHsNAlj%2FiCJf88ah1WPSY%2FQMH2M4%2FrFHu6dSFQdA1CygV8Kp13Co%2B6mCHHq84yWdW7Nf4S7kfcweK1&X-Amz-Signature=a2af7fdebb9445108454dd0f7f5d3b41ae10101457422399df44981bf09de67f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZQFNYYM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCaMFuhZIOW0%2B80%2FuZIuzNUXf23DoRSvdWKqonimOwYJAIgFQy0%2FZfv0qBRx2vs%2FON7bzGd8i5qfXJWu0SnHGnnyQQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDEZ1uYLjK0qdjy5JFCrcA%2FLqNv03hbC73eWoOtBJXM5jT3RQSfcGgQNO4jNV8Xv0LSR24WcuisvErBGKuP%2BXliZI8N2ZfsBwSiw2sVRkgHblBQusu6PfL%2B9IRy4h81KMJeTHz0TJVrum9Sc2lEGDraIWY3PUUmk%2BWQMRdJ%2FqOHf4K4zCyWVr0PkO2OuR8Fk654XzwuvGmROrb7iZKYy5B8hDf8IJEwrMmjLeBmlD8UphPUfJCYGGattsdGMMkudbibNb3RqOfZqvNIRTOoRc%2FmhxONmFVJK3gHtY%2BMroxatdGSiHT7F8PE5nvZJ%2BjggQYFSmOrr9KbGbtcraLuoEGmGfEHACZy3QSGqHxRRmP3A%2BwSWiAw%2Fa8yrpRrJ9Dvv0Ip9HK1cGAgn6XD7NmrHy%2B%2BYqFafP7gXOJAmKnLWQcsnRxYAZsD20QV9SJSIH28L1g661ShNasVuvI07PwY%2Fo6xQx%2Bta5lY8YmOiKGzMJ3c%2Bp%2BckXSuy%2FdsFpbRzp2fD%2FpdtQAotTdRA2qGB76UKVC5mOx1sB3O8KfeioQar3feoNwCWeH9e0fH2Sfio3xBb%2B%2By34xhSpxbGsyqH1ULmu5%2Fav1Y2lApEMWkygoubaMbki38iXZFJL2XjGMWRALbyxykRLFDG3cKc414PNMKW6jr0GOqUBHHsWwaP%2Fcyj2hc%2FRMKryEj5qKidHJmT743Z034Nao4PaNk%2BUmGcIpwyQO4xTcK%2BVdKIJMd8yDxkeOiiawcPimW2UznNNW03meCxqzyNBANzBJwGtvMekKGpQCDvVeyb2sf7uABIdsnWCQ8Mc2%2FVGgJMgLzdXGBUb9%2B9DxPJ%2BgFSO07m4g57amAZqeBTyM2N7fw7YHZHZLlMVGtF0x5Qatu4YThB%2B&X-Amz-Signature=73a10f7576f876d4a23c4b9008c3d0b9cd03c1e45945bffaf7ae3366db549ac7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRBF4YS3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCID3vXXtM9bdhU4QWnpSLEeR%2BGzaYm6w%2FKguMcCL7F4MkAiBWxDmoSm05neR%2BxvcuIbKCndi1ms967GUmUhEUY2wVeyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM7KJPWt8a4bg8Ob3GKtwDbIdmdCLHn85AhXbYdZnodRbbeNP8DH6qCDtijaG7PFfy6G%2F6KAxYvHx1lfGc8d7r0%2FmerRMPup4k9GxQT2uvH2V7T%2B46XQriw2hf7Lf%2BwI0uAtJho4VWGUAm0t4dgBEkCjZXo2CuAqYWxOw22Paf4M7VKg%2BoYNX3FWDUNaXsuh7VejAuV6bRTSdfiRjcEDQzFXJMb0ZTIDrsaqsBwTJAJqXQWzCV9F7KVNcmflXjet3%2B1faYQJVJEXHLdm5l7OICEPwATakVEMqGf17L6mp4ggzZpS9p43uXWFOXrunhjn79Ol%2B0PgrArSnylZ86RlS5o%2B5lkmRwNP8UslDWZ11%2Fq8KF7scp4VnCV2IlmUvXIgTuLAehy1xEdR2yRCpQ%2BvGIg6PuV9tUFKo4YguIeQ9stJo%2ByOH2OIvW1EV%2FLFQ%2F7XL1W5hk25ZCVRWf1LDHuLasxLiQWg7lvjjhmDBIQkK76%2BGH3N2Z4Kk1OJy5St5weNGXjbIx2SxtzQf2IoO2Vmtyfa1%2FGHWGbf8QmaLobTnE0tlKZExviTbsD9Ky0VpqgCzxELIsQCqlh4VO%2BvFF1BnvcIPKfi3mCOSeIZTGhDdQlqhfBGHl%2FtUyW5dc8aB6NSUxov7h8TqHe%2FUO5lwwrLqOvQY6pgFWX8eRdLsTY1GMnVeIr1LsycJvREQ4lMKbWNM%2F8tbG3HMLn%2BF%2F1ZFPO%2BdwTYe14ulvCY90sNzF4jYq5PEC%2FPoqPmIWlqTf4az4Elpy3Dikg%2FzeVaiNEznf6OE9yMducZ9tehB41i%2BDJRdfHjm0f4FPefwMKfJ5%2Bu4iAPSb3e3iqIeJoYP%2FEEeCNsj8GOqpi4XBBXcrUo2aO5Xy6BK7iE1QA2%2F%2B1HYa&X-Amz-Signature=0233c8697146b431ffe51d293124934cdf92e4be47580add038e2cb9b1911d77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TVAGPSX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCNhwxyo4%2BuvKqlgg0%2FITx20GgjWgvygB46riZkB%2BY4zQIgDo5KktFaEw34Ze9EdHQQc%2BWGX2Alpu4YzVjxiqLTC4Uq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCDmFdvaK5WawlZfoCrcAzHjERNLgTecgvGIvW%2Btbn1eixGPO4WiONXbK3WzN0tbbwocMKZhn0t9xDeT848oe1iqVuFL5XGol1hp9xlpD6AFWVw4aiLsFfZhqWW0K5Z2YYdsRAMLx1QLTg2IA%2FKT4H07zwXPjAoVxngDBeKk4jlffuaVM9rns2WRqQ5PT4R2rUQlKVmf8%2FqVv06U8e9bFX16tcmCEnGi1Cl%2F4RlhPhspg91%2BbKFUTU2w5cu%2F1XWXAsLOtOKRlhHHCW1D4uwVxJvAmX8nNyqu6kw5YUKQ9%2FxycgODd46LvLN4qWsP2U7ZOxQjViCeFN0xKPr2g14eBeEbY2bZSms0%2Fooi%2BQqsl5B7SZJCsKjoy5s45VdMPxLE8GEo5sjtNMQCV1PD4wbgSoWoU2MYyPNOeDzgWtDanuhHXMWWq4QhkVKepv0EgPugaKw69DXf4IdjDzfKAy26ywXChYSc1uc0vw0yTIvDs%2BYVVbOooJmbawmrjd9%2FBk9kzQEjUv3Lpr1QibvT1UlSuwKJ0HQGXh17f0V89TCKigGjOxr7ihq1ttqH%2BDO%2FPnI33MHXClM4oOvrY%2F3lbuFE5D176vrw5aF51DoH8eRBNuQ1I4viFgK19BwjhZSwUGZFdy0sgtMd7RpOy%2FEOMJy6jr0GOqUBBqvZBbmeuk9DJIdxiwx%2BFn3XmIXN2sA8AiS3nYnxiQfPrdSD8pJ2E%2BnUNk53cjTHVFxU9zY5QEB01hk5y8yQk%2BbfBxO8TkXPv9DcSLy6rS2ToXKdr7MiJ7PvB4ZZYsiU1eXDO99YVYLggsSrKZURtRn4Zr0cZ3X64HNANQ5tI9FjIauAco6FUdaNPeYNqT1ZA9gZgJtnsC5f9CcnvnR6skdFeoxJ&X-Amz-Signature=39d9df0712b4fcca1daf6e9bf71d8ffb4dd7c81a67f8b327e9e5d732af0d369c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2CTUYCS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAJH9swPgKqf%2FgVUsAQaRtzZzhm8eXr%2BqiOIdcM2nBOlAiEA6ed0EYy0ataoQTpg4tAv6%2Bp9NvRx7GAdV1ovdyPUYIIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCCP9%2BWGWNp4wGV%2BfSrcA8zgD%2FwAm8lHUPej3JsiKz7fqm4FTBP9gJvwV9pupQi4iGdJ%2BUurn56GJ1F1FYT3UtyF1Htc3y%2BLIaf2iR2YNNbvUHs6cgcpqMI%2FZYxb%2FKOw6ygiSO%2F1ms5TaeDR7E7EEPckUC2n%2BdGstPNAFx7HGgh9itwZ3NM31IF5LTS7oCNMIXT3aC3maOj7qD92ZgxZlvGal%2BG%2FfcZrHOV%2F95sJfxmckTvfCcMeZmno%2Fh6xed%2Bt0MpXpEtj5e9MRaPY67hd%2B5R3M6rCKRBRdLl%2FwV9cH4DUjUMgozBcTmjNcD6Nn5zLZKfKqyiOfvDZsI8tGoAM2XujuYbL9F8Sn0vK0ATKF8iyuObBs7ZDq6dh8atyPKHA9Anlxsrm2pSMyx5qU3J3AtH9%2Bd2wH0lhTVfF0fhQ6HAlmki4MjndUWvwy4w5M%2FrOPvM8SPc5La0nuu49edkzHZXIfgLDx0ZDC30YGauBAVcnpw1njtSB1cXwajoemtmJw9yLoONqPxUypO6lL6oBDdMMbsvHBfGpGrZNRcD%2B5HuSpOea2mLTHk%2BggXhZIiySIqJ0MzvIdYgmR26UcXgCGmxYyVDg48GKlZSxG%2BH24Uxmv2iaE0VVgtYZHB8XuWlwlSf5T%2FHxIxTc7za9MPO6jr0GOqUBUibnO4nN3lYEG6z8Kz3efUJYyS0HehN6BveMeC0pKj0K5FQc3PtRua%2BmX0y4YafGj%2BeG9bSjUlJSIZZrfpwiLJGlYU83%2BhuW0ZZp4ygaL%2F29irbLHTx8rGzO9x2MRJqyCjyn9MMMWAUpK%2BIwCT8ebHXOCSaZKgkZh79fpK3hrYc0Sg1AuGCFvg%2Ff4iWNBVIsUn4YkVkpngngHMs%2FipPQL7HnLIOB&X-Amz-Signature=4e7889b221d411f1420f22eec484e74cc1dedbce6f1237d737afc0dba2429cc2&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX6NY5UY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEnskG4iCQAb%2FhcMhVOJjitIV420t1UcTcUUQFpXHGBwIgb9VN9VILevzhaOkViaI7wC%2BmWEO%2BHYZZ1zzxT6rbdsEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDII6CIThHQIKVlqH3CrcA3%2BS4GeYRekMb3jiX23siCn5o2VgMYgpzVKKp1gYxENcA7jHRpeZOP1bVZTwbtAV91c79lRan2dzg3hc72h%2B0PLa%2FMRtb8uKb9wXWqhdMmjdY7bbq8o%2BiMM72Q%2F4zMDUjy08ll9KQxD%2BlWKZ%2FozBIuK2ccLcb782NBYKV%2FK4TbpwQiR9nRJPOYZicD6t6MBYU3TFQIy16Pb4Jc9COHwE2awxHhZcn%2B%2FIEq1g%2F1JWA0P5yTc8sxurS3HqN1AbFxMuUUGjVy3Xk6WHoFGpX20grd9A5vi9UwtbU2tyD5GnGR9a6chUSrgFwFw5x59SuFnleVsYHwVnpXrSfgZqmYqbeup6WGx1%2FxzYDkdL42p7XawuIBi%2FlCJQaBCdRPyW5E8GgSoIaeq9BZCYAY%2F3uqJjKe%2BdFevF%2BC%2Bd8MPS2wh7nsMp9818HaFStBR1xozZ4foiDxfNddio0ov9dfUOUJMCgbJp6WAn2P7Bi%2B5cKXDlhh0EA0wMESg3tWYw3%2FUVXGD0FhZTwTxKyqxTYSRJ%2B5t%2BpFE%2BZdcOOtG%2BB9TRFd9WKy8%2Bxz4dVfIs307C2r6YBIgvzpFgkZsfykGR7B5ob83fUsddGee2iJXNxGwJnXFLOaQx1t8PPI8BMzPdf30NMKa6jr0GOqUBVCRTsez%2FYZemuSK0VD6j8zkefFir78OgRfQwjaNyQbK2ACrc3H66PyGQQiRSi1O4XunbiCIHNNplt7kZnW3M9R96x85iMdxIvHjnDLyQWic3HymTkiUw3QurgR2cc5Qof55XBQ4vYpDfVEiz7y93bfWIdafT6IKd5c02rR8pihg1ztRaVMDFSWeoUYDfWApbSX1VXa6iqW7Th%2FU0fu8%2BohgB3K0J&X-Amz-Signature=e1a133d1bcae15a6b2691b08efeee86f73f51a8d83a601fdb0c1b83761bc4305&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTUWWDDO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDvZM2nMnBdr2b8zjgWbaLs02lE%2FVkmiIV4KUxN7ZaRuAIhAMUvrHQxOXugXtWc8jmsBmFDZcx6qhMoMLrcr%2BsFH2iDKv8DCEoQABoMNjM3NDIzMTgzODA1Igzm%2FoqZsytnej69qbAq3APmpREM%2FzO%2FUy0DGD9gZQSR8g01n9iIZSw%2F3DbrxeW1QIJi5BqgfTdcmJfEkeKxSJeSE9u1XliKdYxO7qrqYjCqlUhLvBwQjjHQa14TAliQvAn8oNE7EWucUdZFAS4mb%2FcAMtnXgqiUpltm%2Btknqah%2B1cNNf0C1GR5uDCBWR3Ir0LKYH%2Bqeo%2F8DIsVY2ytuuewAwq75VjHrty84WEHDu97GRKQeE%2Ftzg4TaLWRMl6JfcQ5uFp6YLDjG3y9Hf2Sg79gTO%2BHJDwCOM9COShVMSGcTAbNbYFifDgh3LxeKwwu%2B%2F6HE8StXu%2FcDIDCYFksoGOm69APqsF%2F%2F5drI%2BA8X7RewGGqqx06ZEHktLCer0wGxEuBjQOJv09BLZhKg%2BoIaWqefrXZRufsOdAxQD4vEaDgM2oiP3PfiA5WEkkhsXq7Ewyzk9gYV4k1fU2IX0%2Bogo6IiVg9j1XgnfLk9SWYznGnm5fry2AJyuZ0D6GNQqalvzblS6PJ4t%2FZKpwdpQK6YGOAkakS%2BNo4v2RrwKmPEpeOOo1BZ7hX%2FB1dI3Dn11yKgA1WFDU0Ma5SyMQO3c12ANI1ddaay%2BeIh9iqFxRUol842eqO%2Belw91LJHx6tIhydwTSoevuLwc1KMD%2FUgDTDQuo69BjqkAX2dl0tHsutRXGdXT33041YOBc2ydywMbUihf0oE6lNzNI54Gcqyo15ewGv%2FyIfSNtMCt%2BEfk%2FVKIG%2FlGtr1ivxV5pQuNyGvHkoHzAgciVdZ8U9aWpPjC1eVW6szQZTrhieV4LA7LmLSMdA7U4TTcK0NJN5Hyk3P44gO%2B2syqYjtCQwsSUxL0OwXztHpxeotv3VScVQTZh6lTAgCijJX%2FfaPvOrF&X-Amz-Signature=812118d9f73e2571c89db6fba31c4dc044438587c017f8843202f8ec342726fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TVAGPSX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCNhwxyo4%2BuvKqlgg0%2FITx20GgjWgvygB46riZkB%2BY4zQIgDo5KktFaEw34Ze9EdHQQc%2BWGX2Alpu4YzVjxiqLTC4Uq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCDmFdvaK5WawlZfoCrcAzHjERNLgTecgvGIvW%2Btbn1eixGPO4WiONXbK3WzN0tbbwocMKZhn0t9xDeT848oe1iqVuFL5XGol1hp9xlpD6AFWVw4aiLsFfZhqWW0K5Z2YYdsRAMLx1QLTg2IA%2FKT4H07zwXPjAoVxngDBeKk4jlffuaVM9rns2WRqQ5PT4R2rUQlKVmf8%2FqVv06U8e9bFX16tcmCEnGi1Cl%2F4RlhPhspg91%2BbKFUTU2w5cu%2F1XWXAsLOtOKRlhHHCW1D4uwVxJvAmX8nNyqu6kw5YUKQ9%2FxycgODd46LvLN4qWsP2U7ZOxQjViCeFN0xKPr2g14eBeEbY2bZSms0%2Fooi%2BQqsl5B7SZJCsKjoy5s45VdMPxLE8GEo5sjtNMQCV1PD4wbgSoWoU2MYyPNOeDzgWtDanuhHXMWWq4QhkVKepv0EgPugaKw69DXf4IdjDzfKAy26ywXChYSc1uc0vw0yTIvDs%2BYVVbOooJmbawmrjd9%2FBk9kzQEjUv3Lpr1QibvT1UlSuwKJ0HQGXh17f0V89TCKigGjOxr7ihq1ttqH%2BDO%2FPnI33MHXClM4oOvrY%2F3lbuFE5D176vrw5aF51DoH8eRBNuQ1I4viFgK19BwjhZSwUGZFdy0sgtMd7RpOy%2FEOMJy6jr0GOqUBBqvZBbmeuk9DJIdxiwx%2BFn3XmIXN2sA8AiS3nYnxiQfPrdSD8pJ2E%2BnUNk53cjTHVFxU9zY5QEB01hk5y8yQk%2BbfBxO8TkXPv9DcSLy6rS2ToXKdr7MiJ7PvB4ZZYsiU1eXDO99YVYLggsSrKZURtRn4Zr0cZ3X64HNANQ5tI9FjIauAco6FUdaNPeYNqT1ZA9gZgJtnsC5f9CcnvnR6skdFeoxJ&X-Amz-Signature=806f2378186d7f8c136e60a90a5bc0a0ab0bca20c46157c41a6857f2b88d0438&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676WFX5OB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQC4DBizDivKVbjSK%2BwXPr5COZON3UJc%2BtS6LNNVMlmypAIhAMlPfduoE4oTig5lpcIG%2BJUXJrxUX%2B7qXdOleJDmqtYbKv8DCEoQABoMNjM3NDIzMTgzODA1Igw8eApnKBebRTjAI14q3AMDbtho5LG60IviotitELGySvmKN6L7UajoYiFXVzPDqh%2Bw4eJydoPq79wZJqmY2N%2FXnjMQNV4jvwaCl7BhtaqnSeyZbcGaWB7OkOb19FUTG6mRyn6JwMhH%2BmpEhYLoov6DYOSsBIF3KTpWk53uBVf2UmSBQHmdKbZe%2BPs18xU11RMT9Ew6yU3387K5h6NDxIV%2F6T%2FIjjdypsDK9lMlte%2Bab1npQUX3QEskN2FFgrPV6aaWrjeKUhJ5N5jOsqXkuSB9h19Vn3rDBrOiacWmRyJ0kbrzm5iX40rqz%2FRZkhVdwJN2RWJ6%2Fm8C5%2BzX6rUlMGH2QgbgAnVb6da5meyNj1XMhv1R48tHO4yQGU0G0b3cEQzPH0MqT%2FArdvL14%2BgA2PigEF3BB4jldqfiMWotKrhbbQt%2F%2BbBY%2FtXckliiQRgM8mDqXWkswJXjdQFFRX4nPpPIigKUWIjvU3uBvGPxBuSrEabRcgikgXkZ9Gkgl%2BLxDMr5YNQtMYNw7EXFK5AhQ3JqyQMoT4xZC1VCo58KYYhixGb8KxGxJVHguo5N8yaJubcx2LiediSevI%2FcLputYKxIMJSBdKkt%2FwDEKyg3CG2cxaqbgctYpg4nY0ECoyuA5pXF9F5sGfAip7j5STDTuo69BjqkAQjWPmEMuga4JaZqfhV4Ci%2FbxfvgkDlgpMrVxO2FbMGttpgjBPscJa5Z7uSLW4lnWOUFaUvM7I5Rb97ndCI8PKPrkECw3AYxlbEFdxPWW7JGeQ92iF0gYjNTrjQnb4tZMkSbi8cbNzLiE7h%2BlEnNFpIa7xL76InJ2slI17%2BAS53nwbM1VBfbt4%2BpwlAwVSy%2FcDp%2BgQXwB%2FJPFCma9NVhYHo87FAk&X-Amz-Signature=cadc3478bb63b11b4c97e37f4ebca1a03dff05dc79f7a8fc0bf0993ddaeeec09&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676WFX5OB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQC4DBizDivKVbjSK%2BwXPr5COZON3UJc%2BtS6LNNVMlmypAIhAMlPfduoE4oTig5lpcIG%2BJUXJrxUX%2B7qXdOleJDmqtYbKv8DCEoQABoMNjM3NDIzMTgzODA1Igw8eApnKBebRTjAI14q3AMDbtho5LG60IviotitELGySvmKN6L7UajoYiFXVzPDqh%2Bw4eJydoPq79wZJqmY2N%2FXnjMQNV4jvwaCl7BhtaqnSeyZbcGaWB7OkOb19FUTG6mRyn6JwMhH%2BmpEhYLoov6DYOSsBIF3KTpWk53uBVf2UmSBQHmdKbZe%2BPs18xU11RMT9Ew6yU3387K5h6NDxIV%2F6T%2FIjjdypsDK9lMlte%2Bab1npQUX3QEskN2FFgrPV6aaWrjeKUhJ5N5jOsqXkuSB9h19Vn3rDBrOiacWmRyJ0kbrzm5iX40rqz%2FRZkhVdwJN2RWJ6%2Fm8C5%2BzX6rUlMGH2QgbgAnVb6da5meyNj1XMhv1R48tHO4yQGU0G0b3cEQzPH0MqT%2FArdvL14%2BgA2PigEF3BB4jldqfiMWotKrhbbQt%2F%2BbBY%2FtXckliiQRgM8mDqXWkswJXjdQFFRX4nPpPIigKUWIjvU3uBvGPxBuSrEabRcgikgXkZ9Gkgl%2BLxDMr5YNQtMYNw7EXFK5AhQ3JqyQMoT4xZC1VCo58KYYhixGb8KxGxJVHguo5N8yaJubcx2LiediSevI%2FcLputYKxIMJSBdKkt%2FwDEKyg3CG2cxaqbgctYpg4nY0ECoyuA5pXF9F5sGfAip7j5STDTuo69BjqkAQjWPmEMuga4JaZqfhV4Ci%2FbxfvgkDlgpMrVxO2FbMGttpgjBPscJa5Z7uSLW4lnWOUFaUvM7I5Rb97ndCI8PKPrkECw3AYxlbEFdxPWW7JGeQ92iF0gYjNTrjQnb4tZMkSbi8cbNzLiE7h%2BlEnNFpIa7xL76InJ2slI17%2BAS53nwbM1VBfbt4%2BpwlAwVSy%2FcDp%2BgQXwB%2FJPFCma9NVhYHo87FAk&X-Amz-Signature=680b3355a43b741ae75eaf70fde93138d002c63e6427da974ac566e8b3d5de6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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