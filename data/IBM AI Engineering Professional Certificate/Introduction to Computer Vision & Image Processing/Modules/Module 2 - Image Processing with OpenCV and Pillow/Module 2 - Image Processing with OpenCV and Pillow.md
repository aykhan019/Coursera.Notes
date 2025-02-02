

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEKPKM3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVKVa2wGW8o2mlYye9jbfSLVXLbhpNqOw8IzjMtya2TAiAiOaRO7QRi9n2bQyS2MMGu5rTpkRAMdzvr6Idt4NEAhSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB4RuD41cRLk141TcKtwDXD%2FY4txHlKyxq%2B7VH2P%2FHvnkcIxi%2FuBOFiOasJRD1KYjqV6k9s6uc0%2Bwwcifh%2B8it8Xt%2FJIuOxnIieA8yCyGq6WpiCsn68frcNl2d0Z2kcUC%2FWWY74n6T69y5aFlHFObB43ffHSzL0tvEUheSmQOm1KQS5wD2HCppenznXsng5wi0xj5t2E8JyLQeGp5vvU5dcWjcPWL9uc%2BoSR0B1uS%2Bxmw1P47%2BuPyBX0fdqh1g%2BIaOfHnuXavTLzWPHryW55ikNR2sZwBYI3A1io6%2BdOaecYvEvk3In5DlR09WbyBCP93sWQV2RbXAYBuCRtUsEC%2BFVqWePcQVKQZ8f%2BHg1MtmzcoQEPeDNve6rHbGljubkCVkDoiK%2BvVL0Usvtd8QPtFZNFGzbGC5hlmDfmgF7peNDG%2BmtsZmly6PCu2nTlT8Hl%2Bs4pSDtT%2BSuk6t2teAJT9g7xEMQ2jMhtcfEyd%2BKj0xOuAL%2Bo0%2BK%2F75a1XmKCp2tpd8VlPn8F1bseNyD61swzQEl5S%2B%2FpTT5L%2BFDYN%2B788qnE2rzRC%2BDExn6ktrija7hq8ytCpS%2BNq%2FoUCtmlC68%2BfsuEEAPGQm3Ul8LnzMrtlu9niW0OhT6MZRVGSnth0nPqkQDsaWL%2B5KxnaxlIw1br7vAY6pgE3yLv3PxrbR3SLqazm5NJfP%2FuHNcDIGF8FKZ2M8JiMyY7VA6D97YR%2FrDQLId4oejQKSrCXYeDEtqsu8azKd1XYFEGV7MN0y5gXQ81mCt%2B9D1DCLg4GSKUzMGgYgd1KHWqa3tL6IiPWOTL53ONPiQntHym5FAFQNjwTKQ5mzVUhPggH9niNGrQwV1N50hnQtFlBoA3N%2FAuvtlgk1Y5qKJw5tHME8UFG&X-Amz-Signature=571cbc0da20748cfff172eaaec133258dc5795c3c60173ea60caf1d175398d0f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVNQDQTH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2tItyFw5vV4ai30VUtGz2RGUmKHQ3LN92m%2FhTytNR2AIgSO019tR6qPB4AsE6neo5v6DuNKUGqJzEqcM%2B56rxcqwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRp06gwnDmnjcSMOircA%2FBHLDzE6yhJioPLQ8JOjRj6yUM9UFoI3HWStIX6y3BwrsM%2Ba2HDE9nAJYkSC6%2BYVi3N9t5sxHIT4iZ8%2B0yhLKGqkIxbWHvlCt%2BRlk6SD5sAqhs5qdkV8TDf1ZgLv6d5eajM%2BWf8DiUxGfJWFs2P2piI%2BJ8IJbPzlMif8aCUTHSYBH1Ti69i%2FLeG5OJwwJtCAJ3y3CrLWhAo5j9NLaS4wT6IYdyImn0WDzXX6oad6aE4j5ZU52Yr5Y%2FpX1G8oPgMNOjqGlNuPfduToCmqneoXZIOC5WdX5xcOyt7i%2FaeKTUx1TWpY%2FZgR6Gq%2BgGtifAGTdF6vTTvOrpR44aEWzdu1VXYfICiz2ShPdLoWaggjNfO4S82X8fCD8NfVQn1k8%2FuOCR5yUsXGGO9YKt4ah8kUvhLBkBHOtabHYY12Ksc0ts7eCitBy9nd4DTYlJLbekcTgN8qKP%2FRN248xl7FRVPX5Jd%2BH7I9%2BnF4qN1C5eiZVpI3E4W6lvNuFsRUtg596ngNg9pMfrJiamoyPW%2FmWhV6T22JSOj7voZO8p8%2BOlGiT0w9Ss65KysQg3sgcXHhju3w%2FN%2F6LcIrI7UxxBHU3oNGUhiPovszJcXk6rMz958HEc59FTUlou2T9CJWSJjMNW6%2B7wGOqUBlzw0%2BQtUKRbgDBQg9WYnB6sAS9ebB2tVE9ZyRgW3lH9yMMFXez0XluvHxaB3NqAjF7L%2BiTSthB4Mm%2BqWqFLPnVmVk7NfvSKln5SrYyuD%2FBcajw%2B751Y0IpmaPncmZ9fn64xw3Vw4kqIzV4O9pfXUXh7AgNEGEt%2BXg5JcxQZQy0HwCXxUTLesWM32n%2BoQeBizBX8ByblfrTpSzxYtD9n6aAEPiRPF&X-Amz-Signature=0147bbefd4b6f6fbea42090edbccd8ecdaa27ebd0e036836297ac76861711227&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVNQDQTH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2tItyFw5vV4ai30VUtGz2RGUmKHQ3LN92m%2FhTytNR2AIgSO019tR6qPB4AsE6neo5v6DuNKUGqJzEqcM%2B56rxcqwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRp06gwnDmnjcSMOircA%2FBHLDzE6yhJioPLQ8JOjRj6yUM9UFoI3HWStIX6y3BwrsM%2Ba2HDE9nAJYkSC6%2BYVi3N9t5sxHIT4iZ8%2B0yhLKGqkIxbWHvlCt%2BRlk6SD5sAqhs5qdkV8TDf1ZgLv6d5eajM%2BWf8DiUxGfJWFs2P2piI%2BJ8IJbPzlMif8aCUTHSYBH1Ti69i%2FLeG5OJwwJtCAJ3y3CrLWhAo5j9NLaS4wT6IYdyImn0WDzXX6oad6aE4j5ZU52Yr5Y%2FpX1G8oPgMNOjqGlNuPfduToCmqneoXZIOC5WdX5xcOyt7i%2FaeKTUx1TWpY%2FZgR6Gq%2BgGtifAGTdF6vTTvOrpR44aEWzdu1VXYfICiz2ShPdLoWaggjNfO4S82X8fCD8NfVQn1k8%2FuOCR5yUsXGGO9YKt4ah8kUvhLBkBHOtabHYY12Ksc0ts7eCitBy9nd4DTYlJLbekcTgN8qKP%2FRN248xl7FRVPX5Jd%2BH7I9%2BnF4qN1C5eiZVpI3E4W6lvNuFsRUtg596ngNg9pMfrJiamoyPW%2FmWhV6T22JSOj7voZO8p8%2BOlGiT0w9Ss65KysQg3sgcXHhju3w%2FN%2F6LcIrI7UxxBHU3oNGUhiPovszJcXk6rMz958HEc59FTUlou2T9CJWSJjMNW6%2B7wGOqUBlzw0%2BQtUKRbgDBQg9WYnB6sAS9ebB2tVE9ZyRgW3lH9yMMFXez0XluvHxaB3NqAjF7L%2BiTSthB4Mm%2BqWqFLPnVmVk7NfvSKln5SrYyuD%2FBcajw%2B751Y0IpmaPncmZ9fn64xw3Vw4kqIzV4O9pfXUXh7AgNEGEt%2BXg5JcxQZQy0HwCXxUTLesWM32n%2BoQeBizBX8ByblfrTpSzxYtD9n6aAEPiRPF&X-Amz-Signature=8259d04717640451c9b28234e96b7060a1d2cd250918317b61f9decbf0077d27&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVNQDQTH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2tItyFw5vV4ai30VUtGz2RGUmKHQ3LN92m%2FhTytNR2AIgSO019tR6qPB4AsE6neo5v6DuNKUGqJzEqcM%2B56rxcqwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRp06gwnDmnjcSMOircA%2FBHLDzE6yhJioPLQ8JOjRj6yUM9UFoI3HWStIX6y3BwrsM%2Ba2HDE9nAJYkSC6%2BYVi3N9t5sxHIT4iZ8%2B0yhLKGqkIxbWHvlCt%2BRlk6SD5sAqhs5qdkV8TDf1ZgLv6d5eajM%2BWf8DiUxGfJWFs2P2piI%2BJ8IJbPzlMif8aCUTHSYBH1Ti69i%2FLeG5OJwwJtCAJ3y3CrLWhAo5j9NLaS4wT6IYdyImn0WDzXX6oad6aE4j5ZU52Yr5Y%2FpX1G8oPgMNOjqGlNuPfduToCmqneoXZIOC5WdX5xcOyt7i%2FaeKTUx1TWpY%2FZgR6Gq%2BgGtifAGTdF6vTTvOrpR44aEWzdu1VXYfICiz2ShPdLoWaggjNfO4S82X8fCD8NfVQn1k8%2FuOCR5yUsXGGO9YKt4ah8kUvhLBkBHOtabHYY12Ksc0ts7eCitBy9nd4DTYlJLbekcTgN8qKP%2FRN248xl7FRVPX5Jd%2BH7I9%2BnF4qN1C5eiZVpI3E4W6lvNuFsRUtg596ngNg9pMfrJiamoyPW%2FmWhV6T22JSOj7voZO8p8%2BOlGiT0w9Ss65KysQg3sgcXHhju3w%2FN%2F6LcIrI7UxxBHU3oNGUhiPovszJcXk6rMz958HEc59FTUlou2T9CJWSJjMNW6%2B7wGOqUBlzw0%2BQtUKRbgDBQg9WYnB6sAS9ebB2tVE9ZyRgW3lH9yMMFXez0XluvHxaB3NqAjF7L%2BiTSthB4Mm%2BqWqFLPnVmVk7NfvSKln5SrYyuD%2FBcajw%2B751Y0IpmaPncmZ9fn64xw3Vw4kqIzV4O9pfXUXh7AgNEGEt%2BXg5JcxQZQy0HwCXxUTLesWM32n%2BoQeBizBX8ByblfrTpSzxYtD9n6aAEPiRPF&X-Amz-Signature=41523620dd656f910a10cd3495b50f26a9776a7d5706b600b51d3e8b23da5b8c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVNQDQTH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2tItyFw5vV4ai30VUtGz2RGUmKHQ3LN92m%2FhTytNR2AIgSO019tR6qPB4AsE6neo5v6DuNKUGqJzEqcM%2B56rxcqwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRp06gwnDmnjcSMOircA%2FBHLDzE6yhJioPLQ8JOjRj6yUM9UFoI3HWStIX6y3BwrsM%2Ba2HDE9nAJYkSC6%2BYVi3N9t5sxHIT4iZ8%2B0yhLKGqkIxbWHvlCt%2BRlk6SD5sAqhs5qdkV8TDf1ZgLv6d5eajM%2BWf8DiUxGfJWFs2P2piI%2BJ8IJbPzlMif8aCUTHSYBH1Ti69i%2FLeG5OJwwJtCAJ3y3CrLWhAo5j9NLaS4wT6IYdyImn0WDzXX6oad6aE4j5ZU52Yr5Y%2FpX1G8oPgMNOjqGlNuPfduToCmqneoXZIOC5WdX5xcOyt7i%2FaeKTUx1TWpY%2FZgR6Gq%2BgGtifAGTdF6vTTvOrpR44aEWzdu1VXYfICiz2ShPdLoWaggjNfO4S82X8fCD8NfVQn1k8%2FuOCR5yUsXGGO9YKt4ah8kUvhLBkBHOtabHYY12Ksc0ts7eCitBy9nd4DTYlJLbekcTgN8qKP%2FRN248xl7FRVPX5Jd%2BH7I9%2BnF4qN1C5eiZVpI3E4W6lvNuFsRUtg596ngNg9pMfrJiamoyPW%2FmWhV6T22JSOj7voZO8p8%2BOlGiT0w9Ss65KysQg3sgcXHhju3w%2FN%2F6LcIrI7UxxBHU3oNGUhiPovszJcXk6rMz958HEc59FTUlou2T9CJWSJjMNW6%2B7wGOqUBlzw0%2BQtUKRbgDBQg9WYnB6sAS9ebB2tVE9ZyRgW3lH9yMMFXez0XluvHxaB3NqAjF7L%2BiTSthB4Mm%2BqWqFLPnVmVk7NfvSKln5SrYyuD%2FBcajw%2B751Y0IpmaPncmZ9fn64xw3Vw4kqIzV4O9pfXUXh7AgNEGEt%2BXg5JcxQZQy0HwCXxUTLesWM32n%2BoQeBizBX8ByblfrTpSzxYtD9n6aAEPiRPF&X-Amz-Signature=362b04412356dfac41d258b759b3f1145b5733514ebc2daf8af5f8a5cf452676&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVNQDQTH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2tItyFw5vV4ai30VUtGz2RGUmKHQ3LN92m%2FhTytNR2AIgSO019tR6qPB4AsE6neo5v6DuNKUGqJzEqcM%2B56rxcqwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRp06gwnDmnjcSMOircA%2FBHLDzE6yhJioPLQ8JOjRj6yUM9UFoI3HWStIX6y3BwrsM%2Ba2HDE9nAJYkSC6%2BYVi3N9t5sxHIT4iZ8%2B0yhLKGqkIxbWHvlCt%2BRlk6SD5sAqhs5qdkV8TDf1ZgLv6d5eajM%2BWf8DiUxGfJWFs2P2piI%2BJ8IJbPzlMif8aCUTHSYBH1Ti69i%2FLeG5OJwwJtCAJ3y3CrLWhAo5j9NLaS4wT6IYdyImn0WDzXX6oad6aE4j5ZU52Yr5Y%2FpX1G8oPgMNOjqGlNuPfduToCmqneoXZIOC5WdX5xcOyt7i%2FaeKTUx1TWpY%2FZgR6Gq%2BgGtifAGTdF6vTTvOrpR44aEWzdu1VXYfICiz2ShPdLoWaggjNfO4S82X8fCD8NfVQn1k8%2FuOCR5yUsXGGO9YKt4ah8kUvhLBkBHOtabHYY12Ksc0ts7eCitBy9nd4DTYlJLbekcTgN8qKP%2FRN248xl7FRVPX5Jd%2BH7I9%2BnF4qN1C5eiZVpI3E4W6lvNuFsRUtg596ngNg9pMfrJiamoyPW%2FmWhV6T22JSOj7voZO8p8%2BOlGiT0w9Ss65KysQg3sgcXHhju3w%2FN%2F6LcIrI7UxxBHU3oNGUhiPovszJcXk6rMz958HEc59FTUlou2T9CJWSJjMNW6%2B7wGOqUBlzw0%2BQtUKRbgDBQg9WYnB6sAS9ebB2tVE9ZyRgW3lH9yMMFXez0XluvHxaB3NqAjF7L%2BiTSthB4Mm%2BqWqFLPnVmVk7NfvSKln5SrYyuD%2FBcajw%2B751Y0IpmaPncmZ9fn64xw3Vw4kqIzV4O9pfXUXh7AgNEGEt%2BXg5JcxQZQy0HwCXxUTLesWM32n%2BoQeBizBX8ByblfrTpSzxYtD9n6aAEPiRPF&X-Amz-Signature=d8a2d614fb1b9c62612b6748e2a94c812f3563fcacd2b19cc7238c7e07f5220d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEKPKM3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVKVa2wGW8o2mlYye9jbfSLVXLbhpNqOw8IzjMtya2TAiAiOaRO7QRi9n2bQyS2MMGu5rTpkRAMdzvr6Idt4NEAhSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB4RuD41cRLk141TcKtwDXD%2FY4txHlKyxq%2B7VH2P%2FHvnkcIxi%2FuBOFiOasJRD1KYjqV6k9s6uc0%2Bwwcifh%2B8it8Xt%2FJIuOxnIieA8yCyGq6WpiCsn68frcNl2d0Z2kcUC%2FWWY74n6T69y5aFlHFObB43ffHSzL0tvEUheSmQOm1KQS5wD2HCppenznXsng5wi0xj5t2E8JyLQeGp5vvU5dcWjcPWL9uc%2BoSR0B1uS%2Bxmw1P47%2BuPyBX0fdqh1g%2BIaOfHnuXavTLzWPHryW55ikNR2sZwBYI3A1io6%2BdOaecYvEvk3In5DlR09WbyBCP93sWQV2RbXAYBuCRtUsEC%2BFVqWePcQVKQZ8f%2BHg1MtmzcoQEPeDNve6rHbGljubkCVkDoiK%2BvVL0Usvtd8QPtFZNFGzbGC5hlmDfmgF7peNDG%2BmtsZmly6PCu2nTlT8Hl%2Bs4pSDtT%2BSuk6t2teAJT9g7xEMQ2jMhtcfEyd%2BKj0xOuAL%2Bo0%2BK%2F75a1XmKCp2tpd8VlPn8F1bseNyD61swzQEl5S%2B%2FpTT5L%2BFDYN%2B788qnE2rzRC%2BDExn6ktrija7hq8ytCpS%2BNq%2FoUCtmlC68%2BfsuEEAPGQm3Ul8LnzMrtlu9niW0OhT6MZRVGSnth0nPqkQDsaWL%2B5KxnaxlIw1br7vAY6pgE3yLv3PxrbR3SLqazm5NJfP%2FuHNcDIGF8FKZ2M8JiMyY7VA6D97YR%2FrDQLId4oejQKSrCXYeDEtqsu8azKd1XYFEGV7MN0y5gXQ81mCt%2B9D1DCLg4GSKUzMGgYgd1KHWqa3tL6IiPWOTL53ONPiQntHym5FAFQNjwTKQ5mzVUhPggH9niNGrQwV1N50hnQtFlBoA3N%2FAuvtlgk1Y5qKJw5tHME8UFG&X-Amz-Signature=79fc652402fa21a643b77deea4bb148b9a236281278b296e3653da40144d197e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEKPKM3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVKVa2wGW8o2mlYye9jbfSLVXLbhpNqOw8IzjMtya2TAiAiOaRO7QRi9n2bQyS2MMGu5rTpkRAMdzvr6Idt4NEAhSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB4RuD41cRLk141TcKtwDXD%2FY4txHlKyxq%2B7VH2P%2FHvnkcIxi%2FuBOFiOasJRD1KYjqV6k9s6uc0%2Bwwcifh%2B8it8Xt%2FJIuOxnIieA8yCyGq6WpiCsn68frcNl2d0Z2kcUC%2FWWY74n6T69y5aFlHFObB43ffHSzL0tvEUheSmQOm1KQS5wD2HCppenznXsng5wi0xj5t2E8JyLQeGp5vvU5dcWjcPWL9uc%2BoSR0B1uS%2Bxmw1P47%2BuPyBX0fdqh1g%2BIaOfHnuXavTLzWPHryW55ikNR2sZwBYI3A1io6%2BdOaecYvEvk3In5DlR09WbyBCP93sWQV2RbXAYBuCRtUsEC%2BFVqWePcQVKQZ8f%2BHg1MtmzcoQEPeDNve6rHbGljubkCVkDoiK%2BvVL0Usvtd8QPtFZNFGzbGC5hlmDfmgF7peNDG%2BmtsZmly6PCu2nTlT8Hl%2Bs4pSDtT%2BSuk6t2teAJT9g7xEMQ2jMhtcfEyd%2BKj0xOuAL%2Bo0%2BK%2F75a1XmKCp2tpd8VlPn8F1bseNyD61swzQEl5S%2B%2FpTT5L%2BFDYN%2B788qnE2rzRC%2BDExn6ktrija7hq8ytCpS%2BNq%2FoUCtmlC68%2BfsuEEAPGQm3Ul8LnzMrtlu9niW0OhT6MZRVGSnth0nPqkQDsaWL%2B5KxnaxlIw1br7vAY6pgE3yLv3PxrbR3SLqazm5NJfP%2FuHNcDIGF8FKZ2M8JiMyY7VA6D97YR%2FrDQLId4oejQKSrCXYeDEtqsu8azKd1XYFEGV7MN0y5gXQ81mCt%2B9D1DCLg4GSKUzMGgYgd1KHWqa3tL6IiPWOTL53ONPiQntHym5FAFQNjwTKQ5mzVUhPggH9niNGrQwV1N50hnQtFlBoA3N%2FAuvtlgk1Y5qKJw5tHME8UFG&X-Amz-Signature=bf88ede18a6f8a3bffde180c9611164a6c5b188dc934f3cb22d6d7169fd92df3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEKPKM3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVKVa2wGW8o2mlYye9jbfSLVXLbhpNqOw8IzjMtya2TAiAiOaRO7QRi9n2bQyS2MMGu5rTpkRAMdzvr6Idt4NEAhSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB4RuD41cRLk141TcKtwDXD%2FY4txHlKyxq%2B7VH2P%2FHvnkcIxi%2FuBOFiOasJRD1KYjqV6k9s6uc0%2Bwwcifh%2B8it8Xt%2FJIuOxnIieA8yCyGq6WpiCsn68frcNl2d0Z2kcUC%2FWWY74n6T69y5aFlHFObB43ffHSzL0tvEUheSmQOm1KQS5wD2HCppenznXsng5wi0xj5t2E8JyLQeGp5vvU5dcWjcPWL9uc%2BoSR0B1uS%2Bxmw1P47%2BuPyBX0fdqh1g%2BIaOfHnuXavTLzWPHryW55ikNR2sZwBYI3A1io6%2BdOaecYvEvk3In5DlR09WbyBCP93sWQV2RbXAYBuCRtUsEC%2BFVqWePcQVKQZ8f%2BHg1MtmzcoQEPeDNve6rHbGljubkCVkDoiK%2BvVL0Usvtd8QPtFZNFGzbGC5hlmDfmgF7peNDG%2BmtsZmly6PCu2nTlT8Hl%2Bs4pSDtT%2BSuk6t2teAJT9g7xEMQ2jMhtcfEyd%2BKj0xOuAL%2Bo0%2BK%2F75a1XmKCp2tpd8VlPn8F1bseNyD61swzQEl5S%2B%2FpTT5L%2BFDYN%2B788qnE2rzRC%2BDExn6ktrija7hq8ytCpS%2BNq%2FoUCtmlC68%2BfsuEEAPGQm3Ul8LnzMrtlu9niW0OhT6MZRVGSnth0nPqkQDsaWL%2B5KxnaxlIw1br7vAY6pgE3yLv3PxrbR3SLqazm5NJfP%2FuHNcDIGF8FKZ2M8JiMyY7VA6D97YR%2FrDQLId4oejQKSrCXYeDEtqsu8azKd1XYFEGV7MN0y5gXQ81mCt%2B9D1DCLg4GSKUzMGgYgd1KHWqa3tL6IiPWOTL53ONPiQntHym5FAFQNjwTKQ5mzVUhPggH9niNGrQwV1N50hnQtFlBoA3N%2FAuvtlgk1Y5qKJw5tHME8UFG&X-Amz-Signature=07b73ccbc0e8d0543cf55769d7b5cc39e9f22c3363fed813f5ab2948edc2d521&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEKPKM3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVKVa2wGW8o2mlYye9jbfSLVXLbhpNqOw8IzjMtya2TAiAiOaRO7QRi9n2bQyS2MMGu5rTpkRAMdzvr6Idt4NEAhSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB4RuD41cRLk141TcKtwDXD%2FY4txHlKyxq%2B7VH2P%2FHvnkcIxi%2FuBOFiOasJRD1KYjqV6k9s6uc0%2Bwwcifh%2B8it8Xt%2FJIuOxnIieA8yCyGq6WpiCsn68frcNl2d0Z2kcUC%2FWWY74n6T69y5aFlHFObB43ffHSzL0tvEUheSmQOm1KQS5wD2HCppenznXsng5wi0xj5t2E8JyLQeGp5vvU5dcWjcPWL9uc%2BoSR0B1uS%2Bxmw1P47%2BuPyBX0fdqh1g%2BIaOfHnuXavTLzWPHryW55ikNR2sZwBYI3A1io6%2BdOaecYvEvk3In5DlR09WbyBCP93sWQV2RbXAYBuCRtUsEC%2BFVqWePcQVKQZ8f%2BHg1MtmzcoQEPeDNve6rHbGljubkCVkDoiK%2BvVL0Usvtd8QPtFZNFGzbGC5hlmDfmgF7peNDG%2BmtsZmly6PCu2nTlT8Hl%2Bs4pSDtT%2BSuk6t2teAJT9g7xEMQ2jMhtcfEyd%2BKj0xOuAL%2Bo0%2BK%2F75a1XmKCp2tpd8VlPn8F1bseNyD61swzQEl5S%2B%2FpTT5L%2BFDYN%2B788qnE2rzRC%2BDExn6ktrija7hq8ytCpS%2BNq%2FoUCtmlC68%2BfsuEEAPGQm3Ul8LnzMrtlu9niW0OhT6MZRVGSnth0nPqkQDsaWL%2B5KxnaxlIw1br7vAY6pgE3yLv3PxrbR3SLqazm5NJfP%2FuHNcDIGF8FKZ2M8JiMyY7VA6D97YR%2FrDQLId4oejQKSrCXYeDEtqsu8azKd1XYFEGV7MN0y5gXQ81mCt%2B9D1DCLg4GSKUzMGgYgd1KHWqa3tL6IiPWOTL53ONPiQntHym5FAFQNjwTKQ5mzVUhPggH9niNGrQwV1N50hnQtFlBoA3N%2FAuvtlgk1Y5qKJw5tHME8UFG&X-Amz-Signature=bfe7abf0176c2838df4a24dd4f5eca9bea0a99ec68d90bdcf62e1dc477fa0972&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEKPKM3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVKVa2wGW8o2mlYye9jbfSLVXLbhpNqOw8IzjMtya2TAiAiOaRO7QRi9n2bQyS2MMGu5rTpkRAMdzvr6Idt4NEAhSqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB4RuD41cRLk141TcKtwDXD%2FY4txHlKyxq%2B7VH2P%2FHvnkcIxi%2FuBOFiOasJRD1KYjqV6k9s6uc0%2Bwwcifh%2B8it8Xt%2FJIuOxnIieA8yCyGq6WpiCsn68frcNl2d0Z2kcUC%2FWWY74n6T69y5aFlHFObB43ffHSzL0tvEUheSmQOm1KQS5wD2HCppenznXsng5wi0xj5t2E8JyLQeGp5vvU5dcWjcPWL9uc%2BoSR0B1uS%2Bxmw1P47%2BuPyBX0fdqh1g%2BIaOfHnuXavTLzWPHryW55ikNR2sZwBYI3A1io6%2BdOaecYvEvk3In5DlR09WbyBCP93sWQV2RbXAYBuCRtUsEC%2BFVqWePcQVKQZ8f%2BHg1MtmzcoQEPeDNve6rHbGljubkCVkDoiK%2BvVL0Usvtd8QPtFZNFGzbGC5hlmDfmgF7peNDG%2BmtsZmly6PCu2nTlT8Hl%2Bs4pSDtT%2BSuk6t2teAJT9g7xEMQ2jMhtcfEyd%2BKj0xOuAL%2Bo0%2BK%2F75a1XmKCp2tpd8VlPn8F1bseNyD61swzQEl5S%2B%2FpTT5L%2BFDYN%2B788qnE2rzRC%2BDExn6ktrija7hq8ytCpS%2BNq%2FoUCtmlC68%2BfsuEEAPGQm3Ul8LnzMrtlu9niW0OhT6MZRVGSnth0nPqkQDsaWL%2B5KxnaxlIw1br7vAY6pgE3yLv3PxrbR3SLqazm5NJfP%2FuHNcDIGF8FKZ2M8JiMyY7VA6D97YR%2FrDQLId4oejQKSrCXYeDEtqsu8azKd1XYFEGV7MN0y5gXQ81mCt%2B9D1DCLg4GSKUzMGgYgd1KHWqa3tL6IiPWOTL53ONPiQntHym5FAFQNjwTKQ5mzVUhPggH9niNGrQwV1N50hnQtFlBoA3N%2FAuvtlgk1Y5qKJw5tHME8UFG&X-Amz-Signature=03fceb4796ccf96197e1865f1643eb995196147574163820288a90601295d044&X-Amz-SignedHeaders=host&x-id=GetObject)
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


