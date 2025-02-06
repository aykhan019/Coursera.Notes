

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637GWFCI5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQC8Gjmo6is0G7u7R70IFj6kytlhcTvnR%2BT1P7REzaun%2BQIga02D4ALx6hplysGspdgNmcR33t5ifDAULfu%2BeHlZDOUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDKkRkTSn6gD1Gx5XQyrcA0VCLOXgGdwRauwA1HZZ39gU0knBySqamkB%2B3CDkezyE%2Fn5f7h9%2Fycb3upYws%2BhG6n3h2qEMDXQvofYfP%2FtcfmBQiI4g8xsj0x4Se4nLfvGxy%2FEbuftMmpW5qSBN0rwjsWfbro4gb9%2BhUw1zOJCYQUsw4u04E9QoJhK9lIzf7kbA%2BoNUMAP%2FwChkOc4AvarSw9M%2ByJ2l5gSDeDkTSnDcH8mU38EgGyC7%2FmUTV9J%2B%2FySVQeBkGbpN%2FYWjdh%2BJ5sj4FtYaV264%2BxgTS76c70V8%2Bbp%2FUOud40WgL%2Bq7bq5%2FL3exMKrPmephyWHYBXGjTrcA0I5IJ5Xjb161UIMEw9U8nyBwjRCbBH%2FrZ3jAPO5WIfSI1uElfkik0ANzk5zER%2BnP0kszW6xI4gPYXcYFGzMdLDF7EnuwEiFZC9%2BFFVV4kaL0SPyXOGBTnwHWTR0iJMB4M%2Fq6qXe3pOceAjt4wX63UfyNrlPf0%2FjFmLihPXPKKsiEPiRLNhjLSXI%2FeOOeFaFISuKFqNFkB%2FWMAdk78Ck5CvwqTAVjxsgfJ3fNq2Is%2FuAzDpXg4vNNmrhyTernfgJtvvuYgNgrcvD%2F3JMwq663LMx1UIubhiAa%2BtyMdu3ycXJp8MNZFo6CZ3KBF2IJMOO3lL0GOqUBPvCG%2BY4DcpZpbNep1v%2BjwpO4fn4pGwYBnWx7I0UcEN1MjhicVji65vzGnvYhNpdcLsLu3vH56ivfg4HE1MxoM6Bjp3iHbdi7aiCwuHb24uLlcLYCSXXMvNodUnW83ZMf25AsHs5ZKsj%2FbGcQS46i6HngMahz2%2BogtcL0WcZdoX6%2BHO5Y6tzgCGOcM5IlwzdanOKXr7DHx1UIfEt97Ojqz6Q%2BUM7z&X-Amz-Signature=9457922582787d45e7642b54759ce2dba8d3fdc6c8228fd5e7e9710ead7ab1ec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H4SFDEK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHWZfZW%2BwpEq%2Bp4RZdejwEFi5EeXi9YwVm5Si72dkYrcAiEA8ALhHzApcW88TxoN7M75EpEidkZFxa2Eja0ltRPz4Xgq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDBbeZKtgVSwBiizfKSrcAzeyNsEr697OfH%2BfWPc9PJo4V16E2p2XcFWiUaAt6anGSGqPWteNFLhhbtFOcFWWJ2Nb%2BWZeiphw3XuF4geZfRxVOEsy5YQquqFAbEB0tJXcvOKguKVRoZL%2BhsdrfouYOz2%2FRW4PrURvbypy2TcMHHC%2F9e8rvh0CCNXSMLO1dB3lHuX%2BXFKAYdnJjlDiLPU619JvqVUbNSLMSSFDTXdC%2BXoUykBO6gIXMdff%2BGaxIknKmSxOnecH%2BeFyE5wbQCbJF9SGaxQPOEFc4fse5IBYMbgEccI5CRenRBP3Jm5T%2FdERF25GQJJ2s8CLI6HNUZaUjX%2F7usRlJXatn1MzsV0gXOxylSzHUqg%2BIe4f6eyL0p643gY5iDaBIxidvGlhRUdVbo9PzM20X7nOWtByK4O4TFUeYrmNZIIJ7YgFoQaoYiG0ty0IUblINI4mxP35LSrIb3sE57SSGEAvSkSc2sKCS3yVXMOYoqal9OaZ6ZFNMqeFQLeIbbSfdNDs%2BUTda8gvCJRlnzsEr2ymyJ%2B0jtBgTpAW0f3Cg%2F7stmitHgyD%2B0lLgdzajGoh66nBjh9W8JtA1uCnOx74jylnYN4DcAM0Q%2B5fanMtEsbhrYjJtx3qLFP5O7%2BOzBkiIsE5TIayMPC3lL0GOqUBIiB9mrcJ3wt%2B3EwaBaEGDHSdlRehm1h8UQ2Y6wzqcNssqBg7lDgJToKSDXj6XsWFq8Xq2Xd7r30zEKiGmzhQn2%2F5np67XZ1U3AEYZIcz1vienpLzGsHwfQAEyDiYlskjWoQt7TCh%2FR6mQTGj6uM71TKZXGIfXpCbMQw84f134C6g0zKGTPucV3%2BpWN%2BRx2qP7oqX0FTn3cD7MOJhUdh4n2dHyizB&X-Amz-Signature=5064121ad75ca8509e0523530e622d139bb54094ce4ce5f1bdb40e2d5cf31df6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675JWN5ZJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDaPwemYMG8WBloZeU7V%2FxlHyJohlKQtigYfBK4r1dOnwIhAKNI242Y60Smj0KGwWasBWIVnDvfBBeZnH3SDpOWeNbYKv8DCGYQABoMNjM3NDIzMTgzODA1IgxVWvemJBc2vf4Px20q3AN20jK2SGxZRrL8IKBdDG2xaY9f1j6S1vyjxwD3CwdNDAsjgNvy6S5xXSZoj05bOzEi3iIil9UOAbsG%2BEwgn%2BQ5H7gORigMprZ3w0tIuD13Jw4fxDQMtkd7HAfz%2BHWimVgFoA%2F37lTWns6a0SciobyGqO5oQXxv6HmAEoWxoJIONNACdl91fZ4JyHgvA1Gr1QmO3JeVYC0egbZ0hzcb9IJ0kArBgAu24nWwtziWnN%2F98XiOZ0aC%2BWduLcIFlVLaOdMRGUE5y3Pa5GYovDPo0lw37VWLXSRYmbyM5bdGmLeXlmkQDKpkiXvqmfv2t%2FFGupuZNRuWHtcc0%2B%2FQrylQaiQTr9KVw%2B5rg5aK%2FzEL60QHBawG50Q4tkEVr8r%2BHlAgcBkNJcs%2BBHjdNPV3N8l8giYOcEbIHbBbdSSrN4AAEo96r44CPjFi%2BAwIhNn3PdRIZHImO0pjkLMXTsyop%2FyM1uL3esrEIuOjvCB1Spr63a7Xy%2BkjEP%2F2dTyi3R6HWwmfRVzkKybCz%2BP9BDoVpSBTQHHGmrMmma2oJocg0SGIbi9tLmpFB6bz81UlVezp9%2F4j%2BNLN%2Bdo8L6RXfXAhMxh8bd2dvYONlY%2Fy%2B2A81rcu3YJJFaCzkZCEL%2FXO6ppD%2BzDFuJS9BjqkAVQGwxeeJmiWmOl4Jyegwz1T%2B78opx4zNDOPBLM2JwHMrsDvQzaxUOStUp7Eo3v6%2FRjCkvrvBsZD6YnrE10nRYl0AQfWCDLA7FjGa8siZac3w3sKQ91TQg%2BLHiOMzeX5FDGIM6haPExoH6gSEY7LDSTOw4lfBKoJIZyX8Aa3Qrhbk1PZXtVJATiuuTKa8j%2BdevPMHVPORqkjHeFYJ1RONm%2Bn%2FM7m&X-Amz-Signature=35f28ab845db18453af5dc1e064f068fc3005dff8d1b362a7ae1fc375c7403d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2SFSUL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCcA3LxkMkwVrnMlu9%2FkIM9n%2Btb%2BIHfZo9gGNTSxxXJDwIgeIBuTxGd98uFVK%2BPVL5S4z4t7Iiir3ZakVhtlzazu2Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCmf0biFgGpve4l9rCrcA%2FLZqNSZKwalvcH03BuRbbzqLhwZ5qlJ68DWoxBPK2RBzpMWcxqFqAy%2FFHbMXMriQnKorr20ac3vO%2FN4dUQ0c9EioxIMZIIgL20bidH9oZh2osg66qI%2BgcMZXX9fMxz32m7AFw6TWD96RDCnxKOSN9i5%2BJqmxwGhZ0qiQob%2Bldj0sQ1IaPFR4DpyK%2FH%2B1MSY3Gnc3lBPp9U0pwLlU55VRhjySPiAJT0l5UfBiA%2B07EiTclLYxmiBaEiSt9gYP%2FBG%2FMNrYbjRcsChybckdEwHfwq8Wd%2BlWQKskQ4BKJPhKVHkaHSch1GeyZSb8%2F4S%2FXAZ%2FC7%2FWMfcrrhAjY86rOuX%2FIYIsHKEsitxMRgHxE37HSrFUodQ8ahzIdhJP0k1gl0sAaO0SHXQcJX1xgxpTADmhhFCoo2AkuBm8dyfF1A8ok%2Bpxogl9SoDRo7cJhH35ZiXumglqrGlP%2B5OeW0%2Fdj2pA%2BuXjfuUNyb%2F8rAl5wlcX6AgTlm5Aag2KEcMJAWX%2BIQ8jMrWRrREtIyXch8Nh7h7YmR2Gd3TYThmZceUTvQAjlPt50GdRpdeofGmw0a%2BJCcbh1r18rw5rYeJjFjDXRys1neAogZMIpjX8gOtKv6bkAqJTtOPbUsCnw1xpB5tMM23lL0GOqUBDfDQuJGh0TntYDpl6FoPR6JRpqtfAP1frV9gGF02CzEDQ4JBmkLWxGnBzK%2Bu4caOcV%2BlWnCCqZPqz1Q1%2Fomyyz8Tbs0SB%2F84BwQWU334KKVeUJo5%2BpR22SM%2BKBVgZ8yTMvhP3uCGTir6tRPjxSE5laxBLzBLk%2BnFN1enwmI5RUUOPhqPtyAWAl8W%2ByOHr6GjiyqkuqcjKzziqNKtcZ4v2ceh3rtq&X-Amz-Signature=4718aab02df3d2b1af6618410b47d45b51f822b60d210263eacff0f0d3a4ceba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQWKISML%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCID1YLQiZxpp5ywUrCSSRFfTlN11BzO%2BhwkpagwbAHfp%2FAiEA8G05SrhqbL%2BwdoRCoIVwGoDGCHty86aYTMexn%2FPV35Aq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDEVG8uDWogW88p52eircAzRG7SaKYKf%2FOvvjD50CxlFK2N2CD1qSSm6U3Em%2FBOZEgE4kBuCsuwcGnG604KSnduqYZHyQLv0Uc%2BaU%2Bs4gkTAb9OTPJtlFewbe2YWumyYaAgJLMH%2Bg37yJgU8D67En0456aM8uVrADYtY7FHePV%2BDzwGOQgwCM3eVek8M27j6MC%2BgvbpwWqYVCrzhkRCVI42tU9bWk9i19Ra3%2BHg%2F%2Frf3405%2BdqR%2FjhEkrYlUFOJoM6edYcyEuKrh7T2xsnc3%2FaM6GljgsuJSwjHsR2aIBryV9tYum6vJHXNfN1DoZzrvMtTzoZ9yak213b5J%2F7%2BC04kfbePGtbzW7obob32Wq6C4xL07ReiNE6iVyvZnXxkRelgiCGvK7tb%2ByR4tyTwlnwpg2%2FsM7abk7Gu2qrDXz%2Fsn0Ztjj5Ke%2BVK4Ec4TWNsWK5pofjqJvgGW663faXfadpboZrKk8qcIZ3WeutBQx2A0e6qOWeDPbZQuyz1%2BOUazj946ZMNdAs66cX3hzH2F8B1EkhW3levUWaq%2BrNQaZlJAhstA92f1%2FgtSVIpSH09%2F0Ay6YJsmgJbRXAE8jcIHvv3nD1wh92kqmpxlXfIaJ5ASjrAzYkiVu%2BAErrxXH%2BaoUHuMuMqCV5o67CXPeMLK4lL0GOqUBlqBBfRQ2GoeE57XTrsowqYsrq7Jdgp9ys67Y9PzhPdvxQCWJV2YtsA4FwNexL5QyfSXvIrK8mnEiLgDg6t8QOStAvekywDnASUeabgMMmj2AN7hrBmI0ndUo9ZMlzDzlUtBWaedkHdGadm1u32jabcL48HGFkK%2FHBkt%2F8MR8jAo%2F93kwtWhrRaiKMMctQQfmV%2B%2FBRr7hk6rfeC1BNgGlDZ15r%2FjS&X-Amz-Signature=5e9ff17fabe0cc88457846c998cc0bc104a253acc9c5941cbfb7aa2d06a20ee6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IRMT6K4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDE8Aki7QkicijQ%2FiQus6ItD%2BdUc46aG%2FkPWQOcT1560QIhAIQa7kUpkxUnxcBDLSdc5hsh0a8%2BHbbkXW4M29CXvrYiKv8DCGYQABoMNjM3NDIzMTgzODA1IgxIlnn%2Bio2WN%2FxBLgkq3AOEXHy7seMWAItXY%2F6gvDJR99Br5EXNnH8XPfXpxJmq8gm1IXDcGhJ21CczPUlnGZzgfgVHijtz3eWm%2Fec%2BmOpOsv%2FR1ocf0E8Uj%2BPHIkz%2B22VT8ccmKZZTHBFi34oqX6MC4mVv5%2F%2BG077nq%2B5RSezfJTVXtv8CB%2BzxDRoYSQ%2F9U2pe8dS74hSPWfrLm9iXxqDfwjBaNcQAZ6pkpzLmETOumRLCpWMhA%2Bqtsmjsewllzid93JWqXLQz1okA93vk2WTUhJ92%2BX7xj9WStLmJIGx00DincAGtmWo7%2FRd6tlOsfTg9nv%2BiRmvo5ecS12MbWiDBmwywRa02C5P%2BF%2FkDbcbCxWie9CBYQRgWEt5dqyzBU%2BOvTCMCTgFYhN8TRLZsTtYpcKQjH4nCu1cetcCfE14Uxfm3Vuorx%2FyHiYVGYeFEBmlQut3AIkYXgBwJH27Nk89NVL1jIyC5fcRx6pn1hLByKexGlJ18MJthIMDyUsg5VkbOOOVM7xoZHR3miucPhO3wjdM6UtUbVhUrz9GxXa04di2gLuHmgAOsBhENXOpV0EKINi2pw1vh8belJK5g19bqatq507MI23gMnbecFlZijun72JVmwyOYmrc9nuccnmA3zfpu2hNtouhpgDDtt5S9BjqkAUUI3%2Fg3YrlDfS7CpcQsrMgtZ8vGOKF8YzHsmsoay3hHXMqKuWXQAbJv9Vaz0448iziSHY7sUgtk6uNKL2mSNCqSxdw7ecbEMJhUPYbAgqEFg4uVPAvw4fP20d2y5s4SDSrC%2FHmoz9RmtWsNa%2BSVgSmEc4ArSofSrUBjzUUxtyV4h1fotQUJfLIWCy2I%2BhBvVlac6Bnil3lKg6WyIdsB5s0t03ez&X-Amz-Signature=cba8e3a0fde9a36f27ad5b569dba2717e5b69dcd87dce32eb5937898fef3666d&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBLQWCH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCS4TukU36HF2J%2FiogYqlpO2HXvzoMOT6DwMl1EWv85cQIgQTp0MxF8rF8Q8GFc3nFCJzaddwsqRgT4E1IBdT9GHNkq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDOMo0lidzTwrQfIGPSrcAyqApikVxGCdLt%2BfjtIHybaFXA9Wv05P%2B3NpyN7WPCYIbRvIf64RgCEHZ8AjE6mW6canZ%2BtU1yUUsAN%2FtZn5Photbhkb1tJ1PSf%2FzV3u9CWdPB88%2Btt2Co0GphFahZStxZcwuijiMtCmbxArC%2BHM6KfX08VYcPLSqOqXESj%2B97BhKp98Rri%2F3c%2FddMgQ9v62QLHy8qoSYVQw7ep74J4lSLiQwBzUwVGUfKTZ9bK%2BUq5G6yyqb4sK1jmbIizTKlU7VEX8hrKMv4XMbhSXTpnG9xFsuUXPSS6901BteoUH6%2Fhz9Oos6Aaj0NQ9QEhyXsNglfYuKzGeHKNn3XVZbSiFbMMmwNCyHenjrh7hxQDMyP4gyzUFhFFkT%2BWP%2FrAnxuVRVssGsT%2F%2FPRrkJsSaOtImTmLVKs6kfiEQU3A3010wWZV%2BCTl6tkufS%2BEzYqWDItcKzbRe48HhhvJA%2BOqh1XDoMNcC6Lhp2ZXUsIDyqHh%2FZdgrBSL%2BrUlAKAGOLcab1Q27iqZej0azu4WeubWhu2b%2BFTv3blqaKPe1Rn8Zmjp1VnjDBYA8j1WBnQwST0AEMBFd7g9fqlcm7n%2F9%2F5Hin2Z44ef%2BGgkfYOBSPWMyeBP8z4NQqvJ%2FuwlakmURH2pHMO63lL0GOqUBPdYA6HBVGagNoLwwU%2B3iqKLn5gvRv2mdY6Mg8Qx1pyERYwh%2BOPp0O%2BVrJyVjAh54Qh8icwWO9X51T3AbGIfDIGOYNVqT4lmMcD2E0K83P%2Fn%2BfJoIA3X2eA%2BtkdkngpSwc79Rsm%2FaFowNY%2FrNxNYRCYWhOVKSurdOwZByyI3soU2p1EAKbyMqnCTGXD5V423UKyke7EFrDmpQNDzpH02QMF1QNK7c&X-Amz-Signature=285bdde19d147f9dbc3905622baf5cb131d9dbc6765a608afa1b4c4515aa4662&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7EE3KY5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCxHQohqG7ZT5OX54cFdBkYdX2gfnLCEXzFqjkaK5aqyAIgHpSxIxI7HIsPxh48PHkgKOdcM5olO7ptBNq4X05BxUkq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAnL4HJYnvorm1%2BweircAzfJtjJRCkU%2BV3%2BpvYo9RKLCEF6PWzLrCwYAkzBKHE5bQ%2FR6GMnQ9Oxwgp8rS11Aj54ibqTP4mBeOOOXEe8R9t%2FnaeHMbluS%2B2KcpkGBlRqrGhKVgrdS2xTtbZD66J87bg8Yg0CwLOJVvwyBlI4Yp6fCFpgZ8BQI3Ey%2B2z9X0xubYixUr8nXf9pzTZ6Wqeu3f%2F3VnxNBMlyC5vIdHDTrn8QoL3lfuiOwj5TnxbMJ%2F3oajMYvk9AHWtLbi3I7mLZn%2Fq2Oy7Fopzr2N3ZbKf8W6NXSGXxaaoYL8oqXo3NmKjB6JXzfsU%2FNoU57hakK72m9bUO7VTBKaaqZxiP6PiIXu%2BRgSbk5GkR95SDHs5G8KzahHL1EPb5NqZbLOGqBeJLGeuHxh%2BuYNfH3L3yGZALR0RSKr8ENv9vcCMMKGUMaWLwDbwgz4K9Zo95sjnqLYufG7MQAzZKqm6i%2BOt8zuhKt89kcYihu5ty%2F78LeOdG1fAVfcLAl8GHIe2nGnlanWuskLToeEZZN5tI%2FiXoQBwxet%2BLdWvi7NrOzhT1R1uie7gE8BHbph20S8Hlc%2Bx68oKl9YoCaFRPbjQVlOV%2BmwLqzNHpJxqBvVB5r0RP5Z5pmQ1E6EYRa77Jd3N%2FXphwJMOa4lL0GOqUBCSBCSM4QEro6B6672gkLJTZsjjI4x18c0%2FCsjs9%2Bg%2FwS%2BcFEqgYd3dnr9Ektpgadoq%2BdyPIW6Q8oAasmYqYETPavtrqVuriKjevDIwxTdEiHhXwXVFnpQ9Ma%2FTP5YZm3QBzbBFvXtPtU%2FcrUqf%2BuZ6vxbcz4kk6ZzuPj2qyev33ZtK9UZ7DivH2p8%2F%2BgWzCzxnq5%2F23ZoP4U2YUtmoW7mEPiH9eY&X-Amz-Signature=045e2050228ecbe570890ebff3dc3d78ae4bd025484a5b2f45cda485ad3f51d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQWKISML%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCID1YLQiZxpp5ywUrCSSRFfTlN11BzO%2BhwkpagwbAHfp%2FAiEA8G05SrhqbL%2BwdoRCoIVwGoDGCHty86aYTMexn%2FPV35Aq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDEVG8uDWogW88p52eircAzRG7SaKYKf%2FOvvjD50CxlFK2N2CD1qSSm6U3Em%2FBOZEgE4kBuCsuwcGnG604KSnduqYZHyQLv0Uc%2BaU%2Bs4gkTAb9OTPJtlFewbe2YWumyYaAgJLMH%2Bg37yJgU8D67En0456aM8uVrADYtY7FHePV%2BDzwGOQgwCM3eVek8M27j6MC%2BgvbpwWqYVCrzhkRCVI42tU9bWk9i19Ra3%2BHg%2F%2Frf3405%2BdqR%2FjhEkrYlUFOJoM6edYcyEuKrh7T2xsnc3%2FaM6GljgsuJSwjHsR2aIBryV9tYum6vJHXNfN1DoZzrvMtTzoZ9yak213b5J%2F7%2BC04kfbePGtbzW7obob32Wq6C4xL07ReiNE6iVyvZnXxkRelgiCGvK7tb%2ByR4tyTwlnwpg2%2FsM7abk7Gu2qrDXz%2Fsn0Ztjj5Ke%2BVK4Ec4TWNsWK5pofjqJvgGW663faXfadpboZrKk8qcIZ3WeutBQx2A0e6qOWeDPbZQuyz1%2BOUazj946ZMNdAs66cX3hzH2F8B1EkhW3levUWaq%2BrNQaZlJAhstA92f1%2FgtSVIpSH09%2F0Ay6YJsmgJbRXAE8jcIHvv3nD1wh92kqmpxlXfIaJ5ASjrAzYkiVu%2BAErrxXH%2BaoUHuMuMqCV5o67CXPeMLK4lL0GOqUBlqBBfRQ2GoeE57XTrsowqYsrq7Jdgp9ys67Y9PzhPdvxQCWJV2YtsA4FwNexL5QyfSXvIrK8mnEiLgDg6t8QOStAvekywDnASUeabgMMmj2AN7hrBmI0ndUo9ZMlzDzlUtBWaedkHdGadm1u32jabcL48HGFkK%2FHBkt%2F8MR8jAo%2F93kwtWhrRaiKMMctQQfmV%2B%2FBRr7hk6rfeC1BNgGlDZ15r%2FjS&X-Amz-Signature=aa3ff1745cd8160d751bc87657d2a5a051fd5df6aa5106bed0cc0f79cf141701&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTU6YWZG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDbA%2FsGm3TUlC%2BGAZiH1bPpXT%2B47B6Uy4pE1KBxscordAIhAPeDvsbmeoDcNPAMemth2DLIojk7KotFDqmZ%2BpRPsqB9Kv8DCGYQABoMNjM3NDIzMTgzODA1IgyTbeNNXqBSY0KMr4Iq3AMZWK2hcXCshkfTdVduDhBz9lfDmyqD7zWa50RNGSF21vM3Dx9CEd4N22g2xoJMG1EiDwRK13YrCuKwmjxifxKmx9cLq8zYZl5aL3HMiYADUbjwosl8mmHraG7WlSpJ8NohVlz2ox7eoMyQWqrV7u5RtIteiiSwTkC3lJhXPDyBI183paggTbARw2sRTQLqB3%2BuucgB%2FOseiFkPKJeppU4%2FCmrOFY2RqahMujAJ0sL8w%2BU1MVlW1pOOTxH7kQJ90DHAls4OBpDOb36PrCxA5fIC943Hu%2BrWf09qjMtU7KGTIkWdnud8vcMyCJscCn%2Bot0M7CbtcEvay3Br9ENLWtxlclfoA0A1mbAG%2FfZb4JPr0G5Z%2BaDT5u69G456gxWvv8G05HXhlOHmwAN%2F33tx3RnQ3IPBspzxEVIdn9TDD4JV81N%2B1%2FV7zAmjw4%2BbFrwA6oX2f%2FIgANXiPuwzweeIP62EVawYyCi7f2z9A5dLHp92pfLvyxha8Jmllf3a8%2FtL%2B0z%2BvmZkhUGHIUTsyLLrrTxeLbX0%2FLsZW5C3PdCDnxbbZZYHu4Oafak41hx9U1LP22FpbMnmtnwT%2Fz8DaRiXyL90d9LWtR58ThgSsFplnzMkNLww8FqtzemrnIG3grDCXuJS9BjqkAZIZNS9mloc40bQt7VA7wOiXKeJOCodyfe8mk956Gh%2BGQBU62bWJpWvzIsF1FGjMS48LKycwngr5fl1PNzPhfMHEGvynR1eThxXjh%2Ft3GMZuiatcVbPR%2Bogv2Oo2Kg0cqkoKEiu2jxPgfhQ8c2xXGYpYWrUpTLw6gnKy4Q3c4g%2BgwE5LgN8jnewIt8pPQIucmalKuPaTqNOZm0v6YznznLidHQ2h&X-Amz-Signature=5f043ac9892821a02a9345224fe9e813fecc3d2623c64ee3cbcbadc0422592ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTU6YWZG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDbA%2FsGm3TUlC%2BGAZiH1bPpXT%2B47B6Uy4pE1KBxscordAIhAPeDvsbmeoDcNPAMemth2DLIojk7KotFDqmZ%2BpRPsqB9Kv8DCGYQABoMNjM3NDIzMTgzODA1IgyTbeNNXqBSY0KMr4Iq3AMZWK2hcXCshkfTdVduDhBz9lfDmyqD7zWa50RNGSF21vM3Dx9CEd4N22g2xoJMG1EiDwRK13YrCuKwmjxifxKmx9cLq8zYZl5aL3HMiYADUbjwosl8mmHraG7WlSpJ8NohVlz2ox7eoMyQWqrV7u5RtIteiiSwTkC3lJhXPDyBI183paggTbARw2sRTQLqB3%2BuucgB%2FOseiFkPKJeppU4%2FCmrOFY2RqahMujAJ0sL8w%2BU1MVlW1pOOTxH7kQJ90DHAls4OBpDOb36PrCxA5fIC943Hu%2BrWf09qjMtU7KGTIkWdnud8vcMyCJscCn%2Bot0M7CbtcEvay3Br9ENLWtxlclfoA0A1mbAG%2FfZb4JPr0G5Z%2BaDT5u69G456gxWvv8G05HXhlOHmwAN%2F33tx3RnQ3IPBspzxEVIdn9TDD4JV81N%2B1%2FV7zAmjw4%2BbFrwA6oX2f%2FIgANXiPuwzweeIP62EVawYyCi7f2z9A5dLHp92pfLvyxha8Jmllf3a8%2FtL%2B0z%2BvmZkhUGHIUTsyLLrrTxeLbX0%2FLsZW5C3PdCDnxbbZZYHu4Oafak41hx9U1LP22FpbMnmtnwT%2Fz8DaRiXyL90d9LWtR58ThgSsFplnzMkNLww8FqtzemrnIG3grDCXuJS9BjqkAZIZNS9mloc40bQt7VA7wOiXKeJOCodyfe8mk956Gh%2BGQBU62bWJpWvzIsF1FGjMS48LKycwngr5fl1PNzPhfMHEGvynR1eThxXjh%2Ft3GMZuiatcVbPR%2Bogv2Oo2Kg0cqkoKEiu2jxPgfhQ8c2xXGYpYWrUpTLw6gnKy4Q3c4g%2BgwE5LgN8jnewIt8pPQIucmalKuPaTqNOZm0v6YznznLidHQ2h&X-Amz-Signature=8f79e580b1792e52dd2cee5596ecc9076e41efc76fcf808bb2345c864bb60072&X-Amz-SignedHeaders=host&x-id=GetObject)
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