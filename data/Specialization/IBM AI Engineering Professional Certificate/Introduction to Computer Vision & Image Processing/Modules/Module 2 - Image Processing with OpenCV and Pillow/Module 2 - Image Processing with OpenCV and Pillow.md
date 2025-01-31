

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CXOS4PV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAgFozbm9fKirlLim1AwuLL%2BoCKm7y7MPTqN85Q7LuTAIhAI0jRfxmCAa%2BK1dzzwPZC2CLGfNjpvloeszDn7%2FQBRatKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgkjzSEKLOMIZTWP0q3AMkEBBimK4kNxZt2kgzmR4UpJ8eutzkB0YcAPt4Dqy7lITVUFUllwHJcrttynQMo%2BAedbQ92nfB%2B2Adqa9aUNEFU1T7c5MtUhfVH4aFnVYz9%2FPtwFGc1LhDItsQqht1VNOXebo7yYLjx3MDiZnk%2FiSUe5yxyb6ZLcURwPP%2FrQiZtKxvGG5eQLXk3641BjZCPde2MpM%2BliTYjQ7Pf4e4vKWngIk%2BANnFaCXBenszM%2Fff9NCcN18TKIHn67SBZgFvmuCYDYJMUgic%2Fv7iZfzMApEioqsVIzmecNx1xPk99G0zdiu2H2RI29qQxyH6VpfvZaMkaETK0YA4DX2mJj2ASnOe3hqNFrr3Kj0VjwyTbDbAAQNGNq0r6zz44eSvpO8UHrGJSAGUvYKMZtN1Hih4AGeTmpRP3bjaMXOr76RmZzUWjA0M74AxhVS2yBVG017Gfh3QoSBQ7YS5nITS%2FUeil20BlVqHCnXQTEzskrGsX59OA8ympwE7l7%2BqwqBMUXH19Qg3zw4hoz3UZFACqIBz8G%2BJVIQYgEiUiMwoJDMcBeu5VuSimdEl4%2B61vZadnrXsKC7%2FjTe2PhfFJXXrvww8VSL1sVTz%2Fage0NdbKA1FJjwQXEYEs46op%2Fo0PT9o9zC3tfC8BjqkAQBSQEig8VHAuFvMa21e1%2Bjos1WLJnVxJpmH3g0V1dEPD8agp0Yaibleox3XPutoZxzUbek5skTdfUwPI4fBiV7r0%2BqEWU%2BNtZp9GYObogzPCDB4U90wstupdLBH3uR3FtLRXVRbqwfr%2Biw2s%2B64xzxcJte4S7ADAN6ciT81xTESXBycR%2BNUWZxId52%2FOIV6nczT%2FCBx2HW5ho3pLjoEYf5Q6%2FyD&X-Amz-Signature=e9c1cbac2bd33c2a282ddd33e17f58f6510a281ca6831e4010a57755cda255a3&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJWTKKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEypgMEX7UJoVNa4xY8SF6QkzOMS9UdR1DyBDHSXJZ%2B1AiBr6iYpHa%2B5%2Bt9nhogqNVRTGaUZhEwyE2F1Hvl72pkfmSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVwRABMgR0L%2FUwMOqKtwDDYkHK1IwZvkhREJiSlVkYl4nwueBi6nPJ7HA%2FEsIC9dJM5Mtf5ExARuXfGS4jHif9XwJQMHZdzhhgTSbGQSILEtiQ6pg7pjYt%2F0ppqLUCu%2FeQt5WHUsZroDadd4EshGknd4BpSXYr5InG%2BHfPl7bFMJZekWGssKY0oTnuHX9TH01blP16DsNHdU6xo9T6P14Jmlk%2BnqmsjUILalTztzlnrZPME2T8SmwZMPeOkHtBKCvkp44zoLm%2BHswos1QG9rxGw9WxrTXCh1WNB3pNTE1H6MZoFtLzE06%2BsvdWC06mBTvdZYLncIjlw7Gvcndpys8OGt30ZNm99UhLBixKp3mSQVQiotj6HPd8TLQHSKTun3XszIbKhUQ3s4IkNR5JVstLipTyFcLDDvp8uxgQ8NDSRFWN56uKOHmaDGBnt00hOlsWtOZHq20opig%2FSrlfpl6c1WbN00BZ%2FNZlNuOBDx9vcv%2BNtcX9qmFKqUK9QPjYHdeSzRuOpiWa36Xmy6tMASjYKZCAzRSnHhevdYzFJ%2Fp3hTa4vUxz50pB2PbC45ywp7VliuwN3ziO5BEfa%2FUSQZv%2Ff9GAtyZcBbtC5L4ebTUIsMNBLqD%2BevfdZ5eUv5wWYrguqFowwI7vlTReX8wlLXwvAY6pgH3UnZdMMP9vCpSyaLAmFF%2BbA0AiiFFSBHNaMv%2BIaOBWF0EfnwTUlKYXCqXqtQFo1LWKst4KQGZ29qhgXAgNxhJJq0WT9KeTKbnoSrK42o63lwY0ON8XTpHffxhtDAZf9qNYJTjcyBmY17Qy7cy%2BSeSmiUqena1I4myn91QP%2FOuGtyCAuN6Er7rhMi%2Bwtr3RJJosHhstkuYyzciGRi2Yjl34GECrheZ&X-Amz-Signature=41905052072ec2f7044fa88ffd42a9fdc2194753ee48c70f3445355785f967fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJWTKKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEypgMEX7UJoVNa4xY8SF6QkzOMS9UdR1DyBDHSXJZ%2B1AiBr6iYpHa%2B5%2Bt9nhogqNVRTGaUZhEwyE2F1Hvl72pkfmSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVwRABMgR0L%2FUwMOqKtwDDYkHK1IwZvkhREJiSlVkYl4nwueBi6nPJ7HA%2FEsIC9dJM5Mtf5ExARuXfGS4jHif9XwJQMHZdzhhgTSbGQSILEtiQ6pg7pjYt%2F0ppqLUCu%2FeQt5WHUsZroDadd4EshGknd4BpSXYr5InG%2BHfPl7bFMJZekWGssKY0oTnuHX9TH01blP16DsNHdU6xo9T6P14Jmlk%2BnqmsjUILalTztzlnrZPME2T8SmwZMPeOkHtBKCvkp44zoLm%2BHswos1QG9rxGw9WxrTXCh1WNB3pNTE1H6MZoFtLzE06%2BsvdWC06mBTvdZYLncIjlw7Gvcndpys8OGt30ZNm99UhLBixKp3mSQVQiotj6HPd8TLQHSKTun3XszIbKhUQ3s4IkNR5JVstLipTyFcLDDvp8uxgQ8NDSRFWN56uKOHmaDGBnt00hOlsWtOZHq20opig%2FSrlfpl6c1WbN00BZ%2FNZlNuOBDx9vcv%2BNtcX9qmFKqUK9QPjYHdeSzRuOpiWa36Xmy6tMASjYKZCAzRSnHhevdYzFJ%2Fp3hTa4vUxz50pB2PbC45ywp7VliuwN3ziO5BEfa%2FUSQZv%2Ff9GAtyZcBbtC5L4ebTUIsMNBLqD%2BevfdZ5eUv5wWYrguqFowwI7vlTReX8wlLXwvAY6pgH3UnZdMMP9vCpSyaLAmFF%2BbA0AiiFFSBHNaMv%2BIaOBWF0EfnwTUlKYXCqXqtQFo1LWKst4KQGZ29qhgXAgNxhJJq0WT9KeTKbnoSrK42o63lwY0ON8XTpHffxhtDAZf9qNYJTjcyBmY17Qy7cy%2BSeSmiUqena1I4myn91QP%2FOuGtyCAuN6Er7rhMi%2Bwtr3RJJosHhstkuYyzciGRi2Yjl34GECrheZ&X-Amz-Signature=7b0b3e756995695ae015704f4d691fa2de330fdcf6d1c917572b400ae9e61121&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJWTKKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEypgMEX7UJoVNa4xY8SF6QkzOMS9UdR1DyBDHSXJZ%2B1AiBr6iYpHa%2B5%2Bt9nhogqNVRTGaUZhEwyE2F1Hvl72pkfmSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVwRABMgR0L%2FUwMOqKtwDDYkHK1IwZvkhREJiSlVkYl4nwueBi6nPJ7HA%2FEsIC9dJM5Mtf5ExARuXfGS4jHif9XwJQMHZdzhhgTSbGQSILEtiQ6pg7pjYt%2F0ppqLUCu%2FeQt5WHUsZroDadd4EshGknd4BpSXYr5InG%2BHfPl7bFMJZekWGssKY0oTnuHX9TH01blP16DsNHdU6xo9T6P14Jmlk%2BnqmsjUILalTztzlnrZPME2T8SmwZMPeOkHtBKCvkp44zoLm%2BHswos1QG9rxGw9WxrTXCh1WNB3pNTE1H6MZoFtLzE06%2BsvdWC06mBTvdZYLncIjlw7Gvcndpys8OGt30ZNm99UhLBixKp3mSQVQiotj6HPd8TLQHSKTun3XszIbKhUQ3s4IkNR5JVstLipTyFcLDDvp8uxgQ8NDSRFWN56uKOHmaDGBnt00hOlsWtOZHq20opig%2FSrlfpl6c1WbN00BZ%2FNZlNuOBDx9vcv%2BNtcX9qmFKqUK9QPjYHdeSzRuOpiWa36Xmy6tMASjYKZCAzRSnHhevdYzFJ%2Fp3hTa4vUxz50pB2PbC45ywp7VliuwN3ziO5BEfa%2FUSQZv%2Ff9GAtyZcBbtC5L4ebTUIsMNBLqD%2BevfdZ5eUv5wWYrguqFowwI7vlTReX8wlLXwvAY6pgH3UnZdMMP9vCpSyaLAmFF%2BbA0AiiFFSBHNaMv%2BIaOBWF0EfnwTUlKYXCqXqtQFo1LWKst4KQGZ29qhgXAgNxhJJq0WT9KeTKbnoSrK42o63lwY0ON8XTpHffxhtDAZf9qNYJTjcyBmY17Qy7cy%2BSeSmiUqena1I4myn91QP%2FOuGtyCAuN6Er7rhMi%2Bwtr3RJJosHhstkuYyzciGRi2Yjl34GECrheZ&X-Amz-Signature=b4ebbadfd771bbc51ae80638b46d971486c8abc038a86bd49a5d56dae3ea147d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJWTKKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEypgMEX7UJoVNa4xY8SF6QkzOMS9UdR1DyBDHSXJZ%2B1AiBr6iYpHa%2B5%2Bt9nhogqNVRTGaUZhEwyE2F1Hvl72pkfmSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVwRABMgR0L%2FUwMOqKtwDDYkHK1IwZvkhREJiSlVkYl4nwueBi6nPJ7HA%2FEsIC9dJM5Mtf5ExARuXfGS4jHif9XwJQMHZdzhhgTSbGQSILEtiQ6pg7pjYt%2F0ppqLUCu%2FeQt5WHUsZroDadd4EshGknd4BpSXYr5InG%2BHfPl7bFMJZekWGssKY0oTnuHX9TH01blP16DsNHdU6xo9T6P14Jmlk%2BnqmsjUILalTztzlnrZPME2T8SmwZMPeOkHtBKCvkp44zoLm%2BHswos1QG9rxGw9WxrTXCh1WNB3pNTE1H6MZoFtLzE06%2BsvdWC06mBTvdZYLncIjlw7Gvcndpys8OGt30ZNm99UhLBixKp3mSQVQiotj6HPd8TLQHSKTun3XszIbKhUQ3s4IkNR5JVstLipTyFcLDDvp8uxgQ8NDSRFWN56uKOHmaDGBnt00hOlsWtOZHq20opig%2FSrlfpl6c1WbN00BZ%2FNZlNuOBDx9vcv%2BNtcX9qmFKqUK9QPjYHdeSzRuOpiWa36Xmy6tMASjYKZCAzRSnHhevdYzFJ%2Fp3hTa4vUxz50pB2PbC45ywp7VliuwN3ziO5BEfa%2FUSQZv%2Ff9GAtyZcBbtC5L4ebTUIsMNBLqD%2BevfdZ5eUv5wWYrguqFowwI7vlTReX8wlLXwvAY6pgH3UnZdMMP9vCpSyaLAmFF%2BbA0AiiFFSBHNaMv%2BIaOBWF0EfnwTUlKYXCqXqtQFo1LWKst4KQGZ29qhgXAgNxhJJq0WT9KeTKbnoSrK42o63lwY0ON8XTpHffxhtDAZf9qNYJTjcyBmY17Qy7cy%2BSeSmiUqena1I4myn91QP%2FOuGtyCAuN6Er7rhMi%2Bwtr3RJJosHhstkuYyzciGRi2Yjl34GECrheZ&X-Amz-Signature=f15f30cc3955818deb31722f082f3001c3f67ca1ad16343fba8eabe21e70e3f9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMJWTKKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEypgMEX7UJoVNa4xY8SF6QkzOMS9UdR1DyBDHSXJZ%2B1AiBr6iYpHa%2B5%2Bt9nhogqNVRTGaUZhEwyE2F1Hvl72pkfmSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVwRABMgR0L%2FUwMOqKtwDDYkHK1IwZvkhREJiSlVkYl4nwueBi6nPJ7HA%2FEsIC9dJM5Mtf5ExARuXfGS4jHif9XwJQMHZdzhhgTSbGQSILEtiQ6pg7pjYt%2F0ppqLUCu%2FeQt5WHUsZroDadd4EshGknd4BpSXYr5InG%2BHfPl7bFMJZekWGssKY0oTnuHX9TH01blP16DsNHdU6xo9T6P14Jmlk%2BnqmsjUILalTztzlnrZPME2T8SmwZMPeOkHtBKCvkp44zoLm%2BHswos1QG9rxGw9WxrTXCh1WNB3pNTE1H6MZoFtLzE06%2BsvdWC06mBTvdZYLncIjlw7Gvcndpys8OGt30ZNm99UhLBixKp3mSQVQiotj6HPd8TLQHSKTun3XszIbKhUQ3s4IkNR5JVstLipTyFcLDDvp8uxgQ8NDSRFWN56uKOHmaDGBnt00hOlsWtOZHq20opig%2FSrlfpl6c1WbN00BZ%2FNZlNuOBDx9vcv%2BNtcX9qmFKqUK9QPjYHdeSzRuOpiWa36Xmy6tMASjYKZCAzRSnHhevdYzFJ%2Fp3hTa4vUxz50pB2PbC45ywp7VliuwN3ziO5BEfa%2FUSQZv%2Ff9GAtyZcBbtC5L4ebTUIsMNBLqD%2BevfdZ5eUv5wWYrguqFowwI7vlTReX8wlLXwvAY6pgH3UnZdMMP9vCpSyaLAmFF%2BbA0AiiFFSBHNaMv%2BIaOBWF0EfnwTUlKYXCqXqtQFo1LWKst4KQGZ29qhgXAgNxhJJq0WT9KeTKbnoSrK42o63lwY0ON8XTpHffxhtDAZf9qNYJTjcyBmY17Qy7cy%2BSeSmiUqena1I4myn91QP%2FOuGtyCAuN6Er7rhMi%2Bwtr3RJJosHhstkuYyzciGRi2Yjl34GECrheZ&X-Amz-Signature=8849550c1bb544b39857dd6774db343b13de3edb77d6b4220bb633958fd5ca03&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CXOS4PV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAgFozbm9fKirlLim1AwuLL%2BoCKm7y7MPTqN85Q7LuTAIhAI0jRfxmCAa%2BK1dzzwPZC2CLGfNjpvloeszDn7%2FQBRatKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgkjzSEKLOMIZTWP0q3AMkEBBimK4kNxZt2kgzmR4UpJ8eutzkB0YcAPt4Dqy7lITVUFUllwHJcrttynQMo%2BAedbQ92nfB%2B2Adqa9aUNEFU1T7c5MtUhfVH4aFnVYz9%2FPtwFGc1LhDItsQqht1VNOXebo7yYLjx3MDiZnk%2FiSUe5yxyb6ZLcURwPP%2FrQiZtKxvGG5eQLXk3641BjZCPde2MpM%2BliTYjQ7Pf4e4vKWngIk%2BANnFaCXBenszM%2Fff9NCcN18TKIHn67SBZgFvmuCYDYJMUgic%2Fv7iZfzMApEioqsVIzmecNx1xPk99G0zdiu2H2RI29qQxyH6VpfvZaMkaETK0YA4DX2mJj2ASnOe3hqNFrr3Kj0VjwyTbDbAAQNGNq0r6zz44eSvpO8UHrGJSAGUvYKMZtN1Hih4AGeTmpRP3bjaMXOr76RmZzUWjA0M74AxhVS2yBVG017Gfh3QoSBQ7YS5nITS%2FUeil20BlVqHCnXQTEzskrGsX59OA8ympwE7l7%2BqwqBMUXH19Qg3zw4hoz3UZFACqIBz8G%2BJVIQYgEiUiMwoJDMcBeu5VuSimdEl4%2B61vZadnrXsKC7%2FjTe2PhfFJXXrvww8VSL1sVTz%2Fage0NdbKA1FJjwQXEYEs46op%2Fo0PT9o9zC3tfC8BjqkAQBSQEig8VHAuFvMa21e1%2Bjos1WLJnVxJpmH3g0V1dEPD8agp0Yaibleox3XPutoZxzUbek5skTdfUwPI4fBiV7r0%2BqEWU%2BNtZp9GYObogzPCDB4U90wstupdLBH3uR3FtLRXVRbqwfr%2Biw2s%2B64xzxcJte4S7ADAN6ciT81xTESXBycR%2BNUWZxId52%2FOIV6nczT%2FCBx2HW5ho3pLjoEYf5Q6%2FyD&X-Amz-Signature=9702fee772aea7732b6d6f10d7e1271876204cf3c6f6b370d915e4af30018313&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CXOS4PV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAgFozbm9fKirlLim1AwuLL%2BoCKm7y7MPTqN85Q7LuTAIhAI0jRfxmCAa%2BK1dzzwPZC2CLGfNjpvloeszDn7%2FQBRatKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgkjzSEKLOMIZTWP0q3AMkEBBimK4kNxZt2kgzmR4UpJ8eutzkB0YcAPt4Dqy7lITVUFUllwHJcrttynQMo%2BAedbQ92nfB%2B2Adqa9aUNEFU1T7c5MtUhfVH4aFnVYz9%2FPtwFGc1LhDItsQqht1VNOXebo7yYLjx3MDiZnk%2FiSUe5yxyb6ZLcURwPP%2FrQiZtKxvGG5eQLXk3641BjZCPde2MpM%2BliTYjQ7Pf4e4vKWngIk%2BANnFaCXBenszM%2Fff9NCcN18TKIHn67SBZgFvmuCYDYJMUgic%2Fv7iZfzMApEioqsVIzmecNx1xPk99G0zdiu2H2RI29qQxyH6VpfvZaMkaETK0YA4DX2mJj2ASnOe3hqNFrr3Kj0VjwyTbDbAAQNGNq0r6zz44eSvpO8UHrGJSAGUvYKMZtN1Hih4AGeTmpRP3bjaMXOr76RmZzUWjA0M74AxhVS2yBVG017Gfh3QoSBQ7YS5nITS%2FUeil20BlVqHCnXQTEzskrGsX59OA8ympwE7l7%2BqwqBMUXH19Qg3zw4hoz3UZFACqIBz8G%2BJVIQYgEiUiMwoJDMcBeu5VuSimdEl4%2B61vZadnrXsKC7%2FjTe2PhfFJXXrvww8VSL1sVTz%2Fage0NdbKA1FJjwQXEYEs46op%2Fo0PT9o9zC3tfC8BjqkAQBSQEig8VHAuFvMa21e1%2Bjos1WLJnVxJpmH3g0V1dEPD8agp0Yaibleox3XPutoZxzUbek5skTdfUwPI4fBiV7r0%2BqEWU%2BNtZp9GYObogzPCDB4U90wstupdLBH3uR3FtLRXVRbqwfr%2Biw2s%2B64xzxcJte4S7ADAN6ciT81xTESXBycR%2BNUWZxId52%2FOIV6nczT%2FCBx2HW5ho3pLjoEYf5Q6%2FyD&X-Amz-Signature=7bd39528c3ec97154ff5a8f521b7fe7400bf156f88dbcb3ff3f1012cef4dea6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CXOS4PV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAgFozbm9fKirlLim1AwuLL%2BoCKm7y7MPTqN85Q7LuTAIhAI0jRfxmCAa%2BK1dzzwPZC2CLGfNjpvloeszDn7%2FQBRatKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgkjzSEKLOMIZTWP0q3AMkEBBimK4kNxZt2kgzmR4UpJ8eutzkB0YcAPt4Dqy7lITVUFUllwHJcrttynQMo%2BAedbQ92nfB%2B2Adqa9aUNEFU1T7c5MtUhfVH4aFnVYz9%2FPtwFGc1LhDItsQqht1VNOXebo7yYLjx3MDiZnk%2FiSUe5yxyb6ZLcURwPP%2FrQiZtKxvGG5eQLXk3641BjZCPde2MpM%2BliTYjQ7Pf4e4vKWngIk%2BANnFaCXBenszM%2Fff9NCcN18TKIHn67SBZgFvmuCYDYJMUgic%2Fv7iZfzMApEioqsVIzmecNx1xPk99G0zdiu2H2RI29qQxyH6VpfvZaMkaETK0YA4DX2mJj2ASnOe3hqNFrr3Kj0VjwyTbDbAAQNGNq0r6zz44eSvpO8UHrGJSAGUvYKMZtN1Hih4AGeTmpRP3bjaMXOr76RmZzUWjA0M74AxhVS2yBVG017Gfh3QoSBQ7YS5nITS%2FUeil20BlVqHCnXQTEzskrGsX59OA8ympwE7l7%2BqwqBMUXH19Qg3zw4hoz3UZFACqIBz8G%2BJVIQYgEiUiMwoJDMcBeu5VuSimdEl4%2B61vZadnrXsKC7%2FjTe2PhfFJXXrvww8VSL1sVTz%2Fage0NdbKA1FJjwQXEYEs46op%2Fo0PT9o9zC3tfC8BjqkAQBSQEig8VHAuFvMa21e1%2Bjos1WLJnVxJpmH3g0V1dEPD8agp0Yaibleox3XPutoZxzUbek5skTdfUwPI4fBiV7r0%2BqEWU%2BNtZp9GYObogzPCDB4U90wstupdLBH3uR3FtLRXVRbqwfr%2Biw2s%2B64xzxcJte4S7ADAN6ciT81xTESXBycR%2BNUWZxId52%2FOIV6nczT%2FCBx2HW5ho3pLjoEYf5Q6%2FyD&X-Amz-Signature=9743a9e3a12d2be5024e320ff54977791e107ff1c155a06402d63c80a88ddd38&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CXOS4PV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAgFozbm9fKirlLim1AwuLL%2BoCKm7y7MPTqN85Q7LuTAIhAI0jRfxmCAa%2BK1dzzwPZC2CLGfNjpvloeszDn7%2FQBRatKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgkjzSEKLOMIZTWP0q3AMkEBBimK4kNxZt2kgzmR4UpJ8eutzkB0YcAPt4Dqy7lITVUFUllwHJcrttynQMo%2BAedbQ92nfB%2B2Adqa9aUNEFU1T7c5MtUhfVH4aFnVYz9%2FPtwFGc1LhDItsQqht1VNOXebo7yYLjx3MDiZnk%2FiSUe5yxyb6ZLcURwPP%2FrQiZtKxvGG5eQLXk3641BjZCPde2MpM%2BliTYjQ7Pf4e4vKWngIk%2BANnFaCXBenszM%2Fff9NCcN18TKIHn67SBZgFvmuCYDYJMUgic%2Fv7iZfzMApEioqsVIzmecNx1xPk99G0zdiu2H2RI29qQxyH6VpfvZaMkaETK0YA4DX2mJj2ASnOe3hqNFrr3Kj0VjwyTbDbAAQNGNq0r6zz44eSvpO8UHrGJSAGUvYKMZtN1Hih4AGeTmpRP3bjaMXOr76RmZzUWjA0M74AxhVS2yBVG017Gfh3QoSBQ7YS5nITS%2FUeil20BlVqHCnXQTEzskrGsX59OA8ympwE7l7%2BqwqBMUXH19Qg3zw4hoz3UZFACqIBz8G%2BJVIQYgEiUiMwoJDMcBeu5VuSimdEl4%2B61vZadnrXsKC7%2FjTe2PhfFJXXrvww8VSL1sVTz%2Fage0NdbKA1FJjwQXEYEs46op%2Fo0PT9o9zC3tfC8BjqkAQBSQEig8VHAuFvMa21e1%2Bjos1WLJnVxJpmH3g0V1dEPD8agp0Yaibleox3XPutoZxzUbek5skTdfUwPI4fBiV7r0%2BqEWU%2BNtZp9GYObogzPCDB4U90wstupdLBH3uR3FtLRXVRbqwfr%2Biw2s%2B64xzxcJte4S7ADAN6ciT81xTESXBycR%2BNUWZxId52%2FOIV6nczT%2FCBx2HW5ho3pLjoEYf5Q6%2FyD&X-Amz-Signature=5281b4e376e7b6deafc3f5330fa4b3199776f1a00f541e30f61572681cea846e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CXOS4PV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAgFozbm9fKirlLim1AwuLL%2BoCKm7y7MPTqN85Q7LuTAIhAI0jRfxmCAa%2BK1dzzwPZC2CLGfNjpvloeszDn7%2FQBRatKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxgkjzSEKLOMIZTWP0q3AMkEBBimK4kNxZt2kgzmR4UpJ8eutzkB0YcAPt4Dqy7lITVUFUllwHJcrttynQMo%2BAedbQ92nfB%2B2Adqa9aUNEFU1T7c5MtUhfVH4aFnVYz9%2FPtwFGc1LhDItsQqht1VNOXebo7yYLjx3MDiZnk%2FiSUe5yxyb6ZLcURwPP%2FrQiZtKxvGG5eQLXk3641BjZCPde2MpM%2BliTYjQ7Pf4e4vKWngIk%2BANnFaCXBenszM%2Fff9NCcN18TKIHn67SBZgFvmuCYDYJMUgic%2Fv7iZfzMApEioqsVIzmecNx1xPk99G0zdiu2H2RI29qQxyH6VpfvZaMkaETK0YA4DX2mJj2ASnOe3hqNFrr3Kj0VjwyTbDbAAQNGNq0r6zz44eSvpO8UHrGJSAGUvYKMZtN1Hih4AGeTmpRP3bjaMXOr76RmZzUWjA0M74AxhVS2yBVG017Gfh3QoSBQ7YS5nITS%2FUeil20BlVqHCnXQTEzskrGsX59OA8ympwE7l7%2BqwqBMUXH19Qg3zw4hoz3UZFACqIBz8G%2BJVIQYgEiUiMwoJDMcBeu5VuSimdEl4%2B61vZadnrXsKC7%2FjTe2PhfFJXXrvww8VSL1sVTz%2Fage0NdbKA1FJjwQXEYEs46op%2Fo0PT9o9zC3tfC8BjqkAQBSQEig8VHAuFvMa21e1%2Bjos1WLJnVxJpmH3g0V1dEPD8agp0Yaibleox3XPutoZxzUbek5skTdfUwPI4fBiV7r0%2BqEWU%2BNtZp9GYObogzPCDB4U90wstupdLBH3uR3FtLRXVRbqwfr%2Biw2s%2B64xzxcJte4S7ADAN6ciT81xTESXBycR%2BNUWZxId52%2FOIV6nczT%2FCBx2HW5ho3pLjoEYf5Q6%2FyD&X-Amz-Signature=113e0de48b3b35e1715c3d39bc308d7c09925ed9accb741a44475883e7fb236d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


