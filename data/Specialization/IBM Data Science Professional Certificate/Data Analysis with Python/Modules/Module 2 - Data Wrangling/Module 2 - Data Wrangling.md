

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGX3SSBD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAnD552YBU6iMyhTA0OgVnpzQ7tFbdYIpm5uSEo9FhqKAiABoTAqtwNv4XXyihRTCKW4UeR9%2FdgsMy5ZJuODWJTcQiqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC4ycGx7tP%2BYmfpkfKtwD4MQUggJ4eol50%2BnccCrrFbG80aIICU09NGCSwuUZK3FjRZzgSlvooEohTc7Xu18aAprQmu8M6Rdyy3LfrjJpxsmpqnt%2Fo0jW9pE1Y22%2FSj%2B01KLmwQGML5Osk7HCjeWVNIPFCAk2yUnT%2B04ondOYRae1SkNSyz7xIzEGkFp612Rw7lvWDFqvslFdTrkHTxF8mLec%2F79dKKa%2FtF2lup5RKjajpeVI1m4dWYjzEgGvSKPp8s0BPQNOMaY4yboQyh7h5FYxfjSDp7tkt1owLN%2FabyhGQ1%2FG9BUx%2F2d4quUzGKX4dxVX3RlTGtRSnCYpWWFuYy%2FAIvqPF%2FJ1tI4oUJBEyz%2FTuxXEK%2BCQUO0b2I3reaxvh8JHOQRXndF%2BxrXyhFWXdnyWgksEXhzbRAbZnI9V%2Fw6%2Bie3UjkL6BI%2BXHRkeQDSSKSpCaEnQg2zdYaMjgQz%2FW5ovXiHwM6VjryC9RehxmknIoCdirxR0bSvY02f3Ylp%2FFH44tYh9V%2F6B%2BWFyhI54A%2Be2wJdd3KMSGjwM%2Fgnjn5d0ssup7zpDTxBde0HpUWRr2J1h31LOBhVPRVEIEBHszlOygc9t9zsO%2FaD%2BkYHxzvtmKbpJELGRk04BX2HXWwZAhhWoktD9j%2FEPuJcwno7vvAY6pgHfFaTk74AZ37k%2BAC2nS0w3rPAZTH5cvyneRGURQaDbVBNA7JUTggSBa%2FYFz338CkZ8U5%2BS9P0B1nrTIyMiSoskdWTbS%2BRebw4i6VuN4DGburn9C%2FfTkEqz13Mpryty4OOgdBoKhTKGMjWE31bTfIDzTyMdIG275mgEZByOLTmWl6ljUXeclCYg2v25rgyarTwHvcCErpE94xOmr6XABZH%2Fjakr09y6&X-Amz-Signature=2ebc7ceeed1fc2ae46ffff9c4d05c598a50d748fc3165a4f102072c5923363d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQFBLLXS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRtTXPTwwSC9EmZsW6GF%2FqKbM2vsbI9zja5HZfJqnIxAiBMeIYPiTM7gtjtNWnjBpxX9OXq2mYiN1SXFA4rdDgaJyqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BnU1OXyzmsTIOdfgKtwDIe%2BX52BkM8RDwIQdK4LH%2FcBXUUWw%2BWdyB64IpYj2Pk8T40oLpb1iz1R4v3yfxHERsVCd03sQTX3r4SFHEh3wllfOKxK7sRjJq39G4dsPEZhZDv0jiAETyDKu9ZQ7P078J3H1vGIwwDZYmK3WDFPyQnqZ9yfNtDwpsIonJ1yMMIIUviu8CWGZWCbevRuuN1M%2BCx9N4E6MntOvQiB9IBkcsjQHMzYY8WTiyjiW41LKIHj1Mpi3KMaTAtkFTctuQ0Tq%2FwdgluNKp9AkGJZuJC5%2FBrlIxPdx3iEt%2Fq5InRNzPPrwM8x6zoe10uT4ZMwVPsH7ILeWtrIZxx2gcJykvGKwwThHle%2BH3h0gyNnLQpwNTgJkj07cC0%2FfVs3Huhq%2B3Yy%2B2MA1%2B0s%2Bf1KZVyZZncaK31zRZLvS5qLezOAIW9kYoM%2FAG5%2B7QFuQgit2xCI%2BMw0JvUyWZKrPcHlApou7GsvrvmvQIfEOlpZ3owt4%2F70L%2BFHoek9qyFDv40sG7cIXYAUxoR3DJlgfy7IW%2Bvdi86GQDleMZi2cbv0Z%2FTPoliOKe03dDyjbXRGhjSWYWlb4ni7dz%2BJ9nIe0z7E9a09LBxMweGpyqKyW0o4WpU7xy2zkSDqudTt3I7%2B9CPJBC%2FQw7Y3vvAY6pgE8t1pqmQTb13g%2FoKTwF6tFITrX%2BUcbVBUCspwPgVKwar0QIgudUxm0Td97%2BKtGFXsz5NdNGA%2BWDkIkZ2%2FCZEWOh7bQ1Do3M6QDhbEfpFfShb%2BaNeY2dFgnrkBcoQnffXt2ohuXYiEl8JS9pTe55aEVqxu7Tg1oFJABGxmiVqiWOQX56Hh6nbG9GCaMXe0arGXt25aIQ1NMBudKRvxL6%2BkMyxs31A77&X-Amz-Signature=c86a334e40a94ad6eaf2e345127b490303da0cf25286df1a77475091fbfd768a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLJHJXX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCa1znnC2A%2FlplwtJVxLReauouu%2FJtFjjozEjjXcFgAtgIhAMpEgwk4mDXB%2F0fIY9pZk65YKMvAsSARdZIVWPRdB41PKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXyQNB%2B1XU1OTnetgq3AOFUzlDf%2BvTPB9huZXJXQXVY9k2tIia1raPXHHS2ASrCpQ3d9iIbuZHqyIF9daweC3CmWmtbo6sS9w2kKpXDarIs5HxXRrTYgj0J%2FpPdmtHa5Nc6mL3WAdSIM5NW5s3oAHMQRs%2FR%2FtpZpFz%2BizL%2FUNCgjC8CmImlQQrimnZINemfrkQ5gWYxhl9GqgnPkHaiyL8WPPpEhoX28SVmOMohCQURzGWFjFrQ9Q1KTh85ib3%2FuWl07jnzdkQooOPDqGRuqc3zSCMbr811LTVUf2Wd9sWzX9IaL2VmW0EIRLy%2Bfgc%2BBaRmTrDxc2ypROCwlaYOl%2BIRnSiin%2BUdmZAyJbP4Q4pL8RCO8oAoR82krMAH9fKDv%2BIO%2B3KDxjpGuifcLCrEfFxT9VWdxlsAIrBTvcf0OYClCYBHvGU%2F2pN85Yx784uzKiRGSSX23OMap02AlcdzXxBxYv6oLRMAOI3MKoxNPPFgjOivHQFf8HIwkuwe%2Fg5r69B7XtgcF8ozsFy0i6X9VHdJvrWIoo5ODabLb6TkdsHuRFnraEkWX0iW4jvbumuC43Snz20g8ac8aJbsl6BveyHazgE0gHNOKfGn%2FpP%2BXiO63I7PZxETGsZf7lR27ArFjQo4lIO1I4xx1kjvjClju%2B8BjqkAVMs%2FlHO3V5itWwfGaFDhKEkKUG62foxTNntNbA4rUksNhUaCGKKGYvVkAVtUyr2I%2FMo78V%2BcU2L8KTL21V8BUzLOIJd1eO9ZUYVxD6SqId0FKRHpb3dX7jsd7p3ybOizHpSIU%2BpkECV0aZik1dGied1KKaLVywrraj14LYAtGS3THkcC3bCdpjrMWuZr5W4f5KDHvU5%2FD7X%2B8hsAPc2Cy6%2F8hzK&X-Amz-Signature=fe03a150fcfddb7571d6ae6cffcda84221dffdde5f111adaf0e9df79bd8a1e03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL7A2OLZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2F4l77mU7UXC%2Fws%2FOtu79AXoppCuSXPmwiM9O8yUqeKAiAJfb%2FzrZkKTCQ%2FglD1bUG1qfcCYayKjsjesEAxAcMpyCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa7Ft15DwdqR2aW1vKtwDuOS6UCFABTnYDjv1l%2FucyoBnP65IZcg8RL6jdLzqEFAVwcMvU2sQSz%2BHeUeoW81lz9n%2BL44MWaTat3VeEtSh5JIoiz2yTCw%2FTu9VWo8%2FWIhlCqnlWJR2rVbu0vt3IG%2BK8hMIjhzGc352X36nddTuRGB9ThtIJQgi7%2B2kUTUTh8ZfH%2BSqSidwSkErbYf4091QUudlErOWdRjNIbctSsvYYGBnnP02VL7v9UqeoIx%2Bq5kIp%2BwrOtPtFK%2BLcrH8xfauEuSs3EUG6GzCHmXYRsbEMLFHsDPOMjivGGqF5KZCSwHA9DN4ZudjCGwwkIskIInGT3F51zXd%2F%2B5SXUQ7f5zJTBImkNSohsGbeKXokglTqPt7E%2BOepbh7EsmF2odm2o6a%2B%2BsoNttdBRlUq%2FGb11TrpPcNkm7aYwfR4aiG83H7oFHxEsN9Cq4JlpVNmEQaEGrSEvG9ZtQJ0TyMBbm25daJAZHKCGKIspuhqkz7w0dIa%2BUN%2FjtSKRZvFA6Q4KVJs4Nr1T6DM1WVAEB0elGuZeyBzyGrqXp0%2Bsk7vLnhA6GSL4BJMvB739td653%2Fer9AqOzCBEiFFNI8HdnW7ES34BD9JrmOdgynGVp9mUwl2J%2BrK8X%2FiS9UO2yBN3B3crowro7vvAY6pgHuJ5P3Y8I0fgBZfn4eGlhlKFnZtRQ%2F%2FV9tjvXeoDczI91WXAjLOQy8Ea2ptVs9Yx4paOwr%2BCtcM50V9kJ6RhtYlAukBxQzZMfF%2FY1bYZv1kVzhRKWlJDjvdyx7277Dhg%2B0nDC88U9hvrWNxBl2w%2FksOBweo7ZO0%2FWWJzxRGNGqvvlJfj099eGU2hw5PxhcPBPEOvDNUIVITMeGbN%2FiBlUzly%2FAb%2Bz3&X-Amz-Signature=54c9273059a0fdfeafc16f9f538b0dfac36894427f83e7ff4197bab0f8711e0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SHVQHUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNhEZk2BPLwYCiq8jwA2zNLW%2FMmPSkTeA5CHS13gauHAIhAKY7XdafapQR1OzrjxBNca1zA2FqZKst2odqy1olyzJzKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8Xk0S1a1Ga0yVZDQq3ANvMVED7BLz3DIJfS8xBiiF%2FpU1LNhAVrYF%2FftDEz0ylXn%2BKebM5ylvjp1Xcma8WjixC34gRJiW51pNxdooFo4SP49Ka7%2BOPGmqwf8w8KtLXS5DUkCAckABjG3%2BOHaT0LRITWluWA%2BEKD8x%2BUHMbZp78KyzBPcXxyhfVOkxibGiYx8ChzSwLgtmKvkc%2Fc%2FAtDZQefccTCjdMMKitOeZ4CRUm9ORsSy4PYuBvoafRRST7j%2BT0sr5TKPOAroudLNJPyEhyKB0VpKOn%2BoO82Dwec20eSEFsljplgsF51cUoVJCBYrf3t3sOHBKq0wdXAdEFXFXi2jGEpg3TFB73tEQiHtJ9Y%2FOJp4SzAX6RDSUsfg%2FxTcUeSZpxH48O786HVIQ3q%2Fkj%2F%2Fuv6QnbAWBAqqFvxGt1qrHjKs%2BR4Z5VG3VZnbgkGLv1RVTOIYfI4c3tDYjL1cyhXJqrm2C9Ofag8P%2Buyxx%2BNGyEXoBT0bE8w%2BLCI8O113N5c6mQtl8eTW3JDG%2BYx5mtxVG13L6Iz3bnc%2FIf7jrbwVc7%2FxaTZyJ4iGiW6ScNkEBaYAKOGCbVSW%2F0rzNELi65NrWBt0Gx5%2FhY2aLD1wqn1DwjoXCUoisjG71O8pJHz0LH2xe98NBRi03pjC7ju%2B8BjqkAVWAi8m3CoOpZPWmWb6DVkcwNoGKFeEY2NtyAfkP7w7vRiZJ3csJOpoOypfEKt%2FeArWbyl7N6x5RfzT8dBdhWeld8zd4CVRCd7Z20AOBZcxd8KsCFBNzSs%2FnXkN2kiFt%2FUAnaEq7GOzrgZ%2B8YnxTTZm%2Bqaxtj2tvebR87vXQ%2FNsQyCyQht0qIVV1vq6cSOhdIQsz6g0gC3RKQRbIbBFP4hpxqJxz&X-Amz-Signature=d4ec6268d4312cc8239439b6a828746fa8519e9a21bc88230d7fab99981a1d7f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BOATDAW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8%2Fq9CZERuAKvyOvHA%2BriQVtUN6RUEzkBu6UF1Yg7mNAiAR%2BgHslofFIwNj7SGfJsNhnFKz7Bc0ZlCJi9bG6a3uBiqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2gLd7RPtv%2FpZOK4aKtwDDR%2FOHyfwqgKegueCG1Oc3g4e9kWqyERie0MkNnqS5xacouIY7dFtR1FkGfcTEhWhIIc4h5j1tZBQan6DWY1o9Rip%2FWBaDvg8ADmHKRMNgGNud9iQSpK1drMm7lt9QaEd316u69XRr2T3jxuIuc8ZmArrzmDUfjz%2B9JNrSj3XR7WTXHwO8JRA8XXq1ICz888UsFD%2FSq6EcFZV2BEJKS6n%2FoaMFuLC8T1FxcVfFMJFqnKWSyfw1mySLuCCe%2ByzQtew4A1tx8w%2FwOKzjjqbGW8qE2tNHk5ZBaLdHLJTS3%2BoCZq2o5%2F6dhjhTRtKxkgMl%2Fgb0geTcpWXMRFlgZjtf8NkOzTu2taYmLHyUvJxkG8vgzeqM7iLwB8vafCJkhyLKlz8VvsPgZdEzikQQD51fgIYNvkqhbHhkfkRR7I%2FqpInuEq2IUDMDreivwLODMG01hcjRzn1FhIn%2F%2F8p%2Fo11%2Fo0s3Ryvl0GqJfgjrAKp%2B6Oamg8cOGVOWzLR2Kgf7rbb9NKyBo8btKhm0yPAwl2Ht3P%2F1Xvvv%2B%2FSw7A1q3VL%2Bh669MbnptTmFCJWweoRAbU6pOFTVzK10impgtIFv7EtrS9i6QO4tj2%2FUpssPLjKMpJrG0FuBm%2BHeZ17e3O%2BI64w3o7vvAY6pgEpUQuMa%2FsZWR73bY%2B%2ByIjZ7JLXAPJ0QRMeJahNz6q5fPUNtOW%2F5T9Hrym2IjRO%2FDxC5WTJz8JXhuSX6dFKKAWi2Jth5j9t7z7IBtEuXEVWAg16PsBoRQfiqbkgmEPtweiFgYSNaGWZF9G0wza9nZ9mIrPQE%2Fv8Tgjl8JjFiv%2Bn5X0t88vyM2Zw7A0nFghTiLPSwheI2BnIoDo%2BU%2BDaQtXseHpZSlWL&X-Amz-Signature=3fc0b3518acd8bf1a028ddbe70fadb6986f0ac904a3f156a6a7b68ca08a391b7&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO4QPYTE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGfauQHL76n14IfP1cSS1DMt7Vk%2F8aKyMxPaerKJNK4wIhAN%2Favg0sIE0SoQdocS7qSau1HJH6vC0jBxyP7gxJTZguKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPjXteKExELa1MIUQq3AMTRGtIs9ONJtfz6b9kZZX9BaLg568nMCqiGGAuvorLEr6SHkvuJ3wLLZuX3IvLrv5gODyQPKjUPyEsNVjQHVfby65hiiXY0nsN%2BM8HmiMSgFZTpoQWVz%2FlZ1mDCjAJZPPsR7xSEkIaanaS%2BHQ5Vq6j3IiP82AiAEZPrY4lSFbV9y5yUtW2Pj6vBnGR%2FRhGNboME3%2BTQ5LIi27z0h0fm4BXEWc3rmFNQYBD4Y4IObE%2BW7Dft43EOiyKtizrKZxp1wEnHPa0BM40rj3y5GC6vmmui1fpLQgPfrs%2Fdd1x%2FmuPrmFLuWoQS%2F1YLkevQ8xR8E3dMVkM7YBz1TaUyKDkISrg6viUhWrGwxOwHhgNdRSJK5bDv5gtO%2FDD8%2BL3ST3Y29QV6NP%2BqmUIDX2eQ5c9%2F%2B2B57ozbgFE2OPim2jAFOdHNL6BKKkgPlMuv1K3Wa3wF44Ao7IKdY0n%2BpBP3zdrgfYsLRDvpv8fivqTtzoRP7X84bzD2UQaNggx5J9LS3qNQkhXLv7aPVCzqiq4Kd9qXohDyvIENq91xRBXFpHHXnnQOLW8hSqWGDIaPugbuOG9BjWy5f6w2Of26mEffnw8QxANhzJgR06%2F0mLcIkUHn9Hlb0PPd4UAUrKUKrcMATD0je%2B8BjqkAWtfkCieLzNVD6V9Jk1BYu1ntoADpqPFttimhE8b03y37TWnv1KTZsWH1EfJWEr%2Fnwg1VeCWpk8rWCGGLVK1tpEEUord%2BmLJ0jdDfJO4P5PanhKih6dPCGG695%2F8Nq5P%2Bv6Fgnwf66kIUC4nV%2BQkaos6D7t1l5JOLtEq4Ot8sy4DAykXlL8KTK%2Ba1gdsIGHJf00R00z8kbKEdZylYGpNN%2BPop4%2Fv&X-Amz-Signature=3bd04ee529df972d587319ab333709c25eb6a573023c61baec94f68e475fa174&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTPRAEVK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGl1Pe2btHBIZO4ZgC55FIMUqGB7wp%2F%2BH4WiGEQNHq%2FUAiAjBaiF5JntvTognTryRZorbrZ9VI1Kw%2FLdpnX%2FDx0SkiqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXXs%2BsRioPCCbobPIKtwDTEAuYmWpYsX7AI%2Bi9psOd1%2Bi0OKvXA0wEfAPSYJd56j70tf1yDjnh%2FWXx4tM1Fm7UOYcNYMHg0yRJKq%2Bma1L1MQOcapnfDL1M3KgRk1TEABt4DgOAWYVQoWGepv%2BGNLBKzcpMiIld0E6%2FkcfK1UVSsvaIXUb%2FEcYfa6XVfdn4y7jeNQHwV%2FsLswqCmdTgunXr0RRo4rcUgTPeLzmWbDqvivK2MLUaFlPKEXDEBn3RD%2B7%2FJdIax7UB91w%2FCSLVkajtxvS0XGkg%2BiJ2VAnzKuXnqeEuIhNSaQqNGMRVEthCqPfIfV%2FnQjzLzyiWgrIcYZ3AVKwvfBzl3Ky7faG9jEZQnIsx%2FfBduY7vccVOdYv8SKGSWjDf54oPTeCHer7ZYWo%2BDSuuAZMg6VvwEylTOpVBZP%2FG9CpHyxCiii%2BAAOzbOPox1MfrZPesqhk8Q%2FRfPk4hANg9x5ko7AXKXwPOQmejXbmHJ6MVdubvIOYK3Oxf59X0kwAsCv2597%2Bm4Wi6kt9vmPxjZeGf3G5ssfOrJtGCCGXuUwn%2FCQvfnD2i%2FbPTSxk13Tkn1V4C5K%2B%2Bt9gYsEkjv3NNQrelWuW%2Bx3JyrXERFM%2F%2FgvK8%2B4FShdrusCMSUGmsZUFI%2FAueNc7UUgwo47vvAY6pgGRMGYZCdi54xjb9dfAadea4Q89m5iUv79%2FocYbfXXG6Nbrg3NdNKYLDh10sbAnmNudSadKjdJjldwAF0TQFFwXAb7tQhVnPQ28KitALx1HYCxTm7E1Li7iuVrL%2B5NOyGp3lJSp%2F0YDfuCK0ZuvZhsDSeh1Wsve6PNpWcRqLSue0tL3uBab4eWhzfthIklu5xT5MS11QWWojH2oB0S1pOClnJpXCYa%2F&X-Amz-Signature=7f40fd38194129e3d1f4016a9f09913781daf68d383359bbde93ca8904910513&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SHVQHUE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNhEZk2BPLwYCiq8jwA2zNLW%2FMmPSkTeA5CHS13gauHAIhAKY7XdafapQR1OzrjxBNca1zA2FqZKst2odqy1olyzJzKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8Xk0S1a1Ga0yVZDQq3ANvMVED7BLz3DIJfS8xBiiF%2FpU1LNhAVrYF%2FftDEz0ylXn%2BKebM5ylvjp1Xcma8WjixC34gRJiW51pNxdooFo4SP49Ka7%2BOPGmqwf8w8KtLXS5DUkCAckABjG3%2BOHaT0LRITWluWA%2BEKD8x%2BUHMbZp78KyzBPcXxyhfVOkxibGiYx8ChzSwLgtmKvkc%2Fc%2FAtDZQefccTCjdMMKitOeZ4CRUm9ORsSy4PYuBvoafRRST7j%2BT0sr5TKPOAroudLNJPyEhyKB0VpKOn%2BoO82Dwec20eSEFsljplgsF51cUoVJCBYrf3t3sOHBKq0wdXAdEFXFXi2jGEpg3TFB73tEQiHtJ9Y%2FOJp4SzAX6RDSUsfg%2FxTcUeSZpxH48O786HVIQ3q%2Fkj%2F%2Fuv6QnbAWBAqqFvxGt1qrHjKs%2BR4Z5VG3VZnbgkGLv1RVTOIYfI4c3tDYjL1cyhXJqrm2C9Ofag8P%2Buyxx%2BNGyEXoBT0bE8w%2BLCI8O113N5c6mQtl8eTW3JDG%2BYx5mtxVG13L6Iz3bnc%2FIf7jrbwVc7%2FxaTZyJ4iGiW6ScNkEBaYAKOGCbVSW%2F0rzNELi65NrWBt0Gx5%2FhY2aLD1wqn1DwjoXCUoisjG71O8pJHz0LH2xe98NBRi03pjC7ju%2B8BjqkAVWAi8m3CoOpZPWmWb6DVkcwNoGKFeEY2NtyAfkP7w7vRiZJ3csJOpoOypfEKt%2FeArWbyl7N6x5RfzT8dBdhWeld8zd4CVRCd7Z20AOBZcxd8KsCFBNzSs%2FnXkN2kiFt%2FUAnaEq7GOzrgZ%2B8YnxTTZm%2Bqaxtj2tvebR87vXQ%2FNsQyCyQht0qIVV1vq6cSOhdIQsz6g0gC3RKQRbIbBFP4hpxqJxz&X-Amz-Signature=fe43e9bc279f145bc5fa1971282b57b03c2fbf69bf9d0c3d3999c3614c9d68f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q56LLTWC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2BPD5ias3BHypg47c0Fhxlr%2B5vfc3kfJFegENoVlZEKAiBjilUqeJmprsX5t9qlqhvtn3Aw6pLduCkFjMTrTMn5VCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM44oJ%2FsvMvjL56pq6KtwDLTGnemodJyzEIng01%2FPg4wWcbINEROKOqGYfU4LkE1d%2FZtjpAU4%2FHjqC9hZ%2FTwAXrV9qVF0cw2qRwqwY9XUPPBadEUumeWBAIMYMT%2BUed5bPRfo0OeQUhFxC4oeS16lZjX7PV3KkQzn%2FcpGS3esOjgSzKX57H%2FPeoM09nItXKwPgkeW28%2BQNqOE61Qzr84h%2F3iI7nVmv7RdC0j91Iai2yCMqCP5gRIlrW%2B5UWCV5ZEBt59OHnW90lKNYW4HmvuqcfokrafSat7%2Fmu25Fcer0411Gf7istvyjLdlCoPm0VU2snn0i88yXS8U21IpmXUOgveFM4fI1eJ3%2BO4TLiGT0%2FqWbxHqnSFRjlICiG9hth5vXRy4jFkIANTcxL64Tmn%2BJfASAabgiJupEjKSMQ5s81yvb44k6LylTzGmRkDwzozQeOvQShKCHKlr5YcrP7SOKZj4QBJIMQdbZxrCzNVwwS0p3w2hy14jeBvVPVrhId8AgaOyHbwwuwO9jD3%2BYUjVBePrZqMJ6toqxBq1esgCfLa0hSx3vDO2SnKwM7pqngOIa0K1u8e1mOCRInmfk%2Fan4piOLv%2BRrZpTnKLsZX2dHoo1FKRXzOV%2F3%2B%2Fp21Wp%2Fk4fque8XEjkCLodBLX4wyI3vvAY6pgFcFg%2FrGIyiBVCzgKy%2B1muj5S2ZyuyzSETX9vXbDARYxSfSt1826b0tufagt3tmHw4UZg8QAN9mqndwSOZA5fZeSA3TQeoVir6L8WHXCX%2BYbUreaVQTjE2PgfQLRXEjSZBRA1VvJokElvXP17aLoDDlPdwMzojYvIYzZwHFEloEZV9ZlrMPjKJhWhSgOLFB%2F2K%2FnNLkc4YZtG4qtj%2FVXrW5MNnHhhc4&X-Amz-Signature=714aba2e2c9c220b3213c26dd12a57b153edb6e21a1af912f8defb4e83c0cb09&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q56LLTWC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2BPD5ias3BHypg47c0Fhxlr%2B5vfc3kfJFegENoVlZEKAiBjilUqeJmprsX5t9qlqhvtn3Aw6pLduCkFjMTrTMn5VCqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM44oJ%2FsvMvjL56pq6KtwDLTGnemodJyzEIng01%2FPg4wWcbINEROKOqGYfU4LkE1d%2FZtjpAU4%2FHjqC9hZ%2FTwAXrV9qVF0cw2qRwqwY9XUPPBadEUumeWBAIMYMT%2BUed5bPRfo0OeQUhFxC4oeS16lZjX7PV3KkQzn%2FcpGS3esOjgSzKX57H%2FPeoM09nItXKwPgkeW28%2BQNqOE61Qzr84h%2F3iI7nVmv7RdC0j91Iai2yCMqCP5gRIlrW%2B5UWCV5ZEBt59OHnW90lKNYW4HmvuqcfokrafSat7%2Fmu25Fcer0411Gf7istvyjLdlCoPm0VU2snn0i88yXS8U21IpmXUOgveFM4fI1eJ3%2BO4TLiGT0%2FqWbxHqnSFRjlICiG9hth5vXRy4jFkIANTcxL64Tmn%2BJfASAabgiJupEjKSMQ5s81yvb44k6LylTzGmRkDwzozQeOvQShKCHKlr5YcrP7SOKZj4QBJIMQdbZxrCzNVwwS0p3w2hy14jeBvVPVrhId8AgaOyHbwwuwO9jD3%2BYUjVBePrZqMJ6toqxBq1esgCfLa0hSx3vDO2SnKwM7pqngOIa0K1u8e1mOCRInmfk%2Fan4piOLv%2BRrZpTnKLsZX2dHoo1FKRXzOV%2F3%2B%2Fp21Wp%2Fk4fque8XEjkCLodBLX4wyI3vvAY6pgFcFg%2FrGIyiBVCzgKy%2B1muj5S2ZyuyzSETX9vXbDARYxSfSt1826b0tufagt3tmHw4UZg8QAN9mqndwSOZA5fZeSA3TQeoVir6L8WHXCX%2BYbUreaVQTjE2PgfQLRXEjSZBRA1VvJokElvXP17aLoDDlPdwMzojYvIYzZwHFEloEZV9ZlrMPjKJhWhSgOLFB%2F2K%2FnNLkc4YZtG4qtj%2FVXrW5MNnHhhc4&X-Amz-Signature=a48fab85a4a24ac0baf10d905fda1f621b7812e51ee91f941fefde3a49d27bbf&X-Amz-SignedHeaders=host&x-id=GetObject)
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