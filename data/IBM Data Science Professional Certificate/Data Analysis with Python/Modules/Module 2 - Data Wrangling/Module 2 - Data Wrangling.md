

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN7HJSCR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIGMdPS%2Fm6mjAI2DsGKV5w1a4BLiO80KDVhx0SRPlq8PZAiEAkXPHViKjuN3QXXOLkGQx7sFu7q4m%2FT342xL9LyRBtPwq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBk%2BsIbd3xZ2ASNH4CrcA%2BqLVgqUnoIuXUwtJFKUs4cm1ynxbty6Z2aZraD%2FVF%2FO2sESBOGh9IKwKbZlXsOmSLsN54T10OqAqC6Oi2sNfVcJAV4a%2Fm%2BorhL%2F8Xk%2BZI0v%2FX7Yr8rpT%2FRXWW5JmAFh2eN2o%2FolGcq%2Bsv6ptshAruFQhe0I1YOu9kvLs68qxmvVrfHKZfAAzO3%2FtSzLW3rsguK0Z2w%2BFjSJz4NeQDALTgHBGh8tV0FYXgARvIGZn5r%2BEEcVYV3tM3fozv87vs7MMbUJ0ocLzKlBq9WMfd7w10d%2FwTbc2LE1pPgxZWa1B8AUEBqv%2B6dSLkKLUSUthAFrIVFxPdocS2t3TCpX7qnoCUt6sSypypV9IHP8a2kF1XSh8EOrOrC740Vp1LkgMb%2BuLriw6A3a0l0msPwQeTm2xsz5FEPRsrVcmeoFjnMFAvS7jUgNiKsVfKTQw1RoXmSGgrcOg8pwYowX60YlFKaKZq9zAoypL3yBzNOtRqUnbxgb4kQYik6lMJXGXpaWHj6VNQa3lL%2Bt8A1v2crXI7c66YHdONETHlnCrTup5MY0pH6j5wymNiU3Mb4mEY76Z8v%2B9iBdJrvQ7jEoDzkt%2Fzet3fMOEhpdkYIOd3Jh6B4oFK81gKknkfpxUSuhL55hMPXdi70GOqUBCNFDE1qcza%2BziQEMz%2BU2p9UILMx8Btawy7yxGl2LMD%2F2T9ftzWn8he%2FEtb2Pzf1S5WgWixFFvzsE%2F%2FEX581eMNUKpCYa8L1DrAWayt3rNh71p8Kl5WFraGqyEQk%2B3OSzok0uZNQQ3%2FicK8FwcjSzNgsrQ2fgh9BlpxJC8s9uQfkNr9Tscpq05AeSOEV8zWOJsATkzhL88foJja229wc7dPH5esjd&X-Amz-Signature=654d520a8486fef02000a18c17c41dead3187af26333d62f4110148db53796a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKM4EPWB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCr73UN2GfBdDVf88tQR4eHrqmRqxYiUVS%2FnI%2B1Fv%2BGsgIgQ1URB3oxOewaT8iBILkL3x%2F6%2BNy%2FPEyQ%2BdYw52KoDpcq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDEewh5fZHz4jjs2rhyrcA34jmhHTpFPtmxMlDW%2ByhGkcwUjhGEptS1t4sKOU8ri6HVQ2U9zzZIEuewnR22rRBdiRNr5XKs7ixKAK6i%2F3vksA4szVpda8UCecdcntnoC57Ryh%2BzNN0CKOX7QSDj1HgB95ocvriNseCgjIcmDY%2FYMuSWGTMrfuVUUdtbl645Qk7xIYejlGN3inP5ng6Gr99KqPVfj5oSvKSaaiSOmqPa7XSWIXolEPhSvwXWCbqwIrEFB%2FGRrdU0o%2BAz6BNQCPdkqQcIJwwbxxGWvfM0mrVIgC8MPkBBdo53i8LMfEMVUb%2Fj0pS%2BjsW5SkwSGVTu%2FnS7nGnCzv9HpAoO60sjuHCXTVwrYFA2vU3hYh1Hb6w%2F3mrDZ86yN7JwlbMjcYqEhB3fSf6TJnO636UM5bh84TVOp8Kd81HzouhxrhZ5nIYC35adnmXlN5xcSkgRO2t5FufZzsqzjR%2F0TJqqH66MbCYcdOE5VM1o3WTk9pJ%2B5K%2BbpRXHOmc96Loffq17fg4U9AMpsnmhhffwPntNdb%2F1lSFX%2Fi%2B9pkoCK1A5Er%2BUyTYLQQr%2Beu%2B9sYtjVB24eQJGbw7Tcdc9XX87IyZf0rCgMHEBdaBY1WlnWNG%2FtVDkGLd5JPqt8NtHH6iZgxn65EMMffi70GOqUB7aJxo0ej%2BGe7CI8hQilwVhIseucyAlHmtp5KELWhsdBDQhq7O0weSRO%2BC4O9v0pbxgwlc1DsedLkGmXCrpkQk6PpO0TTS8AHKQpY%2FtLvrkFVb11W4hfdd4KT3N1086Y7EFj8vxO2HzAsy4bs%2BihKGpcgiBhz66zFaghPinFCFnejvcduJxcM2eu2dU3usgJwMPJK4Y8HNyNblbd3Iu1WSxbMFhY5&X-Amz-Signature=c42da0f7cbfbfae36c840952d1320722fde431834f72d2daafa2ac8f07dd2d40&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJGJZSL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIFRqYUICMegyJoDT1fCYwWZVhQUPZWxLkdXMckCN3Io0AiBprO4rrnfCMf%2BjZA%2BQ3EX2lmjte407XNMbAn5znWZ8OCr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMrtweaSVmjjCNrNvoKtwDXmgIz1Y593y3YcjOf3tBruDfWsxg%2BFosYe3TH%2BqSZHHhyYaLD%2FgWrxnJ1CNJyd7TPhVU5GFy9tRXGJa7DwZgGj59Q9aNW5t7AEperu9scmDSQSLZzpNcmffyKrDl5PAG2eF1kBN%2B6v3YLqEsnOvqMtJCZW%2BwyjB6QrTVvaQEYSA5et%2B3uSRIu4fjxcB7psXoo8ZgbsIv67sT5kXno65Z1EfVaUBXGW0bh8Gz5Er8DKbCPgmlGFyRYswJv%2FfT3veVGqo5k8ag47csTNqcQ3sUusRe%2FDij3TLAviaOinVECwJa%2FF7I7XZKcfB0c1%2BA2mVZ1u4Oo5ck9tRvhNMWaXn%2By%2FQtetyqZhycjGy0Y92nIBPqi6VmYlDCfm3EuxCOKm2IEKpj%2FvUy5hQv4pzFsVR7tgecB5IOmS0pha2%2FfU15sRjNZevl9M5PvVpcvU1VXiITdsqg5L5MP4Wnksfe0vqf9uQbUHGpsc2Ht08bIpBaUcJvm0bH3L5Rzt40zE4C7%2BgqYteaH13445O0XUGRbjOtMCUAQ%2BQqgIXnN9QY14v2IIfhd10QaJHQsaeut00MZmZIimUktOq8Z%2BnR4PW07kfNssCm5WXmylvurdzC5T2%2FgohUDEAr6pMnt6Tzol0wxN2LvQY6pgHXrz9PlA0QKdTUXVp9ygPPWoa4ZgCxhxOasFIGHM6wH%2BxwMrtea0dX7yhJxJvXt4fTKvsYLmjAerpZjR9yF2ZnG7FSm%2FdTE4GGA5yMoNtjerUnzOQ2c9aMJqmRc1eB3u15IStiZs2MV8KLYbVmcAWC2W4GpPT0ve8CwlSWOO0sCH2Ma3Abmr66JlZh%2Fkp3P%2BtVfLEBY4sPDMXf3%2BCbvHyP3V%2BZDUL0&X-Amz-Signature=615a6eceddf304d2fd29f0ff4158beaba68deb6b42e5f5eb1deaae6e65ef01cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MD2L4NY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQDl80bR5EKBUWQ%2BK5yEJ1%2FZr24TIk9Hjo%2FqC7DGPo7cnwIhAJC%2FILaM8J0Dtk21ZfB9wziG9YFJPO9FH9MFS6YOQ1cIKv8DCD4QABoMNjM3NDIzMTgzODA1IgyfGf%2Fc9zWY%2BbgPzuUq3AMTJyzkjLKYcnUXIlZgJkYUlY2FjuYqM%2BP2Hb8QLtbLZ9TCXZVDVwBp2kx4FOIRMIDW5Ja13Q8uCQ%2F3h4%2FEjBeIAcp13tT5Wf3zNv%2Fl%2FmflNI2%2BKhvFp4Nr8x3WVBy7lQF3%2FppU456mwi0fgNE4%2BT3JCuUvNmbmAVqjABp6rd29MYlvFLSSayq5kISIQy%2F8bKIvexK4tPEYZJXSe92hvj6nh5hubq%2BV7Kgtg%2B43ub3ahaYQ%2FsxDkSYDEXdzN1qZmreR9nXUATXox5tE23xeoTcBa1r5V%2FBZRWnOBalqT2V467KDxAzW%2FPSy9kEcT9u1iGgPpaLD4FV2yg0lyp8olLfC9GOQUK4g%2BiG6gr8chWcsS9zUOCtLQRSchl3zx1Gas9R2CUUtmtJAQOx%2BWY5ex7hVD7wSNvAZ1NNE9M4KeMt2Wv5dfGENUXGii0bnvD6v6L9lOVKHCksPTyiOrnvb0zTsyCGv0u9arnIw2rZosFzNn%2BNhaKugb1lamDHMMuasuGFc1NqmPsdxCqiuAgNb38wX5G%2F1A%2BxEyjAzWqk4sh9qyAsayhQz%2B2WKRsK29wgAqw5Vg1JKE521%2F8uXUa1aMtRM8Ax1Q9g%2BzZIJWLf2dgcVxCrwSzJIbdhEJyWLXzCv3ou9BjqkAW2mpk5bgFlsCVnmEjCFAxso2WULbEG6G4fkMjJMoMsHFl8q98b3c1Cpz2S2QKskz74AR87J9WWFYo8G%2Fhm05H%2B75e6F6spass5J%2FllfHktVVSkT8NuDUfEzH2wszg3wow7WBHOAo%2BzQ1zS7YNPh2%2BL6N7kngXKjkd%2BtoJAomTJf%2Bzi7pWHC2%2FiWY6FAe%2FaC%2F1GQQMG7T7Hn6zThEvUMa87cMaCc&X-Amz-Signature=8396ece45228f02e5d33cadac78aa8e86748a12c8684be81fdee70f37e40a8d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T726LOJ3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCICGOzect09f9RiMhXsOWEctXPxpfCrnrEKOU9eXozC8AAiEA3AyLCqI3ZwrcphGsolQ1UEcU8s6T7dBRTL%2Ba7KkKUXAq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDGt2dtc48BIuRja47ircA2FZyN5j5Xa3zoo8VnvlnftMV%2BDWXMGcB%2B9G3WY8SdvJbm%2F4XlMZCFfg0lEp9MzKAYECDQzwfjciQH30n9%2FfmZb6m%2BmNwV%2Ftri8cmd%2FOMUBGuFjJprlNBpmLp3yuCZ9mihexPPQCmX5l2gYP59q3sj9jr%2Ffl3YOSeg0V48nijR8VAiisC7bwYHOpQikAHcYiqQZ7HKHY1c0F%2FE7ZYx%2Fp%2Bi%2FB1jR77FflZ6GDR8VUyzNPJ%2B6yebRwjXwIPDtn1QB2ANPNYrqjlf4WbQDvmtZnlZDLVJkFbS%2BxuT6BwqUF86IVglBtkmHCh2NMd4p3AE3YPDoZKYON0Oi74UieHizgZihqToQWvlJivnbqhi7NYTEH3elscN1F8lL8ygOPigVt3FLiM8l3v%2Fpf2pQQ0Mfbn%2FDHngWKnRuY2SGYbZ6c44kawYimLzAmYNTNMJHdUw4ZiLSET1ITn%2F9py%2FSceWF%2FJyP%2BkaNPNMgHFQe6618FyaGofuMbMUlLkP73BPPTYG%2FnBNZTqMR9a6Dyw9gXtdF%2FP03NcYyr4xPS5O4jn2Sw41e%2BTz0xGmLKGjBVn%2BLIBFqQEtPdETKF6oDjw8oJ0SZVQ%2BIAAjBOwBr3Y9M5rF2Q8ptjjqtvRDk39I23Yx8jMPrdi70GOqUBc7KyY47jSPMfsYqWDRX5Wl8wwbMZoW%2BZnVRsGyqHDwiKw0P48yB6oO6pg3EwXEtCV4EqfAAZelwjowDHd2bXgu1KJZTbedqmvL1t8RpvmqzuiODy17U8tqqjGSp0Oh%2FQIAXH8c170yP%2Fy43yBffmrzYYzemPVPJsHgfcZB%2F9Vt9z7iRDAJnmFYHCTVd%2BoJGn4eacr%2Ffn236HSaEKsilFEQukR3To&X-Amz-Signature=a3776ff49923e3183b8614c8938e363628301b832faed278177f7adf8f85791e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2Y6DID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICXvVgGa2yBkY0TJ%2FTpkdGs0ZAHx2wtpJYpP3M3I06wbAiBxXGT6snqWWfbRr51x3hrqnijxVWSzI0sT8WKQJK8Vsir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMKAn1VleP44mi520AKtwDqLnVJCXPX2bDBbvDqp7oLONK0HzCTt1Ob4zyAe12WtRCWhtazlEo7yu7QmelVzh6ysoqgkF%2FAOe%2BKrq441lZ9T9HncX%2FSJHHX%2BXSabQRSR%2F2mECBjF3t2M0ZkWoRg94OUhy3HWXRqlftJL%2BhN8kLqDTMpWtjy2%2BU4i8fq1RuPJKg%2BqSuFWNPvVcQaLpQZpuQ%2FU4jqpK8phgOxjTLsDllZ3W9WI6KehpmJs0aQ%2FQoMwAHXWhTz5clAuq%2FimZUUzplfHoVoWS%2Bge9zUxKT2aEe73QFPG0ID45ECUv5TdfECV8snlApPWlfoVuKuAuo6hpWBZ8IZy%2BMmFtJkhWr7%2FCra1ZNzkVT3YDP07KpAdOd7QYYCWkuBefrdDEVJwXx4y5PYL1HCS2pFbozNr8oZMq0LgNdoI5OCHRcXunockcZd%2B8thREXdIqosv5mm4uMEhRju5L%2FGUa9Nmf0T6ugUtPRQzOh69vBr2tTeZAoApgEbE78pXyVCUA%2BQ8MEYw58KNDwlHtDPuMPtY5wgnL1rJu6UanA6VULzT3O1bY8S1lbi%2FHEWASzhffANy81lo35U9w9%2FQ8MJVutgZiZMDIhcWtSERQMx%2Ff18YRHEgVSjz8RgAZIkWgS6udzBfn16Ukw992LvQY6pgF%2BtVAhcwuPa8gnutAKms6QFib90u0kynsZbFhTh0B5oYG4SxglK99HAP0vwkgD0rpsl3%2Frsf05nm6EnjrrVyrEgFjR1EMw8KHv792WslbZhat2QAcmnAptuXj58Q5jfFDW%2FaEiJzOEjhcrMPg%2BETv%2Bnyd%2B9C3OSbqwsEh9k%2B56xImFFh4o3Kq66iftcJm%2BTpHa3Qwc3hEkD07Oc2p%2FIwKzgNetWkPC&X-Amz-Signature=77e28ca38b9fdf4d16deca331f2311436cb21c081b541ee62eda81cf575d56e2&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTPV5UGR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCICGFEELnxHefz%2B6kMBW0xCvOyF9w%2B64nNHK8hj64frdYAiAWMfKDDZ72vX4V3Nqm%2FGFMolbO9jKRh%2FAIieIcJAOU1Sr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMGWNUBkbi8R5hmZGoKtwD9SvSxSx5UlvvvSNSFlID3T%2BH0ORTXsAM4ptdhRUZs8PUNLUMvM8tRGThCgcofgyMLclihLvLgs%2F5Vd1qLl3JN1IRz1XfStck6Tka%2ByMk4yxp8mFuOxRuDo%2FuRU3NAK%2BpwyHE0OPcizG3KsrBpV5JSukwai4lGBAld251ByEvXq2pkf0bCpQiyrM0%2FfJGjAe7WnQUWL6zhZEan23%2Bu%2B75vVsY0wLvNbJrouApPbGU1nGqIq%2BIXX3H81u%2FoAirpYi6nbPWFSQ0JB5gNsj4163G%2BSbalakjR9naJjQnY%2BI%2BXnGBbcTHA01ixnHZkHm6E5HEcy1on0V4aaq3TJqlQVqY8DvsaZlTwrzvuycgQ2MU0CICk%2B5s6CO9Gf5kzGFagX37tem4j11owoM7SXGXbReeBCRZnMKiQAylVn935Ndpa1KyIXz0ZsgK%2FwJX33QizU0IKOfQq4z2%2BKPS2MTweVowuSij8RW0K%2F6P2hNZBcg8WZV4XYUksyQmgexswSCJuvKLetk354thdXEIkYXOJ6WOGEiHluqXBZdegW%2FfPTPsiOhEqCijeSUYN%2FqfzIPua6Vntk%2BprHMkSnt%2Fnfoc1SJuxkzxIXi9z6KuJyETe7GuRfLVuIdrfJkJLgtqq74wu92LvQY6pgG25TbWNi%2FlGOFQ%2F3t9T%2Fkj4Xd0nI%2BRVcGdkVM6ul6XUD5FKdl2%2FcXmDSPuAGB72y8sKzxhfRXHRyV50s7XdG6tFpuaecqkbEL5jluL5ilREzJCfMirGBNZ0yV5po0s2CuB0CsRsumD%2BQS2WpY7GnHOmY8tvmmj9nb%2B6zF1oTva62VUgNkqs2UfeXMFDBq4Xlv4FJ86dHwFQHLN1RjVLxWmtBbsP7%2FK&X-Amz-Signature=09683c0a7be8e7145c45e45cb97e8081dae3477ca025d1ef450fb3e32ec96237&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LIYZT52%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQDajC4vruVS%2Fw%2BETfuNGxl8GGLT6CDAXMl6MHV0Mro2UgIhANF7P2GLUVZtKy8OkF8VIyMxSmKMb3otr5CVxwjWnr%2BLKv8DCD4QABoMNjM3NDIzMTgzODA1Igwhute6hWcL5chkKAkq3AMXV8N%2Fcv0l4YmDVpRdTzoU%2FHjFR73WtXmu7bJ8VTuQ0FrzzaLrwLX%2FVGkYJZNkfN6E6kzlTLVapO5vNxS7zj5Nqs6a4U5vaNtJhYLUJtZwTPLQ7q41WjVyvJNTIEi4aOX7J1Ni0d4EGVVwNPR9q4P1rZJpOkGBK7tW1uRrb4I4cFZ5H2uoSvYaGGmO6I1rAZC2KGG4DeF852Ol6J9rbM53Oef7kPSV9ADTuKWUt5Kg%2BGvZNLk3E4TBRgg%2FvgDU5KMuUSdEDvg9ZqWvb%2Bs%2Br%2BNrkai%2BdaN8WAsNOcv3rJsQDQI2hvtVuSRpVdoOx%2BQrKTivT%2B2keqWg1Lq3Lz75JvNQGJvidb8r5kW02uMfg8YHG%2BWeQACk9C8vUd12%2BePMeneFP5HbwG4zOQhNkwtIG0wVzwTT1HFM24wNXK17Y5fMrag6dkFkYtqmzs4V4FsuJtxxj%2F%2F%2FE1v8rJedxhpLqlkY3FKqeQTLbJjg%2FGN8qwynTaWE%2Bok1Vqrr66EZPgi3ZS1dKeH86L0bGtN5BXl%2Bx6p%2B3mUWVaVvKJwvVsu%2BdbdSajj2wmX9it85nC%2FBk57sd82LG1ypxIWpUxKqMpuMEF44gHmV0otWEuTqSjU64EDiTGkaNlMpiiJY%2BQwc0jCI3ou9BjqkAZbnWvBORbO1BiT13gZynwPqJpE0nUlUv%2FlMtNFOhYKYpMn1B%2FjQUEb85wyXksPEZbv6IcNH4sXSOyYVOQ5sesG6Rog4n111S7ApBVzeKVxC9BJgNg7affAQCFe6po%2FCJNBnLvf6hLlrPelTtTsi6MFwdpibMCIYJtKYe6hrNo%2B4lzVqchimNuit7bOsIqGGsCeZMh3tdwHAd2pbXkva%2FuukmZmN&X-Amz-Signature=4f052b3178ff80d0a5ad61424780eafc9a75df9b010c184b4262905ea88abe46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T726LOJ3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCICGOzect09f9RiMhXsOWEctXPxpfCrnrEKOU9eXozC8AAiEA3AyLCqI3ZwrcphGsolQ1UEcU8s6T7dBRTL%2Ba7KkKUXAq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDGt2dtc48BIuRja47ircA2FZyN5j5Xa3zoo8VnvlnftMV%2BDWXMGcB%2B9G3WY8SdvJbm%2F4XlMZCFfg0lEp9MzKAYECDQzwfjciQH30n9%2FfmZb6m%2BmNwV%2Ftri8cmd%2FOMUBGuFjJprlNBpmLp3yuCZ9mihexPPQCmX5l2gYP59q3sj9jr%2Ffl3YOSeg0V48nijR8VAiisC7bwYHOpQikAHcYiqQZ7HKHY1c0F%2FE7ZYx%2Fp%2Bi%2FB1jR77FflZ6GDR8VUyzNPJ%2B6yebRwjXwIPDtn1QB2ANPNYrqjlf4WbQDvmtZnlZDLVJkFbS%2BxuT6BwqUF86IVglBtkmHCh2NMd4p3AE3YPDoZKYON0Oi74UieHizgZihqToQWvlJivnbqhi7NYTEH3elscN1F8lL8ygOPigVt3FLiM8l3v%2Fpf2pQQ0Mfbn%2FDHngWKnRuY2SGYbZ6c44kawYimLzAmYNTNMJHdUw4ZiLSET1ITn%2F9py%2FSceWF%2FJyP%2BkaNPNMgHFQe6618FyaGofuMbMUlLkP73BPPTYG%2FnBNZTqMR9a6Dyw9gXtdF%2FP03NcYyr4xPS5O4jn2Sw41e%2BTz0xGmLKGjBVn%2BLIBFqQEtPdETKF6oDjw8oJ0SZVQ%2BIAAjBOwBr3Y9M5rF2Q8ptjjqtvRDk39I23Yx8jMPrdi70GOqUBc7KyY47jSPMfsYqWDRX5Wl8wwbMZoW%2BZnVRsGyqHDwiKw0P48yB6oO6pg3EwXEtCV4EqfAAZelwjowDHd2bXgu1KJZTbedqmvL1t8RpvmqzuiODy17U8tqqjGSp0Oh%2FQIAXH8c170yP%2Fy43yBffmrzYYzemPVPJsHgfcZB%2F9Vt9z7iRDAJnmFYHCTVd%2BoJGn4eacr%2Ffn236HSaEKsilFEQukR3To&X-Amz-Signature=793d39ac0c28a4c6a6a2c6637f0d8b5cdbd6a7703bc948dde8d75eb51b43ab50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXPNYDZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIG3TxzDFJkkRKl5xUmM%2FhkdcA5w%2FscJTw05GdI4GpEkJAiAsGGPfcdpj7bT2d6PJywKFtKPdTFK2IfETbekJGuPBkir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMUHwC4xkO995hx35YKtwDbntzPGQZNieXk3sWc%2BdLywwLyEe4eVR85rKc9O1oO5Uj0jKsZKiR3Ei2CKtGzfU0pWvMuIpCkK0vZtpBve4QxZsmTIlVYyCmUhPNHNNIDFBiq3I6Er8Cs65vpZs2uVQwDfsGpvqbHd1PGoS5gL%2BQh9HWprXmLG07x3juAjCf6A5w4FE5ROuewPupnPwpXq5kHyatHt0U3G%2BJWLtBNXzrxyRIN0nMM7DnfrZESfLJXs4HjNzTLs3btpooxvY%2BxWBB5kcw6UsCUURSlYlXODb9HFgP%2BWAv3TuZHqVpmnFDRxFkMBiMBiXUYSfPU8%2Fqbkk3c2INAVOmRS2BKM3xFKWnO14hPWpBydQkr3Yghp5MQjeDtpcYaHxXDQWA3NqJOfvI1KEk1ciQK4RC50YyanfnsYjrQOLxhNAbvywi%2BUoC7XVaYzEfUDKecSVEv19S6vwBwlxuuH%2F3N9GY3s%2BWI5ONAMQTpbBwWqSmBiBVsMjrOQyFYuuDU7YoO7Dt17r%2FDCOMP49pSmDyn3qM%2FJo9hI4rlbQRF8GpZYicAb%2FUZSlbcJA1hTYVwBf4N4iBIaX6bZwYd1uSUucamwRuC5fA1kdeJfPnz9m5KK50PqJHGYL73d%2B0shO4zsuk%2BjQ5y4cw5N2LvQY6pgE9rIl8PYVrANVJZRGeIaIlSN1iXzr6BfFFuJGR51QCnzEPoVhpKX8bQCuUIiQ7%2Fm%2Fc%2FmSq1Z8CojDXvzpQVJr1bKcloPHWv2gd700ohmOWXTl6Ynl5uKt2qTYcMLVrwH7M%2BGCLMHyC1%2F%2BtFnCWD6yFg6FqOyc%2FILH7%2B%2B0GKS5vwqo1OQ3K3zhxlW2DhPFxgUNpwrTeTtWIqcSQhkxigaK2nau8nd2h&X-Amz-Signature=b1ccf7d9b147c5bddaa5ad3984a6bd43a62855e01313ec8c52e5dced577a2bf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZXPNYDZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIG3TxzDFJkkRKl5xUmM%2FhkdcA5w%2FscJTw05GdI4GpEkJAiAsGGPfcdpj7bT2d6PJywKFtKPdTFK2IfETbekJGuPBkir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMUHwC4xkO995hx35YKtwDbntzPGQZNieXk3sWc%2BdLywwLyEe4eVR85rKc9O1oO5Uj0jKsZKiR3Ei2CKtGzfU0pWvMuIpCkK0vZtpBve4QxZsmTIlVYyCmUhPNHNNIDFBiq3I6Er8Cs65vpZs2uVQwDfsGpvqbHd1PGoS5gL%2BQh9HWprXmLG07x3juAjCf6A5w4FE5ROuewPupnPwpXq5kHyatHt0U3G%2BJWLtBNXzrxyRIN0nMM7DnfrZESfLJXs4HjNzTLs3btpooxvY%2BxWBB5kcw6UsCUURSlYlXODb9HFgP%2BWAv3TuZHqVpmnFDRxFkMBiMBiXUYSfPU8%2Fqbkk3c2INAVOmRS2BKM3xFKWnO14hPWpBydQkr3Yghp5MQjeDtpcYaHxXDQWA3NqJOfvI1KEk1ciQK4RC50YyanfnsYjrQOLxhNAbvywi%2BUoC7XVaYzEfUDKecSVEv19S6vwBwlxuuH%2F3N9GY3s%2BWI5ONAMQTpbBwWqSmBiBVsMjrOQyFYuuDU7YoO7Dt17r%2FDCOMP49pSmDyn3qM%2FJo9hI4rlbQRF8GpZYicAb%2FUZSlbcJA1hTYVwBf4N4iBIaX6bZwYd1uSUucamwRuC5fA1kdeJfPnz9m5KK50PqJHGYL73d%2B0shO4zsuk%2BjQ5y4cw5N2LvQY6pgE9rIl8PYVrANVJZRGeIaIlSN1iXzr6BfFFuJGR51QCnzEPoVhpKX8bQCuUIiQ7%2Fm%2Fc%2FmSq1Z8CojDXvzpQVJr1bKcloPHWv2gd700ohmOWXTl6Ynl5uKt2qTYcMLVrwH7M%2BGCLMHyC1%2F%2BtFnCWD6yFg6FqOyc%2FILH7%2B%2B0GKS5vwqo1OQ3K3zhxlW2DhPFxgUNpwrTeTtWIqcSQhkxigaK2nau8nd2h&X-Amz-Signature=24332bcbd886f3c49ed2ab48ea3649ebcbe0e8b8a73b12e322c4381621cdbe49&X-Amz-SignedHeaders=host&x-id=GetObject)
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