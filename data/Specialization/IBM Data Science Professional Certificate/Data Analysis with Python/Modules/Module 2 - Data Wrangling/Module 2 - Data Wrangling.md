

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52ba3383-bb5a-48e0-8404-2b9dadcf9392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CTHMAJS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICb7%2FLfwxoZumgQyuVrHpYd39RZNZi8FyInr%2BI8l%2Bp93AiBKZJcGD5zc0RtX29xTLOK3aKtXcAP3kCwf%2B%2FGkdCmswCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDonsyXFczUwsKjp4KtwDcuM2mKmDkqV%2F%2BMBG78usU5VcPjrG6fxPsfhlgM%2FjSce2MZT2td84TCEleW4i7nNE9qUf6uheARhMAwAE%2BgpoJkfJ4xOrjKN3%2FTYnEvr%2BqSlk%2Fi9xzGv%2BvisGnrCNGFzaD6uoeTWaV0A%2FlWsGUseCDPMYas3MAmGcWTFb8%2B3MdGlkX8LKHwFzyPlejDJz12x5U6Ojvlb65pzJ7QC%2BiIsEwbStAfepJPtWpEBWPDfRivf7RorRG3cuvlNNTMS5d9BVmM4VKOmMZxQp3TF%2F1Z6CCJObTRPHcE8qsFBkaqAy20jSzT0FVfI7l9roJwDdmqi2d7ILSbPcEjfmXFaQyasq4qYCFKIjJPUSJ6EDgfq%2FYDCLq%2BldCSD3RIv2o0CgHKbFclP3vI06eDpfeHIZCnocNOBbUABm%2Fj7mD0ou4RO8dtLNJM6hkqzxxePLZIGl1KTr1KUkvlqYOHyDbDV89UBcL%2FdQVdPGc2sojvc1Gsr5LUdBpICB9CcnAFKhM8xTceYEn33v52v0eAPpLI%2BkglOQQlw0Hvh8nYscXalEEnVHcFMSBCcN0EcRlaFvWn2PMORRJo71IpEV6qRgPQf6ZXWFqo6I%2FGReUCdgeFtpyMmxhj%2BZypj8f1ihXAO4G1Yw2qjtvAY6pgHcEtR6cUCpbjF4FrdNnsPxKFK9YVc4mXyxXvGFjE6AlOBax4lxhh%2BIQYxpmHqhoHZLt8Wk%2FDeF7SwugVERPDdSzhUs%2BxWkFlkj9NK6ybGFNoQPbiyp9bAbEqIWNrUxu24mCyFVN%2BZdMhRzk%2FPavB1M9fZMIHmt%2BAY1eGKISgYBx43wC8vMWYFetXntKY05Bc1X2vX5cMA8pZRZAAtj44j2rDui0EED&X-Amz-Signature=40f322a3132b90661be42c259df09633daa6adc3322bfef2f9df40a531cd8089&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Strategies to Handle Missing Values
1. **Recollection**:
	- Check if the original data collectors can provide the missing values.
