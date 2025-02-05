

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LWAUQDC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCICmkn4DNoUdDc6YklzhQgBkoFWCcA1CC5B7JpURp0RShAiEAnGbIhz2IJSxoo1TW8f6i9zgx6alzdUToFKSzwtqKB%2B8q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDC0ctAVbWbD0DUxnqCrcA%2B2fRq6glPx8L1aWmghvQPfJ%2FD5gl62CoLFmC7j%2BGFeFla%2FonizSJ2IHFZpCQPQaum1U4osjIbM9sUHcgZayCf0F8T%2BJRO9VSdv4YGGMGCeVirbsUWKiz65tUz6w5gesEtyYPIj6YNZF3JMiS5SPTJc8xoYHnktg9NSvxwNrmPVnKaAoFN%2F1OOieNohnBR41pNu3Zmj0ORfD32w8FLjdFrSUMkp%2BeT0xXXSVC7wc1GMJlsON%2FNIEehfve08rF3sb6R2Imuc9wn4Ir8jcYha%2Br2XMeva%2BcC6r5XzI62tqu1CfVp8hawBGi8nzN4fRpkZgi5I4sTQt1qetSt2P5nSYQFTbzDJITx6QDe8QaHrGoBwZXBdQcwk3I949Yd%2FsB4VdYy%2BwS%2FDCTqKqRnmnxId%2BPMcWX7mAjW6KadZ1gSbZu5Hvl5QtuzWsioLgY19QPyVQBqdrFeDsANCoB%2BuUrzBr69bw%2Fd3KMVHJrEWvLDDf1P1bshYxbEOXekemZA0obMD78fngyfyedXV2kIlGR5sxZbBFrIkmzyeHXC4Pqkp%2Bn4zr7EkbKLFrpt1nZt9P%2F%2BtDnjp21BRF0LooPOfUtfmSVAsr5ksl1mK5K%2FOaZBvutQe3dqoSjFLAkjfhVTZ5MNbvjL0GOqUBfrWv5EjdVef93YELErccjRL09i0RMzGj%2B%2B3ckTsQKHy7upnfTkXESQD3JpVxscn20bZnont7Vtm4VbscALjiEqDFanSQ3SdkKM5VJs1lqD7t2xdbiRVqWTOJ4cXKpy9Pld%2FVUjI9J0TbzLOfOuosHRFCrh%2BFZcwJJqC4Fo8%2Bfd4zg4bB%2BAj1g%2BBHo2IvteebXs4Iox4gQhj3fFNfe%2F7L7jVs09um&X-Amz-Signature=1024a7584478fc732402602545c6b50f318d96efae877f304f353d020cb790be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KFJYSIT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDJImSWF8zoNzV0J7Di9zBWs5iSgXzc8AeKZ74%2Fn0EO5AiAInvRqA2WbJj1C3ECmNE1PQ08vg1rnm0OHb%2FD1g25KdCr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMrzGhR6lfEqjvCvyFKtwDriO%2FZC1GKtiu0J9SapnTP%2BWhh2D2KkYmONoEqvjJLgUN4G1POocnVlvFM1kWThuPM6O1hCFawBSkNNKzdehGeQOPZsFa59%2Fhs5p7MaRDx3FEcj%2FUFBptJuHryGDiD3AcVX7bEbIB8Kkpd%2Frp60aqzG50ryePYreGRhzkVln%2BnfBvpS3nDmQmrsry09d4yue9zP3SxaB5C7QeFAOaOnY7Kp4Vf1xOb7btFrJLUnSQBhTW3CR%2BegYepiHlbze5f5XcwphcDXOOxOaTH6Tdxi4VJR6OzlFCAvwJHe6fNBCMnNVk030HxPb9NXzxkO8stvoHAO%2BqYZQCxXMqUrBtB65%2FsbvN8P5R9FuH3KnMH%2FJirsd0%2BRUT%2FZ2k4f5G3u7kFYEuc3ZHf%2BnJK1Z232yD9xNKAfmQqNyqgPmFgXNU72USRZsG5ccseQQp0OFrE5ip93NfC%2FpvZMSV%2Bh9LlLzkKdWoGzUqtddAk5CnWZ%2F3ht43FHipqJyvTWxFQy%2FDnqNFwC33QdgABbGu4j0GlAKVfGNldd7ESdUnrLJC4b2wkmeeNd5u82RD4HdbQY8xgDuWqUt3nqrda%2F1KfXiWxE4XTmAblKiDqRvJubn5lRwRsdeQSoe1BHU3pd4Xqu3etvwwx%2B%2BMvQY6pgFSuOjBclT6vzIz1Hz9pFlWk2j48r0ZE6v1m0PB5EFDjHznX3sZCGGx%2F5YY1RRqx67o7E%2BVX%2Fb1D8hAlhQZtL1zy384Ep3eK%2FnH%2F5LODTAj%2FSuJXhlaazKMCDx3Q8Ap4hbeLi%2BcfcpHJEYZiYLfz0%2Fdawv0Y0jpyyp5gyt955%2BgYBDENVLCMJBdmScSftLHO%2BooxBQXQfLPlx2hozu2IrHEEa1GMqwt&X-Amz-Signature=da8d5db0ab50e8a6033a2d6237542e7745ef576f8c828a4c2500c4b98014ba3b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRO3VX67%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIEwzo3A4BsxI6mSvq8m9UGMcV1TGLDN57kQMdBVWD09wAiAhwsHTfar6wT%2FYStSO8%2BB6cquF%2BVFD3mK%2FF6ZPV2O76Cr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMEds9XuOaAFbdh%2BxtKtwDuC6gwd2Te%2BBpeIC%2BT6K31IjbCvS6Wo0IsXWQcb0gz3q76aefMwJ8m%2FVNKe81%2F5hZ8a2TUeZcu1y0HDj3o3yhF%2BTje2QKMpyyAmwhC71tgS0MghnITa4YM6wlK7r8%2FWQflAJgbn6eFhjZodHAT4qWQy8LGTdq12dKIRwPt4xojGh5CoPMkG6P83%2BPlKI3B5MLU%2B9KSH3BUIEwD1VgTkcFh3mIRKCbKoou%2B1MCMIXi3rU5mpZOHis4N5IxmF8dhwE0yh2Uq1eZ03H0u8W1VPxqxNzdbm9uCGQEOYtHN2LQeNOlvGN%2FfuIBzxulrleqz9x%2BOYkXPdG3o3x2cZab4cjCSbc5KVOOBVl6t%2FEA7cswFZtXs5y22XpVxczl9IVZ9MSq0xAnh3GgPMO4pZyXeAWmFrwIZMTc3c7ZYeq4AcSUDGcmu0La82jOkx6zcRAbKiOnmhBY9n0yY%2BkltY6QGtuu%2BUcUO2Bis1EWMHjzBGCTQVF5DSmrvDn2t3558IhuW50EnraJQEXU1B0NmbmYR2exIyz%2FnPnKg7%2F4qkzLbii0DsT1EWVLBqks40V%2FRb2BrDXEPQObxZPbAHAAkcwwt%2B1tr4Ojfg3GkjyIIgAWz22TfB%2FBRL%2BH7w6qaWEHxPkw5e%2BMvQY6pgH%2FtDYvQwVU7rH2IHE5fkmXsPAAlvw380eaRzHlNAZo%2BrYCC7dlgRmRmhUV771fCCyj%2BGwCx4URTDkwjL%2BA2yGcHkKoLSTURFixHeQpAlENAddbEFZ48ryZgntNGad8iTRBr7ekQO6u2%2FK%2BeYhEfVbr%2BNaPSHb1nK0rLzOmT2jgGEvsuc5JMmQQCxuRxHeE9s92Gc6OfUG7hr9S8lgeBoLQXh82FRQD&X-Amz-Signature=394a5b5062961456ee079294596098c78ef5c757b99f7a7eb9296b80352940a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3FXVDAZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIHHbFoG5BFw3liXAo19VrTh%2FPg%2F8g5bWnYgxqtTPZa0%2FAiEAq9S2yAdTVzw8Its2XDNa8g3lqDyC0LMIgmVNEJRfqBQq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDHVe14Bx8j8%2Fb61r1yrcAxKlc3cLONNV12llGXeMhSWhwLFQVuCqUJ7i2zvGHXMk0rxw%2BjQJglte9yIi0sa5FSWkcSS4pAKQGayYB4vNXoYrFVhSjZq%2FrJ0xmMMlczuE26RS5cs6K9bEXp87A3c1USJArvRO0VZ5deJUn8TWk2SbGCsuZ6NCKxVQNJc1m3vG1nVnqE3o%2FJQeHxqGziFz2SSFHz%2BS10Ioi3vsiW7G2zTYxum7QpoErkvQIWfbMqFiO9OEtus9Y9fcCtRdt9apLZjKNATewUjUIWPRfRuDqRuklZj%2BfqZWUrZ6%2FTnpSwbJ6CHctRtxmV5w0IbgFGGqwEdMeBo7VwW8L%2B1Y%2BRji6vsbkxq5dLsizahKOyFwglI6lQh6GXg0QFxIq9WJx0ggeSWwqQq2sQX9vlbGCk%2FV115nZv4QBrWVOqYjfgwyt5TVCfF%2FtcWGK02nHy%2Bpe8dtt3OygxZ5ff2sORNf%2BiNJjedEt4rTbJa6IjhwSR6Uursqpnv4qp6zde28cu38irMRuZ5EkPUYV%2BFIo%2BFCOoXDwRjDdweKs0xe3lZcOpfFzrs3CoXXBu%2FNjYoowGx56IzNy9pAGnYvdkgSOWsjW1a5qxjG1k34c7nfnChIi1XlujhlOL4wqVvxnphS%2B62iMMTvjL0GOqUBevLJowV5bRQ3YXhwVAqjjnvmpyLCGUovEU3VsSx32wsw1S%2BBhhVxpc3Tx2R5VKSrqawyv4HeqERwVNZqpUlUfULM%2F95JxECOcuyHH93Da%2F8gjNBCwztUNA3T8gCD%2FzN7PJF5fSIkf4N%2BNk9mhNAZSu2VYryNnikVqpV66a5EIcT3LCMrNYNz0edJUFwTGabuzgA0BvGYxOE58qb%2FufCAoYFwEcEh&X-Amz-Signature=defee20103d8d5a736e63bdac439ae13cf552d25768faa8dff7ec952d7b9e5d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YN7PAS4O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDI%2BmNpdBHEqnW2NW5FXvZ3%2BN9USD6t1SsNQkySqIvMQwIgDwL4GvLZJuSsmdm2oc%2B5D9buXv2SLVsEy67X%2BNPIXekq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLeXtLBooT%2FUb9jbfircA1tvv3yLnDBIrNNkzVfoxb2LG66Cukj9IDz%2FqsyIICruIetQo9KCvD84MoSnZZvmVgGq8MhC2MShs7fq26s15DfBPcc9p0%2BeFvA%2Bux3f17sR7dcrHU%2BJjsyMip7n%2FAUZ6fzFFYubfiC7qopypUSObwZxRZoV4MLuL2sa%2BtI1pCvE029LKCU2udd%2BfZVD5t6kRhoDhnmmi%2F70099kDTqaefAh%2Fmn3vA4cuh1IuE4SpeFeURw8q%2FDW2xxLyWX%2BkEss8uLOQ0DjdGQmmIC8JxPnLoxoIpyVmhD9lvashtHpL%2Fe2bCnGTRWRoXbpbI%2BR7AOGpRatdAZjpYrg3OMBT4RgnHCdCTkje4oKSdzT0KzE4e9ieaeMvaKVnXylC%2Bv%2BrdhmVMNcJxvyGVEjpCO9VHn3621Zu4Bdt%2FfnovMGO35aX%2FcZL67LkFPPGJB%2FOmagsuQ7w7WzEpjcKpEkdyvVyJ%2Fih%2FZzpKyrWv4YMge9y1GXMHXh1W%2BQJf5YhBRE%2B3kMI8vRHFKoQZumBrD%2BBUkhWgjA%2Ftr4RNwG6b8GRyqdQXTwMPH%2BbIVKAxQGgEBoAG0AiZw7Tt%2Fc5cJaFiXy2JN83Cto3FOTrXFDMSjlUP6jLNimhSe3U1OyVqupgKl6pFaKMK7vjL0GOqUBuSoxvyFdUvwz%2BWNmr6gLlwcCsHTDuNstHyNqjxHUWbf4KtcT%2FxOVczhKWOs0qLtxL09E54CFSGX9xmSAOGfxpg2sKvIGmK2oDBx95jt73tNebu3QxP5m%2FZU9ZcVO8E4w%2B8x4tycvHxFGgyRoW8CA0%2BeL4fNgW2chJiJnBYZieJr%2B0Hg%2BALtLTPzrM053I2DfZa8cWEnl9od3it7Bo%2BKPIMEY1RJe&X-Amz-Signature=f5986c98bee1d7e2ecadb96a24ee7b086c1192eda52cc7d2d1e5bb346f436ae4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM3KKTXI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDmbKTjJz11spD9CjhiQpPDr5AjM0Dhk0Z7jeYSHB%2FqAAIgKOEuAC3Yt5CK9T%2FxFABz7IjbN%2B6IULFve0E7JBDKVmIq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJWWZ0xA4ngl52raBircA62ztoXcGm6Yypfj7K6qYB8POYu4KJnSqrVc0gFuT8Prz85aXPknSBqE4P%2BihxYUy%2B7RCfX9jY2wpbsKdpVwsJalDGoQvUW6DO19oprHPzJ4a%2BkTBojivRO6FhtulHcYni7m%2FI7d7NAqoDsdMQN%2FeEUxbfVSzvpiSzy%2BNtOsmE%2FjovFcp4L%2FUIhPJDz0VoiBwWdTU0nlVlYgS6ky2MABzTODQU2RuazRrKbSAimkpGmYJ9q0ydvMJ7kL73%2F1fY2a%2BETyAjFI%2F9v%2BX28AMQ6HNI1iQ8PyioNlaQnLr%2FrnEqb3YNmnVYldVqSJ4Src6QXx7tVWLkqeoor%2BFSjSLs0TrHABMGHF7DtE215jBsyu3CTI54ugoXiMTXs9EQusuEAaIjGI3nuudiFp%2FoQ8meiRqa%2BqMxKGi8CsyQYS2UZyKXMm4kXYd8G7HhJyphFstP5oIyai2M0aIYNi68VDD0zN9KgmUr7Glk6QxfIVyQb0p%2BCj%2FT%2B9MKGxWvi7COe%2F3rreC6mHTn75J8U%2BiOh9pOkd3BJsDlJYHNuX2a%2BlLDd4oBbXTfvKTYSETCn2pNjU8AS%2FmireNoBZ%2Fsqaltm5OjUuXDGFp75yc1JlwIp9m1tGIl3amfoGJ7BB%2FeRZzrJXMK3vjL0GOqUBYzIqS9Kv%2FWPJtZlkpqqgdNoR4gxL6IGKCRNC1D7EGwojchFz1WgWmE%2F2Zjiq5hDsKdrbWULg1JZDvkRSsyKDiZT8ENYbr9VDFpZaTfX%2BIRom55usYihjSOUn8tQndDAqZeQvq5ibBhxKtyeF7n5dYgRcdEgWwZyOHLOTXIK1ndT252H8n5iiH8lUu6lIcoKCeIdW54vEpjXamofXUaAIeMXzN%2B66&X-Amz-Signature=1d364a8feb5f61478871f38f3a09dfc842589bcf6ec2e36deaa924f71c5acc71&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HX3H52Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCMTST35RStseqhWhZx1caqXRylPXpgWAXqegDS43XDdgIhAN4I0Mxc2SOe6ZF42DW%2FEKBaack0x%2Fdt8btMIt%2Fg6fdzKv8DCEMQABoMNjM3NDIzMTgzODA1Igw%2Fr%2FSAIjFBHlSuCA8q3ANPYB7aMDUJw13wSHnjneJEvfdVOEJBIw%2BBgrsj5u5pXyeYZlNE3kP3GGhJIKpr9utCTxwycXjifmXJvRCpIEnaJoHd4YfvF6DoiE3z6K4ZT5Fl2yCqGMpNZbYm3YLtsLs6TB%2BqzJ9Cjr5lFoGFeAQn0Lf%2BSrxsMxcL7EnQaG15wxEahXl5HQnLFLx3ur6HZBNlj2vkOeVF%2FA4JE18GJJhgtVHetlpuEqVv93bbBD29XRY6xF33NabfYcFF9f7lC7nJOKJQ0UxEVbsMQLfiSYXxCdmnAMEv5kMAwbU6VlWRhGnDb%2Bb8W3%2FDOWSLm5tFaehIoVBvaaTzUhO4ioCWqF%2FzUtRZXlVrKxCG444aeQu3l%2BJOZuvIK%2Blj5lsTIN4dajxvpS93Sl%2BKX2c7VM%2FUFb0b2oCE2fFgYXRaBzQ5ZoAt8BKSm3oLc%2FC%2BgT9JirLMIkUKLFi9jsHIo8V96582x1oaqM7VkWydP91ZQjuXH2CFnbp%2BPhMEipxK1mZ57gxUNKILGwGoPk23p8FceNP0IAHVm3Dc1NXoCid1Rl3C5EwQWjCol6LLuls%2BGwAFkOigSTqO0UMSsEvBjAKmZRbu5iyaeOCT%2F3iyYapB0UNuR3IWs02c%2BIPDPKHvCMseXTCM74y9BjqkATwqHvptpVfcmgxn7uqt59RVAwHctBodEQwqeSm0r%2BDuwNbAVOeZyhLh2BuK8v1vTVyRMvge%2FhgopxtYpjjtVs%2BRUrq6%2BDnjC%2FvIs2KcWW4oxeMg1Hslkln0%2F8aPC5PZ5u5O5fMqClQg4pSxXSni7TWoPHlY04tKPjt5YIa53SjWTvWpGPrMxeLXjNuNUfXXOwgM4xJGvXztCFqNkvZOk%2F1liIBF&X-Amz-Signature=69664b9e083beb2a1371f38c0f07d4dcc3e140b6169435bfac8ec5aaa4455a3c&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U73BL65Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCID3VlMSSlZkKFwgtAoQbRYzE9dzXbA3qzjJ0LrTGSoTwAiEApx4y%2FrPSG4o9FdkJz0DVlgZNkz7PbF0C3M%2F721jE71Eq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDC5YapYTejPnOjiuiCrcA6BOyGLXgARrExQ%2Fjmfo9Un0Sr%2Bd8kyhkZUt0NSvhhzpD7kR9%2FZ2z%2B6X6rwdTdxBWrfTyGJtU%2FhvUWZH6Ax2d0%2Fz%2F4%2BuQbrS%2FbX1IZEFFn8Av0Rxbk9eEcddh3jIAXBQUDuDO6wa2KYQB51U2zhgdu%2BQJyKzd02GkpV2evBlH40FRjUlZcy5k13PL5YBYTznVe55S%2B1rAM%2FXaRbHy5lnu9UQZQwZXVmJpiBmt2VghQp7rXJfLbtt6mp1NcFcXPF%2Bv3ybmJ8EmqFmj9SblHuW1y%2FaDj93JIszrD39HPDX%2BEXuikaBYe8kCMdLfs8I91pcQNSi%2Fqna3jlyUAnUgOpbvSCBJGOsqS7XZ7not00p3DyG10Y9HK04Pr6e8RF0W5owsln3MkPVjbQoYGsMCdsSlkNcsXTBkQvGQzwOXamO3ptAxobFwDcPC%2BLoBSHuEjrSxsyWlQIL5OeCJciy3x9bqoszKiQq%2B2TxLU3qoHvfnsI1dKaV4e1Iv47kOXsCPrnxO2%2F0wcRVoSslp9i0eR2qm8keMUTGbHJEnvLbAqdBQyAw2YDfCkIJzTWDrfoOezuFWxVfJpSaJz%2FprcilpvKTIwsxdiuXLcl8g96bL1UvgSTS578zat3lWmHH7O0dMIPvjL0GOqUB6lNdD1NrgQRUDtRxVY5rrukytV1vAxwZwH1vA1lB7vf2WW52Siv%2FaZLm%2FfPD5RlErLb%2BhU8rcphqMmD%2FihQRRwycPAVNPNqyDchNt2jkBWJJgPnasYc6VA%2Bv1osO%2B7qhJNBfSZ%2BjtrlRweSU5Gi6SwrMy0noN6bDGaE7w89z9wK1mU3cpH2NwgpZW5EinED089G8jjFh3BQyuwtJRbO5obqGxbij&X-Amz-Signature=3ef0da1fd8d6bc2e127d2bd510efa8bfc664877060c4bcab830d6f444dcecad2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YN7PAS4O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDI%2BmNpdBHEqnW2NW5FXvZ3%2BN9USD6t1SsNQkySqIvMQwIgDwL4GvLZJuSsmdm2oc%2B5D9buXv2SLVsEy67X%2BNPIXekq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLeXtLBooT%2FUb9jbfircA1tvv3yLnDBIrNNkzVfoxb2LG66Cukj9IDz%2FqsyIICruIetQo9KCvD84MoSnZZvmVgGq8MhC2MShs7fq26s15DfBPcc9p0%2BeFvA%2Bux3f17sR7dcrHU%2BJjsyMip7n%2FAUZ6fzFFYubfiC7qopypUSObwZxRZoV4MLuL2sa%2BtI1pCvE029LKCU2udd%2BfZVD5t6kRhoDhnmmi%2F70099kDTqaefAh%2Fmn3vA4cuh1IuE4SpeFeURw8q%2FDW2xxLyWX%2BkEss8uLOQ0DjdGQmmIC8JxPnLoxoIpyVmhD9lvashtHpL%2Fe2bCnGTRWRoXbpbI%2BR7AOGpRatdAZjpYrg3OMBT4RgnHCdCTkje4oKSdzT0KzE4e9ieaeMvaKVnXylC%2Bv%2BrdhmVMNcJxvyGVEjpCO9VHn3621Zu4Bdt%2FfnovMGO35aX%2FcZL67LkFPPGJB%2FOmagsuQ7w7WzEpjcKpEkdyvVyJ%2Fih%2FZzpKyrWv4YMge9y1GXMHXh1W%2BQJf5YhBRE%2B3kMI8vRHFKoQZumBrD%2BBUkhWgjA%2Ftr4RNwG6b8GRyqdQXTwMPH%2BbIVKAxQGgEBoAG0AiZw7Tt%2Fc5cJaFiXy2JN83Cto3FOTrXFDMSjlUP6jLNimhSe3U1OyVqupgKl6pFaKMK7vjL0GOqUBuSoxvyFdUvwz%2BWNmr6gLlwcCsHTDuNstHyNqjxHUWbf4KtcT%2FxOVczhKWOs0qLtxL09E54CFSGX9xmSAOGfxpg2sKvIGmK2oDBx95jt73tNebu3QxP5m%2FZU9ZcVO8E4w%2B8x4tycvHxFGgyRoW8CA0%2BeL4fNgW2chJiJnBYZieJr%2B0Hg%2BALtLTPzrM053I2DfZa8cWEnl9od3it7Bo%2BKPIMEY1RJe&X-Amz-Signature=1b1a56bb4683d773f85a62f0456419abd29f5bb7ac192b73a72e24fad70cd51a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HMEKSIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDZRsBMMSTUeEF2Cmv1JbcoUHsSnfQWICpdF9C35XsscgIgc%2FyJcvoD7yToF07xVBvR7FA1bNqXtVVdgcQY8ohSoSoq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJcIKPLU3ccOITm%2BACrcAy6zxt9GbY2aXwEJ352Ts2jbE8vx94CyMtWC%2BoX%2FN4FD1BhpPGsDhByL51Fdwqc7fI4CH44mvdMbeRZrW%2BY7hVYzDkp0jn8U9lAYEIuMcUJUOjdmzRb5KAXJoUCd17vq8AWK9kFDJjfrJJuy54dTGzYvLYxm4fB1hmSHCGXVPRw0nuPQd3Ckw99O3KDW4XnoA44sETgK7QBwh8gu27Wvks2YjTMycSAMwFXpPIvJ0lFezyxbwzcdrD3AJ2%2Ble6CGX914583GE71hsnDrOYUhuSoG1htcfsdBz%2BdGGTfFmP%2FApvMx%2Fc6So6jvjtZI1u%2BBf08H6C38YjyIT0vwmAh1qESFUQeIIVx0iKG6V3E35wiMv%2Bd526YYMQlF9EFpEKGSh9sxzNW4X7vonaeBx1ojiDGW3%2BAy43Owc1366yeDAP8GGLw7YjWlSPXW56ru%2FbM9JbIKJFSOSFr99Qm%2BlJwSyFe6PhQ%2BUN69BokSLCPqbirz8aEWMaM6D85MsqdXdTQM0rR6uGrVYEyzherCEU%2B9HTk7hVkW39g5LWhEuxWo4MdckP%2FLZSDLoww3Bz%2BHotheq%2BNn0pzSbibjf4wsSyRRwTtWzhBZBqsvQhGWOdcczvDhAgG2dAjkze0JeyCNMNDvjL0GOqUBJYXD43PVhl1QWrRsijuiWiBar1vZGnIPlFparpRa332BRtjt0iQlRHcgnWK1bDeQP8%2FG97kcNNKEEGWyOEBha%2FfB3bhchewuGRUWdyWAy1f8yEauivuESSrfj0LnQP3b4Wj8qldXgkdXlRQWqhP9uXBCR8ocueM15CvEqyGVYZExLvXfdC7rKfLdSiYPMFrSkb%2BdMrfhZhhnHx2KoyOMmQlYNkaA&X-Amz-Signature=cdde5715ccab5ec2f65ddfe0f6eeada5bd4f301779a6ed447cc2d6cddf2558c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HMEKSIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDZRsBMMSTUeEF2Cmv1JbcoUHsSnfQWICpdF9C35XsscgIgc%2FyJcvoD7yToF07xVBvR7FA1bNqXtVVdgcQY8ohSoSoq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJcIKPLU3ccOITm%2BACrcAy6zxt9GbY2aXwEJ352Ts2jbE8vx94CyMtWC%2BoX%2FN4FD1BhpPGsDhByL51Fdwqc7fI4CH44mvdMbeRZrW%2BY7hVYzDkp0jn8U9lAYEIuMcUJUOjdmzRb5KAXJoUCd17vq8AWK9kFDJjfrJJuy54dTGzYvLYxm4fB1hmSHCGXVPRw0nuPQd3Ckw99O3KDW4XnoA44sETgK7QBwh8gu27Wvks2YjTMycSAMwFXpPIvJ0lFezyxbwzcdrD3AJ2%2Ble6CGX914583GE71hsnDrOYUhuSoG1htcfsdBz%2BdGGTfFmP%2FApvMx%2Fc6So6jvjtZI1u%2BBf08H6C38YjyIT0vwmAh1qESFUQeIIVx0iKG6V3E35wiMv%2Bd526YYMQlF9EFpEKGSh9sxzNW4X7vonaeBx1ojiDGW3%2BAy43Owc1366yeDAP8GGLw7YjWlSPXW56ru%2FbM9JbIKJFSOSFr99Qm%2BlJwSyFe6PhQ%2BUN69BokSLCPqbirz8aEWMaM6D85MsqdXdTQM0rR6uGrVYEyzherCEU%2B9HTk7hVkW39g5LWhEuxWo4MdckP%2FLZSDLoww3Bz%2BHotheq%2BNn0pzSbibjf4wsSyRRwTtWzhBZBqsvQhGWOdcczvDhAgG2dAjkze0JeyCNMNDvjL0GOqUBJYXD43PVhl1QWrRsijuiWiBar1vZGnIPlFparpRa332BRtjt0iQlRHcgnWK1bDeQP8%2FG97kcNNKEEGWyOEBha%2FfB3bhchewuGRUWdyWAy1f8yEauivuESSrfj0LnQP3b4Wj8qldXgkdXlRQWqhP9uXBCR8ocueM15CvEqyGVYZExLvXfdC7rKfLdSiYPMFrSkb%2BdMrfhZhhnHx2KoyOMmQlYNkaA&X-Amz-Signature=fe86301b459ac3e7d04c7db30adb8e74fef166cc1e563e70f1a1706490caedec&X-Amz-SignedHeaders=host&x-id=GetObject)
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