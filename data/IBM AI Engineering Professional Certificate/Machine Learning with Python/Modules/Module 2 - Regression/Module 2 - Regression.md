

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=c28932ed77758506206697035db8c788f33b94151497fa6ee3e845f9c8c9ebfb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=12862cecfc5b8e391b04e2332724bfa891f9f10116a26c39f9af34d1da0344b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=ea85cc97a3b4ee755421380f829bfd192b992f13ab8f5dbe349ef543a163d0d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=b031cdc21b1b04c95a147d45c8da362e90af4e881fbb1cea60fef9e8b3db44ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=8b3313404d4dd3ebca79b3fa331a2e47dd21c733bd36de65d749291a4d20c3c1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=81d552c730e9f6a6a405a6fffaaffef5c8fdeeb528b182c1084a8cfffb32117d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=5fea00eb3e90313a7bad23dc9d6d2ceebf722e846439284c6cceeef5e0445bc2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X22OR5PQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIHnsM6xwjUeTJ2pxReCP5sGCwcsxDMjaGZMD%2Bn4%2F1PzjAiEA0W%2B0o6Zw4kLhTHx03jbUspVmqsXsHAvL3RzORIlQd2oqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUrGnxb47CvHQd1NSrcAxD5tAb7StY%2B3yYjGVpZPCUnbSI7EdDDJFH7I6kAD37DBy%2BEUTlZW2FNwybgVwJya1Sd%2BA2ndUFZ%2FozFCWgvuRJV30TxAKhAsIWTDiJwy10T5X4m7nEZUCadJ7iD7MCNivngaOhrxdD3MwMhHrhiT24rs2GyIMesQRRUsSUIM2aYsIf3R31KiCdxVeknRpKld13FeM0QzsKPeWKJ1UsGdnbt2zP%2Fd7PiWSPWvY17eXYrCBfePYQpvSqZ9q4LKq6qiLslsIJsMUjMAeTOEX8NRtYUsFo4VNjsoYDTH%2Bx16NulmgrYImcUUTVAY28QlzM4DR6yrop0FaABxRwAGlRTRLVqu0J7WL73PD4TdMPPLhPsArIRxqpmgVwdA0%2FoREG7GwYLJZZ%2FtX%2BlYPFU7v%2B%2Fv4Qqm95KV1s%2BrrpkcQvvqXZJD9URCZtiYMoMq%2BFHUaHe9xaYJhkNojUFjbkr%2FY2UGl32GStE9Yf9%2BMlAdoElfWlMPSCOmzcxyIfHAvrD7se1GFxFG%2BsL4VHKn91%2BRgU%2BRMXtZZjKdyJY%2Br2UllOuLseRfde8oHmLXYos%2BUpOap1cE9TjM5c%2B5uBpke1zQoWuVwW7Lq1KFrGbI0uNhkFZXaHxKSxMsKeBTvi%2FHaGYMJy%2Bmr0GOqUB%2FIJynEp4rFuvR7Kp6VY3dvnMFQCygpPFJAOCFsyZbRCDLniW%2Bq5hcFy3v2IIekP2zcFfucDNfwyQzXFiFnQXPpqudo6%2FYUVXz8aTnPQMFZITM7DfF3d34K01eH0PIy5%2BOTzBdT0vfl%2B86bZ1geegmHU0VVONNBJAvbPexGVqVLfEGc%2BzcfusBA8%2BRg9bMtFFqpFPOxc6wQCiU0WJ%2FXI4gOcHmnNw&X-Amz-Signature=e356bd9749e2f60901b52420c644842dafc68204ea6c0526a9d5f0f5321f2a8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPI4LQ56%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIG3eBpb8%2BLh04W0fNSf5hcQ80cftp7vBsXh5Zham8JSBAiEA9BvlKPMmbYO8yohCzfxCW8%2B0X%2B%2Bs1RPBVVLQ%2BmFberYqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIEzCgIwxa3rews6CrcAwRaVlz6KNPN11nQy9tnbgBuEDYK7gmzu8TdUIRFF%2BWJGF1vTW5AZUsFVS3igGd1qCpzvsxe%2FYXq1Uk8OET%2BaMOUdNVLU9DAeptASDOTwyvKQt5Ellw0vibLNW7uBu90zSC2dyBUbALtcngavBhV0puOIvncpQi96AVKYh1q1OEbaHGi41s2bBtu1dVv6UPdwi9HXkXDdAkDqXhk95x3sl3W8zvP2FA%2FBzwhM89IL4I39fRS4V19jQxTdFTqbYUQlheqn9%2F84Ts7IHfhu9DbEN7flUsBRwjhTlSX%2FviJyC3157nzhLViGasTuHDWV3BiqJwkLhCEBaZ0BOHE6kUmrpUAyl6XVstojHoKEh39pdRb1p7nqnuSavbyAz530%2F6v92KK72x7mYqXZoneDmPVcdobe%2FW1egDmAkJpFXgbFFmLO2azEU1AiCxAZFIrCc%2BT%2BWVu9pT9xIDwK8QBOro26FWbwTgs6sGB6KEYt2bfAkDDUN8uas5%2BNdObPoWctLSurWpCkFennipd8Vtq5jXalDvg9CyiRGUNjdhWDxHMFIOr%2BtiT5AOanSH7vLTUEJgusv1eOho37PWNwilI0W1MMtT9%2BRRbKffMcBraJFCFLKxIfMuXmA%2FysASYNiA1MNa%2Bmr0GOqUBIV1Zlc8wSXXP%2BWUJC%2BXinRLsPPnefrfbAhFereH9DMLlD9EOU8PJJRziIAm9xXi7I3Ksd%2BvIf2Vxqf70nlGSBrXnk6Ni9mw4HyJ3kJFu9tCmCiCY9hwVZajVRCEyZAXgp7SbwY8INDlF718wyKpQ7jvDa3ayVLVDbt6rlBJzdW8TapYQnIQD1kAcOsY1tBf7613T3hKDXcq9RrBgrZKO2UZ2rsd6&X-Amz-Signature=5603edad9ad3553620f17ca7b2dde3addb3d0914892bf5b31f700ce294db8af3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3TILEJI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIE4GflLWg1oPWS1OdCc70D9vUyT92EJf5xRySD7mWPRJAiEA0YYpBF0XgocEtGCFYA7OeKjTZSd%2F5eU9sI1i2IuUj7MqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHVNIFAGSobaOGJFTCrcA7DSxlQWglfXVkC4yNJUbXl6MBg%2BiQTIVb2i%2BwwRjPiVMyM8YLJtC5pMh2jiWCfTDfW%2BqYoXoxH5PsiB6raQO%2FK6h8ZMNZVILW27OALhag5gz6vUynS%2FYajGN3WgfQXyCasMGb62fA2i15GrxFO855Rs1SMSmEvzRskfmF8e%2Fw40qAFeU%2FLOxW6eLnIgsVWhonZkQUjxY%2F9FdJtSNWjXwr0fuD%2FS71VbUYs6FBvqKQ%2BFyA3IOo4PfsPc%2BRFSJMrTorsRV4tywcXQ1M7E3pEM6TY3k9v4%2BZ3meRR4nBe3fKYE7FwZWWE3d1dHJha7rBIsrPDhVLBoGyqq1N%2FT0kqWhHmHWOUAFErKkW6qx30sfOeaqe2Hw3F4I8jktdm1qtRtgtFIP5jydqjX2QbpkifMo5VQWbTJ5nuXa4axkd5QyQX90IPUkUQzBRK4jxNovh5ehHpbPwWKNKDsdProZt3RriwoxccGToMzuuwfRf%2BcK5gZeUHD%2BD4wFFPGzpWF%2Bo5JDqRSQs13xP%2FFgo%2BvD5GiMSICEhwk0Spje2xsVLQv5i5LOy2bVx6zAeSvuGnZjl4AAAA2u%2F2PUHEuk%2Fs0QkDe2Er%2F7cL2TjzAvYcsBUcFbw8sSmXxWsCcRBvsY1yVMIC%2Fmr0GOqUBRMn96OMYk8bS4hxi%2Fspk9Q8F9Vfz3%2FTaxSy8n9PmMQp15HVRpOG5RaOrAjn3KW111MyrN7uXuxf7Sfxj7%2F5gpzdf1GpECV9xsR0KVD84Klj%2FIRcaGneT4Pdr%2BsjqHEgkBwVOWtYyxt7tEuFrwyVuU4QpFaMWrzPnvPmbWLDrsSpRi2TamdlUcc%2FTf6ZQ3WCfvZPmBl3X%2BEe99EV3MtbKcOzr0Xja&X-Amz-Signature=ad6a523e9c7de542f16bd812e4839562d19593100255cd3e9df9bc1267956027&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBYJRQUT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIGVoSrMEtTvCWHGa6NsccGhno6JzUahovjJ8JPE5zQXiAiEAwXfLRnx9UtgcDOaWX0OhqqhMdVhDNAjp6eXXLg18WWwqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGI%2B4NJmdaQi9OvMESrcA%2B6MiwUVVgqFdFZDeun2TeVuzGu7erw5JslcjLJwURKhobmD0oVF9JrN0LoDpFOPhrpNx9OqS4EhnONsAIgY1HNE877U72ZPwwpsnS39yGRzCms9o5hCYfw2omJNVLaMcff4bX1nMOrars4BuK3K1RkC5LslWPCEtc0tev4e0SMH7yf%2BMIjYnY0umpnGPlfBpJ9PP0v%2B7Avv5MtshxPt8TXssVFEQ%2FBKLU7xENSZEAbK5QD297%2BPa%2F7urMwEobqAIdvk9hi6vG3%2Bl7ybdzqJhdkM2ZCHQ6dX01AKTUh2kBwID7KxOuBECj0iaignT5s0ASpD0RiWh42fBJPZdwyeV%2FUhaotEMaLiwtDiIpt7jTQ0gKlsdl20c2XCh9CWHvANj0pRKlIS%2BfA3AznRpUfotjuetuZtrtaz0IZbd%2B%2FoSm2LyRvhgg2FJXP4HevBHmxxCoCFhbv8badG98wTTLC%2Fah0fhryP65Vfmyn6ojGTAWWD0paDBxQo7DJ85Bv7505bbKfc64qjf3XedYbVFrWkPCU3mKeALycVqGh8zv%2Ftf61fX9git6gbpPvrqtPa5887yTH96m2idKEKDLM2V5nT%2FZTA2uD2LqrjZcJOoiTfy4tm2Y4RHYt0iinZd%2BwVMPG%2Bmr0GOqUBLwyYyqQwO1%2F%2BUHXZcIMF4%2BH21L9O9u0Y%2BnR8F%2FBYq9dHKMlV4Te5x0i4hswl340cTXGe3R5jp%2BQ9jZ5a9rfjwD1NDEYn53M9l%2FIslcyO55oLmIf5e49r7P6tcH29pLkg%2B3soI2OsYJabJuyixM69vP1180ZWWZstDmrr557%2BR4ttHgxLB3OdLF0AJ9q09EGp5drtjYyVYvVYb3s4Zc1eUj2AVbY0&X-Amz-Signature=9b547621c38d638ab5f7f43858fe6b74ba4ddb558cbd0d23587204f39f1f9cba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBYJRQUT%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIGVoSrMEtTvCWHGa6NsccGhno6JzUahovjJ8JPE5zQXiAiEAwXfLRnx9UtgcDOaWX0OhqqhMdVhDNAjp6eXXLg18WWwqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGI%2B4NJmdaQi9OvMESrcA%2B6MiwUVVgqFdFZDeun2TeVuzGu7erw5JslcjLJwURKhobmD0oVF9JrN0LoDpFOPhrpNx9OqS4EhnONsAIgY1HNE877U72ZPwwpsnS39yGRzCms9o5hCYfw2omJNVLaMcff4bX1nMOrars4BuK3K1RkC5LslWPCEtc0tev4e0SMH7yf%2BMIjYnY0umpnGPlfBpJ9PP0v%2B7Avv5MtshxPt8TXssVFEQ%2FBKLU7xENSZEAbK5QD297%2BPa%2F7urMwEobqAIdvk9hi6vG3%2Bl7ybdzqJhdkM2ZCHQ6dX01AKTUh2kBwID7KxOuBECj0iaignT5s0ASpD0RiWh42fBJPZdwyeV%2FUhaotEMaLiwtDiIpt7jTQ0gKlsdl20c2XCh9CWHvANj0pRKlIS%2BfA3AznRpUfotjuetuZtrtaz0IZbd%2B%2FoSm2LyRvhgg2FJXP4HevBHmxxCoCFhbv8badG98wTTLC%2Fah0fhryP65Vfmyn6ojGTAWWD0paDBxQo7DJ85Bv7505bbKfc64qjf3XedYbVFrWkPCU3mKeALycVqGh8zv%2Ftf61fX9git6gbpPvrqtPa5887yTH96m2idKEKDLM2V5nT%2FZTA2uD2LqrjZcJOoiTfy4tm2Y4RHYt0iinZd%2BwVMPG%2Bmr0GOqUBLwyYyqQwO1%2F%2BUHXZcIMF4%2BH21L9O9u0Y%2BnR8F%2FBYq9dHKMlV4Te5x0i4hswl340cTXGe3R5jp%2BQ9jZ5a9rfjwD1NDEYn53M9l%2FIslcyO55oLmIf5e49r7P6tcH29pLkg%2B3soI2OsYJabJuyixM69vP1180ZWWZstDmrr557%2BR4ttHgxLB3OdLF0AJ9q09EGp5drtjYyVYvVYb3s4Zc1eUj2AVbY0&X-Amz-Signature=9af8d05142eeb9d83fec6fc9d0fcefa9fa7521e6707eebee02ad40279a576638&X-Amz-SignedHeaders=host&x-id=GetObject)
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
