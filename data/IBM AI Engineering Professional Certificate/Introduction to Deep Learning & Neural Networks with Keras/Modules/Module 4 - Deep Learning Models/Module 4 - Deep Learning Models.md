

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=628d327fa07f5708c548b7f960639717a5dda5b3a1a53c73d796e19eae171287&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=4792caa25818b1f8d2669fac91f148e3f92345fc24c44b1e21c79d2d7dda8d5d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=5173ca3f0306a314359ce983b997cf0142ad2b60d3a7f6ef6ae68a86c6e42227&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=92e13cf6c2933297f40755e1df38f0d2b6e79003baa77990fbe2cdb3689852ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=fe0c58eb0831a554814cd4161eb264c78f22230e78a0d30e6541d1ca731b701d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=75f47acb44a3e83d002b6e709badb0288be7b32c7225e39abaaaf5209e332da9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=2b5eb32961a51bfbcd90b26d0c1ec887944d71c927512c5143e196afc70317d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=be60203eceef7e28f78bbab184a60318ffa9200e86432097fc738b18b19b830c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWQWFR5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDh2i7wVq%2Fy54WUwoa0iuP2dcAe0qXwhzF30VSkZEz4yQIhAJJJybTntnY81O26XQDmf5mM1PTCnShWyrkWnKKZ4nLEKv8DCHsQABoMNjM3NDIzMTgzODA1IgwtGUMvhZB4KS9ZleMq3AOABIb8QyqqgHeGKEx4c19363ncd%2BO8JWMBqAVM6vD%2BNbgGnarcYAQkWlGDUM6zUvgZWY4%2B2C12E%2BrsQh3vDahaZwTZY5gtargZRQgmkIwBPoEGsLyzk%2BcK5mA9nrAqMH4BCe38iwc1czoQxxkckLntkf3HYwvjry6ZaE%2F89sGh%2Fi24S9VaC0HZQmd70MhIbxoQkzbqdLWFisSd%2F3m5n2nRyi49ygt6DeuFzlQRZixlqD9BCq45B1mzJQTYPUo1Esio0HVpRYlcJTMdu3i5%2B7MKybixsHP%2BlFiFgEgaj0qagvwAzneJsn6cmlYypTEuFEaBmVxRAEbAlpF0JxLWZTCDf8p7V8BK3brwFd2CxlyzCF9FsFXZwUqAnqjY0X3HoHleKyMEN0UdyPSGFXPUCK3FjPOZtgTDqetWLrxWQiHJk6G1cDdZm%2FwSuSBiNHDHY4HzClOLd%2BzPMvRsYik4nFqeU3k4AcdcMPQ%2F05km505W%2FcHHqoYsjZgJtxFZtdgybiik3a1AVrjwvx%2BzoQeXtDHj6bi25FtBRjRNTr8qNbd%2BjYbBNJrQRWlSmt2Rq2HVWdqigAXIb066P%2F86dHBknNDdbePdlbMUEbjKFFMe%2Fivu7kbmfsguwcK1PHQJLDCtmZm9BjqkAZR8DTGkC2jbxnbtpPLxFF%2FFMkSQNw%2Fs%2B1qGkInrm1DRfdu8CDmZn7eEBjJEW%2F9Z8MKXoMNZrkthfJdxKI7iEQsGs58QsJgnnzcDO1D1hx08StcG5tYOKAf9GmILlK0nuDyWioIGL%2BNPw5fY0QgyHBSi0QMry7xAQpHggO%2BfGZXpssl7cv9GDr2uZq%2BOItGQ3shW64tXb1zrLNWtFU0pykzjsQa7&X-Amz-Signature=e2f8b32cb473175cd4fa01c2f52162887aa846b5a956df805467b9229f9a93de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO7JNWT7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDQEF4rTKBVYqnhNdUekLGFLg269DhwDVCKRANoWWe6ZgIgX5hUTeg0PZCT1y51SlZXTLoZXHCVbu1G8zsGj1vYWMcq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDEx4U2XPWZiN1s7OzyrcA5uA4agrpRkxbApLej2TJ07%2Fhd88vLP6WNEyZ6hFqyaWMYwZVJmkt7khVtvnOEIT9f4UvPSFu8N%2FwvLwuH7JUir070PxDofTWUD0i2r%2FEAH1GET0%2FLOIMzD4n6D3anyqlmZKFZD2uHxs%2Bq79luwHWrukvdXy9ydIlMOl1vlvh8r8UIXSCTTxTAwbVW1LCXD10UpN6jd24gahb04XEbEt74jsnCsusE3oHZy8ie1EJb%2BxUWd84ZBT%2FsqlMy%2BGWuEMVWryCyeIOM1725PjjKTO8bQNRlf4n6vUrOXBN%2FXey%2BPeubPfT6B8fb8qm%2F4lcV%2BzH3v4bYQTAiLIgBpVlWFy1MOGTUMRAWxYQOsxSRyPwHvIlDnQ4Vev%2B2oMqdV2CD25MKGjOMocWWaeOSLMofh%2Bdfoy62tiYdZ3NtFvg1qsyCz3S8%2BBOBUqaJWxZoqtqs%2FNKGi%2FWwmviOTbdPRzemyiN8Q0dXUVeggOSjwiqehq8qYFDKsaiOKPor6%2Bx9UPOls0r9aXXQ7yNoYV963l0v7R60KHXkxYWoA5dzITvnVlDtvDI2QmNd0FmSp1h5Og1cY3ZSZo%2BEs8dJYUfTNr5T4DjmgUrVdnoQMNPwNwMx1vPWJ5RPGnEEblyX3YoESNMJuZmb0GOqUBYXtD3c0DbAgcHpK6bQXe952Napbd3z%2FaUgyUGP96%2FIBzSfNk%2FIx0Rwe4j5VE3ffp3CHUBWilRGSNy5ORCHLJJqfw%2F%2F63fTfhA7eSTQrA%2BJMKSX%2Fj3rFPjUGbsRofTOwqMZ084AkzbG5LsF%2FTlMr0Otg6PykEdKkHVIzSnFioWIBNEb6g3aBkT8UWNmgO7msIZuteo8p0p4pT1gjj5vauqCxvbzFV&X-Amz-Signature=62de1a02c49b825b52f33a5d4663a53c0849df1c7f500bc7cbe69663c503c529&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO7JNWT7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDQEF4rTKBVYqnhNdUekLGFLg269DhwDVCKRANoWWe6ZgIgX5hUTeg0PZCT1y51SlZXTLoZXHCVbu1G8zsGj1vYWMcq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDEx4U2XPWZiN1s7OzyrcA5uA4agrpRkxbApLej2TJ07%2Fhd88vLP6WNEyZ6hFqyaWMYwZVJmkt7khVtvnOEIT9f4UvPSFu8N%2FwvLwuH7JUir070PxDofTWUD0i2r%2FEAH1GET0%2FLOIMzD4n6D3anyqlmZKFZD2uHxs%2Bq79luwHWrukvdXy9ydIlMOl1vlvh8r8UIXSCTTxTAwbVW1LCXD10UpN6jd24gahb04XEbEt74jsnCsusE3oHZy8ie1EJb%2BxUWd84ZBT%2FsqlMy%2BGWuEMVWryCyeIOM1725PjjKTO8bQNRlf4n6vUrOXBN%2FXey%2BPeubPfT6B8fb8qm%2F4lcV%2BzH3v4bYQTAiLIgBpVlWFy1MOGTUMRAWxYQOsxSRyPwHvIlDnQ4Vev%2B2oMqdV2CD25MKGjOMocWWaeOSLMofh%2Bdfoy62tiYdZ3NtFvg1qsyCz3S8%2BBOBUqaJWxZoqtqs%2FNKGi%2FWwmviOTbdPRzemyiN8Q0dXUVeggOSjwiqehq8qYFDKsaiOKPor6%2Bx9UPOls0r9aXXQ7yNoYV963l0v7R60KHXkxYWoA5dzITvnVlDtvDI2QmNd0FmSp1h5Og1cY3ZSZo%2BEs8dJYUfTNr5T4DjmgUrVdnoQMNPwNwMx1vPWJ5RPGnEEblyX3YoESNMJuZmb0GOqUBYXtD3c0DbAgcHpK6bQXe952Napbd3z%2FaUgyUGP96%2FIBzSfNk%2FIx0Rwe4j5VE3ffp3CHUBWilRGSNy5ORCHLJJqfw%2F%2F63fTfhA7eSTQrA%2BJMKSX%2Fj3rFPjUGbsRofTOwqMZ084AkzbG5LsF%2FTlMr0Otg6PykEdKkHVIzSnFioWIBNEb6g3aBkT8UWNmgO7msIZuteo8p0p4pT1gjj5vauqCxvbzFV&X-Amz-Signature=3e9ae0ffbebadc10f6a9e6da6d17a268d14c4a125110d9268afb71f50e9e9155&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