2. **Removing Data**:
	- **Dropping Entries**: Remove the entire row or column with missing values.
		- Suitable when only a few observations have missing values.
		- Example: If the `price` column has missing values and it's the target variable, drop the rows with missing prices.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/08d6fa26-a234-4a16-b8d4-c6d7102d2a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XF4744VU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHyDH7UnZe7UNLC5c6eo6Yc%2BanGUKboAaDqlH2pyRTLGAiEApYjuI4QtWvkuGuGlENvc361TbEEfpBr8HffnbMwyAVMqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF5Zk3wwZZbBMUVm9ircA5WpCJhDEkN8V3VLwNtBwNmk2nGPQc9HjtZBzK5WUuGANTVoYhJw388W%2BY9nDxS9%2BEFkDtUYdteQdQ7TIejVBw7E4mRAlXG%2FPlgJGtopo1alb9WOWAtMwb7vi%2FKx%2FREavsk3deyGjqIJ5bvJGYEeoEi%2BPptbrMmmt813AFzLICkHA%2F7Rrp2yxly%2BGYr99rHbPJSpQtPfXzbw%2BW66dTopZkCugtZ9%2FyQ9DPYTD%2Fu0sUcSRRvhbuQOx2u2aICQav%2FOuvZU0vf3gW6ymqlkctRNnkhqNDETM%2B6UDF%2Fp265x%2BPdXj49iuwukkqQp2xkFGfPKrg%2F7CJ%2Bjc7h46%2FCJPhzdyoQOmac1vTcTQ1d%2FcvGIWe5SDDg5q5SLuT6KblZV6dpL5HWz9y4iQ6iEirlhXcSJaJdFpznJooaBD09FZHASXbaGc%2FjpLyD91IYhNr%2FeaS6HIeGt%2FfLNiJBvk%2BzCCHXsSVQ4WUeuTokPfpJseXFgIyJWh02h5GQ58VTU0SqbzOtVlOCw250IHfhtvFKUnpcSkDZtJKpqSP6vuag8bKTmgx0%2B2Mlw7j8zYqTlqii94L9KGZhgwWIgsBO%2F3%2Bdzj6eu7JICnydOzR5T6YtWBC5R7FZLAV0nKP7lqPbH%2Bm71MPmn7bwGOqUBbJ%2BmRK%2BjR6eSAk%2BdJbWNMeePkeIAITQ%2BZpQirlmfdEI3xI9PJTbv3vrECH9V6flqoFlB6m7spSM1%2FosBzbCibBigC87yQGL9lKSwMbeTVIzn%2F4Xja%2Bktbe8TguMMZCtglvDqGE4ELb0%2FIR06aPfJUJIe22LMM4tgSMt4Eh7pY4uByFlthi3a97fyeNLfyZQlcjzRt2t5G4lKMUq9RsADLPrhTfP2&X-Amz-Signature=19d193a4667add7effb2e4c0492e6e86db9731be632c64f24ac1ab493d19f7e1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **Pandas Method**:
