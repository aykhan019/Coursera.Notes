

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=2755d6a0e3c6bf3cf43b74b24e3d957aa67258324ba6f91d9596793192e9b086&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=1d80eacdb5e3797b9bf95ebbb761e54fdfedc26f210d59b0868f1083d0418a3f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=5a5da1ffce666d89195edb7d164255f0fe8ea67b82b1417ffb9ec48471fbf029&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=f0bad7968f723269c02abb8b075ada6b7c4e7d8e81fd15456e49fb8c8c63e8da&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=7357a32ae99397297af92efbd96c201312e0588b229fbacaf66dbd7e32c3a23f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=f0f3f30584af8ea717de8e06006fa70b3c48d869199c192c36bf5416bdb8f34f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=09edb62a4e63406f4b9518e553d3326a970db40d1935ca7a6a581fb4dbc91c8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=c5a099c6da68a51fa743698b69f14f338fcf692dd3552a1419ed1d03d70cf999&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAYGGUXR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2FCY3KROk0GdKyJoF5B21DJki82i0m1eRs%2FjmmyWukkAiEA8Fj56V6iI%2BKmoJkPUAn2XlIjChS55feIoXFCzHxZbbEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDJlTGQPczw69a8ujrCrcAxG9RlsUpPDzY9C2iGyy67CTdOE08i1TsXkLxgFzhzw%2BseGgctHuCX1ksgq2PwfyFp1S64xjPWY%2BSMwwnGl89u20o4Q5zrQtpXBtEDYXiRrqotki0ib%2FLGIQ%2BH1oSVMUdYxcD6Sh695YsURRR1i602Jsp5nM362G%2FgI1TNWwxBXCz%2Fls4%2ByGp3gSZfLeiDBfaSj5kAiHEkdbGleaJZPAzs%2B0guMmDXy0%2FYayvjNa7cjnRLRDBqiIvTMv8OQ64SVT%2Fi7zfi7mGhnnfUT9GxKJThV4vA8967i3ZrWSkhJyxPMvfi8lhB%2F4IMV8fnRW%2BwjWbUfsJj7WvntFKhSnn35pl0wxEaL8G1vQVpo2jxMAHEq5CEKrb3wvuNAChU2ZGRdAHV3jJs26aNJ3ZV8TOgY1d766c0QAzAwPl7dU9P3GgbVZKD82GV0BQowx%2FMcALcd8aI%2BlgPkfCb8pVlLwndWOPfVZ95b8sZsaIaJReaGrNYys%2FmKG4uA1ZQtYbRktKH9vuKgpNwJWPZUR8ACZPbc5ToEdjfFCBtyGFU4XdynWULUFhC4jcTp%2BAl8wuv9xnlfemDKuUamJ5jT379RVqRkPV9NN4bOGwuWhoewtLt2hfMb3q7vdJ5HCC1SrrNsGMIP5kr0GOqUBIaMmiIYCHWp0vLRheO9ra7vn120rZVwSO17DontP8iPijS%2F03gBlzh4JEe4CBKRPRRXgija9imSoxMfQVwTg%2FjUrT9F97z30iRltrimRMwI1XeXKFVOlbVm5trTHvKiA7oXTguLkMKWZ0pQLLapzMj6Cn97OVARSzqFTMz6iiA8%2FMTsidyHLQ%2BHo4U%2BR4C2xfk3hVB9uUy5RFLCc3ndMbiim3m%2BU&X-Amz-Signature=875e43fda43a015f633d8e5dc207e3b939517b41a47fe392f6ef8666929284b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XC3TFBT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCrF7SByxb8mDMFLZJCy7BllSoEuWQFsnky3M%2B3gG%2FLbQIgCzUR4cbEkhjLjokPS5WGhGbRH7pSMUk4VlmQoNzqtM4q%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDLEDmimD2J8dFVRtxircAyGuTzmf5omq6Zfh1JF%2BLr1gPQvCH09C3O7ycEMN8rWwsyBpkuApGaOgbvk9EjiVtAtkYDwRpoErmuQ1l9z6N3xgeTl0hHSSo7q7xsdjCL9vIvX5D7REu7Cv0qKuZwejtzb8ODp3cu6%2FnGnPmcbnyCXSpQ9DZ%2BBr6I%2BQ4bhLyuSytvaC%2F2cXruW%2BWXtvQwnE%2F0uoe6jbyIw9aLayUFaTKYs3X5frnhe0x3tj0cRdhQVDOAMrSjO2tGbFF4W3AJ5zGADPo%2BERVqQZ%2FzWuY2GhUNAQ4wSjqtGiYtUqKESNxRgDCQGQjfQz0rMN5vvlSaoi6k9JIaQRa1cGuOsmQH0T2%2FtmxQcZBYjJi2r9pfIkzrFQeupm339tMV1ZWE8tcyuzFhCCZ%2F7MAJYJ8MgnNAoQspRaM0jV6By%2FtjGnO12PMGo65p5SPf%2FIsflBqh3UzKQ4qVGyJ1tercizeDpiaVb0VKqwWMu06%2B4RhH3Sfgruw4CvkEPN1R8N3Wmskwz1OqN4fV33AR3tYmIiOIG4QjSi86qjFo8rY45NAEWMbREfNX3nRAdQsnwmdSIgUoBfKMFv0SasMULk%2Bc7PP7QO6bObQ7euqO%2BJWU1ayk9EnQvZMIuum83wIrO4BbU0Pu0EML%2F5kr0GOqUBE9rgj5krIOltq9MoHPWJ1sO2wZM6lxib3SnGLnuGCHqXodAjRMiq39VcghjXGr%2FN3UljiGJ%2FyCQXCak8QbItFfgTidAJrIvQ%2BgBq%2FhY1wIMQWP8IRIZ0ruPB7FT0Uj1SbyV0Wu4c8Fxr0qevYM0MO%2Fdh91tz%2BCcaMBf4ZBwa4sAsLzZLcjURI1UjX%2Bfqgt752CkzqAwgOYBQZ7q8qGysP8tm7xWH&X-Amz-Signature=b6567b45d40b448d0d3b041ec61e71befd6ea272af7a9f6e9c8cae7c13fc24d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XC3TFBT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCrF7SByxb8mDMFLZJCy7BllSoEuWQFsnky3M%2B3gG%2FLbQIgCzUR4cbEkhjLjokPS5WGhGbRH7pSMUk4VlmQoNzqtM4q%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDLEDmimD2J8dFVRtxircAyGuTzmf5omq6Zfh1JF%2BLr1gPQvCH09C3O7ycEMN8rWwsyBpkuApGaOgbvk9EjiVtAtkYDwRpoErmuQ1l9z6N3xgeTl0hHSSo7q7xsdjCL9vIvX5D7REu7Cv0qKuZwejtzb8ODp3cu6%2FnGnPmcbnyCXSpQ9DZ%2BBr6I%2BQ4bhLyuSytvaC%2F2cXruW%2BWXtvQwnE%2F0uoe6jbyIw9aLayUFaTKYs3X5frnhe0x3tj0cRdhQVDOAMrSjO2tGbFF4W3AJ5zGADPo%2BERVqQZ%2FzWuY2GhUNAQ4wSjqtGiYtUqKESNxRgDCQGQjfQz0rMN5vvlSaoi6k9JIaQRa1cGuOsmQH0T2%2FtmxQcZBYjJi2r9pfIkzrFQeupm339tMV1ZWE8tcyuzFhCCZ%2F7MAJYJ8MgnNAoQspRaM0jV6By%2FtjGnO12PMGo65p5SPf%2FIsflBqh3UzKQ4qVGyJ1tercizeDpiaVb0VKqwWMu06%2B4RhH3Sfgruw4CvkEPN1R8N3Wmskwz1OqN4fV33AR3tYmIiOIG4QjSi86qjFo8rY45NAEWMbREfNX3nRAdQsnwmdSIgUoBfKMFv0SasMULk%2Bc7PP7QO6bObQ7euqO%2BJWU1ayk9EnQvZMIuum83wIrO4BbU0Pu0EML%2F5kr0GOqUBE9rgj5krIOltq9MoHPWJ1sO2wZM6lxib3SnGLnuGCHqXodAjRMiq39VcghjXGr%2FN3UljiGJ%2FyCQXCak8QbItFfgTidAJrIvQ%2BgBq%2FhY1wIMQWP8IRIZ0ruPB7FT0Uj1SbyV0Wu4c8Fxr0qevYM0MO%2Fdh91tz%2BCcaMBf4ZBwa4sAsLzZLcjURI1UjX%2Bfqgt752CkzqAwgOYBQZ7q8qGysP8tm7xWH&X-Amz-Signature=df3087202cdd496d46d38a77c2d2075aeeb216219db3a6eeac2eb37b96460e06&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
