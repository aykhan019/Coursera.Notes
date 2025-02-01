

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633LX6M6B%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLsC6Z3W1qY0SG3yegAVQ%2FYoQ3tPrIZb%2B3Tz8yXjyY9wIgNXlat9vPsPEAWaYu82eYbm4fzaBb5pQCGsObFgAUhxYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2B55mU5FxO1KI1O7SrcA00vZEY8qrxEn%2BaAkMT9YfELl%2B8%2BCJFHmKHV41HYDGfVM%2FqbE4PHvwVibUHoLhXXPvTUEXDri1zdmejc3r642iBxbmF4P%2FzjdBXLq7Z7oLdB8o%2B4G%2Fz6cTYMV94aDVwAS%2BVouczgMyVBbFG9E0NDCTrw0r5PPnP3cPBIv9BZzNOwAel%2FcbD9hTrL6AKr7DumcyOnrnB77c86ZbJT8AGSpyS1bn7eyevaQnjRhCmZUcrFOP7jDnlHVyGDTR%2FyvLgu2ShgR3gDElCz1vrtEN7Qzk41X56btGxRCmoaOeu4aNNFbTNG%2FFUKgxD%2B2%2B7C9ZbbpyTmsZoCMGD4vnVEJV3XqcPlLtUC1U0yCP4DaKC6Gaynnh4aIl05NfnICB8ec2HSf1mUXhhKQ%2FVllM%2BZ9ascXk25uGWzJMKOos5%2FgIAWda2zFv6LhdKtjYFsxeqnusI3xh78I5Qk54y%2B1T8GYyrt3pOxwSs%2BI7zBzoCknvY3bWqxMq1E4z%2F16raPfljjT8rvPOm5jznMfLYsp79YHDGf%2Fgrkou4jJy1SWxB8EHDJfG%2By8MWKOUMXZHT%2FpB9SDkLowgvTZhtWxlDJvbV38xekwhjsiaZQebDdLpZRtocrYVYytpIcN0dCW1KbkQWUMNvE%2BLwGOqUBLQVTTokUhVRPEbt0EQ%2FUr24ts4lDZ3qwTTQSDkS3buATbhzBXkdbHf5FQ2gowIEc8Ipx3%2FCKdirGbkpxbj03p5sCfi0luxHkv7B0feCNiclRoXCKSepbM8UpVCA1%2B%2FS9Z%2FRhOTvuSQCLHrdzD137ffejrGIVzuEeP%2FZWpB7KMXmDXe1wqjyR%2FKma8LmeVmMP63xUdOW3N0GGiQahVWYJq%2BtexkYz&X-Amz-Signature=6c05df806af0d2bb2a095d82c840ffbc8ab526a927e97044da134ead7e657eef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOC6GKNB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXCUysLzDwM62uKkgB6mQ2OI5zjV3HaGbt3K5AugQscAIgf60%2BkxA2KKtmcYyTuQZTb6vLL6NXXRBFEaW8gYBqkFYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6ruLbt5Xt5sm9h4ircA%2FZDWMS9I39IKbo3Bux4OH6OzEt2i3L1sWFcklJsaQdtiwA%2BgHiSju3K50BMJZv0fzYuUqfgcvZmV%2BYj50J1JhJMW%2FZ6EG2lGbRsmNnNpTZeR0KDKgq04E%2BZtX0SszMCZoLH3rmXc2uHMgnDjsy%2BxYsgGO4TRChkjIfXZ8%2BILK2ZlhKQRKrYdp60HD5deLPtROcpPH5JytjiqRJJpZOHuV6JxJaSTXxizR5DavM1tLOajzpJ4aABGDoN7erQJ5h3dbYvyIGxNyd2Hu1YQm9Zl%2BHQI0zpQceUoN50RNV64dbNb45SUJkTbRXs5TTYressYuC4SRG5GBNLN80ievTXatxbAUbsjiB1wlq7Q9IXicsFCD7rv6f6ITJ2icjv4C0cZR4G%2F8fE5IHuEq2ZcyO7TrrXVD9Nt7ELOTTXa%2FiEYdaisr1PjTAZu75HN5kBdMJX6sm24%2F9fTKIZfdYe635ukwQudjiNAKuLq7s7qU0F5d82xp4s5ZTr%2FcQiQ7icrh9BEg8%2F5dctsrnR5RVB%2BHQKcWRkxtJGRadr%2Ba3cixjQ2vaD4qxwcD3yqNu4GjtisMHQYCa5%2BngFCQWPmfDFjlg3NHublJReHGz3XhpTnxnuv1m34515gJnsCxrooFNwMIzL%2BLwGOqUBYfJQCcHGvD1ShhqUasiX1Np21%2BGUmJ27B1c8x8dHLGTLAYZvRAr84UVOJsw2eXCaCwXll5KD9X%2Ffo8r75Fn4TugdtpiRhI2DD8m1m9Fhnf%2FoHXjrX5rT2EMuXQvdXypNDQvc5Y1w6Rb2TuFTe07fdEXhGDBR0XvnG6F1Lka7BGeSAvyntHreB4uhDMuHo89LPL5t%2ByWM4plWbag7LlwKSr0t%2F0Ut&X-Amz-Signature=b68fc379932922df1198a8895bcca8d540da97047e667e70f7ff27a7d656617d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K2Q6IEV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtb9cihpDNMoPP8B1555Plu35%2BxwNHz2ezb5pjSXOo1QIgcZIEL%2Bn25rV%2FAw1t7HYM8unRFNsIMRJq4%2BMUkXsHICAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2wIeZ264SvZ8noOyrcA0z2fxZm1dsXwza51WdrI2SVrmH48TrmCh9nhRHKM%2FgKlwNj0uTs8ZYC%2BQVFUZS5eSzMfWNhrRAQdouppjfNb%2FgSrxUBgqpMGdsagwWuI2444GJskZ7gWO9PLhpBtiFljb8qE9kcpqqCKlGK3yw%2Bt57ncjX9NeIBpFhSq3aoQ5JCl%2Fr%2FHmV9uQG6vUcnMwAYYssbDN7cLLZedLq%2Ff0vTU2XCcJmY9o5Cmg3HGn%2Fev0VYrIwNhQxPUa9EtzLyVE%2BAhHA%2BcfaLpi%2Bf4MHyTZbOtKwLLsI9pJ4g%2B2TMq4B1LU3cKifOsdye8k45kFQZJrhl3awhdsmzSIvAM0dxUeYIlLTJ7Ssq1alVKmiON%2F7dr7vFG4sSj74D3s%2BUpKuPYAhkxPcgErwsGizDJp7e5p93I7bhvbJYQDwp17Uym%2BrBsHdqvV5qUkZ%2BeMF1uX%2FJTVCZqSQroS9PmYkRhIkvhMX2mpglKtmOeAOvZR%2BI%2FlEutSBYtXSp%2Bo5pmjiQFLkGDZi%2F0Lg9%2FauTaay2n2rTFJIsKBpF4vnP4wSli67T78UPdXV9EAx1AVQnDxCAh08tsDZ%2FkwfP7I5Fm5NU0rX84uK9nFJEarzzAKDX1XH6eod%2B%2F0N56BsBexWcPPOZw5DwML3J%2BLwGOqUBtSZWIDaaNqnmOT6Y78oHDTw8UIT7dcz0bfErR53GFJ2RMyYhqFYSjH0L2ZYUo%2FgoTL3jL8d07m0czuAzd7dxPO8vuGDZKL1EtvxgS6ZlhR2Aozlxs70ZyCtqngqqfBs6S89%2FZUuHCh0FAd3jRMDvfRiBIv6Rbvh6n0c4iBS3tseki54Oes3P7DMTJgQypQtNEXqsth%2BK7tIAw1iJO42K4br27UFS&X-Amz-Signature=0ce248f2e72a62685a74873cae4dee133f045980176a2dc042e4e51af9b11f28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATIA2VA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJEdADRGaV46IIvferXg78k2aNxlbxL8iXPsJ24NuObAiEAvMTIaoTjRbJ5Si2gvhTc6s539YK6%2BeKtWWgM73ZEwSYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMirBuhDxfM0pi3UCCrcA5dk5Wd5ujnlEKKKmnzq%2FaPXvZRWOjPHy9lCZDJEgT7kvHwNwy3pvu4cHzsKCZHYzhkDQr7YVkwo4D7BQ%2BANaWfbUuZvQUoV6DzN4FAt1dye6NPVYjv2HWgjIqetOXdQ02Df%2Bd6C35PFCR4k5Zd9wuk7DXgZdWFoG%2F9X2Q2N9EWQQbZQBDvndosjadSeXTSKSI1Pos%2FZPUUWw7nf1F8QaXnILOJphwSlIrAH1W%2BsNC3V%2Fp%2BFgPS%2Fn3U8ndRYhj2KLql3W8dL7bL8CMWrRkd4738wBlqsdY%2FR1FaTHcpr2IIsj5PEUcMJIutWfEXFnzscpo%2FBBQPRLtq6esNe5m%2FzGB6rhAtgoyD38awz2LK2CYkReC%2B0b43lTPoyaYTD%2F9p7OUoIzPSrUynBeePrq7krJok53tTBsVQp7zASY0Js126PZd2gBOpFVe8cuApze9EWUD5uBzqyEMNLDjWmddU%2B1e7PFHD3DPQu7gx%2FzMtRvmOnix9KThP10rNfAkMkLV732pWCDy%2Bp6Hra8D4ZM3QXFg3JTf4QxAOdJstQqqg%2FjVE7whmc2IWTuqNxxuPnFiAugH%2BjjPIHVfQarLdCe0Dh69HW3O6FwaiOVuZ72rPgmTqDJ9EKBH12Uvnhatj%2BMPbA%2BLwGOqUBfaygaVMxiTWLPuTfowztvre3DXE6rJ1leAICDdsLUMhzd4fEIlD5rNq%2BdsZqRxKQmrtzFVN3FmzxQGrrJfYLVxPmZD4xYIIIMUXN8YmDhZE%2Fq7OR3q5X0TvoLjEHslVXCf4q1M8x3vXjSwDHJvCOcGwAFJdEMcCLY0%2FFe3zY0BfWLwybsRicJ8zViBEKLgZnJLtsuMDw5p8ikNEvGBCuEu%2Bf5Ddd&X-Amz-Signature=ca4eb52ee77311031dfc11b7528487f9229f926c591d61fcaea70b898690dbb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPC2W5WP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgdic%2Bbsfw2KdrI06piFVH%2ByrM8vz%2FJmTwicVGCGIvWAiEApeSd1dKWIX9ZN56SdVR2a4UZFcUsOtWk%2F1FU6zMm%2FXEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJ%2BT%2B2DcsDxLSeOSSrcA9IdhFGZ0jCW1JbT7bGA5ArhIog7kUQqldCtOqStyAvAbnzu5%2Bh7i59S%2BA9WCdVMbf%2B4xFavX7t%2FxDLz98d0psp5D8kqwiP%2Bo2XBXX5mSweAR4MYxzANaRBubCkB909Kk8bna5yoT8BdHPXtMvzqXs3%2FojNAJTGEvZTzn8l17iYTPsOu9FH8y0C3zuCJwlX1Zs3URJQc5Otxb3NyInlbaR5pl%2Bj80OvbfFMciApH5Ihq2RwqTM1Vcq%2FyU5iFGw5Sg%2Be4wCeDs0R8Zos2D27mMKxRdJ2s4p4sAL1crv7AJeun1okPxY%2FeWWQHlhW%2FliqcrddmG%2FlGG1iDIhhaEK1HfODyGL96qz6E4gcZFggUz8kXrgMW1QV2bIMSASytFWc5G7lQC2dEgH%2B8LgsQdOHFEWmEFszXKZIs7ZpGL94xIJZScTuhg9z7ohF%2FpErUb5lBjB9uXgW7U%2B4FDB5kAV5%2BeXBUd5bIYunkTD4Y6GLmLgjIPm8UXwqS2H8%2FiS8NXDrDWVKdVVfNG6zTrEirF6WAo2CCtfy9%2FC1nj6aV6lnVDBRnR2CfLeIjv%2FRPUrJVBgNrqhwG0Hd4BcC0xKRTSvz84%2FLzZj5XF%2BcoTOzTiRM8Z9XLOdPhwLZ9QFZ2Vz%2FLMMrH%2BLwGOqUBxFzV3vq1TuHxA%2BgVwB6%2FfRr%2FVGhu%2F4ypDXEg%2Ff5J%2FKIBMGQRGmF0nHwQyUMqovgvI9bkzzxd0dQvWUv%2F4%2FsaxyEf7wRKF9wm9rVKA3uAywCVcrkmNtd3%2Ba118mDw9EjqC3kRYS%2Bv32KaM%2Bom58PxO0mGJ%2Fb3fQypKYY6N%2FsQRf15X8A0uLAMZUHjW9B1h7Q1m3xlXIvmjcy0tnAMf4u19pTOjBG6&X-Amz-Signature=86f94fbc8bdfaa4fa953a2f96d62e1d266bafb89bd1a75a85a744574948100bf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K2Q6IEV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtb9cihpDNMoPP8B1555Plu35%2BxwNHz2ezb5pjSXOo1QIgcZIEL%2Bn25rV%2FAw1t7HYM8unRFNsIMRJq4%2BMUkXsHICAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2wIeZ264SvZ8noOyrcA0z2fxZm1dsXwza51WdrI2SVrmH48TrmCh9nhRHKM%2FgKlwNj0uTs8ZYC%2BQVFUZS5eSzMfWNhrRAQdouppjfNb%2FgSrxUBgqpMGdsagwWuI2444GJskZ7gWO9PLhpBtiFljb8qE9kcpqqCKlGK3yw%2Bt57ncjX9NeIBpFhSq3aoQ5JCl%2Fr%2FHmV9uQG6vUcnMwAYYssbDN7cLLZedLq%2Ff0vTU2XCcJmY9o5Cmg3HGn%2Fev0VYrIwNhQxPUa9EtzLyVE%2BAhHA%2BcfaLpi%2Bf4MHyTZbOtKwLLsI9pJ4g%2B2TMq4B1LU3cKifOsdye8k45kFQZJrhl3awhdsmzSIvAM0dxUeYIlLTJ7Ssq1alVKmiON%2F7dr7vFG4sSj74D3s%2BUpKuPYAhkxPcgErwsGizDJp7e5p93I7bhvbJYQDwp17Uym%2BrBsHdqvV5qUkZ%2BeMF1uX%2FJTVCZqSQroS9PmYkRhIkvhMX2mpglKtmOeAOvZR%2BI%2FlEutSBYtXSp%2Bo5pmjiQFLkGDZi%2F0Lg9%2FauTaay2n2rTFJIsKBpF4vnP4wSli67T78UPdXV9EAx1AVQnDxCAh08tsDZ%2FkwfP7I5Fm5NU0rX84uK9nFJEarzzAKDX1XH6eod%2B%2F0N56BsBexWcPPOZw5DwML3J%2BLwGOqUBtSZWIDaaNqnmOT6Y78oHDTw8UIT7dcz0bfErR53GFJ2RMyYhqFYSjH0L2ZYUo%2FgoTL3jL8d07m0czuAzd7dxPO8vuGDZKL1EtvxgS6ZlhR2Aozlxs70ZyCtqngqqfBs6S89%2FZUuHCh0FAd3jRMDvfRiBIv6Rbvh6n0c4iBS3tseki54Oes3P7DMTJgQypQtNEXqsth%2BK7tIAw1iJO42K4br27UFS&X-Amz-Signature=0ee94e56655ed82d224099cfdfe1635ea8d507d2de8ba0c898cbffb93e059423&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PIOSVVG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGTiZnduAXQ3fV35CQZRmzyf1EMq4XPeARiTqbIRLS33AiB9pQ7wXEpR8cjj3xN%2Ba6ka0tj%2FTrNywys8e2Rsb%2Br64SqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnHi4uGekYPhi%2F7WvKtwDdPnG1yO3Wgc%2B4TXvfxqlcAeXg3STlHUKXEZJjCGvvVakwRYuTJXq%2FRxPsfYUrNwXg0MZ%2F0Uluao3Kvm5Xx1wVe3vlAloQLtPoqVsmY89htY0YaOv1GXRASeVpW5EplqQbEgXjBX1OVIHTVX7qP%2Fj0FZSNpzMcKjwHSuI1ZgbTdeGs5LJStxDUhN05qkN5KLMRnJQJm60%2B%2FdHjQNJ1JM%2BQEN52lLy%2FahyPpYmu6wJGrg%2FO212cVC162gBVzjB6Y%2BiUTe%2Bqzkai95Y7HhDqqN9sgdJgX77LNel%2BamRKiKYumtF0d3nKd2SEo0ZVx61EMr%2FUxLx3HAM%2FdP%2BTUcBnLp7btVIG0igHNx%2FdV12cSHiNNhKMPDQAQImgjaMU1nzchz%2B518TT5AS8EXlKBp4uw6FuSgHvuviQVFXflVTIsI6laRCpEQU7e7iMV%2FCKEV4gd7jnUDzmbbO9zhoT1XNQoKV8Ih42x3%2F7yvmY074vQIGNEb3SRdjL2Ko71VnkmdKb98Fs4p07a%2Fj1A7oC8pgyaK8ivC639q9CfYYLXjx1Xc4l6wrg2vCu0OJss%2Fa7v58eBO%2FS5qONF5Txs%2BcoIkbFjAK2pJT1PSoikN2SGRrQacXaPXZmFZJ9W6O18KwAxYw9Mf4vAY6pgEUvII5AVV4oP%2FkMtElcMN9h1qVjtQ88CbtMe0guB9UG1CrtEjhc18%2B5E9CfnGx2NrXhUi0YVil0sqt2bB9YoL3gNcwqMA1JbfG%2F1L0AsZEhyzftNA8FZcfpF2YOHrt%2FLQsmSMkkHT7Jih%2BtpZFElBzJgxZ0bA%2Biv13ldzeBT06Ug591rcuXTyLq8GjxkYTX%2B1Y9FztQfAvoqCVGB1D1nLBY2g33sQJ&X-Amz-Signature=17010077abfbb9169e475c8596ea7d889447f6b822eb46b1eea708aa02ed74e1&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI52H6KR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQjxKtjqXoJVT3%2B6SM2C%2BEx59wUni2HZtsM1mbKj2lkAIhAMWoePCENhPSiFeQLhqMxB%2Fvrh84zNtD4udHWumG8z1%2BKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyHRwWWvWxqV0F%2BMqMq3AOn6YLRC%2B0tEhVS6TTPJaD8WoxNrB3GkhoCV9JKUgVVLstCMBiyyLgpO4oRKvDWJZSwm%2Bt81nYauEQjbYdWiAzA9gXmE5J4CPUp073xwW9i930rLIbJVgFxJEh54eTsxm%2BI2IxeEhCkXzN6%2F8Mp1SMHWxytumVAXYaMyYwErd0aSJ7V4ggWjEyeT2aO89wxsti7JY%2F0RyOcm%2FFZgUfRVTu%2Bs3VZ0ukX%2FuTgGb5s%2Fo2T0ekjfkxvQelTlDM06Wr0gbyF%2FkR4UpkU7QojJwRo3wF9ByypfwSbHsQ6%2FsZApIggwREWHQZBs%2FeL1sIgbiS1f3vBImdLX8AA29Ii9IV4DgqqC5tSTo%2BWYuT1KrRDUpEFZEs3pwRVdHbjvMqd3rgMgk5GK5ezA75uD%2FIPS%2F4FREPb2g4HWP0e5bgr4kN4fH5iQ7AvrlRMKvtKSjBFL%2BgzdwbFc042cYt3OWyKDAdIZ%2BrzdANE1CSiv6f7Ct6HN1JGEG%2F7uye0oGcATV9tCuOI8sJT%2BHnK09br1lEAu978b33aRkoqSsBtQ%2FigOfxmmL5nyV9yZCW4088f2Dq64cSJ7fcaAksi6aYESv4HUUnz4r2JIFKWuNofdZH6232jBAk0BWxW6PrgWOoWQaX4uDCOwPi8BjqkAc7OhFt1BhqBVz1K3AhWzIREv9hAeR8zj3X0E4XCq%2F69c8SSdpi380yENN3Cbs9OsfHAxQV4%2BUSEDWN2wbtgPTeNFhGlvKJ%2B%2BdjgCIua3OF47AMff9TqPGn7Hn1AU9pavoWcEW%2BL%2BxRIr2qKh5wm9u0hix7pk1VAbBSQcADUawA2xfgxJXTT%2B%2F7oWQU%2BsosICRRXB0%2F23fetHlC3jsRkic4y9NSB&X-Amz-Signature=f29528488387c91c71398b8797f5f7dbe703665994a70335789cde6f4636f831&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPC2W5WP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgdic%2Bbsfw2KdrI06piFVH%2ByrM8vz%2FJmTwicVGCGIvWAiEApeSd1dKWIX9ZN56SdVR2a4UZFcUsOtWk%2F1FU6zMm%2FXEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJ%2BT%2B2DcsDxLSeOSSrcA9IdhFGZ0jCW1JbT7bGA5ArhIog7kUQqldCtOqStyAvAbnzu5%2Bh7i59S%2BA9WCdVMbf%2B4xFavX7t%2FxDLz98d0psp5D8kqwiP%2Bo2XBXX5mSweAR4MYxzANaRBubCkB909Kk8bna5yoT8BdHPXtMvzqXs3%2FojNAJTGEvZTzn8l17iYTPsOu9FH8y0C3zuCJwlX1Zs3URJQc5Otxb3NyInlbaR5pl%2Bj80OvbfFMciApH5Ihq2RwqTM1Vcq%2FyU5iFGw5Sg%2Be4wCeDs0R8Zos2D27mMKxRdJ2s4p4sAL1crv7AJeun1okPxY%2FeWWQHlhW%2FliqcrddmG%2FlGG1iDIhhaEK1HfODyGL96qz6E4gcZFggUz8kXrgMW1QV2bIMSASytFWc5G7lQC2dEgH%2B8LgsQdOHFEWmEFszXKZIs7ZpGL94xIJZScTuhg9z7ohF%2FpErUb5lBjB9uXgW7U%2B4FDB5kAV5%2BeXBUd5bIYunkTD4Y6GLmLgjIPm8UXwqS2H8%2FiS8NXDrDWVKdVVfNG6zTrEirF6WAo2CCtfy9%2FC1nj6aV6lnVDBRnR2CfLeIjv%2FRPUrJVBgNrqhwG0Hd4BcC0xKRTSvz84%2FLzZj5XF%2BcoTOzTiRM8Z9XLOdPhwLZ9QFZ2Vz%2FLMMrH%2BLwGOqUBxFzV3vq1TuHxA%2BgVwB6%2FfRr%2FVGhu%2F4ypDXEg%2Ff5J%2FKIBMGQRGmF0nHwQyUMqovgvI9bkzzxd0dQvWUv%2F4%2FsaxyEf7wRKF9wm9rVKA3uAywCVcrkmNtd3%2Ba118mDw9EjqC3kRYS%2Bv32KaM%2Bom58PxO0mGJ%2Fb3fQypKYY6N%2FsQRf15X8A0uLAMZUHjW9B1h7Q1m3xlXIvmjcy0tnAMf4u19pTOjBG6&X-Amz-Signature=a8a40225f394a884c2aa36a7a8c0926b20591d124039481ef481de5e81977aaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=ffb7653ce9e254f5bab082a5e766a03aff6e5f391b549e01b1621ee25b9520c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5HYNZHB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYzpQHSWMzTbIBPXPMFU2LKpis%2F4aLEo8LyZZi1MrScQIgCnl59zaUmayT128AAnxNGW5PaG8gycCcJFKDHzNF5zMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDkQNNyI523tyJuKHCrcAxnsM%2F%2B6PAdv3FLUYnCznMBG44gLSL0B2S5u6Pa4XrYISgCP%2B%2FRbmoo1PKNA%2F2WWmVnkKonOXLn1nfCsF69XGMUHcBuKPDr3GMaPn8IZq8aZ%2FkuR0KDknzEf4mb45AqOOHpGGf7Fv4tkZf9guapw33xA8y3VjzeT72OnJ5RsYsGxb8QSN15cwEE1LJWhx80mZ35BKQ1BCCtZENp4XRqcC%2FkJzi5QSqVwM3tGAnaQwv2He7orAI82aaZ%2Ft6Chn9hTt%2FmGSwms4c5L608hx9D%2FvCZPeGBmLjqkh80qPwomQkKwehL9LmBUo8RDmv%2FiQw9lwy2v88QHVtncwpRhwGjaV2LCpSPzLcyUxUF9nD21QNBy%2FipfVhLFuboOJ74ovpI%2FIn%2BZtrcLtqSXgLme40hA0Vikv7P7nqbetHhX8cLgdV6KEXjQ%2BWe6VMOcVnM36Lk5TN5LHl%2Bez%2F9sS7vQh8eEEcinWuEdFy8PLShhBAw9wyRSe2AbmIdKphp4KA311k7ascRo8rEhMZrlWMV3wMeiF%2Bdw%2F0WjCcF2wAGA5kuHquuLmRuf6HBAhE5w4YG8c3cZY9AsfQPiEN8joH1U35KZaZ%2F2Ns513sII3jFWD2NJ8RvcpEMYnk0ctr1w7dvjMPvJ%2BLwGOqUBllVMU6We%2FshcojGWP5beOZBgbYT44vxNxUgYijeahLpcNcaKSfr7mEsqvbFtb6f2PSjZrMnl9G3xsbBUytSQ61cAWGLDUs2FwTG3Ecoo0ehWG1lnxScSWfX47bPC965MEZyGcpgfRTg9JdM%2Fk3nZpWT0pOqjF9t9eK%2FKaUAil%2BvhZBheqyoXfMTF8Yd2vjZjDbFwFX3FAOHOCWJpG62SKSLsaZRF&X-Amz-Signature=1194949e19501b9778283d6ace1707fe454ac961cb37c7d912724c8eaff7b0ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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