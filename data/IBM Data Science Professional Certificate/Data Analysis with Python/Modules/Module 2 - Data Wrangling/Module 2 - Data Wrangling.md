

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLQUOD2T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID7zUfFPPoqZ5uJthmz5m234Izmif7hmijsl%2BBfkNS8YAiAxGIgBHl3riVYKDJM1hvp2K84JLHX0xxFIfX52Wb0bSCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPwQ4WCsluSxp%2Bke5KtwDB68MYlLF7Zq581Xt8W2SdXKZMFK%2B0tuohSF%2FGtw1Z1HZEUg6LQ%2B%2BMJvzZ39BWHR7jZV7vAGJSf6zc1dk%2BnRGEdLn6jqddh%2BngZaxKWt0wLFkISWVc3uaXXgaTgI5EYhhqPC1mVaIk%2B7jlqA2rbzrTl2TCVr4JjaPJapZMx8Gj9kgoxwElq8VrCUHkSOE3f8c%2B1%2BSRHx8lFW5NTVRalHFe6WnYcWzWnCdRCDX5Fy9P14sO%2FoFZjWvhTjjq359O7pRrw8pRZlzeJlzqHdmv235oo%2FQStBMXz5kbqDeh7dWR7Gph3TZV4u4c8doC9%2BIYGEvuoNKuRbrV8gsyH8xQwjwNbHtTBA0E1Y5zdCeuqWAlrV%2F%2B9BFbKKSVqEC9Qzb2oZBny7XHNxP2BURkiWjSaJugHQ40op4wLicX0vZA009GMIKBj5vJoWV%2BwXHMX9%2BsVQ6GbMzSNJ2%2FjCfZkFEIYwN0bo%2Fud4PRvEiOj3gNNDWJsrzBjvdfmyH4cR7%2F5PS29qXP0lvA6%2FIAJOtGyO3JkmL9GddYYZTLWosFMwrC6G4HC2wk5pIPq1QrckrYh1Q6f2gipLWrdEZYR%2BjswXUMWgMM3ogWkWEBNQmeHXu5Zu6DmMUqk2XNoyd20sddUgwmtT%2BvAY6pgGzGA4LNYD%2FgMUcsIaC6zTWHCJ3EmvJQJci5oz6ffsdDV2jDgxOqiTwIS2Tvk8Ys6sSemi%2Bog5x9UdgvmZDa6GqjsZbbd2D9SWAaesn6Kk9hGf8Ltk5Skus8N6B2TFJw7TFh396ZElrRjbKHBzED7oec5Hz4eVHB5mGikZtiicJ4UxLv9bDfNVkWHiOT1lcNmkdWOpm%2FZNtQ5LJmE%2Bi6kNpHylU7DWg&X-Amz-Signature=3e926d8064c4aaddb252feabdc1fb42dbf7e51f4890d2297d0a6e8eaa707a613&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FZNWCKQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr0jis04kKf6IgeRvrx1zSfe%2FtJbZfnBrzch0Jfg0GFwIhAJ4o%2FE10nnYwEV9yOkfXVjxseKgbzJGQybhu6ucQiVVXKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVXO9Pukz44kMJTmwq3AOECMmJ%2BL9s%2B7zwtAHJuDMnJ6DfP9qHCZxzpO%2BXUd6hAgfLcwFSkXGptdDBuunKu8E3HVd%2BPyoUvwP%2BfnIgeOQsEntBhrqytEwWnOdv5zhuz6byqk2KKRWI97sf0kjAhdexP36yjD2xJ4PzXUpQziqVlAKHP6T9NRjDlS2qjcUvd4gySqq5PEAC5E6W%2FCobYUVSrZSHpJcClX3%2BxYx%2BIcOQpx8gVoH2PY4sTNceWl8Z1E%2BD0JF9UqM7iVaLFwrOimvkY6laYRQomhE0j8kIYpmtOGcEZx05ajPVuVXa9tnuVaMHNhObb5xcw389oi9%2B34CefBsWOtlMs%2FRx%2FKeBgGcGRGmby54d%2FzLL3Ykjol4QXGZip00ygAzi4tc%2BSN7l0fBttGj4p%2B7yga1zf%2FROYepctcM%2BSM1%2Fta42K5sdXG6ZysISdkQe15cPGVGDEtKfGDwZCCcZskg3ZBdr6FFJgtPw9NLR1iMJd1hsa8P4g%2BRP7KkFsJHv7FLQED6ePYoJftM%2F8qDCpzwK%2B0slkQrXfvW49uVdkTB0FGKVUp5J1STU16Bs3MaRrPrQqGtcV7quVpd%2FL0zfbP65DlBvirFfK27HEqORxvwyb0ZHDH7kKTSLNQyw4jbvGMwMK3WxqzDA1f68BjqkAYOV2kXLlCoRL%2FBTIB6%2FyycUaEKN3NLWBbrOZECvT%2Ba5dVUxM1lUDu1ywTMJh4KjEAxeqAD6%2BjhlBI3%2FcxKVuwFo51RfGMLfKlbvk0e%2BWyiZLYWmSrn0bs4jse2AvfbFGmlkcu884NXZZkIzdC7kFBTMT0lY4CSssALnk9La26EkIQsDvxhEkwKmo5W95xgJ5fOa%2FuCFUF2CQzNpvpLPgxdIZlqM&X-Amz-Signature=731f587bd64a7be0e94b956263a426bec308479544790eb5090ef163ee1f7edf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D3PKZNU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICe3FuXLjfoU02tBC4wmX7FwBiHTTqaTKBdknu17GbJNAiEAhXswB%2BISFF3GPpdd2ACfVBC1XWhba4K59A7hdpoW38IqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErE6%2F8DZJj8jlZuVSrcA7It5IzgXkAdnjluflFEkTk6i6wgYFDnjPJCbaiTsz27%2BdGvjj4XrU3YrTSHOcK8ZqXfdaHY9%2F2sB0QulRSXbA%2FQbrJoz5RBxMZuCb472q7HZh0MdfIjscXOfLhtxaaO826bFTjpIaEHjT%2FpIpa3oOtP1ka3Gk73%2Bvow2igiYNfNeS3JwCPFHrEJLF2Do5fV3obWvrvTAL7Is1eKEatcdhJ8W9nXKnP90B604ItVZtuxxp3fC%2FrQLWIUGbnA%2F1UTkrQ%2F0WRScDl%2B4Uk8Zhby9q7BSWDMTltK%2F8ATxW36S%2FXyo%2FbGfVME4ui2tuR9CYNB3VWiFLH%2FlguTGr4sKsjGUys4rgUzthecnM3gq%2BXJEWmLNrK1JBAzljs0Pzvy9zM%2BUa5MOWVzhHnrVOPurX3vf%2BzLc6MTKPZDv444XTOnhsZlagfvKevgQlWRcH0JYeLmZ4pjxw3kBv%2BjsRvd57JXs15tKeKEjt22E52k80ltbGJt3RWUQ8hxS3AXuPtrsf7exK9UGY%2F0yYvSu3Vjosh1fVnKHNwYu%2FmIT%2FZFyMKGAb1vcfYVRAhAVC7no9F9%2F1S%2FtW2tBH9sEnSag6SEAGuRpxvxPrK3q%2FSVbU9LzlXvOr5XWSVcH3hSdmz%2F6tYnMOLX%2FrwGOqUByVQikTDBhqsQ0l%2FtvhFzQ4Ho0QP8ItQkvbX0XSg7RmOFEQMMu7ZIT%2FZZVTOHGRUzIFtXuaIM76tCVLOW%2F2dOZdcysEmnO1nnRIJUtJMnTrKTkg8vqdvCTAjvx7iS6pvwPtSdgi8LAqCdGD%2B9DG3UYJRT7vYOBkhlW0hFyZaVH5IEAjhxofI1OGXhi8mksYixa3hjO%2F2WElBGjHcILu145xEzDYgW&X-Amz-Signature=8c20a29ab306b50bc4ce4dec4e2bea7790fac575832123478e4f73395d1253e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JDC7MCF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaKR2M9Lec6PGGMuA83gT7nlsQaF2s9vu141Ap52rHggIhAOSE2Sqi1DQDeN9cWxhiSlxsvyA0RiVxxe5ptj563F5KKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxA2OCUQG9slkEVxL0q3AP2g4FVa8x7MuWz4yTzqcYmVSXS7UjIpvG9HsOm4jO9JkZIEXL1DdiJj445%2BwSvEtCrOM1D85xRIxqF9fcjVvRKkOwxjbpjVtYq38hZAku55ExImAV6eJz%2FEkXqGebeUsyn0oYQrKc6Kud%2BLswiNHB71OeGqCReSz412cYxBOV0HmLvVl8%2BoGra1pUOwR8BV%2B8CD9wrudZ2vlb4%2FOeB%2F7Z3kIIDn%2FEaNRtFhWmMMRATgAmzqyBLy4DL7E4tZdr9yeEfPt0JjIpupmXe%2FqN8XvELTNyflsPNpSFTiP7AizNrxW%2B5YDrhmzjQi6GGtl%2FW%2BDUxrlSBMjrj%2B%2B3kt57TRXLU3lriNXpjKUy59aowxXOh9vQZkRkiKvRbjHnsLuc8fCffb3x%2BqlCVUT9INiWD8gCV7GOZ1qllAtPsnTZmZ42Q%2Bv7mYqpmRuhDanTbGWFqVIoJ0CPQyF5DKc7ohWuaP2WiFvboyPAHCyIZ77DW4D2UMMX0vqzc78%2FjExC9odyjcMacZxmbq8m7Uxyb433Adi%2FEaEvKIiKGbtw2kwEv%2BKXjLiUVTcA6QKG4IirbR4XaraZ34LiW%2B6YLTLxSLmV%2BOrW1kSsz5UQ%2F1DIFhahxpt6kZ5AKbBGsWvviYUH7vTCl5f68BjqkAVCANC8zXiGfxlw4s8BGgQJoXGqc8mt8Pzmv6Lri374oDeat4OCYukZ2%2F0de5oVO%2Bsm0SIFnUr56fOZ9pl8hAMYi2nAUrqs%2BzoOIsHmdQMM1HwbTFZ6L2eau9yQdheaIlsNQGR0L9Z9SimxICC%2BG9H0XOjg%2BWy1E%2BgCc2wMQPm1tJdF8rtGToZe2GktITGUjj3dYQa3mnudYTzG98bSZj1Ql5vMF&X-Amz-Signature=6eb4d95e1fcec45f99e55e8b1a4627826f0b0c33567442bdd893df3a156f5620&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJI7SX4O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBJ5EWtuF2L459PjXCR5jg9L7yvv6irkXEaRbldTt951AiEA%2BcJ2jv7kiMBcSxVKQkbX5j8tKz1qgQzktSnoVeXI2bMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsuqUhYshAKXG3B8CrcAye8HzvC6pAtBVDI%2FgD1TL1LAZT7wHUKRdhzlgkurd%2FKbSup5NtgbTIN3gQWSY%2BFrcCifeD49I33UKhsRmk8rowrM1VqyPTpH9GZmXLj06cvEs9FcefygJbPq58stbpGTy5KKpt53yvq60o%2BMYCU9NBynI48Ef8vb%2BxZo6BZle9OsONy01cv6HxmSrTmsbCMcmEcbBdHcIP7m8DOezWKh0LF5gwn%2BOcYCrqB5bPjO6XJCZBJ4gpq%2FACYpAfZ7WFgER%2BkhGMlMPdIf4P9oXoGCBVeFxknWnkxTkO4UlbytNt1ob1bqY%2FCmOJu9jGABHrGEks%2FQAkvtbFVQE5y0jc85ZjR5JemhxSgK9EUwcfXrcob2un2XBjMJ4AKQ9nybzEqcrcymrc0iZ2MEOJ4KtN7aQuFlbGsThnY7TkMXas%2FHPKAdewqwty6%2BJyZbzHLpuNrSU2DcAI3xMf2rNyLrZsTT9J0jmGTehNbZSJWChyka28SWw7tZCdjsY42xoBeDMc6mN60950eGDJhHaM1h%2FgrTJUdNhfv02HDARY%2FWXUQ2hZZMry%2FeHUl6%2FS90b%2F3Bh9tP%2FyBxLdkmXHwzSZue93KGY2ikf3DaMuBJtk%2BLXR9B5S8UZ4oUeeN7q9xc%2BIlMLTf%2FrwGOqUBJZDNmV3opZdumOsg4V3s8tzPAAZzBnnR7Ny1pIZUpm3hukS700z8T5bvkcl%2B6d%2F%2B8Qc08V14%2Bht6vSLZ8FwrRtg6NApBv4vYvfViAlxdF0CmF2wDatR%2BkWDceFgxWIxdGte%2F%2BeDZVpOhd4sgzKRp0GCL37vMCBFUXrhiC5L4%2BSpIRKR1VPmnI%2Bx%2BbcFUkGnS1rf%2BwTQVYChcpmImWfhiT7Fc6Aft&X-Amz-Signature=906bb20384e458be00a5a6223535fc2460efec385c60d0e1cd37af68a4c52170&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBRVBDEP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDum0cClqAoh1hdmmlgm3wGyaIPxaJwNsbYazCWFN2kVAIgKXssMC4%2Ftz0APJDa%2Fhz%2BmbGeL5HyRsqbz1UWdeNWFyAqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMA2Jdj8nBrqD1UaJyrcA22EKRddtGIfZkVM6gSP5Ljia69DfaorFF9tGf444l4I3F0WBN0UMjVDFrOW%2BL8sadAucwntADTDfhKnazAbI%2BJBf3V5%2FVBfVo%2BJ%2FZKd%2BJAR98iiLlVoisDwUXJ1alIsoWJ7pGc3p3dZ%2B1%2BkIP1JbivssbfeqgT5yYBaPEkYRE590ODbW1iUgiMhoqlvBopgJL%2FtQg23W5SmRnhE0tq9TYhwUis3jRixuh%2FOI0nRnTaqiirMYLaCg8N97VtaS0mDJXuOizwiI5KC%2BfjcsprjSF9jUECGg4qhvTfAdDLGm%2B3yCLbr4tsrTnYF33njzBh9C3SjydVITqmIzRMVVL9rNOIw3FY8yfS98ocKga%2FXVhgjSI%2Blmr%2FBfxdyTgedP%2FZxBCvYnNaky1pO9ML7FKidUNmgJLiCpL4IQszM20bdQXYqPBI3naJs4l%2BF2%2F1jvNQwCdF9NCmArV6xno2za6XDslzfnnmmEx4FFMFj%2Fn%2FV982o0dZ4FZJ5ljjtovzz6lzeNL%2BSOhjZw9hhVgV3HRroQKrP3MU3m%2FOm6e8PxBx2%2FAlIZujr5xh%2FmkgYBOD1xGz%2B8HV7N8Q7dotAe7B4AjPxLsFBn4qIr7OILMm1IucuQco249iOVDZxyTND5ZgtMJPm%2FrwGOqUBvPAFGgarvlAWFNGhaORGe6wEU6G7ojMvUrXNN%2BF5WpM3JP15NeLVvuSPn%2B5qGIzr6Bn2yATr9qA83%2FE7EpdAEdSaPF90l5ukqgXjAX2Dzok0Hm2AWH3sVPleb9ZNkOK8DtvFnrDPSIS5jtT6f5PUPtji0%2BfklEL716It9eXuFgZMUNuujP3Ljy0sMs3YomgBKdWopPwsrjTaF%2Fk9ZcRBMwvZWHcf&X-Amz-Signature=4c4faf10094d4746fd3a4011cb1a204555f85a6f2850f565f357d805c14306f6&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPRQIZ2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHn3O8GG0zqvgJb1RMtfJufaEUDDO236l4lqDHgBCWNEAiEAvfr8DqXzdFqxnMsWUjE1LjX0oohXQ5hkUKkyUux2w3AqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2B3PFPgfDtvmJhi%2BircA%2BR8jcIihZL350UFuFDBlB4VOyLB4AfGvdZN8T7zdKcKwSwu0N4IBgboPEL1shpBxcvw6eOKdPix8zTuaIOHc1ZF1%2Ba46dJ21oPu2gbdKl67jW246eqXFA6QettA7E6syMcZWRY4XlqnfRgXyulI9WsFd3zPaY2BUlfI%2FVA3sAmY%2FUB0g9hYYJJ5%2F27HyP38k0Gz0hiDPnb28DRJNEGdt3Vu%2FRdRuvmCovW2RSIa45NA4h3sSLt9KpQEcfCRTMWSh6toLHt7hlyxAVsJ0xEwbFEJI3eguCZ6BL0%2FhKeEu4NTbqDzDzfc3toWUknDbj%2BwA7%2Fhk3ByOdRye47%2FaYhzDlEUsUthIC7n3d2tjQ0YiqjYfOsEpAltHilSzJ3CxHL%2BlJnxSiW%2FetEjE55yltyyFByov5zOO3zx9hfuj0t%2BKDUO0AStqWI6ELQFxkc75etMr5K4NCMYPomscGRp7nZWIVSSjyfql9OVobbDmg%2FjPfEPNbEb2aOg2YyeZcTxHEDfZWDCi%2FUxVFF%2Fs7pYesO9RD1v6ZlyNRwvxwhdHGVK2JrWlkPO98M51SqG7OaM%2F26XuvYnHyG3s2dBpCgOoAvbwy%2BzdPfHaNRi0Rebw5mgZSlVp9VWsC6SCSjGoObQMNDd%2FrwGOqUBem%2FzdNQ0VmgKKf6etnth%2FVRiBAfd3orBBv6ybGOfgjzkCNHczeIw%2FEH%2BXnvb%2FB9ql6H51gU37jMuWw%2F0lLUAsszK%2B5xtuAXOqODrFppHM0zYMzPSsulBPKqYg5G%2BmppBLC%2FMU%2Bgjx1xBGoueExoY0D1ZPs5gHbwq%2BaY%2FXvocA7pEmgCDkD2vUNdeBEzSMKAe8OOY%2Bd1D%2B8ZOomJLaMZr5oq31W0h&X-Amz-Signature=6bdb727b409bd2a1c58039b5248bc9c56dfec13873897479e3b4f307755c4666&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNIFMCGL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3opOj8dfnUcOhnURGAEHoJAAEIZOEWfhZvfAraZAQjQIgbJ%2F40%2Bs1aViupfb8KROPyXSIbVUF3Jgy6Ie15WcqDoEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNwuE7c%2FDFnY4tC7vyrcAwEo%2BtXjvZ8dWnbWa5x9dhAKsCdbLSfzZilb%2FLmgT951Bbm4JJzZDh6%2FoO2vmDJ%2Fs7lvyCSA0uyAaXrL7unRGhMgyNECSqOKiZacYxjZ%2BxVBlRivZUN6BLa3cy%2Fm1NEAoB%2FMCYBjadOby8NAWdIQVzWLfLa%2FdGmhDdHXXYz26A3Gvu%2BBDHyQ%2FsQJWn5ioiW73BnGZieFFtAnW4OsAXBjdM6GTg8UH%2BgwhgxhlY6w%2Ba%2F5TOLTQs0%2FXZW5uKrQCeuBNQIdvXebsUSX9SsWTIjSvaB9bHzniz34gc4omNe0ENAQaFwzHwPzCenx2pFWubztHzzZrn8J3XvRxA0T9Hor6MZNOwR1tz4JJ7V1oM8NasexeT0qCG%2Bj5Y1s5LYemGaEcVmN9ccIPUFOGz%2BzghN8LMmU0p05J%2FK1xlHfEXOxQmMjtkZ3RCF49uoGpN8J4y8yqIKl14TaSGFnqc16jNGei8kIqZec7G9tVDllyk1iy4kRlMHVFqXq8J5W6DdeW7tagews8Ad0%2BohN447wygRVW8laI9WanWg8LNUbedIVRbPb7yz5xkxGZilCtT%2FRrwAPtJIoYRuLBTJgmNZXxHwMVDNOH7O%2BrP6PWY8A6uuGBgAnOmxhXcc64UAGKAPXMKLj%2FrwGOqUBeHDt17r9L4KZZ%2BuU4eNXpKuoN4pF6bKVBriAPYI06R6EipN0bhhfJtkeNoNV2Ptca1GqG8OWLZEZl%2BC3VxPvsYI%2BLw0vtmjhKnMdKSsqRkpkyeEskDjg83C%2Fx%2Fh6IJokokEM1GnAKbZgsWd9CKS60k9KDizkWF9SopqujAbcYC4NsaAnyGb05jduDYhkpWYxHhSXvNqdsDl7aTP6XAEW1HOVn6WI&X-Amz-Signature=7c5df5f5533a5ac0b6e25d96ec2d30960eff400fce76f728a359c017e4a44926&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJI7SX4O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBJ5EWtuF2L459PjXCR5jg9L7yvv6irkXEaRbldTt951AiEA%2BcJ2jv7kiMBcSxVKQkbX5j8tKz1qgQzktSnoVeXI2bMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsuqUhYshAKXG3B8CrcAye8HzvC6pAtBVDI%2FgD1TL1LAZT7wHUKRdhzlgkurd%2FKbSup5NtgbTIN3gQWSY%2BFrcCifeD49I33UKhsRmk8rowrM1VqyPTpH9GZmXLj06cvEs9FcefygJbPq58stbpGTy5KKpt53yvq60o%2BMYCU9NBynI48Ef8vb%2BxZo6BZle9OsONy01cv6HxmSrTmsbCMcmEcbBdHcIP7m8DOezWKh0LF5gwn%2BOcYCrqB5bPjO6XJCZBJ4gpq%2FACYpAfZ7WFgER%2BkhGMlMPdIf4P9oXoGCBVeFxknWnkxTkO4UlbytNt1ob1bqY%2FCmOJu9jGABHrGEks%2FQAkvtbFVQE5y0jc85ZjR5JemhxSgK9EUwcfXrcob2un2XBjMJ4AKQ9nybzEqcrcymrc0iZ2MEOJ4KtN7aQuFlbGsThnY7TkMXas%2FHPKAdewqwty6%2BJyZbzHLpuNrSU2DcAI3xMf2rNyLrZsTT9J0jmGTehNbZSJWChyka28SWw7tZCdjsY42xoBeDMc6mN60950eGDJhHaM1h%2FgrTJUdNhfv02HDARY%2FWXUQ2hZZMry%2FeHUl6%2FS90b%2F3Bh9tP%2FyBxLdkmXHwzSZue93KGY2ikf3DaMuBJtk%2BLXR9B5S8UZ4oUeeN7q9xc%2BIlMLTf%2FrwGOqUBJZDNmV3opZdumOsg4V3s8tzPAAZzBnnR7Ny1pIZUpm3hukS700z8T5bvkcl%2B6d%2F%2B8Qc08V14%2Bht6vSLZ8FwrRtg6NApBv4vYvfViAlxdF0CmF2wDatR%2BkWDceFgxWIxdGte%2F%2BeDZVpOhd4sgzKRp0GCL37vMCBFUXrhiC5L4%2BSpIRKR1VPmnI%2Bx%2BbcFUkGnS1rf%2BwTQVYChcpmImWfhiT7Fc6Aft&X-Amz-Signature=c5679caaed081e741a573e6929fcd8a76e593de2bf20085e2cd5a966b08b1dc2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662COO5EG5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICroRmGFOXmnaPaLjFuyNo8nHQ3fFGkiJl%2FnymYew1iZAiAY1GOBqEVDPdxJ5Te6Enl4PD9OU7O3ho8Xk21qM7JYUyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPLPyrc4g%2FFHCOn%2FtKtwD5iaxto2GErk0dIgFD0A%2BapAtdttfa0Han2LXr91nOnvvar6I1bVK98%2B23%2B%2BxquR3xQF4ikdkkZ3mi%2BkOE3mqfpqxHmS2UKKQ2SQOx6JvPGX7kkjFudi0qBJzbPdhFSBMNR9%2FVqW9yMVr%2Fx9X%2B8N1GdIBiPECK3frzk78awVgn2mXgtYnMSK9o%2BmKmvfvZu2wb0im5TJg%2FKSJiehbZBQ0qYjDcE6RcC9cmcehXi1TSgh97Q1Fz6QhesV2wvqOAU2ea%2BYEhMx94Rks4iXEsBAuhy%2F3eBocMkteKs1NoAQQlbrL35Ie03XTpz6%2FccXN%2BhmoP5mUEPabJgCRHbYjxh5WyE09pTBWgadMfucz78k4kpmEHxMnA3%2Beo4EBfU9jgqbbgBwAsY0ogQb4P03hVb9BAtYR6SBm4PW2owWrNnLAsGq5%2BFZ8GfTsLiainN9gWfBt%2BENppDiE8%2F7P6%2Budm%2F3HslIbhJssODgh3lemLgJoSECUr%2FTEZbwhuh3K7Auo2ICZGawO%2FPiDQgQMlUoq2R5lNY1e%2Fqac6NbE6SpJdbAjL1omJS%2BzVflLPpP5PvT%2Bn7sN8B4a%2FTlN4LQaOnd3dd%2BEk34AIPkeArxYJqfNaZz1aRB4IX8hij3ssGzCZBEwnuL%2BvAY6pgHFTNcQVa3BtYgbLkXGndE7Z8UYZVdt8KkQ5MLsrNfXiQphPnzUI4D1JWebwVrKoCETIMAjMWSJNyl3p7hTNAXUikBTPQ3Ss2imAebWi%2FyAyJ5kIntTBKaN9cWMRiZvKxaCap0%2FRSRtsD0Kmbv3uvvXN%2FEeRpg6cZcom9PT%2FNkmD8tRWTDhT0rx2f56hu%2B%2FkX8TJs5FKqMLFfWuaDXL2Ou8d0VOoTkm&X-Amz-Signature=5c15243256de36edcf8f9312dbd51f05d729472fb3f882425f10f6721224e178&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662COO5EG5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICroRmGFOXmnaPaLjFuyNo8nHQ3fFGkiJl%2FnymYew1iZAiAY1GOBqEVDPdxJ5Te6Enl4PD9OU7O3ho8Xk21qM7JYUyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPLPyrc4g%2FFHCOn%2FtKtwD5iaxto2GErk0dIgFD0A%2BapAtdttfa0Han2LXr91nOnvvar6I1bVK98%2B23%2B%2BxquR3xQF4ikdkkZ3mi%2BkOE3mqfpqxHmS2UKKQ2SQOx6JvPGX7kkjFudi0qBJzbPdhFSBMNR9%2FVqW9yMVr%2Fx9X%2B8N1GdIBiPECK3frzk78awVgn2mXgtYnMSK9o%2BmKmvfvZu2wb0im5TJg%2FKSJiehbZBQ0qYjDcE6RcC9cmcehXi1TSgh97Q1Fz6QhesV2wvqOAU2ea%2BYEhMx94Rks4iXEsBAuhy%2F3eBocMkteKs1NoAQQlbrL35Ie03XTpz6%2FccXN%2BhmoP5mUEPabJgCRHbYjxh5WyE09pTBWgadMfucz78k4kpmEHxMnA3%2Beo4EBfU9jgqbbgBwAsY0ogQb4P03hVb9BAtYR6SBm4PW2owWrNnLAsGq5%2BFZ8GfTsLiainN9gWfBt%2BENppDiE8%2F7P6%2Budm%2F3HslIbhJssODgh3lemLgJoSECUr%2FTEZbwhuh3K7Auo2ICZGawO%2FPiDQgQMlUoq2R5lNY1e%2Fqac6NbE6SpJdbAjL1omJS%2BzVflLPpP5PvT%2Bn7sN8B4a%2FTlN4LQaOnd3dd%2BEk34AIPkeArxYJqfNaZz1aRB4IX8hij3ssGzCZBEwnuL%2BvAY6pgHFTNcQVa3BtYgbLkXGndE7Z8UYZVdt8KkQ5MLsrNfXiQphPnzUI4D1JWebwVrKoCETIMAjMWSJNyl3p7hTNAXUikBTPQ3Ss2imAebWi%2FyAyJ5kIntTBKaN9cWMRiZvKxaCap0%2FRSRtsD0Kmbv3uvvXN%2FEeRpg6cZcom9PT%2FNkmD8tRWTDhT0rx2f56hu%2B%2FkX8TJs5FKqMLFfWuaDXL2Ou8d0VOoTkm&X-Amz-Signature=934bad847d2793d21a734a75ddbcd75ece8ac6c0d2fae6ae76876934ffa099af&X-Amz-SignedHeaders=host&x-id=GetObject)
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