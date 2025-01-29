

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZULM7O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk9ZXf8%2FvlkvkH7pkyAy1c2iGuFVRiTHVWxjEdmw0YbAiEAhonELmLcPDnzpkcnn5X4ftiGU70V73Z7dxXXg4IB0cMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhiiQplXuIZ8jOcJSrcA3%2FNrhLC2AUtPWXHFpjRh4gUBPMVzDglRRS2s9AySgmKGTj9puyxzHr%2BKVzR5s6fUvKwy2ojx1KsRhv9Bpt3qAS57bljcN3ta1Fjrm5FQOzdog4T74v%2FfNs5AG71P0jbqzm%2BpXQdVQrnfRmzYRhhb3XL7orNA8cpAe4GSsR7pkLxm4xE7cPlH6cAxwySk037y0hnQvc90ALBeES35RNoOAV%2Fwu4tsBxZxaBMJAsmkTXPny2AaxgFi%2BY2ceuU5TlO2JSoA5mxs6nu4KW7aE6M1kFbKTSm%2Bu4W%2FJytgAPu%2F4xL8ftx%2BlXkShVxIG7HcOe4RIGNIifTrn3D4nyVHYMvEpDQc3nvOWGjv%2B4sh3hFAyjPV8Qw3dLL2pzgJSOWh5L5kHbtxMGpRwvT%2F%2FdibhgxMvNPTmXuM8skneMW4y%2Bysj5cQR7Tq%2BN%2BjkXYPf23MU8xRPdWmaNH8jlyiPH%2FbqeuKTDwZebURJb0vaNaAA53QsCXyxv2bg3Q4LIH9Xu7unkm1yRw9bCgpqklGjLM4qe9VelX884ahRElyS3CvILOTVYV8bRH8mfL8O%2BjbOQWgblfMyIIosyWXRUV4o2s4NtSwNFgigxzsQIYcRJO0hSsIWWw%2BETHX%2FcmsYWeytczMJnj57wGOqUBTd%2FAVhpdeQsc8xosJQw2q974c%2B7C6ElsxnOIAFT02maE%2FbgAqWhhgyddidPh07GxPYEio70gOLuFebsejdyoTd4cMcSRg0W%2FpsfKmEwq5WqvconJx7s3M6ccbt1srZIzm2Wo46t9OsMX%2Bi7TTeeZO98aHRwYUhZ%2FfUHLyYLKqhDGXVE6gNjaOCk5POmbYcvOMLVke1b0HVnS6GEznxsBhSnp7FoR&X-Amz-Signature=e0c5da5debe7f104dfc33eb62f7a190ca8f6b7d9dfdedfc5a8559c5d32607dc2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GK4KYD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmIl4MzwM%2B4KiYkzHPFRPIKQelBINc0dYjJP%2Bu4nOXLAiAH3uTemSAErAxzVAm%2BpvPgrnexMexR9RcXk9GbBZZMviqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeByMA%2BWiswLtI03kKtwD7aoTQbQ%2BcmIqh11hpgtDl%2FLsXJkCuS%2FYo2RcbKDT4NzcfCa3%2Fu0Jv3vQlwhMkwPnfE6xKd7kLszBPFg0UYK6JMVqMPEjuweWQSWrodF37joz5A5g%2FLtL4KfdHPbHJtfPuKQsGOXrpXyoKc76sIZlBbQAtXEV8PUTaIxNkp4qJSARo5ktSGuhkeQbYL%2BaS5OHhtFI6pzUZyJeOtTmjf%2F8OePY%2FjYwqKUFCq2oRVpIZ6yXEguB2ZBjDJE624uVLhTx3kEWxIkAIY5TCrSdsbYXy4eE8vz1jZCqeBfpXrvaPQVfA2EaHk7ujO1l2oJ06Uy%2FiycxAS%2FZ%2BxS3hLncFI8EPqYRGUIrUK%2F7Y0jicOm7LUT3diwOUQU7g7Me8UC0HYcEnI93fRHdfhlV0J0zOnSe%2BPLUsI%2F1Px3gAB7FjjeQVh0mXcurD5X9ag1c5VP7hh99qBR4nUgmEMAoDlq0uet9CHrqio3YVLK9fSlRJzHF4ZGtzSvzv3hsjm5k6axa5iAbq6UpoV4NXd4VQvz3AcxYXndqVwBwn84yW%2Ft6dOjHUa5I3tGKdbOTzA8tta2%2BpFFrx7yinQqtWjb4VE13NvSG1daclJ8kl%2BbxFsvIBKnvDDq1s3JVUmLDDGvNfrowy%2F7nvAY6pgH8WA3SAVqSeMVS%2BqKw7p8XTTOFsJZN7XY0rapRTwkP2sv71aTlzcOsJChoGjAMPY1TUQ3CYxotl6rdQR3QdvxgRhSkEE1JsVwSCPtb6eamTmxRp6xtWSeKTgSHqVveBqh56apr5vkjFSv%2Fty4j0usG7Sdid0saSAVzcotIx963W6CscWKCD%2FNJQKvgNgcuCaFaN2cpctXd8JKm5EBcfnzOmmG2a5Ny&X-Amz-Signature=5e623c0bbaf43f7648382ac8acd87f2aae284725aacb5ff92035846833d65936&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GK4KYD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmIl4MzwM%2B4KiYkzHPFRPIKQelBINc0dYjJP%2Bu4nOXLAiAH3uTemSAErAxzVAm%2BpvPgrnexMexR9RcXk9GbBZZMviqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeByMA%2BWiswLtI03kKtwD7aoTQbQ%2BcmIqh11hpgtDl%2FLsXJkCuS%2FYo2RcbKDT4NzcfCa3%2Fu0Jv3vQlwhMkwPnfE6xKd7kLszBPFg0UYK6JMVqMPEjuweWQSWrodF37joz5A5g%2FLtL4KfdHPbHJtfPuKQsGOXrpXyoKc76sIZlBbQAtXEV8PUTaIxNkp4qJSARo5ktSGuhkeQbYL%2BaS5OHhtFI6pzUZyJeOtTmjf%2F8OePY%2FjYwqKUFCq2oRVpIZ6yXEguB2ZBjDJE624uVLhTx3kEWxIkAIY5TCrSdsbYXy4eE8vz1jZCqeBfpXrvaPQVfA2EaHk7ujO1l2oJ06Uy%2FiycxAS%2FZ%2BxS3hLncFI8EPqYRGUIrUK%2F7Y0jicOm7LUT3diwOUQU7g7Me8UC0HYcEnI93fRHdfhlV0J0zOnSe%2BPLUsI%2F1Px3gAB7FjjeQVh0mXcurD5X9ag1c5VP7hh99qBR4nUgmEMAoDlq0uet9CHrqio3YVLK9fSlRJzHF4ZGtzSvzv3hsjm5k6axa5iAbq6UpoV4NXd4VQvz3AcxYXndqVwBwn84yW%2Ft6dOjHUa5I3tGKdbOTzA8tta2%2BpFFrx7yinQqtWjb4VE13NvSG1daclJ8kl%2BbxFsvIBKnvDDq1s3JVUmLDDGvNfrowy%2F7nvAY6pgH8WA3SAVqSeMVS%2BqKw7p8XTTOFsJZN7XY0rapRTwkP2sv71aTlzcOsJChoGjAMPY1TUQ3CYxotl6rdQR3QdvxgRhSkEE1JsVwSCPtb6eamTmxRp6xtWSeKTgSHqVveBqh56apr5vkjFSv%2Fty4j0usG7Sdid0saSAVzcotIx963W6CscWKCD%2FNJQKvgNgcuCaFaN2cpctXd8JKm5EBcfnzOmmG2a5Ny&X-Amz-Signature=267856cb327766f71dc8f558a7cc79224491c66c908b810a02e7f5ed5e6885d6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GK4KYD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmIl4MzwM%2B4KiYkzHPFRPIKQelBINc0dYjJP%2Bu4nOXLAiAH3uTemSAErAxzVAm%2BpvPgrnexMexR9RcXk9GbBZZMviqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeByMA%2BWiswLtI03kKtwD7aoTQbQ%2BcmIqh11hpgtDl%2FLsXJkCuS%2FYo2RcbKDT4NzcfCa3%2Fu0Jv3vQlwhMkwPnfE6xKd7kLszBPFg0UYK6JMVqMPEjuweWQSWrodF37joz5A5g%2FLtL4KfdHPbHJtfPuKQsGOXrpXyoKc76sIZlBbQAtXEV8PUTaIxNkp4qJSARo5ktSGuhkeQbYL%2BaS5OHhtFI6pzUZyJeOtTmjf%2F8OePY%2FjYwqKUFCq2oRVpIZ6yXEguB2ZBjDJE624uVLhTx3kEWxIkAIY5TCrSdsbYXy4eE8vz1jZCqeBfpXrvaPQVfA2EaHk7ujO1l2oJ06Uy%2FiycxAS%2FZ%2BxS3hLncFI8EPqYRGUIrUK%2F7Y0jicOm7LUT3diwOUQU7g7Me8UC0HYcEnI93fRHdfhlV0J0zOnSe%2BPLUsI%2F1Px3gAB7FjjeQVh0mXcurD5X9ag1c5VP7hh99qBR4nUgmEMAoDlq0uet9CHrqio3YVLK9fSlRJzHF4ZGtzSvzv3hsjm5k6axa5iAbq6UpoV4NXd4VQvz3AcxYXndqVwBwn84yW%2Ft6dOjHUa5I3tGKdbOTzA8tta2%2BpFFrx7yinQqtWjb4VE13NvSG1daclJ8kl%2BbxFsvIBKnvDDq1s3JVUmLDDGvNfrowy%2F7nvAY6pgH8WA3SAVqSeMVS%2BqKw7p8XTTOFsJZN7XY0rapRTwkP2sv71aTlzcOsJChoGjAMPY1TUQ3CYxotl6rdQR3QdvxgRhSkEE1JsVwSCPtb6eamTmxRp6xtWSeKTgSHqVveBqh56apr5vkjFSv%2Fty4j0usG7Sdid0saSAVzcotIx963W6CscWKCD%2FNJQKvgNgcuCaFaN2cpctXd8JKm5EBcfnzOmmG2a5Ny&X-Amz-Signature=494aae262f40c3befc765bdb33200e8c9e0c1dbc432a40eb75b35404ba225e1e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GK4KYD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmIl4MzwM%2B4KiYkzHPFRPIKQelBINc0dYjJP%2Bu4nOXLAiAH3uTemSAErAxzVAm%2BpvPgrnexMexR9RcXk9GbBZZMviqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeByMA%2BWiswLtI03kKtwD7aoTQbQ%2BcmIqh11hpgtDl%2FLsXJkCuS%2FYo2RcbKDT4NzcfCa3%2Fu0Jv3vQlwhMkwPnfE6xKd7kLszBPFg0UYK6JMVqMPEjuweWQSWrodF37joz5A5g%2FLtL4KfdHPbHJtfPuKQsGOXrpXyoKc76sIZlBbQAtXEV8PUTaIxNkp4qJSARo5ktSGuhkeQbYL%2BaS5OHhtFI6pzUZyJeOtTmjf%2F8OePY%2FjYwqKUFCq2oRVpIZ6yXEguB2ZBjDJE624uVLhTx3kEWxIkAIY5TCrSdsbYXy4eE8vz1jZCqeBfpXrvaPQVfA2EaHk7ujO1l2oJ06Uy%2FiycxAS%2FZ%2BxS3hLncFI8EPqYRGUIrUK%2F7Y0jicOm7LUT3diwOUQU7g7Me8UC0HYcEnI93fRHdfhlV0J0zOnSe%2BPLUsI%2F1Px3gAB7FjjeQVh0mXcurD5X9ag1c5VP7hh99qBR4nUgmEMAoDlq0uet9CHrqio3YVLK9fSlRJzHF4ZGtzSvzv3hsjm5k6axa5iAbq6UpoV4NXd4VQvz3AcxYXndqVwBwn84yW%2Ft6dOjHUa5I3tGKdbOTzA8tta2%2BpFFrx7yinQqtWjb4VE13NvSG1daclJ8kl%2BbxFsvIBKnvDDq1s3JVUmLDDGvNfrowy%2F7nvAY6pgH8WA3SAVqSeMVS%2BqKw7p8XTTOFsJZN7XY0rapRTwkP2sv71aTlzcOsJChoGjAMPY1TUQ3CYxotl6rdQR3QdvxgRhSkEE1JsVwSCPtb6eamTmxRp6xtWSeKTgSHqVveBqh56apr5vkjFSv%2Fty4j0usG7Sdid0saSAVzcotIx963W6CscWKCD%2FNJQKvgNgcuCaFaN2cpctXd8JKm5EBcfnzOmmG2a5Ny&X-Amz-Signature=d3da3941610fbceec2522dab892534b6c35e0977e6c66bb82daa454df29c9151&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GK4KYD6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmIl4MzwM%2B4KiYkzHPFRPIKQelBINc0dYjJP%2Bu4nOXLAiAH3uTemSAErAxzVAm%2BpvPgrnexMexR9RcXk9GbBZZMviqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeByMA%2BWiswLtI03kKtwD7aoTQbQ%2BcmIqh11hpgtDl%2FLsXJkCuS%2FYo2RcbKDT4NzcfCa3%2Fu0Jv3vQlwhMkwPnfE6xKd7kLszBPFg0UYK6JMVqMPEjuweWQSWrodF37joz5A5g%2FLtL4KfdHPbHJtfPuKQsGOXrpXyoKc76sIZlBbQAtXEV8PUTaIxNkp4qJSARo5ktSGuhkeQbYL%2BaS5OHhtFI6pzUZyJeOtTmjf%2F8OePY%2FjYwqKUFCq2oRVpIZ6yXEguB2ZBjDJE624uVLhTx3kEWxIkAIY5TCrSdsbYXy4eE8vz1jZCqeBfpXrvaPQVfA2EaHk7ujO1l2oJ06Uy%2FiycxAS%2FZ%2BxS3hLncFI8EPqYRGUIrUK%2F7Y0jicOm7LUT3diwOUQU7g7Me8UC0HYcEnI93fRHdfhlV0J0zOnSe%2BPLUsI%2F1Px3gAB7FjjeQVh0mXcurD5X9ag1c5VP7hh99qBR4nUgmEMAoDlq0uet9CHrqio3YVLK9fSlRJzHF4ZGtzSvzv3hsjm5k6axa5iAbq6UpoV4NXd4VQvz3AcxYXndqVwBwn84yW%2Ft6dOjHUa5I3tGKdbOTzA8tta2%2BpFFrx7yinQqtWjb4VE13NvSG1daclJ8kl%2BbxFsvIBKnvDDq1s3JVUmLDDGvNfrowy%2F7nvAY6pgH8WA3SAVqSeMVS%2BqKw7p8XTTOFsJZN7XY0rapRTwkP2sv71aTlzcOsJChoGjAMPY1TUQ3CYxotl6rdQR3QdvxgRhSkEE1JsVwSCPtb6eamTmxRp6xtWSeKTgSHqVveBqh56apr5vkjFSv%2Fty4j0usG7Sdid0saSAVzcotIx963W6CscWKCD%2FNJQKvgNgcuCaFaN2cpctXd8JKm5EBcfnzOmmG2a5Ny&X-Amz-Signature=5f9d39a51af05a92be280feade21290bbf824bdfb408441655741f47cb94c82b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZULM7O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk9ZXf8%2FvlkvkH7pkyAy1c2iGuFVRiTHVWxjEdmw0YbAiEAhonELmLcPDnzpkcnn5X4ftiGU70V73Z7dxXXg4IB0cMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhiiQplXuIZ8jOcJSrcA3%2FNrhLC2AUtPWXHFpjRh4gUBPMVzDglRRS2s9AySgmKGTj9puyxzHr%2BKVzR5s6fUvKwy2ojx1KsRhv9Bpt3qAS57bljcN3ta1Fjrm5FQOzdog4T74v%2FfNs5AG71P0jbqzm%2BpXQdVQrnfRmzYRhhb3XL7orNA8cpAe4GSsR7pkLxm4xE7cPlH6cAxwySk037y0hnQvc90ALBeES35RNoOAV%2Fwu4tsBxZxaBMJAsmkTXPny2AaxgFi%2BY2ceuU5TlO2JSoA5mxs6nu4KW7aE6M1kFbKTSm%2Bu4W%2FJytgAPu%2F4xL8ftx%2BlXkShVxIG7HcOe4RIGNIifTrn3D4nyVHYMvEpDQc3nvOWGjv%2B4sh3hFAyjPV8Qw3dLL2pzgJSOWh5L5kHbtxMGpRwvT%2F%2FdibhgxMvNPTmXuM8skneMW4y%2Bysj5cQR7Tq%2BN%2BjkXYPf23MU8xRPdWmaNH8jlyiPH%2FbqeuKTDwZebURJb0vaNaAA53QsCXyxv2bg3Q4LIH9Xu7unkm1yRw9bCgpqklGjLM4qe9VelX884ahRElyS3CvILOTVYV8bRH8mfL8O%2BjbOQWgblfMyIIosyWXRUV4o2s4NtSwNFgigxzsQIYcRJO0hSsIWWw%2BETHX%2FcmsYWeytczMJnj57wGOqUBTd%2FAVhpdeQsc8xosJQw2q974c%2B7C6ElsxnOIAFT02maE%2FbgAqWhhgyddidPh07GxPYEio70gOLuFebsejdyoTd4cMcSRg0W%2FpsfKmEwq5WqvconJx7s3M6ccbt1srZIzm2Wo46t9OsMX%2Bi7TTeeZO98aHRwYUhZ%2FfUHLyYLKqhDGXVE6gNjaOCk5POmbYcvOMLVke1b0HVnS6GEznxsBhSnp7FoR&X-Amz-Signature=78b95c29d6c9d7038afb188875ac9ef590bf741bc4fdccef87eec9b16dae2a4c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZULM7O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk9ZXf8%2FvlkvkH7pkyAy1c2iGuFVRiTHVWxjEdmw0YbAiEAhonELmLcPDnzpkcnn5X4ftiGU70V73Z7dxXXg4IB0cMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhiiQplXuIZ8jOcJSrcA3%2FNrhLC2AUtPWXHFpjRh4gUBPMVzDglRRS2s9AySgmKGTj9puyxzHr%2BKVzR5s6fUvKwy2ojx1KsRhv9Bpt3qAS57bljcN3ta1Fjrm5FQOzdog4T74v%2FfNs5AG71P0jbqzm%2BpXQdVQrnfRmzYRhhb3XL7orNA8cpAe4GSsR7pkLxm4xE7cPlH6cAxwySk037y0hnQvc90ALBeES35RNoOAV%2Fwu4tsBxZxaBMJAsmkTXPny2AaxgFi%2BY2ceuU5TlO2JSoA5mxs6nu4KW7aE6M1kFbKTSm%2Bu4W%2FJytgAPu%2F4xL8ftx%2BlXkShVxIG7HcOe4RIGNIifTrn3D4nyVHYMvEpDQc3nvOWGjv%2B4sh3hFAyjPV8Qw3dLL2pzgJSOWh5L5kHbtxMGpRwvT%2F%2FdibhgxMvNPTmXuM8skneMW4y%2Bysj5cQR7Tq%2BN%2BjkXYPf23MU8xRPdWmaNH8jlyiPH%2FbqeuKTDwZebURJb0vaNaAA53QsCXyxv2bg3Q4LIH9Xu7unkm1yRw9bCgpqklGjLM4qe9VelX884ahRElyS3CvILOTVYV8bRH8mfL8O%2BjbOQWgblfMyIIosyWXRUV4o2s4NtSwNFgigxzsQIYcRJO0hSsIWWw%2BETHX%2FcmsYWeytczMJnj57wGOqUBTd%2FAVhpdeQsc8xosJQw2q974c%2B7C6ElsxnOIAFT02maE%2FbgAqWhhgyddidPh07GxPYEio70gOLuFebsejdyoTd4cMcSRg0W%2FpsfKmEwq5WqvconJx7s3M6ccbt1srZIzm2Wo46t9OsMX%2Bi7TTeeZO98aHRwYUhZ%2FfUHLyYLKqhDGXVE6gNjaOCk5POmbYcvOMLVke1b0HVnS6GEznxsBhSnp7FoR&X-Amz-Signature=e2ce55b16cb6a7b40b394cdbfb5b315192edd66d34f2acb0af56c8ada23220a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZULM7O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk9ZXf8%2FvlkvkH7pkyAy1c2iGuFVRiTHVWxjEdmw0YbAiEAhonELmLcPDnzpkcnn5X4ftiGU70V73Z7dxXXg4IB0cMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhiiQplXuIZ8jOcJSrcA3%2FNrhLC2AUtPWXHFpjRh4gUBPMVzDglRRS2s9AySgmKGTj9puyxzHr%2BKVzR5s6fUvKwy2ojx1KsRhv9Bpt3qAS57bljcN3ta1Fjrm5FQOzdog4T74v%2FfNs5AG71P0jbqzm%2BpXQdVQrnfRmzYRhhb3XL7orNA8cpAe4GSsR7pkLxm4xE7cPlH6cAxwySk037y0hnQvc90ALBeES35RNoOAV%2Fwu4tsBxZxaBMJAsmkTXPny2AaxgFi%2BY2ceuU5TlO2JSoA5mxs6nu4KW7aE6M1kFbKTSm%2Bu4W%2FJytgAPu%2F4xL8ftx%2BlXkShVxIG7HcOe4RIGNIifTrn3D4nyVHYMvEpDQc3nvOWGjv%2B4sh3hFAyjPV8Qw3dLL2pzgJSOWh5L5kHbtxMGpRwvT%2F%2FdibhgxMvNPTmXuM8skneMW4y%2Bysj5cQR7Tq%2BN%2BjkXYPf23MU8xRPdWmaNH8jlyiPH%2FbqeuKTDwZebURJb0vaNaAA53QsCXyxv2bg3Q4LIH9Xu7unkm1yRw9bCgpqklGjLM4qe9VelX884ahRElyS3CvILOTVYV8bRH8mfL8O%2BjbOQWgblfMyIIosyWXRUV4o2s4NtSwNFgigxzsQIYcRJO0hSsIWWw%2BETHX%2FcmsYWeytczMJnj57wGOqUBTd%2FAVhpdeQsc8xosJQw2q974c%2B7C6ElsxnOIAFT02maE%2FbgAqWhhgyddidPh07GxPYEio70gOLuFebsejdyoTd4cMcSRg0W%2FpsfKmEwq5WqvconJx7s3M6ccbt1srZIzm2Wo46t9OsMX%2Bi7TTeeZO98aHRwYUhZ%2FfUHLyYLKqhDGXVE6gNjaOCk5POmbYcvOMLVke1b0HVnS6GEznxsBhSnp7FoR&X-Amz-Signature=1d3115c9f47796a534e1559f6668412e7180fec222833a4d2a71a4da23f7f394&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZULM7O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk9ZXf8%2FvlkvkH7pkyAy1c2iGuFVRiTHVWxjEdmw0YbAiEAhonELmLcPDnzpkcnn5X4ftiGU70V73Z7dxXXg4IB0cMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhiiQplXuIZ8jOcJSrcA3%2FNrhLC2AUtPWXHFpjRh4gUBPMVzDglRRS2s9AySgmKGTj9puyxzHr%2BKVzR5s6fUvKwy2ojx1KsRhv9Bpt3qAS57bljcN3ta1Fjrm5FQOzdog4T74v%2FfNs5AG71P0jbqzm%2BpXQdVQrnfRmzYRhhb3XL7orNA8cpAe4GSsR7pkLxm4xE7cPlH6cAxwySk037y0hnQvc90ALBeES35RNoOAV%2Fwu4tsBxZxaBMJAsmkTXPny2AaxgFi%2BY2ceuU5TlO2JSoA5mxs6nu4KW7aE6M1kFbKTSm%2Bu4W%2FJytgAPu%2F4xL8ftx%2BlXkShVxIG7HcOe4RIGNIifTrn3D4nyVHYMvEpDQc3nvOWGjv%2B4sh3hFAyjPV8Qw3dLL2pzgJSOWh5L5kHbtxMGpRwvT%2F%2FdibhgxMvNPTmXuM8skneMW4y%2Bysj5cQR7Tq%2BN%2BjkXYPf23MU8xRPdWmaNH8jlyiPH%2FbqeuKTDwZebURJb0vaNaAA53QsCXyxv2bg3Q4LIH9Xu7unkm1yRw9bCgpqklGjLM4qe9VelX884ahRElyS3CvILOTVYV8bRH8mfL8O%2BjbOQWgblfMyIIosyWXRUV4o2s4NtSwNFgigxzsQIYcRJO0hSsIWWw%2BETHX%2FcmsYWeytczMJnj57wGOqUBTd%2FAVhpdeQsc8xosJQw2q974c%2B7C6ElsxnOIAFT02maE%2FbgAqWhhgyddidPh07GxPYEio70gOLuFebsejdyoTd4cMcSRg0W%2FpsfKmEwq5WqvconJx7s3M6ccbt1srZIzm2Wo46t9OsMX%2Bi7TTeeZO98aHRwYUhZ%2FfUHLyYLKqhDGXVE6gNjaOCk5POmbYcvOMLVke1b0HVnS6GEznxsBhSnp7FoR&X-Amz-Signature=aaa023ebbbf2e610c09cb0f4b4622ad39625def07ca2eb94d96d6d3c5815968c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Video Sequences
A **video** can be viewed as a sequence of multiple **images** or **frames**.
### Image Formats
Common image file formats include:
- **JPEG** (Joint Photographic Expert Group)
- **PNG** (Portable Network Graphics)
These formats compress and reduce file sizes while maintaining image quality.
### Image Processing Libraries in Python
#### Pillow (PIL)
Pillow is a widely used Python library for image manipulation.
- To load an image:
```python
from PIL import Image
img = Image.open('image.png')
```
- **Attributes** of a Pillow image:
	- `format`: The file format (e.g., PNG, JPEG).
	- `size`: The dimensions of the image (width x height).
	- `mode`: The color space (e.g., RGB, L for grayscale).
