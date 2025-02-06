

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLJ4SUD5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDaxppZTRY%2B9HIlGI37b4z%2B21IWCn%2BtlFpuW9hA10HXfAIgO2oL%2FX8n55nWHxFm8e0BPT7rJMaXpXxtkFjz5SR7IB0q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJWrwn9enumaokrMgSrcAxT8uJwxk9u0zyPTY%2BxZTLmt19FzKrCtB3sCp88866rNDvRqehz9KGhF23roeDwyUvvW%2FI99LgKcJ38NOIotXQ0oGxSaWvvjGFO%2BiuUVpnPxtOXbmyFi0K7fIJMyoXrpSn5vUwXeq2ad2QHGLRG7XSQmNfSf25mGlLBzNRtZ%2F3cOtPWoZwjuwg7Uq3E%2FO6rHlE3fTSb97jwEV5CBkh8mYp7ktR7btgYvPG5B4anXTdfif7kNQI%2BtiL4h8XgC%2FAtgpd1h0CiampmNemTjZtVbnH7f5kXFrWEOtYzfzm9LkLa1ydDdAbM2LvIJcP1a1LmAOvhOcY6sQa9DINoYgExYe9nSNpe9p3WTrCglEjxq4dCigWZSpU8BTpGZOMzxODpXcNud85Xn6XZ8kKGnRhYpjGtTZKRePgLcA0laTgyLz5%2B7JTRTeBc%2F850Z8Z4eoDJOzB46zClxnouWHPDFqk58%2BxUXXfPMLvE7k7kX4swXP639bjD79BE%2Fs3FDhVBFgI8A3yS9gK6x1GIBx1VB7waiLGYdMCPXb7fcnqbEWhyIzasUulTdTWOzD2xbGK69lx%2Fp1g8Ewvm9mXxpB%2Fgp8%2FwcJwxYd%2BEeuEAXFQrwp%2Fq%2FC%2FqqRAZdc8qSucNK%2FnpGMJmck70GOqUBLTjmzR2KshC866qonEZ4OycAOJ3FPIQwmB3KxiPmNcoIuLRMCQVjJWpZhxd6kTWVWbo1lAFIlHXyFeYJDxYCtJ%2BvpQsVGCoD5ODtmBWJb1ebuiWFIfEBc3czquaI%2FEGuHIj0tk1V6U2rQqgdfF5h7QvsxhRuiU1e9kEl9n7VfGGKRRfzRtWCus5fi1Wju7qQVWqKaiuvLJrSoSkn%2Bd5hKDl7Fjhg&X-Amz-Signature=0a38323a99d50113db628adc3957df416d24f680c7e61fefb9dddfd8de869ca5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4GUCVRY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIHSPd731MOoTjyHrvhp606120n5rKY3EoRxaluS63VL%2BAiEA8GCfDT1Sjz%2B5Kvi5JLfT%2BjQA4HBJ2MRr5WS9cHJzJr4q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH6DH3G%2FhPMRpu9rsircA5RKZbRuT5PDJ8n8qjLkpjuPHL27xWPdnaFgZmGf%2FIUPF8GiqwTOG5QHPMJy9oVvGN8bjEglRJ24hD%2Bmjeg7fvY%2FdS6RSWbOoILmXSjpICwbIFk56oWszfrxwrUW4PzXk6rOJgyx%2B2J7YiJZE9ED77q3MZmagZ1e4Wt1uLBOoHv1CgU5vwyCGvpmxNYMRksotVT48IZg3AhstTlVf4uJMejtMZiypAJgmM%2BCqEcgWBB8CJSWTPZTHARRT1voQX0w8S8atlZVk0WjgxAivjXCvrf9Nrxo9cXRgXVGzeKo50Wmp0IGlCUsJ4GiHNpZeFzAllD0M6VZhMZJrA7J1YVqPATuBk6Y0KsE1W%2FcQqJ5KCJduQxoMq4v2aZL%2FrjHQ3Zs6KQthDpzeKQPJ8HHaBgI%2BaG9OWXZ58jEdyc2tld3WaTU2IL9TZrYLAI54F%2F57ZkuBtvqzlarj%2F0r1tO8xmXt7ZKMPB%2FZK4iQPWCGZgrn360cbp97ojUcpntTJdcDv8lFTVs3UAjqMdB1PkagUgtJZ1PsjCpD7ZVKeIM306kHJN4Kktdp18ELf4nr74TOwfCUjZ2gPDrjDPspdxwMqD5GNe5gZO0vfyGuNrXmX0vH9RfQx9WlJ8KCvk%2FK8BLnMLack70GOqUBHr2sg%2FRwyxSqIhpTwT2SPRlY4TdWQX4GqIyHc7L2bsjmcJ%2FS5LIY4reZ%2B1150fFIBC5o%2FiO5MUuKaAZgBKM0iL3mdkEDTPBqQdlHaEDeG0tGT03mNoGHa71wmpQ%2BM3oUXTmynndjcoG3sMGT0OK3QkBKCOm61rA5M1DME4UEzij9%2FjdVstvjxaHk3OER41Svu4pNRfy0sr%2BWz6zl0nQ3%2BC5l%2BWzC&X-Amz-Signature=64957a25a3a54153e5ed5a8e272a7b7fff2cde1783bf7f10b983d58b09699f5a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFOBQKP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCz7Yj1GryR4oQ%2FNK%2FcY97ZTGwFy9uqJKoxf7Iy4SHq3wIhANCStYRACdyfmGk3ZvasWJPX%2BOzN4laFysO7ulMo2wmiKv8DCGAQABoMNjM3NDIzMTgzODA1Igys1Te1x1QN3ploJ9sq3AOlu4G5F00LLR7ylVCW6dth8A99DNQ8AstUy7EVtqMbPtg%2FnHvEmG9YajWQ7GpV6noqTNqz1CAWyPMkMWeGTg%2F9D3Mo3SH7WK9NudRmmOMGwB5LgeBcf2N4rJbPDPVmHk0raSb44MHktg1cTVTwBF7Oom2vVJm3JdyG69bgAIrYoCPnW5gFfBMzUqQ8kscTatcsxgR8G5zY9hV1Ht09MRvp2pRMzraBWPCUuMWjIMtdQwgcrK1sHy3lxMLKLGLy%2BpykzF6truWvXaVpFx2YDlMEAx3q1YWbd1eJ%2FDDFE3OtD0F2k724hp%2BTP4PjfIjvoGgmH9glPUzlJuHIbm5j8S%2F%2FvzE84v674Kyd4HOPQz4qDzEbl36wLrB2st3gVWuxkr%2FSQNa4wiJ6blt0GmDMDW1GdzO7u2CEVDVhq2cDZ0OfK3bDyHV%2FKLM8qaNZUJuxjum5UCMy4idt7uTYAkEGootTSc8toBn31CQvpFrIUsGe0FRUzRYxzh5bFaBj%2BYQKysGl%2BaKzYQ%2BUAUvaY0Vu953Kp9c8oz2Mj9WV7ZssaAhS83%2Fan%2FCtlJ%2FbaKkDx6JEWKOEB0BiUKXnmVtkY8KMsLU7X7Gn8wnxltr4tJ87qsxk%2BpgiOM2E3geTl0mwPDCEnJO9BjqkARYsYALweNin%2BU1Vm8PZwQfD2zmTjhbzKmJzMTQirf9ODG9uzRYV3KHMD68oWMwJ2FzPZxpQUu0knqNZTxlLzHz2zEqqkc1Pv8E1fsBY6QkzMKPxRJwPDGPGnWA5lK%2FzSSdJJe5Baw5lW7a7opBvgQ19Af6cUoGiBMGGGUS2of55YLaFR6a6iuI%2FqlBV9FF4aZCQmTkHqjPn5O%2B0NRVzeZX6cf%2Bn&X-Amz-Signature=e715e54d9c45229c713d52c475c3a74fb7adec7568e2e35ef1c4145b54aa44b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZRY33D5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQC191%2F858n2xPtNcxEcKS5xa067BxT601mhoc5ZUZ%2FRQgIgXmftnh%2FcitjWGbfg8vR%2BLaKPNfKJVU61SY2e9QihtLUq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDKJ7mgHDbv4oXrd4GCrcA1lfeH6YNuxoHGIrgRDbti%2BWim0EO7BhQCe2UIekAH2Aimo7wWtGLREXoaYW8lQBFES7o1PTZRIw%2FFWyfkztFhdmSNsYSAKJSOtw7MXTPY8LMXvJttmoCXqQwiwNTWg%2BPVO0A7kuAV346Zi299sVYUbKWzzhxrZMXoderJLMb1VLN0GlJsv%2BQCRT5hdNgbBDAHIGiQdwdbFirgHcktl%2FRF3CRUA92zeJHqbjn9j9B%2BRRYLGjLiU7B%2Fcl6jLNrl6uRdOY9mbjWrTwGxmAYdy8kNd3P5EEhcIRLCtqz3J2%2BneT7tSkbf0eXx61n2vBSGRGeaAmNEaXAIBvaKNc5v4oAoBO%2FKAvkY%2B5FykASveJJvGxmSxNTEIIEiMVLrRoaQkUft%2Fj5QXPfMznVxvcFOZG7b6%2FxOMwedD20rwl7uXDt0%2F7Go%2BS7Cf5ibjyM2KnWScFO0fBBXvDTtvs7%2BW%2BLuitAy%2BOGYtyox%2BplzzzD12NNWskDdfdGt5uHyZ4A4pOSBZPdHnILYR8x%2FOkogSsuZIULFHhg44It4b8FfEJ620RgmEe2qeR2oywoMlsz%2B4guatvqVgnTIcUrTLUDechwsfUB6weBQAzCoFwK7Zy%2FDxJ4PqLecdHqpIV2Vwq02JBMKGck70GOqUBecOBraC5mmqwRFTKD%2Fb7hdXO%2BCU0Mv9M8IVJGDXi3rY5xIW%2Fx%2FznaRg9fDWPcr8iygeOPGZkLuShEptXWAw2zl%2FjezE84hTtcnwWbCXAubtMTgtW0zyqTmSBWOLZ%2F2ni73PBpz5gk647pBCI6cfapM5LV3gCn3mml%2FeN2vFjkxzDeSwF7v32tzub0pzqx%2BAuba4kpzGuMoSpZ6DTWi2jR%2FlB8POk&X-Amz-Signature=684c9d20fd78c7b64fd8a1910bc77216310724be232e27ecbc6f9434d0254d80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XNPWDZC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCICvQ70gitcma%2BWe0LUYL1Me9S%2BBj1hR69PlM5QyT6LhAAiAyhZCzr3BpjYQg0%2FfWCw0zlFnUqGjPXFMxTbicauBk%2FCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMy42U3a%2B36yjNigkwKtwDT47l1Np96XNUcSkk7lOiwo%2FSw0Db2WeU60yBKtFoTNwIyj4vUTapxsl7qtJdxpqJhnYbH66dA%2F97WRiqYFxA8fTSdEMrNgwaqkUKFibSXzboXCBiRymmIcdHCaOIskUsvWtql1WgeW%2FFxhp11qf6%2F5LoYGjN83pJQ%2Fm2H1QPhWkt4I4axCwJ7RJ%2Fl857JfnVlt3kApCECQsY2y63R9tKjwEePZ45qSel4ExWWGLWHKQZmaf3gmNbHkK5PXOjHhA%2BXG34dzcMeAvK6mb0ktSaAB1UAG0yoTCuYXau8gO55yRyCxs5kHoP1AyG6ZT6GVK326OIvRzcybrdxDZpF8nrLbZ%2FKDBi48vu7HWs932Xqw6sLnnmLIkKyWue0SneUVUk4r2qrxan29nSX1HFfuQLGlB811xAJhhUBZJxmkGXWSYLHjJtRwK1FMf160l75wJ1r4HzZR%2BKTyiUojdt3KG2LzwfpuWZp0Hhzf0oNuW3Va32lZDI1ym0zIvMsrCQfqPiPW1kEc56obzf7yEi8Ut0B3Bu62%2FMZeNm2tDyFzvcFJ4Vn8N3yh1vKrlD3TyoJNsLZpzkR8f4f6lpp%2FydiFKTEYP8QZ9BRj%2Fjh3qp51jtjBkhuTM2iNfWF5k2OykwrJyTvQY6pgGBv3zCbthpN3ob%2FezmsJL1cjRNF6edRPKkREuR%2FpKjIgmgeLglcLm1J%2BeH8O%2BRjtCk0ZV6M48CTfYsEHPfd08YI3MHhC3D9Ee%2FdOZe34XNo1TJ6W5tJ%2Bc%2BQof2TZuGOmCiRex11p35rXN3FAc0PxGzVOiDwRYbX83gqu0bhd%2F7mzmNZ7uU35onxatucUrxiOM4IyapxtUCzRu9Adf03q9wlbGXOmIh&X-Amz-Signature=0a9e91e16bd9d34b447b4750defc41d758015a950da1e73b545f3b5945e05583&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=35d79774bd612fc01a516aada211ab8074d04589500283376de2c07b11ef9770&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666G325JMW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCyrHJXB%2BOXiJNtHZPxqHbU1ADJIOdvV4rWQE7XNV1EeQIgZf5%2BZTQ1fJL%2FKhB%2Bx0cBpwtk76LARpj9kIIe9ZEsz9Iq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDA4NQHem2j7QPa7QVCrcA5utL1%2Fl8THgJZBTTBO4GNJwOdoPM06nLo3mL5Sb%2BXI9FGHlPaArDeGZG3OhBQbeRPXVN3BLyqZKrjPVqe3h813vv%2B0qfD%2Fh5F84sljlNeEGExZH%2BZpAQexD1cNAQCEJfWwXjdo0cyasqLTCFiUSpYdGxzhQr8xvrAYbSb9yYgw0Ec4XIzRJthfDmgvzfIYjoF1Z%2Beha3UyIGRDfdBYaUaV93p9JAyl8xGZvnAmy6SraEV4OLrXIfHOMP3mIQsukTpAhzKqiE3zU18WqTRjXEkJDpn8ZvliCFTtG65auDvyrIJpKru0LLJ17oPwb4cZEDwhdg35GOcps%2BTyJ2di%2BVwecjyBLVLehDJjRnDv9pdotN3JdhR8GPviPwJ%2BItjMEJT%2FYp5anKYUSp8SIp1pXjRX5Jx4gwj9lSK3P4k%2FLOyYrwC3OKDuLBrNY1epYI1GrtRwvA0vWVl9xrMWIi3UDb%2FR2pMqeb%2Flvz6KOsg81QRtoLm%2BonnlOzN1I19%2FxbU8sg2kto5hNXXjpBPd%2BVZEbRCvZmk3jXdCwm1U9MN8dt8gPnurhOqmGuZ91CZ%2BvlL8DyHIhT9GMgyw2V4gF%2Fh4K0bW7g1YMFBD6prAtN6aQpv%2Be0aIdfMvRo%2BEBO8G2MOubk70GOqUB8DyVoO8OVZZXvDJogWzEipjbdj8bOEPWSBqgMLvy0mTUZt%2B82Cx1ELYncv3MRcD4SNZ%2Bm4P8simlYkJnSVuso5rZXnDHPKFbuPBieJQZ0z%2FtX9gV1N5w1h2Pugp8Oesok0kxeCsOEkYhjPmtFtPvobfeAxG%2FBZ9Vghj%2FrxcOaLyQle9S2Ghvk5kgV%2B4GTU62P1Zsvpgr6w0EiTF4O%2BuF1V%2BgiIdI&X-Amz-Signature=292ed833cca4566df14c83242713db6a0022c9261854bb2d43cae17639093eae&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635LJVQ7Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIBniJR0OWeJeYkKE7x9RusCnVGc2S2XJ6z%2FCHbtEmGR1AiEAt70TkumOOeTrVw0osdSwIYm9Wnyjm%2F1gpcej1oDU0Yoq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDH3t3KLpZ2%2BobYQm8SrcA5YWrmuzHv17nGuNdj%2FIvR7sweZFEokf8kOScmINOlUHxjI8T4Qk3CTAUiQfBkVC7Mj4pRaWiUtBDWMiVnPVEk%2FpHSAfh1cBBJDWHPuaSzFU1jZtnXURYUmt5JAnC9K3hWJ3VYXKSSCgnX5KI7ACe4d%2Bp1uTgcOx%2B67qToGLP7QjRQQ0WVt6sQfvtVyBhA7ZemSuvweVRWvSpBdPtppERrvmNlhtGhkr%2BE%2Fu7wP53%2FPJJhBEXphrCheUVUWU0wVsznN3%2ByeYJCzR9Tok9g8z6Idz9IUGt1t%2BJtewc2QA8sqfZstwRTF%2FcR2UH5th8qzjM3QGHK8pUzIyT5jfsxFSn9OeLUlPxMeMC9cqJG0RNjz8v2eQlYtHcBJEyMC5F0K8OSXCA0v%2Bj3CHzU4J2CsLAyjgtiv%2BoQiXmeci%2BFa%2F1fErNw9aHc0MFaEWinuBkgSHwtT%2FsNzTEh1j61dKl450gtz%2BpbiBaeV5T3%2F%2F6u1FbanjwXdh6HMQW9WlULXLNY8NCs41WIz77muAdmPo5xkmNaHZxwBRoAAfvF9VdXE2oTGs%2FmcphUnQMUxI4b8hVBB2tP9fcFITmEUeRMZ%2BS7MF8Tmq8320fIdQOiETCD%2Fs9QxsHj7eYc0xyR%2FSG5jXMNSck70GOqUBdHGkHW4cxvjrUN2rcS2SwKx1xNP7RB5CScNX4D2YLRfb%2FLlHKLgVd7ykW8jW%2BiQN9OdjlbuQwI74tEumgyTdSKAHWMsuPH%2B6hn4PvqzrG%2BiS9bXFEziAh3KzPEuU918Xxng00YVHZag8%2BNolN%2BVgFCuEMigWuirBmH9vY76iDnqT747ldUoCvhlny1Ve5KmWwH4lVGpM%2BXvhRCC4mJSZFgldTUOA&X-Amz-Signature=0b42a950ed0724b8cfd7694cdd5886d892399db1095a72fdc6ab48010099e969&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XNPWDZC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCICvQ70gitcma%2BWe0LUYL1Me9S%2BBj1hR69PlM5QyT6LhAAiAyhZCzr3BpjYQg0%2FfWCw0zlFnUqGjPXFMxTbicauBk%2FCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMy42U3a%2B36yjNigkwKtwDT47l1Np96XNUcSkk7lOiwo%2FSw0Db2WeU60yBKtFoTNwIyj4vUTapxsl7qtJdxpqJhnYbH66dA%2F97WRiqYFxA8fTSdEMrNgwaqkUKFibSXzboXCBiRymmIcdHCaOIskUsvWtql1WgeW%2FFxhp11qf6%2F5LoYGjN83pJQ%2Fm2H1QPhWkt4I4axCwJ7RJ%2Fl857JfnVlt3kApCECQsY2y63R9tKjwEePZ45qSel4ExWWGLWHKQZmaf3gmNbHkK5PXOjHhA%2BXG34dzcMeAvK6mb0ktSaAB1UAG0yoTCuYXau8gO55yRyCxs5kHoP1AyG6ZT6GVK326OIvRzcybrdxDZpF8nrLbZ%2FKDBi48vu7HWs932Xqw6sLnnmLIkKyWue0SneUVUk4r2qrxan29nSX1HFfuQLGlB811xAJhhUBZJxmkGXWSYLHjJtRwK1FMf160l75wJ1r4HzZR%2BKTyiUojdt3KG2LzwfpuWZp0Hhzf0oNuW3Va32lZDI1ym0zIvMsrCQfqPiPW1kEc56obzf7yEi8Ut0B3Bu62%2FMZeNm2tDyFzvcFJ4Vn8N3yh1vKrlD3TyoJNsLZpzkR8f4f6lpp%2FydiFKTEYP8QZ9BRj%2Fjh3qp51jtjBkhuTM2iNfWF5k2OykwrJyTvQY6pgGBv3zCbthpN3ob%2FezmsJL1cjRNF6edRPKkREuR%2FpKjIgmgeLglcLm1J%2BeH8O%2BRjtCk0ZV6M48CTfYsEHPfd08YI3MHhC3D9Ee%2FdOZe34XNo1TJ6W5tJ%2Bc%2BQof2TZuGOmCiRex11p35rXN3FAc0PxGzVOiDwRYbX83gqu0bhd%2F7mzmNZ7uU35onxatucUrxiOM4IyapxtUCzRu9Adf03q9wlbGXOmIh&X-Amz-Signature=daff8a383ff603e596d017dbf1815653c4b8ad1c849cd2a794db2a59c1905233&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z5GMV3B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIAyDIJRAy%2BeULHf0KNS62cABJA25G%2FuEOH0jT6oRIctkAiB6NLWR0YlG8u7WwPYN%2BsAS8jzkvwuDqiohRnnfQY6dKyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM0szZL%2Fus%2B4xSmKwhKtwDesCDu6C%2Bi4nXa1m%2BaFrpy44iwYTfJNbZjUKksORHze%2FSuFSJ9pllwGqVncuj9q2VMlCaLIFzD3rcJyYwTcea6%2BpzfSujAzvvxmihKi5KO100EEWdA5LaODHjuj7R1g6rtJ%2FUBrAnB0sDIKdF%2BshUdBaVOKEDQWkEtXd0Z5zjplq0CUkkTVZSkwxTtxFSRt%2FNIB%2B6zpCxgWfzY2C9WRDgRJkeyNX1h2TUaelLy%2BeZRkTUY1wfhYHDBIWQcIYZnxqLTheURwg4wAKzpgBHfUrS%2F3Y%2FHCp%2BzuyVAniCBxkwA3IqPYlnEGdHxidZIyRiRmKaKfclqTKIasvUtQIF9EjNVsFijpXAxowqlrRkmX5mMWi%2BQjLSNzcp9XELwvecl0%2F%2Bba0%2F8vyXSEzU5Sey%2BQhsOJ99TWsMktpJBo5pxEKZ9VXv5B8fTt6%2F0NKoM%2BqgpRFrug2LrrGY9n%2Bygj%2B%2BQBc6grTvOcLhMPAe996HkfS5pjgnNOgfQvHlHe8LMLUWDuNNgTN9iZd93vGSDP1%2BC6kYMvEqw4zLSyW8zWbE6rW7LOpYnBHVVQHfBlK8eongsgE2CjI2GwhwoT6Ox3MF6naWbOHYVv%2F5pqPxFFIW6nAUoYiCuBiXiV4Ruu%2Fl9KcwxpyTvQY6pgGqdfb1WfkctIEfVVlrKgA3giog%2B9R9XKShU4FfVgDyecnEm3r5tMJ6Tk%2Fx1Y0XnbJj7wXiD6402mkbGVRoaKjWMSiKxWz47gEn2amJezndAz38RnPFa59C9qoCyxcYKHUPg0GhctZfY3htWoMU2kHNgL%2F%2BFo2JQ1IF0ExkFaVn5vGwHILWOGR2A8xWmi5KG6gzYjW6uby7gjwFp9a0H6bOd35oQamj&X-Amz-Signature=c4f19fa4e0e26fbe8641dacfa26f2e8b6d14d7474a6d53be13e14f8bee2d1c99&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z5GMV3B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIAyDIJRAy%2BeULHf0KNS62cABJA25G%2FuEOH0jT6oRIctkAiB6NLWR0YlG8u7WwPYN%2BsAS8jzkvwuDqiohRnnfQY6dKyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM0szZL%2Fus%2B4xSmKwhKtwDesCDu6C%2Bi4nXa1m%2BaFrpy44iwYTfJNbZjUKksORHze%2FSuFSJ9pllwGqVncuj9q2VMlCaLIFzD3rcJyYwTcea6%2BpzfSujAzvvxmihKi5KO100EEWdA5LaODHjuj7R1g6rtJ%2FUBrAnB0sDIKdF%2BshUdBaVOKEDQWkEtXd0Z5zjplq0CUkkTVZSkwxTtxFSRt%2FNIB%2B6zpCxgWfzY2C9WRDgRJkeyNX1h2TUaelLy%2BeZRkTUY1wfhYHDBIWQcIYZnxqLTheURwg4wAKzpgBHfUrS%2F3Y%2FHCp%2BzuyVAniCBxkwA3IqPYlnEGdHxidZIyRiRmKaKfclqTKIasvUtQIF9EjNVsFijpXAxowqlrRkmX5mMWi%2BQjLSNzcp9XELwvecl0%2F%2Bba0%2F8vyXSEzU5Sey%2BQhsOJ99TWsMktpJBo5pxEKZ9VXv5B8fTt6%2F0NKoM%2BqgpRFrug2LrrGY9n%2Bygj%2B%2BQBc6grTvOcLhMPAe996HkfS5pjgnNOgfQvHlHe8LMLUWDuNNgTN9iZd93vGSDP1%2BC6kYMvEqw4zLSyW8zWbE6rW7LOpYnBHVVQHfBlK8eongsgE2CjI2GwhwoT6Ox3MF6naWbOHYVv%2F5pqPxFFIW6nAUoYiCuBiXiV4Ruu%2Fl9KcwxpyTvQY6pgGqdfb1WfkctIEfVVlrKgA3giog%2B9R9XKShU4FfVgDyecnEm3r5tMJ6Tk%2Fx1Y0XnbJj7wXiD6402mkbGVRoaKjWMSiKxWz47gEn2amJezndAz38RnPFa59C9qoCyxcYKHUPg0GhctZfY3htWoMU2kHNgL%2F%2BFo2JQ1IF0ExkFaVn5vGwHILWOGR2A8xWmi5KG6gzYjW6uby7gjwFp9a0H6bOd35oQamj&X-Amz-Signature=7c1cf69c8188b97c3fc6b6c74904b3a46790997168431b46a23a28bbb0709ca9&X-Amz-SignedHeaders=host&x-id=GetObject)
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