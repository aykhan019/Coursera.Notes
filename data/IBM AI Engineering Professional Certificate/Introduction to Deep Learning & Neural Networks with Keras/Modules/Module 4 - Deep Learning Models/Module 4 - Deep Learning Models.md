

# Module 4: Deep Learning Models
## Deep Neural Networks: An Introduction
### Overview
Neural networks have evolved significantly over time, transitioning from shallow networks to deep neural networks (DNNs) that handle complex tasks and data types. This note explores the distinctions between shallow and deep neural networks, and the reasons behind the recent advancements in deep learning.
### Shallow vs. Deep Neural Networks
#### Shallow Neural Networks
- **Definition**: A shallow neural network typically has only one hidden layer.
- **Characteristics**:
	- Simpler architectures
	- Limited ability to extract features from raw data
	- Often used for simpler tasks or as building blocks for deeper networks
#### Deep Neural Networks
- **Definition**: A deep neural network has multiple hidden layers and neurons.
- **Characteristics**:
	- Capable of learning hierarchical features from raw data such as images and text
	- Ability to extract features from raw data.
	- Handles more complex tasks and datasets
	- Example: Image recognition, natural language processing
### Factors Contributing to the Rise of Deep Learning
#### 1. Advancements in Neural Network Techniques
- **ReLU Activation Function**:
	- Addressed the vanishing gradient problem
	- Enabled the training of very deep networks
#### 2. Availability of Data
- **Importance**:
	- Deep neural networks excel with large datasets
	- Large data helps prevent overfitting
- **Current Trends**:
	- Access to vast amounts of data has become easier
	- Deep learning algorithms benefit significantly from increased data
#### 3. Computational Power
- **GPU Utilization**:
	- NVIDIA GPUs and other high-performance computing resources
	- Reduced training times from weeks to hours
- **Impact**:
	- Enables experimentation with different network architectures and prototypes in shorter periods
### Conclusion
The combination of advancements in neural network techniques, the availability of large datasets, and increased computational power has driven the recent boom in deep learning. The field continues to evolve, with deep neural networks becoming increasingly prevalent in various applications. Upcoming topics will delve into supervised deep learning algorithms and convolutional neural networks (CNNs).
___
## Introduction to Convolutional Neural Networks (CNNs) (Supervised Deep Learning Model)
### Overview
Convolutional Neural Networks (CNNs) are a specialized type of neural network designed for processing structured grid data such as images. This note covers the fundamental architecture of CNNs, their operational mechanisms, and how to build them using the Keras library.
#### Convolutional Neural Networks (CNNs)
### Architecture
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=b5e1754b72cc04df96ee9e61a9e23206092efa3b5b60953f188974328f511aef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=02936e634c67bdb4b3ecf0fbef26abfdc90fbf26ee2814a7a2073447854b8eab&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=d88f0f6527df2671f2ff194925ad0061fd8db48231e64416d53f651a8316caee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=b2a4883221979c7a9df103e92a191ba20fe0223fc0d9ce490dbc701bd1129e10&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=73d27c6004bd5348c3efb6b2233f56bcf90611f947c2570355b2bdfedbd4251a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=49dcac3f9da18fb93c2d35548b5b5a840ccddf636c9a5ea306c9046adf3df4c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=dbe38efe51af8d3b76612a73aa35f1d31c3f7a55bf4a9360cb7b2cf211fb433b&X-Amz-SignedHeaders=host&x-id=GetObject)
### CNN Architecture
- **Input Layer**: Defines the size of the input images (e.g., 128 x 128 x 3 for color images).
- **Convolutional Layers**: Apply multiple filters and include ReLU activation.
- **Pooling Layers**: Apply max-pooling or average-pooling.
- **Fully Connected Layers**: Flatten the data and produce output based on the number of classes.
- **Output Layer**: Produces the final class probabilities using the softmax activation function.
### Summary
- **Efficiency**: CNNs reduce the number of parameters compared to traditional neural networks, making them computationally efficient.
- **Applications**: Ideal for tasks involving image recognition, object detection, and other computer vision problems.
### Building CNNs with Keras
1. **Model Creation**:
	- Use the `Sequential` model to build the CNN.
2. **Defining Input Shape**:
	- For 128x128 color images: `input_shape=(128, 128, 3)`
