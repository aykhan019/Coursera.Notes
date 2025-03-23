

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=2b8641370f5a038eee060f46fdef458bbc86b7176640ed91017956b4b36f7408&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=c1a5e52ed450f060c9c0dd475df24cea2a5e8d00400db0e6fe752d77b3162b5d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=134444d80cfd0ee47740b439017e5b0e792223127a31c4f01529fd48c635e04a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=bf74d676ab5743db0197030e5a09648ce8a6bd78a1efde7cab70490ec90dc1a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=8662766720237929eb28afb5f305655ed8059e8db049b8d17e54f990e4a068ac&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=4a384fa0dc12393a7b4064d3700719f10e9e4a0c8ba9a739191c6b77363b9c74&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=0165f945a5a57c10a19a5f65f039d101e499e82c09bbff43b8d875ca60c82cdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=7ab3b179f56fb5c62e0aa22a42b8cd5d36ecd0559c57539f55c53c20b6f3e8c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPHKWOEO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF7qsvmGOYORAiARKK5MoHCO1AtQ1owkxqy3DY1Q%2FnpfAiBPAWixyxVgPH9gLkW3LFjvpGwYdLgBZrH%2FA%2FmIo6qWjiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcVTw8kToet%2Fd4Bp3KtwDmDASurYFbNVHFycwA0XfCzSqdierdrnqhcTqpSakPwhmtIbcFDdtK2d4uLlMe5gRu41AgMqGpTbCzcRikt%2FdFbc1QGMbDvbhC%2B%2Fpt2DCP7qNFrmrmJFyHSc1S2MpX6f3y0BzORb2Jqq1O1FC0J%2BgcvD01JBpTDRXly7RNQsr4kKnRQjiWoynNUEYrU%2FrjL7Rw0w6l6xorwoVokWgT3fIxlb2Angs4%2F1KL8gSu9%2B24aeoC8BVXsf8NEM7KGDISR4gCtgUiRXsFrhj4AsjVWZmjwdcHqDzP%2FGBK9nHWAJXBs3iFdXBFrDEbSDvlJdyR%2BFQibv1hxlHRbYw3KiJ1wDrIeYsNT5Xi5UT0%2BH2Imx%2Bj8KPqYaobBqeHthx%2Fx5hSlFmNhcfQwfAWN2%2BtR4x1%2BzolQc8I%2BaZItgIPpS6ujjqMRQ8IWdNu71Xyihc1xIrgU9iwj9StVIYM9zytvE825%2FEYy1wsn5sqZiX%2FOYt0XwUR0RA802ISCl0832GDltPHLUsDzkCNj4y%2Foj7emHmpVzYxKoDGLiXNpBgL5wDCW%2FgNB%2BQGRE9MNZGP2m8XmbmEbRLbe8%2FK%2BUy9ca%2FfZ5h%2BpkaWbeGWo3OC1Xv42DUPue8caGyK9wA%2BUuRSjqp2%2FYwh7X8vgY6pgHcno1Bh7wrpeum23MwT4UjB1kMLv6KuZvPwV2X1cXn7%2FA5WFOZ3%2FP50nfwPXb3dtcVANzVgCifDcjJ3cZYuwIY0kWQ0tYVoeM5iXzpJE69ik3rJT9v3c%2FC9C2TbqzT8PiiUTDd5JcJ8roMbkljzob8aEtqsZDWRXtGcGi6LVxC88%2F0HHwwJQFU2prfZMiyfkj7maAm2h0mo%2FNeLipy0QghxcHCnJg2&X-Amz-Signature=f3a11863a95843d15f5d2528193816c51fd3f60c4cf9fbc77cff49f6f898a749&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL7SKLWY%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIC7bDQ0xIEVyBQwa2mBSs5AXDCu9S%2BKenmUO1CG53tRFAiEAjbiu0V1GL3IO0Pd4Za%2FOommYVwZblnBHpBg9jFc23JYqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC0F0bTj3s7GxHcwrCrcA5Ajz59l2r5P3z7MbXoXptoISm%2Fz5jeBFuJ%2BhD2Jgvctd0N0KtP3gOUCpzzxUgamO0IYYFUxWBjUgjXRlkGf%2Fq%2FTVCv0APYI4owia6tit6hQtZX4D0dq3rTep2rvSXgDWCnTKK%2Ffmr46XezhopRfx33uSFHpfeIQtkDEb2MZV9S0lt0zzobX5q9q6ndUiawPZWC5p9MhVeoacQ7HocprOfLbKc4YvT3D1selmv5prpZDSaaUckuvr5iqv0Sc8F%2BWb2Yav1p%2FhD5Dsh5aIcHa4bt9IPTLm%2FtNVw5BotXEa6OSdtpIQBkgUouOWI67perKIaOGqnh5kVHwy5zfk8NMKwSIRPasKhEfeA59Qk5nP%2B0ueiySn437ZQyDLKsXZ3%2BIsgYV3dvAHHfiqjwYgU1Gagmj6N%2Bl2wbJHpEtsRnLltZEfmAY2rZIQzHoDAl5aushFsn4UKt9uppYkJ3NGn2Tvg2QFZNcNSbtWPV7v9WmCDfgUdHsaeyf6Wo4E01LffcazkQ7aevfOD6%2BqLdcJnDRVhsiWi3Fwgb8Lr5Cn%2F7fwCcsAjOFHUxNnavnhM%2B%2BtxZzPYhasNrJl9mVI4fLg6IpcTn2IISU0e63lEHngMbFtuyNTplzO2JEI4wl7IhAMLP9%2FL4GOqUBjqqNm0%2B8%2F0dFVzxL4X7XouvSj7b8LWlQGBmW52MGT8uXmZ8sG%2BfK62tZKsAuYzHufl77qMiws2tWiIJgbUDGwJDR%2FAsEj9rJIhf1U67tLQzZJ%2Bzin%2FXVCsrwc1pVXE7J%2F5oUxjw%2FC9ROrBRuuKJuYpZ8Tfo052n6njhgE1xFVFROhaSpAkXb8xoKJ8TEtsjsJZ1wO7DUOHjzYC1Ogcic8%2B3hoF8M&X-Amz-Signature=e3f3cceb519628212f67d7ecb3710233a2e108a7d40c85fc40196b7d0dd0abc2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL7SKLWY%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIC7bDQ0xIEVyBQwa2mBSs5AXDCu9S%2BKenmUO1CG53tRFAiEAjbiu0V1GL3IO0Pd4Za%2FOommYVwZblnBHpBg9jFc23JYqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC0F0bTj3s7GxHcwrCrcA5Ajz59l2r5P3z7MbXoXptoISm%2Fz5jeBFuJ%2BhD2Jgvctd0N0KtP3gOUCpzzxUgamO0IYYFUxWBjUgjXRlkGf%2Fq%2FTVCv0APYI4owia6tit6hQtZX4D0dq3rTep2rvSXgDWCnTKK%2Ffmr46XezhopRfx33uSFHpfeIQtkDEb2MZV9S0lt0zzobX5q9q6ndUiawPZWC5p9MhVeoacQ7HocprOfLbKc4YvT3D1selmv5prpZDSaaUckuvr5iqv0Sc8F%2BWb2Yav1p%2FhD5Dsh5aIcHa4bt9IPTLm%2FtNVw5BotXEa6OSdtpIQBkgUouOWI67perKIaOGqnh5kVHwy5zfk8NMKwSIRPasKhEfeA59Qk5nP%2B0ueiySn437ZQyDLKsXZ3%2BIsgYV3dvAHHfiqjwYgU1Gagmj6N%2Bl2wbJHpEtsRnLltZEfmAY2rZIQzHoDAl5aushFsn4UKt9uppYkJ3NGn2Tvg2QFZNcNSbtWPV7v9WmCDfgUdHsaeyf6Wo4E01LffcazkQ7aevfOD6%2BqLdcJnDRVhsiWi3Fwgb8Lr5Cn%2F7fwCcsAjOFHUxNnavnhM%2B%2BtxZzPYhasNrJl9mVI4fLg6IpcTn2IISU0e63lEHngMbFtuyNTplzO2JEI4wl7IhAMLP9%2FL4GOqUBjqqNm0%2B8%2F0dFVzxL4X7XouvSj7b8LWlQGBmW52MGT8uXmZ8sG%2BfK62tZKsAuYzHufl77qMiws2tWiIJgbUDGwJDR%2FAsEj9rJIhf1U67tLQzZJ%2Bzin%2FXVCsrwc1pVXE7J%2F5oUxjw%2FC9ROrBRuuKJuYpZ8Tfo052n6njhgE1xFVFROhaSpAkXb8xoKJ8TEtsjsJZ1wO7DUOHjzYC1Ogcic8%2B3hoF8M&X-Amz-Signature=2af0cc80da5306089a51a43bf4d561d1bf0909257bc2705646802b05bb38eeaa&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
