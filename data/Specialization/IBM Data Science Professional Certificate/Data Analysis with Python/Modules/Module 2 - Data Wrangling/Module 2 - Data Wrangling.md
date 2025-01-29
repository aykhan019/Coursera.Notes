

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZFLGC25%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNbAuzm9rGxckUNPXNo4pOzPX%2Banl3CXKJG2ZWHGih8AiEAzzgIgLTp1sB75fpRN8F%2FmZbjpu%2B2RN1E88H4KwsAyJ4qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLm%2B%2F%2FQheIMB2b7geSrcA2y6mMpv35DjKM1mMt753ndt6uuDkhtEJpy7LqD1MqJR3oU4wthpwLoG%2Fn%2FjVT1wARP3Ew2h2p6pgxASmbs7M%2FGi1FQPEhdJujCptpEvDQg3mRDuZZDsOelrP65UjL67OzLQ%2B5z9h%2BKl%2BMxXtFPGpKc2j5zybSSkfhOhqKntv5%2FH9h37GgVRyzEOxmJB7snAwP41yQCWJWJHFhDN2b4iTMjZXGd7zzNHnLeqqFsDO0LbL3SsEHPXmP7F1AVUb86bTYfvNuS3MUXNCffDoiJOmGbRwI4W%2F0DkE%2BG1%2FztqetyPxflEfR2XBqJPztilGuQyXc6GrYGSSfYqvZAq809xg%2F1k%2BRrJ0OgCGz5OjnzFb40rwtrAwHdn%2F%2B3ZbzqmQ%2BAUzN5ePBjkI3mkEIuGF%2BpeAyQlHLQGlhgjM7EQu5nNkzjltGSn%2FIEa4CKaTUr6H8uRfeRbaZ1T2fPpOokzkFcVLWSc1oA5TESnWKKWeIKn94xR7aa3olz%2Bzp%2BNGXdLLQcsuVfxP09NE6t8lSZIrdjSgaSo3l846piJuMwYXCu%2BPRSUn9sluORqIomEE9fyCa8vjepjnTrwQo7xXw5idq5f5Hi0of5%2FIHVI1bdHp3NyHm3JSVI3iIzTjqeVsOYZMM%2FL6LwGOqUBLXsbH8%2BXy%2FeDI2Ju2WGF%2BhKIv8MfbKRUWLeKhig1WNyrimte9zIZE1l6VXwZzJr%2FI1DwUoBCMN6HHN%2BCZzZxAmFBBLXNDnP5RKGYmYf1B7q2fdf57r9sMzyJEfJ2qAe5fysn%2Boyz2U7CLY1WJU2iGhdys1MBXvKUBOsXybuvfhQ6rov0LyXYsECpr2KTMApJi%2FJdXl05L4OcrMlSwkeO%2B9VGBFRo&X-Amz-Signature=60536a821511c73a321a778a9430a64c15a798a8219e736f7335bb9227bef758&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HW72KXT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID6Vmf7ybNzfzTYwGpMC2v1Ctlq47LjVmJ34sz1wVT9HAiA5K9faTGXKxaclJMCi5hbijBLjzz8cLu0baa%2Bb6%2FiKnSqIBAiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMu65ZHhRlQjNk0e1OKtwDi%2F%2BVV2FBRqUd3%2BSQBW7tFB0AJOLPzAcd7IiyWlj8zImfr4rfOfFa57rMu1MiaKpZ2KQNq7KEBhtOAdXGF3Tj02aTQkwznuUXoJ%2FOs8VyU0xlNP0gmAdgxjQf7p1JwkSvYfE8f%2FGIsCsV%2BBB0Ora5dRHRI4VBGYhQtMg1NpW2iqsnV5Aq1Af%2B7HtDIhwVooHbXhQuQ%2FRZeqI%2BLIATSa51IA9gw7w4ag427Iv4lhqWjU3mtO6HhQJFjNbd0a59ZubyHAngsGNWO%2F%2BPJ5qnT3P4JKJ1mKbiVZbpydIoe%2FS6k%2FUYqwAtc7btXdbqnx8K909d%2Fz0HqnDN71%2B9In2BjcIGpRPi52C5JeRjeiiq9z2htySN0PBjKWPkysooR6BzeVti%2BxLh%2BTvorH7xtn7QgwoY7aJEKLUPA3CJm8xjXf8DrGj6BlYtnZ0XxLulA1HJBVuYNRh1TKPPGQkTydTLmULi2ucbVLYpPMY9nmKW2jm1HjhPXOoznGJp2u%2FlmDKYPqN4%2FMgC%2BaHnfDpmVqf4GU8cAwdPra2TP7IG1YW6PWnRMRo0vYBPOz4TTTFn4Oh%2FhtI0v7Z0JfTHY3oGy3B7LjG%2F23d9zmT7AAB8RNuO%2F64lerJHtZC2Va1vYOhz388wu8vovAY6pgH6pIcQecmRBDMigrW15l5BvwAWCgNg9fnVv4zTshVmtgffj0hOgSd4nqsP14BRaH0etR2Yz%2BQ6WVri0tZP65WAzL0xbTpNCwkesvLKU5y0%2FXE9em7uM3xSiIN7NOq1H%2BuPT8ed4wpyA%2FDNB1GdGrYNptlWZRDcwoRBCbQTZo%2F6elTjJLUsdlG7EbChArZ8JcZ%2Bx%2FSgk6Zfb%2FgPZ18rVp%2FHoGP6Jn9e&X-Amz-Signature=00ddf31906f550bfcdbb3924a1c2332d5977e51da0db1ff46a2a585ea970584e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKSATZCW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCc8f2SxSskHVR2tiwI2pRnHRUc7HXJAu%2BVjma4OXqxZAIgZ%2BZ2AY9Wp2u7fT2oqYrg%2F5Hb%2BtrOAyxbbpJE%2FoWIYIMqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOtJ6UxrKzvJO6xQACrcA7%2B6HUVCAAo46j3r8Vj%2F0P9%2BSpDDlaF0mOEbPOAYTmvitDhtatakdRXg2f%2F0Urh8xXSACWq406aZXDR7MpXOaJdEnyBeY78%2BG6EWm%2FZeZhLi5lwNabJ59%2FigKDK8ZrXWYnodYps2tyxpXi5eF8PKNqzEAdCdTefKEJng63UdJuuL5WKUk8CZSV2Ma2GJ4vwo4y%2BSfPEfLpBbJagU54Q%2Fdgda%2FxaxPkj1hTcBboyJLzxuGTYCE23PpCdNpevtHznO0NxA3drfN9N%2F1xt40y3G2l2Qc9K74UswGI4%2Bt2eYGvRQ2YFmZXhQRERQUT1wc06Q1xdo21%2BZjNJ8b2UhRWvjxv4OgbtfYis3gKK94KwdthovP1rwbjsESs3mQLYUbCW9FIotrMpy5iL3OaHpK2ayC1jaWcMj5quukWMmkbQm%2F2yX0N45ZhCvD8VCSq7%2FkVLS6Gp3Y2uJOR0X7T0rD%2Fo5lTc9nchK%2Fv%2F%2Fwf9FSCZ8%2B3XBq8oEU9zEmZCqzN73Z0E6TY7VchdKcEWrHuT8yZTbMtYbJiqluLs5fW1nYgsO7yK9FJIIPt7ApnYIRnHXJrueDionppp%2Bnua57ZMgTpyh64n0H02gf%2FNbsZMMsS%2BrohWsueZ8o1WdMsHzDHf2MNHL6LwGOqUBoPCH3HziVZ8SOYaoM3rznMPFV%2FWzlFfvu5UDe2rGH3o9TH5W68Oux4h9nuVpxc7RWVUea%2F4H%2BaOKvgaqljUkJm2tabOqIJzSTp%2Fyq0Rgf9WNaoFA0FhFgWjZ8aCT3QVZ5xjbAlAdLSfnUZPWn6ZAcaMk%2FjLsdewATXnxWR6%2BqfYJqbSms7X2V5Xr0E3ymN87uG9OVI2%2BWM%2BA%2B39wcfD16o07nixy&X-Amz-Signature=b8e1c0ba81c1459eee3024c04a6a582cf123d321038581228eac643980c5a030&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJEBDXJB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2BJhxav7gqh5lUXMm7SF4Kr76HcsNVSKt4pgMakxfZAiBXjCJtOjlQiZgFJ6d1mieComIsanurl84%2FV2hmXemCNiqIBAiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBdMZ%2BBQM76Nu8BfJKtwD4%2FQPB8SFo8Eq0qSC%2BZuBT4Xt6hpPVWv6oZBTAf6Rjq%2BaaUZX%2FSZ5K2xWVhMDsZUXdJRNcp4LVMLy9zzcfwz%2F41aPBweyOmzE8ThHTlnsW6ika7fVL9mAVVXawjRsDRKVtheotaLEh8QaBOhYnmr61K2pvZrBfo3vxHRRvZxMGQnzv%2FPwNGIL%2B9dzhtLn8Us%2BHXFiWgBYSOGyN4lF%2BZiWrZKxPrm2YdGVY10bE70FfHLW45S1W7xxSevQPgoL%2BlMgHLM2ul%2FyhvHo0wU13DKX1qz%2Bb7Rj0td4u0I0ZLww4Ivohn622Ix8%2FWHT0TA9Q0mwCBznhFZWt1KpEYhCO7XCfOR%2FUqThohQsEjbPcPdII%2BfA%2BX1dUVUR4x2KYxQAwu3NnT%2FVK4p3%2B%2FCMlmJ%2F6RZgKSMMz6G%2BDQaZOUyqabs4fiJ8X8zFg4qjutYEi1XcRNJvuNNBre3x8aVFpduhjctdm74OqNZf%2FB6rpUAnhVjLct7UiMCrlmpcWfBy9wiX6F7n3oNJKfLW5L4zZ5CHsF6IybI9V%2Btei1R9gaaq7%2BhyynUeO6BXC%2F9nBox9ZkS6yn%2FmOH2gVBsDMH0nMfu9XTqDa3P1%2BCT0G4aK68G1YOyYG%2B4AXDMiu1T7zxU7Xv8w0cvovAY6pgE%2F0YGSy5hLM3mI8ah5e8tma8NtkE08MAbEGFcvYF4%2BMztIbDcS5GLn0YEEJlV2FT0T9bjatsuBsOKK369jit2e49q0L5uTyigrEJbbDTR9uFCgGHSOGdvr4aRPwTweTE0ReSeUnGP3f9Q4H8EsJ7dsZ9To2lRR%2B93EynWH8jjvMKZq65Bl3gS%2F4OBiB2Hk0iUJB8GgMIuGXAnnW30%2FYI1DbL5XI4wA&X-Amz-Signature=9fb4ab7c74e3146793b2ccf6469ad0d40afa2b62de0477858201419e2c9d895a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JP47KKV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZsF2RoQK5LYIYjY0EpZk6G9e918f3bswcp2CV1ZVPEgIgSn11jrAzFlrbh1irKIK74I5PUCsP8RNPBnW5jYZaD5gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH0oMGXBIHG5U%2BTBircA22XNkHbI56NaEfRUWFHC4zsKE6McLDSRxyJ3ZIV4aSp8wJ8ygnKfr4gkPZLdJeRiKdc0w7YKtB5tC2tHLWvrhwrxcSf%2BuwveVAW%2Fa4Y12ViGuOhFH2cB%2F3%2BPYwLhX77zxqxf7fdFIQFCvJZe02APIZhDQHp3dx3y2rtMbswaHKrtwTqp5Ik%2B3cIx7090KcR9yn%2BJ%2BGQmTAkzUWin4GpmsOLueNPQsF9Inj0Z6rcqNJduszCHKqepDOLD11v%2FGkdQuVVQLpxeQvB2CBwN35U5qG6dyhldtpzkHVOlkXUb%2BJtLbDBLimgRj9om0K4MjeJPe2bQqpdCdz6LLS0mwsFCTkqXmbFWkHkypjToRaqqg3pWVGHRaQmiHmQj7DkJSC4e142%2Fju4YVM2890u55NSdyAxShTaICNqORtheWa%2FZqPj%2FXlP7GMejT03AgB%2BXGLNmGJ92zJvQ9rGT7s9mgeBAYLQcxolcWCUiFzyhvfz2o7pN6hsivIdZbgFlq5uN1%2FOmCFDUTPDftZ5xIRpm%2FLNKquoS3P%2Brw%2FS7g07E4ilq9mEmyQ9q967uMhXhqKtGvZAsWeGJ2iMmT1fMcpxexAi7cM3eGljaxvC8s%2FB8m9wJlOdYhTZvTzyW3Ml%2Fb2cMOfL6LwGOqUB9WP5Dho8TpSd7fcYXh7cb3BebFYyI7XYCvwofJPRSNFmRaBEtzUbcDUvFFNWtqgmDs183tkQmY0msOthAeWgqoZJQWReLkEe9j%2FTsT4I4prGm7Yw69f5sSqMfrx4bN2jM5gSX9N86FU6OGCCdNsrDXo5NHkl99idAZIGL%2FRTcCNdfTtjjFeYWfCLItAYfMpAAL%2FWvB747TaociZUIvCsPRneCXgl&X-Amz-Signature=93b92032df0734721cbbcdbc15d211322c46eb57e35fa26f3ec4e6272f754e24&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q3MPQJN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsBCXK1YFPNltTUwd26hvWXm0%2B%2BXcL2XTic%2BiopXNrrAiEA25TBa1Fy00MUU%2FGH5SzHWefzo38wVcjyPzBhcc2q7poqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJDVqJIoeOKmoTiMFCrcA4lJWB8%2Ft7M5xxCtYKSAvuHMwsUeaRvYjP%2FOC%2BSWB%2F1dBB8XlNw%2BJn%2BoMU9XSkmn%2Fgz58PlJNs1BfAJgIi1ry%2FiNk5Jsi8KGnWtcE8JGE8bHAZE2FXuZvXFqms1cnOKiPtbRuLslOU0MpL%2B1wX4XU4KTzlG2SEcE0cbLa059vGbERR5B06%2BAKRJ92PVytLwwPGevkS3o9Osol0KAZM95xXheTS9jtCK%2F%2FFt6QddyO5rQPwcDtMkwp9FhwfHux20pUS1m%2FpaWpstL%2FMJaDhob9dfHWr3JIgR93sRie218XrqXaLULkNq0TlWt0A7Q2bwZ0eDusyt9jMZI94Lr3ZrVUCD0vCz2XrSRHoE3nLjZkpNPmUWeCXXaZ3mihB3jmCjPnevwcoqdlxiAhcZJDAYe6uUYbgwWsfMwZG1u9dySRpH8XJCBZXUEay10NtX8hzBHS4gf4pPLkma86yZZmO1pcRCojvw0%2BqDzC6JULE0ICkhz3eznRMRDZX1lUgB4jaA9lpQQ7G0I%2FS7%2BhqOoyZi8rDE8%2B8ksB%2BR%2FC3sVyE%2FoLC37BXrypM%2FO5kS2R5im%2FU3SMuDzql3aXqmZ9L4SCgYCQDIyD9Fj%2F%2BBqq3Eb428GivMJJJenzZElWIiJzeOwMJLL6LwGOqUB3ffEixSP16ggfpuq7HA10nhl4jl%2Fbq14qjKA8kOvc6s%2BwYHpbM0yYG%2Bl0wpyKN%2BDsppWpGo1IpPwPIAFvG7H93vYefPzW1sn%2BWvMYDhVHAF3bDYFgAQqN85yI%2BibqXdVi2wf15DD8UApHp7erKCxRm5hr%2FcLS%2BQCancUJOAMLjn2l9vkS3QKfwMrFqcLokYYbKKaB1ubzYl9m3KstiU1FhOrYWuM&X-Amz-Signature=b54859cf536800c54e636c1fc940dec4fe8fc8acd86814248325308cd50141de&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUUERMNR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG4kn0JFn9uJ97Us7Z14ucM6Oa7AOWjXw4XPN998ec2ZAiEA2bhkr5yPmfBvyJ%2BLITAz3qUGBimQyueB6cR6usqTavQqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCqjdUmMritOMwZWNCrcA4HGGWK1l%2Bjdzb99xaXKN7wSFGWtZIiHseXlVhcQxA7tUod6uFajYyW5X7%2B5jZmuoRXXTM26R7fg4RDLaA5r%2BqE7cG6y9atLKWu3fnpSoxol3CwStMs78jDvyzY92RQlZ6kaP5%2F65CRLYnIuoGMMTFL6Z38MKrYVX0sOaxTobmvCHRG3BA6W3ITrhYH9H%2F8XPNKv54buAxqxDw5cADgFtxFs3YJ6YR4CD3f6jK%2BQbn6uaGipYPVCkcnyPLq%2FW6GXs3nznRiRp9yEQnrNKCC9rr%2BZ3HbmEU8H98lCT1x8vZCUbrDBHtHK4l9kPHKTkGJYiY3vA6PmSiYiVMta6bzqUdr9eqEtsPwtEG4Xbnedq8OTRylgA6SNUw5%2FvrKeVv%2F2IU9xkyH5E2m7vJPQJQL5ERaHr75LbF5e2Eax9aEXeQRONIUyFLeTlsV41k3IWj15mbOrprTOh%2Fb%2FlKQejZCsehUAmwBuFDHDYrxXe7yrwoPyE4GOTAfEyj005jVkph5pjShb3syTd0aKrS1c0bm9spD%2FgKBlBobP4CFGAHoBV7NmNNJcdzI0ELc5uZq9xkjkdsHlR%2FC%2ByIUfnXjmeZ%2Bn95wUUCdDfNtX0yKmDgf4dnK9nFasiJpEtXYqVJ9MMJbL6LwGOqUBnpOKQfPFiXIJ%2FU5Vf3j1smi0ORcf500XNBg8XbD%2Fer4LepaMP2QYmYYUHtCfPFrWAT3M5sSgxKAucVb2hE1vlCHLtGLB%2B5WSHJC4ZobE7zDHmq8ZNhE7CLeUt34CSLcDs7f15Gj6s4Se32sxmEw0yWX%2BBAfe5qM7wPV8TTECnhdfKGUWAwA25DK7bmCICGHK%2BIt3S8wXOcCCGcYyQbfzAq3FzrTn&X-Amz-Signature=e726bc056cff6fe7f16c18f1c077665650c3a3bdd00ad983a146ae31b6c1bf9a&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHFFKYLX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8cwFAlg7BM0qq0urQiXG0ydhf%2F%2Bq4tm2hMfTvj5zrJAiEApDC%2F6mSjOvhMFRIoguYjeLxDMAlmT96uYaGMOrRJ3t8qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNIIKJ874Ci9Z80fGCrcAwFY%2B2uU8zAl9XkCaOrt4koM7up4SHy4IbEFyVfOf%2Bo0pjePUQmiyMs6%2BuvLIya1Ef0zwWSXEWnwmMy76aO12xOEjbytvNuvferBEqFh30xCEuDLc%2BEqGp8oAHZWiieWXjdvsAzBtpViTQi19kgWipcF0322Lrbi7LAn3yWoVqIE4aw63EaBXV2BPJGZaAOU%2B%2BFlvbondg8YiMGcilfWEcpRyNZfwS%2Bej2PUL8JhiQfdICGO%2B13lReUKrIiTxa2XyNZKJNvCpWLDqs2PYZ89OsFbnPjolUG3Dy49qkbW1hQMiONbGlS7AU0VmoF3roZjUvZFi0bP7Z94nCbSyHS1K%2B7bARocqtayj%2FaFgR%2BQRAeXfFi0NULLvde11HpdGSB4Z6JUJMgENHWIjD%2Fb26oSj%2F6WTQSVZbzhiYd9ii45280SonPQVqc7Spqhgpk%2Fq%2FUocar043kY%2Fr107GPROetr8e1%2FGVG2MVxwB13ANUZjP2NtG%2BfHMPbIiumgKsrtVKkYqeMr%2Bcq06lzUeBBFWbpgEG6r45mWth4dYtFkYwfSc9UGHYC%2F2fGJE%2BcFUw8K3ZobTrqJckDMiQB5qoeEoPJR%2F2FgaBlCCr5lF7%2FHWRGfpzg2d5pMIJddufxmB9tbMNHL6LwGOqUBzRSCbCj7fMIekUsRPsDHuzbD7EGEMpN1qwGT74imOw7w6eRtSu47lzl007NiRWvb7ZuHpvpwJwk%2BdlxpRv7CUmM8suZVVwiUPr%2BBTjeJluVD9S6tRvIZ5BX%2BQO%2BWrnuj1abT9BAFyUyaKeAeejNY4CPPi73qxm%2FkN4fMiNlfNAxkH7EJbHINM%2BvdyuyNuMm%2BaAg2hos2YT4pjyXs%2BI9nnFapclzH&X-Amz-Signature=c5184ed42fe8f759073e9c38dc4d4cf90e4c0686d05688adeb427a80c74ef766&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JP47KKV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZsF2RoQK5LYIYjY0EpZk6G9e918f3bswcp2CV1ZVPEgIgSn11jrAzFlrbh1irKIK74I5PUCsP8RNPBnW5jYZaD5gqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPH0oMGXBIHG5U%2BTBircA22XNkHbI56NaEfRUWFHC4zsKE6McLDSRxyJ3ZIV4aSp8wJ8ygnKfr4gkPZLdJeRiKdc0w7YKtB5tC2tHLWvrhwrxcSf%2BuwveVAW%2Fa4Y12ViGuOhFH2cB%2F3%2BPYwLhX77zxqxf7fdFIQFCvJZe02APIZhDQHp3dx3y2rtMbswaHKrtwTqp5Ik%2B3cIx7090KcR9yn%2BJ%2BGQmTAkzUWin4GpmsOLueNPQsF9Inj0Z6rcqNJduszCHKqepDOLD11v%2FGkdQuVVQLpxeQvB2CBwN35U5qG6dyhldtpzkHVOlkXUb%2BJtLbDBLimgRj9om0K4MjeJPe2bQqpdCdz6LLS0mwsFCTkqXmbFWkHkypjToRaqqg3pWVGHRaQmiHmQj7DkJSC4e142%2Fju4YVM2890u55NSdyAxShTaICNqORtheWa%2FZqPj%2FXlP7GMejT03AgB%2BXGLNmGJ92zJvQ9rGT7s9mgeBAYLQcxolcWCUiFzyhvfz2o7pN6hsivIdZbgFlq5uN1%2FOmCFDUTPDftZ5xIRpm%2FLNKquoS3P%2Brw%2FS7g07E4ilq9mEmyQ9q967uMhXhqKtGvZAsWeGJ2iMmT1fMcpxexAi7cM3eGljaxvC8s%2FB8m9wJlOdYhTZvTzyW3Ml%2Fb2cMOfL6LwGOqUB9WP5Dho8TpSd7fcYXh7cb3BebFYyI7XYCvwofJPRSNFmRaBEtzUbcDUvFFNWtqgmDs183tkQmY0msOthAeWgqoZJQWReLkEe9j%2FTsT4I4prGm7Yw69f5sSqMfrx4bN2jM5gSX9N86FU6OGCCdNsrDXo5NHkl99idAZIGL%2FRTcCNdfTtjjFeYWfCLItAYfMpAAL%2FWvB747TaociZUIvCsPRneCXgl&X-Amz-Signature=cc61252dfff712143365f80cfd585e1031aef219aa5a1f60cbb608900d1d783f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JJTNFTF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpOmHjxk90LtTdXh8vAcoVWhWGZvxuequSKOo9S4UnkAiBQQ0coHN%2FJzp1oj%2FhZjZGxXFybMi%2BhC%2FMSeZfCqXJhryqIBAiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuY20%2F%2FLmdyhz7JDqKtwDOYACNCYh26x8uwgSTSgDz2zjc4zHyEtvcESSEGwxwATZYEbDE44cUpRoxJp8luygOyNVLyPLTcRltr%2FklBFvgsNmetJruE2V8XErAtTYXmzDzDSomuJQugYOQqVrKlwOesmVGA1SV2oYJ937wPVn6TQbQ1wV%2Bf6SrEkJlcD6NW%2FDXkyVd6XbMcLv4vcrtwKt8t6%2BeCqTtKu0%2Fgp9ck5LRwlAug0HHA5%2BphDvnSCEheHFht%2FQaqnD9YDlM3iyzCcaWc8XeUjO%2FFjHo68ODf9wup%2BRFnyt1Rho0Wxelm6oiioQwDTSiOiePAlLl179tM%2BmxOwL77%2BI%2BuLWzlvBsL%2F4%2BLyXGQ4YDDJ9H8IPJ6z6%2Fj21e89LucGZ6D%2B%2Bvip8AHAnto%2F4qu9TL073HOEixGKNbaDq7NW2pfVIH7gy14p4l9%2BYqyuCCnEv2wt1eWbDqMKZ%2BLXwvq1z48QCuczqJkQJTBUgFLLyM12nOxeVDYz2rjSBzZaGy5bthHc6IDvIWzWTr9PkjB2TSjYCcTZgE3Jefv3ErQldNlHFXx4hPLxTHAoIVM8Ooh2%2BrfmUK4r8wMXNQ18hUf0rBxBy8vXpFBiA9kEJOWdIfiJ5OHJDRd2el9jzQ6TckMdH%2BKNkArUwlcvovAY6pgEQUg368gSZ1ssrZXCER2TXgaD0l4PEcdQSVE5V9KwE6il9ezapZw%2FzqRq9dGQS9V6iwXntkiQdVtCqQdJGCnrucGWiZ9tbyFq2m0Buh%2BwloHKVKoqjI0h86IdgZR%2FT%2FjNp2p5urDup1aPou6q1ykGLlteyMHtHfRL1eX5RmaXcKxwxAziIEwluknnJMdrHk%2Ft%2FAi86mZnmX8n49gdc9sqXWGTM5FUa&X-Amz-Signature=c502ca79b79ef7374754264ffb30e4071f9d1b0308024941d7342cae88be3439&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JJTNFTF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpOmHjxk90LtTdXh8vAcoVWhWGZvxuequSKOo9S4UnkAiBQQ0coHN%2FJzp1oj%2FhZjZGxXFybMi%2BhC%2FMSeZfCqXJhryqIBAiO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuY20%2F%2FLmdyhz7JDqKtwDOYACNCYh26x8uwgSTSgDz2zjc4zHyEtvcESSEGwxwATZYEbDE44cUpRoxJp8luygOyNVLyPLTcRltr%2FklBFvgsNmetJruE2V8XErAtTYXmzDzDSomuJQugYOQqVrKlwOesmVGA1SV2oYJ937wPVn6TQbQ1wV%2Bf6SrEkJlcD6NW%2FDXkyVd6XbMcLv4vcrtwKt8t6%2BeCqTtKu0%2Fgp9ck5LRwlAug0HHA5%2BphDvnSCEheHFht%2FQaqnD9YDlM3iyzCcaWc8XeUjO%2FFjHo68ODf9wup%2BRFnyt1Rho0Wxelm6oiioQwDTSiOiePAlLl179tM%2BmxOwL77%2BI%2BuLWzlvBsL%2F4%2BLyXGQ4YDDJ9H8IPJ6z6%2Fj21e89LucGZ6D%2B%2Bvip8AHAnto%2F4qu9TL073HOEixGKNbaDq7NW2pfVIH7gy14p4l9%2BYqyuCCnEv2wt1eWbDqMKZ%2BLXwvq1z48QCuczqJkQJTBUgFLLyM12nOxeVDYz2rjSBzZaGy5bthHc6IDvIWzWTr9PkjB2TSjYCcTZgE3Jefv3ErQldNlHFXx4hPLxTHAoIVM8Ooh2%2BrfmUK4r8wMXNQ18hUf0rBxBy8vXpFBiA9kEJOWdIfiJ5OHJDRd2el9jzQ6TckMdH%2BKNkArUwlcvovAY6pgEQUg368gSZ1ssrZXCER2TXgaD0l4PEcdQSVE5V9KwE6il9ezapZw%2FzqRq9dGQS9V6iwXntkiQdVtCqQdJGCnrucGWiZ9tbyFq2m0Buh%2BwloHKVKoqjI0h86IdgZR%2FT%2FjNp2p5urDup1aPou6q1ykGLlteyMHtHfRL1eX5RmaXcKxwxAziIEwluknnJMdrHk%2Ft%2FAi86mZnmX8n49gdc9sqXWGTM5FUa&X-Amz-Signature=5d41a18e19ec196d1fcac9c248e3c5211b94cd8fd06599a47bc68c33f5452940&X-Amz-SignedHeaders=host&x-id=GetObject)
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