

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTVQZW7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnCb35L%2FYFlrQOx0tYY%2BvC0z%2FzFcKtxVrQwk2vU3EoMAiEAvBhWWrmEFYqg3Lg%2BicWClcGnu6mnFX%2B3UUFjVK9nqsQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPS1TcIBKH6S9sigPSrcA%2FmMetQaM%2BOqOU2jIdDFliHCcZmYzyuuhQugdp26MW59ucL8M0hGDOxVv0ff4MykrLicUnIt7y5DGStb%2FIVyML0Y6eA0dIY07DjD9kGOiulMqFvYJzRa9wILDZVAvnHK521RCrQvQqgC75bo7Hjl98nO8%2B4lfg3akAYnDkb7YI2y%2FHGa87vbvdrVo%2B5xbtaxHd7193le83H2BLmD0nL7oxNlJum2gu4v7zNl%2BHMvej9KwfcdQCRYgChIq64y9uyEg3JhbiJaxWNK85POEX%2Bl0xzCJ6jTbvTVT9gmrj5zqf3yUB0Lj62eZYtW8IVBIo1FwfnfDM6fa1BTbodRY%2BktK823UAk8Mph8tVc8GUJhD3Xpp%2BduZsOOkeHKsqZzAGBdaZpnpK07ql0mKjQnsNy1NS5Uzdx3mtnUmPPyIWK9V3sStenO%2Ff0vgnn9EeZWCsBQqF5V6ZbYog3mZF9tI%2BQ5EdyyKPRqqvZktckj5o%2FgGCjekvua8TdJ9QimMIv1fo9qVijl2sBZwOL58QQ0F%2B70fco8Q6nlvYKmerk%2BFjKvnM%2FxxZVHMMIFEr9YmerTIVOmqg53Am%2Ftkn%2FRrH3%2FA27vI1jYEkd6sPrZ7UtNLR7ATWd5v4c2IqXtgHISdtkAMMjh%2FrwGOqUBAJqeziBm3ueNuyTaupH7Om7B%2BJZtRHi7p1FtMWXIvpTQn4PTubTVs3SlE0MGxyppEDoyFt3Aelkas%2FzHzGqbE2a1RfDzriUshJ0QKMWfg6foeCx%2BmLPFSRQGUx09OV337ipswus5CvHySZuniYiUErpMNw6weCm%2Bwrb2YRG7s%2FhphZg3I9igTv0Xy4heA704nkUthQqcI0dYCeaQ03OWHt0vaBnw&X-Amz-Signature=ea21b90f62ef45403241b2e9d32e50010d393f7c827a561aa20831a4565e37c8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZEIXEIX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCd%2BsBd9MVg%2BiM0QlpdBl%2Bxk3Lo7kKz3wAblsCgKVsxdQIhALjlOGddP85QW580FYt8crF2%2BsZdqEye8ubsT211m%2FQGKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwcSWQekp%2B%2F9t814u4q3AMCZF606JgKaRL8iicdRHCzYamovLxaSzezETQcvR95NKkbajJAfVXWbWCrwsRF2uQrzzPNbbiSFhm0FQ2UohzybSRmfj%2F9wAEkUC4VmxrBeBtB%2Fp96kZRAQxxiBSOn4w3TKZtY6B8wsgsTnY2%2BPz%2FsVY20IFvab7tBsoqc%2BQE1Aj9vCJG4g%2BTRizTtxR9SikmoeeLw44SRa4ZbNNecs78IdaKawflXfGqNa1THXoygFLEG7e%2FEKhe2AhWEs5XaDaShYx36fb09igaaPKjedWYD7pObexciCyK%2FEcAhUOcVuNDkKmZJU9KrIlPI0%2BMAlT5ISHLNFkym%2F3lkDixTMQxCdSLlErJFRJd7I6C0JicpI4hh4%2BpKQ0zor1lYAaE3O7VbzoSePjehOrojhTc8ne4emXL8R%2BchADlA8jTKXFOqm6GVx56dJFmeU7MPQcsSC7NeGCnzwJF6gZ3IvTp9TdEwkG%2B5srVAwGp%2F57op7At5uEMx%2FeINJCd6z7QyemFw4fJ4ykJ%2BBXRvcNbqF1Jq%2Bs0PP3tvEfnypO3DdeqnDpv6%2FQNovhPjJFUx30ZANtwwLQc%2FoMiOtL4CWUNG1tARUol1PddAhCSBcrAp5vI2ha1WOGzBUNR4Ka45yISoqzDi1%2F68BjqkAXZ8HOyu7Lytr5q%2BWKPRqETLAhTH%2BKGZIwxutJv9yLFtSz0cnfoY%2FOJqc5taKFJgLE%2FQYa9YwuiUzVaUyZqf2NZjt0j49K8Fye%2BVJtxQ%2FuBhN0mbfZqkCtPv8jPT%2BoZ7V4hWuztMRfyhayo%2FwMoFyzd%2BahvB%2FBEp%2BKOSJx3EgcKejEiqtB%2FvBFL69SfKUQJFPqJVV%2FBF1iU7G0VambTt6Pq2Bxz1&X-Amz-Signature=9572f5a58a9885fa5d2871c34beb95f5596b1fc5db5fed05e58e488a0a1e9789&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M44VUHO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYRF%2BC9PcA1bjcr86rIEmbZLvZXVPBrBMvPMp80XyTjwIgPJoK6FPgvSEvXO4cAbzXDZ5%2BkgA7MrLSie7SPPi6EJMqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGFljRHewvI447nECrcAzyO1lMN4aOnJGRG%2Fwb%2FMaH54TmhDzphIlMbvkzayiKa%2B%2B%2FFE2x8ZkmHmVZL%2F3brVpgvWZfUVe5uXN2cMs6oWySY%2FuXcVj6yt6GK3O9pLlI8yX1xXDg2c3seFfQYtcviGA392CdhgMSKj4Yjt8pLNkvjaJOND40hfqCG6nFwPFZ0OLk%2ByyFlx8vbQLAWC5ImXqds7dBKDmAvXjZ7c7En826Tciy4Gx%2FfXDfX4aXWnC2SUimJZCnwCXR8zHVw7m5tyDfmbDnbESl2WLst%2FL5ck0WIcZQ2AZsfhjK0qKHYkemOzAKNHNuCylbX%2BKdNhfVua5kpdcyC0dCsgnDDpKNlz6UpIliDzSRtD37ZrFwrrBbo4EW3o7X6%2Fcdhb0wDvt%2BhT21ka0jfayGJJvT%2FvZS1bsmR6KwkCPckrzeOUfmYrOrHf3nJKPmg7pKMinzxtMGwe94q7s3Y8thuSeWeQmRKEguoTL6kOdMcL6PUgDAPzy39eAmS9WPJgcmNALasLbY7mvqXsJvYYyQxen1m9%2FW9OLyFrgGPMrAZyw3L7eoanhWM016Rqr%2FmWj6bLl3yR4ny4SCW72HMWiEGnHk9dh6yoxdhkFXor28M0erTtwFgwjnWBdAu08XC2FumQlgNMOnj%2FrwGOqUBJGF%2Bg5iUVXgRnkamuszF2PFXzXdZxSw7hECAcjI6pcbqxz6Km9zPP4QQPBIlNBcPUE9MM1McnDjm5b0nyuwydV1cx%2FVTsB9H5aKRlEiJUTh2DkoVcCg9YIiSr1ZJm%2Bza%2Fw8riHxDYiQ3ab09I78jNj36zKwpsSKGsw0mGNMh0IaKwSiWNBUcrsKA3OQWxkJM1JlGd4SkIRdz%2B5%2BWeII5JKr3Mhhe&X-Amz-Signature=381bf139b72d8c85579327a9a8898bbb22674f3812b4aa774befa26bbc4f3714&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J2QESEH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6Dma8OpSdlLUN%2FuFkiifK4tE4bvkdp%2B%2FJPes%2BNeMRcwIgf%2BLEwSg%2F3wCTuDlvJrYYaVQNzwZOxGdm1cr%2BKCtpYmoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCoy6nxjLSYp3NkvNCrcA46bzhK41B6ofIdrZ7pXgEeSJvsXE8lK1Cukb%2BVwRq9htS36EHeYFRgS9w4uqe26wXrP1PhrlURZ9NJ8cwVEzcj%2FNXgfzDSGFne2ga9Q9cVmYuLAO4Ngm2jm9trsnXzdoRMe%2B50mMQUis%2BiXrqDAPbJC5ilUkczTLI%2BlRDliQIIFlYhBLpddvbzxFct6ChsDbHZmLDf1KzXnUaf0LMU7%2BgCcCAxYrGbkDgy7%2BAxVdGg95mmSTTBhbKe5e5A8Z7KYQumuz0Quco8521MF%2FzOCwMrPnNVapaqYdxj26KckUDm0sizRQiE25Egqd0ytuPcVgF3IvAOMcdTgVqKolE8cGcm6KANMX9ANOvkkK6AS8%2F5w%2FT%2B1LqP%2F9s71%2FuAuGOOuDvL85Zuw0NCYvKDAU6s8hDYil9ua%2BsqWHzRuSDw5TzMQr%2B6YNlLgCuANXVmqyTNpsQ%2BtiLs1NDO6xdG01F1JTF0jRqLNZ%2B320e7MsQQaqPUb1OM7h%2FXjViQzlsJTlbmm3H3wX0LhogWS0xwPgmeOEpxQR%2BByAEC614Er8hEFQJ4Kb1gdfX%2BRPX7arDcnNvKW8OSpfym7GQLo2s8CfX3Uo2xYJj1MoTigs7RLlS7j7jekhuD08F4zXAazRB%2BmMLzk%2FrwGOqUBJS60fhn562egGLO0A%2FjBOKFHFdHkfKX3y8rsSD0%2By%2BCj%2FW8DjYr3BuVvaznBaaZyHPOzOhatETZ1m6cxFpObkhJ8D96ctkl0qVQHEtaCNvQdAbv6fGXbxboIIDMr3wnomwKs%2FwENNuQi6x3LgYf0uCTP7p5xIlI8BdWNkbMyoOyBB1j9RH4Se4NHIxeVkpljQjCG%2B9NBNPdxfYWFq%2BOe1jxPbKcO&X-Amz-Signature=c3066eca10a2d2dbc50c146f6d9bbc56993c48de7ffee8705103fa751de38990&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635N3VSD4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FyKZTc9jUFL9y8VKxqHCZ1XCnycJ0jQb%2F54wcQ4IRjwIhAJl8ZlrNBwRy%2BHDtYe%2FeS%2FKMhfBogwk4B0be71za7iphKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwh2jx9jpikarHuCDgq3AMbGwcM6Uz7f4oCXxB9F%2BPTeB1CsOR1fajhcJ%2BTKpGECTTqGRMdSerEBz9iecq%2BaCoRSvKKqfxmS1wvTTe52jeS%2FQtXsYBnGgTYX12a6EdegiroQSRbLn7mGTTrr0HwiL36B0mSZPhrpSQLT94Zb4jvdDdnPP0fHfg1pZARMDA%2FYYLswn1L%2FzyCgXj14lPjgsl6XMhisN%2F3DCu2WT37OKhoOZCmtT96rRCfznCXqUyEo%2BBucLt380pOoy5EcQ4O%2FPyyRYrNN3pZaVe%2Fbh%2BsJFFC0nAIctPAtTd696o9WJ40nw9ZGqYXB7yyFgfNVcnHAlQ6oYlflMVkhXBDi8n29PKU9EqSXy3%2BTQg4L6RIJmwz5ZuQdVbBLpxYzu6Y56GSQP0k%2FVjvN05HhBZY4rbcCHpoUWlouJZUqNE5iWgudtBsKMo0ptpWNh4ta5LgjDiFXJNuSfHIblQJAv9oioRwLApNuQn7hVGDtr0Va8QDsZ4%2BQS%2B5i0mOaOPdaqi%2FZEQ%2BYqnCbO%2B9SY2z8ePh%2BqvjaydpgpOvpCVngUcL3byam5xLKwenqcxdpMprCnxVjd9CcptoPc4vEGAcKHIzBD%2BjEEETZAj0F1b5QAcowrs6X2oBR7ROa73cMedyz9gtDjC14P68BjqkAVPcU6oaAmUUHxMtjGamfpZkaV0CixHJGjnXd7ybGeBqyJrZqzZcUpjJagg8neWmhm3hThQBewaz0HQRCCtIZGoXN3Qs%2BJ30poSxnywZzVHkKE2J4d%2FDpDuxS%2BaiNnEhwnNCVoYa0QEOdF82Dvbw8ILfqdqIWVp5sgqUgcEPSqRB9V2bE1OG545lW9W8ZkvbKR5UimQ241Ip3%2FBgr2lSl5VXuNPC&X-Amz-Signature=c2b504588d6017e9e5db174201bf3018a52357b80752cae5017b6efa0aac25c3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6FJ5KU7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZquQIAa5Q9UhkIf6R54Hw3aQcqQZPDBziu7ctl%2BRR8gIhANfHyR0rIIvOcxRdqcG0ZlWVHKDfcYl7zY3kfmRK77vHKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwhrv88vMtlnh6Mnakq3ANPmp9DP%2FGQrKEmUYBBdd9KCSb2hG%2Fg1k%2Bu3ywJZcBWFEBp87PY6iNHfcumimOxkRcpmcs3w%2FJhouZy7PQ7OFP3CMk2hGfc4cSN2lQfGuhLi4OA3sbv3J7eBf2Zsgm%2F6iRy1qs%2Bb2PpWCsFyMD0RaTYXVGFWnsiRfxn3bvRTPprAM0OLpEnXdrhP9g6s0iFyHZZH%2B2SvRGYkU%2FwGsY7UQBWA68H1Miaf446J3pYcqj%2BX2Ra6i1O%2Bnd%2FebiDe%2BV1%2FDGqMClefTXGNlE1YLStXa6R1CmR5ZngRn4CuwdQR3n5DDhWdxVM33nzgJWlA0CoTuaUJIzv3BTNDn%2BXMmUeYSMkXdmccB7PGI60%2BQSJoFCFeoSQK8fL6PN1MdswPHUVcjhNMe1ZW2rAuOBefHzf1OoY2u4ZuZpWCPtXOKzU6jxFK4T0dX1GDv4c%2F5FKolPAmh%2BH5INSfhtUeT5Th3RKx%2B2BjbWjvyDbBgQgVPCnZFyEKsnBGnYLP9sqJwNfHs6RmifULkMlPbR7x7dJQCDqzNzA79v9YQqNGVDDduXMk9IYzHdreffICvRBCetag%2FJlMk6GeAspQdLSY13nCG8XrdnRpnCi9SF%2Bkhp1X5z%2FzLBw6Xg2woNBG9zo6k%2BekjCS0%2F68BjqkAcOpo6bKwRPWFNYRe%2BfH2Ami11j4bCMtdYjiC6mIRJyeqmBFfXZJZbjBiY08woA6x9RKjUgG8C0L%2BAhmUqkPNTYlnUvk12kf6BKVR9D%2BVnlmNBORrWWdkUiWmmRhoMaekabMLTAyIPZSqC7mFYZ3NlGaK1BMfZPuWTZY48%2Fq89uo7SvzX5q7Go79403%2BgEc1601lDS%2BoMqvBCqHgYxWrQmhsywpH&X-Amz-Signature=85c7eccd7aa8266c385959cd571ef1e06f2b9f292a4a7c51110b105c670ad024&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT2K5E4J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCef6x6%2BaeILxnhYkn2JfPL2Pc0hACphLiUM8RlkbcWgwIgNASgoo9KTm5oM3Xxbb1VOYQz78ALjvbBcY7fq0TyNMsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPGXkDD5r8f4V81VNircA1z1tLnLjqTIre2QwTyGdMT9L6AR4huz3kDIlrNWduSswa5g7RouVUuFpjATj%2BF79Qo0PKLLh0acg89F9xDKpgAstdfJNX1NeP7DzxSzJMQIopYsnvEdQKcnCXKqAAHCxAL1fzBjBvmK%2FhJksOrV3HtX1%2B30NX1KwuZwEuJe60LgmRTg2ZPqXe2S68g7SHcrX8VSVxhzhy1fKRfVaUym3Hk1dAJLCWRCjS2gufFQiATjmersKkzD%2BThC1UsoH0su5HCs2nTJBiE3jZEnANcpXZg6oFLD7EbmBZuOvRTn7EeC3LgIgiefLy7SH2V3%2Fk8uM1x1arIbOLXQeQBN537%2BDJgQ%2B9aUtcHeBGEoelKm%2BJgEec8NpP%2F%2FFqNXQVGjo%2BIswfujqZ%2BdTcT4iad360rcSB5ssECuzzquEaUyyB%2F5ZIC0hXZKOo3nTMDYJCxmaN0IrBB%2BuJ%2Bhe79hP8g%2FF%2Fm1akPeYAtkY4qmfW6%2BfQOh47xD1M5ou1ifC47O9Au4GZVkxGkDwp8U1Z25Vd8nAqlyKbIE4G3vKjRf2uVD3fQ%2FUc9aWdQ2D4N4ZRR1q81WHcLnryohlpiFoy%2B8pjRuww31CjsYk6JMTnPgNibBanwVI1nV%2Be5M8wxulghSclDmMITe%2FrwGOqUBpmL3EpmBHQkhbwLs3lROyqcLHXbKDmhnPtyrr6fZYXfCcRitFtGn6LWf%2FQIkZ1SROwmbXQxcGyappzvmf9eh%2FNVfez6Mw5s9hVYvK2gu88UECgVNj6GHU75wQRBCnxPf9fabHV9TOX13Ay5YMDNzidZpbJhyw0Mx8Y3qWMzddCM6XA1CwmbtgYQXcaX8XB77u%2B3z%2BUPaFUOVvlwLMHh4PceH%2FX3T&X-Amz-Signature=82a31f26f7988afd6b404f9a49ffbea740957c16bfcd8b8be3026946ddf5dcfa&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653X23VFW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG4TrsbktwXbnXHWJnGFMCDCRyx%2FvjIST3pY8%2BmIft%2FLAiAHppmlDpNGbowCsmm54MDPY%2F4le198z0O8c2ULDaTqkCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzCMzfW5uYouNblKUKtwDFPhzx9sy1VhZQH6i4AiyQ78ifo41am1IUgluh7KvQ3Hw0YUbhiCdXwns%2FC0EzgSgGNLxUSkfh682bthEkjHsil%2FB8%2BkSiA4RtMn0OAXW6JufjiKL1WPJxiMug1lGdiaIbfJ108HKGNLmmQlT18raqHr84n6on50%2B492a773GUxd4UnRhb%2F1fKn6qIpWqds%2BTwKLCvFY4sj0mMk4%2BM%2B%2Bx0AO14c1C9g%2FHIfVhhDuqglFZvtiSXuZoYsTMxiKMDuVYMI4unRlo43fQw8uQPmZjtoSWhuHmZ4YvwtLqqVScqwx3hCyuhx22%2BNaQJ18RYWc6YmdRnY0ruiqhwu2VOIRWFP6FnPKXXou8pgO%2BZXz5P9Fjl1dGhNqd1jOXSK2710Umrdqpx%2FpvwqLwZXOr%2BDjswRPVEniz%2B6vkN%2FgOSjIRoMqqFVKSGduyOz0jB7QYpjlRD0wNRU7lJ8rIB%2BSkt0Jjvo12j8rmU73HtgLgdNiNwjVEXW8SBkf8gzkoBlv21rENymvDeVDNxA5sUQWUDtYXPeGG8CFZZgpknUYdlY6ASnmSPTGiDvtB1lMmxNcyy365Djr8hKu8i1Rbcss0VNjsrpdBf6lDsGJ4dieLRjYBqPam5TW5x1iMi3ZnQqYw3eX%2BvAY6pgFIgBax2dqe1qXTE2EuV%2BNcRnlMjVfSr0%2B5Nkd9rPbK8T5%2Buu3nojv1tPBeFCglTLIZggnaI2k0NILa37CAAkYkkyNboBOLklG%2B1oRPEslS6LVXxL5xpNmZvmLOADeWaJPC45qOgxym8lKaQMhhGS2kghBWT4H8oKFypMvuDSTXKAXDw0qhCHIEgZSISKwSkmOZSi30jl8zgwEpkqK%2Bwzbp090hKYsm&X-Amz-Signature=64a8ae42f8bb8097c812fc990936066feee26069d451b40a94b72078bf63eacf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635N3VSD4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FyKZTc9jUFL9y8VKxqHCZ1XCnycJ0jQb%2F54wcQ4IRjwIhAJl8ZlrNBwRy%2BHDtYe%2FeS%2FKMhfBogwk4B0be71za7iphKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwh2jx9jpikarHuCDgq3AMbGwcM6Uz7f4oCXxB9F%2BPTeB1CsOR1fajhcJ%2BTKpGECTTqGRMdSerEBz9iecq%2BaCoRSvKKqfxmS1wvTTe52jeS%2FQtXsYBnGgTYX12a6EdegiroQSRbLn7mGTTrr0HwiL36B0mSZPhrpSQLT94Zb4jvdDdnPP0fHfg1pZARMDA%2FYYLswn1L%2FzyCgXj14lPjgsl6XMhisN%2F3DCu2WT37OKhoOZCmtT96rRCfznCXqUyEo%2BBucLt380pOoy5EcQ4O%2FPyyRYrNN3pZaVe%2Fbh%2BsJFFC0nAIctPAtTd696o9WJ40nw9ZGqYXB7yyFgfNVcnHAlQ6oYlflMVkhXBDi8n29PKU9EqSXy3%2BTQg4L6RIJmwz5ZuQdVbBLpxYzu6Y56GSQP0k%2FVjvN05HhBZY4rbcCHpoUWlouJZUqNE5iWgudtBsKMo0ptpWNh4ta5LgjDiFXJNuSfHIblQJAv9oioRwLApNuQn7hVGDtr0Va8QDsZ4%2BQS%2B5i0mOaOPdaqi%2FZEQ%2BYqnCbO%2B9SY2z8ePh%2BqvjaydpgpOvpCVngUcL3byam5xLKwenqcxdpMprCnxVjd9CcptoPc4vEGAcKHIzBD%2BjEEETZAj0F1b5QAcowrs6X2oBR7ROa73cMedyz9gtDjC14P68BjqkAVPcU6oaAmUUHxMtjGamfpZkaV0CixHJGjnXd7ybGeBqyJrZqzZcUpjJagg8neWmhm3hThQBewaz0HQRCCtIZGoXN3Qs%2BJ30poSxnywZzVHkKE2J4d%2FDpDuxS%2BaiNnEhwnNCVoYa0QEOdF82Dvbw8ILfqdqIWVp5sgqUgcEPSqRB9V2bE1OG545lW9W8ZkvbKR5UimQ241Ip3%2FBgr2lSl5VXuNPC&X-Amz-Signature=3bc3efbe01b5ae1adc65d26cf9ed91c6206e30a2f35bf5b124aa85c0cdf08ab4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EAJB4AR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2Lpc8ryoLrwlQlULqI%2B8FcLPRtq%2FfFsgjrgzXeYfTxwIhANZZwvoCXeLCGL9Pe3USq5YfNm7OkJweKw2fRaN%2Fie7FKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwkm6vmzGgTH16OocYq3AMl2cVlqa7H7kjLSbVdXmWEPChrmgHQUtxzk%2FbWC%2Fb%2BD6wuDyaxJ%2BgInEpLZor0J6547rUKagwT99zvRTIhj0fMGSHxIT%2Fqu6727hCHBbzrmsHnFxZc8MTGVKV7ggRbva8jqblmId4oHB3Y1RksTB90U7%2B7mOkg59DZo%2BvVjFB5U7OWRxq6Bwkk7yJ2XvDHE9YR5Vs2XtDUKZDhyBXMBQA9bXqwicWm04Yqq7XFeJQBMR8au%2BxzNnJ7GA0a8DEjZUToHs3tDur8peXgVEzI4bzvz1iVCGIE2U%2Fg7Oqmfa71l1%2FJfRVSmRLr1Xa9lgK5R9w2rHCksYiCUY6Vkdi5JWJ%2FP%2FMvDwOFYsMYRCZRm1bGQCKxZZCUsfUQgu0LcwSpR%2F6M5uT75wnxdYd68q8dE0efyFpH47UmsnolEAnDrazg02dYNbl0q7mLGf55%2FBXxZBlzpFEVDVmgNkPcGoOo4KTfEPE490518t8Nr1NRdPcvczrLGIq7RfHMSJF2W4jomls0CDqOY5i8W4bl8Bns8jq4qEf636dFrCsXaYIgSKs5l0y40Mt4tKRoGCnSqzfNT8rhfyGm2uxUNqW%2BntaIMlvBisR4lbcG4deaWbTpcNH4xcHlcCEg7oELPa51KzCt3f68BjqkAWeaXk%2FyJLohZzd6HCkij5v%2F8%2BsIdphpU%2BuQgvrY9FLl%2F0RIRVQH7Ai%2BJp0mKXVNlfXo3v%2B%2B5owrXcyyJ41xa1%2FUIOlZNLLAetBuPkj4gw19e6hqNTiYpy1cF9o7i3xR5GMRKbkjrsDBbCg8jIzeO3PDw%2FhgPRJoyGKK6Os%2F%2B%2BeZMoj3gHy427XlFfxlPzaYOd6Ap8Pk23T%2B6vwt2Uh00sjiTI2p&X-Amz-Signature=5f85b0466ff99a163a5f421e87a62ec4d1b94ab1509bac8b49dd4a20e0fe8b84&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EAJB4AR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2Lpc8ryoLrwlQlULqI%2B8FcLPRtq%2FfFsgjrgzXeYfTxwIhANZZwvoCXeLCGL9Pe3USq5YfNm7OkJweKw2fRaN%2Fie7FKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwkm6vmzGgTH16OocYq3AMl2cVlqa7H7kjLSbVdXmWEPChrmgHQUtxzk%2FbWC%2Fb%2BD6wuDyaxJ%2BgInEpLZor0J6547rUKagwT99zvRTIhj0fMGSHxIT%2Fqu6727hCHBbzrmsHnFxZc8MTGVKV7ggRbva8jqblmId4oHB3Y1RksTB90U7%2B7mOkg59DZo%2BvVjFB5U7OWRxq6Bwkk7yJ2XvDHE9YR5Vs2XtDUKZDhyBXMBQA9bXqwicWm04Yqq7XFeJQBMR8au%2BxzNnJ7GA0a8DEjZUToHs3tDur8peXgVEzI4bzvz1iVCGIE2U%2Fg7Oqmfa71l1%2FJfRVSmRLr1Xa9lgK5R9w2rHCksYiCUY6Vkdi5JWJ%2FP%2FMvDwOFYsMYRCZRm1bGQCKxZZCUsfUQgu0LcwSpR%2F6M5uT75wnxdYd68q8dE0efyFpH47UmsnolEAnDrazg02dYNbl0q7mLGf55%2FBXxZBlzpFEVDVmgNkPcGoOo4KTfEPE490518t8Nr1NRdPcvczrLGIq7RfHMSJF2W4jomls0CDqOY5i8W4bl8Bns8jq4qEf636dFrCsXaYIgSKs5l0y40Mt4tKRoGCnSqzfNT8rhfyGm2uxUNqW%2BntaIMlvBisR4lbcG4deaWbTpcNH4xcHlcCEg7oELPa51KzCt3f68BjqkAWeaXk%2FyJLohZzd6HCkij5v%2F8%2BsIdphpU%2BuQgvrY9FLl%2F0RIRVQH7Ai%2BJp0mKXVNlfXo3v%2B%2B5owrXcyyJ41xa1%2FUIOlZNLLAetBuPkj4gw19e6hqNTiYpy1cF9o7i3xR5GMRKbkjrsDBbCg8jIzeO3PDw%2FhgPRJoyGKK6Os%2F%2B%2BeZMoj3gHy427XlFfxlPzaYOd6Ap8Pk23T%2B6vwt2Uh00sjiTI2p&X-Amz-Signature=055152b0e7c7ec620c451b7cf2f4a9d113a54b297cc261a3ea8e555caf2815c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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