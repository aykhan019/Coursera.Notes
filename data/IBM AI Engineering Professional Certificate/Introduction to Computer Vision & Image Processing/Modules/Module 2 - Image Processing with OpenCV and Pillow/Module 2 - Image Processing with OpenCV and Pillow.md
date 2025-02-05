

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6OBPUAM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCi%2BzAiJwF0YVUX9zs0Mc%2BOZm4bCd9g6XvwrCvpn%2F85GQIgFklFgdkSG3ntSC63w0euHiErI8K2qP5dc5BR8TNpRGgq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDOomRdwJBdo%2BWgEHECrcA0FznwFwf6ZeM4toCTspORipDZOMxxCSvqP%2FahyKlYXmwwPitvV31Ub%2B2gmd6NlJCgQt%2B9g9b%2FqxKbDpuXqkd7yM%2B6IsOmFU95AZ%2B23%2BZx8Ux1hFky5T7fuL3eqP9ERCzQcbK3WL2cksX7ZF3AnP90%2BajkFL121%2BuGaMCn%2BnqnCruA6fOPZL36FTFVGzHafwmy9yC%2BlPj4DznkLeA3JLX24Wr0Dj8zEWwMJkwsj0B0%2Fl%2BYI%2BIDTg0xoDz0ldea1l7p0N7jU18S4Aat6q%2FXBDhegdjDhHvlayCjrLUIEvgalm0hIrBLrpMVkuoU9icsS69JRVuimbptPCgmYWfnWK0BlunQs2nqJ44kUNu9gigF3keAauDeOV8tLJd6Z1gB%2FX%2F0uO0OKlHTr9RVZLHX%2F9dCMvTDtRpLcnt2%2BpAyRByPioGPs5kNgKGW8uA3o6YbU2bYwx02xwFkIY9AsFXfiZPSSApk27CmNt6KgC%2BJ%2Byke6PELLkMoT%2F7mJx3EgHka8PuisOJn4BPHzOqTkeML6PzrsMX3EeDGeQJO6nZzYKSBwLdKFODF1iwHrMzlGFZIUXqDYAOtyHKQtyAfpdDUZFloaRsGLEaUZSkXNR3dmeZy0gxPQQXqncN6XjEyaOMJizjL0GOqUBlclFLv3kkb%2BEPJ%2B7JEvD75rZGE93iHoIIO0QsZRo4e6gua52%2FR0t0Yvg%2B6i6wUaga%2FqgvLAek7BKyjcXKijGgKHkKFH4nXtJ6aLyaSPcUgpRa2dqZ6l%2FyXFPBKJ%2FUwXXYIhQtE7%2BKfNbePp8VvbRKw1IQjsz2vZx3UWB%2BYKvMx3X2S7KIj6PVHb7M0yCT9InSsI1%2BPGdeOhyvkeCqvkAR0qqTPKa&X-Amz-Signature=c196405059d0b204b5899c06c97d33ca637c375be9cd8c6cb105adc96e941bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGVQN4P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFVv0s0WYe4yp4%2FuhXXQMFj%2FONM824yIFF179VxI2XebAiEA9MLef71vH%2BFH6dATtbFVYo7averLxfhKuD4338J8rX0q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLb1DNdXSKwIZwVuXyrcA6ynFXc296ioTLMKNcU4WQuF58JHoryUhMvHNiGA%2FDWj9MPDfLRop%2Ba%2Bi1R4cyRm9kbZyVAO56dFJJVrkt%2FQifVjgppzhhI9tAcU1IUzjyNP5GaJduq1AqHFmg%2F8BvtoOY6%2FfgsbSxjSgjJBJuOsJlUrlksb4K4wk5WpCZTXjn2C0h%2B8ldGo76Vzj70Y9zP9I%2Ba9M1zlE2Fizw5%2BSeTcG2wv6BaZ7HZWgdOPgRiV%2BbPNAmfihJeGgNqEf8%2B4i9iIspD07JcDBZz8Z7AdjTrASRft1ywTK25HCqdRkj2m9Q%2BXSj5Vxz141stlz0HIAaa2qudMV4MxwROChsoTIPBRsn3Hgp8eTFUg5frf1uQvI8lUMC%2BE%2Bb5TuNppHgDE8IQz7ls403hgJksYXa%2FQMjA01SF%2BjIUoqkLdkIlCl8Pd1VYw8EPWztzYaeatOOP2rfOolabpKAFeiyovYgTeOOy29ylB8ABrsRYbnM5HXQZ6v9tRBFch0meeZGuearIW6XoO3%2Bkv9u8n4VWUJGB2Mj%2FB56ayd%2B1jYhUGFAu8V8A85N%2BLBIHHsvD8wWVyisUKrjG3Wy4TrKxm6pW67FDSfGLIBgjZfirypOs7t8rVamdMlVxlBeCfawID9WW2EwnwMJmzjL0GOqUBm%2FqVH3TPAVta333CrGtfHh8mpsaH3pTG7v5yE1nESgNoJkH48FD3nGnq%2Bg0sCzXdd%2Fi9P92EhGfane7%2Fc1hLv%2B9%2BoZ5%2BHhJ6%2FbWyKpwGLh7wAcynZ4LAFwi%2Bof6yAp%2BeAiTebBUfBZ7iaehfUowRKPuN2VqToc8UpiFH7%2FMMYcf5IzrqmVfgObi78X8m00ULvZrMmu4fy%2Bmq%2FChL9Rl89jJ9b8c9&X-Amz-Signature=4ed244e1da1d4390cbdb81355f948d6fe193045956b180fcfd2c6c4220083f7c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGVQN4P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFVv0s0WYe4yp4%2FuhXXQMFj%2FONM824yIFF179VxI2XebAiEA9MLef71vH%2BFH6dATtbFVYo7averLxfhKuD4338J8rX0q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLb1DNdXSKwIZwVuXyrcA6ynFXc296ioTLMKNcU4WQuF58JHoryUhMvHNiGA%2FDWj9MPDfLRop%2Ba%2Bi1R4cyRm9kbZyVAO56dFJJVrkt%2FQifVjgppzhhI9tAcU1IUzjyNP5GaJduq1AqHFmg%2F8BvtoOY6%2FfgsbSxjSgjJBJuOsJlUrlksb4K4wk5WpCZTXjn2C0h%2B8ldGo76Vzj70Y9zP9I%2Ba9M1zlE2Fizw5%2BSeTcG2wv6BaZ7HZWgdOPgRiV%2BbPNAmfihJeGgNqEf8%2B4i9iIspD07JcDBZz8Z7AdjTrASRft1ywTK25HCqdRkj2m9Q%2BXSj5Vxz141stlz0HIAaa2qudMV4MxwROChsoTIPBRsn3Hgp8eTFUg5frf1uQvI8lUMC%2BE%2Bb5TuNppHgDE8IQz7ls403hgJksYXa%2FQMjA01SF%2BjIUoqkLdkIlCl8Pd1VYw8EPWztzYaeatOOP2rfOolabpKAFeiyovYgTeOOy29ylB8ABrsRYbnM5HXQZ6v9tRBFch0meeZGuearIW6XoO3%2Bkv9u8n4VWUJGB2Mj%2FB56ayd%2B1jYhUGFAu8V8A85N%2BLBIHHsvD8wWVyisUKrjG3Wy4TrKxm6pW67FDSfGLIBgjZfirypOs7t8rVamdMlVxlBeCfawID9WW2EwnwMJmzjL0GOqUBm%2FqVH3TPAVta333CrGtfHh8mpsaH3pTG7v5yE1nESgNoJkH48FD3nGnq%2Bg0sCzXdd%2Fi9P92EhGfane7%2Fc1hLv%2B9%2BoZ5%2BHhJ6%2FbWyKpwGLh7wAcynZ4LAFwi%2Bof6yAp%2BeAiTebBUfBZ7iaehfUowRKPuN2VqToc8UpiFH7%2FMMYcf5IzrqmVfgObi78X8m00ULvZrMmu4fy%2Bmq%2FChL9Rl89jJ9b8c9&X-Amz-Signature=9022088a43ceb3a42d783af9d05b084c5dde9b796da44fe8a1ad7fd987fc4054&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGVQN4P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFVv0s0WYe4yp4%2FuhXXQMFj%2FONM824yIFF179VxI2XebAiEA9MLef71vH%2BFH6dATtbFVYo7averLxfhKuD4338J8rX0q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLb1DNdXSKwIZwVuXyrcA6ynFXc296ioTLMKNcU4WQuF58JHoryUhMvHNiGA%2FDWj9MPDfLRop%2Ba%2Bi1R4cyRm9kbZyVAO56dFJJVrkt%2FQifVjgppzhhI9tAcU1IUzjyNP5GaJduq1AqHFmg%2F8BvtoOY6%2FfgsbSxjSgjJBJuOsJlUrlksb4K4wk5WpCZTXjn2C0h%2B8ldGo76Vzj70Y9zP9I%2Ba9M1zlE2Fizw5%2BSeTcG2wv6BaZ7HZWgdOPgRiV%2BbPNAmfihJeGgNqEf8%2B4i9iIspD07JcDBZz8Z7AdjTrASRft1ywTK25HCqdRkj2m9Q%2BXSj5Vxz141stlz0HIAaa2qudMV4MxwROChsoTIPBRsn3Hgp8eTFUg5frf1uQvI8lUMC%2BE%2Bb5TuNppHgDE8IQz7ls403hgJksYXa%2FQMjA01SF%2BjIUoqkLdkIlCl8Pd1VYw8EPWztzYaeatOOP2rfOolabpKAFeiyovYgTeOOy29ylB8ABrsRYbnM5HXQZ6v9tRBFch0meeZGuearIW6XoO3%2Bkv9u8n4VWUJGB2Mj%2FB56ayd%2B1jYhUGFAu8V8A85N%2BLBIHHsvD8wWVyisUKrjG3Wy4TrKxm6pW67FDSfGLIBgjZfirypOs7t8rVamdMlVxlBeCfawID9WW2EwnwMJmzjL0GOqUBm%2FqVH3TPAVta333CrGtfHh8mpsaH3pTG7v5yE1nESgNoJkH48FD3nGnq%2Bg0sCzXdd%2Fi9P92EhGfane7%2Fc1hLv%2B9%2BoZ5%2BHhJ6%2FbWyKpwGLh7wAcynZ4LAFwi%2Bof6yAp%2BeAiTebBUfBZ7iaehfUowRKPuN2VqToc8UpiFH7%2FMMYcf5IzrqmVfgObi78X8m00ULvZrMmu4fy%2Bmq%2FChL9Rl89jJ9b8c9&X-Amz-Signature=4086d284332c1c2b72c5701e58024f496aad52ef730b74f188472674e952bea7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGVQN4P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFVv0s0WYe4yp4%2FuhXXQMFj%2FONM824yIFF179VxI2XebAiEA9MLef71vH%2BFH6dATtbFVYo7averLxfhKuD4338J8rX0q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLb1DNdXSKwIZwVuXyrcA6ynFXc296ioTLMKNcU4WQuF58JHoryUhMvHNiGA%2FDWj9MPDfLRop%2Ba%2Bi1R4cyRm9kbZyVAO56dFJJVrkt%2FQifVjgppzhhI9tAcU1IUzjyNP5GaJduq1AqHFmg%2F8BvtoOY6%2FfgsbSxjSgjJBJuOsJlUrlksb4K4wk5WpCZTXjn2C0h%2B8ldGo76Vzj70Y9zP9I%2Ba9M1zlE2Fizw5%2BSeTcG2wv6BaZ7HZWgdOPgRiV%2BbPNAmfihJeGgNqEf8%2B4i9iIspD07JcDBZz8Z7AdjTrASRft1ywTK25HCqdRkj2m9Q%2BXSj5Vxz141stlz0HIAaa2qudMV4MxwROChsoTIPBRsn3Hgp8eTFUg5frf1uQvI8lUMC%2BE%2Bb5TuNppHgDE8IQz7ls403hgJksYXa%2FQMjA01SF%2BjIUoqkLdkIlCl8Pd1VYw8EPWztzYaeatOOP2rfOolabpKAFeiyovYgTeOOy29ylB8ABrsRYbnM5HXQZ6v9tRBFch0meeZGuearIW6XoO3%2Bkv9u8n4VWUJGB2Mj%2FB56ayd%2B1jYhUGFAu8V8A85N%2BLBIHHsvD8wWVyisUKrjG3Wy4TrKxm6pW67FDSfGLIBgjZfirypOs7t8rVamdMlVxlBeCfawID9WW2EwnwMJmzjL0GOqUBm%2FqVH3TPAVta333CrGtfHh8mpsaH3pTG7v5yE1nESgNoJkH48FD3nGnq%2Bg0sCzXdd%2Fi9P92EhGfane7%2Fc1hLv%2B9%2BoZ5%2BHhJ6%2FbWyKpwGLh7wAcynZ4LAFwi%2Bof6yAp%2BeAiTebBUfBZ7iaehfUowRKPuN2VqToc8UpiFH7%2FMMYcf5IzrqmVfgObi78X8m00ULvZrMmu4fy%2Bmq%2FChL9Rl89jJ9b8c9&X-Amz-Signature=d616664512352f9bb7d080996b29915cfe8c0cf9f5262bf01b6b9bf069be5062&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGVQN4P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFVv0s0WYe4yp4%2FuhXXQMFj%2FONM824yIFF179VxI2XebAiEA9MLef71vH%2BFH6dATtbFVYo7averLxfhKuD4338J8rX0q%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDLb1DNdXSKwIZwVuXyrcA6ynFXc296ioTLMKNcU4WQuF58JHoryUhMvHNiGA%2FDWj9MPDfLRop%2Ba%2Bi1R4cyRm9kbZyVAO56dFJJVrkt%2FQifVjgppzhhI9tAcU1IUzjyNP5GaJduq1AqHFmg%2F8BvtoOY6%2FfgsbSxjSgjJBJuOsJlUrlksb4K4wk5WpCZTXjn2C0h%2B8ldGo76Vzj70Y9zP9I%2Ba9M1zlE2Fizw5%2BSeTcG2wv6BaZ7HZWgdOPgRiV%2BbPNAmfihJeGgNqEf8%2B4i9iIspD07JcDBZz8Z7AdjTrASRft1ywTK25HCqdRkj2m9Q%2BXSj5Vxz141stlz0HIAaa2qudMV4MxwROChsoTIPBRsn3Hgp8eTFUg5frf1uQvI8lUMC%2BE%2Bb5TuNppHgDE8IQz7ls403hgJksYXa%2FQMjA01SF%2BjIUoqkLdkIlCl8Pd1VYw8EPWztzYaeatOOP2rfOolabpKAFeiyovYgTeOOy29ylB8ABrsRYbnM5HXQZ6v9tRBFch0meeZGuearIW6XoO3%2Bkv9u8n4VWUJGB2Mj%2FB56ayd%2B1jYhUGFAu8V8A85N%2BLBIHHsvD8wWVyisUKrjG3Wy4TrKxm6pW67FDSfGLIBgjZfirypOs7t8rVamdMlVxlBeCfawID9WW2EwnwMJmzjL0GOqUBm%2FqVH3TPAVta333CrGtfHh8mpsaH3pTG7v5yE1nESgNoJkH48FD3nGnq%2Bg0sCzXdd%2Fi9P92EhGfane7%2Fc1hLv%2B9%2BoZ5%2BHhJ6%2FbWyKpwGLh7wAcynZ4LAFwi%2Bof6yAp%2BeAiTebBUfBZ7iaehfUowRKPuN2VqToc8UpiFH7%2FMMYcf5IzrqmVfgObi78X8m00ULvZrMmu4fy%2Bmq%2FChL9Rl89jJ9b8c9&X-Amz-Signature=affabb7e0de7a3642eb9334270c21482551da56228e043eb2f7e0da57b911980&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6OBPUAM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCi%2BzAiJwF0YVUX9zs0Mc%2BOZm4bCd9g6XvwrCvpn%2F85GQIgFklFgdkSG3ntSC63w0euHiErI8K2qP5dc5BR8TNpRGgq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDOomRdwJBdo%2BWgEHECrcA0FznwFwf6ZeM4toCTspORipDZOMxxCSvqP%2FahyKlYXmwwPitvV31Ub%2B2gmd6NlJCgQt%2B9g9b%2FqxKbDpuXqkd7yM%2B6IsOmFU95AZ%2B23%2BZx8Ux1hFky5T7fuL3eqP9ERCzQcbK3WL2cksX7ZF3AnP90%2BajkFL121%2BuGaMCn%2BnqnCruA6fOPZL36FTFVGzHafwmy9yC%2BlPj4DznkLeA3JLX24Wr0Dj8zEWwMJkwsj0B0%2Fl%2BYI%2BIDTg0xoDz0ldea1l7p0N7jU18S4Aat6q%2FXBDhegdjDhHvlayCjrLUIEvgalm0hIrBLrpMVkuoU9icsS69JRVuimbptPCgmYWfnWK0BlunQs2nqJ44kUNu9gigF3keAauDeOV8tLJd6Z1gB%2FX%2F0uO0OKlHTr9RVZLHX%2F9dCMvTDtRpLcnt2%2BpAyRByPioGPs5kNgKGW8uA3o6YbU2bYwx02xwFkIY9AsFXfiZPSSApk27CmNt6KgC%2BJ%2Byke6PELLkMoT%2F7mJx3EgHka8PuisOJn4BPHzOqTkeML6PzrsMX3EeDGeQJO6nZzYKSBwLdKFODF1iwHrMzlGFZIUXqDYAOtyHKQtyAfpdDUZFloaRsGLEaUZSkXNR3dmeZy0gxPQQXqncN6XjEyaOMJizjL0GOqUBlclFLv3kkb%2BEPJ%2B7JEvD75rZGE93iHoIIO0QsZRo4e6gua52%2FR0t0Yvg%2B6i6wUaga%2FqgvLAek7BKyjcXKijGgKHkKFH4nXtJ6aLyaSPcUgpRa2dqZ6l%2FyXFPBKJ%2FUwXXYIhQtE7%2BKfNbePp8VvbRKw1IQjsz2vZx3UWB%2BYKvMx3X2S7KIj6PVHb7M0yCT9InSsI1%2BPGdeOhyvkeCqvkAR0qqTPKa&X-Amz-Signature=8d0d9a31d180ab29ec924d3c547471880d57dd88f1af695e12d69ae3772c6111&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6OBPUAM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCi%2BzAiJwF0YVUX9zs0Mc%2BOZm4bCd9g6XvwrCvpn%2F85GQIgFklFgdkSG3ntSC63w0euHiErI8K2qP5dc5BR8TNpRGgq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDOomRdwJBdo%2BWgEHECrcA0FznwFwf6ZeM4toCTspORipDZOMxxCSvqP%2FahyKlYXmwwPitvV31Ub%2B2gmd6NlJCgQt%2B9g9b%2FqxKbDpuXqkd7yM%2B6IsOmFU95AZ%2B23%2BZx8Ux1hFky5T7fuL3eqP9ERCzQcbK3WL2cksX7ZF3AnP90%2BajkFL121%2BuGaMCn%2BnqnCruA6fOPZL36FTFVGzHafwmy9yC%2BlPj4DznkLeA3JLX24Wr0Dj8zEWwMJkwsj0B0%2Fl%2BYI%2BIDTg0xoDz0ldea1l7p0N7jU18S4Aat6q%2FXBDhegdjDhHvlayCjrLUIEvgalm0hIrBLrpMVkuoU9icsS69JRVuimbptPCgmYWfnWK0BlunQs2nqJ44kUNu9gigF3keAauDeOV8tLJd6Z1gB%2FX%2F0uO0OKlHTr9RVZLHX%2F9dCMvTDtRpLcnt2%2BpAyRByPioGPs5kNgKGW8uA3o6YbU2bYwx02xwFkIY9AsFXfiZPSSApk27CmNt6KgC%2BJ%2Byke6PELLkMoT%2F7mJx3EgHka8PuisOJn4BPHzOqTkeML6PzrsMX3EeDGeQJO6nZzYKSBwLdKFODF1iwHrMzlGFZIUXqDYAOtyHKQtyAfpdDUZFloaRsGLEaUZSkXNR3dmeZy0gxPQQXqncN6XjEyaOMJizjL0GOqUBlclFLv3kkb%2BEPJ%2B7JEvD75rZGE93iHoIIO0QsZRo4e6gua52%2FR0t0Yvg%2B6i6wUaga%2FqgvLAek7BKyjcXKijGgKHkKFH4nXtJ6aLyaSPcUgpRa2dqZ6l%2FyXFPBKJ%2FUwXXYIhQtE7%2BKfNbePp8VvbRKw1IQjsz2vZx3UWB%2BYKvMx3X2S7KIj6PVHb7M0yCT9InSsI1%2BPGdeOhyvkeCqvkAR0qqTPKa&X-Amz-Signature=9313986c5f1dfb84a76d89af09df864bef4d12116649f00f6f9e19e6a93b6f5a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6OBPUAM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCi%2BzAiJwF0YVUX9zs0Mc%2BOZm4bCd9g6XvwrCvpn%2F85GQIgFklFgdkSG3ntSC63w0euHiErI8K2qP5dc5BR8TNpRGgq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDOomRdwJBdo%2BWgEHECrcA0FznwFwf6ZeM4toCTspORipDZOMxxCSvqP%2FahyKlYXmwwPitvV31Ub%2B2gmd6NlJCgQt%2B9g9b%2FqxKbDpuXqkd7yM%2B6IsOmFU95AZ%2B23%2BZx8Ux1hFky5T7fuL3eqP9ERCzQcbK3WL2cksX7ZF3AnP90%2BajkFL121%2BuGaMCn%2BnqnCruA6fOPZL36FTFVGzHafwmy9yC%2BlPj4DznkLeA3JLX24Wr0Dj8zEWwMJkwsj0B0%2Fl%2BYI%2BIDTg0xoDz0ldea1l7p0N7jU18S4Aat6q%2FXBDhegdjDhHvlayCjrLUIEvgalm0hIrBLrpMVkuoU9icsS69JRVuimbptPCgmYWfnWK0BlunQs2nqJ44kUNu9gigF3keAauDeOV8tLJd6Z1gB%2FX%2F0uO0OKlHTr9RVZLHX%2F9dCMvTDtRpLcnt2%2BpAyRByPioGPs5kNgKGW8uA3o6YbU2bYwx02xwFkIY9AsFXfiZPSSApk27CmNt6KgC%2BJ%2Byke6PELLkMoT%2F7mJx3EgHka8PuisOJn4BPHzOqTkeML6PzrsMX3EeDGeQJO6nZzYKSBwLdKFODF1iwHrMzlGFZIUXqDYAOtyHKQtyAfpdDUZFloaRsGLEaUZSkXNR3dmeZy0gxPQQXqncN6XjEyaOMJizjL0GOqUBlclFLv3kkb%2BEPJ%2B7JEvD75rZGE93iHoIIO0QsZRo4e6gua52%2FR0t0Yvg%2B6i6wUaga%2FqgvLAek7BKyjcXKijGgKHkKFH4nXtJ6aLyaSPcUgpRa2dqZ6l%2FyXFPBKJ%2FUwXXYIhQtE7%2BKfNbePp8VvbRKw1IQjsz2vZx3UWB%2BYKvMx3X2S7KIj6PVHb7M0yCT9InSsI1%2BPGdeOhyvkeCqvkAR0qqTPKa&X-Amz-Signature=d4cf42e83da5a9afee749be4038b55945b6748d89552178404bf652c78314c70&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6OBPUAM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCi%2BzAiJwF0YVUX9zs0Mc%2BOZm4bCd9g6XvwrCvpn%2F85GQIgFklFgdkSG3ntSC63w0euHiErI8K2qP5dc5BR8TNpRGgq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDOomRdwJBdo%2BWgEHECrcA0FznwFwf6ZeM4toCTspORipDZOMxxCSvqP%2FahyKlYXmwwPitvV31Ub%2B2gmd6NlJCgQt%2B9g9b%2FqxKbDpuXqkd7yM%2B6IsOmFU95AZ%2B23%2BZx8Ux1hFky5T7fuL3eqP9ERCzQcbK3WL2cksX7ZF3AnP90%2BajkFL121%2BuGaMCn%2BnqnCruA6fOPZL36FTFVGzHafwmy9yC%2BlPj4DznkLeA3JLX24Wr0Dj8zEWwMJkwsj0B0%2Fl%2BYI%2BIDTg0xoDz0ldea1l7p0N7jU18S4Aat6q%2FXBDhegdjDhHvlayCjrLUIEvgalm0hIrBLrpMVkuoU9icsS69JRVuimbptPCgmYWfnWK0BlunQs2nqJ44kUNu9gigF3keAauDeOV8tLJd6Z1gB%2FX%2F0uO0OKlHTr9RVZLHX%2F9dCMvTDtRpLcnt2%2BpAyRByPioGPs5kNgKGW8uA3o6YbU2bYwx02xwFkIY9AsFXfiZPSSApk27CmNt6KgC%2BJ%2Byke6PELLkMoT%2F7mJx3EgHka8PuisOJn4BPHzOqTkeML6PzrsMX3EeDGeQJO6nZzYKSBwLdKFODF1iwHrMzlGFZIUXqDYAOtyHKQtyAfpdDUZFloaRsGLEaUZSkXNR3dmeZy0gxPQQXqncN6XjEyaOMJizjL0GOqUBlclFLv3kkb%2BEPJ%2B7JEvD75rZGE93iHoIIO0QsZRo4e6gua52%2FR0t0Yvg%2B6i6wUaga%2FqgvLAek7BKyjcXKijGgKHkKFH4nXtJ6aLyaSPcUgpRa2dqZ6l%2FyXFPBKJ%2FUwXXYIhQtE7%2BKfNbePp8VvbRKw1IQjsz2vZx3UWB%2BYKvMx3X2S7KIj6PVHb7M0yCT9InSsI1%2BPGdeOhyvkeCqvkAR0qqTPKa&X-Amz-Signature=c9f5fa1f8fc44120fb2d490f0762fcac1b797bd3259d99282a3d348e8e911aff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6OBPUAM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQCi%2BzAiJwF0YVUX9zs0Mc%2BOZm4bCd9g6XvwrCvpn%2F85GQIgFklFgdkSG3ntSC63w0euHiErI8K2qP5dc5BR8TNpRGgq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDOomRdwJBdo%2BWgEHECrcA0FznwFwf6ZeM4toCTspORipDZOMxxCSvqP%2FahyKlYXmwwPitvV31Ub%2B2gmd6NlJCgQt%2B9g9b%2FqxKbDpuXqkd7yM%2B6IsOmFU95AZ%2B23%2BZx8Ux1hFky5T7fuL3eqP9ERCzQcbK3WL2cksX7ZF3AnP90%2BajkFL121%2BuGaMCn%2BnqnCruA6fOPZL36FTFVGzHafwmy9yC%2BlPj4DznkLeA3JLX24Wr0Dj8zEWwMJkwsj0B0%2Fl%2BYI%2BIDTg0xoDz0ldea1l7p0N7jU18S4Aat6q%2FXBDhegdjDhHvlayCjrLUIEvgalm0hIrBLrpMVkuoU9icsS69JRVuimbptPCgmYWfnWK0BlunQs2nqJ44kUNu9gigF3keAauDeOV8tLJd6Z1gB%2FX%2F0uO0OKlHTr9RVZLHX%2F9dCMvTDtRpLcnt2%2BpAyRByPioGPs5kNgKGW8uA3o6YbU2bYwx02xwFkIY9AsFXfiZPSSApk27CmNt6KgC%2BJ%2Byke6PELLkMoT%2F7mJx3EgHka8PuisOJn4BPHzOqTkeML6PzrsMX3EeDGeQJO6nZzYKSBwLdKFODF1iwHrMzlGFZIUXqDYAOtyHKQtyAfpdDUZFloaRsGLEaUZSkXNR3dmeZy0gxPQQXqncN6XjEyaOMJizjL0GOqUBlclFLv3kkb%2BEPJ%2B7JEvD75rZGE93iHoIIO0QsZRo4e6gua52%2FR0t0Yvg%2B6i6wUaga%2FqgvLAek7BKyjcXKijGgKHkKFH4nXtJ6aLyaSPcUgpRa2dqZ6l%2FyXFPBKJ%2FUwXXYIhQtE7%2BKfNbePp8VvbRKw1IQjsz2vZx3UWB%2BYKvMx3X2S7KIj6PVHb7M0yCT9InSsI1%2BPGdeOhyvkeCqvkAR0qqTPKa&X-Amz-Signature=36c10240f16c66d414cd2c94f61063b41e68a06bc863fa845b8cd99a734c59ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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


