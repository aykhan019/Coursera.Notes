

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCEB36C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGalWTqpepdudk4UFscxRZWKeEtxFLK9%2BqVAbJLa1LKTAiEAy887OqOXGJUJOoGnmRXdWT6pVB%2B77uhk9RDjgao68Osq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGpsdJbPwKPSUWiDLyrcA0Qtmz3NpyIrkeaEHNpEU3w07bVvbWWbd37fldaTF2dIkYfK1o1qCOWBgcBxGHvbqRPlYL3Z%2FjQcmAK9fEbgiWib%2Bh6%2FyQQRhL3pgjiPO8Mg4MJiZ9k%2F9xcxTNjh2wREIvIKbWkwivQPrWgQGcXqwJ%2BK7U4xEyzZEBuBFpiOhaWhpWAfhTCDg3qZVTDbvBMH5w9TRPfvwE2F%2BnzrwlsR9IhyK09daI5lufTCkQxo7u2xnSQuKQ1brA7FBUxQzitlCUCbxOnZttjv2%2Ffn0bMEcKaLdAHGo5HVWfAX2q6cJ0iR5QjGvndgMIROI6R%2B7rx2hiHOTSxf4nZFjrdeSu1QdtZhJOZzOOoPxHQDX99CJqC0Tsh2VupsxNVEL60hj46RT7NIRZi04oSNewtpXfXgL%2F2CxNoRBCN7VxgGe4AfA343suFm8hWoorGEI7DGaOrh3U87hLV9R3eEidZiCaWCRqi8I59Sffbv2TfU%2BUAw%2BuuXw8zf4SucgDHWZDP41PLlASnhx7EcBCL3iH9P%2FEkzaPWAAl%2FMWrCuQPWEr5VVfh2PVaoZKcygCqBoSkJAopru2ZJLneAGy9EiIHXrTn2JKxTilnef4J5F%2Fq4h%2BjA%2BOYW%2FCPBQGM7nz1Rcrh5LMPO6jr0GOqUBhf%2FmXvsL0Rwe57ToGsemPKYi7AyOreWjpVOsj94kk%2FzPm3XmlKy2TOSsHnTyrLYE4QQ%2FoiAZOhRgCpav8Y%2FYqlcf2injKRhI1Oi8ufFHQ8y6TYhM7qeqMsrDTuXbFTD%2BGtCYW2htxK3ZhTRKmcICo1WL%2F%2BccX7L3CXFN%2Byypdgno1EXxZgLKkid43OqWThbtFFz6laaJTIip9hdh%2BetDB%2FvRUCb7&X-Amz-Signature=34d0a72cb29be39e40976d3ee3d07fa5db6ef0f8676d497738d29b3ea66d4f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFZMES7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBy6%2BbAt4xi3kgm4zLkFnSa5xO0K6uPpQu5vdRtpDUDeAiEAuF6yiuIqE4%2FkHsiv1B4E9j1WOQBz6karpKQJAbLAlN8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDDZnrnivmiQSpx9R4CrcA3orSlArlIsh0mv4nhjR6%2FusWGgU3ZSoRVe%2B9umrW4Rjlaofx449Wtkvi%2B2N19XMHtpLOqGM3T320VSntoasfmLtGsriI6gvUd60z%2BP6seWeLhNNwbmh5OpA%2FgZ83styPA9IuJ%2BthaZJC318cCAdpe9UnCk0EI7GX5cUscurgZX2RYuWGjQqUG8pw44n7zqp44lbYus5FESp6YDN%2Bx15I3ZPpW2myqwRZoB1pCftkxk8%2Bd22jwKL7gn4EoKCKtx43b5i7Wz3eSx3Tj34%2FFxBeVXcoCKIMFTQ4jOa%2Fkd0xjcz2flMccA8n0wEMkTt6SzW9tsZOZNYqOoTdOuF%2FOoMNXsQXxR75pM0iZGVR0Y0bJoQ9Up2Jzl3hoLpuqANSJhFrO8V5o6eGFbbDbImHsLro7zUC%2BZbXR2VvtHUGh3yXKxgslvEoIhXSleU0cu%2FojzWnxTOwrXJ%2FwRUKzTbyfOurj%2FSx9q7CxEyoNVzHaEqtVPlWikfRRqIekLJkD06DSFOh9uYUAdes5%2F38hwGNdM1QLqN3Z6pCS9FXOJ7h%2Bo3II%2BkXhRnp7vDb1B9T3aonXMtLj2joXPxm%2BB38aR8rjlH0XUKVLGWj78ZHJgaeejftK%2F%2BkvNJ86eUXfgTeNz3MPS6jr0GOqUBoIJPLl0q5EXpa3LqvyMnhckLFofvII8KxCup6wQpv%2BmsTj%2Bap2Zbt5a%2FbOE%2BaBcEz2uNeifNO9iAlr9S0QF2Vekeqmjv3tDk5luStPNP3kgGN0TfRoDUb2IYjIMSei9rDA0Uz5OFsI%2B%2Ba2DOJNvWqgMUMF6P5IFQCyLABvwqBK6Yk2EqerqGLczefTSfwJNSgRfuOZP%2F%2FVBTlK8ktvanv2DV9v8w&X-Amz-Signature=dc5ff8a85779b530e74ef02036d39ae4c8844a4609228b8c35dc8a7f55ccacef&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFZMES7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBy6%2BbAt4xi3kgm4zLkFnSa5xO0K6uPpQu5vdRtpDUDeAiEAuF6yiuIqE4%2FkHsiv1B4E9j1WOQBz6karpKQJAbLAlN8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDDZnrnivmiQSpx9R4CrcA3orSlArlIsh0mv4nhjR6%2FusWGgU3ZSoRVe%2B9umrW4Rjlaofx449Wtkvi%2B2N19XMHtpLOqGM3T320VSntoasfmLtGsriI6gvUd60z%2BP6seWeLhNNwbmh5OpA%2FgZ83styPA9IuJ%2BthaZJC318cCAdpe9UnCk0EI7GX5cUscurgZX2RYuWGjQqUG8pw44n7zqp44lbYus5FESp6YDN%2Bx15I3ZPpW2myqwRZoB1pCftkxk8%2Bd22jwKL7gn4EoKCKtx43b5i7Wz3eSx3Tj34%2FFxBeVXcoCKIMFTQ4jOa%2Fkd0xjcz2flMccA8n0wEMkTt6SzW9tsZOZNYqOoTdOuF%2FOoMNXsQXxR75pM0iZGVR0Y0bJoQ9Up2Jzl3hoLpuqANSJhFrO8V5o6eGFbbDbImHsLro7zUC%2BZbXR2VvtHUGh3yXKxgslvEoIhXSleU0cu%2FojzWnxTOwrXJ%2FwRUKzTbyfOurj%2FSx9q7CxEyoNVzHaEqtVPlWikfRRqIekLJkD06DSFOh9uYUAdes5%2F38hwGNdM1QLqN3Z6pCS9FXOJ7h%2Bo3II%2BkXhRnp7vDb1B9T3aonXMtLj2joXPxm%2BB38aR8rjlH0XUKVLGWj78ZHJgaeejftK%2F%2BkvNJ86eUXfgTeNz3MPS6jr0GOqUBoIJPLl0q5EXpa3LqvyMnhckLFofvII8KxCup6wQpv%2BmsTj%2Bap2Zbt5a%2FbOE%2BaBcEz2uNeifNO9iAlr9S0QF2Vekeqmjv3tDk5luStPNP3kgGN0TfRoDUb2IYjIMSei9rDA0Uz5OFsI%2B%2Ba2DOJNvWqgMUMF6P5IFQCyLABvwqBK6Yk2EqerqGLczefTSfwJNSgRfuOZP%2F%2FVBTlK8ktvanv2DV9v8w&X-Amz-Signature=19357f29bb0352f8311d8d92705c095cd4f237edb347b3d920b7dc7cf396387b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFZMES7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBy6%2BbAt4xi3kgm4zLkFnSa5xO0K6uPpQu5vdRtpDUDeAiEAuF6yiuIqE4%2FkHsiv1B4E9j1WOQBz6karpKQJAbLAlN8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDDZnrnivmiQSpx9R4CrcA3orSlArlIsh0mv4nhjR6%2FusWGgU3ZSoRVe%2B9umrW4Rjlaofx449Wtkvi%2B2N19XMHtpLOqGM3T320VSntoasfmLtGsriI6gvUd60z%2BP6seWeLhNNwbmh5OpA%2FgZ83styPA9IuJ%2BthaZJC318cCAdpe9UnCk0EI7GX5cUscurgZX2RYuWGjQqUG8pw44n7zqp44lbYus5FESp6YDN%2Bx15I3ZPpW2myqwRZoB1pCftkxk8%2Bd22jwKL7gn4EoKCKtx43b5i7Wz3eSx3Tj34%2FFxBeVXcoCKIMFTQ4jOa%2Fkd0xjcz2flMccA8n0wEMkTt6SzW9tsZOZNYqOoTdOuF%2FOoMNXsQXxR75pM0iZGVR0Y0bJoQ9Up2Jzl3hoLpuqANSJhFrO8V5o6eGFbbDbImHsLro7zUC%2BZbXR2VvtHUGh3yXKxgslvEoIhXSleU0cu%2FojzWnxTOwrXJ%2FwRUKzTbyfOurj%2FSx9q7CxEyoNVzHaEqtVPlWikfRRqIekLJkD06DSFOh9uYUAdes5%2F38hwGNdM1QLqN3Z6pCS9FXOJ7h%2Bo3II%2BkXhRnp7vDb1B9T3aonXMtLj2joXPxm%2BB38aR8rjlH0XUKVLGWj78ZHJgaeejftK%2F%2BkvNJ86eUXfgTeNz3MPS6jr0GOqUBoIJPLl0q5EXpa3LqvyMnhckLFofvII8KxCup6wQpv%2BmsTj%2Bap2Zbt5a%2FbOE%2BaBcEz2uNeifNO9iAlr9S0QF2Vekeqmjv3tDk5luStPNP3kgGN0TfRoDUb2IYjIMSei9rDA0Uz5OFsI%2B%2Ba2DOJNvWqgMUMF6P5IFQCyLABvwqBK6Yk2EqerqGLczefTSfwJNSgRfuOZP%2F%2FVBTlK8ktvanv2DV9v8w&X-Amz-Signature=db21dc4364c2708eaa0c7223d9fc2af62c10319111628373c3f07df336133f2e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFZMES7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBy6%2BbAt4xi3kgm4zLkFnSa5xO0K6uPpQu5vdRtpDUDeAiEAuF6yiuIqE4%2FkHsiv1B4E9j1WOQBz6karpKQJAbLAlN8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDDZnrnivmiQSpx9R4CrcA3orSlArlIsh0mv4nhjR6%2FusWGgU3ZSoRVe%2B9umrW4Rjlaofx449Wtkvi%2B2N19XMHtpLOqGM3T320VSntoasfmLtGsriI6gvUd60z%2BP6seWeLhNNwbmh5OpA%2FgZ83styPA9IuJ%2BthaZJC318cCAdpe9UnCk0EI7GX5cUscurgZX2RYuWGjQqUG8pw44n7zqp44lbYus5FESp6YDN%2Bx15I3ZPpW2myqwRZoB1pCftkxk8%2Bd22jwKL7gn4EoKCKtx43b5i7Wz3eSx3Tj34%2FFxBeVXcoCKIMFTQ4jOa%2Fkd0xjcz2flMccA8n0wEMkTt6SzW9tsZOZNYqOoTdOuF%2FOoMNXsQXxR75pM0iZGVR0Y0bJoQ9Up2Jzl3hoLpuqANSJhFrO8V5o6eGFbbDbImHsLro7zUC%2BZbXR2VvtHUGh3yXKxgslvEoIhXSleU0cu%2FojzWnxTOwrXJ%2FwRUKzTbyfOurj%2FSx9q7CxEyoNVzHaEqtVPlWikfRRqIekLJkD06DSFOh9uYUAdes5%2F38hwGNdM1QLqN3Z6pCS9FXOJ7h%2Bo3II%2BkXhRnp7vDb1B9T3aonXMtLj2joXPxm%2BB38aR8rjlH0XUKVLGWj78ZHJgaeejftK%2F%2BkvNJ86eUXfgTeNz3MPS6jr0GOqUBoIJPLl0q5EXpa3LqvyMnhckLFofvII8KxCup6wQpv%2BmsTj%2Bap2Zbt5a%2FbOE%2BaBcEz2uNeifNO9iAlr9S0QF2Vekeqmjv3tDk5luStPNP3kgGN0TfRoDUb2IYjIMSei9rDA0Uz5OFsI%2B%2Ba2DOJNvWqgMUMF6P5IFQCyLABvwqBK6Yk2EqerqGLczefTSfwJNSgRfuOZP%2F%2FVBTlK8ktvanv2DV9v8w&X-Amz-Signature=e87dfb069f3923312ce35b844ba5dae62779439f390bdc116277de1afcd061cf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LFZMES7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBy6%2BbAt4xi3kgm4zLkFnSa5xO0K6uPpQu5vdRtpDUDeAiEAuF6yiuIqE4%2FkHsiv1B4E9j1WOQBz6karpKQJAbLAlN8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDDZnrnivmiQSpx9R4CrcA3orSlArlIsh0mv4nhjR6%2FusWGgU3ZSoRVe%2B9umrW4Rjlaofx449Wtkvi%2B2N19XMHtpLOqGM3T320VSntoasfmLtGsriI6gvUd60z%2BP6seWeLhNNwbmh5OpA%2FgZ83styPA9IuJ%2BthaZJC318cCAdpe9UnCk0EI7GX5cUscurgZX2RYuWGjQqUG8pw44n7zqp44lbYus5FESp6YDN%2Bx15I3ZPpW2myqwRZoB1pCftkxk8%2Bd22jwKL7gn4EoKCKtx43b5i7Wz3eSx3Tj34%2FFxBeVXcoCKIMFTQ4jOa%2Fkd0xjcz2flMccA8n0wEMkTt6SzW9tsZOZNYqOoTdOuF%2FOoMNXsQXxR75pM0iZGVR0Y0bJoQ9Up2Jzl3hoLpuqANSJhFrO8V5o6eGFbbDbImHsLro7zUC%2BZbXR2VvtHUGh3yXKxgslvEoIhXSleU0cu%2FojzWnxTOwrXJ%2FwRUKzTbyfOurj%2FSx9q7CxEyoNVzHaEqtVPlWikfRRqIekLJkD06DSFOh9uYUAdes5%2F38hwGNdM1QLqN3Z6pCS9FXOJ7h%2Bo3II%2BkXhRnp7vDb1B9T3aonXMtLj2joXPxm%2BB38aR8rjlH0XUKVLGWj78ZHJgaeejftK%2F%2BkvNJ86eUXfgTeNz3MPS6jr0GOqUBoIJPLl0q5EXpa3LqvyMnhckLFofvII8KxCup6wQpv%2BmsTj%2Bap2Zbt5a%2FbOE%2BaBcEz2uNeifNO9iAlr9S0QF2Vekeqmjv3tDk5luStPNP3kgGN0TfRoDUb2IYjIMSei9rDA0Uz5OFsI%2B%2Ba2DOJNvWqgMUMF6P5IFQCyLABvwqBK6Yk2EqerqGLczefTSfwJNSgRfuOZP%2F%2FVBTlK8ktvanv2DV9v8w&X-Amz-Signature=68fe41b356f4832c28101739420824187977746e8cb0c4d06c36fd61bcf0c885&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCEB36C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGalWTqpepdudk4UFscxRZWKeEtxFLK9%2BqVAbJLa1LKTAiEAy887OqOXGJUJOoGnmRXdWT6pVB%2B77uhk9RDjgao68Osq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGpsdJbPwKPSUWiDLyrcA0Qtmz3NpyIrkeaEHNpEU3w07bVvbWWbd37fldaTF2dIkYfK1o1qCOWBgcBxGHvbqRPlYL3Z%2FjQcmAK9fEbgiWib%2Bh6%2FyQQRhL3pgjiPO8Mg4MJiZ9k%2F9xcxTNjh2wREIvIKbWkwivQPrWgQGcXqwJ%2BK7U4xEyzZEBuBFpiOhaWhpWAfhTCDg3qZVTDbvBMH5w9TRPfvwE2F%2BnzrwlsR9IhyK09daI5lufTCkQxo7u2xnSQuKQ1brA7FBUxQzitlCUCbxOnZttjv2%2Ffn0bMEcKaLdAHGo5HVWfAX2q6cJ0iR5QjGvndgMIROI6R%2B7rx2hiHOTSxf4nZFjrdeSu1QdtZhJOZzOOoPxHQDX99CJqC0Tsh2VupsxNVEL60hj46RT7NIRZi04oSNewtpXfXgL%2F2CxNoRBCN7VxgGe4AfA343suFm8hWoorGEI7DGaOrh3U87hLV9R3eEidZiCaWCRqi8I59Sffbv2TfU%2BUAw%2BuuXw8zf4SucgDHWZDP41PLlASnhx7EcBCL3iH9P%2FEkzaPWAAl%2FMWrCuQPWEr5VVfh2PVaoZKcygCqBoSkJAopru2ZJLneAGy9EiIHXrTn2JKxTilnef4J5F%2Fq4h%2BjA%2BOYW%2FCPBQGM7nz1Rcrh5LMPO6jr0GOqUBhf%2FmXvsL0Rwe57ToGsemPKYi7AyOreWjpVOsj94kk%2FzPm3XmlKy2TOSsHnTyrLYE4QQ%2FoiAZOhRgCpav8Y%2FYqlcf2injKRhI1Oi8ufFHQ8y6TYhM7qeqMsrDTuXbFTD%2BGtCYW2htxK3ZhTRKmcICo1WL%2F%2BccX7L3CXFN%2Byypdgno1EXxZgLKkid43OqWThbtFFz6laaJTIip9hdh%2BetDB%2FvRUCb7&X-Amz-Signature=9e81295bdb27576e91a4510f67917d0d41ea5f1db8cf2fecd07b6609e4bf3e00&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCEB36C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGalWTqpepdudk4UFscxRZWKeEtxFLK9%2BqVAbJLa1LKTAiEAy887OqOXGJUJOoGnmRXdWT6pVB%2B77uhk9RDjgao68Osq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGpsdJbPwKPSUWiDLyrcA0Qtmz3NpyIrkeaEHNpEU3w07bVvbWWbd37fldaTF2dIkYfK1o1qCOWBgcBxGHvbqRPlYL3Z%2FjQcmAK9fEbgiWib%2Bh6%2FyQQRhL3pgjiPO8Mg4MJiZ9k%2F9xcxTNjh2wREIvIKbWkwivQPrWgQGcXqwJ%2BK7U4xEyzZEBuBFpiOhaWhpWAfhTCDg3qZVTDbvBMH5w9TRPfvwE2F%2BnzrwlsR9IhyK09daI5lufTCkQxo7u2xnSQuKQ1brA7FBUxQzitlCUCbxOnZttjv2%2Ffn0bMEcKaLdAHGo5HVWfAX2q6cJ0iR5QjGvndgMIROI6R%2B7rx2hiHOTSxf4nZFjrdeSu1QdtZhJOZzOOoPxHQDX99CJqC0Tsh2VupsxNVEL60hj46RT7NIRZi04oSNewtpXfXgL%2F2CxNoRBCN7VxgGe4AfA343suFm8hWoorGEI7DGaOrh3U87hLV9R3eEidZiCaWCRqi8I59Sffbv2TfU%2BUAw%2BuuXw8zf4SucgDHWZDP41PLlASnhx7EcBCL3iH9P%2FEkzaPWAAl%2FMWrCuQPWEr5VVfh2PVaoZKcygCqBoSkJAopru2ZJLneAGy9EiIHXrTn2JKxTilnef4J5F%2Fq4h%2BjA%2BOYW%2FCPBQGM7nz1Rcrh5LMPO6jr0GOqUBhf%2FmXvsL0Rwe57ToGsemPKYi7AyOreWjpVOsj94kk%2FzPm3XmlKy2TOSsHnTyrLYE4QQ%2FoiAZOhRgCpav8Y%2FYqlcf2injKRhI1Oi8ufFHQ8y6TYhM7qeqMsrDTuXbFTD%2BGtCYW2htxK3ZhTRKmcICo1WL%2F%2BccX7L3CXFN%2Byypdgno1EXxZgLKkid43OqWThbtFFz6laaJTIip9hdh%2BetDB%2FvRUCb7&X-Amz-Signature=41bea504e180b6542e7eddead044234201b0235d4c0d7747c2a8e9824d83e548&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCEB36C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGalWTqpepdudk4UFscxRZWKeEtxFLK9%2BqVAbJLa1LKTAiEAy887OqOXGJUJOoGnmRXdWT6pVB%2B77uhk9RDjgao68Osq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGpsdJbPwKPSUWiDLyrcA0Qtmz3NpyIrkeaEHNpEU3w07bVvbWWbd37fldaTF2dIkYfK1o1qCOWBgcBxGHvbqRPlYL3Z%2FjQcmAK9fEbgiWib%2Bh6%2FyQQRhL3pgjiPO8Mg4MJiZ9k%2F9xcxTNjh2wREIvIKbWkwivQPrWgQGcXqwJ%2BK7U4xEyzZEBuBFpiOhaWhpWAfhTCDg3qZVTDbvBMH5w9TRPfvwE2F%2BnzrwlsR9IhyK09daI5lufTCkQxo7u2xnSQuKQ1brA7FBUxQzitlCUCbxOnZttjv2%2Ffn0bMEcKaLdAHGo5HVWfAX2q6cJ0iR5QjGvndgMIROI6R%2B7rx2hiHOTSxf4nZFjrdeSu1QdtZhJOZzOOoPxHQDX99CJqC0Tsh2VupsxNVEL60hj46RT7NIRZi04oSNewtpXfXgL%2F2CxNoRBCN7VxgGe4AfA343suFm8hWoorGEI7DGaOrh3U87hLV9R3eEidZiCaWCRqi8I59Sffbv2TfU%2BUAw%2BuuXw8zf4SucgDHWZDP41PLlASnhx7EcBCL3iH9P%2FEkzaPWAAl%2FMWrCuQPWEr5VVfh2PVaoZKcygCqBoSkJAopru2ZJLneAGy9EiIHXrTn2JKxTilnef4J5F%2Fq4h%2BjA%2BOYW%2FCPBQGM7nz1Rcrh5LMPO6jr0GOqUBhf%2FmXvsL0Rwe57ToGsemPKYi7AyOreWjpVOsj94kk%2FzPm3XmlKy2TOSsHnTyrLYE4QQ%2FoiAZOhRgCpav8Y%2FYqlcf2injKRhI1Oi8ufFHQ8y6TYhM7qeqMsrDTuXbFTD%2BGtCYW2htxK3ZhTRKmcICo1WL%2F%2BccX7L3CXFN%2Byypdgno1EXxZgLKkid43OqWThbtFFz6laaJTIip9hdh%2BetDB%2FvRUCb7&X-Amz-Signature=5ad8e3d40a92b2c42d1516758e685eeac0b2e64c9da7fa7940bd5b6bcde26c2e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCEB36C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGalWTqpepdudk4UFscxRZWKeEtxFLK9%2BqVAbJLa1LKTAiEAy887OqOXGJUJOoGnmRXdWT6pVB%2B77uhk9RDjgao68Osq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGpsdJbPwKPSUWiDLyrcA0Qtmz3NpyIrkeaEHNpEU3w07bVvbWWbd37fldaTF2dIkYfK1o1qCOWBgcBxGHvbqRPlYL3Z%2FjQcmAK9fEbgiWib%2Bh6%2FyQQRhL3pgjiPO8Mg4MJiZ9k%2F9xcxTNjh2wREIvIKbWkwivQPrWgQGcXqwJ%2BK7U4xEyzZEBuBFpiOhaWhpWAfhTCDg3qZVTDbvBMH5w9TRPfvwE2F%2BnzrwlsR9IhyK09daI5lufTCkQxo7u2xnSQuKQ1brA7FBUxQzitlCUCbxOnZttjv2%2Ffn0bMEcKaLdAHGo5HVWfAX2q6cJ0iR5QjGvndgMIROI6R%2B7rx2hiHOTSxf4nZFjrdeSu1QdtZhJOZzOOoPxHQDX99CJqC0Tsh2VupsxNVEL60hj46RT7NIRZi04oSNewtpXfXgL%2F2CxNoRBCN7VxgGe4AfA343suFm8hWoorGEI7DGaOrh3U87hLV9R3eEidZiCaWCRqi8I59Sffbv2TfU%2BUAw%2BuuXw8zf4SucgDHWZDP41PLlASnhx7EcBCL3iH9P%2FEkzaPWAAl%2FMWrCuQPWEr5VVfh2PVaoZKcygCqBoSkJAopru2ZJLneAGy9EiIHXrTn2JKxTilnef4J5F%2Fq4h%2BjA%2BOYW%2FCPBQGM7nz1Rcrh5LMPO6jr0GOqUBhf%2FmXvsL0Rwe57ToGsemPKYi7AyOreWjpVOsj94kk%2FzPm3XmlKy2TOSsHnTyrLYE4QQ%2FoiAZOhRgCpav8Y%2FYqlcf2injKRhI1Oi8ufFHQ8y6TYhM7qeqMsrDTuXbFTD%2BGtCYW2htxK3ZhTRKmcICo1WL%2F%2BccX7L3CXFN%2Byypdgno1EXxZgLKkid43OqWThbtFFz6laaJTIip9hdh%2BetDB%2FvRUCb7&X-Amz-Signature=7c0786e8d6fa4a61dce5648b34200a4817e5d803dc0bea856d679795eb79257e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCEB36C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGalWTqpepdudk4UFscxRZWKeEtxFLK9%2BqVAbJLa1LKTAiEAy887OqOXGJUJOoGnmRXdWT6pVB%2B77uhk9RDjgao68Osq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGpsdJbPwKPSUWiDLyrcA0Qtmz3NpyIrkeaEHNpEU3w07bVvbWWbd37fldaTF2dIkYfK1o1qCOWBgcBxGHvbqRPlYL3Z%2FjQcmAK9fEbgiWib%2Bh6%2FyQQRhL3pgjiPO8Mg4MJiZ9k%2F9xcxTNjh2wREIvIKbWkwivQPrWgQGcXqwJ%2BK7U4xEyzZEBuBFpiOhaWhpWAfhTCDg3qZVTDbvBMH5w9TRPfvwE2F%2BnzrwlsR9IhyK09daI5lufTCkQxo7u2xnSQuKQ1brA7FBUxQzitlCUCbxOnZttjv2%2Ffn0bMEcKaLdAHGo5HVWfAX2q6cJ0iR5QjGvndgMIROI6R%2B7rx2hiHOTSxf4nZFjrdeSu1QdtZhJOZzOOoPxHQDX99CJqC0Tsh2VupsxNVEL60hj46RT7NIRZi04oSNewtpXfXgL%2F2CxNoRBCN7VxgGe4AfA343suFm8hWoorGEI7DGaOrh3U87hLV9R3eEidZiCaWCRqi8I59Sffbv2TfU%2BUAw%2BuuXw8zf4SucgDHWZDP41PLlASnhx7EcBCL3iH9P%2FEkzaPWAAl%2FMWrCuQPWEr5VVfh2PVaoZKcygCqBoSkJAopru2ZJLneAGy9EiIHXrTn2JKxTilnef4J5F%2Fq4h%2BjA%2BOYW%2FCPBQGM7nz1Rcrh5LMPO6jr0GOqUBhf%2FmXvsL0Rwe57ToGsemPKYi7AyOreWjpVOsj94kk%2FzPm3XmlKy2TOSsHnTyrLYE4QQ%2FoiAZOhRgCpav8Y%2FYqlcf2injKRhI1Oi8ufFHQ8y6TYhM7qeqMsrDTuXbFTD%2BGtCYW2htxK3ZhTRKmcICo1WL%2F%2BccX7L3CXFN%2Byypdgno1EXxZgLKkid43OqWThbtFFz6laaJTIip9hdh%2BetDB%2FvRUCb7&X-Amz-Signature=35be9d1f48455cf61fbbd4e5b55cd577c82ab48b984791c3cf60d23d2b6b40cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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


