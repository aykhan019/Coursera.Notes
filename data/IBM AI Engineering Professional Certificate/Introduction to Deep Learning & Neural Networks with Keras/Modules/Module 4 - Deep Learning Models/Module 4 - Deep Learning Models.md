

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=72e8d20e14f53c2263d04d87aa537390f254e4c8a0c3b46067261844e832987e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=dd926f5334408df838d5e2390cf9f70d1f7d289023ffe70c1f4f09bf45df8b43&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=c2f31e8ce108db1e9ba631a5e1f7b54113e2995e0a5f43b88546a4330c48c98e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=14732b271c73aa376d28637cefe23399e52f8322a8c87470c8b6f5fe9ba5aa30&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=418395b8637376dcaa07fc3140076b5019f5f95e53c4a3fd4d930337bceda529&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=ec369f1879c9e2d07dc2f2b3ef1c4c5a2cd4ba3f64bc2a76fabbc6a2837d8d1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=dd10e3e6f690e77c86e49b31eccbddb37e593f6c39946264129120d8e741916d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=02e095a24d78dfd8e2d639b596b85f8b3b29548c2f5704fceb40004589fedcd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI6AQSRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCi6sm9sO%2B%2F6REotpOaJYGAPNY0d5%2BbNF7dkGBir0lr1QIgctZfspRAbTeJX9hHTn4kvKMdvvaYxDTCHtPWcYuFPFoq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDLUl%2FQ83gBMqnvf5GircA5zSYiqO%2Bs29npkFsrN7ldnNVTMW%2BPfS%2BLt67ceob%2BTKB%2FtsqgZPI0If0fV3W79%2Fa9P1Rb6HKMrNxkpLMo%2BNV75kTFx7xBRgd4PcVrM3KA6Ue9q%2B0o6WaOrLCXTPfYMzzaX16UQqOHXw8BwuhLGPNiEggBPVFQbMagJJrWeFszy31g61v4SFcM2zRlb5QUTCMuv2vj8ZS%2BQVD%2BLEIM6jXfKqpVCxLlp%2FUYQjeWoY4GCbn2QT%2FuDA3KI2E36z2igAVF5z1VgGO4n3Am3BAT8O7xEJM9Xc%2F8La0RpeIMB2wQm34%2BfFuOdTDs37EHldDK6NG9y2cz0OOuqKsI4YmCzHIxMWJ9JzzfocTw6oxNGq0d0iqfIcq5chHBcYklG%2Fqa7v68DyHT9dwBqk2QTO3kMhOZNHQyySIrX8aeNNrfrhld1iIC67aYkQ2PutS%2FVqKVXgwHBXudViiDz0QDL38clsC9ruOH6Q9YI0t%2BFKU%2BKFcjX6uNwX7MD9IAs%2BvqXcofI53DVNhksOWEh7NE7m982mqpwyQBRs54tM2WPX3ZrXONEEDpffWVNrG7kJIgWAqG9bAI%2FJVkV9wlG6%2FE7%2BiyEmmBLhkjrAPm5CE6VTOWjJFAkfp%2BaKI7oTBxOSpKFEMJfNir0GOqUBzUh12KGzl8wgQw%2FxtbSS7DCwDJSVDAvzvupdrOy5ddNGFZAl1R47MlanDeKdkG%2FuM2p2wNf5Zs2RK9g6Fnrp5%2BEAS247KC3AMIChmNCIbMmnYBOOSSQBfLe0F6x4Ske6oHQpr48JnmKQ4x7QtsyN04FQ4At49N2mYuRQ6%2BQcq5Umec4GKvypo%2FRqqDA5i97IWvFyGiIQFPXpqTrmjzrok3ET7nnJ&X-Amz-Signature=76ddf29e4e2454557c56a36cf181a8a94867c924841f5b38af37931414b031a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVQQNTAR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIHOMFg94hhQz4LhZADFbsVF6wXsP9Jjq7WTz%2FO3tfLosAiBsMW1N%2F6ZONJ8iJ%2Bms0dHpW4zPjAFiXftqrv%2Fp%2BnAx%2FCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMDiLWwe%2FFuCQe1BuZKtwDiJKNV8oHWxDgA8OLFOrEp3LpWtfu1zpFWl1g0GP8v7DU%2FEODjoy1XGHKhaBYfoc8SbrG5%2BRVXioKBRkoioli8VhNZmJywH9dH%2Bm0P8359yzHcRkDOrrmDSk1sIgb7NXbYmIFN6usP2ezviGU0DAl2zNQRsrD98hhdwhNaDjgdRWvHoZYGYxqTsGIeC1lbXAY99rPOeBPS5Avb4s2OkzeoAVI6TubaIEXAdFuq9IgSM7KBNaeLsY0QT9NKKaBlQSFM%2B0vgH7rkQp7oQlWENCAsy7OElbQ0%2FZR5Jby4qePWlk%2FBy1Q1QidmMyMO7dGsrbcSbFBOTiYUcUaB6gqUoepzszgF04h5fffUSMQMC7Yev6Z9xjQNYJlbAs%2F3j6S70%2FHus8JCmI4M0%2Bw2tpqQx27U%2F%2BXQ9IjwcLeSIeKxweb3wge84BH4DS%2BXPsMqI%2B3tci5Rv5%2BubbtH2p99k5%2BEnfdWze8AoTEDXiq2JpzH1lqSswIlJReFWP14OnVOTfLTjKaHIfS5q3BO2TA5qxW%2FAC73wAcYfoq0BAmqzX%2B%2FW%2B7ToMmLgcZOhSptlIbg%2B4ByZQwicizsHC%2FGu3QNWA1%2Fq9ctBjWC2fc2uMqwXks2KTLWi63UdwzeclfylI3wBAwu82KvQY6pgFwynWXNP0Ol2RzDYBMKgcEwwk1Qq528zYAguQcOOXW4hOD83YWJOPDNWOcz97AdeIEHTkBALyLTyy4mVXLJJKy3HsuLsDDGlFa5U6UfEOB3v7awnoOE4OVasuByPq9EFwqHFTUII9faxCK18pTtlQTUVuklaWMsfjKKKCLIZ86q4MKPDEiXMl4bsWLGbQ8QorRHPjAC0%2BliMr%2FN9uMjhUK1sQrLAxT&X-Amz-Signature=48af5d90926dd22af134e0adc67f6c643faa092bd8d0419e350a9097ec8203c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVQQNTAR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIHOMFg94hhQz4LhZADFbsVF6wXsP9Jjq7WTz%2FO3tfLosAiBsMW1N%2F6ZONJ8iJ%2Bms0dHpW4zPjAFiXftqrv%2Fp%2BnAx%2FCr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMDiLWwe%2FFuCQe1BuZKtwDiJKNV8oHWxDgA8OLFOrEp3LpWtfu1zpFWl1g0GP8v7DU%2FEODjoy1XGHKhaBYfoc8SbrG5%2BRVXioKBRkoioli8VhNZmJywH9dH%2Bm0P8359yzHcRkDOrrmDSk1sIgb7NXbYmIFN6usP2ezviGU0DAl2zNQRsrD98hhdwhNaDjgdRWvHoZYGYxqTsGIeC1lbXAY99rPOeBPS5Avb4s2OkzeoAVI6TubaIEXAdFuq9IgSM7KBNaeLsY0QT9NKKaBlQSFM%2B0vgH7rkQp7oQlWENCAsy7OElbQ0%2FZR5Jby4qePWlk%2FBy1Q1QidmMyMO7dGsrbcSbFBOTiYUcUaB6gqUoepzszgF04h5fffUSMQMC7Yev6Z9xjQNYJlbAs%2F3j6S70%2FHus8JCmI4M0%2Bw2tpqQx27U%2F%2BXQ9IjwcLeSIeKxweb3wge84BH4DS%2BXPsMqI%2B3tci5Rv5%2BubbtH2p99k5%2BEnfdWze8AoTEDXiq2JpzH1lqSswIlJReFWP14OnVOTfLTjKaHIfS5q3BO2TA5qxW%2FAC73wAcYfoq0BAmqzX%2B%2FW%2B7ToMmLgcZOhSptlIbg%2B4ByZQwicizsHC%2FGu3QNWA1%2Fq9ctBjWC2fc2uMqwXks2KTLWi63UdwzeclfylI3wBAwu82KvQY6pgFwynWXNP0Ol2RzDYBMKgcEwwk1Qq528zYAguQcOOXW4hOD83YWJOPDNWOcz97AdeIEHTkBALyLTyy4mVXLJJKy3HsuLsDDGlFa5U6UfEOB3v7awnoOE4OVasuByPq9EFwqHFTUII9faxCK18pTtlQTUVuklaWMsfjKKKCLIZ86q4MKPDEiXMl4bsWLGbQ8QorRHPjAC0%2BliMr%2FN9uMjhUK1sQrLAxT&X-Amz-Signature=d0b659e459741563ab548df3281c464d7653b0905244eb52e242a13285790b3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
