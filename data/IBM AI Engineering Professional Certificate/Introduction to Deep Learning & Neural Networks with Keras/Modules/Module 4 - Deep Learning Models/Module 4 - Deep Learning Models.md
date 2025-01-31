

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=c02c53744bb64819ee97532afd71bca5898ad0539bf15fc420868861c31f4add&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=84c6b5870312796ff26108f2b5cb2e669a45af208dd93199e9822a2f380717b9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=e7c420c5754e7480495e297818b815c80bca86ddf68bdcfea8c27798cfd86269&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=1dc7e4b8cd543c2f14f622f94b61f85a5c9467fdd981f89b2fe64922264c021f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=e9c16ae46d16c457dff1440f6af1b90bec51179c8b2fca9de8bfbf945912f713&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=b31e24cc32a99efba05eb0c32399e2c48ce0b8327285814d3f1bacebe1e1c878&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=fee563abf804cac9a53fb20aa2590104f0b00b144c2f70a70f741d232b7f7436&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=77aaed91f4e236a2046e093939ea99917b4fd0f1c6f05be841ad6c9afdbaa451&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPVFQY4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbc%2Bb9WUGi3CtIO3CRRDpipheSPNaE%2Fg4wZEQkWYyaagIhAN5rwTK%2FX5zSDbulx8Ap4r93ItIFoEMl1F2HRFD5oD5XKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcEe62vX77MTswEzoq3APesoDW05iFTi4H%2FegCeauS4fvzvaB9QuV4Jd44%2FZA27xxuzIEICjQIFxplm0zbUWmUUZTpjANTpAEui7XsrZboaKZGDN7Q922t%2FxetAH%2F8qI%2Bi3boiRDBAMn1OUUyHV%2FsVtP2eAkMiRjUqzkSJNhhBJ59%2B9zbm48MIDy%2FluN6aiTOX1Lf2ix85Ubg0cDo2LCfYR2o21seQ9YMMmCNNGbEswLGCco7QbzU32dRwRiOAVi5MN1pdJIe%2BxTYJJ1M9Nr5MkpadaMEMO%2BOXmNtk6wz07xcqjJ%2BJuW9%2F9SVgN38OT0sK6cUOj9vOoyxYzJPEq3XYATUYoUQZrJpKTBj%2F3%2B9DD2SS6lfnkZm2MquKOm4De5bdcUSPlfxV7bBI4lzKwq0cF1hcNQJiBrxxMNxydRj%2BEkBTkBojZk%2FSmlMexvGkA2pexipRo4sfc9fa5fZuOkGlr%2FTsTDveFhhOLhK2GkajIOXqom4RoA%2FFiQPbEEqzwlCoiOuJo0Jj5ZNKv5pISjPeYecaavRd4RpyJiH3Okp7uewNF3%2Ffz1PvavGT6rfedZSBTTVmHQlzqeTe%2FafjlF1wFJ42yP3WzfRLhUDD3IAcosiCNf6Fvt%2B36WeHyjp9TGgSM%2FtTR7XYKFwqWTDBpPS8BjqkAWu5sFYyOBtguPJ7M5QQ%2F3jz6mcMct4RazojiPvwnewD7jTXuMaLw1hhIBBKvcSAukzNzqQ7bluYpPjAxS83C6rlCnuWKWdVXHOaC50Sqa3o7MHHr%2BC3sq49vFL4xGaXtHZr6cWmBEoAHoZFCTsHzN3q3dDhPJoLeEwNaHkR%2FKgnUk0I2x7HronIsI7sQzqReDvF4YPm5S2CbbNWV68KpB9Nf%2FY0&X-Amz-Signature=1fd3a6c7516eabf9ad3428fb12533e5f68005fb98b60301cfd175c5ed8fcfa4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NFSO5ZA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjiWwpFuFhI7DmThA5Lg2DDpgiYaGpKX24xc%2F4LTUAdwIhAP7TJD56qrOnhA3L9G9h8tTi1hY5o01HFQ8RHCTKRtkEKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BIW3ap6zMS%2FvMQysq3AMyhRq5DvhjYi14ZZhIgArUbHCmao5UeMGO4vXaYWiu2LsQJmWrALCCsUEahSjmkN2EwtzuH1%2Fp5Iwwe%2BPwxUWpyuTYUJI0O%2BKfFLzbAXay3HKEEzs0kUvmVqeDLc9HSpwAoDpJZRMFms23dBBYPaY799EEa19KTyuohi5Jh278%2FcoxGOp2yZ1MrPnG70pr2Mfq5CLEOU%2BF7VTc2Ycdwn8dzBr05V%2FqX30fgsW%2BRGt95OUL9FHRIAo5%2BjcV5UWN4FVFW2zt88Xwsaq%2FNZ1enfM4Edf7Y3P7%2FDrfKPXkrcLabPEiu2wY%2B7%2BYX5z77mefdwkD7c2FlM2GWIuMlwYD3hNHrZSQ%2B%2FfofbHZkSir1NrH4o%2BxbPm%2Bz%2FvwaYfglFTEzgmtg8x1T76ez5aJj%2FD5Fno2SaH3JT2rgXGvoe2TiU0uqd%2FZXnP1whot7rDAO1IbrnIUCokpS%2BzQNLmbA3h19Caa17V1sDG%2F%2FT8fw5pDTIZf8FoE9VvXmzQyzuAFS%2BiQul1xL8EFgJfh1TWd3VwY1Ir1z1ScLk4lRvKs8AV975HdCXYYDxCWZT4K4RdXvYUcLrNKIw1x6cFcFe8qJShn1OQLrf8yCl9Y5O0fv0tpd%2FABibPaL5LD7Fl9TYXnTzDzv%2FS8BjqkAX1BF1yx64pNATkIngnjFsHsmbhDVPTszJ6%2FZAXgejTCBCekU4gJFSRjyL25dXVnL%2FoU4re%2Bkwft9IpBkS72InU9qD7YCvqrIdgu8HWk3tZGpoDsw%2FNIvud%2FkeM6PQE8bgp%2Fn6sJP6FmcRcPyID3O9c%2FcuWV0Y%2FyJuuSYYONJODRurPROxFEa12y2esfvmlmeC1ey6U5dv%2BPgWwlsMv5MD3dBuGt&X-Amz-Signature=cf81a29d815acf7e5c9af22d78d580bcb917041f1fd3fea23a5778812e2236a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NFSO5ZA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjiWwpFuFhI7DmThA5Lg2DDpgiYaGpKX24xc%2F4LTUAdwIhAP7TJD56qrOnhA3L9G9h8tTi1hY5o01HFQ8RHCTKRtkEKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BIW3ap6zMS%2FvMQysq3AMyhRq5DvhjYi14ZZhIgArUbHCmao5UeMGO4vXaYWiu2LsQJmWrALCCsUEahSjmkN2EwtzuH1%2Fp5Iwwe%2BPwxUWpyuTYUJI0O%2BKfFLzbAXay3HKEEzs0kUvmVqeDLc9HSpwAoDpJZRMFms23dBBYPaY799EEa19KTyuohi5Jh278%2FcoxGOp2yZ1MrPnG70pr2Mfq5CLEOU%2BF7VTc2Ycdwn8dzBr05V%2FqX30fgsW%2BRGt95OUL9FHRIAo5%2BjcV5UWN4FVFW2zt88Xwsaq%2FNZ1enfM4Edf7Y3P7%2FDrfKPXkrcLabPEiu2wY%2B7%2BYX5z77mefdwkD7c2FlM2GWIuMlwYD3hNHrZSQ%2B%2FfofbHZkSir1NrH4o%2BxbPm%2Bz%2FvwaYfglFTEzgmtg8x1T76ez5aJj%2FD5Fno2SaH3JT2rgXGvoe2TiU0uqd%2FZXnP1whot7rDAO1IbrnIUCokpS%2BzQNLmbA3h19Caa17V1sDG%2F%2FT8fw5pDTIZf8FoE9VvXmzQyzuAFS%2BiQul1xL8EFgJfh1TWd3VwY1Ir1z1ScLk4lRvKs8AV975HdCXYYDxCWZT4K4RdXvYUcLrNKIw1x6cFcFe8qJShn1OQLrf8yCl9Y5O0fv0tpd%2FABibPaL5LD7Fl9TYXnTzDzv%2FS8BjqkAX1BF1yx64pNATkIngnjFsHsmbhDVPTszJ6%2FZAXgejTCBCekU4gJFSRjyL25dXVnL%2FoU4re%2Bkwft9IpBkS72InU9qD7YCvqrIdgu8HWk3tZGpoDsw%2FNIvud%2FkeM6PQE8bgp%2Fn6sJP6FmcRcPyID3O9c%2FcuWV0Y%2FyJuuSYYONJODRurPROxFEa12y2esfvmlmeC1ey6U5dv%2BPgWwlsMv5MD3dBuGt&X-Amz-Signature=062accd7caf3ddb909875a7420959050b7b2923f89f11f039bee450f2f0189fe&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
