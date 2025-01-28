

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=031fe16c2ffd993954ba3da722048a3ae65ba6e781264cd121232a0d559cb352&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=88f55eb2e05b89a11803c92c5a6cd76aec2eaa0b8bce5d7a249ae1b5ab524f58&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=8a048ec16d98bd0fbc41cabb32051b15f2d9a4869c46c087f92c082c57fcf412&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=5a680090ce63f5695bd85feb7f18f6ae39e0126f64b2074ee0fe773e624ce659&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=951cdfec83163dc52f07c196f8bab15fe8c6496b06de827bb2e22d7f283ad9af&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=752da4b337232428289061a9f3db8c57ddb84580e4536d21e8805954e2658149&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=aa360ca7677fcff4387212b5e97a466a00b873cb35872a5194c9c0e9020959d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=0d2764124fd4ef485c25f5dcb41eda216bf0b357509ca05f27791f8fef5ba4db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4QL7X%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFzsXuZKmEYw0F%2B0tjT%2FKsfyLJOmFzbztpXl4zdRbF%2FaAiBEPUj7EylPihlaTLY5KbCEq8mBMhbuksQtHm6F6nOjpSr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM72497dgMweK6JnW4KtwDScJ0VGF%2Bmz26XMgvwxafo6esFsCsNZolt0QmlmlW1Q6jRLCH%2FbwifOd6%2BaZck%2B3hWH1v%2FF04HFsT4A7pMM5ENhzpT%2FAr%2Fk3IWne7zA5IsPsKDe7jA5OnvM%2FXMWx2Dk3yY5eGluUdrBsuekeVrZsaTG5xVVGpAAyC4kGcaibwY%2BGEByrc4e11h%2FTQERki%2BjrZoGL6IW%2Fix154lUD3SkAKcgs96YHpKFJGuKHPq6YW5hTVevx6vTR%2BM%2FhR5TH35wi91NA0W8cfXiVeUu5tTHE52qwVWUhm291ETx6aqnfStQXlrzCyn3DA0jGILDwwpYCw39NqOv521QcBDdaW4%2FJg4BrGrOn%2FpkQy4aDLfyXTjfB7VfQiJfUbAWMkuKb8%2Bw5m9PFWG25Za5MXEXXGjK08%2BTxmyQ9%2BQbrPAHcX8dv%2FcU%2Fsc7WLzWT58IBIhBq5a8diBaPgAzlc%2Fj5i6hnuMaL93EUyueH9kJrBMeUJ9sv6KDu6SpsLiseAOe9lWWSE79ju1iJirF3pqVU63dMC9gyItSL1M7vKDtpFM%2Bpb1BbwzNJ3bv9plXk%2Bt39YkJaOegPUN24hmDDt6cxPqcGmYTIkdGSZVejhMdmd3DsRVVyQTrGww%2F3XvnCri1bfIVcw3ZTlvAY6pgGCaK9LCMmFH%2BVI1o50vYasr7TGcJZ4D9ZZ5MnKddkwio%2FqE8VZ%2Fbdg58JPCa%2FOU20vtAL7O2QiVJhP2pEqFnSlWUERYsslTlXqaKQP%2Fspmp%2FmwQOlEy9WHMYOARzj%2Fqyia06BotTE%2FAVDqkhWY%2BrLzHS8JY8e18EU9cNjVAJ%2FsFq92AGX2dzHaudDNZ9fpzvVSQcNWk%2FHeGQMe7jGu4zzZk4tM6i%2Ba&X-Amz-Signature=fa5d162523ad98a5a23b5cbb746e0189c2ad9e148eec3b47f35ce4494dd049da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7STBPOM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIGqERo7iYsoQxL5O%2BKm47dX%2B3Ci%2Bf83dDEJohxGGze8fAiEAyWOaAmy0TVtjJMEhInSCPdAAbOssFrmpBOmKqv94Po4q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDJmY4IEbzBh9zIuSOSrcA5oZKlzfdxMU75x%2F0cK%2B4Aa03YE6Xot8lv7qwmf%2Bgj9QdjQSUlFtxo9xDtrGHPSIm%2F7QtqQDWgNJVVwqNyfjmvubX4J0Oo3d4KZ358bKZdIFHDlaEmeiqKCtBnvg2GbuiQLu1eqMld8s%2B2mtpEOD9ZJvoiAfXriEASyXP96ffKo41Of9cQEfdm80lqcvauAedsC345%2BvFhwMVD1qDR8EZxnx1cjRiUHm6TAtxXu2XTFn37o%2BhePZZp7vMQIHRNuc%2FcnlttRbr8KcTJpmfm1%2FaCONoarD44F4ACHg7efmqCNUw5v%2FqPs5V9VKN1e%2BBQ%2Fip9Xd7%2Bo3DIbPhlMhLdNPsfJOVdi74%2Bn2QnakrROaTqwvsC2Nx2K38ueggdQgIK51IYVNpClUogXpPPi%2FXhYudY4bjijlUGetFEjk6c%2BOj4GeYOGmhs6NEGlAmYG1hCUO4geavTq5LeqNJpZgPGsxdJoF0NTXV4Xw9H9a3efDp35jEVmjA%2F9dzMWoJ0nnll9TwPVfRBX2e8hzzJ69TVU4Ldu2nLuQ4dO%2B5nPA93UijIPGk44QJD0tF88froNlRhJ1k3gpiY805bv9vgavSl4vjnt0RR8MnXzHg6%2FWu5tJckcs5aQNkGd%2F8m%2FQvERpMIOV5bwGOqUBdh%2B6lty9HQMxEQ8i%2FDfmQvNq5jIvyMoNPssJNHu%2BLSp8jJnlbtfE18plnx5fEOJZwQAXUYVySUHbQgZlPcv5yTfS4J%2BE9NdDbouFAaCuFJ%2BuohumQ4aLhpH0gK2NIStK21tfPp2iwyo7z5PxZaWt8%2B%2FGedjk6eM3qN1Bfz87qusD%2BgjgLCRlNwEfoZC0gc7vWRa0oHir951oKsRhanXY92Q7%2FKo0&X-Amz-Signature=8554a4628ec69a30fdf69d2f6aa75da78b16e32922d626f9f3670a50bb99f4b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7STBPOM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIGqERo7iYsoQxL5O%2BKm47dX%2B3Ci%2Bf83dDEJohxGGze8fAiEAyWOaAmy0TVtjJMEhInSCPdAAbOssFrmpBOmKqv94Po4q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDJmY4IEbzBh9zIuSOSrcA5oZKlzfdxMU75x%2F0cK%2B4Aa03YE6Xot8lv7qwmf%2Bgj9QdjQSUlFtxo9xDtrGHPSIm%2F7QtqQDWgNJVVwqNyfjmvubX4J0Oo3d4KZ358bKZdIFHDlaEmeiqKCtBnvg2GbuiQLu1eqMld8s%2B2mtpEOD9ZJvoiAfXriEASyXP96ffKo41Of9cQEfdm80lqcvauAedsC345%2BvFhwMVD1qDR8EZxnx1cjRiUHm6TAtxXu2XTFn37o%2BhePZZp7vMQIHRNuc%2FcnlttRbr8KcTJpmfm1%2FaCONoarD44F4ACHg7efmqCNUw5v%2FqPs5V9VKN1e%2BBQ%2Fip9Xd7%2Bo3DIbPhlMhLdNPsfJOVdi74%2Bn2QnakrROaTqwvsC2Nx2K38ueggdQgIK51IYVNpClUogXpPPi%2FXhYudY4bjijlUGetFEjk6c%2BOj4GeYOGmhs6NEGlAmYG1hCUO4geavTq5LeqNJpZgPGsxdJoF0NTXV4Xw9H9a3efDp35jEVmjA%2F9dzMWoJ0nnll9TwPVfRBX2e8hzzJ69TVU4Ldu2nLuQ4dO%2B5nPA93UijIPGk44QJD0tF88froNlRhJ1k3gpiY805bv9vgavSl4vjnt0RR8MnXzHg6%2FWu5tJckcs5aQNkGd%2F8m%2FQvERpMIOV5bwGOqUBdh%2B6lty9HQMxEQ8i%2FDfmQvNq5jIvyMoNPssJNHu%2BLSp8jJnlbtfE18plnx5fEOJZwQAXUYVySUHbQgZlPcv5yTfS4J%2BE9NdDbouFAaCuFJ%2BuohumQ4aLhpH0gK2NIStK21tfPp2iwyo7z5PxZaWt8%2B%2FGedjk6eM3qN1Bfz87qusD%2BgjgLCRlNwEfoZC0gc7vWRa0oHir951oKsRhanXY92Q7%2FKo0&X-Amz-Signature=33a6152d23b820481cc56f318ea2c231501f278a2587d9e98e66115916f00801&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
