

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=65fbaf5bd5ab27dc6570d68af164a6bbed10186c0a584e58243d87cebb245a28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=976f922738950b72e45267804f52601eeac12f391d645a4308f3877ec0679710&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=75742011caface29122181382504e06f83b7565f6ec98641d15b16ccec5ac7d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=fdba0ac1c22b35f512ce01f1e9211da64e904008d1a10a106a96b69df756c04a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=8237bbfeeb0619ba750f62c131fbf13106a80854868b4377f9a2a2b9d339b52c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=57e67eb2533ed71b2267f3532cc9402452c96581b3064afa0a13fadad517643f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=239752ebed6ebe227305268224dee3e24b27dbbc5f3421f59eedf15f0f68a5d6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KIMM2C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCn9bbXFa7pC98%2Bgii4cPSIoSXKg%2B7MNbV289WpBC3q3AIhANB1%2FUV88nQX4fGFG%2B8YtO2IMbg6BCzrHXL88ELMwR0NKv8DCEQQABoMNjM3NDIzMTgzODA1Igz2og6UbYkGlOtuWLEq3APQSDo6akUP7YJtnGcUoUEXR073evqDI5OTcgjIrMamCCT247MRCpKG8uYN79%2B1n9u9FOUE2LjnpIlV1Y%2FrkvP4D4fVRIjvDw0g3P8u%2B5L1PNIRfRZUA1ZBkrjyNm6WvWABgbdmx1bmTJUZddviYqVtGqkdtDCjmbktRaOvRGaq%2FbG69tXPfnKI3fxKA6pBVKBrUunefPZwZxsPdm7SVRQc3tFDmKTxZsxoKedoBid16qjJRMD7HM9BGErROblwYSMXwTGI2oJBolo9hqcuPtgacxg7wmFZc6dAxnhmpHvtpLt4ehjyFk6uYpKjK57ug3r0IuRH3OJdRplpX2ndoWvA2S%2FhByUsUg4RO3YYWSTTu1NQIgjZTB5p5qY0WwEYKgu3KwOYwhWV%2Btybw0nLNJ6P30H6CyqLMpTcUdEsGE9ML6s%2F%2FOkPpKUQU7fMFVlZjNaKp%2FfmvKmqnUUFYxdkqzJl4%2BwJIb6hkI70kjuE4zmZWAeae%2BfcvxgPjcUPbUPKzgbUkHggfdeERapLDyt%2F%2F4DoTBipc35jMC05geVXJaA4jmXS%2FAtXiowTsWyQ3N8QGQIgV2yWt0mIkrxDH8Tgr5YqC%2BIv%2FEsX9Vcf9yzd3OVTTp9EUbrS%2By10EI1xdTDyio29BjqkAT3xZCSrvEoe7%2F75d8vsVNRt2sTSGJD9D8%2Ba%2Bi5uPypV585plFy8AJ463BMBA1XW78d%2BxTzAig1aPKhoh6ICe9KSoY9%2FG%2B6kJqp%2FKNv0B45WQrxNAd2gmX9l2ECAukhE3XTB7ltLs4jrlqZWg4bSzyAzz%2FzbYbbX1K9z6G3wHOtIAgaep6uflo1tuMHWS14I%2FR%2BI%2BLn%2FTr1UY79nZXM4SjJjNM%2Fu&X-Amz-Signature=5c6f8d5daf099afb19d4beeaa211f9d196297bda045bb38bc66ce4591242a236&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIYBH75P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDSHcF3mUaLzNUd4P%2Fy1Edm90nmgax3quF%2BHs5p8RbqrAiEA7cX81Kp%2FMKPo7kc1g7sc3nBxoLGEmK8QrjlfdXlsmUYq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE%2BgTtGHAxyH1iSGryrcA11T5%2FIgYvKrFLC7PIslz4GTDNfjj2Psr4ScBr%2Fn9%2BwHRUgze%2BASEHf98pDtPg9BrNkvcgGG9PxQrlPc5yOvluX1%2FmI1342PV3FT7alLfH%2FbAlTF1PdW8zo2g%2BWICEzOg9SXMTNqDdC%2F3XJJ5z6Nt%2FS8kCKcrC0BG3jn%2FQg7AHBz%2FPGc%2F2BpiErEhZnryRlxYKtk4ryCuNaMNa9Jl8eldmp5ahBZrBjgrD%2B9fLz8QWzV3RR9NQImMlHyeEnYa%2BloqeMyEWyTYIhKKfKCQyv4CTGJrVJCZLZhoI4xStkd8HDFaR8o9zKubROFibfhvFhARoWP%2BF0lHrI6Zw4tlzKga7YzNZrAivvU3WVUsdvRtu4iwOOsxmt124iFB5GpYdmj5ZPywt4cPWD4LJLYlPQ%2BfDKs6brqZujrfZYOc1CKroF4emm%2BPPF8PTJVpj5zZleSYKxzw%2BSNIojULiWucpaVJo2MIYFeJ5xdqEr4Gnj%2Bgj952tB5O5EtrUzcrFIup03wYlhP86Osz1sLhlxU9IrENiWtV3ziCQubdGcAU12g9PWwX11eyparjQufXbrAOINJtitLp4L2VFw8xdHGsv1nqxFi6F98iJNXR3mAGYA7NWAb8Gmha8%2BW%2B2g1kb03MKiLjb0GOqUBHC0cnITDeVKGLnGgS4TpFSQ1GNQYSukuCzDaK4jh1NNgFFjmypk8f7lRRz8EodjbYMcoGbftABgxlI3MUQQTc2rSpZqFGCQHw9hdXe0TLPchrFUG43eRf1huyHwNCHvkSateMTUfGfmHN1rN7KGdL64L8%2B8vDC4PWuf6ZJbKM98ZnIZv6F6teiQjk4NYWO2BBjwtMsLy3Wp8DTCOUByFBlP5A5ud&X-Amz-Signature=d3773c3cb8d9dfb2a09d270075a106823e874dc969431b04a8df314b4717a8fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5POJECJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIHhZbCm990tyi8WaIaQ4AoMA8a5CBsz2U9U2WzpxgKRtAiAk%2B9AQlEWNl5VHcp%2B%2BwW41BgU2aYvDNkm1l4NLggD6WSr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMD2I8IwNwO6vP%2FIxkKtwDir0He%2Bw%2BEPW6XNxytZyNIwNmkVLFtrqzfP2%2Bxz3W2EunYtNCQrQmnV2VKhvWdCFJ3QpqPObE08HEkfljJ2x6LH8WupNNWJSD60nkMreGuWuxjC6IhQjYPJe9auuUcK%2FytWWGcD5D90KS%2FBjpobyPZF3GIjEqVt9MW0u02aJaBPK7GoB4HjHPaxGk89fDWmCw%2FdvoB1MDHSNcSmEe%2BM8mY1tyYxQZoTVhbi6pPEzsE92LYlOUyLWhIBj2vb8LK8EWpT6jLZeEuVHRdSx%2Bu%2BH6G6c7Xl2mCpMZCAbhwBdLTOwmnqzk2CuB6im7ZMoJxVX6q2OWG599a52ten%2Fd4t36qQS18TPB84KNW8VQass4LTRTmJvbe8pSeqvUFEDqVBwHlcs%2B89cK%2FXBy53A5n0Htkh8g6eyfVBG199ffOWifG0T45hO1u5AcFa%2B%2B7P31YxhZkvYbG%2FoCnsJihrPQBL85oyQI8eCe4hKlNP5H65yO2hOLK%2FG9vO7KQdgXg5fVtitnnCRG1xG8nnFUqwz0FOWa4i2ZdiigW78kb%2B8rXN%2FmAkABZg6dUBWQ5%2FGeheq9xdnT%2F6ZMUaQzBDiH2IClz3TtwS%2FOzbk1K2G8WZDCF0mz1xLu2eKKu2t3GImCP5Ew%2FouNvQY6pgEtkf3uorpD3lVp%2BUHZMU2tEl43b4K7981AtNQaWZMJuQQxgo7y5E7vgt5sLxo6u2qn1qTODrvx%2BTvDfp4ZRrrbFC5fYoKOm%2Bt%2FyO%2BifUpCdYN40jHkTKfLjU1Ir9hAk0m9rRKA%2F2FYPIEV2s58F8nYofEg3u4a5Py9auTmDSavWXn3bNoBwlMP9D67qNSUQQ5yKtcMR7JmnIzFp193tBOJ5kd72UHG&X-Amz-Signature=e03f5fe32006f8dd40b5d98f6750ead2825e69112a629ddbdd1469559471e6dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEX4S2W6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDOEKuMBmS967bFjY%2FJh%2FCNB0aBZ0kc7WalwZLhV7pggQIgGMo9QyhTLde68vmkvKFUR%2FqsyqTU7F9djsfCJAV4%2Bpsq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDPb2AJtcG6eVaqsVJyrcA797xm2Vmo%2B7arxvf%2F5wPKilD9jslR5b%2Frrj4SjyvyqN%2BnxEHN8C6kBc9XttmgonJNwyLrHVX7jx7PkfG2R5XJku57Rno3RqocPr2uEkznwZnsevsODaMAU1ibBJ5yscR6vkbSM5MtDpcVMqDfqckMiISQciKvpbMDkzLJ2xyjTaa4TmpvA2s39CamRZtqyNKa7CUgAp7LRzF%2F40Cdmotn3BDbQzzHtzIaKV9DFJovCmBIGvcAyxb7Avso%2ByUDCRRkZPPduojL6IsfDsVsDypQII19deS08rTN6vO6AVd8clpRHFzKES0ddB1JWl0Y8DJkDKVJYSXc7dm76kXsjVKoMC43qA1%2FzMFJYKPGSzS4HhG5qyuTKUPIWfIiQtjOYHQNyh2JzIUqqsU4XoUhWca7jEU50SqlwM3o0KxNr3%2ByBUOA2NwOQJIOK%2FIn5Ij5Ts0znbswowZunDwwLxhm%2FaHmcAT9khgoenRiyP1xrgmBlXab71rxWRbcFkJNZQz%2BUt%2B5h13B9zueN9wjLFA8skeQMe%2BpiYJPasQ%2BTG6Snkd%2BJamCXG3zN7nffEkmONXRB3jgWIaJq7DHNM4JlTFSWkykACjh7DQLYvvLpX8JKC9hzoNQTucFPuAfO2f6esMKyLjb0GOqUB9M%2FoXifIMiBsOdyEhPk6f72J00nhzDdl6ZzMyY%2FnYxDKkipsXUKfuaXE5bUhnZGemrm6Bo49BAnf62uVariUJT%2BEXqonWv2IXXgSu8VXXwGLihmSbBi68lZpMFnLtrgZp12NUIFYAKPtxZExkwhJvpG8P6MbnGxXUYXaO5BqUIP9e2498I9IAyKGjtFYcfmYguvUZFdTPTMSBSBwTHlxfzGr5JHc&X-Amz-Signature=7f2f61abfbba54860bee4585e7ee4c28458770f81ef1de3ce0e7c150dd80222e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEX4S2W6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDOEKuMBmS967bFjY%2FJh%2FCNB0aBZ0kc7WalwZLhV7pggQIgGMo9QyhTLde68vmkvKFUR%2FqsyqTU7F9djsfCJAV4%2Bpsq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDPb2AJtcG6eVaqsVJyrcA797xm2Vmo%2B7arxvf%2F5wPKilD9jslR5b%2Frrj4SjyvyqN%2BnxEHN8C6kBc9XttmgonJNwyLrHVX7jx7PkfG2R5XJku57Rno3RqocPr2uEkznwZnsevsODaMAU1ibBJ5yscR6vkbSM5MtDpcVMqDfqckMiISQciKvpbMDkzLJ2xyjTaa4TmpvA2s39CamRZtqyNKa7CUgAp7LRzF%2F40Cdmotn3BDbQzzHtzIaKV9DFJovCmBIGvcAyxb7Avso%2ByUDCRRkZPPduojL6IsfDsVsDypQII19deS08rTN6vO6AVd8clpRHFzKES0ddB1JWl0Y8DJkDKVJYSXc7dm76kXsjVKoMC43qA1%2FzMFJYKPGSzS4HhG5qyuTKUPIWfIiQtjOYHQNyh2JzIUqqsU4XoUhWca7jEU50SqlwM3o0KxNr3%2ByBUOA2NwOQJIOK%2FIn5Ij5Ts0znbswowZunDwwLxhm%2FaHmcAT9khgoenRiyP1xrgmBlXab71rxWRbcFkJNZQz%2BUt%2B5h13B9zueN9wjLFA8skeQMe%2BpiYJPasQ%2BTG6Snkd%2BJamCXG3zN7nffEkmONXRB3jgWIaJq7DHNM4JlTFSWkykACjh7DQLYvvLpX8JKC9hzoNQTucFPuAfO2f6esMKyLjb0GOqUB9M%2FoXifIMiBsOdyEhPk6f72J00nhzDdl6ZzMyY%2FnYxDKkipsXUKfuaXE5bUhnZGemrm6Bo49BAnf62uVariUJT%2BEXqonWv2IXXgSu8VXXwGLihmSbBi68lZpMFnLtrgZp12NUIFYAKPtxZExkwhJvpG8P6MbnGxXUYXaO5BqUIP9e2498I9IAyKGjtFYcfmYguvUZFdTPTMSBSBwTHlxfzGr5JHc&X-Amz-Signature=4ca1b68f6fd71d4b36d25933717f228a3690e72ae39fda4c1b40b1193ca5d61c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
