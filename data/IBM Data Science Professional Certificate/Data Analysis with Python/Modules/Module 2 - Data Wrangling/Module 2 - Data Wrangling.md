

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYBEGPZ2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGF%2BHFTR9N%2BS3JbW4CuB2PdpCdshtbyEn5ejHkpyYBVuAiEAgeiqIW55FcZ1FSf2WVuADDI6yzbOwfRfglv3ybqijeEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGQWrExr7Mr8ych9ZircA4x9dfUaFH1CuRSY38RRdZwXvw02BDvPPqV73E4s6cNDRqWkJ1Zc4OfppbBJ%2FnUpieiFsN7KW%2BCSTUDIPKUDZnjdv7bDcWpLVK3GiBv%2Fdi8ZKEZWEgCGbXytQPa%2BF8N%2FiaeProEWlzKU9yoN0mtx8d2H3gLrqZRLukGqb936XjuohpBmL9PisCNY3ZDxs%2F%2B%2FeePKBvHOioGyiMl1cxPgkuoxka4nl66%2B33MCzo4UX8jh8rowhB4uYPx8XKo9zGDisU39WO6F5WAnwOFlnPr9YQxiK0sB11A5G3eOM2VBvaqG%2FgvDDJcHshsc5EJ772%2FAAyfGB3UeVP4ccYAWB3pCETkkAV5vGeBqvjGfZzy%2B6NknUSwHDUD5SWeDOIDNCkQR%2B%2B%2Fk%2FIC%2BuIUMdBXCOWw98cJIN%2FHVD4FCTHgWTzEZZQZd%2F3RNoA0gfzVZzRoO9vWQ9U1yHXs2Qj9b3jRmMXmtMPmIXMQVviAsYL4yJXc7kvy55PfC7CXCCq%2BnlS%2By8e%2FuwcuF8Az2Yo9zpRGp5O1K6UYKyq%2B0O3gUn8iTQQhuYOmxsbPjCYTh9hnMSj4mShlzodcwsQBZNyBdC1R920Eqk%2BgVOxsYtN5OvhQ%2BoSzM0bB9FyyTrsuuGTp%2FIcQtMKSc%2FLwGOqUBfVkPf53aiTFRGOY%2BKmHLhHXNyXuB2nP%2BUg2d%2Bjf%2FeV%2FXDkGRr3lA5CBgi8asRq8AnN%2F%2BqPFbKzx75uo1Ko6qHDCoGHEKHG7EQXAO2Odow9FRCfXyH5S8wBc%2BVx3gPqE8JdvNe1FyoqvMiM%2BKl5uAWzdeatWPF%2FBTdGXIPV4CkiU3t4XQDlvBH6muKGij6Ve%2B%2BHnpR6lNY4pGxDkA5sd1KeX7Y18g&X-Amz-Signature=7ee2027ea060c90739367472eee148853f0644ac5acf88e3b98dd0366131d80a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HAEVKKX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ2fcSFX5EwTlReh4zcKx6NlU3ZscLs3hvxUBYx%2BhRmgIgLMp6pLmkGfhrWqoyzH9efP433hc8eZsavNxPi%2BFk%2BH4qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDANzuamJJuKKFApyLCrcA1SASLKY%2BcZB%2FJWCqoYtkC1gJZA%2FcU7vYTrOVJyHPE3iIivfnDNMxCzyScGfrG90GSNUkPQbFBVT3DdUyUNSQYLKU2u6FXSyimWoRzSov08WVvVvAlxRVNYKr%2FOX7nsa6ncc2dstdOI0PmIyI50oJDYrsdrmG0Vhkck3O5s55f1ccv5Sdrp5cbnPa3EMBTaoYcA%2B0%2B0ENf0cgg%2F5qQorbcaDSeu3yEPrGvfcwQ%2BVQB8Ceu%2FxqoXTAw%2BJcjw4Eg0oKqjVdJseKB9PNPd9of%2BHm6UPAxnD9c36Pc54wFC3Tv964znwyNre1oFYwW284CFtmy%2FZTV55f%2Fa1Cd%2B7LZV3%2FrqI%2FT1tKQnkmlmiZwm8Zibyw1OI2wkQSz55MeYp1Y2NSBUZ4O9GAPUW9jTTsxprxJZwPFfasW5V%2FXChi6SDb5pUf%2FxSoHz8ijsxfhW%2FqH%2FByv%2F1wyre2xDDBAdgVm23iawzjCNDyZEmOH397rcGneuO327C%2F8MHGskirhcI32gtBDTPWMlvu3oc5FnQgkOovo%2Bmx4FoLFQJbJwWeWR%2FQOdwzM59861Z%2FoUKlAGdLQJy4n%2BQC1SbgNmYv3dUm86oQEiSdxDlKP0Wffg%2Bqejict2vnQlA5sAhxA84x1R5MPeb%2FLwGOqUBYislYVVvDdNNSzNSj9bvLQ63X9M5QwXhSTQRFTtYCcFXkDzJrg1QsgSXDWnVCTiI3CbAluoSTxbH%2BS7sGLv2q90LmatghW74OVm1tRrnAuCqeaKthUo1dm8eTvSigqqvcTO5%2FC1bjp0sy05j7pDMo2xlJCmVDSy86KOJLchC7ealDr2e6eGX2gqjQ9%2Fq%2FyssG49gJR6Qdvoukzywt6M3XV7cbIXB&X-Amz-Signature=03587d5797b168c04a632bea066b3823648bbcc39bee4d86df1575d64f4736b0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PPLEQ7Y%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcU3BAau2CxqtTHV%2F9HIEPhIcHPZ2dXfBe8lcx34g4mwIgW2xQubaxpBq%2Fx2lwdekSVEnM14WIIwu5ItlytyWig9MqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKnbvRiwFvugyMfZ%2ByrcA3qritjV0TM8%2FPLUcTMoiYa1A62i89zvmXFC1RyOuZ9ceQj19ph83FxKY3uFlshlJpHncmohPQ8a2rfWjzmjPDvGzdCxvLBX5mBvVVv2fWEfppMpDSVJKHBZW%2FTMxaxA1ZN4pLE%2BFLOShOrMwBCXIxkmfQMk61BLC0KJRv4ugbKqsxaSOQdQ2I%2Fy6Ef%2Fjgbyy96D51t8Wk3YnyhkXm31eFLg1z%2BuTWh9nM5IWD9ek3RISgZbeZmgkwsp%2BQTYRV%2Fg7QmYRlvvD6S3Yp6xjVND5iBrKev5LIpDRQeHyVHE5SM%2BJKStfI3CxIn53Y9uPVbG2qGuM1rn6ufaEvht967wWZuPKvIXILVP%2FF4Sdg3fFVfPizXENA2lkVzg2K%2FRPATx%2B7t9jbWzRklxLuBQ1fMJb1AirQ%2BU%2BMq6W5tdu50kb3J6y7qW08Vwiqpipk5LLoFQqcumU1bTelApkwT2g9aFgLeQ2czu8ak23LhlI7XHb6pZCu84jW%2FobHchA88bySelz%2Bo4l%2B8TAuUVm4PHwqZT2CNspqgKvynBPEtOvHBwJECq72UookPtKjuhtE1ZEiQdAHG6pTz%2FBwEcxUHEQ4e2M8UvJx3mwfXd%2Bn1GfnqxYjsBaQ9NudatmTDjmCHjMKOc%2FLwGOqUBoGOicP3NNtCqcfJIooQ3pV7bRpu1r%2BmxwYf8yFPT0D%2B7f4aA6EAiQ0PgGn1PUN4QzOea2EDXnrKQJE8zaAvFATJS4lD3pNDYPN8WyefVI9EN1WkmGF61Fexc7IgL%2BqkWPI4VGY%2Bmz9oILXhi0XIsA7hl1novGpjaJd%2FFm4amKtcs%2FL%2BVOkFukXO8NZnyFbsYg%2BQrVExreXd%2BdPq%2B%2FmDFgI7UtFQo&X-Amz-Signature=01bdf58e70b6c80d703f0e4e1cca98a83348914b22a8943a59702280d8147bb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXCT53TQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIByRirX2cF2HNDJJJwYD2Nne6tHjZ00voqkd4%2FOxKtuOAiEA0BnXZiv%2F61KKT%2FUwFVMXYTEftgVIE%2FiE4Ovr67bElccqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrRmOzcSlMYy%2FlgHyrcAwoxcTciobMaXYnDelUxbBxb842rXNQru2FjPhS1LEkgp9kp6YEu16t8ttk5lGUaZJDEwv%2Bxcw4rdAqe2avym2fQmOZhzAk3QxrIllr8mZ5u0j0JU52g9K2Uky%2F1kFfIVVDIxLgnr0pcSAjTF5xN6TDLJ8MwmxCWhdbgFmw7vBEK3mrTfWNKIm7P0snfIbnzVMQzE4iQTdlbPKKrjBSJu71cNFu7F7jUUFRCu0umWjSnQV3VRwYnZf6Mkl%2Fz9EVWnxZl0tVtf0EV9ZJCyVJrsDI0NdtbA2zJDAyAiu40sByGk%2FGa%2BULgMvZIF3arkJEjmG1jbswTo8CnKpdyFVIWEplf9nh9Tx2iY0eP0MYEvdULB4UkbI%2FFLZCUvXMMDe%2FTyxX9V9C08zvHmTAZMitiym2f18IqrPLdpkjb9YaVgtQ5XsVpTiVKOsloc0tb%2BUqDDnI73k%2BdU%2B9SWqgPsg79YceTthbXFAKSl0ZanAsXMNT1haClfpjWMcJrLAUQJtQNX9Mu0jO4yywjkVo0Igz3hHJQu7w75kJghzyF6H9Reuz4AIkFfnJt6bLo7QHpTOszHGHEgy3uh2X208p9BKzpovn1Y2Y2%2Fybpu2whqwcFNMLo1qLH3O8po1pYbd03MJqc%2FLwGOqUBCM%2F2CheUwDu1teSHETpyET6v3ZaZ1DpuuicUGOP%2BMKw1iHi7nmIEHGBtxeyi48mA4PGLpVME%2BtjtZqX%2BkNf0NuxGd9CKMMhLOfB8fjtJy%2FAIX4lFCCLRK%2F2rpAJqARPTeyKgmDsuy0ZZtzz37KGKIqiKKXcEytcXvDNM%2Fld0z5tmcCH73NiW6TOAhFcT33BHuV1Drw%2FQk3yNdkOy5FSlPFm%2FSXkG&X-Amz-Signature=3fded11a9bd68d1be3ec22776b9ff82fe22401badbd77db3e1585226592fd934&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627OONTHR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAJc4jBhSKTffH%2FKmxapjhiGfM2HvfKH4kWQ77UXYw2OAiB7o7tcUJ9KCDL6GezOJYbWOzf7PU%2BS2HdW0PJApZLmyyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVFx5fKVbDuSvAZgwKtwD2besunXv75d9bvogg9rOgOJ8wO49MNY77Hwm0ldUhnz4Rm6gqHQkx9kogGKVi%2FR5MBEe0xYPfeifKL198sYLe%2BczI3Engtbh0lFxb5mqukasOVbBVJxNzCrFj6KgxIymW7%2B1qyeGli%2FRN1Q8lWM6ZFJlBAsKD3c7lA26rJKa7Cbsut69La6ua4eho0DsITMLSyfKiXLx%2BKsSTEMJKk4s1qqq2edmaOGAYGOIdZHIl7d3KdQcmHAzhYeb1xlamEXT8Q9eUTdhGS5vNtbROO7i44WOgeO56Le7NydIkFrk2uLbQh1Bq97ZIUMoP38Zms8i6qJ0na6vwqTe9%2FHzQh97aTGqPWeWo32RZ9tQVAI6Jukt8ODXokSwVBLDZpH7mHcbeNoEiGsMPc3lArGQi7uaDKlW6FtToQ9cDWti0hWBHHxfO3v8Eh0yha7KZh88RCvx1IthuYjwnP0M%2Fh8sUx0p8SYVynjfK1NqyWwtQWD5klFMkwgAudVOeOz5xOfCLTlEjYHP6y3%2FSkOFvwx334xE2W4gzXSQgu5Xn64Dos%2BEZhvElCApsDhFs2PiFFwW9738T93kKExMClrUH3ElMMQfi33l4rmLOEBgfOIYGtdPqvvpOP8F52Ag52aO%2BGUw2Zv8vAY6pgGntZC8%2FzaEBmtSO8oFxvnUwijrCNKbmqbL6dQtCaj6FSZ4pPMNdhJRumuvg4NBabFlhTruk16Ho4Bge63yley78Tf37H0QcikkQAfdkm%2FRzmxs5ghgmtAx3s0MS51RbI441WnKgPSQ4nhMU1MrhhUPHE1ex5wjZeAXARg%2BlI3grcqeVuCcBXPtmeA2zTBnj1IV%2FNHgcn7gOet53qA0X8l9jo8ZidmD&X-Amz-Signature=566bdc743648137d00dfb43fb193a1dba456a58a77f836b833df5a84cfb39709&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJN2WWOC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcCiV3c%2FDYSNhwZF%2FqzBml%2BMrTDoTJiMllpzFPeLQtPgIgWtM1bjnHsAoCBw7Kd2GGvx5IxXPK%2F8pveqFgFwoWmy8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCWWiSZ9JLVHjQ7ozCrcA0aYqgpQ1iyVPBz3R%2Bnwk4thLengCg36khuwB%2F1vdFjTIuWnPFdpEkO%2BsjV1AaDQk237uWILo8ObT8W1d%2FZ6eL1hGwPRXUWpK6EXaMVD8Adyjp8zMXUlgthOZzcFOwPc762qyIYxDxDDHc1MQSPSEjIhjCQrvqOYutKAGwK08EGWblzAWZz%2FnscXJ2C75I7oMSZVJR%2FLE7SDTgPWvEl7VhONQyHCKvGxJOj9TrsZU0aarqjrSVh9KsF44ktL23yWkM9hyjp3dis4KlalyqhcaNshgvQQZtllTfO4vwSd0eJjpiwqaqZ1%2FalmBo2G%2B7vhplHD5veFh9S%2BS7aUnSYXMcCBy178ZJJNI%2BgDdFYgsorFgfy9v02SBiQq%2B6PUec1Mis2g9nIgf5ArfaN5lfKSZA1NCclB4T1bC9H15WO%2Fls3%2BrSXB%2FZ2hmR0kHP9ln0b18nCgUcWQptPDdgya1iGQvmZAlleWsW46J6OhLm3TmCiPjhm%2FHFLQXuw4V%2FBZdr%2FoecHff2Shwz5NXj8FxKxCyQpDpzbYftWt4G4i4Zid9IIJtQBCpo4eW%2BwH172RBH%2F08ow3kF8jLANOU84UOoRfMtwVr69GBn449TAVM6r9sWUzMWt9%2BVGUpk8iXMSqMKac%2FLwGOqUBd8hEpSYH0hyWwLRP18D5ju0tpgyJU71U2A9juza%2Foeba3PkhTSHnm%2BShW0qP%2BXN5W3sHNYmatl2YROpZStiYX%2BizW%2BQIZm9y2P%2BJCG6FOygT%2BL2jbVnC61SCGhqXIksblYyPO79HybXzXmemUpKtkWhd4vRrPs3M6pkMNI%2F99WOr68ExXf9wSoDspaSLarnE9KIoBti3uJwAGraP8BrrAChrYy4I&X-Amz-Signature=b09d33a69b9d9a22266fa65df9c68b9b1d9da97af31cf9bb35e3466421f6259d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLWH3TFG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxvnLa3AgE9f5AGluBcqqDkr8%2FDOqOXwHfvT3xPMtp3QIhAOzstUa1JIKaC7ZyuJkRIBFXgJ1rfu%2BSiHSwhiUqwdd9KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyHfkKU2RK0LgOAxzkq3AP9F0rUxW0NX2X2Vlfl%2FtHJ%2FRtBgwxxTfqcSodCpUgOt2%2BQ741s%2FelRWFEiYsK67vrA1Ue5pUdW1WfkMP1GoWhhDmn%2F8sq3BWF9Fg5jvkLSoiesdOASJ8jgSc0gNkDq9paZDWlW9VYbAln0dVs8wbQSE0d2W1a0sLeRI7OIhdnDthG4qDZwzouofQy8CtiijiWJjh0o4LO83StpqI7q2S8D%2BKKkB5SzolvkUVIU4bLcWfRaLl3DA0HQ7WnXSWZgJROxAxW35mPiYQHGhqbuDhmsNC3jWlVNRTiee%2FI%2FZDBfrJroEw%2Fqyt%2FxlPg0Yk1rK4ZxvscDwTcpFRdNscK6WO0pIrd8pKjiwg0jTS06TsjhZlW98RkFDhladpFRe1jgnp5VytsEd4lP0h50Qb7eD9Ecgh1veG16BFWDP0ZZZ46sRLAahq05F%2B%2B7R2PPk2LyNuZb9uHhBP1CLtaQRbdynp8%2F901vCkJPmTDfa22L%2BgZnQtbkhDCU7YGWIPrd3eF7j%2FJnqCMTKrqT2nNjhFBjjMTRrIG%2BUhFGJpKLdcz8%2B43ioKw9ojrXlKr0li6kxlWL8hrh1Y4cSI5IhKlXREn4%2BRCMV9KbOEbC8YQ1g8Z%2FQ4b5cMAj4mJMWJ5My%2BvZJjCjnPy8BjqkATlcnJVdCIwmC%2BPJnMESpSOBA%2FKkcNchtyN%2ByOU7oDWx7Spn5v2M0Wl5pnoxSpdJSxcEXJ0RTvsmswo3DLyrXxwqjLko00rUkhaA7XN4SW%2B%2FvGtxWYzbjZD%2F7DZQSjYAK64xS5d9n5lVERekwR9122rlqEv%2Fw6fHgNFCPsKJEnmKmJ%2B6j7JILMxpr0K%2FePgkaQmVi%2FuQr8mxrmG2aOLiONf6A1Sl&X-Amz-Signature=c68f6c56d5d7c45c93d0c5987d3538f5e636ab94edea718e8b7c9a5cd8d4b179&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDJKBSPN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGhpbH9V2tbTTaxkTkH2Y9PrSjCwd0b3HSPl4q0Cz42kAiEA0n5i%2Fl6gTLXXA0Zvxb3pdK8s8NyAwb1juh21iOvJum0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPti7FHzU1gnLk5JsCrcA5gEmUtK3Ci4GCHBunn2Zuw2pgtmdEBmMf1%2FtkhJXuB3OJXyBlRCnlPNoNDODJesabtJxBeB9nGGBd5o7VEm1VZImKaeLNIiskCJnsfLniMaZfY%2BaH3OEdlSMUaETjLcpdD49wb2EReon5ZGn3gzni%2F%2FUUZCo1YEHp6pc4eG63F4F4plupLkbVYjOJoYITOyd8ozafKeO%2Fym2mH17jY5miCGILjMkSS6aWFeSwHQKM74j6f6aE4OFIogzXwA9w5LqD%2BXQNrlv%2FDbaA6xGdrDjngAtYFvT6NLHZay97qjspYeOLfpY0VY54l6NOYaTGjsMbSpabIu1NOt%2FURZfACw6%2BcaikhkJlNjE10wchw06%2B1h4TK8%2FhGiDyMWyymn9tJXdpNLJKvgG4YussVZeSSZmdMGwe88%2F7VmjQQosYwW129oYVgk6OECUp%2BXYN6SRw%2Bf%2FgXh6iQChUN5zHXldwc6MM7XIE9tkZeCvxkAswUMuLLKudI3TjhpB45z%2F%2B7fMsiJ97ZU4St4UKOTbIbTeXrgJ8hgR1B%2BsbcQ%2BhV4AOp4VfdMlKTgMCfDLI4POLLgaGY%2B01M5H1ciRXMtvCrBqQMOqMpZAwGtAM729o9wr3xL3qdl7%2FkqWnNJLzlFLpWFMOWb%2FLwGOqUBOqPyz420qfLyrjkh14nVWJvHN7jVH2LIdC5%2F8KLlqwcE3iQ03FZm6t4nvd1RowXZkyMsLUjFlYmU5mRyf3KS62gcJhIpTlAVsbrcVkqnzttbqxRTmNWV2atbdc8hx8SJR8Ipq3PDDm25J%2F%2FrFp9TyQqy9KvuQufs8QrhFZWCUEoxy5vpDH6BDINxO%2F6O2WdOmIILtY6YAbjULxbh1QwkOWkdCDJ8&X-Amz-Signature=9faecf04178f62ee8a232921216a3268ef72f390e5fcf28f6f286f553f3a2558&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627OONTHR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAJc4jBhSKTffH%2FKmxapjhiGfM2HvfKH4kWQ77UXYw2OAiB7o7tcUJ9KCDL6GezOJYbWOzf7PU%2BS2HdW0PJApZLmyyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVFx5fKVbDuSvAZgwKtwD2besunXv75d9bvogg9rOgOJ8wO49MNY77Hwm0ldUhnz4Rm6gqHQkx9kogGKVi%2FR5MBEe0xYPfeifKL198sYLe%2BczI3Engtbh0lFxb5mqukasOVbBVJxNzCrFj6KgxIymW7%2B1qyeGli%2FRN1Q8lWM6ZFJlBAsKD3c7lA26rJKa7Cbsut69La6ua4eho0DsITMLSyfKiXLx%2BKsSTEMJKk4s1qqq2edmaOGAYGOIdZHIl7d3KdQcmHAzhYeb1xlamEXT8Q9eUTdhGS5vNtbROO7i44WOgeO56Le7NydIkFrk2uLbQh1Bq97ZIUMoP38Zms8i6qJ0na6vwqTe9%2FHzQh97aTGqPWeWo32RZ9tQVAI6Jukt8ODXokSwVBLDZpH7mHcbeNoEiGsMPc3lArGQi7uaDKlW6FtToQ9cDWti0hWBHHxfO3v8Eh0yha7KZh88RCvx1IthuYjwnP0M%2Fh8sUx0p8SYVynjfK1NqyWwtQWD5klFMkwgAudVOeOz5xOfCLTlEjYHP6y3%2FSkOFvwx334xE2W4gzXSQgu5Xn64Dos%2BEZhvElCApsDhFs2PiFFwW9738T93kKExMClrUH3ElMMQfi33l4rmLOEBgfOIYGtdPqvvpOP8F52Ag52aO%2BGUw2Zv8vAY6pgGntZC8%2FzaEBmtSO8oFxvnUwijrCNKbmqbL6dQtCaj6FSZ4pPMNdhJRumuvg4NBabFlhTruk16Ho4Bge63yley78Tf37H0QcikkQAfdkm%2FRzmxs5ghgmtAx3s0MS51RbI441WnKgPSQ4nhMU1MrhhUPHE1ex5wjZeAXARg%2BlI3grcqeVuCcBXPtmeA2zTBnj1IV%2FNHgcn7gOet53qA0X8l9jo8ZidmD&X-Amz-Signature=994c8c68443588a6dd828a3cd2c776df8bd0d973e1e60b65b1a796e60ff32187&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YT23Z3S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp1FavYPYlhbTrrWdfl919w%2BMWueissP%2FKPmJawjhCcAiEAsy30POTsm6iwEK3AYtBcJFWnwOBySK%2FmBn4eaizGce8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGIzCio8PSKrLr%2BZCrcAzqiKSnfYQsm%2FQaFQzy%2F9Npw7zbBLoRtz%2F6x4EWkn%2BWywHqrPmTtomXo5Xj5aLlJXwRl5JqMhOU463uvdflqLHdZEXe1dBYcsySVOYUw9O0oaMErtkQZPFWUDeT%2BBusKgRySquPRRSwBGC4Fu47ds8pvInwAyCpihpye%2BxY0I0x3QG3Fh3N%2BvMMiOgUP6HcaACpBZ11g0cOJaNGif3nCUek41ycUpKgiA%2FEo81q2Da4oSbfA9zkEuIl9eHckWKF1Dt07FmhGoKlUSYlW%2F7FgHsnGKIr6kyd0N7gTdqj5%2BWQ%2F0OE8liKPNzRaicMmHdm2ezOkple3wpOlXe2tIYCK6kwwpRW2Qln8TOwjL2K5WQhsxCzgrS%2BwIxq7C9pVJg9r0x8cMW%2BkpeF0AVCCeZzs%2FQ70uOuOGAHzez7T%2B6fo0JJJd0wclPdP1FLO7JnE%2FMpnXtB7ebLybniHWIXawJqMJHtVqVByuklx2SPixAcT%2FUOJzY%2BlI77yCvvqCLYOOD3pyvLiFg0BvSRA%2BGyZ9OV%2BThMPvB07HPvZLCiRzI8E7Y5SjulFc6J5wLULTBw4d3tlUHvhHVw6Y7%2FDKZvr7IbjpamncR4oiZn183zB1EbAyE%2Fe9pPLT8ZPuIG3SGgkMKOc%2FLwGOqUB0SUcSBNypQyV2Z6QFZONoF0uan81eOB7ljEi0agPkSr8Mi%2BVuQ%2F%2F10VKjo%2BJPCiUBXe9Bc4rRHNpGmMa4ibUvkDQ3xo09yV3QXd993w0pDNkvnWkDC47xN2w%2FfTHKiX5hJeljexPxrtuIccOhBldmdVJGjEyoZLlhnoLX7v7LIHvgvJGrcF8u5jCVOy%2Fwz86gPoTne28buxYinARdvjh%2FZ8jzPOC&X-Amz-Signature=402b3a9f8307f98a1ef1f8da889ba78b7b39d7a8fb8514e4b9578e61c1c9bdd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YT23Z3S%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp1FavYPYlhbTrrWdfl919w%2BMWueissP%2FKPmJawjhCcAiEAsy30POTsm6iwEK3AYtBcJFWnwOBySK%2FmBn4eaizGce8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGIzCio8PSKrLr%2BZCrcAzqiKSnfYQsm%2FQaFQzy%2F9Npw7zbBLoRtz%2F6x4EWkn%2BWywHqrPmTtomXo5Xj5aLlJXwRl5JqMhOU463uvdflqLHdZEXe1dBYcsySVOYUw9O0oaMErtkQZPFWUDeT%2BBusKgRySquPRRSwBGC4Fu47ds8pvInwAyCpihpye%2BxY0I0x3QG3Fh3N%2BvMMiOgUP6HcaACpBZ11g0cOJaNGif3nCUek41ycUpKgiA%2FEo81q2Da4oSbfA9zkEuIl9eHckWKF1Dt07FmhGoKlUSYlW%2F7FgHsnGKIr6kyd0N7gTdqj5%2BWQ%2F0OE8liKPNzRaicMmHdm2ezOkple3wpOlXe2tIYCK6kwwpRW2Qln8TOwjL2K5WQhsxCzgrS%2BwIxq7C9pVJg9r0x8cMW%2BkpeF0AVCCeZzs%2FQ70uOuOGAHzez7T%2B6fo0JJJd0wclPdP1FLO7JnE%2FMpnXtB7ebLybniHWIXawJqMJHtVqVByuklx2SPixAcT%2FUOJzY%2BlI77yCvvqCLYOOD3pyvLiFg0BvSRA%2BGyZ9OV%2BThMPvB07HPvZLCiRzI8E7Y5SjulFc6J5wLULTBw4d3tlUHvhHVw6Y7%2FDKZvr7IbjpamncR4oiZn183zB1EbAyE%2Fe9pPLT8ZPuIG3SGgkMKOc%2FLwGOqUB0SUcSBNypQyV2Z6QFZONoF0uan81eOB7ljEi0agPkSr8Mi%2BVuQ%2F%2F10VKjo%2BJPCiUBXe9Bc4rRHNpGmMa4ibUvkDQ3xo09yV3QXd993w0pDNkvnWkDC47xN2w%2FfTHKiX5hJeljexPxrtuIccOhBldmdVJGjEyoZLlhnoLX7v7LIHvgvJGrcF8u5jCVOy%2Fwz86gPoTne28buxYinARdvjh%2FZ8jzPOC&X-Amz-Signature=b019c61f231449f5cd05756eb533d90f8b4fe9090bc12c3799bc89911b69cd71&X-Amz-SignedHeaders=host&x-id=GetObject)
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