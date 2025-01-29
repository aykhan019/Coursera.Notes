

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=515589af8583e8dc72bc9acbf25bf9a1ee1ea994d5c4f0cac47d1014a17fbd29&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Dataset
Consider a dataset related to CO2 emissions from different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emission
#### Predictive Question
Given this dataset, is it possible to predict the CO2 emission of a car using other fields such as engine size or cylinders? → Yes
### Historical Data and Prediction
Assume there is historical data from different cars. The goal is to estimate the CO2 emission of a new or unknown car, such as the one in row 9, which hasn't been manufactured yet. Regression methods can be used to make this prediction.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=d6cfcb2851a8ce8b2029b9a2ad4703a5008e6813af397a6d65e3fc3808fba2ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### Types of Variables in Regression
- **Dependent Variable (Y):** The state, target, or final goal to be predicted.
- **Independent Variables (X):** The causes or explanatory variables.
### Types of Regression Models
#### Simple Regression
- **Definition:** Uses one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using the variable of engine size.
- **Nature:** Can be linear or non-linear based on the relationship between the independent and dependent variables.
#### Multiple Regression
- **Definition:** Uses more than one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using engine size and the number of cylinders.
- **Nature:** Can be linear or non-linear depending on the relationship between the dependent and independent variables.
### Applications of Regression
#### Sales Forecasting
Predicting a salesperson's total yearly sales using independent variables such as age, education, and years of experience.
#### Psychology
Determining individual satisfaction based on demographic and psychological factors.
#### Real Estate
Predicting the price of a house based on its size, number of bedrooms, and other features.
#### Employment Income
Predicting employment income using variables such as hours of work, education, occupation, age, and years of experience.
#### Other Fields
Regression analysis is also useful in finance, healthcare, retail, and more.
### Conclusion
Regression analysis has numerous applications across various fields. It helps in estimating continuous values using historical data and independent variables. Various regression algorithms exist, each suited to specific conditions, providing a foundation for exploring different regression techniques.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=b96cc0f6f9ac086d1021dc2827ea728ca09b66b435830587e180860a294a95c3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Introduction to Linear Regression
Linear regression is an effective method for predicting a continuous value using other variables. This introduction provides the necessary background to use linear regression effectively.
### Dataset Overview
Consider a dataset related to CO2 emissions of different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emissions
The goal is to predict the CO2 emission of a car using another field, such as engine size. Linear regression can be used for this purpose.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=b10f04721df16985124fc49c477a13892710f3df394703a911709bef1905cddd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Linear Regression Basics
Linear regression is the approximation of a linear model to describe the relationship between two or more variables.
#### Variables in Linear Regression
- **Dependent Variable (Y):** The continuous value being predicted.
- **Independent Variable (X):** The explanatory variable(s), which can be categorical or continuous.
#### Types of Linear Regression
1. **Simple Linear Regression:**
	- Uses one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size.
2. **Multiple Linear Regression:**
	- Uses more than one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size and number of cylinders.