```python
df.dropna(axis=0, inplace=True)  # Drop rows with missing values
df.dropna(axis=1, inplace=True)  # Drop columns with missing values
```
3. **Replacing Data**:
	- **Mean/Median/Mode**:
		- Replace missing values with the mean (for numerical data), median, or mode (for categorical data).
		- Example: Replace missing `normalized losses` with the mean of the column.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4791630-48b4-4a44-ba8b-95b0c1d6759b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L5MQVHG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQrbLU0ZTQr%2FKSXQP5M2GujsIunsG2NwalbArkmj%2BxdAiB0jTawRj%2Bv8p9ooIQCgWkTWNSuM%2BnvgaukEb2Qdlv9tyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu24lforzqu9SkjHKtwD19TVnB4etFssj0n%2BMYZ1OtBvkOEz3AG26tO%2ByXHqx4d2J5%2B8cU3lAew40YkROX9W8BX8kfF7Ok8lQ36Qukjc6ZMxJcHSuO3NsvjWLk4zEUBH%2FZfy3u%2FwdQpg8IXmGqTRhm7oydCrDt%2FHZdaabm5vAvZP6Hex6ch53TrWL7kPCxM9LZPuzhyABrLL8Z9K1UUwwhZ6f8jCDorrnIYOrvxCOeixJ13RasJQoIyHk40OTj2oclu6IkJt5eesBr6w%2FEx3a82epnfZHnZ%2FaSkh%2FomByqCCEEeMW8soLRvAOKENbHCRGjOz4HXijRpHZ7SR6UDguAXjdTR6Kaw1n0ZAVXVvdDYcHAq%2BTG1%2BOOwD%2BK3AF%2BL5W3qpjzzHrMsKjQo%2Brhix6PlyKxer9ihodhFWqfRGKme70OduxS7Pf3YpBTZem6048ebb%2FoSXWJACgFdKzRIRHhzeHVfqPqyLpWl9zIPfhkZXOM9xanQU5sDgsg1zS2g4Cmw0Fyfamxo%2FzvZ5vCTvIWVIQhtbX1rqt5udigivcsCqyujKmkZ1F116AMjd7k9w%2BV8NiEvOn4UhruC6fBHH%2BEJMILuZ8ocYuE0eEfD4XjLKcXb8SCRVFuY1U3PtqnLPqUpD1pyP6q3YzxEw5qjtvAY6pgHQRAnBbS94WyGWTzrUMn%2FnJU35TpNKtvq1R3XoI5EcVnQ7cdBwEwoi4yhOdAx6R6M3%2FnNy7nORGjdowyyB5F6DeBUId%2Fr5WrzUicYqIO8OX3YEsYU4wfwU9DX%2FBMglCiOI1%2BqvyjjT7a%2BN%2F0SJOeOPda7M5kvJIB3F0N55TW3Z9VPgoGgO1gTVsVs8TJEo9n6JDz%2BB6txV1m6uEGjtdqQzhqQOjlm7&X-Amz-Signature=522d194bdc7c37f5ce045b38dc72f7f780a2acf71e851401fec8ae272a94ff25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1af152b-1030-49c0-b8ce-858e515dacbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPFOOECP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRjrrS%2Br2IAbDAsGs3pvV2P6ZbytHJ%2FOq9q05JFSsfMwIhAJlhPadNXL8bXBM9%2FaNvNSkGpbTxBbrm2T%2BL%2BnuUz%2FNRKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzt0pzGXcxN71MAhEq3APCubiuUIjxjnVDkjgTrqiF3H6lEZT1o43RaHzk5rBQ1%2BpQ33N%2F3zEAGeZyde0tTkumnS90JyzGfottsH8UfZm4uVNp1P5yqGru1rR0xU3Knkf70NO04naFWFh8YvPtl7DJ5E9e6Baof6%2FVQGJ%2BocxSsr4YLeMvxiGcjxVL2Y97qfuhLAEs6QzTh2o0YzGnCeU1jiLli6c5E6opNH7dO7ev8%2Bq4JHRAQO3ds0l1emuWkeBHKURwWMaZzAA8uJU%2F4l%2BwyYy9nb7NCUSp29Yd7WUtm%2F8BTuf2Rp3EQERK%2F%2F0HCkmX46AiMEglhLOhznlmTKFZ936k%2BKnopN%2BChFYoHhrvc38VFMqaV16tWX8JRRSBVUYCcrFifknl9Go%2BxCwyDLxK4q4lgYWxIhXa8%2FEwOP5OJg7ghc89d1Zifu3VvE77v7jyBSwcXBDoQPmdOPerrsKKRd8P5e%2BFsaclWxc1dtByj97ICZERdA5mNFZeYikoOIA0ShFF7FHZDmBO9BtshSLn16UJr94nNNQo2O6XbTVwHJhDlE%2BcIKLn8dsbOWAHmKxbfcsn7OszrubQ87yTjoTqFJebEv0j5S5wi7ImuqOlUuMckOgN%2FWfxRkzcVTKMjmrhrciP%2FnKJdNKzVDDbqO28BjqkAb2WBycHDrg2tiZMExim94yxUhitjnBDpDJDSzPfHgWWW0T0MVbDZzakfXn9Xfulr%2FqFBK2zoIgqngcp2XiuD3rXdiKpGXvY6AMrRD4HnO0j%2Fi6ox%2FNW8dY62E%2B1mlWoWJJevTi78EOsjISnn6gAHvpy4Gaz%2FgetnkR654pnr2NJo3MdhG2eAPFq3XOlrjao91A%2BoxfBVZNMsA7MC7RFZntq%2B7Fc&X-Amz-Signature=f652ec36329316e5cf67c67b6681b88f52f9bbcb98bb1c762b74b8df1237ff17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/da5c198c-c176-40b5-98f6-10f801ec4bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOT27M45%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYN683a3DSJI8Vq0j7MGSEDRz2KTCPIEumvlNBT7eGAQIgbsHndkjQi%2BK8sKfTO7qveAHrc5wBcCyWguy6F%2Fh%2BSoYqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9O0qtNZYIKkPUPhyrcA4wWfw0%2Fn855fHqPvbF%2FclJyqhvXvF91T49NJo8XKIlIBzzByInAwr5DB3e1vPMeq7s6%2Fjt%2B4luaeYG9bdRpDZSVN%2BrRfwBFiCVCo8l%2FNbSXs3RVie8J0f3th%2BBmOmYprvjt2w369imgbouWwroRDQMXYc3b8e77TMepiWAueye4Uk8EYs0c2UpjIHQHH9cZKxO8DgzaxSeYoQi%2FJald0Vm1wbqMYNY1hiu3bDXV7DiEG0ZtHxE%2BcGjXuIOPaG8qsTr2jrexL2djI6Forvd32%2F3b2MDH%2BMf5nvqbO0ky4m64OHYiZzBHLS89qir2a6cAQDpRk3kmOTSzOUE3O3NCxVGZ2xZiRTzmgZ%2BjxaUhjWL2joWDZgSol2dipgo0UZTwN3tmJ6l%2FMiyyBdUTSurErgVx9LrR6ZPrdzY%2BQbtAqLpzTNcO7ozQMExE5hyG5d3zuM%2BPa6jv5LC0FfsNtOAHAwtB81IsudbfXubV3qZwaHpVWG8FoKhN3kymNKX9vhAsLONdazGaKvc0rrPCMGhcnEvgQLBEP7urall8r6KPCMMxxSU0NVUz6xFW4ar6qOy7eFh1LPELuRS%2FwGnAc%2FJddTAawHOsmfITTNQWck1nHuxO0zb5qLf6zdZnqrAlMMmo7bwGOqUBtWJIOc%2F6NgtCOU%2FvZp8i5YuGRHtSaE61z91biFnFMAa5CztJ%2F33IvnJOp4w3%2FkA0enq9zFKKvsS3v0y1mH3eZF%2F7TEacjVV26NaK%2FdkhvsjcsAmGyxUt3sFQeZ3bxBUeU9oSRhaGoAmrzCTRdkXmS23pxe9ST58RqtlsA%2BoAsSav3VV6XCQmj6xe%2Fb5uYGPdsyM%2BSpvalV6iaqQHFwcBd6qtWt6O&X-Amz-Signature=a16726597a8eba445d09c73dcc78516725313341eb5f61274a83db6454cd31bc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Methods of Normalization
