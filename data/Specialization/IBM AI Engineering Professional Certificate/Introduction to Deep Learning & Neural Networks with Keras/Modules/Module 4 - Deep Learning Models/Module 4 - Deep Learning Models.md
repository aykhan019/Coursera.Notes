

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=96366bcb4cbf9892bb1e3993bbd2a7cd61eb55ccd834b9d450599748ef29a384&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=847197595505bd92e185f1d55cd81aed6dcbc2a6fac0c2908e31b1b8bd7bd702&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=4b98c62ddf44409d8f5613e18a13e702038a72eaaf809d798f9e0715b6aacb83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=27c1c93d1796084cb91aa16f39a14e656d59451a713693537bc7a86c1bb293c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=bd76e511457f915be52726972894e1c6bf61473764ddc53d1bbe509286029bc9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=3e9e44c2a02b69f4d395ac39d7214da9e07ec610cde1a7e433f12cd7b70d408a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=0ae3fdd6de4029d9af938961cd2233eeaf88face7c6a376438bb405ea008fd64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=350130c7ec6cba3e84a5cac22f9ae307b4eccdf45119079b6f225f4c1685964b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVKQEJDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZLygHxCcSAWch7KxCxEl58Fqg8smLkdpVv342FmfMvQIhAOtqGxb41X8ho%2FA81yfqsBoktX6i%2BLL71exBfg6JBdMmKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4V1rsOXFNWUaxV%2FMq3AMt5BdoZ08MnpsotcId1h1qsrcd8SODhkX3Of4mKXDEpkQXwLvEcPsGhTQ%2BogdejI%2FSFHPxEZld54942DysvL4u6u1hJHk2VtUCTST9bG1Ni507JHV1oXMQfUf%2FJ%2BNJNKFHVVK6DFWkMx9cn5nEvS2abSiJCMUBIGsjnT9ZFOl7sJ0PrBnwIh9yvOq%2FoHekJVMtfUpJ7Q3U0FvN6lq%2F8xU%2Bdlrmaq%2BWTVDO66Flo1KrQqTo5lyLDMgWcrYvTyPt8NNL48Hx8QB%2Boksqx5WR5rOKLk6F%2FxoDJQG566N%2BVj6S%2FmTN7GvgxANRGQ1pA2Y8QLyx6r20LmLi59fYjU9Y89uNppNaZQxdVkveuvQkQqSG38EVxwIFPZYF7b%2B1x5Jrvb4ALsTssIrjr4316jbZhROGB1LAdoO85Jzc7xotPRgD%2BOJNDpkPPuXxMNx%2Ff2SNc4%2BWwo869rz2TImIUy8wpAvXExPBiwOdTlYyKltyyb4aVNTo2SZPR8ypSx5H6RKudBl9vQCP0Np6KhxigaabAccxewroasV9Td1V3sDJRa8KKkHqAJlstNlwXuYNKepUDSgX8EmqQY3VksKQVZTbFGGIrU%2B%2BOhAj2%2FZ%2FY7GsvWmQl2gVfn5bhSS3MxiXCjCj3%2B28BjqkAQjNHOdMYRdttC9f9npuC%2BoJTanM0W5w8Oz0pUwJtxgNt46XDKGadfZ44L%2B4imJDb9iTGEcEcd1qfhCXMw9L0Z043%2FNW%2Fgy3MA0QfIxTKO5KE9AtIDzCDOaOMG7c8x%2FZXdhcm7XKVsSAIuNqSgb5kUxrcI0%2B1myVsU3ZL1TXvegbNIj7IHsEMPBNfFtisXJ4wabLWUtE0wDT3F7gJWoDkhulYWJm&X-Amz-Signature=43d70ce59a106a582300d8cd49ea02177db78471ccfe8895fb395d9f275fea8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLCYOKU4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnqwM8kZ6kCa0cI4P6pK9N4Z7CytacUVHlR5r3V%2FGhhwIhAMvVoS9k2CcpbDJkr%2BDB%2FBeTWW7PXKCGEd4ScQRfIJgDKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6ZjqhlCwHbnh7Rrkq3AOnY3O5QDelX%2BjPbGz7XiqAbvR3NcR%2F%2Bzfbj58rgkFijVnb0Th1a91avOB%2FUtWaWqeSQNvM%2FjDeSBPeTxDk0dK3wLzXah1KJuW1v2HCOFlV1tBtnY564EKxeUEE9OypXgajXDH2CDw996WuNB7ZTSyiw0tFkmsNNGT9q8ZUNjTPetq%2BAVsucDEBYd%2Bj5Tp1JbYWqvG8fgrMMiJQj6bQyl3wTigli9tXVq8VK5x1Ysi%2FLPyF5yXhzVW2rIBH7pek%2FIgb2jkqHxA9s1jOLXl7owKZkdvGz7qAPE1SeeUw01RqGnZOZ%2F38aSmtjegpHBRuHjw7ZiMCTElZfeHVHFMLgenzbUWJ%2Fb5iEOiKlYilMtXNwKc8FaXOVB3%2BvNV7qPe%2F5P0mFqih3JrtHs7KXlRGGWcQ1fp5kRlzW0%2BqCMTop7hxezEAFjrElbQXNFUT3D1ONmL8NV3LoqtGJyL6FccvNbrZXlzqKlk478UnGCp85x239vo%2F%2Fm764mB7505y7hM7IN3wFI1jJgYZx1LHVuLd5u530Y70DPioBkdrDGVRrvIzjj%2BVR4mcWjvutObX5Zk4B7IBK7I4xdvrwTyUl75awDeIJ6mp5%2FhI%2F4vCFO0We9YzOua%2FVG0K9GPwKY91dDCP3%2B28BjqkAeOBKIqWK01oMqKwVNwOTFQ7auwmWWxeuESuePSLAi9J%2BIMn5UgkJ8gf4HDyBhSPcTJjvQMVQX2FEETcTB%2BuFO%2BleGzkPDJ1KYykIkqUs9E4kZifnHZodZ2NF847Dm%2B0uMIl3LpSNXPGxwptGrSkHW3sEwgVvNhRp4WXbm8oACIrMVg1SdIxKdKGKAQlCUtYkC22w1nJJSA7Lfj7RklIxP7GwkFN&X-Amz-Signature=be652e390a3aa85105050fa279da40fb10442ff1b13585b0c30a30eb3cd975c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLCYOKU4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnqwM8kZ6kCa0cI4P6pK9N4Z7CytacUVHlR5r3V%2FGhhwIhAMvVoS9k2CcpbDJkr%2BDB%2FBeTWW7PXKCGEd4ScQRfIJgDKogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6ZjqhlCwHbnh7Rrkq3AOnY3O5QDelX%2BjPbGz7XiqAbvR3NcR%2F%2Bzfbj58rgkFijVnb0Th1a91avOB%2FUtWaWqeSQNvM%2FjDeSBPeTxDk0dK3wLzXah1KJuW1v2HCOFlV1tBtnY564EKxeUEE9OypXgajXDH2CDw996WuNB7ZTSyiw0tFkmsNNGT9q8ZUNjTPetq%2BAVsucDEBYd%2Bj5Tp1JbYWqvG8fgrMMiJQj6bQyl3wTigli9tXVq8VK5x1Ysi%2FLPyF5yXhzVW2rIBH7pek%2FIgb2jkqHxA9s1jOLXl7owKZkdvGz7qAPE1SeeUw01RqGnZOZ%2F38aSmtjegpHBRuHjw7ZiMCTElZfeHVHFMLgenzbUWJ%2Fb5iEOiKlYilMtXNwKc8FaXOVB3%2BvNV7qPe%2F5P0mFqih3JrtHs7KXlRGGWcQ1fp5kRlzW0%2BqCMTop7hxezEAFjrElbQXNFUT3D1ONmL8NV3LoqtGJyL6FccvNbrZXlzqKlk478UnGCp85x239vo%2F%2Fm764mB7505y7hM7IN3wFI1jJgYZx1LHVuLd5u530Y70DPioBkdrDGVRrvIzjj%2BVR4mcWjvutObX5Zk4B7IBK7I4xdvrwTyUl75awDeIJ6mp5%2FhI%2F4vCFO0We9YzOua%2FVG0K9GPwKY91dDCP3%2B28BjqkAeOBKIqWK01oMqKwVNwOTFQ7auwmWWxeuESuePSLAi9J%2BIMn5UgkJ8gf4HDyBhSPcTJjvQMVQX2FEETcTB%2BuFO%2BleGzkPDJ1KYykIkqUs9E4kZifnHZodZ2NF847Dm%2B0uMIl3LpSNXPGxwptGrSkHW3sEwgVvNhRp4WXbm8oACIrMVg1SdIxKdKGKAQlCUtYkC22w1nJJSA7Lfj7RklIxP7GwkFN&X-Amz-Signature=375604395622bc5216d76e8d19115493c04ae443c1ac4647abfabae4c84a2916&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
