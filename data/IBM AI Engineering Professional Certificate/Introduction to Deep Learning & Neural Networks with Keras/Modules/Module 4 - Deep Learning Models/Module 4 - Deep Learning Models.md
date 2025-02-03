

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=6a8846984c042d00195ea7f187bd25d5c75cfba1b7d7db00b2a5cab9d76ec6fe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=8ff975ee7c220891bb939f6b372154ba5b8360f4ffc44b9f05eba2d9f6fc4e52&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=b330d96852c49dc71fcfdd842db032fb35ad3eda7a652cdb0a6d665b816cbce4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=919a79d5ff631bc8e53b8faf7b5bab4da442654611d274eb6f0aa02063bda110&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=621b38c58681cb7e48be7e74672230157f31527af219e7711294c551b1316034&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=8d028a9ce954f4e652fdf6011586e21dc260bd96b2febf0d90ec46107422b6eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=5dceb84de20b83ae6fa3b8f333cadc7233cda27fa0cef18e4750ac1e4703ec9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=2de19130382eebecf09650ae4c460269e2c5ec04847bc1ff2c5567c4e11cfafb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LZUVB2D%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBJhk8x%2BIb7fHWL0BWnQnDLE3%2B5uesNDQYzG9yzHhVzOAiBATZQJYQK1Ty2%2FOsL97DLHHMegA0NGEjStUflKyy%2F11ir%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMBgdl3gPzf1XjrUIdKtwD61RZ1pFoA8holb6GlY9kmUyxcegZS8WdkRuQ5ICiMG%2FDPN%2FmRMnbIor%2FdGrhCXrTXWEOdmFqQoa4JMzC4y1dhZic03kdDGrs0mJIW%2FfalulB3UVCwXlg%2Fk%2FOI2X2H62q8y6kL1rquOPsjWWMF3J2w3dfCJ4abXh5OzZQyMQht5TLbFLJBjcCdcr%2BBpeYgTWx4aBTo0oZD%2B6R3Y%2B4rCd%2BpjDcUmhB3AeayYGLpokcWTsGDkHm4rKHRcx0xAFQdi%2FIkJD%2BgLBohUiWnUqhsvFrzwWfb0GD9G2DhiepBPH8VWNLGp812HeVK1QAc4Odop04gxhD4Pu3ZJGGWQfy4XcWT2EZyU1XOXPOIurdNPmDpb0bdeGiN9ObRA3pqXjq4tj4O3L7zKIspd0QEnzq5GEON95ggofq5rt%2Fdc4RGK0fsmIZgpeNGVNw%2FNXsdBTrLubMf3CjFgAaezqDsyjywq1PzRPhjsk5lquqIj6AWkEmDWBEUGoNxnwGv6ruLZoNLeEjKyD8gPaAWYxNytyqD29VqLwmSOMhyeKwQ0HWJC5lPkXf8rlZXOr%2B2SLxYKOHUaxMeTPBt3PzTyRUXRcAsdmJwMWmy5na%2BDGrlVxflBd2devBIMnBMt669CM%2BPYUwtdmEvQY6pgGA%2B4O6IbWa3qBR9a4oa3xS715JtvI5JfUGpwh1f12SyFsmCq02%2B%2BAQ9D6bQ6UjPhD7h7GC469WdN1wlKoAiLkeHSwEpOoTlW%2F6dE1WUxZ%2B7YBBExJ93rCG0IDX6c2HFgWY9X18QXl4rFy0IqcRtRYEYAcPE65OdB05fxNtOFmElfv8RMgOqijN3lq%2FULO0v6bLrtGC%2Bdi30iKnME3pOj%2BHsfjSbtPr&X-Amz-Signature=811feb6b78c13ac87ff418569cb24bc4e9a55abd181c21cb8b30229fb5073671&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REHU2B6A%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIDGax07wnjT6uxhpQuyqAg%2BtFY6rIENFxoSVBkWS4VtWAiEAsvmHpfBO0iBxF67C0hBsgeifTv%2FZ2UKNVd3kmf1DHV4q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDAPuaYpuIvL8EmrmLCrcA7fnIJOkxK5ONlL0Ov9MrpxB%2BtYluA7qfaDsnzwFb7hANfkyXBTZ1pCfRiwp97vfYazyMoDSbZ%2B9mXani9CckDYjARHytfedyQtamMyLdCzmcuAtxixWq2gZjXSA%2B3RGpFx6UN6mQUJDh0ZcF2q3Q6vRs5GgoJCE9vx%2FCw72l6dwanD%2FKF78LAorif7YebCXxfLkXZ4YEX%2FBu6qfTnMLlzEYOodeZWLdK45%2FBGmTRId2ouC2fjK73y8uLroicWNjyI9N1lmAP%2BiQ1atULwVX9dmsy7Vp0SXklcZY7yMBq2z%2BLYvrsPXUZzacjjBZ6IMdBzzOWHu9svvpLiUs%2FZGbp21kH6SRFLamj1nnyGPrGL%2Bl8IZKPH0LJIhxQvbpwFS58GlCsbmWQn%2F19GJFlq6Yt5BXZHmGmMl28klany9HUFARcizB%2BSqn%2F3M%2BD5Ey6xgsbXWdehAbDgRcLusOEJh1AI%2BrSIsYUeVLzA4U5UkH30CHWJqJ4KCuyY6x7qla67plvEIXBv81tqwAzEGlHV%2FvzsyM5CRoKfNqM%2FFsk9NzAC93o0w%2BNyoYEYd4NfUxGaqKLZGXRe24hSARtISxWC8yfPMt7vO0NxLZIsXMq%2B27el4EP3ahOaNsnX3%2FoDhBMPXZhL0GOqUBIBOEKeMP%2BmmhubJAIJWakdMFs1D3Q85BMxuO3wivKSqHBv5z0DJJAcxGs0lfH21ZfDyoIJTzPn7doKRkS0cbgXMiuM6cyvbZGnmJ%2Ffuxll24c0VA6ZVK7rrBhRBIkZtZQT7aCgevGPfCuAlfna%2FZAkYgptOagoeGMdEff6vEYqYsZoUcZsbUS%2FJLFO9%2BeFUjV9WwGIkJiKT7ScAgE9y%2FCi9HsJ9p&X-Amz-Signature=4d5a04ef5d651499aa04bd59bc4453220ee0c2d3dbee63f6086b00f9f41b8367&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REHU2B6A%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIDGax07wnjT6uxhpQuyqAg%2BtFY6rIENFxoSVBkWS4VtWAiEAsvmHpfBO0iBxF67C0hBsgeifTv%2FZ2UKNVd3kmf1DHV4q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDAPuaYpuIvL8EmrmLCrcA7fnIJOkxK5ONlL0Ov9MrpxB%2BtYluA7qfaDsnzwFb7hANfkyXBTZ1pCfRiwp97vfYazyMoDSbZ%2B9mXani9CckDYjARHytfedyQtamMyLdCzmcuAtxixWq2gZjXSA%2B3RGpFx6UN6mQUJDh0ZcF2q3Q6vRs5GgoJCE9vx%2FCw72l6dwanD%2FKF78LAorif7YebCXxfLkXZ4YEX%2FBu6qfTnMLlzEYOodeZWLdK45%2FBGmTRId2ouC2fjK73y8uLroicWNjyI9N1lmAP%2BiQ1atULwVX9dmsy7Vp0SXklcZY7yMBq2z%2BLYvrsPXUZzacjjBZ6IMdBzzOWHu9svvpLiUs%2FZGbp21kH6SRFLamj1nnyGPrGL%2Bl8IZKPH0LJIhxQvbpwFS58GlCsbmWQn%2F19GJFlq6Yt5BXZHmGmMl28klany9HUFARcizB%2BSqn%2F3M%2BD5Ey6xgsbXWdehAbDgRcLusOEJh1AI%2BrSIsYUeVLzA4U5UkH30CHWJqJ4KCuyY6x7qla67plvEIXBv81tqwAzEGlHV%2FvzsyM5CRoKfNqM%2FFsk9NzAC93o0w%2BNyoYEYd4NfUxGaqKLZGXRe24hSARtISxWC8yfPMt7vO0NxLZIsXMq%2B27el4EP3ahOaNsnX3%2FoDhBMPXZhL0GOqUBIBOEKeMP%2BmmhubJAIJWakdMFs1D3Q85BMxuO3wivKSqHBv5z0DJJAcxGs0lfH21ZfDyoIJTzPn7doKRkS0cbgXMiuM6cyvbZGnmJ%2Ffuxll24c0VA6ZVK7rrBhRBIkZtZQT7aCgevGPfCuAlfna%2FZAkYgptOagoeGMdEff6vEYqYsZoUcZsbUS%2FJLFO9%2BeFUjV9WwGIkJiKT7ScAgE9y%2FCi9HsJ9p&X-Amz-Signature=6bbecd0ed089a8fdb19746d350dd8ff3491d45ca0c481ca04e2ec80fc16679f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
