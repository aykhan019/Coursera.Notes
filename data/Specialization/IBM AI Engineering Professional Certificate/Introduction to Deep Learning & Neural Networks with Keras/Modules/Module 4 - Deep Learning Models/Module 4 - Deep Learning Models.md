

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=90ca57a9f8f8412fe5b9d800e494d65806d6e4c64e66f8fd3c288d4d28882b69&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=4f908148506b472f7d1d86575c618c5abcebc880e7760057349ada77f7f2c257&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=5302a38ff4d7f9a4942cc50e539f6fe28f550ea935df077e8071621f85dbe193&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=87ebf9292a4cf2da4e417ef9aa67f7afb5709a9ffa57e8b2de894dbb2cb8ade9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=e397261e2f63a95426eb78acb611fe706a65b05b6d49254e5a11abd47566512c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=1346deb4ad80594c4b88251a30e7e1ea6e73fd4dac440fe72899ed398c730d33&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=63764d96f0a41931b9f6973c6fbae3af845769a81094e074f52ac7322093eeb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=aaca363ad49762c0d2fddd84d5c3f46c64cff572940d2ed05307e0d3db7f0404&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBY2VT3E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDL4ZdSWKoE8M9XxDWWRnUAAd%2BsyFakXppx%2F3tfLibWmwIhANw%2FLQM4KxCDMaUrE0z3RF%2B1s4hPbtSBKO9aTQzGxL2CKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuGdVSx5gMDK3CLQ4q3AM%2FJun8avT9TWEy98cZQqLN5suF3RRe48Ndy4MVKEXKCmvFawzHjkYtmh5vwMW4i7M63nsORt8IDTasy1JC7jmXFFaw5x7PYMiB6OARTRjuPdtcEZNglCxP4V4P8YnLzv8P4wesnU1ZA0X5U7ym%2FgZcq7Vz8sIcoEH5t%2Ff8LfCGcwyD19kIL5Y2y2GyIg%2FsduxHiI%2BdoAC0Q%2BtuMNgkEZsiuoBditDCqRjVqKYwiyyj5JAqLEfB37KR7zsrgOiSFynFFb3TkmCn4YAjiFnes9qRmrWmgt5nehIqpqpxdyIkhSaZFnOwasGJDy3kMhZ7y0NqxudEUfjl7Fw7CuuDepsj36Q3sAyJGz0w5fT5FED1pYBPGW%2F%2BqJIfSj2Rh14BQBiKFFiailwOV1JUAHcCaM2Wu%2B3TBLnFDfHvADuGa92Sl2Kap5bCwQmLtDK%2BM%2BxNEZQEcnK3t2IsfHBMTy%2FWZ6bPuhLrZJ4fJm9CehcUxVBfGm2kFFNykwVd5aK2dGIu9j%2FOaovZyvpQhRdJr4ZokuVre23CpvfAycP1%2BHeuv2E6HFmtjP8ePNAHkkyhHbLAq%2FiyheVV0d58PVnbFKMlf7GzG5rWLG%2B4br%2FxSs4NdwnpaeagvepjvdRBdhmEHzDRseu8BjqkASeQb8S246Nywr8C0UQDwPEDc5q%2FkaNegbjqYsoYWR9jyRYk7EJDsFTCCEkCjH%2FHLSKUMe6V47c1xW%2Bqlp%2FElWIhK%2BWGNRs%2BvPfI0dPdUrvd%2BFX81BaGgbHCAx1lLfwE0Zsq79NL1PjonQ0udbKS%2B%2FwZoWeP2PppgQVD5375eFFzzBmSvlKB0NrU%2FH%2FEyEezpC%2Btpi39K3RkZ2eCPdUw60p09YQ8&X-Amz-Signature=3ff92ae4debc227180407175526a45cd55dc8e1c31d9a5a40a1b198ffb0cf9ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPV255UH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQ0OBkSNerUWlaHhCwWq2N882c71VlpMovFZLvAqXbdgIgWmPzIKBW5nIJcnYF14dwOxvupV5XEDC%2BbQz8ijGuurUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOQ2wA1OEwmb4h8tSrcA39DPNQXHs6YV40m1L3zsuJczxx9uYxa3G1zrHnXlcmPaQb4hN139EbOoua45y63dxqpU46xXycUxu%2BotbXzs3x2EJ2rnWP2pN1MHNKMX3P8wMTJRjBGgwUQHfuJ5I9cHI2TV6r9PgvAKtRzn%2FUh4yYGylTz9eo8165lRhuQ8%2Be65zbPlL6z4UteQCDi1%2BKgvkZ91Cln4OzUGbf30MZWgHlCF5REg97BsXXP5pOgxE9RwEafKG0yEFbjzcp8YpGQCoMCWXzFQXUvmqqhnUnr8eEojQhG7EeMYGy6%2BWoa8Pbff%2B8gvj1zSHtxxD0cZF0d%2BlKCZ77Qjrmu%2Fvngp4ZoKaxK6Zxage2upIITOzvSRTZS%2BT16WwdZuNnWfz24QE8ASzr1KNfeB6LsT6xUdawGiDeL5kQDVyL7KenHOoath%2Bamm0%2Bx45giiYse%2By6F8VVxwm99%2F3cy%2FD5zMmVJzsPoji%2B2FXphJQ0MMdv4yP%2FlghNJnXqHi0n14ke%2FEKleWh8Eau2Z9%2FB54Rjc37inl7qOPaZZ5lbuS58llcUscv7WOYGduD671Xjdq6ERNNOaoM0EeydhX%2BRRl6ymmgbtBprZRyZp%2Bj%2FHY3QKW4CxFPuBoZgAJcb8O8bL1hFbCLhtMMix67wGOqUB6ucnVxOtuH09%2FTOBOsZZjA7ORCIjGJpGTzyg64HBHUP9QiMCxGIaJv30FWr4FqfZFavQjFDONSgFpC6bLbz7dj7SPCsfSVDqopRBx15mhI%2BsThZVCFR%2BScvkq6A390WEJkfcW7cogdRZg7Xrtddk7p4L%2B9mE%2BY3UFGjd72MlShFrsZBrb2gC49w0LNNT8ZCs1JUg8F6UDAKBNGOjyxmxx4QoRyrF&X-Amz-Signature=0385253c973e707a3f4b42bd2e1b107cdeb96f1f3da9c880ee8e02717d130b22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPV255UH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQ0OBkSNerUWlaHhCwWq2N882c71VlpMovFZLvAqXbdgIgWmPzIKBW5nIJcnYF14dwOxvupV5XEDC%2BbQz8ijGuurUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOQ2wA1OEwmb4h8tSrcA39DPNQXHs6YV40m1L3zsuJczxx9uYxa3G1zrHnXlcmPaQb4hN139EbOoua45y63dxqpU46xXycUxu%2BotbXzs3x2EJ2rnWP2pN1MHNKMX3P8wMTJRjBGgwUQHfuJ5I9cHI2TV6r9PgvAKtRzn%2FUh4yYGylTz9eo8165lRhuQ8%2Be65zbPlL6z4UteQCDi1%2BKgvkZ91Cln4OzUGbf30MZWgHlCF5REg97BsXXP5pOgxE9RwEafKG0yEFbjzcp8YpGQCoMCWXzFQXUvmqqhnUnr8eEojQhG7EeMYGy6%2BWoa8Pbff%2B8gvj1zSHtxxD0cZF0d%2BlKCZ77Qjrmu%2Fvngp4ZoKaxK6Zxage2upIITOzvSRTZS%2BT16WwdZuNnWfz24QE8ASzr1KNfeB6LsT6xUdawGiDeL5kQDVyL7KenHOoath%2Bamm0%2Bx45giiYse%2By6F8VVxwm99%2F3cy%2FD5zMmVJzsPoji%2B2FXphJQ0MMdv4yP%2FlghNJnXqHi0n14ke%2FEKleWh8Eau2Z9%2FB54Rjc37inl7qOPaZZ5lbuS58llcUscv7WOYGduD671Xjdq6ERNNOaoM0EeydhX%2BRRl6ymmgbtBprZRyZp%2Bj%2FHY3QKW4CxFPuBoZgAJcb8O8bL1hFbCLhtMMix67wGOqUB6ucnVxOtuH09%2FTOBOsZZjA7ORCIjGJpGTzyg64HBHUP9QiMCxGIaJv30FWr4FqfZFavQjFDONSgFpC6bLbz7dj7SPCsfSVDqopRBx15mhI%2BsThZVCFR%2BScvkq6A390WEJkfcW7cogdRZg7Xrtddk7p4L%2B9mE%2BY3UFGjd72MlShFrsZBrb2gC49w0LNNT8ZCs1JUg8F6UDAKBNGOjyxmxx4QoRyrF&X-Amz-Signature=1b7ea2197c65622d5590f0ddf1d75fb9a1a9c28427dbcbe7325a22c6a60677f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
