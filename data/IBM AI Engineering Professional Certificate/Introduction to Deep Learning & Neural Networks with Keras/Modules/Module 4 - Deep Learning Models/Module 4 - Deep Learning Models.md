

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=2abc4430a85d5e8f9652eb7418172bd463763d032b1b64c58579256a36420910&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=4535b400782c4dab438606fb860999e96d7b22e2d04629ab57d4a62037ba3313&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=35a3823109318bb6642d1b28991e1067a14e37244b0b3ec39f8c94385f41b3c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=ee6703745a36bdf0f055a5984bdbed8341eecbf7f8ab76cec2d865befedd29db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=25b1d58d07c222869e0c28938280d31c7a7f8f7379b5fd4afda25203c9584050&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=74193eb12294856288b90c222a88db84604749bef14af2bc60fdfbeff74afe13&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=b15ca8d50eb753d0d6a53020de7017e799bde2568ed9fc8156b2a829e813a51c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=160a6ba4a9820d02be489500398ffa56ead72a79cba7ed6ca01706e25a329486&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVUYICET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDAvh%2BDBfnwuIXN1L5t%2FtlJn2cVvtwNdsXbpQG6eovOfwIhAJlPLg4Bx5D4LGo7QF%2F2eJs3oe%2BmQhpcR41bL0xue1%2BsKv8DCDMQABoMNjM3NDIzMTgzODA1Igx%2FnMeoId6pa5g0Q%2F4q3APe4%2FiGABMDkOPuONZCtR3iBqwsIvQBHrxjuaKFJ%2FPYHmFuv5GZRPjT6jAw%2BAReFF8BRyy5pwqxKBUfJA3x9ayMiob2vuwGQnlTzOeL5IqVkqdnBjxKXEu0qkmgO9c1X%2FuTUYukZyznO3YT7bSbSDOIG5iTK1gddeoS1xvoVC%2FUiZlIoem1IHjaqhPbXUffrKx2dtDVAi%2FHd1qCAcEICBZoYU6CoXVCVgFbpCaDZhTeyMQW4P7UyfVvqs00c%2B%2FrOhzUev5D4dG3NghV%2BMVWnlf9AZJ4giaSCe9b%2FrMHlg5yUQS%2BNIlS9XQt2rHec3sV4CHN9Gxdfm71%2BOQ8CIssBAdqPQQuxXQo3Y5mziP25pnmMaKuwN5AcUUD1QlS1%2FhTwMXQoGlFgEIg7i4nIK9Tt0Pld7Yvlbvd7%2Blt5HqfFGjcE8utKqDHaY5SRN7Pza6z1TX9M078rMeDgYPANPgAu9b4%2FpG1yBKih%2F9INc3sSCp%2FGqmt5%2B%2BaiLSaHy0KkQZM2uKNw1Jc53fd2fEZIdzK1p3u14zfKa31wKDK8a5ceVM543LSCkpLb%2BpxgPjBUssu40PxTIQnqeJthF9KL4kJzYoGusqLprnYUqrWVcudXFc9Azhr8B0n0MX%2FAPLYJjC4oYm9BjqkAbtL%2BTaE5sEfBIJmOzjH%2BM9QzJ%2Fqkh0gaPXTgrtQgQH%2FOj2lI8IDaAcoiSjgUlYLNf6L45nAt2BJDh74j46EnBWgN%2BNMkOUvKJTlZEOWOfK8QScUgLmQTJeYpYc9zqoPzjD0btYrB3hWOQxwPglb4XlzqW1YCRxk%2FIigWsQI%2FiETZWU1ZZlvaLe22QvSd%2FTxjJk7EPgPD9TUh%2FGX3MHbWtt6fTG%2F&X-Amz-Signature=9aabf659900fe0432634fa3eb5787a1f605b0d311e73d5bc39d7311ad6ecdc92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTSC5GM5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDuNsSsk6vDO6cBnMYZL1y4SWGJsBUDddRqcej2ox9Q%2FAIgAJL2liBcDJhNFUWHoJzzxJ6hxQZD33OKoKMkZ9SNOqQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDODxcvWJ6KISTH%2BidyrcAzxl%2BF8pvJifk9k93%2BMJLvAqfJdJm%2FMzSo%2B9RQRDwrK6ThFbSs0vuO9p7JR5A0n%2Bjehr%2BY1eGDW%2BMcP4Y0DBglqgNbuOXvjZsXPpZVQY8CfiaEH1jsqEttkrSCw5%2FsfyEa25uO5KXjEv6uTqIh22Z6dFMtu2QHn303gbHp7dnBEYJK8cyvZm5DVhYU3%2BUAP7VwQJP0NYx3O918iPs6xzUb367VxvD%2FDHnwLAQNUmyh8tQxP1rSnOd8EwAhf1rrpXAFRz4RPANU%2BWi6reEbSFRua6PoMCpenX9VaTXC4fhEMCsTvInPcQBf4%2FhnhYV5rwQKssEU2MEd4%2BwgPBffL2CO8Y4Hj4hRi9WvSAx9MRu3iKbZxGu9gDfa%2BtaBTuVFYpE5nmqf7P7fnefi2gB5gFr%2FfXP%2Blo3DG4%2BhmQBuymv5Vruec%2FyE2%2BWk1ByJcRcbmuIoQxSxkv9O%2F46bHN0mkG5rbsRS1tq43rq%2FFOxQaxsKhLS3ZQLTmd8a1y9lqhV8%2BTSHsOeXioB4JC%2B%2FBROyN7uvhAJk49kNAnvh356aFi1F0ibq38cHWZ8Xz1XBGIfl8aIGIHSj2fARigUB107WbMpHaVrm9r%2BL9vHanU3XTdpJAM0ePxBl4oZeDvnSW0MPCiib0GOqUBlAYsKcbP5R776PxHY2VL7%2FHOpbZm92OIRi4cj5NdflX2OS71WJYvPJMTSL4rrOq6AQJwpBRyk8cw28sxEhAvtFtm7%2BVs%2FdxgbUlMKJULDpXRtPFadkQCPaKqAJd2cBAhre8MzRmelKznT2HGxDdTDZ1HYF94HsvoxvC4QDLxK%2BtBt7185UIp%2FFWF1BQxlQnztDvw5TUQ4v9JJonwSVCeaoYQ3mZQ&X-Amz-Signature=b5626d88cb2e7f80f1d176ca2004a929558831ef0c77c14baabc4df69e0846e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTSC5GM5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDuNsSsk6vDO6cBnMYZL1y4SWGJsBUDddRqcej2ox9Q%2FAIgAJL2liBcDJhNFUWHoJzzxJ6hxQZD33OKoKMkZ9SNOqQq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDODxcvWJ6KISTH%2BidyrcAzxl%2BF8pvJifk9k93%2BMJLvAqfJdJm%2FMzSo%2B9RQRDwrK6ThFbSs0vuO9p7JR5A0n%2Bjehr%2BY1eGDW%2BMcP4Y0DBglqgNbuOXvjZsXPpZVQY8CfiaEH1jsqEttkrSCw5%2FsfyEa25uO5KXjEv6uTqIh22Z6dFMtu2QHn303gbHp7dnBEYJK8cyvZm5DVhYU3%2BUAP7VwQJP0NYx3O918iPs6xzUb367VxvD%2FDHnwLAQNUmyh8tQxP1rSnOd8EwAhf1rrpXAFRz4RPANU%2BWi6reEbSFRua6PoMCpenX9VaTXC4fhEMCsTvInPcQBf4%2FhnhYV5rwQKssEU2MEd4%2BwgPBffL2CO8Y4Hj4hRi9WvSAx9MRu3iKbZxGu9gDfa%2BtaBTuVFYpE5nmqf7P7fnefi2gB5gFr%2FfXP%2Blo3DG4%2BhmQBuymv5Vruec%2FyE2%2BWk1ByJcRcbmuIoQxSxkv9O%2F46bHN0mkG5rbsRS1tq43rq%2FFOxQaxsKhLS3ZQLTmd8a1y9lqhV8%2BTSHsOeXioB4JC%2B%2FBROyN7uvhAJk49kNAnvh356aFi1F0ibq38cHWZ8Xz1XBGIfl8aIGIHSj2fARigUB107WbMpHaVrm9r%2BL9vHanU3XTdpJAM0ePxBl4oZeDvnSW0MPCiib0GOqUBlAYsKcbP5R776PxHY2VL7%2FHOpbZm92OIRi4cj5NdflX2OS71WJYvPJMTSL4rrOq6AQJwpBRyk8cw28sxEhAvtFtm7%2BVs%2FdxgbUlMKJULDpXRtPFadkQCPaKqAJd2cBAhre8MzRmelKznT2HGxDdTDZ1HYF94HsvoxvC4QDLxK%2BtBt7185UIp%2FFWF1BQxlQnztDvw5TUQ4v9JJonwSVCeaoYQ3mZQ&X-Amz-Signature=dca6393721f40e86b0c832e5561dd9bf221cf63900d4310164ce5b68ed5485f0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
