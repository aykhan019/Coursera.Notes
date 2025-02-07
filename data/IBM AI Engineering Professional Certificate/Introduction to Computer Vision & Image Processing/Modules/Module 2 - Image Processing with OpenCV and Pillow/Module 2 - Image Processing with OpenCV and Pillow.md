

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF3JLPNP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDjVCLVCJPpLKAtVb1WNkV7f2a1EFdcsqGQmqML9ivmAQIhALCKB1Mgnr14cuQG%2FSyEVLWi2nAC89jxJ9USDaXUjPJtKv8DCHAQABoMNjM3NDIzMTgzODA1IgzGehgWHCHt65sZiSIq3AOXEYCBFlQ2mWsjw2R4%2BIUH2YZa6cdGoORwT9gae7TfQI%2BN4aLz97m6yiIN8nWGQHH65R5eLZsa8bXSgMw0ATqvCm7kqkACZYDB2cu4DWqAiPVAvVwNoSjMa8pAx0%2FfTqLq5YgP5WXBG5X50A9qG1DCVHg4IXXgBgY%2BpZEuFxv1gXyqbKFNXqC1WvFVIhjG1iTIeLzV6BlMhe6iD7Em%2BCIlsWbTxj5QmtnWnSsNkAL1%2Bbq%2FPu2zSKCPa9ibyYkeqH0rlQ3mKEilItGANz4FvgF9A4bpXq8iL68FB2nB%2FRVHxFcFWj4T%2F%2FKKj7kNcX5jHL0bn5nqEvyXItHbc5c4aT9b5ZHfbJBUFnrq0flzFJOnFP5R3NiMc4aB68lF%2B2nkq6NklheDTuD6KYqxxOP50Rj6eO6dN%2FUP%2BecZsVj1%2BgUbxGZlumUO4Y5NUX3AFp0NGsiGOwav81Vcy5CNY%2Bx2gMiKkvT7GKZ%2Fs76Whqa1cs%2FkQZoEPpVxXzXS5elDyLzKzw56gZmk5qk%2B9g1INvXf%2F%2Fzh9WljxukKLFoNpnO6w7cjGKQRQDWiwQr8i7qoOuOC%2BxiUgNQI4zWok4I4ZIS%2BgUgVvFS2LQYX39kR9hep6cbz5aeW%2BCKkMUyzFjpydjDT3Ja9BjqkARakOVczGob%2Fsp1jITpJI3Wbe5UGifJqxZGVuEVbxpSISiNk8UeOsoyzyGKFWOFoG9WZPWAWSEr4UoVsSXZFF2CHi7G8V81OTXPcYQZUbdO6D1XimqPhJTXTrBQ5b8x80UU2S7qeQpl41eQf35c0MInNVybJeHERfyJg4Y6z28D2LU9YvqPdO4eyTyp4jpHLCmHibj1qLtJNSAqi2bYeiJPwfWkz&X-Amz-Signature=19608e641e220fb7a010cc54ac38468bb8d1424db8a2e9d592970fb0d2fcd5b6&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MFL3YY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIFG3S0IdOyCmqa8VUlU%2FApSgM6n9jq4ODlN2re%2BtWClnAiEA7%2FdZwPYPRHBiw9%2F3PTYlQcrwcYRLH8gPlkW7HYGJTIAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDO%2BMMw8dgdrUXYnvryrcAwaVKnFPYLWR79jpSlKQ7YS7kAkIVKv4hBdKwbVek3uycsNQyA1ntgvc3w6S2n7O72yVAjkcC8WRKgvAAtD7C58I%2FKsSMwclxj9OlEKqvtbyRqvRpx2lJlP6urHXyHTxyktN7ullKlMwVy3T9loRzCgXFV%2Fn3f8BKgF7ippgnIAEGYy5t1eLNPzxBJyWakAqDHDeaTEVoTDGZbNHM9HC08%2ByOuvzc%2FnLMJY4pzuibZQwbYk65tth0VYhoU9fjRdl6FfACZIPGjrwuo6ylZtsnykU0R88Ty%2FL5pZphgfaFZYzGqK1JPY4pJMrIdWoXekbZGne2w%2BIUTkcnFOGA2jC6ATfayRJrUHwfADWS2m3MncNYjuXSmz5BcR3j2OZToc%2FSiwABKGAem3Ypq%2FVW%2B%2BF5mv1XOSus0nABJD2nRSr9Cbm4N7dxRGnCS6PMrHmVxzjGVDJ5Kgb24ZmbA8ZnywRgyWi0SKt2LqPmRzOJLJAyjOoaDHFeZhVK3eYG7O1JvMc0CStzQsGvTKgsVrI2YDm%2BdqtJ8T5P9qGswbYDCL08aTr%2F%2Bnfw57%2FXdAgkzHjRKhcXKT09kM2qIo80ZPLA8CPo3Pihs5Byrc7haEXgj%2BrSEwfpdDlKO2UGvWIsU5XMPzclr0GOqUBzR2QadXZPsvfefP1uwHX1VZCziECbKPhSSGD1LQFCn5KmZWf66a0eHtDTSiEhOq4XHFBrlIxR9bsxico%2BaDStApnqj4NpMwCQpo23nDrpUrKyP1c8pGX4qfLCSSiMUdbtkzBNUVm2poVrdllhJH%2BpLiqJm55TtBzQ45RVj14rKLaC6vF5kp1F3S%2B4dRwPpID5WHyEnx6PH%2FT%2Bze0gku7sGmnxKKK&X-Amz-Signature=6651f1b8d273a3557ceeee1921ae755885b121195b5bb96575d121ae8c39412a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MFL3YY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIFG3S0IdOyCmqa8VUlU%2FApSgM6n9jq4ODlN2re%2BtWClnAiEA7%2FdZwPYPRHBiw9%2F3PTYlQcrwcYRLH8gPlkW7HYGJTIAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDO%2BMMw8dgdrUXYnvryrcAwaVKnFPYLWR79jpSlKQ7YS7kAkIVKv4hBdKwbVek3uycsNQyA1ntgvc3w6S2n7O72yVAjkcC8WRKgvAAtD7C58I%2FKsSMwclxj9OlEKqvtbyRqvRpx2lJlP6urHXyHTxyktN7ullKlMwVy3T9loRzCgXFV%2Fn3f8BKgF7ippgnIAEGYy5t1eLNPzxBJyWakAqDHDeaTEVoTDGZbNHM9HC08%2ByOuvzc%2FnLMJY4pzuibZQwbYk65tth0VYhoU9fjRdl6FfACZIPGjrwuo6ylZtsnykU0R88Ty%2FL5pZphgfaFZYzGqK1JPY4pJMrIdWoXekbZGne2w%2BIUTkcnFOGA2jC6ATfayRJrUHwfADWS2m3MncNYjuXSmz5BcR3j2OZToc%2FSiwABKGAem3Ypq%2FVW%2B%2BF5mv1XOSus0nABJD2nRSr9Cbm4N7dxRGnCS6PMrHmVxzjGVDJ5Kgb24ZmbA8ZnywRgyWi0SKt2LqPmRzOJLJAyjOoaDHFeZhVK3eYG7O1JvMc0CStzQsGvTKgsVrI2YDm%2BdqtJ8T5P9qGswbYDCL08aTr%2F%2Bnfw57%2FXdAgkzHjRKhcXKT09kM2qIo80ZPLA8CPo3Pihs5Byrc7haEXgj%2BrSEwfpdDlKO2UGvWIsU5XMPzclr0GOqUBzR2QadXZPsvfefP1uwHX1VZCziECbKPhSSGD1LQFCn5KmZWf66a0eHtDTSiEhOq4XHFBrlIxR9bsxico%2BaDStApnqj4NpMwCQpo23nDrpUrKyP1c8pGX4qfLCSSiMUdbtkzBNUVm2poVrdllhJH%2BpLiqJm55TtBzQ45RVj14rKLaC6vF5kp1F3S%2B4dRwPpID5WHyEnx6PH%2FT%2Bze0gku7sGmnxKKK&X-Amz-Signature=df17afead8fe8b78827b5adf48ca93bc35471814afc3a5e029e78aed53d9b27d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MFL3YY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIFG3S0IdOyCmqa8VUlU%2FApSgM6n9jq4ODlN2re%2BtWClnAiEA7%2FdZwPYPRHBiw9%2F3PTYlQcrwcYRLH8gPlkW7HYGJTIAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDO%2BMMw8dgdrUXYnvryrcAwaVKnFPYLWR79jpSlKQ7YS7kAkIVKv4hBdKwbVek3uycsNQyA1ntgvc3w6S2n7O72yVAjkcC8WRKgvAAtD7C58I%2FKsSMwclxj9OlEKqvtbyRqvRpx2lJlP6urHXyHTxyktN7ullKlMwVy3T9loRzCgXFV%2Fn3f8BKgF7ippgnIAEGYy5t1eLNPzxBJyWakAqDHDeaTEVoTDGZbNHM9HC08%2ByOuvzc%2FnLMJY4pzuibZQwbYk65tth0VYhoU9fjRdl6FfACZIPGjrwuo6ylZtsnykU0R88Ty%2FL5pZphgfaFZYzGqK1JPY4pJMrIdWoXekbZGne2w%2BIUTkcnFOGA2jC6ATfayRJrUHwfADWS2m3MncNYjuXSmz5BcR3j2OZToc%2FSiwABKGAem3Ypq%2FVW%2B%2BF5mv1XOSus0nABJD2nRSr9Cbm4N7dxRGnCS6PMrHmVxzjGVDJ5Kgb24ZmbA8ZnywRgyWi0SKt2LqPmRzOJLJAyjOoaDHFeZhVK3eYG7O1JvMc0CStzQsGvTKgsVrI2YDm%2BdqtJ8T5P9qGswbYDCL08aTr%2F%2Bnfw57%2FXdAgkzHjRKhcXKT09kM2qIo80ZPLA8CPo3Pihs5Byrc7haEXgj%2BrSEwfpdDlKO2UGvWIsU5XMPzclr0GOqUBzR2QadXZPsvfefP1uwHX1VZCziECbKPhSSGD1LQFCn5KmZWf66a0eHtDTSiEhOq4XHFBrlIxR9bsxico%2BaDStApnqj4NpMwCQpo23nDrpUrKyP1c8pGX4qfLCSSiMUdbtkzBNUVm2poVrdllhJH%2BpLiqJm55TtBzQ45RVj14rKLaC6vF5kp1F3S%2B4dRwPpID5WHyEnx6PH%2FT%2Bze0gku7sGmnxKKK&X-Amz-Signature=2394ba59026807872619213ba2498984152da785fcd6b9a29e4a8bf385d7140d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MFL3YY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIFG3S0IdOyCmqa8VUlU%2FApSgM6n9jq4ODlN2re%2BtWClnAiEA7%2FdZwPYPRHBiw9%2F3PTYlQcrwcYRLH8gPlkW7HYGJTIAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDO%2BMMw8dgdrUXYnvryrcAwaVKnFPYLWR79jpSlKQ7YS7kAkIVKv4hBdKwbVek3uycsNQyA1ntgvc3w6S2n7O72yVAjkcC8WRKgvAAtD7C58I%2FKsSMwclxj9OlEKqvtbyRqvRpx2lJlP6urHXyHTxyktN7ullKlMwVy3T9loRzCgXFV%2Fn3f8BKgF7ippgnIAEGYy5t1eLNPzxBJyWakAqDHDeaTEVoTDGZbNHM9HC08%2ByOuvzc%2FnLMJY4pzuibZQwbYk65tth0VYhoU9fjRdl6FfACZIPGjrwuo6ylZtsnykU0R88Ty%2FL5pZphgfaFZYzGqK1JPY4pJMrIdWoXekbZGne2w%2BIUTkcnFOGA2jC6ATfayRJrUHwfADWS2m3MncNYjuXSmz5BcR3j2OZToc%2FSiwABKGAem3Ypq%2FVW%2B%2BF5mv1XOSus0nABJD2nRSr9Cbm4N7dxRGnCS6PMrHmVxzjGVDJ5Kgb24ZmbA8ZnywRgyWi0SKt2LqPmRzOJLJAyjOoaDHFeZhVK3eYG7O1JvMc0CStzQsGvTKgsVrI2YDm%2BdqtJ8T5P9qGswbYDCL08aTr%2F%2Bnfw57%2FXdAgkzHjRKhcXKT09kM2qIo80ZPLA8CPo3Pihs5Byrc7haEXgj%2BrSEwfpdDlKO2UGvWIsU5XMPzclr0GOqUBzR2QadXZPsvfefP1uwHX1VZCziECbKPhSSGD1LQFCn5KmZWf66a0eHtDTSiEhOq4XHFBrlIxR9bsxico%2BaDStApnqj4NpMwCQpo23nDrpUrKyP1c8pGX4qfLCSSiMUdbtkzBNUVm2poVrdllhJH%2BpLiqJm55TtBzQ45RVj14rKLaC6vF5kp1F3S%2B4dRwPpID5WHyEnx6PH%2FT%2Bze0gku7sGmnxKKK&X-Amz-Signature=cb87015fa5369104783f7cf9fc6eee6f5c9dc594e03721fc43bb26d4bbd80f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MFL3YY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIFG3S0IdOyCmqa8VUlU%2FApSgM6n9jq4ODlN2re%2BtWClnAiEA7%2FdZwPYPRHBiw9%2F3PTYlQcrwcYRLH8gPlkW7HYGJTIAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDO%2BMMw8dgdrUXYnvryrcAwaVKnFPYLWR79jpSlKQ7YS7kAkIVKv4hBdKwbVek3uycsNQyA1ntgvc3w6S2n7O72yVAjkcC8WRKgvAAtD7C58I%2FKsSMwclxj9OlEKqvtbyRqvRpx2lJlP6urHXyHTxyktN7ullKlMwVy3T9loRzCgXFV%2Fn3f8BKgF7ippgnIAEGYy5t1eLNPzxBJyWakAqDHDeaTEVoTDGZbNHM9HC08%2ByOuvzc%2FnLMJY4pzuibZQwbYk65tth0VYhoU9fjRdl6FfACZIPGjrwuo6ylZtsnykU0R88Ty%2FL5pZphgfaFZYzGqK1JPY4pJMrIdWoXekbZGne2w%2BIUTkcnFOGA2jC6ATfayRJrUHwfADWS2m3MncNYjuXSmz5BcR3j2OZToc%2FSiwABKGAem3Ypq%2FVW%2B%2BF5mv1XOSus0nABJD2nRSr9Cbm4N7dxRGnCS6PMrHmVxzjGVDJ5Kgb24ZmbA8ZnywRgyWi0SKt2LqPmRzOJLJAyjOoaDHFeZhVK3eYG7O1JvMc0CStzQsGvTKgsVrI2YDm%2BdqtJ8T5P9qGswbYDCL08aTr%2F%2Bnfw57%2FXdAgkzHjRKhcXKT09kM2qIo80ZPLA8CPo3Pihs5Byrc7haEXgj%2BrSEwfpdDlKO2UGvWIsU5XMPzclr0GOqUBzR2QadXZPsvfefP1uwHX1VZCziECbKPhSSGD1LQFCn5KmZWf66a0eHtDTSiEhOq4XHFBrlIxR9bsxico%2BaDStApnqj4NpMwCQpo23nDrpUrKyP1c8pGX4qfLCSSiMUdbtkzBNUVm2poVrdllhJH%2BpLiqJm55TtBzQ45RVj14rKLaC6vF5kp1F3S%2B4dRwPpID5WHyEnx6PH%2FT%2Bze0gku7sGmnxKKK&X-Amz-Signature=04b37cd4546df22a97269d08f15977e6433da0ab30f43d83daafeb118f3791e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF3JLPNP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDjVCLVCJPpLKAtVb1WNkV7f2a1EFdcsqGQmqML9ivmAQIhALCKB1Mgnr14cuQG%2FSyEVLWi2nAC89jxJ9USDaXUjPJtKv8DCHAQABoMNjM3NDIzMTgzODA1IgzGehgWHCHt65sZiSIq3AOXEYCBFlQ2mWsjw2R4%2BIUH2YZa6cdGoORwT9gae7TfQI%2BN4aLz97m6yiIN8nWGQHH65R5eLZsa8bXSgMw0ATqvCm7kqkACZYDB2cu4DWqAiPVAvVwNoSjMa8pAx0%2FfTqLq5YgP5WXBG5X50A9qG1DCVHg4IXXgBgY%2BpZEuFxv1gXyqbKFNXqC1WvFVIhjG1iTIeLzV6BlMhe6iD7Em%2BCIlsWbTxj5QmtnWnSsNkAL1%2Bbq%2FPu2zSKCPa9ibyYkeqH0rlQ3mKEilItGANz4FvgF9A4bpXq8iL68FB2nB%2FRVHxFcFWj4T%2F%2FKKj7kNcX5jHL0bn5nqEvyXItHbc5c4aT9b5ZHfbJBUFnrq0flzFJOnFP5R3NiMc4aB68lF%2B2nkq6NklheDTuD6KYqxxOP50Rj6eO6dN%2FUP%2BecZsVj1%2BgUbxGZlumUO4Y5NUX3AFp0NGsiGOwav81Vcy5CNY%2Bx2gMiKkvT7GKZ%2Fs76Whqa1cs%2FkQZoEPpVxXzXS5elDyLzKzw56gZmk5qk%2B9g1INvXf%2F%2Fzh9WljxukKLFoNpnO6w7cjGKQRQDWiwQr8i7qoOuOC%2BxiUgNQI4zWok4I4ZIS%2BgUgVvFS2LQYX39kR9hep6cbz5aeW%2BCKkMUyzFjpydjDT3Ja9BjqkARakOVczGob%2Fsp1jITpJI3Wbe5UGifJqxZGVuEVbxpSISiNk8UeOsoyzyGKFWOFoG9WZPWAWSEr4UoVsSXZFF2CHi7G8V81OTXPcYQZUbdO6D1XimqPhJTXTrBQ5b8x80UU2S7qeQpl41eQf35c0MInNVybJeHERfyJg4Y6z28D2LU9YvqPdO4eyTyp4jpHLCmHibj1qLtJNSAqi2bYeiJPwfWkz&X-Amz-Signature=50c52825ddaa83d145a5b5ac706c5c56c13eecf3f62588e2f93f141f79d01f1e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF3JLPNP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDjVCLVCJPpLKAtVb1WNkV7f2a1EFdcsqGQmqML9ivmAQIhALCKB1Mgnr14cuQG%2FSyEVLWi2nAC89jxJ9USDaXUjPJtKv8DCHAQABoMNjM3NDIzMTgzODA1IgzGehgWHCHt65sZiSIq3AOXEYCBFlQ2mWsjw2R4%2BIUH2YZa6cdGoORwT9gae7TfQI%2BN4aLz97m6yiIN8nWGQHH65R5eLZsa8bXSgMw0ATqvCm7kqkACZYDB2cu4DWqAiPVAvVwNoSjMa8pAx0%2FfTqLq5YgP5WXBG5X50A9qG1DCVHg4IXXgBgY%2BpZEuFxv1gXyqbKFNXqC1WvFVIhjG1iTIeLzV6BlMhe6iD7Em%2BCIlsWbTxj5QmtnWnSsNkAL1%2Bbq%2FPu2zSKCPa9ibyYkeqH0rlQ3mKEilItGANz4FvgF9A4bpXq8iL68FB2nB%2FRVHxFcFWj4T%2F%2FKKj7kNcX5jHL0bn5nqEvyXItHbc5c4aT9b5ZHfbJBUFnrq0flzFJOnFP5R3NiMc4aB68lF%2B2nkq6NklheDTuD6KYqxxOP50Rj6eO6dN%2FUP%2BecZsVj1%2BgUbxGZlumUO4Y5NUX3AFp0NGsiGOwav81Vcy5CNY%2Bx2gMiKkvT7GKZ%2Fs76Whqa1cs%2FkQZoEPpVxXzXS5elDyLzKzw56gZmk5qk%2B9g1INvXf%2F%2Fzh9WljxukKLFoNpnO6w7cjGKQRQDWiwQr8i7qoOuOC%2BxiUgNQI4zWok4I4ZIS%2BgUgVvFS2LQYX39kR9hep6cbz5aeW%2BCKkMUyzFjpydjDT3Ja9BjqkARakOVczGob%2Fsp1jITpJI3Wbe5UGifJqxZGVuEVbxpSISiNk8UeOsoyzyGKFWOFoG9WZPWAWSEr4UoVsSXZFF2CHi7G8V81OTXPcYQZUbdO6D1XimqPhJTXTrBQ5b8x80UU2S7qeQpl41eQf35c0MInNVybJeHERfyJg4Y6z28D2LU9YvqPdO4eyTyp4jpHLCmHibj1qLtJNSAqi2bYeiJPwfWkz&X-Amz-Signature=e516ef3ecd6b38186ca845534b4136b18011e7685b0a9081b8b7660d64888dc2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF3JLPNP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDjVCLVCJPpLKAtVb1WNkV7f2a1EFdcsqGQmqML9ivmAQIhALCKB1Mgnr14cuQG%2FSyEVLWi2nAC89jxJ9USDaXUjPJtKv8DCHAQABoMNjM3NDIzMTgzODA1IgzGehgWHCHt65sZiSIq3AOXEYCBFlQ2mWsjw2R4%2BIUH2YZa6cdGoORwT9gae7TfQI%2BN4aLz97m6yiIN8nWGQHH65R5eLZsa8bXSgMw0ATqvCm7kqkACZYDB2cu4DWqAiPVAvVwNoSjMa8pAx0%2FfTqLq5YgP5WXBG5X50A9qG1DCVHg4IXXgBgY%2BpZEuFxv1gXyqbKFNXqC1WvFVIhjG1iTIeLzV6BlMhe6iD7Em%2BCIlsWbTxj5QmtnWnSsNkAL1%2Bbq%2FPu2zSKCPa9ibyYkeqH0rlQ3mKEilItGANz4FvgF9A4bpXq8iL68FB2nB%2FRVHxFcFWj4T%2F%2FKKj7kNcX5jHL0bn5nqEvyXItHbc5c4aT9b5ZHfbJBUFnrq0flzFJOnFP5R3NiMc4aB68lF%2B2nkq6NklheDTuD6KYqxxOP50Rj6eO6dN%2FUP%2BecZsVj1%2BgUbxGZlumUO4Y5NUX3AFp0NGsiGOwav81Vcy5CNY%2Bx2gMiKkvT7GKZ%2Fs76Whqa1cs%2FkQZoEPpVxXzXS5elDyLzKzw56gZmk5qk%2B9g1INvXf%2F%2Fzh9WljxukKLFoNpnO6w7cjGKQRQDWiwQr8i7qoOuOC%2BxiUgNQI4zWok4I4ZIS%2BgUgVvFS2LQYX39kR9hep6cbz5aeW%2BCKkMUyzFjpydjDT3Ja9BjqkARakOVczGob%2Fsp1jITpJI3Wbe5UGifJqxZGVuEVbxpSISiNk8UeOsoyzyGKFWOFoG9WZPWAWSEr4UoVsSXZFF2CHi7G8V81OTXPcYQZUbdO6D1XimqPhJTXTrBQ5b8x80UU2S7qeQpl41eQf35c0MInNVybJeHERfyJg4Y6z28D2LU9YvqPdO4eyTyp4jpHLCmHibj1qLtJNSAqi2bYeiJPwfWkz&X-Amz-Signature=782452f3becaa787fa8cb6b49cef52c39bb2c183205538c74c8cb31eb695836f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF3JLPNP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDjVCLVCJPpLKAtVb1WNkV7f2a1EFdcsqGQmqML9ivmAQIhALCKB1Mgnr14cuQG%2FSyEVLWi2nAC89jxJ9USDaXUjPJtKv8DCHAQABoMNjM3NDIzMTgzODA1IgzGehgWHCHt65sZiSIq3AOXEYCBFlQ2mWsjw2R4%2BIUH2YZa6cdGoORwT9gae7TfQI%2BN4aLz97m6yiIN8nWGQHH65R5eLZsa8bXSgMw0ATqvCm7kqkACZYDB2cu4DWqAiPVAvVwNoSjMa8pAx0%2FfTqLq5YgP5WXBG5X50A9qG1DCVHg4IXXgBgY%2BpZEuFxv1gXyqbKFNXqC1WvFVIhjG1iTIeLzV6BlMhe6iD7Em%2BCIlsWbTxj5QmtnWnSsNkAL1%2Bbq%2FPu2zSKCPa9ibyYkeqH0rlQ3mKEilItGANz4FvgF9A4bpXq8iL68FB2nB%2FRVHxFcFWj4T%2F%2FKKj7kNcX5jHL0bn5nqEvyXItHbc5c4aT9b5ZHfbJBUFnrq0flzFJOnFP5R3NiMc4aB68lF%2B2nkq6NklheDTuD6KYqxxOP50Rj6eO6dN%2FUP%2BecZsVj1%2BgUbxGZlumUO4Y5NUX3AFp0NGsiGOwav81Vcy5CNY%2Bx2gMiKkvT7GKZ%2Fs76Whqa1cs%2FkQZoEPpVxXzXS5elDyLzKzw56gZmk5qk%2B9g1INvXf%2F%2Fzh9WljxukKLFoNpnO6w7cjGKQRQDWiwQr8i7qoOuOC%2BxiUgNQI4zWok4I4ZIS%2BgUgVvFS2LQYX39kR9hep6cbz5aeW%2BCKkMUyzFjpydjDT3Ja9BjqkARakOVczGob%2Fsp1jITpJI3Wbe5UGifJqxZGVuEVbxpSISiNk8UeOsoyzyGKFWOFoG9WZPWAWSEr4UoVsSXZFF2CHi7G8V81OTXPcYQZUbdO6D1XimqPhJTXTrBQ5b8x80UU2S7qeQpl41eQf35c0MInNVybJeHERfyJg4Y6z28D2LU9YvqPdO4eyTyp4jpHLCmHibj1qLtJNSAqi2bYeiJPwfWkz&X-Amz-Signature=49dba8d25dd8b2664976ca98bef6c232cb9e771b2331a4ba7f1f808da6e94d06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF3JLPNP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDjVCLVCJPpLKAtVb1WNkV7f2a1EFdcsqGQmqML9ivmAQIhALCKB1Mgnr14cuQG%2FSyEVLWi2nAC89jxJ9USDaXUjPJtKv8DCHAQABoMNjM3NDIzMTgzODA1IgzGehgWHCHt65sZiSIq3AOXEYCBFlQ2mWsjw2R4%2BIUH2YZa6cdGoORwT9gae7TfQI%2BN4aLz97m6yiIN8nWGQHH65R5eLZsa8bXSgMw0ATqvCm7kqkACZYDB2cu4DWqAiPVAvVwNoSjMa8pAx0%2FfTqLq5YgP5WXBG5X50A9qG1DCVHg4IXXgBgY%2BpZEuFxv1gXyqbKFNXqC1WvFVIhjG1iTIeLzV6BlMhe6iD7Em%2BCIlsWbTxj5QmtnWnSsNkAL1%2Bbq%2FPu2zSKCPa9ibyYkeqH0rlQ3mKEilItGANz4FvgF9A4bpXq8iL68FB2nB%2FRVHxFcFWj4T%2F%2FKKj7kNcX5jHL0bn5nqEvyXItHbc5c4aT9b5ZHfbJBUFnrq0flzFJOnFP5R3NiMc4aB68lF%2B2nkq6NklheDTuD6KYqxxOP50Rj6eO6dN%2FUP%2BecZsVj1%2BgUbxGZlumUO4Y5NUX3AFp0NGsiGOwav81Vcy5CNY%2Bx2gMiKkvT7GKZ%2Fs76Whqa1cs%2FkQZoEPpVxXzXS5elDyLzKzw56gZmk5qk%2B9g1INvXf%2F%2Fzh9WljxukKLFoNpnO6w7cjGKQRQDWiwQr8i7qoOuOC%2BxiUgNQI4zWok4I4ZIS%2BgUgVvFS2LQYX39kR9hep6cbz5aeW%2BCKkMUyzFjpydjDT3Ja9BjqkARakOVczGob%2Fsp1jITpJI3Wbe5UGifJqxZGVuEVbxpSISiNk8UeOsoyzyGKFWOFoG9WZPWAWSEr4UoVsSXZFF2CHi7G8V81OTXPcYQZUbdO6D1XimqPhJTXTrBQ5b8x80UU2S7qeQpl41eQf35c0MInNVybJeHERfyJg4Y6z28D2LU9YvqPdO4eyTyp4jpHLCmHibj1qLtJNSAqi2bYeiJPwfWkz&X-Amz-Signature=37e59c3972241111a0aab3115931e497a669f415cce09345592094053864bf06&X-Amz-SignedHeaders=host&x-id=GetObject)
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


