

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=4c32029bebc16ab9f3db7bd35fe805060c9058739821aeded065d900181f6bf8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=0147612e865d5e1d5079297a0e4e883a205b53066c967d68275dd4e509a362ae&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=3429555436fb6ec328141c2c9944f9d0955ce2948755b193c87074ad55b1c1d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=e94ac52986c4f15a2ebb8fcd1da178910dad68db516b8364db8a5978083aea1c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=baecfcad6cc67f5d0fffeb8c3f4c21b7fa91ae5b8bb9d3cbf2d3b3b02f171837&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=63d5cceee27d69003ece974e44c90829dfd5f1061edc75e12694c7b5272cb29f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=50d69cb0dd525298c54dfab3cac12df840a15468781a2ff5fd779258aef36060&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=c39408aff2880286c8e567dbdb6d25a5a2def52c46a965f8ce71df5941b8043b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOEZCGV3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIBqolECMdm%2BzMjMvdV0s2FNCwbwzWKalRBHFPnBKs9J7AiEAuN5iy8JQrXdvTf%2BLcdcnHWlUIE24eJx54cGbiPfz9WQq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDB7oQWfxnFMbA8dPZircAyrhdK3lLYzrApnObU8I9EMXj5rw%2F14WNJdndVDcnElYiP%2FgD%2FT2FHCjjf%2BLkyAIUiqZSriq%2B108GLDckxaQRRoRw%2Fh5zm7suFnu6yT8SAvIWDEEU%2B2yec%2Bw7GT%2BJqLt%2FoFqM1p0RUiBdEOTZxRqO1qe2yQJH2Y0K2VC%2FgVbsx2klGK%2BYK5ANGMf67fOW327LzLEa%2FTUGj%2BZQFWEP2IUPbOGPUzC1ycoAwFDWUMz5r%2B6LP%2B56KUBCSbafRIGI0Ohu9z06DOjgIqEneSuPiOrkyQ837698nEy4gmFBBYCfIkhtS5nqNFV9tns5uqIBW6lIJqcybLo8tbguLhkeW1dyWOrySWu6fXH7YZh2BBWwPzjoC7nryHPJS9MI09%2B25qMozhzpLgqV4GpUGWGWDP3Xd%2BK54wukg6NM%2BSbeCxMzlo%2F8ipE2Sj2Ige%2FZ0i3tY8uD86uocdNDu0%2Bgr9LDNGE93reZjE7rnRBNJZ9zwItwjG%2BBAFRqrqzWlaI8I4NfY4SVCmCMZ1D5bs9cXHLXPP9jj1QYeUMFHqgG4MeaqkhVv99h7i2AJED47m%2BtoBVbnl%2B7kOuraOcLDTsVyM1Y4T05b4vB%2BEKH3gP0laE0yelHzq%2BEHVhXApYViCBZv4fMLGalb0GOqUBPaum1LDd%2FbGe%2F6MjwZhdlEelVZPH9MRBC1iNh2icByfAgCJGfLIewI3B31WWHTeZ1ONcd1mQnXrUrQwT8A7AgZD7uKgKL1HgTjT5tnRkl018nsjRc2X5ealO1DJlIX0fQlsjBlX%2FuJk%2Fno0KQyWIGX%2FEaccaT%2BEUwojuuCSne%2Bn6%2FxNjTMHtxo%2F8cgjN%2BwOKhHrEMU%2BtzXzEvsC3A738b5bCoH5e&X-Amz-Signature=d4259e1e913b1ff406cd536c67ea571a234073bbb1f048fb1c29bf3cf3e42366&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVRK7UO3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIHuvZH5wCCB7QQR5%2BLHMPpVXQnk45jPKXskVjMLcX4sKAiBjf41GM5epsVOr%2FJCQYGSWi%2FPq8gbpsXIG6tjdKMC3HSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMZmPZN2qZPdjpLjDaKtwDvHoYOj8yJUVZcRI0os9Vl6TKAJPiZjBcZM7GMUM7VV5y4UN30VTVQGKvZ4WzMt%2Btdt%2FTHGUPdMpr3yxQds6eS3SAOSd8XVSFbc5g27ZY40WOdg0dMcP84ONh0py4yM9BQ6X9a9%2B9qIy9y7xrEui5hQEAodwSnudEh4TNqKnW72mxUB5TOVws6AXWKjZXZ5gRjFiUL7OCWnC4Sdewu6BQgWTjzSoixZyMoVRb4RC4xAwakKFxvSf5U6TGxgTHLUv69k04LLumyRwyv1RlSK10jqBjnriQ06mNbJKgU1SXQayBYmq0KJRFoiNsBWIHhg488z%2BapfdxELuremoHTl1d58jCvwpJyplH6uK3%2BOprh8%2BaOUe4scQ2gh4DbVvH4OwX9Ns%2FP%2BWNDTxVzu3ByWvlYvPhw10qI3eAiGWji1vpLWsWuZtCnbIFMLNhWn3JOUC7lnI59fFCRrb6LYqbvFyhW2KZF8%2BkxjVO1UCzMR942I2%2B5iEClwNm4XJZQPLBF6Gu7%2B%2Fj4IVNGSlSj5lE9815mskdAaEGOzbOffb5MrUywUjTviTYAitkYoJg6Fq4sLpR2g3CVcgIztd0vdEifbLrGEp7MVomiSDgW2pTlyDWutqLrQ8atfMV2oUPZw0w2ZqVvQY6pgHVaeFoNb5qKlJXJ3kAQHljfoQozoABMPYPofk1oEwlYm7EhAJbTclce%2Bf%2FoAZMNzvJ8ON5ZEOmfo2uL%2FolxkJjG6m1BCYs5fV2wPL5LgpoCr%2FDuJx2hXkju7EeaRBhFkMaruz7A8MNJj1gH%2FbEYXhm9nN5eDbK%2BJz%2FnpobT2WJZI6k9ftKvuP7KLiHtS8Xbnnc3Px%2FRMsKVlkS5uI7TbntyMUmnsZA&X-Amz-Signature=fab04132b443ea7769b2303a73b3e12e7151cffac576b00a07cdc63c3b76131b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVRK7UO3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIHuvZH5wCCB7QQR5%2BLHMPpVXQnk45jPKXskVjMLcX4sKAiBjf41GM5epsVOr%2FJCQYGSWi%2FPq8gbpsXIG6tjdKMC3HSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMZmPZN2qZPdjpLjDaKtwDvHoYOj8yJUVZcRI0os9Vl6TKAJPiZjBcZM7GMUM7VV5y4UN30VTVQGKvZ4WzMt%2Btdt%2FTHGUPdMpr3yxQds6eS3SAOSd8XVSFbc5g27ZY40WOdg0dMcP84ONh0py4yM9BQ6X9a9%2B9qIy9y7xrEui5hQEAodwSnudEh4TNqKnW72mxUB5TOVws6AXWKjZXZ5gRjFiUL7OCWnC4Sdewu6BQgWTjzSoixZyMoVRb4RC4xAwakKFxvSf5U6TGxgTHLUv69k04LLumyRwyv1RlSK10jqBjnriQ06mNbJKgU1SXQayBYmq0KJRFoiNsBWIHhg488z%2BapfdxELuremoHTl1d58jCvwpJyplH6uK3%2BOprh8%2BaOUe4scQ2gh4DbVvH4OwX9Ns%2FP%2BWNDTxVzu3ByWvlYvPhw10qI3eAiGWji1vpLWsWuZtCnbIFMLNhWn3JOUC7lnI59fFCRrb6LYqbvFyhW2KZF8%2BkxjVO1UCzMR942I2%2B5iEClwNm4XJZQPLBF6Gu7%2B%2Fj4IVNGSlSj5lE9815mskdAaEGOzbOffb5MrUywUjTviTYAitkYoJg6Fq4sLpR2g3CVcgIztd0vdEifbLrGEp7MVomiSDgW2pTlyDWutqLrQ8atfMV2oUPZw0w2ZqVvQY6pgHVaeFoNb5qKlJXJ3kAQHljfoQozoABMPYPofk1oEwlYm7EhAJbTclce%2Bf%2FoAZMNzvJ8ON5ZEOmfo2uL%2FolxkJjG6m1BCYs5fV2wPL5LgpoCr%2FDuJx2hXkju7EeaRBhFkMaruz7A8MNJj1gH%2FbEYXhm9nN5eDbK%2BJz%2FnpobT2WJZI6k9ftKvuP7KLiHtS8Xbnnc3Px%2FRMsKVlkS5uI7TbntyMUmnsZA&X-Amz-Signature=72b8d9c391e31298c2ecbfcc0d3c9e65bfb05f23d14f2d9c297aaf8b1d3c8714&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
