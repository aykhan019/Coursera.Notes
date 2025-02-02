

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IHSHMP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5ovX31GkWHVAZ6t9VTbJxwr1WpQWXMc9QrncRcJBnXgIhAPVYZUzQmOiPFkFun1ARiuKKUf5if4pO0IK0t5iXn7rXKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLVI9%2FuVltJ2CeSIkq3AP0A8eIaRk%2FdMvtQrxX3Hy73m3hyk2pqcY0jS2uB2S3pXjYplAmcZjLYF%2BqsOWlxTJW5x%2BjePF2O4%2BZXqavEYAW0%2FglpKlMHRpEjjA60lCb0Th6cDZKbTpmFfJ1MM5Y%2FGJ1OEWKEfiYWTYoWELC2BNLDJyRrJaohTEVqnHMADn2qA5FrIXGq0QFplHFF1b9Gw4BFoGS%2BeaIcUdbKUnUB7iFoahT70jvorwjnld5QIeZWCJvGolLC0zB1fdgu%2FFarlliFq0%2F5G7F9FFRQCXog78dad45FOVAU%2BPdZK%2FWX8TmidK%2F70O%2BMfyJDgWs13LcU5juOlqbrXBKsdFg%2BcGnzJ6rPRo74Eht%2FSr9hjVH4w8ZU8QE3KF1y8VggyMaRyQ1Uchqg857vbixjViRO0Md1bF5R%2BCZws3J49XN8hikWecswExpm%2BLckRyH8XiqPDoNej%2F7elBZw6lkeTPOsS6vO%2FIvheYDZ7TjYsUy9Ios6PFZxXJUEI6HD%2F0NcJ4ggzqbbJWnKUcSVx8CGAAQtQgl3t9J4R%2BzEkuiMgc7Tbb7l01DMZ1v1rMVzVvnugae%2BhomkIgZTVtr3iRuapQbMfWsKOc7PH1a5aHDu3ZoMElkHk64sD0QCxelg74uxp%2B8hDDfuv28BjqkARi7EPE30BvzU8e7vtpoIb4FZJwpM3hyKePf9%2Bzba1JrWrDOYPeHKkelH35VAI7OhLHGsk35q5wDUwJF8Fa90Z9BR3IzmJhdcu%2B0agU0xljlahx9602AdLRyH5lbfJBAHPbXxkzDTf4s8zHirUmJLyVHmtHy3ptKh8pcBBAKPkm2W7Fk%2BUio8ZmoFvPkaa%2BaTdypF002kiTGxGyyeLPwxyDKpn59&X-Amz-Signature=d0b395a46d8cacc22cf7e48fb5597fa1ae09baee3b5167222bc1331b0a42d9f3&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMB2YW6G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDaRBigIZax2Fya1s0aXO9ZXWpmoW0CrxLoPEA9O6UEAiAQxXSGXDRH2ogEjaF7sfgju4LNlW12Hn2JyWzjxzlCcyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVH0Ncsv8KPgZPd5mKtwDSarT7I7poNFJqLciDLIFMEiDvV7nTZutxzYa2YW4xPtd%2FtUGJVrxr11MH0oIXIoxGOA1%2B7ySB6m0%2FzaMouUdNAyKgEUA0BoiM9IFTstlF1g2bLFa1X6UoNpLGlU464I5vJDytWDEy2lLvRP7yXWgtfYFtdEA4vwJegwo3soJzUDO55kzE05WlF2MfdLsWNWZFFdFVvfxRqlsemApx2vWcIZDAzjenekZXXpI0B2M6uLlOxvtq9ewq%2BelIQ0BVFBCZIdwnggswLDE34z1JeShbFc8kuEJF%2F1i0HaNkI70ZV6QPT96Yn59dXJRQaGNDH4mVwhwx4egpM8ktGetH6e%2Fvekn7gGEqsKGuUeBTVqdrCoM35JPYzzNQBF2KINEgnAUoXGcn5ZgFz09p6yXJ5iF7ffWKSIBaKo7w8XvpEnHZ90pLXAz6zP87sZ8otdnSHO7Z56SIO9SBZ2ZX7c55r3DcutCu%2FsIHE3KeUevlzRPLxAVMJlD7hgxxw60o%2FwzR%2B2iDJ2KyPuM%2BOgNGrsYIBZ1pbHOeICJxpWSMeaZcq6EY7vZ3ce4y957Fw7837ZQ6O85rjB2lfxQhG6nPsivWtsbYhYKOHJk%2F6nn7X20EruOfHVo1Ak0MZvLOIXW2iUwsL39vAY6pgF38fwXNqAZgasEmXyr2fvl4BjbEoEN5yOVa0PaDbevaqB%2BBfIlKW6Xbbs2RkjC4TmhgokVBta%2BCFLZ49ak4XH1xl0bnvHAnw6EADrfUWB04VUAIY2QZbysYZ6j9%2B17PhqnA71KHlrDbKC2QpzDuyRvW7xCXPvQwAbdeA2fStAbQDVcX%2Bx0tMenxM9tN64z07NWVgK5KJbfWIDHYqyTM%2B1RYYO6CtFj&X-Amz-Signature=1f232d7843df024fec781cb29094ec11321bf77035a21d073c6703f27e9d1339&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMB2YW6G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDaRBigIZax2Fya1s0aXO9ZXWpmoW0CrxLoPEA9O6UEAiAQxXSGXDRH2ogEjaF7sfgju4LNlW12Hn2JyWzjxzlCcyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVH0Ncsv8KPgZPd5mKtwDSarT7I7poNFJqLciDLIFMEiDvV7nTZutxzYa2YW4xPtd%2FtUGJVrxr11MH0oIXIoxGOA1%2B7ySB6m0%2FzaMouUdNAyKgEUA0BoiM9IFTstlF1g2bLFa1X6UoNpLGlU464I5vJDytWDEy2lLvRP7yXWgtfYFtdEA4vwJegwo3soJzUDO55kzE05WlF2MfdLsWNWZFFdFVvfxRqlsemApx2vWcIZDAzjenekZXXpI0B2M6uLlOxvtq9ewq%2BelIQ0BVFBCZIdwnggswLDE34z1JeShbFc8kuEJF%2F1i0HaNkI70ZV6QPT96Yn59dXJRQaGNDH4mVwhwx4egpM8ktGetH6e%2Fvekn7gGEqsKGuUeBTVqdrCoM35JPYzzNQBF2KINEgnAUoXGcn5ZgFz09p6yXJ5iF7ffWKSIBaKo7w8XvpEnHZ90pLXAz6zP87sZ8otdnSHO7Z56SIO9SBZ2ZX7c55r3DcutCu%2FsIHE3KeUevlzRPLxAVMJlD7hgxxw60o%2FwzR%2B2iDJ2KyPuM%2BOgNGrsYIBZ1pbHOeICJxpWSMeaZcq6EY7vZ3ce4y957Fw7837ZQ6O85rjB2lfxQhG6nPsivWtsbYhYKOHJk%2F6nn7X20EruOfHVo1Ak0MZvLOIXW2iUwsL39vAY6pgF38fwXNqAZgasEmXyr2fvl4BjbEoEN5yOVa0PaDbevaqB%2BBfIlKW6Xbbs2RkjC4TmhgokVBta%2BCFLZ49ak4XH1xl0bnvHAnw6EADrfUWB04VUAIY2QZbysYZ6j9%2B17PhqnA71KHlrDbKC2QpzDuyRvW7xCXPvQwAbdeA2fStAbQDVcX%2Bx0tMenxM9tN64z07NWVgK5KJbfWIDHYqyTM%2B1RYYO6CtFj&X-Amz-Signature=747126d96a74ca6af3f3a6e84fae9bbbc190d4733f2e9a1cecf839a835ab2a57&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMB2YW6G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDaRBigIZax2Fya1s0aXO9ZXWpmoW0CrxLoPEA9O6UEAiAQxXSGXDRH2ogEjaF7sfgju4LNlW12Hn2JyWzjxzlCcyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVH0Ncsv8KPgZPd5mKtwDSarT7I7poNFJqLciDLIFMEiDvV7nTZutxzYa2YW4xPtd%2FtUGJVrxr11MH0oIXIoxGOA1%2B7ySB6m0%2FzaMouUdNAyKgEUA0BoiM9IFTstlF1g2bLFa1X6UoNpLGlU464I5vJDytWDEy2lLvRP7yXWgtfYFtdEA4vwJegwo3soJzUDO55kzE05WlF2MfdLsWNWZFFdFVvfxRqlsemApx2vWcIZDAzjenekZXXpI0B2M6uLlOxvtq9ewq%2BelIQ0BVFBCZIdwnggswLDE34z1JeShbFc8kuEJF%2F1i0HaNkI70ZV6QPT96Yn59dXJRQaGNDH4mVwhwx4egpM8ktGetH6e%2Fvekn7gGEqsKGuUeBTVqdrCoM35JPYzzNQBF2KINEgnAUoXGcn5ZgFz09p6yXJ5iF7ffWKSIBaKo7w8XvpEnHZ90pLXAz6zP87sZ8otdnSHO7Z56SIO9SBZ2ZX7c55r3DcutCu%2FsIHE3KeUevlzRPLxAVMJlD7hgxxw60o%2FwzR%2B2iDJ2KyPuM%2BOgNGrsYIBZ1pbHOeICJxpWSMeaZcq6EY7vZ3ce4y957Fw7837ZQ6O85rjB2lfxQhG6nPsivWtsbYhYKOHJk%2F6nn7X20EruOfHVo1Ak0MZvLOIXW2iUwsL39vAY6pgF38fwXNqAZgasEmXyr2fvl4BjbEoEN5yOVa0PaDbevaqB%2BBfIlKW6Xbbs2RkjC4TmhgokVBta%2BCFLZ49ak4XH1xl0bnvHAnw6EADrfUWB04VUAIY2QZbysYZ6j9%2B17PhqnA71KHlrDbKC2QpzDuyRvW7xCXPvQwAbdeA2fStAbQDVcX%2Bx0tMenxM9tN64z07NWVgK5KJbfWIDHYqyTM%2B1RYYO6CtFj&X-Amz-Signature=81ee43c7ddbdb31bfac1f802e2e4007477d48889da0e244baf87c81f2f473fc4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMB2YW6G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDaRBigIZax2Fya1s0aXO9ZXWpmoW0CrxLoPEA9O6UEAiAQxXSGXDRH2ogEjaF7sfgju4LNlW12Hn2JyWzjxzlCcyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVH0Ncsv8KPgZPd5mKtwDSarT7I7poNFJqLciDLIFMEiDvV7nTZutxzYa2YW4xPtd%2FtUGJVrxr11MH0oIXIoxGOA1%2B7ySB6m0%2FzaMouUdNAyKgEUA0BoiM9IFTstlF1g2bLFa1X6UoNpLGlU464I5vJDytWDEy2lLvRP7yXWgtfYFtdEA4vwJegwo3soJzUDO55kzE05WlF2MfdLsWNWZFFdFVvfxRqlsemApx2vWcIZDAzjenekZXXpI0B2M6uLlOxvtq9ewq%2BelIQ0BVFBCZIdwnggswLDE34z1JeShbFc8kuEJF%2F1i0HaNkI70ZV6QPT96Yn59dXJRQaGNDH4mVwhwx4egpM8ktGetH6e%2Fvekn7gGEqsKGuUeBTVqdrCoM35JPYzzNQBF2KINEgnAUoXGcn5ZgFz09p6yXJ5iF7ffWKSIBaKo7w8XvpEnHZ90pLXAz6zP87sZ8otdnSHO7Z56SIO9SBZ2ZX7c55r3DcutCu%2FsIHE3KeUevlzRPLxAVMJlD7hgxxw60o%2FwzR%2B2iDJ2KyPuM%2BOgNGrsYIBZ1pbHOeICJxpWSMeaZcq6EY7vZ3ce4y957Fw7837ZQ6O85rjB2lfxQhG6nPsivWtsbYhYKOHJk%2F6nn7X20EruOfHVo1Ak0MZvLOIXW2iUwsL39vAY6pgF38fwXNqAZgasEmXyr2fvl4BjbEoEN5yOVa0PaDbevaqB%2BBfIlKW6Xbbs2RkjC4TmhgokVBta%2BCFLZ49ak4XH1xl0bnvHAnw6EADrfUWB04VUAIY2QZbysYZ6j9%2B17PhqnA71KHlrDbKC2QpzDuyRvW7xCXPvQwAbdeA2fStAbQDVcX%2Bx0tMenxM9tN64z07NWVgK5KJbfWIDHYqyTM%2B1RYYO6CtFj&X-Amz-Signature=e4c0633c1be588056d75de9dce49cc001c646ed6c41bd730603640a13450f330&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMB2YW6G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDaRBigIZax2Fya1s0aXO9ZXWpmoW0CrxLoPEA9O6UEAiAQxXSGXDRH2ogEjaF7sfgju4LNlW12Hn2JyWzjxzlCcyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVH0Ncsv8KPgZPd5mKtwDSarT7I7poNFJqLciDLIFMEiDvV7nTZutxzYa2YW4xPtd%2FtUGJVrxr11MH0oIXIoxGOA1%2B7ySB6m0%2FzaMouUdNAyKgEUA0BoiM9IFTstlF1g2bLFa1X6UoNpLGlU464I5vJDytWDEy2lLvRP7yXWgtfYFtdEA4vwJegwo3soJzUDO55kzE05WlF2MfdLsWNWZFFdFVvfxRqlsemApx2vWcIZDAzjenekZXXpI0B2M6uLlOxvtq9ewq%2BelIQ0BVFBCZIdwnggswLDE34z1JeShbFc8kuEJF%2F1i0HaNkI70ZV6QPT96Yn59dXJRQaGNDH4mVwhwx4egpM8ktGetH6e%2Fvekn7gGEqsKGuUeBTVqdrCoM35JPYzzNQBF2KINEgnAUoXGcn5ZgFz09p6yXJ5iF7ffWKSIBaKo7w8XvpEnHZ90pLXAz6zP87sZ8otdnSHO7Z56SIO9SBZ2ZX7c55r3DcutCu%2FsIHE3KeUevlzRPLxAVMJlD7hgxxw60o%2FwzR%2B2iDJ2KyPuM%2BOgNGrsYIBZ1pbHOeICJxpWSMeaZcq6EY7vZ3ce4y957Fw7837ZQ6O85rjB2lfxQhG6nPsivWtsbYhYKOHJk%2F6nn7X20EruOfHVo1Ak0MZvLOIXW2iUwsL39vAY6pgF38fwXNqAZgasEmXyr2fvl4BjbEoEN5yOVa0PaDbevaqB%2BBfIlKW6Xbbs2RkjC4TmhgokVBta%2BCFLZ49ak4XH1xl0bnvHAnw6EADrfUWB04VUAIY2QZbysYZ6j9%2B17PhqnA71KHlrDbKC2QpzDuyRvW7xCXPvQwAbdeA2fStAbQDVcX%2Bx0tMenxM9tN64z07NWVgK5KJbfWIDHYqyTM%2B1RYYO6CtFj&X-Amz-Signature=093f0026237cfcaf129a34c425de134494105628518f64d160a03c4420a2a0f5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IHSHMP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5ovX31GkWHVAZ6t9VTbJxwr1WpQWXMc9QrncRcJBnXgIhAPVYZUzQmOiPFkFun1ARiuKKUf5if4pO0IK0t5iXn7rXKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLVI9%2FuVltJ2CeSIkq3AP0A8eIaRk%2FdMvtQrxX3Hy73m3hyk2pqcY0jS2uB2S3pXjYplAmcZjLYF%2BqsOWlxTJW5x%2BjePF2O4%2BZXqavEYAW0%2FglpKlMHRpEjjA60lCb0Th6cDZKbTpmFfJ1MM5Y%2FGJ1OEWKEfiYWTYoWELC2BNLDJyRrJaohTEVqnHMADn2qA5FrIXGq0QFplHFF1b9Gw4BFoGS%2BeaIcUdbKUnUB7iFoahT70jvorwjnld5QIeZWCJvGolLC0zB1fdgu%2FFarlliFq0%2F5G7F9FFRQCXog78dad45FOVAU%2BPdZK%2FWX8TmidK%2F70O%2BMfyJDgWs13LcU5juOlqbrXBKsdFg%2BcGnzJ6rPRo74Eht%2FSr9hjVH4w8ZU8QE3KF1y8VggyMaRyQ1Uchqg857vbixjViRO0Md1bF5R%2BCZws3J49XN8hikWecswExpm%2BLckRyH8XiqPDoNej%2F7elBZw6lkeTPOsS6vO%2FIvheYDZ7TjYsUy9Ios6PFZxXJUEI6HD%2F0NcJ4ggzqbbJWnKUcSVx8CGAAQtQgl3t9J4R%2BzEkuiMgc7Tbb7l01DMZ1v1rMVzVvnugae%2BhomkIgZTVtr3iRuapQbMfWsKOc7PH1a5aHDu3ZoMElkHk64sD0QCxelg74uxp%2B8hDDfuv28BjqkARi7EPE30BvzU8e7vtpoIb4FZJwpM3hyKePf9%2Bzba1JrWrDOYPeHKkelH35VAI7OhLHGsk35q5wDUwJF8Fa90Z9BR3IzmJhdcu%2B0agU0xljlahx9602AdLRyH5lbfJBAHPbXxkzDTf4s8zHirUmJLyVHmtHy3ptKh8pcBBAKPkm2W7Fk%2BUio8ZmoFvPkaa%2BaTdypF002kiTGxGyyeLPwxyDKpn59&X-Amz-Signature=ed81939af4205dbc1fc65a6d441e5ef0e3c0f02a76bc258ecf40a872bdf1af44&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IHSHMP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5ovX31GkWHVAZ6t9VTbJxwr1WpQWXMc9QrncRcJBnXgIhAPVYZUzQmOiPFkFun1ARiuKKUf5if4pO0IK0t5iXn7rXKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLVI9%2FuVltJ2CeSIkq3AP0A8eIaRk%2FdMvtQrxX3Hy73m3hyk2pqcY0jS2uB2S3pXjYplAmcZjLYF%2BqsOWlxTJW5x%2BjePF2O4%2BZXqavEYAW0%2FglpKlMHRpEjjA60lCb0Th6cDZKbTpmFfJ1MM5Y%2FGJ1OEWKEfiYWTYoWELC2BNLDJyRrJaohTEVqnHMADn2qA5FrIXGq0QFplHFF1b9Gw4BFoGS%2BeaIcUdbKUnUB7iFoahT70jvorwjnld5QIeZWCJvGolLC0zB1fdgu%2FFarlliFq0%2F5G7F9FFRQCXog78dad45FOVAU%2BPdZK%2FWX8TmidK%2F70O%2BMfyJDgWs13LcU5juOlqbrXBKsdFg%2BcGnzJ6rPRo74Eht%2FSr9hjVH4w8ZU8QE3KF1y8VggyMaRyQ1Uchqg857vbixjViRO0Md1bF5R%2BCZws3J49XN8hikWecswExpm%2BLckRyH8XiqPDoNej%2F7elBZw6lkeTPOsS6vO%2FIvheYDZ7TjYsUy9Ios6PFZxXJUEI6HD%2F0NcJ4ggzqbbJWnKUcSVx8CGAAQtQgl3t9J4R%2BzEkuiMgc7Tbb7l01DMZ1v1rMVzVvnugae%2BhomkIgZTVtr3iRuapQbMfWsKOc7PH1a5aHDu3ZoMElkHk64sD0QCxelg74uxp%2B8hDDfuv28BjqkARi7EPE30BvzU8e7vtpoIb4FZJwpM3hyKePf9%2Bzba1JrWrDOYPeHKkelH35VAI7OhLHGsk35q5wDUwJF8Fa90Z9BR3IzmJhdcu%2B0agU0xljlahx9602AdLRyH5lbfJBAHPbXxkzDTf4s8zHirUmJLyVHmtHy3ptKh8pcBBAKPkm2W7Fk%2BUio8ZmoFvPkaa%2BaTdypF002kiTGxGyyeLPwxyDKpn59&X-Amz-Signature=eaa4ea03b2074b2f4a64a0cef4488e961e8c7ece9996aa94bf271f8c29560961&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IHSHMP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5ovX31GkWHVAZ6t9VTbJxwr1WpQWXMc9QrncRcJBnXgIhAPVYZUzQmOiPFkFun1ARiuKKUf5if4pO0IK0t5iXn7rXKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLVI9%2FuVltJ2CeSIkq3AP0A8eIaRk%2FdMvtQrxX3Hy73m3hyk2pqcY0jS2uB2S3pXjYplAmcZjLYF%2BqsOWlxTJW5x%2BjePF2O4%2BZXqavEYAW0%2FglpKlMHRpEjjA60lCb0Th6cDZKbTpmFfJ1MM5Y%2FGJ1OEWKEfiYWTYoWELC2BNLDJyRrJaohTEVqnHMADn2qA5FrIXGq0QFplHFF1b9Gw4BFoGS%2BeaIcUdbKUnUB7iFoahT70jvorwjnld5QIeZWCJvGolLC0zB1fdgu%2FFarlliFq0%2F5G7F9FFRQCXog78dad45FOVAU%2BPdZK%2FWX8TmidK%2F70O%2BMfyJDgWs13LcU5juOlqbrXBKsdFg%2BcGnzJ6rPRo74Eht%2FSr9hjVH4w8ZU8QE3KF1y8VggyMaRyQ1Uchqg857vbixjViRO0Md1bF5R%2BCZws3J49XN8hikWecswExpm%2BLckRyH8XiqPDoNej%2F7elBZw6lkeTPOsS6vO%2FIvheYDZ7TjYsUy9Ios6PFZxXJUEI6HD%2F0NcJ4ggzqbbJWnKUcSVx8CGAAQtQgl3t9J4R%2BzEkuiMgc7Tbb7l01DMZ1v1rMVzVvnugae%2BhomkIgZTVtr3iRuapQbMfWsKOc7PH1a5aHDu3ZoMElkHk64sD0QCxelg74uxp%2B8hDDfuv28BjqkARi7EPE30BvzU8e7vtpoIb4FZJwpM3hyKePf9%2Bzba1JrWrDOYPeHKkelH35VAI7OhLHGsk35q5wDUwJF8Fa90Z9BR3IzmJhdcu%2B0agU0xljlahx9602AdLRyH5lbfJBAHPbXxkzDTf4s8zHirUmJLyVHmtHy3ptKh8pcBBAKPkm2W7Fk%2BUio8ZmoFvPkaa%2BaTdypF002kiTGxGyyeLPwxyDKpn59&X-Amz-Signature=77cbbe2d3f0ff1ed319f9e01b61a3661e81823fa519b603520889da3648523f5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IHSHMP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5ovX31GkWHVAZ6t9VTbJxwr1WpQWXMc9QrncRcJBnXgIhAPVYZUzQmOiPFkFun1ARiuKKUf5if4pO0IK0t5iXn7rXKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLVI9%2FuVltJ2CeSIkq3AP0A8eIaRk%2FdMvtQrxX3Hy73m3hyk2pqcY0jS2uB2S3pXjYplAmcZjLYF%2BqsOWlxTJW5x%2BjePF2O4%2BZXqavEYAW0%2FglpKlMHRpEjjA60lCb0Th6cDZKbTpmFfJ1MM5Y%2FGJ1OEWKEfiYWTYoWELC2BNLDJyRrJaohTEVqnHMADn2qA5FrIXGq0QFplHFF1b9Gw4BFoGS%2BeaIcUdbKUnUB7iFoahT70jvorwjnld5QIeZWCJvGolLC0zB1fdgu%2FFarlliFq0%2F5G7F9FFRQCXog78dad45FOVAU%2BPdZK%2FWX8TmidK%2F70O%2BMfyJDgWs13LcU5juOlqbrXBKsdFg%2BcGnzJ6rPRo74Eht%2FSr9hjVH4w8ZU8QE3KF1y8VggyMaRyQ1Uchqg857vbixjViRO0Md1bF5R%2BCZws3J49XN8hikWecswExpm%2BLckRyH8XiqPDoNej%2F7elBZw6lkeTPOsS6vO%2FIvheYDZ7TjYsUy9Ios6PFZxXJUEI6HD%2F0NcJ4ggzqbbJWnKUcSVx8CGAAQtQgl3t9J4R%2BzEkuiMgc7Tbb7l01DMZ1v1rMVzVvnugae%2BhomkIgZTVtr3iRuapQbMfWsKOc7PH1a5aHDu3ZoMElkHk64sD0QCxelg74uxp%2B8hDDfuv28BjqkARi7EPE30BvzU8e7vtpoIb4FZJwpM3hyKePf9%2Bzba1JrWrDOYPeHKkelH35VAI7OhLHGsk35q5wDUwJF8Fa90Z9BR3IzmJhdcu%2B0agU0xljlahx9602AdLRyH5lbfJBAHPbXxkzDTf4s8zHirUmJLyVHmtHy3ptKh8pcBBAKPkm2W7Fk%2BUio8ZmoFvPkaa%2BaTdypF002kiTGxGyyeLPwxyDKpn59&X-Amz-Signature=704b70fd8dd9c1f3bffc7e20da652974fa82392d9f7960761d2e9d5cb48d13a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IHSHMP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5ovX31GkWHVAZ6t9VTbJxwr1WpQWXMc9QrncRcJBnXgIhAPVYZUzQmOiPFkFun1ARiuKKUf5if4pO0IK0t5iXn7rXKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyLVI9%2FuVltJ2CeSIkq3AP0A8eIaRk%2FdMvtQrxX3Hy73m3hyk2pqcY0jS2uB2S3pXjYplAmcZjLYF%2BqsOWlxTJW5x%2BjePF2O4%2BZXqavEYAW0%2FglpKlMHRpEjjA60lCb0Th6cDZKbTpmFfJ1MM5Y%2FGJ1OEWKEfiYWTYoWELC2BNLDJyRrJaohTEVqnHMADn2qA5FrIXGq0QFplHFF1b9Gw4BFoGS%2BeaIcUdbKUnUB7iFoahT70jvorwjnld5QIeZWCJvGolLC0zB1fdgu%2FFarlliFq0%2F5G7F9FFRQCXog78dad45FOVAU%2BPdZK%2FWX8TmidK%2F70O%2BMfyJDgWs13LcU5juOlqbrXBKsdFg%2BcGnzJ6rPRo74Eht%2FSr9hjVH4w8ZU8QE3KF1y8VggyMaRyQ1Uchqg857vbixjViRO0Md1bF5R%2BCZws3J49XN8hikWecswExpm%2BLckRyH8XiqPDoNej%2F7elBZw6lkeTPOsS6vO%2FIvheYDZ7TjYsUy9Ios6PFZxXJUEI6HD%2F0NcJ4ggzqbbJWnKUcSVx8CGAAQtQgl3t9J4R%2BzEkuiMgc7Tbb7l01DMZ1v1rMVzVvnugae%2BhomkIgZTVtr3iRuapQbMfWsKOc7PH1a5aHDu3ZoMElkHk64sD0QCxelg74uxp%2B8hDDfuv28BjqkARi7EPE30BvzU8e7vtpoIb4FZJwpM3hyKePf9%2Bzba1JrWrDOYPeHKkelH35VAI7OhLHGsk35q5wDUwJF8Fa90Z9BR3IzmJhdcu%2B0agU0xljlahx9602AdLRyH5lbfJBAHPbXxkzDTf4s8zHirUmJLyVHmtHy3ptKh8pcBBAKPkm2W7Fk%2BUio8ZmoFvPkaa%2BaTdypF002kiTGxGyyeLPwxyDKpn59&X-Amz-Signature=cd81eef3b92223ddcbebe82e579ae4738e710d1d5db90d3193e59520596bdada&X-Amz-SignedHeaders=host&x-id=GetObject)
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


