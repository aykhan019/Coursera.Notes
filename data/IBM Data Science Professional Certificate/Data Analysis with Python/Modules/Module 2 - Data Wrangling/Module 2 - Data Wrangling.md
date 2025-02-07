

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZXEOFNW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA0iOr1XrthBVvbkgc5uyDbd0SDoAr%2BUNm3S2QLI0fVxAiEAv7L3nQVXaOPqx8fcfOVxRYt2ETj1j6mFuuRqVRtLPkQq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDLXLvawHlPh%2ButUO7CrcA9BCYNpg8AEJ6%2BX039pygmQ7AkmBQBMqrKhFz4YUueAOyz2nBtGHWvBfQEr2hVGKtAxznj4jaAt4fNmY88GnbVftGIKoXs8JY5%2B2cyShMgUYtASmo0YvD51jRQvgBok7E%2F2bInmHiUnRSL74w0JiDM%2F2Vp4YsRQ%2FLeJ4%2FsfXBtQdFz%2BPaLnmZxOZl0acuOp3ijHOgT4h0J0I4pEmL6opEcUXt%2BYo%2BnX0EDY1U6bmd5GRDvAWvrdG4Y%2By8t3WZU%2Bciiqso8o9a6dX9VAaUopHrozZET6ro4Fsn8Avzz4LhCPm4FL2acVBzmmTXiGs3HDVm1f3oUypIq95WmwWFtfXuKvbNBsQ1iptX%2BfPL4eeSlMQhCWZJKGW1IB7DxedNNXykbIwl0sQYBap7lty0086MSw3%2FVYwyM%2F0Jj1vb1IICgoBqSrRxMoXorYGJ3%2FKGruutEVknUXE4KnVFFgCD5OCtW10CQKPl3Y4ITJOOa8d92Ub%2B%2BZuS7SBxemjinWe%2FVjMWKaIkTzkjR1ZMFd%2BfvMDfJT0hNnOvTbz%2BDAX5emj8FnLXo1vOW0dbuIbN4zC73PTernOGL%2Ff4e9YJa1ORpQGrXr3h8SHY%2BJn4L3zWGlgTAGd6aXpuNd1ZZP9G8IgMJmhlr0GOqUBQAMb5sRli2XZ9vxNjXtsnq1UHepi6nNFB49%2BVuxtk0tqrBslMtWYxmskBwGvr9nSG4%2B5Uv6Nc%2BBDqZjkm7iNg6TIF3tiuWI9JZ82Vu00%2B6073GRarjMiChXLi7kWPW8bi8wMBETjxfglg1q46ihEtPdbr43hmFiP%2B%2FFah6c4gVI8ExiA7%2BvGplw41xGEJKSIujrn5YGRQh%2BfJl8FcRcIGxP%2BefrJ&X-Amz-Signature=64055cd71faceb11462cbd4224c7d1fe296f18c5fe742f06c54e2506d57ff5b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7OHJVPN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCs0ad4ZE8tN9D47%2FYSBbYQ%2B0zveeXv%2BAve2Hx5iqvAyAIhAM1soPClUT0d0tsQ7w5%2BtNaXyVDF%2BuPvHe0nBvNn7nYRKv8DCG4QABoMNjM3NDIzMTgzODA1IgyB0tqi0BWktXjsaOEq3AOWjqeuHJKK0%2FHWf9a3pBEks2uikal1PxQXPpVT12BraZXkEbuN0q%2Fps%2Fch8nOFs7hVLgCBO1Hda11I%2Fbmr%2B1CFN8uhWg97FU2TtLlgz7jwEmZcYtHeB3E7V84BedO3FTbTk1M5Q6Az5ydba%2BxZ%2BeAT3C7eJSnwxrbKSJAWln96xw8EaTC6LJnxUNhjmO0m8Z3Oa2Rz9VHiN%2FGTGMfWcaOQP%2F9LuouUFX2uonuvy%2FOnc%2B2o3ulW9op5X4Wigd5hPMKuILgoMB0MV2NXllHAdAm95GaGdFMlvCtfidhck1k2LVcotEq61IUpJ8vIY9rNQfqb6rcU8RuSvWNvWqmX3vOxiQAE5ewxWg3jHrTr1rW9zE4DOB5JINd7vkioH0rMVX6EyOa8If02NhvqZrxaH5wvuU%2BF%2FlJEFcJW9ksFYt1TkWgFfB8PvuI3RvY3Ltx36zxMrbjQWdVhuQ%2BUcnl6i1BHJxHEWEcTua8YKx3c6N6EzX5nl5uodNzSA2TOyItIhszV21umNP%2F3ecmDqP4LKIrL818VDAiHGDrywIxZ%2BtEpm0gZlpok5dZyAlqwBG3LdjnXmi%2BQqRxvYI2K%2BNrnh2Y%2BoRbLjPle77AV0m%2FdkddQRAyz8w9TgB47O8QgJTCLopa9BjqkAT5mgkDLqoroIFCtNq2K%2Bw0%2F1%2FgSGVVPgFhLWUKpPkYgv3hOSsEbzwMHXo1Ajd3RSD%2FFGnkDFAMLYulNIqgVCvK6HTXIfF6Vk4RXaL23EB0iWRPQWHYZiH7wucH8qeoga%2FcJseoOcSf7P%2FamE02liX4zym21OxnZh43jPBGwLnDWGJ4KmuOCadQ3exoicG5n6uAEG30ofjUibX%2FYvRukeNhamHsB&X-Amz-Signature=9fda63c1b203e184ad69d11a9b2cfc325526f9d6a3f1fdbc34189a06869a0479&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LBUDDLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCe1sfmdRMeDVq%2Bm9UehUp0U7PrxJXr4G41n%2Btqi7lTJAIhAIVu1hveR%2FgVe00j5u6RZpzbUdJduCmiJ8UlJQprHEZ8Kv8DCG4QABoMNjM3NDIzMTgzODA1IgzM7xrj1gwX2hUvIlcq3ANH%2F1KpIrQZJAad%2FkBm3QGWfkAYBmUjcGypjRVfb7PRjXfIlR3%2F2Af8mTsexfmnzNubi2c6aWoTLtWJIvszACN6deJMjLj%2Ba3LrduqHbCV2vskANpPQ5YxlGyfbGHZpSe3gMhcAUCL7bPcPUMl4e73%2BXIhbSFqMv32u18D195IUOi7HB887q386W0J3E4NoJVSsm9fRUTuUhk%2FM83vKeG69ZomplJWxaWOg%2FeADc5DnRMWUngrHnhsXVWCztQ%2B6h8sMC%2FX2%2FwA1CB1hn3Cya%2Fxpy0sojLduaUbDsjb2V3OtRTXOQGcA240umKeoVVjLx3qYZuM6j0uRIBboZPpAznfGTBJIMv%2FQrTFH5XHoZEdLS2niDlcQHctgonaN4ZCns8D%2Br76zE8VxT62P9EPFvC%2BZJ7vkrLqAXpt%2BizwrjK5pDfIm6AP8%2FUZbP5bjlo5LFrWWdx6fEz5B9jCggnrqresSzK89UT%2FebF8Q5kMegy%2B1opB8fD9eP3lnBlSeJdqqWtwRHWsCyLKxXxIKPDQ0i2cLwm2hiD9u4nhI%2FrMvrn5WzPzG7zWKN8SeaA0OHcyn9R5oQBAEfrbulV0NmTcXAjWzrEiyIBrd3SNfIuqoqjW6zKXMCyhf7OidqdPRfTCEoZa9BjqkAVR73yK1my32yE0NQyLTjsoR4O3sIRS%2FAvjZlRzpAo1jlPCuqeblL8OWp2luA%2BneqDSbfDztjXJiptcn2cJ5t0IL7DYegmpX8HqE%2Bs8%2FLMFUNuo4morNtmoQjPC5CuDxFTq4oPwzjxvfWc2gSYWcGSVA3F4icUMDypUQ%2FJaXoHU0gI9MDaVtkOtBvqhcBRyW2JW%2BRInxQJIpPYf3WVh3E%2FfxI8TG&X-Amz-Signature=f7f5a392adc78974a8e424246b15b65523355e70e3b5b2b2b404654d9780e19b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKCKJMCJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQDjiO%2BDo6DZACgYQXmO2AlbgwQDE7VBRizDwEHiKrVSAwIgU3uTQsBXxJpHhRXlrpQM09SUUG7jwmvKDyF5BeiciKkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDGjqdQB%2FU2E5iR5DNSrcA9hBMbG8r2FER0eLoMlqJBFjvEFxzqOJ38i%2BnepiDOT%2BRc8o%2FyYp2LvPt4Wz9roUonJcyBWiS%2FNBBmDEfpHa3dp%2Fh0AiKeSjVw%2F7%2Bicb1VLoHzzgUc2rz9tp6Mya6%2FGnpZwahI9VJdCNpAnllByW8bkd6eyA7550BorUdIoAXTKwjIWKPZnQlOCItkNuonh9GvdDoVzxuDQV4E7mPRnSoGcrupedNgKo9oDrFmW9fng0a88UaUWgU08NunImpcd0fVPPHWQLFwl%2Bq1OIaYJqXcVyr4PN%2BwrnxMmpHsDloNmgerHSGW%2FIhRvvvKDuuvNfg7io78BygVBkhI%2FsDObXy9hfgPpJFigD7n%2BgskSxcvFcC9iu6tGezo9nYBTw5g%2BQ3OHRneuyKmTgdJz0wSMWUNnukb%2FjTZODe2LHcUXhf7A7emR%2Bzm3WQ8mSE%2FHDnrA2b2ylG4B23H6CE3cgckyK4MWYuasap79N22CbvwBGSACgpebpNs7DP52ATF5juPXIPdrLiC6NagAwoSxqLUAJUUN7TvSnINzQvcIqXCtW%2FyjGm%2BG%2FeP0a2DeWH4qwPjVR%2F%2FieY9Km9E09J8VHSsJgs1PnT9bwdyIF23fWJFnRdY5XD%2FyzsK7sOKAKTG9aMLmhlr0GOqUBCOmoVAHdviABgZgUdpvLRzbRYbpIxgRakLWOthn7%2FQ60VioKxHt5PDShEAZ%2BuBsDv%2BAOw7OewZ3DM%2FESrGdxUIikPC088B3vnLB%2BOIstQyTy7o4dy%2BhfSdiAg6QCo72Se0vdS4idPw0a3%2F%2Bl%2FbeCv%2BxPb9sy857iH7pqMHqlG3Xqx8SIKIo6YKfMGFLk5J6vew6DVgsUNUFQjB5Up0ZyTCo5x5kQ&X-Amz-Signature=da375d748756808750998009997866828e4bddf2e26c2d46988f92bb0c839c32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SORHK7XK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIBVbqWfhsoXJee8oIpeb7Csd0eKYKhVvxr3aRUgg9ybyAiEArHbwISkRYC8iyFwTLVVrbNqjsI%2FytjE%2Byyqz902jOHEq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDPGfxqUYYNY1tk%2BlcCrcA2AiiqO65mKYMtzvHUEjcGAAfDp1aMXFcWLeNb4kTj%2BQnYGxwb2QRwGh4uvbyDBDgPOAi1Jg%2BQKVJHTFzFoFMaoF%2FlS44QIENS4%2FqNxdLKcGn7LjDyPgSDqWB03crGC6GGTSdRjJnENxQkITi3Bcsouqpq4dncJfozv97l5rPJkQ2CYCB7kWFdoNMETUe5GKmgpHMt73tG7U7hkORKG5Wmil0%2BsLFX3bc7mNozoEflaiXTcScOCEdHTLptJJusHmwP%2BAhmcaOCzVtVSvWXNb0PZUSSTQ5YaI5G7j8Qr4DqBuBM1JMom9%2FC9piGHcg%2F8I8UvfEQqTuMcq%2FNbcpOPxswNgrMmAdA%2F6BGky%2FuXfJ3isJsH2vMoUbaE8SVN7ARHeGFubIGoQ9dZ%2BjGuGm7TlP5xE%2FQM%2Bdkxt1x2qEcWGt5Z5WQKIycTcnkkpei9%2F2mYeq72vHKFOVDuFFSg8q1Ivrkr1HJpO%2BOY0YEATiZoo%2B%2FS5Kgf9vBzi1YRoy1Dw3IhVSM0O4JRivbAq0P8wcJXoUlrcAX1YaMBr7ziF7aG1XyAYXCSY07CdSmVMDSQXXA3i2zF7UhzAfH3uH%2F3dUgWILUdGk2FiFN4XlNb9EuKfIYGZZzzg8mL6VooNzrMvMM%2Bilr0GOqUBWOxGTx8rU9NcWwKeLAjCCuJvIYX6olrgqdCplSMOzyGTLqRNRpR6dvCODCqhqhELVlxtISsB1D9cMuU0ZH0PLQs9Oqqtu%2Bwa0kChDlWXmfZJoYV6o8aCqmyatsGAKNg2ZU3OpqGszDUsmHcXGYttezagHXDkxrZ46AsUoQJkrzwz39MtttWA9U2Hb4DzL4HeKh1pQ3vVYy%2FQ4E2rJlzUdfoKGQ5K&X-Amz-Signature=f72555b9c2aac0b2bf55fa4b2eb2b624075b81ed925d4ee7cc06d8e27c91b935&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZGJXDF5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIDgzUBaIAGjhmUE7bauk6NWVs%2FEbbs1aw0GTejG0BVT6AiEAsxjxoRJ4mzup6%2F4SVE%2BY%2BxaFp3P4%2FI4m%2BCqr2NgeBvEq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDDKlxMcyrjrbleFWeircA%2FX%2B7qjG841wxxKgdnfLfJq%2Ft8pokqJWCl7vMtb9q2zE%2BW4EgXLp9occPo6AfgDy6%2FFEii7d17PIDJZSQeIbnOm7yXO55c39jBXAT52tAtBje3WOZZL4cfydShlp9Ceruwf%2F59hh%2B3qpUaQcoDMISlwFnAIrtcyxLLIin%2BnwM4kTkg08y85z805oOpUiMxeOWKdv9MYvuzE5NYL6qY5sLKZMATzs%2BsPbw64xhHPU94%2FR1NJrUCNPyKIpFjtllONsRfuE69Uz6GzPzRdLvScLWdRblh8U%2Bi5LGeVT1F484pZdUm6DFweMnT6KUiK2AkwSVQDOcfS1Y%2BH3EKWcPZpkomQrCqa5HyJCXySPPIPbOZTICFAHvHm9aIUwJMbXgWF5O%2Fju3EOk8oixzu5veS1kZSyh5YsgpFy2ScTijYw5E2wCaM048xNw6z59RZ4zKNZ6UXzP40rOahAKjCYA8dCCvmDyZyFkGUd%2BDgGbJ8rgHuiecOGuHqn%2BJo8dpD%2BmbtU21sBMxV6exKSJSapJcy9oDME1VxHgHSPsN%2Bqn2qNRCr65KgZB31V32v0LYAod3xF2CYcX%2FeIZKGXL5LzoDOBvZUtUH7js3i%2BXlaPYZAeBQv5WbAJvy7itOP%2BMcwIDMIWhlr0GOqUBLNTITKWhAm0g%2FXCVjpxQgLTfqoLFdktvhEgjuimLsd5xjhn%2FtuhaTwWnszvqodeRSkmokMWlCzdZAoSjhihH6jKR%2BY51KpkYG2rczwPrwlRf4v3GbSmEF%2B%2BDPjdHj%2FhqNpyldEonWobtB%2BIpszVzT1r3YVyl3UfsAVA5AU%2FEeXrh7z9xa3AJQozMLVEworv0gKIYdxnwvnxsBDUXC11HowYnHkhF&X-Amz-Signature=67ce92b3aa98b2a469a85008dc1e9c41bf1edcd7b752d9a643534f095d8fdd16&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VCF3HQB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQC3AyyDU6jrAtFzfX7sOPGmaMcyofjKP7M8MflkrvIu9AIga1TpOV7Z0%2BwvJ5zuPuXlmrnnP3wJ1peM5dEoPHk6IXAq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDJ5TLubwt4KFL6LRICrcA5AJWtiLH5eGdhIzd1e2c8DBsQHw5GEK3N%2B6HjlISkGiSlMYyNoZwcfceIgpe9IHcG%2FloFA8I6EwdnG4bU%2FBiL9B%2F7tNVMIFrZ1jCQaWMA2dJQwdxxAQRyKTgKDwMVOMYuF4JIKsSlTMi3aNbKoV4L9l9wQUTTPVEvUYHGHo724QhwiIHd8vXV6oDUvMN86BZPBGNdaWS2GyTRV9ZrnL7QlOmTEHVLjR9bQ0%2BuC4%2BaIOifPHp3B0NVkuxlfk%2BJLZa9TKsvcDcCcFS8G2pfs4ozgt3q0DXY3LRFMTex5Sm47H33tjbM8B2lKF8cvzcOt8j2uS9969As3U69B54erDTT%2BI%2BkUYoCx%2BaOn%2BWNUjtysSMS2jSWGXLBV36WjM6hbt8VdgrzYdaOM7OqH14EF%2BHNWT1RgzeVgZU1B%2BzxTqZCa31F%2BWjJQIlf8CRQPqFSc1igQc2APTsbnHU8ljadngWHVfB6quNz99Uub23ONfsbOL6FEXm6W%2F5tLarA%2Br4sIY1%2BhNM1XeWe7DvGTsfS8Q9pxnvpeO4FboDh0zlEnOcPGj4Owb0Mom4OcNSEsDM5wmJS1qW%2BTJ3ilA%2B3m0yRu8Z8bdeb5orSJ%2BkesvAl1Gdm4cHhJH1ootGZH50RiZMOqhlr0GOqUBms3DELU18bO9hFMYqs2GvGInAYvLOk4oKq02stKxekIrReUPP6g0vRRQXeBdrCTO40QrcA4ImiKwyI8CzTOOts4Jzg1CCplJ5igc5FxmY00b5tNGtUIQwWeaW6vNZQV7klMqsoeQxMv19LWOtFjd8uCrWf6tyVM3RomY0vgYJw9d97tg9W9j%2BQdUCSuMcWoYYPPDmK%2BjG8n7ttjeAltbPwRascUX&X-Amz-Signature=92870add9dd8ff77d4f6c83d7fdfd34d21833ad9ce3935ceeef89278a3f74462&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WWCKZFW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIFK0VMGhYo0NudGNelFXRvWCTnC4XI85MEUxC%2Fxn1l3WAiAbB526tLyD%2BTnYZO4bFCUqXRIJpndbOvTtkaQDowBQhSr%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMGqda2lzyscYO%2FVXZKtwDIAYxlZCNPVD7PG4S1T6VaCbvYGcJCbCNOKcUbhSZPaOS0A8CnuAvKF1XTkgWgBfpoFySLOykgRa3RwMESYVtENLqzvkXV3b0rA%2FPJGYnpPzUhJ6uIqtx782zFTaSkZWHe2huuLwQFwZ21ZavpHWubzl%2FS1HyVbC1dxCVKEHAkJSFXyeoKOQJjn0oqKlWnt1WueHceUuAHwV8TNDSJ19tBshfvfgsz7XXZu%2BLAbXLHuEKgf52q2nLYcRmlKxfQxkYNhkXd64bWiJi%2FcTsIyzsmDWC04IvdE6i8uv8HxP65GH0nvzJ9jzAls3J2aulgMNNr48iXjb%2BihhU2WxfXykTN0tLUqUvXoo77%2F17ybsgt9rwzHbrqRYKeQsK%2F9yXydTbUKwjfmaaGkY0XUHHYUtnOPCImWHq27%2FVbN6%2BXbcD9O9C4ep0mGo429GFmqX0G%2B8U8IM1zGn3qlK8R3nOOGcR3I0PFbQHQHuMhebn%2FRwRALqdZhJHEGRgkzk7fkdJSZ1pg96fetlLZnAxdU6%2BhybYX1gQrgAQTDK8wqtZ%2F%2BfkVo%2BlBP0o0DAXu4L9fX4AhqBx5mi92temCGEPOzjwsjbg403XpmSQrUniUr1NfeReqC8y2j7JRVqEsYoAixwwjaGWvQY6pgEwbhWvESwvDCwh%2Fy0S1PIGH6d5QHYJybYx97POMFufrWbkcjDac6wkFMNOofmfj6ItAcRG0s%2BVl77PRkr%2BWphgj2aquVwkmvJYITI6ZVD%2Fvag3%2FWbR%2FiI%2Bq%2BBa5z9Dtq1bd4sTAhDfzSO2X%2BFpHpTESxGVxkkv89p4f%2B%2BmazAsfn4XZKP82ytQknevFWyzGRpySuGAhkf9Hh7NAK4%2FIz1y2HWJD6jb&X-Amz-Signature=7a558daa44a71f0e2155a2cefc067e1fbc6d06e70544d5d5e0579857dac05a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SORHK7XK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIBVbqWfhsoXJee8oIpeb7Csd0eKYKhVvxr3aRUgg9ybyAiEArHbwISkRYC8iyFwTLVVrbNqjsI%2FytjE%2Byyqz902jOHEq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDPGfxqUYYNY1tk%2BlcCrcA2AiiqO65mKYMtzvHUEjcGAAfDp1aMXFcWLeNb4kTj%2BQnYGxwb2QRwGh4uvbyDBDgPOAi1Jg%2BQKVJHTFzFoFMaoF%2FlS44QIENS4%2FqNxdLKcGn7LjDyPgSDqWB03crGC6GGTSdRjJnENxQkITi3Bcsouqpq4dncJfozv97l5rPJkQ2CYCB7kWFdoNMETUe5GKmgpHMt73tG7U7hkORKG5Wmil0%2BsLFX3bc7mNozoEflaiXTcScOCEdHTLptJJusHmwP%2BAhmcaOCzVtVSvWXNb0PZUSSTQ5YaI5G7j8Qr4DqBuBM1JMom9%2FC9piGHcg%2F8I8UvfEQqTuMcq%2FNbcpOPxswNgrMmAdA%2F6BGky%2FuXfJ3isJsH2vMoUbaE8SVN7ARHeGFubIGoQ9dZ%2BjGuGm7TlP5xE%2FQM%2Bdkxt1x2qEcWGt5Z5WQKIycTcnkkpei9%2F2mYeq72vHKFOVDuFFSg8q1Ivrkr1HJpO%2BOY0YEATiZoo%2B%2FS5Kgf9vBzi1YRoy1Dw3IhVSM0O4JRivbAq0P8wcJXoUlrcAX1YaMBr7ziF7aG1XyAYXCSY07CdSmVMDSQXXA3i2zF7UhzAfH3uH%2F3dUgWILUdGk2FiFN4XlNb9EuKfIYGZZzzg8mL6VooNzrMvMM%2Bilr0GOqUBWOxGTx8rU9NcWwKeLAjCCuJvIYX6olrgqdCplSMOzyGTLqRNRpR6dvCODCqhqhELVlxtISsB1D9cMuU0ZH0PLQs9Oqqtu%2Bwa0kChDlWXmfZJoYV6o8aCqmyatsGAKNg2ZU3OpqGszDUsmHcXGYttezagHXDkxrZ46AsUoQJkrzwz39MtttWA9U2Hb4DzL4HeKh1pQ3vVYy%2FQ4E2rJlzUdfoKGQ5K&X-Amz-Signature=5d15abfa57030071ed87dd8387852581622c20b93357c191122973c983e2c0f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YQHPSUZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIDhDaIjRC5mgvXMMp6euCH3jB4CYk3YQ6AKtgniHeWegAiEAh%2Fict9v5Ypv4JcjsQO%2BcXsEpDd%2F3%2FPQdEbjN0r78fOIq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDFimzUJ%2B7w4gDWcBcircAzapdv5%2F4j9Xt87LH%2FJrtTD1HeIQZRhKSTe2uMWiVk0w1HrOFuxVitLLwhgLPNCyU47qInZh5HeRkn5lY03FTqKNcSU8C5V%2F3tw6pJYmVF4RehXuS%2BzWYg%2Fv9rKxSDg1pHFIdQOZnvmqJPB1Muv5KJGM%2FcUkzDcZ%2FQvQfJhBcmuEECSuiK7ZN9wOqdgTMzk6zc2%2FseCssI5r8rXRGubTnTipxc9DN9rid%2FPK41lwmip8AAxqjhnXb6Fx6A9YUAk%2FwZZMwEzU%2B8%2FpVfAeVJG%2FhWsKFIfb5MM8NtkNyCFb7OrqgOPo%2FpWJjrQINsOsQuTUULyIQkkQuJYvJCUp3%2BkLFgMxdLFTdxLlRxbSL7RgKAxENqnHmZppLsn56GhgtE1cHH%2FCYZaew1s8h%2F0lLZc8gTp88ljmss9NJDnQsKzNiYHRwz7cvM4bklmN8BHxb10B9YLr8fll8BMmsu0mg1jG6llT1l2kRa8CYUzQglTsrA4iprW9%2Bqn5M3WaOIZ%2BcvyECBGA9MyCeK9F2LvRkvWmk%2BgyTAaSgnWarLY95llksxs36%2B%2FNLWMIO2dxdhjFnZSXY4ubEJC0VF6P0TcgrLz5R%2FRVBhbcnXE61soN%2B0bm%2BDBPf9%2BlEMjcqO5KuUhMMJehlr0GOqUBgj1dVhmDZbYvf1a3o0wZtmNLRhl%2B3keFzJsoJWoehoNiOfO%2FveFx6cZES5Wllfll7yVESbGxVkQ%2FMNAHZjdDVBQ30bzLStOGtH%2BPpeHGkf8rlsxnJUAKfhfC%2FO1kjYfw%2BPCgD%2BdmCrpRn6ZaNLFmicGibiamFdhawt0innBGFhh49DlgnMV7wLZCYMKP2nH93cu8Q3d9jF37%2BswUKkfSHcc2PxEi&X-Amz-Signature=023738fd026be3962fb2ba31ad3d9fe0aa350111191fbbea84aab66ebf232284&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YQHPSUZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIDhDaIjRC5mgvXMMp6euCH3jB4CYk3YQ6AKtgniHeWegAiEAh%2Fict9v5Ypv4JcjsQO%2BcXsEpDd%2F3%2FPQdEbjN0r78fOIq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDFimzUJ%2B7w4gDWcBcircAzapdv5%2F4j9Xt87LH%2FJrtTD1HeIQZRhKSTe2uMWiVk0w1HrOFuxVitLLwhgLPNCyU47qInZh5HeRkn5lY03FTqKNcSU8C5V%2F3tw6pJYmVF4RehXuS%2BzWYg%2Fv9rKxSDg1pHFIdQOZnvmqJPB1Muv5KJGM%2FcUkzDcZ%2FQvQfJhBcmuEECSuiK7ZN9wOqdgTMzk6zc2%2FseCssI5r8rXRGubTnTipxc9DN9rid%2FPK41lwmip8AAxqjhnXb6Fx6A9YUAk%2FwZZMwEzU%2B8%2FpVfAeVJG%2FhWsKFIfb5MM8NtkNyCFb7OrqgOPo%2FpWJjrQINsOsQuTUULyIQkkQuJYvJCUp3%2BkLFgMxdLFTdxLlRxbSL7RgKAxENqnHmZppLsn56GhgtE1cHH%2FCYZaew1s8h%2F0lLZc8gTp88ljmss9NJDnQsKzNiYHRwz7cvM4bklmN8BHxb10B9YLr8fll8BMmsu0mg1jG6llT1l2kRa8CYUzQglTsrA4iprW9%2Bqn5M3WaOIZ%2BcvyECBGA9MyCeK9F2LvRkvWmk%2BgyTAaSgnWarLY95llksxs36%2B%2FNLWMIO2dxdhjFnZSXY4ubEJC0VF6P0TcgrLz5R%2FRVBhbcnXE61soN%2B0bm%2BDBPf9%2BlEMjcqO5KuUhMMJehlr0GOqUBgj1dVhmDZbYvf1a3o0wZtmNLRhl%2B3keFzJsoJWoehoNiOfO%2FveFx6cZES5Wllfll7yVESbGxVkQ%2FMNAHZjdDVBQ30bzLStOGtH%2BPpeHGkf8rlsxnJUAKfhfC%2FO1kjYfw%2BPCgD%2BdmCrpRn6ZaNLFmicGibiamFdhawt0innBGFhh49DlgnMV7wLZCYMKP2nH93cu8Q3d9jF37%2BswUKkfSHcc2PxEi&X-Amz-Signature=c83674111cfa94b286b4e698b6544371cee40cb009eb5cf3f583d6f605c06bfc&X-Amz-SignedHeaders=host&x-id=GetObject)
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