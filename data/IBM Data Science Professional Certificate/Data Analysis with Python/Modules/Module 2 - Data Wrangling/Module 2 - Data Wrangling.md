

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS5VQUNG%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQD6WGqrOtmzC56kRFixCNoo4D9KMgWamMkZtajey%2BymHQIhAN35Xo8qfOn7Cd5GdBZFA0BNUsiH2kYQ%2FYL1ZDD7%2FDZWKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhUbR9eq9TOSzUzWkq3AOxGAeS47X0vFco7vl6vgii2M7rH09MtF7DmRWA%2FvhD8jdMKqC24j8PJrXhNrOievIq17%2Bm%2BxYjpxmzMArsYcIh4AEMyK43ZDC2M8Mrh4V2TRhPO6HXOQW%2BhVaAK5qRLc2AawLRtUthJEW7aVzeUuVZrTwjD8pia89r%2FPQGDh2GDSiGQQCCiMmjtWvn8mt8RPdgShdhgaYtt4neRFk6cti%2FvLtzXYuwwWilWbJSs3YU7nogU2nyaIgieSq2IJwdc5AZfOP5TwMOx3NJH76AUuId2VFy0nvgJol8qyMluvKqBf1PB3sm33iEhK1ffB5yTI%2B6yBVRFXpC2t0wn%2BtM49PVwxETM9jpU%2Bz6tHogDnLnSoZ7fLP0xhEeMVKhnKLKzm8%2F%2BnyduslY94adhxB3kDPfsK6Cmv8Wb%2BUlcpSJHwiQM4VX2zThYOhtFQ4Gml3drhPdF9vzs10ZDR4rWtj8Yp310OZ%2FRI%2BRUP%2FwECG0OQfEzbPSkjKNfCeddV5TzL0%2BiMZ8LIkQ6%2FoGqtVRDRPkNZbGtfk8a%2BBRweuFjElcr2hqEIkHuwe8K0ERGMXr1dW1gbj%2BYjMPfFYJUgVYJZ0hMp9c7%2B%2BXjog%2FekZ4A8Czd1HqzGTnLA4GkqlIRAQVGzDct46%2BBjqkAcYS9TMIBnIDF5kzLaBrnDLgce4LEA6IoAypur6Dl6q8aD0Vq1T2OoJiO0JFn8Q0bSH9QDGPlUfaU1PLvpEMJXJd3yV11ac9Wbnpp%2FtxWtNtlcAvySnj5stbJ%2BrekdRgvu7Vt7%2Bxr86BLh6hm52XFBkbnnMjghvBZU3jvsUM5nOeMGIRtEg3SoWaGHQ7RrwAz2CKA%2FpO9Bm3%2BOm%2BJoGzdI3ty49B&X-Amz-Signature=e73be63aa10971e71cf957634a5f7ad0d1ab7cdf7553693c9e5c2713dbc46c3d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOPER7WN%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB1OiMZ4raXiexh4zmKc5%2FtpaqsoAIdMN8%2BqIq0DxwFVAiEAtzPqTJb5dzRg%2FcNK%2F%2FxeLvVkCG4DpqsxzF2lWLs9LOEqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHyTZ5u0%2BV4cH2ghCrcA%2FBOEU3VQ2xvv2huWM8rGZu%2BNdaGXnqpyxSXhxHQb8z%2BBtuKAkIFfskbk9xsKPbp0805V1d8OY9zbqeHWudycqPKrwzvajMMU7KqDEL7fPN9WY6M9ErNReDkhpcUZF74ozqQ7wmQhvTLEa6dJq8cpI99AyTteN17cnL4zH2WMRVHgNnstupCgtJezQqUsj00rYnEN10m0%2FoCku3BUWysRuyQ%2BMtR8yxTH1aP17KX9Z%2FZqvxzhGMWVvvfhflEGv8GSXReAFtTmgOvX1P4LTOMHzJHasgrm3XRc0j5kyNleqsitWJvhYJEdHdU5IGQzSu8%2FVMXH9oTVmNWunW%2BPGmQ5LDweg5opkFxCZkaM%2B4mTTIx3aLTOII4IM42FbS7uwtbR%2BZrp9cWSTU%2BqVx5uTKlO%2FbcxAjHih8DjG%2FXbhBGgt5QvFpxtgc%2B%2FIeIS%2BQummSKV5%2FErSACiczMQpPcqqYF5%2FrOT2Ja5igICL%2FqFxBAKwisfwyLvrd6IqrnAflPOi%2B06FQtXxdm2OCFxj1EDOm1TWuvjuLSDXV7pUq0Il23rusl4UmSDGlzTK1PDf6ffdV1IwOc5J%2BBL3sP4JcCRUJLG%2Ft5Thygtun5p9cE4W3Dimp78zsdIdaaVVCf3YNRMN23jr4GOqUB55gf2qwMW5g5YWSfFY7deVoG%2BIs9At9njdJDaPawDYUEKAmxRacSvX1dH0Z%2FenbtLvnw7TVZKCX8vj4rakE3Li%2FgGyJVcPFl6UioqOFN1lr1NVyk2s6nfa0JEyORcBcN7SL14CB4qmfm9p9imRklBjv3IlzKCEJC9TWXLOUIs3wixSRzYWxdBitF01bqrviFVmDaeoppE7%2F71ovusJJ1MW9fh8AW&X-Amz-Signature=5e30151f1e0f5512f4b77a1ac4d3419fd43a32a2379c658e6796fde0cb034f87&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEYKKT4K%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQDR8LE5tdtdq5ntxXQD6OOiw0KFLsAi86Yd4Cjvjmdi3AIgHjhYpM4KuH32Ef86HJOunFL6nSO6XTjvdRcvbn6%2FNLYqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLcREg%2Fuh8jAM50A%2BircA5qQtL29e7xUxjXOJzbfa9DoK5h6Y7J374w8biWMgxpe9giDRsOUjC5tezru1TXM2uh7ncGr7YtKM2tkxiyvThIEP%2FWlnOIDVgiO1kPorUpTjkYMGLqfTiIcvoyD6%2FR%2FlOj47AOfmo4nQdxKfFKjLpaopgDk%2BWd%2Fkk%2FGM741XtF5MikOGD3mEQUNhHrYlfioY7c9sIBhj1W0MvaLAfwixSIiUVAnLdO5XvL2tD2ped0QsgBpDTmXNyno0aRjdk5n02L1ok4cDtFWgu9EQkAiepzASJeiClgjtHlJtcS9Ge7WeLnHT9yZuOwF15ro%2BxP3VCEKDLpteuCUxKfNrXX1UXkF0YBu6i4U7k3T5ub1VDRu940ZCTNzMJSbMwlmliHXEdbt8DqPu3k8twKKhYT3GA%2FGYJci5VwB2vr058ERW7Eo3Wey6NWkWNGAwmbA9YcsTZQTSyrxIdSf1zmd5GANiQcYfc1WJrYs5LWVJcrxDgdGrCQx1%2B4ONi7m76yA3J2NniDKqSLxMhpjYwMwrQmnUvgSNnH2%2Fw068YONvIVBwSo4j3n8187q0Xrtn%2B421yNs4xPq4mmiyckXnGlATj6wibW4TceqMN6KWNgODOE58RXBeXQ4he%2Bm7x%2BjM94NMO%2B3jr4GOqUBCoGVp9TyndoineLr2PQPsTDafNGdGmrZHycXEws9Cuf6EabNC9LO%2Bt09vHaeXpUhbSqiTWrRrsHAnRCFcTZRwatSx%2BbN3M9Sngxry5YVnjQTvry8WxGA%2BD1NmPv7rKF%2BmRtnuPEqjq%2F0VOrZx2gG3wAm6TxY0cOsO9O05KZofzGAV4hb1NRT%2BJ4yjoBd9ItIhzOlfP38zR3H5cbtR7oRgxsT2I6E&X-Amz-Signature=a81dac1860b23e9f05d114e46b7761204e8b7f37726194e81777eb826b5c484f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHY3IE5B%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIQD2ysKIpwOwOISuQpdF%2BfQLZ0asoipk5%2BB1RDssPmDWJAIgQgCaBqBPz8N5s1Bp5nN%2FZEQoZ5hmkxsXpWU4Mej47F4qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDOcuU6MWZzDcu%2F7OyrcA%2F9QfReKBC%2FAmGzvum0whVXWTIATcE48AV2LP9noNt%2ByZ73rYJCmfpsypF9kU1268Ird%2B57q2xayKqFEtHI2ROuFEiSZEcwsCkJ%2FX4GKb88P%2B5der33Zm6COSXkjUC%2FnehMhqfCwQuae7ABdflceousOPrfMvFMX9gYFIje4ftMW5MCiq6rutVmEGjrEFdiEQPLX1MBI1K1QUWwfWu3On%2FqDZBLOS7q7i%2BwE44An%2F9klf33eAYEDqxXB86FsLSWPn4%2FUh25%2B9fshHssyF1T%2F3MKLDHX0BjXC3kCMOUBWmPO7BtSTw9gd%2F72nFB%2F0TdFP2kPmWZHWLN0dou5s68v93v0veiZDfrd2LB6ktlYmnYlTwE8klcj3cnDtcXPnf1dVfIG7oihZUF20W6%2F1P31fyLWfUWO%2BNMR4St83sMs2R2ezfKQVGGP0h1O%2B0zFKiDwfPdoGCy79eCHQhtt0MqaoDjc%2BazU1qTZJsQGKqhmzxdvvUfJM6hSKIDj1IywhyVPW7r44bRumTV4K0YEY5W0Gaxh5Vfu3%2BPjXqvmBw0OtkIdccho%2F75ET6aan2YZVLkHsx6MVOvlrxIU3zzd52AX0801SqRt1T668lwYKU7NGjCph4%2FRQjnmQLpxfJ8khMPu3jr4GOqUBo546GCAAFU%2F8GuRWrkoxfAD%2B4ZTNQ3LMbTzm7hFm6yZuvtOtoHvID5%2BmoGsLYNGDQw1Y1E%2BuvPBzazcu3vJV4lQwEDGosfF7ia4%2B5RwHOFJ7Y7plff%2FSCxi5sSP5hbNy%2B2bWodQ51Z62Zz%2FwVSCTULIKPHlpQO1HAuhXGCpYE%2FnkElwVXf5RKuwNooCW1Beli4hIYl2tgTIdFqKypoJ8HJTF7yfl&X-Amz-Signature=bf45691de806d5b3d78c819d55aacb540ce0af31f1938378a8479b581110e323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMAP7FT3%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB%2FMPkqJ6wSlXifJtQsk%2BYwZ1rN6AYut5dSf74Vw4z01AiEA6WMt2f8leA3mwgDlMesRd4co9l3MFqLAtNNHRlyY3TgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLx1MINPsUzPa9vWvSrcA2a1QaZSw0N92mgID1FUMhOBc%2BB7Oo97wBCnwvlQsfXCZXvkzFMYdJu0Gme88QcAoSxMOONCsFo7tE2rJMcaBvbKy%2BwEXas9LmvzKQhVDO0PEolqQh83F6XzMh9VOXafqVFYNhAqSOm9sVEloV3RZgcVI6pmhGt5KIqYfXYC9Y7mTBTTwi%2BUl8qvqOy0WvUWgMLkhUd0t51J1K%2FLrZbkCZlSdWIBYbVd1uiDnhmZyGiLQ2V4Q%2BRh9nWruCcjRC%2B9SwQq0IL7ocHcLOfAg26Gbg8jCvlau0j29EwbgKHxR99BXpDEa5uNMfOQuxxs%2FeQB0cEJec%2BxfgxOcC20MD7a%2FdadKWMpm69xF1ZNu8NoEzh7XY8Cbu2Hw2ekPY0zimX4fCd7xrzsUKNS1OzOJLLisr43qIzKG3cF07BCn8UnOP%2FkkYMvxkmzcVDwFVEZXge2wrpIKtLeCmOQJKyBa9kMHq2HuEU941jVqdEQAqlHYnSOXijd3WLzoTz%2FnOmvMOKvtxOYW3IkUfrbNlbaXGjEyZidEf9n%2FVAKXe2YPpvQsgag9wzrrPrs%2BY693q0nAI0CU1bu2qrtZalzFdVua2sGt0p4A6kfOqokuz8z5KIslNAGhxI4rjwKT1nq93G2MN23jr4GOqUBX%2BdQiCh3rwRdy6eUpH%2BKYa1oLNkUmMyRBJZ6qss5uYw3%2F2vGoLKLbFdAvq3gQd4hqc11buO9BgIj%2Bezj1umxmmoK8sRHMckPdKbgQ%2BBxr3iRCCXMpRQoLrZ8uZFn5hXEIe9cQZWrfChyzJs9bQf42xK0cuEZeNt1NyFE09NdqSfIO8KQL7MgqZvz3bNYlIelwWj4zZixlbxb3utiYzSApNdaqJ1x&X-Amz-Signature=0364d80f821db0a59a7380fc08e96b45eb5c31a2dc1ab1f711a9fac28469e319&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMHDMS25%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIAP1M4hiMXUk5zpcQSl7Y2WlR1mIZfmmIDdydWS6bWEPAiAJwW4qi05bPbTsSGRbe08zcmb%2FrXCiWyKVY%2B4CQHWQyiqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHHo7SM%2FXgajM2OsPKtwDNc3uZleNb1OeR0qJJ5Soy9wFMvAX7vNCwRDH3m0nLJ8MrkmvHnbHFv2vacvjHwWuehQR%2Bzp0X0VF0lQcQi2Wxeqy8bqx1NGJXzL6inE%2FUzvJsvefora7Yi1n9EWCtH5t4Nz4dIaq4Ju5p1tljBAin3OKVZlxksqIjL5zxazUkY2C5syy1KxyozxSV6paoNxUmdi4QWxdUnxKMkkf9YIuvEjMpDXhUyR2na50bQ2WgjuhjYATdqWdtHro5Zdt%2BBPSZhPEKb5%2FwCOOu7US0B5prllSyQl9UqsEXAediR%2Br2UxU6oEMegQqwTuNFXoFmkuHULDwNssmX8LY78XxHurPkkbNm6IUMtueasJQIJcQwyncSItLawD5saExq1XZhz6mmKSnL0JPSPLEt0tb7dHFqaCte0ieas1NrlgbpyboSXy%2BjQMuyOZDZWYbyAwcZKZFbc7LTu54k%2Brrg7mRZ%2BHcYS2aWqnhebX%2BQme0PuEm3IEvyZWj%2FdiajZ4d5LdRTFp0qWXKK0%2BPdu9YqWmKe0n%2BA6X9dqTgxSvxm9Brx3HSa%2FjXlHhI2wRKHH2jH30a6XCeVdxLrkwPeq9qa7D7soXHuwyEXnhlXA82FN%2BNB8ysFD%2BXmUgKBSiSS%2BVF4sYwzLeOvgY6pgHKO14nijssQ%2FkcZ50MnwYz3jV7OVc4U6oU7o%2FpFMEFxdH1Mnz%2Fld9guVfxlj395NwMkClgrqXNXZu1Qv0b2WwSVcy9LsOB9qBCWKCkqPril%2FtTPPowQiGpNhvoduHF9Z%2B8eEwg2pi6JiYqvvxk%2BcKx9Sj7s%2F%2FHAFt6rcv6JCzTFIpyr8YMovgQrn7AnAFw5zD0PTFyd3nEa7p45CMVIKcXhKTemjSU&X-Amz-Signature=b973d785a6a9ea619188705d758cb49c0600723c06ecee8af580112aa316e173&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TVPV4YE%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIDywg%2BxtqXG%2BXj%2B8guidPMtPG6o%2FPI4X71dOMJJay19GAiEA8Sqi9gooj8eYLDhRzBBcbPMPmabMTlxa1vSHNMw0EvwqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQC7LU%2B6m62QslF%2ByrcA7e4pH1OMhXeuOiAG74y%2FvGgcis1%2BQxqLKzxyd184UoYytQPnyg%2Bd8dfFkwWRNxF6eD4U%2F7WqbktJraee%2B%2FN8ToBTb%2B%2FmfewJKCQ78X7VHpdgEes9eLBOkdYfmE3DXjc88KY4PKbf1chKt%2FWTCmVPhiId%2FMvuoZ%2FKf26WJTu9TOtaNOXfgDIE1p22YXTuptAF%2FgMyHHdBgfO76wZGl4ZMo5JnW97BjQ38QLRfoQHD%2BhIAJ3O9nVVL0Gg9XDJtXcWJAAsBEmUwJRjmjNkXXibzGa9P3UeqGrIoQfgCpAj4CRr6QUiFUzuN9IphKJDcaHhCHdeR7oNEqJxudwpySma1nKZo135WfFUSC9NHXoB61fBb7NE%2BwBSP4MmDT%2FVvO9ok45lhg82pKu6%2FvDAvvd0%2BBVJF%2BUMipEhxA3j%2FjjLoj2pcWXlS2Vu0H5C%2Bc9KYGu5ewT9PtY3VkCuTN3c03Jp4KFr2YOPWEKbiyaUH2%2FYXaVvo326I6Rs5hcE8keq1AhfY%2FiJLlYzIqic5R5%2BnpaAkz%2FP%2FmGiyfVkBxHN2iYI9kKVzeV691iJbjonru7FVQRHqqqOPyos8dpHTUJmJ036wUGs3Vin5GcZ06UyxlHBgN4mMc8u5KU%2FNDuthRswMLy3jr4GOqUBNS0wf1P4Hw%2FtIy2DmPGnMzMSqg6iuXOQIT7TfKE9AuwWDDxyfY8FmoNoYT5DGPG4kJjrT%2FPCZJAaGJWhkTUBA4%2BNF1rgy2IDI1yZt13t32Fwl8yiBqNojaRPGBN21rQQHfyDKLh3RorepTXfRQ6xvlWUzyDE54aLgDQR%2BwI9A5A%2By%2B%2FyyD5AcJWbmdLwjc0rBreWoEuZYxcmDSIWnSuu5cNqaN0P&X-Amz-Signature=a71b15f4c02fc28a0cdcf4a918d4e6fbd0c02d6b2ca95c8ccd864765b88e81b7&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A7BAY4Q%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDYn7%2BavVEo3Z56Ttm%2Bv3DIJWUgxVftF24OKIRj7ar7UAIhAM9CIanfLVd7HWioWqVZHJmPEJCfF7x0QmAs11RnFDm%2FKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwApt2mYumcEK8eQ48q3APUR%2Bx2g4juFykFtAXC%2FzDSwxdGqtUrxsa89bhWjW6ZLMtxdHrTUN2JnI8oVtye%2BNJoj2hNDAl0awHo9Mr%2Fra3q7Vy0tlnnjq%2F8eTY4HEtr6UdZ2clZqFRlgzb1K%2B2OmIySGw2k%2B0NzkKSuqYzL%2BniMZliKxMcBfBN2dbnVgRFVzcUHREKTopz61Px5RInj6DpaXv9Unhd2oPpu95%2B38gjr%2FyQuTKKOksApVWrcNBSYSiBlIzWaHpjf69a1VKaTaVf4jXzJ%2FqSoN3qT2g%2Fo8Shn%2FRNDplZcHbh4zwOhV8YKyzU8mM2mWdLFUHOw%2BUAWSLb%2Fq4FBYXw6kcCWbLxycsJtJv8NI7szNxS8vp4PVg3PC74U1Q%2BqacnGvBxUU4QZvgCTk7pkRtSlg%2FX%2FJHq%2BylvjzexDnCyZmhROc5h6tgQROxCVp1KqL9c6bOcGsOc9Ye2C%2BDnPEqFupBmHbmWynH1wcVz37RG%2FdgKxi1P1PEyo7KRl%2BEZPCrUUghnUkEZCDY0Qx9S7U2fJC0iXtcCxnPcNVSena1dQ6igJL%2F63yEJquinH6tDKj6bfesteeOUO61SpKsDGxpj1O6b0gHqzYyPN6tHTW0OwQlLrBA8ZI00wTombPB1dshliUXT9RDDnt46%2BBjqkAX%2FpEUEkUALQDzYcC0u3355J%2Fo1hftedZdEZ%2FoPIHqOh4tEyOyrt2mizMHvKszMJAa4RpT%2B3DLb%2FXwD1V8sehh7h5OFEATyUPndXRJOsWi8IGDMpm4x7a2391Rv6Yiq0ZY2E0s50f2%2BSy%2FM0F4L0Rj1VzqTgoczlnfh6X%2BiEoymqhRSLISygWcQj2iSyOYJfgAunX9RSPf0Jpke2j2PcElIeuKIX&X-Amz-Signature=5c3037b900ef4bd51ae42c96da0ee52bfc7abf10d79a825fa434ab8eb9d04bc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMAP7FT3%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIB%2FMPkqJ6wSlXifJtQsk%2BYwZ1rN6AYut5dSf74Vw4z01AiEA6WMt2f8leA3mwgDlMesRd4co9l3MFqLAtNNHRlyY3TgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLx1MINPsUzPa9vWvSrcA2a1QaZSw0N92mgID1FUMhOBc%2BB7Oo97wBCnwvlQsfXCZXvkzFMYdJu0Gme88QcAoSxMOONCsFo7tE2rJMcaBvbKy%2BwEXas9LmvzKQhVDO0PEolqQh83F6XzMh9VOXafqVFYNhAqSOm9sVEloV3RZgcVI6pmhGt5KIqYfXYC9Y7mTBTTwi%2BUl8qvqOy0WvUWgMLkhUd0t51J1K%2FLrZbkCZlSdWIBYbVd1uiDnhmZyGiLQ2V4Q%2BRh9nWruCcjRC%2B9SwQq0IL7ocHcLOfAg26Gbg8jCvlau0j29EwbgKHxR99BXpDEa5uNMfOQuxxs%2FeQB0cEJec%2BxfgxOcC20MD7a%2FdadKWMpm69xF1ZNu8NoEzh7XY8Cbu2Hw2ekPY0zimX4fCd7xrzsUKNS1OzOJLLisr43qIzKG3cF07BCn8UnOP%2FkkYMvxkmzcVDwFVEZXge2wrpIKtLeCmOQJKyBa9kMHq2HuEU941jVqdEQAqlHYnSOXijd3WLzoTz%2FnOmvMOKvtxOYW3IkUfrbNlbaXGjEyZidEf9n%2FVAKXe2YPpvQsgag9wzrrPrs%2BY693q0nAI0CU1bu2qrtZalzFdVua2sGt0p4A6kfOqokuz8z5KIslNAGhxI4rjwKT1nq93G2MN23jr4GOqUBX%2BdQiCh3rwRdy6eUpH%2BKYa1oLNkUmMyRBJZ6qss5uYw3%2F2vGoLKLbFdAvq3gQd4hqc11buO9BgIj%2Bezj1umxmmoK8sRHMckPdKbgQ%2BBxr3iRCCXMpRQoLrZ8uZFn5hXEIe9cQZWrfChyzJs9bQf42xK0cuEZeNt1NyFE09NdqSfIO8KQL7MgqZvz3bNYlIelwWj4zZixlbxb3utiYzSApNdaqJ1x&X-Amz-Signature=9670b53aa99bd8e7cc4f69c9e107c7ddb3f20874978dd25638e84b181426350b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UY34CFK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIE7SlPu4Y2W7pk2xUG0sqpWsbFHQ%2FpWqNzQ86gtfsm1tAiAji0MwyDXIzFb9jxkubXKc7%2FZA9erxoXmKOvMW85hmSSqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9dZmec507jJeLa8oKtwD1XcPnUq1yHjN43q2ii6orbKZRboTFhHYZOK15GHuC2ORkCPm7Ku6CSMb3QlInioDX3fHAb%2BQwaFI3OydCfy7p5fGlcMgirJkXdovxveUc5rzajDkv1QKXDg%2BLp6D1dx0pEKclsCVGRzi3L755uYn6mbvF6vHeKu8Eun6rEgxWN%2FUcAJybB9mQXSRwbbwVwhlbSiRGKiROjJXnfuTtC%2F2Aec5tDs0eaaIsPzKDTjNlKhdlzLXtXwBLcq12%2B3Qoh1VKJzoCzwQdzJcJGNXwxYAr0mAf%2F0XKMgqSkLkbQtn8Pu1aYIz8fNeWOhbBNZi0pMBLoFM0As%2FW5%2FZaM5M%2FviqA0ZZ4t3Z1T%2FKgY%2FEURhitVAIE0dRv8lTP20ucpfGqwyGXRA7RjA%2FQMtIRQmHUvUjNpujjcBNMjJImAFMa8Dn0FL1ru0K9Xa7FNwx7NyuNxOECqI9lWMYx5bneGF5KvWkp9SVv0sQhJiY3KMRWrnyk1JjLCq1M2PSljHcZii56FJkrotbE0d15iKOt4qUnovceCnsS6OkVvX%2B6lNExL1CxSC2VTkMDKQsO9DtlENcoQGZNk80vaz1pCxw6C0DTJ75TscfVc4efOkKLvP6LlEqqhXTWLVdmqt3TPZA8aAw%2B7eOvgY6pgHCgY1ebvi2eYIiPb3VZlmjGApv4p3fE%2F2dVwcUxfVswu0eCrBLlfJeZ3cZIyzrpamDuJGdh0nAtBnoKTEjWe0yST7BaSEGgfqYfVytUt9G3KVtmGQzMH4vL9BYfbVudVkNKE%2BEnLGl4Jr0kMs09hLqoFDNi7Z0z5hcqkLshAD7eU29k1zmVdD9kvntLMUXHQ7ZIIFHJMlyGlhtMl5sz4f0iJWzr4b3&X-Amz-Signature=1ae32582705613bd8e83ee72b734c6d9902a5c921b5dfe21cb4f00f6e53849ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UY34CFK%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIE7SlPu4Y2W7pk2xUG0sqpWsbFHQ%2FpWqNzQ86gtfsm1tAiAji0MwyDXIzFb9jxkubXKc7%2FZA9erxoXmKOvMW85hmSSqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9dZmec507jJeLa8oKtwD1XcPnUq1yHjN43q2ii6orbKZRboTFhHYZOK15GHuC2ORkCPm7Ku6CSMb3QlInioDX3fHAb%2BQwaFI3OydCfy7p5fGlcMgirJkXdovxveUc5rzajDkv1QKXDg%2BLp6D1dx0pEKclsCVGRzi3L755uYn6mbvF6vHeKu8Eun6rEgxWN%2FUcAJybB9mQXSRwbbwVwhlbSiRGKiROjJXnfuTtC%2F2Aec5tDs0eaaIsPzKDTjNlKhdlzLXtXwBLcq12%2B3Qoh1VKJzoCzwQdzJcJGNXwxYAr0mAf%2F0XKMgqSkLkbQtn8Pu1aYIz8fNeWOhbBNZi0pMBLoFM0As%2FW5%2FZaM5M%2FviqA0ZZ4t3Z1T%2FKgY%2FEURhitVAIE0dRv8lTP20ucpfGqwyGXRA7RjA%2FQMtIRQmHUvUjNpujjcBNMjJImAFMa8Dn0FL1ru0K9Xa7FNwx7NyuNxOECqI9lWMYx5bneGF5KvWkp9SVv0sQhJiY3KMRWrnyk1JjLCq1M2PSljHcZii56FJkrotbE0d15iKOt4qUnovceCnsS6OkVvX%2B6lNExL1CxSC2VTkMDKQsO9DtlENcoQGZNk80vaz1pCxw6C0DTJ75TscfVc4efOkKLvP6LlEqqhXTWLVdmqt3TPZA8aAw%2B7eOvgY6pgHCgY1ebvi2eYIiPb3VZlmjGApv4p3fE%2F2dVwcUxfVswu0eCrBLlfJeZ3cZIyzrpamDuJGdh0nAtBnoKTEjWe0yST7BaSEGgfqYfVytUt9G3KVtmGQzMH4vL9BYfbVudVkNKE%2BEnLGl4Jr0kMs09hLqoFDNi7Z0z5hcqkLshAD7eU29k1zmVdD9kvntLMUXHQ7ZIIFHJMlyGlhtMl5sz4f0iJWzr4b3&X-Amz-Signature=ef119afa9bd2fac857eceb84e48a63e5ef2acf419f898e932f30d73cf5526a3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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