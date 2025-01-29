

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=1fd0bd3a866a4fb26080e25fe07e37e949061452bc219528f99f970229d990b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=eb587fc977f17af69e1efef069827696a53d1b9ce113ca995d5519e3996fdbff&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=56347f03adf2c8918fad55a6e31e5d6d29167cf72e753c6bd3cba3f3722fab84&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=0b8357b6577e14d0db870e768292b7e4a8e486415535c442f7ecf6226b913585&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=b100ea86b1e19b682cba0894babd12937140d158e89ad9757290208c3b6aba22&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=1dccf9a6791d0e30f9ebbf6cbebdfea486df9b645ea6d35ce85eb5b8da5a455e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=367daeaaa3fbc3cbf57a8ddeb08fda19f7bc66ee295774f030f2b65a013b445d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=b5121c84e4aec6f392d03a879e5b530ba62cc9ab1ea7ae74da293483a976c025&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466427D7UA4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBy%2FpDMti1r3JmFRt2W2mHytkyRBU8oRJhWrV5q6mP1CAiEA1YKMoxzxKD6nQMsT%2Fg9pfkQXldn6RQnZG%2Bj%2FembF8w8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSNkiyQYDHuSQ9qDSrcA40M%2FIQR%2B4oNPCDNCtuJa1lZEhrL0V%2FtxBSJGkGquBx8%2FWZ51ni26pj%2F2r%2FQ872AThpJrJAb6U%2B4Bs%2F%2FMQDBICsSZNOCeAeJWSX9NSidr8mszlMji0r3LaRD%2FO842PaVq%2Bx510X2ugkA2%2BPliv2Vey4G1Tg4t0S%2BWEPKEpgfZOM0o2%2FxwK806WNr2HL82%2Boq9qKU961t1%2FEHc3mGR9ujmDXbWLYf9ODfughj5lW%2BODFgrd86C26Z2%2Bu1glGRn3ZH9FVgkYGkyJMvLu0QISyWw5nyyqrkAwmRqzRbuJ%2B5ilP67fqAaoYJXI2K37saWRB3OgQBHRV%2FOirZAo%2BOzgtxmy8u4PFcVdOIF%2B%2FdGJJ9%2F3Zn9%2FLxOLAv6I6AxHPCfbs9DMN0PJbf%2BtPpuxzSCG9xAJ2tTd%2F%2FyiL7G8l%2BpqKmN9vitPV%2Bws%2B%2FTrCDkIbjSIjjkHShYytUGS4Kd1ZhS4MSCZLen1V%2BnFqVsdLyNn%2FTq9mtltlBgLkwEV6fhVhoXAYG0x7xe6b50mgwKI%2BvjMinyoYuUPGUBDS%2B3tom0imVHx1m65M2GuZGN3ZPdOSwyWYKp8QsaWPQvrnHUPOE2PogFfUNF%2BjehrVmFxOpCrlUe9dNNvEjjDzlyvx99IaNMLWQ57wGOqUBVfbVMSyZvlLHpv5bgSKkuGU5DxhZJUx9ELcaPA6mnSnjX0Cj%2FSoJ36pwUbUPYd4aCBwOA8a5luy%2BUOMGHK8ideHTlOaUUmYCLJyovEVzYgrAhi9ZdQVOLhsdbGTCPSp7DpsnuXTVgGzj%2FmOPkwg0j70x5aCrgavhM3ntlGUhOzsPjLkZE0%2FGHsyYUgJctG8fZtO0Fp53ERiehcXZ%2FbShj5dWfNMV&X-Amz-Signature=9ca6fae00f6d574933da658f20bff491a6df9a00f29800f190f641d70753818d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ET2JBGB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBxaeUQHsFo1%2Bio%2FWGNoBqMvy%2B8Z%2FKMgyhGZ81tc36jyAiEAp9ZtRrzjD2YJihqfhdUguzLZ2vZZLyV90v25SbzxvzgqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOpYKUil7nchWlT4oCrcA%2B3wvdP%2FyjO%2Bq%2FZaRFETW2KUR27nOVyvFISfg3BRdeYK5QjeSyEzubhx9xcyv4SdcouUCBXgUieG6zkdlnEDohnCQnqY9LDNFhTiGh38tdOMUloTsqybr9AKoUlQGVDt3lln3mk%2FozBWOQ4JxGmHdeyKfR7ab8o6UADDFBna4YFmh8PPyS9zIxdfxeDYlN11fXrhT%2F%2BzgFbOtGBP8M8QvO76nYxp%2FlfmhnScq2Asl6Rs6RdfiED813oHUyHJ4ZckaOQNfzzJQpCYriaHcYCT57Rh8ZYBH%2BatVJXbVYPEjn9%2Fm86hyz%2BPYNTGBeyOAS%2B7iv2FAmKfNHyW6FP5dw4zUul3YgZ5tSFXvSScsmSfItLGu3g9wxgHmStIIvjaRkA57AHhnqGw%2B5yLG33LJaeyHZtpWOEshP6pazlsDhynoszMmnBxEfPptyPPjCVNwi2kkVDDqwS0NmNloRUSml8b50BB0DdtSP1VqRsCXR9Hp%2FmrAxoY3PrMmGQLQR3YR%2BMYNQH8X%2FNAMMISbFq%2B%2Brnaqzu3PmtR8EvCCgxnvISRd6OvEc3xjVbE3BnAsLGYl8hP5IZYdZ3z7gj2b2M8x%2FTChS2PE39ZABA9CPf6qm2sVq%2Fri8ouoMqDDvgvUswrMMeQ57wGOqUBwU%2B0EIVZIa7PDq%2FZg7IRK0BSiVOdC%2BAUNNcEMTa09btQgG7rchb13po5ydt%2Fmb9nnqqwe3E5P%2Fg6AGREeKsYVsRsegJ0VAIgKBTUWL5FPAvzEBCSvKCTI6jGGyWd%2FlVP%2Fw5Fl998vHTkGiby7845Bu3rC8AT0cpmdDuKrdFQdl0L0PycgLwYjPx%2FVc0fMNh0%2Fay%2FwCWfAShJhOk1ZUK34uoTqDLU&X-Amz-Signature=c25d179cd7846e8f6decd367d058dd17f5795c5d8e6f2e4a97df3428609bd52f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ET2JBGB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIBxaeUQHsFo1%2Bio%2FWGNoBqMvy%2B8Z%2FKMgyhGZ81tc36jyAiEAp9ZtRrzjD2YJihqfhdUguzLZ2vZZLyV90v25SbzxvzgqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOpYKUil7nchWlT4oCrcA%2B3wvdP%2FyjO%2Bq%2FZaRFETW2KUR27nOVyvFISfg3BRdeYK5QjeSyEzubhx9xcyv4SdcouUCBXgUieG6zkdlnEDohnCQnqY9LDNFhTiGh38tdOMUloTsqybr9AKoUlQGVDt3lln3mk%2FozBWOQ4JxGmHdeyKfR7ab8o6UADDFBna4YFmh8PPyS9zIxdfxeDYlN11fXrhT%2F%2BzgFbOtGBP8M8QvO76nYxp%2FlfmhnScq2Asl6Rs6RdfiED813oHUyHJ4ZckaOQNfzzJQpCYriaHcYCT57Rh8ZYBH%2BatVJXbVYPEjn9%2Fm86hyz%2BPYNTGBeyOAS%2B7iv2FAmKfNHyW6FP5dw4zUul3YgZ5tSFXvSScsmSfItLGu3g9wxgHmStIIvjaRkA57AHhnqGw%2B5yLG33LJaeyHZtpWOEshP6pazlsDhynoszMmnBxEfPptyPPjCVNwi2kkVDDqwS0NmNloRUSml8b50BB0DdtSP1VqRsCXR9Hp%2FmrAxoY3PrMmGQLQR3YR%2BMYNQH8X%2FNAMMISbFq%2B%2Brnaqzu3PmtR8EvCCgxnvISRd6OvEc3xjVbE3BnAsLGYl8hP5IZYdZ3z7gj2b2M8x%2FTChS2PE39ZABA9CPf6qm2sVq%2Fri8ouoMqDDvgvUswrMMeQ57wGOqUBwU%2B0EIVZIa7PDq%2FZg7IRK0BSiVOdC%2BAUNNcEMTa09btQgG7rchb13po5ydt%2Fmb9nnqqwe3E5P%2Fg6AGREeKsYVsRsegJ0VAIgKBTUWL5FPAvzEBCSvKCTI6jGGyWd%2FlVP%2Fw5Fl998vHTkGiby7845Bu3rC8AT0cpmdDuKrdFQdl0L0PycgLwYjPx%2FVc0fMNh0%2Fay%2FwCWfAShJhOk1ZUK34uoTqDLU&X-Amz-Signature=369ef480c90950c8935edb7a3d441e2cc77de7c366a337bb8305f7fce94bd2b7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
