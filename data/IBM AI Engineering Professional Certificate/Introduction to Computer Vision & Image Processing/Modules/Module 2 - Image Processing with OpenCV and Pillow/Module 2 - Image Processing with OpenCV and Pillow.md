

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQQGNPW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIhKYiEY%2FgXxDZD7tcKUQaQQdTBWDrbhv1tRj9ZdvwQIhAIsmaUiuo5LHSeRSsLhog9pCqT3ghrHXXgz4nSQIXKKbKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4gu1krqJ6GqGBpuUq3AMPDwtjfrTMKe8csjXr31SCiSO%2FVkGwjxTSwzrYSog1%2BjWy4EOw81c8S5GCrGzRT6Wu0A%2BE4qedbYqHZtFsXh%2FyAaE5rhAM9O1M0sT2uVWjAhwUHUaEXu9eOH2VcWwA%2BCDNbB3TUv3CApOg9c8EwXmYL7A54x4Cy%2FCI1HaJB1%2BGPWuZPlwXhA5yvNaGCH9LURrAxRLQGitwLF%2BELYuz1GYiEz2c4vgWuTXTPQSHmR1vgOOZ5Ve2EmpL5MneKZn6G%2BMAz6D%2FvorR3KXtcRb6HsKVrrGg0KqpcUGG1OKoyJObcklt%2BWlOMPKrtTY%2F%2FtblpEiQ0pQwuC1ykkNsURJbgjbNd9boSQml5t557kjZR4ABtV7MhfAwj52gg0FnvGzZT8iikM%2FiguFXcAHXDPXI21EFxZOiAU3dRYJW5nZmZ67usTW61FmkvJYSdcNPrIL4263WNdQhASAB%2BZsDmgdLHn61JN3qN7l3b2HvqJAFuEKriLyBiZC0helGaWF8%2BFHbVLw4mq4iRUS1VXemduVYoRh7f5wb8zhoIvBy8lZstRklEQ8hqXR4YuySH%2BLEoKLrG9MvooJ04bhemOG6ey41rRcalxvTnYq8pvhBQ4nhkceoSjR1hsvS9n%2B8bF6MmTDJpPe8BjqkAdFnD5r8Z61RjzTyNQ3Q4MhOx9vNs0NB61SDjPGSTEncicsM9Ji39zbdz0g93Xj%2BWIDsOINALrLDKJFyoOz8rQpgpWHs1bjT%2FIlR5ZgreoPftBicxlLOgSGPLlgp6zizKdQ%2Fk0qXPcDq4t0cAyODW6Rb0LTekDkGWnGEO37FGI0f6gIwGyzcjItoCxmV231V38X36ucBX2a66oIZdNLdoz06Ke5D&X-Amz-Signature=29b5d074033e32d74abeaf522977e0d3b34a7495abf8fdfcce5d43fffb3e8e09&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU46DA4X%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzT7Tk1JG2HwQR%2BjWEdCwVeHRYBjpGnmBJpy9AHPl%2BiAIhAPmq9m7svvoBlgh50Iq1zL5Ms64dwZLlMAR9ozdGiSHRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzt4hTMn6wZynKFkk4q3APd70oT52kptGxXqXEMggpoCqtT3CAA27qK0IJw%2FK3oUnncLJynFrm4VePEL2XjYQBqqbwAFg%2FDUxCm1VI63iqNKX0s%2B95joFxxgENBL64Au2%2F7vkpVMu8xOX5wC3cJYeUNm7VjtUygrXz813Hf%2BfHgaWVwDDnGMv4mSCzeHwzjO4hH6mftHSUg%2BzRbavjOlbvUkxoPa82yOam8hmnhXkTVFAP2X9WcMy11WMHPvWrcHCCBuB3aiNw7AcF06LmM5zURS2ON4E5eQQyD8sQGcQ7B79miCQ5EZ9wVYL6qSNayFFFQ6Io%2F48qSANppItYqUKJTqFDzmeBqqAHymF8Od%2Fd%2BN3pLJGOis%2BAwSA6dF9dUhjsSsOUio1mSClollW2GBfFvULp2Bfeqi%2B1ND70gXd4Sqip%2Fb%2BoIfjscPYh5TPTTP6GDRnqzFhK5lZ4RbBIgwk1LQFRnhto0ZqyyIl%2B1NklEtWRlVW8aFaEXJioTqz02Ss%2BojEmqqoXzAFdRm7jG9ZaSI2foeraikVQ8seI6wWckWVaTM1LZe%2BXUKofo3Xqe%2FY%2FkXOYYpOx8k4vh7%2FGNwZ6j8kiZ07q7xU3ni%2FrFsdSF1BbEmLpjDS%2BWDXbJ3JubZ3PPdF8n2OSRvFFihTDbpPe8BjqkAarqn1MOsJurrl5UvTDI%2FII2GR5%2FsQWEPVOwBLicnPrd5wIhlP%2FXcQ1kWpl2TffFHInaEYGz4npAomk322FBDBh38boFVh2d0uVPAemtufGCS3EgFGFCfthOrdjmcWpp0kELnmjhWfqDZdHdFGneR7n%2FT33kOjDnYqfSKmwaLyCKyjcUoqjUEkl4PfEZtmBjfelBL3oSZqgRloFfY7opQSXM23IF&X-Amz-Signature=e6d77b587e875d4e80313a314c5e801a008784b3c7a880cbeaba0c42d61cf4d8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU46DA4X%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzT7Tk1JG2HwQR%2BjWEdCwVeHRYBjpGnmBJpy9AHPl%2BiAIhAPmq9m7svvoBlgh50Iq1zL5Ms64dwZLlMAR9ozdGiSHRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzt4hTMn6wZynKFkk4q3APd70oT52kptGxXqXEMggpoCqtT3CAA27qK0IJw%2FK3oUnncLJynFrm4VePEL2XjYQBqqbwAFg%2FDUxCm1VI63iqNKX0s%2B95joFxxgENBL64Au2%2F7vkpVMu8xOX5wC3cJYeUNm7VjtUygrXz813Hf%2BfHgaWVwDDnGMv4mSCzeHwzjO4hH6mftHSUg%2BzRbavjOlbvUkxoPa82yOam8hmnhXkTVFAP2X9WcMy11WMHPvWrcHCCBuB3aiNw7AcF06LmM5zURS2ON4E5eQQyD8sQGcQ7B79miCQ5EZ9wVYL6qSNayFFFQ6Io%2F48qSANppItYqUKJTqFDzmeBqqAHymF8Od%2Fd%2BN3pLJGOis%2BAwSA6dF9dUhjsSsOUio1mSClollW2GBfFvULp2Bfeqi%2B1ND70gXd4Sqip%2Fb%2BoIfjscPYh5TPTTP6GDRnqzFhK5lZ4RbBIgwk1LQFRnhto0ZqyyIl%2B1NklEtWRlVW8aFaEXJioTqz02Ss%2BojEmqqoXzAFdRm7jG9ZaSI2foeraikVQ8seI6wWckWVaTM1LZe%2BXUKofo3Xqe%2FY%2FkXOYYpOx8k4vh7%2FGNwZ6j8kiZ07q7xU3ni%2FrFsdSF1BbEmLpjDS%2BWDXbJ3JubZ3PPdF8n2OSRvFFihTDbpPe8BjqkAarqn1MOsJurrl5UvTDI%2FII2GR5%2FsQWEPVOwBLicnPrd5wIhlP%2FXcQ1kWpl2TffFHInaEYGz4npAomk322FBDBh38boFVh2d0uVPAemtufGCS3EgFGFCfthOrdjmcWpp0kELnmjhWfqDZdHdFGneR7n%2FT33kOjDnYqfSKmwaLyCKyjcUoqjUEkl4PfEZtmBjfelBL3oSZqgRloFfY7opQSXM23IF&X-Amz-Signature=5c9d97790e7c1c368c5abf78fb354cc3e9610369d662d48d11376c60f4dde723&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU46DA4X%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzT7Tk1JG2HwQR%2BjWEdCwVeHRYBjpGnmBJpy9AHPl%2BiAIhAPmq9m7svvoBlgh50Iq1zL5Ms64dwZLlMAR9ozdGiSHRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzt4hTMn6wZynKFkk4q3APd70oT52kptGxXqXEMggpoCqtT3CAA27qK0IJw%2FK3oUnncLJynFrm4VePEL2XjYQBqqbwAFg%2FDUxCm1VI63iqNKX0s%2B95joFxxgENBL64Au2%2F7vkpVMu8xOX5wC3cJYeUNm7VjtUygrXz813Hf%2BfHgaWVwDDnGMv4mSCzeHwzjO4hH6mftHSUg%2BzRbavjOlbvUkxoPa82yOam8hmnhXkTVFAP2X9WcMy11WMHPvWrcHCCBuB3aiNw7AcF06LmM5zURS2ON4E5eQQyD8sQGcQ7B79miCQ5EZ9wVYL6qSNayFFFQ6Io%2F48qSANppItYqUKJTqFDzmeBqqAHymF8Od%2Fd%2BN3pLJGOis%2BAwSA6dF9dUhjsSsOUio1mSClollW2GBfFvULp2Bfeqi%2B1ND70gXd4Sqip%2Fb%2BoIfjscPYh5TPTTP6GDRnqzFhK5lZ4RbBIgwk1LQFRnhto0ZqyyIl%2B1NklEtWRlVW8aFaEXJioTqz02Ss%2BojEmqqoXzAFdRm7jG9ZaSI2foeraikVQ8seI6wWckWVaTM1LZe%2BXUKofo3Xqe%2FY%2FkXOYYpOx8k4vh7%2FGNwZ6j8kiZ07q7xU3ni%2FrFsdSF1BbEmLpjDS%2BWDXbJ3JubZ3PPdF8n2OSRvFFihTDbpPe8BjqkAarqn1MOsJurrl5UvTDI%2FII2GR5%2FsQWEPVOwBLicnPrd5wIhlP%2FXcQ1kWpl2TffFHInaEYGz4npAomk322FBDBh38boFVh2d0uVPAemtufGCS3EgFGFCfthOrdjmcWpp0kELnmjhWfqDZdHdFGneR7n%2FT33kOjDnYqfSKmwaLyCKyjcUoqjUEkl4PfEZtmBjfelBL3oSZqgRloFfY7opQSXM23IF&X-Amz-Signature=00a42f45700f63c298560e7e506f85f3181334ac2e51e30c0c7edf29f6eb535c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU46DA4X%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzT7Tk1JG2HwQR%2BjWEdCwVeHRYBjpGnmBJpy9AHPl%2BiAIhAPmq9m7svvoBlgh50Iq1zL5Ms64dwZLlMAR9ozdGiSHRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzt4hTMn6wZynKFkk4q3APd70oT52kptGxXqXEMggpoCqtT3CAA27qK0IJw%2FK3oUnncLJynFrm4VePEL2XjYQBqqbwAFg%2FDUxCm1VI63iqNKX0s%2B95joFxxgENBL64Au2%2F7vkpVMu8xOX5wC3cJYeUNm7VjtUygrXz813Hf%2BfHgaWVwDDnGMv4mSCzeHwzjO4hH6mftHSUg%2BzRbavjOlbvUkxoPa82yOam8hmnhXkTVFAP2X9WcMy11WMHPvWrcHCCBuB3aiNw7AcF06LmM5zURS2ON4E5eQQyD8sQGcQ7B79miCQ5EZ9wVYL6qSNayFFFQ6Io%2F48qSANppItYqUKJTqFDzmeBqqAHymF8Od%2Fd%2BN3pLJGOis%2BAwSA6dF9dUhjsSsOUio1mSClollW2GBfFvULp2Bfeqi%2B1ND70gXd4Sqip%2Fb%2BoIfjscPYh5TPTTP6GDRnqzFhK5lZ4RbBIgwk1LQFRnhto0ZqyyIl%2B1NklEtWRlVW8aFaEXJioTqz02Ss%2BojEmqqoXzAFdRm7jG9ZaSI2foeraikVQ8seI6wWckWVaTM1LZe%2BXUKofo3Xqe%2FY%2FkXOYYpOx8k4vh7%2FGNwZ6j8kiZ07q7xU3ni%2FrFsdSF1BbEmLpjDS%2BWDXbJ3JubZ3PPdF8n2OSRvFFihTDbpPe8BjqkAarqn1MOsJurrl5UvTDI%2FII2GR5%2FsQWEPVOwBLicnPrd5wIhlP%2FXcQ1kWpl2TffFHInaEYGz4npAomk322FBDBh38boFVh2d0uVPAemtufGCS3EgFGFCfthOrdjmcWpp0kELnmjhWfqDZdHdFGneR7n%2FT33kOjDnYqfSKmwaLyCKyjcUoqjUEkl4PfEZtmBjfelBL3oSZqgRloFfY7opQSXM23IF&X-Amz-Signature=2b7f612adcc2c0d57b6bed7712f6cd5ea771db6a685e7e3d43597b5deb5b4e54&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU46DA4X%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzT7Tk1JG2HwQR%2BjWEdCwVeHRYBjpGnmBJpy9AHPl%2BiAIhAPmq9m7svvoBlgh50Iq1zL5Ms64dwZLlMAR9ozdGiSHRKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzt4hTMn6wZynKFkk4q3APd70oT52kptGxXqXEMggpoCqtT3CAA27qK0IJw%2FK3oUnncLJynFrm4VePEL2XjYQBqqbwAFg%2FDUxCm1VI63iqNKX0s%2B95joFxxgENBL64Au2%2F7vkpVMu8xOX5wC3cJYeUNm7VjtUygrXz813Hf%2BfHgaWVwDDnGMv4mSCzeHwzjO4hH6mftHSUg%2BzRbavjOlbvUkxoPa82yOam8hmnhXkTVFAP2X9WcMy11WMHPvWrcHCCBuB3aiNw7AcF06LmM5zURS2ON4E5eQQyD8sQGcQ7B79miCQ5EZ9wVYL6qSNayFFFQ6Io%2F48qSANppItYqUKJTqFDzmeBqqAHymF8Od%2Fd%2BN3pLJGOis%2BAwSA6dF9dUhjsSsOUio1mSClollW2GBfFvULp2Bfeqi%2B1ND70gXd4Sqip%2Fb%2BoIfjscPYh5TPTTP6GDRnqzFhK5lZ4RbBIgwk1LQFRnhto0ZqyyIl%2B1NklEtWRlVW8aFaEXJioTqz02Ss%2BojEmqqoXzAFdRm7jG9ZaSI2foeraikVQ8seI6wWckWVaTM1LZe%2BXUKofo3Xqe%2FY%2FkXOYYpOx8k4vh7%2FGNwZ6j8kiZ07q7xU3ni%2FrFsdSF1BbEmLpjDS%2BWDXbJ3JubZ3PPdF8n2OSRvFFihTDbpPe8BjqkAarqn1MOsJurrl5UvTDI%2FII2GR5%2FsQWEPVOwBLicnPrd5wIhlP%2FXcQ1kWpl2TffFHInaEYGz4npAomk322FBDBh38boFVh2d0uVPAemtufGCS3EgFGFCfthOrdjmcWpp0kELnmjhWfqDZdHdFGneR7n%2FT33kOjDnYqfSKmwaLyCKyjcUoqjUEkl4PfEZtmBjfelBL3oSZqgRloFfY7opQSXM23IF&X-Amz-Signature=fafb187ff81e93863b1a86d7be487783459cb18497138780042b84515bbc3949&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQQGNPW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIhKYiEY%2FgXxDZD7tcKUQaQQdTBWDrbhv1tRj9ZdvwQIhAIsmaUiuo5LHSeRSsLhog9pCqT3ghrHXXgz4nSQIXKKbKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4gu1krqJ6GqGBpuUq3AMPDwtjfrTMKe8csjXr31SCiSO%2FVkGwjxTSwzrYSog1%2BjWy4EOw81c8S5GCrGzRT6Wu0A%2BE4qedbYqHZtFsXh%2FyAaE5rhAM9O1M0sT2uVWjAhwUHUaEXu9eOH2VcWwA%2BCDNbB3TUv3CApOg9c8EwXmYL7A54x4Cy%2FCI1HaJB1%2BGPWuZPlwXhA5yvNaGCH9LURrAxRLQGitwLF%2BELYuz1GYiEz2c4vgWuTXTPQSHmR1vgOOZ5Ve2EmpL5MneKZn6G%2BMAz6D%2FvorR3KXtcRb6HsKVrrGg0KqpcUGG1OKoyJObcklt%2BWlOMPKrtTY%2F%2FtblpEiQ0pQwuC1ykkNsURJbgjbNd9boSQml5t557kjZR4ABtV7MhfAwj52gg0FnvGzZT8iikM%2FiguFXcAHXDPXI21EFxZOiAU3dRYJW5nZmZ67usTW61FmkvJYSdcNPrIL4263WNdQhASAB%2BZsDmgdLHn61JN3qN7l3b2HvqJAFuEKriLyBiZC0helGaWF8%2BFHbVLw4mq4iRUS1VXemduVYoRh7f5wb8zhoIvBy8lZstRklEQ8hqXR4YuySH%2BLEoKLrG9MvooJ04bhemOG6ey41rRcalxvTnYq8pvhBQ4nhkceoSjR1hsvS9n%2B8bF6MmTDJpPe8BjqkAdFnD5r8Z61RjzTyNQ3Q4MhOx9vNs0NB61SDjPGSTEncicsM9Ji39zbdz0g93Xj%2BWIDsOINALrLDKJFyoOz8rQpgpWHs1bjT%2FIlR5ZgreoPftBicxlLOgSGPLlgp6zizKdQ%2Fk0qXPcDq4t0cAyODW6Rb0LTekDkGWnGEO37FGI0f6gIwGyzcjItoCxmV231V38X36ucBX2a66oIZdNLdoz06Ke5D&X-Amz-Signature=daed2ad7100ce61565c2141c2841df873789985355c53f3b9e3ec2f0f2d4b9fa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQQGNPW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIhKYiEY%2FgXxDZD7tcKUQaQQdTBWDrbhv1tRj9ZdvwQIhAIsmaUiuo5LHSeRSsLhog9pCqT3ghrHXXgz4nSQIXKKbKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4gu1krqJ6GqGBpuUq3AMPDwtjfrTMKe8csjXr31SCiSO%2FVkGwjxTSwzrYSog1%2BjWy4EOw81c8S5GCrGzRT6Wu0A%2BE4qedbYqHZtFsXh%2FyAaE5rhAM9O1M0sT2uVWjAhwUHUaEXu9eOH2VcWwA%2BCDNbB3TUv3CApOg9c8EwXmYL7A54x4Cy%2FCI1HaJB1%2BGPWuZPlwXhA5yvNaGCH9LURrAxRLQGitwLF%2BELYuz1GYiEz2c4vgWuTXTPQSHmR1vgOOZ5Ve2EmpL5MneKZn6G%2BMAz6D%2FvorR3KXtcRb6HsKVrrGg0KqpcUGG1OKoyJObcklt%2BWlOMPKrtTY%2F%2FtblpEiQ0pQwuC1ykkNsURJbgjbNd9boSQml5t557kjZR4ABtV7MhfAwj52gg0FnvGzZT8iikM%2FiguFXcAHXDPXI21EFxZOiAU3dRYJW5nZmZ67usTW61FmkvJYSdcNPrIL4263WNdQhASAB%2BZsDmgdLHn61JN3qN7l3b2HvqJAFuEKriLyBiZC0helGaWF8%2BFHbVLw4mq4iRUS1VXemduVYoRh7f5wb8zhoIvBy8lZstRklEQ8hqXR4YuySH%2BLEoKLrG9MvooJ04bhemOG6ey41rRcalxvTnYq8pvhBQ4nhkceoSjR1hsvS9n%2B8bF6MmTDJpPe8BjqkAdFnD5r8Z61RjzTyNQ3Q4MhOx9vNs0NB61SDjPGSTEncicsM9Ji39zbdz0g93Xj%2BWIDsOINALrLDKJFyoOz8rQpgpWHs1bjT%2FIlR5ZgreoPftBicxlLOgSGPLlgp6zizKdQ%2Fk0qXPcDq4t0cAyODW6Rb0LTekDkGWnGEO37FGI0f6gIwGyzcjItoCxmV231V38X36ucBX2a66oIZdNLdoz06Ke5D&X-Amz-Signature=f2f9eff6897464d73b4952e418bdac359ae0a08783e580a8b1fa744ba83e6ca8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQQGNPW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIhKYiEY%2FgXxDZD7tcKUQaQQdTBWDrbhv1tRj9ZdvwQIhAIsmaUiuo5LHSeRSsLhog9pCqT3ghrHXXgz4nSQIXKKbKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4gu1krqJ6GqGBpuUq3AMPDwtjfrTMKe8csjXr31SCiSO%2FVkGwjxTSwzrYSog1%2BjWy4EOw81c8S5GCrGzRT6Wu0A%2BE4qedbYqHZtFsXh%2FyAaE5rhAM9O1M0sT2uVWjAhwUHUaEXu9eOH2VcWwA%2BCDNbB3TUv3CApOg9c8EwXmYL7A54x4Cy%2FCI1HaJB1%2BGPWuZPlwXhA5yvNaGCH9LURrAxRLQGitwLF%2BELYuz1GYiEz2c4vgWuTXTPQSHmR1vgOOZ5Ve2EmpL5MneKZn6G%2BMAz6D%2FvorR3KXtcRb6HsKVrrGg0KqpcUGG1OKoyJObcklt%2BWlOMPKrtTY%2F%2FtblpEiQ0pQwuC1ykkNsURJbgjbNd9boSQml5t557kjZR4ABtV7MhfAwj52gg0FnvGzZT8iikM%2FiguFXcAHXDPXI21EFxZOiAU3dRYJW5nZmZ67usTW61FmkvJYSdcNPrIL4263WNdQhASAB%2BZsDmgdLHn61JN3qN7l3b2HvqJAFuEKriLyBiZC0helGaWF8%2BFHbVLw4mq4iRUS1VXemduVYoRh7f5wb8zhoIvBy8lZstRklEQ8hqXR4YuySH%2BLEoKLrG9MvooJ04bhemOG6ey41rRcalxvTnYq8pvhBQ4nhkceoSjR1hsvS9n%2B8bF6MmTDJpPe8BjqkAdFnD5r8Z61RjzTyNQ3Q4MhOx9vNs0NB61SDjPGSTEncicsM9Ji39zbdz0g93Xj%2BWIDsOINALrLDKJFyoOz8rQpgpWHs1bjT%2FIlR5ZgreoPftBicxlLOgSGPLlgp6zizKdQ%2Fk0qXPcDq4t0cAyODW6Rb0LTekDkGWnGEO37FGI0f6gIwGyzcjItoCxmV231V38X36ucBX2a66oIZdNLdoz06Ke5D&X-Amz-Signature=60f88da9254863f9a8d2325ade6b8b9c980bf5827f32a50d7fe903171241f4e5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQQGNPW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIhKYiEY%2FgXxDZD7tcKUQaQQdTBWDrbhv1tRj9ZdvwQIhAIsmaUiuo5LHSeRSsLhog9pCqT3ghrHXXgz4nSQIXKKbKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4gu1krqJ6GqGBpuUq3AMPDwtjfrTMKe8csjXr31SCiSO%2FVkGwjxTSwzrYSog1%2BjWy4EOw81c8S5GCrGzRT6Wu0A%2BE4qedbYqHZtFsXh%2FyAaE5rhAM9O1M0sT2uVWjAhwUHUaEXu9eOH2VcWwA%2BCDNbB3TUv3CApOg9c8EwXmYL7A54x4Cy%2FCI1HaJB1%2BGPWuZPlwXhA5yvNaGCH9LURrAxRLQGitwLF%2BELYuz1GYiEz2c4vgWuTXTPQSHmR1vgOOZ5Ve2EmpL5MneKZn6G%2BMAz6D%2FvorR3KXtcRb6HsKVrrGg0KqpcUGG1OKoyJObcklt%2BWlOMPKrtTY%2F%2FtblpEiQ0pQwuC1ykkNsURJbgjbNd9boSQml5t557kjZR4ABtV7MhfAwj52gg0FnvGzZT8iikM%2FiguFXcAHXDPXI21EFxZOiAU3dRYJW5nZmZ67usTW61FmkvJYSdcNPrIL4263WNdQhASAB%2BZsDmgdLHn61JN3qN7l3b2HvqJAFuEKriLyBiZC0helGaWF8%2BFHbVLw4mq4iRUS1VXemduVYoRh7f5wb8zhoIvBy8lZstRklEQ8hqXR4YuySH%2BLEoKLrG9MvooJ04bhemOG6ey41rRcalxvTnYq8pvhBQ4nhkceoSjR1hsvS9n%2B8bF6MmTDJpPe8BjqkAdFnD5r8Z61RjzTyNQ3Q4MhOx9vNs0NB61SDjPGSTEncicsM9Ji39zbdz0g93Xj%2BWIDsOINALrLDKJFyoOz8rQpgpWHs1bjT%2FIlR5ZgreoPftBicxlLOgSGPLlgp6zizKdQ%2Fk0qXPcDq4t0cAyODW6Rb0LTekDkGWnGEO37FGI0f6gIwGyzcjItoCxmV231V38X36ucBX2a66oIZdNLdoz06Ke5D&X-Amz-Signature=adf078a0ce3f606edd3a6dadd18cc85e7ada7735f0735b8dc1765430794859fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TQQGNPW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIhKYiEY%2FgXxDZD7tcKUQaQQdTBWDrbhv1tRj9ZdvwQIhAIsmaUiuo5LHSeRSsLhog9pCqT3ghrHXXgz4nSQIXKKbKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4gu1krqJ6GqGBpuUq3AMPDwtjfrTMKe8csjXr31SCiSO%2FVkGwjxTSwzrYSog1%2BjWy4EOw81c8S5GCrGzRT6Wu0A%2BE4qedbYqHZtFsXh%2FyAaE5rhAM9O1M0sT2uVWjAhwUHUaEXu9eOH2VcWwA%2BCDNbB3TUv3CApOg9c8EwXmYL7A54x4Cy%2FCI1HaJB1%2BGPWuZPlwXhA5yvNaGCH9LURrAxRLQGitwLF%2BELYuz1GYiEz2c4vgWuTXTPQSHmR1vgOOZ5Ve2EmpL5MneKZn6G%2BMAz6D%2FvorR3KXtcRb6HsKVrrGg0KqpcUGG1OKoyJObcklt%2BWlOMPKrtTY%2F%2FtblpEiQ0pQwuC1ykkNsURJbgjbNd9boSQml5t557kjZR4ABtV7MhfAwj52gg0FnvGzZT8iikM%2FiguFXcAHXDPXI21EFxZOiAU3dRYJW5nZmZ67usTW61FmkvJYSdcNPrIL4263WNdQhASAB%2BZsDmgdLHn61JN3qN7l3b2HvqJAFuEKriLyBiZC0helGaWF8%2BFHbVLw4mq4iRUS1VXemduVYoRh7f5wb8zhoIvBy8lZstRklEQ8hqXR4YuySH%2BLEoKLrG9MvooJ04bhemOG6ey41rRcalxvTnYq8pvhBQ4nhkceoSjR1hsvS9n%2B8bF6MmTDJpPe8BjqkAdFnD5r8Z61RjzTyNQ3Q4MhOx9vNs0NB61SDjPGSTEncicsM9Ji39zbdz0g93Xj%2BWIDsOINALrLDKJFyoOz8rQpgpWHs1bjT%2FIlR5ZgreoPftBicxlLOgSGPLlgp6zizKdQ%2Fk0qXPcDq4t0cAyODW6Rb0LTekDkGWnGEO37FGI0f6gIwGyzcjItoCxmV231V38X36ucBX2a66oIZdNLdoz06Ke5D&X-Amz-Signature=f26b15433047ee5e26e875e35a49dac4296e2caf9a162ca2517862c2a2ae3aef&X-Amz-SignedHeaders=host&x-id=GetObject)
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


