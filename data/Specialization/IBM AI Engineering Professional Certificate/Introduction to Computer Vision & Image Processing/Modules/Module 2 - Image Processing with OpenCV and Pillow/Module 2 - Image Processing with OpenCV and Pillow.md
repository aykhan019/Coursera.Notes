

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YOWUO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDJrI6ApV0Lh9mT0zQqXW6JJPwXJxt2Bj%2FFNgo6eqGRwIhAMQz5JOONRj0QQNO9WnZO9FmFTD8V3VPty%2BE7Jnt%2Fu4XKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1%2ByOi4r21zFMuVBwq3APUYvufHwmCpUTXG2vw6xJC22xkc07T1rphN4ubMnU6XRgLQuQGS6njhFAknL6NJdB%2FgKrllFr5DiqqlubDf3HqMWqAiWi3i7Y0ZQ5SS%2FYF5V4Ja4KKuOdyjyKzBdNwSwZ59rLXog5iuW1SByHEVO8EI5Pj8exeMHSLzQR%2FbSfVtCEPdcYLNxwn0aLts0hPCKkuGwgSH0bllFAhHUBBaB5KkXq5SoZBI%2BmtaYcCq%2FNuS3Hgaq0MotfxiDhRN3tDpFWdzz3isqMSQJj36Zx1sJkY674jVOLexyKEx2PpqkfvmtH965qSUimu8lQvnKqLLXzR8TT6HxncSgOuGDv4BnlXadDiCJ7t6h8BFwZgKIYdg%2Bg4Jeh3ialEbpExIcQ7eyk9riFe49wZ3SOmcYRmHSlojPYlVDgctm4MAmLw2vZ6wRafjXAj6J6eQHZBm8SvNgiGnzCCo3k5Kur29qjm1ciKNes1iNuPQ6i2Z8JbIw5AAX54gsvQ6irvKbPFj6Ub8AgOSjgO1Hu7oKeUOK2nX1HSk5WeslbtmK3MMk8JDfAYfy5uoxvJy64b3ULwboRQ6pbbHoihz%2FH8yTGuuA1B98cA2YVX3CQHh%2Bh%2BWwHzNvILP3P%2BNhJ9HxARhH0j0zC%2Bi%2B28BjqkAaEni0wvdTpmkWeF268Im7hHab4ZmsDWnl6lbXBoiU6QIclTSx61OjfutsdYHGpmsfVSIYFTC1G2PxEql3wDi%2B6nuxLswtpcnTg%2FxsmqGtr51xyHc9JCzYuD3W9jQQ4BXr4Z7ffk21puzDihy5FCA56Pn93PMmKUQqCJxd4XRe8Y4Np%2FB25vh8EdZAhOgWQJRydoNd0%2BU4Yut3gkHG6wBnk0BUYn&X-Amz-Signature=208b3386ae74cd9ec145c57567f318a74fcb31236432671f77da26926b439e78&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZKAA3AR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlTRePivPlm3Hwxm%2BxIjGOQuy%2FffvbEzSQWhDDOqk8ZAiEAyCbaEP61r7jQLFpt5crQ9pYpx0o7X8B9PH6trRncHzYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTcV97l5pbfHGfuzyrcAzo4sL%2F57N1G4QgA9hVjZ4%2BIxt3PCy5HC5DTwlI8yzbvKD9wK4KdKPqnquo4sccTcICfja4%2BgZC7QIhr%2FF4QyRGz9y4fuSbx2HDt7HNiqNoisGQJjSz6dbzJTpl2pWKR3QTJbNOFXmpfal3p19%2Fhgke50QzGrADWQxOnP9sb2p50cmhceXwThuo5xwK2iIgxKmkQJ0vkW7sHFN%2F8Do2X33DYCqHbuDLZPzsQfkm5p5GojWdeWsYfr4BhsPV3abWtQbKiJftcBNNv6q%2FP3WrjcdURNdyIiYcWn16AXKX1NUxxVGAT21vYkgA8gbdQpOr7DheUU6dwDMpTPj%2F%2Foex%2FVIXhLO6SffFUfDgP0r3CNgNSescQKYarQ4XO4UjbsbeR%2B%2F%2FfRp2DwS7S8Gvm%2BMjDFFhgPjOH34TB%2FhnbAgrTNXNZu0hYyniHZMI44XKqNJdBNePdjq%2BT0wxn%2FxWsSOvDpeLGxOq5fQPKA2P97KPEo9OqIOVHOBcTlpaKdqmsnqPVBT0PGua0PCrQdy%2FY9bYVfWY88StQ8KFXXwWPwIT56d0MbcdKH6dzVJ%2F%2F%2F1l2%2Bfi%2FsbGg1d4dFwidaDcLNAqz7jTYaz41cKMV%2FShfhXD0vH8HMdqYjUM7uA0bVbnuMNuK7bwGOqUBP9N0pL8ptDTXraYI6U6dk66KZ3%2BtC3LoIclwTi%2Fb4RTWYcf9Qz%2BwLrsH4ygZ2GYvB%2FmwgrSwfJdgwLyZ%2Bc9qrlI52bcJ2wEiQ8PdOGQh3kScv1U4B4bLWm5w0fWab%2BSyprHiqOCNIDYzJ5L67nh8InPw%2FetajXeaAHkNYlQ3RFjumF3rISpeAiJvmfJIoKW5yl7mIFm8s781C1YVTiLeIVdm2HbE&X-Amz-Signature=07400e29e7198be038444c3dd7c6c8c32238c1ab0cc455cb0ea304cc286e72b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZKAA3AR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlTRePivPlm3Hwxm%2BxIjGOQuy%2FffvbEzSQWhDDOqk8ZAiEAyCbaEP61r7jQLFpt5crQ9pYpx0o7X8B9PH6trRncHzYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTcV97l5pbfHGfuzyrcAzo4sL%2F57N1G4QgA9hVjZ4%2BIxt3PCy5HC5DTwlI8yzbvKD9wK4KdKPqnquo4sccTcICfja4%2BgZC7QIhr%2FF4QyRGz9y4fuSbx2HDt7HNiqNoisGQJjSz6dbzJTpl2pWKR3QTJbNOFXmpfal3p19%2Fhgke50QzGrADWQxOnP9sb2p50cmhceXwThuo5xwK2iIgxKmkQJ0vkW7sHFN%2F8Do2X33DYCqHbuDLZPzsQfkm5p5GojWdeWsYfr4BhsPV3abWtQbKiJftcBNNv6q%2FP3WrjcdURNdyIiYcWn16AXKX1NUxxVGAT21vYkgA8gbdQpOr7DheUU6dwDMpTPj%2F%2Foex%2FVIXhLO6SffFUfDgP0r3CNgNSescQKYarQ4XO4UjbsbeR%2B%2F%2FfRp2DwS7S8Gvm%2BMjDFFhgPjOH34TB%2FhnbAgrTNXNZu0hYyniHZMI44XKqNJdBNePdjq%2BT0wxn%2FxWsSOvDpeLGxOq5fQPKA2P97KPEo9OqIOVHOBcTlpaKdqmsnqPVBT0PGua0PCrQdy%2FY9bYVfWY88StQ8KFXXwWPwIT56d0MbcdKH6dzVJ%2F%2F%2F1l2%2Bfi%2FsbGg1d4dFwidaDcLNAqz7jTYaz41cKMV%2FShfhXD0vH8HMdqYjUM7uA0bVbnuMNuK7bwGOqUBP9N0pL8ptDTXraYI6U6dk66KZ3%2BtC3LoIclwTi%2Fb4RTWYcf9Qz%2BwLrsH4ygZ2GYvB%2FmwgrSwfJdgwLyZ%2Bc9qrlI52bcJ2wEiQ8PdOGQh3kScv1U4B4bLWm5w0fWab%2BSyprHiqOCNIDYzJ5L67nh8InPw%2FetajXeaAHkNYlQ3RFjumF3rISpeAiJvmfJIoKW5yl7mIFm8s781C1YVTiLeIVdm2HbE&X-Amz-Signature=8ea6d870de23dec2498b220528a1bbcfc32e1e2fbead5f8fd1f540c11ea6369d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZKAA3AR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlTRePivPlm3Hwxm%2BxIjGOQuy%2FffvbEzSQWhDDOqk8ZAiEAyCbaEP61r7jQLFpt5crQ9pYpx0o7X8B9PH6trRncHzYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTcV97l5pbfHGfuzyrcAzo4sL%2F57N1G4QgA9hVjZ4%2BIxt3PCy5HC5DTwlI8yzbvKD9wK4KdKPqnquo4sccTcICfja4%2BgZC7QIhr%2FF4QyRGz9y4fuSbx2HDt7HNiqNoisGQJjSz6dbzJTpl2pWKR3QTJbNOFXmpfal3p19%2Fhgke50QzGrADWQxOnP9sb2p50cmhceXwThuo5xwK2iIgxKmkQJ0vkW7sHFN%2F8Do2X33DYCqHbuDLZPzsQfkm5p5GojWdeWsYfr4BhsPV3abWtQbKiJftcBNNv6q%2FP3WrjcdURNdyIiYcWn16AXKX1NUxxVGAT21vYkgA8gbdQpOr7DheUU6dwDMpTPj%2F%2Foex%2FVIXhLO6SffFUfDgP0r3CNgNSescQKYarQ4XO4UjbsbeR%2B%2F%2FfRp2DwS7S8Gvm%2BMjDFFhgPjOH34TB%2FhnbAgrTNXNZu0hYyniHZMI44XKqNJdBNePdjq%2BT0wxn%2FxWsSOvDpeLGxOq5fQPKA2P97KPEo9OqIOVHOBcTlpaKdqmsnqPVBT0PGua0PCrQdy%2FY9bYVfWY88StQ8KFXXwWPwIT56d0MbcdKH6dzVJ%2F%2F%2F1l2%2Bfi%2FsbGg1d4dFwidaDcLNAqz7jTYaz41cKMV%2FShfhXD0vH8HMdqYjUM7uA0bVbnuMNuK7bwGOqUBP9N0pL8ptDTXraYI6U6dk66KZ3%2BtC3LoIclwTi%2Fb4RTWYcf9Qz%2BwLrsH4ygZ2GYvB%2FmwgrSwfJdgwLyZ%2Bc9qrlI52bcJ2wEiQ8PdOGQh3kScv1U4B4bLWm5w0fWab%2BSyprHiqOCNIDYzJ5L67nh8InPw%2FetajXeaAHkNYlQ3RFjumF3rISpeAiJvmfJIoKW5yl7mIFm8s781C1YVTiLeIVdm2HbE&X-Amz-Signature=d8de3c7b0403af641cf8a725575dad0b693b7ac1511da747b2b60b2a8a10ce81&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZKAA3AR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlTRePivPlm3Hwxm%2BxIjGOQuy%2FffvbEzSQWhDDOqk8ZAiEAyCbaEP61r7jQLFpt5crQ9pYpx0o7X8B9PH6trRncHzYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTcV97l5pbfHGfuzyrcAzo4sL%2F57N1G4QgA9hVjZ4%2BIxt3PCy5HC5DTwlI8yzbvKD9wK4KdKPqnquo4sccTcICfja4%2BgZC7QIhr%2FF4QyRGz9y4fuSbx2HDt7HNiqNoisGQJjSz6dbzJTpl2pWKR3QTJbNOFXmpfal3p19%2Fhgke50QzGrADWQxOnP9sb2p50cmhceXwThuo5xwK2iIgxKmkQJ0vkW7sHFN%2F8Do2X33DYCqHbuDLZPzsQfkm5p5GojWdeWsYfr4BhsPV3abWtQbKiJftcBNNv6q%2FP3WrjcdURNdyIiYcWn16AXKX1NUxxVGAT21vYkgA8gbdQpOr7DheUU6dwDMpTPj%2F%2Foex%2FVIXhLO6SffFUfDgP0r3CNgNSescQKYarQ4XO4UjbsbeR%2B%2F%2FfRp2DwS7S8Gvm%2BMjDFFhgPjOH34TB%2FhnbAgrTNXNZu0hYyniHZMI44XKqNJdBNePdjq%2BT0wxn%2FxWsSOvDpeLGxOq5fQPKA2P97KPEo9OqIOVHOBcTlpaKdqmsnqPVBT0PGua0PCrQdy%2FY9bYVfWY88StQ8KFXXwWPwIT56d0MbcdKH6dzVJ%2F%2F%2F1l2%2Bfi%2FsbGg1d4dFwidaDcLNAqz7jTYaz41cKMV%2FShfhXD0vH8HMdqYjUM7uA0bVbnuMNuK7bwGOqUBP9N0pL8ptDTXraYI6U6dk66KZ3%2BtC3LoIclwTi%2Fb4RTWYcf9Qz%2BwLrsH4ygZ2GYvB%2FmwgrSwfJdgwLyZ%2Bc9qrlI52bcJ2wEiQ8PdOGQh3kScv1U4B4bLWm5w0fWab%2BSyprHiqOCNIDYzJ5L67nh8InPw%2FetajXeaAHkNYlQ3RFjumF3rISpeAiJvmfJIoKW5yl7mIFm8s781C1YVTiLeIVdm2HbE&X-Amz-Signature=a504997dccd22569fde46ef0f05401edc21782678a9c927d9751992c182b0317&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZKAA3AR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlTRePivPlm3Hwxm%2BxIjGOQuy%2FffvbEzSQWhDDOqk8ZAiEAyCbaEP61r7jQLFpt5crQ9pYpx0o7X8B9PH6trRncHzYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTcV97l5pbfHGfuzyrcAzo4sL%2F57N1G4QgA9hVjZ4%2BIxt3PCy5HC5DTwlI8yzbvKD9wK4KdKPqnquo4sccTcICfja4%2BgZC7QIhr%2FF4QyRGz9y4fuSbx2HDt7HNiqNoisGQJjSz6dbzJTpl2pWKR3QTJbNOFXmpfal3p19%2Fhgke50QzGrADWQxOnP9sb2p50cmhceXwThuo5xwK2iIgxKmkQJ0vkW7sHFN%2F8Do2X33DYCqHbuDLZPzsQfkm5p5GojWdeWsYfr4BhsPV3abWtQbKiJftcBNNv6q%2FP3WrjcdURNdyIiYcWn16AXKX1NUxxVGAT21vYkgA8gbdQpOr7DheUU6dwDMpTPj%2F%2Foex%2FVIXhLO6SffFUfDgP0r3CNgNSescQKYarQ4XO4UjbsbeR%2B%2F%2FfRp2DwS7S8Gvm%2BMjDFFhgPjOH34TB%2FhnbAgrTNXNZu0hYyniHZMI44XKqNJdBNePdjq%2BT0wxn%2FxWsSOvDpeLGxOq5fQPKA2P97KPEo9OqIOVHOBcTlpaKdqmsnqPVBT0PGua0PCrQdy%2FY9bYVfWY88StQ8KFXXwWPwIT56d0MbcdKH6dzVJ%2F%2F%2F1l2%2Bfi%2FsbGg1d4dFwidaDcLNAqz7jTYaz41cKMV%2FShfhXD0vH8HMdqYjUM7uA0bVbnuMNuK7bwGOqUBP9N0pL8ptDTXraYI6U6dk66KZ3%2BtC3LoIclwTi%2Fb4RTWYcf9Qz%2BwLrsH4ygZ2GYvB%2FmwgrSwfJdgwLyZ%2Bc9qrlI52bcJ2wEiQ8PdOGQh3kScv1U4B4bLWm5w0fWab%2BSyprHiqOCNIDYzJ5L67nh8InPw%2FetajXeaAHkNYlQ3RFjumF3rISpeAiJvmfJIoKW5yl7mIFm8s781C1YVTiLeIVdm2HbE&X-Amz-Signature=8ebb5295846706732a8887e70a40376f4b076bf300cc4b28472a8f00ce53a234&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YOWUO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDJrI6ApV0Lh9mT0zQqXW6JJPwXJxt2Bj%2FFNgo6eqGRwIhAMQz5JOONRj0QQNO9WnZO9FmFTD8V3VPty%2BE7Jnt%2Fu4XKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1%2ByOi4r21zFMuVBwq3APUYvufHwmCpUTXG2vw6xJC22xkc07T1rphN4ubMnU6XRgLQuQGS6njhFAknL6NJdB%2FgKrllFr5DiqqlubDf3HqMWqAiWi3i7Y0ZQ5SS%2FYF5V4Ja4KKuOdyjyKzBdNwSwZ59rLXog5iuW1SByHEVO8EI5Pj8exeMHSLzQR%2FbSfVtCEPdcYLNxwn0aLts0hPCKkuGwgSH0bllFAhHUBBaB5KkXq5SoZBI%2BmtaYcCq%2FNuS3Hgaq0MotfxiDhRN3tDpFWdzz3isqMSQJj36Zx1sJkY674jVOLexyKEx2PpqkfvmtH965qSUimu8lQvnKqLLXzR8TT6HxncSgOuGDv4BnlXadDiCJ7t6h8BFwZgKIYdg%2Bg4Jeh3ialEbpExIcQ7eyk9riFe49wZ3SOmcYRmHSlojPYlVDgctm4MAmLw2vZ6wRafjXAj6J6eQHZBm8SvNgiGnzCCo3k5Kur29qjm1ciKNes1iNuPQ6i2Z8JbIw5AAX54gsvQ6irvKbPFj6Ub8AgOSjgO1Hu7oKeUOK2nX1HSk5WeslbtmK3MMk8JDfAYfy5uoxvJy64b3ULwboRQ6pbbHoihz%2FH8yTGuuA1B98cA2YVX3CQHh%2Bh%2BWwHzNvILP3P%2BNhJ9HxARhH0j0zC%2Bi%2B28BjqkAaEni0wvdTpmkWeF268Im7hHab4ZmsDWnl6lbXBoiU6QIclTSx61OjfutsdYHGpmsfVSIYFTC1G2PxEql3wDi%2B6nuxLswtpcnTg%2FxsmqGtr51xyHc9JCzYuD3W9jQQ4BXr4Z7ffk21puzDihy5FCA56Pn93PMmKUQqCJxd4XRe8Y4Np%2FB25vh8EdZAhOgWQJRydoNd0%2BU4Yut3gkHG6wBnk0BUYn&X-Amz-Signature=338976e0bdd8bf5a780b513020d27e8e221d2280898fa78c4b6a0cb4735e71fe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YOWUO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDJrI6ApV0Lh9mT0zQqXW6JJPwXJxt2Bj%2FFNgo6eqGRwIhAMQz5JOONRj0QQNO9WnZO9FmFTD8V3VPty%2BE7Jnt%2Fu4XKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1%2ByOi4r21zFMuVBwq3APUYvufHwmCpUTXG2vw6xJC22xkc07T1rphN4ubMnU6XRgLQuQGS6njhFAknL6NJdB%2FgKrllFr5DiqqlubDf3HqMWqAiWi3i7Y0ZQ5SS%2FYF5V4Ja4KKuOdyjyKzBdNwSwZ59rLXog5iuW1SByHEVO8EI5Pj8exeMHSLzQR%2FbSfVtCEPdcYLNxwn0aLts0hPCKkuGwgSH0bllFAhHUBBaB5KkXq5SoZBI%2BmtaYcCq%2FNuS3Hgaq0MotfxiDhRN3tDpFWdzz3isqMSQJj36Zx1sJkY674jVOLexyKEx2PpqkfvmtH965qSUimu8lQvnKqLLXzR8TT6HxncSgOuGDv4BnlXadDiCJ7t6h8BFwZgKIYdg%2Bg4Jeh3ialEbpExIcQ7eyk9riFe49wZ3SOmcYRmHSlojPYlVDgctm4MAmLw2vZ6wRafjXAj6J6eQHZBm8SvNgiGnzCCo3k5Kur29qjm1ciKNes1iNuPQ6i2Z8JbIw5AAX54gsvQ6irvKbPFj6Ub8AgOSjgO1Hu7oKeUOK2nX1HSk5WeslbtmK3MMk8JDfAYfy5uoxvJy64b3ULwboRQ6pbbHoihz%2FH8yTGuuA1B98cA2YVX3CQHh%2Bh%2BWwHzNvILP3P%2BNhJ9HxARhH0j0zC%2Bi%2B28BjqkAaEni0wvdTpmkWeF268Im7hHab4ZmsDWnl6lbXBoiU6QIclTSx61OjfutsdYHGpmsfVSIYFTC1G2PxEql3wDi%2B6nuxLswtpcnTg%2FxsmqGtr51xyHc9JCzYuD3W9jQQ4BXr4Z7ffk21puzDihy5FCA56Pn93PMmKUQqCJxd4XRe8Y4Np%2FB25vh8EdZAhOgWQJRydoNd0%2BU4Yut3gkHG6wBnk0BUYn&X-Amz-Signature=01240903a02b294ecf33430809bddf8c8f726c1438eedf3311479b5f20e2f678&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YOWUO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDJrI6ApV0Lh9mT0zQqXW6JJPwXJxt2Bj%2FFNgo6eqGRwIhAMQz5JOONRj0QQNO9WnZO9FmFTD8V3VPty%2BE7Jnt%2Fu4XKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1%2ByOi4r21zFMuVBwq3APUYvufHwmCpUTXG2vw6xJC22xkc07T1rphN4ubMnU6XRgLQuQGS6njhFAknL6NJdB%2FgKrllFr5DiqqlubDf3HqMWqAiWi3i7Y0ZQ5SS%2FYF5V4Ja4KKuOdyjyKzBdNwSwZ59rLXog5iuW1SByHEVO8EI5Pj8exeMHSLzQR%2FbSfVtCEPdcYLNxwn0aLts0hPCKkuGwgSH0bllFAhHUBBaB5KkXq5SoZBI%2BmtaYcCq%2FNuS3Hgaq0MotfxiDhRN3tDpFWdzz3isqMSQJj36Zx1sJkY674jVOLexyKEx2PpqkfvmtH965qSUimu8lQvnKqLLXzR8TT6HxncSgOuGDv4BnlXadDiCJ7t6h8BFwZgKIYdg%2Bg4Jeh3ialEbpExIcQ7eyk9riFe49wZ3SOmcYRmHSlojPYlVDgctm4MAmLw2vZ6wRafjXAj6J6eQHZBm8SvNgiGnzCCo3k5Kur29qjm1ciKNes1iNuPQ6i2Z8JbIw5AAX54gsvQ6irvKbPFj6Ub8AgOSjgO1Hu7oKeUOK2nX1HSk5WeslbtmK3MMk8JDfAYfy5uoxvJy64b3ULwboRQ6pbbHoihz%2FH8yTGuuA1B98cA2YVX3CQHh%2Bh%2BWwHzNvILP3P%2BNhJ9HxARhH0j0zC%2Bi%2B28BjqkAaEni0wvdTpmkWeF268Im7hHab4ZmsDWnl6lbXBoiU6QIclTSx61OjfutsdYHGpmsfVSIYFTC1G2PxEql3wDi%2B6nuxLswtpcnTg%2FxsmqGtr51xyHc9JCzYuD3W9jQQ4BXr4Z7ffk21puzDihy5FCA56Pn93PMmKUQqCJxd4XRe8Y4Np%2FB25vh8EdZAhOgWQJRydoNd0%2BU4Yut3gkHG6wBnk0BUYn&X-Amz-Signature=b8c01b23f7dcb28a65ec110f22de5424ce6cb47913a149daa21ecbbcd875a2f6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YOWUO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDJrI6ApV0Lh9mT0zQqXW6JJPwXJxt2Bj%2FFNgo6eqGRwIhAMQz5JOONRj0QQNO9WnZO9FmFTD8V3VPty%2BE7Jnt%2Fu4XKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1%2ByOi4r21zFMuVBwq3APUYvufHwmCpUTXG2vw6xJC22xkc07T1rphN4ubMnU6XRgLQuQGS6njhFAknL6NJdB%2FgKrllFr5DiqqlubDf3HqMWqAiWi3i7Y0ZQ5SS%2FYF5V4Ja4KKuOdyjyKzBdNwSwZ59rLXog5iuW1SByHEVO8EI5Pj8exeMHSLzQR%2FbSfVtCEPdcYLNxwn0aLts0hPCKkuGwgSH0bllFAhHUBBaB5KkXq5SoZBI%2BmtaYcCq%2FNuS3Hgaq0MotfxiDhRN3tDpFWdzz3isqMSQJj36Zx1sJkY674jVOLexyKEx2PpqkfvmtH965qSUimu8lQvnKqLLXzR8TT6HxncSgOuGDv4BnlXadDiCJ7t6h8BFwZgKIYdg%2Bg4Jeh3ialEbpExIcQ7eyk9riFe49wZ3SOmcYRmHSlojPYlVDgctm4MAmLw2vZ6wRafjXAj6J6eQHZBm8SvNgiGnzCCo3k5Kur29qjm1ciKNes1iNuPQ6i2Z8JbIw5AAX54gsvQ6irvKbPFj6Ub8AgOSjgO1Hu7oKeUOK2nX1HSk5WeslbtmK3MMk8JDfAYfy5uoxvJy64b3ULwboRQ6pbbHoihz%2FH8yTGuuA1B98cA2YVX3CQHh%2Bh%2BWwHzNvILP3P%2BNhJ9HxARhH0j0zC%2Bi%2B28BjqkAaEni0wvdTpmkWeF268Im7hHab4ZmsDWnl6lbXBoiU6QIclTSx61OjfutsdYHGpmsfVSIYFTC1G2PxEql3wDi%2B6nuxLswtpcnTg%2FxsmqGtr51xyHc9JCzYuD3W9jQQ4BXr4Z7ffk21puzDihy5FCA56Pn93PMmKUQqCJxd4XRe8Y4Np%2FB25vh8EdZAhOgWQJRydoNd0%2BU4Yut3gkHG6wBnk0BUYn&X-Amz-Signature=0b0ca49f327b1a981afa0bbbcf44d297951aa39e7ad1debc76c5845d05ef660c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YOWUO3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDJrI6ApV0Lh9mT0zQqXW6JJPwXJxt2Bj%2FFNgo6eqGRwIhAMQz5JOONRj0QQNO9WnZO9FmFTD8V3VPty%2BE7Jnt%2Fu4XKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1%2ByOi4r21zFMuVBwq3APUYvufHwmCpUTXG2vw6xJC22xkc07T1rphN4ubMnU6XRgLQuQGS6njhFAknL6NJdB%2FgKrllFr5DiqqlubDf3HqMWqAiWi3i7Y0ZQ5SS%2FYF5V4Ja4KKuOdyjyKzBdNwSwZ59rLXog5iuW1SByHEVO8EI5Pj8exeMHSLzQR%2FbSfVtCEPdcYLNxwn0aLts0hPCKkuGwgSH0bllFAhHUBBaB5KkXq5SoZBI%2BmtaYcCq%2FNuS3Hgaq0MotfxiDhRN3tDpFWdzz3isqMSQJj36Zx1sJkY674jVOLexyKEx2PpqkfvmtH965qSUimu8lQvnKqLLXzR8TT6HxncSgOuGDv4BnlXadDiCJ7t6h8BFwZgKIYdg%2Bg4Jeh3ialEbpExIcQ7eyk9riFe49wZ3SOmcYRmHSlojPYlVDgctm4MAmLw2vZ6wRafjXAj6J6eQHZBm8SvNgiGnzCCo3k5Kur29qjm1ciKNes1iNuPQ6i2Z8JbIw5AAX54gsvQ6irvKbPFj6Ub8AgOSjgO1Hu7oKeUOK2nX1HSk5WeslbtmK3MMk8JDfAYfy5uoxvJy64b3ULwboRQ6pbbHoihz%2FH8yTGuuA1B98cA2YVX3CQHh%2Bh%2BWwHzNvILP3P%2BNhJ9HxARhH0j0zC%2Bi%2B28BjqkAaEni0wvdTpmkWeF268Im7hHab4ZmsDWnl6lbXBoiU6QIclTSx61OjfutsdYHGpmsfVSIYFTC1G2PxEql3wDi%2B6nuxLswtpcnTg%2FxsmqGtr51xyHc9JCzYuD3W9jQQ4BXr4Z7ffk21puzDihy5FCA56Pn93PMmKUQqCJxd4XRe8Y4Np%2FB25vh8EdZAhOgWQJRydoNd0%2BU4Yut3gkHG6wBnk0BUYn&X-Amz-Signature=f17c813b8946dd7a4cb1519ee4d98854c5f7d6b0644b179b59cfd0576ebc89c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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


