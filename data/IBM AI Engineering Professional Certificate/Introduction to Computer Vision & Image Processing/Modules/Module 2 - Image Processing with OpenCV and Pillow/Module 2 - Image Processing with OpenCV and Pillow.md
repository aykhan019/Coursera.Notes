

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ESTSYAD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCID3dQl2UKGr9tBY0ctBJekHDu%2BA8tjgzCHnBdB9QMB4aAiEA9aaYO10g%2FGkPiikWjF1nCBbY%2FUBPwWlZ1XNGwdd42Aoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK1tExQQ%2FpvW1o7AWircA8wRiY2qBYcIS4cbzUli%2BFg%2BGKgH%2BI23HgIOrqVnHyn8FfwPGpp3wepdYFp%2BCRSmLGiNscFlYjkNhS9oHCQ1NQgWm3VydUnmyHqG3JKJYwvPh2aUDIx3A6exYb1DgWJouSxKaQP0KK%2BchoOwuThjnyHscmb7Fnsv9ZHfRWR7dLfMCGVmixPAoBdd6wIkj%2BfLGINmFkdffJb46HuWZcJbHPzvzUxVpfJkRgMxw4MQ%2FRPaJ%2BvBYpRQ2JQTSu2vbGm4PHkt4uGuRjhgzCYQDXqZDyZAhOiWHMvdP0VVeinpLiHEGRTX10YVq6NHvlCjZElLWYOp5z9K2t%2BJiEq1yv3b%2Fufs7yUbCdNOScuP%2FF6RmS21%2BhWpOzsQKhUulo0n3APeqt0jXR1yIEv%2BgmZXcmYcDsoWx4wpPeCcoxnmehMHOu45Nbp%2FmRdPElOtIZsEK6K%2FA05kiubmg5PIHKa30fz6ApnAkmAT3A7uiAjWmQEMUPkCIuzk6EGnOxQHmwIBlcsreeHNkrT9Qyd7qWmhnpUVhOg48r27AVkneStdM3NiY39ILYhXgzkKaJTcgRQ6xZg7Lq5zChh9frN%2FxKzKs08eWVhAXJ7TxDNVpnhSKJaPxIClyhKwulRoqq8ahZi%2BMILrj70GOqUByrgmJZdupO7xoD6rcFP7PnsMYlz0MyfCPtaUH969D941Ywc01K2jLs7B%2FuAY%2BTXTIPqEOegC1ZEXp0YSjE9JdBjXpyKFm8Yw8GhIQUHfXKTMqW3YzoadUhZA2pepFlV1kbTGJeiFjCerT8eSgBuXoXGRhtk15Pt7Gb8yuil%2BfUCPU0KWxGzQ%2FNaBrWUpgDFHBp9SaoW10c99AaAclvIEKX7JH%2B0D&X-Amz-Signature=8ca4eb631bb593b6c9da188b9c8a2e2f2b776db19df3be990ccf5c3f4fdac326&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2U2JZEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCv%2BoIkdBuVj1b7G4095YD7D3vgGUMTxDhBDX1i02r10QIgJpqoRkC0yOhyPZ%2BxvVrp7bd6ipn4%2BisgN8zAX1T%2FGU8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOTqcumQGgSP0fpQHSrcA0S3wqezDoVjowCSLga8SwDuQnIpDMcT1SckTb7jREkBHKfOo8spVwFlcXFcPmf%2BENynXnUpOrB0aSVY%2F0Yn0SmhtvN2srlMvxBqdrMDi10GDHpPG98Mp%2B4tJz3lZLSmjfWvm1XlHtpUVxLuRpE8FopZHfq354VhGQekWnk621rjat%2BTMCr%2F1CBXx%2FGLH2XZ0oa5vWXKuiEJlaEcOuhasua6sdZs73xicnwvyJiQiqYGWi18hIISuY9%2F%2BKP5zVRalpvH5%2B6yW3a7OpleYUBGP7lB6dXH0my1qA63XMd6m9LMn2QwkvoMvmw%2FpAVu4yUTXOpshgLRBLALI7bmOWmT3ttY%2FRbTnOQuHhAX8i6c5M25TACZtZLRqC3wJByzD2jCzN1jDZ8iDRpl1SV%2FKc8joaOKjDBXJW11girJjHS0ow%2FIRFOxvrEftV6cRY3adXQy4RHopSYN6IRitjmCSiCc5aKSf3RNAmvTzTXQgYDLHbp5lGXkmOAuLTD1tFWGvlRInPGXyUIG1Sgl3j%2B4PFrGTlbHvjDUtID3YWFTPpBLeEw0D9kDCQe5%2BUYe%2FzjISZ7lw66Vbntf7C31xa1QwHbpVyGARa9lpF85ByewEasy09gxv1kRzePKYgaBi%2F93MJTrj70GOqUBKxwPdQjeO5E7IV%2FOMs5kBJc%2F8TXJz1gaSMbBpGvjeUUZaxmS3aZhQv6Z5v41iKWhbb0Xgx3AjeWcWmVOdlvlEqzI%2Fb%2BuP6EPPjBkQlZcVulFR3tLji5BdDnWKebgA3FQkblwlAnss6of%2FB67jYXYAADDf1fVa1DNYjSc4gXqbLPfJOj%2BBUpRpVbylI1K5Dr9Wn39U60AWyyBkyAXDh%2BzIziGcOAD&X-Amz-Signature=89b6590616185bf33264ecb5a5f59389e0a4f8973f2fddcd27175e817ac0af1f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2U2JZEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCv%2BoIkdBuVj1b7G4095YD7D3vgGUMTxDhBDX1i02r10QIgJpqoRkC0yOhyPZ%2BxvVrp7bd6ipn4%2BisgN8zAX1T%2FGU8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOTqcumQGgSP0fpQHSrcA0S3wqezDoVjowCSLga8SwDuQnIpDMcT1SckTb7jREkBHKfOo8spVwFlcXFcPmf%2BENynXnUpOrB0aSVY%2F0Yn0SmhtvN2srlMvxBqdrMDi10GDHpPG98Mp%2B4tJz3lZLSmjfWvm1XlHtpUVxLuRpE8FopZHfq354VhGQekWnk621rjat%2BTMCr%2F1CBXx%2FGLH2XZ0oa5vWXKuiEJlaEcOuhasua6sdZs73xicnwvyJiQiqYGWi18hIISuY9%2F%2BKP5zVRalpvH5%2B6yW3a7OpleYUBGP7lB6dXH0my1qA63XMd6m9LMn2QwkvoMvmw%2FpAVu4yUTXOpshgLRBLALI7bmOWmT3ttY%2FRbTnOQuHhAX8i6c5M25TACZtZLRqC3wJByzD2jCzN1jDZ8iDRpl1SV%2FKc8joaOKjDBXJW11girJjHS0ow%2FIRFOxvrEftV6cRY3adXQy4RHopSYN6IRitjmCSiCc5aKSf3RNAmvTzTXQgYDLHbp5lGXkmOAuLTD1tFWGvlRInPGXyUIG1Sgl3j%2B4PFrGTlbHvjDUtID3YWFTPpBLeEw0D9kDCQe5%2BUYe%2FzjISZ7lw66Vbntf7C31xa1QwHbpVyGARa9lpF85ByewEasy09gxv1kRzePKYgaBi%2F93MJTrj70GOqUBKxwPdQjeO5E7IV%2FOMs5kBJc%2F8TXJz1gaSMbBpGvjeUUZaxmS3aZhQv6Z5v41iKWhbb0Xgx3AjeWcWmVOdlvlEqzI%2Fb%2BuP6EPPjBkQlZcVulFR3tLji5BdDnWKebgA3FQkblwlAnss6of%2FB67jYXYAADDf1fVa1DNYjSc4gXqbLPfJOj%2BBUpRpVbylI1K5Dr9Wn39U60AWyyBkyAXDh%2BzIziGcOAD&X-Amz-Signature=6f048850af30aa628a54ce9e2653772bbe2b9146ffcc748cd2bc074fb6214efa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2U2JZEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCv%2BoIkdBuVj1b7G4095YD7D3vgGUMTxDhBDX1i02r10QIgJpqoRkC0yOhyPZ%2BxvVrp7bd6ipn4%2BisgN8zAX1T%2FGU8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOTqcumQGgSP0fpQHSrcA0S3wqezDoVjowCSLga8SwDuQnIpDMcT1SckTb7jREkBHKfOo8spVwFlcXFcPmf%2BENynXnUpOrB0aSVY%2F0Yn0SmhtvN2srlMvxBqdrMDi10GDHpPG98Mp%2B4tJz3lZLSmjfWvm1XlHtpUVxLuRpE8FopZHfq354VhGQekWnk621rjat%2BTMCr%2F1CBXx%2FGLH2XZ0oa5vWXKuiEJlaEcOuhasua6sdZs73xicnwvyJiQiqYGWi18hIISuY9%2F%2BKP5zVRalpvH5%2B6yW3a7OpleYUBGP7lB6dXH0my1qA63XMd6m9LMn2QwkvoMvmw%2FpAVu4yUTXOpshgLRBLALI7bmOWmT3ttY%2FRbTnOQuHhAX8i6c5M25TACZtZLRqC3wJByzD2jCzN1jDZ8iDRpl1SV%2FKc8joaOKjDBXJW11girJjHS0ow%2FIRFOxvrEftV6cRY3adXQy4RHopSYN6IRitjmCSiCc5aKSf3RNAmvTzTXQgYDLHbp5lGXkmOAuLTD1tFWGvlRInPGXyUIG1Sgl3j%2B4PFrGTlbHvjDUtID3YWFTPpBLeEw0D9kDCQe5%2BUYe%2FzjISZ7lw66Vbntf7C31xa1QwHbpVyGARa9lpF85ByewEasy09gxv1kRzePKYgaBi%2F93MJTrj70GOqUBKxwPdQjeO5E7IV%2FOMs5kBJc%2F8TXJz1gaSMbBpGvjeUUZaxmS3aZhQv6Z5v41iKWhbb0Xgx3AjeWcWmVOdlvlEqzI%2Fb%2BuP6EPPjBkQlZcVulFR3tLji5BdDnWKebgA3FQkblwlAnss6of%2FB67jYXYAADDf1fVa1DNYjSc4gXqbLPfJOj%2BBUpRpVbylI1K5Dr9Wn39U60AWyyBkyAXDh%2BzIziGcOAD&X-Amz-Signature=affd01ba0b419ffced19da88d51597519f25be70994cb49ee5e21a1df3fc48b4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2U2JZEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCv%2BoIkdBuVj1b7G4095YD7D3vgGUMTxDhBDX1i02r10QIgJpqoRkC0yOhyPZ%2BxvVrp7bd6ipn4%2BisgN8zAX1T%2FGU8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOTqcumQGgSP0fpQHSrcA0S3wqezDoVjowCSLga8SwDuQnIpDMcT1SckTb7jREkBHKfOo8spVwFlcXFcPmf%2BENynXnUpOrB0aSVY%2F0Yn0SmhtvN2srlMvxBqdrMDi10GDHpPG98Mp%2B4tJz3lZLSmjfWvm1XlHtpUVxLuRpE8FopZHfq354VhGQekWnk621rjat%2BTMCr%2F1CBXx%2FGLH2XZ0oa5vWXKuiEJlaEcOuhasua6sdZs73xicnwvyJiQiqYGWi18hIISuY9%2F%2BKP5zVRalpvH5%2B6yW3a7OpleYUBGP7lB6dXH0my1qA63XMd6m9LMn2QwkvoMvmw%2FpAVu4yUTXOpshgLRBLALI7bmOWmT3ttY%2FRbTnOQuHhAX8i6c5M25TACZtZLRqC3wJByzD2jCzN1jDZ8iDRpl1SV%2FKc8joaOKjDBXJW11girJjHS0ow%2FIRFOxvrEftV6cRY3adXQy4RHopSYN6IRitjmCSiCc5aKSf3RNAmvTzTXQgYDLHbp5lGXkmOAuLTD1tFWGvlRInPGXyUIG1Sgl3j%2B4PFrGTlbHvjDUtID3YWFTPpBLeEw0D9kDCQe5%2BUYe%2FzjISZ7lw66Vbntf7C31xa1QwHbpVyGARa9lpF85ByewEasy09gxv1kRzePKYgaBi%2F93MJTrj70GOqUBKxwPdQjeO5E7IV%2FOMs5kBJc%2F8TXJz1gaSMbBpGvjeUUZaxmS3aZhQv6Z5v41iKWhbb0Xgx3AjeWcWmVOdlvlEqzI%2Fb%2BuP6EPPjBkQlZcVulFR3tLji5BdDnWKebgA3FQkblwlAnss6of%2FB67jYXYAADDf1fVa1DNYjSc4gXqbLPfJOj%2BBUpRpVbylI1K5Dr9Wn39U60AWyyBkyAXDh%2BzIziGcOAD&X-Amz-Signature=08bad0bc34a6d8aad64c0ccbfa490961b61d6051a09159a09d3775303eb7fb73&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2U2JZEW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCv%2BoIkdBuVj1b7G4095YD7D3vgGUMTxDhBDX1i02r10QIgJpqoRkC0yOhyPZ%2BxvVrp7bd6ipn4%2BisgN8zAX1T%2FGU8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOTqcumQGgSP0fpQHSrcA0S3wqezDoVjowCSLga8SwDuQnIpDMcT1SckTb7jREkBHKfOo8spVwFlcXFcPmf%2BENynXnUpOrB0aSVY%2F0Yn0SmhtvN2srlMvxBqdrMDi10GDHpPG98Mp%2B4tJz3lZLSmjfWvm1XlHtpUVxLuRpE8FopZHfq354VhGQekWnk621rjat%2BTMCr%2F1CBXx%2FGLH2XZ0oa5vWXKuiEJlaEcOuhasua6sdZs73xicnwvyJiQiqYGWi18hIISuY9%2F%2BKP5zVRalpvH5%2B6yW3a7OpleYUBGP7lB6dXH0my1qA63XMd6m9LMn2QwkvoMvmw%2FpAVu4yUTXOpshgLRBLALI7bmOWmT3ttY%2FRbTnOQuHhAX8i6c5M25TACZtZLRqC3wJByzD2jCzN1jDZ8iDRpl1SV%2FKc8joaOKjDBXJW11girJjHS0ow%2FIRFOxvrEftV6cRY3adXQy4RHopSYN6IRitjmCSiCc5aKSf3RNAmvTzTXQgYDLHbp5lGXkmOAuLTD1tFWGvlRInPGXyUIG1Sgl3j%2B4PFrGTlbHvjDUtID3YWFTPpBLeEw0D9kDCQe5%2BUYe%2FzjISZ7lw66Vbntf7C31xa1QwHbpVyGARa9lpF85ByewEasy09gxv1kRzePKYgaBi%2F93MJTrj70GOqUBKxwPdQjeO5E7IV%2FOMs5kBJc%2F8TXJz1gaSMbBpGvjeUUZaxmS3aZhQv6Z5v41iKWhbb0Xgx3AjeWcWmVOdlvlEqzI%2Fb%2BuP6EPPjBkQlZcVulFR3tLji5BdDnWKebgA3FQkblwlAnss6of%2FB67jYXYAADDf1fVa1DNYjSc4gXqbLPfJOj%2BBUpRpVbylI1K5Dr9Wn39U60AWyyBkyAXDh%2BzIziGcOAD&X-Amz-Signature=1e5f30f64e6cceb57c7c46248a675d930809e83b42bd1491a468051e99c15120&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ESTSYAD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCID3dQl2UKGr9tBY0ctBJekHDu%2BA8tjgzCHnBdB9QMB4aAiEA9aaYO10g%2FGkPiikWjF1nCBbY%2FUBPwWlZ1XNGwdd42Aoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK1tExQQ%2FpvW1o7AWircA8wRiY2qBYcIS4cbzUli%2BFg%2BGKgH%2BI23HgIOrqVnHyn8FfwPGpp3wepdYFp%2BCRSmLGiNscFlYjkNhS9oHCQ1NQgWm3VydUnmyHqG3JKJYwvPh2aUDIx3A6exYb1DgWJouSxKaQP0KK%2BchoOwuThjnyHscmb7Fnsv9ZHfRWR7dLfMCGVmixPAoBdd6wIkj%2BfLGINmFkdffJb46HuWZcJbHPzvzUxVpfJkRgMxw4MQ%2FRPaJ%2BvBYpRQ2JQTSu2vbGm4PHkt4uGuRjhgzCYQDXqZDyZAhOiWHMvdP0VVeinpLiHEGRTX10YVq6NHvlCjZElLWYOp5z9K2t%2BJiEq1yv3b%2Fufs7yUbCdNOScuP%2FF6RmS21%2BhWpOzsQKhUulo0n3APeqt0jXR1yIEv%2BgmZXcmYcDsoWx4wpPeCcoxnmehMHOu45Nbp%2FmRdPElOtIZsEK6K%2FA05kiubmg5PIHKa30fz6ApnAkmAT3A7uiAjWmQEMUPkCIuzk6EGnOxQHmwIBlcsreeHNkrT9Qyd7qWmhnpUVhOg48r27AVkneStdM3NiY39ILYhXgzkKaJTcgRQ6xZg7Lq5zChh9frN%2FxKzKs08eWVhAXJ7TxDNVpnhSKJaPxIClyhKwulRoqq8ahZi%2BMILrj70GOqUByrgmJZdupO7xoD6rcFP7PnsMYlz0MyfCPtaUH969D941Ywc01K2jLs7B%2FuAY%2BTXTIPqEOegC1ZEXp0YSjE9JdBjXpyKFm8Yw8GhIQUHfXKTMqW3YzoadUhZA2pepFlV1kbTGJeiFjCerT8eSgBuXoXGRhtk15Pt7Gb8yuil%2BfUCPU0KWxGzQ%2FNaBrWUpgDFHBp9SaoW10c99AaAclvIEKX7JH%2B0D&X-Amz-Signature=b3100fee136750137b865c79812726cc64b61b6204949f40a9d6503402c3fb2e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ESTSYAD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCID3dQl2UKGr9tBY0ctBJekHDu%2BA8tjgzCHnBdB9QMB4aAiEA9aaYO10g%2FGkPiikWjF1nCBbY%2FUBPwWlZ1XNGwdd42Aoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK1tExQQ%2FpvW1o7AWircA8wRiY2qBYcIS4cbzUli%2BFg%2BGKgH%2BI23HgIOrqVnHyn8FfwPGpp3wepdYFp%2BCRSmLGiNscFlYjkNhS9oHCQ1NQgWm3VydUnmyHqG3JKJYwvPh2aUDIx3A6exYb1DgWJouSxKaQP0KK%2BchoOwuThjnyHscmb7Fnsv9ZHfRWR7dLfMCGVmixPAoBdd6wIkj%2BfLGINmFkdffJb46HuWZcJbHPzvzUxVpfJkRgMxw4MQ%2FRPaJ%2BvBYpRQ2JQTSu2vbGm4PHkt4uGuRjhgzCYQDXqZDyZAhOiWHMvdP0VVeinpLiHEGRTX10YVq6NHvlCjZElLWYOp5z9K2t%2BJiEq1yv3b%2Fufs7yUbCdNOScuP%2FF6RmS21%2BhWpOzsQKhUulo0n3APeqt0jXR1yIEv%2BgmZXcmYcDsoWx4wpPeCcoxnmehMHOu45Nbp%2FmRdPElOtIZsEK6K%2FA05kiubmg5PIHKa30fz6ApnAkmAT3A7uiAjWmQEMUPkCIuzk6EGnOxQHmwIBlcsreeHNkrT9Qyd7qWmhnpUVhOg48r27AVkneStdM3NiY39ILYhXgzkKaJTcgRQ6xZg7Lq5zChh9frN%2FxKzKs08eWVhAXJ7TxDNVpnhSKJaPxIClyhKwulRoqq8ahZi%2BMILrj70GOqUByrgmJZdupO7xoD6rcFP7PnsMYlz0MyfCPtaUH969D941Ywc01K2jLs7B%2FuAY%2BTXTIPqEOegC1ZEXp0YSjE9JdBjXpyKFm8Yw8GhIQUHfXKTMqW3YzoadUhZA2pepFlV1kbTGJeiFjCerT8eSgBuXoXGRhtk15Pt7Gb8yuil%2BfUCPU0KWxGzQ%2FNaBrWUpgDFHBp9SaoW10c99AaAclvIEKX7JH%2B0D&X-Amz-Signature=3190f5c4723669ea1026241a5e30e55ae3e3726ff476f6b40d6f67df8de29eaa&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ESTSYAD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCID3dQl2UKGr9tBY0ctBJekHDu%2BA8tjgzCHnBdB9QMB4aAiEA9aaYO10g%2FGkPiikWjF1nCBbY%2FUBPwWlZ1XNGwdd42Aoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK1tExQQ%2FpvW1o7AWircA8wRiY2qBYcIS4cbzUli%2BFg%2BGKgH%2BI23HgIOrqVnHyn8FfwPGpp3wepdYFp%2BCRSmLGiNscFlYjkNhS9oHCQ1NQgWm3VydUnmyHqG3JKJYwvPh2aUDIx3A6exYb1DgWJouSxKaQP0KK%2BchoOwuThjnyHscmb7Fnsv9ZHfRWR7dLfMCGVmixPAoBdd6wIkj%2BfLGINmFkdffJb46HuWZcJbHPzvzUxVpfJkRgMxw4MQ%2FRPaJ%2BvBYpRQ2JQTSu2vbGm4PHkt4uGuRjhgzCYQDXqZDyZAhOiWHMvdP0VVeinpLiHEGRTX10YVq6NHvlCjZElLWYOp5z9K2t%2BJiEq1yv3b%2Fufs7yUbCdNOScuP%2FF6RmS21%2BhWpOzsQKhUulo0n3APeqt0jXR1yIEv%2BgmZXcmYcDsoWx4wpPeCcoxnmehMHOu45Nbp%2FmRdPElOtIZsEK6K%2FA05kiubmg5PIHKa30fz6ApnAkmAT3A7uiAjWmQEMUPkCIuzk6EGnOxQHmwIBlcsreeHNkrT9Qyd7qWmhnpUVhOg48r27AVkneStdM3NiY39ILYhXgzkKaJTcgRQ6xZg7Lq5zChh9frN%2FxKzKs08eWVhAXJ7TxDNVpnhSKJaPxIClyhKwulRoqq8ahZi%2BMILrj70GOqUByrgmJZdupO7xoD6rcFP7PnsMYlz0MyfCPtaUH969D941Ywc01K2jLs7B%2FuAY%2BTXTIPqEOegC1ZEXp0YSjE9JdBjXpyKFm8Yw8GhIQUHfXKTMqW3YzoadUhZA2pepFlV1kbTGJeiFjCerT8eSgBuXoXGRhtk15Pt7Gb8yuil%2BfUCPU0KWxGzQ%2FNaBrWUpgDFHBp9SaoW10c99AaAclvIEKX7JH%2B0D&X-Amz-Signature=2ce8a8e14d1940847d47166fc6578400939dfc5a7394722f38347b091383c42d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ESTSYAD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCID3dQl2UKGr9tBY0ctBJekHDu%2BA8tjgzCHnBdB9QMB4aAiEA9aaYO10g%2FGkPiikWjF1nCBbY%2FUBPwWlZ1XNGwdd42Aoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK1tExQQ%2FpvW1o7AWircA8wRiY2qBYcIS4cbzUli%2BFg%2BGKgH%2BI23HgIOrqVnHyn8FfwPGpp3wepdYFp%2BCRSmLGiNscFlYjkNhS9oHCQ1NQgWm3VydUnmyHqG3JKJYwvPh2aUDIx3A6exYb1DgWJouSxKaQP0KK%2BchoOwuThjnyHscmb7Fnsv9ZHfRWR7dLfMCGVmixPAoBdd6wIkj%2BfLGINmFkdffJb46HuWZcJbHPzvzUxVpfJkRgMxw4MQ%2FRPaJ%2BvBYpRQ2JQTSu2vbGm4PHkt4uGuRjhgzCYQDXqZDyZAhOiWHMvdP0VVeinpLiHEGRTX10YVq6NHvlCjZElLWYOp5z9K2t%2BJiEq1yv3b%2Fufs7yUbCdNOScuP%2FF6RmS21%2BhWpOzsQKhUulo0n3APeqt0jXR1yIEv%2BgmZXcmYcDsoWx4wpPeCcoxnmehMHOu45Nbp%2FmRdPElOtIZsEK6K%2FA05kiubmg5PIHKa30fz6ApnAkmAT3A7uiAjWmQEMUPkCIuzk6EGnOxQHmwIBlcsreeHNkrT9Qyd7qWmhnpUVhOg48r27AVkneStdM3NiY39ILYhXgzkKaJTcgRQ6xZg7Lq5zChh9frN%2FxKzKs08eWVhAXJ7TxDNVpnhSKJaPxIClyhKwulRoqq8ahZi%2BMILrj70GOqUByrgmJZdupO7xoD6rcFP7PnsMYlz0MyfCPtaUH969D941Ywc01K2jLs7B%2FuAY%2BTXTIPqEOegC1ZEXp0YSjE9JdBjXpyKFm8Yw8GhIQUHfXKTMqW3YzoadUhZA2pepFlV1kbTGJeiFjCerT8eSgBuXoXGRhtk15Pt7Gb8yuil%2BfUCPU0KWxGzQ%2FNaBrWUpgDFHBp9SaoW10c99AaAclvIEKX7JH%2B0D&X-Amz-Signature=d9127eb7bdb9bfdbb10d97b5753c61cb7c782b5add9dae6f761f723f09a0c225&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ESTSYAD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCID3dQl2UKGr9tBY0ctBJekHDu%2BA8tjgzCHnBdB9QMB4aAiEA9aaYO10g%2FGkPiikWjF1nCBbY%2FUBPwWlZ1XNGwdd42Aoq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDK1tExQQ%2FpvW1o7AWircA8wRiY2qBYcIS4cbzUli%2BFg%2BGKgH%2BI23HgIOrqVnHyn8FfwPGpp3wepdYFp%2BCRSmLGiNscFlYjkNhS9oHCQ1NQgWm3VydUnmyHqG3JKJYwvPh2aUDIx3A6exYb1DgWJouSxKaQP0KK%2BchoOwuThjnyHscmb7Fnsv9ZHfRWR7dLfMCGVmixPAoBdd6wIkj%2BfLGINmFkdffJb46HuWZcJbHPzvzUxVpfJkRgMxw4MQ%2FRPaJ%2BvBYpRQ2JQTSu2vbGm4PHkt4uGuRjhgzCYQDXqZDyZAhOiWHMvdP0VVeinpLiHEGRTX10YVq6NHvlCjZElLWYOp5z9K2t%2BJiEq1yv3b%2Fufs7yUbCdNOScuP%2FF6RmS21%2BhWpOzsQKhUulo0n3APeqt0jXR1yIEv%2BgmZXcmYcDsoWx4wpPeCcoxnmehMHOu45Nbp%2FmRdPElOtIZsEK6K%2FA05kiubmg5PIHKa30fz6ApnAkmAT3A7uiAjWmQEMUPkCIuzk6EGnOxQHmwIBlcsreeHNkrT9Qyd7qWmhnpUVhOg48r27AVkneStdM3NiY39ILYhXgzkKaJTcgRQ6xZg7Lq5zChh9frN%2FxKzKs08eWVhAXJ7TxDNVpnhSKJaPxIClyhKwulRoqq8ahZi%2BMILrj70GOqUByrgmJZdupO7xoD6rcFP7PnsMYlz0MyfCPtaUH969D941Ywc01K2jLs7B%2FuAY%2BTXTIPqEOegC1ZEXp0YSjE9JdBjXpyKFm8Yw8GhIQUHfXKTMqW3YzoadUhZA2pepFlV1kbTGJeiFjCerT8eSgBuXoXGRhtk15Pt7Gb8yuil%2BfUCPU0KWxGzQ%2FNaBrWUpgDFHBp9SaoW10c99AaAclvIEKX7JH%2B0D&X-Amz-Signature=6faa82c9ae15b097b2bf436ff7b756482285d4a75e1ec1b8e57ae08c968ec32c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


