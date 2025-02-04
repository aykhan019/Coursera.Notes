

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=128dd54495bf9d2bc605d44a466eeaebcd93ade91d79b03c550ce4662be03816&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=bcdb395c8ef2fc9937b785ba8f9f253c80266494803b8e847bf5f25c16b2cf3a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=c3d4b03337946ccdc16abf5b5d718155df1764c95527c0ff36e09b4a7952f78d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=84a9c2cb70e6bb2dcce00ffe8d2780f3643668878e2ff55f0b3b6b4f715748d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=1b7210d28102acfbfaa07d7cb5976440c541a0dd2bd59afa2d460a4de8ef7854&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=252cc85bb73977c5a93c4df19fc5fbed7335026288395741f39c5ef23f51f3b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=cfe38766e6a76f6e03584c7f23db7bcfcf21917d8f5604a6f4e789dad46931b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=d8c4418d947f805d7607df2d56df8b5fabcafb03c6602dd0b3b14e7c9420adaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N3IXRC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCYAlAQsKs%2B5eeYPbjfaa1LNfiHwFEoBHD1NyG3fDokYgIhAPB75yQX%2FHSvcjH864po3pBUOLbEa%2Bwwog%2BRMpsZ7BSnKv8DCDUQABoMNjM3NDIzMTgzODA1Igyy9XI9xtOYGZkFrg4q3AMnSp8rlGji8uFbhpg09D3R%2ByImZpbQorWrqqYwe7sTW57ktudjUTboeF971YPiPANS7EKO1lHBdKPV8hHL8xubCKZbkOOWr27I%2FaIQc1e7cY2IIfLcy55mwENEFJqrez2J6UEnVmbSkx%2BSNkGJ922hN0%2FAZUWUsuRH6XfzmTZAv9g6q9gIw1wa4EE7lFvGL2k83ECPw1rk7v2x787gt4t47P%2BpX%2Frt1XeSHRccUj1hqAOVAzKCp9zLVwiyQWQZ6PfO7f3quQArVASJtrd%2BHb1%2ByyHCvPNEK7XLbFt%2B6A3WcqL8jA0aWA%2Fq4cn98nl7nb%2FRtREweoptA4MYLKHPf3HD4wcdv45IrYzrnhqpn4TYi5Kfg48DBZ7mD5tAS5a3jB4N7ejzS4iDfqYhJrogVZbQHnsJyDHGxeJ8wj7mGCCsiMiQxGmCD2Ff6VGx24vCzxK0j0h1ZbA0r0S3KInCPivqjoHXHcVoikFKcvyVIIGZL%2B1A%2FEH6z8Z%2FGeD4pPqBZePZTnAPFqKo%2BVUGKKr7msxkBcseSyYL8nr%2B76RpmMMpOx9T1djVf5%2FCMbBfqnH3uOYDnwHpDno8XymNVijkJiEbN%2BXWqNc8%2FLSYoFQHekE6ngaSjG3Q0KK1mCV%2BgzCV3Ym9BjqkAeV4SB49S2TtNiweG2BEvUA0AlyY3k5AAMenFROKK4C6xLG%2B5YFp9ddw3zIgaGKkHkpuBRrtCAD67iItIRIBmjuUBLVlg1UGgMueHQPp86FnVQWKyP1%2BJFFMKN5450AaBY%2FVrrpPsV1mbNaQPbEBCEoSa5c7QwuUdgy7VeiEOay06%2Bp0qeLLwHEhox4hBHDeZjciJJ8SRRZoRqxg1FBjTKDQioX1&X-Amz-Signature=19a6cda23b4d41d49a514f1dee3fc441892061d9dfc9a2e87f4dec62d96f7e40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXBEGRL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCnlPE1RvulJGYTS2bXz1he6r0mvv7UCBU6iezqWR3QVgIgO%2FKk28R1gFN6KaYLMBm6ddzjBMRyeSLbEaRaCmZOSU8q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDMt6WVTtU9ZfNp9XXCrcA1fi4Y0%2F%2FPoIA%2FONv6%2FG0SNbHtDfjvfzwTIfZoovRt1p%2BcMQeg7KRf%2Fug4Xf6XrzvdXTzxUASL5844UYdTkqyLY%2FJNpp2XHqo2sv7cRi7eIp%2FnKvtGFFlc1Cqvic4WUN8m0xlfO%2FqRUcPh3zgLPiNiB49FJokn%2B8hyvLf%2B%2FapN%2BFEl1i3iXYUXBOfzSatAolcaxLFQSZELJ2N%2Fx3pPwLEgMuXIOQVKokcYIo59%2BFiyeFa3poSGyj4stirEiHzhhyonZquwZ48jnQNUimfAPaJE9kOUHR4n66iik5c%2FxVAxQpfJ%2B8Qa0b5KFQz79RiO5dJfyBc3%2FHf7bcQ3XKheH%2FifrO%2BIZRt1BmN7uQXmsPiuFLT0Xm6IaHiojRjtcJWrmmijRDhnVJf%2FFUDTO6TpWSyeBpC3smb%2FoLihw%2FnTqhN02o8P9MdRkALO%2FPrS9eQxEDMAiJjxQPTrT%2BHc5HrzAv%2FlpUHZYcGXAQaTQpd1uiOaiRdLfob5hFUjvwwti6g7n3w%2Bj7%2F%2FDS4Sz3vj%2FkHsYDhI%2BUwjcSvtz%2FW0G4Be7kNGIJark1wdI7VMPM0xg3vzdiecoTU6T4KEh%2BDH40sgsxSSNbefKrnRaPfma7BS4o942fgbfEiAYxNgrBHrGmMI%2Fdib0GOqUB%2BpqqsQdtCPM51yEeSuiCu%2BkA3wJlugyg2Oi7E3dRVQRL49z5m4aXwZbpVtcUHsYuheZZ9ngQaLmv5%2FdD7JAlmMhXAMdidVvSrosle2wu6id9eBbXeyuti2Wci4fvbNPXE9u6FCa1Tr8icnejRr29JMr1OgTcnmB7UgA%2BHiP%2FUydBJC84ltLA7YZs9X7l14VEjopdhSCoCHtPROsB05Z9un7MjNsI&X-Amz-Signature=5eb2537557ad9f9aeea36c5b653a1a242fe476eba20dffa4291400c0b49c5d96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJXBEGRL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQCnlPE1RvulJGYTS2bXz1he6r0mvv7UCBU6iezqWR3QVgIgO%2FKk28R1gFN6KaYLMBm6ddzjBMRyeSLbEaRaCmZOSU8q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDMt6WVTtU9ZfNp9XXCrcA1fi4Y0%2F%2FPoIA%2FONv6%2FG0SNbHtDfjvfzwTIfZoovRt1p%2BcMQeg7KRf%2Fug4Xf6XrzvdXTzxUASL5844UYdTkqyLY%2FJNpp2XHqo2sv7cRi7eIp%2FnKvtGFFlc1Cqvic4WUN8m0xlfO%2FqRUcPh3zgLPiNiB49FJokn%2B8hyvLf%2B%2FapN%2BFEl1i3iXYUXBOfzSatAolcaxLFQSZELJ2N%2Fx3pPwLEgMuXIOQVKokcYIo59%2BFiyeFa3poSGyj4stirEiHzhhyonZquwZ48jnQNUimfAPaJE9kOUHR4n66iik5c%2FxVAxQpfJ%2B8Qa0b5KFQz79RiO5dJfyBc3%2FHf7bcQ3XKheH%2FifrO%2BIZRt1BmN7uQXmsPiuFLT0Xm6IaHiojRjtcJWrmmijRDhnVJf%2FFUDTO6TpWSyeBpC3smb%2FoLihw%2FnTqhN02o8P9MdRkALO%2FPrS9eQxEDMAiJjxQPTrT%2BHc5HrzAv%2FlpUHZYcGXAQaTQpd1uiOaiRdLfob5hFUjvwwti6g7n3w%2Bj7%2F%2FDS4Sz3vj%2FkHsYDhI%2BUwjcSvtz%2FW0G4Be7kNGIJark1wdI7VMPM0xg3vzdiecoTU6T4KEh%2BDH40sgsxSSNbefKrnRaPfma7BS4o942fgbfEiAYxNgrBHrGmMI%2Fdib0GOqUB%2BpqqsQdtCPM51yEeSuiCu%2BkA3wJlugyg2Oi7E3dRVQRL49z5m4aXwZbpVtcUHsYuheZZ9ngQaLmv5%2FdD7JAlmMhXAMdidVvSrosle2wu6id9eBbXeyuti2Wci4fvbNPXE9u6FCa1Tr8icnejRr29JMr1OgTcnmB7UgA%2BHiP%2FUydBJC84ltLA7YZs9X7l14VEjopdhSCoCHtPROsB05Z9un7MjNsI&X-Amz-Signature=e93b047dfe606cc1765f365877492a83adb25b38506b3cedf5b4dcdc1b9e9722&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
