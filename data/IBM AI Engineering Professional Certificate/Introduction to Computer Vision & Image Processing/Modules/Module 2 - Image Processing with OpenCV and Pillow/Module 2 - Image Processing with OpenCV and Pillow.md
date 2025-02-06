

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2SFSUL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCcA3LxkMkwVrnMlu9%2FkIM9n%2Btb%2BIHfZo9gGNTSxxXJDwIgeIBuTxGd98uFVK%2BPVL5S4z4t7Iiir3ZakVhtlzazu2Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCmf0biFgGpve4l9rCrcA%2FLZqNSZKwalvcH03BuRbbzqLhwZ5qlJ68DWoxBPK2RBzpMWcxqFqAy%2FFHbMXMriQnKorr20ac3vO%2FN4dUQ0c9EioxIMZIIgL20bidH9oZh2osg66qI%2BgcMZXX9fMxz32m7AFw6TWD96RDCnxKOSN9i5%2BJqmxwGhZ0qiQob%2Bldj0sQ1IaPFR4DpyK%2FH%2B1MSY3Gnc3lBPp9U0pwLlU55VRhjySPiAJT0l5UfBiA%2B07EiTclLYxmiBaEiSt9gYP%2FBG%2FMNrYbjRcsChybckdEwHfwq8Wd%2BlWQKskQ4BKJPhKVHkaHSch1GeyZSb8%2F4S%2FXAZ%2FC7%2FWMfcrrhAjY86rOuX%2FIYIsHKEsitxMRgHxE37HSrFUodQ8ahzIdhJP0k1gl0sAaO0SHXQcJX1xgxpTADmhhFCoo2AkuBm8dyfF1A8ok%2Bpxogl9SoDRo7cJhH35ZiXumglqrGlP%2B5OeW0%2Fdj2pA%2BuXjfuUNyb%2F8rAl5wlcX6AgTlm5Aag2KEcMJAWX%2BIQ8jMrWRrREtIyXch8Nh7h7YmR2Gd3TYThmZceUTvQAjlPt50GdRpdeofGmw0a%2BJCcbh1r18rw5rYeJjFjDXRys1neAogZMIpjX8gOtKv6bkAqJTtOPbUsCnw1xpB5tMM23lL0GOqUBDfDQuJGh0TntYDpl6FoPR6JRpqtfAP1frV9gGF02CzEDQ4JBmkLWxGnBzK%2Bu4caOcV%2BlWnCCqZPqz1Q1%2Fomyyz8Tbs0SB%2F84BwQWU334KKVeUJo5%2BpR22SM%2BKBVgZ8yTMvhP3uCGTir6tRPjxSE5laxBLzBLk%2BnFN1enwmI5RUUOPhqPtyAWAl8W%2ByOHr6GjiyqkuqcjKzziqNKtcZ4v2ceh3rtq&X-Amz-Signature=e1dc34479ff66cee8b643e8734679f192c5d92d9d7741fe78b8543ab6c6a47e1&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZPDSD7K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCVlFoS2tcPnYVLns4yb%2FSZfogflIH3S1WGLMUvgdfKZwIgazCCuIauCXgp4quetubWfF2QdJ0iymRSvo86An9PQcQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJXzUW%2FuJ98bcgJoDircA1cUTTi0rOTwTCf1YFfrWJji6i1fyelgFQ1j6CifCCNPNc5pE62KIFxaTJbN0zTSDAjvSAAQqeYiuHgLhsNh%2FHnMUbMni3C8bH5K9S0NihZ8PLMTeqfs2IoiVORl5ujZ7RTvxAxywDOL3zGSgc2Dc5FG3IsiPppEHi5wU7PmGNt9xH1jgjAIaT4GkXbx82oBgRGSChllHsx5IO9ZZiRQd7d%2FBhC2QiKCzVs7eNY9RlqHI6IgLXLKzkWcG2Bsaj19y1JVs58EmMQmi4L1SvgpRMRtREj6T5Uf7YzVPALJ6QFOTGUS%2B1Fcyveq1bX3SX4F34Q36RDWMTu7DQbjzZdMMoTeGagMeQ7dp0k%2Bi69UiDcs62iLVbCOgTl%2Bp7JkGshg%2Br7mTDe5MJ138g4H8rsbVHedjjvXtGlvpWCRgoGVPq1f%2F3fTBcqe2suTlwqCoxfKTWqAMqfTCGP15B87hOLdEuQPkCeO1XMykDkzNMdjdKFZLetnm%2BFn45NyUWzagoThza07cjcQhfHdJ1bxX310K3tIvhk0wHtskUFyxNpT6Rqh6Le%2B2N8dE5KySfTNgjWgo62Lhr9J8sjkyFj7wTMbd%2BNyvgTgUKvnfjv%2B1llBwZl7svCCBVHKmPOIwUnxMLK4lL0GOqUBphygYoUsuqoSplwvDGA%2FHZ29UJw4AoLWoiX8ZSuT1Ev9Kxm%2Bw5CnbyChjnXXL5ck94OwRBV8pEOnrzyJk08S0uCUOYyrYcO1IEX0303wCxAHtmNAnIIoIubI27B6Fhm32FC5ilD9%2FZIpWNL2ZEqYEzQm5fhjfFEj1FZS%2F5nF2jjLz1WnwQ0bZ958gaiDmRuu6W%2FaRhpIsmxFseroVRdNwVMk4%2ByZ&X-Amz-Signature=f7450d3f52d2cc49f2a86064a90bda9d9527c704c5e129b1e92c490ce7322f50&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZPDSD7K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCVlFoS2tcPnYVLns4yb%2FSZfogflIH3S1WGLMUvgdfKZwIgazCCuIauCXgp4quetubWfF2QdJ0iymRSvo86An9PQcQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJXzUW%2FuJ98bcgJoDircA1cUTTi0rOTwTCf1YFfrWJji6i1fyelgFQ1j6CifCCNPNc5pE62KIFxaTJbN0zTSDAjvSAAQqeYiuHgLhsNh%2FHnMUbMni3C8bH5K9S0NihZ8PLMTeqfs2IoiVORl5ujZ7RTvxAxywDOL3zGSgc2Dc5FG3IsiPppEHi5wU7PmGNt9xH1jgjAIaT4GkXbx82oBgRGSChllHsx5IO9ZZiRQd7d%2FBhC2QiKCzVs7eNY9RlqHI6IgLXLKzkWcG2Bsaj19y1JVs58EmMQmi4L1SvgpRMRtREj6T5Uf7YzVPALJ6QFOTGUS%2B1Fcyveq1bX3SX4F34Q36RDWMTu7DQbjzZdMMoTeGagMeQ7dp0k%2Bi69UiDcs62iLVbCOgTl%2Bp7JkGshg%2Br7mTDe5MJ138g4H8rsbVHedjjvXtGlvpWCRgoGVPq1f%2F3fTBcqe2suTlwqCoxfKTWqAMqfTCGP15B87hOLdEuQPkCeO1XMykDkzNMdjdKFZLetnm%2BFn45NyUWzagoThza07cjcQhfHdJ1bxX310K3tIvhk0wHtskUFyxNpT6Rqh6Le%2B2N8dE5KySfTNgjWgo62Lhr9J8sjkyFj7wTMbd%2BNyvgTgUKvnfjv%2B1llBwZl7svCCBVHKmPOIwUnxMLK4lL0GOqUBphygYoUsuqoSplwvDGA%2FHZ29UJw4AoLWoiX8ZSuT1Ev9Kxm%2Bw5CnbyChjnXXL5ck94OwRBV8pEOnrzyJk08S0uCUOYyrYcO1IEX0303wCxAHtmNAnIIoIubI27B6Fhm32FC5ilD9%2FZIpWNL2ZEqYEzQm5fhjfFEj1FZS%2F5nF2jjLz1WnwQ0bZ958gaiDmRuu6W%2FaRhpIsmxFseroVRdNwVMk4%2ByZ&X-Amz-Signature=c119b9464ab29e15002ebd502dd2fbb8b9060ee30686a97f0a55db5b35c17e6d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZPDSD7K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCVlFoS2tcPnYVLns4yb%2FSZfogflIH3S1WGLMUvgdfKZwIgazCCuIauCXgp4quetubWfF2QdJ0iymRSvo86An9PQcQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJXzUW%2FuJ98bcgJoDircA1cUTTi0rOTwTCf1YFfrWJji6i1fyelgFQ1j6CifCCNPNc5pE62KIFxaTJbN0zTSDAjvSAAQqeYiuHgLhsNh%2FHnMUbMni3C8bH5K9S0NihZ8PLMTeqfs2IoiVORl5ujZ7RTvxAxywDOL3zGSgc2Dc5FG3IsiPppEHi5wU7PmGNt9xH1jgjAIaT4GkXbx82oBgRGSChllHsx5IO9ZZiRQd7d%2FBhC2QiKCzVs7eNY9RlqHI6IgLXLKzkWcG2Bsaj19y1JVs58EmMQmi4L1SvgpRMRtREj6T5Uf7YzVPALJ6QFOTGUS%2B1Fcyveq1bX3SX4F34Q36RDWMTu7DQbjzZdMMoTeGagMeQ7dp0k%2Bi69UiDcs62iLVbCOgTl%2Bp7JkGshg%2Br7mTDe5MJ138g4H8rsbVHedjjvXtGlvpWCRgoGVPq1f%2F3fTBcqe2suTlwqCoxfKTWqAMqfTCGP15B87hOLdEuQPkCeO1XMykDkzNMdjdKFZLetnm%2BFn45NyUWzagoThza07cjcQhfHdJ1bxX310K3tIvhk0wHtskUFyxNpT6Rqh6Le%2B2N8dE5KySfTNgjWgo62Lhr9J8sjkyFj7wTMbd%2BNyvgTgUKvnfjv%2B1llBwZl7svCCBVHKmPOIwUnxMLK4lL0GOqUBphygYoUsuqoSplwvDGA%2FHZ29UJw4AoLWoiX8ZSuT1Ev9Kxm%2Bw5CnbyChjnXXL5ck94OwRBV8pEOnrzyJk08S0uCUOYyrYcO1IEX0303wCxAHtmNAnIIoIubI27B6Fhm32FC5ilD9%2FZIpWNL2ZEqYEzQm5fhjfFEj1FZS%2F5nF2jjLz1WnwQ0bZ958gaiDmRuu6W%2FaRhpIsmxFseroVRdNwVMk4%2ByZ&X-Amz-Signature=d88bffa90f2a880a92a52543ed26ff793cec62e12e8de600e02bcd82ede159c0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZPDSD7K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCVlFoS2tcPnYVLns4yb%2FSZfogflIH3S1WGLMUvgdfKZwIgazCCuIauCXgp4quetubWfF2QdJ0iymRSvo86An9PQcQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJXzUW%2FuJ98bcgJoDircA1cUTTi0rOTwTCf1YFfrWJji6i1fyelgFQ1j6CifCCNPNc5pE62KIFxaTJbN0zTSDAjvSAAQqeYiuHgLhsNh%2FHnMUbMni3C8bH5K9S0NihZ8PLMTeqfs2IoiVORl5ujZ7RTvxAxywDOL3zGSgc2Dc5FG3IsiPppEHi5wU7PmGNt9xH1jgjAIaT4GkXbx82oBgRGSChllHsx5IO9ZZiRQd7d%2FBhC2QiKCzVs7eNY9RlqHI6IgLXLKzkWcG2Bsaj19y1JVs58EmMQmi4L1SvgpRMRtREj6T5Uf7YzVPALJ6QFOTGUS%2B1Fcyveq1bX3SX4F34Q36RDWMTu7DQbjzZdMMoTeGagMeQ7dp0k%2Bi69UiDcs62iLVbCOgTl%2Bp7JkGshg%2Br7mTDe5MJ138g4H8rsbVHedjjvXtGlvpWCRgoGVPq1f%2F3fTBcqe2suTlwqCoxfKTWqAMqfTCGP15B87hOLdEuQPkCeO1XMykDkzNMdjdKFZLetnm%2BFn45NyUWzagoThza07cjcQhfHdJ1bxX310K3tIvhk0wHtskUFyxNpT6Rqh6Le%2B2N8dE5KySfTNgjWgo62Lhr9J8sjkyFj7wTMbd%2BNyvgTgUKvnfjv%2B1llBwZl7svCCBVHKmPOIwUnxMLK4lL0GOqUBphygYoUsuqoSplwvDGA%2FHZ29UJw4AoLWoiX8ZSuT1Ev9Kxm%2Bw5CnbyChjnXXL5ck94OwRBV8pEOnrzyJk08S0uCUOYyrYcO1IEX0303wCxAHtmNAnIIoIubI27B6Fhm32FC5ilD9%2FZIpWNL2ZEqYEzQm5fhjfFEj1FZS%2F5nF2jjLz1WnwQ0bZ958gaiDmRuu6W%2FaRhpIsmxFseroVRdNwVMk4%2ByZ&X-Amz-Signature=777b45978b72275c11669d7cdf68075c2202be8f157a6f8eb1d0e87c5851bc75&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZPDSD7K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCVlFoS2tcPnYVLns4yb%2FSZfogflIH3S1WGLMUvgdfKZwIgazCCuIauCXgp4quetubWfF2QdJ0iymRSvo86An9PQcQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJXzUW%2FuJ98bcgJoDircA1cUTTi0rOTwTCf1YFfrWJji6i1fyelgFQ1j6CifCCNPNc5pE62KIFxaTJbN0zTSDAjvSAAQqeYiuHgLhsNh%2FHnMUbMni3C8bH5K9S0NihZ8PLMTeqfs2IoiVORl5ujZ7RTvxAxywDOL3zGSgc2Dc5FG3IsiPppEHi5wU7PmGNt9xH1jgjAIaT4GkXbx82oBgRGSChllHsx5IO9ZZiRQd7d%2FBhC2QiKCzVs7eNY9RlqHI6IgLXLKzkWcG2Bsaj19y1JVs58EmMQmi4L1SvgpRMRtREj6T5Uf7YzVPALJ6QFOTGUS%2B1Fcyveq1bX3SX4F34Q36RDWMTu7DQbjzZdMMoTeGagMeQ7dp0k%2Bi69UiDcs62iLVbCOgTl%2Bp7JkGshg%2Br7mTDe5MJ138g4H8rsbVHedjjvXtGlvpWCRgoGVPq1f%2F3fTBcqe2suTlwqCoxfKTWqAMqfTCGP15B87hOLdEuQPkCeO1XMykDkzNMdjdKFZLetnm%2BFn45NyUWzagoThza07cjcQhfHdJ1bxX310K3tIvhk0wHtskUFyxNpT6Rqh6Le%2B2N8dE5KySfTNgjWgo62Lhr9J8sjkyFj7wTMbd%2BNyvgTgUKvnfjv%2B1llBwZl7svCCBVHKmPOIwUnxMLK4lL0GOqUBphygYoUsuqoSplwvDGA%2FHZ29UJw4AoLWoiX8ZSuT1Ev9Kxm%2Bw5CnbyChjnXXL5ck94OwRBV8pEOnrzyJk08S0uCUOYyrYcO1IEX0303wCxAHtmNAnIIoIubI27B6Fhm32FC5ilD9%2FZIpWNL2ZEqYEzQm5fhjfFEj1FZS%2F5nF2jjLz1WnwQ0bZ958gaiDmRuu6W%2FaRhpIsmxFseroVRdNwVMk4%2ByZ&X-Amz-Signature=4637972c42d0b7eb8d51cdc102838a6d8c9aa71b31e22aab718dc1005fcd488f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2SFSUL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCcA3LxkMkwVrnMlu9%2FkIM9n%2Btb%2BIHfZo9gGNTSxxXJDwIgeIBuTxGd98uFVK%2BPVL5S4z4t7Iiir3ZakVhtlzazu2Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCmf0biFgGpve4l9rCrcA%2FLZqNSZKwalvcH03BuRbbzqLhwZ5qlJ68DWoxBPK2RBzpMWcxqFqAy%2FFHbMXMriQnKorr20ac3vO%2FN4dUQ0c9EioxIMZIIgL20bidH9oZh2osg66qI%2BgcMZXX9fMxz32m7AFw6TWD96RDCnxKOSN9i5%2BJqmxwGhZ0qiQob%2Bldj0sQ1IaPFR4DpyK%2FH%2B1MSY3Gnc3lBPp9U0pwLlU55VRhjySPiAJT0l5UfBiA%2B07EiTclLYxmiBaEiSt9gYP%2FBG%2FMNrYbjRcsChybckdEwHfwq8Wd%2BlWQKskQ4BKJPhKVHkaHSch1GeyZSb8%2F4S%2FXAZ%2FC7%2FWMfcrrhAjY86rOuX%2FIYIsHKEsitxMRgHxE37HSrFUodQ8ahzIdhJP0k1gl0sAaO0SHXQcJX1xgxpTADmhhFCoo2AkuBm8dyfF1A8ok%2Bpxogl9SoDRo7cJhH35ZiXumglqrGlP%2B5OeW0%2Fdj2pA%2BuXjfuUNyb%2F8rAl5wlcX6AgTlm5Aag2KEcMJAWX%2BIQ8jMrWRrREtIyXch8Nh7h7YmR2Gd3TYThmZceUTvQAjlPt50GdRpdeofGmw0a%2BJCcbh1r18rw5rYeJjFjDXRys1neAogZMIpjX8gOtKv6bkAqJTtOPbUsCnw1xpB5tMM23lL0GOqUBDfDQuJGh0TntYDpl6FoPR6JRpqtfAP1frV9gGF02CzEDQ4JBmkLWxGnBzK%2Bu4caOcV%2BlWnCCqZPqz1Q1%2Fomyyz8Tbs0SB%2F84BwQWU334KKVeUJo5%2BpR22SM%2BKBVgZ8yTMvhP3uCGTir6tRPjxSE5laxBLzBLk%2BnFN1enwmI5RUUOPhqPtyAWAl8W%2ByOHr6GjiyqkuqcjKzziqNKtcZ4v2ceh3rtq&X-Amz-Signature=76fdfc0cfae76124d4dec349fca87965d8553494c0f0f21f73e7ee6e4b842f89&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2SFSUL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCcA3LxkMkwVrnMlu9%2FkIM9n%2Btb%2BIHfZo9gGNTSxxXJDwIgeIBuTxGd98uFVK%2BPVL5S4z4t7Iiir3ZakVhtlzazu2Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCmf0biFgGpve4l9rCrcA%2FLZqNSZKwalvcH03BuRbbzqLhwZ5qlJ68DWoxBPK2RBzpMWcxqFqAy%2FFHbMXMriQnKorr20ac3vO%2FN4dUQ0c9EioxIMZIIgL20bidH9oZh2osg66qI%2BgcMZXX9fMxz32m7AFw6TWD96RDCnxKOSN9i5%2BJqmxwGhZ0qiQob%2Bldj0sQ1IaPFR4DpyK%2FH%2B1MSY3Gnc3lBPp9U0pwLlU55VRhjySPiAJT0l5UfBiA%2B07EiTclLYxmiBaEiSt9gYP%2FBG%2FMNrYbjRcsChybckdEwHfwq8Wd%2BlWQKskQ4BKJPhKVHkaHSch1GeyZSb8%2F4S%2FXAZ%2FC7%2FWMfcrrhAjY86rOuX%2FIYIsHKEsitxMRgHxE37HSrFUodQ8ahzIdhJP0k1gl0sAaO0SHXQcJX1xgxpTADmhhFCoo2AkuBm8dyfF1A8ok%2Bpxogl9SoDRo7cJhH35ZiXumglqrGlP%2B5OeW0%2Fdj2pA%2BuXjfuUNyb%2F8rAl5wlcX6AgTlm5Aag2KEcMJAWX%2BIQ8jMrWRrREtIyXch8Nh7h7YmR2Gd3TYThmZceUTvQAjlPt50GdRpdeofGmw0a%2BJCcbh1r18rw5rYeJjFjDXRys1neAogZMIpjX8gOtKv6bkAqJTtOPbUsCnw1xpB5tMM23lL0GOqUBDfDQuJGh0TntYDpl6FoPR6JRpqtfAP1frV9gGF02CzEDQ4JBmkLWxGnBzK%2Bu4caOcV%2BlWnCCqZPqz1Q1%2Fomyyz8Tbs0SB%2F84BwQWU334KKVeUJo5%2BpR22SM%2BKBVgZ8yTMvhP3uCGTir6tRPjxSE5laxBLzBLk%2BnFN1enwmI5RUUOPhqPtyAWAl8W%2ByOHr6GjiyqkuqcjKzziqNKtcZ4v2ceh3rtq&X-Amz-Signature=12089cfa667cff34c0fae65c242ceaffa898aefd5bbe1246ffd9419151647a27&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2SFSUL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCcA3LxkMkwVrnMlu9%2FkIM9n%2Btb%2BIHfZo9gGNTSxxXJDwIgeIBuTxGd98uFVK%2BPVL5S4z4t7Iiir3ZakVhtlzazu2Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCmf0biFgGpve4l9rCrcA%2FLZqNSZKwalvcH03BuRbbzqLhwZ5qlJ68DWoxBPK2RBzpMWcxqFqAy%2FFHbMXMriQnKorr20ac3vO%2FN4dUQ0c9EioxIMZIIgL20bidH9oZh2osg66qI%2BgcMZXX9fMxz32m7AFw6TWD96RDCnxKOSN9i5%2BJqmxwGhZ0qiQob%2Bldj0sQ1IaPFR4DpyK%2FH%2B1MSY3Gnc3lBPp9U0pwLlU55VRhjySPiAJT0l5UfBiA%2B07EiTclLYxmiBaEiSt9gYP%2FBG%2FMNrYbjRcsChybckdEwHfwq8Wd%2BlWQKskQ4BKJPhKVHkaHSch1GeyZSb8%2F4S%2FXAZ%2FC7%2FWMfcrrhAjY86rOuX%2FIYIsHKEsitxMRgHxE37HSrFUodQ8ahzIdhJP0k1gl0sAaO0SHXQcJX1xgxpTADmhhFCoo2AkuBm8dyfF1A8ok%2Bpxogl9SoDRo7cJhH35ZiXumglqrGlP%2B5OeW0%2Fdj2pA%2BuXjfuUNyb%2F8rAl5wlcX6AgTlm5Aag2KEcMJAWX%2BIQ8jMrWRrREtIyXch8Nh7h7YmR2Gd3TYThmZceUTvQAjlPt50GdRpdeofGmw0a%2BJCcbh1r18rw5rYeJjFjDXRys1neAogZMIpjX8gOtKv6bkAqJTtOPbUsCnw1xpB5tMM23lL0GOqUBDfDQuJGh0TntYDpl6FoPR6JRpqtfAP1frV9gGF02CzEDQ4JBmkLWxGnBzK%2Bu4caOcV%2BlWnCCqZPqz1Q1%2Fomyyz8Tbs0SB%2F84BwQWU334KKVeUJo5%2BpR22SM%2BKBVgZ8yTMvhP3uCGTir6tRPjxSE5laxBLzBLk%2BnFN1enwmI5RUUOPhqPtyAWAl8W%2ByOHr6GjiyqkuqcjKzziqNKtcZ4v2ceh3rtq&X-Amz-Signature=0f69c6cce065ad2650a58639e1b188500a03c2c09321e0f8caeb9cb086ca55e3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2SFSUL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCcA3LxkMkwVrnMlu9%2FkIM9n%2Btb%2BIHfZo9gGNTSxxXJDwIgeIBuTxGd98uFVK%2BPVL5S4z4t7Iiir3ZakVhtlzazu2Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCmf0biFgGpve4l9rCrcA%2FLZqNSZKwalvcH03BuRbbzqLhwZ5qlJ68DWoxBPK2RBzpMWcxqFqAy%2FFHbMXMriQnKorr20ac3vO%2FN4dUQ0c9EioxIMZIIgL20bidH9oZh2osg66qI%2BgcMZXX9fMxz32m7AFw6TWD96RDCnxKOSN9i5%2BJqmxwGhZ0qiQob%2Bldj0sQ1IaPFR4DpyK%2FH%2B1MSY3Gnc3lBPp9U0pwLlU55VRhjySPiAJT0l5UfBiA%2B07EiTclLYxmiBaEiSt9gYP%2FBG%2FMNrYbjRcsChybckdEwHfwq8Wd%2BlWQKskQ4BKJPhKVHkaHSch1GeyZSb8%2F4S%2FXAZ%2FC7%2FWMfcrrhAjY86rOuX%2FIYIsHKEsitxMRgHxE37HSrFUodQ8ahzIdhJP0k1gl0sAaO0SHXQcJX1xgxpTADmhhFCoo2AkuBm8dyfF1A8ok%2Bpxogl9SoDRo7cJhH35ZiXumglqrGlP%2B5OeW0%2Fdj2pA%2BuXjfuUNyb%2F8rAl5wlcX6AgTlm5Aag2KEcMJAWX%2BIQ8jMrWRrREtIyXch8Nh7h7YmR2Gd3TYThmZceUTvQAjlPt50GdRpdeofGmw0a%2BJCcbh1r18rw5rYeJjFjDXRys1neAogZMIpjX8gOtKv6bkAqJTtOPbUsCnw1xpB5tMM23lL0GOqUBDfDQuJGh0TntYDpl6FoPR6JRpqtfAP1frV9gGF02CzEDQ4JBmkLWxGnBzK%2Bu4caOcV%2BlWnCCqZPqz1Q1%2Fomyyz8Tbs0SB%2F84BwQWU334KKVeUJo5%2BpR22SM%2BKBVgZ8yTMvhP3uCGTir6tRPjxSE5laxBLzBLk%2BnFN1enwmI5RUUOPhqPtyAWAl8W%2ByOHr6GjiyqkuqcjKzziqNKtcZ4v2ceh3rtq&X-Amz-Signature=e41f424de6ff787ce7f5061e04fa06d78d0aca41dc994cc342bcaef697b116eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR2SFSUL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCcA3LxkMkwVrnMlu9%2FkIM9n%2Btb%2BIHfZo9gGNTSxxXJDwIgeIBuTxGd98uFVK%2BPVL5S4z4t7Iiir3ZakVhtlzazu2Uq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCmf0biFgGpve4l9rCrcA%2FLZqNSZKwalvcH03BuRbbzqLhwZ5qlJ68DWoxBPK2RBzpMWcxqFqAy%2FFHbMXMriQnKorr20ac3vO%2FN4dUQ0c9EioxIMZIIgL20bidH9oZh2osg66qI%2BgcMZXX9fMxz32m7AFw6TWD96RDCnxKOSN9i5%2BJqmxwGhZ0qiQob%2Bldj0sQ1IaPFR4DpyK%2FH%2B1MSY3Gnc3lBPp9U0pwLlU55VRhjySPiAJT0l5UfBiA%2B07EiTclLYxmiBaEiSt9gYP%2FBG%2FMNrYbjRcsChybckdEwHfwq8Wd%2BlWQKskQ4BKJPhKVHkaHSch1GeyZSb8%2F4S%2FXAZ%2FC7%2FWMfcrrhAjY86rOuX%2FIYIsHKEsitxMRgHxE37HSrFUodQ8ahzIdhJP0k1gl0sAaO0SHXQcJX1xgxpTADmhhFCoo2AkuBm8dyfF1A8ok%2Bpxogl9SoDRo7cJhH35ZiXumglqrGlP%2B5OeW0%2Fdj2pA%2BuXjfuUNyb%2F8rAl5wlcX6AgTlm5Aag2KEcMJAWX%2BIQ8jMrWRrREtIyXch8Nh7h7YmR2Gd3TYThmZceUTvQAjlPt50GdRpdeofGmw0a%2BJCcbh1r18rw5rYeJjFjDXRys1neAogZMIpjX8gOtKv6bkAqJTtOPbUsCnw1xpB5tMM23lL0GOqUBDfDQuJGh0TntYDpl6FoPR6JRpqtfAP1frV9gGF02CzEDQ4JBmkLWxGnBzK%2Bu4caOcV%2BlWnCCqZPqz1Q1%2Fomyyz8Tbs0SB%2F84BwQWU334KKVeUJo5%2BpR22SM%2BKBVgZ8yTMvhP3uCGTir6tRPjxSE5laxBLzBLk%2BnFN1enwmI5RUUOPhqPtyAWAl8W%2ByOHr6GjiyqkuqcjKzziqNKtcZ4v2ceh3rtq&X-Amz-Signature=202e3919de937525ffdb71d40144d1e59a079e4dfde33317f5f89c2688fe3ae9&X-Amz-SignedHeaders=host&x-id=GetObject)
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


