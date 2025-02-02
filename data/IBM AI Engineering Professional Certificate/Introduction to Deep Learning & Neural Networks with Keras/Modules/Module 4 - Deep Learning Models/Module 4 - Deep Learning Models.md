

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=50c9589c54272f6faf59a67e760d5f221c4e6444358b744cd239e8bd1edcada5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=3046a5f78e65d0f4ed14a38b279056bfad0413d4715084efe08cbdda23403dc8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=36423539899a9d0ee7d4b99db557f688d1487b65015896890d331836f93014fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=71b16727c6eae1984236adbb5155362467f67373d2c93778e9bc9e809ad9ea60&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=c0e77f71c6a9665d40a8b9c7fda19e282b1cd23724235fc992c4abe4246aa725&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=04f4b485e63efb047933c85da95b1534bbac7d7b0f82269c1b3cf9b71d1bd916&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=70c116d2e844582804a5d159a8bf3b16a611316bc6db16b3e797f084087c1ebf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=655924b805afe6ae410c3f55b322bc5bda5cd996486db9ee545506b9e51a3e34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T36ROWLZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5X1QgGLklz79KbL%2F26jCKiZOyXzkEPodvLublmbogzQIgRbvJQQ71ss6xWLL0b6ND%2B4OJ46QjT6fmz4gpWZL2sEgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlpCPRHoddCktaESircA%2Bxzpx%2BW69Iow93azYPsBTqG9AdbfNxZKnC01eTuj%2BfIklmYE6NeeTaVP8WsSmbcXUruarfVfTcgTr5hDGpXUorJ8xFnbyki%2BUzVN89Xw32PQWSs7p1ebvxhsYDazIsoTsiu%2FRGRZDhqjAlTVFJtRwfEwjbaP%2BC17m%2FbsmKsNafuG0ysD06XampC6HzwRiwK9nqLJgaqtpexj%2FgD7PUMQSESOqIyuRJt2eTnVdp0HnpqkEH8hDDyxSSZ99u1Lhr0wvc7CZKGEuNveXKE5hzEx%2FQKfqaqXGC9WYr%2BFD27AepDJJE8AnsgFe%2FMkycl8h81JYNocTM%2BkOgEWA%2B96rp3wyqfB0shNw7v%2FrkHM1SNW50sPWI2Pu3em7uIT0QjAMrY6D2mYsIw8CLErcF1y%2BIi3uZp%2B7Fxj%2Br%2BdR7G0hdOglFpy6QjX3V%2F8Rgco%2FJ8q%2FuU3vudW1sKItj8Kv2wwTQJoXd2GWASmpt5kX9uVe4GsWcUU88s4PUG8JAdA1lWDAp4NmwiCNNm9HUkcBEN8CwLJaJFIGM2sC6AQiqUGxw39ewG5J%2BdJTg9dbNCfziqA15MpY3ILuFu0kZaEge4PdsDw2jjlyXVR0nBiZA7l5xRHJWUzrhosHn6gUT5RPOsMObZ%2FrwGOqUBqjw2byKirvs5QAPuFRIzd2FPRizH1BeSYYzvvo%2F8femIrZ0wRKMuSm7puJk4IW87ZEk%2FKpzZQSnXDWbdeoqoFZ5zUyHJRB7r2mGN2QclEGaaJTOXoARo5KQeICPPkvoQDUYxe5pEK3GlMjDiXB3DH6jGV452NGXyuFoaC%2FOzQYA2mbZbuOLGmO6St4C9w71cRCBKqchxtObv4UiUiuvDAcL4Mkkg&X-Amz-Signature=3b48ebfa59517bb8adbfc407ab74278211196c00198b996d92cfe2fa698dd456&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676LYD76H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbmDUiuh8DGTDQy7QAPEcfvYZY7Y%2FtUCml7nZEpo6BagIgHQxdz5Pt1DcQhSDScHRaOYQuvm4ArWvN3BgVJS9fsjoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2IcEOuTLSIFEk5nyrcA0r8mr6qGTMcmw%2Bf27E2TFoPpFCpV1X5UTiax2XjX%2F3nD6qbUaUwcUFI8fTGJNkBqmkCgkZiTUPLtfKJ%2FaPbCLhsJSHgQWr1DSmSTtK02ZUIlC1PbeY8G4zr98FJiGR%2FSxQdYOgxGkLH7W0vqEy6eIGOyZ9TGZ8InxXbuZM38KgzTPN6RIltOUTTvI%2Bx9xj6klEUaBxK%2FPwXYSE%2F8M68dLYDKNrZRJxzJ9ai4M1BIx5UPC2P%2FTnF%2BrqQD3yRQ%2B8oxQav%2BsK0lASPy6GxEdHQ%2BC17D7NTDfZ2M0Hr6ZS5ODCNz%2BAibSAt3gHTCFZSpQIem%2BLJ4n3X5ZLUH6VtsUTGA02XO18J9OQ1AwKu5AjCdz9FsXu3367w7FPJPoLft8YecqeH0Lr97dIbraHwwOK7JzbXnToNtuK3CyMOdY8NfjQR5EJH9le%2FpjFw1wFumbz4840zimovsieaW88S5Uy9iUYk1VpoZinLYuRUUGrUGPYdJ4wfL5uVzbecCs%2BjMFUe%2FKoS6MEQ7DhWfFZlADkfGnts8bG1wqtGEEF7yEXpgIjxGC5341UyjPHHJ459mL61nbZmKvS8btz0c%2BrLboQNeQyWICqOwgmt9bS90xKU1u%2BkXtdMvP9k4s3ipp7kMIfb%2FrwGOqUBWkOit%2BhfJGqBf2WRMTWj0D62DncqZ94mYd%2BWUu%2FCBwocq2iYXe6rLU3HsKNTZ5BQJmxyccg%2BHmF%2Bh8%2FANgIxO0V%2Fqpvdyu%2BMgtGAT6Q5QIkxYZq%2FMKHlMlXEeQyr%2Bb3kzpgymXJd0nRXKwGuvaW04smqLCD5zcQql19Ukfwm0IlZ7PxOzI6T%2BSZydcK7SozS9nScxH8829ivFy5S%2FvyKIbmHE3Cu&X-Amz-Signature=e6a4e4f986aad198712f3077a009bb1b83fa906c0e50a931d9c1b8dbcbaa6196&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676LYD76H%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbmDUiuh8DGTDQy7QAPEcfvYZY7Y%2FtUCml7nZEpo6BagIgHQxdz5Pt1DcQhSDScHRaOYQuvm4ArWvN3BgVJS9fsjoqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2IcEOuTLSIFEk5nyrcA0r8mr6qGTMcmw%2Bf27E2TFoPpFCpV1X5UTiax2XjX%2F3nD6qbUaUwcUFI8fTGJNkBqmkCgkZiTUPLtfKJ%2FaPbCLhsJSHgQWr1DSmSTtK02ZUIlC1PbeY8G4zr98FJiGR%2FSxQdYOgxGkLH7W0vqEy6eIGOyZ9TGZ8InxXbuZM38KgzTPN6RIltOUTTvI%2Bx9xj6klEUaBxK%2FPwXYSE%2F8M68dLYDKNrZRJxzJ9ai4M1BIx5UPC2P%2FTnF%2BrqQD3yRQ%2B8oxQav%2BsK0lASPy6GxEdHQ%2BC17D7NTDfZ2M0Hr6ZS5ODCNz%2BAibSAt3gHTCFZSpQIem%2BLJ4n3X5ZLUH6VtsUTGA02XO18J9OQ1AwKu5AjCdz9FsXu3367w7FPJPoLft8YecqeH0Lr97dIbraHwwOK7JzbXnToNtuK3CyMOdY8NfjQR5EJH9le%2FpjFw1wFumbz4840zimovsieaW88S5Uy9iUYk1VpoZinLYuRUUGrUGPYdJ4wfL5uVzbecCs%2BjMFUe%2FKoS6MEQ7DhWfFZlADkfGnts8bG1wqtGEEF7yEXpgIjxGC5341UyjPHHJ459mL61nbZmKvS8btz0c%2BrLboQNeQyWICqOwgmt9bS90xKU1u%2BkXtdMvP9k4s3ipp7kMIfb%2FrwGOqUBWkOit%2BhfJGqBf2WRMTWj0D62DncqZ94mYd%2BWUu%2FCBwocq2iYXe6rLU3HsKNTZ5BQJmxyccg%2BHmF%2Bh8%2FANgIxO0V%2Fqpvdyu%2BMgtGAT6Q5QIkxYZq%2FMKHlMlXEeQyr%2Bb3kzpgymXJd0nRXKwGuvaW04smqLCD5zcQql19Ukfwm0IlZ7PxOzI6T%2BSZydcK7SozS9nScxH8829ivFy5S%2FvyKIbmHE3Cu&X-Amz-Signature=4ffd6e8103359d2006cb73b2d88e40ee6b63dd9266fa024a35df85b290dd5a1f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
