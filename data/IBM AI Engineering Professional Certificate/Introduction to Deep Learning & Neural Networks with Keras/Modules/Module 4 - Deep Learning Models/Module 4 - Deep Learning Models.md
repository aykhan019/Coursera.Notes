

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=cba6fbff0e6ea12c81c574d3903015691ed6022a4e9ef3c65f73c1e81994a80d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=971ab616e7c1d22790ad3a2f4932c0e54da3d086dd8630ac0da41d9943412f34&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=6e5f32fcbe4380d3e0bf4b7b6cb5ec2f5087d47b07798065f22f23b6fbc061bb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=d247dabbacb4706ec53a98a1056c85f54992de1922da0a44fa8807d76c3eb2f6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=4b32382c18650cefdbddeff98f08d0cc803ad157f64cd4491a401b6732b6cd16&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=86a1c3c02f666ccc3eda679637fb043093c15246f576f78e2219f1d140ed5270&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=242da1bf2861d79a66f68ad9fd91dae5f1bd627a58da1c432d14891b587b19da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=e70d0c2f6ea7eda88ebd20a37f250807c43c7f8b5a04670f4406467cb3462004&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHY6VLO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFKVzKtYmajPjxfMntVkxQ8mlEIu7o6M8A6RV58jFEoQAiEAuI8u%2B6vlQ%2FmHAkPJ1Aw3iGL6kcvt2cxgnespqQmlxHAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt6Daqr1%2FDzRDkPZyrcA0FMXKHi8FFa%2Bfpr4I2DhFXXNoMJVqWWxefvaLV%2BqOrSDpuJUs1UTFmP2yTwnbOTwgaMpXxTXoaVpfKBhZFntTnYl5ifQPTbKAkmu1QDWoSmR2I1jenYK9qtSiz7icrxFcNZUpd%2Fq6UuuaMgnRKyM6i4AC95MnZOdv5NG6GnC1%2FaRBhlLAhgeWciZFsnARrLOyl%2FwV%2BQgitpIzcC3pN047IoiU9FV1%2F1UnuKAOj%2Fw4WCnsUk%2F%2FirLYiOalK4ASw2eA0DM7YhKI9Pj0w9DCWuA714BCPTsEhZ6udn9GyAxluhXZ%2FZbT6pzBA8gpxfxL8slPenXCz%2BpOyiphUvq%2BFMTM2HYa5%2B0F8R3MRSxpkI%2BAh1OZ2mRNSAzka0bxlsYu%2BwnsPgQO2UdGqjAQRo6DhLAWbj76lPkvFGROtvfo3GC5p7JERVj4%2FIpfSPlgMpivy7kknOkMWDjaQTcfjaSK9u049%2B9HW9ym1qMsXVZG6eSNaeMIOy4EgKVY2AGjl6Crcj7FuYT0rTR0npMPHpefIWBBWp3rj7WjaJhetdxpnijjd%2BHX2wKED6A1uONzc7bRbuiuWDVwiFVYXssp%2BHSxyQxnLLN85kgWjsd13z4Q6%2Bcl%2FeN80yVPC%2Bgz2X0bSRMLuWm70GOqUBiSk3o4z5pG66eb0TYuWNHTUQ64TZFgh1gDRNUBl0cLs2pQeMLJoqrW59KTsA6lJVaLpw31wqvF8prqlzpEbPgx9u%2F4XgxEU4aA6joEq7f1%2BUKfGYw%2F2vMfMc1aZ0Y8tBofx2PF5D%2BYacZnU2Wxln%2B8pz16PTbVYsybDAS2iYn38mlbyvsYE08Qf74Hxs1GUOkxnIpuFrMvuPE%2FJILG6AjFJpqijN&X-Amz-Signature=42499e5a948e8c987914203d32977133d0e682daa249674d993a19befbbfbf2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVCS3D65%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCiYdw1a8Bn1ocl3i5iYox%2BB2vaevVrP4c6m05d1YfqHgIgRX7sRLaZv1q3lrKzn%2BFrxJPd3y4jwcyTz%2BckqXevru4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFutsOE4yijLT4F5qCrcA0838TaXvux1uq49rwmurIwGP1AzwSdvSpQXkQJD2djE6OLVjhaQFuHStnC0oAdBJeRD0ClO3ii%2B3KOsg8jIbuWULZlT8CL9G1I5EBsJbMKaGODH1x1FhrHDrjT7Gs7Eo63%2FUSyBjw%2Fhn1Ifo0p3TKU8SsUwgANeO3ZHtkdkL5clHHF7NooyxG9%2FsCTxGsEs35tKDvqc4mGxatM1%2B2IVLcyEQgtVXGNvmd9RKkuJrPuMcbxcxStpshM2IoSHGNvhg3dU5zmXxOz2ut02Mp4toPwgMS5orFFXC8Jb8GuQ2wGLqxgeYshuhheLloyKWIUyEzJE%2F%2Fn%2Fy7fdAvus7qVRH%2BHgrq85MM2vTjicDqEB7NkSqr4EZwbL3Gbt7DyFOJNeSB115w%2B4KF%2BQe9zPIfiJBE2ychiGtNVZhn4u8h8xDD6A9mo3LTfS80eLB2YmTEyIOw0ccMBHcHC4Ltis2HMnkR%2Bno8bNi5tB8v8AjhJEqWmQ6ijLOvw%2FE5Oo1S185GBlES0rlCxzfMr%2Br%2Fd2tzVeSLCjxFoGGDRUzgIAZ0oF33KMVzvDJgoV2ullbs4QH2%2FbJ9O3Cg0OpqMT6YrmCfeaI7zvOA5mPSpYyHkc6%2Fe5ZALRDsl%2B6Jo9Z0umha5QMPqVm70GOqUBIlZRoU4TIpX%2FXz%2FhZZcCq5cL06yAOLZ94TJQHIwL5R10zzp52TBlpQNcoP5NobaPO52V2dhpYvhzv5QBT70FzWljh6wtTKqS%2FGo6N4d01bpkP1D2K4Z7ny1iIIX3WBio%2BT0PV3gWtMXoVuGtAt%2BgncEBuzFq%2FHBFQI3DdxxkzhgbFyEsI%2FcUIw64kHUB3lC%2Flks3WGh1q9J8HOkQc36XflWzuajV&X-Amz-Signature=ed69201fcb3c07b9e25611ebaf3334854c744fbdb2e49bd555ee5079e7f42c51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVCS3D65%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCiYdw1a8Bn1ocl3i5iYox%2BB2vaevVrP4c6m05d1YfqHgIgRX7sRLaZv1q3lrKzn%2BFrxJPd3y4jwcyTz%2BckqXevru4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFutsOE4yijLT4F5qCrcA0838TaXvux1uq49rwmurIwGP1AzwSdvSpQXkQJD2djE6OLVjhaQFuHStnC0oAdBJeRD0ClO3ii%2B3KOsg8jIbuWULZlT8CL9G1I5EBsJbMKaGODH1x1FhrHDrjT7Gs7Eo63%2FUSyBjw%2Fhn1Ifo0p3TKU8SsUwgANeO3ZHtkdkL5clHHF7NooyxG9%2FsCTxGsEs35tKDvqc4mGxatM1%2B2IVLcyEQgtVXGNvmd9RKkuJrPuMcbxcxStpshM2IoSHGNvhg3dU5zmXxOz2ut02Mp4toPwgMS5orFFXC8Jb8GuQ2wGLqxgeYshuhheLloyKWIUyEzJE%2F%2Fn%2Fy7fdAvus7qVRH%2BHgrq85MM2vTjicDqEB7NkSqr4EZwbL3Gbt7DyFOJNeSB115w%2B4KF%2BQe9zPIfiJBE2ychiGtNVZhn4u8h8xDD6A9mo3LTfS80eLB2YmTEyIOw0ccMBHcHC4Ltis2HMnkR%2Bno8bNi5tB8v8AjhJEqWmQ6ijLOvw%2FE5Oo1S185GBlES0rlCxzfMr%2Br%2Fd2tzVeSLCjxFoGGDRUzgIAZ0oF33KMVzvDJgoV2ullbs4QH2%2FbJ9O3Cg0OpqMT6YrmCfeaI7zvOA5mPSpYyHkc6%2Fe5ZALRDsl%2B6Jo9Z0umha5QMPqVm70GOqUBIlZRoU4TIpX%2FXz%2FhZZcCq5cL06yAOLZ94TJQHIwL5R10zzp52TBlpQNcoP5NobaPO52V2dhpYvhzv5QBT70FzWljh6wtTKqS%2FGo6N4d01bpkP1D2K4Z7ny1iIIX3WBio%2BT0PV3gWtMXoVuGtAt%2BgncEBuzFq%2FHBFQI3DdxxkzhgbFyEsI%2FcUIw64kHUB3lC%2Flks3WGh1q9J8HOkQc36XflWzuajV&X-Amz-Signature=5a77feb8187b564d79f0d71c1d6b573373c37e4b53e5dfb99de19a3acb9a2f82&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
