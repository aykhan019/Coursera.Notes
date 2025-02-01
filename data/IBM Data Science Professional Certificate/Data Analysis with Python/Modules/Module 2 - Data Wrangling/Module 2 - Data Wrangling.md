

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YCFEJYP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdQkXj%2FFqGgoTbXnkWNO3wbs34Oa%2BaR%2B%2FAjceM5g4NrAIgBv8%2Fq1fnAp3Nz03hnTBLtFFsrR8GZPW%2F0bXLSFRPokYqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2Fe6sssoKhb%2FhsjeircAxsC8l8TA1h6wfzc0MQLCxANrKLy%2F9zLy62kIpZwiZpvRpq0961dkLKSuH6mCY67GgnvyBC1tGSuFtE7zXBDNmO3iKdLt7gXJ4KBaSO%2Bwq48YybQRIE61jmK45uz%2BIoQ1SbHzmBqcQz6ERhQJTdBFwNRBW04mGhH5OdltzRwViEgEXicryQPip4ouvAH8ZOQSgUp55vXOFzb9vvtWLXVEYtuWDoJbszbHQeDwkpjWZmsgdiMwvBWLEcaihcO%2B0zsJ6Ev5jvLoRROs60ASjZht9BpSDUj1ahoi6rvapBGH0Owddnbz67rO%2BX2QJjcz4UpIOVG1Mr3Kho%2FOlSveaTA1idQ9M1Qqaad0QPtmGNhKE7BzfE7DznMAQt46qNA%2F1mx5cB7wTzajDCxfl5jCCwWOCvxExkaXmTUj6Ia%2BheuY%2BH84TIKEejualTIoszW7zisRl55cgcoTWh3HRH3tbZ3HrRO7xxXUX%2FZtZriK3xZ%2FdSTsvPDEGoQeC3UEGv3LPHVm41CRTrm9FtZN3c6p%2FgbM0WUthi3LAxySuXItZJBB9YKgtC44EfiAlJq40OyX1i6X4Gh2I94XSP6evuhEAXt59CqNTniULc2t4OT4K%2FHxz03Ix9twqoJSjGsaPLKMNOk97wGOqUBBV%2BdnTguBEF7LVCuWqv2CcJgCl%2FDzgfKx0M0BcwX%2BhVG%2F7e6opFb%2F8X31r%2FW3A5KhbWT2Vn4iGoQAzt9pu1Sy1%2FRkyGmfYFgulvaenQ7XxLoW0S0WKgoz9XhQg2w%2FGNl8WYLITsvbrMm%2F52KvXtHLFXmwqUbJLH4j8WJ%2Fm5ywco5V5K20QhJ0W3%2BUXEONErTIIGAicCFXWC6%2Fg%2FG23uzW6SMCV0N&X-Amz-Signature=fed9a6ddcc2fde400a1555814b3eefd5be5e3f6180073569ad9f718242c60d75&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STAEV7YD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfX2ooryAExCQg9cMvKJbFWPW0Ca4r%2FC9tg3yy605P5AIgNWwsAF8HJTuk0ogCRQ2E%2FlDkXKGWSIg4QDMjdMOv2X0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmcKeM5vVbQ6QHaEyrcA0VsYgZIIuElNQLqUoKeW%2BQ03qDpAmJYR00IApCWmSGU78fMQpB26ZC9OMmMZRcXlmw1gQXRkK92fWWoLwqR5K%2FQ1prWpUI3JovpyRV%2FIha4SZdx773Yt9F1c4C54oiS75glOFvM4slwjnsGtj24n%2B4yeyn8jkMUHWggJt%2FU7KHIiH%2FwNu16NVQ3Mfpj2K2IitOa8h3ILXQAx7%2B2u6cp%2B1urdhEjBbnb%2BYxIp7XYJnP4W825nNbE8%2FRgvz7b8hJwqlO7dPDfAKwtYhYpLUtiF17hK5KEFoPMa6I78omD9BXyKouU%2FsuV4%2FgodCi5c%2BSj2BMx3oXrOdQ0uV7BHe1vL%2B9cPQVIBHmpM9AqeMO94K4LMTBHb1RHgtSe36NZFyif4HDurXGuAYtJ0UGqJZBsuR27PCvqMrcBmzKWtelVjT1RLZwrMV2Z4n1pPWGuHu2VsxcGFLMm6g2NhREoOEhTzUmYnUlultSSrfsmu8UWx3pVBlzP7h35CzyCMOcOU0fGkptcIRiQOgHQegk3ot44coC43MLPcuIw3Ftv%2BeGasiIrt4GylufREaZFfcYGgoa9AYejhSXUPhq9ApFfDVmYz%2BLYxnPxVuix3RchcGvt2v8P6chKR9%2F1iosGBoR9MLSk97wGOqUBmSX1zVbkFGlvwlHix2Rb6WRRGewio76o7GNFv1OF0dJZWRnpShzn138%2BqW%2FTlubzEjsBaBF3n9yFI9m%2BjU1nTwxIrcwhFlT6EquTAkuyWXUWPYTPRlRJX5qf6I8q%2B1NRkmeE7g2VMfdvP1mFfIif5X%2F8PXxDFW9ilCc5LqVM4CE7yTE61wk90QlelcU21AZdk5PL6MR3tIXRiz1dleRYB3EPXqA5&X-Amz-Signature=cc7ffc2d7238ce70b17d2fffef5ae8ec2cb473a434ed850177211eb499b2fb79&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIWUEIT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBMhFS7btYhmik439hdSrF62vrYctiYRa70rEoVGS6NwIgf6%2BLw28u%2F%2B%2FXxFnGpkfwFTv1y8xnhmDwYU0KjNXvd0AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCIxx9hPbUJWXGKoTyrcA%2BdVTFoaqgvH%2BGeDQkaee4I37aPeurLgd4tZ%2F0JpWwtsoTklB0QoPJChmzjh4UrCxaVI%2BKBFXwGhPbwN188WSIkBbtigqwm4nlnsOi71TqszhTHjwmgnkYKNChiSaEZQKysCddblhrELrFUvgKlEZLVZJHUVBxzxqjWJmJkQ10qENdbVgRn%2BMAzt83ExDhYqFveyRwDoSpwR4MKgYX0ikWGTXFUbjYXdqrq8jWAedlt9j%2B8%2BgOB9Gw3scgmi4YsgruEBav%2FkstR3Fb5rZRGmS0Ex0YpSl5maF3AtALRDxesmFV0uQjlFG1k7nscMM6pMNCbrbswseHCZdkcMdIQjHpucT1wFTbqM7cEb61N7%2Fi6kV51doTPMN9aTttDocQgYHYAfelgz0W8WEBj4Nzd5%2FKh6eaNu4qexCXMOokfWlebfOUREArr%2BwwLOGZz1i3mV8T%2BD37rOLAVq4984TMc7PkZ9kvxaOUiGib7seyoGz8xGcs6TeVlx83CjiMmLegxiCBDTHGvWTVfoQwm2VQe810wAd25%2BdAgn%2FdqLivniJDkew3T%2FeMaXCb4y5XgATMnLC8vQ4MBoBPoIde374pUvO18BeQfllMAB01Xstn6Ii4p2zzSjlt8sx6UiSqiiMJmk97wGOqUBQ1dszDRICPa6NX%2FuKLnUjTSO4JGEndh9vqnsQYdiQclRDtRu0NRoyqGBFpS7fCkOR51xVv2S6HbtEC3KllWmzXIMdO5xrLZz1W0P6wIZQpvDwpbbwt2R70EEUVBJuBEriQXlxh2yEgAw0%2BIijPTPhagaKh5SlbpAgU7GVERtgmZ3lqbGR1Si1Wac3%2Fl0OFs4j%2Br7X5%2BJ%2BshoDqFD8nZihhmRQOyj&X-Amz-Signature=3153d5fb0074e193b9c26efc02b4f8264dd2d9bb88c2fe56172ae9a2a3280cfc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624XEISDY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVDARgsV5hJEl2uPsMEkUoovPfEunaCbUSvWx%2BiSKjXQIhAO2zWUfPqSXuTLxLM8Isgb4uqQor86P7MuUBcmO3EU1ZKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwStQFojBMccWTRsVEq3AM%2BnXrX6EPxASlEPV7b2nG6G%2FQAhUI5vz1rxRVU8ZwyuiBfYhyiKPklNwTyYj66PxJwAASfJqOtle7IHMWSaukZzhT%2FyjC2O5LKKiKc8yWINNRWK0iomZNeVbkx9b1hdptkot2o8lT7WVfZqYMtp5AyuqLR1wHouAgBwnyDIwoot6DJMZwpFW4WaAYccNL0lbL7ZVro2bg8Jnul9yaSWG8CeM5ah0jFgGL98Hyv8bv3t0ohd0pG27%2FQF6z5iiT1nI%2FhkkzKXDvJX9ytGxMfqyKlkTYGvP%2FOLNq08t69PHZOZP09U9pcNH816RBL29kO%2Bt1S71NrVr7ipn7ND4MgaOcXJhxa3dd0Il9S2bt0l%2BjaLduj7%2FQpPLmcje0S%2FYz4h%2FuA0lKlAQgVUTGDh9ptQqpQgQHkoh7FtZDKsEdxBazg9wl4ovBCa7Hb9VSQFORjcxirKEgEYCV%2FwaFJY7sCZbNWgmvPuuf3uxr3Cki%2Fw0RRLBj64UNwZLDk3RPpTTxB6QYOBbj%2Bvwlb7Ru7WRAbHyDucLiCwO1mPy3%2BdyNRcOqi5EO7dSgmLdXXdHmxDFez%2BEWZhFgOETAuKCOTux6sUZFAfgoFgX3%2BOopeSFZE2%2F%2BLQpaFGR6T63t%2Fl8OIwjCrpPe8BjqkAVDOoC430VDR3d0%2BIezYePAEyqqEN2MLdWzgZMIBeVtSvNt%2BPtK6b6J%2FSzAb9hVWaS3OTijkK%2BYejggbnt4DkeAWW2fM%2FoKEetA8PtYuR516IpnYkfrCoF67rQ0lIVXfVI1zWqVP4Iw8TrhQl3cCeiEYJbcRb0NkkabF051xVB3%2FRJdsSsNfw2Vn8R2O8jugZo7cmdkY8GAgTFFpkuUyqVAx6QHM&X-Amz-Signature=cc8eec26799aa6e81576112988d5a64faa7bd29dbd667396c1b258fa7373150a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PF7WJMB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC8CGCS4w6r1zBhsi90JlQXl1b4fYZcUCMnO35sw1WSAIhAPgiK30TmYe323gML95aAKQTeTshiREs%2FtwfM9VGTzGsKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3HHWEXqnk0u7cvOcq3AOLuoZJPtAs8V4xXTHcsvOMH4v%2B63UNLE1WphqVsI23lb5GYL6mhY22dm37TIs67HwmPd%2Fj9WZ5KgGN0GYVsekMKMLJJq2dUIFiUC6Vaud0TMj7zfbg0pCX1%2FwbYsdAmyVQqPxhDlo1eLly6c2ias06ZFDgyxVPlvyBPCU%2Bdv7m9SXdKQsOAJkRj%2FOc3oMRt12uy%2Bz%2BUTCDy2FqtwEtCId4OY3gv7SWk%2Bu%2F7YJxN14SIL%2Fj77U59x1Bl49NLkTS5k1MDmwchkYfjVXt%2BFvXV%2BJakabxv9sEZTgArkhTAPKk05M6G%2BetRfqyRlJX8ylye%2BowO1q%2Fk6y%2BEVm56r139Ow6R%2F6Vb9hHg6%2B74mjujJLppIGydXjXFT%2FXOQAdNeVSnSc9xn%2FmzdVqUIG%2FRg7uAJunW2A74RdAj01%2FFQ3ADrXzAUNhiefi28ghIPlyYCz97pvAI2hcNLTMVudC7gjJsxRji4Ssr0Y9GlG1diLlpJfJBCZoA5UYZn1Tz4RAevuOGmcCsR7eU52wW%2FfYhZ6093cXM1MM4N5sq4L3vYnVDgEStOu2DI5owE6V0itr4IYUBdJ0YM0VmwjQZU1JtT7d60unmOcE9qHew1F3ONxrDEobRWjLngkyGv%2BPKi7lXTCipPe8BjqkAfHmtKueNFhwA99u3OjF8Je8z44d3SH24Tgsbf9eN9vfowUVCb64MgVyUeIyOCXv7lxWeVkbdxOGdbBvGFsKsbwCeZJYH1HZ8XJWnQ0p98fEZoZG1ISJdpIle60uZsHI9xQy1%2BG0E0rXk8gD9m5CX0HO0gTjYOA0ZjAbDF6C7IFeTg7%2Fgb8l3YJd9sYxAMExGlfGmVXh6VypMqSZZ%2ByOjoN1qzjJ&X-Amz-Signature=4968ee658682d9f9a35b3c9a263a09f9ecf85eb3e5ea386b53ebe18b054a66a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKBAJT4S%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDATySbVUAyv7Pjh9gbqWR8xdmmvYMeyEOsQWUEGHM0QIhALZ6luj%2FfD1%2BbP5kgA71fkOlfEOQNyA0VjejXE%2F7uB7KKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyhm2brjSolcSPgJxsq3AOTkuhOJMMgK0ZDN7LtOOUvSG7xUGs3OuxzMn8wBuMDFox8M%2Baxf7jgJVl%2BhHchD7VR1RL6AIrhKoGg%2BxbrM4V9hpNumFmdf342E6zi73PplMrSC08conI7A6L8Q3HvsQSo8xkuK49CWyso%2F4M2kfePMkbLFt9FJOu0TpC%2BI8lSEZ2pTZjB5Qyio20xrXD5gPn9ax2zjNdlDn2b8LTZD0WS843VFiMKpn55B%2BBDawsrhnoPsVSYCAvShHGKSNLaIHMUkbstTYOGJPwMdiJT%2Fkrrf4TcIrLfBKI5yOiu6X3y%2FBZdghNJkNpO2p8353Pja3Jf%2FkqOUhdsr45rJ9JMEuAWkVV7qLtdCr%2FMuc3efSdCf3qYZ9mbbqikZ6ZTJhLRWo%2BUpXZnjnoTUqzXJ8L1qT%2BGcYb7bWG79hJCP5P%2BaggdWrtTZw2UuF6wqCmzw5CRc%2FBwwdBPC7VfwxodfYrD%2BcdXADhtcmMOj0zwM7eqBXAKq1sdPsLVB4cEu9uegtKzseUS23JjetQwvAFZzuWPnphUIIa3MfOBaxwSW5X%2BYm5dAsBugBIETa%2B1GRi%2BNBuJklLjgSasHlbMz6taoagEnHcp66Vxs0s0KvQJI1yZ6%2F0lcvj6NIqkdakM074YGzDJpPe8BjqkARgR81te1d9KA1v2wjNa2fQ18WsXrGwKybTHFEy%2BX02o2HB9ThD0H4g9zsEtGueKkBKaLr0mZeTxqDb720%2BbwmAjvRE7P5FY%2ByqenuzE7Ssu1kIH1pukQWpm76VFQbwqC4Vx%2Fb8dp4Z3NuPDCDpaEf9Rd%2Bm0DXx%2FIWA1gJtwpZRI28kBKoRQjzmQK0cA%2FzxHDnPG3a8JTVy9pYhRagXYz3tqzaYP&X-Amz-Signature=9e9670c6451735b7da22ba77e482501fea48d8ef991b07879f4b78bb6477a43b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPXKSVKV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGxZDSKhIDF4tu2Wf%2FvCqvUypK4qRd%2BPpXG%2FUa1Jerq2AiEA35s0MbZTjCT%2FxIb9Sqr0iiCqZzVL%2F%2BpYQ%2BeKj%2FwJyn0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAzJ6paaOaXlvl4QfyrcA4DR8GUabyOdtLy03lbnQzvHC7gtAIXsJulgLp8Ys%2B2o0LcWSQB20OEmJtiVDA%2FsOawBe8qSBXOTWdPNqe%2FIzS9ViHaHWDPkYo3VEpAoJw96SnG1HSbH0eEJrdxbClR67a4Oahkr7rq0rL9UMDGgwQnbgIuaTHQwFHT3Db9QSxYv8vYmNAYM2e8DbJs%2B9H9Np%2B9mKBsoIUe%2BqrHhV948gWWGIVc43K4NJcQl%2B2VLQ3yNdeOidefipmPrJUCwcPXHwycHwqYRjPcS7EXKmQwig3nH22CFzZ%2Bct1QYzC5HvBihIYjAQ0L726fzM%2BhzfAbJaP3XVMa77mUSoxkMr%2BHcuIobIiN9%2FcmOuS7LSAM1%2FR9xRczfReD4V853Mg4jYuxBZR91UnrB%2FAj4iGyqWFZIy%2BGtdZ3QXXaxAqOHytELm87eAu3i6Pd6yFbe1%2F1Ug36RFkdiivLRdG8M3VBLqdCDvWmvQEew6v7v8ybSOQNO2ZmF%2FHFD7lM4eq8%2F%2BYrqME8DiaO5Cka5nUdXy%2FwCqFexPzw8ocQpnzssBV91wo9af7kjDE%2BFQkFOXNbBnkZgbX9Fv4e5ZTlYCVHPi%2FrBrWx1%2BMyZPYg5EzW9rL%2BBbLveghDp5jK8dMyZ%2FBAGdxMbML%2Bk97wGOqUB6dXE8Fba9Ad6f7GL22y%2B6tWLB7uAF%2FgfAZuJtuDRxUemFxfT%2FcX5hMaxjhbhFaGlEGhm9L%2F0pWk37b%2BRjzPiA3Bit5q1S1n8RSXu8g2Qn7cxyk2bahL5r4xxhwn8ZheOZJIh9Q3JKmLcB%2BMm14t20i9h2HgUU9oYFPuc9iMFCy6wGRj9OHFSPDcvRlO1plGuSXYxEPEA%2BC2XZjuaAK9XgQiG9JXt&X-Amz-Signature=5b866a3f3fe1e72d5b67623467f5124ae407edbeb0e14f0a27da40f5fe82e032&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YR6FT3P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDha1%2FeFbiIxZ5mZRrBGPhl8BMpiUmJNly8BnM5Zi%2BmtwIhAMgbXKzlMSdniH2%2FeJfrx7J6TpHzkVio%2FoBp5CQ0PFWyKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnGvNOBunzT8K0Ploq3AMZR2S9QDSXBSlvY9Xm8BCZ%2BAJvu%2Ba3Ht%2Bv8fRnga2Bs1KpZqPp9Y2pdvno8NkT1Y2n0kojr4zRa59B49C8KtbC0oNukU4JQ%2BL5OPmSpmXFpQU79w4np0DMKa0zHKXLODW0QpQ1vyRjYF5GVMs%2FiFKcKLq24p4s%2Bd1fT2h%2BYHTJVronvw6XcZn7%2BmFM6XFh2YzkU5pC5B%2BuI8lrAvx0SAcS3tzd36mTxhinTF7Z3BvVBl6hgcg7QHo9yYodTIIMTcExqZGUTQPnRkJsiPOhoxEuIu1jGhRoIcZnKx2F8Fki2m7y5Yr3wArXrnDAK7DU52ufbgNblMZuUpFh2z5BKZf8TukAG6xdkzNsisVzy4vGjpOMDpDUryGKTcW3w77hEpk%2B%2F181q3KRzEe8LJTtt1FfCnq2gf6Ti5%2F4YGHRD8jpKKZohatxP9pCyc1se4JwUTSv8pB0scciEGsV8RspIkxCV64IPxiyszaJ9ta%2Ftk1IB5gqcq58rVKqHzdfowdhShFaEvRb1YJD5dV%2BTvlW78%2FPR3puEjU5powTeMU%2BhAfU2nsQ3x5tMBaxYuqKlZbCNXghzxqFfSVj%2B9fc5CGX%2BHOzzB2OpRL%2BgG5exo0GSqJw0ZbAC9KjvoG9d8BHPTDdpPe8BjqkAcM0YI9V2ayHAaB09%2Fy3oiO6uzTxI5396EICcPZTJ%2FRWz1VBBUhiMtjqXL7FlMuMQr3T2bFjxp3F8Z4pFEypLyIwql07TviDIal38EQk7moP133XuzK0yvuBg0ehjyrr5GkMZBWpMuxaWvIogczNTF0UlNo6UIXPBbAILXi378rxjnlHtIoHIKrNOV6P0yI4FbIOBAWeNEXQY4Scd8GHRk8VVx3x&X-Amz-Signature=fe17764f2c18f9cd31f58f8d2d15425b89ed0e9c45497827fa655e7198003a1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PF7WJMB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC8CGCS4w6r1zBhsi90JlQXl1b4fYZcUCMnO35sw1WSAIhAPgiK30TmYe323gML95aAKQTeTshiREs%2FtwfM9VGTzGsKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3HHWEXqnk0u7cvOcq3AOLuoZJPtAs8V4xXTHcsvOMH4v%2B63UNLE1WphqVsI23lb5GYL6mhY22dm37TIs67HwmPd%2Fj9WZ5KgGN0GYVsekMKMLJJq2dUIFiUC6Vaud0TMj7zfbg0pCX1%2FwbYsdAmyVQqPxhDlo1eLly6c2ias06ZFDgyxVPlvyBPCU%2Bdv7m9SXdKQsOAJkRj%2FOc3oMRt12uy%2Bz%2BUTCDy2FqtwEtCId4OY3gv7SWk%2Bu%2F7YJxN14SIL%2Fj77U59x1Bl49NLkTS5k1MDmwchkYfjVXt%2BFvXV%2BJakabxv9sEZTgArkhTAPKk05M6G%2BetRfqyRlJX8ylye%2BowO1q%2Fk6y%2BEVm56r139Ow6R%2F6Vb9hHg6%2B74mjujJLppIGydXjXFT%2FXOQAdNeVSnSc9xn%2FmzdVqUIG%2FRg7uAJunW2A74RdAj01%2FFQ3ADrXzAUNhiefi28ghIPlyYCz97pvAI2hcNLTMVudC7gjJsxRji4Ssr0Y9GlG1diLlpJfJBCZoA5UYZn1Tz4RAevuOGmcCsR7eU52wW%2FfYhZ6093cXM1MM4N5sq4L3vYnVDgEStOu2DI5owE6V0itr4IYUBdJ0YM0VmwjQZU1JtT7d60unmOcE9qHew1F3ONxrDEobRWjLngkyGv%2BPKi7lXTCipPe8BjqkAfHmtKueNFhwA99u3OjF8Je8z44d3SH24Tgsbf9eN9vfowUVCb64MgVyUeIyOCXv7lxWeVkbdxOGdbBvGFsKsbwCeZJYH1HZ8XJWnQ0p98fEZoZG1ISJdpIle60uZsHI9xQy1%2BG0E0rXk8gD9m5CX0HO0gTjYOA0ZjAbDF6C7IFeTg7%2Fgb8l3YJd9sYxAMExGlfGmVXh6VypMqSZZ%2ByOjoN1qzjJ&X-Amz-Signature=0a86b35899b5eeafca212eefc08a0fe6aa69c05c84ff34182cf46f2ce3171f65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2CHJOCR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFnngrxpfrxVhQdTWGB2p9yEIFR1W7oX18mvFfLeWAs5AiEA3NsA9Ta3d8Pvn5RhUrLygTd3AQux8HXcGUBAzQ4z64QqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJsfOxbJhfgxe8qpSrcA0CI9pX68T89MCC75Xl1zZa%2BMg7Yy0m3kTcb3lWR%2BOnQrPRsvFj0djkiKEs7MO6Im3ijlzoxxD4WOCmOd50wd0Yyhwb9ugW1RWlZgu7Ag7AvjNQ4LN1q5EdBAYd2PoDhFqYUdF78JP76KpbVUhZg1glngr3S%2F78MoBRfZKWhro8SMOXm91lekAxIedorYmncbGQf84N5ZwyIMytuo7GiqzQg%2F3AwmZbXmz02%2F4%2F5rFWghMbLg5mJBTjXIepwuFPjAu0ZoK80Flyp6raWqZx1CLCJxBlyiUwpxvlvXXG4aAQ5RRM%2FybG%2FQKpRJ87%2F5SdcNWYeZEetqJ%2FpptZMZhGarTrNNiYeU1Gy%2FVAzyIScjUlZnX8YUmTZqbBZl7p6SaTAmdIZBxxelrXYm4njcQB1dHIcKyXR44lQqzz2xf6u16eXHkJUSMo%2BE9veC4H1juM792Kp3WmlI1zgTuziuLspUlR%2Fk%2F1xvnK17M7YXyS0izXM5O8gMXi0TVCM7y0CCr8GHU2%2FvplKZ3CRmogEixoR593lQiNtXeoW2cc%2Fi0L1GzbOa9qg5nJ6RCAglXw2enJJWr7VXJxKsUz8bsXg0jdhEMjwAeqdej6rjACAgG1ZmGT8%2FpYOKGamQGDiIITKMN2k97wGOqUBU7U4h1GYw%2F1FS36yA1JlLfJTcLjWEaH5gkV2MGhXGRrx%2BQOS6EwW92otqFLPzs%2BnmYVzVtVC3L8R4HBNClhvOQf7%2BCfDj5HmTl9BSE3mhmqQwyUvaCXdkz16xVYSO%2B8lN%2FqGc1xr6DcuChCt0zgFIY1SncO%2Blm5TcTqfqCLY8S1%2BlmuXBSrvS%2BqSFFX%2FiHoFWu5K9KHJ40GBKaH%2FZTp01Eu%2BSk6p&X-Amz-Signature=6e6cd49e8b877f44e5ee78e51a373e799570e1fcd8e7395fbad3664c8a81a737&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2CHJOCR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFnngrxpfrxVhQdTWGB2p9yEIFR1W7oX18mvFfLeWAs5AiEA3NsA9Ta3d8Pvn5RhUrLygTd3AQux8HXcGUBAzQ4z64QqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJsfOxbJhfgxe8qpSrcA0CI9pX68T89MCC75Xl1zZa%2BMg7Yy0m3kTcb3lWR%2BOnQrPRsvFj0djkiKEs7MO6Im3ijlzoxxD4WOCmOd50wd0Yyhwb9ugW1RWlZgu7Ag7AvjNQ4LN1q5EdBAYd2PoDhFqYUdF78JP76KpbVUhZg1glngr3S%2F78MoBRfZKWhro8SMOXm91lekAxIedorYmncbGQf84N5ZwyIMytuo7GiqzQg%2F3AwmZbXmz02%2F4%2F5rFWghMbLg5mJBTjXIepwuFPjAu0ZoK80Flyp6raWqZx1CLCJxBlyiUwpxvlvXXG4aAQ5RRM%2FybG%2FQKpRJ87%2F5SdcNWYeZEetqJ%2FpptZMZhGarTrNNiYeU1Gy%2FVAzyIScjUlZnX8YUmTZqbBZl7p6SaTAmdIZBxxelrXYm4njcQB1dHIcKyXR44lQqzz2xf6u16eXHkJUSMo%2BE9veC4H1juM792Kp3WmlI1zgTuziuLspUlR%2Fk%2F1xvnK17M7YXyS0izXM5O8gMXi0TVCM7y0CCr8GHU2%2FvplKZ3CRmogEixoR593lQiNtXeoW2cc%2Fi0L1GzbOa9qg5nJ6RCAglXw2enJJWr7VXJxKsUz8bsXg0jdhEMjwAeqdej6rjACAgG1ZmGT8%2FpYOKGamQGDiIITKMN2k97wGOqUBU7U4h1GYw%2F1FS36yA1JlLfJTcLjWEaH5gkV2MGhXGRrx%2BQOS6EwW92otqFLPzs%2BnmYVzVtVC3L8R4HBNClhvOQf7%2BCfDj5HmTl9BSE3mhmqQwyUvaCXdkz16xVYSO%2B8lN%2FqGc1xr6DcuChCt0zgFIY1SncO%2Blm5TcTqfqCLY8S1%2BlmuXBSrvS%2BqSFFX%2FiHoFWu5K9KHJ40GBKaH%2FZTp01Eu%2BSk6p&X-Amz-Signature=57c819ff695b9a524b4ec808c9d3ad369ea5b7cac9f5ac9f07e6dde4744b601b&X-Amz-SignedHeaders=host&x-id=GetObject)
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