

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=c69a0d4ed7e2d5cba1d6d333500cd818b280d26e68fb73741b0a3c3949f61156&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=b2336b5c346882fc12c1255c6a5f23173207715672da3d2186e538cdd9c78574&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=770c9a5a0761b863929c630148a673024657080d1e2da388f23982faf62525ec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=b5e5569468ba6e5cf3f2e5595be38fe3a3ecbb18828ae4cc3f63c2c9f670c31e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=d89fe66365d2332e2b534024eee8ab2b3994999ae8d65f6e4715bb41c1145c79&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=7c20897b3c45f55885e3464d44689a8422b5059f4332880fd8ba359dc914c218&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=661ebf4ff5780198ac9ecc9c9be870f4024a2413670655da67ea0b20805a0554&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=c4365c78f0d20d8cbf119d6b82aebf6ef7fca927861f73292dfea425810f448f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBIQSJCU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCICji3%2FnKoPGXm4qU8AKhos%2B23UMS3x%2FZuhK8EvVxg9ReAiEAv3FSyJAjOgsjr7ZlndNGe8sRG3M0RHnWjB93O%2BX9bTMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDBFrDR5mthQp1DrSwSrcAwEOhGtIkk%2BYJsCopubb2rWjezY7seqNKilTyNxnm9nmyAxqA3%2FzjggFjEYvI7W65gIA0YTg%2Fss2GZAKf%2BAFb6TvAloIu2wGC3axZy%2BcFNzAbYRtSFG%2Bm%2Fh0eD2zEXWy4EjJ8%2BJcB0qURJsQugZphUfRQCoLfSgc2hu%2FaDElKhyYsCDJikMZhYOwU8xtIaPRBoWPrA0P797DlcH6OscDeAV3gBPLk3yEpL2mjtr2mcepbvTEkYqgttmaegurxDnSerWCX2Lbgw%2FP1jTMyqzGgqKIN4gI2Scb92oNijkabi69FA7Btj27Qx28%2BRySTal7fqbyOq1oM0AqKucvlEovTerjPV3i%2FiH4tc2TgiiIP8OANJRpF8H5KqCh3d8JcMN%2F5mL8tMjHqYeqgPdPXXfhLovOq%2FpxeV3%2Fryl1ZiLgDe1Fa3EVpIGw12CBLpFcCOubhLBO1xPJ4ubvYu7l27YUDKYkR61sy6njKqkMsYNhx1QEYdj1kC3liD32Nm5AaU4B2LY9m6k78H4K7aPVGxMgim%2FD2rBZ0c9ZCC08zz1bgS1%2FBgMFWwie8fd%2FK2Fqh4pSrS5ERNO%2Fuv0XLW%2BhpqxEmbBnkAw%2FFamIhCSgxf3xXCpjtQ9vgVy%2FwLNu5SUHMP%2F8ib0GOqUBuskjIpWPWvmMUakinLYX94gh7Zf1xRw69pv8%2FQGyUMQiIpncUF2qnQz9Ut2i%2F%2FUsTG00VS607CVx%2B0BjTwCJaA8t8On2rNmBmHD1AwFMZekUvKz5SfSOiCeVuyA3%2FV6zvx5fFqKqt9kj2nJ809m82EayrlTtcds%2BaUIfFSUXKcs2L67qpbJaXzAiLHavgtTQ4aXnFZ%2BGudqmZnR5f%2Fp7P28zxP5p&X-Amz-Signature=72e5cf34e14235affd52ca3546d6074554696e987b33eec53ab60ae87c46f51f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGSCP2BW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIF%2BCeHueNrpe9I60aqOGn0j1UGPoimAT7kzHG%2FpZ7%2FtMAiAW6rwEOqRj2ijLQm3LwnD7k6nFdz5KJxApFCDKXO%2BrLCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMbnlYQzN%2BEzU7rLv6KtwDJavEOcoJso1p3l7%2FhiBQls%2B1cLcDuhifEWeUJNCUUVh9T9I3aWmFdBg8tBed%2BOk0KixXIOzRdQU9Le6doTIGW3R4gGJDzHT1jtKlhb%2BED8UDIs7Mrhdfj5l59gJbohyEHqvhvat%2BNqFRduONuS5e4hy%2BMrJEQ2rRnLMeVHs%2B2kIMnGK53WlvhS%2BfYdXdN0eA57ZKV8vAGOk5T2XgsyLdtEWqV52YX%2BzDtWc5utsrud1xc9IHMXkFyULfnRqiy96xBx0PSNU2rzfQDRJIbI7pWW1xKZM6DjECkVf1kSzp%2BtiePHt485W1kjYH8AfEkyk5ZayZr5DGu5oTiW1ZU2icqBI%2B%2Fdp9ood%2BxpFQ9W6JkNCpQg%2BwUChReYu8WVqHfbn8T1XcSdPJTtQZnpNZA6VjGs9J%2BoPVDbs3G73ar2WWI%2BAmDn%2FO1a5%2F%2BYPyl4f%2B0lStXx6NSgdQczz%2BGaT9Zk8UnDqrOgaZLvdwCLxyKCm%2FJdDdv29B4FqEw4LwEJvQ4Cp8dfRsDZKVxFwSZ2ImB2b4f7M%2FbcPBMg1Cs8VHmSUQaKxPPYsziowV0lF4wbH7Q8jTFsKzNZ7yGnqqEjf0d6j7M82syBo2i%2F0gM%2BrjL18U2My5WqkvJHu79WzAEYAw1%2FyJvQY6pgEKQedieiqmjWmJr17dMKUDQJUN02OVDHzyJ7IGZmKp0KJOh5OeDJCKg%2FRBEx5tkQWRJeIcC%2B5Xwy%2BkvHKMgen3XPJE8taopgUI3U5UYGG2ph%2FE%2FdQOW2iY8qs5%2BqOyvk%2BEQ%2Fn02v7MxfoVqtwDwmmIQNk1Jpyd0iidh18ulNHnb8yKSKoVJFpc%2BafN0aOCaxHXCTj%2FlZlwzJwP2bEvCFb6FObg55VN&X-Amz-Signature=5791bf6f9a3923c9101cb829fc4698bae997047acdb74ba57c05c31c255f5e71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGSCP2BW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIF%2BCeHueNrpe9I60aqOGn0j1UGPoimAT7kzHG%2FpZ7%2FtMAiAW6rwEOqRj2ijLQm3LwnD7k6nFdz5KJxApFCDKXO%2BrLCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMbnlYQzN%2BEzU7rLv6KtwDJavEOcoJso1p3l7%2FhiBQls%2B1cLcDuhifEWeUJNCUUVh9T9I3aWmFdBg8tBed%2BOk0KixXIOzRdQU9Le6doTIGW3R4gGJDzHT1jtKlhb%2BED8UDIs7Mrhdfj5l59gJbohyEHqvhvat%2BNqFRduONuS5e4hy%2BMrJEQ2rRnLMeVHs%2B2kIMnGK53WlvhS%2BfYdXdN0eA57ZKV8vAGOk5T2XgsyLdtEWqV52YX%2BzDtWc5utsrud1xc9IHMXkFyULfnRqiy96xBx0PSNU2rzfQDRJIbI7pWW1xKZM6DjECkVf1kSzp%2BtiePHt485W1kjYH8AfEkyk5ZayZr5DGu5oTiW1ZU2icqBI%2B%2Fdp9ood%2BxpFQ9W6JkNCpQg%2BwUChReYu8WVqHfbn8T1XcSdPJTtQZnpNZA6VjGs9J%2BoPVDbs3G73ar2WWI%2BAmDn%2FO1a5%2F%2BYPyl4f%2B0lStXx6NSgdQczz%2BGaT9Zk8UnDqrOgaZLvdwCLxyKCm%2FJdDdv29B4FqEw4LwEJvQ4Cp8dfRsDZKVxFwSZ2ImB2b4f7M%2FbcPBMg1Cs8VHmSUQaKxPPYsziowV0lF4wbH7Q8jTFsKzNZ7yGnqqEjf0d6j7M82syBo2i%2F0gM%2BrjL18U2My5WqkvJHu79WzAEYAw1%2FyJvQY6pgEKQedieiqmjWmJr17dMKUDQJUN02OVDHzyJ7IGZmKp0KJOh5OeDJCKg%2FRBEx5tkQWRJeIcC%2B5Xwy%2BkvHKMgen3XPJE8taopgUI3U5UYGG2ph%2FE%2FdQOW2iY8qs5%2BqOyvk%2BEQ%2Fn02v7MxfoVqtwDwmmIQNk1Jpyd0iidh18ulNHnb8yKSKoVJFpc%2BafN0aOCaxHXCTj%2FlZlwzJwP2bEvCFb6FObg55VN&X-Amz-Signature=ab0f28672bcf5bad73b51272728cce505697b4cd449f69a8b894845597e54486&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
