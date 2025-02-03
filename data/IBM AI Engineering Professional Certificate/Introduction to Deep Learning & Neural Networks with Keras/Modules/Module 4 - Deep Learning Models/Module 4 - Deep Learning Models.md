

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=3a8a1d5dc41a7bd946e3ecb92d37337f38042e61143e3bfc9454646f5ac3aeb8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=c2d606af500ff090f6024620e7bbd498b52f2b97125bb57de5372691e4d2a7f9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=9bdccdd801c316f8b4fea823da9c10eea45c537619abb45a67e115edcff3e31a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=9e76b4cbeba894db220020c0a09d655adf40908b46484add379b4be4f22a3d49&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=4f02d33b2854286ee8fe869c177950b53a1c3d47c9c4350bbe2065d9cb18aa3e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=b65dcc6e7146f36a8573529c20ef20eba5acd06cc02b4d01ab54b2dc3d91c0da&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=603fa40b6d9be47658ccb45e1f81caf0883aee8ac347763ed9c50ed0a107e3d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=7e588f622697686057a29170978c57cf8e8fea506580e7e3d43936ace0c88153&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3IR2K3V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYEnmhaOww23%2B96H%2FST%2BW8iphk0bozxSrGOdU7LG%2BSgAiBvSmtgcIYsXHMI87HNk7c3UYFq8fUx%2F3Kv%2FmYfTq7Soir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMAFigcWyiFVMMHPw5KtwDKF3McFE3nTcgy44DQvjBCv5V31%2B39Fzjdo7%2F868Hw4%2BMIKJU9QczjrDYPEuWIztk%2BUgxFWkIqLf63rBV3rhDwrX%2BCbn4Xhg0XghkXc7Gjs4eZvzcELEa6jvU4rhB5BsKUmOIb4HG1lg9lYAuIfqnyaIl%2BGopQS8xvYBBDyS3dkGqW50WtBQz2MJq3PUDPc67ZFEqu8HLkd8RmeBO4D8LP0%2F0yGQH92eRrYCYOcDOyZfCE1hWhbgTvQNwvBA4ZI1ERpYgM%2FV%2BhzBjhVf3VWrBn2sZrCXz8t%2F5X6IUQn4kKVJAqYzd1W0IEY8PL95DS0eBOu7VD9G9DuzVwqxWSq02upgT8sY0IIxeVwvwXoXx2LXuEe%2FC0LgYIb%2BZZthLtvH8OLOoPEoy1z%2FB3HLkQb6ZFsHfTZK9qCk3fZYlUmoFm1EMmioJ%2BGzSx1kNufLkY45EsnGn%2BpS%2FJFPZFjvx9MMn1NFTKRLdzD%2BFrngUbxZ%2F0R%2FN%2FSVU1qrJZbOF4UK13892gVCzvsazJ6O4LUo5LD4H91vpvpiF36qBhS%2B1bVvU98jW2e8mGu1xhe05hxbsCvb380cYqbsWWv9LhrROt30jdn6frNv886OB%2BTO7BryAQKsSmz%2F%2FdnMKDMlltU4whbWCvQY6pgEXPpSUdLG%2Fn3iKTMYbdEqfDRPMuj6zX8cCBpdW3shrVjhPozx%2BiRMlKSPX4aMHQoqapah0UtKpL11VC4qYtrtYEQ131aUpPs1SsnJTSEuLwzCV56AEvv3XKwZURIlMNoX2b0bAqVPRlvSUMSwDaQWbVjMZmhY8DvjU5CzHS3MqXJXX8BWXt0iVNQzZpXRx0WgIP0R1JVi1K7tUndNz6vWUhXGZTMWz&X-Amz-Signature=bc3f904f8da6ebf7ea764f1be6ca1262ebed15538236e1132cd841179272ceac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAVJR7J2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0Qm4KM7NQITA9aD0J%2Fmb9xsco8kLsnr%2B41D1XwtPLFAIhALqTg04YlWjKnss9cc6rOTXlnbBYfcbYJvXgtVSCj%2Ba8Kv8DCBMQABoMNjM3NDIzMTgzODA1IgxoxFTH9Nc1doiuhDcq3AOAyRjBuwt23bRBXRbUURA0ZpuAxVh4Gx2wnQgzxZNeYxAUn9TrNxYoubKl3%2BTKQzJhwQ029bnT%2BXGsfcTMWFAiQ8TyaZ1A4mvJsmAA2F8OcroptED%2FlhsCmYfiQvcdq9ly1wKERQGEFKxGZ3ctGM3D08I%2BlJkCkF%2Bd906FOBZF7kLMiHg1YDtP8Go0Azk724qYa4zNlp%2FcqP4xhXtmyN%2FN9XMq00qxy%2B3byRdKyqRgZ8sYh1PDV220gEmwYpWPP8g5tw%2BBqb503vAEy3%2FVhHjz8V2uzZeDMIc%2FORQEj3510YokJ8mIvanBGosckwcjrmPrhC3cPTo7C2Xgc5x7fOCEm0HYnAgWxVzqsBNjLwsgxlDenX5%2BMIJBO1DN2isookTqxYRfBBcJvIhpxhOIjcZ4wTjbiLmgXW5T5UBKksdRo7uVR2orWnbwLigGUe5DRq1TlOViXSr8xgwMfjbaW1KXlWKD92eG%2Bl5Y3aLISqmKGVuD4Uqa%2BGkBEG44GHQ%2BJ0l2GTAgSyHdEHJS4uiWEFeET6DttAhZXyRS8eKGhMNBR8Sz5sSwVmhDVPQznOIQoEX9pFz8eOCdkuOMUBonqqS1JFI4BtMz0KbGxaLyMb%2FKwkoNholL2Y%2Ba56zivDCEtYK9BjqkAaUTR07TiRdrWb2uPDN%2FNNuWlwFt%2FP9BHI2eMmjdfxt%2BYHXCTa69vBmLyTp6zlIqFUTTCHVkKAi5kXZGC9DsfKzICOpMI6UcMjydo3%2BEiXyB5Awy5QSCwRstmWFXYqsV1N%2BEaeGY4%2B09s71PQz1c1zBZCyXbjrFlWTxIZihIiExm2I2GkCpHfK2DJ2tZs%2Fs%2B2oSJ9dX%2B%2B9zTKq1EBRzG00LPp1cz&X-Amz-Signature=ce9a0165d1f5c67538fdf327e79080e3a7351faa3850b27c72d7bbf5a5bee5da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAVJR7J2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0Qm4KM7NQITA9aD0J%2Fmb9xsco8kLsnr%2B41D1XwtPLFAIhALqTg04YlWjKnss9cc6rOTXlnbBYfcbYJvXgtVSCj%2Ba8Kv8DCBMQABoMNjM3NDIzMTgzODA1IgxoxFTH9Nc1doiuhDcq3AOAyRjBuwt23bRBXRbUURA0ZpuAxVh4Gx2wnQgzxZNeYxAUn9TrNxYoubKl3%2BTKQzJhwQ029bnT%2BXGsfcTMWFAiQ8TyaZ1A4mvJsmAA2F8OcroptED%2FlhsCmYfiQvcdq9ly1wKERQGEFKxGZ3ctGM3D08I%2BlJkCkF%2Bd906FOBZF7kLMiHg1YDtP8Go0Azk724qYa4zNlp%2FcqP4xhXtmyN%2FN9XMq00qxy%2B3byRdKyqRgZ8sYh1PDV220gEmwYpWPP8g5tw%2BBqb503vAEy3%2FVhHjz8V2uzZeDMIc%2FORQEj3510YokJ8mIvanBGosckwcjrmPrhC3cPTo7C2Xgc5x7fOCEm0HYnAgWxVzqsBNjLwsgxlDenX5%2BMIJBO1DN2isookTqxYRfBBcJvIhpxhOIjcZ4wTjbiLmgXW5T5UBKksdRo7uVR2orWnbwLigGUe5DRq1TlOViXSr8xgwMfjbaW1KXlWKD92eG%2Bl5Y3aLISqmKGVuD4Uqa%2BGkBEG44GHQ%2BJ0l2GTAgSyHdEHJS4uiWEFeET6DttAhZXyRS8eKGhMNBR8Sz5sSwVmhDVPQznOIQoEX9pFz8eOCdkuOMUBonqqS1JFI4BtMz0KbGxaLyMb%2FKwkoNholL2Y%2Ba56zivDCEtYK9BjqkAaUTR07TiRdrWb2uPDN%2FNNuWlwFt%2FP9BHI2eMmjdfxt%2BYHXCTa69vBmLyTp6zlIqFUTTCHVkKAi5kXZGC9DsfKzICOpMI6UcMjydo3%2BEiXyB5Awy5QSCwRstmWFXYqsV1N%2BEaeGY4%2B09s71PQz1c1zBZCyXbjrFlWTxIZihIiExm2I2GkCpHfK2DJ2tZs%2Fs%2B2oSJ9dX%2B%2B9zTKq1EBRzG00LPp1cz&X-Amz-Signature=92135bf64d5e7db5cb70a9ec5490150911f7e097ee055461c9261db5131d4e9b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
