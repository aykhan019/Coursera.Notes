

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=08861390929f38a620db0aa057832d95867098f0c883af656ff1af9e7f509d27&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=e2ac715f139527f68bdd86d3b9c1330208af88014c70a46af06f0ea91c003161&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=ab45fa0a9d55f2a19d062e355e8d5c4f15556b86dd36588bc2e41218cbdd10ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=504e1d65e1c38208400705f799d65346860c32ecff9e70ea7d3e7e9ba7c09f5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=74c375ed06d868dd8c3ed4c649044dab0fa189da4cfe4aa59e344111c8106935&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=571b8c973cabde2e76098235b9eaeb854cd9afb62bd2dce43514db6b79f19442&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=dcd843b18fe0755ec11ea6d21ce94b1641b056baa2a41ab63034f7240762c2b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZTKNEX5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHjtvswW4NmdTZNosgiEw4hOJaepNhLo2SHv%2FF1IGMs9AiBDYfa1HcIpFybe7wfc6xFOBk5jHs0%2FZuAxWBW%2FNrI1FyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8a0OyiDRMTZIbpXhKtwDp61jU%2BkQM7I8kxruAJDa24jjiXY5cDuF%2BhS1%2B5FM3iZNvrI8dCp%2BoTzVd%2FMjVkDNKd8k9stgSY%2BTYf%2BpVGQGpMbODMgStC1wMfflFNGrsrAT%2FHvky%2FGdqNdypucawTYfw27fzwKxbufonuSBh%2BHU9yyO735JWQ51SrNmTptknA%2FJIbWC0iZoj4uFiDKqmTzUGfU9JGRLCGBGRMDLUO7WW5tBmhCiI0ZrmmN6f6SCrlxFRGkd3jEf0XGef%2BhVoR3EoNHZ3mV%2FleV1%2FxceUgrCRpmRjR5vTM2L3vTrwKPylywS0MsAtbxq70SRn4uyg9j47F29L4vfc4XrouR35pcYCNt9cktMKKOGOG2EV8yRyCMPvaVFTVGkAJ66%2BMDlTYitaMFl%2FsTITE8gWfX5WeRSf6ttVpBpgicW7Q6kAP9v6OdxG7KHCRQ5O1MX3rM5YhMQ6QMn7aZjwDQeVhmKKCXMmBSbQ45v7xd5QAPpMNpkhglWVIrzdW3rFJArFkj1%2FieATKDRo%2BEUAuHLVO7gnvGsH8DJH57yIXhC1w3IQZAJNEc8tUU1ZkZGuA8Lnq7XfLoTKkPeVLCb1bgVAiNYiMgWHYhKHPe%2BrwLGZ1ZoI0Dwf5VRsjcLcFE0uVCBNacw5qT3vAY6pgFK9pqkDUVnnCfF6W%2BL2b%2BDeamJe0kfx6j%2BMUk8kZ4G8NePIFHvIoM0PozZjIPpJIDRmPe6SvuNd%2B0iTMVTejygytqse%2FW3lD6HJcgOiECt%2FOcR5iRy2%2BI%2BKKPTDs6nMyBQDfo39370Lg8fl%2FofKmap%2BEGetqWQXikj%2BZmAXmNLQXS%2FRg4M7gWfVNjsEeO6KadHEO%2F6Yw%2F5XRQ2dsJlFeiFgyy5lPFI&X-Amz-Signature=9f6945793385e6d4dcf38c6ce06ace1eb0aa2318dd2b90acc1db1a61f353d293&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKABDKZ6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJFkqvOLtIkOOQS2%2Bhp8Hr2j8BWCv8951G%2Bfduvi63vQIgCi0rS1qylS2uXO7AIrAq%2FtP%2FBhRCPX0Z60x7sBKNulwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4vDmYt9sx6UUGK7yrcA2O3n9Mak9ukV6FE78spb9w0%2FikbQg1LhKbAjjIwfjcm9wmvrT1x8MmXqkg3nRlo2FdF3v%2FqJzkDK4ULDFpU4naqBCkllMP0jV5xjIgjH9zCNwr4GybV8buCZeSlrf4Kospp1kY%2F6%2FsdFh9CP%2FvZUGtD9%2BCQlFSpaMrNMOeB95vuh7kdqiZPahFVYVhVxR3VMY9k6lPlLPcbPa9cRjGnzdKP4Z0XB4f7BQyeB1DzVaHDpuURMid6AXsaeTiQJjH%2BI3CfrYtpMrWJYyXSXepbQDk7R14PHHbPWOLcfZVC1Fr0ydviv%2Bgjk7jXb%2BfUpymlT8kMQTxTK3O6fSnsBK%2F2UTZcPu3rjt9Znf8FVH3Faz9XxE%2Bcv0MfTN%2BNNLIDZWq91jp7NVpJ%2B4CwITVOUm%2BP6Z1gIQeZiMF7hPjLKNtJqKMmH7h%2FJZIwFSHU3gzddVQ4IhTRF19EF4IdSWE3Tkgzd%2F1%2B%2BX7GYCJCPfIQK2fwts80zAiduT6CJ7ATWSWNWHboTLmCREFFjjJOp%2F3dLYD65gZa%2FrEVvzu0uCb80yA4JBDC5CvdBRqLhPvADlz%2BLZz9pgr41M3DcEevoDDtgZC82soMINJ3rk0DuuUWOFPJSrW76RQjyjC93JWaHiC4MLyk97wGOqUB1uv4scNu%2BDJFp6vCSz9Dm0LdLqbg7GxX6ftsX2qlLtNeIdzgFUw11HYW0no5052%2FPv1t3sekgSx4W8jDhrqfEMNP2uQ0qezBh6X%2Bni1zn8M14eRFEY%2FeBf6ulcoddCSkfv4DNo3flyurd4OGBQrSSRE3idHozAD5mei1hWOV23VMRalMLzrSNXPsS1aw9n2RTrBWL79kFtkZGtpHKkogCkDA4fKf&X-Amz-Signature=119f336cfcb88d516d39e783396e11ba88dd51948d7a793d0402efeae5d0fbde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXOIKBPZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaaIi2Vx29eGoFHyybb4y9zfE1f4Szt%2ByEA5R1E9K0PAiBvnn7daPfan08VQSpk%2BUAC6UIyhVZkP2drTxbAJ%2FY7qCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEOKXm57n9oo5JzWNKtwD6jSRX7JYhzTtumOruiwUhBidN6U44RAS%2FaCv5%2B8J3HlR%2F9mUYmegi%2FaRyLWL3RSsywK6Kv9kYc5GgNyHC6nL7CG8i0T46T8An0A29vEf8P5F2ZmggQhSa9LeQhigZBCUg9CGPVFJd%2Fm2IbmvPGaJXZXeGbmlMG73qQ5JrIhRJgADwOJA9J9Ev62wwwvOo0RPNxOUDKuX%2FbND8%2FJL%2B%2BGPcc0cSLnUyFJ60zsRciQVO4oWb5AvvnOqV5YNE1yOl2hJvBrXabAusZnzhi%2BAPuleJHO1afAKPxAutBMZG9Y5%2Bm0VZmrvm8uS8qgE07%2BBLzz3KFmQdgD4AREPNl5vz2JpycqBiFEc1NtbEITjutkmU1C1yTMUla%2F1Sq%2F1tSxQjtX%2FYaA9%2BE5qit2MY5%2FUAwaRRMRDzU4MLSKOBijcuok1ntk0IwbFLG8xmWn3khYtLKVUfW6YhSPNcRuMqdsEnmMIqb5pP6OP7muTGLwl13rrrrFgZkNIIbeIk4fTtzzIVzd%2FUMykKwrC9oUpJ4gEm416jQGcb9GzypTY9SwegBH0bZXuZno1Z3hyCBjXZ%2FBe2ZQ4IYvmKvABWsTaDbo3HrtaJj%2FMqU6ctnhk%2FEcLlV%2BjHmZHlDV9ufWyA08NmEcw%2FaT3vAY6pgEfydbkG8kTGBbU2vNfUvI%2FxTc0o3cwklZRnsMZ7un%2BVNf0H0he5t0%2BzvqyvvuiYDPsEZgOCC80oyNVwmPFer8sxb5xIJLBSzEuuHPOJh7EgC84FFkoszO8tb86CfeT3B42qQEGZxEYAYyfrXPm2iExI8yQQpqZd%2Bj5kJ%2F9cGtXHxJtMi9ksNpuB3WPEvnM90%2FwSJi8l1q8RdjEw%2BAAcPUxM45yDLmy&X-Amz-Signature=032635d2d76c417e874c62d91289acae6a85e3d3b822bd33a8d15e06f8f2f865&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634UY6DPR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsDOVM5vQZ1ooQeeTB5TFDE9PlNB9dsM7IOif%2FJXH5PQIhAIn0bTzNt7URu9IcRdVm0mxIQFR0yVv3rLalXpwB5VVXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIr5w268PDG%2Fhv2Uwq3ANr91%2B43GuqxmTA%2Fz%2B8cv5tHilkxKyxzNI4qmLBlyyZzDFfGvfio%2BoVmkyr%2B2WpV5ukALHRR1MvN62fSVN9XDhZtS9f5QSYunff9DIeJ%2FBJLaijwunnp22QnHwZviit5tt08ZYZDkrVaC1kVZDpiAahm18seoVJbHyQ61iUpuj%2FoDyAuU0XIaQC%2BcZ5KPOkeGh8BmmXDpnFyQoGPH%2FpMBKo2gHeS4cu9CBB16noDDjJ1r4zmjsz5tWwOLkgvTmIak8cSwyEcJQtlnFwaXIARDA%2FRncfqK83drmir1DaMDoYs78ZGRwqjTG%2BbtADTCTLv0VM4Jjbdz1ESb0JGRDff%2FzrFywnUpkitYxOa81evk%2Fxkkf%2F8uvASrfx4ZVFPWvStir2U0VJqkX3qQmyKOg7KhRLwlrduiv%2BErAsFUciSJIPaTqyjKVQ3OwHc7jhq17rjv8x1%2Bmoubs8oiNaCb6thSK9XBkW%2B9NlkkARMRc4V5wL6%2B4SYnDDMJTuKSgemnxvlH56zTXGY701bxloCQhxdY1Rt4AkYxRM1AkbdtefAyFXQDAWndIYl9jrK7eQQQfDz%2B6LQZwaWftU8eY%2FlJhOWIAobJJsZDNgAbqVJi1Lkgg%2Bj2mUaEY5z3jt4EDR6DDmpPe8BjqkAWFz%2FUOMN9X1pXv2SmOYc%2BNuainD9KmsOxu1SQbziNZ4LakH95ozA1QsBe84h66dP%2FSWKM1N%2FCKhNKDWQTQb0Gb6RLszEKqRWhjcK2utTSLRIwR79K%2FSupnH9S%2BqeoDnNWGQwegZzPQDgSXP6wWxVrhUmcj8%2FOKuBUMc28PvhdzyNKVhwEnr0jklFu%2FpZIUHJpAbzBBYYm7dnQLyoykFXEYRWacC&X-Amz-Signature=68a4c1285052841549eb74314e450a1e9a2151b6f2e6712503c7f897529ffe42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634UY6DPR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsDOVM5vQZ1ooQeeTB5TFDE9PlNB9dsM7IOif%2FJXH5PQIhAIn0bTzNt7URu9IcRdVm0mxIQFR0yVv3rLalXpwB5VVXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIr5w268PDG%2Fhv2Uwq3ANr91%2B43GuqxmTA%2Fz%2B8cv5tHilkxKyxzNI4qmLBlyyZzDFfGvfio%2BoVmkyr%2B2WpV5ukALHRR1MvN62fSVN9XDhZtS9f5QSYunff9DIeJ%2FBJLaijwunnp22QnHwZviit5tt08ZYZDkrVaC1kVZDpiAahm18seoVJbHyQ61iUpuj%2FoDyAuU0XIaQC%2BcZ5KPOkeGh8BmmXDpnFyQoGPH%2FpMBKo2gHeS4cu9CBB16noDDjJ1r4zmjsz5tWwOLkgvTmIak8cSwyEcJQtlnFwaXIARDA%2FRncfqK83drmir1DaMDoYs78ZGRwqjTG%2BbtADTCTLv0VM4Jjbdz1ESb0JGRDff%2FzrFywnUpkitYxOa81evk%2Fxkkf%2F8uvASrfx4ZVFPWvStir2U0VJqkX3qQmyKOg7KhRLwlrduiv%2BErAsFUciSJIPaTqyjKVQ3OwHc7jhq17rjv8x1%2Bmoubs8oiNaCb6thSK9XBkW%2B9NlkkARMRc4V5wL6%2B4SYnDDMJTuKSgemnxvlH56zTXGY701bxloCQhxdY1Rt4AkYxRM1AkbdtefAyFXQDAWndIYl9jrK7eQQQfDz%2B6LQZwaWftU8eY%2FlJhOWIAobJJsZDNgAbqVJi1Lkgg%2Bj2mUaEY5z3jt4EDR6DDmpPe8BjqkAWFz%2FUOMN9X1pXv2SmOYc%2BNuainD9KmsOxu1SQbziNZ4LakH95ozA1QsBe84h66dP%2FSWKM1N%2FCKhNKDWQTQb0Gb6RLszEKqRWhjcK2utTSLRIwR79K%2FSupnH9S%2BqeoDnNWGQwegZzPQDgSXP6wWxVrhUmcj8%2FOKuBUMc28PvhdzyNKVhwEnr0jklFu%2FpZIUHJpAbzBBYYm7dnQLyoykFXEYRWacC&X-Amz-Signature=2a122d8d11ac7ecf8ec042a6b84bc60bcc3fff626ff02540028d20dc46697bc0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
