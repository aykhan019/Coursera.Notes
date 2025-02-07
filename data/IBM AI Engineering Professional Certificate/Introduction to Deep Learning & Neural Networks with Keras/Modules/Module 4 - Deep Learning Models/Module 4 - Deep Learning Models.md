

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=b5408c4dad028fa2a5d827231c664b35d8d13a9feca229862f9a8a14dcf2d882&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=182f4bfcf22055b88671406c41181e88a82f980cf1f7fe7f64415d0d031f71a7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=0e883e1452edaa54dd945d17ade23535f6e8e0ddc504b01ab0b99229dfc46e35&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=dda22973dd050f77c0c4038344d76f6dbe64f0a6c55632f39531b332cf2a8e72&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=86535786aece8d4e0b1e726975a00a75f38fa4c9c01ef4c8cb5cdc610520cf60&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=55b84170fcd75c3a5c48d5ab632b799c6dbbac068f2e212436d16cc8cb396678&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=34380669ddb44becb6d467fcdd7508a90e5a0c8392b2fd61338a4bf44e0aa7d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=82047af7e1eee4baca011135610409792d91a44832ccb0d104519f0bf567df32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3X6BQAS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFe3VMekXp9fHkOS4eD8EwkpULWGP59BUT8kphh41dmPAiBf62l%2FK2idb1G9JSBxCDgDvP0p2RTS%2BoCdRceHECUauSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMlGduTyMZ4iWJM8t%2FKtwD%2FLwTSONQW4tCNMkhTH934CDsVsZ%2BalqRoidgJUMAf4pOYZgzVtgV8Y0mxsdp5d0ROgwC9%2FxlW%2BprBoOaQdS%2BTSx7TRsWSJccm%2BUfiQYKb%2FIsuXtvGsc1a981f%2BFjohd%2F5rGg%2FAQKB2f8PLqL9syRXFjSDNxH6%2Bq80G2F%2FVYVsG%2FvgcYGSTD54ENmBrzttis4HDmtMfYs0cB3%2FLNnCYnvVAP9vOfrIxCT3bH7gOAhG%2F8suEkgTJvM8Qxs8Ct%2FfCmFq32rbdEIhiob1K3wuc426ZmL9xSr9buz7IzZsh%2BP7BjTnUQ8VSNOxIaRX6QsInh58wY1a21WIYwYEJXTwt4vt7bYGklKe95hZnKt39WGdI%2BoWjzltnFaAmebm4zbNBgFgsKP%2Fqbx1ijOeDh50jXg1mDMvlbpPoWmSu1xwZodpIW6B%2BcaMoyQHecSUZ687W0q7o4PHR8A8K%2BYUCp%2Fm8AE3rS%2F80OSMF5Lg%2Be4rq4wZZMv%2BZPV51d0fLknE6uJw9XXu%2FSdJdt%2FmBvTU%2BfhjUiJnxEKgYWnGrEKCQBA9r6SlzUglswertcsY7jlOHDvGHj6R0%2Bn89hacj7FIHyQLHnBmGR2fpkc4ho2Lyu7pOS8qvWF3y9nj9kObk2%2FBtAwuYuYvQY6pgGFd%2FOidLCgBS3a4BY8NeUCZISL0OLV%2FSRKaSpJfRslDV6mm71yOXhelL860i9%2FzPP%2B%2Bm0SFBLNMdEpO7fH1zSCIzp60aaJWCBsRx7BF8WTi9siGxY5v6ifm%2BxUWQIi7t2uQMWp4YQRO6I0mLybmvY1C3Fw6JKpeKXlAeLTKdB%2FmOqzPcMsR%2BQhpRyT%2BSaBEdd%2BEYRcg5Y5UEheiqsNHh1HfK3xyPYG&X-Amz-Signature=5c918c563421d3117a70ebb0d29e358d90dadbf823a34da1324e09f94de0a134&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZPQBEHX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCNQ3%2FDTxLrq6btJaZSLmwDYPAi66Gts0nh2gYNnl9nOgIgcX0vqQDsmpz7z%2FXhoBI4pz%2FNs%2B4UqAVLl9%2FPUaBpzL0q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDPzBagwgakdy0aowWircAy%2FYH8Id5jV7zxIAuS8jA0yBL9%2BYC8Pg4cDyXH9o3JovuAt5dYUah3C43kQI9DOhU5Ma8xgN5suMZ8bRR10b%2FmF1Y%2FbOpqomOIvfBs%2Ff4mHOZjtfBYfylaMV%2BLuqWFs1sYrhsMSlDPEhs9X%2F84lUFkpJo6hOr4k%2BMFpoSY0UlCCWi0KPro4EJp1hXftlU052pPhxnAZykyOJ9GcFtYcTCd%2BU6pcWXkiMaP03EdN0Fojtxf8tX3UJjBuvBqrU62lWbXGw57hg2dYUUOUp5RANUgUDJZslRwirY%2F%2FY0ZV6SXVmAkRSjhNeMja15OIDtaHiXTshIFNCOBlu99M1Uye99%2FGYLIMwHG6beID%2Bf3xkwsMCQlTTDhYX%2Fb7vMSdWbDIV%2F3HEVX676Gc71FrqODhmOwsS20bgWhIoAfU0mvkO8q63136UMngDH%2FjOHldUGc7xc9PfkHt%2FSYRU2%2FfZaYUcKlMnBPb2omG0nzhWHXMChvPTfwwqJPIy5pdXmIH8LR20oew5DCOIjjYSeF8mxv9%2F5N70ec5n3a24awKFZv42n0kThIF0%2B0CzRP4TdZJ2QtzpvPgxIv9%2F61Q33Ya%2BOz5IR%2FyqFZ0u%2FlYmie4oVUuYr241O5liPlFvnM48cWuWMMOLmL0GOqUBpEsVFcL0fc26IL97gnfD4a8Y0fHPAVnKDy3QGM7b8UdlqXYPFFv7M2szJfgNsSE%2FOgcOkAJCFXiX1KPsVyDwaKvBzrmzhdVr2WWbP00lcleR%2BJw%2F49cXlrQHRFQjb4w2ETRB15zWqDB7BOlXS%2BbvLxdjBNIzmWxlBvcAERQ49m4oCHFHwSeDC4Ewt0ri9m0ewZ29cyuEsDBUe5%2F5Tyjvqf1uNhX%2F&X-Amz-Signature=e288a90c52329586344fe97bee2fd451efdf914c9aa7ba3d7bbfc2b235cadf1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZPQBEHX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCNQ3%2FDTxLrq6btJaZSLmwDYPAi66Gts0nh2gYNnl9nOgIgcX0vqQDsmpz7z%2FXhoBI4pz%2FNs%2B4UqAVLl9%2FPUaBpzL0q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDPzBagwgakdy0aowWircAy%2FYH8Id5jV7zxIAuS8jA0yBL9%2BYC8Pg4cDyXH9o3JovuAt5dYUah3C43kQI9DOhU5Ma8xgN5suMZ8bRR10b%2FmF1Y%2FbOpqomOIvfBs%2Ff4mHOZjtfBYfylaMV%2BLuqWFs1sYrhsMSlDPEhs9X%2F84lUFkpJo6hOr4k%2BMFpoSY0UlCCWi0KPro4EJp1hXftlU052pPhxnAZykyOJ9GcFtYcTCd%2BU6pcWXkiMaP03EdN0Fojtxf8tX3UJjBuvBqrU62lWbXGw57hg2dYUUOUp5RANUgUDJZslRwirY%2F%2FY0ZV6SXVmAkRSjhNeMja15OIDtaHiXTshIFNCOBlu99M1Uye99%2FGYLIMwHG6beID%2Bf3xkwsMCQlTTDhYX%2Fb7vMSdWbDIV%2F3HEVX676Gc71FrqODhmOwsS20bgWhIoAfU0mvkO8q63136UMngDH%2FjOHldUGc7xc9PfkHt%2FSYRU2%2FfZaYUcKlMnBPb2omG0nzhWHXMChvPTfwwqJPIy5pdXmIH8LR20oew5DCOIjjYSeF8mxv9%2F5N70ec5n3a24awKFZv42n0kThIF0%2B0CzRP4TdZJ2QtzpvPgxIv9%2F61Q33Ya%2BOz5IR%2FyqFZ0u%2FlYmie4oVUuYr241O5liPlFvnM48cWuWMMOLmL0GOqUBpEsVFcL0fc26IL97gnfD4a8Y0fHPAVnKDy3QGM7b8UdlqXYPFFv7M2szJfgNsSE%2FOgcOkAJCFXiX1KPsVyDwaKvBzrmzhdVr2WWbP00lcleR%2BJw%2F49cXlrQHRFQjb4w2ETRB15zWqDB7BOlXS%2BbvLxdjBNIzmWxlBvcAERQ49m4oCHFHwSeDC4Ewt0ri9m0ewZ29cyuEsDBUe5%2F5Tyjvqf1uNhX%2F&X-Amz-Signature=eb312ed578aa70c1876373aeca9cdbff1201b12f619353d0730b4c1a28462d54&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
