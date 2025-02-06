

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QS5ECGLF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIEXqEqyixBCm3wXyGmy4YRAsNwcquSMMUFOFWbDcKq51AiAbF4VLQqUmvRE7VSTummEMM1IePb5iLwKGl%2F8QB7FZpir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMW36702CWkv4RMPgaKtwDFR9NCuWe%2FX9Uxl4KwHSAoOMrCv%2FxpDe6JpYcTAhbtiXWGNsP4lfhaf4Q7PUxX9SKue1bMio6rMIn79eZBpWLCINe7I3Zw5pjzEKu3J7mpStMhnpFdVLoFRnG16vGjPaP0fLku5VmIy%2B%2FpcQjZBWPiKWndIhWBot6AzFBJ653hsJCCT5%2BzA%2FInRDHRv5FHC7eBZ60d9TxinVMzQnacbvKCtuTJuozlFqpssZCl%2FifXfPvVRf%2FZ5sCOj4aCuSEWcqgFLBtwSPLlDJh4MOo4E90hLFp1OmH6zlyEeTY8helN73vuV7cI0ASxiSVZe8fMbbCRYZHjifqou2mN5qv4Ccun6U2U087zPey%2BzFR%2BBVd2EKNlz4Nsgn%2BQr7sk2LPcz7kLRVp1ZX6TjXCfhq1Q0kMT6ID52Oy2T%2FAndS3AIudRIZugNhWz11fJjhIA0NAsc6gprQoSY9rv%2BPsfV9PBUO042pEyjT21f3QkvJJJ8DG16Ko0OsdX7wlJFcWkiWAhkgSmdat0oo8KADa5BOKQnEJfv1ednIpaLv7fpoiRbmRild10%2FmauJAYBqklyyFBq0ekIwUubHrxWpANX%2BieXsVy4l%2BrJ%2BjdT4KcU4zoDaD%2FtFZ38DHzqUBsYtzfqXwwnrWRvQY6pgFPoUs%2F5xGItUA%2BZil5CJdW2k%2BF9ST8Gx4OLITrwhbfR1RrrjnIf52fmmq%2BbwslnaXU5GHddLJfMcMtFewoQmmwbTZrNjoo%2Ff15TwTS6j%2BR%2BN11WyFTvAfJe4lTxjggh9PHlOPnpImDkdS44QUcoKVHdPxKlDoVOHJKbiAY9aKX1LuS2tjPlGyV%2F63JzsUAaHEQmjgrpsqEP69LWYk5Hrv%2BfmxYT%2Bx4&X-Amz-Signature=d8744a5a268417083425e0f506264b9a644b4c2866fcbd7e2f700070174b0b86&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EMNJ22D%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIHUAXs8Wn0JotqFlYrJfNNnTLGTJ64Ov3k%2Fako%2FJ0z8dAiEA1yF5EfKBaF71IIR78UPZ79roB5yrPm5NGEb%2FNw0Z8mQq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDId4DKackJYTbTPabSrcA%2F3mYnWq3oclO6MyYN3ZOiskXRq%2BQaxI6%2BaBqb62qfKSIw%2BwM1W8xSFYx4b4se5ZCTjta0rpjiHcVWAK%2Fng0xJnIk1PykEqsBh5nqLIKsszJvMSxRPpoA6h19rALrSap0TGmOw5xcKtfP4Uvk67Erpmc53sLNFOGZcc3eF%2FIbVS%2FwWQuZepuLYWL3Ft4vzIdKOIoeEDaBQwCjooJ8DFCObrKxbAB3D7wiyo9NeirZuujJXUyTMDjTNI%2BhP00Q6Zq1Y2PHeabZMAARMHkAroIjP1bIvkzKy04cF1NWJZpMKjBeIxbyBHokY1X3sjp0zSeEW86obd2mr%2BHrXU6FtQowaijeM7ivv4u3kC9IM4a%2BnbJGoTsmrmqR11qNbSL6HJPSTBZn7xyMyegdlKginMHHRtwcfyVX4Ew59QdGNkV%2FXH53lK4sx3%2FgSPklHq7u6hzaS7WmtM1rQ0Ryyx2NcxT%2FOn%2B6sIakpQ%2F9j2sZPtpV9lmFV7NCo%2FF1dNiT%2FKlPJwi5DbLvzpTKdeP%2BK8zgkqB%2FlA9yMheiTUSqGJ5XZ3EW9p304ACmB%2Bz2jl2dCKiQBrz1dipXqIiFxdCzHh26%2BXLJ5HQsA3%2FaSbc9%2BXULMz0tF%2FPKblqCa%2B9LGMe6OUUML60kb0GOqUBCWyv7pfN53Pm6uh4Ws%2F2cbNqEeGPcP8J3xfBTcWDrJvyQJIXU7WmKC%2Fe%2BvAlE8qgQ1L%2BkDYbUYRS0wDn5m3eCTX23SP2PX8Ood2sBEqI4HAgXC3wbyq6R%2FekFX0NFsPqAIlxrWKSbH1QKYWgRgLNY3zuvOzOhWBzAcnrNtvdVcs%2BNIfECx2uGKhsh%2FlRcZcC3SF9cyTD%2BSob73ClDMi2VTTHtUgx&X-Amz-Signature=c19ee3bd05bd5afcc048640a7061d435699380031fe6d1695fc7c7068315d2a2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUD2MGZC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCID6HBd9sCHzIwZ4tq8Hl9KAK%2FzeGM0qNIhzpyB0SxCsJAiBJgHgg70JUHdOEAO%2FXtbawg0I916C8EK5YfPQpzqOYTSr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMRgo6xYVYvqyuW2uAKtwDXHrGqPFj6zVqm6LpYa%2B4skZVOiuxVlC9qxQGhsggTtmnZPGjGen7kLvSDWgdYECzScmATYF%2B727rE%2F%2BbJY9AsRka2FCrTPe23YHTDrd5GYejz2rS%2BMB7s1oCmmRcX4QTmetRPoSBFBl4QpJRxSGG4h2B5G3Uh4EyI%2BLpj7JQ%2FXA%2F0OufknA87q%2BCH%2BCRipzf9hNlRJhx020ULpEVPlEpZhM9Gk4SGcP8zpNU6x9E3Yo3Xelllgl%2BTSRtySUOZfivjwszAAqL8mkUQ%2FsIGE0jNy9UFzlWIvHML1WiWyC8%2FD8S4jCVF2yauebn6c3wH8f%2Bn8d4J1DPuCcUvZEVJwsdhYA0MMgCaQ09P0%2F2DagaYhmgtNl%2FAGNPry5rhr%2BC9GtrNUqLO7AapxnMg1G1b69EI4hCLRmMV9BmmLK9x1S9Oy6k7xqkgXnRBS7qYQB9giH4mz%2B0caBVBBOL9mO4FD0IocuU2g0%2BC1M47FtoTkzvIzXHSV06As0LJYAH1KP2ndlqnptSC0bf0bBt%2FOBaEDAQnA19vq5gDj7Oign7C2ejnn8hBsKr5myiiPJqEGQQ7oNpuZb8RsmQ1oKXWlsRahm1%2BkXxMGInsZxg%2BeCHPWfDJ8Ylo7SPXtWsZXw%2FHuEwp7aRvQY6pgHA%2Ftn5ejBgCkqIUtaIlGFaFZyL9FHb8pR3sh%2Ffj7gknqUXHCgyAXgYU8jm%2FHgX1ZTZ7si571cfIho9UneVvpRiwJ42ENYrSuDWVuHphydBl5%2BReFcDmOeRGzVkONuKYxkzItec65nEm%2BjfgmvSMDfacxDTcol0CgDbIeh3mJCk06PuuZduYp90uKiGPq%2FKwCm1C6%2BwzIrVpTLWpzKzw8rNrLvHIBnx&X-Amz-Signature=6c15717e1b5b02ca9e0017410ed0ba646fa3d1c7262ac1d4a10f7b3c056f4abf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLW6GS2D%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDwcSnFqf%2BBp73Yjcx%2FOzwTVB3ZFs82yynOeyy0DVJbLwIhAPNJ%2Fxfz3jrF2if06rYFHeWe42SD9CVyDt31Gn%2FrZJTxKv8DCFgQABoMNjM3NDIzMTgzODA1Igwo0hFLayZX3%2FAdj6sq3AOVl%2BOWD5jdApUrMXpPeRGygZkzmQNGRSKVu8BnriKCxju%2BHRordxvPl1szLkDvpn2s1B7uQ7yQwrVsicaKLdU12aKQrbYLE2hEvxGGhhy6snyiXxFR25mcGC%2F14cNQENlj7QItzmnFye8hOpdm6KFF13QGA%2BUHvcjYIc%2BAR9EWkMZWXvUfFD4dyZxZG5ve314t83xHprnqEYwiLxvViM5EzOThgBuTUnOQCQxowvGly8J5g6p3hznA%2FE6ual%2FDGlt7u0RJ3%2BoZDZVuDA73FG0M07xXOqBYziulQnLA3k%2FFEgsutSYoZUKHku0R%2BAHUgIUqWinpNHN4KtqJBgOPBxK84dmnwq3OGmYdVNd7%2BWcz69y6u7yoBDLq2oLlMQC0ojpXf3yj%2BzN2Il26yP99KausBXIXDrs2aGKiwqyhHdcrXcbVs42ulBOxYfinZABHECpNauFABkUNN9OuiCjL86fgawt6UIuH8MHK%2FOaiBSqX3l3un99bsDHQ2E0%2B2ABz%2F1jt2NtyW2%2F4UMADYl2Z8ZCOscRifKFgT8Vm3gjV%2F%2FyBE6dNfrUQSwYiqfX7HrsUxpV3MAJgfO%2BJrZLG5AFtPsz8iGCVyeKzmV%2BPluKkafzw2RjoerOkeJW8xmh6bjD6tJG9BjqkAYKb1duj21JqZH7muuMI98WP7a0DS31uZfu2IrQWjN6GxP1DaQUYuiyD01OTaeJ1p0SEoM9gSzM6NYQftJrYAYB6e5%2FDR0lDCM1U3ILZbuzaxtlxJu%2BSuLDYjzWwh2d9nuPW2pZR6XZHGpX2%2BjoVo7dRTElr%2F9E%2FhO9fwh7f2q9SlaZEDxyikiUmoI53yIzuu3avUL%2FZAfoOGUcgc9QIP2PpebVB&X-Amz-Signature=644e5f75962468e9887a0628e4b5f26fd62672aa76b85bf3e6d8028d04ae0a66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVC4FYPT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDS2UPPMryU64v%2Fk4izM8AaVj9Qax%2FRlP1ON2JimKh2SQIhALXyiS9bQMhPDn6eWw7EhBTc0uzwyitRGn6zZL8qOP6dKv8DCFgQABoMNjM3NDIzMTgzODA1IgxCcdO6VBqZ0qG%2BVxEq3ANvkU4XzdCUW4vaGbcksBbA%2BlwIoEdxQK71EzzGWlPIc1rHfNbI%2FCsaQ87cn%2BCVzRA8gAQK7EmZywWgN0fHlpsSY9PejjR8yTckrDypz%2FZKzozTUoRM2j2R1WYUzVl2oOnrY0X5drDmr5uQhg1Aiky1UKQqPJUxpyH7sxQckhNzF35PSP0gqC%2FNS9C70%2B%2Bcp4W6MTyP3re5mxU5sFe4SP%2FRoqttlKeHu6FR0TrRYLu8%2FJCMKVPDyIujpR08XcJs2TY41o%2Fheh2slsebxzoc7YbeuxxrzTGnwScLqiukQAXGv5YgIpTIwGziiNeKL2cWXlwvxe58RxbrkwaqYVquvvRFVGbWW8QsQpRWQJw2EmhdIIweGoaWTCK5%2FeOdSWdNxAbx1NNin%2BghdJMKKoo81nGIf6C1A2L5tRIfuCb4SFdWIxxSLOulju82%2F%2FtXEIVh6mvFXToFwYyXQArO1piWTCtyqucEELujRdeS7KaZ1AmVp3uHjkZy9ZaKs54IiokdtcLSJj8k7%2F3PQy46WpB0q7%2FExkPLS7qP0UAgn6K401jdmBHv2pUkdTbhvlJOoX3rYNLfjQHo%2BBbbePaKquhhLeAuU%2BM3HPuebeha3j0p%2F%2FYvQh00TJtv1bMT0sk%2BujD3tJG9BjqkAe2k28ToOZKwNTp15iEq7LiWYJtR%2FhcgC8KDl5KpM0mPaYsOQzHvwWc7G3WEyCqDZ8u%2BDYVatfG1yYYWI6d4xpV0ZoKnc5XT7iU7A1ZuLAftXdbuta6aYifBE8cWQvQXuWIZNeY4cIgLCFFQhP97m8%2BBbeHW4DU8BUWTRWD15xwCjqoWWqiM4oQTXbaJqwVHMMDl5E2LXAa%2BOgLfEeBFMmmHPerO&X-Amz-Signature=38a0c8f6ca965585c48d88121b9dad49f37ce68e7e11a6f5c57c6bf281431952&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKUOIFYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQCuklLYB%2FzMaRrXwTNPP9FGSfrp1GMG6NUIZvJdwDMjiAIhAOLcgW9JERJz%2FLrcV7xGWfREPMWa3yvvmf9ADXYaJkUqKv8DCFgQABoMNjM3NDIzMTgzODA1IgyjG%2B2GLQqk89DQRzsq3ANJ2y8jZil%2FMJ9i53QOPlkmUOS5BQrui7B9AHvIslF%2BVByuil2EVg2Ae2sKpTdThes%2BbTOjbvFqZoYnanIihqSqW2IgA4cCUysgq6wX7G9sGBMvQ4TfX2lL3rrpUKlZW38UCp8lCNBfbPzu8e8e0CxsIO8ohF895%2BtDA2LznMpAWzfV1Uquj2y9JoB5K8d52my4Zr0m%2BN0ZVarlwPjucfSBl7TjoAunjHNTJD1u4NPbGUJ25Dz1UHx1Q0p0bbWOxKnWumhzvbNfjta%2F5DWkj6TISlKvlVCXw0fhnIqpl6qiFQ1Ul2bZWVeUN7U8WpC0Drha0%2Fp2GjBAM9Ti7138xw2vpZBo7Ih4jCOh1mBu2g9eizCx7rtB00rFQAMJqCO11m86%2BT6YWqsSngr4Vz0Vz2UEsAWwsUHVGH3Cdc%2FdG4%2Fb7Y%2F9oM65C8aO16eAHHdioZsjPqZSK9Nhcgn9z5JbOaL%2B2eMFRNSNh%2Bhvt2uXPXcYO%2BY5W97j09NB%2Fzy3aiV8NseFMf%2By%2FEDP%2FUiv8vg%2BQiTAkJdtkDW4tz2faL6L%2B26z5W1HmeEC02SSAVa1GtIZLYYk6IDwlozshXTXqovHgAc%2BkOhdAnn%2FBdV967ualC3kLOJ003%2FonHbtUAR32TDitJG9BjqkAdZPSkmVSzH8DspWobDmcFSTNBS1OP1EddsbdAdX%2BgO8V3ugycBTwn5oJB4kkFQwWBYtzfkG5Z1JsaTA%2BE0otE8%2FQxPy41vPd7%2BEsKzHT9arlAPX5h5dPgBD4gQbCy02TFRVtRAUV2YskXipgBPx88m3mfNecIRNsnmQ3gQgBffbX%2BZ%2FRy7g0YKnxv5rqESnTyUNF%2FnVB64wXKlkegAE9TXlMtB4&X-Amz-Signature=09687804d15b5c9242b3f50410a40fad7e935149bec6bdf1b36c44970cdb28ea&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QD2D4BZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIA%2FkuvyYNDADYNceb5vjfYn7rb2LZERemxcwFCgIfdpwAiA31ZLyhQQwrFISaezhDGIDo1%2B%2BpggBPhLfS9uN1fvwvSr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMsRSsFz1tXUOzEaKtKtwDTJl9yxK7f7h5M%2ByOXxsDI7SUHec8tP6SnnfbZyVb908cxf1hqdLlER8ccaSOIGIzhSJC1DUv2cGd5MDtEvthADgJv%2BliYWNENVdGGTfuEbEkOL%2BApk%2BAeXTLEaoJb9z%2FXcxeu6YE8qE9kMw%2FDLiPh04Hh%2Fzq2LiHTdsdBJWCdwpekYi5fY35yaVwhiebrmblOp%2BWssYvPj%2F2G%2Ft9M6iGOj0KJToTL5xTeekZJ8ZjlHw65HH%2FQND7d6p8O%2Bpw13FxNhFu4d%2FGMw1cSHM1DpwSw0rYqmJUlmhgiZZARLfCvidM6DmoZN%2FFvrFSfMVckhXwzOlLYcFblCVYeCgphd%2Bn3Sco%2F2tEf8OCj1pyE5LKe2nkqjmiC9Uu%2F8QwbWWjV0XZgS1K%2FhvJSn1RHvQXr1QaDd18Qi%2Bh0lWIEK8XnfSsx%2BpQ9ggmMybC1SZJiEti09DHGRE1wQbXdK0SffHhuDWe9pINlgE%2BoW7AH%2BffwEjXqaOnihPRVY5plGnLg1GnLK2VJDdjcBELUyjAb79R9Q12AUJwUMcDs%2BrF6oUfPPLmlhugvr4%2FeL%2BlNNiTBHHJZX3ocIjkeV52%2FIM5GyE7rbB9Uks9D7XB02kMZezfZMxCNlh1oiALjNm9IN6PscYwwrWRvQY6pgHK4dApb5xknBfczX%2FNJOBMhSWmCHCAiqFP39zOwFLOnc1krtQvPoYsidyLcesMMAA9VS7CI0ACvBxLnoWYmEPxi%2BhgWxaC2YGN%2F9lhO9zW6I1s2ru3rigFdjFQp1fTaJRFsIrJRNiwQ8Vu0YynmTMuMGsbqsELqUynW5RgAKFVA556Ufr37S%2Bhq0sepAzQ6QadSyXk95CTMeRw%2B6GMrXPAGjFX%2BgO4&X-Amz-Signature=b2a15fad5500bdf9cf2f2e3ac01757e2842adc7cd4afbaea65465f669e48717e&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632AH7JSZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCMizs1nDPKr0qDuTpv8HOlkDA4DCoowixPmx6C0S7LwQIgS%2FAUeEH55MqWI8lHKdN9tiRQzHZGyeegS%2BXT93YlWAkq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDJMfGHBtXsfRP4%2BSrSrcA5p2hg%2B6aI%2F%2FOjw9amvdBghYv66rZ77hujAcDrTMBulmTbjZZRaEQ9nQ6euUECZAQCMMD4KftlgcmIH3OU7K94IIj6k07jRddhY3TcNdCoOIGq0rc%2BQzSTATtftiPRo0N0%2FKLiHFjINl7dWY4%2FkTEOZLtC8pc%2FF70suiN2Y40H75PKz646PdLD%2BPntm0bxTW%2Bb6QEAn%2FOVYWTIvaiRrn7sKthjJb1jJOmsD8kjJYBFzmggzTpWooPMx0BH7NU7RMiFj2fFEwMFj7xo6aDAl6%2FluBE7kMewNIcCVS0ZKNVVMz2jiBFPM7oQ2FIVQsbaMqlCxINYoByWPZ63LdziC8t77yZJMdlHUF%2FPG5b1%2BLP%2BQrqkfTSIbe3TE5qap%2FkF%2BztYEsEI9GEqicpf3NR%2FyNGUFZd5hVupGrX86oJH10t512ijHKmcRWvyEH03Ia8ffeZUBGryBgSbYFDdiXfKNbmt%2FsqFWgfjUdSzVYJz%2BGcJ1pfqz%2Fr6vzWp7%2FTG9X4C%2BAfQ9of9WIc%2FLB0b5ExmYa8Y91lRBV%2BC%2FTB3PRV5G59qObhmNweShJgGsYgEw0AUCsjfmiKtLDzhVdRqR8KYYoiFs%2F1Stm46j0PJLUNtjNWzu7%2FZTdXK4nyi%2Bp5anUMMS0kb0GOqUBmIXDqruggUuwrMjYHjP4vWcqsvUtHmsq8wz%2FCyI5cfxz5ZgTIGTYYseAAzMCym6dnz7e4QpICbK4WSGstXtF7gfn8vPCGWFBQxBDh7MXGCp2RhKg9em3YJLijGQJR78GVbNWuimBhGwdGdyQ8hkrEbvuZeM2IPRHGlRoAPHYgA%2BSz9M1DgOGQXkb8X7Eul8ghy%2BD1DUmD0NkHWiH4uzNCmYUmY0I&X-Amz-Signature=3e4f4aae101a6a8d14459b73c3849b6d49cc2d75c4427b4653430894dd968f69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVC4FYPT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDS2UPPMryU64v%2Fk4izM8AaVj9Qax%2FRlP1ON2JimKh2SQIhALXyiS9bQMhPDn6eWw7EhBTc0uzwyitRGn6zZL8qOP6dKv8DCFgQABoMNjM3NDIzMTgzODA1IgxCcdO6VBqZ0qG%2BVxEq3ANvkU4XzdCUW4vaGbcksBbA%2BlwIoEdxQK71EzzGWlPIc1rHfNbI%2FCsaQ87cn%2BCVzRA8gAQK7EmZywWgN0fHlpsSY9PejjR8yTckrDypz%2FZKzozTUoRM2j2R1WYUzVl2oOnrY0X5drDmr5uQhg1Aiky1UKQqPJUxpyH7sxQckhNzF35PSP0gqC%2FNS9C70%2B%2Bcp4W6MTyP3re5mxU5sFe4SP%2FRoqttlKeHu6FR0TrRYLu8%2FJCMKVPDyIujpR08XcJs2TY41o%2Fheh2slsebxzoc7YbeuxxrzTGnwScLqiukQAXGv5YgIpTIwGziiNeKL2cWXlwvxe58RxbrkwaqYVquvvRFVGbWW8QsQpRWQJw2EmhdIIweGoaWTCK5%2FeOdSWdNxAbx1NNin%2BghdJMKKoo81nGIf6C1A2L5tRIfuCb4SFdWIxxSLOulju82%2F%2FtXEIVh6mvFXToFwYyXQArO1piWTCtyqucEELujRdeS7KaZ1AmVp3uHjkZy9ZaKs54IiokdtcLSJj8k7%2F3PQy46WpB0q7%2FExkPLS7qP0UAgn6K401jdmBHv2pUkdTbhvlJOoX3rYNLfjQHo%2BBbbePaKquhhLeAuU%2BM3HPuebeha3j0p%2F%2FYvQh00TJtv1bMT0sk%2BujD3tJG9BjqkAe2k28ToOZKwNTp15iEq7LiWYJtR%2FhcgC8KDl5KpM0mPaYsOQzHvwWc7G3WEyCqDZ8u%2BDYVatfG1yYYWI6d4xpV0ZoKnc5XT7iU7A1ZuLAftXdbuta6aYifBE8cWQvQXuWIZNeY4cIgLCFFQhP97m8%2BBbeHW4DU8BUWTRWD15xwCjqoWWqiM4oQTXbaJqwVHMMDl5E2LXAa%2BOgLfEeBFMmmHPerO&X-Amz-Signature=eb5c07ba5fd40e0ce21e89810976943fa5c6815df2aa8c8fb1fa3624c9614651&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3BMGX4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDSWkM9ojsw7tfKrdHgQLFFlDdWi9KgDhIHVl81jZ9ZRQIhAJ13VfY1V18k%2BGxBx4flHFZw20UaNFnD7btbo3eZ0olbKv8DCFgQABoMNjM3NDIzMTgzODA1IgwRmutt8YrWOJXsmsEq3ANgn%2FG6qgYnDAvFEb3027upy4m5dOsLtg7Rp5IMKLUBIvlGgCHMAjozFqZu6eXEH3zPnoAEFqGl5tGpCZ1TV1BkqMOKfkpbkrAAtNekcMDZi%2FehOowqhaRcM%2BcICom7%2BLpawfZaF%2FQOew9nBzASh8FdRKb6v0fhTy3knq6MI0p43e1SgV7C2f8y22oIyKJFNpKuVITI1e%2BwjBGw9ar9pp1rca7pnwuv4zQnSSn%2Fzul6WfdFm3410cmSzVvvb5Wx3DrwhgH38A5786GO60MZlYAkIKqhvI5YIr4KSJJwOWzNaDuZ6G8tcRk4ALQtvDDu6EP5QpsKMBECPromEO9cB8cM3eDexv%2FgeZPcIkPCOldk8WTr8j%2FvqgcGLceUqNGC74mKoxnsIM9IxFJq%2BG%2BwI3I5Dq18xTkqUcTHAFNAvPEHVqyGopuxwDe72BuQQRIXH41Eo3SPsNG5AdP5CbvSeGqZNiCeh31dL34QDJwbpa3ZZIGKN6tnNm31XPyEYlqMFARuLK5MeUfeMQ4wEPzwKHed0BhBK7j51IVtER%2FIZB8E6xQ5b8Uj3R5UJR4tmTE9dHx7maR3Gcu7g%2B43rYmBMUwYkl4SJDvjabIt9ch8%2F%2FBDtnepqc6ep%2BaZ7REU2TDCtZG9BjqkAf1d1kUWA%2BW2VEWvDGBEIbtj3HJiEbn1%2BwfMxzLzQVAS6cG0flnUUUg1kEh2l71SgPJPN8lFqp1X5EGXh7mRBAN%2F6Wg09SfeDdG7jxL4QkGBVNqqf69VB2it6wsratxwmvQnrkXF1BcBjkhPQZJYsOR0u%2BB8cfIiTN0IL%2Bbd%2B2GqD6QV%2FLhSBA09Ar0ubm5LSRpf8ORSfNwCvjpSEc5Vkv9Wb2AZ&X-Amz-Signature=310254a1cd50b2a072551e62c6eafe00c1c88799eba70120c0bb8e1ac31de037&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3BMGX4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQDSWkM9ojsw7tfKrdHgQLFFlDdWi9KgDhIHVl81jZ9ZRQIhAJ13VfY1V18k%2BGxBx4flHFZw20UaNFnD7btbo3eZ0olbKv8DCFgQABoMNjM3NDIzMTgzODA1IgwRmutt8YrWOJXsmsEq3ANgn%2FG6qgYnDAvFEb3027upy4m5dOsLtg7Rp5IMKLUBIvlGgCHMAjozFqZu6eXEH3zPnoAEFqGl5tGpCZ1TV1BkqMOKfkpbkrAAtNekcMDZi%2FehOowqhaRcM%2BcICom7%2BLpawfZaF%2FQOew9nBzASh8FdRKb6v0fhTy3knq6MI0p43e1SgV7C2f8y22oIyKJFNpKuVITI1e%2BwjBGw9ar9pp1rca7pnwuv4zQnSSn%2Fzul6WfdFm3410cmSzVvvb5Wx3DrwhgH38A5786GO60MZlYAkIKqhvI5YIr4KSJJwOWzNaDuZ6G8tcRk4ALQtvDDu6EP5QpsKMBECPromEO9cB8cM3eDexv%2FgeZPcIkPCOldk8WTr8j%2FvqgcGLceUqNGC74mKoxnsIM9IxFJq%2BG%2BwI3I5Dq18xTkqUcTHAFNAvPEHVqyGopuxwDe72BuQQRIXH41Eo3SPsNG5AdP5CbvSeGqZNiCeh31dL34QDJwbpa3ZZIGKN6tnNm31XPyEYlqMFARuLK5MeUfeMQ4wEPzwKHed0BhBK7j51IVtER%2FIZB8E6xQ5b8Uj3R5UJR4tmTE9dHx7maR3Gcu7g%2B43rYmBMUwYkl4SJDvjabIt9ch8%2F%2FBDtnepqc6ep%2BaZ7REU2TDCtZG9BjqkAf1d1kUWA%2BW2VEWvDGBEIbtj3HJiEbn1%2BwfMxzLzQVAS6cG0flnUUUg1kEh2l71SgPJPN8lFqp1X5EGXh7mRBAN%2F6Wg09SfeDdG7jxL4QkGBVNqqf69VB2it6wsratxwmvQnrkXF1BcBjkhPQZJYsOR0u%2BB8cfIiTN0IL%2Bbd%2B2GqD6QV%2FLhSBA09Ar0ubm5LSRpf8ORSfNwCvjpSEc5Vkv9Wb2AZ&X-Amz-Signature=7e7bf0713a392a8f3d25d32646c698fe4759e136a9059e60de75c7c6490aac1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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