

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=6b971c861e56ec80a49ac74d7b913ecf07e8d765219b3053db57c21992236a78&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=604c75e10d6c2cae7e576b4f8e832c37438eff7a74a431f6cbc219018cfd1aa6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=02c2d2dc6fcc2acd6ecb7a0a3e9d112d3f4d8a912f613bb7d2eacc91b8b0e024&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=c1b5c6d0f45c36951e857abc763e42245bdca8fc3f0b512d6868b7ca34701e54&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=d3e49c679189c9f2dfdd94c4c381b70f3158e50cd2c6b4ce8f4e54738d8d3bb9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=c99bfd8374c9407403db9e6fe1e044289c5202787f4a3395e12ea2d67ae0579c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=669004222600a83c7ccdb8b7c4fca45d368733d883b027a81ae577cc8d5f77c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=5c156cece976418788361feddb00ca866f9aa8089c82fca347b0ddaacbd32466&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVATX7G%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjlw8HvdQmrIIX%2FfF02LwgJrkYs5CspcLnoVusIBPXvgIgN%2FdXQUcQBWhZKVnt4nvUhkW2oHHrj7DNXoWxJZQdIR4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCy6Ih7jj53409HjTyrcA%2ByYbz48enHny6fOCaX98aH9%2FOhMgh2QcYh5n%2FRIgNNOvnmmZbHrCsemymTlPAvOAlOes7p1bsjN7RMtVB%2BY43yfpLJrPuojIU5KRudyoZRU255TT4cr6Cjdxi6Bx7udlHf2gct8cXzaqUOV0vuSPCbhtGCqZjW%2FE0nD0rSoIW8dDh6Twkbt0yFPR1tHf56500HrE08C4BYgg3D18b47VLZtcrJjIgZrpX61Q2nxTcJ3DEhi6nvNsOFnnU6oiWsGeAQ7YmVaXpmOuEjJriUsAHobLFkCFGNiwtu4VuD2EVt4JPJ87J0WKrRHgorsIcFWaqYu8o3kCnJntQoVofcSWyCUUwcDxYOhpRkKcsz3QikAb%2FCRSGgAgh7DDR0rHm89t4de3%2FQCfn72ufP3gnhuXDams%2BZr1EN6J5w7vJScGXQzV0r%2BzAVewDxlApGHSz2v2JEgPuFNi7NTUWTXjk8SaYohSGHU%2FgOGXUYCsDuj%2BVwdbyFGgyu8eYPbkMAn76Zpir6lHLVK2Me%2BSPKcZNbSrQxviyrX0y01yJmT8sxG%2FL3yxUzuguu96fm%2B%2FsfzJr%2BGnJ0Ua9T%2BaxKLLomU47ERmmsEDKCksWOJ1rivKReiCJ71MIeervQdNJUM%2FaFzMLa%2FgL0GOqUBt1c9kZB%2BzN%2BjuZCnThJPGpPm5pGEjpRuN69HlPa%2FlOxla9VTgLNjMsp%2Bi77bLyr%2FFG%2Bb05xo%2FQ7pHcpTRPmJ3Wc17YbiUu9dHV1PXr8L3gYcnvDsi1V0%2FAqmBe0BlCf%2FZncTbuwt%2FDONBtEcqWEDdNV2dkoyWXA5uvcNj2b%2BctiMUCdXfMxDgYY709A7uM4Av1JR7SaWQmlCzxqjWWCtjBZfeVzl&X-Amz-Signature=ac0811b7749734ca00255430c6424c59bed27e8c99bf0710c8f4de3ef034e888&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4OIZ67%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGuZYmYTw5YfVPWLSz6Fz5HuDYiOy6e2Vqgh%2FCNEe%2FILAiEA1rG5qjFu7Ew2PNkkeXvjv5%2BpY6Q%2BuzNs6xne4XPCggQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqRAlDN6wbkG5%2FJZCrcA47j6ikM9ubvM5QSZfw68BAmQqtyU2%2FeTP82sLglN8PSiNb4f3g5wFO%2B9KQkv9HbBQ%2BBMJUchzLWXIKwVBypcIhQyp8yyLOz4tgOonuso715AvRJn09KjDFYetn663jboNNGVJsta7u3aJId0Gqy3eitkjGOKv2qbxVCvGDYMOAL113J2ers%2BHE8xY2NqvDcJr1q2NWdxMk8iJ%2B6OUz45%2B2nFuCN6%2FEE69zpJmDVVOyEHSp3KPRyJGK%2FfFTZp%2B9BQp5Qeuj8KrsUz2xQwTv6jNwORtUC7QiHMp8a2ZyfxnrUI%2B27%2FxZrnlMM6pzcDUHv%2B%2Fu%2BA%2BE9q8WSt1747vrkxUMU8opGIOVsj8lAL8mWKJW2pzDqObn92J1%2BY47sqiWWf47dIEFyWXIxGja0gSkUFTZwDolX1YLWtB6Wa07seMquDHJTzR6Sc0dCM3ty%2BrJwRwNwN6ZNtpM0FqHfii8cLELkVakWtw6CGh75d01U3EwJgO6D2KZe9BfUq6eO0IzTM3JV7eRGBVz2PaqJq7bhlWiwosh9qLqkjtt5IrnbL1MIteVPzy4wyWWbQqqGsdRnY1rDl6Js5vf5bYIAmEmeMZC%2B803gCbSaHVyJrs%2BW53qUMFox7axuUiai97HkMJzAgL0GOqUBHWZ81JnplzMuNZkbFuxDtP4RNADwnpGms80wrgwLor7LSc0pdi4H2ctnAsQxSiDb6ZUQxzcvQa1qIm4no6WCWblf%2B1ZJ%2FOTORyaHjAlcgzUfbjLgphY48PEeTgkSi8Je9hSoaRfBFCbRJggzSs7QGGnkHod5lkNSJW9mTyXn0DuU3AuQZK%2B7M4cmu7DB%2Bi0nBKL%2FJhQetnF%2F3sNHVHeBZYP0t77E&X-Amz-Signature=eda7eed790dc8be55e1fca049a07dacec05f27471f54be714e82b49c86b6246a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4OIZ67%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGuZYmYTw5YfVPWLSz6Fz5HuDYiOy6e2Vqgh%2FCNEe%2FILAiEA1rG5qjFu7Ew2PNkkeXvjv5%2BpY6Q%2BuzNs6xne4XPCggQqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqRAlDN6wbkG5%2FJZCrcA47j6ikM9ubvM5QSZfw68BAmQqtyU2%2FeTP82sLglN8PSiNb4f3g5wFO%2B9KQkv9HbBQ%2BBMJUchzLWXIKwVBypcIhQyp8yyLOz4tgOonuso715AvRJn09KjDFYetn663jboNNGVJsta7u3aJId0Gqy3eitkjGOKv2qbxVCvGDYMOAL113J2ers%2BHE8xY2NqvDcJr1q2NWdxMk8iJ%2B6OUz45%2B2nFuCN6%2FEE69zpJmDVVOyEHSp3KPRyJGK%2FfFTZp%2B9BQp5Qeuj8KrsUz2xQwTv6jNwORtUC7QiHMp8a2ZyfxnrUI%2B27%2FxZrnlMM6pzcDUHv%2B%2Fu%2BA%2BE9q8WSt1747vrkxUMU8opGIOVsj8lAL8mWKJW2pzDqObn92J1%2BY47sqiWWf47dIEFyWXIxGja0gSkUFTZwDolX1YLWtB6Wa07seMquDHJTzR6Sc0dCM3ty%2BrJwRwNwN6ZNtpM0FqHfii8cLELkVakWtw6CGh75d01U3EwJgO6D2KZe9BfUq6eO0IzTM3JV7eRGBVz2PaqJq7bhlWiwosh9qLqkjtt5IrnbL1MIteVPzy4wyWWbQqqGsdRnY1rDl6Js5vf5bYIAmEmeMZC%2B803gCbSaHVyJrs%2BW53qUMFox7axuUiai97HkMJzAgL0GOqUBHWZ81JnplzMuNZkbFuxDtP4RNADwnpGms80wrgwLor7LSc0pdi4H2ctnAsQxSiDb6ZUQxzcvQa1qIm4no6WCWblf%2B1ZJ%2FOTORyaHjAlcgzUfbjLgphY48PEeTgkSi8Je9hSoaRfBFCbRJggzSs7QGGnkHod5lkNSJW9mTyXn0DuU3AuQZK%2B7M4cmu7DB%2Bi0nBKL%2FJhQetnF%2F3sNHVHeBZYP0t77E&X-Amz-Signature=2c2b445d268b67e97d0adf82237c8258d27ad23ffa961a54827d11edca9b2cf9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