### How Linear Regression Works
#### Scatter Plot
A scatter plot can be used to visualize the relationship between variables, such as engine size (independent variable) and CO2 emission (dependent variable). The plot helps to identify if the variables are linearly related.
#### Fitting a Line
Linear regression fits a line through the data points. For example, as the engine size increases, the CO2 emissions also increase. The objective is to find a line that best fits the data, which can be used to predict CO2 emissions.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=96df2fd594988d209e78bfd8ab01f5c13105a788bc0ca2883ea3b3169873911a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=884284e65e33bfe274948c8d6659b4c06efd5f1b4288fd996222b9ee3204fefd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Representation
The fitted line in linear regression is represented as a polynomial. For a simple linear regression with one independent variable , the model is:
$ \hat{y} = \theta_0 + \theta_1 x_1 $
- $ \hat{y} $: Predicted value (dependent variable)
- $ x_1 $: Independent variable
- $ \theta_0 $: Intercept
- $ \theta_1 $: Slope or gradient of the line
#### Estimating Coefficients
- $ \theta_0 $ (intercept) and $ θ_1 $ (slope) are the parameters of the line that need to be adjusted to minimize the error.
- The goal is to minimize the mean squared error (MSE), which is the mean of all residual errors (the distance from data points to the fitted line).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=35cacf0bb38e7719de8b24bb3e9d45654fe5b55c1890ad9c468c04347778fc40&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA2ZSPP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOHU8%2FT2FTuNvc3osh0EFhhynyG%2F3%2FWJln873bg0iKOAIhALNdNIm4THtGffzQUVJMmnmE4R7WvZL%2FoL7YSOBXkVLNKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxcnpt9aAj9Onc6cycq3APRkZlc4dFMw7PmWZMSuHyb9cwz%2BEe0bP74yaC7mjk1gbgBZioYnogfg90T3tR2Hgza6PQPnhIgH5QQiwVIIbgnudozAu7uw3BjtCwMKOC6kzm3SHiIOILmcDmY602WDoscf6FEkLP2wonGizLREUovjl6P0NKMsmAfP1cIyfKu6aCRCmOEvNFHK%2FejSrSnmLjs%2BM5fhTssxae4vK2S7wKk1NOr01JfysyoSlUcXcLa2LVOLC8m64kJSutVohDhafYiv4XJariMbCFdaZAL8tP6KTlS1qVIZvpwwfJYUqz1Eh%2BpBPqK1%2FlgjNss%2Fo%2FP9VytL1bCzWRXJia7KGAx2pIia%2BDTq0BrpjAbQl9Zdd0dBtxh0cQsGC2aYd3ISmjYDSIpOVdNFr5u1wHNpk93VdDj46%2B8BhMAbLYQepNlqt%2Bo3kUdzX80agZQoN6bHI9n%2FWfvSl9REB8Zm4tO1Cy33Nmgr5j%2F1o73WVTPx0gORhlZDvsS4NTXwgWXnRfBrdlCZWZLbLp9Lou%2FqH6RIzouNwqfUPr%2FFqZzgrso7eRruNJAoLOgcv3NOn1LaJSuCPXRa7f4GUkc8yHnuriJSqfl8LSfVfT2rDK6lV3gz20rWZNuIkNM7LkWgR2gNXXBRzDU9Om8BjqkAcDlPmHbQFPJpyMa7hA2IvKqBT973ooUMZb1yDSILsVv6R%2B2j%2F9gVfVknhUhAcbonkjuRVUGtxWwm2sfS%2B8mRGF07NsBp7PKIwVd4BEWqx3rprBOW8jnCNeuVHWFvZECALDImXBlh1PcrnC66ltPGKqopbZNQeQeKlwAXQMm4hi9qK5wTZ2ELatCXiGduf158cuU0R%2BPWxfu0ye8qNTw2soFRvFW&X-Amz-Signature=192cd7cb12c4e22db6ceed75b98b91b001f0dd1f906038b6d4cb28f9a6700941&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Calculation
For a dataset with known values:
- If $ θ_1 $= 43.98 and $  θ_0 $ = 92.94, the linear model is:
$$ CO2Emission=92.94+43.98×EngineSize $$
#### Prediction Example
For a car with an engine size of 2.4:
$$ CO2Emission=92.94+43.98×2.4=198.492 $$
### Why Linear Regression is Useful
- **Simplicity:** Easy to use and understand.
- **Speed:** Fast and efficient.
- **No Parameter Tuning:** Does not require parameter tuning like other algorithms (e.g., k-nearest neighbors, neural networks).
- **Interpretability:** Highly interpretable and provides clear insights into relationships between variables.
___

