

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPY6K2JT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHv9Ak9Td6vR%2F1hMIni3whAS9pEG%2FefVNbHJubImqB8gIgadkmS%2FioaZld8CrQD7zG1fBEzmpoG1kggDavN9BpYMAqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYfXMqFXm9uPoGy3CrcA4SaTTmWJyKwBnMsgA4CUG0a3U%2BH5GHgKUbLgO6CUiTYPsOBuyWD3TulXdLmvsW40KHwvTWO0q6Wnewi3lE4HiUZ1MUoxr634k1PVsevf7yFWDjDm6ilLekFJhM5Mmzac23h6gaOVKJyMsoCmfoU2M2jPaHHsiwM0LMCJWyrmBvOc6klfdGifl5GR8Ge8fcFWkd%2FzEJhWxQeyn%2BE3ZudqA1VTpYruauYkmjE2UCCxm6DF4WeXqGt6fzHjzLxAL8spRfH96hw9QmpfobyxYgkMUM5V%2BIBRVQPaqsb%2F%2F2OWI8bfhSW09UZcnlsLjvi2p94ITpWHE88IJ0QmtnKtzqxwijWFAPSNaov0lTp%2FPtUTfdH8nWHCfGGBWsyWwfDMUKiMrL7uWmNEfVuCOQPKyizn299IOhUEPtPay8Ie1utbWTjOw%2BLNkntsK5ZaDTnxg7mN14QQC0osITPZUffzaML%2FP41Ql2UMWdhlVhPvtlGpqH1ovedRs6DMkebYZiNnEhKBomOpR2LOCyn7V3ywkSqUjWdt%2FRcfncllbGCsGoh2o0fMYAt7vgTxifYwF%2Fu20Pl03IrthU1YoQYUwKJVG1pWjvijF%2FR68%2F781TmxXCW8zhPE4WNXKRm7n5c4yOWMLnR8LwGOqUBwZZVbLs5z5K4gazNq05YgnAtZiHkfSqJmQNNCplNRjtDKR%2ByN0v2vbOKC7JzKJBF9C%2FtGRBzMiLbN9oRbgEBg1jARrMxqoOXJ8Q6uWsYCu%2FCEPfVN5AEi%2BY8YlGImW117ORTKlt4wCDYVKxWHhbcJ6VjX4FAwQ%2FARci4roak9OdfkljAyg9Fd%2BMWKueNumCJwkm7JmYsznhkhtuSC3n%2BiMga9Dhy&X-Amz-Signature=f604965c946f81bad9095210a1c8cb5b243dd5823011d86d04015ff4171bc5a5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KMEIOKJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9N%2BxxuMDPELSRA7k%2BTfwPn3LIzdvSPOZJRz%2BAqH0JAAiEA8vLxed3qgZBx9h8VC824U8qwv8phjbXgR%2BVMmz1UXKoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEVZTpKAwAqIFQnf9yrcA%2F3UKIxPlCMYZWOiHlq5LbNMVeJDqaguaUyl5so1a7jsMVhHFozxRCtBFeEU27G9daeWWw8VR0wrK%2FvYRcj%2Fa2K7zhMVXkF1li7HCgPvudTdtrV4Gz7HZUkwg101saVnIwJVQPFSXbvRFdhS%2FMtyjLrX1Zb5nmZc5LSWPLEs8R1MBqw5HHmWcJvVLuZ2qRkkwf3xnMsGf2Fcz23EXkfs1es1A178i3kzN3BaR6hIZkCwUUB1nLkVoTllDMyc4UxLteI93i87h3BvVZ%2BRd%2Fism2n0JnJV%2FhS3Wd1%2FJ%2BqSvcM7szA8FYKSQs2CQSSFHA4PtRT1WbHm2aiXAV%2FRBOX5rONKa69ZLSlXR5RVqFpa004YJ30uBcOcDNAbge%2BTBnHWJQguo0UND9mWv%2BhpN%2BI81iZ5OLLCztb6UimiVL%2FsmFysTeDP3N%2BAdDW8a9%2BohlofbIJjT3NxooNtPpTag5i27OruzqkXdQ8pwcptxfVd0OWJeMTLyYkoAO3wHQnWbHB256z2W%2FE0wQ5OH1%2FMgFZX6ZNOSP8NV%2FdnUCXTvPXhBqHhmkkcV16%2BE0IBb8M5S7MXu6IPH7SfSfsjNDxLIUE5Rv5y0aovfNHaDwC9F9P08dmJONMS%2FGwwoUD6FUFwMJHQ8LwGOqUBagceOcyn4CITMI08El7eLZwqkLlC4gKcB96Di%2B4LubMniLnq3D8O4OBzOpMBjG%2B8Niy38qbCmLvi5PrapKKVLnYoj5XF6IXcIk53DidTobWyuQfJDMWXGKeITPgeHUqFWgbF%2BAjk%2BPA0ZEpUOwXAdWYJizJvJ4r2RPmgOJkJS9e8WNuHcq7cU%2BSz7A2Jsk3rg3Vt3StCVWMEza0%2BzNy7knzFhkai&X-Amz-Signature=3030857a4cdfcdb87ca5e6d8bf9fedbcee5ddc5a560b3bb5384ada51de24fbe1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHWOXHY2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5Yxzxx8ahmUZt8xlHCBTpxMxpHWJmZaGDeQ%2F1HrCq5gIhAMWuuWSLMG7j6DHSvMFwH02BVf4DwFyy%2FeSyqRRgb9WCKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4OndV795geaJmr04q3AM5NF95rUbbBmw4TbbLfbNtDdV9fHVp6ULU7%2FcJiyJq2QIenale8nx1lcVxwp2Dy70bXF6xVO58bNQuMR5Ahx8%2B5nKwzd9bn2J8%2B%2FvYoPGi8p9ZPjdBEN9DbcYo75q5UZMohcEQzPxpoWQP%2BCcYrB9SV5%2F6jjOBiKGFeYCrne5KITfPXnFbneKrSBiGlKejHQJ7p9u3xQ0GEDYPyfHjPDz0vthlyv2lJZtAfpBmmwU7jKEnrBqj%2Ffhg8Zt8YOPGp1Rz9q812vqzwAVYUojPglIMAbbYS8Nb1lT7pDvEcxVHYzZvxZz3WwEysTJjsxxtXExhNCYatRPFQlZ0lFBLlx%2FD%2FryvdPtznLENEzRqBBa7nQvQiDRsF94Yea1YQ6Y54LHcUF44dMhIXzXqK8UtUpggBEqvCvyUGtOh5%2F33GDDgmGK%2FJOGWYOWG53YremfeTyGgJwxdxZsf%2FU8cncjvCrA2nEkN%2B3pWMN7xTEHY3ZfpH5xah2tJ8sT4XAR%2Fr42CK9vlc63vKh%2FhZ7WSLtwHEOsn3CKFWHZ8DwpH3RQx7HH3NvghpvjvElh56zg5zqHKDyai6%2FE7f8ZIVxZuN0XJ%2FWHf8cae1VyTbOMccwTho7CEFgQSGlWly4bqj1cLETDV0PC8BjqkAaaGtSosSFVYpCfQolo8we4xl1oUjhJ3g7lCHdc%2F0OD45UtpOozd2hSeBlDRVwT%2BX%2BnKptyq9Mulw8mp974MjZNcZsCrUiSX4mQNdfe8XhjVwF8C%2FgUcqUM99Jxg72sZ5EZ5rp4gvSqGAAN%2B4%2BC8xRP8v7eLl%2B22dAJQ4%2BdtfrVU7r0W5hIq4uWKFSzpO8O7NglZSBapEvuCMPIbx8cWA2El5jPv&X-Amz-Signature=c73ccea28ad3488b6bad73b7228a258d4602188fce22e05aff7d06bc1decb4e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFWBLVHE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BIVF6xIgeIpuLTtYXNT1L%2FguA1VofxPtEGXp%2BFr%2BjmAiEAtXlB9sTAZKPiIS56Tb2Rlh3riAIjvNbW%2FTTHJ%2B0i%2FNYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7raSclk0LeSbeNQircA%2FEP8S45DTYR%2FSjFYU%2Bb2u4%2FajonHlFbE3731UJOek0InwrlPMkj2aXGkcGmCOmR5JeC%2BuVdnq22LARUXXqaEt1%2F0DBRMCDl1vqFmlQQaERrGRb01sDWTIibnLB%2B6VKgsnznIlLXa35Gdmk8LPNDp6ARq%2BvP52yjORSQB21pjudSKQULjBKdPNS0kTSwc5Np7ifgDtGU9hwqW6FqWkVESMTsgAXEPAiqhkjxA5lnzdaRbn%2BcjKunxk4hCZwD7VqUsY%2FRdOToXjARUCvq7CnXvpNkyCxdNwS%2BG8SQpbLJTh%2Fpfu4wC7p9jIhLDlPX%2Ft5O01vKlrBu7opaGYOe1wGr%2FqmzvlylKC5liQHn3pWRbU1KfyEO5gaW0LkrPGZmot17TLWdcIQ2Wp8MUPBZZGp5DnEjg9DvF1Sh5jRhRrXKA5SLQPlQdRDBOfzmg4GAm4ruSEeTAVY8ReaT0vetgT%2BtOQnCZSP4OZirxJx%2B9568KYNOF3l5xyt6Q62uwrsUzDiOeI4eXIHS3Tieb7UtxXH%2BtHtsvolpmMb4bqS2u0zrHb%2BXZUQmnG0zprXSnw2laXrfMFwZSHTFkpT5weLi02fGtjdb5nfpiY1mSdd4EiFpNgACW6jUkNkeo3ZFqlWRMIbQ8LwGOqUBWyqu1G0JKVonVT9tFNvwiL5Ya8%2BIl%2BslT5JW3c1V7bfifaQeD2cCSZi%2BbUk2RMecgggcZs5xXRIYD3FTe80cinC6MYzRGU86UKmsFwZ6QRnUkW1AJHXfQPaBupSNBiGnn8JvYFhHtM9PaxSEDUPSbx7dFWG9KKjJqP2G6fFHPb1un8z2EEqpK3Z%2FAvMWqIFyIFCIHY2znO6ll4yOuajlLu7LTtHT&X-Amz-Signature=b67b2e2b5d3a0ef9ea7b1334d026ec260faf51699c374c5513b4c34df7943bda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUCHBH5Q%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGv2c%2BR7jDqVOZpelSLods%2FEwCxzJFV2Y7fsC7a91V9SAiAM6LzsKKsOc7NY80wdxVV4P1eNznqgGeVQ%2FUvt5sOWcCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Bq87ljjkqcA%2BfyBkKtwD1pijnworkY3Q%2BdQtqEXEwMOdxoe6YWlMoFNtg4GBgtn6EM9iTuiTsA45YOKOirbnPHXq7fb%2FaExP8U8vAisEd8Um395vNu2K4cEMovaxZquQzTZ6mnZy7tB%2FOrvg5a09IdmiofJY1LdqLDDXEmYuNm7HxjSSUU%2BNs52DB2xqRcTq%2BRtUEZru6vsmtI9DdRYnpGv6R%2Bj9qOHGTL%2Fl9C6115lSt4mLB%2BgTVILlZnz2YvLNKZSqIK52X29ubOC10FdbkP1NvKkGiEoPgdfOiZqVeeeOSY8UbYb%2BUWUdO1zn7hmm1CUNYsJrMcwio2Zbf6Q9DgJRWm8tt6ya5nXxHtxuf8Py%2BIJcHFLUhdatLarvDKPcpa%2Ff1lzxeyd%2FtljACetzlnxRL8f177RMOBtM6bYqyUyE1fSMRRxww56uOY8h7eluonFHjdoRiifr6hv4HTN3EUOwGmT5IfzOC172BG2EzTAt6STXgFQOVLVCneO2pY92uRFxuEKAxOcsk8DtjA4dWi4LylhP70OClD0RAHAWu5qmkm2BLJQRdjq4dLKdV%2BnbeEi1q6dIhO5%2FANvzU7lg63UFu5WwL1djqzg3rqUmWyXkXP%2BCsEcHtE3GEkWYlx7dzX0VFitBr8hMkyEw4NDwvAY6pgHOS0qCjstJRt5DsupAC%2FN9l6RJkgKFrmlQEz7RCZvQJcYNAhYdPTjq7N2LTf4bqnAnZJsH3RNR%2FzPLcggOuYXpAKqZ1WboleopZSwetkXRmGr5IFLranfJvGLAClAhoBI7DfOWg07vpnV4DhHQ8XCGqSAzRBI2%2BJF5XDceh1%2F1yRtIwIuEOQFmAR2Mslvhfk5wdHWdcTJDstbloHCPpfUdUS6z5sUw&X-Amz-Signature=1a01ba085a037e0a07862576108539c027983f4789f1e36c44ecbcc8b122d603&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4Y3XFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3HzS0z8ctX%2Fh%2FIQ4tCKpJalgrcta89MHiy2LY0eqJgIhAPX3PcpqXSaKLp1Y8hJApqQbJh5PQGttAn5SoBFxEotBKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuuxU3PmAZJ0g4tuwq3APPq0tvIcgtrhAWuHSIMb5EkvifhyjbFyDyh%2BugU96C3cStU8MExSIrl0PTDr4lRLl7S0wMD%2FAwTj2w2IqHVK6TnBUqZHxHygS9uZ5idvylqgKg3ygldVgEECJYTcLw8YNUOr17XHn4Pw1XX%2FCKF%2FxwUgsx1eKwGKVrc9xJ%2BoM%2FL0iz2jyqaxL3%2F7tlyJcaf%2BIg7l6VgFstwlJI8h6x4uhHzqW77xLKd%2FwL60Honys68fHwt7MeWFFJ8UL%2B%2FDP7%2B6zelPY4bvgM3lt0yzITziqp8n1sqllv%2BmuA0yxU73d7CyRxwmdLYuYFSPqemsxG1GS2mI78DLoSz0vBtXAQYnLnQodhWVKYb7xBzK07yXEB5ZE8hx7KqPNRbQ9qnui%2BQPvikLio82k1xUdiBET0kz6%2FrWXsPx7aeK%2BzBB2vo4ME3hh4fkMLXuFauqSgBGGHWHN%2B0btke656jGK0aFCD3GQKHEwPVSGkt01kGq7e6D0pTwSGoLFeS9ZAJvSqhlIgtj%2BBW0lWQvRhozlas31x8baPkxnRQOziAZYjQ65I2RFanurfeks7AXtBTJB75ddpG7VWE%2B8aKm1%2FJshj5SB9Mwo3rOWg%2FcBN5Abpx%2Fmrn9GTj3RFbvQ59NFpfIxmYTCu0PC8BjqkAYu1aYRddGFBFvKIl%2Fid80VFcPvWFibCDTNzp%2BsDy5Ox53mcGBzazkbfMv4gg%2B1KRUtMrdSAjqfeTh5ljCYuTL7hc4Xmp%2BgSpcayylvz3LUMzi4q3IqGgDjnlvma1X17WnKGvtAiDQ0c1atzy%2Fq6EFWROodE03Qx9MoMhe487xK%2BEHzC%2FT2hDY9D3IOX6EXrhoJ7es1MNUwRpJQgfM7HJuLHxDJP&X-Amz-Signature=cdb38168b3a5ce4f00b00eec5dcdd58039eac4cbd70cb61b1e5646c1b3adc25e&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WY4KILQP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEv9TU8L8olDtEmbhaPjsF%2BjOSHoFUNvh%2BV2wY9nLzayAiEAlSmLliPbCA8QVUJxNlTq%2Fc0SkZy%2FnQpSlz4xPuGaE7UqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2BUM4A5Lk9LYOlBiircA8n2OkJaEI5mBOXZkgyspSjobv%2FJmtqhj21rAy3z6cZGAXXL1UspSrh9W4LHTxNCqjwI56zNnlqZiXh7%2BWdcmZ0OnN0bik4Z66Al7vO6nnfloyJ7w4lqLuFXq9cyWPkv%2FdiFx%2Bf7qbNolhFWepfN8u7%2B4mrFNNRQS8ZPHYA6Y0Q9UsAAIama7Gl7UtfYtD3I2tXxj96geZMY9h8Zw5tF2ezSPaA68SR5jOsUjiFWamRwb7P9MpSU%2BIfJPbIdVu9S0yWRxZn8wRqcp6T7ZbVnVcrJeFEiAX22KM2bDCrvOVxsr4qSdw76x5f%2B0u1UEowyNveI65GAfDKPSFIXiRD3HoJc3WBEOYWZNl2sPoc7c2gbKXJiQ8WSzozGsdwmHno3nB24pCVe7gv6oAphNgqu2oC2V%2FA6sAO%2Bs%2BCMW5hueG30r%2BCBBOD6v6Sgf28alCwaq6kfSaB4uByHMWJ8%2BIUKOrZEXPo%2BXYcYIepjVtNjIQk3h48Br6X7ky9xWvQK67BQ7grJIxq2hdKS%2B%2BX88emPBdSTz5mFx29dTVoZ7T0Qsz4E%2BGzQl8CcFUcj9n6SLm2xcVHOsDlKSZYDLnGuB8a6eNC9xYECybSIZepxXKXGM96G1Wh20Qq%2F838vEjNbMNLQ8LwGOqUBym2xL5qdaeLzXmLrwq4kfTq1pLm3dPT8%2FQOvea9nhc2nA6bZ%2B%2F5VQ71uhpPfuw5U1a7CpsrNnfzvR4x8GMLhrqMkyaeRc5K1DCgx9KA%2FgVobOuj6uOMwWnc%2BzaKYSWR%2BjDtMdFKVq0%2BBjxwoKdlaw198wZfnIvfXbxuRsOlJibwhp9krTZecHwEhGBIuo35MSE%2ByW1Fefs%2FnZgvxVMpyttFiMGUm&X-Amz-Signature=592c0e3ff86d7ac0442640f6358bdca8312b3d8b103100608f345d948e8af966&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KTPOOVC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpwa8%2BcG6RMK5sCj28z10HGehkXcACrJEAQ4Yb%2FHtgrAiB9etFGwI%2BuLE0YVu%2Bmpjd1KvMQTt%2FlgGnYxdpPAKu%2BXSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXt33Iv5XHQ21lsqhKtwDbkfJBM2OEQ8advdgfZkjj2fuHOe4jmsJybdpH4TBid2ugH3biRLIo89qZDDF7mywXyw4%2BZoD8TRKounebPzMB1qDPmv84y5i19ha6sivnRRtOT5qfSRQUVjWYqZ0EtP0OodJLEmTzm7dhKDCnQXHZph7PENeRpWCD%2FYqJEqhU3V6fn52Y917tprhorJyVoEue48AobLS%2FOGeRwjSklb8IM%2BsNRpa0zEyoEMDuu0VoE21A%2BX0%2Fb5g5IuVJi5R1Bh9G%2Flm9m6ME1a%2F2ik77Yz65sLgFN7J45xiJ9lCO89%2BxbFB%2BDYir%2FMquXEilQeA3z4EPyFzomGvqryzLQA7z6OSDXkgGCKWatNM%2BLy9ij6iBSSwValIWyA1twdpxar82JtfyQFLxpIK8RSNnIRl3f5Cqxe7CJqgI4yNTpBFdPQelSEpDMB%2BjBT%2B6V4aDlJPDZPPC434%2Fez1INHESqhbdQAi51iDPoaO459e0A1ox%2FyXGpQsx0czb%2FcCIjAtOelnoBMpR3Z6sW3y7vD89jD%2FlMc7fNFfg3LO3PJsGbxBIIgX3Dpr7IbMbyD0F23msUfiJ0w8Y7HVjffx3Eu788PlWW9Hu7U5t27ct1k5aMQhdwS2vqDqSikcvoDk4CDrck4w5NDwvAY6pgHsmhTVzr9rIAC6EeW2%2B3xcKqm5e0onseYZHHlgQnX4aBI6OCSJPJifz7rJkmEv01%2Fygz8qP38az%2Br%2B3ytod1objEzIrbn2ujPz3JqsFH8GbCO5HzrFNrDTF88lmjn1oFQOsSOzaqIVhlwGPMlSuz1x4BZr%2FTSIhI9BskjSu5%2FVG8JkvhV4VqaJYiDstXiwN87o3v6M9vls6k2C9Yc9dgots5JrHAbC&X-Amz-Signature=c73b97b52669d79ef706994cc1a9062c5bf570cbc9c160febd485ec80424db84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUCHBH5Q%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGv2c%2BR7jDqVOZpelSLods%2FEwCxzJFV2Y7fsC7a91V9SAiAM6LzsKKsOc7NY80wdxVV4P1eNznqgGeVQ%2FUvt5sOWcCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Bq87ljjkqcA%2BfyBkKtwD1pijnworkY3Q%2BdQtqEXEwMOdxoe6YWlMoFNtg4GBgtn6EM9iTuiTsA45YOKOirbnPHXq7fb%2FaExP8U8vAisEd8Um395vNu2K4cEMovaxZquQzTZ6mnZy7tB%2FOrvg5a09IdmiofJY1LdqLDDXEmYuNm7HxjSSUU%2BNs52DB2xqRcTq%2BRtUEZru6vsmtI9DdRYnpGv6R%2Bj9qOHGTL%2Fl9C6115lSt4mLB%2BgTVILlZnz2YvLNKZSqIK52X29ubOC10FdbkP1NvKkGiEoPgdfOiZqVeeeOSY8UbYb%2BUWUdO1zn7hmm1CUNYsJrMcwio2Zbf6Q9DgJRWm8tt6ya5nXxHtxuf8Py%2BIJcHFLUhdatLarvDKPcpa%2Ff1lzxeyd%2FtljACetzlnxRL8f177RMOBtM6bYqyUyE1fSMRRxww56uOY8h7eluonFHjdoRiifr6hv4HTN3EUOwGmT5IfzOC172BG2EzTAt6STXgFQOVLVCneO2pY92uRFxuEKAxOcsk8DtjA4dWi4LylhP70OClD0RAHAWu5qmkm2BLJQRdjq4dLKdV%2BnbeEi1q6dIhO5%2FANvzU7lg63UFu5WwL1djqzg3rqUmWyXkXP%2BCsEcHtE3GEkWYlx7dzX0VFitBr8hMkyEw4NDwvAY6pgHOS0qCjstJRt5DsupAC%2FN9l6RJkgKFrmlQEz7RCZvQJcYNAhYdPTjq7N2LTf4bqnAnZJsH3RNR%2FzPLcggOuYXpAKqZ1WboleopZSwetkXRmGr5IFLranfJvGLAClAhoBI7DfOWg07vpnV4DhHQ8XCGqSAzRBI2%2BJF5XDceh1%2F1yRtIwIuEOQFmAR2Mslvhfk5wdHWdcTJDstbloHCPpfUdUS6z5sUw&X-Amz-Signature=36222ae794b5310fbeaf6ef99d341c810148c6552ef6e193db399c02c62d9b5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BZURZ4T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBRIbpKi6zPNlPAQ7vQ7GVb0tXT%2BWQu%2Ft6RhTapgfpwjAiEAxiy8PRp4mt3eUuewdCFgSl9lZwRxBFySCoJuy6vqqvsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHMHMmIxRnb83wdhjircA86BwTUgqmTeppO03A5pxmXjCMVOm9KUVm6r5faDh63UoAAJE6RCSOcz9glClBTQLo3G8ytfFsYbXDI6ryOI55tvvU1n%2FjXEEWIv4B%2BosGBUjkzFcmZWYf%2Fc7%2FK6UTXz8zpDjaVZe4ACG%2ByiWUp6nu2N8YCLycK8G4H9XMVekpMW%2F4iK4xmxIfCj%2BfD%2BwM9nr0m94JGxePoXt6qx4GQytzHD1zfiLCeMYK4RRXcoDEicH11%2BHtEd7ycur3gVLtZZ2vZgdMYrAmF1D2q%2BSsVNqeVs3c5uVDTbSQC7Vc2KXw%2FBxRhaun8HpA%2BCFWQ8ZFgf8yc%2BqUxaklboqkAD2L%2FvBF2QnHVLPkooYYiKwwG8W4Flt9kzGerY%2Bq0IN1K0zXL%2F254ddxxjKLMqMvkgBwotLIWt2%2BT0SxmLjXHVRLRmnfK9IlOPP%2Fkg2dFqNMjk%2Bfyug2XWdLLRaZntsy0EPxp%2Fb1%2BypQqX18zHAEe6biR9VJwC7cWsHxJXAtv8BS2Qx8TbGME79Qc%2B1io9z1qc34Eho3aP8wUzn6yhsxM8FmRyYYEppBR%2Fpihce7sBRqI6evmgPuO2nWa6fYwNCWoUHuo9Ge33AsV7QM37m2XGQRnuHbDNwyXxrK5pfN5KX1KgMJHQ8LwGOqUBNTsR1gs81vVDNiZwI6suDELluaMFxGKePGRJ1%2B%2Bu9gmgZvSZa2BpH6BcKzluW2KAQW7wxudoLyf5C2DOBiUH417KYlRlpRPmdL0Wg2ONUkKYCtnfmmYxxwSkVQr1i4ZTaK8kLFsXXNlWK6lcyacuJDStCW6Fx0yRFdEb8hzZ9aU0QQX9AFzBsYbAkWa0VN9vbqVcvBOW4AnIe0nrnpVbV%2F7jnyr2&X-Amz-Signature=67d17fecd2a2c96daea7392b4df05a1c19b8ba5cceac828efc09dfc47ca80446&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BZURZ4T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBRIbpKi6zPNlPAQ7vQ7GVb0tXT%2BWQu%2Ft6RhTapgfpwjAiEAxiy8PRp4mt3eUuewdCFgSl9lZwRxBFySCoJuy6vqqvsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHMHMmIxRnb83wdhjircA86BwTUgqmTeppO03A5pxmXjCMVOm9KUVm6r5faDh63UoAAJE6RCSOcz9glClBTQLo3G8ytfFsYbXDI6ryOI55tvvU1n%2FjXEEWIv4B%2BosGBUjkzFcmZWYf%2Fc7%2FK6UTXz8zpDjaVZe4ACG%2ByiWUp6nu2N8YCLycK8G4H9XMVekpMW%2F4iK4xmxIfCj%2BfD%2BwM9nr0m94JGxePoXt6qx4GQytzHD1zfiLCeMYK4RRXcoDEicH11%2BHtEd7ycur3gVLtZZ2vZgdMYrAmF1D2q%2BSsVNqeVs3c5uVDTbSQC7Vc2KXw%2FBxRhaun8HpA%2BCFWQ8ZFgf8yc%2BqUxaklboqkAD2L%2FvBF2QnHVLPkooYYiKwwG8W4Flt9kzGerY%2Bq0IN1K0zXL%2F254ddxxjKLMqMvkgBwotLIWt2%2BT0SxmLjXHVRLRmnfK9IlOPP%2Fkg2dFqNMjk%2Bfyug2XWdLLRaZntsy0EPxp%2Fb1%2BypQqX18zHAEe6biR9VJwC7cWsHxJXAtv8BS2Qx8TbGME79Qc%2B1io9z1qc34Eho3aP8wUzn6yhsxM8FmRyYYEppBR%2Fpihce7sBRqI6evmgPuO2nWa6fYwNCWoUHuo9Ge33AsV7QM37m2XGQRnuHbDNwyXxrK5pfN5KX1KgMJHQ8LwGOqUBNTsR1gs81vVDNiZwI6suDELluaMFxGKePGRJ1%2B%2Bu9gmgZvSZa2BpH6BcKzluW2KAQW7wxudoLyf5C2DOBiUH417KYlRlpRPmdL0Wg2ONUkKYCtnfmmYxxwSkVQr1i4ZTaK8kLFsXXNlWK6lcyacuJDStCW6Fx0yRFdEb8hzZ9aU0QQX9AFzBsYbAkWa0VN9vbqVcvBOW4AnIe0nrnpVbV%2F7jnyr2&X-Amz-Signature=f7def1b9472416b1df948516262d4b533a29c6351b9217cf021a2d136d3c0a98&X-Amz-SignedHeaders=host&x-id=GetObject)
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