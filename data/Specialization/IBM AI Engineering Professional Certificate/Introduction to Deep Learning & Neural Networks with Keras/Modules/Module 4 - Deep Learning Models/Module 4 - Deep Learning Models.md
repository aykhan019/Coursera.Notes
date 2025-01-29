

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=020dbea66fee97f645b124d1e783732ceb7879f40ea657991a97fa4527bac6cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=3a05d8e494908c987fdfbf1f035b338fc4834a3a1a726f29ff1fa4d0fe1e711c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=0490fc8919228c8f538ccafd7a57945a0ffd8d6bf8939e22db54a1ea36948d74&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=87797d5dd92c2212bc9d00d47a813707a505aa8facfd97354f049c6e3331828c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=6cb4ffd2a4e9911b6642aab07d858230cde3a9633d61f88b07721d985abff8b6&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=48acd4cc649458d334615dbfebc02b043142ffb72a3467daef48aa364f260553&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=6c0406f38f831791b71187457c1f94c2df702c2fa38951f31a167e54c02d26c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=fc3a30ddfc42bf21586c9e2f4753bd575e84b6f131af8c725bd8147b30e90168&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REUCLQZ4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1hhvRi0WtyHjBSOFpsbQRzQcMKJ6PCuF8xoQUUNDc1gIgdAK%2BTlV4b143saSz0xYYnZyBSmiKY7p2jdRqQ0zfI9AqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMsTHeZ9Ok63v5tKircAxpMcC7BqqMMKObEZLUVb%2BUfzxCqRMMy%2FNwH8ZaZ%2BVNoMZkrdYtJLMzaBnc0D0x5AOuq0GOkfgEHwGQTTv0kmSm2nCONW5%2FI3XcpZEAVS26hJJ6ywS9P%2FFl%2BxNz2dTnsneFUYFg0DBkOf8L0xCW62ITrw3oLwfeDL4Fo5ucuoroilk1Jc1svErlZ%2FFDBCvMWtaE9lP%2B0fEU0ppr7GehKjuss6F7OanHadcU2trtKICrnDc1Nb4N7x0QF1xQwE9z3WGKLWew0%2Fl%2FJG%2FKkSOspA97yMG1BrLAipwKS4KLq6%2B0q9eKUVfejblRNGl3dV1BeawZAl62xp47CzEx22hPxI%2B%2B0RbuAeHpV2QA5%2Bz4GqpqRz0otSXbA%2FcQgYfSgNOU5S4LKHMOzwAjXaIembzRos0twk%2F3SID7igvitpU88Ft6poUE%2BTzgsRv56lqHshLWH%2BuJ1TILBniYaUD%2F14Z4Jjl8QcyLLfZ%2FvNrnqSzCNCGFcwxGKiatSHA3R38nwbcZG8Vv%2BammDQYZ8yx7rCzuCbmPm0fW2nGoJhPqS6lFDkGSPTQtI60besTxtqCyZ1Ki6NGfLnfOn%2BgtnXM15JhgB4HQwxx9LGZbTxSqHCWQgcYmKCS7VYLUF33MqURvnMM%2FL6LwGOqUBtrs0PLxjfRZtLJSx6I9j78thEHG%2FQR%2F25yim%2Ba4mA%2FdMWOuKDLoUEcudOh0ov10CF6kWcZ2QRJ8mvp%2B%2BbE1IVFa2ICdSXhRwerYCV63bL%2BsESINQPEdTYVMIlheVfyuFwh2jpMTp3uy%2BHgRXixxK4%2BCPENHqNZGG9VBytjcwiJQ%2BDA9NgRExH%2B%2FGlsO6Bm9557rpd3xu8kY%2Bt6t8mKYR%2Fhe%2BfrTp&X-Amz-Signature=2f0c8a8435eb128fbff836a5ad865f62fd5ec0083ce4934cb076f5b53722e5f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673OPMT6P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAa23mRWZMm2BU7zpK1lG3yvi6Z%2Fln4j6i6Wp3VtV58xAiEA8r0HOHr%2FqTDY8y9XXMlkvH2Abr1%2BpBfC%2FUMdaRnY5EsqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BcUPqM7ubrqcI4DSrcA3BGRqGJc0gn5tLqcha0I8b2V1%2F3yWUoxNl6G1%2B8zM9UkMdYaeayYJepOKQrSv4zFrnn5pTReRVu1pHQEnVXS4GAuQWsjQPYTYuTlA35rxrHqtsY7%2FTrEB7MM8PEozIOs6WFUOJ4%2BXmzvLb3Z7%2FAgRBllBcgevpuq7H9tBOY2aBZlZVKb1Y8URNn3rjodMvbdKpFZaFDO2XwRqAGVWXArvLL0AIrKjoS9QEpP6r%2B7SToQn9IIn3APwZIG026%2BHfSVwKulULXDCQ1UudAsdbHimpFdTm5AWtD6BrBWpaCsvrW8RxMTpzNtJGUFUIlu%2B7mYRVgK7o2N3Hps9mGeqPVzp%2BWJXzMU9aGcP5ZaPyd5rbDmEdA0b7AAXh1AxT%2FTAoCDmUj4VQh7xG%2Bd9jQhNVs8siOD8mT%2FCjOs6OlD7tOjR%2BFrnO2wVpsPk0X03PyJ3KVUP%2BagWWIh5tlROJMYp5mAGzOupDFud5hJh%2FSZtD3RoJWCjV01MPhDzOTwzC00u2fzwhjQIMMpwdnJiFGdpsTHvskn%2Bbroi%2FzGDVuctagdifMpuF2gugJ8l%2BxKpcDCogpYkYFbV0mCxWCFFGYRoqn2O2qIUrxfCxKk8GpAVS4nZyjdHg1%2F04FPvrbB%2FwvMIfN6LwGOqUB7qFyHqUI4ZoOBBv%2Fz39y90d8lVRpvKDiV04M2WHoyUpfpfl1cLfsjHvooGKwmbMmzaefP1Y2wpLbOT%2BoEw3DzanCd72QDeOKu5cCEWk%2BUkgLj99zR7%2BFFPpkq101kgSvUFDBMzCdpHse3CONQL9yU2u1AshhwUcwRlLDbqSBp50JR3z9fx5Azw6po3Ay9Hyg7WcSbwr7Szkm8Natw6fTfOHkR3L0&X-Amz-Signature=90978f601341747c4b9c0fb828e08eb1d412ca054a2f4c65f68a7981a26d29ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673OPMT6P%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAa23mRWZMm2BU7zpK1lG3yvi6Z%2Fln4j6i6Wp3VtV58xAiEA8r0HOHr%2FqTDY8y9XXMlkvH2Abr1%2BpBfC%2FUMdaRnY5EsqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BcUPqM7ubrqcI4DSrcA3BGRqGJc0gn5tLqcha0I8b2V1%2F3yWUoxNl6G1%2B8zM9UkMdYaeayYJepOKQrSv4zFrnn5pTReRVu1pHQEnVXS4GAuQWsjQPYTYuTlA35rxrHqtsY7%2FTrEB7MM8PEozIOs6WFUOJ4%2BXmzvLb3Z7%2FAgRBllBcgevpuq7H9tBOY2aBZlZVKb1Y8URNn3rjodMvbdKpFZaFDO2XwRqAGVWXArvLL0AIrKjoS9QEpP6r%2B7SToQn9IIn3APwZIG026%2BHfSVwKulULXDCQ1UudAsdbHimpFdTm5AWtD6BrBWpaCsvrW8RxMTpzNtJGUFUIlu%2B7mYRVgK7o2N3Hps9mGeqPVzp%2BWJXzMU9aGcP5ZaPyd5rbDmEdA0b7AAXh1AxT%2FTAoCDmUj4VQh7xG%2Bd9jQhNVs8siOD8mT%2FCjOs6OlD7tOjR%2BFrnO2wVpsPk0X03PyJ3KVUP%2BagWWIh5tlROJMYp5mAGzOupDFud5hJh%2FSZtD3RoJWCjV01MPhDzOTwzC00u2fzwhjQIMMpwdnJiFGdpsTHvskn%2Bbroi%2FzGDVuctagdifMpuF2gugJ8l%2BxKpcDCogpYkYFbV0mCxWCFFGYRoqn2O2qIUrxfCxKk8GpAVS4nZyjdHg1%2F04FPvrbB%2FwvMIfN6LwGOqUB7qFyHqUI4ZoOBBv%2Fz39y90d8lVRpvKDiV04M2WHoyUpfpfl1cLfsjHvooGKwmbMmzaefP1Y2wpLbOT%2BoEw3DzanCd72QDeOKu5cCEWk%2BUkgLj99zR7%2BFFPpkq101kgSvUFDBMzCdpHse3CONQL9yU2u1AshhwUcwRlLDbqSBp50JR3z9fx5Azw6po3Ay9Hyg7WcSbwr7Szkm8Natw6fTfOHkR3L0&X-Amz-Signature=c9cc39d32643323f66dcfdfa621fc14e9c781de58c06b58f2b1b92eb8b7d6aa3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