## Model Evaluation in Regression
Model evaluation in regression aims to assess how well a model can predict unknown data. Two main evaluation approaches are commonly used: train and test on the same dataset, and train/test split. Additionally, K-fold cross-validation is introduced as a more advanced method to address some limitations of the other two approaches.
### Evaluation Approaches
6. **Train and Test on the Same Dataset:**
	- **Process:**
		- Use the entire dataset to train the model.
		- Select a portion of the dataset as the test set (without labels during prediction).
		- Predict target values using the model.
		- Compare predicted values with actual values to calculate accuracy.
	- **Metrics:**
		- Compare actual values y with predicted values $ \hat{y} $.
		- Calculate the error as the average difference between predicted and actual values.
	- **Advantages:**
		- Simple and straightforward.
	- **Disadvantages:**
		- High training accuracy but low out-of-sample accuracy due to overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GYI2KAP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtwW1sszot7P%2F0hdNieUsx6LtYy%2FvIzKaWhDIg6OypaAiBOkW3WLJp%2Bm4PDKn2axZ%2BQ49nrHNa5fVn%2BiR9xqKE6QyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY22X9I9uJm1asJO4KtwD2T7WqdZI%2FcoHTfpXsuHwvPVfeg0zLbPkY6BhVPSZs7XEe7kWuFUoCQR7b9EznM3znEapk%2BRjyal24%2Bwk6m7VwqwvR7J3ZbYje2IGrRTERx4j5DpOaoud%2F2hxOT1RtkDFDQYmPIgXd8Sk%2FWAxlVJQcNzLhEUTSFwO1C%2Fj6sjkTgID0N9WoM3nOLXl62gaUS700R24TQYb3CFy3U72lu%2BwDkQBklF3FEGzGpSRUF2hJDD7jqRgtwpgstxcygP7g%2FYIsdqU5lw2%2FJ5nWEbdsMK350ZDp%2BnwxdTk0rg7zIgyMjDRzPv3JGKo1bkNSeQ3eazvgtzDQXK0FEGyBp2QyqiywBkmece1aRgYvnbruBq5Op%2BV8lXa0X%2BHkjSVRPry0q1s4z6fi0jkOyWpwi%2BDEN9Tkk7KYHSajJ4HQrC5DRLG5e2b7NOil4nrGqnKHE3B%2FLgWOlHwpg4zxY4pMX%2Fu08h6U8DOqaDRv%2FM4o1THd1ghh2eqIe7yLtS%2FKS%2BIZo%2F%2FAIw10%2F29L6QClCBACM01%2FXNuKG1l4WxjtJj5mbpuSxe8dK3TQqBE5FwRvzIqFQ1V9pitqVu%2BHfdiqGARQMV%2BWw1qzI6USGhbmSQsYKVIbCIlMRbCd0IXOYEFBX1hh6Qw%2BPTpvAY6pgH1%2FkxxPAiVygqknJYqxqGVvcIH6iqbUn3iVe1BDG7n0YmHxfKi1LFtlFZeEPB0MoZY0JaekDe4MllI%2BGvZzMBLlHZlWQRpuEO9k%2BbKaoz5oFRQYhGjyxB1wYw7blv4E%2BBOXTRjcuvY%2BLzDCJYpk%2Fgv7m1AkAeF%2F5j3nSmIEvHOmYG809pui8yxuTiKv6ab8eeK5lTsJqb2wGzHr2%2Bw5ObfjXUkjXGA&X-Amz-Signature=55f3e63e66fef57e37a3bd62de71c2306f94f3135231ac42a5aa1ef80d609393&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Predict on the same dataset
predictions = model.predict(X)

