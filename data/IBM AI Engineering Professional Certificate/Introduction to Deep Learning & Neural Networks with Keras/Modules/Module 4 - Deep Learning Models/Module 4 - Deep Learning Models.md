

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=db26ec23249dd72a8df4473119264341b15b4ff377204d012df4a35a7ae1f586&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=28c2d6f49f77c74a29feab5897e4237cab09fd0830abb4f7e26856ea28f8b4a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=d8c5b8ea589408ac2a9d4a76ef56eef3f9ec510865f8b092a696c6c454b7c5ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=069fb3098d57b1dfbbda63fd58407f8f28fcaed5c69e7aa9551ca9c8303a4b00&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=c2fdc4893a0a2704992d7f17b4dbfcf8921bdf1753b7d80681745d1ee70d884e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=c03a860af12811f17754b11047c132fce9f3939e19cefd53bddec64818ff4c0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=4a003660df975d54e48a75d3d706bbddb6d080cc016642f90945484d0273c5a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=7b4255212ac496afb2b5a98d1fdcfec93c40555f97506044f892ff6fb699da58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOGAVRI2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQClu%2B5r0PIQTPbeWqNSGR8t4r3tnP9%2FcQUmzI0K28NZUgIhAKOcSVkC%2FfpJXBkeeqGAG%2FeeuvfQL5i4tDClLcKjzLtkKv8DCCQQABoMNjM3NDIzMTgzODA1IgzjPMZBR8h2GAfW1Rkq3ANiTyOJBaxZ%2FKwtn90a3aMrryGepkor5Lj4hmq2sqKQlDNdlDBIJwh61LNPdoaExsLsBTa0xA1bQ0cps1T2ADvL0LXSY%2FbESlsHtrIKkXlVUTw%2FE8FxuAOxd2YDsPqU8BIVdV94rz1Oscs9UTqjmsc116kfX5b%2Fgqgnpq7R84ZQVH1myoBnA8RiWTtq05RUeh2BvJ5lO3xLiWh0ftwg75ghu%2Bn8DosHK84Ssg%2FfoHyS0p3ts2JdQNoV7for5Rtzs9ocuZFMKt%2BUTzvYw4rqnINbCiEknNnby1BBKT85tmnK7DRNQzQvRKO%2BuYG%2BSNgfXx64TAtd1nBkfDfYwfF2lvhfxB%2BlmD0YLIvIrY1Arxe%2BA%2FqQuIDo1KnQh2q7RsiB70LZ9rvk%2Fv9syc%2BeibflYP1vKeDzraRQMjmzy75cYKgtM2zqzmQGaoiFetjN48ydjs0Dh7J84hj8w7C9qo2ebN%2F8hSMMDtEZSO9e8VAxYB48ERvCa1R%2FF9oJTT9Ip5lCvH%2Ff0Qc9lDxaEeIEQbbN%2B5z3Hr8LlOAVEWpledQo%2FDHwWJIB7010OZ4GGZG%2BFIflOaIndNVQQhETaSW82GuiGC9BImloXOGTg%2Bto%2B%2BsTbhussmejcccujZljaU7vvjClhYa9BjqkAdKb8SslpSLVDBdsnu13k4Itq5FBGP0w1hM4dhEXU8UanrV%2FIb48PIUpM197Rsck7kbkibIZHCL%2BQmtA7%2FqQJ9TSlTpn6DzEh7PEqi73m3e3XnJlWMcAWSGkafY4Ts9V6eNjv1Mv8et%2F7a7n68r5EFyxlkcdwyLjf8T7UpDFrddeCYf6%2FGx5c68K%2FKNwloC8zx%2FzjTjQVEcnJ3%2B8MPxq4RImfJ3q&X-Amz-Signature=fc075c2005778c51915c3dbcd0522db27106eab496dfdd7dcd46f02258e34016&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634AWFRWW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIGX%2F6a78noq82vZSgh9W9vpPPENnyOm0DehZeY9ENMyiAiEA92BuMo5yAS8mV1gVAELMdodlrwY%2FWyLuIMgOQfPr27gq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPzPW4TCqKJ2kQd7uSrcA1gQNawN3rmvBLpPONSpfe8xBnYRa9ZYlf1jmUrVYe62NTHwK2XO2uvb3twpaiifmLGJdmfMUpXjgoHk3EqMELpPROgeUZDme6oyk0TQ88sg%2BA7F6M2RVqEB2wMA%2BP%2F%2B9uJbYykl6Yw%2BqcIvtIVQpT2naXxNhmbKg9wLaivFYjPkIzVplX5UBGzM8HEiRCoJOmInD5mlcbv2nT9kAtJQ4%2BsbivO5zH9B4DqoOdJb6ttFPGDDBcHl4sDIoEz1bZhvE%2FJeRWgpy1lNkdCbDAhIKojwYAQyjshOm2WdUmSpVtzamUq9J6VO0fjxzOESAxXr7H74YJTTVszvenwmR04%2FdcTAcbDQP9s2dgagRXtiDR0qtFtDlxEaJ1GYJMVIWVafjhWy%2BdgZfBp1bI%2B8WsY00v8z%2FSCvY%2FDGLmDIXmsH8PMBi3xd7mbdHZYtyW2rQSwJhfKHMYM1sghh%2Fj18wRdQsyNMBjZKWcvuSRFXdRpaZ0jcFOLn7SY6NuL1PjqTIZhmT8iayIaf84U5QHSiZyoGgFoItwxXa%2FFFkSYZHq7HtN0m1TIynmdYOM6K9UPKBLBfAayI%2BW7Vu0nNzXJmH8nQ7ng3DnFjovNeC%2FQzxouJHytPaeg%2FosX95RItIc4%2FMMGFhr0GOqUBJV9w04NSEuULDBIN7VRLUQC4sx%2FGsXFQfhWOUoEyM6dfFFVO8o3rMiOeKJ4QVDOL7dYHeeDvqRGMaJZRr%2F2nxxLRVaP3jQFrn2U2svVq3hH5tOXZBj4VnHbbwbLXbiGdBDgw0dYYuwUechfYQzmTBsGGfjRy2dSSH%2BmyC8Vcrh3NOQ91MQ%2FH%2BgQCiQs9IzPpZvyR7Y39Wr6WxXy%2BO33%2FGcfYmkDP&X-Amz-Signature=3772df678db31785b9ecb4f12255583f8ece0427583586d14dfe5b843cacf2ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634AWFRWW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIGX%2F6a78noq82vZSgh9W9vpPPENnyOm0DehZeY9ENMyiAiEA92BuMo5yAS8mV1gVAELMdodlrwY%2FWyLuIMgOQfPr27gq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPzPW4TCqKJ2kQd7uSrcA1gQNawN3rmvBLpPONSpfe8xBnYRa9ZYlf1jmUrVYe62NTHwK2XO2uvb3twpaiifmLGJdmfMUpXjgoHk3EqMELpPROgeUZDme6oyk0TQ88sg%2BA7F6M2RVqEB2wMA%2BP%2F%2B9uJbYykl6Yw%2BqcIvtIVQpT2naXxNhmbKg9wLaivFYjPkIzVplX5UBGzM8HEiRCoJOmInD5mlcbv2nT9kAtJQ4%2BsbivO5zH9B4DqoOdJb6ttFPGDDBcHl4sDIoEz1bZhvE%2FJeRWgpy1lNkdCbDAhIKojwYAQyjshOm2WdUmSpVtzamUq9J6VO0fjxzOESAxXr7H74YJTTVszvenwmR04%2FdcTAcbDQP9s2dgagRXtiDR0qtFtDlxEaJ1GYJMVIWVafjhWy%2BdgZfBp1bI%2B8WsY00v8z%2FSCvY%2FDGLmDIXmsH8PMBi3xd7mbdHZYtyW2rQSwJhfKHMYM1sghh%2Fj18wRdQsyNMBjZKWcvuSRFXdRpaZ0jcFOLn7SY6NuL1PjqTIZhmT8iayIaf84U5QHSiZyoGgFoItwxXa%2FFFkSYZHq7HtN0m1TIynmdYOM6K9UPKBLBfAayI%2BW7Vu0nNzXJmH8nQ7ng3DnFjovNeC%2FQzxouJHytPaeg%2FosX95RItIc4%2FMMGFhr0GOqUBJV9w04NSEuULDBIN7VRLUQC4sx%2FGsXFQfhWOUoEyM6dfFFVO8o3rMiOeKJ4QVDOL7dYHeeDvqRGMaJZRr%2F2nxxLRVaP3jQFrn2U2svVq3hH5tOXZBj4VnHbbwbLXbiGdBDgw0dYYuwUechfYQzmTBsGGfjRy2dSSH%2BmyC8Vcrh3NOQ91MQ%2FH%2BgQCiQs9IzPpZvyR7Y39Wr6WxXy%2BO33%2FGcfYmkDP&X-Amz-Signature=d31b3d10192ea8e5d15b2873f27cbca13e99e982e1e6965278b8eef873207b63&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
