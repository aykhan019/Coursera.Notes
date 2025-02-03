

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=525866c3d68d44579e3cc23f6ffdcdd8b317ff633960ca6fff3ff785d40193bb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=811d6504dda1c7413d1749ed8b7263f113a2bcb73f09c3e5a55a0ff477df5b05&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=2b4e0f72123f2d1101e09cf82434cb5b40a42563fdef6fa6ffff4de03ab93ea3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=577c36ad88ab665928343a13f207be09e2df470324a5cfd6d824e27a9e0dde8f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=ff0ed2407bb7fd37dd5d507584a58c4e11a4f19d8544bdcf63d1f090d67d5032&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=e9f91ebbf48bb987f708eab1a1ad4ad93212de843d75c2644fd241a936b28eac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=6549169edf9b7b2c1635bcb7bde108b46d32095b688459cc11fd052ae8d21aaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=bd6044d3326c2d6f762174148580e3fa10252aabd20541b08c4970c1ff11e35b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BKOEWAZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS9XMBkSZh1maEvks1dtFfh5xbcGow4PEU4C5rxOZxygIhALhMHLINpUgrh6UaxwHv1yrGcL8S%2Fu4fyESVlx52PvG%2FKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZkri%2F7I17LlMYIw8q3ANYT0ye2op0fAxINv%2BSjVBKohxoJn5QnIy%2BkFBWg9ZtHsITwq1JcbvwlnPtkPW0uEzZweg4Km%2Ftt7xgHU5oXcg5arLdSxrJkQ1E4fcrZW0%2FjZnvtfUA39mGbxEuuCDCYWxAm501vmSBBT%2BfPk%2FqdDFoE4g2wEYjs8sgqsLS9seM%2Bd2c1Qx2TBQMoKx%2FR%2B%2BjdjFl6RMT%2FpG04czns%2B9mLTx7C4AhvFdJzSldemVHvFYV3tMKT%2FoTboVA62HokssXflK9bdsgknDSYkWRZJLEH3f37irpU0brth7szkm2NMrgYbF4qztCjKS5A2Or%2BRPFJPymTsBZp%2BNbFZapNCWc6XRNu9u1s3uVmzXioY4vsAYlL2FfMFlorAeqQUfAPvf2ClLsKuUMd638yJ6Cbw0j1EyKGn1WQzNtc2z75AuW43xME5rkgf58y4z%2Fr6SQ3imWg2BzJmKy2M11ZnOt%2FF5cate0h%2Ffw74%2BSKAMZnzofimQmBPJktQF3iis1Y2TPokvegPmA1C8OYg6mGtLRszIM4ppegBNjPbWt0wZWDeN0eI1niIjsSPy1p%2BvOreKdFU6tc7oCXkyNu%2Fkuy12RrJwgC2aRy%2Bbj66PjUCXkSIcYMVMPi6aVdxz2LmUNQBWK%2FTDbv4C9BjqkAXJRi9oBCq32fBgJXvtUSSlTQiEVN5rgbaRRnqLX4qpkpTjL2EykPlYVQD1aKPuUGZ2IlE0KE77Je6syHpC4LxkkIL5FZ23TFotgbUFHQ37P%2Bw9bhMaalonrz%2F5pUuEkBVtz%2BfBZWn2XkLSUsNMkwHm3kuOl2t08UPXwBZdXbgx4u9%2F%2BYxBmyx3X5%2Bbwm09X7BlTafEeG8oUy1XaKR%2F4NjcQXBXi&X-Amz-Signature=ba6f030dab366ace0fc48c9f6ee48c9afdb45dc594b80c66b988c7fdf7db2b4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPPHC4TI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIbNWc6SYFhCSiwyGqdGSj8Qtliqr6lKBTtgFe%2BKPxTgIhALwyjhMBkVBGST3mBwruDvmx1ORRCzPFG1Cypfq5D%2BIOKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BhJCpGQrtr3DJag8q3APP8VTv%2Bi4vhQW6aLk0ruujQEn6Fjd43uiUz3VJ7GjbXeA8ZTm4eVlhnQLg1U1BZq9azPmdS600I7zEl0s1LDEfwRei8rCDv0KcorItZzqvngmCDv0X7z8nCcGCVbYWuVXxQpi5wWY0w8WQy1JdIfvNKMLvNGhqQV0j5w%2BAW1QRApF94ZwhtS6TnYjXMIuxOfHEKhg9Aa5udb%2BEil458ZrHhj1wt9qBYkck1Lhon37tjt3bQBhZNrtk0xOolJ9D4CpOeXvBcdWUWk6opiCLzb8GEKaQ6%2B8KnB5gICfU%2Bkzqf8Bik2bGUm2R9s5Bd7zDZi3ekayMOCzjW6XZzM78paS1n7geuF8EiHmR3A1fP2soYJWiAORlGpwltcdI5S1PRV9RG0mdOK%2ByDkIEW8QVsbCmbNkl%2FqcU81DumXV0LPUO2h7VamU%2FSYJlSijnf3pH2f25dwunxsqctR%2B3nugTqoqHMlaEzhvaNHsZpFd%2B7TDG9B9SU7UwJHwmVDPM0Ah9Pyb5tqSVg3H8NEEW6YFKfoME%2BpCO4qXTzzUuUdGL7ezFy0iAsJM30rqYbBMqGJIgIL%2F3t5SFuGyQ9YgHz6a7gSo7brxsfe1xVUu%2FxBdaAm%2FgwvotLJ5hKg%2BMwkeCpTC8wIC9BjqkASGn9cf0IihAXPymUnql4tipZOsJZYZxa12qNx%2FU8AsddxWjpIxHHOZEVTxcR%2FVs2gImxCUZxL%2FASMeercNZe9MHD1%2Bei8UhDrVaYw3%2FBe0UArBvl%2B%2FBkRwMjlNgqD6wdUQ%2Fd44rSJtfSURrxMMtJBQjVbMk%2FT03XxFO%2B4ljZgn8jpg1vOjgdKAGl6kY%2BPtPylvx1g3NNS8mnldEp4JdA1Dwy5Zn&X-Amz-Signature=4a6d2ef34feb40fd22e504f1c3d8b1570cff1662d3c87d80cc960848b0b27cab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPPHC4TI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIbNWc6SYFhCSiwyGqdGSj8Qtliqr6lKBTtgFe%2BKPxTgIhALwyjhMBkVBGST3mBwruDvmx1ORRCzPFG1Cypfq5D%2BIOKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BhJCpGQrtr3DJag8q3APP8VTv%2Bi4vhQW6aLk0ruujQEn6Fjd43uiUz3VJ7GjbXeA8ZTm4eVlhnQLg1U1BZq9azPmdS600I7zEl0s1LDEfwRei8rCDv0KcorItZzqvngmCDv0X7z8nCcGCVbYWuVXxQpi5wWY0w8WQy1JdIfvNKMLvNGhqQV0j5w%2BAW1QRApF94ZwhtS6TnYjXMIuxOfHEKhg9Aa5udb%2BEil458ZrHhj1wt9qBYkck1Lhon37tjt3bQBhZNrtk0xOolJ9D4CpOeXvBcdWUWk6opiCLzb8GEKaQ6%2B8KnB5gICfU%2Bkzqf8Bik2bGUm2R9s5Bd7zDZi3ekayMOCzjW6XZzM78paS1n7geuF8EiHmR3A1fP2soYJWiAORlGpwltcdI5S1PRV9RG0mdOK%2ByDkIEW8QVsbCmbNkl%2FqcU81DumXV0LPUO2h7VamU%2FSYJlSijnf3pH2f25dwunxsqctR%2B3nugTqoqHMlaEzhvaNHsZpFd%2B7TDG9B9SU7UwJHwmVDPM0Ah9Pyb5tqSVg3H8NEEW6YFKfoME%2BpCO4qXTzzUuUdGL7ezFy0iAsJM30rqYbBMqGJIgIL%2F3t5SFuGyQ9YgHz6a7gSo7brxsfe1xVUu%2FxBdaAm%2FgwvotLJ5hKg%2BMwkeCpTC8wIC9BjqkASGn9cf0IihAXPymUnql4tipZOsJZYZxa12qNx%2FU8AsddxWjpIxHHOZEVTxcR%2FVs2gImxCUZxL%2FASMeercNZe9MHD1%2Bei8UhDrVaYw3%2FBe0UArBvl%2B%2FBkRwMjlNgqD6wdUQ%2Fd44rSJtfSURrxMMtJBQjVbMk%2FT03XxFO%2B4ljZgn8jpg1vOjgdKAGl6kY%2BPtPylvx1g3NNS8mnldEp4JdA1Dwy5Zn&X-Amz-Signature=176b21f1dc619575b4d7c8246f87a7fbd75e2b0d36ac29e76239be045cedb173&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
