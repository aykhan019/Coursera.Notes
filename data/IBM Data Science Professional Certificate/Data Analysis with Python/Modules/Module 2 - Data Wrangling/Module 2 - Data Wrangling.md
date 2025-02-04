

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYUCR3X4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDdzH4O4mUpaHDMHixfRudoTL1h5XUryoaquTy3%2BSgE%2FAiEAxPKriZFF9CGJQgEAQZoey2Ag2wst4Zury7KLBfrmejgq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDKTXVAUxek9ubeSp3CrcA%2FdL11xIweEG0sEKHnxOyAAFjMumHbazLUkwgFYtMQCwkcNFODMnDbnQjQSLJNqq5XvA2Asy7P31sI6fTW9h4iG0f%2FRSeqx2PZM%2Bl%2BTEhYLBEEQrzpCXVC7f%2FUoSQyKP2d22XHVQLuGnHFnQFoaM7tb6tGg3vI1dL4MCMjs2BMvFpWGtl7WeOWQLjHP8fp45aCAH9wYX%2FJbzfQpAMevgUxeKbymBtp9%2BO9SLW%2FBGYfauWM00qfAkCyYTKxa4ayuV%2BcnD%2F6G5rV%2Ba4TYzM5fLfef4f3P2eC6%2BNBaaLuzyr%2BNrSj3qoIBAV%2BD7l8%2FNfFPsS%2B%2BJSef%2FmCRSXq6yrRVK4lV9NIxY2T8ftWMq%2FK9bj%2FvKIXOdA8oFU%2B25X2QLAJV8xhw44ziP2tOA5f6yfBsGBCRNXfu2LX6SgXD1SPBEv83SRREQdekHvRriHrvBnybSVrGrg5J3i%2B%2BVbU1Ffh2w1ZXSEtqhk4Rf0W6vECsw9xg%2B6LNQF%2BdMT6oyND9EGd%2FXlTQgi%2FRuj12OH%2F%2By04Tu%2BUIAVtNTn9Wju6RDZQ1%2Br%2FHxNsHcI05kz9CzVONTbn%2BWM9hXiMzwlOLf%2Fro0Lc5gL1PaqQuGN88k1%2Fj6j6d9irDyhch4%2B2Z6MZ4O592xMOKgib0GOqUBSmIh0aJ%2FHZtFWA%2FJe31xE2M5547Hb5SHrOGh22jB8KrxYAsk1ugv83b%2BfNTayI0zmTLAuYmImzOeZH9TUDdTuimnwHak7QkwN9A%2F%2FECVd%2FVck8qdYSwA%2BzKxklQSArikZ7ls4Za5eQ99Z%2F%2BEQRnmYZw%2FBcyzIAqp6E2DpBngtHmZxq238AvnH0AF5unS8XbjAFWORpb2iCxrZ86Sc8YgNN%2B88Pid&X-Amz-Signature=420481ee8ee340861d54f6922af767ffaf418bd9536188c0529170e3afa659eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667O24KFI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQD2vWsqUf7FOYSpdfNaO8fjvo2KNXIZ6y3GHwYusa%2F2oAIhAN9kY0XiNCai9FAwqmjN6XG8hi4dVond%2BLhjsLzSNo8jKv8DCDMQABoMNjM3NDIzMTgzODA1IgxhyZTOukjTF9zN8%2Boq3AOUvFlCxInM3%2B4rQ07Uyh2%2FmdJD0Z7e9CTYm325LUFBhfZ1ywrXi0wh2%2Bpde9LMH0a5LHkFFTJxO51nDtBzQK00fLTzTet5i3Gi%2FwtfNbEg7bOeF6DkHWN6d2vwpRaCwLF73l%2B0wsd5BuYY1%2FSecuiATigY1x1H0RtM4znFZjHjcLA1xFZTNldm%2BI9trXVpaAeYtrkTpRSUcQsaIBUZddM1ctfP7tGGoeeqkk3fPzEbRHp2BL2d3zgOqrcHaHz9h%2FmZW%2Fcz%2FsWHh8%2FQ4Em5T72uzkFmD9Jksq5C9LjyxTMQAESIchQoRrNOXB2%2BaH0LqXxXOQGDdSzmwa5vJN5jiuDMSJ8F4SxdbJPgmo54LLIlNpbGw10yWPcnlgaR6NcURqObxB%2BzMlATXiDxYxv42X1fKtXhTSrKlawUnOebMFivW5fqqO8fiGluLJEwHPoxWYp7OZEAoztR6ThNeOwe0hg8LLRtVcYww3CzUIwvI6O2tynyV%2FyqXMNnoY36CmlKx2y%2Fu3hsGHhY1oWwwSsNV8C9ucYipYxLsrCS6%2F3Vndt1%2Fy31sOCO1cwR24FDrMjNmU00SNDprvTb5YiWWhXIEBZ2Zy9Rw4vBWSSbLtme6U3yYcxd4VM6tzgv9gxgGTDgoIm9BjqkAdigm9GgEwqVPtqZ5FTJLGUqhhp8MKMcTn8yLLOWu0HeohdPNTtd47uYVvReuZTNhpsgQ1usMWVFAJQyGaNLwM1bJ0cP7m3agcVfKy3zW3xzp%2B%2FPAAnb2%2BZFT6eQJHT%2F6RZrxgmjLftbFdueSsukRoj%2FAVA%2FTeDP9ES8MzhH7eXr6w3tECyGSujrVSwqcdNA8uR88di35MzLsXAKgX7lR9BzUQYF&X-Amz-Signature=c8fb01aaafc9602bb3f6e63ed1a44ce18ff99ffab255a6c671a3b0b51dacc3bb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOCUBKVV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIGC7M6suoyZLRH2kQ%2FIcpsZ2GXtvNTmKZ4hwFEZATpy9AiEA9SGWnFYCTIHvJw9WMg3NMn%2F4NorTvPlO%2BHD9QuHiI78q%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDMPn45r7HH2evub4TSrcA0iyK%2BHdKRz64gLfZrFJLUx1tttbwoUh3ljpF9yF%2FOkyTmF97GrU1mxbPL8chTdFHP2wdu5itCV0UfodE2WxQHlz2Apbz4kckpIALtI0cqXwJ79xVqEOW2RYE2WOhI%2FRgMCoFo1iqXLzCcH4gVA%2BE5vjQkuZX31D%2FXSoGFp7LCmob8yRLzJzQCOLMklEqxJBUelOU2XA7Cuwxs5WdyFgzlC5x4hgx9BABuOWfxpDwCjziQkeQ7aDxTjWI49FETq27OR7Y4FbzYVsq9%2BC7FTzSakwj3T9ZpCHMXI1c7SbqBbNf9DcAoeUNDR3FcVMfDoDrjgU8iOY1NvSmymDcIukzKbyRBBfaID0d4gYHAKJJU9aUff%2BysJn%2Fm%2Bi%2FPmwhltWVktTaP4Sa5vvXXijXyAM1tEGgskcQlet14BrgecV2yLx0xcSN6zp%2BavYK4hMEVYEs9P%2BINTE4a8xuv0EM5ZinFn6mLKOLpEB5YA4rXp3UAxZefdzd6qeyIHFOc5e2nvOKJMJnVFFqbGVVmugcYKuoRkVmWGS8PMaT3du5X6rTmn2bUycCVss%2F4pyLFayIiULct1dlRSt6BqiUnvTDljVBOdKgfUeKJzPvfAcQF%2Bk83l74IqSX8AGBgk7ND7EMKShib0GOqUBd2ztvLWDdKjyt5lHyzC1QnLd0k1Rm0DNN7UlomNiaTNKzFPbpirDOjV0X7UAwU164hBz%2Biy6GC1AiU6oBD%2FycY20h2gKJ%2FsML%2Bxm6xnd9JrZgJ6iT6m%2Bv9xC4QZR0T793lRS5t3jYeNJnwNaCRaLhgEpaGuiENafk7FlOGO%2BRdMTe1wTNZHffiDPNFf3J5mprZ0Agvf4Zc9%2FfSV42FPhCjdbGmjn&X-Amz-Signature=59e654e84f46eb546a378427dedc891b2dd7d5957fe86a9939b25a174a63cc28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6NGDHCP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQCLSyRhfu%2B0dNMhGEHIPdGG4MGJ4%2FCTJUGmyHzuQIVZ5wIhAPEi9aGAdL9W5XfoLyeD7l0G8irCqHOrFqYg12RvjqjOKv8DCDMQABoMNjM3NDIzMTgzODA1Igw5dI6Aup9o5KLdWjIq3ANkgfU8UYzs0yuV8cflrhOg%2FU8c77mj%2ByC72l8G72DokLvCyk8tQgaU4HETMsJIqrWbWhh6zUmr5cjK5molU%2FBgU%2FxsPNIOG%2BDt%2BRBoROuglt1xbLGA798jMhqpkteCKFQYjU8PEMrnstgFxyH7N60cAzJCb%2BwIJk%2Bbgk1S1XddBxY9qtGCLGliNl59TiUrcKGqY4uDY2LnL2uOrLeMGitnjKMiYgKbhrOTAUsfcDtkdjnHfyI%2BwKiUeOrWOMtTf4oR20qQoPWZawIhnhVko93ReXJLsYEOp2x2SsjsVvQVW3zgofeUFGrvvT66sgAn%2BpM7y43%2FptYhtGnJZRbmemKoIOpexxqera7y90BygAODB%2FCLcCQMcByl1PCZX6NNks3bAFbHALNYneNVr8VIueVXaTLKrCd%2BjIpdRdJ2iN%2FyFRgdGjdHwKrCi8XVwv71c1akcSyvUj%2F75nNFVJDfIjAdFJvQtEEqFNGk5rw%2BVImguYDzZ6qu9X%2BNhccvtyvNT70SYDZLH1CCYTs9i4UOXKsz83POrekWN6BZAOhq2dz%2FJzkNaM7EkoWMKD5VipvUvmV5Xnl1xQ93rvCatHXU30vgHBfnX4IcVe2BYCGp1r%2FXnCjkN46r2jGRjXyIhTDOoom9BjqkAZS%2Bdpdwe8DdcwhSzIMxCTza88%2FFlLEgtICm1gyjjrSx9iFM%2Bz4QgSzXETQ0dNNOlnUs79jzmMdSKW9ZxmTdD1r2%2BqNHEPUvqMTmywHwAdkbTOfVcvkY7mXYUXPF1hoS9xG2SOvHFis7fgZ3p%2FLGYECpAvgdtGzIxYCAS%2FxOrJSo4Zc%2FW1W9LF9erXfrLZuIgyfqe%2Buqa%2FjfiQSh%2F%2Fp1npkPo6Ly&X-Amz-Signature=974a100eea3a00091267dae1bb1725f87b30f357e027e95c8aae2a4b65b22a27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN443XWQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIAuWrjriUN1Fuo3P9fSpjh0NZKj5bRf0hTKUm%2BtOYaDBAiEA2BFCn2ByUNlOTSciJ9Juvso93pnu9sNX2qE7e2rLX2oq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDFtvR6a0%2B9usurgSjCrcA611oWpgdgBZS48cVBUptXYyprj5Ecjt7fTsD5tkl%2FpiRCdIWqBM0CBesRTanUvhjxrIottwsVYCZ5GY2rLeVhy%2BRbFm6TgfiPlbmP4KR5eIYqjCrM0KFxJzmBIhhBFCQzizMnCxq3nSuPrEnWBs2rG69Fv3WcLqryettC2NMRAaSZyOIlfMJKd7D2cmT%2BvCw1dLv5EitPlUBPcEEdkTVP%2FStZjVgerDPqrrPv9zj19Y8tVc697pSMbdjKrPkH2VmPa2LUSYndqbbMykywKvgBiL2K2doFxCm79BabQumTmU3yUOk8AuPMuYbQTjWVPkcdi%2FjUtCb66yjB4cDAzDR1bjOjbEtWXjkWdqSvO%2BeOKWvIEy%2BTQjWqj4gqsHPyLbgGtTF0H6B3ZvEmLAeoHkFQlMP1LDGcETe9CuqLam%2Bwjq9lvlmg7LGZQnD%2FUSi7AK6N3rR7CNBp3fNtToWy%2F%2B6wyqJSHcS7MyZaphQ6ZXF8SHQNVsp1kbPcYX2sx0yyiTrkvBjpfHyud4VnfkeOItVt79H0USFDV1tmWKsnNnuyuUXwmXk%2BxA4GWkol57GZaAiJ7XVpiBdTm07srz%2BpAxS%2FvipXWJNoKS4NnyjG2WUv7Nkm8DEYhpmHhrnFNnMIihib0GOqUBT83T%2BmYS%2BTeO3aIwMb1IbecLOoiKa0jKL1lAK5QY4Q4ipVD6fUYQxWpZYn2FSIwi%2FJOFoTmE%2Fa088WhnjKFuGis5Z6MnJjrG1mM7mrl7jb1ss0gON7XRLd6pJsknTxEwPLMMALbZ6h2rLJO4wxyb6LpH%2FF1dA2QXYgbHeZHaC4bHiVKh7tPRA4cOLnMOL7tEPC6mr6bSrOWxcvzQZyJZdqccc3lK&X-Amz-Signature=bef44557acd07f23ac6baae302a9846605c2bd9796bd4ef0df528dfc3c38a8f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUUHUAEH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIGOqECxJkCFrMhB5t%2BWso6CNRh4JnH5C2sTe6MQ0CwSSAiBm1BHdIAsQCgZCx6W%2FbNT9XyGqeW15gBK3zIS%2BzoSC%2Byr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIM2bpWiIdjUhVKmKlcKtwDPb7pgCslGzAi%2BqrJ9Rt3Z2zySOB2u%2FtnJz86Ml4JERmM%2BAizdH2ac2flMRhq2jx43x333LmZsCXlWUvm5cQF%2FWewmE4kXtAZgUhUdIb7zPueXMm%2B2WPIXG9goUHhj3RaJV72Y6GN6QD7ZCCvx6806ghx0QVg%2Bu8q8XyFSJpEjN29bN8K58tj19BtTIsCcVCc4BYZraAAej7S2ROOAxuIo3%2FINPmDUslcSAIy%2FK6wtZJQhTM09WHRCspBzuAVvVgWPUPpfj8bxyybcl3EFLDHV5PJg7kkT3a3IvARTTJ4oE0rRvvGmkyZxMaGyiVtYLwOf17VdwVnE0eQXR%2BECyfYNlOIq%2BhLbbc0V5Hec2J9KEWHu2WAKzpFF%2BsREoulj9M7wRimnSY99L%2FosTujdz%2B%2FuB%2FtM4w%2Fmy5XQrdgKczLri7a%2BaI5LtIye0AB24NqAesMpvppXy862NudwYTnXmRcoctXB2X7qkihfmfECYIS6G60vKsmIJXcXhv21N%2FD%2F2Apq35oQMZaqJlErP0pF1XlGWPK8W42BoiQ0la8hwZrwxrgeX5Br37y20Pdjb0PjP%2BzUpFGuP7danXVwt%2F0m5M9IHM3ol%2FgneiO4sZqQPMLXtOY6utgjcC6l2w%2Fgtswz6KJvQY6pgHJltNqEtlG9qb267NmHFZQQDZ70ZKTpe%2Bhuuzolp%2BWJ6RzjQxbvzUQBEN%2F1PPRkKUQnFVosjZEBChr7dzU4xDN5qqaZXwIZcDJIFqqhnuMcBh1ad0iosVUXswd2Mvr1sJf6cP%2F9dOuvY5WBbgjJ6QH4db4c7v8bAE%2Fb9zsGmL1XKqZ1FQZySEMqBVgjiy0sJ5fR1M0VZgyx%2Bd1qVJkt5y0HMz7ohbl&X-Amz-Signature=97f2702e40151f0922325db9ada205166f2693ac81349114f9abc463157e7cce&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FY7GDGM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBV3xa22g6%2FFt2HC2M9fkEL7wT8omMwUoDf7BT9xTKc9AiEA5E%2BXOjhAICNeNMiCwnGKtfR6jtl5%2FZeD6z5UdW3%2FqGwq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDOepQVogysaBX1e0KyrcA20YCOSbKWn8XeQ%2FoEB7av%2B7MMm9YNuDH3I6Hk1wEvEncuYEiSosO0QC6PS85zriW1IEOCX0igGU8bR01cTLoKAaxID%2FwhmqXhaT6YI4LzpX2UaCt8MnNG8WcP3cyZepbRB1Ot3Ty3P0ID4I0MMIl3jeNxBNMI2HStgMWpPharF6ycLouI5XGqFItalJ70UfYE%2Be%2FjyNv8bV%2FT6Us1bbnOIhDi2M2kIoY9zdZySX8WiGW3kZsDstzsUzKeI%2FN4%2FcXE6%2FwtqxflQjQX00S9x9DLb7QDHIWvM6hbbhPBcOGTT3sbmKwXfHdg1gZCVagVH5iYYnpXPk9dtKFjPggoEVwOyNzQr9M7C4I2PrGpEl8%2FPr736vOVlB3j91r9Z6rs88RUM%2B2bFE9WfazHpVKngz7Ng%2B5kbfTgd6xz4mop8QVYMui9UyO6JTKLSNLdsWXUV08EbEg7CPyZerQW3hd%2FA8tze8lL3ARxX8UdfqCHDH%2FXd7NA0cAIl117yhQjXSs6OjR4n4DuvX1FV%2Bd%2FCoDIDj5jB%2BF112wnIMVIMV6yH1uzV1HJ9YNlVF%2F%2F%2FNllkdAg%2FFRn0K8hT0MPiZLB5tLax7GWHtE6GlnCw0SI2T5ikGWVtLWqb2TPj6XFp7bOvYMO6gib0GOqUBQweqY4j6zBx8nvaLNFcaP8Md%2FaARSJsC2HzwSSev6YLfLb0rpVhgNpGHCh2n2lrykgDjBub5Qq0Li0ybBoZC2ldy8Per0Jg0Lw0FnE5fH%2BRtPTPFw0IheZV6MuheH2XX4ZH3jm7UJm%2B876J1R6ntxawmWPqDVsEviXXlOn1Kknrqbjiz9zTKZkcWJM3EexE1gPBWFXm9E1sJCl166OzWT%2FKcm%2FAc&X-Amz-Signature=44b3475d31504e50eb94c2eddd8bcca201440b3d7d1881c8d030ad59fb32f39f&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AHL74KI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCPwavw2hfmX26NXPaDHa2bqenXiKCHQL%2BgC0Fl2KST0gIgft03KMvzqUYm1351Th5BxHxR3hDKpRGa4%2FYXU05CptMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDI0CtKigGWwkmVpbLyrcA45RnFg9lId2C95V2%2FeeFZ2Fl8JqkqhhzJ2BtvmQVC%2Fh2tDNGDQZmxoGg5hF7VHC%2F1v0M%2BFRPc%2BsxvUFGzWHbw4Qdh3tQXaa94OFpAs0GPbwdno9Z7%2Fr2dhjyLWL7ByzsKoKvShX%2FDc8BGP8HWoYCfXUfjhUBEzGk9UDh3A0MkwFIHAKAd7%2FIl1ZKTuV1QcrLkFems8jWCOWbnCgBrNtD%2FXp3qWu%2F1cm7B9Sy0yOnMVmA%2FsBynmMlW8ZIVpqFcENHympA%2Bf6zOm6nvhkOEuRRrPsEdcYbkQDeCrAkLHHQ1JrempChzQ8QHwaxkm9eNGF1jh5JmqnieakS2NmWb1TCJdFO35bgg7kXq72YRvXKnUTITUNDUOCCedadTRdtKB2%2FUIEI5%2BBwE%2Bwg2O78z9cyvx8NKT7zyeGOEnKYF%2BoupE35swRwJC6odIgQIJcsKjyRyld3mmZUZxeeExDe9dqn5B9qM92tuKKEifeeY60PcLFze8PrbfFNU4npvibT%2F4SfMSSX83t8ctTaV598fLasB03ZY%2BDhM8fkngbrAauBZt%2BSY%2Bx4NyZOr1bKoUcHrj8USHo0AmwnWA3FSKS%2BkiEcToCQEPrgfCnYL1Zgo8ANsJxQdoWBMnLGv%2BBVqdHMPCiib0GOqUBPFivLW%2FTaQCOrSexgJ%2FFEEGEbzBBpw6pTy9FAUf4Ev6H%2B0a4nhIBuzC%2BOqpADBwVCYvnDwQwh0AoJGRTvKu1A1nVSo8tWP52lGI3LlzRvSJeV5TquCBDaG7Tchp9l7YznfCOCHeEm%2F4BM2cDVfOk3bZbdboR%2FrZ3d37aCFafCCqacQ%2BObDlu8MmOHFNzycv1xOno%2Frdak7q6uXAJMoC0KYnf%2F6K1&X-Amz-Signature=794c6f7bfdb21ec4661465174d64d6dc97e5c6bac225ac8643f65302acd71aca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN443XWQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIAuWrjriUN1Fuo3P9fSpjh0NZKj5bRf0hTKUm%2BtOYaDBAiEA2BFCn2ByUNlOTSciJ9Juvso93pnu9sNX2qE7e2rLX2oq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDFtvR6a0%2B9usurgSjCrcA611oWpgdgBZS48cVBUptXYyprj5Ecjt7fTsD5tkl%2FpiRCdIWqBM0CBesRTanUvhjxrIottwsVYCZ5GY2rLeVhy%2BRbFm6TgfiPlbmP4KR5eIYqjCrM0KFxJzmBIhhBFCQzizMnCxq3nSuPrEnWBs2rG69Fv3WcLqryettC2NMRAaSZyOIlfMJKd7D2cmT%2BvCw1dLv5EitPlUBPcEEdkTVP%2FStZjVgerDPqrrPv9zj19Y8tVc697pSMbdjKrPkH2VmPa2LUSYndqbbMykywKvgBiL2K2doFxCm79BabQumTmU3yUOk8AuPMuYbQTjWVPkcdi%2FjUtCb66yjB4cDAzDR1bjOjbEtWXjkWdqSvO%2BeOKWvIEy%2BTQjWqj4gqsHPyLbgGtTF0H6B3ZvEmLAeoHkFQlMP1LDGcETe9CuqLam%2Bwjq9lvlmg7LGZQnD%2FUSi7AK6N3rR7CNBp3fNtToWy%2F%2B6wyqJSHcS7MyZaphQ6ZXF8SHQNVsp1kbPcYX2sx0yyiTrkvBjpfHyud4VnfkeOItVt79H0USFDV1tmWKsnNnuyuUXwmXk%2BxA4GWkol57GZaAiJ7XVpiBdTm07srz%2BpAxS%2FvipXWJNoKS4NnyjG2WUv7Nkm8DEYhpmHhrnFNnMIihib0GOqUBT83T%2BmYS%2BTeO3aIwMb1IbecLOoiKa0jKL1lAK5QY4Q4ipVD6fUYQxWpZYn2FSIwi%2FJOFoTmE%2Fa088WhnjKFuGis5Z6MnJjrG1mM7mrl7jb1ss0gON7XRLd6pJsknTxEwPLMMALbZ6h2rLJO4wxyb6LpH%2FF1dA2QXYgbHeZHaC4bHiVKh7tPRA4cOLnMOL7tEPC6mr6bSrOWxcvzQZyJZdqccc3lK&X-Amz-Signature=18cb26308d4f35255d01ec9c32587ae188e2eba751059b3745ddd7ae19b1cebc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3SNQ4F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIEdk%2Fc2wybuR43HwbfAdxMOzk5iEUq7hLMNuXwyuPeLDAiBhsW%2FT5PTrU%2Fm%2BSzOMRFsaPL7KsW49plrG4LSk7U90vyr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMYPb3rNG92JbaROsLKtwDf8e6pxe66F3Z%2BEcJ6TFM9SsqKHqNOmaM%2BTbiJ7NhJqFROaobEbWtrABBcM%2BmCRNk3hDL7QL3wOCfEMORNhEJCo9h5Y8VLTF1i3EV%2FGIepSaL5sG%2FLQW2vjm6BAeZ8ckSjwplmqobZji4jUxez%2BL7odpXQ8aufmaCZYxQcDxUtUxfSZMq3QAH9QTejAnMJVWKk4tmYqNRnnYTTShJaWrKLfOYUK1POjWvjSQbSVdSrf1jG2mPYpGYamkVhyC8vVG4Fq08z%2BVrHC6N7hOluQVQLhemyQuaBYRc2tyNLZHfzvrNkuVJizMu7mjQKo8ijAl7QTZuzOv2j1Mn77kP66I5qZZuYct1CEFz5P5FZDVWvNCnVODt5lqoAjxoHDKDIN08twaC6pOq7byODZsjxd4i3m4sz55e4yBpBArwVkORq2jdCpeNTDM0O3puUx7FL6pxfZVPJ6d1w7B%2Fmfok6kDmVKxh7zoi4iGE%2BjDG5bXhpHqQbA%2FdHjuVDIig0IgIIWuUU0nU7%2FVa%2FPJCEID8gDFlBrYK8soH7j4JWpFyEWD6gyqtvGbLQFM6t%2FOeGxSagqGou38B11nT3Ow1%2F2aXlmtRQb9eWOOAZt%2BPHzx7uC7kC5pkF1m8IwtUkQlFR2YwsqGJvQY6pgHfhx2Szqo9qXitRY%2B6f%2BiemswZTdHlj9MzMKB8XwYeMzNJemQJRfm23VQEJKRs%2FeOoa%2FkxKWxPYjTTVQWmk6Q1Il67BYMwAo%2F%2FS5ygymsFVx2JQ6miy6eJlHAJaHMi%2FKh9EW8bFTes%2FfDgdbkuvexH1FfqELpO3pqhajP%2FFiDDpe8rvbfH%2BESallQCMxIMt%2BoJSBkm3HKWBtNLPJccD0L0O%2BKmTBwr&X-Amz-Signature=14c68addad828fa747e4c54632379e9ff1f9b9024a23785a49c0ad8bef40ca7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3SNQ4F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIEdk%2Fc2wybuR43HwbfAdxMOzk5iEUq7hLMNuXwyuPeLDAiBhsW%2FT5PTrU%2Fm%2BSzOMRFsaPL7KsW49plrG4LSk7U90vyr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMYPb3rNG92JbaROsLKtwDf8e6pxe66F3Z%2BEcJ6TFM9SsqKHqNOmaM%2BTbiJ7NhJqFROaobEbWtrABBcM%2BmCRNk3hDL7QL3wOCfEMORNhEJCo9h5Y8VLTF1i3EV%2FGIepSaL5sG%2FLQW2vjm6BAeZ8ckSjwplmqobZji4jUxez%2BL7odpXQ8aufmaCZYxQcDxUtUxfSZMq3QAH9QTejAnMJVWKk4tmYqNRnnYTTShJaWrKLfOYUK1POjWvjSQbSVdSrf1jG2mPYpGYamkVhyC8vVG4Fq08z%2BVrHC6N7hOluQVQLhemyQuaBYRc2tyNLZHfzvrNkuVJizMu7mjQKo8ijAl7QTZuzOv2j1Mn77kP66I5qZZuYct1CEFz5P5FZDVWvNCnVODt5lqoAjxoHDKDIN08twaC6pOq7byODZsjxd4i3m4sz55e4yBpBArwVkORq2jdCpeNTDM0O3puUx7FL6pxfZVPJ6d1w7B%2Fmfok6kDmVKxh7zoi4iGE%2BjDG5bXhpHqQbA%2FdHjuVDIig0IgIIWuUU0nU7%2FVa%2FPJCEID8gDFlBrYK8soH7j4JWpFyEWD6gyqtvGbLQFM6t%2FOeGxSagqGou38B11nT3Ow1%2F2aXlmtRQb9eWOOAZt%2BPHzx7uC7kC5pkF1m8IwtUkQlFR2YwsqGJvQY6pgHfhx2Szqo9qXitRY%2B6f%2BiemswZTdHlj9MzMKB8XwYeMzNJemQJRfm23VQEJKRs%2FeOoa%2FkxKWxPYjTTVQWmk6Q1Il67BYMwAo%2F%2FS5ygymsFVx2JQ6miy6eJlHAJaHMi%2FKh9EW8bFTes%2FfDgdbkuvexH1FfqELpO3pqhajP%2FFiDDpe8rvbfH%2BESallQCMxIMt%2BoJSBkm3HKWBtNLPJccD0L0O%2BKmTBwr&X-Amz-Signature=65489284eded1ef91096ea7a90fc28c1111131fdd05cfca3f889c9a08bdd30e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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