

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=113e32f8dfe1e8ce6d5a72902baf8a26bbd6254c86900d47e8f802ee4df5ffbd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=b625146caf33b735e5ed32566ceebb1215137a2db72261018fc88d5ac1df03b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=b3a4e144b3ec998daf61c09db217c573e65073669e4e96ba621337bab7414030&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=53e2fe176d3e525557059cbcd13976f2a1140b808d0795e331ced8b3b116702d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=ccdbf0bc98edb8daaca735d5515878df34abb64aae2a67b7cc950a676732f423&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=c61243ce2f8877dbad566fabcd5833e8229316ea017f2600b6f88f2d9d99b531&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=fa920d41abca57ce22e327deced0c45f647c43487e9e3bc58c1159e94842559e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=83b5f0404c20958cab2b8a176c563c15a8e042acc2b58de416a5eea3f37c8d72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRRM54Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwSGtO5BrnrMV73ourNc6Zq92wVZBTHNZU8TotJk1J%2BQIgX74QXmN0PeTytxMLyC0dkPGw%2FegW6N%2ByNvVJ3lUACXoqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGDna8ZJIWVGQuGfTCrcA0xhhklacH3kkCHfzsphp3fxNgnwiv8xLy96aETCEG0u%2B1nVimJXWmDrKrpdLLrUgKvir38rEbvV7wgXF099n6o5HHijTzFiNJJCpb7IFUN8MPeGopLXxma8qE6NlQIRKPNNSadWxgS%2FUKRXhC3ouZdeYqUQeX37hGC7g5Ua7wbOdGiQymLGzacfyGjbkmHCt%2BWka74XvuHF50cg2g6Hj%2BW3gHQ%2FuGZRtrUfTYYqtuQZ7YzQ8zs1TuA5hlnrrFa5BKHcpltKna%2B%2BoSMiPXqL0iiHFHih5J44ekTB35VSl2kxCL1LOe0EtpQ%2Bz3Jux%2FWXrhzoY%2BQo6cYb8F8uUWpeWKslkNN6KrvOf0ESZyo7nYyWVUqaNVyWlmVO3kAaOMUTB5D1WLaF4vK%2FXoLVxhgSUNG0TSFxJvB5YU4Lx7u9VACQ9J%2BDP%2F1kQV7kNjwE5vYL6hjRlSGudqTdw7haeM1KxbmziSQCEwhYkjt2p2a2r%2BytF%2B5rqAo%2FQ8CZz2IOfyJM0mGsqmqSC8fc6sTEubYskS%2BoesgwFIRaH4KtXcQcqF0wAUUF7OywIsO11IVZD5Ye2pv5NKE8wJL1h%2Fe3sXAQ2j1VET2tZ5yMIw3gf7b86ZAFRfBOyLWcJJyhcAX%2BMOXY6bwGOqUBkrzerTLHz49yij3%2BVVPtUJYJ0kzBq8yN0tWRA2QDZe9nZDdsAaAXcUsDLtwr98jrGameIxro%2FfWviN1wdh7y1m%2BwKObxNqz5ZJhRqOPbGOYeuPUzBsYvAcVKTVFafylpu7sT4q5zE7%2B3zsYLMfu2M2%2FDqhjuCgUK%2FRCwpNrpNe770uVEO5MZ%2BHMTrxyBMgstYcQnN3jMgac8Q%2B%2FNT9i9wLzjAzRp&X-Amz-Signature=ffc5e780cdcc92c316c15e2237a1a7c7686c17cb202b23eba27a8e9e6e083efd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYECLYTK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgi9gwqXECpdXdYNGhQRGPkmO8KL3DZwGNOEH%2FISFtBwIgSHY%2FlBHaSEusznMwbnpi42oEzFOYD%2BlgkJpTWPVwZyAqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDoA9lwhhQsZU%2FgrxCrcA5%2F8kZmKGJj1Dw6Fm845EqXyOkjIKo%2Fg59EQsRbRF%2By2rbyVokT7A6fsD8lbMwPM44beT4cFv4QX8yUPKA4r3ldNJrjnkFicKDvO7mNfiTopK7%2B5yVJmQMTOfff%2FAfwenRAqS384h3aztwy6aYMAd4MPficKidYl2DMGEwqoCwgpv%2B76dPNA8ql3J5Ltm9TFtA2%2BmY%2BSH8CElghT2vQnCxmReoK%2BUw8nxzD8uIlV8wioBK%2FSuD8K%2FNLfQfYhPOaqyqz%2FyelUuSAXwpBmG8br%2FjmazQUhsqOhsu%2B2Y%2FlWKkGTgh9aAPg%2FY14jyWy7hb0Ww3UTQ1D21f%2FZ7CR3FpOebjZF0ZkKHwGq8vNlp4YfsC4d6jRaQPvjxC7NGkzpiBTdIH5veOFZu9njxEMojvdclh58g8PmXGkicXpSts7K89ywGLbNkE5Bz%2FrO09gXpHHNon4Y8o6wGdfofUb46Bh69pK2vOEsRilaaiwRUsr%2BN9IJEyXPUfwq%2B8VaCCqhP9rTxTsB2mos9Ln7p7BDNft5QGyVotID2zttEcr3d23M6TMefOpDDwt27n8wEaCh0mlfsfNHkjFb8KXf2PHHEeq%2FvfHu7AQajPRW4V5PdSC1g0qHQqmz5BjsPOMnzcM2MKLY6bwGOqUBMb09%2Buv%2FSk0jiZM%2FBSHIVE5EuroapAt0Dv4rHadxs2hipudzfkIQP8d6L48NGdubDNJggRgx16iHH29cq436K%2BaZqfCOIrsY8qZwW12VT2RXQ8joL0QgZfy5xHW16%2B2DssMLesyuCxKYUv6N9mwTrUWp5LkzzaS%2B6%2FRUUHXMkcK%2F1b5JMetacAeIP80y2Iu5pMCBRc2QV580yApoJXzvIWdLaCz4&X-Amz-Signature=5fd5da38f7da61337f62c4e1354d289979692b54ad747af7404d50c2fdf81bbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYECLYTK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgi9gwqXECpdXdYNGhQRGPkmO8KL3DZwGNOEH%2FISFtBwIgSHY%2FlBHaSEusznMwbnpi42oEzFOYD%2BlgkJpTWPVwZyAqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDoA9lwhhQsZU%2FgrxCrcA5%2F8kZmKGJj1Dw6Fm845EqXyOkjIKo%2Fg59EQsRbRF%2By2rbyVokT7A6fsD8lbMwPM44beT4cFv4QX8yUPKA4r3ldNJrjnkFicKDvO7mNfiTopK7%2B5yVJmQMTOfff%2FAfwenRAqS384h3aztwy6aYMAd4MPficKidYl2DMGEwqoCwgpv%2B76dPNA8ql3J5Ltm9TFtA2%2BmY%2BSH8CElghT2vQnCxmReoK%2BUw8nxzD8uIlV8wioBK%2FSuD8K%2FNLfQfYhPOaqyqz%2FyelUuSAXwpBmG8br%2FjmazQUhsqOhsu%2B2Y%2FlWKkGTgh9aAPg%2FY14jyWy7hb0Ww3UTQ1D21f%2FZ7CR3FpOebjZF0ZkKHwGq8vNlp4YfsC4d6jRaQPvjxC7NGkzpiBTdIH5veOFZu9njxEMojvdclh58g8PmXGkicXpSts7K89ywGLbNkE5Bz%2FrO09gXpHHNon4Y8o6wGdfofUb46Bh69pK2vOEsRilaaiwRUsr%2BN9IJEyXPUfwq%2B8VaCCqhP9rTxTsB2mos9Ln7p7BDNft5QGyVotID2zttEcr3d23M6TMefOpDDwt27n8wEaCh0mlfsfNHkjFb8KXf2PHHEeq%2FvfHu7AQajPRW4V5PdSC1g0qHQqmz5BjsPOMnzcM2MKLY6bwGOqUBMb09%2Buv%2FSk0jiZM%2FBSHIVE5EuroapAt0Dv4rHadxs2hipudzfkIQP8d6L48NGdubDNJggRgx16iHH29cq436K%2BaZqfCOIrsY8qZwW12VT2RXQ8joL0QgZfy5xHW16%2B2DssMLesyuCxKYUv6N9mwTrUWp5LkzzaS%2B6%2FRUUHXMkcK%2F1b5JMetacAeIP80y2Iu5pMCBRc2QV580yApoJXzvIWdLaCz4&X-Amz-Signature=eddf3ab3cfafe601790b06e427e29d8e08a4b0b835d4183df73987d3ea3c76ba&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
