

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=2724cb15552094eb91ef514d7d72d02a34d633b44b802effa0a1db486000b443&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=cdaa29f32264ddf11320f4169a4ce005840aa0961c2eb43eaa533a6dd0ca4b9b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=0f47a550fbc0006ee42c0ef19e0068f42705aa722cd65e7835568c8688a2e372&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=bb757ba55a0a77cb0ea465ec180205a6493be6f5849f405f21e96c4f7d9a3fa9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=a489004c83c798e9b97e67560dfd1a1295975073fc9b714087f4af282d05eab9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=f3769d65e9d285177ef884912bb0175e37aae51d790af9586bbb94d171bd85b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=16a9506bb2c3f1aa413d07f1e9d984c05d3860f16a821079f4f9a4421414d6d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=3f4cf2a048d64dd5d61d313374a40c3887a25254be191a8d9b361d0430bdbf5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67LUM2R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEEcvSS%2BTwXFVMl1ae7Ub4O6OWx0%2BH81vwmtY5s7r8LbAiEA0RJSPZsl32zpUDWsEJYHm3c17qPkCrgb9mkOotEyIHMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIJdbFUKfT7x3pI6fyrcAxflHA5dzIokwIIWAFD%2FVHI8zDqdyiA7WsUA0CeE7ET%2FMkKGG5vJh6dbvDgQyMyWXVg8I4J1OMdASOtCjNoEs3H1mM6Ol8RE10fLZGWQqR79qJk8nGaGhuEFXNqLRethmCuttGibtGV2%2FU508%2FpKmyoCiGMvAV4aL57cap8ryXTCxZ4NTbiaQUorSjwEuyBBEGclm5lLKlCXTFReLNgZg0cbz%2Ba4QGeJWisO3FHu5d8luIN8otzLQRRDpDUcNCHzFqSg9gKT98I%2FU4RhhpXZJ2gqJBiEckCSgyWx5Kl8lb6YMbnUnRMNe6ogy%2BxQAOjM2RlT7bXAnLLMLDaM5hwXfw%2BtubYE%2BHbpTWkGkgb1BZrUPH6C7YM5oHdc4QqsxG8nvos7H9Fn16DP3RmIlowbGTD2x34P65nosvSnn6Q0vzijbe94z6h0cfGQGF1zvB%2BxlMk8ohFHiz4uDjh9Pq2pGQ%2BkEmACNnSSyZkqBDA5XTWVrV%2B2FHeEpbBT1w7%2FtyNXyybTG0zVpCN0XGsQPSq6kuGlSHWXDNXLHsB0sZXgtzXBV6i4MsiSQMGKvAWnAD5n8yIGtIupA26DjYmUykSGH4J12ecq8CGzAlIV7r%2B0Z8xJH7B2iuA1Tc6nXjwnMPL%2Bmb0GOqUBM7RNf%2BArBCfaieGLckRmvsFnNzMyoWUD2YLycMt5cSbeOm2DEAYlU2KMq8zBUMgSIJlh%2BtIKAyfm4HUyg0hZ9tN3AJzjBuWiK6vFJtMrlagTqc6T9VrkDJRHE%2BMvmDE9FKT96EAeOamHmptTOfhC7YGxKXgnSsMsRxuV8cn0piQePmYi65KP4VguyURpTrN0gc4X52k%2FYGReSVNjaCPiUkUkumig&X-Amz-Signature=bc467241cf2c6bb7d047f838bda1b91c305d159bd9b47712053792d70933417b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3HXYMM3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIC%2BV2%2FWu%2BYB78MNsymlHGSn892up55lmdSjnmx5uaHaNAiA21ABV9Mg2gIV8UlqGnLP0Ti%2FLMj4CClc6c%2FedklgAyyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMi%2FS9dDqWvql2XAVTKtwDwahxFHMMwx8DY1GKXgN6rR3QRL3toaleYcUun2nAbdxc%2FDgcztp7cpyTU9nm4pk64%2B9wazTMdkuDupCp1VVOMANRDPKKJnEqvAyYr8OwaPxaWr0j2xCeVFi4oy%2BRolRMTcQESKzJrJ9N9wvFrpvElcg5BBif9nAYY7khee5s1bFS3cKqxGAW31KhLHgL0jqADt7L8IwvS6mLxf4h2GaTfIcTJPoKS%2FmdGbCvMRO7cYImhQNSHCfIx8VWNTGj%2FgTWRoyWHRzDr285zdfm0Jm39J%2B%2FByLuTjB6Vag4QOkvUcRNsBwCvjk8un3McD1NXMlnkmGZcL3X7Yfr4HfRAyw%2Fv5cYwFOs4X4yOcUYfBfvB82F5AvtHIfL0wSnS6NyR9wprQn7BOXwrhBr8Wpn%2BWxE5xv25H%2FXwyruHbh8MSk%2Bjo02J7noctOj4FOLySmew4XRAzjqWx56jgHgNccnYSSxeTHHtzuUc1p7loy36qURkxt28ibxL0mTiJoQnD0TVkfOza3UYG4cig7zCZyQo%2BXQg4p25WBY9i599c9iXyDHw1bjsTbrIsQiBKvv5kqMl2R6hg3LLlKXib0q7WEnPAT%2B7tumRtskEo0LyZsm38W94W4W%2BXLvMQC0N3PsK34w%2B%2F6ZvQY6pgFgWOY5lGOLx3HYyWgkUpZnO3ghamm87QxAuMy5wLUEGdi%2BvrvufrFB7EnUCJwpW3KLuLSW%2BxfUmdd9sRvtNYZoFdJkUn25D%2FrMa6kRd8apK8MsO7JL70Xuva9fqvlS2kCcN%2FCJCM%2BuGyz4Z8Cna0BmflhmcXE8Zx0CQWlFxkG8SeHLJVqJRVdYetRbgB7rOqAikUMbxxZdWIHKkT2T1m9mUvmdLlbJ&X-Amz-Signature=e60e4b5834a1401693cb9cf511dfe1f6284e832120bfc44773722ab616d917b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3HXYMM3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIC%2BV2%2FWu%2BYB78MNsymlHGSn892up55lmdSjnmx5uaHaNAiA21ABV9Mg2gIV8UlqGnLP0Ti%2FLMj4CClc6c%2FedklgAyyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMi%2FS9dDqWvql2XAVTKtwDwahxFHMMwx8DY1GKXgN6rR3QRL3toaleYcUun2nAbdxc%2FDgcztp7cpyTU9nm4pk64%2B9wazTMdkuDupCp1VVOMANRDPKKJnEqvAyYr8OwaPxaWr0j2xCeVFi4oy%2BRolRMTcQESKzJrJ9N9wvFrpvElcg5BBif9nAYY7khee5s1bFS3cKqxGAW31KhLHgL0jqADt7L8IwvS6mLxf4h2GaTfIcTJPoKS%2FmdGbCvMRO7cYImhQNSHCfIx8VWNTGj%2FgTWRoyWHRzDr285zdfm0Jm39J%2B%2FByLuTjB6Vag4QOkvUcRNsBwCvjk8un3McD1NXMlnkmGZcL3X7Yfr4HfRAyw%2Fv5cYwFOs4X4yOcUYfBfvB82F5AvtHIfL0wSnS6NyR9wprQn7BOXwrhBr8Wpn%2BWxE5xv25H%2FXwyruHbh8MSk%2Bjo02J7noctOj4FOLySmew4XRAzjqWx56jgHgNccnYSSxeTHHtzuUc1p7loy36qURkxt28ibxL0mTiJoQnD0TVkfOza3UYG4cig7zCZyQo%2BXQg4p25WBY9i599c9iXyDHw1bjsTbrIsQiBKvv5kqMl2R6hg3LLlKXib0q7WEnPAT%2B7tumRtskEo0LyZsm38W94W4W%2BXLvMQC0N3PsK34w%2B%2F6ZvQY6pgFgWOY5lGOLx3HYyWgkUpZnO3ghamm87QxAuMy5wLUEGdi%2BvrvufrFB7EnUCJwpW3KLuLSW%2BxfUmdd9sRvtNYZoFdJkUn25D%2FrMa6kRd8apK8MsO7JL70Xuva9fqvlS2kCcN%2FCJCM%2BuGyz4Z8Cna0BmflhmcXE8Zx0CQWlFxkG8SeHLJVqJRVdYetRbgB7rOqAikUMbxxZdWIHKkT2T1m9mUvmdLlbJ&X-Amz-Signature=55b81a393798c554bb65c0549512d04bb527c2a4a8ef17d008fa3ee05821674f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
