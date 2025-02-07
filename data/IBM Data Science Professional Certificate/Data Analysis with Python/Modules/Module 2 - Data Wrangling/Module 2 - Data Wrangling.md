

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI6YVOA7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQC1oCeLYIAQegAT%2F1WvfGUb6nfgfK4lm4t%2BVWn6B97nMQIhAL4QN5V2%2BRfxycDbgW5hf0FsVw1GBBWiFFTBMyYct6QQKv8DCHoQABoMNjM3NDIzMTgzODA1Igw8lVtFLt4QR6wWKUcq3AOTYGYWJNGMM58uy8IqldehTDX94%2FHcwsSmMcsNRvbofTDQoNg6PwWngcGQ6wdw%2FIShLqUbiotaHbiJ1mV5I0d7Ajj%2BUp8aHV5jr%2FQe5ryGU1bn8n3706H40twjDWjv1n0amrw9cwYjuQx4c4rIpnu8oJeJTmMxWVpqv2RpN0wejatAJAL9iItSpJ7NSp%2B7PAKEVKND3lOr7hG%2FbVD5h1FEq0rL9nhkvxQbNuDJFSk%2B2L%2BYjieqsqGB0VvkwbESvPBhpf%2FXlnquZpDxdXXe7V2wmyJgbgQIAzrwKk1x9d5v%2FgAsUKo%2Fbwdy2EYj23yhSdzAQ4%2BsosFvaDIa8zON0rLwKqrlD20sHuidu6YXCZsEBi0tZDEKfiCywGU8w2bdgqA2UxmOGAUXRmrENlkI0LSoWi778u2Iv4V9pHx%2FNdHgCN2TZtrbDn9C0DIDgPLl5%2BkWvOhcBjjRIR2HXOLF8Omp%2F576axzgL3L49SKFrp7TW0NfqEQk659LUnCy%2F7FNocqjJPVwec%2Bi9GOXEJnnH5dXTE1pwiHnH3Q4%2Bz7iExdHdjvPHjSyt3YI6fRwZodhFu1iHK89oWlmTdDeRzT2S7Vww7Tw2AWQlwdLPXpdxEZsqrEazfpacGmPL7dqnjCF%2FJi9BjqkAVCHnfCX8wz8617HI%2B74L0hGtkgv%2BiUIycF1%2FgJdBIaR0qRCupG4IKNA3K%2FQSx06ISeYLtbN2OCS6rP6BAe6kOy8aYmgJ3So07owGTjGWIRiD145yfU2ZXsbh8r0hZxpSi4RDXuT8E3TDTy0gaZZ2iTJGFOdSTVTf1UFN%2Fdi%2B2n%2BSOF0jLz0I72pdY4y3FzbQEgwJyTd%2BFda3HUNbsY3Z4mAl6mB&X-Amz-Signature=ac437a211ad009f5883dfe5e72cf81a9e83aecab5542a06d62e09d2fe2ae148c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXXCLKJT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCICuBRn6P7rF9iDYYqRJJc49%2Bta0ii6%2F4lXh8vFf3vyUgAiBqWA7xsBgeVCl0uOsbG2J4rg2XC3Qp%2FJ5%2BVKwY4DewmCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMILU0tYPfK6%2Fq%2FOByKtwDeTNY%2FacePgknnGmOlrAj5ZTFwddF7UmSiyk4Vd1QfnxAFRcuuU0U1%2FfSW2JymNMB3Or%2FF6EP0PgJLLWuvERgTIfpbijb4SvpN0dIUIAGM1OlvsXbax%2BSta6YWzvFc4XFzhiAtUpXjTPVnXPRLREgLT7wFl9iuiOEGVJpkd6rvaL%2B4R4PtdqTBESCyeL%2FUcjp2nt56nCRcBf44muC43bI1rvJGflEXo%2Fedr9AnNs7HowNLqvUaGEJGY%2FbTjl0RKBHFs16%2FYw7S%2Fn%2FCtTr5JRDwB8T1j%2Fzj4QDUjiBYBpMJK2k1JS%2Fw%2FAfvMB5frxlcxK45jkRT6KqBVudrwfAaEbxWID%2BZYuHqyTnn8Aage1tMVhNG0a6GjWbidH61c5UQv2d%2BJuwCgBrNi21TB9mS4IAlkx4%2BINeu9fdA6gsnbfdWWepG0V8Ui%2FA3OAX2VplocUXzllDwDZ64ZDt59cPXNasXVypbloqgtHH4pcUBZHCcPEtdMQ9R3b6wXBlFf7ZdfC8p7SXhxmJNO0oOJbQQcV0iEGo1%2BwpZobPVLAISukgEd5dlDyz7vo4SGjm06lnW1Gb2ZAjfo90FvWv30fINI6tASqkYF9CLfVROvC1ig4wKR3qDuv6HCL5OGnT1N0whPyYvQY6pgFiPPbf6UvQibu%2BwdQBfwEMPI2zBmd8Zc2%2Bin3S3PTrzdMGrdKT6qg0%2FoEmqu1sR5swfNewN6fqKGH%2Ftz7bvuiipyaNsY4%2FnZ4YBLYa5WeX8GdB8AheufF6%2BfYjs3p1tRYQlkstlTVsp7wXFa80eJ%2BrYGMuAxENjNSEbFI3Vbh1OLz8XdwSsWEPr2DyDdakDQA5Vk8RhWrO9B24o7zgqRpWfdgN9uDf&X-Amz-Signature=30f3c0958aec7bd73e90bf0def1e3e7327b4341ede75cae151736314352b1378&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJNXRTRM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIB69AVeV1M6lbCnHgyfFRX5y832AWbInRl82YLpF3PdoAiEA8G%2BI%2B02dzi77qIh84ngjqkRwl3hKteolhTJSwqkoK1wq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDO9Qxp0B6%2Fi4qIz%2FdircA26b7iKk0klK8srGCV9aMLrAQ1vhqxodrQwyzfH89DmqcM2NhV%2F2V2AYhQ1wBIcKstopLj4Bp4oUPIsM2Lpkq0I80aD7tTQqCVqljj5MEZ%2B1DEVOTx8vgbn4biJ1CjyCROU6GYN12bFLdM38hay0BKMQYEOJ6V1wZ8Djxh4ukAZBW7bKRF%2B7WAI3ecaY9RmOrEnRMd%2FPfC6l2nuoSKnmL4dju553Spe41R2ENzk7gpLZtlG92Cb5GDpPQp5SwujkElS10M9WKX3OI5Mr%2BS%2BYVrygY3%2FuH35KZrkKRNkmPodWboEcPVIFgWDBrLJOzUDZlltyIUqYat9krJTBJdn7p5Wnr1BCPW831sJg23u9LwzbSgUYzZWHd7Nx47AqgzwBJ5g39xA%2FmuBReVbH9V6TeXXolPAznnNmc5WNLo%2FaaMokAnD0sb5dUHzX2dgwSFFSZ%2FtneGaAl%2FNMqeZvqG4mJZpcgnP5m1eBtgAZDR%2FAJrFFjwCXaFTvIy4K2xqDjZN6SGDAxDLZ5kNXOeCS1ZnRoU5hpmJeR2Wak8b3Doay6iD813qO3Y4OycW8i6j0n0mQMrGTqnBtKzPCOEcr8jETwrLQZqcXHkw21SCm3u7sGzenqmckcctbpphFyl2CMNb7mL0GOqUBD47Ivfkx0EbR9y2tGM5yIfcWZRhcmfS909bumbhfP7j1y1%2FE9ptc7jrqKgNwVacjf3U2Zu5gg1WVfjE%2BPnZnw9J3T33YJnlfD%2BQxJ1yVzzAP5cJCoAGl8ImF22SLiqH7ES%2Buj1oTIgso8hPuuXDoCgCkmAe2ZWYLYdCO9FEAN%2B0MGWd6%2BfYCIehijELECy2SY3iqIPua%2B7glDX1YNa8dVU1gKvuH&X-Amz-Signature=6729e45735b83ff9af7b5ff60ce3c9016f9349c16c92bf6da1a10921756f4f61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRBNIRTI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCICKe4pJbhZX2ZXUx7CDE57Xzlx3XuCdA8LDg52EvViFyAiAP6mDFaYDtvdrJxT%2F22Elp3ab3xVvxRrtCyGzb3JqKOyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMtIOf1jo0sZNx2%2FW8KtwDv%2Buo9e9OnTJpSO3Be0408xXAjzhRWQUJw8IDREKYRk03EH0ZIRC40iCZeGgi%2FHzWsDefQR6hTMwCo7FVYBId4%2BhygubOeiS6nk1hn5kL2fVkyY4C9dshI12fIVNso2%2BZ%2FbyktB4mJ80q%2FlKP%2F8UWKU9JEUp32S4qfSWZoldYBlu5VIrq0oYnjUynk01v%2B8pSpyr1tXPJzH4GGLfXTvjjA6dhHtTFCoPJ1kg76dRze%2F8JJ9FSqqMg3wFuNkiaR4me0Fp0jLFmAGFr65%2BjqW0fH7rsOX4gGqDXso8cMQMCSOQUVwMuuPW%2BQJwYNeaV7k2NLtfvCDNZBIDf4EDs%2F%2B7Mnuf%2ByCYSp6M3%2FQG5WGGuXNzwC%2FzKaalbYIgnCU7D0V%2FFffZH8A%2BFKDouVu2M2l74Ulc7%2BV%2FTuS98D08wiFy%2F2sIP18oIYFzobFH6YAzpBYKJMyhIQmaixYtqxfdVoqe6jefwV96DhZs90rJs7JKQf8dbHNKOHu6kwTHnLj9lt9AVe1wNY6bszpWPaadGYkIvx7Y7Qq5FlYZ%2Bu1k%2BV%2B3aATKNJi79mjmEOtXu%2BZV9F66fE%2Fh5H5Vtk6p9zDTTDwMweD%2FrzMdHsERGvfXJqeQd7a9tTuBWF5TYAAW1GfUw1fuYvQY6pgE%2BdilSLu%2FPUFAEeEpRfBWsVl9OT%2Bwwym4ZSmSWS0N5ErqIc5YJmzRfTSTca%2BLtgFqNuZAp%2B7Fk7wDoFYnY8clTLqmZo0NUPwu9igDmHfBMJJKbiZmqZCe1pfYp6b%2Bqqy2NwP2SRpPYftfPXdMAOzGX6kgDNnRrlP79U76bjAdfRGpkNZwCRkNINv1Q1FEuMn%2FqQPDr%2FLI%2FXv5%2FpwFY1uQEkk2uE6cZ&X-Amz-Signature=33f99ae3871f1dc2b3a233099e34b9f5c85e89d0e36bea1e73c5f45912d06359&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDW757HV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDFUnkwoRAUIQUjJHfbY9c%2B4PPCqTnqK%2FAhS%2B1I10qlhgIgb3P0YqFqSkNVXl2sbvdCDYGgwzpqyYB9Zpd7KvWCwQAq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBIy8K0dTUAHw4%2FS9yrcA17YRoAf0Rsi2gAYqeE6egyFmVp39elrluV7wJAPgo%2FgFbsSfvGbcsTk%2FDwuUDMSBB4hY0NuBoqsH%2BowNJXSFdLqGmcAr6IW9Hf7DvmZI7x1FgiYNFsk6vvGOYZm02kYh4UtFaFAb0xS4XakolKQlaQvxNNbaG%2BLi%2BExBiyVjbpoS%2BwPYZQ1CocPCgJPsu1Kr%2BnohDLWLOWfaB6yUK95mUnPQI%2FIjsdAfVkh1CQH7ovkicnLNJQE9I526oQ1ux3WC23xN1UfGyM%2F5YHP3GhZa4TX5P3tBazg5bs0sHe0wNAxvGnlypsDmnrdcMrvSOthWWKUZlC3dJKdP8s%2FFiKpV%2BCpSbIHKxIYeyfTUFQe9hs3ek%2FOdZAi5dCT%2FQrQCMlgUhFbG2Cdjdf0tph68lUQoeeU7Cv97vBGKLanLOdJbiyw4j9QjqA9tsUV1DsTRpqn7gYvRiMSPoEUwRH1ktlWq3KGzHh57pVedUOnr%2FVrNA3C4gzGiJbUDjWUwGY6eHnRgturP1wyn8DExwBsiKCswAy5TbgZISuZRcRuXmVVfaKa2zfPTdpQGag2W6LWBvunvLnhGp5g992APlGYtz0V%2BVhzCpnOlKIuF2xUDJTHS2cTwFYOj5yIcMepmZ3aMOD7mL0GOqUBbRgqt%2BRW79%2Bmh%2Fzi0MBagBWo0OoN%2FZIgQCV6xlQPzF%2BESayxFR%2BmFy270nKRxrx2LLxLNzLHVy26XtfZvEOo%2BrdzUa6auupQNn1%2BuydnpB9Zxx4ZbieNliJY%2FmTWh8miyW2%2B0s3P4jdmKoxdFvQCJr5XwTBwMmWZ8G62RJD4WRb0PsmUK4Ax8WTeMajggkvz9cyV0%2B7rJNYMV%2FKr4l6%2FeKYP4oau&X-Amz-Signature=a178e2ff9a29bc7983618aa2a472391b40994c6d7f48e842453b79a11dbc1a98&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFGEUICA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQD9tQ0irMxpEGL6E5ze6KLGV3hKjSXa3qaIbWH5qeSALwIgH6ECzejN5JXy%2B07oGbGijF3N0AgsXXU5kyAytajR6DEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDMnAAOq%2FegIRMgyOsyrcAxeaRU%2B%2FM4kxsCHl02vm5ZRehUXUSARbzPNIfIxrbUwWn0MGwFic4XmFaReaMwXk1dqTsSw3ALoDfZEU6DgqZbWSIO5VzU8b0Ybpb7oyhgCJXvJUv0USqJIOwd13h0O5xTdB5R0btDiOEmtqOjzujRuYkKtyvGOvu0e4D3zt5Y7FVAVANV9C%2F2qjrW4LcwVBooN%2BmuM%2F%2FtcrUkkFwHe2QluhglOfkQoEsmo4QNoiNkvGK9JpZD%2BJ%2FB%2BT6Ak2Niq83NNnnQLhfWIuL%2BaKJBmCdyMrcz4hYX826O6bOGqaNIDZjavd4YqW90IL5oB3zoBfBoo8qsLHPXtkvM%2FhZpxsABuM0pK5C%2Ffgv09S%2BObIC%2FsPMkxQBb64BnWNfATHRqCKHve9fS%2FSP%2BGz7uz3IRBt%2Bb8zM5u6TEaxUsqaNstB7cVo3mVEUhTB%2FQR0EKCQyiEGYlsFgPpjHGOLWzGtf5ttfiDm0KSJg%2BIltRG%2FSIE1F%2BSFkDpPim%2FV8rQLYOhfWYtyzYRj3FV95CE34tf4KSJhYU9FFEanSFCUMhZZJCfoHO6NHbhkw6JjCookFjq8btIaQAfKzRp6O%2BxTrqVuuHQspyvoeU%2BLX%2FwIGXLf%2F4FsCS%2BU7vU7VfiU04g5UOIbMMT7mL0GOqUBpyVSyk6J3%2F7%2FDb1GCt90K5PulijWgvv19CfWbYltmhGkSnQ3UF5JBJoNdX8RjIlrTyLPmh1EvDDUMpsWePgmHor6i9ZLUb4R4ywEh%2BfPv%2F1Qw3vURwwZyhKxIkYzi18cRCaAoK2D2FK3QWSp0y2JHhkEv6OHzTRiPgLuUjniGaWR%2F1JY3SafFskis02%2FJ7mdyr%2FRjxpI0pxcpI5S%2FdbnbzB%2BfmVV&X-Amz-Signature=fc0cf158cf4f422ce17dd928628d95bab50ebd6a2484fcc836fd1c96dcbb3004&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5H24YIB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIGfHJ2P4pSIvfgwYLrcLOWd8X6NiAlP%2FcY4OB7IHpQhcAiEA%2BzWVoARlsjMob3dbhimU3T8UXFSXrjSeZKngVvafZ14q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDH0WuXfTok2jwVRC%2BCrcAz7ByuLm4ndF%2B3i0sAolc9sMKiSPb1Eyd1INwWfiUnOX4vm0tSuap%2ByNwBPnFldOePRZGy6T%2F83zX%2Fsmt3gb1vJnux0hSbIk70ePT9XvC18bYVm2croKcCd2Qlkk5ZCEHXsjxKrpOY%2FdmEcJHYKULVQRBZacE7emDlAX2SVSWgGog1Ui3ylzRf1FJB75ENolVMg38TSv3yDJJHqfTS%2FPND6onpLNQYg5zEdWZI58c%2FKjS46wCSgjXcrtjICe0u0O5nKDz4dbmWNf6SBVA8tupAJ2xVZYytynasCjhza%2BCvQh0dEy3q5QD3%2Bj%2BdV%2BZWzYpFu6PrnSVfqJe1rVzj04qJkZaOzy3cjKH5KK%2Bbm6nYcvdu%2F5DW12GSQrL%2FgiGwUUZ6jgBgwUHEq7MlGlPzYp25QksO9B%2BtEUMwF1N%2FWGQdsZhbnHrbXlf88FOvwagV5qAweEQ8N0vEPMXnMZSLC4mCG6puYCJi1sQJ9FTRjmDjUn9ptLx4dq8CTbhoesZ%2B3Ew3H%2BPN7wv1uMO5fSihmrU5nQKAv%2FXVRwFC9M2AAevsoz1QM%2FClgSXkIwLc8nMIR83YFxK7oo1nc%2BZWCMWYy3c6%2Bm0Tvj9oHGKLoOUtUmgOuZJcljCzZJCC%2BiBdNUMIP8mL0GOqUB6XFiJP%2BH2d5U4rdtlbhjpiyKbUfYZR7NZGZpzub5WwcVCEZjKGpxqbB5nFTzOjFOUXyLUfVfC1XLEI3Oujf2DhWWuCatHGiuFTWuP%2BxeeEs0woezJ3xu3p1ozPyXkiW8vnLn5RybBTIvcg8%2BPzuHD3JaULUT%2BydOKu3k9WUPv%2FLXyFe%2FMf6pPk1rhOktVOsB2WvcA6%2BDDdsyERPJAPWvKnAZMoy%2F&X-Amz-Signature=79bd17b5bbdc3b084c453bc896e341847e408cc5f4d08fd3d40751d1c7d4b7fb&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLSRLXWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDg3lJp9c8Gkwu%2FNLIdDKTljmS%2Fwn4vX1SATvLxRcOpLQIgSuqbteQAJeGwR7UzPQphyhxu6JA6Mc7m9Ny9ojZ7qioq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDLAXge%2BnXnZHoEd8tSrcA%2BL5cOpj6MX0Ku3aUb0BLly5bItcddm0eJVzao61QQltU%2FP%2FVYFYUCHaahhy9lScyox55mAHF73E7KvTRwTMYqDWK8e6ojdG6xBOdJe8ZvOgS1TKXFfMLlQOh71vf5OTVYiO2%2BatYmJ%2B1%2B9oaWjDtajzUxNlrgmjXfiHLR6iS1UmO3slgCOCdom3rVi2KexPpKXhbtlzgmxiegZpG3tCmsqbd29Dah3dkVrTwpOPFjzaHkzn7%2BwjAcHIZcom2JlGfP4SbGhRZhwB4DHJ%2F0vBaRBkXBnSS8F6tiJd7AS58dmTFQdV9NL8CK8nCakmPMoJVlQ5dXVi%2F%2BVJRnlJ6%2BtzZ8qzErlTjLCVOpePeHo6AV6uyY2E%2BDFzDcjYMWHlw8UkStCRlrDC9YevMv4XbR8nlsBsJOkh9wcVU4z8klcuzdI2iwleYDifqt9s7wLoRUr%2B9nMRe8gp%2FF18LGJc9%2B8gaNH4DeTOEjI95kI2%2FUeKULMuJ7MXY2F7F0pDk%2Bk5LkDBAufeV4bm6ABGJrnp0RZfWIJsX4cf9%2BJ3DG55lTejbzgzb5GMtl4vr326I9KXMi9AAz8OdJkJL7ofKB5cCujSr2BzQydCpGoNU9xCPfDyFjx0QE7KgzG4fxwu4tM1MMv7mL0GOqUB2%2Fv6baSQG%2BPUsmo%2BTiSyh6PxcRj2GMSfF6KswrIf8brgPgzWPnJvz2PojgbaknTNwsAKLqiGgoRoK9DDIEdJIFNfrxYi%2FoO%2F6cmPhQjIzO83k%2FYM%2Fc6ZmITXFDuyvaqSa3YlWDI7RZniDNqunZ2yl%2BrpCvjZ5LHFG7turMXdLJ3p5LCW5TEa%2BgCTnf3Y1tpaIHt9kHR7VdL2cLjCXz7r3sWulwZw&X-Amz-Signature=2f0593798d02f322c34518a77ecb21c44cd618ceefe9ff01ab221fc030e4c0ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDW757HV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDFUnkwoRAUIQUjJHfbY9c%2B4PPCqTnqK%2FAhS%2B1I10qlhgIgb3P0YqFqSkNVXl2sbvdCDYGgwzpqyYB9Zpd7KvWCwQAq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBIy8K0dTUAHw4%2FS9yrcA17YRoAf0Rsi2gAYqeE6egyFmVp39elrluV7wJAPgo%2FgFbsSfvGbcsTk%2FDwuUDMSBB4hY0NuBoqsH%2BowNJXSFdLqGmcAr6IW9Hf7DvmZI7x1FgiYNFsk6vvGOYZm02kYh4UtFaFAb0xS4XakolKQlaQvxNNbaG%2BLi%2BExBiyVjbpoS%2BwPYZQ1CocPCgJPsu1Kr%2BnohDLWLOWfaB6yUK95mUnPQI%2FIjsdAfVkh1CQH7ovkicnLNJQE9I526oQ1ux3WC23xN1UfGyM%2F5YHP3GhZa4TX5P3tBazg5bs0sHe0wNAxvGnlypsDmnrdcMrvSOthWWKUZlC3dJKdP8s%2FFiKpV%2BCpSbIHKxIYeyfTUFQe9hs3ek%2FOdZAi5dCT%2FQrQCMlgUhFbG2Cdjdf0tph68lUQoeeU7Cv97vBGKLanLOdJbiyw4j9QjqA9tsUV1DsTRpqn7gYvRiMSPoEUwRH1ktlWq3KGzHh57pVedUOnr%2FVrNA3C4gzGiJbUDjWUwGY6eHnRgturP1wyn8DExwBsiKCswAy5TbgZISuZRcRuXmVVfaKa2zfPTdpQGag2W6LWBvunvLnhGp5g992APlGYtz0V%2BVhzCpnOlKIuF2xUDJTHS2cTwFYOj5yIcMepmZ3aMOD7mL0GOqUBbRgqt%2BRW79%2Bmh%2Fzi0MBagBWo0OoN%2FZIgQCV6xlQPzF%2BESayxFR%2BmFy270nKRxrx2LLxLNzLHVy26XtfZvEOo%2BrdzUa6auupQNn1%2BuydnpB9Zxx4ZbieNliJY%2FmTWh8miyW2%2B0s3P4jdmKoxdFvQCJr5XwTBwMmWZ8G62RJD4WRb0PsmUK4Ax8WTeMajggkvz9cyV0%2B7rJNYMV%2FKr4l6%2FeKYP4oau&X-Amz-Signature=925c443cbee7e536aae6cad20a072b530041a3054f1374fca8570ac950629ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMBEX5E7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDoC4uCxiiV7pHgfV0a9lZ7adtFpoYw%2BdiYlPNyG97DGAIgKNrZBpvr2wiejGsKmtnPSA3t4pN1yGaROhp2%2FXeH%2FqUq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDFkyoh9HoR0kPagIpCrcA4bcUG%2F9FFiakXBSmLG0oagTsJ0h7cGJOF%2FLKheX8sGeJuAkqNbhsn6NvDryP%2FkArH5SUI19K84z9Iq52uIOnSZ979Hjc3WdXGTAtf24lGi%2BdM1rc5obecKKdvsyWiVjwDa%2BPA%2Fq9pHeRe2Jrz0UKrMPvfBlClllvv84nhaRexms590XdwXiZo8VyKPoPxxdd19VYE%2FyfG3QX%2F9Uof4VDgOJQKxOo7S1%2FTAxlvec58Dwnc56Xnb2x55KPjdherPjDGlOgsQ0oERcgEPHVfFqJIECSuRzQ1JLz7NUCfrLr2szLjDFhNoMWCBdonad9kCwWIzCbSGj96mSLPMmVWdpB0%2BB%2BYbdWHMvpFYrisgYlTkfsJxYeqWgrFCnkFCI2WD%2FxRHNbLfpHucvL%2FrQb%2FwPO37fheSrhzTrikJ54SH46lOWpWC3VpUBSEz8SacTcJrrf8DKlIwOsbawqJUxlCUNRHItg6hTkSs2uLttMTHYe1hIYpH3mNMgCfaonfV9m9VzvI8y7MOtOwwWkFQKHw8mQpz5gycUkhTdzNJ4RRFpHbrmsTp5awsDWylb0JvaPIT1fDWx%2BwnPhSfJYokez2E2S%2FTNIRjIkkbDuzXPKgq3j0o6WbMezEioaelaY6IuMNb7mL0GOqUB3%2BVk4aVoiu6nk57Ci5CCEJgn8MQ59q6Q1nFZan2mEbmWTJM68GacEhrplJIZDmrlrd%2BzGIYZNHmgzLkeVpzGJRVGSu2YolZHrODx5CJnWD5O6IbfC1eTyT2%2F%2Fd5EbqM219mM2kDOcqcBqTaLsERjM9SwM3CxBS38q7kYMi8RINZy9eVjJc1mzwedFS8%2FrRwMIKCao9RGgSCy2pRtnxfTib%2B9tH%2FY&X-Amz-Signature=b9a770747781ffbfd82059d422aba44a194a0bab87c2ed704b74bc7b5ba19f72&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMBEX5E7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDoC4uCxiiV7pHgfV0a9lZ7adtFpoYw%2BdiYlPNyG97DGAIgKNrZBpvr2wiejGsKmtnPSA3t4pN1yGaROhp2%2FXeH%2FqUq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDFkyoh9HoR0kPagIpCrcA4bcUG%2F9FFiakXBSmLG0oagTsJ0h7cGJOF%2FLKheX8sGeJuAkqNbhsn6NvDryP%2FkArH5SUI19K84z9Iq52uIOnSZ979Hjc3WdXGTAtf24lGi%2BdM1rc5obecKKdvsyWiVjwDa%2BPA%2Fq9pHeRe2Jrz0UKrMPvfBlClllvv84nhaRexms590XdwXiZo8VyKPoPxxdd19VYE%2FyfG3QX%2F9Uof4VDgOJQKxOo7S1%2FTAxlvec58Dwnc56Xnb2x55KPjdherPjDGlOgsQ0oERcgEPHVfFqJIECSuRzQ1JLz7NUCfrLr2szLjDFhNoMWCBdonad9kCwWIzCbSGj96mSLPMmVWdpB0%2BB%2BYbdWHMvpFYrisgYlTkfsJxYeqWgrFCnkFCI2WD%2FxRHNbLfpHucvL%2FrQb%2FwPO37fheSrhzTrikJ54SH46lOWpWC3VpUBSEz8SacTcJrrf8DKlIwOsbawqJUxlCUNRHItg6hTkSs2uLttMTHYe1hIYpH3mNMgCfaonfV9m9VzvI8y7MOtOwwWkFQKHw8mQpz5gycUkhTdzNJ4RRFpHbrmsTp5awsDWylb0JvaPIT1fDWx%2BwnPhSfJYokez2E2S%2FTNIRjIkkbDuzXPKgq3j0o6WbMezEioaelaY6IuMNb7mL0GOqUB3%2BVk4aVoiu6nk57Ci5CCEJgn8MQ59q6Q1nFZan2mEbmWTJM68GacEhrplJIZDmrlrd%2BzGIYZNHmgzLkeVpzGJRVGSu2YolZHrODx5CJnWD5O6IbfC1eTyT2%2F%2Fd5EbqM219mM2kDOcqcBqTaLsERjM9SwM3CxBS38q7kYMi8RINZy9eVjJc1mzwedFS8%2FrRwMIKCao9RGgSCy2pRtnxfTib%2B9tH%2FY&X-Amz-Signature=e84496e5b6301cf6b0008473cdb63ee4e060a9c1e3d8a17f991dc3ef680efd0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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