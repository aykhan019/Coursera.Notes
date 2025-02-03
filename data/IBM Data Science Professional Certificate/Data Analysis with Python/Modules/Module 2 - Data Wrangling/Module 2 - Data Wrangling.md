

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEZTJDFK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQD9rNv1SBQVIPYCzxwyW01tO%2FD9LkbbA49pNMy9z858vQIhAIahQqoL27pBE%2BotbHiObdM9QVaKtYdhyuP8eytru7bvKv8DCBoQABoMNjM3NDIzMTgzODA1Igw1i6fe6BXGCZQHla8q3AM9bX7P38RuAJODzZGssyGcOqxMshTSr%2ButCoUIXHIsQNrxCcY%2Fiz%2BaqLYieMjF8qU4rxwuWARumwMPOuE7AvavenUCrr0TZXbHk0uhUlpi8MNbDov3Y5wzwA7QPhWoBkxSX5slzndLe2DiAafpCi8714mK%2BNXKiHojughwJYHpJTa5BmskPHz2AiTsmxfaIPCli0gVcirWsriGdrOx5206eP%2BescnEQ4hf80%2BtCYKxDSazaDZ4Bjgx4p6eIVTf4YAQFPvlb6l1Fz%2Frm6XZIqO7hROE6cy%2B4gP0yVQpsrAWdGwenw6kdGPCnwb3EQEO%2BAyRCc5JqVItKaCMNPLSfWw51HK%2FP3lNK%2BULQFAs4QXIY8dtbAvz7sinebCdFfCq0JUuVGWpcufwi67KKdLqJS6%2BE75v9g6JLndsWo9Srg3zyUlRcJptZQnMgOxpq4kJxL9mwdeElBKEI33O6aiVnTSQ2xppagtCyKdd9Eg9eo9%2F7YOiMaJn8RW8PMgBAfnQixrqnlbzZcXNYSr8TeBSvsfufVzmF2WaXfnjo%2F1N7rmjhNjtJqkZ%2FbAZkFhNKTdlcZIxySPHQbJB4dseyl%2FrfDoLWEGNxJzQXqphR4Vpiutr8Gh%2BJpqsCCHxERzDeTC15oO9BjqkAdf9GR5s42Vvj8HO3DnsUZ8vD3OeYZOnGgeQwryPC6rd%2FkbV3KatymK94aOrgI20ZTW9sZR2PsSD7bsCKNftA7J927G9IhGqXlJRMAwK4BByuY1HjpgUQXMhB06mc4QZmoXueOorxmIcxb7juUi3D90E0Foxo%2B%2BPEgbtJGe%2FEXroYIeKyPfA40cjl%2F4yxerpo2LDVVq2jYV6nh2LZ3O7F4PmFQex&X-Amz-Signature=29efe350cbf8164697c420358d75ecef3c1d1a76b8924072bd9d11bdf179ced8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS3NQYX4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIGd9em90CwVH8lMOFBerA4nRImj5as3nNtXtWzXofRX5AiAcKj8pMhFe6UpmeYEP4RHBnU29pM%2B7FsXC3t%2Bm7fKEjyr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMUK2EtFV%2F%2FFE41IWQKtwDf99IcSv6v61Le4d56nlomNwQGMUJWqjlvUsbLXX%2FzaNksHjRwS1fdgRNHGOxVO0%2B9cp7mYVkgkQ3cGqDOtE4GPS2deUq%2FmoNsNwOk59m1%2FIZ6r3bi6rrVpkCTRZXOsgX9EYCV243QpNSnK5b2%2B9Xovc4jVTej6%2BM9MglUEAt6urEs0uMrWoJDzkNNX69ydYgp26A1f%2FZXkpO%2FycC7ZcCWvqFsZNphf5OU%2BlwNWyAWiFfK%2F3aWwikFZ7gsmO%2B1iKRBruwl292%2FMIpFvhsFx3DZFw6PEX8JmAJqQvojKpmvyHMvHB6nZ1Nfw9zkCVSk89kiVXaMBKMKFcmCsHThZKtgcybvZ4fx%2FoGrQ%2FQBv5SY636HaIRd7nk1OTiWJbbFuqxd54CyOKhX0wMu5v8QcEjnkdECpTkGba6y0Mu%2BLYE2ggMCbsbwNFOMMxIAcB3m089mTVNRirpwMyqr9nZfc6Hfgk3wnxEBb6VgbKlizSeaMrdOnZT0VOUTqtsmhIz%2BwAAIPpzBxaRWlfeyXl2Puhg2wfj3k4H8SMhpaSyiSUbtiZUatI9P64dASsSB7R3%2BznHb7q3%2FpE4sgwcBn2HkzWUbf9sDehQVvIeEvbLy0DGNnPrnjGAKlrPQB1tuXAwy%2BaDvQY6pgHeAU5os3dDnYtfc6wKNmnwbqToNChXXYOPIU%2BC7emKdXZikvYE1DmeR8V60L902JGx9MlRlCuOHVbQReGyYdY%2FrgEGYx9zyGmWPX60MBkd65q2PxbxXjT1eYhSrcuZeZ7qoB7%2FcKAri6BZkA4nUyaso4yf69sn8W0OOB6nOoyBTIi6NfBFA5aOjsC5lqa5YOKpoT7UOvxI%2Fq8I%2Bot9KA0BHV757trw&X-Amz-Signature=5eea203ceedf5bf2ac95a7cdac96ee35a24f4a26b7a0074976a5e74ed5d7a77a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4DTEIUR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDIaXi7XMdNcFc7GoCZPI2CU2INSKep4Mcs9MT4YC86bgIgZBlvcQtRQfDspcp6gXCfPxKSiwTj%2FwsBQ4wUZTOKO1Qq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDPncwvqFZXNLbriTpCrcA8y5zEom3kgCA5CQBZLRsqQZi5LBJQG6IxtRMVFHAXlOo10n6c0uHdUKuefHMFBsc1iG9pl3xDZGHKzrNM6Ht5wlEU7oVE3CHoSoLWX5Wu%2FVSzIqaTTJ4Chyf2S1s99wXdLjBMYf3P0Mz%2FEriF9RyKjTEhfeMxZv3ZIXIwuYNtcVxol%2F1a9LN37l%2BHbp2bpMjMgmKe2eVq%2FqbR1gBxXGv7iyPZrid23laovgiRjcGV%2FiMcpY%2BPBXae3rgxJzkyVds6DVsV4yj7INqd9kMp3WhvOoQJVhU0WaCmYo5bvNgIO%2BOr%2Bn%2BTl0qPYyJFV25tWmlA3EwZXoZn9EWMCG%2FE8WoY8oYV6GrstbiAbOvtGly%2BOm641FuIi2KERQfbj4VkLhnoY7B9WSnMc32ruoWNe34h20kYRmQYAJUwYuGs2YnEJBpvfSi9SvLe6PwXuAqhaGwBJszLb5XUPcHm%2FaphsWLrYOmzM%2FahLfyjeKXOnilzY1GoFXHOBqLZizBS42GKunr5qxf9PJvq9B0ZK3pZIaEBkfHxZ32srgV9xObv5TRu6368mk6EeJqJSUAXqZe0xudRLPSmLcwRr2ldquwXYtjzAveNwWzK5u29%2FGLZ8Wk4ZLL7%2FsCJnKRk35O72AMPflg70GOqUBECrp5x0XxfqKFM%2FAoUHunceIIfWQ0g7tcwV3hmab4Xh9RYw%2BJHdyV8FjIsKBbBvzO9HB3hVDfGdXBCqxOk0%2BvKpZZqQOgj%2Fj52yDJIE1CTdNidoM6NXMq77zBCu5Ilo%2B0W9fShr7%2F3%2B1VVr2u9iGuCQ9jl58XBa7%2FcdRvsBnUNti063GR4TUTpuvbIrNRJCkSPYnfh6SF3jwIscI2SpuZeVfYlIt&X-Amz-Signature=e5e3c6889b17db79594d880145312a67bbb8de9809dbd6ada5d7c7c30a823ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XEJQY4D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIDlQ2H%2BFAI2aZGHH4GqFzIpt%2Bw0Mp0V4BC9WJ0aY3cMhAiAOHlb0bYPC2XB6bzUoR7dup%2FF7o6fA4amxQL6SsVQpwSr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMIyazMssTl%2FTUMBe3KtwDcFnoDyWFgZZQYOOjDz6HJR%2FgogqY9wphsVR1pIdri%2B%2BDIuCHSUdJl35%2FoyG9aT0S6Z1MP%2FpeQQRtKXQntKxf1sRAcKeSdJ67dEqNlNYiatwPcreuDphVL4%2BGazF8XGNsaxhpxFw5gsrbC5GLnFZgFBMOQYgS%2Fwnocq%2BG6ijhXW04E02LaY7%2FNZCCCiUKu3yza1BBwafWO%2FVnowGFfT%2F7AvzYzLHLbz0AAtQonm7TtdWaTE95TfK6HCP9Ni0fcPfj%2Fcwys%2FMoZVT5zqslXjBubIw95TPQdIZpTR2mn23FQ20sUeuk2XRidoj%2FSMU3z5KxHm3T5DslyeLJt0pkXSLUgJCgBg51TMKp9x2MxHvinTdYmgwsehVf7GvpxY%2FDf5zMYLkjmDWAXvMRLQ5za64Ft3V2H5lex6Kw%2Fd7YtXCT2JLnsOvdhH9JnPEQR9DHYxmYnRf4JMETv%2FjZjHMD336oXqrQmcJ0mOjqvoIGE8cUCmtkAJNIL8QnK5dVEMzJstaVlJLmG5HsJsSuBcLR0V9mdt7F%2FZbe%2BzbxJB1nYF6MCZ4EtTvGnnUuAzGGXcuuc5gXRLK%2F2Gj%2BlA8Wa%2B3BX5ToZQoQK5qyxhQmQDBtPTYeuyEsDvlTquSdJrxQmFUwxeaDvQY6pgHarFQz0lvYTCmqesL3Qhp7eAapWwLBHkX8vvktZzWwcPAx02LlSkjXPQ29PRNUiAYy10yJ8urgqttNPPj6nYWX2M8UmCK2diRNOPaKBykGF6pBpMBpXB8qXyZL66gfHaf2s2Vg8EyL6yj8KRXDYpeESkMgDvklcZ5T8N6omYHyo4A7d09ucZEthUnLLVoXJko9zYLDsDn55OLzEo7sUps1l8azSzsd&X-Amz-Signature=0986dd3ec429da1e4abe983a5d800242589d6a88a13296b1c4ff25a0f2029615&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIYGQYJF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQC0azKLBbgzyxkR1m4A9zS9MTkw5zJjMvD0%2ByuWuQ8k1gIhALmsjCc9ZRUJPZC54xpttTUM%2BKLCA%2FJZdiBa17lNk4q2Kv8DCBoQABoMNjM3NDIzMTgzODA1IgybzKZv7ndP0wMuolkq3ANMwA4HF01FN%2FbhxZO6kOrUHtlIUS9yB8Az%2BTEX%2B2yzDcdnn4ISiZIp4%2BZ%2FfHn2q1Vk7oQqlRcRGgm614BfJDChKZC1gnXiiN9Y7vyzktnfgK99BbdpQZGJLkKvC3EgwuGAir0lZQIjwQhYLjO8MvBWD3Lr1ghnDoNt9dzS8o%2Bb612Ezo5Brsg7ZJdkTjbLSl3kbPnRIvd803Q6md9%2Fk82brffoaum0UE2JamI5WopVHeA%2BcKESQegOZFaG%2Be4pjDmFcRxjRVAuqPl6lD04fi68YVxVvE%2FuDxG7nkjk5X4HyzhPtvcXTlF0lYBc9Leu%2FFTv0q0eyFnlnPIOog%2FOZBQh6%2BlYb%2FUWhDq2ywBj1SCFws%2FNGyGantmnLQoaehDog75ndVIfMUXK9GVNuJUB%2FS7RdMCnJv8zCgHo2cDttnqUZsWNdXKA8rQS1uxMD85%2Bc0%2BDkqOos3Gs%2BAoYMwF3J%2FH%2BeMqI532LVNsgfpn5RyF8uPJ1Kjy5xN5FFahpGPbevBR0xOF2KhgOyjcpKl7cTIGepMuVvVUGt5XSkKpBgQt2nvQfjMcF9l8U%2Fsx%2FE8jf0inU3H692c53Hnf1WcmktBAbvZyG62Wqv%2BnC9CKa9PiDNdfmaJKRPTeFq5XAITCZ5oO9BjqkAeKlghHAXc%2B49cN8mgNVj%2F3APk9wuKuO7ZghMZhC1yo5MTQZ7gJ1mXvuJzfrhJihhwbeSL7X22UdFiRIRFutflqnNPtIq2VKxAlPUsWH%2F7IBJ8om3EnraG9CqmGw%2Fa%2BfR9ZS18tehSHSIo%2Bey8usavQRHR3lCBlgHuPbMrLyx%2Bget5x9zpjTQkZUSERHc6GRFJRLHwDWbMPpGtx%2F%2BBA0pz%2BYoCB6&X-Amz-Signature=faeb513bd5f5228ad142c714bd6eec796bb68175e2fe53f227c823244d82abff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CLN76XC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQDBYLT08Q0MJmxknIqz7ObdoxnsXhpvopVD9ocPouCdhQIhAN1DxZBRgRjzpAMYlri02VueLQod3LOlfrGYlV66haZ2Kv8DCBoQABoMNjM3NDIzMTgzODA1IgyyDgTT%2BGui1O5SKrMq3AOaX2QfMQnsw%2BhX4%2FhRp7uJaP8amEWANmpZrxKp7bMv61S6Pz5ld8HcbmYmFbIPC8O%2FUEQq9719UK382HJAp5R9mb%2FRc%2Be60VOKc6gPMrn%2BURGrHOuIoPtRq67BAXVlUvU94ejKzH0NvQhyTp64AIvDJ3LjGJ%2BwubtnDk%2BYi8QRgv1y5McQ7anmJeW7cBDwXXBjlWme1qVthKsWnn4i5bw8poqBvJ5ZVmHJjOxqneEOFi%2FM6yhAMhi28zpX5B6mC5Q8bmlOxCrtNK85Y1C0tk1f1n7Ayj%2Byvsxt1R4vD2pzqMrpwRmGsn0o8UDB2ehA8eBNX81TgF1xDotTzTf9pjvV02rJVmcUhurCOjv15cZMvo63ZilmaBLcNniADmVoV2OzKYIf2nq6yms7s1FTpbsknffzAK9JzN%2BGWJ3StPDYaxSTllazQB7TJ9TaJoPkwAdcnu16OiWgtcZ4vNqbejIcTUWorznrWJj%2BWvr%2BBFhv3GFsIOC3%2BvHTlwbR%2Bv%2FjZNIVmar4Pkv%2FBL2a%2FEjwl4WcAMy2%2BPnFdIx5ULbFuekTCju37bh4uXhKvYBYAvEr6iYJLUtOUeOja6nIWiV59hdTiD71alVtYZr6DuwRKffkdE8qJVCj5Uj8Pe1g3zD55YO9BjqkAXg09C23MgCH%2BMkhaZgs8MJ6BrnapzZYg9%2BiyvsDeOYA5wOJn8U0jPGSbpDY%2FoPX6U0P3Arrzqf%2FBRokVw0qcIgD5g7Z%2BBHWuQxBkxq40zSv3ui9pQ7tFsNGgAnnxwD9lA1Xensfb5yuANwUQL1irKF1oM4awVQtuoPMs%2F3x1FpHhBlx%2BAiwhdr5%2F%2B8dnKGShdsI2ZXNE6XoqVDJwrDfY5skX5GS&X-Amz-Signature=4d59908200fbb019618e7c446857e0e1b71df4ca08335802cca9232f270b3672&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6QLGFWL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCRAbSQnTUVzSvwDtK7GWtdOkN19tO9TY4eAuLYRhEJfQIhAMyWwGpGJ7HUplpEITDy9hcv0kYgK%2Fp0N6CHgp%2BDohMeKv8DCBoQABoMNjM3NDIzMTgzODA1IgwNiYWwl5F%2F9gxOrQIq3AMGXaPomDoYByEnHcOUHBbz%2FL0L5Qb04fSoQsCNwunftOpP6Py7VcMXxjDSbUDcIBVlaHIg%2BtpFc5QLCTme8TdQQdSG7xL4wcQxc7%2BemVvInN3XXt%2BKM8DOLyWoAs025Gb69je4pEvbO5Xz62KCXjfoVtgNet4hSVHAQIxOxANqxQb%2BkUe3PoRC8sFfDNlH2xOqMT7WyS8nGg%2F6%2BZ7wFDqIgCIDKEf6mBvExpfi5GWKhjqHH7Zs%2B%2BQ9R%2FeN%2BuuGAXU8Cz1Li43xmGYOctcgU%2B0WvVRogFklsZCq0FBhccqeD1r%2F%2Bn9ExrHa6be0DMr4F5%2FnIK2uKJOzeB%2FM1zCm6jxmcp1z1dZ32PuPQ8DXU%2F9X6olxoJfKfC9VGKoZfOWRyf5UokHcFu20ZzsDByQ8dJtwuVJLGVwgxN56sfz5wwyeQnJZwg38MY9mV8ivXf%2BIQY8vmfh0vvzSwd3drypRInvmj6Ky2lhzGkyJxH0JUt8SGpbxpvRHr18dhTaFPSUXx%2FG8L62Bk6yGboWO%2B%2FMH8Qybj2RxcnfTz0gDn4u5C17aRt3rdb6X6birKXAED%2F1Fmsf%2FDSa2UM2Jzr7Rby1yQezPXPGoczWRuTwg8w7v91dYjaKVB41JnXcvVNNHjjCA54O9BjqkAd1mvrcExrw3F1H8pfFI7xMwW9tyOE9%2Fcj3%2Fl06Zf3H9UURQIiqKbZonFH0JO%2BzyM63WcfmWta7I2Jsf%2F0HGbkiFNfGqsAXjL7r9PZ3qNmVfKPM5bKATxnv4UJNkf4k7Iklc6ZIanm4qEz92GvKGeE%2Fqode8OYKZjy45SDv%2BfIxohu%2FXf6%2BvPuLs13rMT2ODZ4VLVdHp9dF7C3ZTo2yCSs5bcyly&X-Amz-Signature=6b112b03a74441e8e54da40ca368d5c2a891146cf753e60526ec419b10b16973&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH7KVF7W%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCagFaLDZbuG3WGfC2Vl6OE3OTRnmR7XDhPVg1pikBQsQIhAIPpUVJM14V0KM5X9B06WuRO3y%2BUACLXppYEljMaVSicKv8DCBoQABoMNjM3NDIzMTgzODA1IgwhkVgI6%2BiwXfsb7EUq3AMqeAs6ZfOwG17vLlRYPs%2B5bq4E5ypl36pMMs77fwgNp443kJcgfe1910%2Fi9LrUaq7gC9BpXzg8HjCy0djVQTCBCc%2F%2FPqGxOaNS3oByXECJylt%2F0oG0uJvFEvesczja5IcbSrQv7gI5ukIFIpzjpKwGiLMP%2BilNEjNWgRp%2BHqeE5WDNjUK8L457iYJe9mgGe95KM0D6sSQkre8qDPS3APXbnQyzzfl%2B4U1oAMpgB%2BJh%2FloQw8ahKjGWDFe3deU1GtLpnOp%2FTNTcoV0aLzVHjz%2FV5wz35jQ%2FZ6WDfZigmy6JE5H%2BZuBaqN9pYOxeJXfR8aQ0EnI%2F%2F%2BHJWRdsGJ4TM6YYla1F0izV8nxZez0oFQDDiYuPdnSucqnkEITuy8yzubFbYpzvziSvRvMqBHFVYPNSmh9GZ42pY6cChnvphJgAI1aHBGs8VmEeKv%2BpoG0%2FhuYMnGh2%2BcxA98c37ynRQdja7QIpLfqj5w1lt%2Bf25GSUR6KfhrXG%2FWAoV%2BEVgOxlT8c3fZhonEpWyCiMIdvDRcCK7HIF7t%2Fxrh2%2BmH8xwHEzhqK6zRdALEAVhYaK81KlleVorAJ%2F69Ep600Djk9O%2F6%2FGc0G80gQ7HyONl9hFuRl5TtKkUbYUBVm6rHQu%2BTCs5oO9BjqkAV3oZ7q6ywYKX55uIbZjCU02vKkkWFLO59Q8v6YH9Tt4Pe21xKIt%2BVn0Lyh2yiWUeKnYVdOesg4I2UsiBEtoGfcHUTr%2BXibp6HXg24vAZ5YsZNvkrlJeM59r0DAllXTv9B4eKB7nxkz1tdnqo%2FSaZzp55ayl8iBOvQTT9u1H78R5YXzG2jK0f9MJGNX%2FUK3ztSrPXH8l%2BxM%2Bg9PrgK8AX5atkfEA&X-Amz-Signature=70b24c4475271ecd0ee1ffed57754762da1c3b40560e47bd9c5aa02b667b8bc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIYGQYJF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQC0azKLBbgzyxkR1m4A9zS9MTkw5zJjMvD0%2ByuWuQ8k1gIhALmsjCc9ZRUJPZC54xpttTUM%2BKLCA%2FJZdiBa17lNk4q2Kv8DCBoQABoMNjM3NDIzMTgzODA1IgybzKZv7ndP0wMuolkq3ANMwA4HF01FN%2FbhxZO6kOrUHtlIUS9yB8Az%2BTEX%2B2yzDcdnn4ISiZIp4%2BZ%2FfHn2q1Vk7oQqlRcRGgm614BfJDChKZC1gnXiiN9Y7vyzktnfgK99BbdpQZGJLkKvC3EgwuGAir0lZQIjwQhYLjO8MvBWD3Lr1ghnDoNt9dzS8o%2Bb612Ezo5Brsg7ZJdkTjbLSl3kbPnRIvd803Q6md9%2Fk82brffoaum0UE2JamI5WopVHeA%2BcKESQegOZFaG%2Be4pjDmFcRxjRVAuqPl6lD04fi68YVxVvE%2FuDxG7nkjk5X4HyzhPtvcXTlF0lYBc9Leu%2FFTv0q0eyFnlnPIOog%2FOZBQh6%2BlYb%2FUWhDq2ywBj1SCFws%2FNGyGantmnLQoaehDog75ndVIfMUXK9GVNuJUB%2FS7RdMCnJv8zCgHo2cDttnqUZsWNdXKA8rQS1uxMD85%2Bc0%2BDkqOos3Gs%2BAoYMwF3J%2FH%2BeMqI532LVNsgfpn5RyF8uPJ1Kjy5xN5FFahpGPbevBR0xOF2KhgOyjcpKl7cTIGepMuVvVUGt5XSkKpBgQt2nvQfjMcF9l8U%2Fsx%2FE8jf0inU3H692c53Hnf1WcmktBAbvZyG62Wqv%2BnC9CKa9PiDNdfmaJKRPTeFq5XAITCZ5oO9BjqkAeKlghHAXc%2B49cN8mgNVj%2F3APk9wuKuO7ZghMZhC1yo5MTQZ7gJ1mXvuJzfrhJihhwbeSL7X22UdFiRIRFutflqnNPtIq2VKxAlPUsWH%2F7IBJ8om3EnraG9CqmGw%2Fa%2BfR9ZS18tehSHSIo%2Bey8usavQRHR3lCBlgHuPbMrLyx%2Bget5x9zpjTQkZUSERHc6GRFJRLHwDWbMPpGtx%2F%2BBA0pz%2BYoCB6&X-Amz-Signature=14e267d6932837d13f60d7794aee62ae9024dcd723b7bd8a7a68b988d408f3ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EOUERXC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQDQioPcc8MRkWMqQiD8CYI8ag88OdFhZ5F%2FkqfWFiqGNQIhALeww4zWoUZU1Guk00Zb4hi8xeEsWe8PxMCHaN76O3uhKv8DCBoQABoMNjM3NDIzMTgzODA1IgwI%2FkbVsnA0ArEuwUwq3APxAYMsMjoZjJfSojPVQGRMB%2FUdBDGTZr44HZheM5c52mOU4B1ApK9VJwiqIIcN7wRzawM8iINKmmDOsiYnsMv8Afu34nHBo91BYlTDySCjNPcicva1vShuyoQ8r4g%2B8TfMZzRWuYRFg%2BlkQcW3wIoKyQRx13cPODYHVBDHflAIfHf6anR8LpP9K4VPtyykGl%2Fi1AXSvF7PkHnBgzvYPYMGobz35m86Hu%2Fd5o%2B4tjuMQUw4XfTTWDf13wCLofaq7LoNtu%2BqdF7m%2BvPzG4%2BGPk%2F9fhC7f35gF%2BYWpy0eumjs6xP2u4UnnFTDc%2Fy2RYTV5Un8uZr6xpk1a5IzaTvECtPKyhPm71xc7Vjf%2BugVYQ9jUgaYwEdrde06Nkuk8yzo0W%2BbmTtqVvQqXnkVF6VaJcUmmllWn84HYDJmB87YMVtHkweFxV5qklh792lH%2BWeU14G06D0t9FbLlgjNNjn2DgQaXogGyrhaYm8o1QRtSp1UhllvD6oe5go%2Bk6Hg5rtxbCpRjRh2twl%2FRrMOmNdKdcQ64ixkMgQCaThyfdrhGdxb%2BhVB3folPRBNVSaIaq7c98ltm9ZZWDhNglAmf23M4XT%2B6iHE0rD%2FshVaDGFRDNm8AQOAzL5MXEu9e%2BiSOTCB5oO9BjqkATAblpKmBNCXUIC0dD7aa%2BTRydzfR39C3hyp%2BgwF7QaIHgX7xH8zPcjgjrT0J0N44VJLqMhZhgtOhUrpX7L4SHKBlGaW95SD9Z6iruio1uy%2FRZdnAJGdKdgxQYP%2B15F%2B4%2F97WsgsPb8k46X675MqawsuG52gXcLM2Z0WAG7nubpIN8OWJZoGqJnI%2BYqMLE5mTEfbvpmAQKJe7Rx%2FKz%2FdCOpD%2BV2F&X-Amz-Signature=bf655eebe639ab7994922cac96668e399929a3f54d9fd69b431f55556b15d7e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EOUERXC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQDQioPcc8MRkWMqQiD8CYI8ag88OdFhZ5F%2FkqfWFiqGNQIhALeww4zWoUZU1Guk00Zb4hi8xeEsWe8PxMCHaN76O3uhKv8DCBoQABoMNjM3NDIzMTgzODA1IgwI%2FkbVsnA0ArEuwUwq3APxAYMsMjoZjJfSojPVQGRMB%2FUdBDGTZr44HZheM5c52mOU4B1ApK9VJwiqIIcN7wRzawM8iINKmmDOsiYnsMv8Afu34nHBo91BYlTDySCjNPcicva1vShuyoQ8r4g%2B8TfMZzRWuYRFg%2BlkQcW3wIoKyQRx13cPODYHVBDHflAIfHf6anR8LpP9K4VPtyykGl%2Fi1AXSvF7PkHnBgzvYPYMGobz35m86Hu%2Fd5o%2B4tjuMQUw4XfTTWDf13wCLofaq7LoNtu%2BqdF7m%2BvPzG4%2BGPk%2F9fhC7f35gF%2BYWpy0eumjs6xP2u4UnnFTDc%2Fy2RYTV5Un8uZr6xpk1a5IzaTvECtPKyhPm71xc7Vjf%2BugVYQ9jUgaYwEdrde06Nkuk8yzo0W%2BbmTtqVvQqXnkVF6VaJcUmmllWn84HYDJmB87YMVtHkweFxV5qklh792lH%2BWeU14G06D0t9FbLlgjNNjn2DgQaXogGyrhaYm8o1QRtSp1UhllvD6oe5go%2Bk6Hg5rtxbCpRjRh2twl%2FRrMOmNdKdcQ64ixkMgQCaThyfdrhGdxb%2BhVB3folPRBNVSaIaq7c98ltm9ZZWDhNglAmf23M4XT%2B6iHE0rD%2FshVaDGFRDNm8AQOAzL5MXEu9e%2BiSOTCB5oO9BjqkATAblpKmBNCXUIC0dD7aa%2BTRydzfR39C3hyp%2BgwF7QaIHgX7xH8zPcjgjrT0J0N44VJLqMhZhgtOhUrpX7L4SHKBlGaW95SD9Z6iruio1uy%2FRZdnAJGdKdgxQYP%2B15F%2B4%2F97WsgsPb8k46X675MqawsuG52gXcLM2Z0WAG7nubpIN8OWJZoGqJnI%2BYqMLE5mTEfbvpmAQKJe7Rx%2FKz%2FdCOpD%2BV2F&X-Amz-Signature=518af7845f8beb46f6750850ed5bc572a7038aff4f633e38570f0f226ff541e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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