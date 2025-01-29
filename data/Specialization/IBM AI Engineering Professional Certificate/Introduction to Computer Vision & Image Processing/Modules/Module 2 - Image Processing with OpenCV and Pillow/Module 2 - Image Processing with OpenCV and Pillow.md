

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AWRNIHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmbTaWksdAjOYYsiLB5gvLom0FNbNnrCgluz97%2FNi74AIhAO5E0ovuJVLB05z1bwSrHbj6zeKcM7gQH0DH6YbvGRixKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIvT6xbBWCrBQFgQUq3AMwPVQQtvXleXe6vy%2FKx9ET4CEv%2FPmzVRGi4dfi1CtI2lYhymJxIerhV9rGRYuIJXygkcg8cwaHoMi2YW9t%2FWDUffGRPQvzYqY7dFLs2agPuOyZmP7jkj1ZC5wceWEq8AI6EmWF1%2F9dryJqQh2pDZHOILRSlHZEbOkes7RjOewpKbW1W2r%2F2imiV%2FF7DGFIWD%2Bnh%2F2TqhIhIiEXQflD9NKi78dEpUpPimjxG0ktF0rrU7FkU7ZYBeZu58feby6wYLl4GUZwjH%2Fq4UmvK%2B3a6ZbJRt2cWwLpBx%2BQmD7Z6t%2FxMxEq4PqgIwk6lMced7B6MSSJN58kLSgYsdaUHWKX1P4KDVfv1R4Rxmd3PZALMQ31Kx443QjHoXw8konPOqbBLzQ1%2B1ZspRABAMzwtwEzdV36WU4eNmAUxJL7KVnVG4QG3GGran%2Bf61srd%2FSkBif2UvwK8taZNks9%2F%2BZwVcPrOVYmbJcj1C3htZ1Q3D%2FheFWKkTcKWDMyYZwUXmqsXkDykXXSUUjqTmIZQ1hCBbLfVSCC0mHCmORT8sD1aRIc8dL1pYLxKUv5t6IhnW%2BRWuGIrufaGxEVhsCEj39waPSj6zTKcS7n7oLqH21NrGfNxeezwgHWVK2VgNjjJeNwNjDTg%2Bm8BjqkAT1OO69Xrzykksepgcrui3pi1e2Br1LFaPZZSY%2FMQgoGXb3cEYU3QoKZHwgC8%2FGP0eu%2BUrQ%2Fny8%2F6cn2bBL%2BidDisTM1vf4dbjNVvJh5y4yL%2B9htZzLlr09MRjLqBalh0kTKh6K2KnJI3qq1JIl2CTgX2ZLVEeOvkOoAdn%2BP%2F0prTmFYUkSc7mBbR3lBjzq2RArWZ6qdaO4PE6iwP3NkCtOWAurj&X-Amz-Signature=149786a871bb807b25f21fce52b250edba7fad7127c758fc0f9c4e68b91df98b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFH24SKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsuVf0ZTYlionAfqgnnO8Ceq6EWEtH%2FZrPruY1kT88vAiEA5fqicILj2ln20f9vF3ABhQJFawr9nJCDRw31ak4j2nYqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkEbUQuKDFMqaCHFSrcA1RcLt9%2FK1gnWEq1N9ZimPjZwEQfJrUesjbxEnnyf9wGq%2FC%2BACPUNikzL1E1NTAqZSJ14VrEU6qFyRmAC1YotbB7fA1FuzpLMdbjFoRRxPUZbA6n3q15TjtW%2Fy0xPV%2FxUPd25tU4Luhd7OPZ9D8NYbvkbzgRHmwLOYQqz7401m3hOcB%2BkS2x75BsnhS48T%2ByDny94YLobga4qWcb5%2FwYxx6P4MnFk1x%2B65fn8Pc%2BHcDHAW%2BWW1j4DDa%2Fa72elGw7Mcr5mkK%2Fljc6qjkQE9ax6vKFtf3vRTafwYmXxc7RLMxhr0gLvaXCn3WXO%2Fmf%2FL0SBhBn25LVJ8SJGoJYagc1FpwGaaHHFMmrlHWJnhrhkdZfggGv5ICfoe5XwqtafOtZ5V9VU%2B4qn0l7T0jnBztLbAuVMyp56iW3leOnywkcfU8ZQZmCbMY1ciHfC%2B26k9YKvSxpcFatF38%2F2Zesqa%2FEysD3rg5BjT0PtSlnxlxXph%2BegP%2B92KVI8BDR4%2Fsb3GxPbRYpYcYoRB57vl3pFRXqRhvmRGVEFvKxNKF7%2FiP3vurjRB69%2BX43uR51UHg0EWyAUFRGNm4uKOoEoKT74Wwn3%2B%2BUhZ7waUheFKO2vJAuEassNQSYrxmJyUlZgS7pMO2D6bwGOqUBkabo3oZue8AFFyCgsTnaFlFzWAlE8awTZEk1AnUFs8EL7RGFnbdljr4kQk9EA5g1pVfeImvgRpvkWdhlqrhqLGlip6exlf8gFnG7AwSru0TevPb2IsXsYnG9x2sAWIdd0X%2F6VfIQjKejws1UmLiyuNlKYWIn6jljTUP44cvP1itJ0lid1%2BMRvW0Ur1T0J0XbBqGlzMHAnI1ha9cRulfY9Ngl17y2&X-Amz-Signature=60d55252676a93d40bc56115586947e79b20992745aab348ed01b5ac872b4b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFH24SKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsuVf0ZTYlionAfqgnnO8Ceq6EWEtH%2FZrPruY1kT88vAiEA5fqicILj2ln20f9vF3ABhQJFawr9nJCDRw31ak4j2nYqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkEbUQuKDFMqaCHFSrcA1RcLt9%2FK1gnWEq1N9ZimPjZwEQfJrUesjbxEnnyf9wGq%2FC%2BACPUNikzL1E1NTAqZSJ14VrEU6qFyRmAC1YotbB7fA1FuzpLMdbjFoRRxPUZbA6n3q15TjtW%2Fy0xPV%2FxUPd25tU4Luhd7OPZ9D8NYbvkbzgRHmwLOYQqz7401m3hOcB%2BkS2x75BsnhS48T%2ByDny94YLobga4qWcb5%2FwYxx6P4MnFk1x%2B65fn8Pc%2BHcDHAW%2BWW1j4DDa%2Fa72elGw7Mcr5mkK%2Fljc6qjkQE9ax6vKFtf3vRTafwYmXxc7RLMxhr0gLvaXCn3WXO%2Fmf%2FL0SBhBn25LVJ8SJGoJYagc1FpwGaaHHFMmrlHWJnhrhkdZfggGv5ICfoe5XwqtafOtZ5V9VU%2B4qn0l7T0jnBztLbAuVMyp56iW3leOnywkcfU8ZQZmCbMY1ciHfC%2B26k9YKvSxpcFatF38%2F2Zesqa%2FEysD3rg5BjT0PtSlnxlxXph%2BegP%2B92KVI8BDR4%2Fsb3GxPbRYpYcYoRB57vl3pFRXqRhvmRGVEFvKxNKF7%2FiP3vurjRB69%2BX43uR51UHg0EWyAUFRGNm4uKOoEoKT74Wwn3%2B%2BUhZ7waUheFKO2vJAuEassNQSYrxmJyUlZgS7pMO2D6bwGOqUBkabo3oZue8AFFyCgsTnaFlFzWAlE8awTZEk1AnUFs8EL7RGFnbdljr4kQk9EA5g1pVfeImvgRpvkWdhlqrhqLGlip6exlf8gFnG7AwSru0TevPb2IsXsYnG9x2sAWIdd0X%2F6VfIQjKejws1UmLiyuNlKYWIn6jljTUP44cvP1itJ0lid1%2BMRvW0Ur1T0J0XbBqGlzMHAnI1ha9cRulfY9Ngl17y2&X-Amz-Signature=1c04272ba395ab5e6aa6659580d86a49df940c9dead19e0239dd72b15cf78fa0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFH24SKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsuVf0ZTYlionAfqgnnO8Ceq6EWEtH%2FZrPruY1kT88vAiEA5fqicILj2ln20f9vF3ABhQJFawr9nJCDRw31ak4j2nYqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkEbUQuKDFMqaCHFSrcA1RcLt9%2FK1gnWEq1N9ZimPjZwEQfJrUesjbxEnnyf9wGq%2FC%2BACPUNikzL1E1NTAqZSJ14VrEU6qFyRmAC1YotbB7fA1FuzpLMdbjFoRRxPUZbA6n3q15TjtW%2Fy0xPV%2FxUPd25tU4Luhd7OPZ9D8NYbvkbzgRHmwLOYQqz7401m3hOcB%2BkS2x75BsnhS48T%2ByDny94YLobga4qWcb5%2FwYxx6P4MnFk1x%2B65fn8Pc%2BHcDHAW%2BWW1j4DDa%2Fa72elGw7Mcr5mkK%2Fljc6qjkQE9ax6vKFtf3vRTafwYmXxc7RLMxhr0gLvaXCn3WXO%2Fmf%2FL0SBhBn25LVJ8SJGoJYagc1FpwGaaHHFMmrlHWJnhrhkdZfggGv5ICfoe5XwqtafOtZ5V9VU%2B4qn0l7T0jnBztLbAuVMyp56iW3leOnywkcfU8ZQZmCbMY1ciHfC%2B26k9YKvSxpcFatF38%2F2Zesqa%2FEysD3rg5BjT0PtSlnxlxXph%2BegP%2B92KVI8BDR4%2Fsb3GxPbRYpYcYoRB57vl3pFRXqRhvmRGVEFvKxNKF7%2FiP3vurjRB69%2BX43uR51UHg0EWyAUFRGNm4uKOoEoKT74Wwn3%2B%2BUhZ7waUheFKO2vJAuEassNQSYrxmJyUlZgS7pMO2D6bwGOqUBkabo3oZue8AFFyCgsTnaFlFzWAlE8awTZEk1AnUFs8EL7RGFnbdljr4kQk9EA5g1pVfeImvgRpvkWdhlqrhqLGlip6exlf8gFnG7AwSru0TevPb2IsXsYnG9x2sAWIdd0X%2F6VfIQjKejws1UmLiyuNlKYWIn6jljTUP44cvP1itJ0lid1%2BMRvW0Ur1T0J0XbBqGlzMHAnI1ha9cRulfY9Ngl17y2&X-Amz-Signature=6035b62fd94d53e010d14ae39f444e7a07911cd25e85d3dd59b076145f328e1b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFH24SKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsuVf0ZTYlionAfqgnnO8Ceq6EWEtH%2FZrPruY1kT88vAiEA5fqicILj2ln20f9vF3ABhQJFawr9nJCDRw31ak4j2nYqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkEbUQuKDFMqaCHFSrcA1RcLt9%2FK1gnWEq1N9ZimPjZwEQfJrUesjbxEnnyf9wGq%2FC%2BACPUNikzL1E1NTAqZSJ14VrEU6qFyRmAC1YotbB7fA1FuzpLMdbjFoRRxPUZbA6n3q15TjtW%2Fy0xPV%2FxUPd25tU4Luhd7OPZ9D8NYbvkbzgRHmwLOYQqz7401m3hOcB%2BkS2x75BsnhS48T%2ByDny94YLobga4qWcb5%2FwYxx6P4MnFk1x%2B65fn8Pc%2BHcDHAW%2BWW1j4DDa%2Fa72elGw7Mcr5mkK%2Fljc6qjkQE9ax6vKFtf3vRTafwYmXxc7RLMxhr0gLvaXCn3WXO%2Fmf%2FL0SBhBn25LVJ8SJGoJYagc1FpwGaaHHFMmrlHWJnhrhkdZfggGv5ICfoe5XwqtafOtZ5V9VU%2B4qn0l7T0jnBztLbAuVMyp56iW3leOnywkcfU8ZQZmCbMY1ciHfC%2B26k9YKvSxpcFatF38%2F2Zesqa%2FEysD3rg5BjT0PtSlnxlxXph%2BegP%2B92KVI8BDR4%2Fsb3GxPbRYpYcYoRB57vl3pFRXqRhvmRGVEFvKxNKF7%2FiP3vurjRB69%2BX43uR51UHg0EWyAUFRGNm4uKOoEoKT74Wwn3%2B%2BUhZ7waUheFKO2vJAuEassNQSYrxmJyUlZgS7pMO2D6bwGOqUBkabo3oZue8AFFyCgsTnaFlFzWAlE8awTZEk1AnUFs8EL7RGFnbdljr4kQk9EA5g1pVfeImvgRpvkWdhlqrhqLGlip6exlf8gFnG7AwSru0TevPb2IsXsYnG9x2sAWIdd0X%2F6VfIQjKejws1UmLiyuNlKYWIn6jljTUP44cvP1itJ0lid1%2BMRvW0Ur1T0J0XbBqGlzMHAnI1ha9cRulfY9Ngl17y2&X-Amz-Signature=6b7f0353acac2647082b37a1adee04607a933db7a09e688280580e9989fdbaa3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFH24SKF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsuVf0ZTYlionAfqgnnO8Ceq6EWEtH%2FZrPruY1kT88vAiEA5fqicILj2ln20f9vF3ABhQJFawr9nJCDRw31ak4j2nYqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkEbUQuKDFMqaCHFSrcA1RcLt9%2FK1gnWEq1N9ZimPjZwEQfJrUesjbxEnnyf9wGq%2FC%2BACPUNikzL1E1NTAqZSJ14VrEU6qFyRmAC1YotbB7fA1FuzpLMdbjFoRRxPUZbA6n3q15TjtW%2Fy0xPV%2FxUPd25tU4Luhd7OPZ9D8NYbvkbzgRHmwLOYQqz7401m3hOcB%2BkS2x75BsnhS48T%2ByDny94YLobga4qWcb5%2FwYxx6P4MnFk1x%2B65fn8Pc%2BHcDHAW%2BWW1j4DDa%2Fa72elGw7Mcr5mkK%2Fljc6qjkQE9ax6vKFtf3vRTafwYmXxc7RLMxhr0gLvaXCn3WXO%2Fmf%2FL0SBhBn25LVJ8SJGoJYagc1FpwGaaHHFMmrlHWJnhrhkdZfggGv5ICfoe5XwqtafOtZ5V9VU%2B4qn0l7T0jnBztLbAuVMyp56iW3leOnywkcfU8ZQZmCbMY1ciHfC%2B26k9YKvSxpcFatF38%2F2Zesqa%2FEysD3rg5BjT0PtSlnxlxXph%2BegP%2B92KVI8BDR4%2Fsb3GxPbRYpYcYoRB57vl3pFRXqRhvmRGVEFvKxNKF7%2FiP3vurjRB69%2BX43uR51UHg0EWyAUFRGNm4uKOoEoKT74Wwn3%2B%2BUhZ7waUheFKO2vJAuEassNQSYrxmJyUlZgS7pMO2D6bwGOqUBkabo3oZue8AFFyCgsTnaFlFzWAlE8awTZEk1AnUFs8EL7RGFnbdljr4kQk9EA5g1pVfeImvgRpvkWdhlqrhqLGlip6exlf8gFnG7AwSru0TevPb2IsXsYnG9x2sAWIdd0X%2F6VfIQjKejws1UmLiyuNlKYWIn6jljTUP44cvP1itJ0lid1%2BMRvW0Ur1T0J0XbBqGlzMHAnI1ha9cRulfY9Ngl17y2&X-Amz-Signature=e655ac48f6b9320ce6e333b213699407d6483844153b53722925a0332f5cd973&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AWRNIHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmbTaWksdAjOYYsiLB5gvLom0FNbNnrCgluz97%2FNi74AIhAO5E0ovuJVLB05z1bwSrHbj6zeKcM7gQH0DH6YbvGRixKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIvT6xbBWCrBQFgQUq3AMwPVQQtvXleXe6vy%2FKx9ET4CEv%2FPmzVRGi4dfi1CtI2lYhymJxIerhV9rGRYuIJXygkcg8cwaHoMi2YW9t%2FWDUffGRPQvzYqY7dFLs2agPuOyZmP7jkj1ZC5wceWEq8AI6EmWF1%2F9dryJqQh2pDZHOILRSlHZEbOkes7RjOewpKbW1W2r%2F2imiV%2FF7DGFIWD%2Bnh%2F2TqhIhIiEXQflD9NKi78dEpUpPimjxG0ktF0rrU7FkU7ZYBeZu58feby6wYLl4GUZwjH%2Fq4UmvK%2B3a6ZbJRt2cWwLpBx%2BQmD7Z6t%2FxMxEq4PqgIwk6lMced7B6MSSJN58kLSgYsdaUHWKX1P4KDVfv1R4Rxmd3PZALMQ31Kx443QjHoXw8konPOqbBLzQ1%2B1ZspRABAMzwtwEzdV36WU4eNmAUxJL7KVnVG4QG3GGran%2Bf61srd%2FSkBif2UvwK8taZNks9%2F%2BZwVcPrOVYmbJcj1C3htZ1Q3D%2FheFWKkTcKWDMyYZwUXmqsXkDykXXSUUjqTmIZQ1hCBbLfVSCC0mHCmORT8sD1aRIc8dL1pYLxKUv5t6IhnW%2BRWuGIrufaGxEVhsCEj39waPSj6zTKcS7n7oLqH21NrGfNxeezwgHWVK2VgNjjJeNwNjDTg%2Bm8BjqkAT1OO69Xrzykksepgcrui3pi1e2Br1LFaPZZSY%2FMQgoGXb3cEYU3QoKZHwgC8%2FGP0eu%2BUrQ%2Fny8%2F6cn2bBL%2BidDisTM1vf4dbjNVvJh5y4yL%2B9htZzLlr09MRjLqBalh0kTKh6K2KnJI3qq1JIl2CTgX2ZLVEeOvkOoAdn%2BP%2F0prTmFYUkSc7mBbR3lBjzq2RArWZ6qdaO4PE6iwP3NkCtOWAurj&X-Amz-Signature=03be0da3b7ad16323f71a9f50236e9f98527d51b11422f1c267e0864895748fa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AWRNIHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmbTaWksdAjOYYsiLB5gvLom0FNbNnrCgluz97%2FNi74AIhAO5E0ovuJVLB05z1bwSrHbj6zeKcM7gQH0DH6YbvGRixKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIvT6xbBWCrBQFgQUq3AMwPVQQtvXleXe6vy%2FKx9ET4CEv%2FPmzVRGi4dfi1CtI2lYhymJxIerhV9rGRYuIJXygkcg8cwaHoMi2YW9t%2FWDUffGRPQvzYqY7dFLs2agPuOyZmP7jkj1ZC5wceWEq8AI6EmWF1%2F9dryJqQh2pDZHOILRSlHZEbOkes7RjOewpKbW1W2r%2F2imiV%2FF7DGFIWD%2Bnh%2F2TqhIhIiEXQflD9NKi78dEpUpPimjxG0ktF0rrU7FkU7ZYBeZu58feby6wYLl4GUZwjH%2Fq4UmvK%2B3a6ZbJRt2cWwLpBx%2BQmD7Z6t%2FxMxEq4PqgIwk6lMced7B6MSSJN58kLSgYsdaUHWKX1P4KDVfv1R4Rxmd3PZALMQ31Kx443QjHoXw8konPOqbBLzQ1%2B1ZspRABAMzwtwEzdV36WU4eNmAUxJL7KVnVG4QG3GGran%2Bf61srd%2FSkBif2UvwK8taZNks9%2F%2BZwVcPrOVYmbJcj1C3htZ1Q3D%2FheFWKkTcKWDMyYZwUXmqsXkDykXXSUUjqTmIZQ1hCBbLfVSCC0mHCmORT8sD1aRIc8dL1pYLxKUv5t6IhnW%2BRWuGIrufaGxEVhsCEj39waPSj6zTKcS7n7oLqH21NrGfNxeezwgHWVK2VgNjjJeNwNjDTg%2Bm8BjqkAT1OO69Xrzykksepgcrui3pi1e2Br1LFaPZZSY%2FMQgoGXb3cEYU3QoKZHwgC8%2FGP0eu%2BUrQ%2Fny8%2F6cn2bBL%2BidDisTM1vf4dbjNVvJh5y4yL%2B9htZzLlr09MRjLqBalh0kTKh6K2KnJI3qq1JIl2CTgX2ZLVEeOvkOoAdn%2BP%2F0prTmFYUkSc7mBbR3lBjzq2RArWZ6qdaO4PE6iwP3NkCtOWAurj&X-Amz-Signature=26b1cba3c4cef350121f676beb72cfce9a83d0772f6527c1447f50ac76d633d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AWRNIHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmbTaWksdAjOYYsiLB5gvLom0FNbNnrCgluz97%2FNi74AIhAO5E0ovuJVLB05z1bwSrHbj6zeKcM7gQH0DH6YbvGRixKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIvT6xbBWCrBQFgQUq3AMwPVQQtvXleXe6vy%2FKx9ET4CEv%2FPmzVRGi4dfi1CtI2lYhymJxIerhV9rGRYuIJXygkcg8cwaHoMi2YW9t%2FWDUffGRPQvzYqY7dFLs2agPuOyZmP7jkj1ZC5wceWEq8AI6EmWF1%2F9dryJqQh2pDZHOILRSlHZEbOkes7RjOewpKbW1W2r%2F2imiV%2FF7DGFIWD%2Bnh%2F2TqhIhIiEXQflD9NKi78dEpUpPimjxG0ktF0rrU7FkU7ZYBeZu58feby6wYLl4GUZwjH%2Fq4UmvK%2B3a6ZbJRt2cWwLpBx%2BQmD7Z6t%2FxMxEq4PqgIwk6lMced7B6MSSJN58kLSgYsdaUHWKX1P4KDVfv1R4Rxmd3PZALMQ31Kx443QjHoXw8konPOqbBLzQ1%2B1ZspRABAMzwtwEzdV36WU4eNmAUxJL7KVnVG4QG3GGran%2Bf61srd%2FSkBif2UvwK8taZNks9%2F%2BZwVcPrOVYmbJcj1C3htZ1Q3D%2FheFWKkTcKWDMyYZwUXmqsXkDykXXSUUjqTmIZQ1hCBbLfVSCC0mHCmORT8sD1aRIc8dL1pYLxKUv5t6IhnW%2BRWuGIrufaGxEVhsCEj39waPSj6zTKcS7n7oLqH21NrGfNxeezwgHWVK2VgNjjJeNwNjDTg%2Bm8BjqkAT1OO69Xrzykksepgcrui3pi1e2Br1LFaPZZSY%2FMQgoGXb3cEYU3QoKZHwgC8%2FGP0eu%2BUrQ%2Fny8%2F6cn2bBL%2BidDisTM1vf4dbjNVvJh5y4yL%2B9htZzLlr09MRjLqBalh0kTKh6K2KnJI3qq1JIl2CTgX2ZLVEeOvkOoAdn%2BP%2F0prTmFYUkSc7mBbR3lBjzq2RArWZ6qdaO4PE6iwP3NkCtOWAurj&X-Amz-Signature=7d82eaa66676f365df5c606d8f4adbc9ddccb543c0ad40084bd4561194ca114e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AWRNIHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmbTaWksdAjOYYsiLB5gvLom0FNbNnrCgluz97%2FNi74AIhAO5E0ovuJVLB05z1bwSrHbj6zeKcM7gQH0DH6YbvGRixKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIvT6xbBWCrBQFgQUq3AMwPVQQtvXleXe6vy%2FKx9ET4CEv%2FPmzVRGi4dfi1CtI2lYhymJxIerhV9rGRYuIJXygkcg8cwaHoMi2YW9t%2FWDUffGRPQvzYqY7dFLs2agPuOyZmP7jkj1ZC5wceWEq8AI6EmWF1%2F9dryJqQh2pDZHOILRSlHZEbOkes7RjOewpKbW1W2r%2F2imiV%2FF7DGFIWD%2Bnh%2F2TqhIhIiEXQflD9NKi78dEpUpPimjxG0ktF0rrU7FkU7ZYBeZu58feby6wYLl4GUZwjH%2Fq4UmvK%2B3a6ZbJRt2cWwLpBx%2BQmD7Z6t%2FxMxEq4PqgIwk6lMced7B6MSSJN58kLSgYsdaUHWKX1P4KDVfv1R4Rxmd3PZALMQ31Kx443QjHoXw8konPOqbBLzQ1%2B1ZspRABAMzwtwEzdV36WU4eNmAUxJL7KVnVG4QG3GGran%2Bf61srd%2FSkBif2UvwK8taZNks9%2F%2BZwVcPrOVYmbJcj1C3htZ1Q3D%2FheFWKkTcKWDMyYZwUXmqsXkDykXXSUUjqTmIZQ1hCBbLfVSCC0mHCmORT8sD1aRIc8dL1pYLxKUv5t6IhnW%2BRWuGIrufaGxEVhsCEj39waPSj6zTKcS7n7oLqH21NrGfNxeezwgHWVK2VgNjjJeNwNjDTg%2Bm8BjqkAT1OO69Xrzykksepgcrui3pi1e2Br1LFaPZZSY%2FMQgoGXb3cEYU3QoKZHwgC8%2FGP0eu%2BUrQ%2Fny8%2F6cn2bBL%2BidDisTM1vf4dbjNVvJh5y4yL%2B9htZzLlr09MRjLqBalh0kTKh6K2KnJI3qq1JIl2CTgX2ZLVEeOvkOoAdn%2BP%2F0prTmFYUkSc7mBbR3lBjzq2RArWZ6qdaO4PE6iwP3NkCtOWAurj&X-Amz-Signature=8fb5501fd602a6c8d97f5b18500d489f6ec6a798b74ebcb46055be8a5f4659ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AWRNIHH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmbTaWksdAjOYYsiLB5gvLom0FNbNnrCgluz97%2FNi74AIhAO5E0ovuJVLB05z1bwSrHbj6zeKcM7gQH0DH6YbvGRixKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIvT6xbBWCrBQFgQUq3AMwPVQQtvXleXe6vy%2FKx9ET4CEv%2FPmzVRGi4dfi1CtI2lYhymJxIerhV9rGRYuIJXygkcg8cwaHoMi2YW9t%2FWDUffGRPQvzYqY7dFLs2agPuOyZmP7jkj1ZC5wceWEq8AI6EmWF1%2F9dryJqQh2pDZHOILRSlHZEbOkes7RjOewpKbW1W2r%2F2imiV%2FF7DGFIWD%2Bnh%2F2TqhIhIiEXQflD9NKi78dEpUpPimjxG0ktF0rrU7FkU7ZYBeZu58feby6wYLl4GUZwjH%2Fq4UmvK%2B3a6ZbJRt2cWwLpBx%2BQmD7Z6t%2FxMxEq4PqgIwk6lMced7B6MSSJN58kLSgYsdaUHWKX1P4KDVfv1R4Rxmd3PZALMQ31Kx443QjHoXw8konPOqbBLzQ1%2B1ZspRABAMzwtwEzdV36WU4eNmAUxJL7KVnVG4QG3GGran%2Bf61srd%2FSkBif2UvwK8taZNks9%2F%2BZwVcPrOVYmbJcj1C3htZ1Q3D%2FheFWKkTcKWDMyYZwUXmqsXkDykXXSUUjqTmIZQ1hCBbLfVSCC0mHCmORT8sD1aRIc8dL1pYLxKUv5t6IhnW%2BRWuGIrufaGxEVhsCEj39waPSj6zTKcS7n7oLqH21NrGfNxeezwgHWVK2VgNjjJeNwNjDTg%2Bm8BjqkAT1OO69Xrzykksepgcrui3pi1e2Br1LFaPZZSY%2FMQgoGXb3cEYU3QoKZHwgC8%2FGP0eu%2BUrQ%2Fny8%2F6cn2bBL%2BidDisTM1vf4dbjNVvJh5y4yL%2B9htZzLlr09MRjLqBalh0kTKh6K2KnJI3qq1JIl2CTgX2ZLVEeOvkOoAdn%2BP%2F0prTmFYUkSc7mBbR3lBjzq2RArWZ6qdaO4PE6iwP3NkCtOWAurj&X-Amz-Signature=434a7beaa2cab68371960a94ac13d1663751da580b46ddc041fd8af3ace078e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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


