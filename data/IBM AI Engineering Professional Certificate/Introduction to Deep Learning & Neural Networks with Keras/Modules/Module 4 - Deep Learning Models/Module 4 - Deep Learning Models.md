

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=7b1022ed1a831b14db8097fa61fc389b2ec14f39226fbd3a510388b31744aeee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=6f7d98b0662e17b8836c1ef5af48beaca56a55162a7720e5572b4de287adb94f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=a7b0db7d2395afa3b62fa38fe81542de4d3a0b32c88b07f909433b91eeb36ad9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=1aa04e2270f0e9d2cc77dcf929c1f0c1c3e44170ff460284d4897ad7e9c32029&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=ba70850ad85cc5e8e1ba3246a8255fdd918e3e793cbc7501ad35de1ff161adad&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=0edc641109f11eb328d7350c5ab1bef952a352b38c752bd07503eacc61352656&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=20dd945bb33352436d86e7aaee2daee8cce9f6d93cfc493ff5b7741939fb8eb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=3c4dab858d1a50f3ae403823035e7ae9d88661d4332cb500e14ef6bf411ad4ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5A7THZR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwHkOSPZ2zvv2r0YiXMMsPHEzsxBReIhJuGGTJ7jSFRAiBvs6hrulupDNbSoXAqty1pI8Co9SADKPyv2Di0WLx8FSqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMai8krBbdbleJSy1wKtwD6grTDyxARw16DMGLuf0ceqNjAnfrNIFUqAj8zDyRmJQgCJzDV7xCV1mHJcSCBBbcoAJjCcl2X3tnlxCsJjye0%2BlUfWH5dRqkeGyGUf2RBE3Wg7aIPgjl%2BZWNC%2BsSVm7BLlOIZ3J1hUV%2B1MYl3tz3FGF2E8%2B9q8sqB7mvqjoD0MPS%2Bunp3TJJBwyjJ88JZKhXtc9ZzVSVygBSjRHYyjG7Hy3iG1ooOxOFcTIogOVAfPMHOqjs%2BDyF%2B%2FxWUYWbq1G7qyKFnYJtnC6B4X5H1b02pqEbS53K1jS5NChveYd4xZ67QfZeC9DDPZVA9aVyd7CYl8hke1WAIrhNU0YUKKtcqiHeiSWziQcW7g%2BrHrgYxsYc9CkawodfW7u2vMVjqUWY886mJWQoWkoec3vPY3pTL2t0sAFJ6YErzfZHhg0QmevIsaQo1tbYkkV182xOrkQygdbjtgvPaDfDsn%2FsBsoJ2USd3GRhDx%2FoFYGCgX5mGvNETwSWMuRuZ0tlZcH%2FFdPFmKLvHiFXIsnFRSl6G1JecnPpoM2iUMzcfUwh4htBibF13S0qjR3gOdVUIgwE6bmKEOYEMEwP1%2BURB%2FWcDi5QAB9MEV2YzqOHXQClsqmo4rOQ8q1WGdlFmkn74D8w9ZP6vAY6pgE9UIgbzlEtKwsMcFcnbmvGt33aZbcV83qCynZuAUWKJ6%2BelWV2bSlqoDegSLSh6fFdtiVu6XDJ3Av30aQHddiRM2PWK%2B0t0QqQLyd3%2BNa9UNUN65s9cnGqS7w832TwcOUpLX2hV54hVsMffxAEYaw6R21NsjQC1HNpVk6kCFKfYWS30%2FL%2Bs57coK5tF5vjTc0y67mI9Z88nBLRws2JvqTFeiOzQjzf&X-Amz-Signature=b95acabc3f6f1f5f16dbc9956285b1f050dbdd51ea374e866519232eb23a82b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCTRF3HO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIElwFkq5KibI4nxB%2BKyyke7b%2FqcL97szdCI2gzFRMFhwAiBW129p%2B8ZxhKP92mT%2F7LbtoK8n04yjw8oAmNBwub6%2BKCqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFU0SaTUjIgB6u9%2FFKtwDBNwuLa6IrFsND2NEDslRgc2NvnZVb2%2F3g2zM7YIa6XlHAGsHaFZvUnvkOi7d5oVrTUlG71n061nBQrwzH0eS8W2KZ5uzt84Mlwsj1o0Yf1%2FcrfweFYrdraPVSaTep5zBVaxBqWI%2FVsdLPI8Us15DSVnVSbCvt73UeG4%2F6VsjlxFhsrX7GXutVRX3nkPX9iHiS2H4cgQI7c0FSvnCN0RPfswGbj3E5Lle9X5EvDdLMm4bLdMkmXLUIFBsxUktxYrg720yu3QQ18CNsdLCU4DfCu1k6Dht2wFTwCt8PMIZQWP7zFR%2BwBol9qCMqyNQiDl5yiXeL2SMbRtzeC6umg726Z0hFdeGdktVFjg%2BfYklz0jiV084EmQHpRtxSGzBTl8jrowjPHDGrs0k3AzUwaoqoqGHdm%2BPy1LrL4dprBiFqdWQi4NeRcb74RV9GKtTQMIHyf2DyCNROTDYzKwLbKk4ww5hfR8Si6G9svG4UKm%2BHijHbDBgYkERGwIrkPjpQv2GAa0CEJhEPpt38pass1Kh5xBl43%2FYVe%2B4P2KXglYmgt0wksSnt1JYIU1tHftvQT8x413FtTLVwGq2o1PX2DLEgEa2thTIXgZ898wMnUt28u0KsRp5Na9sqjjzdvcwh5T6vAY6pgHUwMWXt1dXVbkpGfuFvz763C7QoNbnnNE870dlfWI9ugGsCWqMs7uY36I5o1n%2FdC6GAfW13peKqnFh7zCPCmXNUZsXI0GQB048yZbHdvTrfgORxsLcsYin3g8KeQ8AZu49FM2DeeMAIOfQGmP8j7dRFfNBP9n5ej7gOjUQgdkM08nwybD5gQDWmPfeJ8vxL9rKW7jP6HE%2FfqdbGgGsYeUTb1dwHM%2B6&X-Amz-Signature=25c251af81cd588b8b9d7d8e7b61531717f2f37ca8fc1b47a17ca41c8893014f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCTRF3HO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIElwFkq5KibI4nxB%2BKyyke7b%2FqcL97szdCI2gzFRMFhwAiBW129p%2B8ZxhKP92mT%2F7LbtoK8n04yjw8oAmNBwub6%2BKCqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFU0SaTUjIgB6u9%2FFKtwDBNwuLa6IrFsND2NEDslRgc2NvnZVb2%2F3g2zM7YIa6XlHAGsHaFZvUnvkOi7d5oVrTUlG71n061nBQrwzH0eS8W2KZ5uzt84Mlwsj1o0Yf1%2FcrfweFYrdraPVSaTep5zBVaxBqWI%2FVsdLPI8Us15DSVnVSbCvt73UeG4%2F6VsjlxFhsrX7GXutVRX3nkPX9iHiS2H4cgQI7c0FSvnCN0RPfswGbj3E5Lle9X5EvDdLMm4bLdMkmXLUIFBsxUktxYrg720yu3QQ18CNsdLCU4DfCu1k6Dht2wFTwCt8PMIZQWP7zFR%2BwBol9qCMqyNQiDl5yiXeL2SMbRtzeC6umg726Z0hFdeGdktVFjg%2BfYklz0jiV084EmQHpRtxSGzBTl8jrowjPHDGrs0k3AzUwaoqoqGHdm%2BPy1LrL4dprBiFqdWQi4NeRcb74RV9GKtTQMIHyf2DyCNROTDYzKwLbKk4ww5hfR8Si6G9svG4UKm%2BHijHbDBgYkERGwIrkPjpQv2GAa0CEJhEPpt38pass1Kh5xBl43%2FYVe%2B4P2KXglYmgt0wksSnt1JYIU1tHftvQT8x413FtTLVwGq2o1PX2DLEgEa2thTIXgZ898wMnUt28u0KsRp5Na9sqjjzdvcwh5T6vAY6pgHUwMWXt1dXVbkpGfuFvz763C7QoNbnnNE870dlfWI9ugGsCWqMs7uY36I5o1n%2FdC6GAfW13peKqnFh7zCPCmXNUZsXI0GQB048yZbHdvTrfgORxsLcsYin3g8KeQ8AZu49FM2DeeMAIOfQGmP8j7dRFfNBP9n5ej7gOjUQgdkM08nwybD5gQDWmPfeJ8vxL9rKW7jP6HE%2FfqdbGgGsYeUTb1dwHM%2B6&X-Amz-Signature=a8fab78386de6b70c53c0efc7e7e5c5027294ed306095140dc57c3a608076446&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