16. **Simple Feature Scaling**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old}}{x_{max}}  $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = df['length'] / df['length'].max()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/011e19cf-0bb6-4853-bf97-527c877b7913/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SESDHASQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9dcYGNgr0vPHAXn2J4LoDBuSBlGs0YyvPUNTsj0dxRgIgHXQ%2B1IO3c74W8g6YvZRwbvoq3YrbTzixllzAUCWhMjAqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJAIMhILGs%2FHNlIM7yrcA8Ip8Z2Bbb22LtHhCnukNjkcAzBpnay2PHFMtuNE966nvVZXNOfoDrhAnhEnYMrMlvXFDny02YweWb3Gd72IilZ1E2p492JvIXDqf0XIupP7iLlKmYm%2FvszuJFgRk3%2BOoZGNge9jgG9QXGSNdUaPv2glc49BrxaDvfWw2cAjk3FNbYYR6HVj4Fo3bFZYZ5UOAFns%2BejyRDattmT5jW%2FqB931DTz%2BZb%2F%2BBArvmN26UtgyfJZ%2BCOh4sXJ7JQrLp0afuLpDn%2FL09lDOME6eJKe9BXLjfRGHYFz1WKvBUauHtj0qP24QYSvzKkpGextTSwobwcUz1XV2nZDAN4TLULrBuOmAC1OvAch2aKReDNT7wd9Ur%2BQVUJ3im%2BY4P2VNASlj2E7SF3ZaCzHSvb3siVj0GaZ9tk3t4jOSQAFV%2BuQrZttvRpKDHhPb6XJctPdX%2Bo23kcYS%2BZK0Qhsjh4YfEdVnfmlLCVe%2BQ2SBkm9fkfS6lJBaDzAxHcOjiON8f3A5zU0gucEz%2FiuWyvbhJ9ZdBQ%2FQfTXFGJlUrlcc6kFgrcPyEQTaGss3eaeTUYcopJOnrMbD%2Brj9CuFzyam71IL6MelALVm3gThPx8FBirZ%2BvUZzLcQleJOCkQ%2BXiZupgdhSMI%2B37bwGOqUBOBIbrOuhGS2XbJKJn9suW1hLYAfUZw83JaCq2NEBsI4YjIJL4vP73yXgl6RXnoHDHnDwDvnEF%2BAw68mnuk38FtQzGbEAQSnXwm3LCFjjEsG2KfqgjoA8sZqSsu4GMJyNc2UP8XfHNH2mNPHqUOV2cgvVv3c3tYJbhU6wQCgb%2FJdGqIdBK3eV%2BV94smms4ss1%2Bq4%2BJn7nAZx7GQ%2FcMHDGth8Ui2%2Fd&X-Amz-Signature=58a3f2932374a3b8717202f881bbe3c5a6ab6539c6962496dc7339f2d4d0f342&X-Amz-SignedHeaders=host&x-id=GetObject)
17. **Min-Max Scaling**:
	- **Formula**: 
