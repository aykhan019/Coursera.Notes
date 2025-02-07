

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=99737d1638f209e144e0268e35781a900eadc12dd2f3d51338f8e7827e79a0b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=24100a6c6d304f21731caf49d20240f06c59f760164b99899af57d2f988a442c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=575b1cdfa7b6680bf396d6882272ffdeb11427fcde3fac634898d72e79404ada&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=87c9417e0f2984d0be44cf3dd4820c29f4ec26cba68427df2a35c4ee8c275d59&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=4f12ad4b1fb87addb8351dd2ddd689c47af7219875d898ecbf4c1785db95c1ce&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=0a8c4a297e807912b8f902e9bd01e2e6bf47ffc6f41d2bec7ff5dd33d7a3c9e3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=14adee8642ee2792b209cef3660a7d5656692190412336ca6db4428de5ad4971&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=855fee476c7738cb77afbc7683d4afa16fc19f1a9dd0238d364715aa8efd7693&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIRLSB2N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCKbWRuSYrQ0Iv%2BkGQqZt1pReNePEQHhFNBSkALnQ9edwIhAL4Yw2LNN%2BNhzadKiMznR7EtviPJ%2BKVJgdlk%2BjtgaKr3Kv8DCG4QABoMNjM3NDIzMTgzODA1Igz83%2FvIi2mIkGIE51Yq3AOGxqB5%2FL6Pg5WJu3rHvx8PPwJGvd5V8YAb5IGKykZ%2Bw5ma5yoQ12y8eR2tE8ng43eab%2FK%2Fwba8ONxpwKgG2LzwCdFeKheHOMd25Y%2FXmqWX0VIa%2FJxA1JeLsE6Vch35ioBal%2BIaQbmYVppRDMh%2BfIYGvHajViWR%2FDQJdqdkt%2BoYivvMF%2FcjJbOX8LfAopZ%2B5hn66qyYFYqst99T0gHasOrYXget4miuELTqsz67ImVGI8yT4j3y0%2B26EJgIVidk9B5ML7nMFD2Gnh8GxdheZFFo%2B9Du9N0UrpTTUKSRYYdW230%2FOfwKPYkY2tphA%2B%2Bpm64LFq4P0H8VajwqGWeTVJptmGC5w7BAJ5xdy1p71mrEyIF3P0T9J9N%2FC1k4KXtjvIHhwdVOmc%2F%2BIIZHyGFZrO14byguRyFfi8Aos8chbo9955yD01qjkz83Fn%2BdxN19%2B0RcBMF3T3%2BC3zdtyC3NDYIxk2JDdUaAUFT3e85knIH2e%2B7aNVrftXz67cL5X0WWnhghrn%2FXqOWJFw3f7YLCjGuCfHgVCScoV4uZz0ulJ41O%2FdxpQirlV8xiG4d8MSTRJ%2FdrVyDXB3e0JIRyF2cbx%2BNEADzIwi8Kn0Ymrqvp2zMtJ4kg9hm5u7fba5oXXDCEoZa9BjqkAZOW%2BNHlp%2BaTZ379Sw%2FQ5%2B43qONR5BgQZGgv4YOgqNgGOlJIoZOqxoauh622O8MrF%2FQuAY0RbzW8w%2FLyo6XqgQZ7mqRmxFlXHjPJpnJb9rye8Qj2unA%2FVxpNvZFJcW%2Btwxn8bNOCQNI0ARQtBOpcBWnVs30o734TLsWJD21YqB7hM4ktZmRtVBTTOMZbEmndPgYBffBdG%2B1dsICX4I3TNXFT2J57&X-Amz-Signature=ddc29ea9f8c7016c4ccb15aac2f74496c163ec878cc95223597974ca9da56b4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWNXLDXD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQCI9YCKJgC9m12rZbJsYxHP7chZD65Qij2nAlFhFQFpwwIgL1JYOMzXLrvn3mHZXLlTo8oJmjh76vPKxEZmuEpRAMcq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDMULLqz%2F%2Ffk0vdYkzSrcA1ZefpIrJ04apndi2DVYzkRWr7C4qCdB7C6Arez0w8QBjkbhkpgJkm3K0u7nNMVH23%2BcVSW9Z%2Ff25vjsS34h884DDr%2BchVO%2BMsgKq2gNQuvT326zKrzP6c6FD4dubg9NVbASF0FxUVker3mIUj5xMypaNtJn5eKLUzwgmOQxw6Ik8mFKWxWCWgxuTzUxUmF7r%2Fw9HmjWb4ho9jRhfsiiQ6P56Vyfhr0E0tqX8Z4xDbXRvL27WPkPWO16wv41XuTbF%2BgbAcRmxbs%2B9hRrF%2FjWIm4weqLGLNRL8cSBukYcigsbOa3avSigaqyqkItuDWXq7i7oB91NVzRiMwQ1DEXXq%2FrNAzX1zfjAvCH7mUvVFnMyzsqlNlYxIU3YIJ8pMAyNvkBdu8s%2BEDF9HjSy23NaRIBBnphqd5ljemqO%2ByQrRdaRbSKPqHpF5Ri3J6SX8IQFB6d0VPAt2f2GCLmFEWJri8%2Fk6VkF%2FMAhoXsGPkWuAR2J6Oe7XZPUxlfjvzXz%2BxjGIY5SyL76F3ahdRhLaslUvYiIDgN39wTmePddATW%2Bx5UtzVdvvlJjAmop993XwxkFuHcAVD9I%2FSBJGymrc9xHXPGesI8inDPonXjaDStzVtx1PGsUXzZj6wKhm%2FlQMJihlr0GOqUBTojgz20G7ECU4fZ8aEt1Gfn9Ixj%2By8SoNEfHdmdzyOcTUrapKXrilKB0Dzwh32gUKUJh%2B05%2Fn8JEf6lLEcSqPL11TV847Bb8UqjwvfBGsoRpDbQpSWBibOaZFF9nalQYnNWePX4s4O3jzqwK5EGPVxlv%2BEuLEwsdPs2a1%2BLkZTExi%2Fj4vW92MZKK6W0cWbVI7xE4bAt2BU9m0sHD9CXYyeZ0rxVn&X-Amz-Signature=b1b3761aab60fb904e6dbbf9d562c3f5c9bb1266523e24a00e67fc485efb2b41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWNXLDXD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQCI9YCKJgC9m12rZbJsYxHP7chZD65Qij2nAlFhFQFpwwIgL1JYOMzXLrvn3mHZXLlTo8oJmjh76vPKxEZmuEpRAMcq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDMULLqz%2F%2Ffk0vdYkzSrcA1ZefpIrJ04apndi2DVYzkRWr7C4qCdB7C6Arez0w8QBjkbhkpgJkm3K0u7nNMVH23%2BcVSW9Z%2Ff25vjsS34h884DDr%2BchVO%2BMsgKq2gNQuvT326zKrzP6c6FD4dubg9NVbASF0FxUVker3mIUj5xMypaNtJn5eKLUzwgmOQxw6Ik8mFKWxWCWgxuTzUxUmF7r%2Fw9HmjWb4ho9jRhfsiiQ6P56Vyfhr0E0tqX8Z4xDbXRvL27WPkPWO16wv41XuTbF%2BgbAcRmxbs%2B9hRrF%2FjWIm4weqLGLNRL8cSBukYcigsbOa3avSigaqyqkItuDWXq7i7oB91NVzRiMwQ1DEXXq%2FrNAzX1zfjAvCH7mUvVFnMyzsqlNlYxIU3YIJ8pMAyNvkBdu8s%2BEDF9HjSy23NaRIBBnphqd5ljemqO%2ByQrRdaRbSKPqHpF5Ri3J6SX8IQFB6d0VPAt2f2GCLmFEWJri8%2Fk6VkF%2FMAhoXsGPkWuAR2J6Oe7XZPUxlfjvzXz%2BxjGIY5SyL76F3ahdRhLaslUvYiIDgN39wTmePddATW%2Bx5UtzVdvvlJjAmop993XwxkFuHcAVD9I%2FSBJGymrc9xHXPGesI8inDPonXjaDStzVtx1PGsUXzZj6wKhm%2FlQMJihlr0GOqUBTojgz20G7ECU4fZ8aEt1Gfn9Ixj%2By8SoNEfHdmdzyOcTUrapKXrilKB0Dzwh32gUKUJh%2B05%2Fn8JEf6lLEcSqPL11TV847Bb8UqjwvfBGsoRpDbQpSWBibOaZFF9nalQYnNWePX4s4O3jzqwK5EGPVxlv%2BEuLEwsdPs2a1%2BLkZTExi%2Fj4vW92MZKK6W0cWbVI7xE4bAt2BU9m0sHD9CXYyeZ0rxVn&X-Amz-Signature=e33e951c17e8ff1811a6baa490962a4b1be5ace0f22727744e2536c95e86827b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
