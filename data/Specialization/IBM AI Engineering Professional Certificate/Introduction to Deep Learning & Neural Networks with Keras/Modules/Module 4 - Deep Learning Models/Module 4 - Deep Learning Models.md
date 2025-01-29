

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=b95742acc718feadda7763309bbf278754af85eabc2403fd1d41c7029ecfaf46&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=2421ea0a1a69bee28231dfb76338161e6c2a49986a34c18a5f30e75893406844&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=9e62b0ca4202733043a42394b65adcad76c045a0ad1182934da1b781858a783f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=e38ab311c9acf95f860f313763861487fa64d33c0bcd23f04891a56dbd39aa18&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=200e025a1e9171b95dc39ddf23ec9c0da8d41948899632252aa93e57b21b1980&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=c0389fafe389de54faf05e692ba3d63bb4af99a80cc564738543de90c199dc26&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=3e1e0c06e356489c33716336a867f19907a554fe0d1995e877dc6eda5aae8d0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=2cee612fd94266e46f9aa1cbc441b3c313d0b455588099dd43991272fd82f747&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ3QLE5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDNPKafqD3AKML9LWLdHRWhiZupp8k8ae%2BBtny3kjGNFwIhAOoaqH0%2Fwcfof%2FEmMEQp7Gquwxpph%2F4R992ma2OBDHpdKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgKQkysriKiQadcgwq3AOiQTDzHsfMd%2FD9CkQEYvs5DDR4xM5MSm8ZuGTa5ABDbDf1lSg0c9wcsT6x8sUY7svw2yEy9D5p3G2CYO0LG7YF1aYlLpLX5vVAxFD6T4FypH2i4lW91prTF%2FJ894WnBt6vtfYYvukRXAqxlneCjlr6qqZhfS5lcOal60Z5B%2BzRGmbfQjHAvLNLsyzD9ZMEAR4qbbVQO1m5xK%2BspqmXgjUMS9UkzscBLpgbw%2BTL9%2BPjP7iuoVS2dQ3%2FSw%2F3kUkW%2FenKRdNA%2BD3agxm1GTf9pHJXJU3ErDcylIcDyDNmdXlkf4G2lHE5Jd2mO5vBTr%2FHCpx2tO57cvF9egv%2FV32VgksZLP6NaMzBpLqQkuOnV03tVDoyhOJnmbQNazOwVK7zCyhK6drRqRKoHL5RkfSeK7x3RDP8Z0OO25USHZtwuNzvCsns7hoShjvGB6gwAXYMv8bVks8%2FEaEnJmZI11ZBTDdHH5OU97XwwAU0wcqCm8ax4lb%2BPU2HwiBhg86oKldtckb8Yi24%2Bb%2FeotQ2dXmghIkT4jQ6PsTH0eV7wD9JtUu3WBfAxINFcDnqMNUvWujCdOgUrznY302phjgvsAy0FnstpTc6TaaKRbDNRk9g1fva963GhTMXSlWF9G0LETDqn%2Ba8BjqkAYm5GsyWb0Nvjvmo3iigkxIP%2FMcXaA19WVPq1BSdIp%2BH3zRFZ7wJIF9sZzF%2B%2B039KcH8QLfPtNf0rqKoPso9LvPKtAKMCBuqX2ht%2BH45YfkgQYnTXChO3WcJoLw63hhDx04QjpYiub4KL%2FPWAyrF2ThDvQqw1waCEvs%2BaQar6E1k81dJLYOVx91alOQ%2BgqofIwerRSvzpjg4jTNBrXiWU%2FPRB4Fk&X-Amz-Signature=7a02d2ccc146f85b2de29d3de6dffb7834ef562541a9581d2d37fd599b74612c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFM256GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHApdow8330%2FjtvZbofM1ZnOp%2F4b9h4cvJOJgoLfHV3BAiEAjWi2NJ6DhtBJkFqTNfrd%2FtF5S07CrZjriIfFzd%2FaKkYqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAKqWHlqeof9kdXEJyrcA79W2YIlbdEsleaxsbf%2FFrS%2FxYxojmEefJwghZWW4rlttAKwOhW7xj5owRl4waQVoCg2Z9hTy2hDUcVNP1ywxtkqG6Ker3Z184uOFFAts%2FMVMu9C%2F86WEruSDwFxs07Fkp4etBj725wdfh1tOk1Kmmt7Ym%2FxjaWpfEa5Ceb8oe%2BjQpULnouXLYVVkWK5ZnQ0L7QScPFQ3l%2FBkV9Mxbpoxe1ukoNVXrMsyg4hN8HytEqOcZXXVxSEeUvPUQ1ua6UjNQK0uSMpaqMViAkkwQrRuK89h9H9F476wwcPjCfJ%2FNMvoB4%2FtM2Ob7tLoyUuQCOr5ckvLiMqAsZAAEuUev02G0IET0ZnfcXCxJYkKu5pHTYkgE9hwFBitOKV5OQYlZFQGsOZvGWOazlrkDNCTmIM50Bo3GnYFEwhEtLS5PQO4DFvcoNGXrKannWHc%2F3%2BOGkiZ9%2F%2F0HxPZIsKAQ8GJmksJY7ef2muTdGRgEUTTCZRVfMCzL9ZCN%2FkPeDLP1h9JkkqKtpqlpK30%2FfCFVzgPHuLeM9FLZW5TLIWcspMOarD6ul3IH8v81korFsVp6ggyC5IEWCCFM1nMt%2BVKysIzWbcO7HfIkQUCO5GUGKXp%2FpBEJh8NZMbc83HEK4OLPDAMLqg5rwGOqUB%2F%2BKlubSMa07qwKEwYPIu%2B84fPDlulVTnbvUQMVOo6rl1qHJx1P1jKY6DMxlgpoo5syEoces6FafYS%2F2HjfhXRiOug%2F%2B8XKgO0MFJXZ%2F4J306HV3KY%2FMUDEKExtsMyPCeVnvAr0fRtupvQVT38CDaE%2FHseu3Tfo5pogAHdX32LlsJ2xmobb5zkRKV1N9CN2qWJZ6pPSxJE7hVDjaHalQOMnEqD7Gz&X-Amz-Signature=e9764403afb936629120b3dfb794ca9e91d037ad41215c811f1257d66fb075fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFM256GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHApdow8330%2FjtvZbofM1ZnOp%2F4b9h4cvJOJgoLfHV3BAiEAjWi2NJ6DhtBJkFqTNfrd%2FtF5S07CrZjriIfFzd%2FaKkYqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAKqWHlqeof9kdXEJyrcA79W2YIlbdEsleaxsbf%2FFrS%2FxYxojmEefJwghZWW4rlttAKwOhW7xj5owRl4waQVoCg2Z9hTy2hDUcVNP1ywxtkqG6Ker3Z184uOFFAts%2FMVMu9C%2F86WEruSDwFxs07Fkp4etBj725wdfh1tOk1Kmmt7Ym%2FxjaWpfEa5Ceb8oe%2BjQpULnouXLYVVkWK5ZnQ0L7QScPFQ3l%2FBkV9Mxbpoxe1ukoNVXrMsyg4hN8HytEqOcZXXVxSEeUvPUQ1ua6UjNQK0uSMpaqMViAkkwQrRuK89h9H9F476wwcPjCfJ%2FNMvoB4%2FtM2Ob7tLoyUuQCOr5ckvLiMqAsZAAEuUev02G0IET0ZnfcXCxJYkKu5pHTYkgE9hwFBitOKV5OQYlZFQGsOZvGWOazlrkDNCTmIM50Bo3GnYFEwhEtLS5PQO4DFvcoNGXrKannWHc%2F3%2BOGkiZ9%2F%2F0HxPZIsKAQ8GJmksJY7ef2muTdGRgEUTTCZRVfMCzL9ZCN%2FkPeDLP1h9JkkqKtpqlpK30%2FfCFVzgPHuLeM9FLZW5TLIWcspMOarD6ul3IH8v81korFsVp6ggyC5IEWCCFM1nMt%2BVKysIzWbcO7HfIkQUCO5GUGKXp%2FpBEJh8NZMbc83HEK4OLPDAMLqg5rwGOqUB%2F%2BKlubSMa07qwKEwYPIu%2B84fPDlulVTnbvUQMVOo6rl1qHJx1P1jKY6DMxlgpoo5syEoces6FafYS%2F2HjfhXRiOug%2F%2B8XKgO0MFJXZ%2F4J306HV3KY%2FMUDEKExtsMyPCeVnvAr0fRtupvQVT38CDaE%2FHseu3Tfo5pogAHdX32LlsJ2xmobb5zkRKV1N9CN2qWJZ6pPSxJE7hVDjaHalQOMnEqD7Gz&X-Amz-Signature=d9d18941ef4d703ec03bac2dbd7b3520b50cde5f231524e0b876c69a824ff04e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