3. **Adding Layers**:
	- **Convolutional Layer**:
```python
model.add(Conv2D(16, (2, 2), strides=(1, 1), activation='relu', input_shape=(128, 128, 3)))
```
		- **Parameters**:
			- `16`: Number of filters or kernels.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `input_shape=(128, 128, 3)`: Shape of the input images. For color images, the last dimension is 3 (RGB channels).
	- **Pooling Layer**:
```python
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
	- **Additional Convolutional and Pooling Layers**:
```python
model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `32`: Number of filters or kernels in this convolutional layer.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
4. **Flattening and Fully Connected Layers**:
	- **Flatten**: Converts 3D feature maps into 1D.
```python
model.add(Flatten())
```
	- **Dense Layers**:
```python
model.add(Dense(100, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
```
		- **Parameters**:
			- `100`: Number of neurons in the dense layer.
			- `activation='relu'`: Activation function applied to the neurons in the dense layer.
			- `num_classes`: Number of output neurons, typically equal to the number of classes in the classification problem.
			- `activation='softmax'`: Activation function applied to the output layer to convert raw scores into probabilities.
5. **Compilation**:
	- Define optimizer, loss function, and metrics:
```python
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```
		- **Parameters**:
			- `optimizer='adam'`: Optimization algorithm used for training.
			- `loss='categorical_crossentropy'`: Loss function used for classification tasks with multiple classes.
			- `metrics=['accuracy']`: Evaluation metric used to measure the performance of the model.
6. **Training and Validation**:
	- Train the model using the `fit` method and validate using a test set.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=def0579d323e8ea7eae295b17de241b886d03f9c25fedc9246057e848105ec0a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
CNNs are powerful for image processing tasks due to their ability to automatically extract and learn features from images. The architecture involves convolutional, activation, pooling, and fully connected layers, which collectively enable the network to perform tasks such as image recognition and object detection.
___
## Recurrent Neural Networks (RNNs) Overview (Unsupervised Deep Learning Model)
### Introduction to RNNs
- **Purpose**: RNNs are used to analyze sequences where data points are not independent but rather follow a temporal or sequential relationship.
- **Architecture**: RNNs include loops that allow them to take both the current input and the output from the previous data point into account.
### How RNNs Work
- **Input and Output at Each Time Step**:
	- At time `t = 0`, the network takes in input $ x_0 $ and outputs $ a_0 $.
	- At time `t = 1`, the network takes in input $ x_1 $` `and the previous output $ a_0 $, weighted by $ w_{1,2} $.
	- This process continues, incorporating previous outputs into the computation at each step.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662INTU6OD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIAPbOnSVKuzlFf27DM%2F1RiIkwdvwpsP9LgGh5OMhJIjwAiEA7Cb3dYzNq7bKlyaIEEqzpXpO904LtWXET0ZLuf%2FIPgAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFshFmelfikjDI72UCrcAw4tIIUuCB0a6EOBrOyRDNYhB%2BlO9jx%2Ft%2BbDqrojneBHstoLHL0AbSpbPyAxbyiHWWci3%2FfcWfrnWWeuNssbdWeHqxnHh29ZR4zRn8aaBcnPfmEtCV9Ku55OlB8ZDcmAkqly83HYYEg4OSq4%2FXfn%2Bhiaw%2BwM8nQMgch8lJewCDzyy53bG%2Fqxv1lw56DkceWtZMRP86pxelxGlCihE2BvG2XyZyhzZaGEKb0gkgPiZSPvsl533WqD0CtAwWJwQz2Q%2Fj30FGgEM5ZNFZknNsdp0x8C5sGD3%2Bhc5Eugedv2TpTh83QEDaix6drvOWd01UoQ0sPnGAS2U3lCKw9%2FJ4gvoquQ0NG1%2FCoou3fU%2FP1LrY%2FXKVSn3fxAQMMNw2%2FjHyJ4ERCX5YjUuA2bE8Oqt6Awnc5vY%2FYccgPPyDo4NlH6v%2FKp5pVdeCSpvxmso56e%2B43f%2BXySHkvVe6COUTwiWw44WTdjKaiLPUrNG6AQrZWOzL3MiuOag3%2FHjArz0DGS4M3zvCnEZtFBEVDW5sECwTj2WViRhWamIGAeBDLidVNwEpmYRpSduCbRkgTUqyQffdB9aDaPsj8wDcf7tw7Jq9zTKmMA0o%2B36Taaax32tlkb0bbfn0ebIwn7kRinIvEQMMW6jr0GOqUBW56UOQAddX6%2FEaHeIXrQJEPTSQJciRl8kpMqKp9gr%2BjA9%2Bidmo6UYGPTL9VMtFbHZio8ySPTttKsA7k%2B%2BmqTTTUSUts3aT4NHvv4Z8%2FzdWaI%2BS4ij4v89BrTTC4MIjFpvK23v6W1ukYSZjM0shyZ6eqCwgGhgzkG3HLlHd0UhWc97aRNdKU5Ej9YrNkBZOaVR%2BhPWD%2FRUMJKYQr7xPPgx1cRFwfp&X-Amz-Signature=6e49c828978fc29a07f21405c3ddc1b7c4bef3f4cdaa9b6966c6e0442e8b23c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of RNNs
