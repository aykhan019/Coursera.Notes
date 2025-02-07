

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=5fd1f97ba6c66063a8f900736fc886453a9280472aae2430a9f99c85e73488b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=68c44ee1314ddefd703432d74e487b16a65d2898c4da1d00cb709236895b328b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=317fb751841f7c6dec61cbd0a33ae55a71269e5dff3878cd29c10a6a827ac717&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=40069d8f4a76f239bc8b4a7b6100e55da9b6bc8ff1f73352779cfcc8f2b4b030&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=a52f90c8de6b280aed2591a9805799377d935a0e73034b2876582bf6852f7da7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=c0117802b534766e494fba2dcc197a74461ed8837053b1b11eec44e385f7d033&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=fd925c4a7e361ce2505cebf2b4291bd9ee37818e15fea9c8760c54ea9c2a9a78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=3315a5244f3c84e3abd40bab67bf56f068563d4640b39d49b9b7fdfc91a0efc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQT3G2X%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICuUeKlCmGbIgf8uJawrEq9qXGErrRanSKqu1%2FmfESeeAiEAlQk0hSPkbPEfgJMyF%2BGVtyVEuDmMUzuKHSW4uAQ2hWcq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDI4UmwPv%2BQEVlt25YCrcA4jIFht3WmNtp6p%2BjlB9lWYmXeyNFNgBN1nwBaI%2F9p%2BaTOp4ZQkGqYq0RAuuDTL1%2BFFRsxUFnoSv5L2ADiypW5GcWT7rAxiCJlFfQzIAYk0K6FN40j5aqKBh%2BLPM8df5g22oztItZ9ModgZ%2FJhwlf6UoVWbxoS0suUDpQafYZeirZgVg7RsP91zROCbB5CGf1jyIzdUEIs9hCCG535%2B9iCXFz7Cpt2Z5Wz7HgKPqyuVlW%2BBMQ%2FzRNgMsfalteHAGOsnV9Tp9%2F3KqSWP54mlQZQEO0AXCAW5XR3tMa1JqHfbDi6APb4hzH2GnC3ytps%2FxTRatfInW5VAIq%2BrS687GqIaQjMh7xUS0NccAtuVbixWFZIPzQgVZrMd3squqTYu30zdiNmue%2FO60qBGSU9k4wSGDeT%2F%2B%2FBdpAf08969wQ%2FuMLMqqV0qF2%2B%2FVX%2FNgGzII2HHvP6zBeqs1AEUZbZPdAghZuNC5WqynOHidsSyhPMKIyU2fcnLqMzh1BtwuMv12ghzQ6jJjPkMkJtR7EbC%2FB0p9nLbTTLXFz7XDVBhh0sadbZ4wtE0kA9UoaI7MNVT9HFVa729WeIzTQVGigfjBGzQr3dMw8NqRNnfdkg71yP8q4uAXUQZJyxXsWPlEMNbKl70GOqUBJ9jSzDGPHwWUAg0ZlIrm%2BO4Q3mvF03CmxYjSLv50ZrRpVFknRHNnosKsZjN%2BbzaOUgATvVhcZS3MkR827vX2WmU470A3N551RRTcuAW%2B1KQaN%2FzyVGD61U13x5J94qqggQ8DCUeJqmaZsN504NAsiEurOsZlPuemB9zNkpNOZUgD%2F7wCOsmznAY4hQpNYXMaItasXYoC4w9quL1Q2htPDwCyqO9V&X-Amz-Signature=fe99a2af268d85b901f7398d2f3bfc1ec5838308c8d492cde7e01b0bfd8c5572&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDTSC5JD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDXYrIlQhbbDl%2FwH1EwedFZ8fuq6yWU2kryOqri1xXJNAiBq6MeygQUVb61h6%2FE12gMDUTmTHtx9E1WU1V1m3UYo7Cr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMO9Nv%2Ba%2Bka2bmHmz8KtwDKMeryEDadAv4y71BW%2BoUtBLWnnkLcRmCvRibZbBQxOiqJ2ILfZJRyOPpDk%2BuCz0d2axveCvJTb9pufNC1XwEVWtcYbkA1n2g0XAD47EHuu%2BZ5hGqgGuRJuhH9o%2FmVrDvCdUcdMdwO%2FJJNU9EP0A51Mth8fRwrntXt4VeOw%2Bnfcnqstjg9d7a%2BYwPO%2FoT2FgVIaOtmi%2BpQkczGtlnnmzB%2BGEYWhzwx0FlY9r7baQRP1l1cycXJAf1twP4VoOUnZ2b%2FtLtYHB26U6TVqUEs8SkE%2BrXJkCjRY%2BMkIYE7XbOF6On9uQsO%2F34O%2F%2B6TFZLN4hmHgzYd1blG3pNFA3kU339PhJbHXKruhwta0RVFtAD2PRsPs9TL3XnfJPx3Rb9djsntXuGitgNmBF2qmPrDvZ%2BxJHBNeLlwOIYl%2B5vM9ppmX6GqnKAYoekesiAir8y4tkB9UwCX9q%2BysNkaye1HKgS%2BSnCqg75aSidK4%2FPDWKaSXXGq0U8shdKjtg%2FRdLzfDcXaONOJS8hAjo43Mh6tigLvkQ%2B7UqGzVKWkRa%2BY4GmZCTt3zV8t%2FnLU3iiuo85aLVytY%2FmR1NWulWPho%2FLGm1FI2Q7NgT8oH281ONNIl5siv2%2FYWxrbbyJ35dcA6owkvqWvQY6pgEL8b1yh2b%2BX5VB2KaC7S0wIMHB8n1qyi4zb%2F8N4koIV3bcRElEALDZvsX7juCZ78HBHWYDbhpMSrqyXFq7WcvcfvJszHJYM4YHedu5C1CVSyFsQy5DqJGTZGK7BgRl7UkDd7h6RfYA9%2FSZ42Aqi7HazLPvWMkNg7XKy0AuPP90N6hvUQaonZzE%2Fvk6dyBxJ4heaZErT59dt7vdzJ44QRrLklLXwrQz&X-Amz-Signature=d13d005ae6efd1000edc82522a7c58ebe358eccdae9ecc59da6af5c6a0f64417&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDTSC5JD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIDXYrIlQhbbDl%2FwH1EwedFZ8fuq6yWU2kryOqri1xXJNAiBq6MeygQUVb61h6%2FE12gMDUTmTHtx9E1WU1V1m3UYo7Cr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMO9Nv%2Ba%2Bka2bmHmz8KtwDKMeryEDadAv4y71BW%2BoUtBLWnnkLcRmCvRibZbBQxOiqJ2ILfZJRyOPpDk%2BuCz0d2axveCvJTb9pufNC1XwEVWtcYbkA1n2g0XAD47EHuu%2BZ5hGqgGuRJuhH9o%2FmVrDvCdUcdMdwO%2FJJNU9EP0A51Mth8fRwrntXt4VeOw%2Bnfcnqstjg9d7a%2BYwPO%2FoT2FgVIaOtmi%2BpQkczGtlnnmzB%2BGEYWhzwx0FlY9r7baQRP1l1cycXJAf1twP4VoOUnZ2b%2FtLtYHB26U6TVqUEs8SkE%2BrXJkCjRY%2BMkIYE7XbOF6On9uQsO%2F34O%2F%2B6TFZLN4hmHgzYd1blG3pNFA3kU339PhJbHXKruhwta0RVFtAD2PRsPs9TL3XnfJPx3Rb9djsntXuGitgNmBF2qmPrDvZ%2BxJHBNeLlwOIYl%2B5vM9ppmX6GqnKAYoekesiAir8y4tkB9UwCX9q%2BysNkaye1HKgS%2BSnCqg75aSidK4%2FPDWKaSXXGq0U8shdKjtg%2FRdLzfDcXaONOJS8hAjo43Mh6tigLvkQ%2B7UqGzVKWkRa%2BY4GmZCTt3zV8t%2FnLU3iiuo85aLVytY%2FmR1NWulWPho%2FLGm1FI2Q7NgT8oH281ONNIl5siv2%2FYWxrbbyJ35dcA6owkvqWvQY6pgEL8b1yh2b%2BX5VB2KaC7S0wIMHB8n1qyi4zb%2F8N4koIV3bcRElEALDZvsX7juCZ78HBHWYDbhpMSrqyXFq7WcvcfvJszHJYM4YHedu5C1CVSyFsQy5DqJGTZGK7BgRl7UkDd7h6RfYA9%2FSZ42Aqi7HazLPvWMkNg7XKy0AuPP90N6hvUQaonZzE%2Fvk6dyBxJ4heaZErT59dt7vdzJ44QRrLklLXwrQz&X-Amz-Signature=876737dc14b3bd2213e71b4ead702f3dc1fd9ff974a4145a0422c674d06df8b5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
