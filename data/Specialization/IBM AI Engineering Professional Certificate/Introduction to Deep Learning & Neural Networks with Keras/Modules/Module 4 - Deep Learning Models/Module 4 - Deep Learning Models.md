

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=1408cb46820d40dca425573fa6af461728c19dbabf7969c857322c4b880679ee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=3b44be5abe87a003a8d590f2353c2f32ab6085045de9945df3713830622caf4f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=884c4d5e33e11d04602ebc8141778ff0fc0028193951d96a2cbd55b9729dc829&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=62fb2d57abc4ebd4adc9b19699691ac491fed2e43dfbc7835eb75d7d48a11e62&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=27b1f3513a26d845d38c02e12a17f1a900e5e2a58d2261789f182b99377a7f1f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=f55d1eb570adaca8d06271f267263270bf175937c8dd00fd88d27000d01440f3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=ad9e5375883fc65ab407ddf26c4efeea06acd3a2a282ed9bc0622997db2cfee3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=58ea8f79a8e6a92dc1af97c5b6c127e38ee2ee471c5d2455d8e6971302ad1ee9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHNQVZ5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDHJ0L3gT1iP%2FQUfrd8cArQMWvM3MDw6t4JCM7j6SitEgIgO7UDwDLKZSsQy4ZOaJ313YzDJK%2BKCcT5TTm%2F8P5dHfAqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqAP7XzKLFG646AcCrcA83zUSbfLAjW8bPk7aeam%2FmF16nTnK0OBrf1VojMfDUr21otigUxENZdgsowMoW7%2BtybF2FyA%2FF2itPpM6PFygdc%2BnLYbptjSuknODyuvc7mnE10jsvl4qcCShZcLaqMxb43PKgnXvMVn9Qb7WB0KFOXHs9J2Fwp5XUt19KkF5Vb6nvRR30sz9FrZX4pSBVv%2Bbcs59MhNRSxuNfcHmOxXuh6IBgyaGWv1q6SVwIRPj5rHCBYj6F5VrS1R3iZFLA02HsWdZ2W6jdrlHkDTApKXGGIKyZE48lyKk0AIsus3g4RBcSrG04sI0hZztkUJc%2FJxrhp0kIBBQEK%2F4CNHwqhllfIWQxIPXfCLALhhiZgx4s5lLtOhkMUI%2FxTCfehzVq%2BvwOZksRI49EPs8W7QSrY19WCRYdsORTy9fZ1GmyAClPZstRdicJUE2p%2FtxaeQmKIVBEeWnK%2BmgJ1mC49pyYPFqQ9t%2FYStQmQTyHsL3Iw0HOxbk6ZMSG4EjjU9oqW30Fh60kAFkLiz%2F%2BZm39KlcWgbQPHQpYtiEHnQKQLFhEoLESwiZiUOP6ScJwiTbfpSv3lXU2H%2F4EgFrdcuK%2B%2Bu%2FZS6pvbfgLzlxvZA8D85lDmPK6YtdPZUSy1KPVRs1xcMI275rwGOqUBi3%2Fui425U5rvkEIWSoQYmA3TwKN30tBCkcUglK7EsevXgjlSMnYzF4PrLFpAKivSqSM59awnDUQ%2BTRaOtuTi5gnl97QUqyeXusoXnJMHWmrVsSdKNbbycSd8ppH8vofrpFfebf0L3lTkIPNO9xfqyrVuHi6Pt82jEdLtAtzhNwu9OXG%2Fykub%2B1uHIIYYUEfx%2FJl8bFVYSj8ucqvFQ3zHJh4sCx%2BQ&X-Amz-Signature=192592501c6b70a0ece4353048fc0d7fe186f7ed44141a7d9f5d345f4b64adfb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466337K3T6K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICnxRrS0GeuCeAVrf%2BtLmdcwl5GRDcfR4qzE7hCkX94QAiEAqNUoOmhIeuVimQtbUyVmZadKciwAAIbyNS0V3hsD2FcqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNsfoL3H2g9dK%2FQV7ircA9%2FZaymINgEqlRBcJHdJoPQ0NovNdIUz5yNAp1lhPwhSYZMxNM3%2F8fA%2BsnZzYl7wnuyzfBBiMp1iXinhV5AOF01M%2FZleaeJ2452sgwSLkipgRudWqWuFrWtddoScNv9QnMviYrxHca%2F6ouh9mySFFZA5AmxiVyGTGVP%2F3281WzPmNwfXoxWRCsoBK5MH9wQ5t7LboA8Uf9VyXwSlABQLbs7qqqlPOOwivM%2FqJ2xcFO87K1j0dq2sKU8%2F%2BLqTn%2FNpR5SYPx6Gr0AZJU8c9o%2F5BZym36G3%2BiMp%2Bq8V5og6BvjmS3O3%2FXL2Xhopse6UmmV6NNtoqLbg4Nh0nJn%2BocU5206924Yv2vA2FyyhoMn4gLDeGO1WLtqnFInLkBc50jZEjVydsOuOYwQNF9rQCltEdNLmU8D0vbCkGrf%2Bw4rC2yebG8JSjayRBs60B1AJhm8lIlpKRBAJzvhmxDjYyMJfY2Kn2F7sif3re55QALvViyDn57lAVM81FcYU67AdAolw5m6TfZthDlaExhDosiLXs9%2FlgWTfDY%2Fs9LRfBhDjbGw8hBmvCLf6Uxzpt8BqFKruer4hmlUhVciKuirHkRLIjT%2B8%2FwW8QuluJzysvvXgvAY2%2FI1sQxaLbtJwOiucMN665rwGOqUBGI1tUnXJ6UMRGgoxKCwxX4yCI06fOsAizDHDSXF%2Bodu9b2PecuAze3%2BtSZ81VliIwWbBVQGtGBcVltDyAIUQpLXArmI8MtL7wd%2BkFScJpT7mwzcN%2B4fMxFwe9whoRjLxUBZDyXpzPpj4mIs7hKLhXClKEzKTvhWpPa7mLYFLEQLprcePHs%2B33edQiuTUGn8Xrpha4oSasQLqKb7kY057MVl35G1Z&X-Amz-Signature=85bf618b7193352c700400cc8eaaf475a492301f4fdbd90a4b6012724ee07839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466337K3T6K%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICnxRrS0GeuCeAVrf%2BtLmdcwl5GRDcfR4qzE7hCkX94QAiEAqNUoOmhIeuVimQtbUyVmZadKciwAAIbyNS0V3hsD2FcqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNsfoL3H2g9dK%2FQV7ircA9%2FZaymINgEqlRBcJHdJoPQ0NovNdIUz5yNAp1lhPwhSYZMxNM3%2F8fA%2BsnZzYl7wnuyzfBBiMp1iXinhV5AOF01M%2FZleaeJ2452sgwSLkipgRudWqWuFrWtddoScNv9QnMviYrxHca%2F6ouh9mySFFZA5AmxiVyGTGVP%2F3281WzPmNwfXoxWRCsoBK5MH9wQ5t7LboA8Uf9VyXwSlABQLbs7qqqlPOOwivM%2FqJ2xcFO87K1j0dq2sKU8%2F%2BLqTn%2FNpR5SYPx6Gr0AZJU8c9o%2F5BZym36G3%2BiMp%2Bq8V5og6BvjmS3O3%2FXL2Xhopse6UmmV6NNtoqLbg4Nh0nJn%2BocU5206924Yv2vA2FyyhoMn4gLDeGO1WLtqnFInLkBc50jZEjVydsOuOYwQNF9rQCltEdNLmU8D0vbCkGrf%2Bw4rC2yebG8JSjayRBs60B1AJhm8lIlpKRBAJzvhmxDjYyMJfY2Kn2F7sif3re55QALvViyDn57lAVM81FcYU67AdAolw5m6TfZthDlaExhDosiLXs9%2FlgWTfDY%2Fs9LRfBhDjbGw8hBmvCLf6Uxzpt8BqFKruer4hmlUhVciKuirHkRLIjT%2B8%2FwW8QuluJzysvvXgvAY2%2FI1sQxaLbtJwOiucMN665rwGOqUBGI1tUnXJ6UMRGgoxKCwxX4yCI06fOsAizDHDSXF%2Bodu9b2PecuAze3%2BtSZ81VliIwWbBVQGtGBcVltDyAIUQpLXArmI8MtL7wd%2BkFScJpT7mwzcN%2B4fMxFwe9whoRjLxUBZDyXpzPpj4mIs7hKLhXClKEzKTvhWpPa7mLYFLEQLprcePHs%2B33edQiuTUGn8Xrpha4oSasQLqKb7kY057MVl35G1Z&X-Amz-Signature=1f23e76b5cb113b92b45b0df91c1168e98732a3e76649a3c7fdde822a688969d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
