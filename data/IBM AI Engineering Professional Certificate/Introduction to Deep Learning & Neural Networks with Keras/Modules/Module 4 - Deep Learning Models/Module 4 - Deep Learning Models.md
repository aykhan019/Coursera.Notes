

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=2f4aadc32060be060615ca93ddc24889cd30a74138db8a73f0ca91fa6411adb8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=ab76758e032080c1af3e1bf920c547bb293d1e4920eeb93323e6cd22bcabb620&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=5380aa88475fa9666379ce31bee7543484c0910ba923890905914a40a8591b66&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=d60bd60fa60f70c7ac9d8d89868598414f3a0646d0d1ad3e1812f2e4d321222f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=db579d973b4e7d4cc4fc18901cb49875cd50e78f6767f0bd46672a396dad1f7d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=ab75e438f5c6245ba48689d04ea3979e654dd370d8cb928b50a1c3db2431be9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=0c65aee6b921479dac71bbfd2f8624435cf43860421d78fd690b587d6a258445&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=636d29941a14d4fbde0c5808962e81ab8e6e284e1c82ab80533a7f82cd0a9c39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSSGYYL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCGXzOnLSe7QTs3cHkkkt%2BQL7t%2FeLECXE3C%2BLnAjuM9VgIgKzNQF9VSKgkXeAWPy72TsJWRwrWhz0BN1molgxrsLXQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXNiOSpX7zmm17RVCrcA3mwdG03NSXwVOsw2mKwyJqHV6WaYfMK7gS2sCjN8UZj0DHKUnLgS5riV3DykEvGPziQo4lke4yd8gKNB4iCnkxgvZHL5qCffWqb5Hsrm5lakhwNHTw6LrSMXiFtNSoj8tHGB5fqgnyEbuVu5RO9oP3D2OExK7VZd86qKVaTq7Kne7OGo1w2N9ty584T5DyyGYQYDzmKGmxzNzVdmk7nCkPgWnaZWsf5TW7%2F8CFakcILGfjxGdX9%2FldWcbwPxcx%2BrSG6bKqjVRdcnM%2Fu%2FgRthEwn1EFthKkmT53usktdMNQuAqc7mTxsZXq0lnLVJBV5IZhyJB3fz3UDzZ6ZOCxB%2Fr36bCvINbhRMUJea2EwqEYyoEZh%2FpDW%2BNo0MlYqty0lB8t1elmmCDmEiDXHJvUYwivJgrY5AaA56LZTCOngj8WSWgts0EfGAIFTIQRXoonmZK0di%2FTi41ljJ8sOEX8KD2dP40J6xk1wquW1NVZe9OBbLTYTKKN2DWMqXaicx%2BTYwA%2B%2FXrAdatP2spB83t%2FAh9UlWplGsr5Lx%2FgRPQQYZDFDoG%2BMBNrp65zr2TgLWWOAIdBD%2B%2Fzw%2F1dYojceEr7k3j7byNceTpc3Gtw%2FjkmswSnhvCcX9nPHnvf9qZ%2BTMICOnL0GOqUBT0wv%2BC9vDikPGXDeaE5ZwSD71peRH4D7drglHVuGay0Q8KTFTS%2B2i1pNwXWCpFYZjHq1jSxB4X1EjSSA1UqGxGEMQhP1EeN1bMHYWtkLCUf6mkJIM7R8ynjzGnHdfuvnMIQIKbv0gB2Ft0XNKIKbhPgrMKX9DEKkH7F5yNHkNkZs0ERDV50Bqev02QtJ99LQXTDvptIqAnYmkFpay8fYJi0qJczV&X-Amz-Signature=8d966cb8c70bf212b1d0019f5807f6ee864211c4b321e590d335f0f989efc84c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CHVDX6J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDhu30oi4Aq%2FgIqFKReSkgS%2FFqs1eaE16hE0Dx0zlOVLQIgQq3ql7GNCi0DBO24rO4YBwSVUy4HRWHd8yNDKHSBRtgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEc4NNsMxpNl4xD%2BFyrcA%2FIY0FmqVogrYYhdILLtxzRqCnjPocRDf2CPbaYKMp4GwJ9iw%2Bgr2kaWtTwUSRYBY8jYe%2BoiJcvrSdkFnQ0aO6BX1JD0ITjLEvqgoz2bwdni1RLND11aDeJBaiWWsWCAbrmMMH6eUqyIJvGhxr6RLMySdKazueVKS1kEnNsPhmF3dJBp89nl1t19dLDv64G%2F2WBY9bm6X0rkKQYl4Yh25QXAxFVZKW3hdF2Oa2nRQjE0J1HAxBm3KjaFFz85k%2BTUA5nAkaAerMbc2cgT801Txlug879DBdhuO47NlQsDMywcPnuz6UhyjciP1m%2FycYtB8SwNLyShqwJbpMK15rE55M60MeJTXmQ8fPVa1NgvmwrSaRcJz1sZb62pGMZOndm6C11q6Ro59RJWAMvV%2FnTIU%2FnnQnMb7YmiBOcWUn%2BGkij%2FxTYXjfvEiE4A8ikg0%2F5jFcmNsWx544jhbwGOVk7wxzPAOP9f5gag228suuw94CKYvX%2FC3bvY3TwEaKZWWziJAOebQACqm%2F8StG8JkxUaMol8UZ2FynlbrOfH%2FYGEnS9BAjwL5N8vDQeAecuP3IXyBVC3zdObppLt1%2FDnHKsGhouXvrYcY8lk%2BGNS3HOdARaqDGKohfmcLSTncEteMPGOnL0GOqUBL27UUXxulBmBiqqPziQjclpm%2BFnhzBbCKwric9TQdfZb1njprTK2rHmY%2Bi4taoMdGJU2ZPqGIBruuAjZGJWO3jacRkFKWT7JAYdrVJx%2FG594lM9HqdGWdKW6gri2%2FILWBQQoSll4DXyyblMmKlCwIOtBHHVI8WmIil5HDj8JkeqsA0tyx6yq%2FvCtmE%2BaKdJQHspRRnIjfSvBxI0jq%2BVZerG24m2N&X-Amz-Signature=0b19bd14fd281ec8e1090ed5502f060400f442ad3f64cf488a9f02bf22998d0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CHVDX6J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDhu30oi4Aq%2FgIqFKReSkgS%2FFqs1eaE16hE0Dx0zlOVLQIgQq3ql7GNCi0DBO24rO4YBwSVUy4HRWHd8yNDKHSBRtgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEc4NNsMxpNl4xD%2BFyrcA%2FIY0FmqVogrYYhdILLtxzRqCnjPocRDf2CPbaYKMp4GwJ9iw%2Bgr2kaWtTwUSRYBY8jYe%2BoiJcvrSdkFnQ0aO6BX1JD0ITjLEvqgoz2bwdni1RLND11aDeJBaiWWsWCAbrmMMH6eUqyIJvGhxr6RLMySdKazueVKS1kEnNsPhmF3dJBp89nl1t19dLDv64G%2F2WBY9bm6X0rkKQYl4Yh25QXAxFVZKW3hdF2Oa2nRQjE0J1HAxBm3KjaFFz85k%2BTUA5nAkaAerMbc2cgT801Txlug879DBdhuO47NlQsDMywcPnuz6UhyjciP1m%2FycYtB8SwNLyShqwJbpMK15rE55M60MeJTXmQ8fPVa1NgvmwrSaRcJz1sZb62pGMZOndm6C11q6Ro59RJWAMvV%2FnTIU%2FnnQnMb7YmiBOcWUn%2BGkij%2FxTYXjfvEiE4A8ikg0%2F5jFcmNsWx544jhbwGOVk7wxzPAOP9f5gag228suuw94CKYvX%2FC3bvY3TwEaKZWWziJAOebQACqm%2F8StG8JkxUaMol8UZ2FynlbrOfH%2FYGEnS9BAjwL5N8vDQeAecuP3IXyBVC3zdObppLt1%2FDnHKsGhouXvrYcY8lk%2BGNS3HOdARaqDGKohfmcLSTncEteMPGOnL0GOqUBL27UUXxulBmBiqqPziQjclpm%2BFnhzBbCKwric9TQdfZb1njprTK2rHmY%2Bi4taoMdGJU2ZPqGIBruuAjZGJWO3jacRkFKWT7JAYdrVJx%2FG594lM9HqdGWdKW6gri2%2FILWBQQoSll4DXyyblMmKlCwIOtBHHVI8WmIil5HDj8JkeqsA0tyx6yq%2FvCtmE%2BaKdJQHspRRnIjfSvBxI0jq%2BVZerG24m2N&X-Amz-Signature=89dc4dbeac3e78ce4d4d5f79610852888947a658c52b9f2088f0fb7252dc78b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
