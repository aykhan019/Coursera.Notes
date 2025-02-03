

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=8698ffdcf0d00fd5811e6926aff53669d56ddee923a1c0a139e24a9c26dbe37c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=5d6d699e828c3efd91f5caca3a21c7b68a0be5baa5c9d6e4892f1fb8ae255c39&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=e18040b18450caed3f8b54d8bd964082c4a32946568b3790ae7f74956e3761de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=cee5e6331c5f6364598d3ca7d97d7cf01605c21635e82f4080531122e52dfe65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=3b72720302ee0ac2864ad5387d78582ebd539d353dd86ee10f0eb8dd8236de67&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=81e7573a539ee04d3ffc048b37b5987f4af805ea3b1b940de27f48b15e2448b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=1eb8ed90dc88a770be0c84e57d4cf62c394df825361f3145252a1c47bdca60f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=acf0f48a6b011e2cd53303a20a0840b63a7cf03a3135483b3b3e1493aec5d2fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2XX6XJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCID147pG4%2BpxD25AYkSNPGC%2FGzo9VP5wAHQyeRM%2Bp5owZAiAinMcCJ%2Fa0jRK%2BpQClCSjJHlpjSojxjVDSA%2Brm8RdYQCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMuQysS%2BZ56ySqbIQAKtwDZUW33xqswh4l4QYZLdgKsgkfx0Y%2F55kFGjdDmsNKl9HUY8J5ckoLXSNSehPmADs0EmeeW7K4Wx%2B3dE0Uzo3Fcf9SQavhs8h8lesJzG4wPahtEH8K%2BzgNfJ5mWcfL9VJYR1KIiUntjzv8JuSksCOSMKHYhDxXIPaYUc6CLpazFok3zpr%2FL%2BHAbENqL5E%2FTKaLFakvzy4O9I4zsHJU6EgBCzj4MkgHaFnJszkmo96nfSEfpN8w2m4o41hkhX3mVg3j2vDXTUABBiPvtfK%2BLw3rSevMaJk0%2FW1lFP6e1FTpcRytv%2FuJ8VpLFUT2vwRThxyVeHCt85o9HrmLhjRrAJu4GiFDrlc%2BsAaRJu2laPETiiaHq7R8mEkPsLGmW0yk3PvMY%2Br8TDDnzpqru4egDSkYQTlFuGp7OkKQwINA8%2FqG0G05YTSlPwXxurWxEU7092WFpC6EWGDejX1nfXd26ujI3ZXtB2oRGAMvIdJJ%2FzD8cGS3HOtlVOFpd362i24gkmjP0nStLoPsXIOu3%2FJmjQS2Q%2BU8YlsigFFyanWHTmwOoErKh6Lr0NiS9qnSjnlYPzPF6Z5iSN5e50wtW%2FGnS1AE3OjD9tspKoj85BpqH%2Bm1w8nEvoM5puXCKROVZMkwt%2BaDvQY6pgHKIotbOcGew6Ehw03Eo089MtwOs%2BXfyAmM91Hv9thBz8wxEv77g2SzCE6CgRTLuphMSFp%2FNunlhvXCZhvrOU5mNNUhnKZeFaJ3d29VEeniVzK4JLgA8fVJCzyzRinkEIjVrOprtkYL30ZDcGRbmjPK%2Fl8iqiKj2gAyT2hPHXAmiXQglGlqOto7fxUTnzUo6IQomiKMC%2ByJVQWxr697AkOL%2FL3%2BPKXp&X-Amz-Signature=ce80b8e5bf8cbffe3391257bccf4d0d9f2b4354e28834c1ee7af357b3dafac44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKGFITQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQCLaBUpmldYqvP%2Fi%2BGRgvkUb9h2anikvXFWBzZQhMFcEQIgIn9nP%2BEcuz2hmQJKLwzZEjoIlN6PGxQ%2BeuzmQ1xgvO4q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIM%2Fkvo6pSQ7ryVjrSrcA8HJahKMiNy%2Fh6%2BZrSbFa8QRf7feGMneljewvAKzu6d%2BVyq%2FtC6MGBd6lnJtRFKdrNsc5I7sGrqOhZXa1e2trPg7rKm5AFoLFRdmZq2MBMQFBHkd1MCi9pMXldaTCDs01DXfs33jRuTFZF33P6jzXotyuoUGwmDm%2Bi%2BDrx2tf0pFF%2BTIW5YVhydP%2FCbcR19apmb5gF8tfNO2NBjDWR2gT2iytcquWBoxiuHzKh2t0I6g%2BVU80l94DrPXsLRVSXSVHh7dZHBcCGB5AFROzS4NmaR7ALwX%2Fe25bP2IKzLtLOufnDBLM4PW1c7oaDpGZEGqhcIbC5xoic%2BPsF3DhY6ysz1wKwx0vYjXNH5KNyA832gUENh5uVzoQ3nXMwopTGEeRClVmOoRWNuUblqGjeVNg1rnFL%2F0HrSYqy3cNz3iqjUrUvOz0WkBeVjCrkWrSnqpKqtrMRq6YG8LYULGLPevrewVt59OfBWVzg%2FWHeWFY%2FaWRm1HTzscvY%2F8lRSwkoZeflj5jVBHvTQ1qiCHchiWqCEQGgRfk451olQisq1HZJZxuWopwwtT7YjgfvFIOiORczHUVIDNNiZrx3HJthdnApMHCPtK5acSAiuc%2BA%2FLyQ4Snw0Cs1KXXSyqUA5HMPnng70GOqUBanhdK04AqlFNFib3j14lY7QNjiq%2BqUwKdG06tJHhY43bjNJTJ1ztqF8gMPTcj6RDz%2FnG7cgWpOhBnFOCrke7UKCCOObBuR7RhoY9XLL6NINlBd2i6bBIFIoJDrFNrM9G70q10vmoNLL886lK%2B0HiA53F1Xg8Txy%2F3Kg1GdYx8PdYRTi%2B77hPGBQGsvAga%2FIiMC679pFt4aM1okktAoes2bziEWLe&X-Amz-Signature=bbfc08e102e2c02ec331ab47ded674306281e2d14bb08a5bee7cca2ed6fdce99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKGFITQQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQCLaBUpmldYqvP%2Fi%2BGRgvkUb9h2anikvXFWBzZQhMFcEQIgIn9nP%2BEcuz2hmQJKLwzZEjoIlN6PGxQ%2BeuzmQ1xgvO4q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDIM%2Fkvo6pSQ7ryVjrSrcA8HJahKMiNy%2Fh6%2BZrSbFa8QRf7feGMneljewvAKzu6d%2BVyq%2FtC6MGBd6lnJtRFKdrNsc5I7sGrqOhZXa1e2trPg7rKm5AFoLFRdmZq2MBMQFBHkd1MCi9pMXldaTCDs01DXfs33jRuTFZF33P6jzXotyuoUGwmDm%2Bi%2BDrx2tf0pFF%2BTIW5YVhydP%2FCbcR19apmb5gF8tfNO2NBjDWR2gT2iytcquWBoxiuHzKh2t0I6g%2BVU80l94DrPXsLRVSXSVHh7dZHBcCGB5AFROzS4NmaR7ALwX%2Fe25bP2IKzLtLOufnDBLM4PW1c7oaDpGZEGqhcIbC5xoic%2BPsF3DhY6ysz1wKwx0vYjXNH5KNyA832gUENh5uVzoQ3nXMwopTGEeRClVmOoRWNuUblqGjeVNg1rnFL%2F0HrSYqy3cNz3iqjUrUvOz0WkBeVjCrkWrSnqpKqtrMRq6YG8LYULGLPevrewVt59OfBWVzg%2FWHeWFY%2FaWRm1HTzscvY%2F8lRSwkoZeflj5jVBHvTQ1qiCHchiWqCEQGgRfk451olQisq1HZJZxuWopwwtT7YjgfvFIOiORczHUVIDNNiZrx3HJthdnApMHCPtK5acSAiuc%2BA%2FLyQ4Snw0Cs1KXXSyqUA5HMPnng70GOqUBanhdK04AqlFNFib3j14lY7QNjiq%2BqUwKdG06tJHhY43bjNJTJ1ztqF8gMPTcj6RDz%2FnG7cgWpOhBnFOCrke7UKCCOObBuR7RhoY9XLL6NINlBd2i6bBIFIoJDrFNrM9G70q10vmoNLL886lK%2B0HiA53F1Xg8Txy%2F3Kg1GdYx8PdYRTi%2B77hPGBQGsvAga%2FIiMC679pFt4aM1okktAoes2bziEWLe&X-Amz-Signature=5a7dd0ada101e8cd99647e47d878ad5399664fa30e70c4285b4c04ca27a34f07&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
