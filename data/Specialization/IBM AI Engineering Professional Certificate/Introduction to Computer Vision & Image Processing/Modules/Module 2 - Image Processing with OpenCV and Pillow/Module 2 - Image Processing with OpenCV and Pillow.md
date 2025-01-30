

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=ef61e1b65e52a9fa72f8fd48b42c0d2335addbf8d06d8310aae3b3a5c3d932fd&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHFF7JP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEsrAk%2F2rnSZ20YUR9FINoGyA7ry1EGsMFHZcav0PTDAiEA4fHnWWhLOXVAd1cKf0aTNbtKji6MuJWl%2BjpS7kE%2FaKwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtKmlWi0UYCdJd63CrcA1Ne23kZSiK2fArZNopClhZCyauMJn4XIqxmF8l%2Fz4cC6Bdzhe3j6hY9n%2FyUSYUFRO1l4Lg4CzAETAAojIRSAgrJJ43QvT7x5VWfKVhRb6pMm1%2BOl0LSbUVxh6QOvxhBH%2FGCET5I0rlxxPtCBx7k%2BTupRzL0ypdIHUuSmgcml0UWPNqWyM4YLHKRz%2B7%2FrhM3OyWaFMlpOeHHAxPx53UMjb7hwFdBtOo8pXBZEO57%2B88BbZSaExqj%2F0SqJZeQ0pKT465CsI2J26Gj3WTisPYVzNQ%2BwJqa2Zs4aBsM3%2BxFjEdwtd4oQPuLw28kC0FFvQm10reJXTIeck1yYbHo1s78qbo6w3ZK2MmbRURLeT8alVSLy0uilg1O48klsDixj6Ob8%2Bzx8zV18cDbxfmIRcybUSR4vANcvVUmLNOo3EYB1cPIvpiprc2oTbPuz2UGMjI3njG5LihS2tQ8NLC0DvA0mdKbi2rJt3fIdO0uEF0vQE%2FGwDPVyuQJ89C2SIv8lZwJ%2FlIf7GD59%2BYGeddpvGJ0Rr7iqtbV7VKXpKi8F1k%2F5KgbnrAFYVc0fo0Nqsb0O6q7aa9uZZlflLjyisYgz1pQcmKOGQJv60Qu7N9dHyYYeimxOgKb6ol2ZQo1YFRNMMei7LwGOqUB602AsI71uxFG4Os%2FY2GogMq%2FiuqCgz3rlJZM8uxV6S1quzn8gEdaNuQBoS5g3iJTvrVtjnIlrWXK1vBwxMrO2SrZzBuqK8Aw5EU1fczKyAyOYG%2BIBL1A9vPKEPgB%2FNADtcGFwPUqF6iUgAa%2BKt0MI1zne%2F5PtAR8g9bSNYL0bjbeO84ww4GoZnyxecpxKKF3Qm6dVK8%2BLxmQftIOlkc67puXwoRE&X-Amz-Signature=60ddb3d35d7af7959797afd70907110b04bb29eff988e6b1e4a9719c2c6b82c4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHFF7JP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEsrAk%2F2rnSZ20YUR9FINoGyA7ry1EGsMFHZcav0PTDAiEA4fHnWWhLOXVAd1cKf0aTNbtKji6MuJWl%2BjpS7kE%2FaKwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtKmlWi0UYCdJd63CrcA1Ne23kZSiK2fArZNopClhZCyauMJn4XIqxmF8l%2Fz4cC6Bdzhe3j6hY9n%2FyUSYUFRO1l4Lg4CzAETAAojIRSAgrJJ43QvT7x5VWfKVhRb6pMm1%2BOl0LSbUVxh6QOvxhBH%2FGCET5I0rlxxPtCBx7k%2BTupRzL0ypdIHUuSmgcml0UWPNqWyM4YLHKRz%2B7%2FrhM3OyWaFMlpOeHHAxPx53UMjb7hwFdBtOo8pXBZEO57%2B88BbZSaExqj%2F0SqJZeQ0pKT465CsI2J26Gj3WTisPYVzNQ%2BwJqa2Zs4aBsM3%2BxFjEdwtd4oQPuLw28kC0FFvQm10reJXTIeck1yYbHo1s78qbo6w3ZK2MmbRURLeT8alVSLy0uilg1O48klsDixj6Ob8%2Bzx8zV18cDbxfmIRcybUSR4vANcvVUmLNOo3EYB1cPIvpiprc2oTbPuz2UGMjI3njG5LihS2tQ8NLC0DvA0mdKbi2rJt3fIdO0uEF0vQE%2FGwDPVyuQJ89C2SIv8lZwJ%2FlIf7GD59%2BYGeddpvGJ0Rr7iqtbV7VKXpKi8F1k%2F5KgbnrAFYVc0fo0Nqsb0O6q7aa9uZZlflLjyisYgz1pQcmKOGQJv60Qu7N9dHyYYeimxOgKb6ol2ZQo1YFRNMMei7LwGOqUB602AsI71uxFG4Os%2FY2GogMq%2FiuqCgz3rlJZM8uxV6S1quzn8gEdaNuQBoS5g3iJTvrVtjnIlrWXK1vBwxMrO2SrZzBuqK8Aw5EU1fczKyAyOYG%2BIBL1A9vPKEPgB%2FNADtcGFwPUqF6iUgAa%2BKt0MI1zne%2F5PtAR8g9bSNYL0bjbeO84ww4GoZnyxecpxKKF3Qm6dVK8%2BLxmQftIOlkc67puXwoRE&X-Amz-Signature=cfc4ce7630646a1e3c1a6e655635154ea429911716783d202e469b68bc8a61c8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHFF7JP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEsrAk%2F2rnSZ20YUR9FINoGyA7ry1EGsMFHZcav0PTDAiEA4fHnWWhLOXVAd1cKf0aTNbtKji6MuJWl%2BjpS7kE%2FaKwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtKmlWi0UYCdJd63CrcA1Ne23kZSiK2fArZNopClhZCyauMJn4XIqxmF8l%2Fz4cC6Bdzhe3j6hY9n%2FyUSYUFRO1l4Lg4CzAETAAojIRSAgrJJ43QvT7x5VWfKVhRb6pMm1%2BOl0LSbUVxh6QOvxhBH%2FGCET5I0rlxxPtCBx7k%2BTupRzL0ypdIHUuSmgcml0UWPNqWyM4YLHKRz%2B7%2FrhM3OyWaFMlpOeHHAxPx53UMjb7hwFdBtOo8pXBZEO57%2B88BbZSaExqj%2F0SqJZeQ0pKT465CsI2J26Gj3WTisPYVzNQ%2BwJqa2Zs4aBsM3%2BxFjEdwtd4oQPuLw28kC0FFvQm10reJXTIeck1yYbHo1s78qbo6w3ZK2MmbRURLeT8alVSLy0uilg1O48klsDixj6Ob8%2Bzx8zV18cDbxfmIRcybUSR4vANcvVUmLNOo3EYB1cPIvpiprc2oTbPuz2UGMjI3njG5LihS2tQ8NLC0DvA0mdKbi2rJt3fIdO0uEF0vQE%2FGwDPVyuQJ89C2SIv8lZwJ%2FlIf7GD59%2BYGeddpvGJ0Rr7iqtbV7VKXpKi8F1k%2F5KgbnrAFYVc0fo0Nqsb0O6q7aa9uZZlflLjyisYgz1pQcmKOGQJv60Qu7N9dHyYYeimxOgKb6ol2ZQo1YFRNMMei7LwGOqUB602AsI71uxFG4Os%2FY2GogMq%2FiuqCgz3rlJZM8uxV6S1quzn8gEdaNuQBoS5g3iJTvrVtjnIlrWXK1vBwxMrO2SrZzBuqK8Aw5EU1fczKyAyOYG%2BIBL1A9vPKEPgB%2FNADtcGFwPUqF6iUgAa%2BKt0MI1zne%2F5PtAR8g9bSNYL0bjbeO84ww4GoZnyxecpxKKF3Qm6dVK8%2BLxmQftIOlkc67puXwoRE&X-Amz-Signature=4b424efb77f3873735423700158856c1c622ac2d226739c843e9451aecd4972b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHFF7JP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEsrAk%2F2rnSZ20YUR9FINoGyA7ry1EGsMFHZcav0PTDAiEA4fHnWWhLOXVAd1cKf0aTNbtKji6MuJWl%2BjpS7kE%2FaKwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtKmlWi0UYCdJd63CrcA1Ne23kZSiK2fArZNopClhZCyauMJn4XIqxmF8l%2Fz4cC6Bdzhe3j6hY9n%2FyUSYUFRO1l4Lg4CzAETAAojIRSAgrJJ43QvT7x5VWfKVhRb6pMm1%2BOl0LSbUVxh6QOvxhBH%2FGCET5I0rlxxPtCBx7k%2BTupRzL0ypdIHUuSmgcml0UWPNqWyM4YLHKRz%2B7%2FrhM3OyWaFMlpOeHHAxPx53UMjb7hwFdBtOo8pXBZEO57%2B88BbZSaExqj%2F0SqJZeQ0pKT465CsI2J26Gj3WTisPYVzNQ%2BwJqa2Zs4aBsM3%2BxFjEdwtd4oQPuLw28kC0FFvQm10reJXTIeck1yYbHo1s78qbo6w3ZK2MmbRURLeT8alVSLy0uilg1O48klsDixj6Ob8%2Bzx8zV18cDbxfmIRcybUSR4vANcvVUmLNOo3EYB1cPIvpiprc2oTbPuz2UGMjI3njG5LihS2tQ8NLC0DvA0mdKbi2rJt3fIdO0uEF0vQE%2FGwDPVyuQJ89C2SIv8lZwJ%2FlIf7GD59%2BYGeddpvGJ0Rr7iqtbV7VKXpKi8F1k%2F5KgbnrAFYVc0fo0Nqsb0O6q7aa9uZZlflLjyisYgz1pQcmKOGQJv60Qu7N9dHyYYeimxOgKb6ol2ZQo1YFRNMMei7LwGOqUB602AsI71uxFG4Os%2FY2GogMq%2FiuqCgz3rlJZM8uxV6S1quzn8gEdaNuQBoS5g3iJTvrVtjnIlrWXK1vBwxMrO2SrZzBuqK8Aw5EU1fczKyAyOYG%2BIBL1A9vPKEPgB%2FNADtcGFwPUqF6iUgAa%2BKt0MI1zne%2F5PtAR8g9bSNYL0bjbeO84ww4GoZnyxecpxKKF3Qm6dVK8%2BLxmQftIOlkc67puXwoRE&X-Amz-Signature=05e1c4d732a936f77efff8d7e6e82186198804499e1e3d1a2a8bb99998de9dc3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHFF7JP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEsrAk%2F2rnSZ20YUR9FINoGyA7ry1EGsMFHZcav0PTDAiEA4fHnWWhLOXVAd1cKf0aTNbtKji6MuJWl%2BjpS7kE%2FaKwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtKmlWi0UYCdJd63CrcA1Ne23kZSiK2fArZNopClhZCyauMJn4XIqxmF8l%2Fz4cC6Bdzhe3j6hY9n%2FyUSYUFRO1l4Lg4CzAETAAojIRSAgrJJ43QvT7x5VWfKVhRb6pMm1%2BOl0LSbUVxh6QOvxhBH%2FGCET5I0rlxxPtCBx7k%2BTupRzL0ypdIHUuSmgcml0UWPNqWyM4YLHKRz%2B7%2FrhM3OyWaFMlpOeHHAxPx53UMjb7hwFdBtOo8pXBZEO57%2B88BbZSaExqj%2F0SqJZeQ0pKT465CsI2J26Gj3WTisPYVzNQ%2BwJqa2Zs4aBsM3%2BxFjEdwtd4oQPuLw28kC0FFvQm10reJXTIeck1yYbHo1s78qbo6w3ZK2MmbRURLeT8alVSLy0uilg1O48klsDixj6Ob8%2Bzx8zV18cDbxfmIRcybUSR4vANcvVUmLNOo3EYB1cPIvpiprc2oTbPuz2UGMjI3njG5LihS2tQ8NLC0DvA0mdKbi2rJt3fIdO0uEF0vQE%2FGwDPVyuQJ89C2SIv8lZwJ%2FlIf7GD59%2BYGeddpvGJ0Rr7iqtbV7VKXpKi8F1k%2F5KgbnrAFYVc0fo0Nqsb0O6q7aa9uZZlflLjyisYgz1pQcmKOGQJv60Qu7N9dHyYYeimxOgKb6ol2ZQo1YFRNMMei7LwGOqUB602AsI71uxFG4Os%2FY2GogMq%2FiuqCgz3rlJZM8uxV6S1quzn8gEdaNuQBoS5g3iJTvrVtjnIlrWXK1vBwxMrO2SrZzBuqK8Aw5EU1fczKyAyOYG%2BIBL1A9vPKEPgB%2FNADtcGFwPUqF6iUgAa%2BKt0MI1zne%2F5PtAR8g9bSNYL0bjbeO84ww4GoZnyxecpxKKF3Qm6dVK8%2BLxmQftIOlkc67puXwoRE&X-Amz-Signature=efbc1a7941bd12808853057b3c43d0530c4637e6d424b3135fd9842fae9f4228&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=f1ab10db7da333a0693c22efbe0953a0f195471a9a41305caadc18878d74b307&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=a01fed41852b5e616fcdc55197c0043a0e6ebfbc9f1750a7fb9b0a989f852d1e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=b662ae024c3debca418e881ad61f53caf0f9e2bc52ec4fb6b5ed08005cb29b1b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=ca7f665ad6517cc0fb8a9a848043a954eed887c106b51c2eeb9f4415da9c8e99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSRBKRZH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAI20Y%2FlnApVJrP7fOzbsPFD64MfACY8N2PoyfY6a%2FDsAiEAoIHbmBQJfw0T7TbAy9jAwwn7KP9leAyME%2Foj0njjYxYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDcXDUDaexvYMe8c0yrcA%2Fj33q4oWUooO%2FAG0nLbqT%2B1BgvF3%2F6iw5DbOM7N93%2B1%2FYwgIjoYIiEGv7EXzLlwkzF5%2FCfe6cqbuCIrX79Frbti0Qr943doNyfZloDq658K9xTBPpdl8JsLNZOORMny4AWQIj1ENV1C6Czn6k%2FIhVEgKrfqv60%2B9b6tN7DKEOwyF8uBiE4ggJ5FepadAk0LiF8U6NJ2y1n33G5boHy22QK80ZSbNuxK1o4TdG05qG%2F1f1jy8o%2Fx1UqBjlvyzTMZG3pqWe8LY17sAEtXo0vk8jAA4sz7so%2Fy4Y8iW1FAZnVhAu3z9s%2B%2FKPAoWKdLfQgMJyCWwHQaUC3AUtTdtxtwMV4vkV1y8uDixPAsL14QN4cedZJAPVE94de8rDIo0aZBuoOEjTrtyzkqz2Hk2baY35%2FCLuOjIWxMR2kYBp36sqld8OXYvEbfc9Nxyx84BOE9z%2F7gcd8CjMUKJRUGgrVExL2%2BV1cIvjz9IUo%2BGlAtir4er6GWp77TAQhDzlofiCGhaqqOTrn33RfrKo6NLn%2FlwUWROLpJv0ui4OjLTdc038MRNmhhHO2Eb7Jq7qQWXVbwv%2FEGCuJwUIyrIVmOjLVjS0tYjH9EDMX6I8mfcWAbYR96VhQtOe6aogmmm%2Bo8MPui7LwGOqUBwYE%2BrvsVqBc1deAP5fxSNbpGn95D3REXvzMKl9OSzGjcyFkWWUXsH1LUOZTiCtpYXIwt8zXMC8BzLWqFwV1GsEQc280tRtQhKjt%2BCuOKtLPvbKFjekNq5No1gnqXs10y6sJ3ildNJrpLf3xO7EV8%2B3wAITB4Rk97Km6TEXi22nQOSQ8MNJdmUtUGGR7vT2qCqsyBT4GW%2BBNcKEYUovjnrpflgpAq&X-Amz-Signature=6cdf158c62053a9015e715a4d08b32efdb7b7873488c998ff6eb526a3f475550&X-Amz-SignedHeaders=host&x-id=GetObject)
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