$$  x_{new} = \frac{x_{old} - x_{min}}{x_{max} - x_{min}} $$
	- **Range**: 0 to 1
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].min()) / 
							 (df['length'].max() - df['length'].min())
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a3e8d8f-fde2-45ad-ba84-11dffd074993/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TSDQGI2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2B%2BDvV0%2FgdN%2BDv9b1Anuk3lR%2Bb7XAFZ1rMJ8%2BDr3L0QAiEAoy%2Bpgnw2fznngzXP0xSrkpExYNuIDYMGYEgvXTUYiQAqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLYirFqh36XJ2h7xoircA07xHsc1HuOUcSl2cKohpGHJSi%2BCKuy4GPvTduhQKQkRefw21jXA8c4gvnBu3MaiaI9u7XSXMZT7FDAmhFNoo75wBp7Fj6y4Vf5YK1%2BYH05okbzVJjMG9NyUoeyx1pcel9SJYJX3sfYdnhrMoyFlsbxlUOL1kshy19rCLhlcyFUkDq%2BSFZfx9hBnJH79aIzfKalaQeXFmvkDOn69%2BYZSPxINijmcPstxw2w66O2Im9fbLK4PokAfeO7EiZPT4nZGuCGYA2iZPf6Ft3tOvNLLhLrF0DaVn%2F2XJkUikr%2Fo2VQguiCg6WiQkKhfEbnp3DKEJV247B8hHDTCLQZHDczYRcfXjBbsx3Uqjwz2GJ6nTae%2Bu%2FDBVAmoXU8p8cxTbAGXHqy0nCiPdfiPknWhY3YpVMBLnM37830p4xEet%2FgaWVaPyGfzwA1OuiudaluYt3hacTGM%2BEuS5wGqXKth2D%2Fj1hAZGC2dncWRG1VqUagibKWocFFM6M1Raqj1yxmHoWnlvCby1GYD8VKaFSYJtB%2FwRe79cK86BAv0fIGP6BzhB7Gz%2FIuszyFAy6rJx0HW1ackppVMMDpuTf3r3BKuqE%2BgXuS1kXYWmrdGT1F5tAKO3LyLVN1DO3lCIn7noGNSMOeo7bwGOqUBsoUV3qrPOjz68VoKS%2BU50JDBli%2BSCNkACujRXks8Y87HvSauHbc06cxadMaruVoRYq81s%2FsWcq%2B6ySU8tVLqIo7NKJhaOArnuiuOs1S7Mmj7nqxEyTYGExqhOecXA7sZRIJ2B5j7GLVUKumC6uXN%2FNeMHJKy1%2Ft8AdfCo2TZyrC8uHvhwyF%2Bf%2BxSyWpWAtUpMQZUy1vvAlFbhbzvDY3TOWDQx6Bm&X-Amz-Signature=629d1b27be5814e88a16e663830c05c3c790969e340d17029a8ed33ca557a57b&X-Amz-SignedHeaders=host&x-id=GetObject)
18. **Z-Score (Standard Score) Normalization**:
	- **Formula**: 