# Calculate training accuracy (MSE)
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse}')
```
7. **Train/Test Split:**
	- **Process:**
		- Split the dataset into training and testing sets (mutually exclusive).
		- Train the model on the training set.
		- Test the model on the test set by predicting target values.
		- Compare predicted values with actual values to calculate accuracy.
	- **Advantages:**
		- Provides a better evaluation of out-of-sample accuracy.
		- More realistic for real-world problems.
	- **Disadvantages:**
		- Dependent on the specific split of the dataset, which can introduce variation.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SHPIHB4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaKWrtxwIsmqVgWBnjfWI%2BtHxysEgSUe%2FnSA6nvCmLvAIhAKJltI4V2HRmP9vIIuYcD3Xd3e1MWMdN50Ymy%2BzzjfsUKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy8n6TtHBGhI6oEvJoq3AMFWL2e47hgADNBYK2jmio7EyXDdrTbppk6xLTaX3Vl3k9%2B%2BscVCaLS6S75Oqi8UdRFRKIgDjCQY%2BHJueElngYbSJfa7LCrH3XLpou9r3dF9Wz8AK9tdDIFtZghnFpFZVJzx1f5%2B%2FNkzPZ1jzBHyNsZOm2CR2UC%2BmtVYyL6foP%2B3mL0qmhIiY6%2BzBPH1I3Tk%2FfEPmCzArjflQDCYXnCHxdMJI6P6RgGdf0edUqKmUL%2B8Ikgswg8znMASXesCOeUaWfYJyWLuqvp5bDwr2PNoATkG5IiDRDqySru8DaELyu52H93qApdXkuGa35yupIA781ngrKqGJnr%2FMBa005PWFnKQ8vPeG%2FXHyNtgY3FHhB2CY50%2BRrfgOx1J5rmtKOtjra9qsTfVSC2WtRuMKSF8eqnQTWX0Ij8sbwhAQBaiT3Rh5mady9fuV7AkZsi9oJFf5ugIIo7%2B0%2Fradt4TTasR7DHNShd1y7MmRlJ702TyQDQo7rUE41f%2BN%2BfDYZkawcvXlt%2FfXEru0T87HHlr5aBTvuhE%2FMgypi3T0UUeZ1IU6y8TAAqFvMVnP7YVhV%2FniPZEYno75WJ0tompaIxeq79DRTo1UY6x%2FhsX%2B5i39kY63meuj8UVQOCRhOyLgKa7jDN9Om8BjqkAZ1pwPN3bOLY2IV5imiBr%2FRuyBeAh7f2LiivumiOJCnAmW5VjQK5Q7eoUS0oC7fQmFRimhAEehV2%2F%2BmL1VmqSSW1IMfjHZISvK%2BABijt8CenFcmGmSRrivy6jlsK0aBFTiyUKvgjOQ05AP6pUgONGOSQFT7rorjodVOtc5PrkR%2BQWJxGfSOE1J3pXxJZePjMPVe%2B01k0VAKxX9cwhNcOK2ueCLZo&X-Amz-Signature=1c409d3de65e92246b65cea359ad47a67653ff79fced914d72758ed4c5d4bb5e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import train_test_split

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model on the test set
predictions = model.predict(X_test)

# Calculate out-of-sample accuracy (MSE)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error on Test Set: {mse}')
```
### Key Concepts
- **Training Accuracy:** The percentage of correct predictions the model makes on the training dataset. High training accuracy may indicate overfitting.
- **Out-of-Sample Accuracy:** The percentage of correct predictions the model makes on data it has not been trained on. High out-of-sample accuracy indicates better generalization to new data.
### K-Fold Cross-Validation
K-fold cross-validation is a method to address the dependency and variation issues in the train/test split approach. It provides a more consistent measure of out-of-sample accuracy by performing multiple train/test splits.
- **Process:**
	- Divide the dataset into  equal folds.
	- For each fold:
		- Use one fold as the test set and the remaining $ K−1 $ folds as the training set.
		- Train the model on the training set and evaluate it on the test set.
	- Repeat the process for each fold.
	- Average the accuracy results from all folds to obtain a final evaluation metric.