#### Example: Converting to Gray-Scale
- Convert an image to **gray-scale**:
```python
gray_img = img.convert('L')
gray_img.show()
```
#### Example: Quantization
- **Quantize** an image to reduce the number of intensity levels:
```python
quantized_img = img.quantize(colors=16)
quantized_img.show()
```
#### OpenCV
**OpenCV** is a powerful library for **computer vision** with more functionality than PIL.
- Import OpenCV:
```python
import cv2
```
- Load an image:
```python
img = cv2.imread('image.png')
```
- **Attributes** of an OpenCV image:
	- OpenCV represents images as **NumPy arrays**.
	- The **color channels** are ordered as **BGR** (blue, green, red) instead of **RGB**.
#### Example: Color Space Conversion
- Convert from **BGR to RGB**:
```python
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
- Convert to **gray-scale**:
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
#### Example: Saving an Image
- Save an image using OpenCV:
```python
cv2.imwrite('output.png', img)
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWZULM7O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk9ZXf8%2FvlkvkH7pkyAy1c2iGuFVRiTHVWxjEdmw0YbAiEAhonELmLcPDnzpkcnn5X4ftiGU70V73Z7dxXXg4IB0cMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhiiQplXuIZ8jOcJSrcA3%2FNrhLC2AUtPWXHFpjRh4gUBPMVzDglRRS2s9AySgmKGTj9puyxzHr%2BKVzR5s6fUvKwy2ojx1KsRhv9Bpt3qAS57bljcN3ta1Fjrm5FQOzdog4T74v%2FfNs5AG71P0jbqzm%2BpXQdVQrnfRmzYRhhb3XL7orNA8cpAe4GSsR7pkLxm4xE7cPlH6cAxwySk037y0hnQvc90ALBeES35RNoOAV%2Fwu4tsBxZxaBMJAsmkTXPny2AaxgFi%2BY2ceuU5TlO2JSoA5mxs6nu4KW7aE6M1kFbKTSm%2Bu4W%2FJytgAPu%2F4xL8ftx%2BlXkShVxIG7HcOe4RIGNIifTrn3D4nyVHYMvEpDQc3nvOWGjv%2B4sh3hFAyjPV8Qw3dLL2pzgJSOWh5L5kHbtxMGpRwvT%2F%2FdibhgxMvNPTmXuM8skneMW4y%2Bysj5cQR7Tq%2BN%2BjkXYPf23MU8xRPdWmaNH8jlyiPH%2FbqeuKTDwZebURJb0vaNaAA53QsCXyxv2bg3Q4LIH9Xu7unkm1yRw9bCgpqklGjLM4qe9VelX884ahRElyS3CvILOTVYV8bRH8mfL8O%2BjbOQWgblfMyIIosyWXRUV4o2s4NtSwNFgigxzsQIYcRJO0hSsIWWw%2BETHX%2FcmsYWeytczMJnj57wGOqUBTd%2FAVhpdeQsc8xosJQw2q974c%2B7C6ElsxnOIAFT02maE%2FbgAqWhhgyddidPh07GxPYEio70gOLuFebsejdyoTd4cMcSRg0W%2FpsfKmEwq5WqvconJx7s3M6ccbt1srZIzm2Wo46t9OsMX%2Bi7TTeeZO98aHRwYUhZ%2FfUHLyYLKqhDGXVE6gNjaOCk5POmbYcvOMLVke1b0HVnS6GEznxsBhSnp7FoR&X-Amz-Signature=44990ec9e63b4f42bc9714c195619b0e510e722b89853b4b10b6d6565df24fe3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Working with Color Channels
Using **slices**, individual color channels (e.g., **blue**, **green**, **red**) can be extracted:
```python
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]
```
Each channel can then be processed or analyzed separately.
#### Conversion between PIL and NumPy Arrays
PIL images can be easily converted to **NumPy arrays** for further processing:
```python
import numpy as np
np_img = np.array(img)
```
This conversion is particularly useful when integrating with **OpenCV** and performing advanced operations.
### Conclusion
Both **PIL** and **OpenCV** are essential tools for handling and processing digital images in Python. Each has its strengths:
- **PIL** is simple and great for basic tasks.
- **OpenCV** offers more advanced capabilities for **computer vision** applications.
___


