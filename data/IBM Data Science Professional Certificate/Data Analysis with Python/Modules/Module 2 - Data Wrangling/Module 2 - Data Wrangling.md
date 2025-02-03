

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623UHUGT7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkriM4Q6%2BaR1b5mHRYmfmIupGTAeM5BqSA67ff2ko9xAIgIk7uTyPTHGSWCh2xxyUCTTM0D4zIDvM0%2Br4osER%2BZ2YqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsQDrWZ1dVzUbYyLCrcA%2BJZLgHrpczH9ADpe0ShD%2BMPZMJmQ5Q3gBJt5ryMyfAGjdZP0IKQVtg9TD%2BauYuu49QdlN457VTRt3NLZbwpmRQnVKrflNBtBvvFZTX1Ht9g1z8L9bEGFY1uvAEP5EXcPX54Eexc4ylZu%2B1nrrmIB064O4KM5D%2F6a6ZdCjyUHJctXVMGldOHCAAlgO45DTFFRBLkN5p7PvQcsS5WQS98JqPUb%2B1CpJtiFaLaoRE7GMxRCcIVd27ZH7aFLIwIaFN1%2FN%2Fd0Fi45BSmYwRaEU20Ru6iRP%2B34jA2W7XJLq%2Bq7JSlbP5OSElegXV0%2FHQAEAC3P8rOY5461wIYqpNiqjc%2B3A23gBdvGcg%2BrVxjiPr1fanhUZD5UaKFod5p6RLXXY4SvDFt%2F6LK0lfZ3HdkCeRMPAubqhIUFDNfl%2FJhAeMl5i6V5P2jHef8fZkWib%2FkgFydMGoNdcoN%2BDYsf7UxG2hw%2BW%2BlYER84gSvSrJDvFdZEsZ5d%2BJsNZPv2nwXtcanGmgZ4j9BDynXEplLMK%2FGgmD%2BMtALeLoxItiinGFqCO7ugs97mgCzKGE0dJWlawi5RNbt6TwYNY2T%2FS8ZvtBVD1YQOyt7aVP9hT0XAeyEefQBycJFd6cQjidEeeqD1B8NMMG%2FgL0GOqUBk7T36X7c6e5oJc8TWfRydZjgp6tONyyL%2FuiIWSCv6d5LkiMboqh8UG1gkHN9tnbECJV4lqhlTstzYegQHDuKlXzIS4iQKSZfiFVODz3XXkm%2ByyIRXfOC5J0iwPuxJ7hmKuXuEhqXpxBRkp0P%2B2EwreI014nrLj9BgNvYIbhl%2B%2FypW5rrAz7fHylAT%2F%2FCIG3srrSnUAnlugRv9i2AP2Jc1OArj3iA&X-Amz-Signature=1645df85d3ae8b36e3423fb46c0dba00f30ea9a37fc8454f5ef2099f89dd5967&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LGW2H7U%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDbTQaE6MFHPY4oLSDTXioE6I8090GNlH9QtJVFuGHOdAiEAulhneTwh4RE84mGWyk5QoJ82dzsl2PfvNxIKO%2FeQaFsqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCxiyH%2F%2BgfCF0YRiCrcA1k95N6%2BhEQC1f4XsPp83Mk7e0qSNkVsHSRTmnoG0Rd%2FvCQurBUcD303%2BZAs2RI2%2B7KOVSAqeL1jlLuDdjkhVH1xMKEnrTqE0y2vOQHU%2FHnQ8xLWi%2Bxgu%2Byra3vEh8FnqgIeWu8vLuG9NqQ8Z5bdFIzXigh%2F0QeiUvfQ6Gy3bsO%2F1on0vV0VKSNBa9Y60nyIc7T46GjnR7YrVHtkxFvalPK3JvpsFqBnTieKIdTZ3XRSJj5gwz9IjEcEaontGdVY7wQ4ws%2Bi7IP2AZ1R8NnFCIgRJo6kYz2haMOENlvFRQof6Jy9GJmnyUnZyQVE9udJnZ7uzF1zg%2BL9ANhlGpRu5CLNvB33Sl3fNfr%2FGpb%2BOzKVqxQuQxYmM54PjTluYGqRF3ywmO6wZxIjxD5UYQkj7BOKLiFlCNHV50WDw7UL%2BQ7ytJK3RMXeUzoMiWJhe4aF%2BWd0y1uCvrgj1UqxMARlzX8SkQMMjuQ5awxYPN00XwsCiuW7mexqGZb6LVGsFin8uO6dtKnUJU419AeJhHCh93dQlQmN4nngPjmx2AF4DEBQiq0B5K6FhaYA%2FuvoF9OYXUcoGX1bLGXcRwtIONwg0dOwSvTwchiNOZp5%2BGmGe7zrIrKrNbUhLNjmSH0kMIi%2FgL0GOqUBwJsAWVbQXREbCiE3ufZebE3%2BReEjLEflKhglXZlmJR6X3LvKhEzaXvs1%2FDvH6EVjC%2BK%2FkBvCdVFtOQhlsTy0x2JyXsK%2BolBcE16Qm96fWI0mffmrOmFZ8mdoRrkN57%2F0DAPL%2BjYqkmBTj413db8RjT8QAmOY6GdHcqGvcWDxSnfeIVlQ0K2HP1pw6cOhfnRDLP80iA1qwgDIyrxyRh1tAJZR2E7z&X-Amz-Signature=ec0fa8936567f118dffc84387168010589907fef2c9127a77b311b2c6ae48881&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN23KGNT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFdS1YhyX6ykZTIoyeIBvZzEQWkOSFYDZFFjlTgeWGZrAiEA63ixMfByzjdwdCkCKt4WgD4Pmu8kP3qubjSp5PnIFgUqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHtpHaKw2JCauZZlaircA6LqEtreor9dey6sy%2BhVZ4p5HQAUQmcZaoY%2FMwK36rgCZCojIclc27vXqdp0hs1l0lnPu1%2F1tmh39d6M0owsJctFTTXHHDtPqIEM6n9CxGCeREXw6DBRVgXfg3pG5DglacO0Z6MW2N%2Fqj3kQLZ7LLtKNpyFmAeT9Yh2%2BkCbwmzDdjTL%2BJHd96P9OiE8%2FiUtFYH64ti8%2F9cA1Y0kQy3FB18PcVaaqfkbdW4oPufgIxa2f3V2LwYxgzrw7AmZAB%2F11rJGF6Y6%2FmDTrt6qyFgUaacx3oTh34U5Txi2lkeCmwB06PGOctzeX5%2By%2BIOXn6Lza4lUKHUcNH1fihY0%2B5vT0RGqqkn1uavjZ2yTddEo0%2FrUnX2voP3%2BEKvgPEisdiDJJNJOJdAPzWb4GhrtWUMs6kSz8QbUyjQfxvQJ11AjzQDBgepnpMD4Bio4pCrUcvE3PisOYqWolu0BpzTFgIePbM5L7SVB5EYUVXuE84TrXHBVQc%2FIiRHSDLj6mS2wX0wxmX4ViaOMQesRCs%2BFoOFP1NvBenXGuxDX9343lLZnGLY%2BTR7sbOH%2B940nWWLehWH7IIaFZKYynYT3vN88HeJQkjj1RtANx%2BoNRTczicNTx5bvEf2IYAqaYNkOsbwh9MMC%2FgL0GOqUBhg2rwr9TdAA%2FmgIpofea36v6%2FXOPxB826nvGFK4%2FINh1WXf5aLPc1chDZy10FRg2lieUL44ZFwbDqWtXastzaLldtJletSfAaYG%2FUHhqY6%2FT6fTyNBI65cFtejO6QRyrc%2Fn3vRq6bZMMoJRqFrm%2B2XEAjLuP11eCK67gtQFMiMPOVRbu8400lwVWLfLYnVWbqA5Fg4FvFLpkC9Vd%2FjoZWusb%2FUDM&X-Amz-Signature=3a1aecead8220bc1c1736318a9a374fdc625ed11791be9bc65fa3f16dad6daa1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WKPAYBG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEJmNbRO%2Byqp1YBDJNP1RQwp7z1cBMhGQwzbZxzdJZ3AIhAI3Z9fIdoZpPXPLl5i1rdkrVt72vVGt%2B4aVaXj7O8K4zKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPFBpwmMQoBaV5uPEq3APNodoC5ydRpz%2BcyaENlWqBOs2xzKMqZ%2FURHu%2FbGcpa2Hw4ckp46TmjF%2FxO%2B3AGukv7qcu7PUosnnsUKGDLgD7MIZf6iI8BpR0m5gkSUfdbslEnVdWD%2B1P%2Ff0xWrtUTpp16lRcs1jqEdi7BTlhvjVqeMo2McONYRNpg00VDYLi0Mle7mee%2FAwGndxnaQzeR2Zm8th8Ym0kuP0FtQVKrWvpxSGqljYShMvLBUJoy1K9qRg9gWHDg1R38pDA9cJy%2BbHWidN0Ai9t9bnoPXE7RwdASptXbxA3vgFx%2B3VWhwtY9egV%2B4V1kKu4VDsk9z9go9GnMyX3TvbN5dXsQrhfSP%2F8FjR%2BIjiTkzWtvHAo6rLuJzI8CG8%2BNVyRfOZSu91gEVnXJcjcD4hLHkJ6sK3qcJgo4HiPZufE7frzRdx66p9JNvQga%2BRpzGmv1MJXKm6x5b9ITv1Vg%2FXK4T1Okl%2FBpfsZOxChxBYD%2FSthwWU9gTXPUHX6%2FgBiCq46fbUqE9MYrDaayCZ9XHQiwh0n0Vm%2Fdh8LKnUSeLXalcd%2FI9r24rQ%2BjqT0mEQZ3UJercNvyAArz2iSYDfOoLkyEtK3a9PaR%2Bzc0qghCCg0Bdh0HCHs5UK5Zsog4GEbBcVvSiFgLHjCewIC9BjqkAYYWj8LKG7oobZBCVHgasZQgM2PlmRdSCdhaeufiPpZrAyKoNWd1oOw07CYHs%2BUtlWhi%2FYKAcPxcPzWWz1SLPP%2FGTvEQ576VdjpDCshU3mxTmvL8n36W86BZi2SJxR%2Bib%2BkTuGYur556DDqHkrh5uUrrNOiJgXIqMdrcjvlMQSyB2lPiatg%2Bwd2X4pu4LchvAuzQbGDmDBEBip7%2FSmKUEaIye20A&X-Amz-Signature=c876df4a6517662bd52b0d5c18a5d1e1205a26a562d0267b48131c3dd551ec98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5PQ5JSI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA72kF6IK78buhxkj9pCt5B4lIf5an2Y2Ako5yFExlduAiBFOwq%2BNOLYDnvRAkAzSdh28MVfYAjybXCxgO%2F%2FvbBpbiqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYMxYDjQ2GEY%2B7LEbKtwD55%2FlaFS9j%2FIBFfTXjHpSkOqpl1uVZ8xzz99wsr594ZJOQ5cjdyNWs%2BO4v1EU2uUTClNFxvjGsuXwanLtxrcfzOr1A0ecT92u71iR4NFCweg9ueKK6YYuieYkiEn%2BKoLWpLwSyo0Y622OUvgqBDEimrfviF%2BjUkZ2Rv48%2FoqFwaqInxeYjf2PeLjGmeVEFUYQKZPs71hRe9FqLGEMizH86w%2FtQPp9v%2Fm81CUxD8IeHC9IMEdpxzM5jFLGIGUTH42wdh01J3G5ooYvEC0zvckdHzcFj6mh8RjnEUX2wFvkqeUVsEsk3nAIX%2Fz0DwyQ0L2P4OfbEQUUuXDGUwAH%2BgeSdUMzkj%2BIRP2HpBsnVw9q7xzw0iyDIdV%2BDgitx3iwJLRqhwvmOIifV3S0e1yZ2G3pttxJvI8r8K6Rpx55AQHE6gCa6pRJqfrCGyBF9KYtn5IxDQGQ%2FGyG4LmOXZhbrDJMlWO9w7esAC3bPXCggiGzR%2F6QyEb9Xuzy3bu%2FZsF43sxkhXkJQlVu5rJZsZUJeDtvfynlSC0v4z87spW%2FacLrFhsMlGw4DZkgWYj4Ior2a6yLkviiiuh2g0FB25GeWk1ytew46WcGnE7TNURjg9kbg%2FhwrpnJejsVz%2BsYqckwl7%2BAvQY6pgH99W8Bo6e0X95ZdPi4EEy%2Bp3r%2FNqX9%2BdV%2FeXkzz5WJ9LNF8FNY0eVuP1BNTW9AD0LeiS1GXix8NUsi79X9w35Q%2BIuuUfhQIR9VFwC6bg9Kwhdgl2ZW7669DBYPj43sJXPGH3ERXXpchakYHkFp549PuIOELcaQRBHEBQiYnqI40Y4PSyfCTDb4ZTZ1QDNSf3gbA%2FbO7bra4re4mTndzN6%2Bynql8f1Q&X-Amz-Signature=c2b0ec2b8e35bf03692545b29460d61ca05fc95437a8884e86723a72bed2edf0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OED4NKW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmsGX14Tnsjd5ag%2FuAu%2Ba5P%2Fm5qlHs15qY6RGDbyI5MAIgMHwS8fgnp49QROFZ4xem%2B%2BRcisiwHijEN%2FEKKj2zrzMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPke9uWIhYUEygBOfircA6MDR8iv3ZLc4hk75tmDZRb3dEJlve3ypLurXtH1mxHu98UxpjhwXqs7bBvOIkNna%2BvQla0mPCkUcGbPt9prwmf%2FQy4iGWd0wumPCYiqsPNinLQoehjDb2rBbgH5Blr10lEs%2B5A3mdyILfDNQIQmNgxpia4tiUsMDpl2CIRhhCn1SnrDEvirNOV78rupZ0QagQRmseHNrSWCNHgLsBMDVNHCxCg5kTiAvJbCQnP3ZAq%2F03yjDuIa4QjeKRdLRMAstrz3G8EPRDwOKb%2Ba0sfnhbhF5pR0Q2XLcA1W5GK8rYNmijqqpCHQGblFz4c9Hn4DVhMynOPLsve962f7bn749cnCO%2BsOtgTANHVlO%2BIvFEGEox8WdViowI0QNB35UcSlo%2Bs%2FYWuA%2BQb%2Fc6Gbv44%2F4RY6EuAu0sdcZ%2BJp%2Fdd6E0zS0td7yMBpjhMKaXUIXdse4o0YqrZYFoML7HyYlkjvWSjM%2BJLrbroy%2BAMC7stNnz%2BTtl%2FWGDzk6PmwfdfCRaJFsVgNlRvJSwhqdLUQsAmWuGrjkWf9LG3C%2B6EJhhXVDc5gUoeLMCm6pEicf%2FqcVbWefkkvkyLh%2FT7xD0eoPoD9Ymy4XG9scgoG7KzEy%2FMxegPwJxO%2F%2F%2F6liQUCzgB9MK2%2FgL0GOqUB4MiLfcRu0qoIKWRF9MR7Z9LS9T0ICnPHJ11N56hUba3MB3J4OVab%2Fy2CPu%2FVbgDH2ljZbFpKGfkDFMEpPrJyCGVug57Pqx7VE2IK2150o%2BwVH0aIlVg5rFaWkUjl01gKaUpf6dAhxzVW9OeYV3SzgxET0071Z7R5GcmPBUIu0ZKIr2w0s1GHzfB4JPmJyOBzmgAtWkCbU7if6UWUtuBDmRloXC8K&X-Amz-Signature=c5d15f6a697dc75e57103da8d094b24b0ff30c4cae3a30e7604e30636380d786&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLZABP33%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBMcklT2kCIfUblQJIQ4q3ToCwNvVLC%2Fb6RqHceP2AfAIgImTDW%2FJ00VX2eT50h66CCG9lOZqyFDfY0qxMmSqP0MkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM2UkUgcvDUk%2Fb5mLSrcA%2Ffc4Li12CbhBDL2lDWLvhkOQAf7p4Upebf7HZBszIE7DQRbJiIhBCM1ymJn3ggIE8JvP6rt0%2FQg6AF8pWAzf9C%2Ft68z1ESkQoeYse9dglAnjlua7YaIy6hoNAMemrrlrEpfhrdxldLLBjhvZQIXwg9B8aJiq9UEe%2BTaY2RsMaP5X3rhXhg1ysfl4FfZtjPcYuqCLRFtNXZJAYxqIzH1Qb129z38p%2B78doLCoQ6NZR370wdzavOlsp7AA65hwXwKEpnvtxMv4Uy8cLo0pUlJqO%2F5WHXD%2BcZg3oRl%2FR2gCL2kBudSLU5EFhC4eO65EfsePM1G%2Bc5l1PyQ8EYB5QW0XrJP8PAwLrH0Kf8hfggpBFRNyvF7zwTVQwEOLk9vyipIi0QH5WAf48cH5fbJL91L2vJ%2FwQv191JymqnztYkZOr0FSBb7HhkX4PqP3qutHkE9UeXsoZYY3007m9bX4ta4DDkxI2q8%2BdPO3bGzOqORlpAUzFw3gXtd9MeN6B3VD8sfqUbgOgMCOFpGVvZ6Vy%2Bes3TbY0bQS9iID4lk%2Fx%2FBABT3WF9oOnH7nIyeGLLj3qqqRYypEqAw5qc5TudVZABmeVsluPMzM567nZPMsg8scO2dntW2YD%2BKC3g7NyGJMMO%2FgL0GOqUBM3y0OsOHO8TT7btd7PcSwcToYKNHFPVp0DSaEmLNanvgrMZDfOJIiWq3G3g%2BT19b4ubcqOkqW%2FwPVQ7z%2Fv0BjelhyQTWFyDwaPzJB5My8SfqBqP3jEQgtzI3GVEAzdNE0rLv9SH8dd8IJkzqTQMhNB0G7NBcviOqzbeygBODYQhYqQROu%2BTR8WwcH82V%2Byr4OLl4tvVEvlhzpnJzhNdONU%2BunCUP&X-Amz-Signature=d49fe261cab5b71b2032262d5cec0bb26ec80acfa71f32b680106d0ed568d876&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLOWS4E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGhuz%2B327WdSXYFK6K3Zfzghr3%2FbjGFOJAuzsGwR9mP7AiEA5V%2FGMBRVIDJ48zml2pjxQIFzfywOCD0OBTe8%2B0CBwvMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL1hz0vJI3T9icU4cyrcAw02tXALvHAoRWutqcJ9yTBHeVZTCsqSvtqIwcPPGgxGQZAo7RzzS4eRgL3PfE%2Bbyvu8vFSjx3cimZyEemZFKOYEjUYqdAuTIfwnd13FzrEgLVa%2FxBpWl39ioKzbfajc3HNM4CPZRnLl1biGP8JWrJOp6FQXxvC53azb4I7ZY7ROSj2jLSkMiiE%2Fcq%2FPFxS5S%2BIi%2BzqwIG3ih3m4ppjA%2BaMVBLZodze0Bw3eWU9owERCAOB24uyy8e%2F6n2T3BU0DlxjrCGrDOtl1VNOsGH2sozfBHDTB9eZ0%2FPGMxkXz3OHt%2Bl7kQwU87CgCci5gLLJIadzmKiXh5WBweENsln4Db3jO%2FfPyjYFg0A7SgCvFAndMzDBAlZ3IybbvuFyky%2Bmlh6gV0IXbUGwlU%2F2I%2FTsMKvqem%2B16MiBFnZTgsSbo0rrrqeqAzxhjsGZw2w2AZgjDloOx2nRV%2BXa%2BTsd5QgjkC5cnh4ox8oqPWN2IbHI%2B5clb6q8IuwzltogPU9RNIWOn7vIi3iKQDT1URpp4NZW4DpcltTxkI01OCIcvzuJrnOkhiHQicSURcdVjgcYFgprCtv2M98lBGijGgCIrNt6MKnO307%2FqGgyc3z3VD%2FjNTBcBrcLXepbLYm87%2FE1IMJvAgL0GOqUBQF%2FuCU0LeMoSsLtn5vzECZ3JHjZzC6TBeV7SGJOk2ZHK2I6vv9RTZavxpm6SNE8%2F1ueBKnKUASLlKU7ePNQSjR73BY1sB8Ntx3RhKJhjPLsb3Jzo4ozk7vrJri29r3FjqgH6juq%2F%2Bc0IdSY8OtM%2BFWlnvU4ykSfzS32bb1i1tE4weJfNIKeIvHOn8JMXK89yo9NVUVgYqCTfcPvNMN%2BjBBc4RVs0&X-Amz-Signature=56bfff3141eb444267e318acc797f11c5ef9365b906ab1a914b1988f4ed455b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5PQ5JSI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA72kF6IK78buhxkj9pCt5B4lIf5an2Y2Ako5yFExlduAiBFOwq%2BNOLYDnvRAkAzSdh28MVfYAjybXCxgO%2F%2FvbBpbiqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYMxYDjQ2GEY%2B7LEbKtwD55%2FlaFS9j%2FIBFfTXjHpSkOqpl1uVZ8xzz99wsr594ZJOQ5cjdyNWs%2BO4v1EU2uUTClNFxvjGsuXwanLtxrcfzOr1A0ecT92u71iR4NFCweg9ueKK6YYuieYkiEn%2BKoLWpLwSyo0Y622OUvgqBDEimrfviF%2BjUkZ2Rv48%2FoqFwaqInxeYjf2PeLjGmeVEFUYQKZPs71hRe9FqLGEMizH86w%2FtQPp9v%2Fm81CUxD8IeHC9IMEdpxzM5jFLGIGUTH42wdh01J3G5ooYvEC0zvckdHzcFj6mh8RjnEUX2wFvkqeUVsEsk3nAIX%2Fz0DwyQ0L2P4OfbEQUUuXDGUwAH%2BgeSdUMzkj%2BIRP2HpBsnVw9q7xzw0iyDIdV%2BDgitx3iwJLRqhwvmOIifV3S0e1yZ2G3pttxJvI8r8K6Rpx55AQHE6gCa6pRJqfrCGyBF9KYtn5IxDQGQ%2FGyG4LmOXZhbrDJMlWO9w7esAC3bPXCggiGzR%2F6QyEb9Xuzy3bu%2FZsF43sxkhXkJQlVu5rJZsZUJeDtvfynlSC0v4z87spW%2FacLrFhsMlGw4DZkgWYj4Ior2a6yLkviiiuh2g0FB25GeWk1ytew46WcGnE7TNURjg9kbg%2FhwrpnJejsVz%2BsYqckwl7%2BAvQY6pgH99W8Bo6e0X95ZdPi4EEy%2Bp3r%2FNqX9%2BdV%2FeXkzz5WJ9LNF8FNY0eVuP1BNTW9AD0LeiS1GXix8NUsi79X9w35Q%2BIuuUfhQIR9VFwC6bg9Kwhdgl2ZW7669DBYPj43sJXPGH3ERXXpchakYHkFp549PuIOELcaQRBHEBQiYnqI40Y4PSyfCTDb4ZTZ1QDNSf3gbA%2FbO7bra4re4mTndzN6%2Bynql8f1Q&X-Amz-Signature=86190050c0048c9eb3bec7822e1645c9ce836205423ebb57d94a6efc59fc2db5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REHSSV33%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHp%2Bcpqftc2f4AIcGDvaLYyj%2Bzd%2B1uqpx32%2BCwvzfJzZAiBbpnmIycwNtRUOcvNhsCYoDx%2F6Vr8jyLSU2ahMVr5cDyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMktoXMLTSPaGLVF0gKtwD0swxIw6TFBBcQMh5glSObMEiMPAPOyOOtKiAcHGJEF1tAlx%2BTaGfXJMRQNMuVIHa2pnxhegFUON6RFlgovawglYDgcO%2FlWI8HRJYD07PWh%2BtQ8KFaqGCgZ%2FQ%2Fdut4puWMvOu8p398mot4N8infhrZ0B3fVFi3vJwhFFypBMl8QxDO%2BpkNf1mxBgjTVs1R406oAgw0use%2F3jiX44CzW9JD%2BPg98CEoXIQSDZoalbydA%2Bpbdne4cHQnzna4TjSmG4%2F2dTsruM3jio9JpigcJxIB2cHZgB9v8Ixxr2QQbMEGLseF9wNyORfNAJ4CtjvGwYpDeUc6xA5x%2BiWDDSK2qRR6wElhR%2FcvpQZl%2BtTAgx5KyugaTlF7zu%2F8GwWkxCyroH7qzYP4vDWlg06bH3QDMcyMN9WbsnbGr4%2B69%2BASrOxskB0oAM7HY9llaIZaBwKqVkgLdaYnfCRSV76iZUeXwP7U3j9Eg%2BibRZiEc%2F8R2yIFcB%2BK4yucPrf%2F2DTWG1TUlTjFzRezSSFK%2BHujAL9nfhplgZdJbbSUhbiwR7Rw1oCo4NMg%2FEyHnnX0tZ964UNL7mm3%2B%2FO6CompTJPMjJzQgBUPvp%2Bf0ZuROBouLt4wr0ptDHv1BySIuW3EOYDDkowub%2BAvQY6pgEK5bPnD1gp3FMH5Yg%2BWTjNgdJWFy7KZnly6ZIuOZZ4T2rLUjw94BOPP9t2tLjEgv2whIR9YDeknM5U%2BAnxqPQuWPQUk7etxxZGiYtQDa5Z07X0JtaZQAJjuq3Jg4cqoSAoBtvDIByc4f2e4V2LmvsopaPa267qh1Z9DKF2nAZz0Jl6Ahe5rAAFX2EUe9AgLibp2VHjYlFHTKO%2BKCdqCsoCf3cAPbe2&X-Amz-Signature=9b236adaf11e24e3f1781692ab0c56491bb0646473b2deb4626222f264c996ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REHSSV33%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHp%2Bcpqftc2f4AIcGDvaLYyj%2Bzd%2B1uqpx32%2BCwvzfJzZAiBbpnmIycwNtRUOcvNhsCYoDx%2F6Vr8jyLSU2ahMVr5cDyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMktoXMLTSPaGLVF0gKtwD0swxIw6TFBBcQMh5glSObMEiMPAPOyOOtKiAcHGJEF1tAlx%2BTaGfXJMRQNMuVIHa2pnxhegFUON6RFlgovawglYDgcO%2FlWI8HRJYD07PWh%2BtQ8KFaqGCgZ%2FQ%2Fdut4puWMvOu8p398mot4N8infhrZ0B3fVFi3vJwhFFypBMl8QxDO%2BpkNf1mxBgjTVs1R406oAgw0use%2F3jiX44CzW9JD%2BPg98CEoXIQSDZoalbydA%2Bpbdne4cHQnzna4TjSmG4%2F2dTsruM3jio9JpigcJxIB2cHZgB9v8Ixxr2QQbMEGLseF9wNyORfNAJ4CtjvGwYpDeUc6xA5x%2BiWDDSK2qRR6wElhR%2FcvpQZl%2BtTAgx5KyugaTlF7zu%2F8GwWkxCyroH7qzYP4vDWlg06bH3QDMcyMN9WbsnbGr4%2B69%2BASrOxskB0oAM7HY9llaIZaBwKqVkgLdaYnfCRSV76iZUeXwP7U3j9Eg%2BibRZiEc%2F8R2yIFcB%2BK4yucPrf%2F2DTWG1TUlTjFzRezSSFK%2BHujAL9nfhplgZdJbbSUhbiwR7Rw1oCo4NMg%2FEyHnnX0tZ964UNL7mm3%2B%2FO6CompTJPMjJzQgBUPvp%2Bf0ZuROBouLt4wr0ptDHv1BySIuW3EOYDDkowub%2BAvQY6pgEK5bPnD1gp3FMH5Yg%2BWTjNgdJWFy7KZnly6ZIuOZZ4T2rLUjw94BOPP9t2tLjEgv2whIR9YDeknM5U%2BAnxqPQuWPQUk7etxxZGiYtQDa5Z07X0JtaZQAJjuq3Jg4cqoSAoBtvDIByc4f2e4V2LmvsopaPa267qh1Z9DKF2nAZz0Jl6Ahe5rAAFX2EUe9AgLibp2VHjYlFHTKO%2BKCdqCsoCf3cAPbe2&X-Amz-Signature=2a81c706d3c488198c3781520fdfd0c8daa2e44f4fe3dd4c24ec10fb00ab40a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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