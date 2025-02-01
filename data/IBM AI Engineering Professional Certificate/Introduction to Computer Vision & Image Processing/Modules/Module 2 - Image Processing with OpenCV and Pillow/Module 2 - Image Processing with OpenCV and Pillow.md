

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MEKGO3Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg0p3XH%2FehRRODBocliYH5kQtohjlnjv7O3g6ZJwl5kQIgTZQFbK%2FXxHrp2XkDeeqRqALi35ON9qFtqJA%2FrTpr2DwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAg0BHT%2FfcjrkweCCrcA51gwRbUXFEYkEYuJ8u4GBIXFrlAmj3w1cszf0yE%2FSk0gwc1kEKB7SbXOWihESaeGBYpHPQ0NaJ8rFITozhahnAyzkwF3OE0sV%2Fc3odRxHPKR%2F%2B41wceyeQ5sgRAjYOr0tdvnNtK%2BwZfDPloPuL5rqcccNoXKnmXFWSWISRXNzvCbygnNM1%2F%2BA87IX7joWiB%2BZeWSZzlpIjbQjlaLjJI6TSCyVnAJFUAcBV%2Fi1Z9tRqUQcPDDGpS%2B%2F8NOlOhrzCFjFeQMJDljhA8AMIl4YGaLts0WRWEe34OBuCpNHeVNBgKeWJAQNJdPnSZ9upbppCosQGzG7lPm0ta5N7FTS2V5T%2FPECZqoBaClwPoE%2BZjZO124Wp%2F6biQxkjexYfIfziDKENG3UHFGYD08xJ2X9TPlr7H%2B3Cjze8iW4GpXpT%2FHNm0siE8%2FtLl19Q9Kl%2BKCanNkUUmEo3qNOCN4A%2BcLxgnHV1NzFX4VgLSOZjiw62NGzvJjjnaFx1j8zGTCJL7yOBNH9LCa2MuKpmdnqG1uZfbRFubaxjQYhI1nKmkG4vUoeJw5wEpUKcdZqswbtENW9qojwdI1KMwHcDF5utSqV4n1fXIFkayJlUnuOjic%2F4HOFfJ3m8oMca1tefB4OKmMLz2%2BbwGOqUBsQjNmS6pdnGf94%2BBMx0F0KtQgM%2BiuWSav4rc86ELd922hDTYvc%2BLl2SNQp59k3ixlNVj%2BWJuAO%2BKzRar9TyaXXsDwsosYCuz43zLOnEqAU%2F05nS%2F0q%2B3eWIvHVibYYIo8MBgkEo8I1%2BM25dCOByoNEMI%2BdzNnz3vgj3vo%2FNqWSNA0lmXFOvoPuoV%2B2YifTsCK6c80fL%2BCQ%2Ft4b3SpTOloU4DDRu4&X-Amz-Signature=454215c7fe297fa24260875d0d5793731547e5ca03734cb5c00fc3f3ea3b2353&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IPFVM7H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcqdXKxN4rF4areArU%2F5BYX1%2BuuabG0GDb3v%2F%2FeoQ3ygIgDUS90%2FFCI0UJbu%2FoP0tGfC2p%2BR2G0FB2CbNr3OAZAewqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdQ2sjrpHyEK5MzRCrcA1MjUnGIRNmj5d8DGM2DQM8oTRMmFT7vDSnGwbGwaMr0sGNPLzQuTFwMPSTba7KJvS6ZPQ8ArcUOfqAyGfgoy0sejpLWm9yO%2F%2FAaaE1sTO1Opdo9CpR1U2s9e9c8d%2BMrC9LVdm3jnk6TVI6gPQ1naGeV191FmJhFm130txCxeTImhNNlfs1NEseHBFB2MAxFuPHyC5OEouZDc2utJ%2FygczV3NKYtNUEzlMyV%2Bd0FGtNnA0HpPoUDGIhoPNDWONUMeGh1c1pNriXFRfz6j8SSDaM1jTxUFAyUEXaGaay9GDzoZNBq4Zvut2oNWUsbI6gkosfcuigs0eOtU3VGh9m1QIOck6FLU0vAGQLEim2nSEW0BkE%2FZYgeKHq%2BDIlN3kP5IiyAygJSf2LurcdiQDR7cvIz%2Bt0kyI4aVbXdJ1HcOZNxQpGAUjL5Rq3a7kjUHh4rX0sh0thTV8%2FwJG48lEaLuHqw52N8JoZVZ5AAi5bjf5cmWP0M40b3a6vMOXcfDnCS%2BGlUx9q4nyM3%2FZ313%2BuT%2FXHWeedg8yC516%2F2JM9vACAttyMHbKaVFDQnhsfZl9B9cQ%2B%2B15Q2rmyNzrCNbpJBrQ9q0xyD%2F4Bi5YXbCvwP26kB1iwxKFm2rXusJczRML%2F3%2BbwGOqUBOaD0sMRnTJ95LMJpMmZzHf2oqqSv0eMaf2eCSDo9ffBtBvqeSooOnyYfyw283NkkE4eT81PZ%2FJ7ZrrhdDHg%2B7SaMobIzT17lgnJmGOcaBPgqvur9dpfaA6dfC0cYKwpz8hrNNSS3LKX3qdEMaxJnSfr%2BgqpTM19NYyjY8POjWqUGb1XzNXugAmCmTXiovzDYy07Hfcurytnk9eCac8KZ%2Fyel14SX&X-Amz-Signature=56204856ec92aa2a9fed77586af8de868e436c4ee4a6f537914ec3942b93702e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IPFVM7H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcqdXKxN4rF4areArU%2F5BYX1%2BuuabG0GDb3v%2F%2FeoQ3ygIgDUS90%2FFCI0UJbu%2FoP0tGfC2p%2BR2G0FB2CbNr3OAZAewqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdQ2sjrpHyEK5MzRCrcA1MjUnGIRNmj5d8DGM2DQM8oTRMmFT7vDSnGwbGwaMr0sGNPLzQuTFwMPSTba7KJvS6ZPQ8ArcUOfqAyGfgoy0sejpLWm9yO%2F%2FAaaE1sTO1Opdo9CpR1U2s9e9c8d%2BMrC9LVdm3jnk6TVI6gPQ1naGeV191FmJhFm130txCxeTImhNNlfs1NEseHBFB2MAxFuPHyC5OEouZDc2utJ%2FygczV3NKYtNUEzlMyV%2Bd0FGtNnA0HpPoUDGIhoPNDWONUMeGh1c1pNriXFRfz6j8SSDaM1jTxUFAyUEXaGaay9GDzoZNBq4Zvut2oNWUsbI6gkosfcuigs0eOtU3VGh9m1QIOck6FLU0vAGQLEim2nSEW0BkE%2FZYgeKHq%2BDIlN3kP5IiyAygJSf2LurcdiQDR7cvIz%2Bt0kyI4aVbXdJ1HcOZNxQpGAUjL5Rq3a7kjUHh4rX0sh0thTV8%2FwJG48lEaLuHqw52N8JoZVZ5AAi5bjf5cmWP0M40b3a6vMOXcfDnCS%2BGlUx9q4nyM3%2FZ313%2BuT%2FXHWeedg8yC516%2F2JM9vACAttyMHbKaVFDQnhsfZl9B9cQ%2B%2B15Q2rmyNzrCNbpJBrQ9q0xyD%2F4Bi5YXbCvwP26kB1iwxKFm2rXusJczRML%2F3%2BbwGOqUBOaD0sMRnTJ95LMJpMmZzHf2oqqSv0eMaf2eCSDo9ffBtBvqeSooOnyYfyw283NkkE4eT81PZ%2FJ7ZrrhdDHg%2B7SaMobIzT17lgnJmGOcaBPgqvur9dpfaA6dfC0cYKwpz8hrNNSS3LKX3qdEMaxJnSfr%2BgqpTM19NYyjY8POjWqUGb1XzNXugAmCmTXiovzDYy07Hfcurytnk9eCac8KZ%2Fyel14SX&X-Amz-Signature=2bf19a14ec86eec25ce0a2d6be1a394a4fe384a63182767712ad54d378a2f039&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IPFVM7H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcqdXKxN4rF4areArU%2F5BYX1%2BuuabG0GDb3v%2F%2FeoQ3ygIgDUS90%2FFCI0UJbu%2FoP0tGfC2p%2BR2G0FB2CbNr3OAZAewqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdQ2sjrpHyEK5MzRCrcA1MjUnGIRNmj5d8DGM2DQM8oTRMmFT7vDSnGwbGwaMr0sGNPLzQuTFwMPSTba7KJvS6ZPQ8ArcUOfqAyGfgoy0sejpLWm9yO%2F%2FAaaE1sTO1Opdo9CpR1U2s9e9c8d%2BMrC9LVdm3jnk6TVI6gPQ1naGeV191FmJhFm130txCxeTImhNNlfs1NEseHBFB2MAxFuPHyC5OEouZDc2utJ%2FygczV3NKYtNUEzlMyV%2Bd0FGtNnA0HpPoUDGIhoPNDWONUMeGh1c1pNriXFRfz6j8SSDaM1jTxUFAyUEXaGaay9GDzoZNBq4Zvut2oNWUsbI6gkosfcuigs0eOtU3VGh9m1QIOck6FLU0vAGQLEim2nSEW0BkE%2FZYgeKHq%2BDIlN3kP5IiyAygJSf2LurcdiQDR7cvIz%2Bt0kyI4aVbXdJ1HcOZNxQpGAUjL5Rq3a7kjUHh4rX0sh0thTV8%2FwJG48lEaLuHqw52N8JoZVZ5AAi5bjf5cmWP0M40b3a6vMOXcfDnCS%2BGlUx9q4nyM3%2FZ313%2BuT%2FXHWeedg8yC516%2F2JM9vACAttyMHbKaVFDQnhsfZl9B9cQ%2B%2B15Q2rmyNzrCNbpJBrQ9q0xyD%2F4Bi5YXbCvwP26kB1iwxKFm2rXusJczRML%2F3%2BbwGOqUBOaD0sMRnTJ95LMJpMmZzHf2oqqSv0eMaf2eCSDo9ffBtBvqeSooOnyYfyw283NkkE4eT81PZ%2FJ7ZrrhdDHg%2B7SaMobIzT17lgnJmGOcaBPgqvur9dpfaA6dfC0cYKwpz8hrNNSS3LKX3qdEMaxJnSfr%2BgqpTM19NYyjY8POjWqUGb1XzNXugAmCmTXiovzDYy07Hfcurytnk9eCac8KZ%2Fyel14SX&X-Amz-Signature=5bb69e4674beaabcf88e3adb1ff10611e925cd7611c31a9dddcbb5a69f3d28f0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IPFVM7H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcqdXKxN4rF4areArU%2F5BYX1%2BuuabG0GDb3v%2F%2FeoQ3ygIgDUS90%2FFCI0UJbu%2FoP0tGfC2p%2BR2G0FB2CbNr3OAZAewqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdQ2sjrpHyEK5MzRCrcA1MjUnGIRNmj5d8DGM2DQM8oTRMmFT7vDSnGwbGwaMr0sGNPLzQuTFwMPSTba7KJvS6ZPQ8ArcUOfqAyGfgoy0sejpLWm9yO%2F%2FAaaE1sTO1Opdo9CpR1U2s9e9c8d%2BMrC9LVdm3jnk6TVI6gPQ1naGeV191FmJhFm130txCxeTImhNNlfs1NEseHBFB2MAxFuPHyC5OEouZDc2utJ%2FygczV3NKYtNUEzlMyV%2Bd0FGtNnA0HpPoUDGIhoPNDWONUMeGh1c1pNriXFRfz6j8SSDaM1jTxUFAyUEXaGaay9GDzoZNBq4Zvut2oNWUsbI6gkosfcuigs0eOtU3VGh9m1QIOck6FLU0vAGQLEim2nSEW0BkE%2FZYgeKHq%2BDIlN3kP5IiyAygJSf2LurcdiQDR7cvIz%2Bt0kyI4aVbXdJ1HcOZNxQpGAUjL5Rq3a7kjUHh4rX0sh0thTV8%2FwJG48lEaLuHqw52N8JoZVZ5AAi5bjf5cmWP0M40b3a6vMOXcfDnCS%2BGlUx9q4nyM3%2FZ313%2BuT%2FXHWeedg8yC516%2F2JM9vACAttyMHbKaVFDQnhsfZl9B9cQ%2B%2B15Q2rmyNzrCNbpJBrQ9q0xyD%2F4Bi5YXbCvwP26kB1iwxKFm2rXusJczRML%2F3%2BbwGOqUBOaD0sMRnTJ95LMJpMmZzHf2oqqSv0eMaf2eCSDo9ffBtBvqeSooOnyYfyw283NkkE4eT81PZ%2FJ7ZrrhdDHg%2B7SaMobIzT17lgnJmGOcaBPgqvur9dpfaA6dfC0cYKwpz8hrNNSS3LKX3qdEMaxJnSfr%2BgqpTM19NYyjY8POjWqUGb1XzNXugAmCmTXiovzDYy07Hfcurytnk9eCac8KZ%2Fyel14SX&X-Amz-Signature=59afa4f891fa91105fa95ead612eb26b180a4603a990bf3f8ad2b87f1b845779&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IPFVM7H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcqdXKxN4rF4areArU%2F5BYX1%2BuuabG0GDb3v%2F%2FeoQ3ygIgDUS90%2FFCI0UJbu%2FoP0tGfC2p%2BR2G0FB2CbNr3OAZAewqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdQ2sjrpHyEK5MzRCrcA1MjUnGIRNmj5d8DGM2DQM8oTRMmFT7vDSnGwbGwaMr0sGNPLzQuTFwMPSTba7KJvS6ZPQ8ArcUOfqAyGfgoy0sejpLWm9yO%2F%2FAaaE1sTO1Opdo9CpR1U2s9e9c8d%2BMrC9LVdm3jnk6TVI6gPQ1naGeV191FmJhFm130txCxeTImhNNlfs1NEseHBFB2MAxFuPHyC5OEouZDc2utJ%2FygczV3NKYtNUEzlMyV%2Bd0FGtNnA0HpPoUDGIhoPNDWONUMeGh1c1pNriXFRfz6j8SSDaM1jTxUFAyUEXaGaay9GDzoZNBq4Zvut2oNWUsbI6gkosfcuigs0eOtU3VGh9m1QIOck6FLU0vAGQLEim2nSEW0BkE%2FZYgeKHq%2BDIlN3kP5IiyAygJSf2LurcdiQDR7cvIz%2Bt0kyI4aVbXdJ1HcOZNxQpGAUjL5Rq3a7kjUHh4rX0sh0thTV8%2FwJG48lEaLuHqw52N8JoZVZ5AAi5bjf5cmWP0M40b3a6vMOXcfDnCS%2BGlUx9q4nyM3%2FZ313%2BuT%2FXHWeedg8yC516%2F2JM9vACAttyMHbKaVFDQnhsfZl9B9cQ%2B%2B15Q2rmyNzrCNbpJBrQ9q0xyD%2F4Bi5YXbCvwP26kB1iwxKFm2rXusJczRML%2F3%2BbwGOqUBOaD0sMRnTJ95LMJpMmZzHf2oqqSv0eMaf2eCSDo9ffBtBvqeSooOnyYfyw283NkkE4eT81PZ%2FJ7ZrrhdDHg%2B7SaMobIzT17lgnJmGOcaBPgqvur9dpfaA6dfC0cYKwpz8hrNNSS3LKX3qdEMaxJnSfr%2BgqpTM19NYyjY8POjWqUGb1XzNXugAmCmTXiovzDYy07Hfcurytnk9eCac8KZ%2Fyel14SX&X-Amz-Signature=75c39c4c2901bdc91daf67d48d069992cbcbc95f563570e50a4be3b590db1fc8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MEKGO3Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg0p3XH%2FehRRODBocliYH5kQtohjlnjv7O3g6ZJwl5kQIgTZQFbK%2FXxHrp2XkDeeqRqALi35ON9qFtqJA%2FrTpr2DwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAg0BHT%2FfcjrkweCCrcA51gwRbUXFEYkEYuJ8u4GBIXFrlAmj3w1cszf0yE%2FSk0gwc1kEKB7SbXOWihESaeGBYpHPQ0NaJ8rFITozhahnAyzkwF3OE0sV%2Fc3odRxHPKR%2F%2B41wceyeQ5sgRAjYOr0tdvnNtK%2BwZfDPloPuL5rqcccNoXKnmXFWSWISRXNzvCbygnNM1%2F%2BA87IX7joWiB%2BZeWSZzlpIjbQjlaLjJI6TSCyVnAJFUAcBV%2Fi1Z9tRqUQcPDDGpS%2B%2F8NOlOhrzCFjFeQMJDljhA8AMIl4YGaLts0WRWEe34OBuCpNHeVNBgKeWJAQNJdPnSZ9upbppCosQGzG7lPm0ta5N7FTS2V5T%2FPECZqoBaClwPoE%2BZjZO124Wp%2F6biQxkjexYfIfziDKENG3UHFGYD08xJ2X9TPlr7H%2B3Cjze8iW4GpXpT%2FHNm0siE8%2FtLl19Q9Kl%2BKCanNkUUmEo3qNOCN4A%2BcLxgnHV1NzFX4VgLSOZjiw62NGzvJjjnaFx1j8zGTCJL7yOBNH9LCa2MuKpmdnqG1uZfbRFubaxjQYhI1nKmkG4vUoeJw5wEpUKcdZqswbtENW9qojwdI1KMwHcDF5utSqV4n1fXIFkayJlUnuOjic%2F4HOFfJ3m8oMca1tefB4OKmMLz2%2BbwGOqUBsQjNmS6pdnGf94%2BBMx0F0KtQgM%2BiuWSav4rc86ELd922hDTYvc%2BLl2SNQp59k3ixlNVj%2BWJuAO%2BKzRar9TyaXXsDwsosYCuz43zLOnEqAU%2F05nS%2F0q%2B3eWIvHVibYYIo8MBgkEo8I1%2BM25dCOByoNEMI%2BdzNnz3vgj3vo%2FNqWSNA0lmXFOvoPuoV%2B2YifTsCK6c80fL%2BCQ%2Ft4b3SpTOloU4DDRu4&X-Amz-Signature=9318f8e5d61acc25069ed37c6483b33aa0e2472ff0b78865ca5ec97c52fc2b08&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MEKGO3Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg0p3XH%2FehRRODBocliYH5kQtohjlnjv7O3g6ZJwl5kQIgTZQFbK%2FXxHrp2XkDeeqRqALi35ON9qFtqJA%2FrTpr2DwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAg0BHT%2FfcjrkweCCrcA51gwRbUXFEYkEYuJ8u4GBIXFrlAmj3w1cszf0yE%2FSk0gwc1kEKB7SbXOWihESaeGBYpHPQ0NaJ8rFITozhahnAyzkwF3OE0sV%2Fc3odRxHPKR%2F%2B41wceyeQ5sgRAjYOr0tdvnNtK%2BwZfDPloPuL5rqcccNoXKnmXFWSWISRXNzvCbygnNM1%2F%2BA87IX7joWiB%2BZeWSZzlpIjbQjlaLjJI6TSCyVnAJFUAcBV%2Fi1Z9tRqUQcPDDGpS%2B%2F8NOlOhrzCFjFeQMJDljhA8AMIl4YGaLts0WRWEe34OBuCpNHeVNBgKeWJAQNJdPnSZ9upbppCosQGzG7lPm0ta5N7FTS2V5T%2FPECZqoBaClwPoE%2BZjZO124Wp%2F6biQxkjexYfIfziDKENG3UHFGYD08xJ2X9TPlr7H%2B3Cjze8iW4GpXpT%2FHNm0siE8%2FtLl19Q9Kl%2BKCanNkUUmEo3qNOCN4A%2BcLxgnHV1NzFX4VgLSOZjiw62NGzvJjjnaFx1j8zGTCJL7yOBNH9LCa2MuKpmdnqG1uZfbRFubaxjQYhI1nKmkG4vUoeJw5wEpUKcdZqswbtENW9qojwdI1KMwHcDF5utSqV4n1fXIFkayJlUnuOjic%2F4HOFfJ3m8oMca1tefB4OKmMLz2%2BbwGOqUBsQjNmS6pdnGf94%2BBMx0F0KtQgM%2BiuWSav4rc86ELd922hDTYvc%2BLl2SNQp59k3ixlNVj%2BWJuAO%2BKzRar9TyaXXsDwsosYCuz43zLOnEqAU%2F05nS%2F0q%2B3eWIvHVibYYIo8MBgkEo8I1%2BM25dCOByoNEMI%2BdzNnz3vgj3vo%2FNqWSNA0lmXFOvoPuoV%2B2YifTsCK6c80fL%2BCQ%2Ft4b3SpTOloU4DDRu4&X-Amz-Signature=c8fabe82fd44f001d4f21dfd5b00fa6e69eac2c2020aae55fb6a6e0bc823a6f9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MEKGO3Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg0p3XH%2FehRRODBocliYH5kQtohjlnjv7O3g6ZJwl5kQIgTZQFbK%2FXxHrp2XkDeeqRqALi35ON9qFtqJA%2FrTpr2DwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAg0BHT%2FfcjrkweCCrcA51gwRbUXFEYkEYuJ8u4GBIXFrlAmj3w1cszf0yE%2FSk0gwc1kEKB7SbXOWihESaeGBYpHPQ0NaJ8rFITozhahnAyzkwF3OE0sV%2Fc3odRxHPKR%2F%2B41wceyeQ5sgRAjYOr0tdvnNtK%2BwZfDPloPuL5rqcccNoXKnmXFWSWISRXNzvCbygnNM1%2F%2BA87IX7joWiB%2BZeWSZzlpIjbQjlaLjJI6TSCyVnAJFUAcBV%2Fi1Z9tRqUQcPDDGpS%2B%2F8NOlOhrzCFjFeQMJDljhA8AMIl4YGaLts0WRWEe34OBuCpNHeVNBgKeWJAQNJdPnSZ9upbppCosQGzG7lPm0ta5N7FTS2V5T%2FPECZqoBaClwPoE%2BZjZO124Wp%2F6biQxkjexYfIfziDKENG3UHFGYD08xJ2X9TPlr7H%2B3Cjze8iW4GpXpT%2FHNm0siE8%2FtLl19Q9Kl%2BKCanNkUUmEo3qNOCN4A%2BcLxgnHV1NzFX4VgLSOZjiw62NGzvJjjnaFx1j8zGTCJL7yOBNH9LCa2MuKpmdnqG1uZfbRFubaxjQYhI1nKmkG4vUoeJw5wEpUKcdZqswbtENW9qojwdI1KMwHcDF5utSqV4n1fXIFkayJlUnuOjic%2F4HOFfJ3m8oMca1tefB4OKmMLz2%2BbwGOqUBsQjNmS6pdnGf94%2BBMx0F0KtQgM%2BiuWSav4rc86ELd922hDTYvc%2BLl2SNQp59k3ixlNVj%2BWJuAO%2BKzRar9TyaXXsDwsosYCuz43zLOnEqAU%2F05nS%2F0q%2B3eWIvHVibYYIo8MBgkEo8I1%2BM25dCOByoNEMI%2BdzNnz3vgj3vo%2FNqWSNA0lmXFOvoPuoV%2B2YifTsCK6c80fL%2BCQ%2Ft4b3SpTOloU4DDRu4&X-Amz-Signature=c865105574f68260a97137f2c5beac9ac34027191929816a4b99b780e1bdaa20&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MEKGO3Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg0p3XH%2FehRRODBocliYH5kQtohjlnjv7O3g6ZJwl5kQIgTZQFbK%2FXxHrp2XkDeeqRqALi35ON9qFtqJA%2FrTpr2DwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAg0BHT%2FfcjrkweCCrcA51gwRbUXFEYkEYuJ8u4GBIXFrlAmj3w1cszf0yE%2FSk0gwc1kEKB7SbXOWihESaeGBYpHPQ0NaJ8rFITozhahnAyzkwF3OE0sV%2Fc3odRxHPKR%2F%2B41wceyeQ5sgRAjYOr0tdvnNtK%2BwZfDPloPuL5rqcccNoXKnmXFWSWISRXNzvCbygnNM1%2F%2BA87IX7joWiB%2BZeWSZzlpIjbQjlaLjJI6TSCyVnAJFUAcBV%2Fi1Z9tRqUQcPDDGpS%2B%2F8NOlOhrzCFjFeQMJDljhA8AMIl4YGaLts0WRWEe34OBuCpNHeVNBgKeWJAQNJdPnSZ9upbppCosQGzG7lPm0ta5N7FTS2V5T%2FPECZqoBaClwPoE%2BZjZO124Wp%2F6biQxkjexYfIfziDKENG3UHFGYD08xJ2X9TPlr7H%2B3Cjze8iW4GpXpT%2FHNm0siE8%2FtLl19Q9Kl%2BKCanNkUUmEo3qNOCN4A%2BcLxgnHV1NzFX4VgLSOZjiw62NGzvJjjnaFx1j8zGTCJL7yOBNH9LCa2MuKpmdnqG1uZfbRFubaxjQYhI1nKmkG4vUoeJw5wEpUKcdZqswbtENW9qojwdI1KMwHcDF5utSqV4n1fXIFkayJlUnuOjic%2F4HOFfJ3m8oMca1tefB4OKmMLz2%2BbwGOqUBsQjNmS6pdnGf94%2BBMx0F0KtQgM%2BiuWSav4rc86ELd922hDTYvc%2BLl2SNQp59k3ixlNVj%2BWJuAO%2BKzRar9TyaXXsDwsosYCuz43zLOnEqAU%2F05nS%2F0q%2B3eWIvHVibYYIo8MBgkEo8I1%2BM25dCOByoNEMI%2BdzNnz3vgj3vo%2FNqWSNA0lmXFOvoPuoV%2B2YifTsCK6c80fL%2BCQ%2Ft4b3SpTOloU4DDRu4&X-Amz-Signature=361dacf6d6b0e5328e662e277f0186f4ac183874de177a09f99c1d4fb9b863db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MEKGO3Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg0p3XH%2FehRRODBocliYH5kQtohjlnjv7O3g6ZJwl5kQIgTZQFbK%2FXxHrp2XkDeeqRqALi35ON9qFtqJA%2FrTpr2DwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAg0BHT%2FfcjrkweCCrcA51gwRbUXFEYkEYuJ8u4GBIXFrlAmj3w1cszf0yE%2FSk0gwc1kEKB7SbXOWihESaeGBYpHPQ0NaJ8rFITozhahnAyzkwF3OE0sV%2Fc3odRxHPKR%2F%2B41wceyeQ5sgRAjYOr0tdvnNtK%2BwZfDPloPuL5rqcccNoXKnmXFWSWISRXNzvCbygnNM1%2F%2BA87IX7joWiB%2BZeWSZzlpIjbQjlaLjJI6TSCyVnAJFUAcBV%2Fi1Z9tRqUQcPDDGpS%2B%2F8NOlOhrzCFjFeQMJDljhA8AMIl4YGaLts0WRWEe34OBuCpNHeVNBgKeWJAQNJdPnSZ9upbppCosQGzG7lPm0ta5N7FTS2V5T%2FPECZqoBaClwPoE%2BZjZO124Wp%2F6biQxkjexYfIfziDKENG3UHFGYD08xJ2X9TPlr7H%2B3Cjze8iW4GpXpT%2FHNm0siE8%2FtLl19Q9Kl%2BKCanNkUUmEo3qNOCN4A%2BcLxgnHV1NzFX4VgLSOZjiw62NGzvJjjnaFx1j8zGTCJL7yOBNH9LCa2MuKpmdnqG1uZfbRFubaxjQYhI1nKmkG4vUoeJw5wEpUKcdZqswbtENW9qojwdI1KMwHcDF5utSqV4n1fXIFkayJlUnuOjic%2F4HOFfJ3m8oMca1tefB4OKmMLz2%2BbwGOqUBsQjNmS6pdnGf94%2BBMx0F0KtQgM%2BiuWSav4rc86ELd922hDTYvc%2BLl2SNQp59k3ixlNVj%2BWJuAO%2BKzRar9TyaXXsDwsosYCuz43zLOnEqAU%2F05nS%2F0q%2B3eWIvHVibYYIo8MBgkEo8I1%2BM25dCOByoNEMI%2BdzNnz3vgj3vo%2FNqWSNA0lmXFOvoPuoV%2B2YifTsCK6c80fL%2BCQ%2Ft4b3SpTOloU4DDRu4&X-Amz-Signature=e1978138a06f491af293e5622f56bfd195a20568ebc6c7d4bde5bfd98af97bc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


