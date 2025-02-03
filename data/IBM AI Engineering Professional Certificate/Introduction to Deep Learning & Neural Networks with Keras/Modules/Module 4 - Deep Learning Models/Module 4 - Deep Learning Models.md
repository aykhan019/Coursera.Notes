

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=689a190db2f518b439fe0fc95bf0fec08a7b7d29a362ea6cf513ee414631067e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=403a589359d7ba55fcda2514e6be765d05713efb4607f7a79edc4c98f85fea19&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=0a759e508de5e10ba806c8d02f687ecfbf96c183bc47a3a2bf3b9db140905f8a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=83123b5328bcd933290a8528c24ec0ba036a608a2ef7de572790b30276b38cca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=bb34196b4b06b1ada2aa7fb0aa4650553f6de54730bd31aa7492275ece54bd66&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=919078b20ca8c056c8a87d17f5a0d8ed1239ab217cc86b637eb69affcd665a0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=70cad47a1b602834496fed81fd2e1cae15fbc90f92ab2fe2d4176f4d854420f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=7263e5ecced5e863620047cac3507f03c5bb576f44c43f39a713f5fa04eb22fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQOPAZFS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDUBRt5HGDQHQ9T%2BAOTskFsA1iMUDG3lqcbHF8S%2Fur4dAIhAO8ipaoLDOhV0d6YuIpbTTXDvWYRAYXGVaksPpK3ABjIKv8DCB8QABoMNjM3NDIzMTgzODA1IgxSVQfiFzy7Yo%2BKPkUq3AM%2F58EeXn3y24uFjDFkvPXp4iAzVeZRDZgPxDemZyp1PtxOHpzP9pqh1r64M6DtfE6G2zVXu%2Fx96y4G%2BTP4PpY3bcR%2FbtFC6dbbCUV%2Fx3QeTL8Pe8riBQvcQs3xWGj21WpYCQCJaaiA%2FWtFgrpsRvnK%2BVvEQmvbgi23%2Biqo%2FOrfQMiNTmOp0M36ESJxQU1iila0XfDcZUb59aCWxpZN0F3iRKTtJ75f39yYIBQuPBiIxsQlB4J9V3NTgVPzzhXQnA47IX6td2b2LZLdWkxIPGmD%2FqDntcQg5th2HV08qamFwf%2FiGXNWMrs%2FdQiVxurTNTGDsmnGPJoEaCE18%2B6uc7rqNQvfRRQiWM4WhL1T%2F0g1PcGJMoE0fWXYnI3p0QImPnXNlukO%2F9N0REawjQCGRA5YhS1GOqAa4Vtf6iDgiQu0HHG1gK43O05CZLh3DxSGMvI5bOoMliV9%2FHo0pK%2F5bYFlV6nTBO%2F3KC90VNNKsTH64skpEgMjDc5UxUXX7RZgZRFHckWZP2MbmFlly4QlO5ghMCI8hemkdyv34Vz75wr94YBJKKlHm81LboJPLz%2F8Om8BJEGNhas%2BVLdPV0TVJO4OpmRx4zhy2W1pCSNniPzLYgvZXBLs6VJqIBxf9zCS94S9BjqkAW%2BwYS4aCu0C76ZdNCl78FtGvF7tl6AV6Aen9mOFfIhZmlir5VwLvZ72d%2FjErMvQp2DTQyN8tjMh%2FObIsrX%2Ff5i0j%2BiC8KRV5RseNBc4fkmSTSqJQeB8dd7kEZeKZamj%2FfersHoFgS136XMIvsrzAHn1YsfhPSeZ3nLH8ki9wqiQUj9N9EMXOvIAXL9d1rar0N0Njkz9HN6L8xU%2BMDHS%2BeHztZ66&X-Amz-Signature=43ff35af7ab3ec9cf83f1993c4ebfb7773cc474d1ee7f74668da029e060fdf23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UKDJLRR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDoYU%2FRcXOgE%2Fwk98liQVxGw1Qc05vnlBbBIvGFz%2BL1oQIgAIMV7UMKCo3vEmsRhvOo%2Bvvi3136gc26TBcxB0uZLrYq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDMF3NfLcBfkjW2ihUircA8isV2GQjaOE6Kw7%2FsquKkTmXSi1G1IDIMy3yZ48fadLB7Z0cr10D1ZII%2FDrReMunH4wZ7C%2BvEs8r0XLvpkifjGOJR4GRv8hF%2FBnXIVg%2FPf%2FVqsobJbUl0SZsjS8ASaRg8Q5EnJSRY1LQaQ6sNl84al5kLhB9l007izKPnYpwXGv3UHUkUuSKAYn43DYvoWyHehYRD2K7qTj9%2BQ%2FvHADH0EwNEhdEUNlpMOkgR4S%2Figt0IHb%2F6ZyKNevDAG0%2FN2M6x%2BoTGyAe%2BjBmFwWXhRV5blyyn6FDHM3fnH9WGtkGCduOfXL%2FJudEA0ZIr%2B%2BLUoxDcnZZp4wGBwK3jy8u8trwFntAGc80cPkGXy04DdRZdQc2oNXzU257E9yFnfn%2BUbju4BTtOUY772XkO62a9es3Ge5Y8xnJL8MjR0%2BXehVPBoT6Dh0yw4%2F%2FpsDcLJuMGonkyMj17xTljVIduUtKyBtSGgveb4CQKG%2FWuwhVHTqpDnyUK36Vw9SiPkn8FlzUFLDUpIXkDuY6%2BeGAx26OQIojN3%2BUGz7TSCMcDY8b1ScX2I6dHw5maim2ndL5b%2Fm2c8N4bRDuBRSFsiSsAZ6k033qMCmWPgiLxnSngyCQuE4N44lkLpLmKnb3GVwDfhrMIj3hL0GOqUB21bhzNKDcBkmQjoQlfeHceweOKhPjGShkf7sk1QOLi6qjsbgdFWkv5O8Bk2ZfYc1jU%2Fh1%2FgYfAGdoV9%2FLgxR5GJzDHitXvlKl2wgjF4NKMG9GEgvPdrEr0AOtv9iAyBHWddcn25esOeREQpdVviqvKKvyPYbuH7RONh%2BG6PfsFeyQyHwiAShi%2FcutTnzIyCzj4yr8OTfAQmHpOyjRfTFJ1kzrp5X&X-Amz-Signature=505942243a162149e658833f9bd6946e2234a26319fef841aad27f27ab0e0d90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UKDJLRR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDoYU%2FRcXOgE%2Fwk98liQVxGw1Qc05vnlBbBIvGFz%2BL1oQIgAIMV7UMKCo3vEmsRhvOo%2Bvvi3136gc26TBcxB0uZLrYq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDMF3NfLcBfkjW2ihUircA8isV2GQjaOE6Kw7%2FsquKkTmXSi1G1IDIMy3yZ48fadLB7Z0cr10D1ZII%2FDrReMunH4wZ7C%2BvEs8r0XLvpkifjGOJR4GRv8hF%2FBnXIVg%2FPf%2FVqsobJbUl0SZsjS8ASaRg8Q5EnJSRY1LQaQ6sNl84al5kLhB9l007izKPnYpwXGv3UHUkUuSKAYn43DYvoWyHehYRD2K7qTj9%2BQ%2FvHADH0EwNEhdEUNlpMOkgR4S%2Figt0IHb%2F6ZyKNevDAG0%2FN2M6x%2BoTGyAe%2BjBmFwWXhRV5blyyn6FDHM3fnH9WGtkGCduOfXL%2FJudEA0ZIr%2B%2BLUoxDcnZZp4wGBwK3jy8u8trwFntAGc80cPkGXy04DdRZdQc2oNXzU257E9yFnfn%2BUbju4BTtOUY772XkO62a9es3Ge5Y8xnJL8MjR0%2BXehVPBoT6Dh0yw4%2F%2FpsDcLJuMGonkyMj17xTljVIduUtKyBtSGgveb4CQKG%2FWuwhVHTqpDnyUK36Vw9SiPkn8FlzUFLDUpIXkDuY6%2BeGAx26OQIojN3%2BUGz7TSCMcDY8b1ScX2I6dHw5maim2ndL5b%2Fm2c8N4bRDuBRSFsiSsAZ6k033qMCmWPgiLxnSngyCQuE4N44lkLpLmKnb3GVwDfhrMIj3hL0GOqUB21bhzNKDcBkmQjoQlfeHceweOKhPjGShkf7sk1QOLi6qjsbgdFWkv5O8Bk2ZfYc1jU%2Fh1%2FgYfAGdoV9%2FLgxR5GJzDHitXvlKl2wgjF4NKMG9GEgvPdrEr0AOtv9iAyBHWddcn25esOeREQpdVviqvKKvyPYbuH7RONh%2BG6PfsFeyQyHwiAShi%2FcutTnzIyCzj4yr8OTfAQmHpOyjRfTFJ1kzrp5X&X-Amz-Signature=8616a6fc4cbd27c2e09edbfff4838e630dce9724207d10c17a3cc55f35404641&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
