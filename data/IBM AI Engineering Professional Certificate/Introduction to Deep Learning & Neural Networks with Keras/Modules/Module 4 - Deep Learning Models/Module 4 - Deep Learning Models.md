

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=8d9140aacab49e3a190b1928e215db0a124e726cca8829b19fea8f2d37c9d53a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=0c19cc20ecefd9a5d099b3fcb5f9f2f0f1812e38d7a4944aefcfe900649f3a47&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=8a127fda5870b0784f343765bc9b62bf4ceb93612a30220d482da322b5b39397&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=4270cdee78f21808b758cc72fb5105c66bf5b0e62342195e96c51cc00cfcdede&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=3445a11f5f50c26ddf1279b08132ffcb93d7dcfd1e177a4fb91a2dee59645db6&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=77ff48a3cee9bec56a6b3102ad72e299b407ca5465d89c1980be8782b7f8f2b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=77056faa4319a9d12139436960bb38f813d602e21244c7046afca91dd6e12d80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=896bc2fc9b8dd2be0e44dec2d4d90aa431b587d6d9ed62f86c080925acd024c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STPDVI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGv13ibvchWlIvbcrpQ%2BLB8NVB8RDvdaC8rljS78zEjFAiEAz4v%2BFmJ28J%2BXnm40k%2FWicWccgGCsfPorh7f6yXRLloYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoDhOBL9g5lxOqMTCrcAzcWM%2F47O83IiA1NnI7FTUhnWYe6OKKZr0zLyBGlwMVBOt0XUJLzshg0kffDrjFzuqtOMuthvR9ojZfLnRSIr%2Bo4akUV9QYPftJuI2J0QqP6yprTqM2OTvH3jFCvvoN51RBjvcv99%2B3kS1dRvT1Sz43ZDolOZ7QSZMOoMY0W6Mr6j7TekRLPv32lwePozIsXv9hiVW2OOfPhzPrXe1fFlQuPVBSGNfz%2FAZ4l66KfzSP0vFx3L1Qi4TnwSbQx13tGi4Uv3Vd6FBtGM6fMDW2hBg%2BeaQxcF%2Fv7149hBCcjC%2F%2BfqW%2FxIbolTSoK9TUfJmMMSxeRTpB8YXYcuUHtbWALavUp5TA3Ekw2UxDSGgWE4BY04Y82oKDk%2F9zZ5FPTORc5IOcWpbnWqj%2Fl97iUxs6S2zhufkWLNhuDYVTHVDyZ9IVekU7IN1fyOEWKz0ubTgswnSgkdeCRDqpnb7h77U2wbxTREwNShp909AMs2c1SyLojB3L8nNtLatXwH9R9SbR0DCMACAhkOD9UJWLtf%2BjHMj%2FgWRR709HwDWYMJU%2FPOzLdQXT0WfMLs24waUgzgUVusqeDrO2mXpmbapAkIOyKDuOpuSGGFcWp3ShzzEeCcTz9w9FZzIFKF%2FCM2cymMNy7%2FbwGOqUBg5GxALMm35J0HBNlQsaBIIwSTxtnZ1VmuZmvps2E6bGpqIFT6nZjDdTfQwafkxIgIhwUqIG835Ucwsf%2BZ%2F6LDFaxm1%2FWjU7jheSqjZMm9e1OYp%2By5WVIVq5QNa3dID3QjGklj19n%2B8cTN0yObRke9Nq%2Fe94wHkulP70xW7KpHuMx2O6j7CWWnvpKND9Oec7NYauySHOwh8WRgPPkSlkCTTVuJ8k2&X-Amz-Signature=fe71aa7b659550aac7f1396f656608364a911de5f825ee45132b185cb5a7729a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XTLSNTV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcg4aD7%2FioiTx%2BHs5tY6RIv5UU%2FxOuPLpRq2CFUcanRgIhAODR497sB8L3Lx2ZnSd139O9lHuJ7DmNIfYXnEetOjhTKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzXNYtL26p2AWN7AXcq3AOMdTBL1WKaQPHCFHDnPKxo%2BQ2iMil35S%2BMkYEnG5ua8AjBh%2FqraCw1tkRwRdIuk0F%2BG6w2%2FlyEKUa1zNa7QUNnrL6c5rZfn%2BF26t0NyLBET5F5WnRC3bkFzgynUJk9m79%2Fm%2FcgUT%2F7dHTmZe8cUFWL3X9hE7TP%2BrZEIDtQY7Dc%2BSLMV11AFqt%2FDmvsbsGeqf6pwe6t53Rf95SUeydCBSa7I9DqEQ0g9tZyT5yFU0pc2CgZPmNSnkdCX6xyH647XcWlVhD4L4sMxdm9kW9DShk3miFFG4Mb%2FN%2FsCKnMAhVzj8jQIiLb6i8HiBpEvnOdDeNaC7drJHQYQrF5UgXayFSRouvlXTRQkF6pRIE9VIYS1BybsZyna7hXM2elhphtS1YRdtQFLJzTb1gZO%2FDk0%2FjXAVhxEc3z0YPc24IgdFYuxQsu50yGhTMZkYCXmuErTiQLJVQ0Xlc4j8714iXifwDl3%2BqtAf2OrfobXdpcKH0gqhJ2KwK7AVTxtCIdUr8Ylnjr%2Bk3%2BePiOsiyqL5ZVlp09G%2BrqT7tEs9GyxQdytMyImI277mDZ%2F2Ut1EaBfNWykIYXTM1MHakzKDnQjfiUKXR%2FL936vaN6UE56L7NKMDxQKAKDMWDvPJmKxkkJujDbtf28BjqkAf5H2mzCvcyhLpnH6txglzCGCRJNL7JdPzz40WSoEhHWV6mPZVgcSWO4DrLNrvb5bf6qTNNQmcjE1z%2Ftv5y1ACj1hiPZRt04%2FpcXBkB1VHTceKa2v1DvyH4mo%2FXwBpCg%2BbTnaVOnrQXka9UtA3r%2FnzdV1KhgGwhP61uhKUGuoPYHCdigjHNyiZydOL6Jsun22KMEoinvNYc6LJ%2FH9jQg3btQvpug&X-Amz-Signature=4106c767743962fd3163fce34d0c5193bae071f83e2afd0da575992ee5ef2950&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XTLSNTV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcg4aD7%2FioiTx%2BHs5tY6RIv5UU%2FxOuPLpRq2CFUcanRgIhAODR497sB8L3Lx2ZnSd139O9lHuJ7DmNIfYXnEetOjhTKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzXNYtL26p2AWN7AXcq3AOMdTBL1WKaQPHCFHDnPKxo%2BQ2iMil35S%2BMkYEnG5ua8AjBh%2FqraCw1tkRwRdIuk0F%2BG6w2%2FlyEKUa1zNa7QUNnrL6c5rZfn%2BF26t0NyLBET5F5WnRC3bkFzgynUJk9m79%2Fm%2FcgUT%2F7dHTmZe8cUFWL3X9hE7TP%2BrZEIDtQY7Dc%2BSLMV11AFqt%2FDmvsbsGeqf6pwe6t53Rf95SUeydCBSa7I9DqEQ0g9tZyT5yFU0pc2CgZPmNSnkdCX6xyH647XcWlVhD4L4sMxdm9kW9DShk3miFFG4Mb%2FN%2FsCKnMAhVzj8jQIiLb6i8HiBpEvnOdDeNaC7drJHQYQrF5UgXayFSRouvlXTRQkF6pRIE9VIYS1BybsZyna7hXM2elhphtS1YRdtQFLJzTb1gZO%2FDk0%2FjXAVhxEc3z0YPc24IgdFYuxQsu50yGhTMZkYCXmuErTiQLJVQ0Xlc4j8714iXifwDl3%2BqtAf2OrfobXdpcKH0gqhJ2KwK7AVTxtCIdUr8Ylnjr%2Bk3%2BePiOsiyqL5ZVlp09G%2BrqT7tEs9GyxQdytMyImI277mDZ%2F2Ut1EaBfNWykIYXTM1MHakzKDnQjfiUKXR%2FL936vaN6UE56L7NKMDxQKAKDMWDvPJmKxkkJujDbtf28BjqkAf5H2mzCvcyhLpnH6txglzCGCRJNL7JdPzz40WSoEhHWV6mPZVgcSWO4DrLNrvb5bf6qTNNQmcjE1z%2Ftv5y1ACj1hiPZRt04%2FpcXBkB1VHTceKa2v1DvyH4mo%2FXwBpCg%2BbTnaVOnrQXka9UtA3r%2FnzdV1KhgGwhP61uhKUGuoPYHCdigjHNyiZydOL6Jsun22KMEoinvNYc6LJ%2FH9jQg3btQvpug&X-Amz-Signature=05b2673a1300f9879b3adcb7c0c90003ddb56c69ba1627d4611d0a23c925989b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
