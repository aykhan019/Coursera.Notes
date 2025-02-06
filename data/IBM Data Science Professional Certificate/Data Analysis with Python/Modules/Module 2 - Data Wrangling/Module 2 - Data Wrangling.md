

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JLACQRQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIA80d0GHbkfyX5YsPeVrXVwxCpIMoKWq%2BQfZng9kZkOOAiEAj15ucLHHSvDrpUHK4pdvXxYgfrrMBeyGTBf2yjSA1kEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDDkUT5Oj3HIdxwReOSrcA%2F9LaHUDx0nsy465iZJj3gUUVLfQ%2BXQaxxpDqDD0fSTWaxTxUhiQAowj24XQFD8WDHSqBdd0DNH6XbUwUeZ7KitI9Btkd9cTFXuVTfn7tKyBys9xF6emes2SOcY%2BVHtiJtt4ThaVLmAGUmAi0h84b%2B42%2B4pIZDejNl78ZPFXR2AtXqcjAcTC5Dn9ZhPqpNZr6y4bxdA1srEr44TgirPoUAF7%2BjMZPqPGN%2F15gt%2FxOete3TzlQC4chwBkved9uUtqILExy25M0sPrfWaSZN5C4WAvkZdOrYFLtwp5iEwB68rS%2BVpalmliGINMvJJ4S035fQUqkT0dVROJaBwYNjDiM%2FTTqal7ubb5%2BbrjCk%2BoxhSdc7vdechNYlnAEFRyZcH8usuU3%2BP5Wog6IK9qhuXzHCG22Odk13xPe97x9OwytMgKaqkkWc4dmeCWN9R6mtsMoy%2BCXVZ8wrDb8QJJXHyvgGA6eyS65YPqTQO6v1otbhy3UI0EvFAjs8oFlsDFv6neoC6KmlL4gPKSR%2F5OANTJIrU%2B%2BIkYoh%2FJIsmqKdDnBr1%2BJ%2B61PDqVsSFppZLnOJ%2F7piZf08GYLWeKB8S3N3hkUUOgHukaznr1SMuYv69Yzwg%2FYeMH%2FsRm5UV9S4dcMLO4lL0GOqUBJGmlYjJUa%2BU3XFA0JLMsgHvDwYp8xx0INeGyZaohwVBmQbd0EnsePLY%2FS%2B%2B1UGKc%2Fg9YwfJGoYTb2%2BvSzxcxDTEqbycczmYYhomU6wZSh5ExD5KU%2B99KquhgMHu5dt9shQjXupLpKOQZ%2FKkmLWQJ0oJm5pZR0j9I3Sdmr1onRVaVPjC49odcL7l5DmoDcBe2KL3KdkHP1Y41AuuHK6u6Ag4fXE5i&X-Amz-Signature=23bb7993665c049183edc645cf47ff7689ad48ab123eb051568ead3b2393590d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UXH3MCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIFLisQUbbeK%2BNRgJJDHP86KNkqBpB5gIEOWJCJHOLY7dAiEAnT9aQ%2B0fCPiU9DiE0vLJgfLZ%2BuJR1pznZqnYogEtUIIq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGfaOTPNOWuXKftxNCrcA9IKMk8W6pcMBLhLJfSYPxjhH7BcJ%2FebY2vCO3fModhn6K2CpDjGgRZhgHXIs5%2B5lqsVQ%2FDdM5YIL3P3QWsdksUg7Lsswg7%2FfGGjQ2yVIujV4Ba9efUsta77VXOHHEPtuIBXF7VInyrnUkQFBguX2yFIZkWnmQuC7FO8ypSJpaStKrdRuD5uZENT2SzxnMoGyBsJx1VB70KQdi%2BDYTq97lt%2F8mYEzyyZCwqCZCtbkKernihI7ayqyRhIvayJ6i7MpFGE9tYzvWOd3QCM1ucbMdvD78xK1hlilmMdPtaZavaCNsMk7j%2BUdJBYdB%2BHf8kAkr6IMfbqmDI7eDZCvFb6QJ6rA0F5D5VEQjpBBginjp8wEDspNLOeKz9ZcE1IlVPQQhUpGzs4KO48K6%2Fm9o4bCswut16HgjJyHWWBTEYdwFfrw2nbk%2BZeCWYBIQiAIeZAI4j5K2dQX%2FVAk91c%2BSCwTMwC1qURRpvAIatFdBDpsOF1bpdXrDbYejcgmMcSBQmYVeRUTxEPfPOL2bE38DU2dL98Y0FuKeMeSGk9wUNo%2F82bXyn0J%2BXrWEdT1J12z6rX8TKqMYCmdc524uTuR%2Bi3XEa%2BZ4I76F7fOGuQDrczxElNTkS2Atd31UN%2BmlMCMOG3lL0GOqUBfIiMTpXhv3Q%2FoiMPEc6JrXHrKg5APQRbus3aSYlLI14aaSgzZ3aSdvvDCQ1rb%2FmfLhTQxzs0b0pL1FFewvOkn9VtflZWy7%2FdcmgcxFw49Dw%2BdV47%2Fp3yngThx3VSXovdj8H9Rp1z%2FcRWyhnsPt9aRx%2Fewv%2FqtfmIA%2BS48tPh0l7yhjmytlVNZOOLlouDpqfL5XB0YiytW3%2F6Ocx3bDnVYAQ26dJc&X-Amz-Signature=b875ed89ca5ace46df452022942812e542d8108b8b7e49243c03b59a0711ef7f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2IBGKND%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCDKdntJMYuJBU9t9MpMPS1hNxtDqLpzYxE5sRd5ZfCOwIgJ8syisa7PmgkYcz%2FDXAfbCb8IU%2BD0ditnAwqsKGnnbAq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDD%2B1Nc41Uwrqa7j73CrcAymJQCzAjKwF1AMVZCBS76Ea1kmfsRtYM6W90YXICFxDqxDdw8ajvg1ofwuCQ0uW5lK4ojbw%2Fq9uEMqzTh0P7BGuh4qlbTCQn%2FObtdytqREczWZl07Ta1dFWuQVY%2FJwI5eL5MQUVpDVNpGNfbio2q4gAywI%2BP2ccN7tuY8VEnOhJVLm9KqEmKt77mE2e7RES7jIWqK4nFzwaXp73KMdj5rbSMSDY52gVzBBMLgObABQMBtZRDJtFEVo1n5eWS%2FzhGVE7cC6HRyZmlqCBwVvGo14GMEJmaKO3Pvji4BijcpNu71dfyS%2FPF7%2Bsos9FBiabFc3iw9%2BJYc27NScYSiKfe4ABiT1ubZZGa5T42x0u3oQdA9haKU8WFuXWcrk0zaxz3QteE%2Fx7Yqj39%2FVs6b%2FOKAeXiJ5QRzOh0EydNFFFTmo1Gu8acopc8kFyWQQcMye6WPX3VRu8a085xFJnHpld2neaFSqbz%2BW%2FSqViDD4pCxeaYN953KQcP10GFDjUDsNdydMeTmNwIog0aU3Oy9t%2BWWffQKJ8nn46mMNQ5B6iGlhqnbSTsEnmHS7cA8eT7faC92%2BEoa3tg5Rld7%2FhvzcB63d7AD35qsjQZABmhCu8kOoqB3bv6ox9uLpJ5rT0MO63lL0GOqUBdLZDnP9bGNiXHgwT01Al8TL1PBNiOMfKU1L68InIwSAwaqjvcTJQbpLRdF0kzqPe7RBAboj%2ByAI8FYO2C%2BQpMvndBHkQi65tqabKjk6FjRw298w87f%2BmCWXQYPzc6pOMdvHC4Vsq0NWNJbCjPaYBy0RbdUDDxW59Q1pIl9ClxtwDzgHfl3WEK7LpiDf0SYCSnNW5WYppGF1gs%2BegV0spuU%2FoYThH&X-Amz-Signature=3b1fd06bce451dc128688d3e8a8219d1d2fad8a432406c227a4eb984bccaca4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7BWYKRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDMw58toZSqXUgt2KywEMHOHXgWtO3EHD2s9GgKossDAAIgcy5rOWdnoEHuFRgLg%2B2edG7jxKaUOmg5IAxHAZtUc2Eq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDFcuFaGV%2FWxKt0bu2CrcAzWwrclyHafRTCmfG1INMTCU7LnYH8PdE8VV3yb0cnRbSt05Z04%2FsBalVMJLVVjoMp1JDWDJ1flUvOKYzh8w5LlsSehqtSw7zMclvOR7wkfZmAD1CeVRIftuA3aqJCMe1nZOF0Ls1iRedJFWSTIvdUOEE0OlFxvOXtPl5Ke2RKr%2FedLYUc8l8wMlBhBfCFTzOV326wihhjQRoXbASxqXofaU6MPwcMMrFz1suMd4u662rAPfNL22kPqcTaLYos0rrvf4QKLbk6GWGfLHhWLTKvyJq%2Bh4MX5DkIx%2FmxZ9tr%2FfLqKEAsN3QvZTkrq0k%2B1bRnoy6%2F4dXRy8p1Zco8HmeJEIapUPppQdorUgsI3A46qZuYfmNk0BWaheEE5aYgtvVmzj3epzNBIcV9yhuH3mSDNkGIzK2Gv0%2BAyBqTwOHFnlbjpsBaNp4jD3sx1HUs6dEb0lAdrCLbr4yFKCAv%2FtOTIBEq5CSfUjqswESabAz8JgkIDV2P1vffhdXyWyg9IH7KMQtOW1L3hJUy8jG4ajh1UnmAQ35vR%2FNAooBaLlYfUjvR8aBywAa6QjGlpOY8EnfzohnKswontYPNrZyGcBaskZ5BWC9feAiFJUGjpRFGpatj2sP67ZJqDQsGYoMJG5lL0GOqUBdtBYaw59gffj0KJp%2FjNThnQxzUFQoEHBPwAIDT%2BaoLXB38fMKV2JSBG0qHeshxm7CBY0shTZe%2BpYpicCZm04pFpZVQrJa4H8gm%2Fm57e7hfWUQ%2F9rxuSbYlBRO7fYV2v8TlgctwRyb5W0EUY5BNCnoNWxrmxKhiY4QgvVEXB0aXfVE5HjfgbL0HIDSM6TecS4CR3%2BBO3px5UX3yq%2B55DC1BzsZ%2Fz8&X-Amz-Signature=9b75dd5c875189a24d30e5e3da161578187fd7a7aeae39f282263f876b3922c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGFGQ72Y%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDBG2axOvw9P0ukjQBFWP8q4D9PKW5bwmNEqlLg6%2FlDnQIhAJNxKggzqM%2BLPTrk9IszpboPD3M2Crw6LP2%2FTXcCswynKv8DCGYQABoMNjM3NDIzMTgzODA1IgxaLemVdAvHVA99Ke4q3AO%2F3Z9fUVBPWHtZL2I3mUjgXWA7DfNmJvLwakksmaoAcT36ueUsX%2FGlr%2BY5wh3JTJwGUVzISq9F7KGwDTAJNrGknv5vJg3hX0CPRX2izX8pnvXrVIMiwCR%2B8aDEtRrEYMGDFmTqXMR2ZUGKI43v%2FgK7O%2FfZTHwl2gX6nko5ZKMeTeJBOJ5GrVh3WUY2Iikq153Opy7wvaKNsXbRcDqBDFr1OaSNQNmNu8NDPMez8xxm8kdTlf%2BPNqgqwlUq0XM4acXm27jzB23iZk56tRcUzKMP7I95nAybCphp%2FyIOpLLr1xlJRvM7dJdMSHjVsVRMyTNJNNniXCJtVvzp975OaV1yITwvgWGq3uArCbNJkd8pGCHUdslEvOHVf%2FPXvgiZrMu1hef7CDZOae5TFJOXtZExFv7YwCOQHpFBAhK33cDy1Vy3Rab3IjIS8hGlb%2FJ95k1UK9osPVIoWx%2BUgAdd5KAGxJBC161EGZ7wE6Vv%2FIoAzUPZnOiIx6bbAGrEuzSlv7s9gy0mFyNk4JOnlTDqu1tmxaIJQalvKlk0XkAbklYsW9llqKEW09fJ7yjbEpDthoRD%2BPhGZ6bBpZpfdY68ES005cduy9TEsD0b3tDyJbhEVrv9SDtY16JSIK3EVjCauJS9BjqkAUy8AILs0bFZRG1YJLnQGdWcYY6qzPjw9msMhXV2jVb1mqA8szUEAUcXt7UJJImWwMMbHuT8wFyxyRVhe4MFZJnjMmoCCBYBCaRplzm5ctZdU8Q%2B%2Fdaoxey8eBJWwwfwfWxUrBebg%2BvHBYtHQv1%2FlMAbV4RQMBnPAWEcRlA8edcjLrArqf0J5%2BLCbkW3BWzpRBjY%2BSLS9gmEwJXHzJ35a0UVVXxz&X-Amz-Signature=c4cb77cfe7554efb80334831af3abe2b8baa041ed92064778983aca5fe52add5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHAANBOB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIBHtuIUd0YRDGtNBZnUtTbA9%2Fd5lSJTeTM5oL1G27%2BBlAiEA%2F0R9TJdpEa1DYgcYcdabHhEAOugaFkQhlDueorqoX74q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHhH4Ibfm%2BYOrEv2TSrcA%2FkpHua%2B5gcrUZIBT5j71T77gjFCjOrq%2F5Ej%2F38jVeaqT637An9DCgD5iKvMYD32lMrg0QuDqPvsFlrAiEk4y9yfIYNji774AKuJGHLkNzBD3OmrnQwZzqr4otgrf2RHSvcxO9u%2FprmfVaFmSY14PuOU1u%2FnIUek6GDb6kdq%2FBbiUq02O5nvQhooOGde1GSMOmMBqieNWmwhYl8hh3xPEU31Wkj82g4BQl22cmByMRuSXKnyLun8158fC62vxoPnMwJGpnxuqx%2BqFa5ostbRzlwcDnsVgYMNrnsyFTGbgmdfEpSHCzsfBlefs3mm7Kh7P%2BzSJrbdoeOmgKlyxFmXJnLr4GAEW0U71gu1GbLiaA9%2BfDVE9A2IZwe4Bem2NniyIbVGbUZ9Fu8XBYikUcvJHaCDPjAAp4iKFSsN7nY77j6KhK7M7bTD21G%2FmHCL9QPoY%2BGWn4iP3nkfFjbsa5%2Bper6gaqPlprvEYFJU18JlmT6fo3N7cbBOSjo10TPMIY3gEv5bPqJirrKFARZCh0Tj51PB5fMGCnWKwTf4U%2BltZUUIP4pRPFmGcDftzHYSC0qXx3ff44oQCEw5DyUWnsR2uFor52NnfI6nkvvVv7krI5ElWJ7uqh2%2FDTn7sn1YMI24lL0GOqUBDSKiAXHeXBI5jU65ob19OHFvFzSJsJ46phERWILfM6T8Ghm99XuMQhDTz%2FwMIGLnJSegHfTv3SqWOpuTE8rtmPKRxMzndZp3we5%2F1aCB%2Bfogs64KpsTIwP9cZgeSnK06u6ZoN1AQnLXLCOmo%2BaVl4Ztz7%2B7ci%2BUNlSW%2BRUhOVMjfr5hULSWrwZje8fdZYMiwYoAC9tTOyg5LUSr%2FLF%2BBT6ol4Bvu&X-Amz-Signature=6b977c1abea8ce57496a71dafaf6226e7adf61db85dd114c1e6c549680e006d0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB37CBCU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDlxgXSsJZWWQXmIrqlFNW2m%2FcYs1gQzk8ly3N6jTvs5QIgTIrJzX0F2pRV4m355mSiD3rU4%2FBDqpA%2BZPTFDF2eaMwq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDFZd9N0l2vC%2BNKfqByrcA2tHBtFlKy3oqxDOjfD0CiyUKbqEfTg7%2FenDzcJZJvC%2BwvRBA%2FMRgKF%2FCkpMmA7MnBmucnUgqdYgxqPZyqehqdY5w%2BHg%2FvfwHZ64BcWCGTUtr2YMaRMiyuwRKOCvSG56cu9ohcIH6bq%2FeVrMZ1JDYOFbj3RdjVeIalbT8AAQsbbcKHs0GDpqLwNaByWtxShRFkZMfiOGFVunfbZ6S7zZQd9ZA1ExQ3dCwKEF9kE4bUxH8yv5zatXud5p6bVVXNjNTMjMWOlHCFXZ8zjwhe0ZD9eYKrxQWp01WCAVt4RmAsZSAjn%2FciyySmnNLCCAGXiKQ%2BNsVwSbWD1STVK%2FsH%2Fy5TIPxxB4fAI%2Bf3PQS6txgOhdAYnTifCwurawMwCR5X%2Bp6sCx5AwKjtaptMVYLJHJprSz1n4EMV7CGE4%2BElt6AYc1C6%2BKyYP9A9lo4oww7Z9ugRmWkxjtLjnrkmTJKdxIiqj8T6U6hPnGwqSxDJ7odm2V4wX9cmALaI5nTAAUv3HepcBItc6c3k8iCZ0QZmKp2kJKUGKkyo65Wynn7pCGAoejbshRtT1Gn8YQHKHIwUKlPk5901%2B1O%2BmrOCFD8zV179muse2ehM04wRbmxDUoU9MWhTc4E6ZS0umqpaiHMMC4lL0GOqUBCBS520og7oNhnh3FozI2AbsjtGCWeosLEDix3ED17u3P1OjaObFMxxppFHKf3mok5TkCOCnr5Tmiz3e%2FPwRM2a2M26re6m2VU6ak%2FrO2ssZj9IpZceZzPAcdXFXzJEmOf1pD1WbaxJQmMPx8CJuOROU990hwvGxCQve9JPKPug9C%2FA4nOPG9BPttSpmUaJBynaR5t8TnnlMFTG%2BHLRC6FSk142rP&X-Amz-Signature=6c8248893525fb9802281e66b250e3f3bec841c0426eb35cfe974a8635fe7e1b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GXBH23L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQD5Lbn2P2CqrSDgoOFiLLdMXb5D%2B%2BdkeDETxWa9HxaBhgIhALPYL80BifTN670CaeCRc2cRWqoHElDqezpeqd1Bo4qbKv8DCGYQABoMNjM3NDIzMTgzODA1IgyqPeyT%2BbmzcrGW1HQq3AMidJ2prFobNhehuCw55bKl2lEQol%2BvTqdZ4TPbKfCBfXjgGqAzBSc02BfucTK%2B0L77D%2FLolEYTbzUxso8U14xMGz8LJOhXNhUQ6cK2rH2hHGeAcWATVdkGeu313WgB33W4Q0DtE%2B1fYTKjUEO1jgrWL839i%2Bnt34S1Oqx10fd%2FiOPoN8pW7zT3Qq7SEbLhL%2Bz3BNmUgM86rcQyVvRT%2FDjxrt%2Fg30b2nS2wp19vdxSzVcbjigtGFN7WaLjjWFqj9TrXQ6yy%2Fpc2ec1igIs75VnSfEcXWntmnu7J2gYWM%2FlgfjiNxVx50HrbX1qtq2mBrhKY8XSyyaxpQutxIfn26SyPp406aMP5yobCJ8eGhcDWztgHa08TYI4D%2BvrCBWrY%2F9KHia3tBjH%2B%2Bgn0BHkYC0sjX2zio01FciQvweyWbt937roK3MEjgNpvVR%2BsKH7%2BSWwCqHkU6daVm7jxEWIDag%2F1dzfL5505%2FcfmInuZzaYdbL14194Kq8klP6NgQBYXngkkJErLAHA8Pp1jUz7UC%2Fq3gduyJCM3rD7JVb9oquIWAu2BUGgeYeTqYj%2FNE6R22%2BNkcCwlOrRJLK9uCiPbFiI%2F3mfMGmNa2rxjWAM9r%2FyAPqdg7tp%2Biq8wZiYwczDjt5S9BjqkAb9yENShfxxW8e5UzlxGy9ENbC7if1aakdNQ%2BLi3YQyDGEJr%2Fxye5xRwObr14GbUStQGGoD38QPTJo4865W2hXEQKP94UMoJmYfsuLUSTGA3qFzcLVXzhLjFqWl30evE3310Z55%2Be0wZFnQEr9sbF%2BN9rRsCoqpHKmPWThnw5Uwgh1yNXEIAjax855e9rQyZ%2F8ShXOly6CnA3aHzv3ya3HHbs1qt&X-Amz-Signature=6f708c34ba24fc9728039de50f772a499feecb6687554ec05c61eab7db2849f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGFGQ72Y%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDBG2axOvw9P0ukjQBFWP8q4D9PKW5bwmNEqlLg6%2FlDnQIhAJNxKggzqM%2BLPTrk9IszpboPD3M2Crw6LP2%2FTXcCswynKv8DCGYQABoMNjM3NDIzMTgzODA1IgxaLemVdAvHVA99Ke4q3AO%2F3Z9fUVBPWHtZL2I3mUjgXWA7DfNmJvLwakksmaoAcT36ueUsX%2FGlr%2BY5wh3JTJwGUVzISq9F7KGwDTAJNrGknv5vJg3hX0CPRX2izX8pnvXrVIMiwCR%2B8aDEtRrEYMGDFmTqXMR2ZUGKI43v%2FgK7O%2FfZTHwl2gX6nko5ZKMeTeJBOJ5GrVh3WUY2Iikq153Opy7wvaKNsXbRcDqBDFr1OaSNQNmNu8NDPMez8xxm8kdTlf%2BPNqgqwlUq0XM4acXm27jzB23iZk56tRcUzKMP7I95nAybCphp%2FyIOpLLr1xlJRvM7dJdMSHjVsVRMyTNJNNniXCJtVvzp975OaV1yITwvgWGq3uArCbNJkd8pGCHUdslEvOHVf%2FPXvgiZrMu1hef7CDZOae5TFJOXtZExFv7YwCOQHpFBAhK33cDy1Vy3Rab3IjIS8hGlb%2FJ95k1UK9osPVIoWx%2BUgAdd5KAGxJBC161EGZ7wE6Vv%2FIoAzUPZnOiIx6bbAGrEuzSlv7s9gy0mFyNk4JOnlTDqu1tmxaIJQalvKlk0XkAbklYsW9llqKEW09fJ7yjbEpDthoRD%2BPhGZ6bBpZpfdY68ES005cduy9TEsD0b3tDyJbhEVrv9SDtY16JSIK3EVjCauJS9BjqkAUy8AILs0bFZRG1YJLnQGdWcYY6qzPjw9msMhXV2jVb1mqA8szUEAUcXt7UJJImWwMMbHuT8wFyxyRVhe4MFZJnjMmoCCBYBCaRplzm5ctZdU8Q%2B%2Fdaoxey8eBJWwwfwfWxUrBebg%2BvHBYtHQv1%2FlMAbV4RQMBnPAWEcRlA8edcjLrArqf0J5%2BLCbkW3BWzpRBjY%2BSLS9gmEwJXHzJ35a0UVVXxz&X-Amz-Signature=d1df937538cfe94ead717863a8a57d9df3791fdf477f87fe584fcfe70534c75b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JLACQRQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIA80d0GHbkfyX5YsPeVrXVwxCpIMoKWq%2BQfZng9kZkOOAiEAj15ucLHHSvDrpUHK4pdvXxYgfrrMBeyGTBf2yjSA1kEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDDkUT5Oj3HIdxwReOSrcA%2F9LaHUDx0nsy465iZJj3gUUVLfQ%2BXQaxxpDqDD0fSTWaxTxUhiQAowj24XQFD8WDHSqBdd0DNH6XbUwUeZ7KitI9Btkd9cTFXuVTfn7tKyBys9xF6emes2SOcY%2BVHtiJtt4ThaVLmAGUmAi0h84b%2B42%2B4pIZDejNl78ZPFXR2AtXqcjAcTC5Dn9ZhPqpNZr6y4bxdA1srEr44TgirPoUAF7%2BjMZPqPGN%2F15gt%2FxOete3TzlQC4chwBkved9uUtqILExy25M0sPrfWaSZN5C4WAvkZdOrYFLtwp5iEwB68rS%2BVpalmliGINMvJJ4S035fQUqkT0dVROJaBwYNjDiM%2FTTqal7ubb5%2BbrjCk%2BoxhSdc7vdechNYlnAEFRyZcH8usuU3%2BP5Wog6IK9qhuXzHCG22Odk13xPe97x9OwytMgKaqkkWc4dmeCWN9R6mtsMoy%2BCXVZ8wrDb8QJJXHyvgGA6eyS65YPqTQO6v1otbhy3UI0EvFAjs8oFlsDFv6neoC6KmlL4gPKSR%2F5OANTJIrU%2B%2BIkYoh%2FJIsmqKdDnBr1%2BJ%2B61PDqVsSFppZLnOJ%2F7piZf08GYLWeKB8S3N3hkUUOgHukaznr1SMuYv69Yzwg%2FYeMH%2FsRm5UV9S4dcMLO4lL0GOqUBJGmlYjJUa%2BU3XFA0JLMsgHvDwYp8xx0INeGyZaohwVBmQbd0EnsePLY%2FS%2B%2B1UGKc%2Fg9YwfJGoYTb2%2BvSzxcxDTEqbycczmYYhomU6wZSh5ExD5KU%2B99KquhgMHu5dt9shQjXupLpKOQZ%2FKkmLWQJ0oJm5pZR0j9I3Sdmr1onRVaVPjC49odcL7l5DmoDcBe2KL3KdkHP1Y41AuuHK6u6Ag4fXE5i&X-Amz-Signature=2e3441d3a066f39e72c49ad9be15de2fb89fde52eefab1f5516501af96329d4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JLACQRQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIA80d0GHbkfyX5YsPeVrXVwxCpIMoKWq%2BQfZng9kZkOOAiEAj15ucLHHSvDrpUHK4pdvXxYgfrrMBeyGTBf2yjSA1kEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDDkUT5Oj3HIdxwReOSrcA%2F9LaHUDx0nsy465iZJj3gUUVLfQ%2BXQaxxpDqDD0fSTWaxTxUhiQAowj24XQFD8WDHSqBdd0DNH6XbUwUeZ7KitI9Btkd9cTFXuVTfn7tKyBys9xF6emes2SOcY%2BVHtiJtt4ThaVLmAGUmAi0h84b%2B42%2B4pIZDejNl78ZPFXR2AtXqcjAcTC5Dn9ZhPqpNZr6y4bxdA1srEr44TgirPoUAF7%2BjMZPqPGN%2F15gt%2FxOete3TzlQC4chwBkved9uUtqILExy25M0sPrfWaSZN5C4WAvkZdOrYFLtwp5iEwB68rS%2BVpalmliGINMvJJ4S035fQUqkT0dVROJaBwYNjDiM%2FTTqal7ubb5%2BbrjCk%2BoxhSdc7vdechNYlnAEFRyZcH8usuU3%2BP5Wog6IK9qhuXzHCG22Odk13xPe97x9OwytMgKaqkkWc4dmeCWN9R6mtsMoy%2BCXVZ8wrDb8QJJXHyvgGA6eyS65YPqTQO6v1otbhy3UI0EvFAjs8oFlsDFv6neoC6KmlL4gPKSR%2F5OANTJIrU%2B%2BIkYoh%2FJIsmqKdDnBr1%2BJ%2B61PDqVsSFppZLnOJ%2F7piZf08GYLWeKB8S3N3hkUUOgHukaznr1SMuYv69Yzwg%2FYeMH%2FsRm5UV9S4dcMLO4lL0GOqUBJGmlYjJUa%2BU3XFA0JLMsgHvDwYp8xx0INeGyZaohwVBmQbd0EnsePLY%2FS%2B%2B1UGKc%2Fg9YwfJGoYTb2%2BvSzxcxDTEqbycczmYYhomU6wZSh5ExD5KU%2B99KquhgMHu5dt9shQjXupLpKOQZ%2FKkmLWQJ0oJm5pZR0j9I3Sdmr1onRVaVPjC49odcL7l5DmoDcBe2KL3KdkHP1Y41AuuHK6u6Ag4fXE5i&X-Amz-Signature=cbc481d7a872dd40f128a71a3961a05050994d7be52ec7de92253c97b27f5b83&X-Amz-SignedHeaders=host&x-id=GetObject)
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