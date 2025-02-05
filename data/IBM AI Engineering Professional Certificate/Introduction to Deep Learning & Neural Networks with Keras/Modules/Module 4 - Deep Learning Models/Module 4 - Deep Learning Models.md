

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=6ec7e8894ecea183e3f847482dbd4e96f27e9190b79ccabfee8f58f1b57c042a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=074788c48ef05f26b8378ecd4d6b2aa889330939234be4a24ca746d95582c688&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=ab67b2458e148d1a5c0366a7c789e539afd7f8fa47e7b0d3d02892898796e993&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=c83bb19707adaa30007c3207349d87295fa622c79d0a29362866cdd8e0180a73&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=03fb6e67f072beae85ad99de38db8c76587edba9e93ace4bf526fbdad03bf5f1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=4d1c71de22600d55c106a77d9c6d9a8a3385c51c0a2103e89790ad1b6f9ba58a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=a989173708db977d3ba7a79aa4e5d6abff35a9ac96d21183a40f6c168bd51322&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=b40ec0b624e00fcb0e40d6fbf2780ac9792c35eb68d287b7e58a32a622bbc02c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMTCMEW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD5lCgK%2FmK3DkjZ3TJS3mDBBR0DCvFVhPIc4UZbxm9oggIhANxvGGmhSqj1fUDCEXbXMZpEyDhn%2FbdydA08bIQo7WsFKv8DCEoQABoMNjM3NDIzMTgzODA1Igzpmp7k0IND33BUHLUq3AMuYB%2BQrdWAUCeeCBU0IgyXTJYdx0xHTr4WUtONTLd1bCgQgoe63Z3iJxGQgfNFq%2FIBvzOHG9mwLo%2BM2kNpZugWAOl%2B6peIiJ%2BE0MvsBfziQWUPhWwwxmWxQyo3YWQBm3YFyWhbElPPMx0DLlC%2FBvbv0lGhVTBfyXEy9hOVfufuPTo2mQLsIrQI%2F0eUs1A5ejPrDsjYuiDPs%2FBtdAnIAZXt8nzoRqfu2YWsmDKKA%2B5Ip2k6jtG%2Ffs%2BCdJEs2BfdRXjQKWgEkmNoS71U3AErU0a8zU%2FaIMf3lN693xQBIdfEhnJtm4vOzauMEn4uGMoaJtFZe%2F3gP%2BSq9t%2FmESAY8m7C3APT4Q8QJI%2FqNhDFPKsD3qYYfSrNO1Wmfuo%2FvbHH3%2BWW2Aqx62PK%2BJRr7kXXpiGby09zv59TpvmV9d9%2BX7F%2Fldnx4RKywRFrrkHfxiCD6yYBMZ%2FCp2z05tPIGnTJRbAp3F6oCjdEOcHyLJ5buSvdGVvv0XQ2ocmOwZRCDIGbhR10HMWqO7O8GT%2B4z9zweIyXo0qTRaBWUBkzdRGk2LvieF6VPWB7P6WUaNPysPZkf0pF%2BDpQ6EM13V56gURuoVN6bV5cMxBeNThApqTWywFwa6OPb0ALLuPpbIIukjD%2Buo69BjqkAVmku1k6L4RnRZzrnPvTRs%2BTI89n4ZcVVlU3qtAAS9FRxsbsHyMI29HwE31Nv8Jl9KnHhY%2F8oRfDFPSMaJWU0b6QmSAvIl1Xs%2BCd2K%2BP4%2FVqDjaYEUBuKehZwsDNlSpSzKCxcMXFmzxK4Q4Fa29m10bWkPWj%2BJEpPVggtA4Q04xMwoHWHxemaT%2FVP%2BOfU6Oijc0%2Fhs4XVQaAAfTA0%2BisOza2YR7c&X-Amz-Signature=58018cfefaaa357e610632e2a14e519f702dac291676501b1335f90b45c9a01c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VBP7LTZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDWc4Z26LbGrxljK6Bw1iTCM5vFgdVPXNXWRKJUxjEapAIhAOtsok9mlJya6TC0uzoWiReoX6pt2x7R7%2Bsrzt3PnvASKv8DCEoQABoMNjM3NDIzMTgzODA1Igxf%2FgZCSwmdDfsLSMcq3AMq2jhNKFUHiazwo3SoynXXM%2BM4HjqnTVm4bDsCcqHf60dvfkp12iMkm%2BgHbU59bDhECN1xrNTXGfWW7j0UI%2FM%2F%2FPBmhkURrwisSBlbnn35RBvBoqevg0HKd%2BYkEpAAwIelzy5ulBvdp8ABPid6CWERknuSWBqRbSbA%2F00R6otxqKqynzHgalonBduG6fBWlsoVGhBFydVx5t1gVbMNMNYuGBeSSceNBc3vuW02zxMS7Q1W26bts7kvFLQskrW1j1TQBVbZ4Io9osGa2lxz17v7sdgLxtyy3GURDyls7yqkjvPJdy%2FK60RFJ9Sz69Gr3dLszuTmvgVqp0Tfd4l3uC4soIqcA0TXapTCS0EqW3Vmin5lSix827psi9AnnW6ENUW2En74htbunRahl9BElsRWZZnNBHfrQ0NM2ndvT3%2FLSa7UnCzFD%2BqHsPFVfvA04LYjOXW86o4VVhCn8Exiaj4L5ZDsmKCBboHylzH0CrNyRkFRgMzuDMyBefPyc6npgQIUWPZqEdkvZSwuRymgGCE%2BpflTH%2FzSLr%2Bnb9RhhizWzXQTsMlru22NKOz4WTwZqhKJ5TKPNe6REzpzEUFXYezjZDVin8nEVhUSLp5zIoB8aqcyky4VUtnfx6yUwzDduo69BjqkAUi%2BbzziHTmHgtpeEdfpBJMTbFKaMcRJ9z5LhAuhG1gtli75bcSbCP8%2F79LAjEC4%2BBXHJW7wj7Y9ecOaAnJ23FBTuBUaL6Lh0jnJ2nUjkj%2FPnYYOqrwUurIV1PTaOM2b7uoJs%2FEwF%2B40870e5fEgrhkAessepMS51hbJgAEBQjlPMxrpHGo%2FhCyS2RL9724uBf848KmObyOJX%2FrPw3bzw9jtbnGt&X-Amz-Signature=5f1e8cc4566247aa41b1ad3b0cfbe758174b06102ee399d362b17c53b20e2643&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VBP7LTZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDWc4Z26LbGrxljK6Bw1iTCM5vFgdVPXNXWRKJUxjEapAIhAOtsok9mlJya6TC0uzoWiReoX6pt2x7R7%2Bsrzt3PnvASKv8DCEoQABoMNjM3NDIzMTgzODA1Igxf%2FgZCSwmdDfsLSMcq3AMq2jhNKFUHiazwo3SoynXXM%2BM4HjqnTVm4bDsCcqHf60dvfkp12iMkm%2BgHbU59bDhECN1xrNTXGfWW7j0UI%2FM%2F%2FPBmhkURrwisSBlbnn35RBvBoqevg0HKd%2BYkEpAAwIelzy5ulBvdp8ABPid6CWERknuSWBqRbSbA%2F00R6otxqKqynzHgalonBduG6fBWlsoVGhBFydVx5t1gVbMNMNYuGBeSSceNBc3vuW02zxMS7Q1W26bts7kvFLQskrW1j1TQBVbZ4Io9osGa2lxz17v7sdgLxtyy3GURDyls7yqkjvPJdy%2FK60RFJ9Sz69Gr3dLszuTmvgVqp0Tfd4l3uC4soIqcA0TXapTCS0EqW3Vmin5lSix827psi9AnnW6ENUW2En74htbunRahl9BElsRWZZnNBHfrQ0NM2ndvT3%2FLSa7UnCzFD%2BqHsPFVfvA04LYjOXW86o4VVhCn8Exiaj4L5ZDsmKCBboHylzH0CrNyRkFRgMzuDMyBefPyc6npgQIUWPZqEdkvZSwuRymgGCE%2BpflTH%2FzSLr%2Bnb9RhhizWzXQTsMlru22NKOz4WTwZqhKJ5TKPNe6REzpzEUFXYezjZDVin8nEVhUSLp5zIoB8aqcyky4VUtnfx6yUwzDduo69BjqkAUi%2BbzziHTmHgtpeEdfpBJMTbFKaMcRJ9z5LhAuhG1gtli75bcSbCP8%2F79LAjEC4%2BBXHJW7wj7Y9ecOaAnJ23FBTuBUaL6Lh0jnJ2nUjkj%2FPnYYOqrwUurIV1PTaOM2b7uoJs%2FEwF%2B40870e5fEgrhkAessepMS51hbJgAEBQjlPMxrpHGo%2FhCyS2RL9724uBf848KmObyOJX%2FrPw3bzw9jtbnGt&X-Amz-Signature=c26e70b6f4b38c8d7d2ed7c417fe2142ed7c4aee925d5578ecc59a5ddc509d28&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
