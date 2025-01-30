

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHONZZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7cp52fiSjAVgmC%2FeAa%2F8osSoHPnjAdgqDZ5oUcafuwIgMxR4rqEKz6eXVat9E08RPCWHcdugDHmsEXgae7lFSogqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGXm4g60n8Z8AfQWSrcAx1yP%2BCciZWwZPpC%2F0bXzi%2BVBzBQMcxp5EjrJMqCIiSxNbWwxG2Ek0R6DQIW4%2F99%2BlVqncATjfFdaVILiWlj14CvQ0fltKDt9Ef%2B8LncskR%2BsPOkCbb3iEAu%2Bvu7NBshrbkYf07BcJAOF7heVKzzMarZmFUS%2BHEDl2HCU4ffCNpBTG%2BCMt8ACy5L12cTqaPiNXPSNjgAqNbVu6mTCs5QftMccXy3IwONePD0%2FRxNcKevZ8c716IojPyPPCaGZ%2FL9vre1G4Hng8I1CyxfwDAYK7P2fzqT1iZ8f%2BeaLSwLTVWvCjukdQ0aaJjwknMQi2e2CWVIJaGpeZnIvXOE1xgdSkiyYGHVV1lQZJ7XkCpzItbS6XXh7hAfmmEtme858QKU8o2wr%2BCxfFCr2P309xxwZmc%2FSkDk%2F2NcnUF5ex7vWHI%2BenrByG85L5wARhM%2FblFGvTkAyWcdx%2Fj3UGr%2F%2BHhM1pyT%2BahBynhN3AobLYiXt1OG%2BlSpYGrfTcpS6sUVp0IW1ttS4DASp%2FjZMtd42rhRHTyTyWs8U0Pdh%2BYLu6u5z7ywvkNY7HvuR7D9SIlXvuvdyk6uAikoQMPGIN7tEvbAehZHy1ECyC3KzaPo7AmHDvxNNkfclyuh7QjEbTZsMObO67wGOqUBxLKN5%2B2WyguWBd%2B9QrkfzWeLEplYsOCYb3PZZrTHDgqqsK%2Fjow7lDCX5nUDMtSiuQ1LQV10niD0EskREFtxhHVkxO1fKIK3ZTAkkWLFNlo0h0XzC0fY9AHFBR6%2BUgGK8wRnfTHTymnineC3WSJB32QlFXxZpEf4EWMG14N0MixpCmIjiUmLQrWvFfj3uQ3H6f1lBoYsSxRTYISlrVPxjXjwzy1tb&X-Amz-Signature=2c90b9214e4690d35534b365f45bb5bbb09960e8e75cf829425cee60a834f451&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKX2MKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAeAoRnljrndjf79BDjdDUTUAFyFdDm9IiLIiDYRdGrwIgTH8ECxpCS2uCoTtMJcyyW%2B3SvrCNlAoiQBTJTUMf%2Fx4qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlWPdEzPrtwrXVD7SrcAxXOM8XjRguTNiG%2BUMYuzVg1uYJrFFPXbr9xeto3u3G982jHXPCxF14998GTwQUC50ynNjVg0CGra9%2FSJTPwTvNQVHj9yZ1okrxvQlvJy3dYi%2Fb4bSyrnqHpcdfbm9rgu3cnMYevIH4v0Wpv%2FvP6WZvDdcH7h77CBjyJ%2FDFGFUZfFKrFGWdUWlv3g2vMJW5KLcvyMI0pZCETPZ%2B2%2BTYXC%2FuAQ2fpC4ncwHAT1Gbv%2F83FTZ0hfWreBm4vnXOHvvqI4yo%2FqVtxFH6vsSirwtUfJCg%2Bp8Ds0RfEXTU8ZjzETlRz0jaV1QXz8k0Yz52tF590e1WoriayFWn%2FW9P8I8ltOwGeZN9cteQeoONhrT0KMypFvFJxLxc7LzxuyZI2%2FlSFpFPJ%2FLg2QcY72d2YpITZyHVVutaMi3xlKm%2B6PbNc0PEyZ7Kvrmj6C9CQPP5qZH%2FxBv9iMVLtv1zYtcj6UrSaoI4n1NVSuzAqequiyJFseB1b%2F0C%2FRpyg5LN7iHjeYL0fKJUW3BHQU35VFMi8S9%2FDWdgBITmtmwLV4pTtMG6PeUqaNCkZCmUoesFc6HM%2B8iDBSXQbQl3z2qJ2oQBL7CSN66%2FeN2MoZl%2FvvcGIqRoj8LGRd6qIYNLHzE8iBygAMKXO67wGOqUBXQV1sWpc2ahdc%2FiOr1X5xDkR0LWLhUS2bYRLZOt09YWMbYEt41EEs2T5%2Bb2oWfYcZdv%2F9pW6MTMm0AMlN1fOFihYtZ0RS3qlCnTukhpX1yBSlJ6DV9LRHwHbFLDl58lYzAROd4eC20pXaLmFHg5vFE9QP%2B1TMI6E%2BLLOaq3tU%2BD7WPwPgPAuBhUH2mXD%2FQmOcGIalQ9tvKgBMfsQPWGltqaGuPRx&X-Amz-Signature=1e678b6b607b96efe5cc0b1746bc6832404355558fc14fd78ee9baa9e16ea7c0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKX2MKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAeAoRnljrndjf79BDjdDUTUAFyFdDm9IiLIiDYRdGrwIgTH8ECxpCS2uCoTtMJcyyW%2B3SvrCNlAoiQBTJTUMf%2Fx4qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlWPdEzPrtwrXVD7SrcAxXOM8XjRguTNiG%2BUMYuzVg1uYJrFFPXbr9xeto3u3G982jHXPCxF14998GTwQUC50ynNjVg0CGra9%2FSJTPwTvNQVHj9yZ1okrxvQlvJy3dYi%2Fb4bSyrnqHpcdfbm9rgu3cnMYevIH4v0Wpv%2FvP6WZvDdcH7h77CBjyJ%2FDFGFUZfFKrFGWdUWlv3g2vMJW5KLcvyMI0pZCETPZ%2B2%2BTYXC%2FuAQ2fpC4ncwHAT1Gbv%2F83FTZ0hfWreBm4vnXOHvvqI4yo%2FqVtxFH6vsSirwtUfJCg%2Bp8Ds0RfEXTU8ZjzETlRz0jaV1QXz8k0Yz52tF590e1WoriayFWn%2FW9P8I8ltOwGeZN9cteQeoONhrT0KMypFvFJxLxc7LzxuyZI2%2FlSFpFPJ%2FLg2QcY72d2YpITZyHVVutaMi3xlKm%2B6PbNc0PEyZ7Kvrmj6C9CQPP5qZH%2FxBv9iMVLtv1zYtcj6UrSaoI4n1NVSuzAqequiyJFseB1b%2F0C%2FRpyg5LN7iHjeYL0fKJUW3BHQU35VFMi8S9%2FDWdgBITmtmwLV4pTtMG6PeUqaNCkZCmUoesFc6HM%2B8iDBSXQbQl3z2qJ2oQBL7CSN66%2FeN2MoZl%2FvvcGIqRoj8LGRd6qIYNLHzE8iBygAMKXO67wGOqUBXQV1sWpc2ahdc%2FiOr1X5xDkR0LWLhUS2bYRLZOt09YWMbYEt41EEs2T5%2Bb2oWfYcZdv%2F9pW6MTMm0AMlN1fOFihYtZ0RS3qlCnTukhpX1yBSlJ6DV9LRHwHbFLDl58lYzAROd4eC20pXaLmFHg5vFE9QP%2B1TMI6E%2BLLOaq3tU%2BD7WPwPgPAuBhUH2mXD%2FQmOcGIalQ9tvKgBMfsQPWGltqaGuPRx&X-Amz-Signature=6e8a4ed0192d1944c96184ae3e0fc90fd9dded95d01d93f5c2fd036675296981&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKX2MKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAeAoRnljrndjf79BDjdDUTUAFyFdDm9IiLIiDYRdGrwIgTH8ECxpCS2uCoTtMJcyyW%2B3SvrCNlAoiQBTJTUMf%2Fx4qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlWPdEzPrtwrXVD7SrcAxXOM8XjRguTNiG%2BUMYuzVg1uYJrFFPXbr9xeto3u3G982jHXPCxF14998GTwQUC50ynNjVg0CGra9%2FSJTPwTvNQVHj9yZ1okrxvQlvJy3dYi%2Fb4bSyrnqHpcdfbm9rgu3cnMYevIH4v0Wpv%2FvP6WZvDdcH7h77CBjyJ%2FDFGFUZfFKrFGWdUWlv3g2vMJW5KLcvyMI0pZCETPZ%2B2%2BTYXC%2FuAQ2fpC4ncwHAT1Gbv%2F83FTZ0hfWreBm4vnXOHvvqI4yo%2FqVtxFH6vsSirwtUfJCg%2Bp8Ds0RfEXTU8ZjzETlRz0jaV1QXz8k0Yz52tF590e1WoriayFWn%2FW9P8I8ltOwGeZN9cteQeoONhrT0KMypFvFJxLxc7LzxuyZI2%2FlSFpFPJ%2FLg2QcY72d2YpITZyHVVutaMi3xlKm%2B6PbNc0PEyZ7Kvrmj6C9CQPP5qZH%2FxBv9iMVLtv1zYtcj6UrSaoI4n1NVSuzAqequiyJFseB1b%2F0C%2FRpyg5LN7iHjeYL0fKJUW3BHQU35VFMi8S9%2FDWdgBITmtmwLV4pTtMG6PeUqaNCkZCmUoesFc6HM%2B8iDBSXQbQl3z2qJ2oQBL7CSN66%2FeN2MoZl%2FvvcGIqRoj8LGRd6qIYNLHzE8iBygAMKXO67wGOqUBXQV1sWpc2ahdc%2FiOr1X5xDkR0LWLhUS2bYRLZOt09YWMbYEt41EEs2T5%2Bb2oWfYcZdv%2F9pW6MTMm0AMlN1fOFihYtZ0RS3qlCnTukhpX1yBSlJ6DV9LRHwHbFLDl58lYzAROd4eC20pXaLmFHg5vFE9QP%2B1TMI6E%2BLLOaq3tU%2BD7WPwPgPAuBhUH2mXD%2FQmOcGIalQ9tvKgBMfsQPWGltqaGuPRx&X-Amz-Signature=f4f7416664a60c982606f3d61958b0e62950be7029184925e818e3c7bd22d548&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKX2MKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAeAoRnljrndjf79BDjdDUTUAFyFdDm9IiLIiDYRdGrwIgTH8ECxpCS2uCoTtMJcyyW%2B3SvrCNlAoiQBTJTUMf%2Fx4qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlWPdEzPrtwrXVD7SrcAxXOM8XjRguTNiG%2BUMYuzVg1uYJrFFPXbr9xeto3u3G982jHXPCxF14998GTwQUC50ynNjVg0CGra9%2FSJTPwTvNQVHj9yZ1okrxvQlvJy3dYi%2Fb4bSyrnqHpcdfbm9rgu3cnMYevIH4v0Wpv%2FvP6WZvDdcH7h77CBjyJ%2FDFGFUZfFKrFGWdUWlv3g2vMJW5KLcvyMI0pZCETPZ%2B2%2BTYXC%2FuAQ2fpC4ncwHAT1Gbv%2F83FTZ0hfWreBm4vnXOHvvqI4yo%2FqVtxFH6vsSirwtUfJCg%2Bp8Ds0RfEXTU8ZjzETlRz0jaV1QXz8k0Yz52tF590e1WoriayFWn%2FW9P8I8ltOwGeZN9cteQeoONhrT0KMypFvFJxLxc7LzxuyZI2%2FlSFpFPJ%2FLg2QcY72d2YpITZyHVVutaMi3xlKm%2B6PbNc0PEyZ7Kvrmj6C9CQPP5qZH%2FxBv9iMVLtv1zYtcj6UrSaoI4n1NVSuzAqequiyJFseB1b%2F0C%2FRpyg5LN7iHjeYL0fKJUW3BHQU35VFMi8S9%2FDWdgBITmtmwLV4pTtMG6PeUqaNCkZCmUoesFc6HM%2B8iDBSXQbQl3z2qJ2oQBL7CSN66%2FeN2MoZl%2FvvcGIqRoj8LGRd6qIYNLHzE8iBygAMKXO67wGOqUBXQV1sWpc2ahdc%2FiOr1X5xDkR0LWLhUS2bYRLZOt09YWMbYEt41EEs2T5%2Bb2oWfYcZdv%2F9pW6MTMm0AMlN1fOFihYtZ0RS3qlCnTukhpX1yBSlJ6DV9LRHwHbFLDl58lYzAROd4eC20pXaLmFHg5vFE9QP%2B1TMI6E%2BLLOaq3tU%2BD7WPwPgPAuBhUH2mXD%2FQmOcGIalQ9tvKgBMfsQPWGltqaGuPRx&X-Amz-Signature=3b88efa5426b76c01545aaa56e33fd36da98c489ee92bf553ede2452776e6225&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKX2MKO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAeAoRnljrndjf79BDjdDUTUAFyFdDm9IiLIiDYRdGrwIgTH8ECxpCS2uCoTtMJcyyW%2B3SvrCNlAoiQBTJTUMf%2Fx4qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlWPdEzPrtwrXVD7SrcAxXOM8XjRguTNiG%2BUMYuzVg1uYJrFFPXbr9xeto3u3G982jHXPCxF14998GTwQUC50ynNjVg0CGra9%2FSJTPwTvNQVHj9yZ1okrxvQlvJy3dYi%2Fb4bSyrnqHpcdfbm9rgu3cnMYevIH4v0Wpv%2FvP6WZvDdcH7h77CBjyJ%2FDFGFUZfFKrFGWdUWlv3g2vMJW5KLcvyMI0pZCETPZ%2B2%2BTYXC%2FuAQ2fpC4ncwHAT1Gbv%2F83FTZ0hfWreBm4vnXOHvvqI4yo%2FqVtxFH6vsSirwtUfJCg%2Bp8Ds0RfEXTU8ZjzETlRz0jaV1QXz8k0Yz52tF590e1WoriayFWn%2FW9P8I8ltOwGeZN9cteQeoONhrT0KMypFvFJxLxc7LzxuyZI2%2FlSFpFPJ%2FLg2QcY72d2YpITZyHVVutaMi3xlKm%2B6PbNc0PEyZ7Kvrmj6C9CQPP5qZH%2FxBv9iMVLtv1zYtcj6UrSaoI4n1NVSuzAqequiyJFseB1b%2F0C%2FRpyg5LN7iHjeYL0fKJUW3BHQU35VFMi8S9%2FDWdgBITmtmwLV4pTtMG6PeUqaNCkZCmUoesFc6HM%2B8iDBSXQbQl3z2qJ2oQBL7CSN66%2FeN2MoZl%2FvvcGIqRoj8LGRd6qIYNLHzE8iBygAMKXO67wGOqUBXQV1sWpc2ahdc%2FiOr1X5xDkR0LWLhUS2bYRLZOt09YWMbYEt41EEs2T5%2Bb2oWfYcZdv%2F9pW6MTMm0AMlN1fOFihYtZ0RS3qlCnTukhpX1yBSlJ6DV9LRHwHbFLDl58lYzAROd4eC20pXaLmFHg5vFE9QP%2B1TMI6E%2BLLOaq3tU%2BD7WPwPgPAuBhUH2mXD%2FQmOcGIalQ9tvKgBMfsQPWGltqaGuPRx&X-Amz-Signature=5037dde46b23b2b8fc19cf9d4a93e980ba6929bcb0db15c7dbc54c82c3f8cded&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHONZZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7cp52fiSjAVgmC%2FeAa%2F8osSoHPnjAdgqDZ5oUcafuwIgMxR4rqEKz6eXVat9E08RPCWHcdugDHmsEXgae7lFSogqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGXm4g60n8Z8AfQWSrcAx1yP%2BCciZWwZPpC%2F0bXzi%2BVBzBQMcxp5EjrJMqCIiSxNbWwxG2Ek0R6DQIW4%2F99%2BlVqncATjfFdaVILiWlj14CvQ0fltKDt9Ef%2B8LncskR%2BsPOkCbb3iEAu%2Bvu7NBshrbkYf07BcJAOF7heVKzzMarZmFUS%2BHEDl2HCU4ffCNpBTG%2BCMt8ACy5L12cTqaPiNXPSNjgAqNbVu6mTCs5QftMccXy3IwONePD0%2FRxNcKevZ8c716IojPyPPCaGZ%2FL9vre1G4Hng8I1CyxfwDAYK7P2fzqT1iZ8f%2BeaLSwLTVWvCjukdQ0aaJjwknMQi2e2CWVIJaGpeZnIvXOE1xgdSkiyYGHVV1lQZJ7XkCpzItbS6XXh7hAfmmEtme858QKU8o2wr%2BCxfFCr2P309xxwZmc%2FSkDk%2F2NcnUF5ex7vWHI%2BenrByG85L5wARhM%2FblFGvTkAyWcdx%2Fj3UGr%2F%2BHhM1pyT%2BahBynhN3AobLYiXt1OG%2BlSpYGrfTcpS6sUVp0IW1ttS4DASp%2FjZMtd42rhRHTyTyWs8U0Pdh%2BYLu6u5z7ywvkNY7HvuR7D9SIlXvuvdyk6uAikoQMPGIN7tEvbAehZHy1ECyC3KzaPo7AmHDvxNNkfclyuh7QjEbTZsMObO67wGOqUBxLKN5%2B2WyguWBd%2B9QrkfzWeLEplYsOCYb3PZZrTHDgqqsK%2Fjow7lDCX5nUDMtSiuQ1LQV10niD0EskREFtxhHVkxO1fKIK3ZTAkkWLFNlo0h0XzC0fY9AHFBR6%2BUgGK8wRnfTHTymnineC3WSJB32QlFXxZpEf4EWMG14N0MixpCmIjiUmLQrWvFfj3uQ3H6f1lBoYsSxRTYISlrVPxjXjwzy1tb&X-Amz-Signature=b5b649e2946f2e15f538dc40d7577b76279f62094dad2b3d964f8ed57545999c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHONZZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7cp52fiSjAVgmC%2FeAa%2F8osSoHPnjAdgqDZ5oUcafuwIgMxR4rqEKz6eXVat9E08RPCWHcdugDHmsEXgae7lFSogqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGXm4g60n8Z8AfQWSrcAx1yP%2BCciZWwZPpC%2F0bXzi%2BVBzBQMcxp5EjrJMqCIiSxNbWwxG2Ek0R6DQIW4%2F99%2BlVqncATjfFdaVILiWlj14CvQ0fltKDt9Ef%2B8LncskR%2BsPOkCbb3iEAu%2Bvu7NBshrbkYf07BcJAOF7heVKzzMarZmFUS%2BHEDl2HCU4ffCNpBTG%2BCMt8ACy5L12cTqaPiNXPSNjgAqNbVu6mTCs5QftMccXy3IwONePD0%2FRxNcKevZ8c716IojPyPPCaGZ%2FL9vre1G4Hng8I1CyxfwDAYK7P2fzqT1iZ8f%2BeaLSwLTVWvCjukdQ0aaJjwknMQi2e2CWVIJaGpeZnIvXOE1xgdSkiyYGHVV1lQZJ7XkCpzItbS6XXh7hAfmmEtme858QKU8o2wr%2BCxfFCr2P309xxwZmc%2FSkDk%2F2NcnUF5ex7vWHI%2BenrByG85L5wARhM%2FblFGvTkAyWcdx%2Fj3UGr%2F%2BHhM1pyT%2BahBynhN3AobLYiXt1OG%2BlSpYGrfTcpS6sUVp0IW1ttS4DASp%2FjZMtd42rhRHTyTyWs8U0Pdh%2BYLu6u5z7ywvkNY7HvuR7D9SIlXvuvdyk6uAikoQMPGIN7tEvbAehZHy1ECyC3KzaPo7AmHDvxNNkfclyuh7QjEbTZsMObO67wGOqUBxLKN5%2B2WyguWBd%2B9QrkfzWeLEplYsOCYb3PZZrTHDgqqsK%2Fjow7lDCX5nUDMtSiuQ1LQV10niD0EskREFtxhHVkxO1fKIK3ZTAkkWLFNlo0h0XzC0fY9AHFBR6%2BUgGK8wRnfTHTymnineC3WSJB32QlFXxZpEf4EWMG14N0MixpCmIjiUmLQrWvFfj3uQ3H6f1lBoYsSxRTYISlrVPxjXjwzy1tb&X-Amz-Signature=5d75d55bca9b88d34ad41b4606c855275f9b65b1aef43bd24d91abd81082b13c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHONZZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7cp52fiSjAVgmC%2FeAa%2F8osSoHPnjAdgqDZ5oUcafuwIgMxR4rqEKz6eXVat9E08RPCWHcdugDHmsEXgae7lFSogqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGXm4g60n8Z8AfQWSrcAx1yP%2BCciZWwZPpC%2F0bXzi%2BVBzBQMcxp5EjrJMqCIiSxNbWwxG2Ek0R6DQIW4%2F99%2BlVqncATjfFdaVILiWlj14CvQ0fltKDt9Ef%2B8LncskR%2BsPOkCbb3iEAu%2Bvu7NBshrbkYf07BcJAOF7heVKzzMarZmFUS%2BHEDl2HCU4ffCNpBTG%2BCMt8ACy5L12cTqaPiNXPSNjgAqNbVu6mTCs5QftMccXy3IwONePD0%2FRxNcKevZ8c716IojPyPPCaGZ%2FL9vre1G4Hng8I1CyxfwDAYK7P2fzqT1iZ8f%2BeaLSwLTVWvCjukdQ0aaJjwknMQi2e2CWVIJaGpeZnIvXOE1xgdSkiyYGHVV1lQZJ7XkCpzItbS6XXh7hAfmmEtme858QKU8o2wr%2BCxfFCr2P309xxwZmc%2FSkDk%2F2NcnUF5ex7vWHI%2BenrByG85L5wARhM%2FblFGvTkAyWcdx%2Fj3UGr%2F%2BHhM1pyT%2BahBynhN3AobLYiXt1OG%2BlSpYGrfTcpS6sUVp0IW1ttS4DASp%2FjZMtd42rhRHTyTyWs8U0Pdh%2BYLu6u5z7ywvkNY7HvuR7D9SIlXvuvdyk6uAikoQMPGIN7tEvbAehZHy1ECyC3KzaPo7AmHDvxNNkfclyuh7QjEbTZsMObO67wGOqUBxLKN5%2B2WyguWBd%2B9QrkfzWeLEplYsOCYb3PZZrTHDgqqsK%2Fjow7lDCX5nUDMtSiuQ1LQV10niD0EskREFtxhHVkxO1fKIK3ZTAkkWLFNlo0h0XzC0fY9AHFBR6%2BUgGK8wRnfTHTymnineC3WSJB32QlFXxZpEf4EWMG14N0MixpCmIjiUmLQrWvFfj3uQ3H6f1lBoYsSxRTYISlrVPxjXjwzy1tb&X-Amz-Signature=09378826f31f21d685d17858fe1a267063f525f68fc883f9547920fdb0a0dbc0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHONZZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7cp52fiSjAVgmC%2FeAa%2F8osSoHPnjAdgqDZ5oUcafuwIgMxR4rqEKz6eXVat9E08RPCWHcdugDHmsEXgae7lFSogqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGXm4g60n8Z8AfQWSrcAx1yP%2BCciZWwZPpC%2F0bXzi%2BVBzBQMcxp5EjrJMqCIiSxNbWwxG2Ek0R6DQIW4%2F99%2BlVqncATjfFdaVILiWlj14CvQ0fltKDt9Ef%2B8LncskR%2BsPOkCbb3iEAu%2Bvu7NBshrbkYf07BcJAOF7heVKzzMarZmFUS%2BHEDl2HCU4ffCNpBTG%2BCMt8ACy5L12cTqaPiNXPSNjgAqNbVu6mTCs5QftMccXy3IwONePD0%2FRxNcKevZ8c716IojPyPPCaGZ%2FL9vre1G4Hng8I1CyxfwDAYK7P2fzqT1iZ8f%2BeaLSwLTVWvCjukdQ0aaJjwknMQi2e2CWVIJaGpeZnIvXOE1xgdSkiyYGHVV1lQZJ7XkCpzItbS6XXh7hAfmmEtme858QKU8o2wr%2BCxfFCr2P309xxwZmc%2FSkDk%2F2NcnUF5ex7vWHI%2BenrByG85L5wARhM%2FblFGvTkAyWcdx%2Fj3UGr%2F%2BHhM1pyT%2BahBynhN3AobLYiXt1OG%2BlSpYGrfTcpS6sUVp0IW1ttS4DASp%2FjZMtd42rhRHTyTyWs8U0Pdh%2BYLu6u5z7ywvkNY7HvuR7D9SIlXvuvdyk6uAikoQMPGIN7tEvbAehZHy1ECyC3KzaPo7AmHDvxNNkfclyuh7QjEbTZsMObO67wGOqUBxLKN5%2B2WyguWBd%2B9QrkfzWeLEplYsOCYb3PZZrTHDgqqsK%2Fjow7lDCX5nUDMtSiuQ1LQV10niD0EskREFtxhHVkxO1fKIK3ZTAkkWLFNlo0h0XzC0fY9AHFBR6%2BUgGK8wRnfTHTymnineC3WSJB32QlFXxZpEf4EWMG14N0MixpCmIjiUmLQrWvFfj3uQ3H6f1lBoYsSxRTYISlrVPxjXjwzy1tb&X-Amz-Signature=3bc6765f4bcb8b1d1fd2debd9cf760def75b13fa2103fc2c3095c5665041fba5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHONZZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7cp52fiSjAVgmC%2FeAa%2F8osSoHPnjAdgqDZ5oUcafuwIgMxR4rqEKz6eXVat9E08RPCWHcdugDHmsEXgae7lFSogqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGXm4g60n8Z8AfQWSrcAx1yP%2BCciZWwZPpC%2F0bXzi%2BVBzBQMcxp5EjrJMqCIiSxNbWwxG2Ek0R6DQIW4%2F99%2BlVqncATjfFdaVILiWlj14CvQ0fltKDt9Ef%2B8LncskR%2BsPOkCbb3iEAu%2Bvu7NBshrbkYf07BcJAOF7heVKzzMarZmFUS%2BHEDl2HCU4ffCNpBTG%2BCMt8ACy5L12cTqaPiNXPSNjgAqNbVu6mTCs5QftMccXy3IwONePD0%2FRxNcKevZ8c716IojPyPPCaGZ%2FL9vre1G4Hng8I1CyxfwDAYK7P2fzqT1iZ8f%2BeaLSwLTVWvCjukdQ0aaJjwknMQi2e2CWVIJaGpeZnIvXOE1xgdSkiyYGHVV1lQZJ7XkCpzItbS6XXh7hAfmmEtme858QKU8o2wr%2BCxfFCr2P309xxwZmc%2FSkDk%2F2NcnUF5ex7vWHI%2BenrByG85L5wARhM%2FblFGvTkAyWcdx%2Fj3UGr%2F%2BHhM1pyT%2BahBynhN3AobLYiXt1OG%2BlSpYGrfTcpS6sUVp0IW1ttS4DASp%2FjZMtd42rhRHTyTyWs8U0Pdh%2BYLu6u5z7ywvkNY7HvuR7D9SIlXvuvdyk6uAikoQMPGIN7tEvbAehZHy1ECyC3KzaPo7AmHDvxNNkfclyuh7QjEbTZsMObO67wGOqUBxLKN5%2B2WyguWBd%2B9QrkfzWeLEplYsOCYb3PZZrTHDgqqsK%2Fjow7lDCX5nUDMtSiuQ1LQV10niD0EskREFtxhHVkxO1fKIK3ZTAkkWLFNlo0h0XzC0fY9AHFBR6%2BUgGK8wRnfTHTymnineC3WSJB32QlFXxZpEf4EWMG14N0MixpCmIjiUmLQrWvFfj3uQ3H6f1lBoYsSxRTYISlrVPxjXjwzy1tb&X-Amz-Signature=dc6f61cc698e6bd4500e8e0020743f1b46e7529a166174ba83807c92df9253f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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