$$ x_{new} = \frac{x_{old} - \mu}{\sigma}  $$
	- **Range**: Typically -3 to +3
	- **Example in Python**:
```python
df['length'] = (df['length'] - df['length'].mean()) / df['length'].std()
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18688735-45f9-4dbf-b6f3-d034c2402668/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677W6J4FK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaR%2BY%2BU8K5Q30myLnOX2ZNKkJZu%2FoeEgvBASO%2BZ04rjQIgYLk1mpAqo1Hktm1UiGzKjb9c%2B%2Bu%2BnUbw%2FH5iUFNct8AqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAolELq%2B%2BmQAeV1ircA7wT%2FjcKhZZpeiJz1SFHbuDsbuS8S6yWHPAl6Y0ryDeeOPLygaLw8tfHMbGD6jcgIYKFAEkz2cpZqp9d2oAaIcyy5Y5IpuS5CJFU7NoY36Zch%2F9%2FC%2BdoDkgH%2FpAq9Czk7%2Bvqa5vel7INutNFetDQfDWBTGMJLta7D4nsaLn64Q2XCgo2EAv6uE2BJKRvH%2FKoJdBnugWqmVq1Viz7kvn0lGJaZSo96q9hsRTHhoYkZzep%2BSGxSOKn3T162WcUkhLQs5yQ4faq6mHAQ2WuEbJU1YgzAKACHZHEPasxjkDS1GGQdNJOe6%2F9JPvm%2BwgfrnNQ6S0s7uUObIy%2B4FB3jYUG%2BS9dZOb2CEj5IUkCA0BR0xrZn3za6O5XO6DhPc6Lb7seTxcm0Qq6%2B74Hj8pdaDqlUuLh5s6EggO3jbX6zmcjeKin%2B4wMOOFIgnQTazNx7laYdZWoMhyAqzw%2B%2Fb0K3JFBujUMFVQQtF6Lk5KorqeIgq65%2BIOsAmc4QFI20J5GswG7%2FqhSg2Dd9AxkmqKE7WzZUxic2TzmtQXPnuAn%2BmxJnRwHERAFxWBDOn%2B%2FdSYHwlTgzhlg2oONLDWeLm9LlDfUxkBUGFelD4SbjZOrvfBky6VxzocS9kfp2qFQ0%2BuFMIqo7bwGOqUB73Kmq74YKRbiWnoHL1ond7nHzcAn%2BHpmarI7yI7ASReUkHeGvyrTOplDrv0aylmGt%2BCnfPEw7O2tlvv0I6%2B7vFTj6F9sZENxniUWvzuz72cEshMPCDmn3jIjoZDwG23krxxGZf8xEWv7acQy2Cw4a4%2F%2Fuh%2FTfdI5NDNhgr5J0Vz25QnVpKUio0xT41eoYjyQqbTjVStqyDiGejw2OgDpX28seJih&X-Amz-Signature=9a58aa38f9118e1edd015d1c57e0c7438b12a838d19f135fb108173f4f47bea0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dbae2f85-b73c-4c1b-b3dc-26d62ce4ecfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOT27M45%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYN683a3DSJI8Vq0j7MGSEDRz2KTCPIEumvlNBT7eGAQIgbsHndkjQi%2BK8sKfTO7qveAHrc5wBcCyWguy6F%2Fh%2BSoYqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN9O0qtNZYIKkPUPhyrcA4wWfw0%2Fn855fHqPvbF%2FclJyqhvXvF91T49NJo8XKIlIBzzByInAwr5DB3e1vPMeq7s6%2Fjt%2B4luaeYG9bdRpDZSVN%2BrRfwBFiCVCo8l%2FNbSXs3RVie8J0f3th%2BBmOmYprvjt2w369imgbouWwroRDQMXYc3b8e77TMepiWAueye4Uk8EYs0c2UpjIHQHH9cZKxO8DgzaxSeYoQi%2FJald0Vm1wbqMYNY1hiu3bDXV7DiEG0ZtHxE%2BcGjXuIOPaG8qsTr2jrexL2djI6Forvd32%2F3b2MDH%2BMf5nvqbO0ky4m64OHYiZzBHLS89qir2a6cAQDpRk3kmOTSzOUE3O3NCxVGZ2xZiRTzmgZ%2BjxaUhjWL2joWDZgSol2dipgo0UZTwN3tmJ6l%2FMiyyBdUTSurErgVx9LrR6ZPrdzY%2BQbtAqLpzTNcO7ozQMExE5hyG5d3zuM%2BPa6jv5LC0FfsNtOAHAwtB81IsudbfXubV3qZwaHpVWG8FoKhN3kymNKX9vhAsLONdazGaKvc0rrPCMGhcnEvgQLBEP7urall8r6KPCMMxxSU0NVUz6xFW4ar6qOy7eFh1LPELuRS%2FwGnAc%2FJddTAawHOsmfITTNQWck1nHuxO0zb5qLf6zdZnqrAlMMmo7bwGOqUBtWJIOc%2F6NgtCOU%2FvZp8i5YuGRHtSaE61z91biFnFMAa5CztJ%2F33IvnJOp4w3%2FkA0enq9zFKKvsS3v0y1mH3eZF%2F7TEacjVV26NaK%2FdkhvsjcsAmGyxUt3sFQeZ3bxBUeU9oSRhaGoAmrzCTRdkXmS23pxe9ST58RqtlsA%2BoAsSav3VV6XCQmj6xe%2Fb5uYGPdsyM%2BSpvalV6iaqQHFwcBd6qtWt6O&X-Amz-Signature=b69a52f71ad4d3dc2656b2ee18d915050c7eb1e93a92bc3507fd2f2e83c70eb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7b15f63c-194d-4b16-adb0-2e54f99ccf11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDSHBRIC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB51UqGpUln79c3TcPXOM2gsO37XOAc1fDaJvb9E5%2F4aAiEA5XPRL2NyvM2Iif9fLkH4jKlEuN%2FR9%2Fa7aAVKz%2FLZi8YqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGu1CaRMwi1DSu1x4SrcA4iwpWF6QFxyLhbpWNRjv7YKv%2B67ITk75QA7vWI5GAmslaPjwizpUYjRafPb%2FGyNXAuoSnyFFF9My2fkS%2FEdTvM0MPvxEYwbRqL7dMlUQUJkHuS4G7zD3PbFiaxErQapprrQpAfY8kE9UMu8z8cTgxHfneRUu52oToC%2B8wG%2BTpR4VF1zj7UFEKGjhAUifWmxnz0buXmJtR5TQxQzOFHXKHAxOVJrYQyTGdVWXRThFDABtSEhNPVi9WKil%2F42AKlzqiMUl2qga5YeaBxcFFISXK5KG2EqMKcQG7WD98qAUpDRvNozZeg98fpEiyV6eyCIivcvxAz6hsHkpRXqF3%2B25A67%2FvnUlIg47%2Fw%2BUmuNg53iieFmZ0awp5jFzfbvSE2FyEXdKSdVxnbaYZH4oIFYPcHhOSM825d2l%2FdNNdO3wHK7L6SHxirDycOfujPMbi%2FKq%2BSrBcCGVEGHVPq7WjdN2XbhM9bwMcB19i76JWlsBZbyhGcPQTptC6eyXh5Nm%2FXNLtTfFn7oUK%2FPzxq9R7FLa5rUCQL5u8GAZbH0bx5AWWu8JwRqiaVDH7%2BOtEN%2BjLV8%2FQPVqKr87wHn9LKQgtrP019dVht9fTgWskBrZbUhxfGS7cENz%2BA3gtRsc85JMLWo7bwGOqUBS9WjXZWEvyJRGNSleaW22YEhgFjgbKfMiflJ2ltQcn48Ev38%2B86%2FuSnYGM9DrgRCtfstjtKcAKiqwyNkU0a2WFb0JGFy6Z8%2F2h1OA%2BNlkJPAZEADoKfnq6EzQkVpLujdCBdcI4GAZLWDWFncHZBFq4o5uxMPF%2BR2Mb9LDJ6DYrpL2o0Ill4LrBtEdmLobjQ1Rwa4jBN%2FqfMyylGz14S4r1cSj3sV&X-Amz-Signature=00214c9f292a267a58a6ef095841313e313c72696bae87a0450f396f44f4b425&X-Amz-SignedHeaders=host&x-id=GetObject)
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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ed895fe2-732d-4632-96db-0746e1225a52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDSHBRIC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB51UqGpUln79c3TcPXOM2gsO37XOAc1fDaJvb9E5%2F4aAiEA5XPRL2NyvM2Iif9fLkH4jKlEuN%2FR9%2Fa7aAVKz%2FLZi8YqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGu1CaRMwi1DSu1x4SrcA4iwpWF6QFxyLhbpWNRjv7YKv%2B67ITk75QA7vWI5GAmslaPjwizpUYjRafPb%2FGyNXAuoSnyFFF9My2fkS%2FEdTvM0MPvxEYwbRqL7dMlUQUJkHuS4G7zD3PbFiaxErQapprrQpAfY8kE9UMu8z8cTgxHfneRUu52oToC%2B8wG%2BTpR4VF1zj7UFEKGjhAUifWmxnz0buXmJtR5TQxQzOFHXKHAxOVJrYQyTGdVWXRThFDABtSEhNPVi9WKil%2F42AKlzqiMUl2qga5YeaBxcFFISXK5KG2EqMKcQG7WD98qAUpDRvNozZeg98fpEiyV6eyCIivcvxAz6hsHkpRXqF3%2B25A67%2FvnUlIg47%2Fw%2BUmuNg53iieFmZ0awp5jFzfbvSE2FyEXdKSdVxnbaYZH4oIFYPcHhOSM825d2l%2FdNNdO3wHK7L6SHxirDycOfujPMbi%2FKq%2BSrBcCGVEGHVPq7WjdN2XbhM9bwMcB19i76JWlsBZbyhGcPQTptC6eyXh5Nm%2FXNLtTfFn7oUK%2FPzxq9R7FLa5rUCQL5u8GAZbH0bx5AWWu8JwRqiaVDH7%2BOtEN%2BjLV8%2FQPVqKr87wHn9LKQgtrP019dVht9fTgWskBrZbUhxfGS7cENz%2BA3gtRsc85JMLWo7bwGOqUBS9WjXZWEvyJRGNSleaW22YEhgFjgbKfMiflJ2ltQcn48Ev38%2B86%2FuSnYGM9DrgRCtfstjtKcAKiqwyNkU0a2WFb0JGFy6Z8%2F2h1OA%2BNlkJPAZEADoKfnq6EzQkVpLujdCBdcI4GAZLWDWFncHZBFq4o5uxMPF%2BR2Mb9LDJ6DYrpL2o0Ill4LrBtEdmLobjQ1Rwa4jBN%2FqfMyylGz14S4r1cSj3sV&X-Amz-Signature=640258cd17592486f0b3e7fe14aac224610bcf0247dda38020847f3cc22d8026&X-Amz-SignedHeaders=host&x-id=GetObject)
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