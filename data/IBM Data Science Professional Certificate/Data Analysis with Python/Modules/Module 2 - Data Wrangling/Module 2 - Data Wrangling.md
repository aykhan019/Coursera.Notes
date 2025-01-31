

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MDZP4YM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOEVOBHo9Qu6rgaHS%2BkrE2A40vS4nH%2BEbp8A7iI%2F9TsQIgKJtIjlcWSDou0RleRJJ31mYZFHtdkNS2Sw2CjnDjYtgqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIi%2Fev3TTH5H7to91ircA5vgfmYLMKLGIRGs%2BHNxVM%2FokEH4FBTTc9kZD3Nl8SL73IgBK2ZqxiFl4E738BLR9VmnDOvtO5Af%2FaP%2BYXA53oa7D%2BykywYFFKJ8LXjUGLdChsJeseRG9c3BLF%2Bwc6bAJ5I%2BCR2LoLydZO%2FRWVCY%2BtgJ3lpCnq%2FtoJ181e%2BGV2oGNtCZvaDGuwaStE4JfShl8z6bo%2BgEDxSDxxQNVdj8gL9sLKULTMbdToxGbl6XzdM8AKwavBiBYs8icW%2Fcpu9OsPVRGDBQGSFKDckcPR1Yfx6QM%2FnoFLJ7dOaZrtsn4Hcu%2BZSvo3%2FbF4fxHsFJ%2FlOgUOzDTf%2B4o6v1OoJZJWf7XCct9iG7NPpL9ezBtqqfzuwLT3dL26zZyMHiYamFIyIuXOPtUrOrxJlogftdl0Doj2whH8If2IjGcLdwHJIsuErdcULUuYLRHdLXamnlhNC8bVZ4U26IMRjbrB19gScjJ4AmuaaKMZD3UNUlKqxWm7IJoLLGSPMpAbtFQECHuG%2FW4bLQTFz3yOT48mpat%2FmIv3kmhmi2ODXq8xNIq6Sgi2J28jPm5K6u%2BNPXOK2FEqUnTDpKwDe9r82bArn9M8os%2Bghp%2BS9zo%2BpxPXizYCny46M82rE1QJ7Uxhd2ajDyMNGj9LwGOqUBXjfyeKN622lmJ%2FTiqdiYSV7p%2BcJZz8VyXfTOyUJCYs157x2TD0as39g4LiXFOkJb9anUjBF9ltRMMi8PQ%2FwFbuhA6SMcM4tkUT7h2nvxVvXTwje1TmgDQt74rlVsz0FAcYoM6aNU8VlJE53tKmC%2FeESTnpPLUj5Ij8ElM8bTUyNQTUfvrfNDY4k8aPZDNZroZjM7X7MqSivrXtNUrptLrB3l5%2BpP&X-Amz-Signature=6c7d00cd4017edc7f8d0575ff50f9c4b073c984b16cbf189b23c0a972821801c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEKXKDNU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2DAs8RKRH%2BjHcV%2BrEN1Hfk0DWTc78%2BnUVdQ6oh27d%2FAiEA1KeupjTCO46qhSqZ2zkw3uMNcj50Gzc1Tw7vK4zQRo8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMiroGjPvSD8i15oKSrcAwjN1DWHs9Q9QWe3%2FbUAUuJhDk6xttcPUZGJDY4RmBaKMaTdTuHbzTodUxmMQiv4Q46QSqTwRocTUFsm9WaOeEdtx3ka5pDlpJ0i2e11CeNG76XoKZSTxbgi2%2Bub8NWbEyoNPpBz8TPaU4Jaxu3MzxUqE9%2F6XpX3k8L8sZwB3ESp3eqKhzhUn2%2BaMH7ztiSukVY5yq9bAddjjoC3qqZNgqrDjQEAHhXUPYxYvD1A6%2FMOZBh8kdmkp2CHx7U8gyH%2BFLZfNBsuSbbY2u97EO5vBDtp7wV7OzN0bEipTJmpKchZqDgSYPFskiMG7sUu9Fno4l0hDecQs0dKoMXvhfKkBQiHRcL4N7cMpfYn0fKDw9exkeCg12u%2BkOrboYI57yhhPuDdQMUaC0UsC01Bf51wotksZkCD7IGHszmewz%2BqT%2FBsqD4dPVbWRaUBB48zgERy2jC1FmKu3IeWGOHWg%2FB2zNHF20vfK%2BoyOOohkSYchchbpBJmYm5ZqTlcCSMi0fqtfGlYIn6%2BXDK4narVU7bj0Zy8fkE%2Fv1bOf0%2F83xi9EScybpvTLQMuFTuBtBZB7FRFkI2b54BWRqKpSNABUDjh41rMjSwH1gdMdLwQs%2FU%2BJa4%2FcxCJV2i2H3%2FWVOfdMJuk9LwGOqUBtqW8SKUkUrsNR3CDVZiB2HtnKHov7Y9zv7g%2BcKDK5ffdW94MV7OFK%2BbtYhcoXeYbVd4wDp%2FcPB9UbiMRZ3bknCHACr91x7%2FzYfLX79VjLe6ymZ1LpfJH60erDPXBcHZFP%2BzU%2Be%2FCLuVhxo02%2FswNftoY0fT6wwqkxe7xzrx7IDy030cWwPiLUBSva4wRL47l8xgq%2B3fnLl0%2B430QW6fhkgLqfV2D&X-Amz-Signature=788e564525ca40e2a8329072b09364f67e0d012aca0c1b1a76fe299aacc6b2e6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM6C5XHG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbN%2Bb7cNcA%2FBf%2FVBx%2F6rY2%2BJ62FaEqyHzBp9waXPSiawIhAKbb%2FqlZIKSfO7bYYoOjVJUawTHTTHWona2x05FIqC9NKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwiQPDjczDrha63%2F2Mq3AMv99byemOo6PjJ7Tfjq4mm2NY8uQtyGWigfyzxwQOpQB2UNTwog3IyTrYxTW%2FUCtusSvZ2gN7ak20Uoe7nwJSo5x3QOwmsjaBBu63OrdysKp4z%2Bt3%2BWkX2q%2F1%2B9QirEyMO%2FHyTCVxfJbKPUN%2FCadWJQK2XYxqV3my1sp2TUMum9H6SNPPXl%2BpyIANezJg9YriPyRuk1ydYVf%2FAtX5M9NhAh4DCG3SCKPio3s6BBjd6bj3HY9wa2DtEaUI6BkUdk8NXZn7G3hf%2B0XQgi%2F61nekpI27rhrT8%2FEw9VdOlHcO9gdtvi%2B5%2FIKg%2Bn%2BF3%2Bis0YFQh2jEso1P4IJURzqDfSLldJs2tVMzzaRqQMkGXH5Mn3e4MS7IQeLwNARnMJlWAJ0mru3GMRBZNDaa5JnWdwlIrWie2HKmG%2Fh%2BhnV%2BfvDlYd50bLNpTlnk0Q0oG9%2FK7SFjaN%2F8CSv1HIXCF%2FpZNYWXj0YHeRuyG7FJMa13v56XIBRCqSuVeKLExOg9lTiXqLkS3Q1vLFzkzQDENpmsgPd0avO6J5%2Fw98s5wUGtDb%2Bx9GD5jYnClo7%2BpZ8X1fofZQJZqLqvBqobWZjNcbf9096Kmc2iRcwMRQFmQhDW6CbSjIMo4ZsmuPBh3B8uKpTD2v%2FS8BjqkAdPA40Ebk6GUdsG%2FBnypSujaS%2FspOBMt35AtSBsG34R4axxSL30jGKt2%2Fss8%2FHQi5uzuBD3OCmeOewO1lBsgJIbFRE2YXLIO%2B%2FoC%2BdMrjfEyY0ciC%2FwFTOPaOonRWa1sWMHdlLwHfpuylAuMJkcKkM218JgDKTLamNuVcDfaQJeOL2NPGFH4ukmOyLHxeHAMiS51h0OXeiPSB5UhwkQdhqU2BSRu&X-Amz-Signature=5dfb33b0184b89d370e46b601f5a58ed3fcc17db9a1fd9518f0543204c1dfbc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIPL2PTL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAQ6ZShuKTwZFO0T4J67tA2MRBvVJxO4qzQo3PXcGhHDAiBjmY6bu4q5G6l3dXpw64XCtiyIi9ASKyJe%2BbBzL9didCqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQ2Zb3SUcArvgYb%2FKtwDYoHCBhgpMxasRsAObAUHLq8P3CejF2CLAF7tHivBEBcU3YlvJocTNKRxg5tfhuGdW82QAg6VwpQpujM3YlOWrDnQmhA11txg3Ueob7K6GxZJBr0QF%2BOyfkzxu3kLHgVc5oxXAV3Jv%2FHBnZpLiDHB%2FHeG7DgFW20mvD0HpJuskPpJIF9EDSLM%2FS0Euo%2FhG0e4y2iGtmyV5YUceU05cqAAVSidSI8drGClbS1xwgrH6mO3N0ouEidZ8OFTdjPht%2FtwtoEvxeFiUoB%2FYDo%2F9DIJ4XyTsiWoOKl1KnwxzfIL8964cOnMkZNVpG%2F8Y9DJboUuvn33OJvUKLE853kCAP1Q%2FEsuk1rllPRunYyNKbctPRXsobDN3X%2B5tT%2FdwnhRlBp5wyNM6quBOE1stotyvh5BJayS9%2FucEsMeJz%2BmytD%2FfbJnLM7uI1TGM7qISTlp17QG2POUMoQTeib4M0wneEBL947fpaMVC2w4bHRhEyNlmpjdeq5RuXMgrEOeMd1uCg3%2Fzu5ypde%2BtveLC50y%2FTa0AWnlaUv%2FPvC2xJoQVekxAxEEI1%2BkfWkZQ%2B4neAf7edzKBQ1n8havKf1VI9Bxq1AUhnS4WbJFdVrxeMdw3etd3lAnxNt5N%2BS49X0AQ2cwg6T0vAY6pgFuGfFjNKVU43X7l%2BxCxkEZ%2FKCuBMLXoDbbbcrA3Fcn8PIakw%2F%2BC2DhG0QgQ10SrZjCwZTZwX%2Bmfv3PXk3T181HGl4ZAl%2FzKfCkUTAT2Dz7Awu0Q719aWv1ibxnidQEoVif%2Fi5ypm10UiLQ3tmbYbrqcr%2B3yL0B2PEK6LpKY7gSu6Hf0LtOwy4mdCrmahptg5E%2F9MSxicMvNexQuWm9ehPr1kfWT3Hg&X-Amz-Signature=a80cf6869d9ed3354840802f33597b3e8f93fe9ffc79a1228cde1eae4ac8686b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USFNSKQB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDj%2Bd4a1aCy4fyFTTRo5ybPkh5DmtUcQFX62kPeec2XtAiEAntTFSaquTFRM3vs6oTnoFbNYVumT2Ir1sM58xFVHfYUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDw7iXe09zmgbRVJJCrcAySBWSPZBIQCBdDUZWLemKVHY4ZXYc3lBkotLTEH8zylG22yaiYHHU2dS26m6aZaU4Pft0KcM6vMk87V8ca7sA%2BN%2FwQ5CWCHmOHjLgCYsWs8D85YpQymn7HZ0x1LC%2Fifn%2FDim17kNPIDDOU2z68NsBw3Wu0sfFQpzgAx3NRU63uGkmEmW%2BOBX4elhhCXKig6%2FNWMuIoOzOeM7I8IIOz6lE%2FJyHt%2BBsTkYzfnwXsWJUiKujLGrPr85VF3EZViac68uM%2FBTBp8z4AxyLZUtyMZyH6FmT%2B%2FCIlzwaK%2B8jsaTnVDLd0nI%2B079oOTa4bk7RQREtBRuJw6hcN%2B6AnrzzceRBhtXOEhiXS2%2FO5d9PiZ5wHtGv3KlTtdWsEbXLEtHEcjRrZ5yI%2BV%2FZ1v4%2FOytNLXSucGieqrUJaMx60CWr3O%2BIQfbjQ%2FJAuyFz151bSJlRa2%2FyTFuEjsEcjNaDw%2F0dZmlhtzD71sxvySJdJy%2FTeWVIgDFyYsvmJPQ3O%2Bc3B38XEF536A9zpjTiq6d1gzQ%2FVR7ft5dmw5i%2BCWcRLS%2Bsg1RCqhTos6NGu8juV5LF2MiZuQoOxtFKsW87nqpM3fXghYMluc%2BZFddCiseveVYSzvBk3SsaKujsahbytMqtNFMJuk9LwGOqUB%2BabP7Ix3EkE46LQzs4O%2FxEoOqlgF6UPQPbxstmXOoIfkHzr%2FBF45zcvgfeewf76msQSlDLopx54Vs4HRkXf0nX0VCpk7405pUFJzqgdhBt7I2ZudGBmudPlMXajU4wPjeGqYor%2BYdUBd9FacuqkmajPVBIK3muDJlKYaJOXPMo4LFV5wQi55sc0POog9FF7jIXZk2CGG3fW%2BXo7LwnYDBWA%2B5lJG&X-Amz-Signature=b41f08a3d351017fbc2a187edeaa2347371f8592f20a781f056fdf04c8b3bf40&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHHHJXXA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvhbr19baEhG%2Bds6mC3yn30DM6zWdKMtoM%2BrTWzS1MbAIhAIMul7v4kTZSJPJTIhnO7EyPJ88egDhOigpkKwouUW5MKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxM1dtQcxT21PCly00q3AMmwieHTUEER9tB023zImjz17pN%2Fc68UyEFy%2FZQUlJ91ob18n1G%2BvtQIzEXckCxWZu4nbIiXvzSNyutF%2BTXaH1uzkVDUKB%2BtufhXIv3d8cje4TQvOUZxHkYsPhVVrOz66m86Jeb7w8XHukYiUh7lHnmExwMOfwyVcBcSgddhQaq95mwAThMaWzZGhhXP9WPLddPZnO6RryH3f7buUGaF%2BVQIr18uJ6QWDfdBEfj2b4oDm009XO4o8VvJsRglU69fOngMWYUGlr9runvmz0u7QHZgEzTLXYaevTmh5GT2W%2Fbz3N6hxYOpsjsu0VFFMpaIfxW%2Fh1Ha7dlbZymk1hUhwipb3XYeW3rS0Gy4WRLNKWPkXT%2BWAxF1V%2B1R1NijcAyAgWQgE7ZMeCn4W%2FXXb8wDpGf4jEjIPkwZvUaMbMW323Vg79YlZmSLnFtjR1QNYdc0JRYIrCR4iRtQw4h4FvUd%2BynGlUV8j00GmyYdQFfO8itO06u0n2rHmREghc3WclY6P%2BwAB%2B2%2FVR6u4tKmWuzLKjaIVdeAhEvNhmnaw%2F6HKmAZh48YgLwF6QmobBlYn36L0dDzk5TG8fAL2aRPUowQV2e%2FC9SyF9b8pnUGpgCtFD6g0IjS2Bd9DKrFhApvDD%2Bv%2FS8BjqkAbw63sjG04DOmY1cW%2FHAcKCL6dZoyq3f22cNNok%2BSip2EqKRhzOTJx9a7paaASSDZ12F4SoW1VrgR1KLpOO44U%2Fr6mBBSxMXeXiBpTdQn949emoG0o%2FghCvuiZKm1AAG8OfweWo%2F3VMq0Y86iPYZNeZRZlB88X6KIm%2BMOYHu7%2BhJFPFp1xNYE7%2BRH23A%2FXoG%2B5gYI7QnUyiSmoofyT6mDIOgciJ5&X-Amz-Signature=5ae8eb676ceb4da5dac66ea2cbad84a21baa182cb523d8f7f4ab2f1007aadcf0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOCNEIXD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgOAH52dTCdoD9SOmNyhtk93wukPyqbKBh9P86rTL98AiBX2qXWzpubBgUyVW%2FpPDP3fGX0XIrB9kzZUN8V6BDC7SqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyBocwZKFi3f6TRXzKtwDrYM%2FNFR9bYztHydMqGhxnc3Gv0BKEB8oDtIN2dUbKYQeUlwmCmYKYobcpDk%2FSJ%2Fhmhlxqpb4zxRsIptRP4u1PhmIUT8DYsf39aWMaalrqlsrkJmaGc6rG5%2BwIRDuXGOENJceBi%2B0DcARP7UP0WbLHDC9tWzraIsh3VC7zq21MKIHguQJY82qVA4lww6O%2FTdQSsajPNyJUEZOK%2FBC3d%2B2c7ICRYkB355HbuTUCZeqtNtojZp4Ef8t8pye8S1I%2FAoKYgNUsvSzN5416B%2BtnhBTG63rJrpKwAOMShEND2ZjgdGNwpzvKpDRSs4SOggxtKExWrE0h7d12UVeBP6xwk%2FVlM%2FN%2FpXYivMkcKJ17Ddx2HzErUJoaDFKhZWmVToA7TuZMILW4dHauX8NxLyvJ7BHmNNJRKYAErgpDWcH7DJnyR19evV2mLdOqfwDaBypp3x5EHgVRqC8FSVbEqTpE1kM5MvrV%2FYG%2BEeuBeBFDIhjQ47OpZRrc0bdUi2vSATgnIIWdV%2BElzsMXUO5zOrFiDBah%2BgU8g9JKcuFyY5yx8O%2BPJBOrIlV9tuf76%2FxeCok8MlVyv3S40jX271PArsBsa%2FNa1yW4XpAsOM6esnd2KBg0TVfL2HaOpq%2BBfrfF4MwhaT0vAY6pgHLl4J7tSUfKelGoWk70ovChzgxt3SVYuqaC4RkXdKJPE0JrQC6papq%2FxkXN2ym%2FSnheZpVMf9bc6vi0XFe%2BNfLNgv4WYT97JtQ6XTSLYPVD6N3GVHdJPtgyxku2aWgwEsYQdV%2B9fzuRzU9ER9WZNI7nQcs7zU2kU2ktXc2%2F%2FSkt%2B35bZ7yTkJyyy5sYyzOFEIyhCnW44mRV70GdHCHP48i3%2B2nmDtU&X-Amz-Signature=0449670af454d24de5fa8c5268df36893383c1331a345ce647459d3bc240c328&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO5TDHAB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAUPtzNCqLHApF1JQUK58N6B8hyb18vACqYCxHZvDXsgIhAIfuAHPhO%2F9dkqrKs2K0LMZsCmKVqNtcP7WcrJYfqupjKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyY3p6Vh5BksFHI0gIq3ANaqzAw6bltOEYCHsdwp9BiFlCyJ2QjZuJwmvgLrF7mtMsichPAIcNvB%2FRtvR6TUAzTsjScQKqd6%2FMj32d0uUmA5e24x0P4ChPrNO1zMMHMlkOClYRr7jvcen29jebZbqw5HFdY2kx8%2FcYrQ6zPgoiL8GWsPE%2Fl%2FdZ9EVEXBzovm%2FSRnscuDGwwrypODL9XN6dziPRaG1%2Fhr0rcbKC82bRIL0z3aIat6%2FyJxYrieG6NrafNcGTuG8RGGZuvVcdBFZIIaMFTh%2BGZgmc49isy3UzDNj0vPlwzwOoRC1EUrqvWinL2aMII30M7JeR%2F9zjkl1s2X%2BoeDFkokyyuVIE%2B8daU0YzqyVxRyYokcZGE%2BVjuAaSZBeoBVVjqppvoUf%2FT1w%2BNpvTNCzLIKfHSKaCFJCAjkzXzO4o4YP5PF1d%2FRY%2F2qFNVeysUm61pAtvmFCbswTi0qMbGRPNjESd%2FBAh4UjBuG3fjRkrS3QSwGck%2FgD4eFYnzT4cF56N%2BYOlpNjiNZaLDa4SRkYCXa6LfgJi%2FKTmwx3sOEjQmA9VM%2FHF99BJ0HzXmeoqD7RCfW5kY6KCrkACMMtolMU4u%2FM2rRwR19mJqPB8ma2gZSUUNCxClOcQ8RsUW0OfiTEKIV9bpTTCHpPS8BjqkARSaIe4xn%2FqX4PqRReuu2mXWln%2F%2Bs%2BRNlq7bV4eD67eDPGxwZmgdxZ3EzXaANyPyLZBe9Op9K%2FXbzVAgCUeTfq%2F%2FVHhmxP4zoTmJox%2Fuy5ciluJvMPuzPicxzAB1zgqtnyg513T6NzLw1DYNo4zUcD7QzC9PBE9E%2BuiUF5Nc3qsxrLa3xbKQPWecYr9wR8qFP0KLfYzNS24GsbiM2xmV7kcka%2Fxz&X-Amz-Signature=9bdcace4f53c8cabf2a498c7559f1f4a2e98100b7c6a0b35cd3c0aae8c5c27a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USFNSKQB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDj%2Bd4a1aCy4fyFTTRo5ybPkh5DmtUcQFX62kPeec2XtAiEAntTFSaquTFRM3vs6oTnoFbNYVumT2Ir1sM58xFVHfYUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDw7iXe09zmgbRVJJCrcAySBWSPZBIQCBdDUZWLemKVHY4ZXYc3lBkotLTEH8zylG22yaiYHHU2dS26m6aZaU4Pft0KcM6vMk87V8ca7sA%2BN%2FwQ5CWCHmOHjLgCYsWs8D85YpQymn7HZ0x1LC%2Fifn%2FDim17kNPIDDOU2z68NsBw3Wu0sfFQpzgAx3NRU63uGkmEmW%2BOBX4elhhCXKig6%2FNWMuIoOzOeM7I8IIOz6lE%2FJyHt%2BBsTkYzfnwXsWJUiKujLGrPr85VF3EZViac68uM%2FBTBp8z4AxyLZUtyMZyH6FmT%2B%2FCIlzwaK%2B8jsaTnVDLd0nI%2B079oOTa4bk7RQREtBRuJw6hcN%2B6AnrzzceRBhtXOEhiXS2%2FO5d9PiZ5wHtGv3KlTtdWsEbXLEtHEcjRrZ5yI%2BV%2FZ1v4%2FOytNLXSucGieqrUJaMx60CWr3O%2BIQfbjQ%2FJAuyFz151bSJlRa2%2FyTFuEjsEcjNaDw%2F0dZmlhtzD71sxvySJdJy%2FTeWVIgDFyYsvmJPQ3O%2Bc3B38XEF536A9zpjTiq6d1gzQ%2FVR7ft5dmw5i%2BCWcRLS%2Bsg1RCqhTos6NGu8juV5LF2MiZuQoOxtFKsW87nqpM3fXghYMluc%2BZFddCiseveVYSzvBk3SsaKujsahbytMqtNFMJuk9LwGOqUB%2BabP7Ix3EkE46LQzs4O%2FxEoOqlgF6UPQPbxstmXOoIfkHzr%2FBF45zcvgfeewf76msQSlDLopx54Vs4HRkXf0nX0VCpk7405pUFJzqgdhBt7I2ZudGBmudPlMXajU4wPjeGqYor%2BYdUBd9FacuqkmajPVBIK3muDJlKYaJOXPMo4LFV5wQi55sc0POog9FF7jIXZk2CGG3fW%2BXo7LwnYDBWA%2B5lJG&X-Amz-Signature=3ad72fe7beac2804e8ceff2a70f21261a50bcfe91bb3252983b6df37803a051b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QG7NQQB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF6DOxInCdo5GrEwKmu%2BpXuGEG4qM3xbRJOUtZI8u%2BGUAiBx3yF6G8Og0V1h63db4wvHfkKY6aJWqqI5K5FRAXsgYyqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCwz0nTBfZH8SmbUpKtwDmxOA7nolcCv0tUkhJCi8GZH3ePcLuWRKgYpvfAZXCHevLNbVqO3Rhlue8KtLjupfrrtI8qnPRSdLoHwX4O3%2F%2FlQcVZyRjcyN%2BmU3yvF9zo8blGlIxqV4Pj0dR4RKB5DF2fm4UtZY2bAZyJmxgylLNENTR5No4el35mE%2B2sEgWCd1zlJeDr39AwE3uabqxalOJnf%2Fkj7o0KNmbeDL2Ib%2BPtsMpUMytrXMesDjhFqOO30Xbj7IjCIj665az7UA3BI3RZ81SV9LRM2ldA56ImVkeY8%2FaL0lBeVEbc85oFolkCiLYBSbX3jSNRH8VqUW6lHMe2hIu2TeIkusGnY1rFkUt3IdtJycDTr9bQHvVZTLQUmRFQBYTN1pccucPPf2FU996pTTDMDTEqm0OO7432G9Fp4s4u1DuB1nrZDaLGNBVDO8k80AMqr4hm7Z6h6LYGWX8M09uhexg6Z%2Ba6GBdFDR2BypDDsLBb6mwAw7sA9ep3ghUMSROqfS2iK8dexNgQMpMguFtgDN3o%2BRPY%2B%2Bt4PQceM%2Fi6Tf2CxBFeRpMx%2BoGlhmlbOssGjlik1LN%2BmP9Z4cpcXwexoPDQ%2BfIEjplypXJmMel7dmfFn9OtSJdu84UhuSTxqt3KQ5Dt2yjnowtcD0vAY6pgEiaLTiFtiT%2FyAg6zOHAKDf2BacmuYRNvrVP5KZrfY2ZTnKDBpAuDjqfYuUo%2B%2B%2FThtARw5lOCK0r8DMs%2BFBqb791iR%2FbORlKSLE%2FfMMOBjk44fJ%2BBR3BdNKMv2%2FQdRuTqF6A05Hhda5pYwLcSGoJduwN0N4QSPcru%2FueQ0Jq06APVVBdXfOb9nA5%2Fq%2Bmc0f5Rzrll1taLWg%2BWlTzVgDiP%2BUIF4RP27g&X-Amz-Signature=042bb6d3e8e7c59fe84beb75df224df055411527440c03ecdb952d920a1be5d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QG7NQQB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF6DOxInCdo5GrEwKmu%2BpXuGEG4qM3xbRJOUtZI8u%2BGUAiBx3yF6G8Og0V1h63db4wvHfkKY6aJWqqI5K5FRAXsgYyqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCwz0nTBfZH8SmbUpKtwDmxOA7nolcCv0tUkhJCi8GZH3ePcLuWRKgYpvfAZXCHevLNbVqO3Rhlue8KtLjupfrrtI8qnPRSdLoHwX4O3%2F%2FlQcVZyRjcyN%2BmU3yvF9zo8blGlIxqV4Pj0dR4RKB5DF2fm4UtZY2bAZyJmxgylLNENTR5No4el35mE%2B2sEgWCd1zlJeDr39AwE3uabqxalOJnf%2Fkj7o0KNmbeDL2Ib%2BPtsMpUMytrXMesDjhFqOO30Xbj7IjCIj665az7UA3BI3RZ81SV9LRM2ldA56ImVkeY8%2FaL0lBeVEbc85oFolkCiLYBSbX3jSNRH8VqUW6lHMe2hIu2TeIkusGnY1rFkUt3IdtJycDTr9bQHvVZTLQUmRFQBYTN1pccucPPf2FU996pTTDMDTEqm0OO7432G9Fp4s4u1DuB1nrZDaLGNBVDO8k80AMqr4hm7Z6h6LYGWX8M09uhexg6Z%2Ba6GBdFDR2BypDDsLBb6mwAw7sA9ep3ghUMSROqfS2iK8dexNgQMpMguFtgDN3o%2BRPY%2B%2Bt4PQceM%2Fi6Tf2CxBFeRpMx%2BoGlhmlbOssGjlik1LN%2BmP9Z4cpcXwexoPDQ%2BfIEjplypXJmMel7dmfFn9OtSJdu84UhuSTxqt3KQ5Dt2yjnowtcD0vAY6pgEiaLTiFtiT%2FyAg6zOHAKDf2BacmuYRNvrVP5KZrfY2ZTnKDBpAuDjqfYuUo%2B%2B%2FThtARw5lOCK0r8DMs%2BFBqb791iR%2FbORlKSLE%2FfMMOBjk44fJ%2BBR3BdNKMv2%2FQdRuTqF6A05Hhda5pYwLcSGoJduwN0N4QSPcru%2FueQ0Jq06APVVBdXfOb9nA5%2Fq%2Bmc0f5Rzrll1taLWg%2BWlTzVgDiP%2BUIF4RP27g&X-Amz-Signature=530a7e0dced350293db27d0d4d682998c7d2f51f3f65be22633d8e63ecb52457&X-Amz-SignedHeaders=host&x-id=GetObject)
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