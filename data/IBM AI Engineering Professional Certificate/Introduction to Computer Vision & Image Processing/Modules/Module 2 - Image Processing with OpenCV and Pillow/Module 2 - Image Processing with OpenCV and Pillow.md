

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z4G3VAG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBPSOkxEKrxPPpYb0zm9DYvwOi70JWOiIMuoy%2FrLmUOrAiEA2rw7BiLmT7oUZAWk5ih%2BoE1s652x%2F5cKe7%2BQxfP%2Buygq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDArs%2FGrA0aPnqvBXsSrcA%2BCkGNfv%2B3pzIk1V%2FHWt5Sai3Xk4i6DDZ9OUg%2BN6Xtn9mwk1ie1iU6uyRPRyv%2FduMrPrzK1QVGm5IW2E5i48Z4O7pW7RoGzr0oUcPti0XW%2FEEg36kCMdn2aWVctD2MWcr%2BK03lwzp1flipCZX0AHmVlVMedtH0Zxn3CKjVlEgsx5dGlmrARRMLlkrPzx6DJX39muNn28HQQWoRmb9tXTc0g1V4HVa8IXL3ilqSoeUr%2B9mQGKgmK%2Fyd5SVE6BaCvlpAU9g2DO%2F09pzm3OxNVhdyENVKaY2868a0UUcD2Q3V2KvB%2BjCw5ersF6S%2FYtSS1clUKsgg6%2BkdbN3JvjgXUWDbem%2FJ2kVLx9DlaHcpWfOnMD%2FCW8lzKta1F8WWDWdWfrXfU05dw5eTIIm8U3RzJkw674AA1C3aRXTsvKcIULHBdq88umEfrHxn6e9LV%2BAZgvv5ZieCR9OBx2bz1aFsGVm30xa8uxt5muF2pWvP3yaw82PX0OfqDKNbHvKlGPu3tCp8ml6QHC5TwKpal4GprSIvrjqeUQnRd5EQZXGav0mkHvX%2FJusVME3F2cWugVFehbRyX5ioNwYVj%2Bl7N5AaF3e3VxmbiobKBwM1fsJCPlAOh7FKasFoXIcbfwh3QdMPbDkr0GOqUBEKboH8vfTLMDgRWcvWSFXFm7W6p6RUMTjxLl6n6mC%2Bd1hQfToXUF2g2T0cZG6Syd%2FjkT9x%2Baq0sPTCDKqBuWdmZOEFBTWHUVqFF%2B2jlj0pXbZs%2B%2FYeqLMr2o2AGUggZB1tqQIZ3tCjMIjLmGZArmfdxo9r2dWGcuVFJOl2I981AOMZp2zZGtf20fy2IdU4Yf%2F6RRdoM6xKR4cFiIbiAiDTRlhdtL&X-Amz-Signature=b6c48e4c026951a987cae5a5085327e9f1e427f7cd836759bc255fd9302a3e0d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPTYKJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQC0LFPBn%2BRAXRhd3ru5GKLMTxG0bkOZ5LyaQ6kx1YN2GgIgATjEt9GEswBCXX3KpC463jNF8DV9%2FUnaheMATY4ueXQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHEMnCn%2B55mpR7tXXircA209%2BwMxXtoC8gMfZczdm5eLkhXCdHtSF6wnIBj9L2uJFDDhyK4axO1Uqd%2Fu3XEpCliJ80a%2BFYOde9o89yFGyK3igwXSWpyM0XbwNM%2BRaUGt%2BJU7H4EUh6upuDjhhwoeSvwcYTtRM5%2BTzbEvWdmmZw9Z01dJIqEa2TXNrb5CUNU115MqsZ8NzFi%2BlgoxxuMH0WM%2BUgkHHt4iKqjYZT3imKHcLwo2pToCRuTcH6jphqHLO%2FTRJAuk17BoFkpDXrsOCo5Zr2fmDUnCOq0bISHSt1g5xYbE3wUgNPp6WBoCWDE0po6plsuBUUaqubgKt4yWe8x0H6pqO9pgotMu%2Bd45AOy9bcIUkJ66U5oCCN5RjoQw%2F1a%2FCnY84Msup8n71Qh70kdiAm%2B%2FkS5qRLPmKm1GtoHnovicoiTuvgIXXiVIz826acpdyJPCbbPu%2Bf%2Bsrs%2BU2xoaX5yFyNODyWVb69YzFwkyqJWF7q6P73aacVAq0iyg%2FTYAX6uCpJkJ%2Bkj6Nzqy95ekWdd1OIpzeOdltWtM%2BH5Aa7nLkdkoFtRFjIfBltTk55OUABGtcOrJviSbCkEp6tF56rU5gjlDGFHtzQndZ8XpnpmrJ2SP6vKBSzldZS7jSzi2k7ACTuNdauFcMNnDkr0GOqUB%2FRMUDtRQ8XZw0Bft%2B3PfEd83zyWBgxOfYe4IketzQC%2Bvxpxv912a3DNvQ0xQbcQmjNgrfNxdHUt4zibLeAZWCIQ40Kpl3AHsl2nNBzqKzHo4qBSh%2FA3XJE1g2%2FBwQ2sV42OlXsbo6lfZo0wiVZcGtxppa3izDA0zrnxbIFAXwbd1wxx8zMhlxtXnkufhtuc%2BzrBfU02k3OAVxNbhkl%2BFxnVFUiVj&X-Amz-Signature=fc7de23ad4ec5b0defee948e1b65bb40375510f25726e8f908e961e5cd62e920&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPTYKJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQC0LFPBn%2BRAXRhd3ru5GKLMTxG0bkOZ5LyaQ6kx1YN2GgIgATjEt9GEswBCXX3KpC463jNF8DV9%2FUnaheMATY4ueXQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHEMnCn%2B55mpR7tXXircA209%2BwMxXtoC8gMfZczdm5eLkhXCdHtSF6wnIBj9L2uJFDDhyK4axO1Uqd%2Fu3XEpCliJ80a%2BFYOde9o89yFGyK3igwXSWpyM0XbwNM%2BRaUGt%2BJU7H4EUh6upuDjhhwoeSvwcYTtRM5%2BTzbEvWdmmZw9Z01dJIqEa2TXNrb5CUNU115MqsZ8NzFi%2BlgoxxuMH0WM%2BUgkHHt4iKqjYZT3imKHcLwo2pToCRuTcH6jphqHLO%2FTRJAuk17BoFkpDXrsOCo5Zr2fmDUnCOq0bISHSt1g5xYbE3wUgNPp6WBoCWDE0po6plsuBUUaqubgKt4yWe8x0H6pqO9pgotMu%2Bd45AOy9bcIUkJ66U5oCCN5RjoQw%2F1a%2FCnY84Msup8n71Qh70kdiAm%2B%2FkS5qRLPmKm1GtoHnovicoiTuvgIXXiVIz826acpdyJPCbbPu%2Bf%2Bsrs%2BU2xoaX5yFyNODyWVb69YzFwkyqJWF7q6P73aacVAq0iyg%2FTYAX6uCpJkJ%2Bkj6Nzqy95ekWdd1OIpzeOdltWtM%2BH5Aa7nLkdkoFtRFjIfBltTk55OUABGtcOrJviSbCkEp6tF56rU5gjlDGFHtzQndZ8XpnpmrJ2SP6vKBSzldZS7jSzi2k7ACTuNdauFcMNnDkr0GOqUB%2FRMUDtRQ8XZw0Bft%2B3PfEd83zyWBgxOfYe4IketzQC%2Bvxpxv912a3DNvQ0xQbcQmjNgrfNxdHUt4zibLeAZWCIQ40Kpl3AHsl2nNBzqKzHo4qBSh%2FA3XJE1g2%2FBwQ2sV42OlXsbo6lfZo0wiVZcGtxppa3izDA0zrnxbIFAXwbd1wxx8zMhlxtXnkufhtuc%2BzrBfU02k3OAVxNbhkl%2BFxnVFUiVj&X-Amz-Signature=98a5618a1172ba5858e5adf4d09440124f8c5dbe1b3b5e7c95610ec824efadf0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPTYKJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQC0LFPBn%2BRAXRhd3ru5GKLMTxG0bkOZ5LyaQ6kx1YN2GgIgATjEt9GEswBCXX3KpC463jNF8DV9%2FUnaheMATY4ueXQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHEMnCn%2B55mpR7tXXircA209%2BwMxXtoC8gMfZczdm5eLkhXCdHtSF6wnIBj9L2uJFDDhyK4axO1Uqd%2Fu3XEpCliJ80a%2BFYOde9o89yFGyK3igwXSWpyM0XbwNM%2BRaUGt%2BJU7H4EUh6upuDjhhwoeSvwcYTtRM5%2BTzbEvWdmmZw9Z01dJIqEa2TXNrb5CUNU115MqsZ8NzFi%2BlgoxxuMH0WM%2BUgkHHt4iKqjYZT3imKHcLwo2pToCRuTcH6jphqHLO%2FTRJAuk17BoFkpDXrsOCo5Zr2fmDUnCOq0bISHSt1g5xYbE3wUgNPp6WBoCWDE0po6plsuBUUaqubgKt4yWe8x0H6pqO9pgotMu%2Bd45AOy9bcIUkJ66U5oCCN5RjoQw%2F1a%2FCnY84Msup8n71Qh70kdiAm%2B%2FkS5qRLPmKm1GtoHnovicoiTuvgIXXiVIz826acpdyJPCbbPu%2Bf%2Bsrs%2BU2xoaX5yFyNODyWVb69YzFwkyqJWF7q6P73aacVAq0iyg%2FTYAX6uCpJkJ%2Bkj6Nzqy95ekWdd1OIpzeOdltWtM%2BH5Aa7nLkdkoFtRFjIfBltTk55OUABGtcOrJviSbCkEp6tF56rU5gjlDGFHtzQndZ8XpnpmrJ2SP6vKBSzldZS7jSzi2k7ACTuNdauFcMNnDkr0GOqUB%2FRMUDtRQ8XZw0Bft%2B3PfEd83zyWBgxOfYe4IketzQC%2Bvxpxv912a3DNvQ0xQbcQmjNgrfNxdHUt4zibLeAZWCIQ40Kpl3AHsl2nNBzqKzHo4qBSh%2FA3XJE1g2%2FBwQ2sV42OlXsbo6lfZo0wiVZcGtxppa3izDA0zrnxbIFAXwbd1wxx8zMhlxtXnkufhtuc%2BzrBfU02k3OAVxNbhkl%2BFxnVFUiVj&X-Amz-Signature=d633af97a5fe0bee7da46ef42e4dc6b5a22ad332d09375cf51567fe1aa8f6d6b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPTYKJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQC0LFPBn%2BRAXRhd3ru5GKLMTxG0bkOZ5LyaQ6kx1YN2GgIgATjEt9GEswBCXX3KpC463jNF8DV9%2FUnaheMATY4ueXQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHEMnCn%2B55mpR7tXXircA209%2BwMxXtoC8gMfZczdm5eLkhXCdHtSF6wnIBj9L2uJFDDhyK4axO1Uqd%2Fu3XEpCliJ80a%2BFYOde9o89yFGyK3igwXSWpyM0XbwNM%2BRaUGt%2BJU7H4EUh6upuDjhhwoeSvwcYTtRM5%2BTzbEvWdmmZw9Z01dJIqEa2TXNrb5CUNU115MqsZ8NzFi%2BlgoxxuMH0WM%2BUgkHHt4iKqjYZT3imKHcLwo2pToCRuTcH6jphqHLO%2FTRJAuk17BoFkpDXrsOCo5Zr2fmDUnCOq0bISHSt1g5xYbE3wUgNPp6WBoCWDE0po6plsuBUUaqubgKt4yWe8x0H6pqO9pgotMu%2Bd45AOy9bcIUkJ66U5oCCN5RjoQw%2F1a%2FCnY84Msup8n71Qh70kdiAm%2B%2FkS5qRLPmKm1GtoHnovicoiTuvgIXXiVIz826acpdyJPCbbPu%2Bf%2Bsrs%2BU2xoaX5yFyNODyWVb69YzFwkyqJWF7q6P73aacVAq0iyg%2FTYAX6uCpJkJ%2Bkj6Nzqy95ekWdd1OIpzeOdltWtM%2BH5Aa7nLkdkoFtRFjIfBltTk55OUABGtcOrJviSbCkEp6tF56rU5gjlDGFHtzQndZ8XpnpmrJ2SP6vKBSzldZS7jSzi2k7ACTuNdauFcMNnDkr0GOqUB%2FRMUDtRQ8XZw0Bft%2B3PfEd83zyWBgxOfYe4IketzQC%2Bvxpxv912a3DNvQ0xQbcQmjNgrfNxdHUt4zibLeAZWCIQ40Kpl3AHsl2nNBzqKzHo4qBSh%2FA3XJE1g2%2FBwQ2sV42OlXsbo6lfZo0wiVZcGtxppa3izDA0zrnxbIFAXwbd1wxx8zMhlxtXnkufhtuc%2BzrBfU02k3OAVxNbhkl%2BFxnVFUiVj&X-Amz-Signature=a3f122f498caf774fca501837d7363d2b924322d9dee371718ec4c0741e3056a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPTYKJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQC0LFPBn%2BRAXRhd3ru5GKLMTxG0bkOZ5LyaQ6kx1YN2GgIgATjEt9GEswBCXX3KpC463jNF8DV9%2FUnaheMATY4ueXQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHEMnCn%2B55mpR7tXXircA209%2BwMxXtoC8gMfZczdm5eLkhXCdHtSF6wnIBj9L2uJFDDhyK4axO1Uqd%2Fu3XEpCliJ80a%2BFYOde9o89yFGyK3igwXSWpyM0XbwNM%2BRaUGt%2BJU7H4EUh6upuDjhhwoeSvwcYTtRM5%2BTzbEvWdmmZw9Z01dJIqEa2TXNrb5CUNU115MqsZ8NzFi%2BlgoxxuMH0WM%2BUgkHHt4iKqjYZT3imKHcLwo2pToCRuTcH6jphqHLO%2FTRJAuk17BoFkpDXrsOCo5Zr2fmDUnCOq0bISHSt1g5xYbE3wUgNPp6WBoCWDE0po6plsuBUUaqubgKt4yWe8x0H6pqO9pgotMu%2Bd45AOy9bcIUkJ66U5oCCN5RjoQw%2F1a%2FCnY84Msup8n71Qh70kdiAm%2B%2FkS5qRLPmKm1GtoHnovicoiTuvgIXXiVIz826acpdyJPCbbPu%2Bf%2Bsrs%2BU2xoaX5yFyNODyWVb69YzFwkyqJWF7q6P73aacVAq0iyg%2FTYAX6uCpJkJ%2Bkj6Nzqy95ekWdd1OIpzeOdltWtM%2BH5Aa7nLkdkoFtRFjIfBltTk55OUABGtcOrJviSbCkEp6tF56rU5gjlDGFHtzQndZ8XpnpmrJ2SP6vKBSzldZS7jSzi2k7ACTuNdauFcMNnDkr0GOqUB%2FRMUDtRQ8XZw0Bft%2B3PfEd83zyWBgxOfYe4IketzQC%2Bvxpxv912a3DNvQ0xQbcQmjNgrfNxdHUt4zibLeAZWCIQ40Kpl3AHsl2nNBzqKzHo4qBSh%2FA3XJE1g2%2FBwQ2sV42OlXsbo6lfZo0wiVZcGtxppa3izDA0zrnxbIFAXwbd1wxx8zMhlxtXnkufhtuc%2BzrBfU02k3OAVxNbhkl%2BFxnVFUiVj&X-Amz-Signature=c3b8b7777ea12133c02883b1fc67c155d91af66d05263ec514e794fc515f2648&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z4G3VAG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBPSOkxEKrxPPpYb0zm9DYvwOi70JWOiIMuoy%2FrLmUOrAiEA2rw7BiLmT7oUZAWk5ih%2BoE1s652x%2F5cKe7%2BQxfP%2Buygq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDArs%2FGrA0aPnqvBXsSrcA%2BCkGNfv%2B3pzIk1V%2FHWt5Sai3Xk4i6DDZ9OUg%2BN6Xtn9mwk1ie1iU6uyRPRyv%2FduMrPrzK1QVGm5IW2E5i48Z4O7pW7RoGzr0oUcPti0XW%2FEEg36kCMdn2aWVctD2MWcr%2BK03lwzp1flipCZX0AHmVlVMedtH0Zxn3CKjVlEgsx5dGlmrARRMLlkrPzx6DJX39muNn28HQQWoRmb9tXTc0g1V4HVa8IXL3ilqSoeUr%2B9mQGKgmK%2Fyd5SVE6BaCvlpAU9g2DO%2F09pzm3OxNVhdyENVKaY2868a0UUcD2Q3V2KvB%2BjCw5ersF6S%2FYtSS1clUKsgg6%2BkdbN3JvjgXUWDbem%2FJ2kVLx9DlaHcpWfOnMD%2FCW8lzKta1F8WWDWdWfrXfU05dw5eTIIm8U3RzJkw674AA1C3aRXTsvKcIULHBdq88umEfrHxn6e9LV%2BAZgvv5ZieCR9OBx2bz1aFsGVm30xa8uxt5muF2pWvP3yaw82PX0OfqDKNbHvKlGPu3tCp8ml6QHC5TwKpal4GprSIvrjqeUQnRd5EQZXGav0mkHvX%2FJusVME3F2cWugVFehbRyX5ioNwYVj%2Bl7N5AaF3e3VxmbiobKBwM1fsJCPlAOh7FKasFoXIcbfwh3QdMPbDkr0GOqUBEKboH8vfTLMDgRWcvWSFXFm7W6p6RUMTjxLl6n6mC%2Bd1hQfToXUF2g2T0cZG6Syd%2FjkT9x%2Baq0sPTCDKqBuWdmZOEFBTWHUVqFF%2B2jlj0pXbZs%2B%2FYeqLMr2o2AGUggZB1tqQIZ3tCjMIjLmGZArmfdxo9r2dWGcuVFJOl2I981AOMZp2zZGtf20fy2IdU4Yf%2F6RRdoM6xKR4cFiIbiAiDTRlhdtL&X-Amz-Signature=97ec253fe71b0e7983594c39ba319e6ca05e8d67116ef788603c5bb2cb484b09&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z4G3VAG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBPSOkxEKrxPPpYb0zm9DYvwOi70JWOiIMuoy%2FrLmUOrAiEA2rw7BiLmT7oUZAWk5ih%2BoE1s652x%2F5cKe7%2BQxfP%2Buygq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDArs%2FGrA0aPnqvBXsSrcA%2BCkGNfv%2B3pzIk1V%2FHWt5Sai3Xk4i6DDZ9OUg%2BN6Xtn9mwk1ie1iU6uyRPRyv%2FduMrPrzK1QVGm5IW2E5i48Z4O7pW7RoGzr0oUcPti0XW%2FEEg36kCMdn2aWVctD2MWcr%2BK03lwzp1flipCZX0AHmVlVMedtH0Zxn3CKjVlEgsx5dGlmrARRMLlkrPzx6DJX39muNn28HQQWoRmb9tXTc0g1V4HVa8IXL3ilqSoeUr%2B9mQGKgmK%2Fyd5SVE6BaCvlpAU9g2DO%2F09pzm3OxNVhdyENVKaY2868a0UUcD2Q3V2KvB%2BjCw5ersF6S%2FYtSS1clUKsgg6%2BkdbN3JvjgXUWDbem%2FJ2kVLx9DlaHcpWfOnMD%2FCW8lzKta1F8WWDWdWfrXfU05dw5eTIIm8U3RzJkw674AA1C3aRXTsvKcIULHBdq88umEfrHxn6e9LV%2BAZgvv5ZieCR9OBx2bz1aFsGVm30xa8uxt5muF2pWvP3yaw82PX0OfqDKNbHvKlGPu3tCp8ml6QHC5TwKpal4GprSIvrjqeUQnRd5EQZXGav0mkHvX%2FJusVME3F2cWugVFehbRyX5ioNwYVj%2Bl7N5AaF3e3VxmbiobKBwM1fsJCPlAOh7FKasFoXIcbfwh3QdMPbDkr0GOqUBEKboH8vfTLMDgRWcvWSFXFm7W6p6RUMTjxLl6n6mC%2Bd1hQfToXUF2g2T0cZG6Syd%2FjkT9x%2Baq0sPTCDKqBuWdmZOEFBTWHUVqFF%2B2jlj0pXbZs%2B%2FYeqLMr2o2AGUggZB1tqQIZ3tCjMIjLmGZArmfdxo9r2dWGcuVFJOl2I981AOMZp2zZGtf20fy2IdU4Yf%2F6RRdoM6xKR4cFiIbiAiDTRlhdtL&X-Amz-Signature=c7ec0c209ebec843ccb261b71b23dcc21a1e92c0ed657bfa2081c12544517c66&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z4G3VAG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBPSOkxEKrxPPpYb0zm9DYvwOi70JWOiIMuoy%2FrLmUOrAiEA2rw7BiLmT7oUZAWk5ih%2BoE1s652x%2F5cKe7%2BQxfP%2Buygq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDArs%2FGrA0aPnqvBXsSrcA%2BCkGNfv%2B3pzIk1V%2FHWt5Sai3Xk4i6DDZ9OUg%2BN6Xtn9mwk1ie1iU6uyRPRyv%2FduMrPrzK1QVGm5IW2E5i48Z4O7pW7RoGzr0oUcPti0XW%2FEEg36kCMdn2aWVctD2MWcr%2BK03lwzp1flipCZX0AHmVlVMedtH0Zxn3CKjVlEgsx5dGlmrARRMLlkrPzx6DJX39muNn28HQQWoRmb9tXTc0g1V4HVa8IXL3ilqSoeUr%2B9mQGKgmK%2Fyd5SVE6BaCvlpAU9g2DO%2F09pzm3OxNVhdyENVKaY2868a0UUcD2Q3V2KvB%2BjCw5ersF6S%2FYtSS1clUKsgg6%2BkdbN3JvjgXUWDbem%2FJ2kVLx9DlaHcpWfOnMD%2FCW8lzKta1F8WWDWdWfrXfU05dw5eTIIm8U3RzJkw674AA1C3aRXTsvKcIULHBdq88umEfrHxn6e9LV%2BAZgvv5ZieCR9OBx2bz1aFsGVm30xa8uxt5muF2pWvP3yaw82PX0OfqDKNbHvKlGPu3tCp8ml6QHC5TwKpal4GprSIvrjqeUQnRd5EQZXGav0mkHvX%2FJusVME3F2cWugVFehbRyX5ioNwYVj%2Bl7N5AaF3e3VxmbiobKBwM1fsJCPlAOh7FKasFoXIcbfwh3QdMPbDkr0GOqUBEKboH8vfTLMDgRWcvWSFXFm7W6p6RUMTjxLl6n6mC%2Bd1hQfToXUF2g2T0cZG6Syd%2FjkT9x%2Baq0sPTCDKqBuWdmZOEFBTWHUVqFF%2B2jlj0pXbZs%2B%2FYeqLMr2o2AGUggZB1tqQIZ3tCjMIjLmGZArmfdxo9r2dWGcuVFJOl2I981AOMZp2zZGtf20fy2IdU4Yf%2F6RRdoM6xKR4cFiIbiAiDTRlhdtL&X-Amz-Signature=a3b71bc04ed33a40a66736252df52ea286be4d1dff87fa5395dba2edeb350486&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z4G3VAG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBPSOkxEKrxPPpYb0zm9DYvwOi70JWOiIMuoy%2FrLmUOrAiEA2rw7BiLmT7oUZAWk5ih%2BoE1s652x%2F5cKe7%2BQxfP%2Buygq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDArs%2FGrA0aPnqvBXsSrcA%2BCkGNfv%2B3pzIk1V%2FHWt5Sai3Xk4i6DDZ9OUg%2BN6Xtn9mwk1ie1iU6uyRPRyv%2FduMrPrzK1QVGm5IW2E5i48Z4O7pW7RoGzr0oUcPti0XW%2FEEg36kCMdn2aWVctD2MWcr%2BK03lwzp1flipCZX0AHmVlVMedtH0Zxn3CKjVlEgsx5dGlmrARRMLlkrPzx6DJX39muNn28HQQWoRmb9tXTc0g1V4HVa8IXL3ilqSoeUr%2B9mQGKgmK%2Fyd5SVE6BaCvlpAU9g2DO%2F09pzm3OxNVhdyENVKaY2868a0UUcD2Q3V2KvB%2BjCw5ersF6S%2FYtSS1clUKsgg6%2BkdbN3JvjgXUWDbem%2FJ2kVLx9DlaHcpWfOnMD%2FCW8lzKta1F8WWDWdWfrXfU05dw5eTIIm8U3RzJkw674AA1C3aRXTsvKcIULHBdq88umEfrHxn6e9LV%2BAZgvv5ZieCR9OBx2bz1aFsGVm30xa8uxt5muF2pWvP3yaw82PX0OfqDKNbHvKlGPu3tCp8ml6QHC5TwKpal4GprSIvrjqeUQnRd5EQZXGav0mkHvX%2FJusVME3F2cWugVFehbRyX5ioNwYVj%2Bl7N5AaF3e3VxmbiobKBwM1fsJCPlAOh7FKasFoXIcbfwh3QdMPbDkr0GOqUBEKboH8vfTLMDgRWcvWSFXFm7W6p6RUMTjxLl6n6mC%2Bd1hQfToXUF2g2T0cZG6Syd%2FjkT9x%2Baq0sPTCDKqBuWdmZOEFBTWHUVqFF%2B2jlj0pXbZs%2B%2FYeqLMr2o2AGUggZB1tqQIZ3tCjMIjLmGZArmfdxo9r2dWGcuVFJOl2I981AOMZp2zZGtf20fy2IdU4Yf%2F6RRdoM6xKR4cFiIbiAiDTRlhdtL&X-Amz-Signature=ccbfff9ee1dedd8b2514b51ad960d8e9fce2f4a7c0eaa670e7043f9b840c81ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z4G3VAG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIBPSOkxEKrxPPpYb0zm9DYvwOi70JWOiIMuoy%2FrLmUOrAiEA2rw7BiLmT7oUZAWk5ih%2BoE1s652x%2F5cKe7%2BQxfP%2Buygq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDArs%2FGrA0aPnqvBXsSrcA%2BCkGNfv%2B3pzIk1V%2FHWt5Sai3Xk4i6DDZ9OUg%2BN6Xtn9mwk1ie1iU6uyRPRyv%2FduMrPrzK1QVGm5IW2E5i48Z4O7pW7RoGzr0oUcPti0XW%2FEEg36kCMdn2aWVctD2MWcr%2BK03lwzp1flipCZX0AHmVlVMedtH0Zxn3CKjVlEgsx5dGlmrARRMLlkrPzx6DJX39muNn28HQQWoRmb9tXTc0g1V4HVa8IXL3ilqSoeUr%2B9mQGKgmK%2Fyd5SVE6BaCvlpAU9g2DO%2F09pzm3OxNVhdyENVKaY2868a0UUcD2Q3V2KvB%2BjCw5ersF6S%2FYtSS1clUKsgg6%2BkdbN3JvjgXUWDbem%2FJ2kVLx9DlaHcpWfOnMD%2FCW8lzKta1F8WWDWdWfrXfU05dw5eTIIm8U3RzJkw674AA1C3aRXTsvKcIULHBdq88umEfrHxn6e9LV%2BAZgvv5ZieCR9OBx2bz1aFsGVm30xa8uxt5muF2pWvP3yaw82PX0OfqDKNbHvKlGPu3tCp8ml6QHC5TwKpal4GprSIvrjqeUQnRd5EQZXGav0mkHvX%2FJusVME3F2cWugVFehbRyX5ioNwYVj%2Bl7N5AaF3e3VxmbiobKBwM1fsJCPlAOh7FKasFoXIcbfwh3QdMPbDkr0GOqUBEKboH8vfTLMDgRWcvWSFXFm7W6p6RUMTjxLl6n6mC%2Bd1hQfToXUF2g2T0cZG6Syd%2FjkT9x%2Baq0sPTCDKqBuWdmZOEFBTWHUVqFF%2B2jlj0pXbZs%2B%2FYeqLMr2o2AGUggZB1tqQIZ3tCjMIjLmGZArmfdxo9r2dWGcuVFJOl2I981AOMZp2zZGtf20fy2IdU4Yf%2F6RRdoM6xKR4cFiIbiAiDTRlhdtL&X-Amz-Signature=3d6105eb33ff716da1ad532ed5ef4e14adb36d68d445e0715ca2a2ab2c44200e&X-Amz-SignedHeaders=host&x-id=GetObject)
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