- **Text Analysis**: Suitable for processing and modeling sequential text data.
- **Genomic Data**: Can analyze sequences in genetic information.
- **Handwriting**: Applied in handwriting generation and recognition.
- **Stock Markets**: Used for predicting stock prices based on historical data.
### Long Short-Term Memory (LSTM) Networks
- **Overview**: A specialized type of RNN designed to overcome some limitations of traditional RNNs.
- **Applications**:
	- **Image Generation**: Models trained on images to generate novel images.
	- **Handwriting Generation**: Creating handwritten text based on trained models.
	- **Image Description**: Automatically describing images.
	- **Video Streams**: Analyzing and describing video sequences.
### Summary
- **RNNs**: Effective for tasks involving sequences and temporal data.
- **LSTM Models**: A specific type of RNN that handles long-term dependencies and is used in advanced applications like image and video analysis.
___
### Autoencoders and Restricted Boltzmann Machines (RBMs)
### Introduction to Autoencoders
- **Definition**: Autoencoders are unsupervised deep learning models used for data compression. They learn to compress and decompress data automatically through neural networks.
- **Purpose**: They aim to learn a compressed representation of the input data and then reconstruct the original data from this representation.
- **Training**: Autoencoders use backpropagation with the target variable being the same as the input, effectively learning an approximation of an identity function.
### Architecture of an Autoencoder
- **Encoder**:
	- Compresses the input data into a lower-dimensional representation.
- **Decoder**:
	- Reconstructs the original data from the compressed representation.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBJCMSMD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD7amKvjQeLdqoYOfnjSXpuEXq3iVIsw13JEe%2Bn5cKZxQIgMjrDq5Bdk4UVx4HXpQT04tHUm9hEmcHBu55hiz2ZP9Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBO1dpcv6LP90ZrUDSrcA%2FvIdIciojaHDAFeG%2FLImIRq9IJvaSpTt1TWVaWE2TORXRL3Ko%2B%2BcR5pNfZOE8sqoefZgzNhPcpX%2FIYOmeTVWaWBlgjH%2BTddgrCuEY7RpTcOQ3rxhg0qh3yteG7D9X%2BI2f1iE9Sfn1cPVT7WNEbcCDG7ebzR33R7b0f7GKZh092E8bNvHDgrnXO9xdtBewH7TTeJcy3pDey0PjeBO4P62n74CtyQbXHcWIxqPMYpoN2RSl3EwQzgaNQr62eqADfN%2F1SS%2FGv9CkX6E9Y6ds77QhYYvFd08dJDV3skDMHeKNHgTM6ByX9ZEAY9a1tusxoaGLcgMcIQ5BXnZK8oFuuJQLrvhmkp5hKebi1pxREH8mvj67eBq2sXTm8HQloIYgLk5IhkRH8CLlSDD%2BtAl7n5qORDdIb%2BZOHz01QJOWY08%2BoX1besljgYfGRhFGN6ZGHBv6Lf2hFKc3CUPoUmK87gKkJCTX%2Fsmny%2FvdQ6%2B8mlx2u0q6lGnsRWL7d%2BosUXHtoZZ1UIPn7xDKKDsI%2B8DnokBnX0xvCIaWeu%2B%2BhevSZfljYfo1aE4KjrvIliZBLBtEfr6UUbQT3aIGUyYSt6XgeYUlxKbBSHET%2F5Re0M7epiMMoM2ek%2B2xfPRzs3hCkbMJ67jr0GOqUB4tmxVlKS1yLoFM67q36Et%2F3g0MHwY3B84%2BSdl%2FWaD7Ru%2B4JqdjUeY2DZMiMjRPGWmFEgTaUmNN6bSoUNJGI0jRZCe6CvBYZEb4awUnc%2BjFPG7P2tg4POEqr829JgH6L%2B64Yh5DwjYRe81aQ1fBgaRBtSxkEhL%2BPau3X2gfntC5%2BUR9pbwumewmbLR2WHGIgh6WA12H1H5zzDECZDae1MUBIeTHSX&X-Amz-Signature=6907d4533964d4eff65f55067a12b8fd0f5b9bf909ca725a584317d361068658&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of Autoencoders
