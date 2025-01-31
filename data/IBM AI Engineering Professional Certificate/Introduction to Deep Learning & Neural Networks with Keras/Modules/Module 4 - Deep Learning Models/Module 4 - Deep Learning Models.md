

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=1bdeae26cb4bf4cfcfdcbd858f555225a1693254afda259192abb4f87ffc775b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=64d3e2941b28c8519be3460400c8d28bac305f07b204b6fc51dea16e2f9f2607&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=e2b719255a7532d034c78811e827208f7b8a71806c9e3a3c90d22687c4bd1d3b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=7b4cb58b0f13e4d463aad37e595907137aee0b2e6e10c8c30ee2d007d48b83be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=3eb230853b572ea87b44b144a1e1d981ed1d3c91fd43ad20808442c8c81df779&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=f0e056c4939e84f1c7fff231389be21511ee5f0d96b5e1a04f6ddfcf65f1b808&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=502bff6eaed8062a0a3e409cf613ed1b99404e909c6af6ccbae83c0033348bc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=06458f5753ee38aa4696689c6301357c74f1cd09f0e587a57a0a6262329b7293&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW66743P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhsWP%2BAvcwkb2nHVbo9XvatTqDJUAC%2Fxt07cn67XbOMQIgFzoA%2FDWHMLQlyhcMaQVv4W1BuKPBhP5dP8gDuGdcEBwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEz7vrwNrtr3fT%2B9oCrcA4nSrEpWJccA28VfwidYhiTDygfup0glCd3xO7kHbCsaNdAQdDWys0qqMGq44YWWL9uWNsGAQu2D7DA%2F0cCHMzT4SlJnPHZ%2BS%2Fwnv4M%2F5Che6qAFrywYV8pmKiT%2BhcsLP%2BnGzrw9u0VXa8Df7IV1ZsouMyQ8iNUkwMgjQzaH8Jn0OVt%2F%2B1TByCyqMdkg1ZYtJFJ84txDjtOYwU2qZ7EsiVA9Mx45ZbFfWoSgVVHQQZ9TTY%2FplN87MlMOBNSgl2kOQuOWo7WmwAEaAGlx0OUZeOLQwCYFr%2FpK8c3xrEsqk1TLwZQWAwjZbRq4mrM9%2FikX%2Fwvtxt1MhktOR1TwmMgajaIMlPaIXcP9IVNL7%2BDnSZkQpNoxHixW7VV7tszX5%2BUi5ysb6qMly3emL1Jd8FuvYjG6vChqRSpr53wuQlY7d4CQWHrt%2Fw7XILLElIqh6YoOokq5JYR9qfBz9SLvIAqMGQGe%2FuI4Ww9MwIXsTU3o5PnISNr0mGoi6XMaR8aueY8uVQ1OkzHPGxiEYscYuXHsnGJynvIpZjCv4Susqrlyi5ViaWDesC72CqqcCAYWQFzWQGeTLosO2NH498JnBhGLRhn%2BelQ75A7tqeyW3VEcXZHrS8ia5eDbH%2FTlx4lCMKuU9bwGOqUBUYBc0EqloZqzbCKVXDJhRD%2Bl5FBkCimD51KaOa8p4jlLcVqEqhSJFW1OdUDGRrdmUlBicwKPTaO%2BUK18u%2BmrUH2V%2B749bkGTiKwuLJhBvsTn0JCs00F5adnurUMUnkJnBol5Rgq32sxbSiZthLEHd4bsWhuAvuC6Z2KChzY3AYF1Nr8AIe194m5IegeqxiPNTS07eFLCU573hHXgnSoNRshelll2&X-Amz-Signature=e326b0c705c2a433b7b353570763e671c3870231bcf0e62c49d6e9e40e5a8f8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622IR6Z5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqEzfXMNneR19O0iSf3vtmlj3FLl1N46HOmkIgtcORBAiBePSFzT70TwA1j%2FHH%2FUTtmv8zbpx2juX%2B%2Fr2ZAHkqacyqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsxMyd9%2FXNuOjwPngKtwDGDh5DX1W3GI23V03EJqreREcYy9IypVij2g2bCLy9v9v8DpNfCc9MLcYM3py7SKfWQIHNVsbQXikIHXe8xJmjJ%2BBQRY2QsQgABvgAuzRUEdMoi3f%2BxWcCWvTtdP9uX1BFJzVypFRQvw%2Bw0FHk4O9aVLNmHUqk6WztqSUEkdv%2Fm9BVWB5YY%2BITYB%2FfegpT2NYGT5z%2FSHr3%2Fd6MJeBMKRe0ctA86FaBOB8KgwfPJelPdbqB5XamolPm6G420XHLYf4OAMmDsO5W2rbQK7FwcpRw9eZqgiytPFZeHvJDbeyQfjWgC0Qa1KmzbiLvOhm%2FWy%2BOROtOeXzAymbEiVN7xlP%2FglKgg6cyBE8WJRcbpeCfc8eywE0KbYSRfaggoVJNbR9w0uYwNHmFQ67D2rb9PYgEInV%2FVIO%2FsOixyCOJg3F%2FSbSoJhzQQAtzQuwlupDjECjWGSt2cXjGpoD2IZ4EwllOQIgI8kqSGH2LJ7DcCfXIM5ezOJpQpk6IBvO0SQFCgybRScxwjRTmXIKB%2BE%2FCYk2SbPAVwJNsowr9ohAEtYq07YXsO9kOR0h1eOF3Hz1xbR%2BZ3OjEoDjdV24iI6gIakhFiEpybguV31AFgdNOh%2FTpShaiDKL7tgvbKfsWuwwmJT1vAY6pgFx0y0Tnaq9Wlj%2FYbL1PbQUW1Eser%2BvbNtDMg6UiWx0FTEJfKNxghgNZvd0JMz4qST6VEokXbhI9oq8nPYO0ijjCdtTNjQLGDvP1fqxFaYnOdoexH38%2BBx6oVGx2qzLZUw29GF05qBHOgbD502GmSOw3wlGbFwrU8ipa7EMktvYimBGix%2FIvoDAUa598ljKjmWvlB7pLA6uXNQi%2BjfLtbo7kkJn%2BRv5&X-Amz-Signature=ea4fe417bc5ea60673f02a785789e94d08e689079b740a74e71a9832a03e6513&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622IR6Z5T%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqEzfXMNneR19O0iSf3vtmlj3FLl1N46HOmkIgtcORBAiBePSFzT70TwA1j%2FHH%2FUTtmv8zbpx2juX%2B%2Fr2ZAHkqacyqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsxMyd9%2FXNuOjwPngKtwDGDh5DX1W3GI23V03EJqreREcYy9IypVij2g2bCLy9v9v8DpNfCc9MLcYM3py7SKfWQIHNVsbQXikIHXe8xJmjJ%2BBQRY2QsQgABvgAuzRUEdMoi3f%2BxWcCWvTtdP9uX1BFJzVypFRQvw%2Bw0FHk4O9aVLNmHUqk6WztqSUEkdv%2Fm9BVWB5YY%2BITYB%2FfegpT2NYGT5z%2FSHr3%2Fd6MJeBMKRe0ctA86FaBOB8KgwfPJelPdbqB5XamolPm6G420XHLYf4OAMmDsO5W2rbQK7FwcpRw9eZqgiytPFZeHvJDbeyQfjWgC0Qa1KmzbiLvOhm%2FWy%2BOROtOeXzAymbEiVN7xlP%2FglKgg6cyBE8WJRcbpeCfc8eywE0KbYSRfaggoVJNbR9w0uYwNHmFQ67D2rb9PYgEInV%2FVIO%2FsOixyCOJg3F%2FSbSoJhzQQAtzQuwlupDjECjWGSt2cXjGpoD2IZ4EwllOQIgI8kqSGH2LJ7DcCfXIM5ezOJpQpk6IBvO0SQFCgybRScxwjRTmXIKB%2BE%2FCYk2SbPAVwJNsowr9ohAEtYq07YXsO9kOR0h1eOF3Hz1xbR%2BZ3OjEoDjdV24iI6gIakhFiEpybguV31AFgdNOh%2FTpShaiDKL7tgvbKfsWuwwmJT1vAY6pgFx0y0Tnaq9Wlj%2FYbL1PbQUW1Eser%2BvbNtDMg6UiWx0FTEJfKNxghgNZvd0JMz4qST6VEokXbhI9oq8nPYO0ijjCdtTNjQLGDvP1fqxFaYnOdoexH38%2BBx6oVGx2qzLZUw29GF05qBHOgbD502GmSOw3wlGbFwrU8ipa7EMktvYimBGix%2FIvoDAUa598ljKjmWvlB7pLA6uXNQi%2BjfLtbo7kkJn%2BRv5&X-Amz-Signature=911f66f81b2095952264cc9d12facc1b85067bdf43991cae04a872fbf6e9c3e5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
