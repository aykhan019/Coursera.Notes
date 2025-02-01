

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26PDAH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGGg7T6k7OAoi%2BdnVIwO0ewMxoT6unwF6HR%2BP0kF6FIlAiBb1pXzSLBcluYBvFkfPBmioA2HgPUYaLFF6UF2WOiK1SqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPdzNMm1ExYg9%2BhXBKtwDr3IFwEk2QSccuZZd2ExlC%2Fn7SJs53DrNXAbE9gHngowIJ6%2BmIRdK0dQ1GhY9AsCaIHwO2VCst5NwhKbpW91%2Bh6SDjkG00O%2FO7s74te1xTEg73XhPr3a14O7HU%2FYwSBova1SGjf%2FeRH3l1hB4PeeitdfDTX7WTVxBpHSfNg37XXgp2uailVuGf3jAQ6vL%2F0EhJRt73UXe%2FcZErPcvsMMC86Q00U7eo6w7Zu%2FcOP83%2BEfmndJM0R0JD1YmzYzPXGEGU0Gk7fN%2BKeceMZiK%2BzgfCasSfwLfe94%2BgRGo7Ocs4M4FNj94HBp7d4bisbHaG3nz42Bufo0H6trZodBb9X5MlKJmMv3fG3xGqpJapj6LYorsFUDGglQWm5OktEO8MbdCYOOpWNnQulqJhsd5aUFFyhYTaqpD6YrTMS9g%2FrQmNUOfhN09Zg%2B%2Bcyi9BizsyCPZ3hKwXj9fgPSlaaHiAc8LQsdgZHFoVfHz47mNWMCe%2FH1dNfUtk%2Bys0X7qUJ8KgORn7SP3NQKaJ%2BMzbH9C5GXhJMGgtyHE7OehV1OqImm4BRZZndr8qKN8T2h8xTZZECNPFXlyAkI4bpulmEFTal0tizvz1EsTmEJlpA5yO8Z1ORleE0rbGORQcAChraYwhcP4vAY6pgFOO6K%2FBtjrQEUiAAXGzMbivj1vFrpnsUQz3fLY1HyAUJeyEudpXsJ1o7OnVFpPpC2FsB5iOYfBEMxZFbx0cFpqB%2BzuhvhpjbzQUrBAdYF4%2BVCWJ4iykpbkL80UXhyeDKtXeoqKL%2Fne6TIL17QzwjeejGk6s4NWVKB1cokq0hvirIwXoGSXLwlcFWVK54q7SHVLr6uD0LHnAfnimacPHtjZ%2FfoIzqcc&X-Amz-Signature=ad90bab122194904022a94763b50379b7239378e8f9912daf2c4bebbf2a4fa96&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CIN5E26%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIgbCSZi140Tnhlqb45VmQ%2Bt9aXwY%2BE4FyL0wi3IRsHAiEApY9gvVH2iMnRsJQG%2FrpzsjNSrEBBIkTkQ9qt3BLc9f0qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAEJtFzaGSrWPArsaircA%2BO1tUqXKwnJygDbm0mrEs8xNOahhDL4w03gPMG1M%2B8i60n5UNimkLy5uJrFI%2BRNfCWM7TgRz8rpr0AFsJM4%2BYH0wokzsyVNzWn3mTgMsJetoEf31eovM7Aab%2BKobZJRD7FHp5NO6hf0sDgLQpIPkxOG%2FgGplM94KQBrJconfzl9ZVE0EjwqBmp9KO%2BjnFDGtI%2BEW6rxlD0WgLn91qF1H8eHvltm%2FPoAVb%2Bonsrbw04NQECCD%2FX%2FaMC%2F51uIlA20NaliDHT4gRSs1tTcaazSr19nLW5Ux9t3zhaz%2FOO8uUDwSH95ZoIPjGVqo2qE9j3%2FR5CeRgorxp8ou6kS%2BEm1b1aAEARgFkXInokmsPTa%2FNpXxoKmq5QxTzKSh1lOpy9hnIGgRfMe58ELE9reHgzpN5sSCoit3U1HWJOXsfnzi3JBIMDJnxOjX6Z%2F43FB%2FU22pHw%2F13r6ijxX56Q%2F6yvUsM3H0X3Qo9WnJpzsPfJRhmMNflPkxeud3o9OP85rLz0Yv8TQt3fxzzqL9uLtc9sUZmMoYlJgm8AXbUL%2F2K7Mh2ACjN0%2FWinpJYFIhsMtPoXHzdD0Cr8WA%2Fu5z8acqVM7R5lLEbeRw0gT%2FWFRyd4ENgS3mFnWWx8M9dTX85oUMIDC%2BLwGOqUB6FKk5J52xv8BjkM8Tj%2FsxoM4AQAhSfQgA12yHV%2Be5FvYxUUPpQcW2pREtzTpF4326oYvodSYJ%2B3q9Rv%2ByOsIMga1a2daCuTDhy3XnaKUWKFZauByUOUrDYvLaByFZvITNqEp6bHif2D3gD66VrM%2FGsZPwIuZkdpjXYcW8oNbbD1dnOWv3UO8grDMEBfg8g1PPDlbpjBE5nkfXtZcXA1TQbqaM%2Bg5&X-Amz-Signature=30bf9c905360bde9fab744e78d0552367f295c0dba6be951b1f7ee186f389b27&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5L43BIM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8IVx1fifoDmGi%2BWpShMbGCAV%2FZGaN1RP221zj9MUjUwIhAOC%2FBHVdvSU80mn9I4Wt75LrSI1Z%2BqELxkgBIvCaKigqKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2gViCEE1je1NlaUQq3AOZvYUiBmrRH6l8QK6s%2B3aLUuy8Z317ze0fL8y7Y2bt2DBiQK2ptg47fPEgGSkK5%2BWmKUYJtr2I1eU82Yf3q4L04rrB72hWXkrPGWS98Q37z4dJG%2FSWJY2o%2FBQXlFTgG4seYeMmNaCRL5CJWPiQjhBNP0T1rv0bqvPCqCtXqJfNr8wvAHXBHWiAfkCQAf8iqlUoQzXldTc2FUanNiS8iZTo5E5JF1QBHxv9BmXMFg9omIsb3U6s%2BROXgnCJOu0TMUcXWvm1TofxOXDz9C6aVAir3M%2FxQjasA%2FTMc8loUMu6KpVlBjsrtvyUdtT1cbDtVOW%2BB%2FPKYAVgtlwnHUAYhk3UoNxn5ymeazMtVSYPNgs01z3iEioHfuUYtNqmthaWkzDe1HzjQ10mtZfN3fPbC9yAVv%2F0MbhLyQ5sXTY%2Fg6jQyYGnrNoR6hOxuIz93WNOAwR%2Bg8qcnJiEjsp1sSnEIM%2BYxOjpQ%2FGfnHGTa84U6VaEnSYpnY0T903Y3oP8UXKJrbZz13rBUu33h3Hgw1EctJvY0pmu7GrLCvPULsc88RzXMLPfQKrUmmtCLJL3xKYrv%2FJb26Chfakos2lt1XUpPeCT6ifkKTMwFfY3XuqcVBq5SQKal3HwvhxM%2FC4r5zCoyPi8BjqkAaBDawaI%2FjAZi%2Fty05SXSteE9C0h%2FTQm4jdkzPMY56OrHImF2luXD82XBQhQhp%2BEk9BAmnsUuPqX6ooFTjyn8My8UAaO2c24GnFsGgGmLtR4tCu3utYaZrpXDWr5yuBo%2FNoGPn3S7Igdh2PN2t6%2BuPc3KDaJepdIsqFoyTnt%2F5hIvL1TKELaatIMlCp6mv4sS%2FqTbwub%2Fn2XqzOMN2m9GrUqOiqq&X-Amz-Signature=f212f704ced6735b65e73f8b7c2df109066f2a246fd391c2f5afcc328c7b4cf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VR4TQCQ3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOYUFIVzLDoDY1KBUhxHJBFSvKAKY9gb5SuQLvt8c3DwIhAME7fGE9KCFHXgmPCfRVLwiAFeW53JsNEwicD59IKMudKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWea4mCTxswLcmpYAq3AOeMR%2F6OIvnAsM1CGOz1A8Qg0wQGiTPrV24sla%2F104R1gvOPuTjQwp6pjjRmleJthCDQexwcDok5x2gpox7phm2g0rEL2I3YslYlbonYxEP9r7mVNEvtcRVBcjSlzQl9rLryqN%2FiJ9M50aTL%2FcTRuiI%2BAmYzMDQPdRpLlwu72Q%2BIYG1YTKuBUyxNLjx9MQ8Go6lyohsMAi38ytTMaB2k4P1%2BqBTQCjiKACkix03tFXw9ZzVPIf4LwD0JadkJFSVboib83A475ivLBEv2eQ8Vost0JI1xflTbys4RQuYBsUQlzTkZkWCzvp%2BNJuKEF5FkLAamgrXSSeN2pR9OLtZpdghT0PxQDsCEnWQaQPgXBOiU7oe4b4TC0y7fTiNSnpkVwng1cMZ2zLFMoqohG%2BP7gqYmZVnsgT94AZO%2BXcd7a%2FhDNBqRvbs95rsOjDZzYXKvclsRpercd4TaNJBWgjeR6%2BbztKnxMEtfbrklgEM9Wipy%2BCDtPZ512%2BgdN22nPe7T5FSnHZeQiWPumpV4JnLypIqHK5w3zLpiVqBzwPQ7%2BNcc27xKsWeUwtnkAmut11wB4jpE9LY4WHiYtoQtGFiOlHEydrKJyJzfw6uCM0qgzFPeIOtPTxlsaCNf4Zv2DDmv%2Fi8BjqkAU7ERJcREncmJQkGasGMg9QCOzE3EXC63L%2Fi6fLaW8TbU372CP%2FDMjN80E%2FzsM%2FysZqS5ju9zgzIkTtwQtjEX1QpWULG7G0iIg9q6WhFP3kjcl1OBSvC8gF%2FkWfejGRvLInp4A3UqWqqRmDbkGKt87%2F5%2B2vGcMTFiRIOestkaxNAHuLqOgkexxCeAscyr%2F%2BEDo0JDri1PZmXvKE7siBVNDjIh7Dw&X-Amz-Signature=c7b26ba649443747a2c5883057f2153884a98b81500c5341b837a70d8025f0de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY4XAMP6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDeEzGtoWL3sQx9yYUBKWjGzBgtp1tHS74GatYOeot0CAiEA1ceWerBg9cCSH6EbjsbLt%2FoPWf5jdNPfEXM1GLarOyUqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtnSlM9zct2qvtpxSrcA7WITNYGcKhnOsfrEXR0V5n8mmLNz1r%2FW5h2uFxxEhCl%2FfLJx0wW%2BCoaDhwbJkX6HwJjTLvuHowLrh3%2BSv42eEHBGNXJb1elDhWQ2pvACmqEgZU9kB%2F7WiA6ZnDh3aJkYolxo5yqnlCmc%2FBlSrYf8%2Fc7p6ucpVUmXdpMCM0%2Fq8iaUkGMKWh%2Fp4RpWtHbH6ajY47%2FVC6fjqljqQQCDP61ysOeI4qMflk3Aq%2FG2S5rhVXcbxKtq%2F1JU7i4FQBRUlpQCKHom4OMBkzKpwPaR7GbJdi6DzpAS5lBz88cG6JpzUjGTVDwZAWokPLbctyr3sd6AlFSMUE0uMEdSOrjROkqpd6LdNbvzHvACSN%2BhRFLTlvv%2BCH8CGG2njARV4WssNO5NYLhFQUn42WiVCtRNHLh6bM02ArD6PLBQ138QvsTMmgt8h1jdd3ffwFxfpNfzCiuDLUP9UizJlxhPZpJcQtd369S99KDza49ftk%2FQQKb%2Bi%2F8%2BX1jXyKyjXoG07uyG0M6UswGfuXpvVbH0Gr4yex2U6%2BVIIHCzpVn0HnovUMOLWN40y9rDFrhwG6%2BbQpcIf66KZ5A%2BhGy1EZr7Rp90ILVUVQBPrfRr2nnf8Jsp8epSnfJRC1tC9H2YuYJWDegMK3G%2BLwGOqUBTnkmhWWPj4BlPsUxV06hplXESiTalokNRrqi6wbi53inM%2BXCshKzLQCMhxUIjvD0p19%2BoWrsnASPuTTlRjAGkW95ZiqW9z3AFl%2BkrVz8i6NVxkh4fXiDBKUgbstUTwgMh7f%2FIjuCK8vQIi%2BE%2B1mAZfgLGq5FPC93Uqk%2FSaUpwX1RBs7uZL7I166l71oRkhSb5IH0FdCuiNhcXVL2TbmLOFLq0TvR&X-Amz-Signature=6b3a7c9ce42ccd9734d8528b058e0c8327d609477f37281942801e00d8fd5dc9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UTM54PW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaWzGB0D3fQP6L9dRW3SLECfyL7GJDVweHxzwRKjVp6gIgIkSnAYoJoeFPK5GgzHUsjUkRDkvDIe80LjY6HJ%2BVeVUqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFG1PudY3Djiw3y6DSrcA8%2FgSCrn66rXLwSA6Xv5EzJ2ny9Q5P3MZzMRGxxItJqUskhJ%2BweHUMrU6W2ELGRM%2B2XwS3EFVw9B0VwxX4YsBvWOtSm%2FE3gJ4QecCGUks1hvVkyKY1I%2By4AhVOKaIdq2YLmBl9OIbRvgNNP3n0X8G72h8g%2FUPyU6RgrqifOdO483tg2pfAEDAl12AZTDHMfta3p1%2FrEYdLJWSzTFgzot3EMqnH7sePOej4nXX7PlhdFyU%2Bwxf18O%2FBD5BTgW7Hw%2Bvo2axBiXXakwZZtsiLEtZ%2FcTj44OcpNWsr9Y38GdkOO8wmTL21R8U9S1g%2F7caAuyoFYTgcjDt30AsbVqPdQbGV0M01xRy9iDtjTPGmIVTyQvzn2QxwaL%2FkPgC9mYloHu2G1tVMv5N0siNPkOjvavSwySdhB%2F7Hf9OGQnsB%2Fn4Xk7FLsco1m%2BUWnuTYxR%2FpBHgeozjwWUpc6bYSQLxK7eqWORRG%2FBaQhO8v9TBmIcD7GcflZrD4rm5SxEcu3urxCJf038sPCbqSPFxdpWKQiFBfuBeS3LgnMiwpyuCNag244o1lZBgMFyS5XIXnwpDle8Sa%2BPbw122SEw61%2BNFq8Uyw%2Fgy8F5w20ZJiiEbC5zG9IaloBVbiXKEBF0FyaZMP%2FI%2BLwGOqUBWlNHMLrMnMJ8O5pA1O3W5FxINqdyJVzSC46tgy8A5l12LyH%2FUxz2VxyxPg8N1i98bxSz38KVKTt85kmhCBYNdiwBYYUtG0Xg%2BL3XeTG410DIMwA3PMg2RnKo61V3O5yXRs11Hl0DQxmILd9izDbVgcZYLlR0ytlYrDAfUaMm3kFS0tToGybcg3v5166dhSO9%2FVOH5yx3o3kkRWfCyAaABl4%2FmlGD&X-Amz-Signature=26f179b4aad43f6795406b072c6c587a11da6c858e668dc8ba606d2e14cd002e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXOQ7O2K%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpfNTIOESdBfEFEXfQmJUDmFde%2BWcG50nYpcIK9YynXAiBpaa0zCHxA7WLS2Uzs%2BvyywbYAJgRrak7krViW5BPAESqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBxN72rXQWMCrt43XKtwDx5%2BX2Q8xARnjnVj3N0zdPQbDm89cjl4mJI7SpnC4Kufcr1INoGO8HFZfCX9swOh4gwPXUJHHTL7HXgNEqMBbjDmoI5sqWzpvDtx5m4M2f4GlAD9V6i8m4h%2Fm7sYCUxe1BTOFVd5AxdYNfMAbTwIFqd8PZjao1Qgb6DPFqy%2Bhdk2l%2B3lybSv0srCB8jZMZcdQXI9wp6SODTQG3kXg%2BFUXnxbCXEJR9MPrFxU96gXvgygrzZVDzoqbPWGJGqDUc0uAKCplnf5UHmJ%2BNtMEcNj67J1aD8VFl2QTwfPOk8Ij0pR0HZjD3iA0nsAg16Xm2ire0TxbBV0EmRZA72GvHGIfkeAQd%2FyGz2IRZQTY36R6VlKnxOpdyO2RBNBx7YFcVYLowRxbQ6%2FTcowYN%2Bkx0%2Bt8cr1JQXp53KDSC%2BL2W8zYj%2FKjOKAnzAeI5XCH14uNl1Bup9Ezi0E5P6vHK8bYic7uz5xoUsYwNkfCOYTvwdsb0y0%2B4%2Fnszpy8lIf38MExMlN4OX0O1GEzrnSqkJmSF82Nf2BMh8n6YGRbsYj09fYi28iwlsUJFaFQOGoFbiB51CTyP94u0L2wuA2TNBNNBimTfQx50Gk%2ByVJakRSiSy4IfRLNkI1BeXXr3%2FGMqKsw9sD4vAY6pgHcEzopdDFbxA9UbKSGtvwUIyvYwgDSJThCiHwr%2BSh%2B5gM2yMwO%2F8T5L4vtOMn%2F%2BKYA3VG15TVLoyuOGsj5BcmtnwSmGJSQVkscpImnNiuCA45tHYH0h%2BJdxChwm%2BzlV9UKmBrc4XRBm8OfJzw1hSbY7q6DVMDdBJIg%2FaycSySSpM0S6qp797kSqRy4%2FLiSs2SPXPsrpjDe0rStqDwnJFPfE4%2FoAUMw&X-Amz-Signature=a5dc9244df4aaa811a04b8d5b9c436bfde2b536e6346a10f468b521223d57822&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE5PPMSE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FCun6VoF5n9UTQFO%2F4OU%2BgSnMFNu6v7pHAIGfM%2FzHKAiAucPxC5IQhYh2ap%2F%2Fa637ksImaGbofYyxTmDRPMyWdKCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN3eXy945CTXAoX2RKtwDLKTm5E0jdYcRU%2BpP9raUmfZLMEW1JN9ldg26u92EBO4jdVOOREzGdW2uEQ%2FwZUTxnbaRrpTfYitP%2Fjl3p8lNIrJKRbm9FTNWXb%2BIXpBy1FvgdeP%2F0kVib1cz7BK2pgCq9T320rfhY%2FUyU8IiTDIa9uwyjubymb4tS42BYFr%2FU4TrZJ%2FONbri%2FWe5YmY56p%2BQUFWIBoV0LSX73op7hcBKO0EqTuAac%2BW5q8rj59DEAe18t%2FmSVqh1SY%2FBTImlfx0EoNFApPDPGqx9duWelTd3vIIN4K1ogTINK6dr0LppyrhwyTswwjqqfwxtm1uOwHMBR7fmdXZy89LfZZdJjmeBYHzh82sCyZ8P6tE1fONKBZCFhDYHdDgw00%2B3dWX5JCdWrtIe8pE4wYgBpVBBLjYJ58aF%2Fn1HLgEGGfic%2FXf8dItcV6bt9j7n6hTuXWIsR65p6M%2B2AFFsDBBOVED1LpDKUPaUlESzU5qinREJH7Pqi37%2B4MKbhyfuO6ElShqb5lwy6%2B3o%2Fvl%2BuB4a52YjDqigMa5nglH%2FSt3wV4tqD4a3Egl1FszlISAB4lXiYkf%2FdfNnUJ7aKtvjs3uYCX9h0zB2Qd3WbVBK8JcrH6KZPHl%2B4lmPR3OX40jz4cSoM%2F8wr8b4vAY6pgGb1vjPMPBwjLgpnxKovWH2bd2jcddJPDV1YDTQ8ZXgtr4BD4DG7200chteVaNaIvY6FiWk4a0%2Fim4HyWlYYUMn8GoQjesdkz0GwAJHuqKJuPBqHGzCkD9BQknuyCknsfcUNy9g2tw1OwrkvMTgxcNGJ17LowjWkg8FflKEtDY0j7q4WcRuf4kd8Xgq7kABrcM4ATsI8VObpdpWEyb5o2Q4Ra8V%2Bb0P&X-Amz-Signature=9693d1f1af3444b7c9ff1dbd57235e98eacf156c93f5db4fa2a45b81b92c0d47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY4XAMP6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDeEzGtoWL3sQx9yYUBKWjGzBgtp1tHS74GatYOeot0CAiEA1ceWerBg9cCSH6EbjsbLt%2FoPWf5jdNPfEXM1GLarOyUqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtnSlM9zct2qvtpxSrcA7WITNYGcKhnOsfrEXR0V5n8mmLNz1r%2FW5h2uFxxEhCl%2FfLJx0wW%2BCoaDhwbJkX6HwJjTLvuHowLrh3%2BSv42eEHBGNXJb1elDhWQ2pvACmqEgZU9kB%2F7WiA6ZnDh3aJkYolxo5yqnlCmc%2FBlSrYf8%2Fc7p6ucpVUmXdpMCM0%2Fq8iaUkGMKWh%2Fp4RpWtHbH6ajY47%2FVC6fjqljqQQCDP61ysOeI4qMflk3Aq%2FG2S5rhVXcbxKtq%2F1JU7i4FQBRUlpQCKHom4OMBkzKpwPaR7GbJdi6DzpAS5lBz88cG6JpzUjGTVDwZAWokPLbctyr3sd6AlFSMUE0uMEdSOrjROkqpd6LdNbvzHvACSN%2BhRFLTlvv%2BCH8CGG2njARV4WssNO5NYLhFQUn42WiVCtRNHLh6bM02ArD6PLBQ138QvsTMmgt8h1jdd3ffwFxfpNfzCiuDLUP9UizJlxhPZpJcQtd369S99KDza49ftk%2FQQKb%2Bi%2F8%2BX1jXyKyjXoG07uyG0M6UswGfuXpvVbH0Gr4yex2U6%2BVIIHCzpVn0HnovUMOLWN40y9rDFrhwG6%2BbQpcIf66KZ5A%2BhGy1EZr7Rp90ILVUVQBPrfRr2nnf8Jsp8epSnfJRC1tC9H2YuYJWDegMK3G%2BLwGOqUBTnkmhWWPj4BlPsUxV06hplXESiTalokNRrqi6wbi53inM%2BXCshKzLQCMhxUIjvD0p19%2BoWrsnASPuTTlRjAGkW95ZiqW9z3AFl%2BkrVz8i6NVxkh4fXiDBKUgbstUTwgMh7f%2FIjuCK8vQIi%2BE%2B1mAZfgLGq5FPC93Uqk%2FSaUpwX1RBs7uZL7I166l71oRkhSb5IH0FdCuiNhcXVL2TbmLOFLq0TvR&X-Amz-Signature=b2500fe93b74f4253966ad70ba872ae9e0be97eefaf26828282a3592f1ba9cc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645OV65H7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdda8culC7kSqJitS6G6Vqcb%2Bgiyum4ZMiv%2BolvfA7NwIhAKQzpnepH4sd%2Fyq2uzt7duCki22UN1ZKSekoIhL%2BCpEAKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPU8aVaXx0hIQEzjcq3AMxFCn2xEuuaiLmqb0eZBdWIwglZn1YChk6KryALH0YWNDhLKwjvuXzwMAGadYQAvoSnlgUGP1cxNzN%2B52f%2FnN9I0rrf0Dh8psxXeaTFwl1XwOMQM%2Fv814tu1ydSCT60YcxFIk8uQXiK2CWVU0h1uG49DxxZoFU6IIUP4opzwTEA6Pkz%2BlSsh6cfp3BcimXy4SwCbLMqgYe8FoKM8G6NW07dWIuKePBXEGFMnrkdYyKGYcDtv8SDa6mtpQnnwuxWnptOqpIAJHQxxlwqe%2BZSzDrISZr3BF5T8kczCW%2FdIlQRIMpq9k%2F2t3dHY4wiJ2B5Pz68hkJBClc4U%2FvnG3QtfJTio%2B4%2BPON9mF2jHQzIDuya6aL0%2Bk258oRYyHdt6Ow5IiAE7ih3fpLKqYPufiIxBQHwv21TOlBsu%2FWDYdOqLhSTF1VAuFqv174DqDe%2F0CeOkexpYYEOCmf83qHg%2BEN0FkUPiYElBlVwSz0I4Vw5IlX1MhIf07Ywc6gSKIE6JHpnV0NehVsAm4DJk0mIrh%2FtbCVV76sFj0%2Bfsx%2Bpsmzoyf8AeQkmPmu%2BpKIQ7H5NjQ%2FjCicCW4nLnpZq7yqFm1T42B4F8PGOgVR9DxLTxHq1TcWs0J3US%2BAXkmZuif3mTCIxPi8BjqkARWiJuH4oyAtuzpDfvIsVLJf6cx%2BXBNI5SA%2FbEhPXbMFV9%2BCg1x0WYFfPEEFmnV%2BNDFJmoo10309LJKxQmKQ5fIhWJ3TMRniJCee8N%2BvOeHl0EEV0XVJOJkBJOrD2Dh8ps7NlwBe9cDhvQ5QyyaWu8f2fe4TVHO2%2BARFS%2Bauca2bie%2FvYK0IXwtf5S%2FGPpRPmEZj0f2MEjWPs1TGr%2F5QYHA5%2Ftki&X-Amz-Signature=43fb2803ab387866c265f76a06eb403188801c8f89656f7690b04416bedc07dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645OV65H7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdda8culC7kSqJitS6G6Vqcb%2Bgiyum4ZMiv%2BolvfA7NwIhAKQzpnepH4sd%2Fyq2uzt7duCki22UN1ZKSekoIhL%2BCpEAKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPU8aVaXx0hIQEzjcq3AMxFCn2xEuuaiLmqb0eZBdWIwglZn1YChk6KryALH0YWNDhLKwjvuXzwMAGadYQAvoSnlgUGP1cxNzN%2B52f%2FnN9I0rrf0Dh8psxXeaTFwl1XwOMQM%2Fv814tu1ydSCT60YcxFIk8uQXiK2CWVU0h1uG49DxxZoFU6IIUP4opzwTEA6Pkz%2BlSsh6cfp3BcimXy4SwCbLMqgYe8FoKM8G6NW07dWIuKePBXEGFMnrkdYyKGYcDtv8SDa6mtpQnnwuxWnptOqpIAJHQxxlwqe%2BZSzDrISZr3BF5T8kczCW%2FdIlQRIMpq9k%2F2t3dHY4wiJ2B5Pz68hkJBClc4U%2FvnG3QtfJTio%2B4%2BPON9mF2jHQzIDuya6aL0%2Bk258oRYyHdt6Ow5IiAE7ih3fpLKqYPufiIxBQHwv21TOlBsu%2FWDYdOqLhSTF1VAuFqv174DqDe%2F0CeOkexpYYEOCmf83qHg%2BEN0FkUPiYElBlVwSz0I4Vw5IlX1MhIf07Ywc6gSKIE6JHpnV0NehVsAm4DJk0mIrh%2FtbCVV76sFj0%2Bfsx%2Bpsmzoyf8AeQkmPmu%2BpKIQ7H5NjQ%2FjCicCW4nLnpZq7yqFm1T42B4F8PGOgVR9DxLTxHq1TcWs0J3US%2BAXkmZuif3mTCIxPi8BjqkARWiJuH4oyAtuzpDfvIsVLJf6cx%2BXBNI5SA%2FbEhPXbMFV9%2BCg1x0WYFfPEEFmnV%2BNDFJmoo10309LJKxQmKQ5fIhWJ3TMRniJCee8N%2BvOeHl0EEV0XVJOJkBJOrD2Dh8ps7NlwBe9cDhvQ5QyyaWu8f2fe4TVHO2%2BARFS%2Bauca2bie%2FvYK0IXwtf5S%2FGPpRPmEZj0f2MEjWPs1TGr%2F5QYHA5%2Ftki&X-Amz-Signature=37332b3c80ad1043e0c70a946b926d8c5cb62d99843b1243788f106a09b45af1&X-Amz-SignedHeaders=host&x-id=GetObject)
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