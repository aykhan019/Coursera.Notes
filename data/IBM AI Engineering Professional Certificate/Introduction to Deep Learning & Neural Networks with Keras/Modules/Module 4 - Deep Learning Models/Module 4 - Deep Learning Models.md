

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=6ae1211affe9c7ec8037fb595caf202c981513b4598d0ea9f8889ac39cf40532&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=43e7fabce09f9d3feff8f8ed5dd0080f437762f85287c8ef93099d795264d131&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=da326f285435bb696d1ba846faef25bccc193f8f242ec1543dc8c0415f8a009f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=38d7cd06420363afdecce9a7af7742a73617cdc3da3d2cd3efa5e544369ecd69&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=12277fab6355ee6e00eb372a02ea288d9c2c4a4c9012f8726e56becb3b3cd041&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=faa6fb62f43855196f47b7811ba827db1401a73e3c9d26da99d706969565da20&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=e42afc69eb6db7b6a6ba3d49896e33c8fd95b689c14760b8f65e91926f4b224d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=49c2d1f5f150000f6b35453b3fe557991a20a2bb265fdd20b9f6736ce2d4e8f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2AINVB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaO9vRkyiYncoyXdt%2FoGB9bvPCJGlKZDLk0Z1Iicy6GQIgGf7iKWWqirer7MF2HSw4DjQoEr6IQ7%2FmCZiN1ug0GRsqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNt6k8RVhbhFbZ3D7yrcAyKH428q1AMuydiqxgq%2BfFEkNJU6K0jIAP%2F1XUESX4YMxD0omS5BPBCKTtn4dpIUkh%2BcvRSmG9gK%2BmaHEDBkiNrYFCyjqE1aJJmVZ8YUwZpQIVM30XmQkFvaSn0I2PCP5fB0jAslXjcDonoV%2BnDjsNGTTR0o2xgI%2BsHkt9GSd%2FKgz0N7LmyqI9OlF%2Bqg%2F2LVxQMtw6EnT9Vj24ifOKprOfoVMhq3ljJ%2BT6FawgFmS%2FzGQOqyhif4GNjzGiMG2SSj7Why0f%2B6IVpoIChZdCIL7vsI1E0s6N1bnGdBNUfOf%2BnXTFyUBl4KMKY2npnZZq1%2FC0X2FIeygf9yt9%2FxRQC6LRs%2Fl7qIhnUkNZdozLTuH0kzBa%2B5dsklqwIxRcccrN3kXJbNuqrREJh90IMSgVjD8WqU7EcWQahXb%2FLfc1G%2Bl%2BKUVwzXGW%2BlG7D5%2BMIIE082prv3iPOHUdk1BUW6N%2FVWlrvosBGJyTxu2ESSijSj7G11EnI4IzUiIFsze3308yYYeyqu6VRGDe6sGqzzKtR1rTGkEe1l1CoRQR1xp%2FbR56OFGAjSw%2BbOkeRZtX%2BQ%2BjuUy8MBC7fXD1rmWLeUeijj%2FGjZCnET5oyDOObf0T1%2FvKJypMq5ALrIp8omCF%2BcMIDK%2BLwGOqUBm%2Fq0nulkStCGya7epGSZNLi5YaKTWGS5BGGsd7e946em3Xf0Lnf4nQf5blLQhgKgmdpd7iwr600HjL1YtDQxa2BICsUDPhuB1SMRTOPgw6FPC86lD6rtNNpdKH6VhtF88reSmBtJQQA1EOu3RoaXj4JHDgh6B1Elky4NlZzRTlc%2FSBhxyk2hTHeEN3bDHqSzcxr2hI33niK2fa0c35hB4KQ0yhM6&X-Amz-Signature=08d3cda0d8b5e570e2b84998e3da315cec802462dac6583c982b34eaeda927fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XK4KCANC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEav3AAf0zKsjMubH9gZCoCHOPAoZk94%2F3I1NngnIqvwIgCT8Vkye3oOVD9J51OyompO5OfjiNLIgi3t%2BYe4YuQF4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsZjoedSwQmLG6olircA2pXe4Xbmr0BmU3Dms%2FsgrQQMcOBNk%2BY5m8W8OF34KHX%2B1%2FnCI%2FTCoziq3Nql7n2nK38khpsOqy1ceA4vLysuAFAmg2j2u2wTO3uH5zZ9kBUsz8%2FiwqyM8RUDeYOzUPLYI81coZ%2F7tZD4fzRivkspLPj9BdvL9rwlVQww4s1nVG8D7fkkUtYsJLzZI4wLajl8qpp83tNOucJ9XAQUnZ%2FhowYTizJbCDlz9h2EYyjMoD8DJkp8b6SfUaGSS9tIeQP0LlnJFviUPz3gMkOlvpnj79RLijzdn%2FlMBlCSY1PilIkAi6DcHdPg7JqAn1amDMrOp%2FJrGOPEwx2lzXZV17B8%2FvrzjmVM6qmIVGWf%2FyuW7i25OLL05fqjsJH4QVaKTT7O7HNXv4efIWPnYr5mpLhiYKwq%2Fr%2BsXjBZrTzX5ooTwlikUgdHaDSPKa%2FQQvpNWgFDhzh%2BrLlPBpfOvXCXnPz7BZRFKxJjWidjCCqIOHJj3QDdhBRbNYV%2BoM%2B9ShxIa6JWFErOnusDNxhmZYPH7mzC1sL0601%2B1Vpcp2s3S6sC6t0%2Fk9bgtfn1W4YjN1JpC8g50rB91Cls2uDQ1chVbpQsU3R0Rnu9nw9ghjnI4S43qLBDzvBCgvIoD%2FsCZENMKvJ%2BLwGOqUBYN9Fig%2FjcCOTKOQiua0aRZOilqQB4WGcBanRNjLlOGjBQ5Zp%2F6ARn65mAKPtuLkLKVlj25MN%2BYAhR%2BAFbHJjM6qucPFFCKdDL6hSvr1XNAPMurE7LzSi%2ByeqHiQ8OSHD%2BX0q5pc2wpnEzdIDJWfjSIDlvkX5t2DRG7DGsbpqten6eT4kyh2NjZ2wVnKmjltm5A%2FVDzmN4WwRjXF7fhC7Lf5tQFU8&X-Amz-Signature=dca4eb8d3aad8cacb7e9785d7268933639be78cb78d2ffbf81334187b02d58c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XK4KCANC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEav3AAf0zKsjMubH9gZCoCHOPAoZk94%2F3I1NngnIqvwIgCT8Vkye3oOVD9J51OyompO5OfjiNLIgi3t%2BYe4YuQF4qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsZjoedSwQmLG6olircA2pXe4Xbmr0BmU3Dms%2FsgrQQMcOBNk%2BY5m8W8OF34KHX%2B1%2FnCI%2FTCoziq3Nql7n2nK38khpsOqy1ceA4vLysuAFAmg2j2u2wTO3uH5zZ9kBUsz8%2FiwqyM8RUDeYOzUPLYI81coZ%2F7tZD4fzRivkspLPj9BdvL9rwlVQww4s1nVG8D7fkkUtYsJLzZI4wLajl8qpp83tNOucJ9XAQUnZ%2FhowYTizJbCDlz9h2EYyjMoD8DJkp8b6SfUaGSS9tIeQP0LlnJFviUPz3gMkOlvpnj79RLijzdn%2FlMBlCSY1PilIkAi6DcHdPg7JqAn1amDMrOp%2FJrGOPEwx2lzXZV17B8%2FvrzjmVM6qmIVGWf%2FyuW7i25OLL05fqjsJH4QVaKTT7O7HNXv4efIWPnYr5mpLhiYKwq%2Fr%2BsXjBZrTzX5ooTwlikUgdHaDSPKa%2FQQvpNWgFDhzh%2BrLlPBpfOvXCXnPz7BZRFKxJjWidjCCqIOHJj3QDdhBRbNYV%2BoM%2B9ShxIa6JWFErOnusDNxhmZYPH7mzC1sL0601%2B1Vpcp2s3S6sC6t0%2Fk9bgtfn1W4YjN1JpC8g50rB91Cls2uDQ1chVbpQsU3R0Rnu9nw9ghjnI4S43qLBDzvBCgvIoD%2FsCZENMKvJ%2BLwGOqUBYN9Fig%2FjcCOTKOQiua0aRZOilqQB4WGcBanRNjLlOGjBQ5Zp%2F6ARn65mAKPtuLkLKVlj25MN%2BYAhR%2BAFbHJjM6qucPFFCKdDL6hSvr1XNAPMurE7LzSi%2ByeqHiQ8OSHD%2BX0q5pc2wpnEzdIDJWfjSIDlvkX5t2DRG7DGsbpqten6eT4kyh2NjZ2wVnKmjltm5A%2FVDzmN4WwRjXF7fhC7Lf5tQFU8&X-Amz-Signature=dc37c22007d20096bde35571fe45c0c83131b246806352380be590b029c639a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
