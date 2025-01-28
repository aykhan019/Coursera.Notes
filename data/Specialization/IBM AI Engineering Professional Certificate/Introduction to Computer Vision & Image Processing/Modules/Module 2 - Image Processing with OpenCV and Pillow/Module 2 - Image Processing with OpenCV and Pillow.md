

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGUXQHHP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQC1aj2Gvms1hvkza5RvTMcAf0d%2FZch3Yyfy7XY1yOlxeAIhAJg275SFDYHTc6N6iBemWhJoovQ3JVMpDddwx%2BDXBzPUKv8DCH4QABoMNjM3NDIzMTgzODA1Igyuojzo1dme0Iq0ZUsq3AMG%2F27On0u9gFXVM3wM%2FAQVU4JB6fc4OM0VRjmhE%2Fewd80Fi0SSh8BhWAXipnBym6meDRoKi447rYlAJEXMEkYqb%2FwHHk8MP%2FcjebteDb5VQ1v%2FRXbMJN%2FJy1zqla8H1FpTGYVhmuw9vCSDggZejZwK%2BCAQ95uHGHIv%2BUUVM8x1SF6IJn4kZnsOSaxoupabMbBJp9tWrzfZ4HJnGpv1k5YcMdKKt4TeGUjXGowXma9YOco7QcCapZdtqf4ms0zqDSWOTQmlEwNqIt6t%2FY84ZO5CtmhYFoGnm%2B6hjqa4HLESfuTk2thE42H5PJvc1VWX%2B%2FGVzwBZotOIg1PiEn2sJ7f8J%2F9kD%2BU8W%2FpUZKirTnFkoV13kUJWrABZ%2BK6IcRuuZxEPDqGcPv7k98iMY8cbCbmpxJYO57W5RkQBG%2FuPPKLgbg8zC33daM7RuGL5uoRRXHpamm89qgPo33rfY6P2DjzPaWTC7HM3j3AwTxCS06iRYRftBhxwuA8tPYDHbG%2FYR%2Bt%2FlHTjkvf2vkA789GU3TZO3pullxRt2RW185Tv8wjZV3QjfEyiK6CfGz%2FG7egNWDmzJd10N8zlm0TeSEMmxobnbimMDH7NGQiJaA5ZoFwuUqtEemD4h18sN9qmajDb%2BeS8BjqkAW2cAf5ETMgLojBWWur0tmT8GTaBJfCxHBIUO4%2FjspZv31Kj4%2FPZVihP3120JjQUd7qjwkENxEXrdeiVzCWkG%2FN924yDzhF5dH2IGR3KbITmZV7UJZXzSGTmZjaKrxKHonP4i0hP7FiNG%2F%2FGW4PXuiCExrRYy7uuCkYgh9fef%2BKl2xGHw%2Fp1KJsoQj4vb8LwVGhlxJsgXhDjz8O8RvR7n1Em0AFf&X-Amz-Signature=1f6a5413509317a8d0043ac3241873ed94aae217ed2938db21dc1ad44cd61aee&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMD3K7J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCkW%2Bk7SRqjp7300PwyhA4IGcujqjk4D1lD%2FAXEx3Rw1QIhANtmDznWjMdqzSvFy5Dp9tMPosXLuVPzZirL9mpg3c3cKv8DCH0QABoMNjM3NDIzMTgzODA1IgzcyyF0HuTgrgthMjMq3APEhUTwhUjIy14Bebe8yfolf4e8iGQj9xUrEn83BOOYr37yy6dF3f1DvE2FEljwwbRZTcwdVu1SHgj5NsMjvcsuY607fTaqjEOpiU7B2pzyx8QROORe4b6Z6SnfqC0CKS7jF0wa60YCpWaEy4G%2FRGlFm9d9PA36UbFcp9d4sww4F4BBqEE%2FiSVnTlAOcsQ03R8ibt8gnO2W92mQZfCpzI%2FU2h6UU1dmxHdkyXs%2BRI9cinSt3H7nvNiXP4%2B%2FLgYrhEaLq%2Bd4eIcJYnaIyQstJsoyECBu34gO2HUT1ymMVvQvrfLE08K66OsiDJ4JeS6FWmqpwAuruN20zYuX8Cz4QDf18%2BWSBLk5xkjV%2BYQIH7%2FCtKc6vBddoCRlgiFj48BDuE7YK51mCiFxu3HNm4Uf8GEbPvXFK4uIWc8ujNxvr%2FrDU9kGBkcZYqI3AnE8v6v5exWZxuUzJONHl6Pga6K1Wflv8wt4lHXtUtuX4n6xW%2FW%2F%2F18TLEsRTrmBtUm%2B3f7OwvrZtvGA8OKLRGIXeHOvIQkSvRmi7E7yX%2FN9UWfcHCoVstwU%2BgwDhuuhbwYLvjOK26iqNC2oohMitPOnHvMZlAdKAGbOhQACBOuPLLE%2FaZIgF0xOhMX%2BGPofKO8MkzDl%2BeS8BjqkAX7l6W195%2BqUNF9t95yxfFzk3XT0Aun9YodgGVeozqPLVzCRGIab2eZAckKoGzYZB3eK0TGW2b1awPgfTOR%2B8yIukKFo%2Bx0l4PMWKqEZHGWuDx2SIUROtBF1q%2B6SuD7OcZyR39vFcaNS9DNWa1h8ZdlNn7L%2FjKMa1XsbaXleocrliYSQu2BUnNA92nAXBqeIMl5IX2gfvVwmyKhZhY8fwx6yXmmd&X-Amz-Signature=f82bedc3730e29e4c7a1406620766881a673ac3fb5f5d687b7f0da54759002c1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMD3K7J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCkW%2Bk7SRqjp7300PwyhA4IGcujqjk4D1lD%2FAXEx3Rw1QIhANtmDznWjMdqzSvFy5Dp9tMPosXLuVPzZirL9mpg3c3cKv8DCH0QABoMNjM3NDIzMTgzODA1IgzcyyF0HuTgrgthMjMq3APEhUTwhUjIy14Bebe8yfolf4e8iGQj9xUrEn83BOOYr37yy6dF3f1DvE2FEljwwbRZTcwdVu1SHgj5NsMjvcsuY607fTaqjEOpiU7B2pzyx8QROORe4b6Z6SnfqC0CKS7jF0wa60YCpWaEy4G%2FRGlFm9d9PA36UbFcp9d4sww4F4BBqEE%2FiSVnTlAOcsQ03R8ibt8gnO2W92mQZfCpzI%2FU2h6UU1dmxHdkyXs%2BRI9cinSt3H7nvNiXP4%2B%2FLgYrhEaLq%2Bd4eIcJYnaIyQstJsoyECBu34gO2HUT1ymMVvQvrfLE08K66OsiDJ4JeS6FWmqpwAuruN20zYuX8Cz4QDf18%2BWSBLk5xkjV%2BYQIH7%2FCtKc6vBddoCRlgiFj48BDuE7YK51mCiFxu3HNm4Uf8GEbPvXFK4uIWc8ujNxvr%2FrDU9kGBkcZYqI3AnE8v6v5exWZxuUzJONHl6Pga6K1Wflv8wt4lHXtUtuX4n6xW%2FW%2F%2F18TLEsRTrmBtUm%2B3f7OwvrZtvGA8OKLRGIXeHOvIQkSvRmi7E7yX%2FN9UWfcHCoVstwU%2BgwDhuuhbwYLvjOK26iqNC2oohMitPOnHvMZlAdKAGbOhQACBOuPLLE%2FaZIgF0xOhMX%2BGPofKO8MkzDl%2BeS8BjqkAX7l6W195%2BqUNF9t95yxfFzk3XT0Aun9YodgGVeozqPLVzCRGIab2eZAckKoGzYZB3eK0TGW2b1awPgfTOR%2B8yIukKFo%2Bx0l4PMWKqEZHGWuDx2SIUROtBF1q%2B6SuD7OcZyR39vFcaNS9DNWa1h8ZdlNn7L%2FjKMa1XsbaXleocrliYSQu2BUnNA92nAXBqeIMl5IX2gfvVwmyKhZhY8fwx6yXmmd&X-Amz-Signature=76fe1d4851862c5d3d558da45910ae5ad70fbdbed294e01482fa864de9829f94&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMD3K7J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCkW%2Bk7SRqjp7300PwyhA4IGcujqjk4D1lD%2FAXEx3Rw1QIhANtmDznWjMdqzSvFy5Dp9tMPosXLuVPzZirL9mpg3c3cKv8DCH0QABoMNjM3NDIzMTgzODA1IgzcyyF0HuTgrgthMjMq3APEhUTwhUjIy14Bebe8yfolf4e8iGQj9xUrEn83BOOYr37yy6dF3f1DvE2FEljwwbRZTcwdVu1SHgj5NsMjvcsuY607fTaqjEOpiU7B2pzyx8QROORe4b6Z6SnfqC0CKS7jF0wa60YCpWaEy4G%2FRGlFm9d9PA36UbFcp9d4sww4F4BBqEE%2FiSVnTlAOcsQ03R8ibt8gnO2W92mQZfCpzI%2FU2h6UU1dmxHdkyXs%2BRI9cinSt3H7nvNiXP4%2B%2FLgYrhEaLq%2Bd4eIcJYnaIyQstJsoyECBu34gO2HUT1ymMVvQvrfLE08K66OsiDJ4JeS6FWmqpwAuruN20zYuX8Cz4QDf18%2BWSBLk5xkjV%2BYQIH7%2FCtKc6vBddoCRlgiFj48BDuE7YK51mCiFxu3HNm4Uf8GEbPvXFK4uIWc8ujNxvr%2FrDU9kGBkcZYqI3AnE8v6v5exWZxuUzJONHl6Pga6K1Wflv8wt4lHXtUtuX4n6xW%2FW%2F%2F18TLEsRTrmBtUm%2B3f7OwvrZtvGA8OKLRGIXeHOvIQkSvRmi7E7yX%2FN9UWfcHCoVstwU%2BgwDhuuhbwYLvjOK26iqNC2oohMitPOnHvMZlAdKAGbOhQACBOuPLLE%2FaZIgF0xOhMX%2BGPofKO8MkzDl%2BeS8BjqkAX7l6W195%2BqUNF9t95yxfFzk3XT0Aun9YodgGVeozqPLVzCRGIab2eZAckKoGzYZB3eK0TGW2b1awPgfTOR%2B8yIukKFo%2Bx0l4PMWKqEZHGWuDx2SIUROtBF1q%2B6SuD7OcZyR39vFcaNS9DNWa1h8ZdlNn7L%2FjKMa1XsbaXleocrliYSQu2BUnNA92nAXBqeIMl5IX2gfvVwmyKhZhY8fwx6yXmmd&X-Amz-Signature=7ee3cf827972af056cab2d070460668fa95f1744e10ba97d5e09ff87287fdffd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMD3K7J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCkW%2Bk7SRqjp7300PwyhA4IGcujqjk4D1lD%2FAXEx3Rw1QIhANtmDznWjMdqzSvFy5Dp9tMPosXLuVPzZirL9mpg3c3cKv8DCH0QABoMNjM3NDIzMTgzODA1IgzcyyF0HuTgrgthMjMq3APEhUTwhUjIy14Bebe8yfolf4e8iGQj9xUrEn83BOOYr37yy6dF3f1DvE2FEljwwbRZTcwdVu1SHgj5NsMjvcsuY607fTaqjEOpiU7B2pzyx8QROORe4b6Z6SnfqC0CKS7jF0wa60YCpWaEy4G%2FRGlFm9d9PA36UbFcp9d4sww4F4BBqEE%2FiSVnTlAOcsQ03R8ibt8gnO2W92mQZfCpzI%2FU2h6UU1dmxHdkyXs%2BRI9cinSt3H7nvNiXP4%2B%2FLgYrhEaLq%2Bd4eIcJYnaIyQstJsoyECBu34gO2HUT1ymMVvQvrfLE08K66OsiDJ4JeS6FWmqpwAuruN20zYuX8Cz4QDf18%2BWSBLk5xkjV%2BYQIH7%2FCtKc6vBddoCRlgiFj48BDuE7YK51mCiFxu3HNm4Uf8GEbPvXFK4uIWc8ujNxvr%2FrDU9kGBkcZYqI3AnE8v6v5exWZxuUzJONHl6Pga6K1Wflv8wt4lHXtUtuX4n6xW%2FW%2F%2F18TLEsRTrmBtUm%2B3f7OwvrZtvGA8OKLRGIXeHOvIQkSvRmi7E7yX%2FN9UWfcHCoVstwU%2BgwDhuuhbwYLvjOK26iqNC2oohMitPOnHvMZlAdKAGbOhQACBOuPLLE%2FaZIgF0xOhMX%2BGPofKO8MkzDl%2BeS8BjqkAX7l6W195%2BqUNF9t95yxfFzk3XT0Aun9YodgGVeozqPLVzCRGIab2eZAckKoGzYZB3eK0TGW2b1awPgfTOR%2B8yIukKFo%2Bx0l4PMWKqEZHGWuDx2SIUROtBF1q%2B6SuD7OcZyR39vFcaNS9DNWa1h8ZdlNn7L%2FjKMa1XsbaXleocrliYSQu2BUnNA92nAXBqeIMl5IX2gfvVwmyKhZhY8fwx6yXmmd&X-Amz-Signature=76ef249556787ab5c80fef0c2c1f474d9670be72bde9977c80ae8f7d1c420cd6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMD3K7J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCkW%2Bk7SRqjp7300PwyhA4IGcujqjk4D1lD%2FAXEx3Rw1QIhANtmDznWjMdqzSvFy5Dp9tMPosXLuVPzZirL9mpg3c3cKv8DCH0QABoMNjM3NDIzMTgzODA1IgzcyyF0HuTgrgthMjMq3APEhUTwhUjIy14Bebe8yfolf4e8iGQj9xUrEn83BOOYr37yy6dF3f1DvE2FEljwwbRZTcwdVu1SHgj5NsMjvcsuY607fTaqjEOpiU7B2pzyx8QROORe4b6Z6SnfqC0CKS7jF0wa60YCpWaEy4G%2FRGlFm9d9PA36UbFcp9d4sww4F4BBqEE%2FiSVnTlAOcsQ03R8ibt8gnO2W92mQZfCpzI%2FU2h6UU1dmxHdkyXs%2BRI9cinSt3H7nvNiXP4%2B%2FLgYrhEaLq%2Bd4eIcJYnaIyQstJsoyECBu34gO2HUT1ymMVvQvrfLE08K66OsiDJ4JeS6FWmqpwAuruN20zYuX8Cz4QDf18%2BWSBLk5xkjV%2BYQIH7%2FCtKc6vBddoCRlgiFj48BDuE7YK51mCiFxu3HNm4Uf8GEbPvXFK4uIWc8ujNxvr%2FrDU9kGBkcZYqI3AnE8v6v5exWZxuUzJONHl6Pga6K1Wflv8wt4lHXtUtuX4n6xW%2FW%2F%2F18TLEsRTrmBtUm%2B3f7OwvrZtvGA8OKLRGIXeHOvIQkSvRmi7E7yX%2FN9UWfcHCoVstwU%2BgwDhuuhbwYLvjOK26iqNC2oohMitPOnHvMZlAdKAGbOhQACBOuPLLE%2FaZIgF0xOhMX%2BGPofKO8MkzDl%2BeS8BjqkAX7l6W195%2BqUNF9t95yxfFzk3XT0Aun9YodgGVeozqPLVzCRGIab2eZAckKoGzYZB3eK0TGW2b1awPgfTOR%2B8yIukKFo%2Bx0l4PMWKqEZHGWuDx2SIUROtBF1q%2B6SuD7OcZyR39vFcaNS9DNWa1h8ZdlNn7L%2FjKMa1XsbaXleocrliYSQu2BUnNA92nAXBqeIMl5IX2gfvVwmyKhZhY8fwx6yXmmd&X-Amz-Signature=7ba9dbb9081c6cdba1409bae4923de24a12bc295ff5bc457b202c43aea26d756&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGUXQHHP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQC1aj2Gvms1hvkza5RvTMcAf0d%2FZch3Yyfy7XY1yOlxeAIhAJg275SFDYHTc6N6iBemWhJoovQ3JVMpDddwx%2BDXBzPUKv8DCH4QABoMNjM3NDIzMTgzODA1Igyuojzo1dme0Iq0ZUsq3AMG%2F27On0u9gFXVM3wM%2FAQVU4JB6fc4OM0VRjmhE%2Fewd80Fi0SSh8BhWAXipnBym6meDRoKi447rYlAJEXMEkYqb%2FwHHk8MP%2FcjebteDb5VQ1v%2FRXbMJN%2FJy1zqla8H1FpTGYVhmuw9vCSDggZejZwK%2BCAQ95uHGHIv%2BUUVM8x1SF6IJn4kZnsOSaxoupabMbBJp9tWrzfZ4HJnGpv1k5YcMdKKt4TeGUjXGowXma9YOco7QcCapZdtqf4ms0zqDSWOTQmlEwNqIt6t%2FY84ZO5CtmhYFoGnm%2B6hjqa4HLESfuTk2thE42H5PJvc1VWX%2B%2FGVzwBZotOIg1PiEn2sJ7f8J%2F9kD%2BU8W%2FpUZKirTnFkoV13kUJWrABZ%2BK6IcRuuZxEPDqGcPv7k98iMY8cbCbmpxJYO57W5RkQBG%2FuPPKLgbg8zC33daM7RuGL5uoRRXHpamm89qgPo33rfY6P2DjzPaWTC7HM3j3AwTxCS06iRYRftBhxwuA8tPYDHbG%2FYR%2Bt%2FlHTjkvf2vkA789GU3TZO3pullxRt2RW185Tv8wjZV3QjfEyiK6CfGz%2FG7egNWDmzJd10N8zlm0TeSEMmxobnbimMDH7NGQiJaA5ZoFwuUqtEemD4h18sN9qmajDb%2BeS8BjqkAW2cAf5ETMgLojBWWur0tmT8GTaBJfCxHBIUO4%2FjspZv31Kj4%2FPZVihP3120JjQUd7qjwkENxEXrdeiVzCWkG%2FN924yDzhF5dH2IGR3KbITmZV7UJZXzSGTmZjaKrxKHonP4i0hP7FiNG%2F%2FGW4PXuiCExrRYy7uuCkYgh9fef%2BKl2xGHw%2Fp1KJsoQj4vb8LwVGhlxJsgXhDjz8O8RvR7n1Em0AFf&X-Amz-Signature=53e6cf00e90dbe214d1b661cca4ebe9588694d9f308a010b4384e2595dfba9c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGUXQHHP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQC1aj2Gvms1hvkza5RvTMcAf0d%2FZch3Yyfy7XY1yOlxeAIhAJg275SFDYHTc6N6iBemWhJoovQ3JVMpDddwx%2BDXBzPUKv8DCH4QABoMNjM3NDIzMTgzODA1Igyuojzo1dme0Iq0ZUsq3AMG%2F27On0u9gFXVM3wM%2FAQVU4JB6fc4OM0VRjmhE%2Fewd80Fi0SSh8BhWAXipnBym6meDRoKi447rYlAJEXMEkYqb%2FwHHk8MP%2FcjebteDb5VQ1v%2FRXbMJN%2FJy1zqla8H1FpTGYVhmuw9vCSDggZejZwK%2BCAQ95uHGHIv%2BUUVM8x1SF6IJn4kZnsOSaxoupabMbBJp9tWrzfZ4HJnGpv1k5YcMdKKt4TeGUjXGowXma9YOco7QcCapZdtqf4ms0zqDSWOTQmlEwNqIt6t%2FY84ZO5CtmhYFoGnm%2B6hjqa4HLESfuTk2thE42H5PJvc1VWX%2B%2FGVzwBZotOIg1PiEn2sJ7f8J%2F9kD%2BU8W%2FpUZKirTnFkoV13kUJWrABZ%2BK6IcRuuZxEPDqGcPv7k98iMY8cbCbmpxJYO57W5RkQBG%2FuPPKLgbg8zC33daM7RuGL5uoRRXHpamm89qgPo33rfY6P2DjzPaWTC7HM3j3AwTxCS06iRYRftBhxwuA8tPYDHbG%2FYR%2Bt%2FlHTjkvf2vkA789GU3TZO3pullxRt2RW185Tv8wjZV3QjfEyiK6CfGz%2FG7egNWDmzJd10N8zlm0TeSEMmxobnbimMDH7NGQiJaA5ZoFwuUqtEemD4h18sN9qmajDb%2BeS8BjqkAW2cAf5ETMgLojBWWur0tmT8GTaBJfCxHBIUO4%2FjspZv31Kj4%2FPZVihP3120JjQUd7qjwkENxEXrdeiVzCWkG%2FN924yDzhF5dH2IGR3KbITmZV7UJZXzSGTmZjaKrxKHonP4i0hP7FiNG%2F%2FGW4PXuiCExrRYy7uuCkYgh9fef%2BKl2xGHw%2Fp1KJsoQj4vb8LwVGhlxJsgXhDjz8O8RvR7n1Em0AFf&X-Amz-Signature=44faf5de4ad96507ed4a31d48fd65c952d79766a8c700c08b3e54b4687ca3885&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGUXQHHP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQC1aj2Gvms1hvkza5RvTMcAf0d%2FZch3Yyfy7XY1yOlxeAIhAJg275SFDYHTc6N6iBemWhJoovQ3JVMpDddwx%2BDXBzPUKv8DCH4QABoMNjM3NDIzMTgzODA1Igyuojzo1dme0Iq0ZUsq3AMG%2F27On0u9gFXVM3wM%2FAQVU4JB6fc4OM0VRjmhE%2Fewd80Fi0SSh8BhWAXipnBym6meDRoKi447rYlAJEXMEkYqb%2FwHHk8MP%2FcjebteDb5VQ1v%2FRXbMJN%2FJy1zqla8H1FpTGYVhmuw9vCSDggZejZwK%2BCAQ95uHGHIv%2BUUVM8x1SF6IJn4kZnsOSaxoupabMbBJp9tWrzfZ4HJnGpv1k5YcMdKKt4TeGUjXGowXma9YOco7QcCapZdtqf4ms0zqDSWOTQmlEwNqIt6t%2FY84ZO5CtmhYFoGnm%2B6hjqa4HLESfuTk2thE42H5PJvc1VWX%2B%2FGVzwBZotOIg1PiEn2sJ7f8J%2F9kD%2BU8W%2FpUZKirTnFkoV13kUJWrABZ%2BK6IcRuuZxEPDqGcPv7k98iMY8cbCbmpxJYO57W5RkQBG%2FuPPKLgbg8zC33daM7RuGL5uoRRXHpamm89qgPo33rfY6P2DjzPaWTC7HM3j3AwTxCS06iRYRftBhxwuA8tPYDHbG%2FYR%2Bt%2FlHTjkvf2vkA789GU3TZO3pullxRt2RW185Tv8wjZV3QjfEyiK6CfGz%2FG7egNWDmzJd10N8zlm0TeSEMmxobnbimMDH7NGQiJaA5ZoFwuUqtEemD4h18sN9qmajDb%2BeS8BjqkAW2cAf5ETMgLojBWWur0tmT8GTaBJfCxHBIUO4%2FjspZv31Kj4%2FPZVihP3120JjQUd7qjwkENxEXrdeiVzCWkG%2FN924yDzhF5dH2IGR3KbITmZV7UJZXzSGTmZjaKrxKHonP4i0hP7FiNG%2F%2FGW4PXuiCExrRYy7uuCkYgh9fef%2BKl2xGHw%2Fp1KJsoQj4vb8LwVGhlxJsgXhDjz8O8RvR7n1Em0AFf&X-Amz-Signature=be2da0252f3eb22e894d4f5cc4a73deb5f408403c892f73602e349994bd915b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGUXQHHP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQC1aj2Gvms1hvkza5RvTMcAf0d%2FZch3Yyfy7XY1yOlxeAIhAJg275SFDYHTc6N6iBemWhJoovQ3JVMpDddwx%2BDXBzPUKv8DCH4QABoMNjM3NDIzMTgzODA1Igyuojzo1dme0Iq0ZUsq3AMG%2F27On0u9gFXVM3wM%2FAQVU4JB6fc4OM0VRjmhE%2Fewd80Fi0SSh8BhWAXipnBym6meDRoKi447rYlAJEXMEkYqb%2FwHHk8MP%2FcjebteDb5VQ1v%2FRXbMJN%2FJy1zqla8H1FpTGYVhmuw9vCSDggZejZwK%2BCAQ95uHGHIv%2BUUVM8x1SF6IJn4kZnsOSaxoupabMbBJp9tWrzfZ4HJnGpv1k5YcMdKKt4TeGUjXGowXma9YOco7QcCapZdtqf4ms0zqDSWOTQmlEwNqIt6t%2FY84ZO5CtmhYFoGnm%2B6hjqa4HLESfuTk2thE42H5PJvc1VWX%2B%2FGVzwBZotOIg1PiEn2sJ7f8J%2F9kD%2BU8W%2FpUZKirTnFkoV13kUJWrABZ%2BK6IcRuuZxEPDqGcPv7k98iMY8cbCbmpxJYO57W5RkQBG%2FuPPKLgbg8zC33daM7RuGL5uoRRXHpamm89qgPo33rfY6P2DjzPaWTC7HM3j3AwTxCS06iRYRftBhxwuA8tPYDHbG%2FYR%2Bt%2FlHTjkvf2vkA789GU3TZO3pullxRt2RW185Tv8wjZV3QjfEyiK6CfGz%2FG7egNWDmzJd10N8zlm0TeSEMmxobnbimMDH7NGQiJaA5ZoFwuUqtEemD4h18sN9qmajDb%2BeS8BjqkAW2cAf5ETMgLojBWWur0tmT8GTaBJfCxHBIUO4%2FjspZv31Kj4%2FPZVihP3120JjQUd7qjwkENxEXrdeiVzCWkG%2FN924yDzhF5dH2IGR3KbITmZV7UJZXzSGTmZjaKrxKHonP4i0hP7FiNG%2F%2FGW4PXuiCExrRYy7uuCkYgh9fef%2BKl2xGHw%2Fp1KJsoQj4vb8LwVGhlxJsgXhDjz8O8RvR7n1Em0AFf&X-Amz-Signature=c606c92c0cc34e3190c1b23ce28d759167b6793a918608da532cd6c48e2ca1cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGUXQHHP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQC1aj2Gvms1hvkza5RvTMcAf0d%2FZch3Yyfy7XY1yOlxeAIhAJg275SFDYHTc6N6iBemWhJoovQ3JVMpDddwx%2BDXBzPUKv8DCH4QABoMNjM3NDIzMTgzODA1Igyuojzo1dme0Iq0ZUsq3AMG%2F27On0u9gFXVM3wM%2FAQVU4JB6fc4OM0VRjmhE%2Fewd80Fi0SSh8BhWAXipnBym6meDRoKi447rYlAJEXMEkYqb%2FwHHk8MP%2FcjebteDb5VQ1v%2FRXbMJN%2FJy1zqla8H1FpTGYVhmuw9vCSDggZejZwK%2BCAQ95uHGHIv%2BUUVM8x1SF6IJn4kZnsOSaxoupabMbBJp9tWrzfZ4HJnGpv1k5YcMdKKt4TeGUjXGowXma9YOco7QcCapZdtqf4ms0zqDSWOTQmlEwNqIt6t%2FY84ZO5CtmhYFoGnm%2B6hjqa4HLESfuTk2thE42H5PJvc1VWX%2B%2FGVzwBZotOIg1PiEn2sJ7f8J%2F9kD%2BU8W%2FpUZKirTnFkoV13kUJWrABZ%2BK6IcRuuZxEPDqGcPv7k98iMY8cbCbmpxJYO57W5RkQBG%2FuPPKLgbg8zC33daM7RuGL5uoRRXHpamm89qgPo33rfY6P2DjzPaWTC7HM3j3AwTxCS06iRYRftBhxwuA8tPYDHbG%2FYR%2Bt%2FlHTjkvf2vkA789GU3TZO3pullxRt2RW185Tv8wjZV3QjfEyiK6CfGz%2FG7egNWDmzJd10N8zlm0TeSEMmxobnbimMDH7NGQiJaA5ZoFwuUqtEemD4h18sN9qmajDb%2BeS8BjqkAW2cAf5ETMgLojBWWur0tmT8GTaBJfCxHBIUO4%2FjspZv31Kj4%2FPZVihP3120JjQUd7qjwkENxEXrdeiVzCWkG%2FN924yDzhF5dH2IGR3KbITmZV7UJZXzSGTmZjaKrxKHonP4i0hP7FiNG%2F%2FGW4PXuiCExrRYy7uuCkYgh9fef%2BKl2xGHw%2Fp1KJsoQj4vb8LwVGhlxJsgXhDjz8O8RvR7n1Em0AFf&X-Amz-Signature=5af46da3fa5b3396565dd75586e1283c357d10d68976f89a08e382b4c1ff5bba&X-Amz-SignedHeaders=host&x-id=GetObject)
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


