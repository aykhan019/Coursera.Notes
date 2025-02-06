

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=087676d58e0bac6ddff12c57eb22f269d6f90084237366f685efab92ada5dd16&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=c5d066b214df37ed60ca77dc645c8a825b7b73405fc9f03c617f84b00a84de45&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=8fa0bac837c1bc9771abd607f608dfb1d3656e120743f4fe9e96169a620bdc12&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=a5e5fff133c952481c04ce6e2c177b4d14538a5f39f34348cff614191c302089&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=865809f4c23df3b0e7c3b05048798f3e897ff49b1ea89fa1860ee328236aed29&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=8ba813f3daffbebb6cf394135566bd40920237b11506279d004377519673d238&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=c31931e131f7f1651d69738157189352f1ece777dd0758a584d97e138d7ec093&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=098fcc19aa9ebc97efaf6c3628a75b23d38921e7447958f3e8b0b8b8675537ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOPB7VEN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCuJFoxPHHobhv8VgsW2nGk91Oq58m%2BSZsTkturCmo4vgIganpOwZaUnVIYb%2Bc62CF7Os%2FHsM%2BvMR3CS0DZIpC63Pcq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDCzYlMRYa9QJTUqxtSrcA2KM%2Bc%2Fh4mxJX6rbOOzWjEx%2Fxr8TCNLp0d5ks6tqQwXAyjiH2CFZc%2FowfCKUIVD6s6CI%2BXaUkEKa1lxp8VmTAmqzvLm2ew3jjWsZB9EfPhtbMeIiLqCU75cVyCL%2BJQ%2B0RkktlbVcG3nuT3M2vXNbnhG6fHuybqEu1OtykMOEQoRkERSXCmsoKF4yjXJMynzgi1cdvvcWr4wFqT%2BPZgXSde%2BEhmgVmEyDtsVqgi2IiohR6%2B%2B0iJ4pPO%2B7u9PbQywr8ACB4aie8P4lk5Qn23yx1WxnqCJdzn3oQ%2FD4Gq%2BuaRYyU9wY5oiaNbE1gKe87LbpTdWU3yHdpRGbCJ4URewE9a2pa03QFycAlGgI91880Ssl00DFu6CHxsGyE5at1HCo97pqowr352o7Eo%2ByJOrW83XUD1TtqQTKvmDo1ZZBod4bBdRP%2B9FheaJB6xBn4DjbVdT4sjp8sQUi6GonzDHP68IyV09DbQFJ4z4txgs0TLSWJCE%2FBnFCLBk3CF123xen8fDqxR5V61Yp3Wz6dBTWQAMZ%2FmDXQRvpG6aD%2FMdtTdWh77x3stjxrKmEPV6Xk1ao9WuFtNFLEITNvTGqrR3GYcy7WFPvZuuvvZyDuhJYFYonCL26%2B818nH0qdUVKMJ21kb0GOqUBgd2ecK6cZijV8udvJDo04fLOqUIzOaIJDSlZ%2FbXxy1%2FCFN%2FrB4U%2F2TyuzwkoGKPVB7b4ykv%2BNpw0NCDSrZtjhOuwQ6qBOxSM9dsQTqucyqJj6Uk%2Bj%2BF0p%2FM%2FEEpU6Nmjt4cCWjQPYFJv0l8ZSbWsF9H0LGGkAMbJf6EctCq6IVoM%2FrBVwDcpjW0HcNhfTicRxc9j3dBiBBb%2F3mdNDFPpFug1YZrQ&X-Amz-Signature=3c845e5b4143a4992420f7feb66a800d99b1a5307bdf267afb6db13d623587bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QD2D4BZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIA%2FkuvyYNDADYNceb5vjfYn7rb2LZERemxcwFCgIfdpwAiA31ZLyhQQwrFISaezhDGIDo1%2B%2BpggBPhLfS9uN1fvwvSr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMsRSsFz1tXUOzEaKtKtwDTJl9yxK7f7h5M%2ByOXxsDI7SUHec8tP6SnnfbZyVb908cxf1hqdLlER8ccaSOIGIzhSJC1DUv2cGd5MDtEvthADgJv%2BliYWNENVdGGTfuEbEkOL%2BApk%2BAeXTLEaoJb9z%2FXcxeu6YE8qE9kMw%2FDLiPh04Hh%2Fzq2LiHTdsdBJWCdwpekYi5fY35yaVwhiebrmblOp%2BWssYvPj%2F2G%2Ft9M6iGOj0KJToTL5xTeekZJ8ZjlHw65HH%2FQND7d6p8O%2Bpw13FxNhFu4d%2FGMw1cSHM1DpwSw0rYqmJUlmhgiZZARLfCvidM6DmoZN%2FFvrFSfMVckhXwzOlLYcFblCVYeCgphd%2Bn3Sco%2F2tEf8OCj1pyE5LKe2nkqjmiC9Uu%2F8QwbWWjV0XZgS1K%2FhvJSn1RHvQXr1QaDd18Qi%2Bh0lWIEK8XnfSsx%2BpQ9ggmMybC1SZJiEti09DHGRE1wQbXdK0SffHhuDWe9pINlgE%2BoW7AH%2BffwEjXqaOnihPRVY5plGnLg1GnLK2VJDdjcBELUyjAb79R9Q12AUJwUMcDs%2BrF6oUfPPLmlhugvr4%2FeL%2BlNNiTBHHJZX3ocIjkeV52%2FIM5GyE7rbB9Uks9D7XB02kMZezfZMxCNlh1oiALjNm9IN6PscYwwrWRvQY6pgHK4dApb5xknBfczX%2FNJOBMhSWmCHCAiqFP39zOwFLOnc1krtQvPoYsidyLcesMMAA9VS7CI0ACvBxLnoWYmEPxi%2BhgWxaC2YGN%2F9lhO9zW6I1s2ru3rigFdjFQp1fTaJRFsIrJRNiwQ8Vu0YynmTMuMGsbqsELqUynW5RgAKFVA556Ufr37S%2Bhq0sepAzQ6QadSyXk95CTMeRw%2B6GMrXPAGjFX%2BgO4&X-Amz-Signature=3d9c39dd6183ef93e2d0eba0e33671e174ac7a8bfac2c2641452615ab3ec1358&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QD2D4BZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIA%2FkuvyYNDADYNceb5vjfYn7rb2LZERemxcwFCgIfdpwAiA31ZLyhQQwrFISaezhDGIDo1%2B%2BpggBPhLfS9uN1fvwvSr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMsRSsFz1tXUOzEaKtKtwDTJl9yxK7f7h5M%2ByOXxsDI7SUHec8tP6SnnfbZyVb908cxf1hqdLlER8ccaSOIGIzhSJC1DUv2cGd5MDtEvthADgJv%2BliYWNENVdGGTfuEbEkOL%2BApk%2BAeXTLEaoJb9z%2FXcxeu6YE8qE9kMw%2FDLiPh04Hh%2Fzq2LiHTdsdBJWCdwpekYi5fY35yaVwhiebrmblOp%2BWssYvPj%2F2G%2Ft9M6iGOj0KJToTL5xTeekZJ8ZjlHw65HH%2FQND7d6p8O%2Bpw13FxNhFu4d%2FGMw1cSHM1DpwSw0rYqmJUlmhgiZZARLfCvidM6DmoZN%2FFvrFSfMVckhXwzOlLYcFblCVYeCgphd%2Bn3Sco%2F2tEf8OCj1pyE5LKe2nkqjmiC9Uu%2F8QwbWWjV0XZgS1K%2FhvJSn1RHvQXr1QaDd18Qi%2Bh0lWIEK8XnfSsx%2BpQ9ggmMybC1SZJiEti09DHGRE1wQbXdK0SffHhuDWe9pINlgE%2BoW7AH%2BffwEjXqaOnihPRVY5plGnLg1GnLK2VJDdjcBELUyjAb79R9Q12AUJwUMcDs%2BrF6oUfPPLmlhugvr4%2FeL%2BlNNiTBHHJZX3ocIjkeV52%2FIM5GyE7rbB9Uks9D7XB02kMZezfZMxCNlh1oiALjNm9IN6PscYwwrWRvQY6pgHK4dApb5xknBfczX%2FNJOBMhSWmCHCAiqFP39zOwFLOnc1krtQvPoYsidyLcesMMAA9VS7CI0ACvBxLnoWYmEPxi%2BhgWxaC2YGN%2F9lhO9zW6I1s2ru3rigFdjFQp1fTaJRFsIrJRNiwQ8Vu0YynmTMuMGsbqsELqUynW5RgAKFVA556Ufr37S%2Bhq0sepAzQ6QadSyXk95CTMeRw%2B6GMrXPAGjFX%2BgO4&X-Amz-Signature=59e107cac8c77d1bfee5ed7f7bd121036a594016ec918ce60cec7305fe1c1e0c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
