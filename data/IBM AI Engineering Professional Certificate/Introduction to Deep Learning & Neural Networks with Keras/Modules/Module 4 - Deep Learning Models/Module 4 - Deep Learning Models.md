

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=067b2dc975aaff2775c6d097304c5b790168a24d4229764ef1b9940447e40db3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=5c70d87b9918e078491b6e09aa79705fc38bdbc7e2095e1cb880725131dec789&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=dfde54748c983f3af8d4d73933573066c30cb103bd7a654cf248dc81a14461b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=e9b9affef88b457d2f19e7661a8c5e4cab5c5574d48870e0deb5ffd3ddcccfd9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=6e1849797227ecade43069e2e29fad9a83dacb9bc7ddf22a9bd078d395aca88c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=58c82959a24f442d3343291380b65d77056856191e72ae8957d045b42b6dbcaf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=72e27d47d0b71d37a5234efd3a6eca9e00ab4d3c74f9bea0ecec62e2b1280c8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=f83e558c3ffc7117f15f4cb7708665e03a492b8844cdb657bf5ff8e00bdb0bed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWVP3O3P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXO17vqndm5Tl2YgoNozQMw0fAjiTJC1WtZBcS3%2FOXLAiAjW88%2FvDXqZ12taB77MJW1DJFgWSGphtAx0758bxBckiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHGXzjMt13iNyYN7nKtwDkyUXosUHVbnmd94c301U1YfA7uAL42cX7MpOUMlk5%2FjAi%2BmB0mElPxJ6rKTEAZyWSCrgECvXdggpQwOlbzajNguW7yVAaZAfXgGxlC7LQU8aHHuXA020xfNOC5JEF%2FcDXqq82Q2YqNKRiFiniHNlJjnp3pggVT9Z6mbHYRIuJm5pZilwyG9TZHOQ06kkfh%2F9akC20UWg9nYppDFyLjpvphYeA5bkdZyrYHVxw%2BYu9tQxtSVUPBHjIFRtWXRgcdcTf2HbhUzT4sKNR5Lyms%2FJStdPPCgHxuQG5bEn1E6ugzuPtcWH7ARjCaXJi6QxfzaD3y%2Fw46aFjCtDWU%2FRzEaiFtbMEVU8QFHebj6jwI6NPXHRTOjuOCyBqldn8xshdh9%2FUEUjsyIWPQUP3i5kfYcqWAgefcXcz2LcgECYeSBncv6jez%2FD7C3xhl3Chtc34ELkC28qBZ2ynOFhMXNmK4Zsrpm0HQ3wjVvFoAGSVUsOiLXIxooPeVtQriHkh%2FKuFSJGPMvJ3yMsYWv%2B294zKEA3alb7eNj%2FO0xH1Flzki34A%2FHTka8sxJndZpCb5NIEGhbGEMunXqB3HSIKs4zm6zaXaXqMVrZlPhkz7twupMObePUmiedH%2BgMBCQ%2FHb0sw4KDpvQY6pgFvzpALq%2FDihQ6CZj%2FZoBxZwQVxyuDH9PW4CclD2LO7c28ncl5%2FRdqHFcwZ4aeP6jqItu3bahOzyFrxppWX%2BMLAyVC3f1VF5%2FI8AYGf%2FolTwiXXdTx7mpwl6eUQfh0DFW5VqsbY2NJN6zeMQv0OaNJ79m%2FxJ3ijbU25PnRZC48iiYTPC81yngDT1yDW2PWVmG2dJ6wjlkQPYgoYWS5xrt8lrUrJWbqt&X-Amz-Signature=2014938665cc877bc064c47625639a3fe87d2e0aec9c06e53c09fa36fc70fcc6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QTT5FKI%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5NVV3K56nbUosJgyxTHJpV1%2B3fspFRIhIA0C950WkKQIgb%2FqJYWy4NhoIXU7OyGs94fGzn7vt2NTtJEHIhnlxjDkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInqWlvGfkpWL%2FFJWSrcAycLCOGXClyLFNMpWzA%2BFVYRcwBRPMkj2LcoAaTfgvmDRLl%2FFmeFNHI0fsHs1IJklW1GJsdT5rCAfmx9X94R6zxztwVquQBRH7sld%2FP55yqsKlQENCuYPuU3zJWE9jdfYWmPejWH4dGm9207Qrm%2BMfmaK8t0ecaoCTWmxOpfDglhwa7HQhGEzxtBP56N9OXnPpdr678Ao5HDS6vjdp23EUoXeQ3D9SKIo5oV5nAMo28FoHYOqwSlXNfCWttZZtX5b4hWfAk7wwmx%2FwQPME8wah6VOosc1Xb3i0gy4CVF5maQiIV3hQ7R3zVVCGs6B8ClKlSrnBxZS3j07Q9bkuBL70NunrvZBAHv4MFi6W%2BXQzliVkHlUh4AwJeJriVYr0mOfTHYmBL9%2BCrinyF0DhkvDpTWDYtMjHDUurD0fjm0VSDlV1UWJPlvTEz1E9ENOOBCvEa4bRaV5C42thFEw3TmCZ3HsZKkyj8k0pC7lHOzKdIJ6lI%2Buw2iF1vazg7WzSVG8C1fKLw5UgKHrHPlKR66xsq4aDdIQhO0YPlvZSeQioD%2BMaE88OJ8vwD3UHnnyG8%2BE40wxF%2Bft7qhAAlavz732cyrxDAPmQ4nQ4h%2FcN6g0VRg%2BN%2F9NU05hTHuvAtyMMyw6b0GOqUB0VnspA%2BzxfBzsUIYAkzbpIVDwPKZ7Mzpv%2BPLAiMuxrK15UfakbpwGYjdUO7DC3RbaNq6rjuADuQFrpfQMEooJs0wZru3XfxnsGtkJbDiVwx4uqMK6QPlqgoH0NTN5V3qdFQYj37PYybG4KrwUGqhOdHR9kI9GUx3tvaaeBEhts195us0yvzh0WNoYAmFlwIjBN9LUcZoP9cYO4FIwY9WR8Nttn%2F9&X-Amz-Signature=b0ddbb709567335eaaef4931346a1186ff5975419cd0aa9a4f3c1a0a217f886f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QTT5FKI%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5NVV3K56nbUosJgyxTHJpV1%2B3fspFRIhIA0C950WkKQIgb%2FqJYWy4NhoIXU7OyGs94fGzn7vt2NTtJEHIhnlxjDkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInqWlvGfkpWL%2FFJWSrcAycLCOGXClyLFNMpWzA%2BFVYRcwBRPMkj2LcoAaTfgvmDRLl%2FFmeFNHI0fsHs1IJklW1GJsdT5rCAfmx9X94R6zxztwVquQBRH7sld%2FP55yqsKlQENCuYPuU3zJWE9jdfYWmPejWH4dGm9207Qrm%2BMfmaK8t0ecaoCTWmxOpfDglhwa7HQhGEzxtBP56N9OXnPpdr678Ao5HDS6vjdp23EUoXeQ3D9SKIo5oV5nAMo28FoHYOqwSlXNfCWttZZtX5b4hWfAk7wwmx%2FwQPME8wah6VOosc1Xb3i0gy4CVF5maQiIV3hQ7R3zVVCGs6B8ClKlSrnBxZS3j07Q9bkuBL70NunrvZBAHv4MFi6W%2BXQzliVkHlUh4AwJeJriVYr0mOfTHYmBL9%2BCrinyF0DhkvDpTWDYtMjHDUurD0fjm0VSDlV1UWJPlvTEz1E9ENOOBCvEa4bRaV5C42thFEw3TmCZ3HsZKkyj8k0pC7lHOzKdIJ6lI%2Buw2iF1vazg7WzSVG8C1fKLw5UgKHrHPlKR66xsq4aDdIQhO0YPlvZSeQioD%2BMaE88OJ8vwD3UHnnyG8%2BE40wxF%2Bft7qhAAlavz732cyrxDAPmQ4nQ4h%2FcN6g0VRg%2BN%2F9NU05hTHuvAtyMMyw6b0GOqUB0VnspA%2BzxfBzsUIYAkzbpIVDwPKZ7Mzpv%2BPLAiMuxrK15UfakbpwGYjdUO7DC3RbaNq6rjuADuQFrpfQMEooJs0wZru3XfxnsGtkJbDiVwx4uqMK6QPlqgoH0NTN5V3qdFQYj37PYybG4KrwUGqhOdHR9kI9GUx3tvaaeBEhts195us0yvzh0WNoYAmFlwIjBN9LUcZoP9cYO4FIwY9WR8Nttn%2F9&X-Amz-Signature=c66348ef6a504172e70a53cbff6c8f3683af440b83dee02aa34c0318e12c6a73&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
