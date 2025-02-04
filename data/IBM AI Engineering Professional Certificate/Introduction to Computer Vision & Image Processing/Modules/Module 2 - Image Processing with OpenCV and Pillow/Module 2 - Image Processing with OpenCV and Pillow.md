

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622HK5HSV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEUL6Gjg4TVhuqugWxuOuHFGqR5NcY2i%2BbyZaiqa7nbeAiEAzTUDU6X5zuMAwUGxKRNZenAlfBwAqIqH78SBzuyLFvQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDGCgk%2FBYqM4ID7eueyrcA5b9KfEDKYYNL2HRluzUS%2BBLkoO8NgZZpkro%2Fwse7%2FpbsSaEjUqwOAYdTksP%2B2ozpbU3CZ%2FRXW4kztn66EcLxkP%2Bn8Rtm9ZL6ijvfdXYO%2BlrUdtpvLTe79D3hhVk6vLsCdaaL4hHjrSz1GFN7cDrItzzqploNa6b8YP2mCe%2BVLC7W4Hq7vYb5AnP6OlWYV2A8tHoGJiDeG5gkt56FYXHSGiH30bJ0ufFakQWKcNR6%2BBjR8EyItfyyNwxB33uH7IME8aWOUOwYB3%2F%2FhAXE%2Bh2ZM%2F7OUDqCNY07piQQhnaX0GDxdQyVoMrKCccvuUBPZ47lz76Y4e5leFvj1zo%2BPPxg%2FS3puChdDeibHUusC8KziBxYxJR04vjC1UEUGZhZ6Cf5fGXGoSIWlR%2F5h2aEpP3ehtVlypeKpyzegvnrfZVKjhglLlqulr1wgXbvWmFZkQC%2F9r8cF%2FytiY8Yvl5J%2Bpvc0bXA8aJy4uMs4tisqMe2Q5Ygt4BuvzGmSmVhfVgjFRKqx32FVLqnDUEpH6SEzA28SUOmjF5WZLVhT8%2Fy%2Fc9FO%2BOzjwTgvniyTlwvhd6%2Fx3WAFDwmGbPuGYKALdbQ1UoRsH22UIp%2FOXLc3DX816vNDtUIsIZ9%2BVyQ%2F8hJgaTMPSDib0GOqUBS79RiW68H%2FnrFSexpg6cV6IqBrvBXrXbvioe0AnT6wvzNeU%2BemciT2Zh82YAuLHfQpwgTjm8zHbXjCExA0pfAE9S97Yl1ICmO0KwOzP1thiZPMzeUILnIhy1IXzW71W4D2lHZJ35RepQwOQWQ%2BN%2FWEogmpwXeY6ffz0t8q9RcatbC9booUSIaLo5HVkdUCs8FtZ5DWa52bTdgU4y9Op67YEUQ91o&X-Amz-Signature=0b74e40dc1c1682c2f56c9af539c35aaaf1b63ec849fa9b9ce704b2e25f41cdd&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=95849878d17e598387c94ae0fdbcad9b7696d9cb8bd8f8f885508498114321f3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=4932e92ce58e3504b19a704134800165b6e8dc80c6f45a57f99d66434559db1e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=ab78b9ada64df5525c77c69b66899176a1639d0dafc4442be9724c34e82a8a8c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=52eeb064d08f3ce8c6819c2fc2201540fc4b35da6f5e8d513511c581ff67ddc2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=d481a40b0b82dfb3a356c2014614030211a75b9e11eb3a49c852f41cd0d3133b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622HK5HSV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEUL6Gjg4TVhuqugWxuOuHFGqR5NcY2i%2BbyZaiqa7nbeAiEAzTUDU6X5zuMAwUGxKRNZenAlfBwAqIqH78SBzuyLFvQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDGCgk%2FBYqM4ID7eueyrcA5b9KfEDKYYNL2HRluzUS%2BBLkoO8NgZZpkro%2Fwse7%2FpbsSaEjUqwOAYdTksP%2B2ozpbU3CZ%2FRXW4kztn66EcLxkP%2Bn8Rtm9ZL6ijvfdXYO%2BlrUdtpvLTe79D3hhVk6vLsCdaaL4hHjrSz1GFN7cDrItzzqploNa6b8YP2mCe%2BVLC7W4Hq7vYb5AnP6OlWYV2A8tHoGJiDeG5gkt56FYXHSGiH30bJ0ufFakQWKcNR6%2BBjR8EyItfyyNwxB33uH7IME8aWOUOwYB3%2F%2FhAXE%2Bh2ZM%2F7OUDqCNY07piQQhnaX0GDxdQyVoMrKCccvuUBPZ47lz76Y4e5leFvj1zo%2BPPxg%2FS3puChdDeibHUusC8KziBxYxJR04vjC1UEUGZhZ6Cf5fGXGoSIWlR%2F5h2aEpP3ehtVlypeKpyzegvnrfZVKjhglLlqulr1wgXbvWmFZkQC%2F9r8cF%2FytiY8Yvl5J%2Bpvc0bXA8aJy4uMs4tisqMe2Q5Ygt4BuvzGmSmVhfVgjFRKqx32FVLqnDUEpH6SEzA28SUOmjF5WZLVhT8%2Fy%2Fc9FO%2BOzjwTgvniyTlwvhd6%2Fx3WAFDwmGbPuGYKALdbQ1UoRsH22UIp%2FOXLc3DX816vNDtUIsIZ9%2BVyQ%2F8hJgaTMPSDib0GOqUBS79RiW68H%2FnrFSexpg6cV6IqBrvBXrXbvioe0AnT6wvzNeU%2BemciT2Zh82YAuLHfQpwgTjm8zHbXjCExA0pfAE9S97Yl1ICmO0KwOzP1thiZPMzeUILnIhy1IXzW71W4D2lHZJ35RepQwOQWQ%2BN%2FWEogmpwXeY6ffz0t8q9RcatbC9booUSIaLo5HVkdUCs8FtZ5DWa52bTdgU4y9Op67YEUQ91o&X-Amz-Signature=8a2d097b3aece090e2b3fa4f77b345f0975d227c11636a8b83f2a726b17b7ce8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622HK5HSV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEUL6Gjg4TVhuqugWxuOuHFGqR5NcY2i%2BbyZaiqa7nbeAiEAzTUDU6X5zuMAwUGxKRNZenAlfBwAqIqH78SBzuyLFvQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDGCgk%2FBYqM4ID7eueyrcA5b9KfEDKYYNL2HRluzUS%2BBLkoO8NgZZpkro%2Fwse7%2FpbsSaEjUqwOAYdTksP%2B2ozpbU3CZ%2FRXW4kztn66EcLxkP%2Bn8Rtm9ZL6ijvfdXYO%2BlrUdtpvLTe79D3hhVk6vLsCdaaL4hHjrSz1GFN7cDrItzzqploNa6b8YP2mCe%2BVLC7W4Hq7vYb5AnP6OlWYV2A8tHoGJiDeG5gkt56FYXHSGiH30bJ0ufFakQWKcNR6%2BBjR8EyItfyyNwxB33uH7IME8aWOUOwYB3%2F%2FhAXE%2Bh2ZM%2F7OUDqCNY07piQQhnaX0GDxdQyVoMrKCccvuUBPZ47lz76Y4e5leFvj1zo%2BPPxg%2FS3puChdDeibHUusC8KziBxYxJR04vjC1UEUGZhZ6Cf5fGXGoSIWlR%2F5h2aEpP3ehtVlypeKpyzegvnrfZVKjhglLlqulr1wgXbvWmFZkQC%2F9r8cF%2FytiY8Yvl5J%2Bpvc0bXA8aJy4uMs4tisqMe2Q5Ygt4BuvzGmSmVhfVgjFRKqx32FVLqnDUEpH6SEzA28SUOmjF5WZLVhT8%2Fy%2Fc9FO%2BOzjwTgvniyTlwvhd6%2Fx3WAFDwmGbPuGYKALdbQ1UoRsH22UIp%2FOXLc3DX816vNDtUIsIZ9%2BVyQ%2F8hJgaTMPSDib0GOqUBS79RiW68H%2FnrFSexpg6cV6IqBrvBXrXbvioe0AnT6wvzNeU%2BemciT2Zh82YAuLHfQpwgTjm8zHbXjCExA0pfAE9S97Yl1ICmO0KwOzP1thiZPMzeUILnIhy1IXzW71W4D2lHZJ35RepQwOQWQ%2BN%2FWEogmpwXeY6ffz0t8q9RcatbC9booUSIaLo5HVkdUCs8FtZ5DWa52bTdgU4y9Op67YEUQ91o&X-Amz-Signature=3f1fcc4abbfe9c947ecf7d5bbe29efee91b6d290d3200dcc5764ae9c8e0b5818&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622HK5HSV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEUL6Gjg4TVhuqugWxuOuHFGqR5NcY2i%2BbyZaiqa7nbeAiEAzTUDU6X5zuMAwUGxKRNZenAlfBwAqIqH78SBzuyLFvQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDGCgk%2FBYqM4ID7eueyrcA5b9KfEDKYYNL2HRluzUS%2BBLkoO8NgZZpkro%2Fwse7%2FpbsSaEjUqwOAYdTksP%2B2ozpbU3CZ%2FRXW4kztn66EcLxkP%2Bn8Rtm9ZL6ijvfdXYO%2BlrUdtpvLTe79D3hhVk6vLsCdaaL4hHjrSz1GFN7cDrItzzqploNa6b8YP2mCe%2BVLC7W4Hq7vYb5AnP6OlWYV2A8tHoGJiDeG5gkt56FYXHSGiH30bJ0ufFakQWKcNR6%2BBjR8EyItfyyNwxB33uH7IME8aWOUOwYB3%2F%2FhAXE%2Bh2ZM%2F7OUDqCNY07piQQhnaX0GDxdQyVoMrKCccvuUBPZ47lz76Y4e5leFvj1zo%2BPPxg%2FS3puChdDeibHUusC8KziBxYxJR04vjC1UEUGZhZ6Cf5fGXGoSIWlR%2F5h2aEpP3ehtVlypeKpyzegvnrfZVKjhglLlqulr1wgXbvWmFZkQC%2F9r8cF%2FytiY8Yvl5J%2Bpvc0bXA8aJy4uMs4tisqMe2Q5Ygt4BuvzGmSmVhfVgjFRKqx32FVLqnDUEpH6SEzA28SUOmjF5WZLVhT8%2Fy%2Fc9FO%2BOzjwTgvniyTlwvhd6%2Fx3WAFDwmGbPuGYKALdbQ1UoRsH22UIp%2FOXLc3DX816vNDtUIsIZ9%2BVyQ%2F8hJgaTMPSDib0GOqUBS79RiW68H%2FnrFSexpg6cV6IqBrvBXrXbvioe0AnT6wvzNeU%2BemciT2Zh82YAuLHfQpwgTjm8zHbXjCExA0pfAE9S97Yl1ICmO0KwOzP1thiZPMzeUILnIhy1IXzW71W4D2lHZJ35RepQwOQWQ%2BN%2FWEogmpwXeY6ffz0t8q9RcatbC9booUSIaLo5HVkdUCs8FtZ5DWa52bTdgU4y9Op67YEUQ91o&X-Amz-Signature=5c415ff0cbd652a386ff78e4302e9cc982ca5a97c52d970e4e909ec90b037afa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622HK5HSV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEUL6Gjg4TVhuqugWxuOuHFGqR5NcY2i%2BbyZaiqa7nbeAiEAzTUDU6X5zuMAwUGxKRNZenAlfBwAqIqH78SBzuyLFvQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDGCgk%2FBYqM4ID7eueyrcA5b9KfEDKYYNL2HRluzUS%2BBLkoO8NgZZpkro%2Fwse7%2FpbsSaEjUqwOAYdTksP%2B2ozpbU3CZ%2FRXW4kztn66EcLxkP%2Bn8Rtm9ZL6ijvfdXYO%2BlrUdtpvLTe79D3hhVk6vLsCdaaL4hHjrSz1GFN7cDrItzzqploNa6b8YP2mCe%2BVLC7W4Hq7vYb5AnP6OlWYV2A8tHoGJiDeG5gkt56FYXHSGiH30bJ0ufFakQWKcNR6%2BBjR8EyItfyyNwxB33uH7IME8aWOUOwYB3%2F%2FhAXE%2Bh2ZM%2F7OUDqCNY07piQQhnaX0GDxdQyVoMrKCccvuUBPZ47lz76Y4e5leFvj1zo%2BPPxg%2FS3puChdDeibHUusC8KziBxYxJR04vjC1UEUGZhZ6Cf5fGXGoSIWlR%2F5h2aEpP3ehtVlypeKpyzegvnrfZVKjhglLlqulr1wgXbvWmFZkQC%2F9r8cF%2FytiY8Yvl5J%2Bpvc0bXA8aJy4uMs4tisqMe2Q5Ygt4BuvzGmSmVhfVgjFRKqx32FVLqnDUEpH6SEzA28SUOmjF5WZLVhT8%2Fy%2Fc9FO%2BOzjwTgvniyTlwvhd6%2Fx3WAFDwmGbPuGYKALdbQ1UoRsH22UIp%2FOXLc3DX816vNDtUIsIZ9%2BVyQ%2F8hJgaTMPSDib0GOqUBS79RiW68H%2FnrFSexpg6cV6IqBrvBXrXbvioe0AnT6wvzNeU%2BemciT2Zh82YAuLHfQpwgTjm8zHbXjCExA0pfAE9S97Yl1ICmO0KwOzP1thiZPMzeUILnIhy1IXzW71W4D2lHZJ35RepQwOQWQ%2BN%2FWEogmpwXeY6ffz0t8q9RcatbC9booUSIaLo5HVkdUCs8FtZ5DWa52bTdgU4y9Op67YEUQ91o&X-Amz-Signature=8cbe363d4ed2622046a73ecde1213ebe0449fb2715572cc603809f7eab9eb786&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622HK5HSV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEUL6Gjg4TVhuqugWxuOuHFGqR5NcY2i%2BbyZaiqa7nbeAiEAzTUDU6X5zuMAwUGxKRNZenAlfBwAqIqH78SBzuyLFvQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDGCgk%2FBYqM4ID7eueyrcA5b9KfEDKYYNL2HRluzUS%2BBLkoO8NgZZpkro%2Fwse7%2FpbsSaEjUqwOAYdTksP%2B2ozpbU3CZ%2FRXW4kztn66EcLxkP%2Bn8Rtm9ZL6ijvfdXYO%2BlrUdtpvLTe79D3hhVk6vLsCdaaL4hHjrSz1GFN7cDrItzzqploNa6b8YP2mCe%2BVLC7W4Hq7vYb5AnP6OlWYV2A8tHoGJiDeG5gkt56FYXHSGiH30bJ0ufFakQWKcNR6%2BBjR8EyItfyyNwxB33uH7IME8aWOUOwYB3%2F%2FhAXE%2Bh2ZM%2F7OUDqCNY07piQQhnaX0GDxdQyVoMrKCccvuUBPZ47lz76Y4e5leFvj1zo%2BPPxg%2FS3puChdDeibHUusC8KziBxYxJR04vjC1UEUGZhZ6Cf5fGXGoSIWlR%2F5h2aEpP3ehtVlypeKpyzegvnrfZVKjhglLlqulr1wgXbvWmFZkQC%2F9r8cF%2FytiY8Yvl5J%2Bpvc0bXA8aJy4uMs4tisqMe2Q5Ygt4BuvzGmSmVhfVgjFRKqx32FVLqnDUEpH6SEzA28SUOmjF5WZLVhT8%2Fy%2Fc9FO%2BOzjwTgvniyTlwvhd6%2Fx3WAFDwmGbPuGYKALdbQ1UoRsH22UIp%2FOXLc3DX816vNDtUIsIZ9%2BVyQ%2F8hJgaTMPSDib0GOqUBS79RiW68H%2FnrFSexpg6cV6IqBrvBXrXbvioe0AnT6wvzNeU%2BemciT2Zh82YAuLHfQpwgTjm8zHbXjCExA0pfAE9S97Yl1ICmO0KwOzP1thiZPMzeUILnIhy1IXzW71W4D2lHZJ35RepQwOQWQ%2BN%2FWEogmpwXeY6ffz0t8q9RcatbC9booUSIaLo5HVkdUCs8FtZ5DWa52bTdgU4y9Op67YEUQ91o&X-Amz-Signature=86d841d07f4cc01d20d65ca0e5f56d520d04269d22b2441eb0154d7bdb673856&X-Amz-SignedHeaders=host&x-id=GetObject)
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


