

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=d7e33964baa37d1190663a00603e733ef51dadd2e7aec644fda73ce55f65dac8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=ee19c65f81831e6bfe74fb2737cc74dc52e02d9eded7624c34b078aceeb44800&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=0e01c3dc0883d228a92fb485b615f60b63e473dfd70d56b50513e68dc5a340a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=10db5e1c6c83ff48ed95b977ec0c7acdc9b83303fd302341ccd2259989f5b59d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=97995d41c58151cded057ff459144c3e7f9bb028cb04b18f7f82a85213887445&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=3c57da0c8e42eed48e948aaca142eeb5681ec6c66b2708eed0ec75ee8f34b3b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=20b120075e537e1260718a4e1b1b284dc84b212234f94817900ac0be8debf6c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=dff74c88ab3b71da2be1836355783ae34a1edc19002952c7fa04ed6471bee0c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCHJF3K6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJc%2FQuZCzfcFSbWaE8MA2fBzvhwN0zMu4NAdUNDylLVgIgNm8KSUd691OGFzseXjzXRB4UmZZnzAm4VjK87FeakaYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKoJZ82bAkbSw39VXSrcAz5swQz1hDxsdynz39E6JrCuujjBLeo49QmBeBbZoRw%2B6M0rtQWdHlDtSITy3Wy%2B4eZ5u%2BW9R0%2FhiTC82cwTe7megIxtLEZSR0HRA7lgHq1ZRV3kLEg7tzF1yDW0v6%2Bdw3vFJd6LLyoHKRQHFBWQTI2BdDBbG8X39pjmQ1o2logD8sHzsqxMwg%2B6cxajay4UUM%2FnVBoq6XTzHb0Da7WL6liYbunYgy9CTTa1VxckcEgF5JrfC1PQFbWNYLDskViag4VkzbIvaXeB80rqS%2BjwJnp5FErAN9TsJGwy0QGpfpfPK%2BnXytZLYN2agwEyuQ0%2BdtHhnGYgQBNiegYM5s86LtUwIrhFyr737JNY9Ly674tlm61c6A2vzsRvW%2F0ayixK69DLXRadLPhDUvm3yrsT8xR4Z%2BVNjwJS6VZFuuHuFiFiXt2gv02K1cx6UbcO2p5Ax%2B%2Frjub2BXquN3zIhqn19hvt6VTkbRs%2Fb2DsCrPje2HAuBMIEjzuREoZ8JyIQyWplPNhBJtGL1DLsmDOTXpYqlzRMsDCAbpDQjqqQRup8RBFWex62NmQsKr%2FPTGuOnNgWWJYJx7UQy9Llsp7T72kbIDOQDHF6EQ5LjvLGAT8pyOnzWRLuP0a0e8cjXDpMOPQ8LwGOqUBW60ilyvB%2B%2FewrNQAkvlgwx7dzlvx5Vntufdef%2FBErLYuNoJXQrwzFjYzxWxbpOJdIYOYhvDm77auZUsPgFwG78DqnyDG9274qekKHw0ZRhPseZXVoi0NRZTNC4e82FmfJf4z3J%2FQqLurlTa62ZalkNstg2oYTjnHc9oRrfSIDwK%2FpnXLttVOOx3jhZ0S2ntfydL%2FZ4kI1m2tFX9RrJxg88XEJDpR&X-Amz-Signature=d61de8fc04ae54453c1d3ab1a6123cc9d0960dbb4633994fa6fbdc695890d179&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=2bff1ae7dd939d565a739afcfe8a9ca54ba7703e7efab812a04094fcc41d8c3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BU2MYE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDATTJRBJgPBn217fPsspYnaeyUlIDVTy4MZIwTJCY9ugIhAMxPf%2FdoWcyTl1ukOTfDdVus9xyqgUrKHWF5%2B8Tju6OqKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPID3dhSRnduJSCVQq3APGL9hLpV2auJNSfZwDTsjg1R1sF1Xy9lWzcYZMKtHyyzqYMTUuPSVS5f7Pzn37dxfJXfP7MvogynLvVjCf1euy%2FqnE6%2FonkyNDZtyKZNnAeuSo66GJzmzOOAOX%2Fqwg8%2BSTxNTlCjLYQXYOp%2F740k1uMD8qjVz1yhrmjstU0YuXoYbRNTHu6Vc09XRYHve57Oirq3RtR%2FN8io1wt6I104K0behZzRU73jIJnGvosMl5xfSwlr6PqVmmzR2iY1FmPjtoa38b6QvWaXnsFum%2BASkPaKsNTbwnp4XokPj9imQf%2F6utdWr%2F8RX6rkfobqyhJ7TST6ZCdJ4GFSqt0iw1b%2FPzQ7QQZKerXQ0iVfHkj0HeJc9EnImmF7i4XW2mPF0wp9nIjIVx3ZcnK7odr5WY5csUfcHetFY%2FwiAyxmVk7O95fws%2Fqd6WN%2BQOYwilpJCzw1ldtx1yYrLrsSLLmKG%2BKPU3yixBwVYfDqIbEcYqZqlvDpyk2xfb4KThXl0V1YIgtXfIjwoXiZDPHabiofQcTjqB1NjGeigv0EjgrO2PjQkzs2HCdEUC1aQPWbZxUBYM9Qp4bBB9tAIVa9LzpEurPFXJianrvoI505gvuUgr%2B0oiGywF9IvioXJkX%2F6UATCF0PC8BjqkAfrkb0%2BHhNLPg9lEBVGRQjzQ%2BlLbT%2BQda9eWNmqYWE9euGYOMS%2FDTbxjCy%2BcLxWXrxbUKSFaYyNbqY3ygAJu6VsorGbiZok3OPqb69sfwd4NrFDaxFuGoWJei%2FqcTz93NGIQNcvXLTuFPqYWijue3E13q44ueOdBjMdUHFJf7czf7xw60qLRmUVGcj5PesE%2FKk%2FgT5%2FJgoa%2BNmU7bCnwojHhCQ2%2B&X-Amz-Signature=194fea0cf18c635c8f29e1be322d1325d22a5327992cfa86e6a03c7be0df62a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
