

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=fef95d3ba9dd50f76afffac6d81fe7d171444cede57193900af70389c8ee3878&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=b89b0e6f1d77d38921e83ba43f3772b2a0fd629d829e4f2559cab749c47a45bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=417e0ae87c99da9e235929eb37859342ac86b61c8ec7ce3068d0cd4cdfb15e14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=49718575789d92af41ba6dbbf04671fe133ad8c92ec06fe91473bc18e63f23f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=28c17a5f59be616c0c10ff26feea3b560adf727af2b0dbe46520d1aeeda7933b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=b222464ba893d506e729e13052cb1368df412f2df1ba913d3727a5cc8092d514&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=949ef54c990b473084aa5b276ec918a6685cabaf9cc3307174eba0395d825ff3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3VXQAK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC5H0psPj7y9T3h0uIqlME5Q7ygLJIEHufEI7pDCMH5vwIhAMrib4jBHBM2yN34opbuR8Wat8BX7fms55ZVd16EFVjUKv8DCDIQABoMNjM3NDIzMTgzODA1IgzAAAQTqPOmNT75EsMq3ANvdQnaW2FX0qXmDyxrDV9SVoNhY2SKhGZpw6hzjstVOsD2tKds5QyCl%2FiqbcZ5QDXuv9csrHVi7n0SECJ9xNXRDZxS5HfCj3rRNsD0%2BY9Crb%2BkhDaylInH41tCfAOxsGY5yXmfSuRVgeJ8tp%2BK6f58pAcZfrkio8xbjYJ7aVG5W3SyMAf4Tt%2BghfClfooeSV%2BtCM4%2FkUnlsYUmcZBKnatmtDfG8Br%2FqkDjeVFcYSoNoGK54M1AljVNqGG4gL2V%2Fq3aHV3QoUKLDEb9f8PeCxnDksYf33nIS1gbv0fqH2ocYxw59VwlXZ1%2FlI16MHlo%2BNVcazH6n40QXQOBa6FMIBtCX6SqE7Xp48vilnP5Kfdrn1JyjWaHR6h6RH3%2FclUmt3CR2jP4VQfPiMzXXH%2BBFjTDyPTCWifx151fTeOEUV81jHu354YGfXlfe%2B8uLscYHd8atWmFrgOzb7DckIfUjQxk%2FuJLLOqmneP6je8TkNo43OPIQ1CC%2BQXeOOOYXgOMus0D%2BpjfhXZHDk4VizBNplSM%2BUY17VNYKjCZLBXKv6%2B4OYwIdC%2B5miwV%2By6PQtQZhs%2BCUxYqDyR1ODsoLAmy9PcQ59IqDqU%2B6HEvPxSGkwsz8RzwdWDn%2FLCDGQV3kDDahIm9BjqkAbVUt1jwj1taywMjYrcl535I%2F2mAoHlvnFQtXYEGYG6LYyabJOigWySvB5vtvo4eIWWYFVGGYTAQj9M21qlo7jTRRc3aZl0dFczl16gBQk3EHsRy6%2FC0VMu3IzvvNpqbZs3HBDo8yOTvOKL4ffhBJIYlTzK7q9qGH2rym93rAgT4cG2raF6ASdp%2BJjujdmPLS%2FoH5P%2BGEDCtjv0tOatX%2Fl9dOfjP&X-Amz-Signature=a35da7aa0c03fdd9fed06345e3fe92455b4de0be0201d5abc51f0a64b690a8c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZSFN7RZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIGcWgCBiBnGB5pJclSWENedbgrHNJszYNSLVSKRynNkaAiAC0aonAMAmgeyZe2eO6euTxuSl1OgWhBItwI5ES6gGOyr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMRohcNKZR8LqOhYMRKtwDiyFJD1V7EVYmhH51bHLvVgw5MMLV2ps0t2Z%2F5TPpmXWpnEXKApFOMCY%2FS%2BkpI99TzuDhEZWvSLQOByPyE9pJvidhjxCpxBYarTq6mRiwJ75LtfzjN69VQrjhwYTohn8dPQuZG4fXn37cnvYlu6ux8VF78LfkfD6TYOXcOA%2BaodM37lb5nV10bTgC21tJDX85uLJUcNqk7ZIAriB8Dwug8zxlVHqCGkM6COIlRw1P4kp%2FmfVMiHThVEQ%2FICcfitqIjtXiKLb726Sjx0npiQrRLe%2Bs9HDHQ3I7gnhhN7mBTta4U4G6%2BhklUwLkbNd3vKx5Zm58tqvxjXscFTMg91DxZA22TPflI9lmvVqkWi%2FseDljV3K2rNe3yFYL2SSDTEDDYFqzQ3hCyVcCIrSgX0SOg1yMOaqJm%2BjvwW7WMX%2FaTvuK73%2FBFen7Rm3YCjumZXPsm68wk0oLE64ijiX%2BaEUgRXEhNvwxg7eGER0UGuCxsM1tgkse6xFPg4%2FSJTKQByIN8KXeIkbemsuMny2YyuNyIKBWm0yXbPeilWXlsuNrrIh5AUlVoeZFlOa8i6SRY2X6%2BSw8OiQLSkR6QyV6p3Qo6ffz86eZOXsQCJFfBhx9i3XEBHub1N5apiWtpQAwkYSJvQY6pgGpWec9XU%2FM3Neensf3kXl3Iuj%2B0qrLFZLn5nypxexy7t2N5P10s2opcnEAgZNK3T0wbKsf2v9T1bgZq6%2B%2FNvnHHHjFwGy5E0FEZWO84NVl2pneO6CNiu8Ug1fsMp1s9DKxgvt7IDwN16hPf20%2F3ArPTDnhOQhS7J7WnNVyhUjH2CZziaYzk%2BqFXZZUiXt5SgtGZlxQiwXTEHfpU%2BQPh0C%2B7slWPxBx&X-Amz-Signature=5df5099a058f1c3c0d028fcba3c7077402653b941bc72ab440bbefe4c1411ea2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWJRNTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDe3mkk5DHTLMuJ8gdG1cKYNetMuWq27HcOL%2BcEFYVAUAIgBaSIOM1CXCzI17KHmPrmf4AGsl6u%2F36R8mRtcfGBWRsq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCfBY%2FDldOVGMUOLzSrcA%2BopkGdyw%2BxCXnamLszLLQHbnqSPKStPfBI4%2FOxTcYlJ6G4%2BdhnREch8pLhLUAWe5GYkKVVb1RKQzamLFZlhZbksLm1JruaCMYFBQmu78ADNQJfAi%2BTuXFUU0bm6hkLafhUeNgJxFYM6Q%2BRHj4mkTfT9zPYJy9Sj7ZX9BF7Rm1qAVey6liVKO93dIZ2Rg4cgbhuNnFZNRt9hJ7XEim%2B3lWoeOT0aioYBgmIH2kGXYu%2BSaLcapN8s8f3d0SwyNHAc70Qx0PNwcgceDaTKIXhEnYCNDSCxpHzLYrmnnunXlIQDV9CSyO%2B5gWcgVQTXXlX4iCkzdKsLs4P8SEVFiCMZsRfJUYi%2BZnl%2BqerqpCXfJOlf%2FruIuCwYjy7RWv07Fq8Z0zJ0sYVhWb7rVmWaJ%2BUt1OJGYViQAUiBqKVN%2BMWcFXEC6G%2Fi%2FkU6yzDtOJqqWIH5tNEUb7buPnIMFs%2FPECnS%2FNXaqCt54DR1AUaoF8uaryXnnpNLeBAp6TUzBdWN0oF2wv69RUGRJmhn2JJMTyrSrTh%2BXTp95ffBtTUiILWCCzB%2BGtdWjEp1mTeBaIRBfgDmkoMR7O6ze0oJrwYYN9Iu9zj73chLVyFtbIVd50vN7kvNAAIQT0%2FXaCgMo0hJMPWDib0GOqUBm5L2YTJ8LbteeNfX1rwRWCdsbnV26hzTanbA9BJ0DmVmM6pnjYIm4l62puCT3zvc4jOyIQrnGoxFGs5bXFIvUPxLWNKmaC%2FR69%2FDB27JjN%2BuHXIkUEkWuxx2I2KKJaNbow3fAsW3XJv1u8lxARE2yKK6kUJsio92fnFlJr6h7tb21B1o0cBv%2Be8tcB5Wka1ZF4zphrtlZl3PIO%2F5ld2EhuayHCrs&X-Amz-Signature=0a5d7a46987cdb4929f8da32f07ddc2dcfaacc82c4cd03405cbfbae70941321e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3QJGV7P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDTpmmih2cMxgw0MT98WlyfWAI9MsWNSuAoikyHMOEPmAiA4CnMN8D88pbbXlzaJ5u4lRRVUjbKQTuOYa0c4XeoqZir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMaa0u9shOItFbIDhHKtwDYUKAzUwL2zoUPGvb4trilkF4xQit0OumEr7R6XnWDsAUtJPubGuYPXtNvd%2FTMrp81lFJFgWGevLWaUiv2Y5DB3%2Fo9fiZkfCVRsxslIaBtm7rEThnkIVzkMp92Lz8fKJinYQp%2BvnXdQTf1Pur65XuijymyoxZ0nFj%2FNymTkwDKzMvgVhfU0zdcdesinR9c1IsgUirMh690XJwyqjCHMOv9I5OwdLGoCe7yRQZriFxGmvelw2A8eRh6SmQifkNnQx3J8rbOFRtrBhVZZOBT8Vo8BBkfB8CIlFDwrhc%2FX3wWPYZgUS3gyy6ufKKOOHc3VcdSx7Shgje3tzmBxLJ7dyrco2b%2FrnJJ0Zf2MJLcC7FS1piqvYouAbt5PuDltVqin7ehwin1MbYg1MacvIMDNRIso9JYVWdL5vBx0VqjVIqLc2cocf6Dud1uPmsNOrkKOZ2aOr3%2FKXsAp92TzT4axpu%2FzBnrA%2F87dP%2FqWoUhbOC6LJjSZGBzk%2BONn7kO%2BHjugXGEEQ7dWkaZUrn7VddpuOcqMaspkW%2FN8HMUzHZ893jsk8G5ML2DFIw1N3kSx0BFokQOiKNn8WwEkhXg1lrS4hF%2BZyiPfx1UjMpKL1iOhQsGALgkH882SfTYGkrH%2FEwk4SJvQY6pgF8pubCeQX8YqII86WOiVwIy3CSZafc%2BRgwAEC09SphZBpxrV%2FxbwCAxTrc2K47B6vbyPJaqzpgC7O2ozxJiFF6EUGouE%2Bg2X6xMPKla2b08quHzUT6nYRuyKbb5sLu4BcpL2iDZZKErXJd0x1EY8WW2deiStqMamN%2FmoIKACMG%2FZtefFU%2Bhq9xLpxQYZE6ZBEQF6zTshC1qE5%2F1wAJxfdQCytCVTuW&X-Amz-Signature=31d06206076032f518168c26f72114bcc464a0167fcb92acfea2eb6b56a8a9b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3QJGV7P%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDTpmmih2cMxgw0MT98WlyfWAI9MsWNSuAoikyHMOEPmAiA4CnMN8D88pbbXlzaJ5u4lRRVUjbKQTuOYa0c4XeoqZir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMaa0u9shOItFbIDhHKtwDYUKAzUwL2zoUPGvb4trilkF4xQit0OumEr7R6XnWDsAUtJPubGuYPXtNvd%2FTMrp81lFJFgWGevLWaUiv2Y5DB3%2Fo9fiZkfCVRsxslIaBtm7rEThnkIVzkMp92Lz8fKJinYQp%2BvnXdQTf1Pur65XuijymyoxZ0nFj%2FNymTkwDKzMvgVhfU0zdcdesinR9c1IsgUirMh690XJwyqjCHMOv9I5OwdLGoCe7yRQZriFxGmvelw2A8eRh6SmQifkNnQx3J8rbOFRtrBhVZZOBT8Vo8BBkfB8CIlFDwrhc%2FX3wWPYZgUS3gyy6ufKKOOHc3VcdSx7Shgje3tzmBxLJ7dyrco2b%2FrnJJ0Zf2MJLcC7FS1piqvYouAbt5PuDltVqin7ehwin1MbYg1MacvIMDNRIso9JYVWdL5vBx0VqjVIqLc2cocf6Dud1uPmsNOrkKOZ2aOr3%2FKXsAp92TzT4axpu%2FzBnrA%2F87dP%2FqWoUhbOC6LJjSZGBzk%2BONn7kO%2BHjugXGEEQ7dWkaZUrn7VddpuOcqMaspkW%2FN8HMUzHZ893jsk8G5ML2DFIw1N3kSx0BFokQOiKNn8WwEkhXg1lrS4hF%2BZyiPfx1UjMpKL1iOhQsGALgkH882SfTYGkrH%2FEwk4SJvQY6pgF8pubCeQX8YqII86WOiVwIy3CSZafc%2BRgwAEC09SphZBpxrV%2FxbwCAxTrc2K47B6vbyPJaqzpgC7O2ozxJiFF6EUGouE%2Bg2X6xMPKla2b08quHzUT6nYRuyKbb5sLu4BcpL2iDZZKErXJd0x1EY8WW2deiStqMamN%2FmoIKACMG%2FZtefFU%2Bhq9xLpxQYZE6ZBEQF6zTshC1qE5%2F1wAJxfdQCytCVTuW&X-Amz-Signature=690e0ced6ced71af2815e5b107edd0099343326e09fe391d2822346400b99dc5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
