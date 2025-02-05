

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDO5WVAE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDq4G%2FIGN3BUYb%2FRLP92TvYYqtMa6VxHPwOvo%2F0sGOUfAiAfqEva%2FI9%2B6iZ5gTmhSHSjfjFL5LYzd%2FTd17BdksiOfir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMV%2FVCSx%2BTGm3zVFAgKtwDkXgH7cZqTWFxrXDHPKH%2BgGqUC0juF7lf8WrSOvwEYuqt2kufSEcId13vC5G%2Fb6uDlqHY6KoYR9bb4ZEDjLOEdHF7%2FfdsaIhTwNsqBt%2FzgFoqLYDxOZCzJNLFL2FMQ7%2BYycfW8NIBCRQUXHQsV8rtC3UXOhVQQOKcPeppZXKv0XkrUMyepNWbSpcbSrQckWpff6dz8VDGPH9MpR6j7LDGEQ9KeeHKRFMLK1Y1noGkFcQ%2FNAyQkKOD6hn3N9ObZ%2BKIcI0Ahu9rgln0dOXWrdypIJyR3ScpLLZMRgR%2BN9NtGRo4%2FJftWBuYMmNqZjGw2R7u6IPPaNifEqgZmNetLWdWNcEIiACzPkIWWO5tgHJXTr3dPQjzvaa1z8Z%2F0egkWNVMo4RU7Nl1dfULSaYmldwZHoeG%2B8sS%2BAwS7tzzHZsKoesOxdOynI5qUZAVxBvH%2BcJfgv0%2Bk%2FM%2F%2BKWI7gcVnYwd%2B%2FyGCTizmxjoh346pYDZvgF3PY63rLbM2MDGuJee0kdH%2B5cpYcLTH1yLODWCMdGgtkAazrWsL6wA3wJhFLlE%2FhlU3uIZPDUAPoYYGV6nYdLJpdWC2TM4FrUqtD9jq4YtXs6HNOo0WBWR5wJH8BUD2DxqX9yMpuKCH8xxuEgw%2BO6MvQY6pgGQuO19i%2Bl6xvqB%2Br8tzPKY5yLa%2FZgI74IYQTsxaJQeehmfHlYuRKeQiXTssHSvOFie9CYupbOH7KOzlmGN7KPxVMT%2FfrS789R%2FEa0gPPpDUwNONUnFflasoZUsN0p2RzmON0kb6BmfApTQ5aHIpLImQd39ch7yuLlBTMiMIWzhQmL%2FZos60NMH9ttddvARwotwzQXJhq6COEgFk9tB2kkPmJXjpnQM&X-Amz-Signature=725d6fcf86987c1c2873a4af2c2d912b8175dc1bf307d76a675ddb9802ebbe7e&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LWAUQDC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCICmkn4DNoUdDc6YklzhQgBkoFWCcA1CC5B7JpURp0RShAiEAnGbIhz2IJSxoo1TW8f6i9zgx6alzdUToFKSzwtqKB%2B8q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDC0ctAVbWbD0DUxnqCrcA%2B2fRq6glPx8L1aWmghvQPfJ%2FD5gl62CoLFmC7j%2BGFeFla%2FonizSJ2IHFZpCQPQaum1U4osjIbM9sUHcgZayCf0F8T%2BJRO9VSdv4YGGMGCeVirbsUWKiz65tUz6w5gesEtyYPIj6YNZF3JMiS5SPTJc8xoYHnktg9NSvxwNrmPVnKaAoFN%2F1OOieNohnBR41pNu3Zmj0ORfD32w8FLjdFrSUMkp%2BeT0xXXSVC7wc1GMJlsON%2FNIEehfve08rF3sb6R2Imuc9wn4Ir8jcYha%2Br2XMeva%2BcC6r5XzI62tqu1CfVp8hawBGi8nzN4fRpkZgi5I4sTQt1qetSt2P5nSYQFTbzDJITx6QDe8QaHrGoBwZXBdQcwk3I949Yd%2FsB4VdYy%2BwS%2FDCTqKqRnmnxId%2BPMcWX7mAjW6KadZ1gSbZu5Hvl5QtuzWsioLgY19QPyVQBqdrFeDsANCoB%2BuUrzBr69bw%2Fd3KMVHJrEWvLDDf1P1bshYxbEOXekemZA0obMD78fngyfyedXV2kIlGR5sxZbBFrIkmzyeHXC4Pqkp%2Bn4zr7EkbKLFrpt1nZt9P%2F%2BtDnjp21BRF0LooPOfUtfmSVAsr5ksl1mK5K%2FOaZBvutQe3dqoSjFLAkjfhVTZ5MNbvjL0GOqUBfrWv5EjdVef93YELErccjRL09i0RMzGj%2B%2B3ckTsQKHy7upnfTkXESQD3JpVxscn20bZnont7Vtm4VbscALjiEqDFanSQ3SdkKM5VJs1lqD7t2xdbiRVqWTOJ4cXKpy9Pld%2FVUjI9J0TbzLOfOuosHRFCrh%2BFZcwJJqC4Fo8%2Bfd4zg4bB%2BAj1g%2BBHo2IvteebXs4Iox4gQhj3fFNfe%2F7L7jVs09um&X-Amz-Signature=c69e3d6dc8b461bc30096c97706fff8ed33241d90396ad5203fdfd7a7360a8be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LWAUQDC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCICmkn4DNoUdDc6YklzhQgBkoFWCcA1CC5B7JpURp0RShAiEAnGbIhz2IJSxoo1TW8f6i9zgx6alzdUToFKSzwtqKB%2B8q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDC0ctAVbWbD0DUxnqCrcA%2B2fRq6glPx8L1aWmghvQPfJ%2FD5gl62CoLFmC7j%2BGFeFla%2FonizSJ2IHFZpCQPQaum1U4osjIbM9sUHcgZayCf0F8T%2BJRO9VSdv4YGGMGCeVirbsUWKiz65tUz6w5gesEtyYPIj6YNZF3JMiS5SPTJc8xoYHnktg9NSvxwNrmPVnKaAoFN%2F1OOieNohnBR41pNu3Zmj0ORfD32w8FLjdFrSUMkp%2BeT0xXXSVC7wc1GMJlsON%2FNIEehfve08rF3sb6R2Imuc9wn4Ir8jcYha%2Br2XMeva%2BcC6r5XzI62tqu1CfVp8hawBGi8nzN4fRpkZgi5I4sTQt1qetSt2P5nSYQFTbzDJITx6QDe8QaHrGoBwZXBdQcwk3I949Yd%2FsB4VdYy%2BwS%2FDCTqKqRnmnxId%2BPMcWX7mAjW6KadZ1gSbZu5Hvl5QtuzWsioLgY19QPyVQBqdrFeDsANCoB%2BuUrzBr69bw%2Fd3KMVHJrEWvLDDf1P1bshYxbEOXekemZA0obMD78fngyfyedXV2kIlGR5sxZbBFrIkmzyeHXC4Pqkp%2Bn4zr7EkbKLFrpt1nZt9P%2F%2BtDnjp21BRF0LooPOfUtfmSVAsr5ksl1mK5K%2FOaZBvutQe3dqoSjFLAkjfhVTZ5MNbvjL0GOqUBfrWv5EjdVef93YELErccjRL09i0RMzGj%2B%2B3ckTsQKHy7upnfTkXESQD3JpVxscn20bZnont7Vtm4VbscALjiEqDFanSQ3SdkKM5VJs1lqD7t2xdbiRVqWTOJ4cXKpy9Pld%2FVUjI9J0TbzLOfOuosHRFCrh%2BFZcwJJqC4Fo8%2Bfd4zg4bB%2BAj1g%2BBHo2IvteebXs4Iox4gQhj3fFNfe%2F7L7jVs09um&X-Amz-Signature=02b54cf606c764242ec32023e962ac7e46dbc636958327e764fae690350ef5ad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LWAUQDC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCICmkn4DNoUdDc6YklzhQgBkoFWCcA1CC5B7JpURp0RShAiEAnGbIhz2IJSxoo1TW8f6i9zgx6alzdUToFKSzwtqKB%2B8q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDC0ctAVbWbD0DUxnqCrcA%2B2fRq6glPx8L1aWmghvQPfJ%2FD5gl62CoLFmC7j%2BGFeFla%2FonizSJ2IHFZpCQPQaum1U4osjIbM9sUHcgZayCf0F8T%2BJRO9VSdv4YGGMGCeVirbsUWKiz65tUz6w5gesEtyYPIj6YNZF3JMiS5SPTJc8xoYHnktg9NSvxwNrmPVnKaAoFN%2F1OOieNohnBR41pNu3Zmj0ORfD32w8FLjdFrSUMkp%2BeT0xXXSVC7wc1GMJlsON%2FNIEehfve08rF3sb6R2Imuc9wn4Ir8jcYha%2Br2XMeva%2BcC6r5XzI62tqu1CfVp8hawBGi8nzN4fRpkZgi5I4sTQt1qetSt2P5nSYQFTbzDJITx6QDe8QaHrGoBwZXBdQcwk3I949Yd%2FsB4VdYy%2BwS%2FDCTqKqRnmnxId%2BPMcWX7mAjW6KadZ1gSbZu5Hvl5QtuzWsioLgY19QPyVQBqdrFeDsANCoB%2BuUrzBr69bw%2Fd3KMVHJrEWvLDDf1P1bshYxbEOXekemZA0obMD78fngyfyedXV2kIlGR5sxZbBFrIkmzyeHXC4Pqkp%2Bn4zr7EkbKLFrpt1nZt9P%2F%2BtDnjp21BRF0LooPOfUtfmSVAsr5ksl1mK5K%2FOaZBvutQe3dqoSjFLAkjfhVTZ5MNbvjL0GOqUBfrWv5EjdVef93YELErccjRL09i0RMzGj%2B%2B3ckTsQKHy7upnfTkXESQD3JpVxscn20bZnont7Vtm4VbscALjiEqDFanSQ3SdkKM5VJs1lqD7t2xdbiRVqWTOJ4cXKpy9Pld%2FVUjI9J0TbzLOfOuosHRFCrh%2BFZcwJJqC4Fo8%2Bfd4zg4bB%2BAj1g%2BBHo2IvteebXs4Iox4gQhj3fFNfe%2F7L7jVs09um&X-Amz-Signature=d6ed2d2504a351462316f0322aea632a61f9923872dadcb9464b8f498c88ba42&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LWAUQDC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCICmkn4DNoUdDc6YklzhQgBkoFWCcA1CC5B7JpURp0RShAiEAnGbIhz2IJSxoo1TW8f6i9zgx6alzdUToFKSzwtqKB%2B8q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDC0ctAVbWbD0DUxnqCrcA%2B2fRq6glPx8L1aWmghvQPfJ%2FD5gl62CoLFmC7j%2BGFeFla%2FonizSJ2IHFZpCQPQaum1U4osjIbM9sUHcgZayCf0F8T%2BJRO9VSdv4YGGMGCeVirbsUWKiz65tUz6w5gesEtyYPIj6YNZF3JMiS5SPTJc8xoYHnktg9NSvxwNrmPVnKaAoFN%2F1OOieNohnBR41pNu3Zmj0ORfD32w8FLjdFrSUMkp%2BeT0xXXSVC7wc1GMJlsON%2FNIEehfve08rF3sb6R2Imuc9wn4Ir8jcYha%2Br2XMeva%2BcC6r5XzI62tqu1CfVp8hawBGi8nzN4fRpkZgi5I4sTQt1qetSt2P5nSYQFTbzDJITx6QDe8QaHrGoBwZXBdQcwk3I949Yd%2FsB4VdYy%2BwS%2FDCTqKqRnmnxId%2BPMcWX7mAjW6KadZ1gSbZu5Hvl5QtuzWsioLgY19QPyVQBqdrFeDsANCoB%2BuUrzBr69bw%2Fd3KMVHJrEWvLDDf1P1bshYxbEOXekemZA0obMD78fngyfyedXV2kIlGR5sxZbBFrIkmzyeHXC4Pqkp%2Bn4zr7EkbKLFrpt1nZt9P%2F%2BtDnjp21BRF0LooPOfUtfmSVAsr5ksl1mK5K%2FOaZBvutQe3dqoSjFLAkjfhVTZ5MNbvjL0GOqUBfrWv5EjdVef93YELErccjRL09i0RMzGj%2B%2B3ckTsQKHy7upnfTkXESQD3JpVxscn20bZnont7Vtm4VbscALjiEqDFanSQ3SdkKM5VJs1lqD7t2xdbiRVqWTOJ4cXKpy9Pld%2FVUjI9J0TbzLOfOuosHRFCrh%2BFZcwJJqC4Fo8%2Bfd4zg4bB%2BAj1g%2BBHo2IvteebXs4Iox4gQhj3fFNfe%2F7L7jVs09um&X-Amz-Signature=84aeaecfb72b7eb483590245dea132e285834b1ae9104197d8332dcb4c259a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LWAUQDC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCICmkn4DNoUdDc6YklzhQgBkoFWCcA1CC5B7JpURp0RShAiEAnGbIhz2IJSxoo1TW8f6i9zgx6alzdUToFKSzwtqKB%2B8q%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDC0ctAVbWbD0DUxnqCrcA%2B2fRq6glPx8L1aWmghvQPfJ%2FD5gl62CoLFmC7j%2BGFeFla%2FonizSJ2IHFZpCQPQaum1U4osjIbM9sUHcgZayCf0F8T%2BJRO9VSdv4YGGMGCeVirbsUWKiz65tUz6w5gesEtyYPIj6YNZF3JMiS5SPTJc8xoYHnktg9NSvxwNrmPVnKaAoFN%2F1OOieNohnBR41pNu3Zmj0ORfD32w8FLjdFrSUMkp%2BeT0xXXSVC7wc1GMJlsON%2FNIEehfve08rF3sb6R2Imuc9wn4Ir8jcYha%2Br2XMeva%2BcC6r5XzI62tqu1CfVp8hawBGi8nzN4fRpkZgi5I4sTQt1qetSt2P5nSYQFTbzDJITx6QDe8QaHrGoBwZXBdQcwk3I949Yd%2FsB4VdYy%2BwS%2FDCTqKqRnmnxId%2BPMcWX7mAjW6KadZ1gSbZu5Hvl5QtuzWsioLgY19QPyVQBqdrFeDsANCoB%2BuUrzBr69bw%2Fd3KMVHJrEWvLDDf1P1bshYxbEOXekemZA0obMD78fngyfyedXV2kIlGR5sxZbBFrIkmzyeHXC4Pqkp%2Bn4zr7EkbKLFrpt1nZt9P%2F%2BtDnjp21BRF0LooPOfUtfmSVAsr5ksl1mK5K%2FOaZBvutQe3dqoSjFLAkjfhVTZ5MNbvjL0GOqUBfrWv5EjdVef93YELErccjRL09i0RMzGj%2B%2B3ckTsQKHy7upnfTkXESQD3JpVxscn20bZnont7Vtm4VbscALjiEqDFanSQ3SdkKM5VJs1lqD7t2xdbiRVqWTOJ4cXKpy9Pld%2FVUjI9J0TbzLOfOuosHRFCrh%2BFZcwJJqC4Fo8%2Bfd4zg4bB%2BAj1g%2BBHo2IvteebXs4Iox4gQhj3fFNfe%2F7L7jVs09um&X-Amz-Signature=257f7022b9e59e74e0478306ac7d3d0f0838331f7f5226f93875fdd1fdd66fc6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDO5WVAE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDq4G%2FIGN3BUYb%2FRLP92TvYYqtMa6VxHPwOvo%2F0sGOUfAiAfqEva%2FI9%2B6iZ5gTmhSHSjfjFL5LYzd%2FTd17BdksiOfir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMV%2FVCSx%2BTGm3zVFAgKtwDkXgH7cZqTWFxrXDHPKH%2BgGqUC0juF7lf8WrSOvwEYuqt2kufSEcId13vC5G%2Fb6uDlqHY6KoYR9bb4ZEDjLOEdHF7%2FfdsaIhTwNsqBt%2FzgFoqLYDxOZCzJNLFL2FMQ7%2BYycfW8NIBCRQUXHQsV8rtC3UXOhVQQOKcPeppZXKv0XkrUMyepNWbSpcbSrQckWpff6dz8VDGPH9MpR6j7LDGEQ9KeeHKRFMLK1Y1noGkFcQ%2FNAyQkKOD6hn3N9ObZ%2BKIcI0Ahu9rgln0dOXWrdypIJyR3ScpLLZMRgR%2BN9NtGRo4%2FJftWBuYMmNqZjGw2R7u6IPPaNifEqgZmNetLWdWNcEIiACzPkIWWO5tgHJXTr3dPQjzvaa1z8Z%2F0egkWNVMo4RU7Nl1dfULSaYmldwZHoeG%2B8sS%2BAwS7tzzHZsKoesOxdOynI5qUZAVxBvH%2BcJfgv0%2Bk%2FM%2F%2BKWI7gcVnYwd%2B%2FyGCTizmxjoh346pYDZvgF3PY63rLbM2MDGuJee0kdH%2B5cpYcLTH1yLODWCMdGgtkAazrWsL6wA3wJhFLlE%2FhlU3uIZPDUAPoYYGV6nYdLJpdWC2TM4FrUqtD9jq4YtXs6HNOo0WBWR5wJH8BUD2DxqX9yMpuKCH8xxuEgw%2BO6MvQY6pgGQuO19i%2Bl6xvqB%2Br8tzPKY5yLa%2FZgI74IYQTsxaJQeehmfHlYuRKeQiXTssHSvOFie9CYupbOH7KOzlmGN7KPxVMT%2FfrS789R%2FEa0gPPpDUwNONUnFflasoZUsN0p2RzmON0kb6BmfApTQ5aHIpLImQd39ch7yuLlBTMiMIWzhQmL%2FZos60NMH9ttddvARwotwzQXJhq6COEgFk9tB2kkPmJXjpnQM&X-Amz-Signature=183a35b57cc92266a5c4e05f56ec4a867fdb14c691d920c9de21d5fbdbe67dd8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDO5WVAE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDq4G%2FIGN3BUYb%2FRLP92TvYYqtMa6VxHPwOvo%2F0sGOUfAiAfqEva%2FI9%2B6iZ5gTmhSHSjfjFL5LYzd%2FTd17BdksiOfir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMV%2FVCSx%2BTGm3zVFAgKtwDkXgH7cZqTWFxrXDHPKH%2BgGqUC0juF7lf8WrSOvwEYuqt2kufSEcId13vC5G%2Fb6uDlqHY6KoYR9bb4ZEDjLOEdHF7%2FfdsaIhTwNsqBt%2FzgFoqLYDxOZCzJNLFL2FMQ7%2BYycfW8NIBCRQUXHQsV8rtC3UXOhVQQOKcPeppZXKv0XkrUMyepNWbSpcbSrQckWpff6dz8VDGPH9MpR6j7LDGEQ9KeeHKRFMLK1Y1noGkFcQ%2FNAyQkKOD6hn3N9ObZ%2BKIcI0Ahu9rgln0dOXWrdypIJyR3ScpLLZMRgR%2BN9NtGRo4%2FJftWBuYMmNqZjGw2R7u6IPPaNifEqgZmNetLWdWNcEIiACzPkIWWO5tgHJXTr3dPQjzvaa1z8Z%2F0egkWNVMo4RU7Nl1dfULSaYmldwZHoeG%2B8sS%2BAwS7tzzHZsKoesOxdOynI5qUZAVxBvH%2BcJfgv0%2Bk%2FM%2F%2BKWI7gcVnYwd%2B%2FyGCTizmxjoh346pYDZvgF3PY63rLbM2MDGuJee0kdH%2B5cpYcLTH1yLODWCMdGgtkAazrWsL6wA3wJhFLlE%2FhlU3uIZPDUAPoYYGV6nYdLJpdWC2TM4FrUqtD9jq4YtXs6HNOo0WBWR5wJH8BUD2DxqX9yMpuKCH8xxuEgw%2BO6MvQY6pgGQuO19i%2Bl6xvqB%2Br8tzPKY5yLa%2FZgI74IYQTsxaJQeehmfHlYuRKeQiXTssHSvOFie9CYupbOH7KOzlmGN7KPxVMT%2FfrS789R%2FEa0gPPpDUwNONUnFflasoZUsN0p2RzmON0kb6BmfApTQ5aHIpLImQd39ch7yuLlBTMiMIWzhQmL%2FZos60NMH9ttddvARwotwzQXJhq6COEgFk9tB2kkPmJXjpnQM&X-Amz-Signature=0e9df9812857fd89f8e0376001add7ca21c8ef82a637d9f03ec8b9ea03b903d3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDO5WVAE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDq4G%2FIGN3BUYb%2FRLP92TvYYqtMa6VxHPwOvo%2F0sGOUfAiAfqEva%2FI9%2B6iZ5gTmhSHSjfjFL5LYzd%2FTd17BdksiOfir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMV%2FVCSx%2BTGm3zVFAgKtwDkXgH7cZqTWFxrXDHPKH%2BgGqUC0juF7lf8WrSOvwEYuqt2kufSEcId13vC5G%2Fb6uDlqHY6KoYR9bb4ZEDjLOEdHF7%2FfdsaIhTwNsqBt%2FzgFoqLYDxOZCzJNLFL2FMQ7%2BYycfW8NIBCRQUXHQsV8rtC3UXOhVQQOKcPeppZXKv0XkrUMyepNWbSpcbSrQckWpff6dz8VDGPH9MpR6j7LDGEQ9KeeHKRFMLK1Y1noGkFcQ%2FNAyQkKOD6hn3N9ObZ%2BKIcI0Ahu9rgln0dOXWrdypIJyR3ScpLLZMRgR%2BN9NtGRo4%2FJftWBuYMmNqZjGw2R7u6IPPaNifEqgZmNetLWdWNcEIiACzPkIWWO5tgHJXTr3dPQjzvaa1z8Z%2F0egkWNVMo4RU7Nl1dfULSaYmldwZHoeG%2B8sS%2BAwS7tzzHZsKoesOxdOynI5qUZAVxBvH%2BcJfgv0%2Bk%2FM%2F%2BKWI7gcVnYwd%2B%2FyGCTizmxjoh346pYDZvgF3PY63rLbM2MDGuJee0kdH%2B5cpYcLTH1yLODWCMdGgtkAazrWsL6wA3wJhFLlE%2FhlU3uIZPDUAPoYYGV6nYdLJpdWC2TM4FrUqtD9jq4YtXs6HNOo0WBWR5wJH8BUD2DxqX9yMpuKCH8xxuEgw%2BO6MvQY6pgGQuO19i%2Bl6xvqB%2Br8tzPKY5yLa%2FZgI74IYQTsxaJQeehmfHlYuRKeQiXTssHSvOFie9CYupbOH7KOzlmGN7KPxVMT%2FfrS789R%2FEa0gPPpDUwNONUnFflasoZUsN0p2RzmON0kb6BmfApTQ5aHIpLImQd39ch7yuLlBTMiMIWzhQmL%2FZos60NMH9ttddvARwotwzQXJhq6COEgFk9tB2kkPmJXjpnQM&X-Amz-Signature=029d297c52b3fb655ff7a3516e08a9faa0a1c501f02aa153f7296083cb9340a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDO5WVAE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDq4G%2FIGN3BUYb%2FRLP92TvYYqtMa6VxHPwOvo%2F0sGOUfAiAfqEva%2FI9%2B6iZ5gTmhSHSjfjFL5LYzd%2FTd17BdksiOfir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMV%2FVCSx%2BTGm3zVFAgKtwDkXgH7cZqTWFxrXDHPKH%2BgGqUC0juF7lf8WrSOvwEYuqt2kufSEcId13vC5G%2Fb6uDlqHY6KoYR9bb4ZEDjLOEdHF7%2FfdsaIhTwNsqBt%2FzgFoqLYDxOZCzJNLFL2FMQ7%2BYycfW8NIBCRQUXHQsV8rtC3UXOhVQQOKcPeppZXKv0XkrUMyepNWbSpcbSrQckWpff6dz8VDGPH9MpR6j7LDGEQ9KeeHKRFMLK1Y1noGkFcQ%2FNAyQkKOD6hn3N9ObZ%2BKIcI0Ahu9rgln0dOXWrdypIJyR3ScpLLZMRgR%2BN9NtGRo4%2FJftWBuYMmNqZjGw2R7u6IPPaNifEqgZmNetLWdWNcEIiACzPkIWWO5tgHJXTr3dPQjzvaa1z8Z%2F0egkWNVMo4RU7Nl1dfULSaYmldwZHoeG%2B8sS%2BAwS7tzzHZsKoesOxdOynI5qUZAVxBvH%2BcJfgv0%2Bk%2FM%2F%2BKWI7gcVnYwd%2B%2FyGCTizmxjoh346pYDZvgF3PY63rLbM2MDGuJee0kdH%2B5cpYcLTH1yLODWCMdGgtkAazrWsL6wA3wJhFLlE%2FhlU3uIZPDUAPoYYGV6nYdLJpdWC2TM4FrUqtD9jq4YtXs6HNOo0WBWR5wJH8BUD2DxqX9yMpuKCH8xxuEgw%2BO6MvQY6pgGQuO19i%2Bl6xvqB%2Br8tzPKY5yLa%2FZgI74IYQTsxaJQeehmfHlYuRKeQiXTssHSvOFie9CYupbOH7KOzlmGN7KPxVMT%2FfrS789R%2FEa0gPPpDUwNONUnFflasoZUsN0p2RzmON0kb6BmfApTQ5aHIpLImQd39ch7yuLlBTMiMIWzhQmL%2FZos60NMH9ttddvARwotwzQXJhq6COEgFk9tB2kkPmJXjpnQM&X-Amz-Signature=07388655db935a5334cb2d44f24879df88431ae79a892f5188a4d64e7c10082a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDO5WVAE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDq4G%2FIGN3BUYb%2FRLP92TvYYqtMa6VxHPwOvo%2F0sGOUfAiAfqEva%2FI9%2B6iZ5gTmhSHSjfjFL5LYzd%2FTd17BdksiOfir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMV%2FVCSx%2BTGm3zVFAgKtwDkXgH7cZqTWFxrXDHPKH%2BgGqUC0juF7lf8WrSOvwEYuqt2kufSEcId13vC5G%2Fb6uDlqHY6KoYR9bb4ZEDjLOEdHF7%2FfdsaIhTwNsqBt%2FzgFoqLYDxOZCzJNLFL2FMQ7%2BYycfW8NIBCRQUXHQsV8rtC3UXOhVQQOKcPeppZXKv0XkrUMyepNWbSpcbSrQckWpff6dz8VDGPH9MpR6j7LDGEQ9KeeHKRFMLK1Y1noGkFcQ%2FNAyQkKOD6hn3N9ObZ%2BKIcI0Ahu9rgln0dOXWrdypIJyR3ScpLLZMRgR%2BN9NtGRo4%2FJftWBuYMmNqZjGw2R7u6IPPaNifEqgZmNetLWdWNcEIiACzPkIWWO5tgHJXTr3dPQjzvaa1z8Z%2F0egkWNVMo4RU7Nl1dfULSaYmldwZHoeG%2B8sS%2BAwS7tzzHZsKoesOxdOynI5qUZAVxBvH%2BcJfgv0%2Bk%2FM%2F%2BKWI7gcVnYwd%2B%2FyGCTizmxjoh346pYDZvgF3PY63rLbM2MDGuJee0kdH%2B5cpYcLTH1yLODWCMdGgtkAazrWsL6wA3wJhFLlE%2FhlU3uIZPDUAPoYYGV6nYdLJpdWC2TM4FrUqtD9jq4YtXs6HNOo0WBWR5wJH8BUD2DxqX9yMpuKCH8xxuEgw%2BO6MvQY6pgGQuO19i%2Bl6xvqB%2Br8tzPKY5yLa%2FZgI74IYQTsxaJQeehmfHlYuRKeQiXTssHSvOFie9CYupbOH7KOzlmGN7KPxVMT%2FfrS789R%2FEa0gPPpDUwNONUnFflasoZUsN0p2RzmON0kb6BmfApTQ5aHIpLImQd39ch7yuLlBTMiMIWzhQmL%2FZos60NMH9ttddvARwotwzQXJhq6COEgFk9tB2kkPmJXjpnQM&X-Amz-Signature=530e73dab885917031b099e3e4e317f4897fff035e377f8c0b2c1cbecfdd879b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