**Example with **$ K=4 $
- Split the dataset into 4 equal parts.
- In each iteration, use a different part as the test set and the rest as the training set.
- Compute accuracy for each fold and average the results.
**Advantages of K-Fold Cross-Validation:**
- Reduces the dependency on a specific train/test split.
- Provides a more reliable estimate of out-of-sample accuracy.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634SUB272%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyFnapHnBn%2FU2O851WQdylVpHWtpHn36bhDr7uhWBUxgIge8Mghgl4vdZd%2BMuVoeh7PsZHAi84snfwTcU4PP4nWgEqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFt%2Bg%2FO89ePYZoRwircA%2FAFTm%2FVuS%2Bs%2F5RVukqKF%2F2CxXBHW2tgEPxgrNmWZvfoLKpPfU%2Fdsu%2FZnd8sosW37ZRPrjMAGjFIHiN3ssg9d3ZuxN6HwEMisiB%2FIa50eXqCcXzeTeg%2FjcSgzBZI4zOOx7noAxEIgqEt0UirblzVoxpgD2R5d%2BwTf5ZaoWeo8KLn1c7ONVB2urlqm%2FwZigkWX6PZnlABtwb2tvyIdZyTuiV0DvAF4xAdUnGit5h4QOV2VjvPhYp7LJzPKFzw7dLLNxLQnrfcYLFN2BNWn610rWbQyPPTHwU9T%2FLAZVVsVpc3zvZAqUehtrXXc1BNmK9A9zk4YFELqvfUF3yXISu0s4Sgh3gemWETD7Qh99qnAkjR%2BSeKonVAa%2BJLei0czAQzGGsd7ysez4gJB2vlDQBYpFneyK5lSg2qpmEuU%2FGurOyPhL3Gz5BF681r04Nu1d3x1iKIuhszJFVBMWhhFy%2FtRb1ruEnBgxt9mLlV8IMGQzuEJuUVr2v61%2FxJQM4NCd8cUy2vC6rDPMdbaVyaaqnOFSymYPgWa3exBWwLxj54bnvsPEOxdgWWelWMVKj%2FSo3TXfjQq0EU5LVtnpS%2BNX1kioGQlv1O%2BZO5kAK4ImZ1HrzTY80jJyEYRCc3JtvZMLH26bwGOqUBKiPz5RoZkhSV1qwZUU8ufpC59TJgPXVnZB9RlsaecxFOuzeqr1iSyTgyX%2Bdk5TBWx%2Baps7KADwEzZMAyq2JU1q%2BR%2Fby8EmE5BXTNifYBKFIYQwvHCe%2Fl8Kke%2FxP2YyY9jxChohp0lcfrSANf%2FiGaVfhCx1aQwtzHfdcry9BvRtOd6c580qKpQRIHxgXFMo%2Fgri3kZG7fXL8p0e4UsQSyE5lCowYr&X-Amz-Signature=98beebac2654f364dd299bf49dd5ad09fc3d5c4d944dce990a6b71daba48ed3f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import cross_val_score

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Perform K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=4, scoring='neg_mean_squared_error')
mse_scores = -scores
print(f'Mean Squared Error for each fold: {mse_scores}')
print(f'Average Mean Squared Error: {mse_scores.mean()}')
```
### **Formula for Mean Squared Error (MSE):**
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
 $$
Where $ y_i  $ are the actual values, $ \hat{y}_i  $ are the predicted values, and $ n  $ is the number of observations.
### Summary
- **Train and Test on the Same Dataset:** Simple but prone to overfitting with high training accuracy and low out-of-sample accuracy.
- **Train/Test Split:** Provides better out-of-sample accuracy but can still be affected by dataset dependency.
- **K-Fold Cross-Validation:** Mitigates issues of train/test split by averaging results over multiple splits, offering a more consistent evaluation metric.
___
## Model Evaluation Metrics for Regression
### Introduction
Evaluation metrics are essential for assessing the performance of a regression model. These metrics compare actual values to predicted values, providing insights into areas needing improvement. Several key metrics are used to evaluate regression models, including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Relative Absolute Error (RAE), Relative Squared Error (RSE), and R-squared ($ R^2 $).
### Error Definition
In regression, the error is the difference between the actual data points and the predicted values from the model. This difference can be measured in various ways.
### Mean Absolute Error (MAE)
Mean Absolute Error is the average of the absolute differences between actual and predicted values. It is easy to understand and represents the average error in the same units as the data.
$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
 $$
#### Code Example
```python
from sklearn.metrics import mean_absolute_error

# Example data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate MAE
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae}")
```
### Mean Squared Error (MSE)
Mean Squared Error is the average of the squared differences between actual and predicted values. It emphasizes larger errors more than smaller ones due to the squaring term, making it more sensitive to outliers.
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{RSS}{n} $$
#### Code Example
```python
from sklearn.metrics import mean_squared_error

