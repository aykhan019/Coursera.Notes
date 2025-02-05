

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFXSLFC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIADzYI4k9M44%2BcASgwRYugTNMghnPmwTkvZ6fNFsTjSnAiEA6QznyLLc9EfvT7h7tE0Yvba1taaboK27tRpAgDFD1Vcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDrDCi%2BwFV6M%2BoMWhircAzhBpdCI5gWfrjvb3Y3ACSlUxfGUmvRCe56T7Dai1EW0L3f7yY367eFPOdWpwBOVMpekLMjOiBV6X7m7%2BNsSP%2Bc%2BkDAVrnV%2FEMMBWKS2%2FUHxGadM6DxcX2S2opbKFf8AdVIfEqBbbUeC%2FL8p3G2oRqBtkYokHI43eWHnyavOK57NxrpyWmrbdjd0iLBeq7aL4Im4xO8LVQ%2FeGHgo%2B9eUJTn18X9hNLvTtrWGs6t5egrWSl03LIgBULuLwcEoGGYY%2BoO5TeKuMVeT71QPGxZaaIemcePdKBlnr%2F89fT0qBo92fAmzOpxDWghKt4urehA12ugC3Vp3GA8x7v4WgmA4cevlL1XHBli%2BHQcnZtjULOhZc8wMnaWj4Pvv%2FU3HJFz8xbXP55murzXnpbif0IQWnyDvnyBpDrzeovHtBcMDKaGabrTcVb8O28EWNZEmsxxxpVQrCkg6sLcWmyqQgGSeAHDYoJnloRpZO4VEQXigw8AhhQjuvwwv74alDIh%2FRtclE%2Bk%2FQFyG%2FaajyjwGCc3Nl%2Bb%2FseV57SaKvIALSKV674usWRDjNGse34%2FnL%2FJscCgDT4KOC0myKc975kZg%2BdyWxU3kVeSjpdi4x2jCwd91nkSdkN19Svd7HTujNRChMJmLjb0GOqUBbMCVxh0uLAEnp682uK4GSecRSqM4RehZUPitBnDquPLTxYhUVZqR56ycQgW%2BfCUPIcjXIGikvXjgPKM%2Br3Wsws1jnAjLNyIaF586kJOu%2FCchviqLNmv5NDsATaHaJlm9yi%2BoBpSGrwaR87pyBF2qGQiGCIcKPWP0JbG11%2B95Dv4JsSnahlQ%2BRpp0g27KFjhr4aD10ZHjfs7JSh9YCSyTDIDpE5gb&X-Amz-Signature=3a82bf3185fb099d11cd802475d9f1f4ab83149b7a940bfde3cd6ce5240607a2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UWJ4L2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIBv3DvKkMiQiI9HKUB6b7l6I3TlcS5Xvsi0tdgtyh24WAiAXNv9Xkdyfh9hPDBRvYWsewjYbxIxKLzK7Mjczg5Ui8Sr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMQWLShNims6tnKPZVKtwD%2BIgOr51OPifhatA8Dbia4aSKg5BepbOYdVsGhw1ByQyAPkoUa3fSeOkAu0PQ9KLOEKs0I%2BQjcvZUG8aU3n5DtfhP1Jd7dkXD0Du00lLyad5g0OjwPiojyLK0sMXr%2BrfuMClFnBqz7pOco32b7x7UO45A8PmIpOYRNkJNil4S6iic3qXqtmErpzAovpMye%2FiWmbvauxkgSZO3b0lCT8O23WViKAbeYO4s%2BSIKwtTAex5P%2B%2BfMDNP6ww16WZf2hirRhQlLpBC2TlmfrBnE9wv1gOjy%2FI8f8daGIIXnFIwg1yvZCmX2Crc4WJC6w0MFrio1nHfKgX34EG0HxZiYL%2BRH2fb31VBvo9LHZOULiDvugOCf%2BuuINOeJJcOzdugl9ewzdLJndZybYb49ZwG1wPZo17gjU%2FkSW6TCd5jbHD2H1YFclAqd2ETAl7NB83udkfAT59ytSyb8l4TdJzSrC41JSqwccEhfdv%2BlXbzXnkp9HcSlZfhdfCPMC7Q3Aa34Q%2Fsh0%2FEEDHUjiO1aMdNRMVtHkj8Wj4%2B18tSL3y6ayZCrWBt0rZ5NhdrgssQ0AW5B97aCD%2F%2BbmgKqyy5VFPATG5DS8PZgGbqFlmnrQAAdXcfMZOQKgu2SD2oxvR9YmB0wzeONvQY6pgGEDgenGPH7Ls%2B0KyGfa9uoihs31pcLeaJlPERLahXhWdOvbR5ngsr1yJKLPz0hQjh5pnHbps7IiYUFewjlWrjcvBT%2BZaTkzN3dSvQFl12JQpc9MIZzqstb%2FDsBjmnhrObKR2cyL%2B1qqOpcAa7slSaQVU%2B0YthxaWJFq4oolLpwPCF1O%2FY4HNMFBEcmP4%2B6BslNkkKN7sTg7Z4pzzmvK7pUwyKGqIu%2B&X-Amz-Signature=2762c7c92843c7fa95ea5f902053812cb5b9f21873e26509f19c10ff7f62e18a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UWJ4L2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIBv3DvKkMiQiI9HKUB6b7l6I3TlcS5Xvsi0tdgtyh24WAiAXNv9Xkdyfh9hPDBRvYWsewjYbxIxKLzK7Mjczg5Ui8Sr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMQWLShNims6tnKPZVKtwD%2BIgOr51OPifhatA8Dbia4aSKg5BepbOYdVsGhw1ByQyAPkoUa3fSeOkAu0PQ9KLOEKs0I%2BQjcvZUG8aU3n5DtfhP1Jd7dkXD0Du00lLyad5g0OjwPiojyLK0sMXr%2BrfuMClFnBqz7pOco32b7x7UO45A8PmIpOYRNkJNil4S6iic3qXqtmErpzAovpMye%2FiWmbvauxkgSZO3b0lCT8O23WViKAbeYO4s%2BSIKwtTAex5P%2B%2BfMDNP6ww16WZf2hirRhQlLpBC2TlmfrBnE9wv1gOjy%2FI8f8daGIIXnFIwg1yvZCmX2Crc4WJC6w0MFrio1nHfKgX34EG0HxZiYL%2BRH2fb31VBvo9LHZOULiDvugOCf%2BuuINOeJJcOzdugl9ewzdLJndZybYb49ZwG1wPZo17gjU%2FkSW6TCd5jbHD2H1YFclAqd2ETAl7NB83udkfAT59ytSyb8l4TdJzSrC41JSqwccEhfdv%2BlXbzXnkp9HcSlZfhdfCPMC7Q3Aa34Q%2Fsh0%2FEEDHUjiO1aMdNRMVtHkj8Wj4%2B18tSL3y6ayZCrWBt0rZ5NhdrgssQ0AW5B97aCD%2F%2BbmgKqyy5VFPATG5DS8PZgGbqFlmnrQAAdXcfMZOQKgu2SD2oxvR9YmB0wzeONvQY6pgGEDgenGPH7Ls%2B0KyGfa9uoihs31pcLeaJlPERLahXhWdOvbR5ngsr1yJKLPz0hQjh5pnHbps7IiYUFewjlWrjcvBT%2BZaTkzN3dSvQFl12JQpc9MIZzqstb%2FDsBjmnhrObKR2cyL%2B1qqOpcAa7slSaQVU%2B0YthxaWJFq4oolLpwPCF1O%2FY4HNMFBEcmP4%2B6BslNkkKN7sTg7Z4pzzmvK7pUwyKGqIu%2B&X-Amz-Signature=daea59a8ab0c5f20847ebed62fe8cc35b4dfd389d92e74d76f598e7c0a2c9fe1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UWJ4L2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIBv3DvKkMiQiI9HKUB6b7l6I3TlcS5Xvsi0tdgtyh24WAiAXNv9Xkdyfh9hPDBRvYWsewjYbxIxKLzK7Mjczg5Ui8Sr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMQWLShNims6tnKPZVKtwD%2BIgOr51OPifhatA8Dbia4aSKg5BepbOYdVsGhw1ByQyAPkoUa3fSeOkAu0PQ9KLOEKs0I%2BQjcvZUG8aU3n5DtfhP1Jd7dkXD0Du00lLyad5g0OjwPiojyLK0sMXr%2BrfuMClFnBqz7pOco32b7x7UO45A8PmIpOYRNkJNil4S6iic3qXqtmErpzAovpMye%2FiWmbvauxkgSZO3b0lCT8O23WViKAbeYO4s%2BSIKwtTAex5P%2B%2BfMDNP6ww16WZf2hirRhQlLpBC2TlmfrBnE9wv1gOjy%2FI8f8daGIIXnFIwg1yvZCmX2Crc4WJC6w0MFrio1nHfKgX34EG0HxZiYL%2BRH2fb31VBvo9LHZOULiDvugOCf%2BuuINOeJJcOzdugl9ewzdLJndZybYb49ZwG1wPZo17gjU%2FkSW6TCd5jbHD2H1YFclAqd2ETAl7NB83udkfAT59ytSyb8l4TdJzSrC41JSqwccEhfdv%2BlXbzXnkp9HcSlZfhdfCPMC7Q3Aa34Q%2Fsh0%2FEEDHUjiO1aMdNRMVtHkj8Wj4%2B18tSL3y6ayZCrWBt0rZ5NhdrgssQ0AW5B97aCD%2F%2BbmgKqyy5VFPATG5DS8PZgGbqFlmnrQAAdXcfMZOQKgu2SD2oxvR9YmB0wzeONvQY6pgGEDgenGPH7Ls%2B0KyGfa9uoihs31pcLeaJlPERLahXhWdOvbR5ngsr1yJKLPz0hQjh5pnHbps7IiYUFewjlWrjcvBT%2BZaTkzN3dSvQFl12JQpc9MIZzqstb%2FDsBjmnhrObKR2cyL%2B1qqOpcAa7slSaQVU%2B0YthxaWJFq4oolLpwPCF1O%2FY4HNMFBEcmP4%2B6BslNkkKN7sTg7Z4pzzmvK7pUwyKGqIu%2B&X-Amz-Signature=7aa9858bc30ed93ec2292acd3370e339a627ffb8b580efa34843e04ac5ec24bd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UWJ4L2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIBv3DvKkMiQiI9HKUB6b7l6I3TlcS5Xvsi0tdgtyh24WAiAXNv9Xkdyfh9hPDBRvYWsewjYbxIxKLzK7Mjczg5Ui8Sr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMQWLShNims6tnKPZVKtwD%2BIgOr51OPifhatA8Dbia4aSKg5BepbOYdVsGhw1ByQyAPkoUa3fSeOkAu0PQ9KLOEKs0I%2BQjcvZUG8aU3n5DtfhP1Jd7dkXD0Du00lLyad5g0OjwPiojyLK0sMXr%2BrfuMClFnBqz7pOco32b7x7UO45A8PmIpOYRNkJNil4S6iic3qXqtmErpzAovpMye%2FiWmbvauxkgSZO3b0lCT8O23WViKAbeYO4s%2BSIKwtTAex5P%2B%2BfMDNP6ww16WZf2hirRhQlLpBC2TlmfrBnE9wv1gOjy%2FI8f8daGIIXnFIwg1yvZCmX2Crc4WJC6w0MFrio1nHfKgX34EG0HxZiYL%2BRH2fb31VBvo9LHZOULiDvugOCf%2BuuINOeJJcOzdugl9ewzdLJndZybYb49ZwG1wPZo17gjU%2FkSW6TCd5jbHD2H1YFclAqd2ETAl7NB83udkfAT59ytSyb8l4TdJzSrC41JSqwccEhfdv%2BlXbzXnkp9HcSlZfhdfCPMC7Q3Aa34Q%2Fsh0%2FEEDHUjiO1aMdNRMVtHkj8Wj4%2B18tSL3y6ayZCrWBt0rZ5NhdrgssQ0AW5B97aCD%2F%2BbmgKqyy5VFPATG5DS8PZgGbqFlmnrQAAdXcfMZOQKgu2SD2oxvR9YmB0wzeONvQY6pgGEDgenGPH7Ls%2B0KyGfa9uoihs31pcLeaJlPERLahXhWdOvbR5ngsr1yJKLPz0hQjh5pnHbps7IiYUFewjlWrjcvBT%2BZaTkzN3dSvQFl12JQpc9MIZzqstb%2FDsBjmnhrObKR2cyL%2B1qqOpcAa7slSaQVU%2B0YthxaWJFq4oolLpwPCF1O%2FY4HNMFBEcmP4%2B6BslNkkKN7sTg7Z4pzzmvK7pUwyKGqIu%2B&X-Amz-Signature=88ac2aa566a94d544a1a18bf48d1fc5922e0093adec75318de3737fd6113cd2d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UWJ4L2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIBv3DvKkMiQiI9HKUB6b7l6I3TlcS5Xvsi0tdgtyh24WAiAXNv9Xkdyfh9hPDBRvYWsewjYbxIxKLzK7Mjczg5Ui8Sr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMQWLShNims6tnKPZVKtwD%2BIgOr51OPifhatA8Dbia4aSKg5BepbOYdVsGhw1ByQyAPkoUa3fSeOkAu0PQ9KLOEKs0I%2BQjcvZUG8aU3n5DtfhP1Jd7dkXD0Du00lLyad5g0OjwPiojyLK0sMXr%2BrfuMClFnBqz7pOco32b7x7UO45A8PmIpOYRNkJNil4S6iic3qXqtmErpzAovpMye%2FiWmbvauxkgSZO3b0lCT8O23WViKAbeYO4s%2BSIKwtTAex5P%2B%2BfMDNP6ww16WZf2hirRhQlLpBC2TlmfrBnE9wv1gOjy%2FI8f8daGIIXnFIwg1yvZCmX2Crc4WJC6w0MFrio1nHfKgX34EG0HxZiYL%2BRH2fb31VBvo9LHZOULiDvugOCf%2BuuINOeJJcOzdugl9ewzdLJndZybYb49ZwG1wPZo17gjU%2FkSW6TCd5jbHD2H1YFclAqd2ETAl7NB83udkfAT59ytSyb8l4TdJzSrC41JSqwccEhfdv%2BlXbzXnkp9HcSlZfhdfCPMC7Q3Aa34Q%2Fsh0%2FEEDHUjiO1aMdNRMVtHkj8Wj4%2B18tSL3y6ayZCrWBt0rZ5NhdrgssQ0AW5B97aCD%2F%2BbmgKqyy5VFPATG5DS8PZgGbqFlmnrQAAdXcfMZOQKgu2SD2oxvR9YmB0wzeONvQY6pgGEDgenGPH7Ls%2B0KyGfa9uoihs31pcLeaJlPERLahXhWdOvbR5ngsr1yJKLPz0hQjh5pnHbps7IiYUFewjlWrjcvBT%2BZaTkzN3dSvQFl12JQpc9MIZzqstb%2FDsBjmnhrObKR2cyL%2B1qqOpcAa7slSaQVU%2B0YthxaWJFq4oolLpwPCF1O%2FY4HNMFBEcmP4%2B6BslNkkKN7sTg7Z4pzzmvK7pUwyKGqIu%2B&X-Amz-Signature=330d3a25bc9a686436da8238bf55cf103fda5df02abc2bd14855f987ac25cb58&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFXSLFC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIADzYI4k9M44%2BcASgwRYugTNMghnPmwTkvZ6fNFsTjSnAiEA6QznyLLc9EfvT7h7tE0Yvba1taaboK27tRpAgDFD1Vcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDrDCi%2BwFV6M%2BoMWhircAzhBpdCI5gWfrjvb3Y3ACSlUxfGUmvRCe56T7Dai1EW0L3f7yY367eFPOdWpwBOVMpekLMjOiBV6X7m7%2BNsSP%2Bc%2BkDAVrnV%2FEMMBWKS2%2FUHxGadM6DxcX2S2opbKFf8AdVIfEqBbbUeC%2FL8p3G2oRqBtkYokHI43eWHnyavOK57NxrpyWmrbdjd0iLBeq7aL4Im4xO8LVQ%2FeGHgo%2B9eUJTn18X9hNLvTtrWGs6t5egrWSl03LIgBULuLwcEoGGYY%2BoO5TeKuMVeT71QPGxZaaIemcePdKBlnr%2F89fT0qBo92fAmzOpxDWghKt4urehA12ugC3Vp3GA8x7v4WgmA4cevlL1XHBli%2BHQcnZtjULOhZc8wMnaWj4Pvv%2FU3HJFz8xbXP55murzXnpbif0IQWnyDvnyBpDrzeovHtBcMDKaGabrTcVb8O28EWNZEmsxxxpVQrCkg6sLcWmyqQgGSeAHDYoJnloRpZO4VEQXigw8AhhQjuvwwv74alDIh%2FRtclE%2Bk%2FQFyG%2FaajyjwGCc3Nl%2Bb%2FseV57SaKvIALSKV674usWRDjNGse34%2FnL%2FJscCgDT4KOC0myKc975kZg%2BdyWxU3kVeSjpdi4x2jCwd91nkSdkN19Svd7HTujNRChMJmLjb0GOqUBbMCVxh0uLAEnp682uK4GSecRSqM4RehZUPitBnDquPLTxYhUVZqR56ycQgW%2BfCUPIcjXIGikvXjgPKM%2Br3Wsws1jnAjLNyIaF586kJOu%2FCchviqLNmv5NDsATaHaJlm9yi%2BoBpSGrwaR87pyBF2qGQiGCIcKPWP0JbG11%2B95Dv4JsSnahlQ%2BRpp0g27KFjhr4aD10ZHjfs7JSh9YCSyTDIDpE5gb&X-Amz-Signature=9045b2e26b489aef638338ecc93fcd8737036f88c801c4dc151973645f26fb36&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFXSLFC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIADzYI4k9M44%2BcASgwRYugTNMghnPmwTkvZ6fNFsTjSnAiEA6QznyLLc9EfvT7h7tE0Yvba1taaboK27tRpAgDFD1Vcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDrDCi%2BwFV6M%2BoMWhircAzhBpdCI5gWfrjvb3Y3ACSlUxfGUmvRCe56T7Dai1EW0L3f7yY367eFPOdWpwBOVMpekLMjOiBV6X7m7%2BNsSP%2Bc%2BkDAVrnV%2FEMMBWKS2%2FUHxGadM6DxcX2S2opbKFf8AdVIfEqBbbUeC%2FL8p3G2oRqBtkYokHI43eWHnyavOK57NxrpyWmrbdjd0iLBeq7aL4Im4xO8LVQ%2FeGHgo%2B9eUJTn18X9hNLvTtrWGs6t5egrWSl03LIgBULuLwcEoGGYY%2BoO5TeKuMVeT71QPGxZaaIemcePdKBlnr%2F89fT0qBo92fAmzOpxDWghKt4urehA12ugC3Vp3GA8x7v4WgmA4cevlL1XHBli%2BHQcnZtjULOhZc8wMnaWj4Pvv%2FU3HJFz8xbXP55murzXnpbif0IQWnyDvnyBpDrzeovHtBcMDKaGabrTcVb8O28EWNZEmsxxxpVQrCkg6sLcWmyqQgGSeAHDYoJnloRpZO4VEQXigw8AhhQjuvwwv74alDIh%2FRtclE%2Bk%2FQFyG%2FaajyjwGCc3Nl%2Bb%2FseV57SaKvIALSKV674usWRDjNGse34%2FnL%2FJscCgDT4KOC0myKc975kZg%2BdyWxU3kVeSjpdi4x2jCwd91nkSdkN19Svd7HTujNRChMJmLjb0GOqUBbMCVxh0uLAEnp682uK4GSecRSqM4RehZUPitBnDquPLTxYhUVZqR56ycQgW%2BfCUPIcjXIGikvXjgPKM%2Br3Wsws1jnAjLNyIaF586kJOu%2FCchviqLNmv5NDsATaHaJlm9yi%2BoBpSGrwaR87pyBF2qGQiGCIcKPWP0JbG11%2B95Dv4JsSnahlQ%2BRpp0g27KFjhr4aD10ZHjfs7JSh9YCSyTDIDpE5gb&X-Amz-Signature=d5b044dd932101748a7a05bb017ce4b4ce8e3fee632ff536301811ed6ab2d075&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFXSLFC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIADzYI4k9M44%2BcASgwRYugTNMghnPmwTkvZ6fNFsTjSnAiEA6QznyLLc9EfvT7h7tE0Yvba1taaboK27tRpAgDFD1Vcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDrDCi%2BwFV6M%2BoMWhircAzhBpdCI5gWfrjvb3Y3ACSlUxfGUmvRCe56T7Dai1EW0L3f7yY367eFPOdWpwBOVMpekLMjOiBV6X7m7%2BNsSP%2Bc%2BkDAVrnV%2FEMMBWKS2%2FUHxGadM6DxcX2S2opbKFf8AdVIfEqBbbUeC%2FL8p3G2oRqBtkYokHI43eWHnyavOK57NxrpyWmrbdjd0iLBeq7aL4Im4xO8LVQ%2FeGHgo%2B9eUJTn18X9hNLvTtrWGs6t5egrWSl03LIgBULuLwcEoGGYY%2BoO5TeKuMVeT71QPGxZaaIemcePdKBlnr%2F89fT0qBo92fAmzOpxDWghKt4urehA12ugC3Vp3GA8x7v4WgmA4cevlL1XHBli%2BHQcnZtjULOhZc8wMnaWj4Pvv%2FU3HJFz8xbXP55murzXnpbif0IQWnyDvnyBpDrzeovHtBcMDKaGabrTcVb8O28EWNZEmsxxxpVQrCkg6sLcWmyqQgGSeAHDYoJnloRpZO4VEQXigw8AhhQjuvwwv74alDIh%2FRtclE%2Bk%2FQFyG%2FaajyjwGCc3Nl%2Bb%2FseV57SaKvIALSKV674usWRDjNGse34%2FnL%2FJscCgDT4KOC0myKc975kZg%2BdyWxU3kVeSjpdi4x2jCwd91nkSdkN19Svd7HTujNRChMJmLjb0GOqUBbMCVxh0uLAEnp682uK4GSecRSqM4RehZUPitBnDquPLTxYhUVZqR56ycQgW%2BfCUPIcjXIGikvXjgPKM%2Br3Wsws1jnAjLNyIaF586kJOu%2FCchviqLNmv5NDsATaHaJlm9yi%2BoBpSGrwaR87pyBF2qGQiGCIcKPWP0JbG11%2B95Dv4JsSnahlQ%2BRpp0g27KFjhr4aD10ZHjfs7JSh9YCSyTDIDpE5gb&X-Amz-Signature=5bacb0a27152e7ba4581aaf522b77a363c9b4ab09c4a7ffd885a97ac5760126e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFXSLFC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIADzYI4k9M44%2BcASgwRYugTNMghnPmwTkvZ6fNFsTjSnAiEA6QznyLLc9EfvT7h7tE0Yvba1taaboK27tRpAgDFD1Vcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDrDCi%2BwFV6M%2BoMWhircAzhBpdCI5gWfrjvb3Y3ACSlUxfGUmvRCe56T7Dai1EW0L3f7yY367eFPOdWpwBOVMpekLMjOiBV6X7m7%2BNsSP%2Bc%2BkDAVrnV%2FEMMBWKS2%2FUHxGadM6DxcX2S2opbKFf8AdVIfEqBbbUeC%2FL8p3G2oRqBtkYokHI43eWHnyavOK57NxrpyWmrbdjd0iLBeq7aL4Im4xO8LVQ%2FeGHgo%2B9eUJTn18X9hNLvTtrWGs6t5egrWSl03LIgBULuLwcEoGGYY%2BoO5TeKuMVeT71QPGxZaaIemcePdKBlnr%2F89fT0qBo92fAmzOpxDWghKt4urehA12ugC3Vp3GA8x7v4WgmA4cevlL1XHBli%2BHQcnZtjULOhZc8wMnaWj4Pvv%2FU3HJFz8xbXP55murzXnpbif0IQWnyDvnyBpDrzeovHtBcMDKaGabrTcVb8O28EWNZEmsxxxpVQrCkg6sLcWmyqQgGSeAHDYoJnloRpZO4VEQXigw8AhhQjuvwwv74alDIh%2FRtclE%2Bk%2FQFyG%2FaajyjwGCc3Nl%2Bb%2FseV57SaKvIALSKV674usWRDjNGse34%2FnL%2FJscCgDT4KOC0myKc975kZg%2BdyWxU3kVeSjpdi4x2jCwd91nkSdkN19Svd7HTujNRChMJmLjb0GOqUBbMCVxh0uLAEnp682uK4GSecRSqM4RehZUPitBnDquPLTxYhUVZqR56ycQgW%2BfCUPIcjXIGikvXjgPKM%2Br3Wsws1jnAjLNyIaF586kJOu%2FCchviqLNmv5NDsATaHaJlm9yi%2BoBpSGrwaR87pyBF2qGQiGCIcKPWP0JbG11%2B95Dv4JsSnahlQ%2BRpp0g27KFjhr4aD10ZHjfs7JSh9YCSyTDIDpE5gb&X-Amz-Signature=b10ec8fa6b117f73622aefedc6c1b4706e6ca11fac567c233a37f4de32696b9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCFXSLFC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIADzYI4k9M44%2BcASgwRYugTNMghnPmwTkvZ6fNFsTjSnAiEA6QznyLLc9EfvT7h7tE0Yvba1taaboK27tRpAgDFD1Vcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDrDCi%2BwFV6M%2BoMWhircAzhBpdCI5gWfrjvb3Y3ACSlUxfGUmvRCe56T7Dai1EW0L3f7yY367eFPOdWpwBOVMpekLMjOiBV6X7m7%2BNsSP%2Bc%2BkDAVrnV%2FEMMBWKS2%2FUHxGadM6DxcX2S2opbKFf8AdVIfEqBbbUeC%2FL8p3G2oRqBtkYokHI43eWHnyavOK57NxrpyWmrbdjd0iLBeq7aL4Im4xO8LVQ%2FeGHgo%2B9eUJTn18X9hNLvTtrWGs6t5egrWSl03LIgBULuLwcEoGGYY%2BoO5TeKuMVeT71QPGxZaaIemcePdKBlnr%2F89fT0qBo92fAmzOpxDWghKt4urehA12ugC3Vp3GA8x7v4WgmA4cevlL1XHBli%2BHQcnZtjULOhZc8wMnaWj4Pvv%2FU3HJFz8xbXP55murzXnpbif0IQWnyDvnyBpDrzeovHtBcMDKaGabrTcVb8O28EWNZEmsxxxpVQrCkg6sLcWmyqQgGSeAHDYoJnloRpZO4VEQXigw8AhhQjuvwwv74alDIh%2FRtclE%2Bk%2FQFyG%2FaajyjwGCc3Nl%2Bb%2FseV57SaKvIALSKV674usWRDjNGse34%2FnL%2FJscCgDT4KOC0myKc975kZg%2BdyWxU3kVeSjpdi4x2jCwd91nkSdkN19Svd7HTujNRChMJmLjb0GOqUBbMCVxh0uLAEnp682uK4GSecRSqM4RehZUPitBnDquPLTxYhUVZqR56ycQgW%2BfCUPIcjXIGikvXjgPKM%2Br3Wsws1jnAjLNyIaF586kJOu%2FCchviqLNmv5NDsATaHaJlm9yi%2BoBpSGrwaR87pyBF2qGQiGCIcKPWP0JbG11%2B95Dv4JsSnahlQ%2BRpp0g27KFjhr4aD10ZHjfs7JSh9YCSyTDIDpE5gb&X-Amz-Signature=1a917f4a31383380d47bd4f4222c81e4af1a8d23095929abcde49ad1f627257d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


