

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676I6UTYI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIDAzWyLYf2xo%2FpIBSnqWWCWaqg9CFohpwO7fLurypyTsAiEAnC0plKtw3uxTxf1iXBOw04giUsRPVt3c3Ow%2BVLVuQRAq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDBe%2FPMd2Uk2BenN09CrcA8K1mojc%2BhadE5uq5dxv4zWNIGOPLsmzf3VNyhbQ65%2BuITMyLFQtPCEZ4uJWqf8yHxr0EXEMhRSV1pU1hN0inW2jq63krzkIiZ6G0F3Y%2FXwe%2FOhvTYCasCQqXieQxOhdVIz%2FDnZCr6ERdvNlafNgfJy1mdye4ukhWJ5fHnE83bff98y1%2BGCS4%2B%2BK2CDbnDSVNxh0ky8onf5iHdRnLP6DICHFmE5G9kjLfnkvMWiQZ6YIuDFCU6SrOj45iYZ5iPCeYhloO%2FkJdniV6v%2FQgY1hp%2FHFRqvEEvWejcQLG2jgbmiYVqt%2Fv4nIdbSXPTbEXCn1T7EjGeXVhiNtFtfufWB49txht1EXQOqJBhdr%2FEfzdhDEsSVWC5qX%2FT9ZYqD6ujMTnw9EXv%2F%2BWg%2FuoRXJWgqDR5%2Fgg9up7vVSwdLKRZw6Tw9SixQ69KBZmGJARfCe4AgXq%2BcM0ARHS%2FZf6DYfShCTHFJp%2B3XTFHhqcFtmqesLhrA9%2BKjsCpfgMOB%2FnAkgnLlriIzThjPS37bb4UjeLWxySl29qYaHcbIKAFAeYmiXGzyo3%2FSibfD6EiKvrLWqSoXf1kgbAeKBTR9kq7MTvxGRxuKxqNohfKtXQt1oVp%2BJyoLNm6VJq5QlzdhBk8EsMMXOhb0GOqUBik8HczBdPGptvH%2BXLgIV1tM%2BCNagbAHOsaE3k91pYMc8Fy997vawt9sguuCtuktoc17zWqt8t0EotW8ZisWKt%2FRYjgeIRrX1T8y9K0Unp0AOQh%2BvSohVDzcf8Zny7%2BYBVVP34QyU0wcisB9k%2FaRd56UGn9V8rTJrMt59ET28xAX0ru2XHwMAs3p3g%2Bw1fV20VzYWnN7BkEYxhOvkPN4EpNT9PDhz&X-Amz-Signature=19b6f47d478ab2b9c85539d805e5b9ab3405cb66771a7f397bfd615a8c39b7ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL5YVKML%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCc0MZk%2BLUKsHK4cnW6vYKpGksZm52bzP92TU5hOmJpBQIhAKzimHyNJSPmE6%2FzeLOzlUEO%2FUIUnMZbCzMQgw3oB5M2Kv8DCCIQABoMNjM3NDIzMTgzODA1IgyXMNLnyP%2Fotu8kZHIq3AMYUxZVc%2B9GzPUDAngsZj9XANsO2KmbWhYACq6tI85GaFWgUEX8%2BnqSkWgp16wb5APQwgB8Y%2FM4dWDMw0fX3cc0V2Tt1qJaoMq7MrpbjSeO8HAKxCuJ85TbIeI0wRr3i%2FiALISVOudRNruGnEsiVnFABuE0tAFoyEEKuhKd7fVWQvTUH2lxpqIoY0OWFrrIEfmDYbzCH%2B12gitL%2Fd8lQvy%2BMOntbf%2BEGs3aqyxqp1jAzen1XP2AruYQS%2FMVOD0dicVHKLuDQgd5wWxQoSHAO1nKOuFqs7tJoq%2BccHpvuO8jCunipeREkX1AVi6JzhKxQ4O8Ee8k2nEcNkZGc%2BfgmxO3aEWwqQLW0jlrv0XUVlPWU%2F3qT3rvMpC6gRnOxBXDk2Zl17tFKdjga3%2B9NoQRSy%2BS13y%2BNot8B8KwDv%2Bl%2BeVusGjzuAwvMuUXQnnqHxiaegD%2F7mdRT00yVd1WUIf5UZqmXrXDPWH6Hpx7Bpr6FHRB9pyKdhx6cXgB3Nd13us8hgGKpMxTiOyzEMnCqLrbGKeG2eDr8ulKT%2B8VYQwrjGx8w50rm1IbxzFyHFGHuQ9%2FsdszeRcGaXGmKR1IeGL1iA33wGlHbVceWEm7ZDAUbWBPnHJtSvXnMTER5HwEgDDQzIW9BjqkAVy9rgu%2F%2F3cBRS7sUClKpJEzY5G8cFkhzKVd3Ol%2BZAzG2vtVQ%2FFkVA2XPigl%2BVImfAlqL2ahM16sg8gYz5SFgruCLX%2BUTlXUcq4%2BFJI6eNXbv9aHJ3MvNSSmdTs6cchARPbo3WsJvy073AK3B8DvrRcVFE9kMxJq6Pl%2FNWI8fzQU%2B0mlvEu04EhvjatlRqYVx2KTZyKS%2BP15RSViYzav%2Fwhumxuo&X-Amz-Signature=cca63710e51d8514861927119f43ab421c033c2a43e5fb8dcfd08d26aed012f4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZONGCR2N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDBhw4VBiIL%2FRfbCEmTH5evQ1KNFhULuSxjQCrrETSxDwIgY22HQJPkc1EnCRVPtLi01Nhh1xuC%2Bzal7atRGgeLXBIq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDH8bCC2qLQ9lhxWvbCrcAyKE%2F9gRdc8Pz4zLo%2FlqUGM3HAOAotEJ0QAelT2elEM%2FqE8mxBOP7XNJHui6M413Bo5ZwrO9Rd5UcOTtNEt1kf1YoTZWLFgiV1YGUrPnr404LKbiUpYkGJRYBPLfAotln837HorSOmLKIVIp4O2NtPlq0P8%2FGXcFgG4yAf%2BVO0Gb%2FsDVVxKwdwlJNNe4RkIVvUandatfgWXNK8fEy%2FteqzyGUTEzN4rbuq2lC0uiY8yBz4phwdusuwqkTkic17A6kyhx9DbuJ5Chn%2Fn%2B%2Fgf9uI8D7BleAQvRlLvt6k5vJzREPKzk2wBPOPoAWEnM7VzQfha0W28V%2FVgH3uE0ggrMBqfxm612EYw%2BS4U5gtp7TIUceKXRYQbXHepT7uyT9Q9e58k9uEUXYX6xjlJ13uST3lqN05V5dSXerb1QbjhNcgeJ%2F%2F1RHEBC3VrMnEazQyR%2FaG3yskctiAGQslnbBKQFGMOWXuOTNnrkxQfbeAGsoB2ZpoF3x0XwzhlpehHY8Dv7LuvBF%2BQ5hD5mc%2FkO9DIwCYPzTtDHFU0RywzGnsHiiqvOtlDBTvRQRV5zflouA3CoX%2BhqP3dMBpVSjeFGq9DB1ITQzwazGeCRxxGBnYJTLVqUNaX2yqO1vvV1DoXoMPDMhb0GOqUBdYWYA9e9Oz6YtGl12OXenUJECQ%2Fr3N%2Bu2iWPa3fdzD4YqofO%2FTAoLWRviv1hnLJTy8I7ZVRMdd9HNMDC9nY9vIX7YbLUXz4Rww6N22Ps4axAnxW4456j8GK5W7jNYUp5LvG%2FT98%2FHZque9JVL1KJtk8sB8NZKSTT1yWYkjWmJE5bmWusZ8dUsDZRbQ9J%2F3LOvfPx0%2Fs9XBhXv7XM2RsxdnpemI20&X-Amz-Signature=222dae2be4afc6164bbe693282b85037ca3c15f04e2c745f50bb41e1d5abecc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5UWMDA7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCZm1y9%2BL78IMuNlhxGD32qgHAIPfAp9Xs6nBpA4VUYxQIhAOdfEvS64pbLbUFPhnTOvnnk6Y%2FfiOhp8ti4KmnQBr8LKv8DCCIQABoMNjM3NDIzMTgzODA1IgzEN%2FhMQBl%2BsSJHHQUq3AMIsEi5dpRZWTG2l37rVC%2Bs5pmbQ9ov6kEo55An5w8o4Rw0Ohw8u54bdTr2f4rir306XPLU4BHB0xbh%2Bxr95YzQZIbjPLsbBeQsx7GREXDBfxah%2Fn6zXMNOwSOFsEHG3d4fUvviu0XHGtNps7pSMrExcWxdarlqCFJOPEsKZ6xRG6iejssj923Lou7oJYRRJUcCYwsvoqB50M%2FFebKa5d2zPX69I0geeQ6Aa0O%2BXTeZ334YC%2ByPSzWP%2FwxrLHPERkUruRF%2BZH67a5M2Iu%2Fys%2FSAl3XvCS%2BI0dRKQb4AU8vcq0p0JH0WTxsLhnb%2B3J7syrRW1cWM499A5EaF%2Ff9JbHHQ%2BJRzFFuSjk%2FAljR6Rjmc14jWx2h6RwzRgZEkOd%2Bd4WwB7yPp2%2FW4dRydRwv2LaACE7g04fW3TzjztCArq%2FFR9U7cn%2FlgP7ovx28ob984WxqH73tTFB%2FOF%2F6LdKMbiCMUOM9GagU5YOnWDH9seMK12nCF5ELTU27sb8SZQ8L1Kf2eE0ZaV8RSDprNMSR5BkpGo0QRve1zJEz2NJOekTgTd3UWiddXNDX%2Fqj3UKk0bbVQdGEpfehryOQBOjMpT%2FeDlGcDhVqmw2VlGijf3c%2FA0Ojnl5dk%2Bmi2LnH%2BqLDDmzIW9BjqkAdm3m5yW16SPqNr3hbiaOk0NFAzThvxfr4NAxJBZuTZl7rSnf8PnBs8FaCLhp4z1MZyHeQDJUkkLg4ffQLcmvJSvKhm%2BbMVfNTyWk%2F5ZCuBlhomJnJ7JbN3yYDYSvl9ayyZb0fwAKQ7DOoFGqvystWjnbW4Bs4dttVeDTNZ52Ajbns0LawiTKRYd9CKt073YuhAo89YPb%2BBZ0oTb4j7XME3Ip9%2B5&X-Amz-Signature=a4854d863cfda73661c5fc3948a1d1481107e3556cc715107bc79a8b17b8801e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHKNPCCZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCICVgvFEMPmutBLdQ1ynxkZvjSCX2jDE%2BsqNH0h4vdeCIAiEAvSg13jHky%2Fyf8SQ%2Friv%2FC7jX8qQgQxj%2FHCQ6CvuLf9Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDBTNOOaizld0DzTOWyrcAzw1%2FMHGzu1BUkEj7uw0sIX65KP00qUTMRa%2FIbI14neU%2Fs%2FZmLjDYiQPUqQCGSguL2KZO%2FKkXw0oXfU9mQATR2UiFibNcYxvun03%2B7AjToC2pKE0XgKj82GdyhBJguc8XIov03d5g159c9YtXt8v4LGoXg7jXBYj7LzyA8U6sZJgldwqyVl2vLA5%2F%2FKZUSNNCfqA17%2Be%2FdzP62rP0oO7jJn9ayjExvjONpSEWbxEX0wrgtMgFiODrLYwzLCiKPOitciJ79I3U%2BtRHHS03xQ95%2FAJP4u1YNvDr7iayCYBFs5MneBcOgtR6fQQ1HKfrwYkVwZyMhsP1X3JLmUA7Oh0%2BNBHNyV6ZyMrBY3uPr%2B8KhwCnyIc%2BKK%2FvSnZuQTOOQusOb%2FpEJa3dA%2F8H59kWbQDvJhlrceVBeG0Q6oDJEM%2BcvkIhcTtlibxQjPmW%2FeM4c0gINUPo7bVeAiPetht35tPCmRvI3Jtb3SCcgWwGRSGg5SNojUwY5%2BLXO7DvwoQ8zZPfwNKG28GQzLgDzQhEFmmleBpt6zOpg945RYEePIAX7GsxHtR1OoJQn2DV5RVpfR8WC5Yb6hnCf5eMni6gsLf6fwhGHwiEmyeBZcjLvaJk%2F3qJQW087U3XOGhpjo6MIXNhb0GOqUBVH22mTUd0d0ElHVIoFZAP4plXrjNieoTsTGoFDWSyyXyLveIz8Wa%2FSyU1AlVF6rXcrX8rBpcB3RfwmyhPDwjogsj%2BJFShPVIsv225FSiY0KfKyrsJWo4f9v0sk4loXh7vCaxN%2BTiZVfIc9GdbRjcBu4xODrImx8j3hJmeoxoVvH5stEx33qG683W2dLJU7LI09L4KhR24ZwFYVSPPb3BsqCDXu%2Bc&X-Amz-Signature=ff524485bdab1ba45e685753ac126e90e9392ae9ba5261fc23762b3ea6127b06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IMGMUEC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDQWFMG%2F5g8%2Bin%2B1%2FL9RIfupph3HfVoAy752VKuuuEypgIhALRRxOYRI3gEb2EtJLNCvygf%2BF8W6She3DrJV8PHnuAXKv8DCCIQABoMNjM3NDIzMTgzODA1Igz5vMHIWZWB0aIb0fIq3AOlJJOmn7D6XMiroPTpAHTUDqfKjkvYoMWkiWwmfMYJRlmoeAsy9aIkMx9DIjVH%2BLNWOtt9HTNTTcKruSCva8Pl86ijZ%2Fk0L4%2FwncjGMSxmFa33TsBnBGimocgQieTJwDTIzilEXfTNUtZpZRIK2oKxAV2c%2FyViErqNQrhS7Uca%2BQ24AyS5f1JcNnA8no3VqLKLUi2R%2FiAzpPtLZ%2B4866C1u99hgKIQXt7u4fMW99EeGPHUNVkYu8MGDD7zV%2F7GlCDXRoyn0qp%2FARUSBwIlUVN0HlXX%2BD2Q3hDxGUv3mFpvDSx2eCPcwv6d1K%2BEuKjNGAejiXNMXVaZAzaKQjudOeKZCMzxTT%2FFCXyWvL23RjBjXt55s4GfL0MW8C2JKJ6KVWA3wKOG6Utj%2BkFAolesGlJuGLrKBY6Q4hfC%2BJ6gIf8l1btbq7851ZMFeTJNSYWkKpDWBpJZJcdvizVcoe7YKWJlImSwMFSD4UC2r4aPQZWQVZ%2FfknbKWZheOjdp9%2FuEG0iEZzW%2FMHl%2BkS39oE1%2FySluG0zv8AfR5GN7xIGxjOJKSQ7XSCo%2BsitNfmxd6hWYV1rgosbY%2BQUekkpuutc34PKAEsYdRg4sRvX%2B5UfjXVsaYfxBoFQvqtWLkcEK1zDQzoW9BjqkAZWWoDWw4eta67AzZsRFEg20NgCZL%2Blf7uj1ZzrfHBJqB72Qkq%2FPFvce00ftzI5RREb7StQhJbf2mzLY%2FeKjN%2BFSi3IaJscBqnkU3p8CVI1fJq0B8N%2B%2FppgKvumb38hsx%2Fm4h7aB%2FwK0PQZvCAO0Vy4E3dHhfGZBYr47%2Bn24Zk4cLmAT%2F0sCPlnUCvHgtiuTEbeLvFpDmdbC4HZrlKOGzABuDF2H&X-Amz-Signature=042512a87dfc7dae2c74ea5eb4e07455b26b3bc22322e60b68a2dcbe6b6ddb6b&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DTTSNYT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQCR8xj7rbeZ1pMvt5RXqSHZJVUm%2F%2F9as1lW00vXsxcv6QIgf%2FpAAm5UERXGadR41Qa%2B7yiNeinFwC%2Bkpk9UQvfJ6H8q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDDlOXYZlMEguV3Y6qyrcA54kaYuEXUj8uYEE5DFAQXcUyEfsGOtsrf3slHK4KRKx%2B3lWkUcQrK16eO%2FdAZXkrZSNir%2B0evRkAweQWTwV%2FHYhwtZcD0fIjoNSEQgfuKS1Lll9ROATMOLrnG1vcghGYSzGBovcKQ4j4JRt9Mmr3Ii1is8AjbwPmCJ0cleZldiJ6Fr%2BwqdoFFXpWFbM959rsdp%2FOMCid28QfWid8nAL2EXfWhXkY%2FficCeEncM1vNUXLOvQ8yR%2FLQ9497lHYMql49CyKUVF%2Bus552OggEEHe6yf3mrb9UmSPVuNS5brabpSuy6Rtnme43I8rRlgdVZC3G6am%2FdoEhu2JLUEzdIhhNEEb%2BFRzITkWvkRv%2FQ5lWih2NfXV71NBp%2FzxEW4yg7ItE15AM9eLrGMHJhOrLqFeR6lmjoNgjQMcTCYftdWIP2X8JB%2B570HRd5M9sC%2FLBgQP8p16TzLVvysaT3J5WyjE9L1Mk8J%2BHZVKGwOUlHLOkbgRXqX3UcnXg58sZ8%2F3wFOTXfVH018U1g%2FWamEQTg4332cmsxi8myXRHd6hiuOHCpG6C7LtjXQ1Mj2lU%2Bp50dXNudaFJaaADvuxi0LpBgMrWx9cUTrQgk9dRJ0t8Rb6y47O1qZfBeEvLdKAvJmMMjMhb0GOqUBtVgV2dB0kCzLRumVWFaIggyW1e0%2BD8LCPvUcJZScjwMkUErRQL5mlZSO2YN5a3auUA2enCQty3uhAIEyAFNsFJ4FUYDw2KXDoX6SZ%2FHde0aDXl147Tf%2FCUp%2F3%2F3cvnAGv5dR2oOuKQpjdl2IIxvjvS4he2N70jb0Aemh5R1OAY%2BII9al9Niu6mM6j9velOXwnseghmwnDwYsz6Jq6QMh2Te4h%2FBj&X-Amz-Signature=90c7d3d42287cc6ea99806488dd739c122661c9d4ddf06fd618dee9ce5105ae4&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5SVT2X4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFdjor8fDlg4l4Jd0h3YH4%2F8zmLs2fq5DxIy5nOZlC0VAiAtHqxK2iTGzbJSqbXlPkehr%2BCHTx3CjGO5xSrCLRDqpyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMBMOsAwn5p8pgyqtQKtwDBNx%2BR8nXa8dCsANeCLRxcBEohgM5PnqASetp5NIbrGcGXcFit7nYOiuW1tsZBe8zq021xuVMYuFdZ6VA65WzC9aRIQkFYQasHLkSpK%2B3JCdSVXK8MlAie9hNu3WfVPah4xECfKe4bafr6kZWGEp%2F5XDrCITh3ZeTAdCCwz%2BB1O3kwKvMJbsFHLKwWli%2Fl2%2FhPczNqhShKxywZ4VTNd455SzMniWLerutiTYR4AfCKSTz%2BztkQNE4ZjGPbKiHGUoQcG5mjfDH1zV%2BPAv03W3TMHXDXdNqkk0WdzTuHxOvqmUa3J%2BKSlFhPaZewX73yt7qQ81i%2Bxf%2Fsgzh4jlEgE9wH15RT5GBaAHdF1ECqnK4E3Fo%2Bf%2Fqap7JG9JSKDa%2B%2FRAEnPs%2FvnnnSFDIE4a9CxP1sTtBUhAIzb290pd2BJ0vIomSFgcxywmq3KaHoVr6DzhHeaY74NgvlgdOpEjDQCZ6CziIlebSVl%2FwWH0o9h%2F11kEdpMmvhlXZoqGOP6bP5g8cluxbscr1FCa44cQ7WnIvn5GFSm5G1A56Q7vzGfih%2FeGtCp19mzM75ZxrzL2sAuZTGIyQb9MNFgSOrf%2F%2FmPXjwLzI7scH2biQND7%2FKwHIslwF%2BqhHqfy9CVl%2FZbowzsyFvQY6pgERopFrIwQ8ze4T7iMw8kjzvKKam%2F5jUG4zarrqs0JC%2F7BV%2FbQV3hBOwbL4TiPthBiy1%2Fi0qQq5ecn45eWUHiCoKBK9TKBhCAWmMVXPhnutFe3%2F5rjCGInfM%2FBkGYp2U%2BPZTkCOYN0ubRsYztkSZIHijw0MfGkWmF68HxzWEdqB2ZwXePZDcY0JL%2BYBpAEe8JX0invgvJjl%2BOIkw1oqN0UTjmSBOiTk&X-Amz-Signature=42b353f786e20eb8bef46e21c2448094389990336fd6b673e374159debb63089&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHKNPCCZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCICVgvFEMPmutBLdQ1ynxkZvjSCX2jDE%2BsqNH0h4vdeCIAiEAvSg13jHky%2Fyf8SQ%2Friv%2FC7jX8qQgQxj%2FHCQ6CvuLf9Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDBTNOOaizld0DzTOWyrcAzw1%2FMHGzu1BUkEj7uw0sIX65KP00qUTMRa%2FIbI14neU%2Fs%2FZmLjDYiQPUqQCGSguL2KZO%2FKkXw0oXfU9mQATR2UiFibNcYxvun03%2B7AjToC2pKE0XgKj82GdyhBJguc8XIov03d5g159c9YtXt8v4LGoXg7jXBYj7LzyA8U6sZJgldwqyVl2vLA5%2F%2FKZUSNNCfqA17%2Be%2FdzP62rP0oO7jJn9ayjExvjONpSEWbxEX0wrgtMgFiODrLYwzLCiKPOitciJ79I3U%2BtRHHS03xQ95%2FAJP4u1YNvDr7iayCYBFs5MneBcOgtR6fQQ1HKfrwYkVwZyMhsP1X3JLmUA7Oh0%2BNBHNyV6ZyMrBY3uPr%2B8KhwCnyIc%2BKK%2FvSnZuQTOOQusOb%2FpEJa3dA%2F8H59kWbQDvJhlrceVBeG0Q6oDJEM%2BcvkIhcTtlibxQjPmW%2FeM4c0gINUPo7bVeAiPetht35tPCmRvI3Jtb3SCcgWwGRSGg5SNojUwY5%2BLXO7DvwoQ8zZPfwNKG28GQzLgDzQhEFmmleBpt6zOpg945RYEePIAX7GsxHtR1OoJQn2DV5RVpfR8WC5Yb6hnCf5eMni6gsLf6fwhGHwiEmyeBZcjLvaJk%2F3qJQW087U3XOGhpjo6MIXNhb0GOqUBVH22mTUd0d0ElHVIoFZAP4plXrjNieoTsTGoFDWSyyXyLveIz8Wa%2FSyU1AlVF6rXcrX8rBpcB3RfwmyhPDwjogsj%2BJFShPVIsv225FSiY0KfKyrsJWo4f9v0sk4loXh7vCaxN%2BTiZVfIc9GdbRjcBu4xODrImx8j3hJmeoxoVvH5stEx33qG683W2dLJU7LI09L4KhR24ZwFYVSPPb3BsqCDXu%2Bc&X-Amz-Signature=050bfb735e8c3ed40741b72550b4d88664875b652c1369a40f61d27b753ab279&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4VL3IX3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIEqx87yB%2BGyg2jou4wDDgsIT4QV4eQevWHxwlL9xrS29AiEAgfFp4yOp%2FJ0MoTm21bobiN%2BPCIoAWSJiHDUm9%2BI6d%2Fcq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDBHnD0yNHJ5jnmepsyrcA5yJguFrC8vg7sMruo2ZVW6nj2KkODdAagfCxGQgeH3Y%2FsTN%2FHdCZpFQeRChm7lk4S1at%2F75BRA3YQiTXTOVQMm%2BVJ6P0gcmgmz86%2FmbnAa%2Bk0UiSlcHpSYquVc3XuvtYcdNN4dQ%2FjBTvrXeLQLbgBkrd8anjWj%2F%2BlCR71%2BZSeb8MtT5ctoHmSEbpADDPM48Mx4AZmsyL%2BVc49%2BN2rVKIlaZfj5K3tmGHyrRQ7y2s%2BM8s2cnNcI3olpNYD8Uhs12UZOB6sYK7xpYbknYKiMb4VGGQ%2FDLRSMqFtPLugmwPm7WLKzKsuYQTPNroPpGEiw%2FHTAP7JXXTFJSgW7hZUDOhZbuELU8ssFv5LeSD7fpdkj0b6efF9s8WvckAXR8OmpDvKrea%2FPaNzfjL2uexNqpGbOXKdBzelYfmTtmaTjARZJroONcbLSHgpVrOAOCgWlW%2BB0KIsKc8EodVHpXhLSndklVO8UhPvmK8rfbI7fo657EbunL70q5jmGmxLxSN1RpQOESrvoRmp2Ikib0hTEvJpcULM19QvFcRCuVWRY3AU77tLIXydBddoOwe%2F3a5fMWnMbt2ImR3L1jVATp%2BSMjHWBLSGK17hnYT18GiwhmHrOXo4NEpu%2FTY0C0VkckMNzMhb0GOqUBTZ70kVV4huk2W1WxGvWfeR385D0Pe2ckFJgRfTnmatShwhBDX1e8IpjhnE%2BK%2BjnBFHOx8kjdIPKVaURqcPeTjME6RodmrhaXodIOIAoz8AJ4TwMbgYilB%2FVfQsAzAlErALpMbB%2FUZGdjxrKtX6wa3%2Fkf7f9Vr2OgeDNTgSei%2BjZhPYsx9kaYX6PNz%2FRCxXUp8KqMwDCmKbTIdld57F8%2FrpXuMbnR&X-Amz-Signature=d718e173c7630505fd6b4f5f8909dd0051e4dfea49332362a097225da76d5ba2&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4VL3IX3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIEqx87yB%2BGyg2jou4wDDgsIT4QV4eQevWHxwlL9xrS29AiEAgfFp4yOp%2FJ0MoTm21bobiN%2BPCIoAWSJiHDUm9%2BI6d%2Fcq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDBHnD0yNHJ5jnmepsyrcA5yJguFrC8vg7sMruo2ZVW6nj2KkODdAagfCxGQgeH3Y%2FsTN%2FHdCZpFQeRChm7lk4S1at%2F75BRA3YQiTXTOVQMm%2BVJ6P0gcmgmz86%2FmbnAa%2Bk0UiSlcHpSYquVc3XuvtYcdNN4dQ%2FjBTvrXeLQLbgBkrd8anjWj%2F%2BlCR71%2BZSeb8MtT5ctoHmSEbpADDPM48Mx4AZmsyL%2BVc49%2BN2rVKIlaZfj5K3tmGHyrRQ7y2s%2BM8s2cnNcI3olpNYD8Uhs12UZOB6sYK7xpYbknYKiMb4VGGQ%2FDLRSMqFtPLugmwPm7WLKzKsuYQTPNroPpGEiw%2FHTAP7JXXTFJSgW7hZUDOhZbuELU8ssFv5LeSD7fpdkj0b6efF9s8WvckAXR8OmpDvKrea%2FPaNzfjL2uexNqpGbOXKdBzelYfmTtmaTjARZJroONcbLSHgpVrOAOCgWlW%2BB0KIsKc8EodVHpXhLSndklVO8UhPvmK8rfbI7fo657EbunL70q5jmGmxLxSN1RpQOESrvoRmp2Ikib0hTEvJpcULM19QvFcRCuVWRY3AU77tLIXydBddoOwe%2F3a5fMWnMbt2ImR3L1jVATp%2BSMjHWBLSGK17hnYT18GiwhmHrOXo4NEpu%2FTY0C0VkckMNzMhb0GOqUBTZ70kVV4huk2W1WxGvWfeR385D0Pe2ckFJgRfTnmatShwhBDX1e8IpjhnE%2BK%2BjnBFHOx8kjdIPKVaURqcPeTjME6RodmrhaXodIOIAoz8AJ4TwMbgYilB%2FVfQsAzAlErALpMbB%2FUZGdjxrKtX6wa3%2Fkf7f9Vr2OgeDNTgSei%2BjZhPYsx9kaYX6PNz%2FRCxXUp8KqMwDCmKbTIdld57F8%2FrpXuMbnR&X-Amz-Signature=04f8266dc491d9fdb4d5e9dd862cd8bee163933a4c6d2da5e0b9447e88bcaf19&X-Amz-SignedHeaders=host&x-id=GetObject)
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