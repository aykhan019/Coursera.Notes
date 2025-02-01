

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=0eca501e53fa0f5e5814ee43434cfe4f95bd900454586e7a82db29d4e1ede75c&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466247MFV5Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy3tYIJy9ss3geYgG3pZZxXs3LsWgIOpePkLb3EmVD9AiEAzGD7QgkazFvVd7Ktf7KHTcUdKvOpMESCNirF0a6lSrAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBurwZ96fDMqI6y5TircA7nqwbj86u3jmoQ4LE9BCXogbMNVd7%2FewoUGulEN9L4X4QqkX96dhAkeBI3i9A2fz6ALMpgD4pE2XGEzu%2FAw%2BrhWdEIHl1GIzRTmwGRCOt0mhKLdSL2WUDUvq2afOmYXtwRJcYPBxzQT%2BGijWdmrq8C0AZRYmAZicuzSWJuGB%2FXuRQza%2FFUSdzV1ewXbqnaTS%2Filfq6pwf9489xKiGZIpd3QogkTUKcQnQNPZ4%2BIqWDSeXAu1tGn1hV7HukR86KPoFQCfacc1c7VFjXkZNoDefDtmHfGvo95QlL7T%2BYL0dMSdZFNzwZM9ATkX4Cj4kdEYn65mWZdeSA7Oh7VwFX1zj1bFys9geAz3a%2B3VQ036THR7dpQp6GrKgD1vG1O4vM%2BwMVUmOTvsiMLNzdgIWB4I%2BEBsCSr%2FQP1zj8vrAmUB4V11831vbVj4N3pP%2Ft2C%2FVlI2dpEhjqLzu0WMueBvfDNPdm%2Ba8dFhr2Cwy1eyoHfH%2FILrwrDskFv6DfLfau9twYot0qCr6ARh3WUld34WOI0etxep3UHWl9YSQ%2Bur9wILziXAuPRbHBz%2B6Qz2GGUWnB8mjXbleHVAe43Ib%2B11gdMS3XKDHmsCbhqN%2Faneg9xjlCvtYxjsJfvxib7D9HMIjE%2BLwGOqUBL16tPtAHghi%2BhAhGfi6lM6RCRWdKOrsJn9t6j7TmEIzX889k0nk3y6qHzXHmqGoNH7R%2BBzE3pf7c2M6dDGVAxczP61DFxqB8JjeI1uCXQjf%2BP0jUOuVIvdwNGE9MU0ARJ97OEMhKeh4ubTzqql91720BYsUIA4ualgy40mRN1dE8igOjNEC1G%2FXCM28%2BwZYLadjmZJHUZ7%2BZ%2FEJpXufZkfQ9g646&X-Amz-Signature=b235417c3fa91e2dc2889c171976363c2b4ab4eb7403f5ec60d71907d6061c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466247MFV5Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy3tYIJy9ss3geYgG3pZZxXs3LsWgIOpePkLb3EmVD9AiEAzGD7QgkazFvVd7Ktf7KHTcUdKvOpMESCNirF0a6lSrAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBurwZ96fDMqI6y5TircA7nqwbj86u3jmoQ4LE9BCXogbMNVd7%2FewoUGulEN9L4X4QqkX96dhAkeBI3i9A2fz6ALMpgD4pE2XGEzu%2FAw%2BrhWdEIHl1GIzRTmwGRCOt0mhKLdSL2WUDUvq2afOmYXtwRJcYPBxzQT%2BGijWdmrq8C0AZRYmAZicuzSWJuGB%2FXuRQza%2FFUSdzV1ewXbqnaTS%2Filfq6pwf9489xKiGZIpd3QogkTUKcQnQNPZ4%2BIqWDSeXAu1tGn1hV7HukR86KPoFQCfacc1c7VFjXkZNoDefDtmHfGvo95QlL7T%2BYL0dMSdZFNzwZM9ATkX4Cj4kdEYn65mWZdeSA7Oh7VwFX1zj1bFys9geAz3a%2B3VQ036THR7dpQp6GrKgD1vG1O4vM%2BwMVUmOTvsiMLNzdgIWB4I%2BEBsCSr%2FQP1zj8vrAmUB4V11831vbVj4N3pP%2Ft2C%2FVlI2dpEhjqLzu0WMueBvfDNPdm%2Ba8dFhr2Cwy1eyoHfH%2FILrwrDskFv6DfLfau9twYot0qCr6ARh3WUld34WOI0etxep3UHWl9YSQ%2Bur9wILziXAuPRbHBz%2B6Qz2GGUWnB8mjXbleHVAe43Ib%2B11gdMS3XKDHmsCbhqN%2Faneg9xjlCvtYxjsJfvxib7D9HMIjE%2BLwGOqUBL16tPtAHghi%2BhAhGfi6lM6RCRWdKOrsJn9t6j7TmEIzX889k0nk3y6qHzXHmqGoNH7R%2BBzE3pf7c2M6dDGVAxczP61DFxqB8JjeI1uCXQjf%2BP0jUOuVIvdwNGE9MU0ARJ97OEMhKeh4ubTzqql91720BYsUIA4ualgy40mRN1dE8igOjNEC1G%2FXCM28%2BwZYLadjmZJHUZ7%2BZ%2FEJpXufZkfQ9g646&X-Amz-Signature=7a0b1f81244f6013f332269a6640c08233f07e6a19446dafdab7fa8061f28b61&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466247MFV5Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy3tYIJy9ss3geYgG3pZZxXs3LsWgIOpePkLb3EmVD9AiEAzGD7QgkazFvVd7Ktf7KHTcUdKvOpMESCNirF0a6lSrAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBurwZ96fDMqI6y5TircA7nqwbj86u3jmoQ4LE9BCXogbMNVd7%2FewoUGulEN9L4X4QqkX96dhAkeBI3i9A2fz6ALMpgD4pE2XGEzu%2FAw%2BrhWdEIHl1GIzRTmwGRCOt0mhKLdSL2WUDUvq2afOmYXtwRJcYPBxzQT%2BGijWdmrq8C0AZRYmAZicuzSWJuGB%2FXuRQza%2FFUSdzV1ewXbqnaTS%2Filfq6pwf9489xKiGZIpd3QogkTUKcQnQNPZ4%2BIqWDSeXAu1tGn1hV7HukR86KPoFQCfacc1c7VFjXkZNoDefDtmHfGvo95QlL7T%2BYL0dMSdZFNzwZM9ATkX4Cj4kdEYn65mWZdeSA7Oh7VwFX1zj1bFys9geAz3a%2B3VQ036THR7dpQp6GrKgD1vG1O4vM%2BwMVUmOTvsiMLNzdgIWB4I%2BEBsCSr%2FQP1zj8vrAmUB4V11831vbVj4N3pP%2Ft2C%2FVlI2dpEhjqLzu0WMueBvfDNPdm%2Ba8dFhr2Cwy1eyoHfH%2FILrwrDskFv6DfLfau9twYot0qCr6ARh3WUld34WOI0etxep3UHWl9YSQ%2Bur9wILziXAuPRbHBz%2B6Qz2GGUWnB8mjXbleHVAe43Ib%2B11gdMS3XKDHmsCbhqN%2Faneg9xjlCvtYxjsJfvxib7D9HMIjE%2BLwGOqUBL16tPtAHghi%2BhAhGfi6lM6RCRWdKOrsJn9t6j7TmEIzX889k0nk3y6qHzXHmqGoNH7R%2BBzE3pf7c2M6dDGVAxczP61DFxqB8JjeI1uCXQjf%2BP0jUOuVIvdwNGE9MU0ARJ97OEMhKeh4ubTzqql91720BYsUIA4ualgy40mRN1dE8igOjNEC1G%2FXCM28%2BwZYLadjmZJHUZ7%2BZ%2FEJpXufZkfQ9g646&X-Amz-Signature=4c25e5e328079ef00dcc8a586da3f913e383e28e23ef9fa0c2988244bfe87b41&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466247MFV5Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy3tYIJy9ss3geYgG3pZZxXs3LsWgIOpePkLb3EmVD9AiEAzGD7QgkazFvVd7Ktf7KHTcUdKvOpMESCNirF0a6lSrAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBurwZ96fDMqI6y5TircA7nqwbj86u3jmoQ4LE9BCXogbMNVd7%2FewoUGulEN9L4X4QqkX96dhAkeBI3i9A2fz6ALMpgD4pE2XGEzu%2FAw%2BrhWdEIHl1GIzRTmwGRCOt0mhKLdSL2WUDUvq2afOmYXtwRJcYPBxzQT%2BGijWdmrq8C0AZRYmAZicuzSWJuGB%2FXuRQza%2FFUSdzV1ewXbqnaTS%2Filfq6pwf9489xKiGZIpd3QogkTUKcQnQNPZ4%2BIqWDSeXAu1tGn1hV7HukR86KPoFQCfacc1c7VFjXkZNoDefDtmHfGvo95QlL7T%2BYL0dMSdZFNzwZM9ATkX4Cj4kdEYn65mWZdeSA7Oh7VwFX1zj1bFys9geAz3a%2B3VQ036THR7dpQp6GrKgD1vG1O4vM%2BwMVUmOTvsiMLNzdgIWB4I%2BEBsCSr%2FQP1zj8vrAmUB4V11831vbVj4N3pP%2Ft2C%2FVlI2dpEhjqLzu0WMueBvfDNPdm%2Ba8dFhr2Cwy1eyoHfH%2FILrwrDskFv6DfLfau9twYot0qCr6ARh3WUld34WOI0etxep3UHWl9YSQ%2Bur9wILziXAuPRbHBz%2B6Qz2GGUWnB8mjXbleHVAe43Ib%2B11gdMS3XKDHmsCbhqN%2Faneg9xjlCvtYxjsJfvxib7D9HMIjE%2BLwGOqUBL16tPtAHghi%2BhAhGfi6lM6RCRWdKOrsJn9t6j7TmEIzX889k0nk3y6qHzXHmqGoNH7R%2BBzE3pf7c2M6dDGVAxczP61DFxqB8JjeI1uCXQjf%2BP0jUOuVIvdwNGE9MU0ARJ97OEMhKeh4ubTzqql91720BYsUIA4ualgy40mRN1dE8igOjNEC1G%2FXCM28%2BwZYLadjmZJHUZ7%2BZ%2FEJpXufZkfQ9g646&X-Amz-Signature=77f77ece80f7cb430a208de6ba273be7fb50ca8c00a99b76f22bcc1a8445a7eb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466247MFV5Z%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEy3tYIJy9ss3geYgG3pZZxXs3LsWgIOpePkLb3EmVD9AiEAzGD7QgkazFvVd7Ktf7KHTcUdKvOpMESCNirF0a6lSrAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBurwZ96fDMqI6y5TircA7nqwbj86u3jmoQ4LE9BCXogbMNVd7%2FewoUGulEN9L4X4QqkX96dhAkeBI3i9A2fz6ALMpgD4pE2XGEzu%2FAw%2BrhWdEIHl1GIzRTmwGRCOt0mhKLdSL2WUDUvq2afOmYXtwRJcYPBxzQT%2BGijWdmrq8C0AZRYmAZicuzSWJuGB%2FXuRQza%2FFUSdzV1ewXbqnaTS%2Filfq6pwf9489xKiGZIpd3QogkTUKcQnQNPZ4%2BIqWDSeXAu1tGn1hV7HukR86KPoFQCfacc1c7VFjXkZNoDefDtmHfGvo95QlL7T%2BYL0dMSdZFNzwZM9ATkX4Cj4kdEYn65mWZdeSA7Oh7VwFX1zj1bFys9geAz3a%2B3VQ036THR7dpQp6GrKgD1vG1O4vM%2BwMVUmOTvsiMLNzdgIWB4I%2BEBsCSr%2FQP1zj8vrAmUB4V11831vbVj4N3pP%2Ft2C%2FVlI2dpEhjqLzu0WMueBvfDNPdm%2Ba8dFhr2Cwy1eyoHfH%2FILrwrDskFv6DfLfau9twYot0qCr6ARh3WUld34WOI0etxep3UHWl9YSQ%2Bur9wILziXAuPRbHBz%2B6Qz2GGUWnB8mjXbleHVAe43Ib%2B11gdMS3XKDHmsCbhqN%2Faneg9xjlCvtYxjsJfvxib7D9HMIjE%2BLwGOqUBL16tPtAHghi%2BhAhGfi6lM6RCRWdKOrsJn9t6j7TmEIzX889k0nk3y6qHzXHmqGoNH7R%2BBzE3pf7c2M6dDGVAxczP61DFxqB8JjeI1uCXQjf%2BP0jUOuVIvdwNGE9MU0ARJ97OEMhKeh4ubTzqql91720BYsUIA4ualgy40mRN1dE8igOjNEC1G%2FXCM28%2BwZYLadjmZJHUZ7%2BZ%2FEJpXufZkfQ9g646&X-Amz-Signature=e47854dac3854d47115ce5657ab0b3e42663f7653653594579bb0df35d782b82&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=2bed633353beeee1a08049b83638983fb2122e80592b1ed697de4fcfe31b629d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=8b47288c009b56dc7c2d582bcfa1a1e45dc1a1dadbca5788a9a7a200fdc205d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=c7550dee281a9d8a6e4a24f25687563f6b7c463c7971f158a768acee17953406&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=28f93abf81b4f8ab79c3b80dadca37544d32d5b3dbca8f233f0cb591413dd59a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPXFGK5F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBbsz29Q%2FQwBaunUGeiGPZhJlnGkcRgDM3N8zjiSKuvvAiA%2B4N8z%2BdGKVtRQMNb8H1%2Fipt6pCXm4uI%2BuDg8Geg1QZyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMox%2FjdssXUKiRdHhHKtwD8oVY6%2BBej6dTEcZQE8213FV8BUjL1HBhobOwoX1tZYM4%2FCHx6a0%2FGCVCcM5CzbXAKNTqY61B2ytOlz%2FG27yH%2FiaaAk2Qa5c2ufVdhRdmHWS%2F%2F2XGU6tdWiihXrsrsTtU5Hbd4SfJUIp1wELwJxgYC80D3QSvPdmyRwvZBNlaVDe8Fp2W%2BBo22rvnWkqsOAjJE3xo5FMuTglogw36B5pmLnpIq2%2Fm6YGSHU7IlCzGDQlt9eewkcrT5xMg8LlH9rW5L%2Byi%2BD1dQmxi0iXWnre%2FH%2FZReMJVPfLUU3Qk%2Bwin%2B5fwXljZucVDExPl64k%2FDIV1gpqAG6D7rlSEz%2F5cWAkohj%2F0rOgdWYGUQjAM%2BWSt5UeesXw9VeZz2tI36%2BRfkZ%2BHFLQkMpGsuzGXNgLEepz%2BUiubLJvzeZAPC2jxpofWjTIZEjKdeuEV4yv%2BY39IDKPmKZPqZ151XpHWRkI8hF2NwldXUzwQX6XWnWJOKH6E442%2FZ66Xv1MN1jKafoCbRl2XSEIq5J9nRTcXgNgNzdCKd6JYiuqbHO8YwfmUxjMUSGoDLRO7U4QMKflJ6bhLWv7iKX%2BEETda80WH2N3tXDkfg32PZEu8O10XtCTm9FU8yB6AKoAKu6Moqe2dnm8w68f4vAY6pgFXlFz0tJT0u8ZvlxJ6jGvW68kZsRDJaLyYEqC0WB3EU8n4pbrZGAH4lm1T6q4Bf1tPUSGH08H1KKMIO%2BR9Sq2QFeH83Vlk3Xt0POwDC5s9LZbRgiBokfGUEpXuOVws3jGlzrpvNHxVkUZf1ClI7228HvlV2r6OxyRbflb%2B98cJRIvkpWzSLBVy2s6bBmlkMYzQmFhqY3LAitbwlX91bjpIp42LvUfg&X-Amz-Signature=b97223bf40e642df70399999d3c3607f2c293bad4ecfc5d22046ff5bffc73b1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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


