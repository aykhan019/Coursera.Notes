

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=e45d6023ae5815b20e29df94092675e22d4c37c06ef429af78ce88af7cf34053&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=b56caced4d646c2082345faea1c57eaa30b021dfcbb17d9118948a5edbec503f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=4b9d7aa32cf890050e63fd67d92c2cf3353bcd2a391f5ed87c93cd569894e3e0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=ddc9640b88561184179ce79ab305c6515b293ba25a5e7c69591c59dcd7a96b11&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=9bea9857917a85a5a0e070dfbc2fc117c22742946130215d18c64f1167ca591c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=4289114977b8fa5242b406d9b816d3317ce12381fb3b4c00df2c2e7c1342491c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=6cd50a8b8efbb8a8bbd41bb5ec1d1841c5c0f6c02c180aee69c775a2681817ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=5fd78f25635b5cb2b82e57ee5fc80d11936ce941f45ed19435d60333c96aebab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFISVJKP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDL2o0m10pGYIr4LBBg1qT%2Bpui7pvE3EWfWB4g%2FrKJM9gIgYIiRn5u5ilEviJNWaaneUix%2FkrFn%2BK9EAqlUvTfG%2B68q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDFnf0ySLQpWF26bXXircAwr8iKuNi9TB8vDVBIiUhtpKKv0ClksEWR9C8HsRe5jtF1O8a7vIwYVofKy4otBz9j6xEX64oEI92byL5iaOfG0I1S7i4tiqdjk3tj02%2BO67A46qdJ3cxALiMPWDwHN7qAdB7YByXSm4wvsbUW8T1wMvmVDW7efT9Q2podYaTigGQZcqJZPUU1knTXl2S389hM4UBLxSUO9ubssEmaLilu7MuWeJpReUNFasuuJQ%2BhPNsTK2W5%2BjhENR4KhbRNYG20GSd6%2BH04GblK9eyzB22yBA6LWtpebh0%2BbiEG5UukF7DZ8M1lnTqviWJYmPFPEAmPEI659CyObDIM4r0rC%2FYUOQtMGnUKkgr%2FGF8I5vRXiNlKkyjg38CIVAFm4Y7cc25esK1vlqsZ30x%2FirCyV1%2BrZShZgO7zpMWLc2YZmYHYU5ShuKHy00Pp%2Fddkj6tyjTZ9T6RvQAfN5FSg0xaHugcR53RPhBwBAh3z2SChj8V0pzczUNcedSBXoyOgk25o2YyQs%2BeOz7Txfz9rruHeNH6zBsJyGG3x0Yzflv90Uzebn5%2FFoGOmI%2F78H2tyY9HiXBE9w9aP0lVuMfhkBKcUwlnrt51vhDH3Cr42Kw%2FsmLyjm%2FdjLXKY%2FDXDDzROGTMJDEmL0GOqUBkAsHEALgXiG2OyyXVGVEju6iVHM%2F%2FQ8ELo%2BT3BC6jUm8i5pUrtmVTnIfOxq0q2vO8Tn0dLYA8sIO1HMSBcdXx4VfG5t9kjQhrqL97ssl5WHT5qhHIPC7VIiJ0kQgpZMal0nCPG7nsOtBok5xrQptaIvlkUN1%2B%2FIulxDnPnk82v%2F3oUzCrCyeZ4M0%2FWQk6pwrBohjtNIMqAmt%2FPDw5q7g6sY0bnfz&X-Amz-Signature=41cca0aeaf5d45d5f54bb70afd070936d612610be642f0416e31eafddedb8219&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RP4GTY2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGf82dSEpniZwgxr3UAFB57F9Tv2du%2BPHoEnAGhNNANAAiBlJFzeC%2BPbKpUeuloX8hi3uDJ6GH5Nl0EgShlbz1vo5yr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIM8o4dDYsvCW7vfjD4KtwD%2B73O%2BVWhi%2BM8wz%2B64k4yH35svdebj6%2FoeFMojoqKavXIH41E8W2HYci9G4xkcf1qOI%2FXq%2FtbBd8PkVOGwJc1HiMinS34B8IXmxZrRTfLpjMkVNcq3QkfbQjB2%2BUGyZhGWyeRX9Iq2QJ%2FOsJWw%2Bu3WprmCs6U7kiaXErc1jaPLsZie92%2BIkfhKih8i%2BX80A5ngvqvZZ67oAg5Tcr6UHyveDnBJGqfas%2B4jApPohwuXnQtCct6uXd09tabWuqjnXmywi818PqpkMpPfrfNGuiWPMfmjB36tI%2B8pqOwDxyTLdAnpRwxWirloc1Ly7e3JXSbIO1jUH9HHlYtx2y4P4qvLT7OLBVrX7OabPFZseOu56kJDrdefYXYSC6fy6FW6%2FG7LfpRivuUCN6FKwVTtUB0LDeJ5fFA1wm5psKD%2FbUnbyvsgI2JvsqyETm4Nc7ssc3gs0QsEJDTkCGwPlsTkdOeWdemZy7M8dAVeddtiv7MO1J4%2FptUAFwr1wCtODzZ%2BXInwlxPOa1W4gH2R9NuvYUDmLAz9Ert4j8yOiOH74aJrWPj8VOrp1BHgS2fuL2K8Z3RncDryryoaZLMkylJ98xt%2FiY5khU0%2FA5JxgA9UzMVvxQzkrzj%2BSkBWDPcGREwn8SYvQY6pgGAOzAqbWMWfbMIjcjs32oMsvtpbvv1hMVP%2BchAsfQlFcwn67EcZzJi7ViAzSHg1rwi1QWPVVCkcJm1cXV7EE9%2F2Q83Ua3oeHbvv%2FWsuk7WeAUo0CLob5gE4CDxtQhJrwgxDTL4TQTEK3%2BmIwvV6CCyVLQaoCUJ88c73sz9mlKnRI9CQlzKA7EYEpA%2FLDxRZXdBMUG0V%2BRM%2BdGByTYIFg56YTxWcJ05&X-Amz-Signature=d9aec166c8d5037449c9880338746831a0c3cabdf6a3e280fab79f77d5379c62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RP4GTY2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIGf82dSEpniZwgxr3UAFB57F9Tv2du%2BPHoEnAGhNNANAAiBlJFzeC%2BPbKpUeuloX8hi3uDJ6GH5Nl0EgShlbz1vo5yr%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIM8o4dDYsvCW7vfjD4KtwD%2B73O%2BVWhi%2BM8wz%2B64k4yH35svdebj6%2FoeFMojoqKavXIH41E8W2HYci9G4xkcf1qOI%2FXq%2FtbBd8PkVOGwJc1HiMinS34B8IXmxZrRTfLpjMkVNcq3QkfbQjB2%2BUGyZhGWyeRX9Iq2QJ%2FOsJWw%2Bu3WprmCs6U7kiaXErc1jaPLsZie92%2BIkfhKih8i%2BX80A5ngvqvZZ67oAg5Tcr6UHyveDnBJGqfas%2B4jApPohwuXnQtCct6uXd09tabWuqjnXmywi818PqpkMpPfrfNGuiWPMfmjB36tI%2B8pqOwDxyTLdAnpRwxWirloc1Ly7e3JXSbIO1jUH9HHlYtx2y4P4qvLT7OLBVrX7OabPFZseOu56kJDrdefYXYSC6fy6FW6%2FG7LfpRivuUCN6FKwVTtUB0LDeJ5fFA1wm5psKD%2FbUnbyvsgI2JvsqyETm4Nc7ssc3gs0QsEJDTkCGwPlsTkdOeWdemZy7M8dAVeddtiv7MO1J4%2FptUAFwr1wCtODzZ%2BXInwlxPOa1W4gH2R9NuvYUDmLAz9Ert4j8yOiOH74aJrWPj8VOrp1BHgS2fuL2K8Z3RncDryryoaZLMkylJ98xt%2FiY5khU0%2FA5JxgA9UzMVvxQzkrzj%2BSkBWDPcGREwn8SYvQY6pgGAOzAqbWMWfbMIjcjs32oMsvtpbvv1hMVP%2BchAsfQlFcwn67EcZzJi7ViAzSHg1rwi1QWPVVCkcJm1cXV7EE9%2F2Q83Ua3oeHbvv%2FWsuk7WeAUo0CLob5gE4CDxtQhJrwgxDTL4TQTEK3%2BmIwvV6CCyVLQaoCUJ88c73sz9mlKnRI9CQlzKA7EYEpA%2FLDxRZXdBMUG0V%2BRM%2BdGByTYIFg56YTxWcJ05&X-Amz-Signature=c527c25ec7659f52508ba718911d2302011689db3afb50fcd202245aac7d6dee&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