# Calculate MSE
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse}")
```
### Root Mean Squared Error (RMSE)
Root Mean Squared Error is the square root of the mean squared error. It is popular because it is in the same units as the response variable, making it easier to interpret.
$$ \text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
 $$
#### Code Example
```python
import numpy as np

# Calculate RMSE
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")
```
### Relative Absolute Error (RAE)
Relative Absolute Error (RAE) is a metric expressed as a ratio normalizing the absolute error. It measures the average absolute difference between the actual and predicted values relative to the average absolute difference between the actual values and their mean.
$$ \text{RAE} = \frac{\sum_{i=1}^{n} |y_i - \hat{y}_i|}{\sum_{i=1}^{n} |y_i - \bar{y}|}
 $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RAE
rae = np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true - np.mean(y_true)))
print(f"Relative Absolute Error: {rae}")
```
### Relative Squared Error (RSE)
Relative Squared Error is similar to RAE but uses squared differences. It is widely adopted for calculating $ R^2 $.
$$ \text{RSE} = \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RSE
rse = np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)
print(f"Relative Squared Error: {rse}")
```
### R-squared ($ R^2 $)
R-squared is not an error metric per se (by itself), but it is a popular measure of model accuracy. It indicates how close the data points are to the fitted regression line. A higher $ R^2 $ value indicates a better fit.
$$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - RSE $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
from sklearn.metrics import r2_score

# Calculate R-squared
r2 = r2_score(y_true, y_pred)
print(f"R-squared: {r2}")
```
### Residual Sum of Squares (RSS)
The Residual Sum of Squares (RSS) is a measure of the discrepancy between the data and an estimation model. It is calculated as the sum of the squared differences between the observed actual outcomes and the outcomes predicted by the model.
$$ \text{RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = MSE * n $$
#### Code Example
```python
# Calculate RSS
rss = np.sum((y_true - y_pred) ** 2)
print(f"Residual Sum of Squares: {rss}")
```
### Summary
Each of these metrics quantifies different aspects of model performance. The choice of metric depends on the specific model, data type, and domain knowledge. Understanding and selecting the appropriate metric is crucial for evaluating and improving regression models.
___
## Multiple Linear Regression
### **Linear Regression Models**
- **Simple Linear Regression**: Utilizes one independent variable to estimate a dependent variable (e.g., predicting CO₂ emissions based on engine size).
- **Multiple Linear Regression**: Involves multiple independent variables to predict a dependent variable (e.g., predicting CO₂ emissions using engine size and the number of cylinders).
### **Applications of Multiple Linear Regression**
8. **Identifying Effect Strength**: Determines how independent variables affect the dependent variable. For instance, assessing how revision time, test anxiety, lecture attendance, and gender influence student exam performance.
9. **Predicting Impact of Changes**: Evaluates how changes in independent variables affect the dependent variable. For example, predicting how a patient's blood pressure changes with variations in body mass index, keeping other factors constant.
### **Model Representation**
- **Equation**: The model can be expressed as $ \hat{y}=θ_0+θ_1x_1+θ_2x_2+…+θ_nx_n $.
- **Vector Form**: In multidimensional space, the model is represented as $ \theta^T x $, where $ θ $ is the vector of parameters and $ x $ is the feature set. The first element of $ x $ is set to one to account for the intercept ($ \theta_0 $).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634SUB272%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyFnapHnBn%2FU2O851WQdylVpHWtpHn36bhDr7uhWBUxgIge8Mghgl4vdZd%2BMuVoeh7PsZHAi84snfwTcU4PP4nWgEqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFt%2Bg%2FO89ePYZoRwircA%2FAFTm%2FVuS%2Bs%2F5RVukqKF%2F2CxXBHW2tgEPxgrNmWZvfoLKpPfU%2Fdsu%2FZnd8sosW37ZRPrjMAGjFIHiN3ssg9d3ZuxN6HwEMisiB%2FIa50eXqCcXzeTeg%2FjcSgzBZI4zOOx7noAxEIgqEt0UirblzVoxpgD2R5d%2BwTf5ZaoWeo8KLn1c7ONVB2urlqm%2FwZigkWX6PZnlABtwb2tvyIdZyTuiV0DvAF4xAdUnGit5h4QOV2VjvPhYp7LJzPKFzw7dLLNxLQnrfcYLFN2BNWn610rWbQyPPTHwU9T%2FLAZVVsVpc3zvZAqUehtrXXc1BNmK9A9zk4YFELqvfUF3yXISu0s4Sgh3gemWETD7Qh99qnAkjR%2BSeKonVAa%2BJLei0czAQzGGsd7ysez4gJB2vlDQBYpFneyK5lSg2qpmEuU%2FGurOyPhL3Gz5BF681r04Nu1d3x1iKIuhszJFVBMWhhFy%2FtRb1ruEnBgxt9mLlV8IMGQzuEJuUVr2v61%2FxJQM4NCd8cUy2vC6rDPMdbaVyaaqnOFSymYPgWa3exBWwLxj54bnvsPEOxdgWWelWMVKj%2FSo3TXfjQq0EU5LVtnpS%2BNX1kioGQlv1O%2BZO5kAK4ImZ1HrzTY80jJyEYRCc3JtvZMLH26bwGOqUBKiPz5RoZkhSV1qwZUU8ufpC59TJgPXVnZB9RlsaecxFOuzeqr1iSyTgyX%2Bdk5TBWx%2Baps7KADwEzZMAyq2JU1q%2BR%2Fby8EmE5BXTNifYBKFIYQwvHCe%2Fl8Kke%2FxP2YyY9jxChohp0lcfrSANf%2FiGaVfhCx1aQwtzHfdcry9BvRtOd6c580qKpQRIHxgXFMo%2Fgri3kZG7fXL8p0e4UsQSyE5lCowYr&X-Amz-Signature=11136e1ec2d6e0448f9c58857698f0f50999443e39c9d2ab17d8537ab00e1d27&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
Here’s an example of implementing Multiple Linear Regression in Python using `scikit-learn`:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Coefficients and intercept
print(f'Intercept: {model.intercept_}')
print(f'Coefficients: {model.coef_}')

# Making predictions
predictions = model.predict(X)
print(f'Predictions: {predictions}')
```
### **Error and Optimization**
- **Error Calculation**: The error for a prediction is the difference between the actual and predicted values. For example, if the actual value $  y $ is 196 and the predicted value $ \hat{y} $ is 140, the error is $ 196−140=56 $.
- **Mean Squared Error (MSE)**: The average of the squared errors across all predictions. The objective is to minimize MSE to find the best parameters.
### **Parameter Estimation Methods**
10. **Ordinary Least Squares (OLS)**: Estimates coefficients by minimizing MSE using matrix operations. Suitable for smaller datasets but can be slow for larger ones.
11. **Optimization Algorithms**: Methods like `Gradient Descent` iteratively adjust coefficients to minimize error. Suitable for large datasets. Some Optimization Algorithms:` Gradient Descent, Stochastic Gradient Descent, Newton’s Metho`
#### **Code Example:**
Here's a simple implementation of Gradient Descent for linear regression:
```python
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = X.T @ (X @ theta - y) / m
        theta -= learning_rate * gradient
    return theta

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Adding intercept term (column of ones)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Apply gradient descent
theta = gradient_descent(X_b, y)
print(f'Optimized coefficients: {theta}')
```
### **Prediction Phase**
- **Using Parameters**: Once parameters are found, predictions are made by plugging input values into the model equation. For instance, with $ \theta_0 = 125 $, $ \theta_1 = 6.2 $, $ \theta_2 = 14 $, and input values, CO₂ emissions for a car can be predicted.
### **Concerns in Multiple Linear Regression**
- **Number of Variables**: Adding too many variables without justification can lead to overfitting, where the model becomes too complex and less generalizable.
- **Variable Types**: Categorical variables can be included by converting them to numerical values (e.g., coding car type as 0 or 1).
- **Linearity**: Ensure a linear relationship between the dependent variable and independent variables (maybe scatterplot). Non-linear relationships may require non-linear regression.
___
