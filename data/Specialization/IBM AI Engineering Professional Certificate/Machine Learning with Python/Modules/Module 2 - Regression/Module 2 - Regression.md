

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=9e997a705ef49f4997eb8e06d44556b69acdb89612dac2b0c99ca7da8b800d58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=2c63fe680e522267f03bee4eb48e3afed562abeb0b96d0112b643f97781a2ca4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=3d4f2a6eaf2ef856647f6ff9b880c8bea5982abc6d6d06dd70b73ded48e7928e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=1212ce8bf02ba2d4667c045d1e30e7f240d68e4748613ff18caed07202df3e12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=3fca40c0fcbd5e4e3b81a646d0f9da174a7abfc5993985a8de18e16dfc4b5c07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=f6e0a47bd87392a4f47e8a25a46ce5cf1f9d3d616767dc8df9189b49995a01c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=c744a93020c1c55337adb9ec502b36a71cdffd2715998b6a3288649aa8da8990&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=0b545097f2239f3169d71947602d6119342673cbf6a07bb7f564302996f0fee8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCTQ5SO2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGf96eKCRB0ZPkeR%2FyTG%2FKckRVLo%2BIemAQW5hjekIyHTAiAKri%2BnG86XtldTZxu1GRShzvirQrrSxOeeAwY4ORmxeyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3JEMVxrlE0djL5gmKtwDhu%2BMvX8w42C7sN9ceLGBhiTszoMyXqSelrjQDe2bTxs6HAR0gLjLllUA%2BN90c%2FsrAAEXZE6jNC8inUbSg%2BR9%2BXM3Gr%2F42O8XBqb2oSZs7MQDKF0yUriNsrjF0ef84OEcNhCb0BApnUv7AawiH0bsQh%2BiARpY%2FZMamYXw9OKP%2FWn7kxf2Yu%2B%2B0uLVOMDIQ8S4%2B2QYSq8YOSw6ZFI7kipQMqJ9Joj1Zu8FhlssSqCPKI%2FxeRFzkA3m0GDKrsVarz8uZIIEYX9bu2sy3XNLgWwYdDsnr45kqcDPMYfbZiubY5sW4ZylHJAS8%2FoErF9jscTS8xdrJ6AdjO%2B5YxkW8b49cEumCSnO6W9XMqULweL1mwTxfM967z%2FkDUOmIq3X%2BCRYB2y1aMjVtG9tq6K%2BwGFhWcA1VqphgbZotFVJFQ6ET0erKBweFT9jMljAAXW0jhlH2Vf8U%2Fa76NXxafxQQ1%2FUlMpR6lamPoRBY%2FDDGY6oK%2F0yx4oG%2FHgMaP7uKqS3u%2Fkw8gRUbrSDui41a8EeH4FAIxpo5x8UotOmGqFTF9iNpZSbzlcAYmojTdZ3ha02c0gnZCWc7Djm9V4lOTYHHHheDUIiXc1V8DQHnntaGVnyRVOWqjHNyI80Y7VzV%2B0wrsfnvAY6pgFicsrVHza5rZx6RErz3gpl7ZqVui%2FKCk76eG1tpShjt4tPutmWd5TElBhikt7tLm2h4qWxD7Fah5%2FNO5oNm2ccA3RKDo5q1qR7oIJh47bZvsOgo1A3XwO0c7EQmB%2B1zZ3ThPq1nf8reWZj%2FjPQLCB9X%2Fjqn0GRGq%2B27ZweAEWgbqY7Vq%2FStgDOFRTrWhuOe%2ByDTva6mVpVTMYaoOoyEAOfKBMZwNJT&X-Amz-Signature=fee81dfcc0b8420f4d81ddd51d30a56f649cf92f9aee19a20a3482ae777f6717&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635H2I4QG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4HQqEtjj688Lf3vCFszqpriNNqctXREB56ys5xfTPpAIgMKYF55Kp50KAf8sDR99FPsvAapxbwBdg4GpDJ%2FnBk2EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKX5G4oTuGj2qloNAyrcA8S5FsoQKJRkWRiKBFerFIu31VqXu%2F5krJHIRlSBZHcPPP%2FErve9C0qM8rowGa2N0Asfa8ufPTBfIG5ZOKSuWGr%2Fpt1mG%2BTKKxbwkB3nrArGKAY5p7xlHTKL%2BXYOx2nIe6FD7KddKjfCtT6WGgX88yhb9Avj9PI9EtdBV2nQD%2FHnxeuflTlvlB7p4NUGh4AwZraJJLJlQj30oa3ZzRQ2nwXpOCCHuZLkM4d%2FNTvKnTbxWtd%2BF8Ks8rDewJomalP1YO221HG6UYjidSBJHMng%2FkYZ8E5F5BGIZ5Gr7qx9loSVIP3UeJgxj%2BcEFK5kHfyeWiOhqm%2F5cZG6zdQoBdr5WeT5SEGck2LmdMnIlrvOFMWba42LOGBysV3RCzEsjjw4KmmHD15iZ1FLr0N3uHJjt2hLcLV%2BPCLgqQh1LLfNrQsaAPdQvdkfKz9jJCDeCXoQT18FEiCCfqaRGQwkGrIPOj4gRsGzVAZvzMa%2FWGenoIAvbizgil1NA%2BFOYwEpZAthKRmcoDNTmotFvOMkXKsiRvRAgrjl5IEj%2Ftg8fSjMDVkuln2WV6arPdERcD3Ee1wgvhgU5sm0uZHqzsV9nOJHMdoR4rlgcrPwJ2cMWfOOhpfYTkELSf6ZeQDJq5OHMOjH57wGOqUBSQAs6Gb8SReBk3y9j7EZgiGOs60UrRRUrdw3UwLB07XKP6V3vj7kxif3Gc%2B%2FSZyYD7H8LDg%2F36m%2B5XiQj%2BOAR89SZQFcmtYAcx3vTzDsDXsJ77IdNUuJXsk030gfoPu%2Fgk8azN3dJO5q%2Fi6mF9f6K8oHPjMWHiBoMKZP09ovL%2B6BIj00s5mktYs0%2FulwfLIT%2FUnc8lD06CHwn95PWZFjFx1eXEab&X-Amz-Signature=4adde455fcf1893570703539c2899fd6c5c1253188dcc747d9017bd962a262df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DSL5SSQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhdBmqQMSMMWpm1vLdVK7VigC6l12GIZc%2B7HbEvapN6QIhAKpmiiPfcGzkNzkkjuBJMoq4G%2BOVf320nI07BjQtAJEvKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuV762Otn3ynx3RwEq3AO6gJDWMerxXTNRXk%2FhyQCzCuvgIkIpXj5mdnWrkeAKKVYlKwEJRtmfIjl841bLHD32ctaelHH1Tndm%2F4XN3TMKp8ZkKMnN5Onz1kqJzNv%2FdERHNF4Q%2F0RqXgvOkaWlY0JFIlBc%2BRJjSI2BU0aPFghewBYbFxMO6jGhUT2dOUsYkAba79h53p%2FjWmxHzbGQRSdAM8cojGAos%2BRAVe2GEKuciaT7qAe9Px%2Fim%2FJLiH4nzs%2BjCqCXeDLEqhZlM5Dp1Ez2BQwnCJ20MvPR4dATbqfe2kJuXecGQypO4A9YU%2BWU%2BSswieBZn3ZMgrvIm6wYBHkbOfgxU5WL8s1lfkaK3LVorW029jx%2FgtZ6EJzD0G5PZlK1D63qqscLMtxu0cbsGag6V17e3OgkNsjISxtiUGOuSe8hQ3MYPj8rS2OpIkPOcRs5r1B3%2FyKdzbDkvLi%2BIAafQT73Yw5m%2FijJhjtqJb3HEvXPOBcGJdJuOYkWr2WwszWkF7RzpLljnF7EcW2a8IEauzC9i0f1VZmPrkMwzYkCamz7LwPoZugCLdeWmS2RE5vZawm0GMHRI7qrK3cXLm11%2ByBbE5%2FmosjzxNOFqYDlxqzHqGFcv%2BjwGx6FFDqXHKuQytvXvi5DuaOVXzDCx%2Be8BjqkAeQx4DHTebprCVYF3Os9rCVQqCf65RmQH5QZnjSwP%2FzZnTigfejlgKIisl6KrTAMeUdjBY6J7p2X5xyAYQFF8n9%2B4uRO9IHlVVV3Nqqb9YpoloSdLNoSB6VcNxvJ35inaUyRD9%2Fi2e2YjfL%2FyLQyPWRIbVn2JFu%2F1I2naxXpVUVnLKp0VEPWx64B8Y0ZZRufdkMx7kCchG0eOAxCDQE0C4ciYotu&X-Amz-Signature=72eb4c63c01a4a6900ed25977ae9c50b29ecdfb08fd5414955743e915b4db805&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DSL5SSQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhdBmqQMSMMWpm1vLdVK7VigC6l12GIZc%2B7HbEvapN6QIhAKpmiiPfcGzkNzkkjuBJMoq4G%2BOVf320nI07BjQtAJEvKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuV762Otn3ynx3RwEq3AO6gJDWMerxXTNRXk%2FhyQCzCuvgIkIpXj5mdnWrkeAKKVYlKwEJRtmfIjl841bLHD32ctaelHH1Tndm%2F4XN3TMKp8ZkKMnN5Onz1kqJzNv%2FdERHNF4Q%2F0RqXgvOkaWlY0JFIlBc%2BRJjSI2BU0aPFghewBYbFxMO6jGhUT2dOUsYkAba79h53p%2FjWmxHzbGQRSdAM8cojGAos%2BRAVe2GEKuciaT7qAe9Px%2Fim%2FJLiH4nzs%2BjCqCXeDLEqhZlM5Dp1Ez2BQwnCJ20MvPR4dATbqfe2kJuXecGQypO4A9YU%2BWU%2BSswieBZn3ZMgrvIm6wYBHkbOfgxU5WL8s1lfkaK3LVorW029jx%2FgtZ6EJzD0G5PZlK1D63qqscLMtxu0cbsGag6V17e3OgkNsjISxtiUGOuSe8hQ3MYPj8rS2OpIkPOcRs5r1B3%2FyKdzbDkvLi%2BIAafQT73Yw5m%2FijJhjtqJb3HEvXPOBcGJdJuOYkWr2WwszWkF7RzpLljnF7EcW2a8IEauzC9i0f1VZmPrkMwzYkCamz7LwPoZugCLdeWmS2RE5vZawm0GMHRI7qrK3cXLm11%2ByBbE5%2FmosjzxNOFqYDlxqzHqGFcv%2BjwGx6FFDqXHKuQytvXvi5DuaOVXzDCx%2Be8BjqkAeQx4DHTebprCVYF3Os9rCVQqCf65RmQH5QZnjSwP%2FzZnTigfejlgKIisl6KrTAMeUdjBY6J7p2X5xyAYQFF8n9%2B4uRO9IHlVVV3Nqqb9YpoloSdLNoSB6VcNxvJ35inaUyRD9%2Fi2e2YjfL%2FyLQyPWRIbVn2JFu%2F1I2naxXpVUVnLKp0VEPWx64B8Y0ZZRufdkMx7kCchG0eOAxCDQE0C4ciYotu&X-Amz-Signature=a0f688d5f5ce81f0612ed21c87f2bf5269bddb355072b3787249efc130b63499&X-Amz-SignedHeaders=host&x-id=GetObject)
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
