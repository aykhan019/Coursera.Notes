

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=7a836cd469e6fff41d027770e29db2af3f4c78fdb4e377806f3726a73750a517&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=eb9e83eb5af7952978057d2b35048305c803d8d9f0c82ea9729c6025b71e173a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=2a8c43e5ee8b7935a217a10db528c7d407876573b2ed43e5a432bcaeaba2427a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=58c6c2b912f54230b4d507eae2f5148c0e986e0cc4310533021a5f01963ceaf8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=b0b3f06cb516527c89bee97fa5a826eeef7bff59c5755e63cf8f78044059b221&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=ba00cb0587e36b897358ca39c8870d1d4712580485fa9af56bb6dcee1be07cc5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=7ae01fdf073c4124b6c8079a2358c0afabfb2542599947da04620fe28accd348&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=cf12dfa3bb867779b45b0e44e304fe170bb3c5a3ba0f810101af1a1d53872503&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZK2W7FP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQC8aa9hntg7DPKeR75h2TBHLyeh8U7milBYg9uZpb0zHgIhAIXZbw9NwuZpdOEeY0gTjFSqmxsUkv%2Beh5AzlYnDgAFqKv8DCCkQABoMNjM3NDIzMTgzODA1IgyyKffSFrQfgeieC98q3APsdLXru%2B8fOlODhEh7VJwLz7bP4ZybPv6D%2FZywkEbSgqQ3oz9s2zC59koOBgDLyfTDBs7C%2FUqOFDdTf0wys30ZAgfzHxiQGiZuc15pm4K8nvtkeGGC9vUEKSxiaxDx4r9xFy0LPio9eEGD%2BFcprvG0Uc56DkObPDkewAmZHPdHTOTq87yWpwWKtcNBRRqFOcdOnV6NDj7i2VSR4a4O0woydpEurrZFc3WghJXqTiwCkReFtOC2UlKzV%2F5f2TCYq0JiuyZj%2BDIp7bqwSOYl3RhMHgX%2FmsHOp3836P%2BLuuJZLZPiWNwrTEzpdbseOiz6mTo7grISy12DPfk4NOM3oQjlXsGvnKBeg1jdhOSJI1mBLi6g2j1uJgYBZva2ehD5ZrfSCfTMcwb9RaS2VuIIy75PrhTuh%2FllICmZsd3mkY%2FrH7gqYXpHrFcQYSRgIEtZ7miPKxIc9auQEji9zCK79coatobzqLLmmeKUdQuHaW7YTC%2FfoDviZCDa7BoAN3xupHd6WUrYL5WxQa1KpAxfTS%2FM8G5%2BdZceMyfFBYAWXbAZrxen4czaioSbkSJ3KsopifKyjBwGklFKMna7Ax9l2NK7lmA7fJtLB%2FZSk83VJdss2MXlpjtjaLxlStYo0jDVkYe9BjqkAUPTYgVS36E%2FfqEY%2Btptc974XNup1Dg6LzMHMVUIJ1gs4tL4J59pHu7EMyG5752eHDvwUAJsymg2rWAx4XDuFNPw0tW%2BgOBw1cGVv1m1Ji%2Fw2HIsrJnDTLy79OyCNIG8XbOOGisQgboI0C%2BF%2BVbpXXKf%2BV7d3XDj0DlNWaP%2FK6G58l%2FD7qFIHjCNcWFgZqpQJfM1xAmgQkPoJ2ohhqEQ7DsVw6zG&X-Amz-Signature=610fd5cfa5c36aa6fc35171643aaea6315e983f36972af3f3d9cccfacd433e21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJ45MOMR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBQAkJHZhBCjODcvxj8l81MMms3qj69mx92mQcjgQ294AiArp4KwKnP2DCxwp%2FSFmkQmpMNYMr6IPCKrtloFzS8IySr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMu2bM5tSA%2BBDacDtcKtwDpSdCOVwt8fs6D%2FZGGvZJ11MePqkJcUaR7Np%2FrkE1ntEw4c%2BBtqk7zRMMwq9FumBstppjoFJxP%2F%2BuXOhlbiSJhvHfa9ARCLjWgvJsYfntXnsMrGY1nrOoxPkTUTbKXlnB1rF5%2BWhFBZUPR%2BR18CRcVl%2Bz0zjMbXEaTNiKKEht31Epad8vxN%2Bi3Y8UFewHRr89daevnmxp9XqFd6g6lbhJ3bv19HWIP7qjb3Ypp5VdXOyQzj4vTT4MN%2B7WES5RHNXR2kVSiM0dspOc%2B8hHxxNHyPvYD0E2eMaIL6RA4Rm8dsi5oPqqE2%2BMXMTRI3uOtXmgwMInNFk7SMVG60j9WpS9R2y%2Fp5fFVrlEOJf0qjCmqSGaPGZnE20jXKAX3kmxoQl2ZxFaWzncC13XpJ13KDtslDo%2FA3%2F5jSDFlYXqDOAoCllwpTocSqweJUs82ruMeuli0nq5w6zPAS%2Bxy9fyJ%2B5upy4LhURxm9uQe5FyJ0TpEyXV2Nx26rUrgI1zjibs1546B50byhEbIQpewOcTtQJ6Mc1GHQFmsuYXaiIXb2TGv7jnmZ7AN6x0E5F1vTPm1reSnj1I19CKCWAwHu7Y6r%2BSuRbfYLcnk96qTO%2FWZ%2BiRAHwO%2FTz8yeWzOWj8WVowm5GHvQY6pgG7xorIf3LGfhaujsXLwG%2F6A3974N24ZEtjKhFWMvxKATJvi7HX%2B5PWwzTbptv9uKaG8R6KbKyK05UefDP1moU9Yzqeb1tFIUUO3jvwuRjZw%2FqQQu5jWqf0ihO6XlhxHSEVpN7x6D6mmmWtPDW8Eh0dFczu%2BnKKP%2B%2FCI3wVqi4EBSQjkFAuFmrx6KBzQCcoL6WcxdIfeFzo%2BqScblIE7TvMwpwe7%2BhC&X-Amz-Signature=2dc06b0aa40944d257ad258b605bd00eda9fd203fa3d6ba2d135a9ca4ad88da7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJ45MOMR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBQAkJHZhBCjODcvxj8l81MMms3qj69mx92mQcjgQ294AiArp4KwKnP2DCxwp%2FSFmkQmpMNYMr6IPCKrtloFzS8IySr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMu2bM5tSA%2BBDacDtcKtwDpSdCOVwt8fs6D%2FZGGvZJ11MePqkJcUaR7Np%2FrkE1ntEw4c%2BBtqk7zRMMwq9FumBstppjoFJxP%2F%2BuXOhlbiSJhvHfa9ARCLjWgvJsYfntXnsMrGY1nrOoxPkTUTbKXlnB1rF5%2BWhFBZUPR%2BR18CRcVl%2Bz0zjMbXEaTNiKKEht31Epad8vxN%2Bi3Y8UFewHRr89daevnmxp9XqFd6g6lbhJ3bv19HWIP7qjb3Ypp5VdXOyQzj4vTT4MN%2B7WES5RHNXR2kVSiM0dspOc%2B8hHxxNHyPvYD0E2eMaIL6RA4Rm8dsi5oPqqE2%2BMXMTRI3uOtXmgwMInNFk7SMVG60j9WpS9R2y%2Fp5fFVrlEOJf0qjCmqSGaPGZnE20jXKAX3kmxoQl2ZxFaWzncC13XpJ13KDtslDo%2FA3%2F5jSDFlYXqDOAoCllwpTocSqweJUs82ruMeuli0nq5w6zPAS%2Bxy9fyJ%2B5upy4LhURxm9uQe5FyJ0TpEyXV2Nx26rUrgI1zjibs1546B50byhEbIQpewOcTtQJ6Mc1GHQFmsuYXaiIXb2TGv7jnmZ7AN6x0E5F1vTPm1reSnj1I19CKCWAwHu7Y6r%2BSuRbfYLcnk96qTO%2FWZ%2BiRAHwO%2FTz8yeWzOWj8WVowm5GHvQY6pgG7xorIf3LGfhaujsXLwG%2F6A3974N24ZEtjKhFWMvxKATJvi7HX%2B5PWwzTbptv9uKaG8R6KbKyK05UefDP1moU9Yzqeb1tFIUUO3jvwuRjZw%2FqQQu5jWqf0ihO6XlhxHSEVpN7x6D6mmmWtPDW8Eh0dFczu%2BnKKP%2B%2FCI3wVqi4EBSQjkFAuFmrx6KBzQCcoL6WcxdIfeFzo%2BqScblIE7TvMwpwe7%2BhC&X-Amz-Signature=61065fac8758ce1784f2d867612aecf822dc74bbda0b48142bb7154f10bb4405&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
