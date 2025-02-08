

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=31e10ee68ec1aced043b74b93c68f23716010e659ae55959af25e01116ab41e4&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=8d7a3c28cbf1b5eb9d2bb32482ccab7bce0a9b2e379c035f08dbc362f8e0418e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=6c87cee5b98b1f8f5091871d78a0226827547fc9cb5eefe3c98719faa860e8c9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=937ccfb93e2d5f02910b9231c4abb00a43f48e259c0653705a6ee14d255ca21b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=11900faabf48bd68fe72623cdbc22ddf142d39c71d450ecf9b52aff5088e2cbb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=33196ed9c7f2056edf109c15d3d79a0286074aac60e866dc5a8cc8b21cd75170&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=49588cefa131d1ed5cc9e4c45d79abcafb48a07565b5a1d07dc5661f26e45f1d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=42d831823365eaeb42b4ba4838dfcacba8f878c8dacaf79684d36f2634c924a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=115d2b68907909125c11d82baa1dd72e9606802dee6dd2ba6c5c83ac597ebaa0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=25882379b772f77a793b6fcfcb765a6620433b1df0f85d032f57f4d258e49514&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAJYX77Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIEspctG6YSkY5iL8PlQDXY0N30fk4VlyVi4AKWjEnrOjAiEAv8iDawRczBEaNtKxfY1b4ZeBRGWB5Z3GbnME7BB33ywqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiqmbhwNIqYzNEASircA6CJbAMWhXJRrBm7z8HcZnkbRDnIbyMsqOqMXWhfzQwMytD8wOhEWwpFRoU3WprDkYG4HF6OM9XdVCaZq%2B805z3Ibtu1%2FEuwVM3mTuPWm13P6YPjQSs9poc%2FJNgUWgki04nUW%2F4LcMnGv4ciOna%2FmznZSGbjumTTc%2BmDaMW0Jlz%2BNTKkeZBdGiNuPIkU8A%2B%2BY5VuBm6uKhz0AIyjvq4kT%2Byu0i4btfWriZyyB9LuwyoOIKl0Br6hpsxX8OHsWFaFA%2BF3SScPwu7uF3L%2FaWDZ%2BGILvEP9WaB%2BKaQr3YJoK9J7ORHkBtiYzJ8UIIWYYwobjUXmPhngtfI%2F1WZzh0gdebycZhtUn0z0i1GRJMmjxAualtnYYi5wIZu0yqWK7ysJlDeFkj%2FO0sXdRRKH5vJd2nBYZkt5FLaGK97BktqGHie7h0af7cgN93tX9CoitsPs%2F22aMDLzUft5sJJme6KKJBusEHFg6E681n67WYbUM%2BUcgXTlV32p4pIbvReki%2Fzq0DNO7sMJtlr8M9bGg9FiFMPAKwkGb3b8PLnLN6Hi82fejyhmQlxYcSTSOtKHo5lB%2Bv1dPxf42GpJVFOCzoSN8%2BYxuKLEU4c2iKkobK9syudTuYIC%2F8BOIcPfluGDMMi%2Bmr0GOqUB3mot8RbP8u7U8wsQ4vxNVFgoANbFqkuxIijf1vZNQV6R%2B6XxBvKPQThS7rUbu%2B4tB25ZHSLWD5aegnRUyycq8NEehqfHRwsVci6%2FMEOTzK2HSQF7oT%2Frn%2BOiYcQ%2BBYrHLUv47fpTbZmVT%2BQqnk3AzDNgvf%2F6%2FtdX1eUMMhpetFsdBEOabbFYrIlZykYhzp4mcunYDaJ%2B5e9CTc4iHTwNSPds15vt&X-Amz-Signature=411f52293f6be606702f4d5f4fb1dc66b5d4d067a2207bf206c9024811ff9045&X-Amz-SignedHeaders=host&x-id=GetObject)
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


