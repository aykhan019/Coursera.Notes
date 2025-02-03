

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHKIKVYW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHviw85UXoVVzyYP%2FsWZfMdR67hGMppiTi7YCkiGjx8WAiEAgoQ7VH8ccYn1uyPaq6%2FfvD%2FsMr19zHLbFGt%2BAuxtNQgq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDDjFbpx7UZ5p62NiPyrcA%2FBt4xlpDJ5VPbryo5VKrj9uI6bSpnT9bcv4IDV1LSJ6amDA9ysSnnbCznUtsU0O%2BQJcqMIzcPIwKff8bm9%2BKdqHk16dHOVRj3LSyfY%2BPisjV9o5VR2OEPCqf1L37E1QOC%2BrywdcLucyFledoNire4Yeh0eEygTSpmDlSVyUwtc7RpIoixcpwDBP7c1ygxZCbAyqR1J57pgAnufQEFPfYn6zNrElLevVwkl8%2B6B7rmhIzGV9RUTbF5%2FlrXb6fKIJ9PKc3mfdZf6qH9BSrtwAFR0nqJWLDdYg36uRi4fUTHDvnSid5oNqIoyIi8iLnRXcSiTzQB82pufcvievkDFC30%2F2qAAAU9oQk1yo5se2Qwb3v4JQ%2B9P9wuZSAtyYPtRfJ4%2B4gMWj4RTuc5SdIHd2%2BTgGPHsH1efZayoTOwaResrqzr29XLoIReMTNYzSJ3FQHNjgcFC3B%2F%2F9WkXBRydTDB2spgqcC4YkekkeO22YacTzAqSekOe6LKiTRwZulg03lYdCiX8UWvS0v2pTmkTN8v%2BZRgjamuSIfKtjwgT1PhiNK5aHUevZGLuHIDBEN47HXHvUmM%2FuVLE7I3YFwKmWs4PcZT6mjEj8Z7hCQ5E7QrGxrZjdnNSHaqjWPMyMMM%2FSgr0GOqUBeT%2B6%2FIhk%2B99fufEs%2BE3%2Bnd%2B74xtJCdG1P5SNtVlBxmwKeaGRK1mQB98ySxeNYogAIdeqrxB4fgeEMac8jwfZ6ulqqbsyCjjckN471VQdRXYuCAqS4MP8%2B1oZLeat4wisZtSop8xBpj5JZuJvBNecK%2B1N9mlauw3Y7ceyM5Go6thmFODXYh1k0bwv2%2F9s3iKG%2Bl80kqkuY%2BeDBHhd2U98aC%2BsAMfb&X-Amz-Signature=aeeec9d96585bd88d8330936828f2258a03840c040828feb1b576e7e5f681ae3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KCYLVTM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLPJkk9GZiyMV2VRRZDeA6pA14Kh2ehFWlUvzrrnWzdgIhAPIBKCorp%2FWc2fGvpv%2BDoUaVqxZ81TVhT0UWEu8PeIEiKv8DCBUQABoMNjM3NDIzMTgzODA1IgxWSpNS65ZJ9QZy93Aq3ANltqYjn0oMn2ctzL%2B5EyRMvInYpzsAiN%2BfTRSfQHqAPa2JKC1F7PYTsiYRsPkQkHlUuQQcU39li7bCNMDv1h5WfmAnvIP4aQm%2Fsr3iXr5vyY0RWmWOITzXLG%2FwXElPyhVjx9LaPzkmMNqIlePyK2cmiJ2%2FCFJT3TfvMokmIfRLDftOsK%2Fy61dhORgNfEBaxuo%2FpX0DWpBUogWG6%2F3KmAGZw9wxARWaCnm48M0nxpUWbInPwwm8W1HcWTn9VD9NX6rV5pGx3Ruo%2FKJvgw0R7JH7AhSvm2TiBhgtyDpJYsHWnqIcww9d4F5AInr9q08r61UeKVX2jXq0ErpsOIQxi%2B05AAvC9CC%2BtffXxYiImGCczOFNcp5r5GtPzBR39wBrCZG5IntUz9VRe7UAClHe5lDOie7R686%2FcHX7JSuax6rcSCFDxNveDKZSJBaAohZ4S6Zcsj4cdXpaAUqdxAglizq8ZhdeBp5MEpTs%2FxtPDbGo8G9ZN94QUzANWcyNfl9ER%2FWLJvC7slGftgA8FOij8pw0Qw0F3hFJ1K4%2Bd46MoozhBX3D9%2Bp8wbDTftuvg3wRDArhqDC1iNjGWK51Rfv9nd0luWI697ZXGneYncrVRYdQZqrAnrKjHygems3UeDC704K9BjqkARwlOJVqPjMBiMjNs1qImT6Oz8BUkIxqyaIWtfEhkA4%2BgIAIRmVxVuruIvCSBXOSnvw3uwr4SEU4MttmLrDNS9ynGHBvRrBo4ifkrbE5affVNUzWctAS2QDP7HzS7PLwCpE5drZacfdlv5eMPeoYYVrrPzeQPY85wYmbwvDD8aP7kzDdxA9xnjMkVBgAm9ULyH0ity3ZFYELDJ1WrRkiNWwlzeTy&X-Amz-Signature=6841fa7c4648416b94f9c1b7f83ffb7159db70a7367a18a0e052681a96654670&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULJZOHV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgZedLc0RDaenafrDak%2FZuH%2FhEhCCvaArXnHtmp7KowAiAUCR7rOG%2FQV5wlT%2FI3AYcd7MEeLiN9x4xWUDP%2BxVCTxCr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIM9oWoU7WwiCobiRxXKtwDlUsyVEWfu8y0wdFjKdJROyujw8PjtGxYrg1tCbKF8bKtSifIAWzR9xkRb%2FwqNVbs1yQY4CMBs67jPHC611d8R4vvp3b0jziM%2By68sVOae3TN3Yq6BEL12QA4bazbC%2FCARvdnsIwMjhDz2LxHUHuKMzgiyXTRqIERIq2sWePd7hB9pRusFRi%2FFOVLNXII0MRYMrZxKMorp47Pd1kmCyidGeD1mwynpJZQ92VRng54gOO1OjSOo7YWSwhSTJUn0Du58I8fJm4BDIs2iM1kIL0mOiCqPYTkxgU5erPuGIymzHNixywjal8drJnJxXAfBK7T7j%2F9l6h3BsCuTSjqnUSiqIcG2Uz018oS4qq1JN9qi7IcxjU9z7oEXLt%2F%2FAPRJHniYBkUCamdkP1Gc3lZVGd0CYMgrPyk2q9gMOwJb9VDdwvfwoKNSAl66bv5xJ7NXf8RgTJPRrlTNV08hy29w411Z0BY%2FojF4SbkEsUsca8SFm7WGf9MaGS6mpZU5jhO6dpKBZZQW5roir0RM9%2BgEWAuKgt%2BUKtMRnf6i%2FbevwVBTfJnWenbWxaX9vapUxIOe2sC2DN5VLjZ0mV4SHtBwgtdmgQJsPQFPuc%2FoObUlgwVdmWLBxCTpXAmf2g5clMwztKCvQY6pgFnhDey8geMcizbFkCyL8XwlPQMjqWjBEW26OI5sCmloe%2Fjzm7ysdyQ225C70dUiVtwfR0g5p%2BrqubsVT9J%2Ff2X4b7NN9Ru9lNSo%2BYEAi3A6OBelxy%2FK9uZHosyp0%2BzHgv2QeqBj9HGiB5vdk1sKIprEnWBwPmEl6v7H38qo%2FToqDQZvWJW6C%2Bjjf6iTYUZS%2FjSEjiGKTDZgXIMIcfukJuJwto2hP8b&X-Amz-Signature=7257a51db531b20a78dcc387d64cc22013fbb8d92ba498112d72a084fa0e01f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JSFWI4O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhlVrtDVFHbXEdD4ljl7X1aKfKfjWTFmsLnANBbvnWVAiEA6gBmwq98%2BW8cHAWqjIt9jadObC%2BTqa2N1kr0JCbZAn0q%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDFXXBWdphznlLhoKuyrcA4vWKTg6u%2Bp5ELdMIeyo4gd32xpwhnc%2FJbV%2F%2BFa0g7wv5BpG2L1gkS5ciZyGCvvyT5yN2aWMTKOEmycrBx63QPNH8g6jUMYfT30TS8MnNFhJzPpZX1oMoE1MsKPN8fbFfxg1fIV7%2Bul6TaYpezkpPzYamPzg616zJkoeHgIEjOfTSB2Fc931fiSJcKR9ycZ0MGrtFCSAYLrT6N8KKeP3vUBxkXWIAXYvjOk8rjeFe0wslDhrG4y87O2%2Bqr8eJm2U3wppZl0Nbfei6n43gyFRcIf8qVrVBbE%2B9VPJ6v1MMAImZmfrwiVNPoOB9TB6Sjb%2B4SA28vUe%2FsRropnuKvZE3nu50%2FX4yHUhQUIjkU6sErcG5kyFcwDDZzmLfW%2FB%2F4Xp2b%2Fm6uVYH1PNvQxKQdbPrLeabbqc3%2FfPL5GTnaUy8nIdkeTIXsRV36eaPOcdkOADppQCWrjEkBFMFBp8RZlrnYIMHTtQ8qpN%2BWGUG9HyUc3IsIG5OPXD6Y7qahDEGwiwbPcjvMQuiMniIVCiwf7NJqG74hbK8hWcpy83z2WSySPdcpngi9EvZG9iv9EMOWRfJzzLKrT7vQ%2FmFl%2FwQ05xr6q32BXSoHjpf%2BtlgFlfTQQhxqsYFiEaaVa0BDppMIXTgr0GOqUBVbtWQF0a6dkRq6cMKklf7NXry5n%2Bc5GJ8T2i6xWCCJs6kkNDC0NKgyx64KVijEIuZrdZr3tTpGBopYxDr3e9Qk6SiwnD285mxdhR1QYjqGeoAbE24p6Z7frkQ2p3OAstolNDkfiJ%2B3p7KJSz%2FJowlsbQ3jHnbRy0hOxom%2BqE%2BIMlSyfp5N6puT%2Bzrz%2FY7VkD6RL%2FvFzWvOc2TaKrnGQeg8obOFzq&X-Amz-Signature=a1f921b0a761ca27018136323e78895b6b756b3afb62bbb3c56704602533e6a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPGZHMSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDNtjcL9I9kCC23jSysLNFnGsitrEMEwMBCZ%2Fx0eq8wtAiBom8EY0owM6FsXCzOcRzSldGDnvP%2FLWqIquq2p4V%2BR%2FSr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMIrW1pAsx2COF8JnxKtwDtgWkU4o15tqUZQNUwbAP2Ygf5EocJpreT2hl5DZy2BqjCAN5Jb4DoEnw9wR5mn%2FIfhAXxNh5e1cGKsMubXPpBGo34zlWZbXA%2Bw9ikhXqh%2BT2e0xD7zLitS%2FGdAhWzt8D%2Fv4epnMIwpXWhob%2Bb%2FO%2Bmph5ELn31GDyLgqoVrx5ANbKhpWO%2BtNl%2FykT0y3JIzhUY7%2F%2F0JXXG3YM2mRlXaedZ%2BnAdv7BWjNg90nMguvrojDAFHurYiLLle1qsLPJ56OssErI1lNZetJ3L%2BzKO91uowIrT9jPTQ6DzfWd%2BSSipvhxATwR%2B2YTauU3rSExdB6k2E%2F5dcmNybFLnvYhqO3znQpxVg4EHFwOo5XjCyImPuKZgH4UccEzSY7UZrfD%2FhS2BA7%2FmJzzQcCywsP01GCJoASvIm0q7qpcvllwbxjmD%2FqU%2F7Ykbn9YveHUmlvemirHKWicQ6zgww7vM2vwPUF%2FkKtPxf95YE4LdgTV0Iex2uLpymj2VhaV31Sw%2FkIgR7G5KA%2F2VoaLNmcLq8ETRGfEezCJjTUyzNIfNgweOX7naer5D%2B5gOKIxKob2xYoXNBBHfsexku7tFn5HksuCRrobCIphUXEmTO6TDa5dw%2FA7bFyRkTlk4TAt7I%2Fv39EwxdKCvQY6pgEU%2BWFY6Ri3ucZK3aj4Yh3sUxxvox9oXRsQO7KPaQVU77WAUb4Nz4NHcxegttofs1fxKNQCqa9T%2F3lA5zwpDBNrGFkMbcKQyIlyyr5GAN22MNYzKXI8JEEDFdWkSr%2Fjbxl5b9x5muNHZTlS%2B5cCfy7Kr4d4vhhP1Y3Euzzcntx8L%2FSCcV8wtcJJHUSTBg%2B%2FB00kPlpznLd1Mp1qBEcmiK5G0n79ugp7&X-Amz-Signature=8b96802ab23e7dc768c3298280fc47c733bde6fd881c48855f7c3f5f2f247fc4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q352GT33%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFpImO0tWfdZvDfSOyjra183JQCg%2BOrIBBeZ%2FNG05TqFAiAAo4bPEhF0PkmHXtUw5ViaW9xn6gF1STSd4p44Mo3fISr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMQd2%2B7mJujIeDbOHvKtwD1hz6hlfQu5SIT%2FfH%2B85X0YFF0gV0ddk5KpuZvHIlIV%2BntB3rJk9i6hRQAeIbtt%2FF5SFUkPeYlNO7m8uABoPH3mm1ty2zR%2BCthHyzoEelE4X46FB%2FBQrGxDjxlZxvXjDOTm7ZKAQhxngDsmLvjBcZdBi6raHiKbIjfn0WZvrt3Qe8Psd4tISDGUR2zY69McKtz%2Fcr%2B%2F19UHEwTw1HVzT7rjxr7COp2ibKwyxPnBGrlgh8hvrjfSeu5oL%2F2yzzXF8Erl1hvhnHOMrlE3xsLft%2FWYiEroTq3d3Qktc%2BVI%2BgIbpZdXGCkigK%2BHNUFzbP1oHZpEhHgT4S%2F%2BrOHRXaSL29%2BBCTKNzBEWPQYuKDQWkeILvU0CcT3yjqim9DXzTwjaF%2BR7NtqWNaxynBwIOpDiFFkwnU4YyUL%2F44dePMYlaVMwMEoyt0wQE34OCtcbITj%2FlLRH3OZKJuFssCM%2BesewiruCYu3q88k7ofkc0bs3eMktwiQK5wnJ%2FUxPYHcOdEZNv%2BPh4%2B1skW3odSZzVXIKqyGnh2%2BT4sMksL78UPk5PsTrB%2BTDNMF9ODH9A5Hk0cka%2BCiyrwz3%2FuMPi4UqXU9w4KBn%2FsKEkrlwY04m7Cc4Kqcg1%2FKYahaXbyPbKaTy0wxtKCvQY6pgHGDuEG%2BuQEoZpeLVZiNOKJKPmIbz8TPcYg21oWGUv06VTbI5cSAC%2BAq%2BjdPzpKrO93a5u7o%2Bp%2F6DvHIOgF48ge%2BNQaNulUCkevNjlP80KOeS8hEX2XvxQobeRnO%2FLxUIB7lBUFvIoFVzeBsGiyAE5FB%2BNpTVaS71tu8iyQ%2FYEhzsT%2F2%2BnKfdldB5rPsKDkzRkqqxmwl4c1qBUJPOuiUuQUuDXQoEss&X-Amz-Signature=13edf14797e72d76f467cb4d391b0357aa2545c07268d3b219cce50268b333d0&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CXEFLXT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENj09qVz1BfUoejQNZpZomtUs%2FITU72%2B7NSKPvZNH0mAiBiUhFlI7W97k9ldMJevdEqfT3aobb6pN66wlLbH3793Cr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMcnkTssySjHowKiGTKtwDmPvgKGSRNgbppe%2B2zyYTP%2FbmsXAmo71KWJSUuT6fNkatD2V2cvXUD52QgWcnXw%2B05gkngQHgznTR%2BCeSQ8mqkQg03Rs%2FdYQqEBRI%2B5o1ppNu7meW6vZCqQfYdFyGwddP6TgMjLbQiNWP5PLM5TiSqudYqKov4e1GVjehUIpH7AMTo%2F7%2BHfIkhFQGuzgiDlPhhPEYCiwVvoQMDQiRzCPOB6tMvvJ5xudsw55VVdY743UfsLOqKxs%2FAzHmDT%2Ff4ZeivHj7UA7MVteuDYDckpQsy6lTnHWBKfBKAZbNL%2FVDcT3GwjX0m89sV9FbXaJj6c%2BiAVhUGnyTSSvGEkb62ZGsNKXvnWfS4RtLnjKc3CkTtEbhZVOhe5RIx155Cyys2AiYcYA5SYQQX8AFUoVd8mLdqt%2FAcK5%2BKRmezKxfDVQHaVP9Q%2BjOx7QSHWp3loR8dSUSPB6XPdGagS%2F4Mcr69rieAR3x5zDHgv9LXixX4EVARkjNX2pW%2FEuFu0M7e3A9%2Fnyj6RMyWyWdRdqld9zfQZA%2FHt%2FSjDkkF0l3Yx797AEDOuo9QTzow438Fs19OUT%2FlkxhQJt5Rvmh7jiy1c73ST7UkHm%2F%2BDSbOt0Bd1XWJ5pLvPvdO1ce%2F%2FC2BObYS7wwk9OCvQY6pgHdpStNWM%2Ft61avq3P9wmwPUGL3XA1E3F9AofEJwOOsAMWCwIvDgCcf3a8phrDl0wsmpdkt49FHlzdki%2BaOPITrhOAO9%2F%2B6aeL%2BREvr8iB53yYHTbFPvnrI2GrDAvepGxH8%2FR4oL5vQ9PL9PKNvS%2FwZZT2JyO5%2BcBKpxM2poznXAgzYBe2FLrc1EbQE%2FHzpXQSMvA6l0yMFyih02aA9iv3cDGhqo6y6&X-Amz-Signature=f52197f57668c26910f9f7d21ab9e942024c3dc02a2185a09f3956670a97354c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUT7TS3M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWQtz3AKkARxhJvRbyMIp5TgH7Q4wQpmnRgrRTqDCG3gIhAKEjaCAPwfBo3JiK%2BpZCcExZM5M5VclHrKy8jUnNZOSxKv8DCBUQABoMNjM3NDIzMTgzODA1IgzDndVicBbtqW4YP24q3ANd3GIbfHEUsZrqMcHL3ZWf0NayrT8%2BiAOHCl4TMB8MNcKWiN03vMLQLRxBFFkFeWbaWs%2FpDOhjax%2FgcMXkT0JBhHHaIVIWRvwCzrRygFTqlgmWrFmweDTjQ5IfsanZ9c9DC%2FlJZ6grlRbeAqKjqTT3xR5hGsNEn%2BjmhM2RoYHS2EOTI%2B7n1M2zYkZz1150N0vJAxyrGk3NkdC6rJgyA64bhrVXz6qSPlVTbz5%2BbdOPJlNLCb69vg%2FoGsby3wp6xeWit4fjlAKxDsTvVkGanxASzbMBIGXLRI%2BIwAxdrwwSnu5eMhOXVZCYNeU3z6bhf6GaCmWhapfKUz5xf7DzWoDezQIivf142KMyxtDyp4rFRpSaQnQ9c2fjJ9QyLmi2ImqZco2CpRJ8SE%2Brj6M4qElX4SvTTQ8mal6YPs2NrvCYqVSwi1RqLOvViinLVX%2FWs3STaM1Bv2wvZmXalLxNC6TiQddR%2BMsuVdLJE9dQeFg6HhDO0gvlRzud5qfgWT1zo9JLAlJ%2BhzvzLkfE%2F9%2FLNZsAbBji5UMsCqKrRA2Kmz5erDnbyZ%2BwtsHXQxIhAimxV7C7x%2B0s3JM0F1NIAKJberUK6goYr0QT8lP8Zk98z%2FJV3mFOyhyIf%2FteQg1s%2BzCf04K9BjqkAUrL4HFhB8u3IxGM21tGHKdkUpRKvyeDQioIMp25Ubzd6%2BHJYVXHMfjIjfEG8zWG4lUaH3TUQ3H40fprlbL%2FTLaHkVqOZzHOm0YABcoVsmL6Ov%2FEZEd6Z1TrSzjTGO9kiBeYoHuMTXxTfQPi8iAQEGf2liAHlCXqp%2FF7nuvxCQaa%2FAYMHPSya%2B4EUtV4nsPWu6eI4SX3lIMQAOKsU5fvIVwEviS%2F&X-Amz-Signature=5dac2811249886a5442f6d25913caa6d2a39036723fbc966ebc90ccce44ea6c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPGZHMSX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDNtjcL9I9kCC23jSysLNFnGsitrEMEwMBCZ%2Fx0eq8wtAiBom8EY0owM6FsXCzOcRzSldGDnvP%2FLWqIquq2p4V%2BR%2FSr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMIrW1pAsx2COF8JnxKtwDtgWkU4o15tqUZQNUwbAP2Ygf5EocJpreT2hl5DZy2BqjCAN5Jb4DoEnw9wR5mn%2FIfhAXxNh5e1cGKsMubXPpBGo34zlWZbXA%2Bw9ikhXqh%2BT2e0xD7zLitS%2FGdAhWzt8D%2Fv4epnMIwpXWhob%2Bb%2FO%2Bmph5ELn31GDyLgqoVrx5ANbKhpWO%2BtNl%2FykT0y3JIzhUY7%2F%2F0JXXG3YM2mRlXaedZ%2BnAdv7BWjNg90nMguvrojDAFHurYiLLle1qsLPJ56OssErI1lNZetJ3L%2BzKO91uowIrT9jPTQ6DzfWd%2BSSipvhxATwR%2B2YTauU3rSExdB6k2E%2F5dcmNybFLnvYhqO3znQpxVg4EHFwOo5XjCyImPuKZgH4UccEzSY7UZrfD%2FhS2BA7%2FmJzzQcCywsP01GCJoASvIm0q7qpcvllwbxjmD%2FqU%2F7Ykbn9YveHUmlvemirHKWicQ6zgww7vM2vwPUF%2FkKtPxf95YE4LdgTV0Iex2uLpymj2VhaV31Sw%2FkIgR7G5KA%2F2VoaLNmcLq8ETRGfEezCJjTUyzNIfNgweOX7naer5D%2B5gOKIxKob2xYoXNBBHfsexku7tFn5HksuCRrobCIphUXEmTO6TDa5dw%2FA7bFyRkTlk4TAt7I%2Fv39EwxdKCvQY6pgEU%2BWFY6Ri3ucZK3aj4Yh3sUxxvox9oXRsQO7KPaQVU77WAUb4Nz4NHcxegttofs1fxKNQCqa9T%2F3lA5zwpDBNrGFkMbcKQyIlyyr5GAN22MNYzKXI8JEEDFdWkSr%2Fjbxl5b9x5muNHZTlS%2B5cCfy7Kr4d4vhhP1Y3Euzzcntx8L%2FSCcV8wtcJJHUSTBg%2B%2FB00kPlpznLd1Mp1qBEcmiK5G0n79ugp7&X-Amz-Signature=63a11242349a3cb77eb25b403d748cc1649d22fcb5f582a564819f5a196a049e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS44I32R%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC5G%2Fv3GQ5sKLLno1fTRws5hzagrxWvdEFSzA0M8AUDAIgSAkRvjcgKA93m0F%2BEdeE9BTV69pMoqNyJ1UhLJn4UOMq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMBJ%2Bq2nyd4K7RP2lCrcA8phA1DuKhocsfWxVfiHQqCvMOdWxGThGJatsmRGMTJ4%2BNWdotdS%2B0ZA8xMyypdZbzZIur30v5YO2AXoBkaDuyf%2FTN55VT716mms5Z42hbfPfHXaX5R5D0prr5qsDZUohhCfJvjoPBl53ZI5%2FaO0c476CmfjtDUS58XVF7dFhrLKeHqfhDZ58c6GwBdrOw4sZDoyabdICIv12TWYuDepEwyMLVFdbBzTilQVZTmkVKuWfU7pQhyu6hhdSF6V2AbEy7fHTu9mNOiu3K0pHU8E6wLjk2sAHNAupWIXDyNEc%2FTTuiF0UO5Afoy6OhKcaA%2BrJoR1rGsKM6DSBe22FuiPwCHdahxzt7h9J3aTn7UQpOe%2F5T0lu5CZh3pEBLTP96Trtf0Df%2Fq6UnNnsnhIpyHBRfb1aNovFnEd2JT89ukj1ZVlNUxI7VpfndkX%2BJwL9b2eisIeh9iPLH4VA8oEJ4Yh7n6MELaNBQGKeAC7HMkORQ5Kl1r42M98nuB8NDUX4lfaqbf7sDVtl4bAv%2FKdD8hQaz2GgqZ6ucgJr%2BV05OIOkNtCYo3t5bEX1%2Fp5JOs7ThpOmE%2BXv%2BerxbAVtWlG2FXk8kOTHcoVHwy1DGmPF3Ei0dU%2BRaxqHtjM1D3TQ6jvMKHTgr0GOqUBpyU5eFvWAz0%2BfOOwBZj%2BNZApG26qkByhI9HSHXaPUeNk3UGOjV%2BWEL%2Bg%2FxwTSLFhKOhDxHUoOV2NsZW5Uz%2F6k0AGVZa5BXYTYKqbHK2eVhceIZ72OCeAV1rBvs8kFs7xNbffsucmDj8kQ6AlJfvoO7lPNZ99klp9YNjvNiI1W0s%2FyFH77Fpg%2FuH16MCabjvpIsLHUt20BgDs8q9ErBhrtanrMwjO&X-Amz-Signature=7081c53ae0f18cb521cd7fcc0ec9c3f50e96b5c6154cdbb4704fa9cb139cef3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS44I32R%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC5G%2Fv3GQ5sKLLno1fTRws5hzagrxWvdEFSzA0M8AUDAIgSAkRvjcgKA93m0F%2BEdeE9BTV69pMoqNyJ1UhLJn4UOMq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDMBJ%2Bq2nyd4K7RP2lCrcA8phA1DuKhocsfWxVfiHQqCvMOdWxGThGJatsmRGMTJ4%2BNWdotdS%2B0ZA8xMyypdZbzZIur30v5YO2AXoBkaDuyf%2FTN55VT716mms5Z42hbfPfHXaX5R5D0prr5qsDZUohhCfJvjoPBl53ZI5%2FaO0c476CmfjtDUS58XVF7dFhrLKeHqfhDZ58c6GwBdrOw4sZDoyabdICIv12TWYuDepEwyMLVFdbBzTilQVZTmkVKuWfU7pQhyu6hhdSF6V2AbEy7fHTu9mNOiu3K0pHU8E6wLjk2sAHNAupWIXDyNEc%2FTTuiF0UO5Afoy6OhKcaA%2BrJoR1rGsKM6DSBe22FuiPwCHdahxzt7h9J3aTn7UQpOe%2F5T0lu5CZh3pEBLTP96Trtf0Df%2Fq6UnNnsnhIpyHBRfb1aNovFnEd2JT89ukj1ZVlNUxI7VpfndkX%2BJwL9b2eisIeh9iPLH4VA8oEJ4Yh7n6MELaNBQGKeAC7HMkORQ5Kl1r42M98nuB8NDUX4lfaqbf7sDVtl4bAv%2FKdD8hQaz2GgqZ6ucgJr%2BV05OIOkNtCYo3t5bEX1%2Fp5JOs7ThpOmE%2BXv%2BerxbAVtWlG2FXk8kOTHcoVHwy1DGmPF3Ei0dU%2BRaxqHtjM1D3TQ6jvMKHTgr0GOqUBpyU5eFvWAz0%2BfOOwBZj%2BNZApG26qkByhI9HSHXaPUeNk3UGOjV%2BWEL%2Bg%2FxwTSLFhKOhDxHUoOV2NsZW5Uz%2F6k0AGVZa5BXYTYKqbHK2eVhceIZ72OCeAV1rBvs8kFs7xNbffsucmDj8kQ6AlJfvoO7lPNZ99klp9YNjvNiI1W0s%2FyFH77Fpg%2FuH16MCabjvpIsLHUt20BgDs8q9ErBhrtanrMwjO&X-Amz-Signature=55b1b76808259ab0941012aed334c68ee6abb6103df8c14fa4f20ead422a3996&X-Amz-SignedHeaders=host&x-id=GetObject)
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