- **Data Denoising**: Removing noise from data to recover the original signal.
- **Dimensionality Reduction**: Reducing the number of features in the data for visualization purposes.
### Advantages over Traditional Methods
- **Non-Linear Transformations**: Autoencoders, with their non-linear activation functions, can learn more complex projections compared to linear methods like Principal Component Analysis (PCA).
### Restricted Boltzmann Machines (RBMs)
- **Overview**: RBMs are a type of autoencoder that can learn the distribution of the input data to perform tasks such as:
	- **Fixing Imbalanced Datasets**: Generating more data points for minority classes to balance datasets.
	- **Estimating Missing Values**: Predicting missing feature values in datasets.
	- **Automatic Feature Extraction**: Learning features from unstructured data.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBJCMSMD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQD7amKvjQeLdqoYOfnjSXpuEXq3iVIsw13JEe%2Bn5cKZxQIgMjrDq5Bdk4UVx4HXpQT04tHUm9hEmcHBu55hiz2ZP9Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDBO1dpcv6LP90ZrUDSrcA%2FvIdIciojaHDAFeG%2FLImIRq9IJvaSpTt1TWVaWE2TORXRL3Ko%2B%2BcR5pNfZOE8sqoefZgzNhPcpX%2FIYOmeTVWaWBlgjH%2BTddgrCuEY7RpTcOQ3rxhg0qh3yteG7D9X%2BI2f1iE9Sfn1cPVT7WNEbcCDG7ebzR33R7b0f7GKZh092E8bNvHDgrnXO9xdtBewH7TTeJcy3pDey0PjeBO4P62n74CtyQbXHcWIxqPMYpoN2RSl3EwQzgaNQr62eqADfN%2F1SS%2FGv9CkX6E9Y6ds77QhYYvFd08dJDV3skDMHeKNHgTM6ByX9ZEAY9a1tusxoaGLcgMcIQ5BXnZK8oFuuJQLrvhmkp5hKebi1pxREH8mvj67eBq2sXTm8HQloIYgLk5IhkRH8CLlSDD%2BtAl7n5qORDdIb%2BZOHz01QJOWY08%2BoX1besljgYfGRhFGN6ZGHBv6Lf2hFKc3CUPoUmK87gKkJCTX%2Fsmny%2FvdQ6%2B8mlx2u0q6lGnsRWL7d%2BosUXHtoZZ1UIPn7xDKKDsI%2B8DnokBnX0xvCIaWeu%2B%2BhevSZfljYfo1aE4KjrvIliZBLBtEfr6UUbQT3aIGUyYSt6XgeYUlxKbBSHET%2F5Re0M7epiMMoM2ek%2B2xfPRzs3hCkbMJ67jr0GOqUB4tmxVlKS1yLoFM67q36Et%2F3g0MHwY3B84%2BSdl%2FWaD7Ru%2B4JqdjUeY2DZMiMjRPGWmFEgTaUmNN6bSoUNJGI0jRZCe6CvBYZEb4awUnc%2BjFPG7P2tg4POEqr829JgH6L%2B64Yh5DwjYRe81aQ1fBgaRBtSxkEhL%2BPau3X2gfntC5%2BUR9pbwumewmbLR2WHGIgh6WA12H1H5zzDECZDae1MUBIeTHSX&X-Amz-Signature=de7b6e6bbda934cf50e541abd81b75ae826a6c971bf70b56a63721950bd20afe&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
