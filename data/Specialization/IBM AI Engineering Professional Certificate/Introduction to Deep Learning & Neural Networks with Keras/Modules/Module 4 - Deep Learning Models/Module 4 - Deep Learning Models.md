

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=7a1cbda34943c836adfe3b39ae6131e0203726d48ef12499517e7e80df6382b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=923eb4eaad144020baa6943772b9592df3b7752209c6383b07d004f640205b98&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=2f9d1d276b5ee418bdb0de0e659ccf391702b7c69f2f0b804632581ead34f3f9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=8e3db24cf0ab4ecca8a63373911f1d416ff71cbd824cb9eb59a8edd4d9a5e979&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=5ad7baf801a04bda7500dee6576dc9cfae9c08b7a3f8a9b863de7a99be314c07&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=a92c33c776f38caddc1088245b496fe0f347068ada8f3ec57608ac10806c2024&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=78d6c1798178a48930e6b0d2ce147fef9e5203eb1db1957cd8ae6a100a315a50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=1047bf62e5eb1f1008893b08b907431b241d6e8a73d8eaa3e633a9b7b4360826&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNSFDOWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3K2LJRtEtEN6gpZaQuNBOQyGOMGvH7zvpXrsh9oyXFAiEAiY3pqueXjGR1md2s%2FxzY2pUUEfnX2oCKfdOhziZbp4sqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFx83tLFY0F4U4HDcSrcA3KXXRiWjqojBUfHhJikBiy0T%2FF9M9daI7fCcBpHZkkb5Hmk7FnGw3Pen9H7wt3DFm5mEEu63Eav%2FH%2BdFbhl5K1PoH7Ye13pijXlYhruOcfWquGZV8p727SMZG4hfZKi5IcEKjIlO%2BUos%2Bv9NsAi1IiQfLl%2BP%2BP97BNy%2BhoyJPRT0sIZhUv6tzVN99%2BkLuaz6kmA1BhXQaCrWOAmBiarK4NQHd4SfM%2BHYOTjnz%2FFdRmgs3GKIobRvpqpKmHXksfKp6yM%2BxP0qlPH6xVt5F57Tjrom0120i2wWLzoElx0tqRMMPVsGYwJnqmPBL0vJV7DFXhCQlP4khKw2F29mee8tqd%2FQvF%2Fym1AxHBTwzfcB4LaSl5vdwey1KuNCh%2BQE6Dj4AUulcvDuQrvEBEqYx4aZVjRKze3xANPcXzeWv5%2FtUaRuTAMYxAujAIgeZzLad%2FlSWZ1OFjU%2BXHoNzLAOsmbeSyyZdjawqX2UUOkCNWB1uvKev7sMc6bQF9HjxosGorpJBMzt9L%2FqQ6ulYNDWCU4xIgLltYK3qn3QB%2BkQEDbelTw3TOJXVExA71dWKT%2Big2dPRvcgyOFVBgsGK%2BElhkU9e4shOMyRtrXFvewOH9tCne%2FEWgzQxRDq2iSczFbMJPQ8LwGOqUB%2BlU9nBWvZlwuT8Jk5Db%2FcirqJDde1cMLlz96d%2B0AMKPvj7HFvQ2F4Ibagl2QbpzXACrsT%2Fe%2BMVqvQ6VR2uzt4dI%2FBS76HooCAE0TEiS8bzDYU1SgEXJbrpdkgdXz9rs%2F2sUPnkPvJR7wKMBl%2BeF%2BhDprJUtVmoD8myo3982ytSnybFEeBjR%2Br6VhMbtxtjQOPyNUaUSJKjL422RhYWieMHMnvYdO&X-Amz-Signature=320c98dd6238003c35d0d91d3fc6b12e2987cbfc39ea7d1f826d96076797227e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWXV266G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMR9bD0wBn01KkfbdiI0NXzfe6tSapIc30RjqgI36JSgIhAPo0xvAt8ZcjfXxvxa7RZo3VJPsDJ%2BL4TDVjrMUv6axCKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0qSUmAMCxBf499hAq3AOEC%2Fra8muU83E28qdTEYF7pZJMJe%2FnqV5Q8MyCWma9sYM%2BaENm1pdyhOLDuEV39YTKhZGMEYdL2fI8Rm6xsDO81J%2FZezQEXp%2BHPt3uK9uawvJcTnqPp%2FB7OLGz4vfdRMDVOd%2Bhoa0%2BZxZ55XwQ2dUPGhGzLZXHLcGXkci4RbJ957WGHUcvdqTPLSPpkB8DbPGrH6L%2Fyo8wmfGfFhTzXUk%2B9a0quZUVslmA2XIBZhbrgKLZ6Nf1f1PDua60GVm0l9PmJC%2BeOqHbU8nlCMS8ZC%2Fp6TcjiqLLVbgt%2BdyW9v%2FfHsjObkCYWX8iqewLNe%2Fg8%2BVX2bjQUqre%2Ft8H4MsoWZYEMGzjOirMCVEkvK2iq2IIMh0BJ%2FSTYoAOMd2GCZUhwqxUKHXJtpIEZixQsW6XqOOa8qybXZKVeQka78eGcJlfDKx2dtpwmQDA0JQqyT6g9KyCM88zFbIsLcRP43finZY0lvqKZTTJEZ%2Bvg%2BOYsOLJsdlrF4PThSGTdUl4KFl4wYQNTHn9O%2FVRSsP8qct9DP1GIUCtVDOU9KJmK6GbcWet8ZHs%2F%2Ba3B99ZlmFsiY6C7KX9qvYQyeV5%2FzZTEtlQAy9oMIX4YG7JFlPTM%2FYk5k9QL9hV47f2D7cjdGBRgjCR0PC8BjqkARx13GOav6VhLDxuiePMLVXf8EH%2BOxKgA9NR%2FLEBNj4wmryG1x%2FtsYAXJiG3Vjfz1CBH5bblG2yXDdTVKZjcGzmZsdCY0ZOC8Y2XmiM%2BOIppbniiAbKew%2BhnYbwPrsjpfHxsJLDKQxZf4omCQrmlGtlCmUiLu9eSkUd9dTNXW08z9OJqVHb0Uv%2BMucRPNlXvWHDgvupOR1X8FH74Nz7d%2Fk0AcI%2Fl&X-Amz-Signature=a8cc84fd5f2eea6b01c7b099cdfa22eed47fd21030dd65a26c3bfb11710c9b28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWXV266G%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMR9bD0wBn01KkfbdiI0NXzfe6tSapIc30RjqgI36JSgIhAPo0xvAt8ZcjfXxvxa7RZo3VJPsDJ%2BL4TDVjrMUv6axCKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0qSUmAMCxBf499hAq3AOEC%2Fra8muU83E28qdTEYF7pZJMJe%2FnqV5Q8MyCWma9sYM%2BaENm1pdyhOLDuEV39YTKhZGMEYdL2fI8Rm6xsDO81J%2FZezQEXp%2BHPt3uK9uawvJcTnqPp%2FB7OLGz4vfdRMDVOd%2Bhoa0%2BZxZ55XwQ2dUPGhGzLZXHLcGXkci4RbJ957WGHUcvdqTPLSPpkB8DbPGrH6L%2Fyo8wmfGfFhTzXUk%2B9a0quZUVslmA2XIBZhbrgKLZ6Nf1f1PDua60GVm0l9PmJC%2BeOqHbU8nlCMS8ZC%2Fp6TcjiqLLVbgt%2BdyW9v%2FfHsjObkCYWX8iqewLNe%2Fg8%2BVX2bjQUqre%2Ft8H4MsoWZYEMGzjOirMCVEkvK2iq2IIMh0BJ%2FSTYoAOMd2GCZUhwqxUKHXJtpIEZixQsW6XqOOa8qybXZKVeQka78eGcJlfDKx2dtpwmQDA0JQqyT6g9KyCM88zFbIsLcRP43finZY0lvqKZTTJEZ%2Bvg%2BOYsOLJsdlrF4PThSGTdUl4KFl4wYQNTHn9O%2FVRSsP8qct9DP1GIUCtVDOU9KJmK6GbcWet8ZHs%2F%2Ba3B99ZlmFsiY6C7KX9qvYQyeV5%2FzZTEtlQAy9oMIX4YG7JFlPTM%2FYk5k9QL9hV47f2D7cjdGBRgjCR0PC8BjqkARx13GOav6VhLDxuiePMLVXf8EH%2BOxKgA9NR%2FLEBNj4wmryG1x%2FtsYAXJiG3Vjfz1CBH5bblG2yXDdTVKZjcGzmZsdCY0ZOC8Y2XmiM%2BOIppbniiAbKew%2BhnYbwPrsjpfHxsJLDKQxZf4omCQrmlGtlCmUiLu9eSkUd9dTNXW08z9OJqVHb0Uv%2BMucRPNlXvWHDgvupOR1X8FH74Nz7d%2Fk0AcI%2Fl&X-Amz-Signature=d1be055bc923adcc1e82a9df72b28a0e9fd6eeaecfb2546074694c75c9c749a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
