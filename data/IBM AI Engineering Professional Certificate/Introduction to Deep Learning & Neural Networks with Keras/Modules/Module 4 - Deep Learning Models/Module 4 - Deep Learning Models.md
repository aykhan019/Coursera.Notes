

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=8ca9fadce92a59ffa43a89120ee013d1516e1aba8e454b81e25f08943f24b4b7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=0c677c076ee769425db52ac7ea6732682b65fb87226bb8fabae32d480d682bff&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=68262f76931b6d6a6cd467d9d956a257789d8fcbe041529d369c03c00bd3422f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=ceab835d1bbc89f1142cf457eecd513673ae1ee7ba93d2b4fcfcda2ef850194d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=504f1458386099f8f887a39e6e5f7359496403c2cc8511e83e132d80c2d3f5a5&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=0b88bdfe4c217189cbd306201efb70f6a483a481af03322d0cd6f3404850e606&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=8d74529910e44f6fe3f5f3eec67fb32d16a089e8f0147cdeb0b839b3594386e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=96ea14e172c3e77c3d59bdec98aaabbd520f4c4c2f50a9eb535e106ad10838cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY7KUE3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmdXDMlrHr2ljtYaU6TrszQEvqBIeKAKU4X81QBk04kQIgA%2FnbJW2cbLTamjRxOGBvtIj9jlSrQO277r85D0RerCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBwzZnwCUNSx82vJJSrcA6Vw2UAkE67THVjW5stj6bRjSf62itGa5RWQgT9KfEsiCPY0eYPBzFuwi%2Fh3AisGTnz38jrw%2F6AjajosoTxD6ERPMWh%2FfYtQd9sKTW%2FTds%2FVU9XQLXs5gnRzXCWp9aBPrMdWvN%2F2J5hYffZ%2BOuJHxsuy%2FbpKJzxf9SluXsD7z70c0F7ycQChzw%2BnvhqEr247Fiv9ywxkKfSruQioR8d%2F1YpBDVM%2F9%2BHCRZI9TuLAhfRdDECB%2BbkmfXQ6NxFdA6w3cAXFZCnY1wiUX%2FeAsQiEPjcZfY%2BRBbXZ70NQtmKYDO5DXX6meW3eSj1uBuSg8SCsZte5Wqh1WBotCD24ldvBmeBisfvJqFcI17YNlydSxLJfqngfk0bG9JUH6RbHWtpChK1%2Fe0ufuSzCI8yRUggK7fPJ2RV8VRC%2BGE8whkTUE1D4aNadBp0up8dfCmhmzY3zUrJ583xt6tCWPBUMh4zwwgzc7agCmlN79LdjHD8rbvBNBcKljm8m2ZkJERkYg%2Fj7c09ie6m%2FFMIPBz1MV4QS9JR5h6cY2sjI%2F929fofYsPL6nDn56DZjBo6XAzDG50obLXazl752pfZASU%2FXKhYbHuv7NrFpFKDd2HwY6oVLMzR74ko57FB3jY%2Fqa3eUMN2k97wGOqUBosibxxxlqexoqYiak4JPuGhyogypN9VDdkjg8jJ2zm%2FbIy8jhDPidl7ryUDzNWUw3ln%2F71FRKuFXqKSBzhGugqSb1YvamgzhqYZaeELcvNxj%2FbBEjmm4xSXtCTKKXbS6wa7eMiDyfWpWRr%2FVuX9VXTYYOUKekEbe1xJhZh%2FQ3GHsIkENm%2FQ8C%2Bsa5N5PvCBbhqHMylTZibUO%2F6rm4Jg5wx5BCNGq&X-Amz-Signature=b5eb67bf5ca546b78ecad0a6ceb4a98b44330736dac0f02f2420b1f6e2b3aff9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKZMF4AO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNhJNUd53HGwoRQA2P3tuxCLeHefOjntG7L7sJIuPnxAiABZ3gzliQZjn%2BwmY700BTJ9YgkqLl55UkBPHdLYSkHOSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNmG2oQ0QgYWLqAjiKtwDJrHgeCZnj1LeJAQ0jqDiYx7llgmAekVAgjHsiBbetDF4pwqjgPf%2BFb3tEG3aO3n5xymSRMGk4AjUmFJa1YXZXgEQI6MWCuu0mWzMJu58%2FaIigYbeAlqnsUWcdN3KqMq1POX5RkmCXzvDl1xVjD4gYWnOla7cwKiuF1wRA5dn5A6Y8Vbgw2ryO8c0CRBZAsVDs4tI6GXLpA3T6l%2BlYYxY9uVop23KZGwmfHRfY%2BMmGcnHwiilJl8AF%2BV6aAg8F2mhl8F8LZUbBmTiWcFuCj25kGLNTiLrwag%2Bk8JckmHgvoNjlvqNYakFjaiFC%2B5C8H1GOyR2bJo5qs3%2F%2BtWiH5ymtfOfYIFre7BEUr3hm20sCOMtZ3izpCBzgtqIhv4lrnv2UPg2Q%2FarsRlqClbNBTXwoohVeQ64QJSQ3j0Cw0k%2Fgxf0OZ60P3QyjqkJKjhBMOkbG7PrubwHueymUIFoOGpDBNauztZ3DnyncJ4nWIkk%2Bkwz8ASCycDptdDi6dR1sokh01Z8HkqqDJ%2F0YRvK%2BycuE3RoMREyFy5J2B5xNGlt3fYPtWO2dqfpcvArQc3eAwt4Cy%2FAGEVjskRY%2BevYQOGVWZWTp8w9Ey9G3UzqC6yNnrfvCtrhMRJX%2BNP3dYQw6qT3vAY6pgE4Om3r9pdsSilNq%2BzcfUN5ibESyTT%2B5FiJf6ENe2Q1Ak9CrrAUhen9j0mezAHNHhjC%2BcC8vEM16ZCXO2351WKF98bbAWcApF3vHBIYRrijdz%2F7RxlGu5ofgdFleO%2FYMWBhqxcxv17OH%2B25Eb%2FwzGPc85T7Z0fUhv%2Be2zn%2BhbEJFafw9hBmTnCFO0Ts04gpopL%2F0dh%2FFNTCrI9B83WumPCbJlVKjrQ1&X-Amz-Signature=370ab253c609fd1b391047d141abf4400778ea6c93467c42484dffd2428385a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKZMF4AO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBNhJNUd53HGwoRQA2P3tuxCLeHefOjntG7L7sJIuPnxAiABZ3gzliQZjn%2BwmY700BTJ9YgkqLl55UkBPHdLYSkHOSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNmG2oQ0QgYWLqAjiKtwDJrHgeCZnj1LeJAQ0jqDiYx7llgmAekVAgjHsiBbetDF4pwqjgPf%2BFb3tEG3aO3n5xymSRMGk4AjUmFJa1YXZXgEQI6MWCuu0mWzMJu58%2FaIigYbeAlqnsUWcdN3KqMq1POX5RkmCXzvDl1xVjD4gYWnOla7cwKiuF1wRA5dn5A6Y8Vbgw2ryO8c0CRBZAsVDs4tI6GXLpA3T6l%2BlYYxY9uVop23KZGwmfHRfY%2BMmGcnHwiilJl8AF%2BV6aAg8F2mhl8F8LZUbBmTiWcFuCj25kGLNTiLrwag%2Bk8JckmHgvoNjlvqNYakFjaiFC%2B5C8H1GOyR2bJo5qs3%2F%2BtWiH5ymtfOfYIFre7BEUr3hm20sCOMtZ3izpCBzgtqIhv4lrnv2UPg2Q%2FarsRlqClbNBTXwoohVeQ64QJSQ3j0Cw0k%2Fgxf0OZ60P3QyjqkJKjhBMOkbG7PrubwHueymUIFoOGpDBNauztZ3DnyncJ4nWIkk%2Bkwz8ASCycDptdDi6dR1sokh01Z8HkqqDJ%2F0YRvK%2BycuE3RoMREyFy5J2B5xNGlt3fYPtWO2dqfpcvArQc3eAwt4Cy%2FAGEVjskRY%2BevYQOGVWZWTp8w9Ey9G3UzqC6yNnrfvCtrhMRJX%2BNP3dYQw6qT3vAY6pgE4Om3r9pdsSilNq%2BzcfUN5ibESyTT%2B5FiJf6ENe2Q1Ak9CrrAUhen9j0mezAHNHhjC%2BcC8vEM16ZCXO2351WKF98bbAWcApF3vHBIYRrijdz%2F7RxlGu5ofgdFleO%2FYMWBhqxcxv17OH%2B25Eb%2FwzGPc85T7Z0fUhv%2Be2zn%2BhbEJFafw9hBmTnCFO0Ts04gpopL%2F0dh%2FFNTCrI9B83WumPCbJlVKjrQ1&X-Amz-Signature=a0fe9e5a9d6e5817ac6cfa16ac98867bdeaa3d1db94cc0d4e9230cef62005762&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
