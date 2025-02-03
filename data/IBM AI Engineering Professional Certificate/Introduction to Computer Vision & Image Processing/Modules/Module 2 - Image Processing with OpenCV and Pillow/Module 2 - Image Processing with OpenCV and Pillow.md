

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H63JGRT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQPTuEKZWcC2QihcWn%2B%2F8AZnr%2BiE0kMPIlJGgei4kUOAiEA51PqhWjCQYj87q9HYPXy%2FrFrd5BJE0mnmOYi9hUN2Q8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAJNy4rU9NK4uukThircA90fOZsG1Re4fdIPtJuHHL%2FSAr0YfWQM2aCr2hrxCG%2F6IWTotaznKTdgg%2B451utTFYE6YJ97H2TRK%2BaeWx6Rh3XcAQAskfoiyJaCy4OyMsbx9Ui6%2FuQ5vPj%2BnhQ0ewq22W1CkEaYApJM0pOag9oVAvYqUm%2B47ZTY%2BlHAYJp1VN71sG20j1AUZCtWAaQSjieWhC2z7BgK0tplQ1oSRha7jw5Bn4FRD1ecw0HNG3Cx63Ww%2FRiWOBP35K6%2BXyhITMfk1TM3CqydfbZIJ93OcbaOJ5jCQsfOVD%2Bm%2BA2%2BqwPswXBz215V8K3Eu5Nck5CAHAp7uWumTsuBu09MgUkFSy%2FxXvkNSYgybfhUR53cnuN6NffzmFyRwlpPKfB96xJE73pjAmj%2BL9CPK2NfsxV%2F6v2k9sIeSibwic3wYuSl9T%2F2SatYrXff2N1WqDm1KQOaWisNQOOJcw4ksWhYNSnntC44K3eEnnfGeBEcNTaq4Kh5cBW2BPgNbtl9aXUGgOJ440DQSlEmVvpokBSwRmYGiWTiWJcLGBGPnh7mtko9Q4ZrjhHh%2FboKaoWIoMsMI61qbPVLKW2X312sCq%2BYhwRQDTKoCZ%2Bz9L%2BXr61D%2FcDY6RH%2FOKnsKyprwFHeRSUAsTjhMJvzgb0GOqUBD9zHFwCjSpB7Om8KsleOqYKTOxPxT8pGCs1m%2Bm080DawRBYTosiP6wTZgP6fJ4qzRackK2YMdENEfOsxmj9oXJNKIDTzbu1zF6Qek47QlxQYk3DwekXeCxFr36osM7UKsG%2Ffz%2BQXqQ%2BdII%2BMuZPln1%2FmgyoS1N%2B6OB825WN5eCVYc5oeEc%2BU2U66cpNZg86jK6NrwFCKsh41gafAbndWxXV8YZOQ&X-Amz-Signature=2a31e44156595d488bb67eb728305e40c4e66151c27687ee837b7c38da411c40&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JPRJDMR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHC%2Bsbf5zPWe0xPxyQffi61hLBtyapoCjxik065SUmwIgae2hyadDdlrBEHMqAf8zRtQpgTlKVgkAkpG%2BJgBcGqUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEpajOmb%2FbmdeTLigircA%2Fb3nGR87R9LvILiPB6t2El00Dyr4%2FeBqWz8GtulW%2FCdCr1CZ2MhDfQX%2FbOr0H%2Bw71c1B8hw%2FhTdktSHY6h1cmp2I2u8kfXiJhQF6%2B4EEKniiq%2FQ0j9BySt2vFxPzzbCLndDsCwtadU%2FIwii0q57FHiGa0UJeSNSM%2F9NyHj%2FtHbCFfr32nRt7zMrzW%2FN%2BkEpwbxdfU7pmk%2FHLSr3d66mtW%2FSTRmIjtbLKwr%2BEsnn53IQNa57BtRphjH45Cdpbo4SoUdqTm1vt%2BmBpo7VkMm%2B%2Fuq3mnXQKN2EQ3LZpJUzFzBT9yakf5ZKZI8fhaXIAp33Nbm6mTjPBX0zMwx8wJXwVBV2iRhYVTHmf1trN8JiIE23sRVUxtork%2FHSEdMs5%2B1IuY8WMQeBMB278P5Q2CLkSyL5Kk9ZIlE91qOw4341E9Ox%2F1eCUTuYCG9E0H%2BFWiD7j1TilF9Gq8HQi84GXIwIKuoJNfJ3wK%2FUrIGjryL6yoDlza2sCo5PxBaWGpqnXkOLyMXGFCW%2Bto645JcD6cNPpSayuHFHW0xtGmMLPszoYPaYToTnK6KfQlJGu8tHYL6jijeOapjnRzebbnBJvx9DGeu%2F%2BKiIZ04BogAgdaPSnjI8w2qsbh6in8YOudSOMMXzgb0GOqUBo4UOYLkWUOcvF3BpipNU%2BYvW0Z2m5IDtUgtEYzosVmbN0tLIY28m5kAVJBz8gGLoRKMO41FeVijebMmSPnjLKC2KuATM%2F5Mxz5rTZdnJ3RZFYXCbc7U1OoYdX1RTsqNYYOjVOXKQRaZumUZ5rmezYPqM8ygLcN10bbvvbCuhVvCxuDjjFMpvv2vSEd2Q1lldxiNYUg4jsVDO34hKajNJhBnC9V%2Fi&X-Amz-Signature=93d5daa5554611874b9535ad9edc8a0fdc6084b7b3e046f8dce877a079435657&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JPRJDMR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHC%2Bsbf5zPWe0xPxyQffi61hLBtyapoCjxik065SUmwIgae2hyadDdlrBEHMqAf8zRtQpgTlKVgkAkpG%2BJgBcGqUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEpajOmb%2FbmdeTLigircA%2Fb3nGR87R9LvILiPB6t2El00Dyr4%2FeBqWz8GtulW%2FCdCr1CZ2MhDfQX%2FbOr0H%2Bw71c1B8hw%2FhTdktSHY6h1cmp2I2u8kfXiJhQF6%2B4EEKniiq%2FQ0j9BySt2vFxPzzbCLndDsCwtadU%2FIwii0q57FHiGa0UJeSNSM%2F9NyHj%2FtHbCFfr32nRt7zMrzW%2FN%2BkEpwbxdfU7pmk%2FHLSr3d66mtW%2FSTRmIjtbLKwr%2BEsnn53IQNa57BtRphjH45Cdpbo4SoUdqTm1vt%2BmBpo7VkMm%2B%2Fuq3mnXQKN2EQ3LZpJUzFzBT9yakf5ZKZI8fhaXIAp33Nbm6mTjPBX0zMwx8wJXwVBV2iRhYVTHmf1trN8JiIE23sRVUxtork%2FHSEdMs5%2B1IuY8WMQeBMB278P5Q2CLkSyL5Kk9ZIlE91qOw4341E9Ox%2F1eCUTuYCG9E0H%2BFWiD7j1TilF9Gq8HQi84GXIwIKuoJNfJ3wK%2FUrIGjryL6yoDlza2sCo5PxBaWGpqnXkOLyMXGFCW%2Bto645JcD6cNPpSayuHFHW0xtGmMLPszoYPaYToTnK6KfQlJGu8tHYL6jijeOapjnRzebbnBJvx9DGeu%2F%2BKiIZ04BogAgdaPSnjI8w2qsbh6in8YOudSOMMXzgb0GOqUBo4UOYLkWUOcvF3BpipNU%2BYvW0Z2m5IDtUgtEYzosVmbN0tLIY28m5kAVJBz8gGLoRKMO41FeVijebMmSPnjLKC2KuATM%2F5Mxz5rTZdnJ3RZFYXCbc7U1OoYdX1RTsqNYYOjVOXKQRaZumUZ5rmezYPqM8ygLcN10bbvvbCuhVvCxuDjjFMpvv2vSEd2Q1lldxiNYUg4jsVDO34hKajNJhBnC9V%2Fi&X-Amz-Signature=23315ddd5329361ebd6fb7f03855f00ba6d72e5386875b7a7f36633e5a748c1f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JPRJDMR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHC%2Bsbf5zPWe0xPxyQffi61hLBtyapoCjxik065SUmwIgae2hyadDdlrBEHMqAf8zRtQpgTlKVgkAkpG%2BJgBcGqUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEpajOmb%2FbmdeTLigircA%2Fb3nGR87R9LvILiPB6t2El00Dyr4%2FeBqWz8GtulW%2FCdCr1CZ2MhDfQX%2FbOr0H%2Bw71c1B8hw%2FhTdktSHY6h1cmp2I2u8kfXiJhQF6%2B4EEKniiq%2FQ0j9BySt2vFxPzzbCLndDsCwtadU%2FIwii0q57FHiGa0UJeSNSM%2F9NyHj%2FtHbCFfr32nRt7zMrzW%2FN%2BkEpwbxdfU7pmk%2FHLSr3d66mtW%2FSTRmIjtbLKwr%2BEsnn53IQNa57BtRphjH45Cdpbo4SoUdqTm1vt%2BmBpo7VkMm%2B%2Fuq3mnXQKN2EQ3LZpJUzFzBT9yakf5ZKZI8fhaXIAp33Nbm6mTjPBX0zMwx8wJXwVBV2iRhYVTHmf1trN8JiIE23sRVUxtork%2FHSEdMs5%2B1IuY8WMQeBMB278P5Q2CLkSyL5Kk9ZIlE91qOw4341E9Ox%2F1eCUTuYCG9E0H%2BFWiD7j1TilF9Gq8HQi84GXIwIKuoJNfJ3wK%2FUrIGjryL6yoDlza2sCo5PxBaWGpqnXkOLyMXGFCW%2Bto645JcD6cNPpSayuHFHW0xtGmMLPszoYPaYToTnK6KfQlJGu8tHYL6jijeOapjnRzebbnBJvx9DGeu%2F%2BKiIZ04BogAgdaPSnjI8w2qsbh6in8YOudSOMMXzgb0GOqUBo4UOYLkWUOcvF3BpipNU%2BYvW0Z2m5IDtUgtEYzosVmbN0tLIY28m5kAVJBz8gGLoRKMO41FeVijebMmSPnjLKC2KuATM%2F5Mxz5rTZdnJ3RZFYXCbc7U1OoYdX1RTsqNYYOjVOXKQRaZumUZ5rmezYPqM8ygLcN10bbvvbCuhVvCxuDjjFMpvv2vSEd2Q1lldxiNYUg4jsVDO34hKajNJhBnC9V%2Fi&X-Amz-Signature=e90217daa39a53c40a2dc2f68aa855f4d271ea77447a6fe4760b78d3c055af1b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JPRJDMR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHC%2Bsbf5zPWe0xPxyQffi61hLBtyapoCjxik065SUmwIgae2hyadDdlrBEHMqAf8zRtQpgTlKVgkAkpG%2BJgBcGqUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEpajOmb%2FbmdeTLigircA%2Fb3nGR87R9LvILiPB6t2El00Dyr4%2FeBqWz8GtulW%2FCdCr1CZ2MhDfQX%2FbOr0H%2Bw71c1B8hw%2FhTdktSHY6h1cmp2I2u8kfXiJhQF6%2B4EEKniiq%2FQ0j9BySt2vFxPzzbCLndDsCwtadU%2FIwii0q57FHiGa0UJeSNSM%2F9NyHj%2FtHbCFfr32nRt7zMrzW%2FN%2BkEpwbxdfU7pmk%2FHLSr3d66mtW%2FSTRmIjtbLKwr%2BEsnn53IQNa57BtRphjH45Cdpbo4SoUdqTm1vt%2BmBpo7VkMm%2B%2Fuq3mnXQKN2EQ3LZpJUzFzBT9yakf5ZKZI8fhaXIAp33Nbm6mTjPBX0zMwx8wJXwVBV2iRhYVTHmf1trN8JiIE23sRVUxtork%2FHSEdMs5%2B1IuY8WMQeBMB278P5Q2CLkSyL5Kk9ZIlE91qOw4341E9Ox%2F1eCUTuYCG9E0H%2BFWiD7j1TilF9Gq8HQi84GXIwIKuoJNfJ3wK%2FUrIGjryL6yoDlza2sCo5PxBaWGpqnXkOLyMXGFCW%2Bto645JcD6cNPpSayuHFHW0xtGmMLPszoYPaYToTnK6KfQlJGu8tHYL6jijeOapjnRzebbnBJvx9DGeu%2F%2BKiIZ04BogAgdaPSnjI8w2qsbh6in8YOudSOMMXzgb0GOqUBo4UOYLkWUOcvF3BpipNU%2BYvW0Z2m5IDtUgtEYzosVmbN0tLIY28m5kAVJBz8gGLoRKMO41FeVijebMmSPnjLKC2KuATM%2F5Mxz5rTZdnJ3RZFYXCbc7U1OoYdX1RTsqNYYOjVOXKQRaZumUZ5rmezYPqM8ygLcN10bbvvbCuhVvCxuDjjFMpvv2vSEd2Q1lldxiNYUg4jsVDO34hKajNJhBnC9V%2Fi&X-Amz-Signature=4265343e16a52f45e014b40018207dabaf4f109ffc94ab6e7bfd6e767f7254c9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JPRJDMR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHC%2Bsbf5zPWe0xPxyQffi61hLBtyapoCjxik065SUmwIgae2hyadDdlrBEHMqAf8zRtQpgTlKVgkAkpG%2BJgBcGqUq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEpajOmb%2FbmdeTLigircA%2Fb3nGR87R9LvILiPB6t2El00Dyr4%2FeBqWz8GtulW%2FCdCr1CZ2MhDfQX%2FbOr0H%2Bw71c1B8hw%2FhTdktSHY6h1cmp2I2u8kfXiJhQF6%2B4EEKniiq%2FQ0j9BySt2vFxPzzbCLndDsCwtadU%2FIwii0q57FHiGa0UJeSNSM%2F9NyHj%2FtHbCFfr32nRt7zMrzW%2FN%2BkEpwbxdfU7pmk%2FHLSr3d66mtW%2FSTRmIjtbLKwr%2BEsnn53IQNa57BtRphjH45Cdpbo4SoUdqTm1vt%2BmBpo7VkMm%2B%2Fuq3mnXQKN2EQ3LZpJUzFzBT9yakf5ZKZI8fhaXIAp33Nbm6mTjPBX0zMwx8wJXwVBV2iRhYVTHmf1trN8JiIE23sRVUxtork%2FHSEdMs5%2B1IuY8WMQeBMB278P5Q2CLkSyL5Kk9ZIlE91qOw4341E9Ox%2F1eCUTuYCG9E0H%2BFWiD7j1TilF9Gq8HQi84GXIwIKuoJNfJ3wK%2FUrIGjryL6yoDlza2sCo5PxBaWGpqnXkOLyMXGFCW%2Bto645JcD6cNPpSayuHFHW0xtGmMLPszoYPaYToTnK6KfQlJGu8tHYL6jijeOapjnRzebbnBJvx9DGeu%2F%2BKiIZ04BogAgdaPSnjI8w2qsbh6in8YOudSOMMXzgb0GOqUBo4UOYLkWUOcvF3BpipNU%2BYvW0Z2m5IDtUgtEYzosVmbN0tLIY28m5kAVJBz8gGLoRKMO41FeVijebMmSPnjLKC2KuATM%2F5Mxz5rTZdnJ3RZFYXCbc7U1OoYdX1RTsqNYYOjVOXKQRaZumUZ5rmezYPqM8ygLcN10bbvvbCuhVvCxuDjjFMpvv2vSEd2Q1lldxiNYUg4jsVDO34hKajNJhBnC9V%2Fi&X-Amz-Signature=fce17f88da544a8da5fdb8325db194a97bf16092e6db4927b0b6d6dac8455157&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H63JGRT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQPTuEKZWcC2QihcWn%2B%2F8AZnr%2BiE0kMPIlJGgei4kUOAiEA51PqhWjCQYj87q9HYPXy%2FrFrd5BJE0mnmOYi9hUN2Q8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAJNy4rU9NK4uukThircA90fOZsG1Re4fdIPtJuHHL%2FSAr0YfWQM2aCr2hrxCG%2F6IWTotaznKTdgg%2B451utTFYE6YJ97H2TRK%2BaeWx6Rh3XcAQAskfoiyJaCy4OyMsbx9Ui6%2FuQ5vPj%2BnhQ0ewq22W1CkEaYApJM0pOag9oVAvYqUm%2B47ZTY%2BlHAYJp1VN71sG20j1AUZCtWAaQSjieWhC2z7BgK0tplQ1oSRha7jw5Bn4FRD1ecw0HNG3Cx63Ww%2FRiWOBP35K6%2BXyhITMfk1TM3CqydfbZIJ93OcbaOJ5jCQsfOVD%2Bm%2BA2%2BqwPswXBz215V8K3Eu5Nck5CAHAp7uWumTsuBu09MgUkFSy%2FxXvkNSYgybfhUR53cnuN6NffzmFyRwlpPKfB96xJE73pjAmj%2BL9CPK2NfsxV%2F6v2k9sIeSibwic3wYuSl9T%2F2SatYrXff2N1WqDm1KQOaWisNQOOJcw4ksWhYNSnntC44K3eEnnfGeBEcNTaq4Kh5cBW2BPgNbtl9aXUGgOJ440DQSlEmVvpokBSwRmYGiWTiWJcLGBGPnh7mtko9Q4ZrjhHh%2FboKaoWIoMsMI61qbPVLKW2X312sCq%2BYhwRQDTKoCZ%2Bz9L%2BXr61D%2FcDY6RH%2FOKnsKyprwFHeRSUAsTjhMJvzgb0GOqUBD9zHFwCjSpB7Om8KsleOqYKTOxPxT8pGCs1m%2Bm080DawRBYTosiP6wTZgP6fJ4qzRackK2YMdENEfOsxmj9oXJNKIDTzbu1zF6Qek47QlxQYk3DwekXeCxFr36osM7UKsG%2Ffz%2BQXqQ%2BdII%2BMuZPln1%2FmgyoS1N%2B6OB825WN5eCVYc5oeEc%2BU2U66cpNZg86jK6NrwFCKsh41gafAbndWxXV8YZOQ&X-Amz-Signature=2b49a30ab1a6bc4f66060167f50697bf977967465c275d50939289e98a001f76&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H63JGRT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQPTuEKZWcC2QihcWn%2B%2F8AZnr%2BiE0kMPIlJGgei4kUOAiEA51PqhWjCQYj87q9HYPXy%2FrFrd5BJE0mnmOYi9hUN2Q8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAJNy4rU9NK4uukThircA90fOZsG1Re4fdIPtJuHHL%2FSAr0YfWQM2aCr2hrxCG%2F6IWTotaznKTdgg%2B451utTFYE6YJ97H2TRK%2BaeWx6Rh3XcAQAskfoiyJaCy4OyMsbx9Ui6%2FuQ5vPj%2BnhQ0ewq22W1CkEaYApJM0pOag9oVAvYqUm%2B47ZTY%2BlHAYJp1VN71sG20j1AUZCtWAaQSjieWhC2z7BgK0tplQ1oSRha7jw5Bn4FRD1ecw0HNG3Cx63Ww%2FRiWOBP35K6%2BXyhITMfk1TM3CqydfbZIJ93OcbaOJ5jCQsfOVD%2Bm%2BA2%2BqwPswXBz215V8K3Eu5Nck5CAHAp7uWumTsuBu09MgUkFSy%2FxXvkNSYgybfhUR53cnuN6NffzmFyRwlpPKfB96xJE73pjAmj%2BL9CPK2NfsxV%2F6v2k9sIeSibwic3wYuSl9T%2F2SatYrXff2N1WqDm1KQOaWisNQOOJcw4ksWhYNSnntC44K3eEnnfGeBEcNTaq4Kh5cBW2BPgNbtl9aXUGgOJ440DQSlEmVvpokBSwRmYGiWTiWJcLGBGPnh7mtko9Q4ZrjhHh%2FboKaoWIoMsMI61qbPVLKW2X312sCq%2BYhwRQDTKoCZ%2Bz9L%2BXr61D%2FcDY6RH%2FOKnsKyprwFHeRSUAsTjhMJvzgb0GOqUBD9zHFwCjSpB7Om8KsleOqYKTOxPxT8pGCs1m%2Bm080DawRBYTosiP6wTZgP6fJ4qzRackK2YMdENEfOsxmj9oXJNKIDTzbu1zF6Qek47QlxQYk3DwekXeCxFr36osM7UKsG%2Ffz%2BQXqQ%2BdII%2BMuZPln1%2FmgyoS1N%2B6OB825WN5eCVYc5oeEc%2BU2U66cpNZg86jK6NrwFCKsh41gafAbndWxXV8YZOQ&X-Amz-Signature=b03f4f699aab005202ddbdc71915cf00dc7bc9371ba2d556366bbe45bce522ed&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H63JGRT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQPTuEKZWcC2QihcWn%2B%2F8AZnr%2BiE0kMPIlJGgei4kUOAiEA51PqhWjCQYj87q9HYPXy%2FrFrd5BJE0mnmOYi9hUN2Q8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAJNy4rU9NK4uukThircA90fOZsG1Re4fdIPtJuHHL%2FSAr0YfWQM2aCr2hrxCG%2F6IWTotaznKTdgg%2B451utTFYE6YJ97H2TRK%2BaeWx6Rh3XcAQAskfoiyJaCy4OyMsbx9Ui6%2FuQ5vPj%2BnhQ0ewq22W1CkEaYApJM0pOag9oVAvYqUm%2B47ZTY%2BlHAYJp1VN71sG20j1AUZCtWAaQSjieWhC2z7BgK0tplQ1oSRha7jw5Bn4FRD1ecw0HNG3Cx63Ww%2FRiWOBP35K6%2BXyhITMfk1TM3CqydfbZIJ93OcbaOJ5jCQsfOVD%2Bm%2BA2%2BqwPswXBz215V8K3Eu5Nck5CAHAp7uWumTsuBu09MgUkFSy%2FxXvkNSYgybfhUR53cnuN6NffzmFyRwlpPKfB96xJE73pjAmj%2BL9CPK2NfsxV%2F6v2k9sIeSibwic3wYuSl9T%2F2SatYrXff2N1WqDm1KQOaWisNQOOJcw4ksWhYNSnntC44K3eEnnfGeBEcNTaq4Kh5cBW2BPgNbtl9aXUGgOJ440DQSlEmVvpokBSwRmYGiWTiWJcLGBGPnh7mtko9Q4ZrjhHh%2FboKaoWIoMsMI61qbPVLKW2X312sCq%2BYhwRQDTKoCZ%2Bz9L%2BXr61D%2FcDY6RH%2FOKnsKyprwFHeRSUAsTjhMJvzgb0GOqUBD9zHFwCjSpB7Om8KsleOqYKTOxPxT8pGCs1m%2Bm080DawRBYTosiP6wTZgP6fJ4qzRackK2YMdENEfOsxmj9oXJNKIDTzbu1zF6Qek47QlxQYk3DwekXeCxFr36osM7UKsG%2Ffz%2BQXqQ%2BdII%2BMuZPln1%2FmgyoS1N%2B6OB825WN5eCVYc5oeEc%2BU2U66cpNZg86jK6NrwFCKsh41gafAbndWxXV8YZOQ&X-Amz-Signature=050cc148c605fe5c3575fb92389aaa23b3eb999f565cb28c6ce5ce488a3566ee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H63JGRT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQPTuEKZWcC2QihcWn%2B%2F8AZnr%2BiE0kMPIlJGgei4kUOAiEA51PqhWjCQYj87q9HYPXy%2FrFrd5BJE0mnmOYi9hUN2Q8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAJNy4rU9NK4uukThircA90fOZsG1Re4fdIPtJuHHL%2FSAr0YfWQM2aCr2hrxCG%2F6IWTotaznKTdgg%2B451utTFYE6YJ97H2TRK%2BaeWx6Rh3XcAQAskfoiyJaCy4OyMsbx9Ui6%2FuQ5vPj%2BnhQ0ewq22W1CkEaYApJM0pOag9oVAvYqUm%2B47ZTY%2BlHAYJp1VN71sG20j1AUZCtWAaQSjieWhC2z7BgK0tplQ1oSRha7jw5Bn4FRD1ecw0HNG3Cx63Ww%2FRiWOBP35K6%2BXyhITMfk1TM3CqydfbZIJ93OcbaOJ5jCQsfOVD%2Bm%2BA2%2BqwPswXBz215V8K3Eu5Nck5CAHAp7uWumTsuBu09MgUkFSy%2FxXvkNSYgybfhUR53cnuN6NffzmFyRwlpPKfB96xJE73pjAmj%2BL9CPK2NfsxV%2F6v2k9sIeSibwic3wYuSl9T%2F2SatYrXff2N1WqDm1KQOaWisNQOOJcw4ksWhYNSnntC44K3eEnnfGeBEcNTaq4Kh5cBW2BPgNbtl9aXUGgOJ440DQSlEmVvpokBSwRmYGiWTiWJcLGBGPnh7mtko9Q4ZrjhHh%2FboKaoWIoMsMI61qbPVLKW2X312sCq%2BYhwRQDTKoCZ%2Bz9L%2BXr61D%2FcDY6RH%2FOKnsKyprwFHeRSUAsTjhMJvzgb0GOqUBD9zHFwCjSpB7Om8KsleOqYKTOxPxT8pGCs1m%2Bm080DawRBYTosiP6wTZgP6fJ4qzRackK2YMdENEfOsxmj9oXJNKIDTzbu1zF6Qek47QlxQYk3DwekXeCxFr36osM7UKsG%2Ffz%2BQXqQ%2BdII%2BMuZPln1%2FmgyoS1N%2B6OB825WN5eCVYc5oeEc%2BU2U66cpNZg86jK6NrwFCKsh41gafAbndWxXV8YZOQ&X-Amz-Signature=eca120d19bbd6745141b341b93bb9f7e6a4bde1770bec0fcb94fd57b0034da2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H63JGRT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQPTuEKZWcC2QihcWn%2B%2F8AZnr%2BiE0kMPIlJGgei4kUOAiEA51PqhWjCQYj87q9HYPXy%2FrFrd5BJE0mnmOYi9hUN2Q8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAJNy4rU9NK4uukThircA90fOZsG1Re4fdIPtJuHHL%2FSAr0YfWQM2aCr2hrxCG%2F6IWTotaznKTdgg%2B451utTFYE6YJ97H2TRK%2BaeWx6Rh3XcAQAskfoiyJaCy4OyMsbx9Ui6%2FuQ5vPj%2BnhQ0ewq22W1CkEaYApJM0pOag9oVAvYqUm%2B47ZTY%2BlHAYJp1VN71sG20j1AUZCtWAaQSjieWhC2z7BgK0tplQ1oSRha7jw5Bn4FRD1ecw0HNG3Cx63Ww%2FRiWOBP35K6%2BXyhITMfk1TM3CqydfbZIJ93OcbaOJ5jCQsfOVD%2Bm%2BA2%2BqwPswXBz215V8K3Eu5Nck5CAHAp7uWumTsuBu09MgUkFSy%2FxXvkNSYgybfhUR53cnuN6NffzmFyRwlpPKfB96xJE73pjAmj%2BL9CPK2NfsxV%2F6v2k9sIeSibwic3wYuSl9T%2F2SatYrXff2N1WqDm1KQOaWisNQOOJcw4ksWhYNSnntC44K3eEnnfGeBEcNTaq4Kh5cBW2BPgNbtl9aXUGgOJ440DQSlEmVvpokBSwRmYGiWTiWJcLGBGPnh7mtko9Q4ZrjhHh%2FboKaoWIoMsMI61qbPVLKW2X312sCq%2BYhwRQDTKoCZ%2Bz9L%2BXr61D%2FcDY6RH%2FOKnsKyprwFHeRSUAsTjhMJvzgb0GOqUBD9zHFwCjSpB7Om8KsleOqYKTOxPxT8pGCs1m%2Bm080DawRBYTosiP6wTZgP6fJ4qzRackK2YMdENEfOsxmj9oXJNKIDTzbu1zF6Qek47QlxQYk3DwekXeCxFr36osM7UKsG%2Ffz%2BQXqQ%2BdII%2BMuZPln1%2FmgyoS1N%2B6OB825WN5eCVYc5oeEc%2BU2U66cpNZg86jK6NrwFCKsh41gafAbndWxXV8YZOQ&X-Amz-Signature=c9e4de0db5661c5513b2f34cde749b00142f161f0296a58d7673e0bcae552bd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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


