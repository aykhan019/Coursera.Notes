

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWBQW3F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmECe8qCRV0kNeUty8vNRvhRS0m4LEaYWcZni5ORUKigIhAOmtCIAeVpLarismbDuu2HL8qizI3ZQ4R0DPHcIO2v3lKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKjb7kpDJ94ufOmxgq3AMIi98rB1V9lodJiuhPfjHvZmklQuoWf7Wk3McPrRRQFgCMX62FNqmfiRZam7Tx5phuWSTvE4Jh2f4auBmwwnvHQyt9hGe9c5nlULTOjx4zYSW29UN2TjHNMP0ZYoi5qDHwPH5Ag92tNM0SbNw5G74za8diCTAhZfpFNu1WCz%2FWmxL%2FZrICmvISjVox8YgRuRxuLfx1DgkTvyaYjQvXK5puv1ZayGu0MV9R2JnrD81OWPUK%2FAizRWUE5fM5ODuUoMTlVH0dmch1ZKGexax2B5qRfyzzt0HcTL1mbgMfZN3%2BJE8RlukYYZMG1pga24chiVreMlN5zpABOncgO1CwBaB8pRnAgo6Ro82KJTM%2FZVuU4eDGrU65gfcs%2FCT2SQoqvB3Pgk%2FmVCPiho3XJ4t8x4AaybhnlSFnsqYWnuqxqs9vju%2FhgViuYwVv%2FhPC%2FyBDfjrD%2B0c02nqRXXwH05IIyLoF4wiv45lOQDr7ktZyECcr23JYvtNFjUaU8hg4xF%2BMYJCgxtkur%2B3UKjJaCEkOlSam150N8SMW3U0LOZZlVjLagvnSf2EM2bvYjfDB91IygoTMMuYtpLvWYKgAG2F0mFc%2B6IT9RwIyesxt4XUSiOsQXexbTJN2hH0rHc4AxDCrl%2B68BjqkARBAGZpL%2BY7mPhy8pnc%2FI6nex%2FJr%2BXqAvyQFrojFFh71mA5p3%2FVvOKrqp4%2BItM7XBJ3gH204%2FMVrK9o3u0iLXLNwEVG8dLHmduUvKe%2BsaqJB%2BHvdK%2F%2Fh7xWxTbzUiflQjCgT4c6nJmzGjY6%2FJsRbsLhcyTqQXcPgvz2Dfo4QFU1qHV9HJIbN4%2B4toSqQwbaJgzpjfdLo%2FPxwYXT3T%2Fm51m0Zzyg5&X-Amz-Signature=83b1b6fbca804c7de575397e4a6a83070b40ade474ddbb8a04cec017fca7efec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFI33OZG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICgjTRhsjqFnv6RoMi7ObwwtpgSm3v9nFmpjNODeRfDvAiAqSF13HbQk5zluRToPH6DrqhB4havGmH5579p%2BvjVN0iqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwVawSm1w%2BgD59ph9KtwDZKaZEC32fL3%2BnvGnrlO4Owdil6RyUbJ73l0B5Fgz7BlPD7woOcfBMdVvVu7osvAxqpyBQFgk6rF7Qk0BE5mnUFeyBgktinW2omt4jWj1gfyfOk%2FrpqnoOZh1xwYxairQQIDCHkkz3S3Q5bRcvRrZZjQ2AT5OkZ3fpcphEy2pwbGzU6W3En%2FlpkPZzgoGpsRMjcNqCh0lb3P6MqBOLH1Shbq%2BIgSyUDGcCQwPQDJzKCNKhXViTjyLGa4sz1A%2BRJfu4PFwPhNuMWREERI4vfQnek9SJzqRPe%2B174YfMEMXsr1xp%2Fc%2FHcgSYFPKoIx%2Bhw3FqcnFHkaeJ6SnbQymvl4MqNYT6yfhug%2Bm2671fWyPxvXpYviklQr8u2uagcdYt2QkXytesmtAJzlw5wer2zBjkjhQToVl9PgB2K26Q8kmCyPelkF3BAHupdX6Bsv2gke1FSzPvHM2e7R9h4bBFJjNcfU3G%2BrIWZPzJ2bsXskipPR3RZoPnZvhEziEr57%2BkOpQa98HRt38ePSUBaAdRydYQnGdnfGjNk9a0SI1LXU2P4gQ75CUy2gKMpNOTVpP1MUA8f2%2FINJPqxapu9cvdCx%2BFnEtqkTkZsOwbLm4TTA2zJjQU4GDwyvGtCi9rT8w35fuvAY6pgGm6006amhmvpDO7IKMnuO4sa8J%2BtNNTsQxp4vGh4beJAxayyOd0674ba6LMxUKQcauZfBLZbdRfzmAcsmX74CWBSIvM%2BDOrKlVW%2BCv0KkYPtdiCID7sqY4Em6iuCLaZWH%2FKvK2TN77hr4%2Fdwojpw02HuJ0lQYtjRZFNMYYHSR17JUJkan8dgvcdulCHdOHPCbJxQIJ7IdkKcpuIuw8XuuuHoAeU7Wu&X-Amz-Signature=55c0bb8e536fa8cf89a3356c4773686c97a209114a17bbf4b9c044dbc2d589f2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PIWNH75%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaHKPYALuyvyBekfmdEYvBHDs53wDMvkJDxI51q%2BDr0AiEAqOI%2FGA53pmvtGffoiYFqrNKmPFI8q4ryDswdXtXQD0UqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPpOu74vHU4FxKsaDSrcA2iPoYw3BurZCMQErR10bTRLWtOn13LGiM40Q%2FFb3RDo5qnTsmLqIacmDpuJTw%2Bj4dHMa59o0MIY5q5Fj%2F43iAYmlbF2JTKmk7z0weLezI2cX%2BMwWdz1%2FCo3gpBn20Rj574QkKxBxdmXmKgNxEvOzz%2Fm6v6Rvsz2r%2FXXPWi%2Fc5LaF0W%2BJXVEozMbEFVA8IZI7BZuT0Eipepy53suVdxMJnjN2FM0KbbD5NXxpa0JsUoOlsrIDIhi03CPwQpVGrepYvVyGT%2BpcWZuWnXBOhOBD%2Bf7ri%2FQi2Wl1y7HXUBYdSyJa7eEhgslNc98Zrs5OadexstZExM21Fi5g1Pk%2B4PHn1Mcg3YyGdivDPRyHy9qrrXgVj3a4pFWvJEDGmXiF1of%2FW9T%2B0kioxCbCZFUSPvL4tciYWtyxwlwWbo8UfM8%2FWONTARvt%2BhI7FsaA2EO8OonF%2FGt6GesRkuGGsCGRPo%2FXo9AKhendcSdcFzU%2FbVufewFgzkzjysfBEjNqOXN8IpsS6U0udAqceqURbetzr7yXYOdNhzt4Yd9oOnDIz%2BFJOziCiUM%2FHyKAMPh%2BxsyJKk%2BWHoW9qSYH2kqlWOfi7OgCcf18NMEZxygMFBgUjPJcM0U9X37c0%2BGuSu6pkbbMJOX7rwGOqUBlywn2bOpgiSq7wCYRKv9KDsfihKpb7dKS74mjadCuabVu2w1ifO%2BAbW6C4%2BtnsnuRFXpD2AmMwKM6SBlCFshNpLhy2JtRsIZ43YDyJt4%2BRpktioD6%2FNzsxA0oLB0LWIYl3fuMEl%2Bh8teVJ86GhUs6yiUeDPmk52O47%2BjCanEa600VpmTeStD%2F5nDQ3S2iPsaPJQwRPiZlQxJwPu7qimO3iu50Q4P&X-Amz-Signature=c033c2ca83cce0897a3dc88d50e74154ff2b9c86057bdcfcbf0a25c0c6396b52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NW62VUV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF45kf%2BJCuQ0d8ic%2FaF3yKmZ5I1ptASXDYK6QETn7TqEAiEA8P2JEi3aakfj1NjgDBu4lYX1SOGzV9k7weqSnTrgx2AqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNICeKgGWa6NKh8CyrcA79KYoxg2XDZcOW2MHeNBvmk%2BF9CbIRhfc1iY9Ae4MbpkfULR%2F%2BN5DJ%2Bl9IXRooqsa2lrk%2B5bau0O5xbhwwtnvbUy25qWg%2BbeOmSDNMFcF7u6WGmlzBVQwAkEsZI%2BLTq6VQFzXrdw6N8MWHlv3bdw%2BaA8zFdcuFi88WAP1Z2NenWG2OtbixQ8tfmCUDV5A246c5BGlEMZWi%2Fmk1frszssgCKhpR6zSahxU7MeEZcwvB30YGvBsh%2FirnZ3A73xB32gwKjF8m0iIScKlzfSwKlPvS5ewWf%2BWugncwBNAd8sWkJn3dQ%2BOORVDx7sseH9NPV2mh5895WWgTYYECvoKV8JOfKYRLYmwsDhRws1x%2BiMHgyvUhHWTIQQ5ATBbEyBZp1Bd6IKbSzXmvcTGUgtlWi%2FGQE6KTIEGzpsNeBd%2FktPfS%2FKlYuURYzmReF99mSRk41b%2FoOqapHq7xEONui7Sb0kzAOtIkj8Ff2Yf%2FtmkKzW%2B8I6qavG77%2BkhnWzkPB3k7av9vmCszWfSXipP4MK7M75erZ5EBmMXF0J%2BZht65DscP%2BNoyBkaKrhIfA8VOJoRiibmMPuIZmb6mJtQwPp2RBuhmOfGUVWonYd8se6IPZzzNs2EGKK691dsYBJ2a7MKGX7rwGOqUBAvVT1dW1%2F6CkGRSwQt5MNyo8HgFgDgVhVMC1JSuuRiP%2BX%2BT1%2BVCFL8U%2FrM2ByizbUjMU6XtYA3Xor5PA6z3r13F60hl6uHlRo2Ei4FURAaHoEUw%2FGwpDZpc1W%2Bn9ZsCES5snuvzegWqoDngd37BSWKtIo3NQLoP5SUWD7i%2FOHGhZp4311wHdtA3WUdkkv4KqytXODBx9l%2FSwqcLiISRqYw%2BVxWqE&X-Amz-Signature=0b3f34e1527fbf51b7a3be10d8da239c00d653909cbb4c222a46f00348b8c481&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SAHWOC2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2iyMYzX5OHuwfepxybinQxz4bxcfdcDwTLZ9Wx2DCdQIgLRHwHjvQeOeKeb%2FFQ83vPe2ZpkdB6g1LXwbsM6eVz2UqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYxR1kscvvcay3pESrcA7wUAKfehojuQ20ZEU%2BROHf4hdcBePGTRSA75snlAGg5lb%2BmnK9Ax8b%2FHVCOyFonz1QGDGTV6azO0duycvO0aDZeDsCZ4iyeNioXXxK4nVs8j75KycwIpllvbus4P9sLT3WWebNqYko37WNFFlowssln6%2FKnq9DI7r7hzj8ZmKGbXbdgswhDCYu0gBJfsSyO6PIwrft3KII5ETWGpR3KDQK19FyhM8sRLNqqVqUS8xOtkGAZAON%2Fw10BbwSj3EDnXpCAmdYGXzZckYMbVLsMM6VC6CeojGJUKvJhJFN8RDjurKdEPX5aPinLno4XvCbNNGdOF%2FPj3ro%2BTdnjIW6xlP3RoFEnBmlus9TGSLTHDyBj7Bii%2BiPJidZsMAUAk%2BtjDhQcK5RKWJ6%2FDvcC3qaEl636ISwQLhg7UKe3c3%2Ff74IWE06Dns4hOKfRswRw0D7VcGNyYtrc5TWYK%2B%2BwGOUnpyDUIHTHPV%2FSYGO9Zx84rvGXAnoozUrAp%2BWClK%2FeYlQYSF7OI2PyU8qUlT0VSd8nXOq%2Bqn4FhzJkhVAF9ihMPHovQNrnqbBEoa5WHFzeQTfHFqPoommWQXJTLF2zVbCEo2%2BtGllMjnyRwoZRmLPO%2FwMgQJTGQxzfQcLuenZ6MOaX7rwGOqUBeYs9LJM8BNrzDnb0Z7abjTG8Ec%2FmjjgGWUhDJWXllPXEJhFQhtlkpGkjCOMwRYYywkGQApFRDomtmLhUhTzd3TAsIpN8IVryN2%2FCr5eIquLAwrtxSZgIgfUTr5C7hyXm3jp85eRntMna3%2Br5rZXAepbb6%2Bc2N8jUzcDDrp3rkcporkE3V6poWV6Cv3Fi8qjow7hNhymh57KftmC8KNHFBw%2FTIqJ1&X-Amz-Signature=393fb6bc4708207d8cc88628e473adf9d29958324f65dcc091753b7049b684db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPMPCWHQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDUOsHNNLI%2BQFZJ%2FOJtvVsBz9ZN5ALO5uhBz8ws%2FHqG9AiEAybhyePPQcASetjsNB%2BGUMvUsKNtk%2F3blZzsydvsaR4oqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2qhOEkTl1KSqsInyrcA7CGeM%2BBhZwPtZSDUFWo4%2BycQ1cz%2F4H6%2B6x7zX2Vy9t2zyR0ENo3thZuj1WsaI%2F%2B%2Fl1PBTlpIG4ZF8MA6v7wuEJ6aXZoCQjp%2F3tJQ5CaqXp1I7EY9D3jM%2BmZjTfRM%2FDaT9d32%2BWX0W6b7zkAJX%2BEfhoMPSxLL5UP5QJ9kdxh1%2F77R9RQDSKFB%2BeUwlnSn4aId8KTkGlotxzBa7EJTrnA%2BeBhq%2Bz4AU5ryV2BM95%2BsoykUdDRaOn5pg9vwQy1rjWaDxlyPiSCIIu0i7mxzCZflDUbV03lR4JFo1%2BkkYNYWmK1KGB3cOiunW6OXgEgdIjCuEdd3BeGeGviAln4rtcLZq9HH6pL3Mo%2FwWfvWWIuqHxLypcWssabVXSXqZpYhLfjcDDH1OMIraPVEvW9Z7zKw0NF0UvdAxpaXg8ojftAbzLF2%2F%2FWvi%2F6o6ep8Zr4CdKu0P1jC%2FdpNLyA8wiMvL%2B%2B0bvwaOYVQReYTqO0GSTj2GgjOu0xcp6JdaJvr5VXofbXC1VPjdgvVxEEf53lbL3hVfXC3RKvNgT4h64iHfj%2F1%2BWujeu3GugBd754xVyEd73zeR28ACrbOZKx%2BhdUIUecUYow5farApY6CznG8tRbKrbkyqjIF4CCNnq86EoeMN%2BX7rwGOqUBQfuZCYQZRXJcetLRXN7d2of1iUuf%2BGARUSxhEW1TJYtqUjEjeAl7L%2BnCZGT4iAUxJeQ82%2Fsj0dCYrlpbV5nGTTo%2BMwCmErRkKpzWTNRn3QJZG1m9YDRkNtaSgTVnmT%2FKrvQkYXMqCzvG6rSAKzIQAcYqno6b5CKjyRhpr2iJFqoEglRZGc%2FPCurYzw5abzDJ%2FmUWCVnBy6wYDOdi7cvRVipKDfrb&X-Amz-Signature=407f402461d9b3d663ecb15c89db03953f7653c0518fae32c54bf7cf0e32ac90&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVIVCDRA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqgpSgg9BCoY8%2Fna9mSeM9KyLpirFqjjeqUFklGaPatwIhAPlD%2FTGExbGiXdePpFBcU41Iw08IuYGkrx8Pk1CGxfwLKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKnkKEB%2BPqBIQSSXAq3APs09e%2FiAUPpH7NkSZhpAXTSU68zCzXJm9IW5tAWrfm8C16GGvbDXQLJ4wbS6IafdUeSFHB1EWUH5%2FzAq1uuToHCrSXHCeW9twqhiAcfbNVcupK7mWgGHrmo5q6UfFfDfvILx1pJa2Q1%2BnYEvOq2vnbIOfMRcwj%2FndmG4w2bPTX3t86lNpuIKK%2FLSxCbyZ0e%2FA1%2BLYoljfMmHfBTCrzico0hjGsW1iF47SkUEGDQxXkkkUGVGgM3aE9iI3RA4kfFQJHtKXbT2fCj%2FsSeoBoVYJcussJoESBQzhPDKhaHv07p9X26x%2FhPIm7UbY43o%2FpftWAHqpIc4I%2FuecLCkMsRgo1TdBl8MHL0JJQwbevY4TqsRUwawZZqM%2FzuZEv7wjxqPpKHrEtJwLfM82SsMOQ520aww%2B1no%2B9y7TNqbJjXeszqB2iBlPWZHJe8%2FWOuvIO%2FI12dmFjrmz%2BurPNwJC9RPS6zUkniH9o0kBBd3jB%2FD5Dfuu2GBMDZfB4roH%2FEDnCm6lVCvxiXLQw%2B6DI88ccDwBG9gEXu71bMfP2IbhG24ZsPYCVuivnlQuNwFSWCKktNdb93xo5wiIafyTD7sQ4YeCxkEeSlcnTVAiif%2FVmhEu6lPX66MREoRiSWYYhwzCgl%2B68BjqkAWZld7JaCwWjvBMGboW8ck6jURGdZekmz%2FxQ71J4bSz2C7vz0jkhBS2FCuY1ADclmQZ8tevNVR6dchzuWgktirWXoAQLfB4pL%2BvL3Ap6j8hAcEqhQ%2BeDHVJqxyIYLQms7JbvrrUUiABBetUhe8LLg3IEYekPUgcQWC66gb%2F9Aw4nXJHNihJV2NyepiKkkCVeaY%2FKVMCJHAhaXr%2F3LCBul8PBOZmg&X-Amz-Signature=cc1d3791d112c3a269073025d7da02b29241189afb2707ad05c7595a640b49f4&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MTEI2GZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwhYQZXTtqRpSDU3MGh0JOfHiPHkfS%2Bl5Ui4p97SNoiwIhAJs3fABoIj7FG4a%2BJlxd68KfVln2B%2FEj%2BN%2FmrSHrfksRKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzGATAO6QB32zqzNwq3ANVKf5raUKpapEymBc68tono6h9oMUvjAfQOEDi7j4xAw6oRu2UE1OGGVLM2n6F8SHKQGV%2BxAbzZ4fdtzqdVTdkMUuh2F2sz5wjiqX4twQuKXYcbbwDZR%2BCZVc8kJSqZebGFKwtvMVIprAwLwVB882oCYdQ4F36vZqyhS0hFBCmM%2F22S1DkpnUVmNrM%2BrB1aQNpDWSTR4IHMOQHz%2BscUFgkGdpff2GfIt8WV0ANhCagA27364RYBe%2BaDrDmCDNwshpRZIpK20O5kQ8gL8JBUBjKqL0V4DCN0q1Tj0OlXJMHlpNuIc5TJPEyBsvJAL%2FPrAk1hys3jnbPCXfYlyvxGp%2F8GNO1uW0wC6R8rBaXEsYNthfYwQPlxluXv77ZTzK%2BSL3pLCU3LTdADHPkYzdQqHH9iTOh4AcEwmVULGG%2BjAxTIZWb9zwn679M0nN3zL5LMrUbVmMu1ZVT9YpV1PhW4puxiZywsylEw%2FH2VO1lj4Opl%2BvBAEtb4cSo3SfWtrzvwC%2BWK51OfAVweiXDPlod%2BhhQ0rbEYGSE2Oe69d%2FdU%2BOCbPcduZRsrD4NYNNjO2feTAh%2BCSMnUyK3xX2qWbuzSs7KL92U0Mdx1HK3UCHSV9RDrlJNSOKrFVw2K1wtZjCKl%2B68BjqkAes9DYA9TBmxahN9Yw35iA%2FkfCy2xiGgns4z2EKryQoVmC5JY8slOM%2BgvjytpFcT7n2x8a4jY0gpXX1CsrsjZZPiqwt6E4XXGIz7fHvZl5iash5SjLpYPGRF8jQqOJDoMKgBKsUuQAAMo0zWWCKp3Eiy7uboxgy3VVTOtJebHDfJ21avMN%2FJbgUAmtuZsuiUeJ7KTda1xoTK6QBNFIeUwr2sU%2BO0&X-Amz-Signature=47921d6758a18f78928ce0f354d343ca2347d00d6f43b07a4766bee9430f92f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SAHWOC2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2iyMYzX5OHuwfepxybinQxz4bxcfdcDwTLZ9Wx2DCdQIgLRHwHjvQeOeKeb%2FFQ83vPe2ZpkdB6g1LXwbsM6eVz2UqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYxR1kscvvcay3pESrcA7wUAKfehojuQ20ZEU%2BROHf4hdcBePGTRSA75snlAGg5lb%2BmnK9Ax8b%2FHVCOyFonz1QGDGTV6azO0duycvO0aDZeDsCZ4iyeNioXXxK4nVs8j75KycwIpllvbus4P9sLT3WWebNqYko37WNFFlowssln6%2FKnq9DI7r7hzj8ZmKGbXbdgswhDCYu0gBJfsSyO6PIwrft3KII5ETWGpR3KDQK19FyhM8sRLNqqVqUS8xOtkGAZAON%2Fw10BbwSj3EDnXpCAmdYGXzZckYMbVLsMM6VC6CeojGJUKvJhJFN8RDjurKdEPX5aPinLno4XvCbNNGdOF%2FPj3ro%2BTdnjIW6xlP3RoFEnBmlus9TGSLTHDyBj7Bii%2BiPJidZsMAUAk%2BtjDhQcK5RKWJ6%2FDvcC3qaEl636ISwQLhg7UKe3c3%2Ff74IWE06Dns4hOKfRswRw0D7VcGNyYtrc5TWYK%2B%2BwGOUnpyDUIHTHPV%2FSYGO9Zx84rvGXAnoozUrAp%2BWClK%2FeYlQYSF7OI2PyU8qUlT0VSd8nXOq%2Bqn4FhzJkhVAF9ihMPHovQNrnqbBEoa5WHFzeQTfHFqPoommWQXJTLF2zVbCEo2%2BtGllMjnyRwoZRmLPO%2FwMgQJTGQxzfQcLuenZ6MOaX7rwGOqUBeYs9LJM8BNrzDnb0Z7abjTG8Ec%2FmjjgGWUhDJWXllPXEJhFQhtlkpGkjCOMwRYYywkGQApFRDomtmLhUhTzd3TAsIpN8IVryN2%2FCr5eIquLAwrtxSZgIgfUTr5C7hyXm3jp85eRntMna3%2Br5rZXAepbb6%2Bc2N8jUzcDDrp3rkcporkE3V6poWV6Cv3Fi8qjow7hNhymh57KftmC8KNHFBw%2FTIqJ1&X-Amz-Signature=2e937baf3d64822397d9497f3bc2fbeae34a4ab190aa61f0bc7f8af249107bee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUOPLVE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA8pkmt2sz8HSSk8TEHUWIhr%2FeLsM7btFWv5cwPAFMawIgYIYoEyHfYQ94BuOiY8Pyz1zlpBOqiF68KnNTp7720PUqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNcNjzF3zbxF3zzioircA4RgKfAZsugjPr2PAVNiIpSPYWDaKlohzbqtxwv%2BEWj0m4nvIdbIe%2Bxq4gFCGZXQcAidm9Xg6f6SrINIIhr9a%2Bb73b0dDEXtL5%2BOImvwjzaXwHl8KtyzXixFeFl04zynvpSeEYDTeczPJZClqXRrMHoXznI%2FgFXrQB7BFZaidQjOjh2qiRKDksEh4%2Fdp3UzhUGTQjvJG6zxYrg7bpY%2BfXFizj9S50gN4R%2FLfaJXzVPhkNuMXLNNDb%2B08fYjoykwx4HChrix0LPlf6%2F4%2Fv1ZATECAz64q0E8azYh03DjkHP6q6ua2CvfSLbgC6VBkWIdJ3OAbQ%2BHNi9tzxMBP3U%2FRyCcW4uPkW0WAQ%2FIOfAjEM9ABxYwuS3F3XNyDBTNOH%2BP6AFGElaaGm5mGNfOuSPXgDmg2P6qC7ium355ipkk7ncBvxw4GpDJylnWNVzSCa0%2BspJeaDwTkuDj7YQdTwCRXVl%2B%2BSfzQ%2FXV1W3O4rymp0zU0DrW%2BLE0W%2BwIcReJ3ieJGt%2BuusjadajsDg1R9iyWQfp%2BjWdLIjDIidv%2FQW%2FSZkUDDkT2NbMwXJig6rNCVRA7kSQi%2BOx1l2DHtGEFg%2Fo7H6BCKPBbrHAT2rIcwcgc9daXn18o1UxkqFGAMKyLCMN%2BX7rwGOqUBNfDPLUyT86Jj5ZSWiCVF87fMXZ%2FdI0wDroB6Qjm%2BLMtGCGGxS7E5jd%2FlKtC0MiqKu1Ra5Eo%2Bsu3ze6kbgTskCmG9kr0vu%2BPc%2BNF4UbFvAsV2LFaeZ11ssRmzZwW%2FSsii3AJ3QLYaoDil0nVmziYOZC6Y9JNTdDUsvpxY4iNOfioNznMTj6HY8Wlm2gjludC%2FQjCXcKzCMAxRSb%2B2fninH%2FO3TGLF&X-Amz-Signature=6bc85f1ca388774ee1269c6223ffc5005fb576b6b9f1434fcef58b755034ab0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGUOPLVE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA8pkmt2sz8HSSk8TEHUWIhr%2FeLsM7btFWv5cwPAFMawIgYIYoEyHfYQ94BuOiY8Pyz1zlpBOqiF68KnNTp7720PUqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNcNjzF3zbxF3zzioircA4RgKfAZsugjPr2PAVNiIpSPYWDaKlohzbqtxwv%2BEWj0m4nvIdbIe%2Bxq4gFCGZXQcAidm9Xg6f6SrINIIhr9a%2Bb73b0dDEXtL5%2BOImvwjzaXwHl8KtyzXixFeFl04zynvpSeEYDTeczPJZClqXRrMHoXznI%2FgFXrQB7BFZaidQjOjh2qiRKDksEh4%2Fdp3UzhUGTQjvJG6zxYrg7bpY%2BfXFizj9S50gN4R%2FLfaJXzVPhkNuMXLNNDb%2B08fYjoykwx4HChrix0LPlf6%2F4%2Fv1ZATECAz64q0E8azYh03DjkHP6q6ua2CvfSLbgC6VBkWIdJ3OAbQ%2BHNi9tzxMBP3U%2FRyCcW4uPkW0WAQ%2FIOfAjEM9ABxYwuS3F3XNyDBTNOH%2BP6AFGElaaGm5mGNfOuSPXgDmg2P6qC7ium355ipkk7ncBvxw4GpDJylnWNVzSCa0%2BspJeaDwTkuDj7YQdTwCRXVl%2B%2BSfzQ%2FXV1W3O4rymp0zU0DrW%2BLE0W%2BwIcReJ3ieJGt%2BuusjadajsDg1R9iyWQfp%2BjWdLIjDIidv%2FQW%2FSZkUDDkT2NbMwXJig6rNCVRA7kSQi%2BOx1l2DHtGEFg%2Fo7H6BCKPBbrHAT2rIcwcgc9daXn18o1UxkqFGAMKyLCMN%2BX7rwGOqUBNfDPLUyT86Jj5ZSWiCVF87fMXZ%2FdI0wDroB6Qjm%2BLMtGCGGxS7E5jd%2FlKtC0MiqKu1Ra5Eo%2Bsu3ze6kbgTskCmG9kr0vu%2BPc%2BNF4UbFvAsV2LFaeZ11ssRmzZwW%2FSsii3AJ3QLYaoDil0nVmziYOZC6Y9JNTdDUsvpxY4iNOfioNznMTj6HY8Wlm2gjludC%2FQjCXcKzCMAxRSb%2B2fninH%2FO3TGLF&X-Amz-Signature=cb243d69bcbcb7be6ede4f23645fe6dc72f6ea3c5ada40a44a53bc2206001bd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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