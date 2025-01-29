

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=728861fe085c3228cb25962d4b2c242a5df040b4d4ccbbd59f976ad9b061ddb0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=54c7a6c47c11dae1c28d39700b839b292c7b72c8e6c609d16bdf9263684d3874&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=4a62bbeab708b231ba4582169d2bb704ccd72ecc84ca86d9bd4a058d26c96ea5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=e9667d6bcb4e5fd55f7bce374f48ca11c53980e3ce2210f2f2fec62760dc9b96&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=e0c0804bb39e1954805e8e33d4fea24a6d1269907f4954487aaf1623643b24d9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=8a2910424887fe92be08b86eed001dd86e41356c147a683a17b53770907ce2c3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=26d739083994637d3b82fe8ea7705cb8e33bbfefc2e62ba7ce753f8f46e3854c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=1329f70331e3e9a118005fc4992ef37eb9eaf3f6019a1ed9d7130db6ac02dbf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRYDRQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAr2ba5hQ6bruNvZXosfXUOIF0Iu3TXB1UkCAg7a16NjAiEA22DW%2BRxElH%2Fpb4%2FVxfPxElN0rvLAn%2BGg6f2wS%2FOAKn8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjJ5Q0sfem644rwLyrcA3m5mMcPnsjt2YNKLf6mVWj5mhueu5tl%2FYlEepFAe9K5VmYjfE9hsYeGzwn51mRbC7KuYtY4RsetSCXDFB4HkvY7Z2R5cfRH3s2hisG%2FCmQwz5%2BDsGIEMp6fKPYV5rZCn6qiP8%2BfPC7OKYo88sKbsr0pjQz4aRYPgoH15UpRW3fs0SdvHGTEdMPF9KKXnrQlpeF9z8waaWH4a5XlG%2Fw8Ohw%2Fc6dZwC8q6Oh02KCdD4i%2FqOh1HIedVecSMn4umoZKeWVvqut3d7Q%2B53D%2B1aqvrDOfOHJCJ8kct%2BlSPm5aEHImlZ9lNPXQmhwOHVsRdWWd357ZBHvYHOqaEKc%2FB%2Bh9isWvcoJbVw8SD8FFFL1SXArRIj9pDsLSeJUE3E2DNjtvfL3rlQfupgapiQerNm%2FJn8x9LUP%2Fkm4tQTIc003gUskFq%2Bj4YGTQKAgl%2BZndDcjhlVHpUKSuVorMEg64RjL%2BJqCM1DAUi%2BqpwbRGwkP1wE5swLgFV3YLEOO6vvY%2B%2Ff386v2RgHtrla%2FJnBOp0ei5QI43YftN%2FtIqIWb8Xmq6jAVH8QUxcTYM0CJj8%2BM81VRWP5qYC6CVbcGYXul4XVgxANOsKqCrGfOyJL97HnPnCJyDK1XVn%2F8ePG9QO3yvMM7n5bwGOqUB5jWwN0stHjrCviJi0unppIyKFq8OFi592BXTkRBnSo7uQ3JLQRUGB5hc1gKymt9JBuxrjajnyUs%2FaOamaWoEZffji%2BFtUUl7HdV9oiHPp%2BRMPn6HIdkMK0rXooAhv89OIl6K38uny6AH2GgvyyU0I1F1ZEX1k95ntoOahPT1pkHOjyUCmbdjw85T80SFeNX0WjizV76Sxsu%2BTTyARuiBQ2rvdrdU&X-Amz-Signature=54fa6c58f276ecc03e9ef1b29a5e64c69514b8f5958763a9ed2836d6b55b1668&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOLRWK3R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIDZNaqevd3QLfcv354zCcX5%2BSQ%2F%2BZmKyF9dFCui4lUolAiEAs%2FA%2FqB3msxmd%2BrwDsJx0JHIefXjuxXKxtg08grHn2SgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0TuRKu0CeWRFE3SrcA%2F5SUvdrFpl4x2lMqdmNLeXEm%2FXuNZOMxZElHJ0hFFrrilXPVsWcE0F%2BrUl7YkU8j3NE%2FjQ7DZ%2Br6PTyIr%2BlZLTl6lM%2FE9W4BfgFxIHeu4kSgThJOLuelCYZu%2BsHpqE5kf9%2FtK8ngDQXVAgp0E96iOgm82Yj0E7tyE8BGtBD0I1t0uLhf%2FjUbuHWFw%2BdPaMl%2B7ReCm2jyE7KdjQ4BOWC1exh%2FsTTfQnUyKmDFiDlXPxXMAu%2FYJonDD6Lj9fawX4LWpvis3t%2FGJvXBORoWRZTondbzDQeN%2FjsKOV4uVqPSxlu%2F%2FVNOIkt3QVXr4x6A6zveOXU1F1X0Ir9DdwbqQfVUaeG6gRLKWyjbXDoyTB9qk31ZE6hOKqScoi3H7rU2m9RUE8lDvKFoNwESJaf9r2Df2tgcfOV7amed92e0pgtc0u8vOByPLTuiY5yDH6l%2BuSJ8YrpXL5iYrqVpZl1C9AnSsswFXiD8i0FBz0GCdRkCUzLMOTRFXPL4070ShDIve%2Foj672YbYORykzfT5t5K7Xsbiiq609yNC3anRS3xGb07F%2FXal7vjcmjo0Xdj%2BkECbulxpIM0FdFUNTrJEEh8Z%2BCfT9y0jHv7jaxUMfxB5N5TBsVD0NUXkjBVCkd4ocMNjn5bwGOqUBPyQyKCMjG4V1TCiaeKhzixsp6ml%2BFyUfd0PeL2dssyvKooWNc2LJgX1cx2p5I9qq5DU%2BjkQGXj9tgSd36%2Fel01WdXFXOwQpOjWWpMjoGrkdc%2FOeMPqSDXMi0zy0sEu6iyyFVLIoFMLXrKLNCDeC6UdI6AJpnHgrC1xsa2cSnhoBmp%2FFZxuMH4IWt0sOgEcsup2Pkb6AdC6CAeQmyv%2BzfL%2FHASZbH&X-Amz-Signature=d5d34b29db63c1c1689607cf40c2527810db2a9aebd29a56519c75a6b48e8877&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOLRWK3R%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIDZNaqevd3QLfcv354zCcX5%2BSQ%2F%2BZmKyF9dFCui4lUolAiEAs%2FA%2FqB3msxmd%2BrwDsJx0JHIefXjuxXKxtg08grHn2SgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMH0TuRKu0CeWRFE3SrcA%2F5SUvdrFpl4x2lMqdmNLeXEm%2FXuNZOMxZElHJ0hFFrrilXPVsWcE0F%2BrUl7YkU8j3NE%2FjQ7DZ%2Br6PTyIr%2BlZLTl6lM%2FE9W4BfgFxIHeu4kSgThJOLuelCYZu%2BsHpqE5kf9%2FtK8ngDQXVAgp0E96iOgm82Yj0E7tyE8BGtBD0I1t0uLhf%2FjUbuHWFw%2BdPaMl%2B7ReCm2jyE7KdjQ4BOWC1exh%2FsTTfQnUyKmDFiDlXPxXMAu%2FYJonDD6Lj9fawX4LWpvis3t%2FGJvXBORoWRZTondbzDQeN%2FjsKOV4uVqPSxlu%2F%2FVNOIkt3QVXr4x6A6zveOXU1F1X0Ir9DdwbqQfVUaeG6gRLKWyjbXDoyTB9qk31ZE6hOKqScoi3H7rU2m9RUE8lDvKFoNwESJaf9r2Df2tgcfOV7amed92e0pgtc0u8vOByPLTuiY5yDH6l%2BuSJ8YrpXL5iYrqVpZl1C9AnSsswFXiD8i0FBz0GCdRkCUzLMOTRFXPL4070ShDIve%2Foj672YbYORykzfT5t5K7Xsbiiq609yNC3anRS3xGb07F%2FXal7vjcmjo0Xdj%2BkECbulxpIM0FdFUNTrJEEh8Z%2BCfT9y0jHv7jaxUMfxB5N5TBsVD0NUXkjBVCkd4ocMNjn5bwGOqUBPyQyKCMjG4V1TCiaeKhzixsp6ml%2BFyUfd0PeL2dssyvKooWNc2LJgX1cx2p5I9qq5DU%2BjkQGXj9tgSd36%2Fel01WdXFXOwQpOjWWpMjoGrkdc%2FOeMPqSDXMi0zy0sEu6iyyFVLIoFMLXrKLNCDeC6UdI6AJpnHgrC1xsa2cSnhoBmp%2FFZxuMH4IWt0sOgEcsup2Pkb6AdC6CAeQmyv%2BzfL%2FHASZbH&X-Amz-Signature=c3652d4b173744f4e7642c9c6dd3b2e299161931dc9b5c8b6b538d1e05c26e0b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
