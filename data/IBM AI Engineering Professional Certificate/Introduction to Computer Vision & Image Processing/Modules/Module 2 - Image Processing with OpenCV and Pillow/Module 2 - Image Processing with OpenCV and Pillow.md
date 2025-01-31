

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BDQQY7A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOU7DQ%2Br92IVhrpD2A0fVWQOvVqDVHOYSqqz1YhB3eBwIgEKUojlSGxZcR2uL7uyiMDyAMiznPBQ%2B9%2BQlzzY5ynKMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrH7SRcxlAv2V2PkSrcA5e44URmx1fSo7iHXqYeKkLl290o1HxL9dKr6ayzVR7l%2FaHPxz%2BsXX9G%2BxC4SnSqCpbLYzTUEoefDwfFfWV7bcROWPp2jT3%2BQ4zbuQk8R2zCE3ASzOGKNFCMqnxxiqHjSJq3wx9AXIbYVfBNBskBDK%2FbjU%2FbHGo8hrD3GBAlPw%2B1knY5xdOmTElTct1pQTNcggSnBF3thaPNMzldXMYFD117ZTnLgSWdVk4%2FvA9XAemObMDIlO%2FkjjXaKJEaddZ0nla06YwHs0i3kHwUDGC7FHx8w0yKEq2dmfeR%2FQSjhLC%2BXnrE3lJdgy%2BLYeAsE7hgrN2CPS9eP3ZjNiitdix3h86K%2Bsgo9%2Fpc391hW0xknQZLtu6%2B9QAj9K7DIcBr3%2FrUUE6SjT65DFIa94IDxNnxS%2BaUiegSc3Xnm9d%2FgKXBjE5bX1fC7p0qnvCqU9HWARco0TnS8cGmLP%2FwbIXV8MkDFM%2FXRXPa%2F5fDay%2FjI%2FD5z5o5ly21AjBf4puTRN6SZO9I1e4aaREdESJgr%2FNrWpGF47n84TBEdBeOFHYQSuIQ0a4Kb1rIQOn1c%2FiMqlMUUaATqsoNhcv2hfRy77EvbhrafYcCtz7sJmr%2Fgvrl3fxSq5DCPp8tkBa8hMepAL6uMLXA9LwGOqUBhdjts3jpkMgJ2WYvBhVhJkkAdEAtnMsssLCX91qYIU9mF6MgX%2Bz8ilGb3sey%2FzbQrj6jlVgPeIClYhgdgQxDjAYto83qKU9TxqwMJeyRVZSFb1ANWw%2BHJwuoeiPtDb%2Bo2JgbQ7RXOivuczkRtboJirWR3PgLWKcv%2BmEZonV76lOr%2BLOh%2F9aBU2RJYPtm161r4oHSKqjjqjDcfQ4u2xYhZKaFnFJD&X-Amz-Signature=01de75fb9cae2a5a80f8bb9443fddbf62b2089419806ca1ab8bf72e65f303940&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GPBT6QK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVIB5JnInmb2KZrIIEdpbWk2vhvUeCGyvX9n6cfB7TqQIgFH%2FtVMYEhO8PS%2F1swyCivfrwx1mHyLurPiHGKP%2FhZ%2FIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjuDJ%2FcSP9EOXw%2FcyrcA188MHKjhmbiKDwkJmLsPLzEmWCGUcuDTb8Ockbxe3DRi%2FG3YVz07Dizg4q925L98ErVTPYCbam4sMugKOAMsxADGKbtY8znwARlwVZxKpggZ7XzizD5RX7bFa5qSsCW%2FncY8pEOdDe8aEKYASlInBl5cTV%2BU%2FdWqZNnDS2fCx8d2afwJccOP%2FNYIBRtrc4c8LETAQj%2B0M9WkBFRjBxxWWV8RgvmmCEik1xIW3Up8sWDPgQ5Xi4P6wCRUWxftRSFk2b3VD2s3Sze2ExXD0hCBnw6EGWG2o%2BO9XGEgxnFmxwnja0lnwZF9nwEliyQFOFYK1XqEGWN8CfSNtXAZWfJV0SWfKe%2FZ%2B%2B9Ej2sBBSBj%2Bff3865SnbcrDUciL94HuKoYRE9fQpnyW%2FfZKcm4ybnI7G0lLCcdA3%2BNasj6hTXgVQLhWZJ5GPNSR9K4sgpIIoBd4%2B7VkIGj%2BQ9uQFMDB2TAnlRRtRaLUBYToc45Y6WuaU9m0UyUnolEDsxWv8p24EEiFbbDa5eo%2FIvai3pIkHk4ghAJSN5tiqiFvYyJ65ncNnIoxX7F7ViiIi1JVL5CjQ6G66bshVgrkPnenTDOo01uy6l2QM3C8N54F%2FR21zF8PF5o3GIvE3RroB0Fj0RMIOk9LwGOqUBjm7%2F%2BhocpWKYULtvuRiimyV9K7e0lWCq23cm29yRkJCIgUvpO59%2BiLNJ1f1R7BGzPLtR2dMvkiWuL3RUZTEPPIXmwvsYcibQWto2DlR56KWJVfzwEo%2BXvqRhFUNz3cnFitAqqeLCdI4E6ksUf35Mtyd1%2F6WY2lucBtOmSs2r3lRWr3BABBFDy8zkUEb4fx2A6FIkrGTqnMlH630fcWAMPchCW0y1&X-Amz-Signature=b7266574c310c835ed098aa3d42b4df7ee9afabc997a2656c99ab80494f3b0b3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GPBT6QK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVIB5JnInmb2KZrIIEdpbWk2vhvUeCGyvX9n6cfB7TqQIgFH%2FtVMYEhO8PS%2F1swyCivfrwx1mHyLurPiHGKP%2FhZ%2FIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjuDJ%2FcSP9EOXw%2FcyrcA188MHKjhmbiKDwkJmLsPLzEmWCGUcuDTb8Ockbxe3DRi%2FG3YVz07Dizg4q925L98ErVTPYCbam4sMugKOAMsxADGKbtY8znwARlwVZxKpggZ7XzizD5RX7bFa5qSsCW%2FncY8pEOdDe8aEKYASlInBl5cTV%2BU%2FdWqZNnDS2fCx8d2afwJccOP%2FNYIBRtrc4c8LETAQj%2B0M9WkBFRjBxxWWV8RgvmmCEik1xIW3Up8sWDPgQ5Xi4P6wCRUWxftRSFk2b3VD2s3Sze2ExXD0hCBnw6EGWG2o%2BO9XGEgxnFmxwnja0lnwZF9nwEliyQFOFYK1XqEGWN8CfSNtXAZWfJV0SWfKe%2FZ%2B%2B9Ej2sBBSBj%2Bff3865SnbcrDUciL94HuKoYRE9fQpnyW%2FfZKcm4ybnI7G0lLCcdA3%2BNasj6hTXgVQLhWZJ5GPNSR9K4sgpIIoBd4%2B7VkIGj%2BQ9uQFMDB2TAnlRRtRaLUBYToc45Y6WuaU9m0UyUnolEDsxWv8p24EEiFbbDa5eo%2FIvai3pIkHk4ghAJSN5tiqiFvYyJ65ncNnIoxX7F7ViiIi1JVL5CjQ6G66bshVgrkPnenTDOo01uy6l2QM3C8N54F%2FR21zF8PF5o3GIvE3RroB0Fj0RMIOk9LwGOqUBjm7%2F%2BhocpWKYULtvuRiimyV9K7e0lWCq23cm29yRkJCIgUvpO59%2BiLNJ1f1R7BGzPLtR2dMvkiWuL3RUZTEPPIXmwvsYcibQWto2DlR56KWJVfzwEo%2BXvqRhFUNz3cnFitAqqeLCdI4E6ksUf35Mtyd1%2F6WY2lucBtOmSs2r3lRWr3BABBFDy8zkUEb4fx2A6FIkrGTqnMlH630fcWAMPchCW0y1&X-Amz-Signature=d5300669e2b19cdc71909f21b9aac5202f5a3765df7998e8a268796efa07193f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GPBT6QK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVIB5JnInmb2KZrIIEdpbWk2vhvUeCGyvX9n6cfB7TqQIgFH%2FtVMYEhO8PS%2F1swyCivfrwx1mHyLurPiHGKP%2FhZ%2FIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjuDJ%2FcSP9EOXw%2FcyrcA188MHKjhmbiKDwkJmLsPLzEmWCGUcuDTb8Ockbxe3DRi%2FG3YVz07Dizg4q925L98ErVTPYCbam4sMugKOAMsxADGKbtY8znwARlwVZxKpggZ7XzizD5RX7bFa5qSsCW%2FncY8pEOdDe8aEKYASlInBl5cTV%2BU%2FdWqZNnDS2fCx8d2afwJccOP%2FNYIBRtrc4c8LETAQj%2B0M9WkBFRjBxxWWV8RgvmmCEik1xIW3Up8sWDPgQ5Xi4P6wCRUWxftRSFk2b3VD2s3Sze2ExXD0hCBnw6EGWG2o%2BO9XGEgxnFmxwnja0lnwZF9nwEliyQFOFYK1XqEGWN8CfSNtXAZWfJV0SWfKe%2FZ%2B%2B9Ej2sBBSBj%2Bff3865SnbcrDUciL94HuKoYRE9fQpnyW%2FfZKcm4ybnI7G0lLCcdA3%2BNasj6hTXgVQLhWZJ5GPNSR9K4sgpIIoBd4%2B7VkIGj%2BQ9uQFMDB2TAnlRRtRaLUBYToc45Y6WuaU9m0UyUnolEDsxWv8p24EEiFbbDa5eo%2FIvai3pIkHk4ghAJSN5tiqiFvYyJ65ncNnIoxX7F7ViiIi1JVL5CjQ6G66bshVgrkPnenTDOo01uy6l2QM3C8N54F%2FR21zF8PF5o3GIvE3RroB0Fj0RMIOk9LwGOqUBjm7%2F%2BhocpWKYULtvuRiimyV9K7e0lWCq23cm29yRkJCIgUvpO59%2BiLNJ1f1R7BGzPLtR2dMvkiWuL3RUZTEPPIXmwvsYcibQWto2DlR56KWJVfzwEo%2BXvqRhFUNz3cnFitAqqeLCdI4E6ksUf35Mtyd1%2F6WY2lucBtOmSs2r3lRWr3BABBFDy8zkUEb4fx2A6FIkrGTqnMlH630fcWAMPchCW0y1&X-Amz-Signature=ec70f2afffc662f5af14085194ec447aec6db89865a0e8f41d4b1b9c1195ebf6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GPBT6QK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVIB5JnInmb2KZrIIEdpbWk2vhvUeCGyvX9n6cfB7TqQIgFH%2FtVMYEhO8PS%2F1swyCivfrwx1mHyLurPiHGKP%2FhZ%2FIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjuDJ%2FcSP9EOXw%2FcyrcA188MHKjhmbiKDwkJmLsPLzEmWCGUcuDTb8Ockbxe3DRi%2FG3YVz07Dizg4q925L98ErVTPYCbam4sMugKOAMsxADGKbtY8znwARlwVZxKpggZ7XzizD5RX7bFa5qSsCW%2FncY8pEOdDe8aEKYASlInBl5cTV%2BU%2FdWqZNnDS2fCx8d2afwJccOP%2FNYIBRtrc4c8LETAQj%2B0M9WkBFRjBxxWWV8RgvmmCEik1xIW3Up8sWDPgQ5Xi4P6wCRUWxftRSFk2b3VD2s3Sze2ExXD0hCBnw6EGWG2o%2BO9XGEgxnFmxwnja0lnwZF9nwEliyQFOFYK1XqEGWN8CfSNtXAZWfJV0SWfKe%2FZ%2B%2B9Ej2sBBSBj%2Bff3865SnbcrDUciL94HuKoYRE9fQpnyW%2FfZKcm4ybnI7G0lLCcdA3%2BNasj6hTXgVQLhWZJ5GPNSR9K4sgpIIoBd4%2B7VkIGj%2BQ9uQFMDB2TAnlRRtRaLUBYToc45Y6WuaU9m0UyUnolEDsxWv8p24EEiFbbDa5eo%2FIvai3pIkHk4ghAJSN5tiqiFvYyJ65ncNnIoxX7F7ViiIi1JVL5CjQ6G66bshVgrkPnenTDOo01uy6l2QM3C8N54F%2FR21zF8PF5o3GIvE3RroB0Fj0RMIOk9LwGOqUBjm7%2F%2BhocpWKYULtvuRiimyV9K7e0lWCq23cm29yRkJCIgUvpO59%2BiLNJ1f1R7BGzPLtR2dMvkiWuL3RUZTEPPIXmwvsYcibQWto2DlR56KWJVfzwEo%2BXvqRhFUNz3cnFitAqqeLCdI4E6ksUf35Mtyd1%2F6WY2lucBtOmSs2r3lRWr3BABBFDy8zkUEb4fx2A6FIkrGTqnMlH630fcWAMPchCW0y1&X-Amz-Signature=e0b88e9ce69cd9f9de6afb79d674bb877d0703709ed83d774e5253ddf0fa47a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GPBT6QK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVIB5JnInmb2KZrIIEdpbWk2vhvUeCGyvX9n6cfB7TqQIgFH%2FtVMYEhO8PS%2F1swyCivfrwx1mHyLurPiHGKP%2FhZ%2FIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjuDJ%2FcSP9EOXw%2FcyrcA188MHKjhmbiKDwkJmLsPLzEmWCGUcuDTb8Ockbxe3DRi%2FG3YVz07Dizg4q925L98ErVTPYCbam4sMugKOAMsxADGKbtY8znwARlwVZxKpggZ7XzizD5RX7bFa5qSsCW%2FncY8pEOdDe8aEKYASlInBl5cTV%2BU%2FdWqZNnDS2fCx8d2afwJccOP%2FNYIBRtrc4c8LETAQj%2B0M9WkBFRjBxxWWV8RgvmmCEik1xIW3Up8sWDPgQ5Xi4P6wCRUWxftRSFk2b3VD2s3Sze2ExXD0hCBnw6EGWG2o%2BO9XGEgxnFmxwnja0lnwZF9nwEliyQFOFYK1XqEGWN8CfSNtXAZWfJV0SWfKe%2FZ%2B%2B9Ej2sBBSBj%2Bff3865SnbcrDUciL94HuKoYRE9fQpnyW%2FfZKcm4ybnI7G0lLCcdA3%2BNasj6hTXgVQLhWZJ5GPNSR9K4sgpIIoBd4%2B7VkIGj%2BQ9uQFMDB2TAnlRRtRaLUBYToc45Y6WuaU9m0UyUnolEDsxWv8p24EEiFbbDa5eo%2FIvai3pIkHk4ghAJSN5tiqiFvYyJ65ncNnIoxX7F7ViiIi1JVL5CjQ6G66bshVgrkPnenTDOo01uy6l2QM3C8N54F%2FR21zF8PF5o3GIvE3RroB0Fj0RMIOk9LwGOqUBjm7%2F%2BhocpWKYULtvuRiimyV9K7e0lWCq23cm29yRkJCIgUvpO59%2BiLNJ1f1R7BGzPLtR2dMvkiWuL3RUZTEPPIXmwvsYcibQWto2DlR56KWJVfzwEo%2BXvqRhFUNz3cnFitAqqeLCdI4E6ksUf35Mtyd1%2F6WY2lucBtOmSs2r3lRWr3BABBFDy8zkUEb4fx2A6FIkrGTqnMlH630fcWAMPchCW0y1&X-Amz-Signature=b889362921511691732a8e2dd497dea36e9155b50bd69d5c03617e20ddc1e45e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BDQQY7A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOU7DQ%2Br92IVhrpD2A0fVWQOvVqDVHOYSqqz1YhB3eBwIgEKUojlSGxZcR2uL7uyiMDyAMiznPBQ%2B9%2BQlzzY5ynKMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrH7SRcxlAv2V2PkSrcA5e44URmx1fSo7iHXqYeKkLl290o1HxL9dKr6ayzVR7l%2FaHPxz%2BsXX9G%2BxC4SnSqCpbLYzTUEoefDwfFfWV7bcROWPp2jT3%2BQ4zbuQk8R2zCE3ASzOGKNFCMqnxxiqHjSJq3wx9AXIbYVfBNBskBDK%2FbjU%2FbHGo8hrD3GBAlPw%2B1knY5xdOmTElTct1pQTNcggSnBF3thaPNMzldXMYFD117ZTnLgSWdVk4%2FvA9XAemObMDIlO%2FkjjXaKJEaddZ0nla06YwHs0i3kHwUDGC7FHx8w0yKEq2dmfeR%2FQSjhLC%2BXnrE3lJdgy%2BLYeAsE7hgrN2CPS9eP3ZjNiitdix3h86K%2Bsgo9%2Fpc391hW0xknQZLtu6%2B9QAj9K7DIcBr3%2FrUUE6SjT65DFIa94IDxNnxS%2BaUiegSc3Xnm9d%2FgKXBjE5bX1fC7p0qnvCqU9HWARco0TnS8cGmLP%2FwbIXV8MkDFM%2FXRXPa%2F5fDay%2FjI%2FD5z5o5ly21AjBf4puTRN6SZO9I1e4aaREdESJgr%2FNrWpGF47n84TBEdBeOFHYQSuIQ0a4Kb1rIQOn1c%2FiMqlMUUaATqsoNhcv2hfRy77EvbhrafYcCtz7sJmr%2Fgvrl3fxSq5DCPp8tkBa8hMepAL6uMLXA9LwGOqUBhdjts3jpkMgJ2WYvBhVhJkkAdEAtnMsssLCX91qYIU9mF6MgX%2Bz8ilGb3sey%2FzbQrj6jlVgPeIClYhgdgQxDjAYto83qKU9TxqwMJeyRVZSFb1ANWw%2BHJwuoeiPtDb%2Bo2JgbQ7RXOivuczkRtboJirWR3PgLWKcv%2BmEZonV76lOr%2BLOh%2F9aBU2RJYPtm161r4oHSKqjjqjDcfQ4u2xYhZKaFnFJD&X-Amz-Signature=f327d917c1b8bcb8d79ac7b76fe840f16ef3d635a296d9cbaab8ad1963b086b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BDQQY7A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOU7DQ%2Br92IVhrpD2A0fVWQOvVqDVHOYSqqz1YhB3eBwIgEKUojlSGxZcR2uL7uyiMDyAMiznPBQ%2B9%2BQlzzY5ynKMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrH7SRcxlAv2V2PkSrcA5e44URmx1fSo7iHXqYeKkLl290o1HxL9dKr6ayzVR7l%2FaHPxz%2BsXX9G%2BxC4SnSqCpbLYzTUEoefDwfFfWV7bcROWPp2jT3%2BQ4zbuQk8R2zCE3ASzOGKNFCMqnxxiqHjSJq3wx9AXIbYVfBNBskBDK%2FbjU%2FbHGo8hrD3GBAlPw%2B1knY5xdOmTElTct1pQTNcggSnBF3thaPNMzldXMYFD117ZTnLgSWdVk4%2FvA9XAemObMDIlO%2FkjjXaKJEaddZ0nla06YwHs0i3kHwUDGC7FHx8w0yKEq2dmfeR%2FQSjhLC%2BXnrE3lJdgy%2BLYeAsE7hgrN2CPS9eP3ZjNiitdix3h86K%2Bsgo9%2Fpc391hW0xknQZLtu6%2B9QAj9K7DIcBr3%2FrUUE6SjT65DFIa94IDxNnxS%2BaUiegSc3Xnm9d%2FgKXBjE5bX1fC7p0qnvCqU9HWARco0TnS8cGmLP%2FwbIXV8MkDFM%2FXRXPa%2F5fDay%2FjI%2FD5z5o5ly21AjBf4puTRN6SZO9I1e4aaREdESJgr%2FNrWpGF47n84TBEdBeOFHYQSuIQ0a4Kb1rIQOn1c%2FiMqlMUUaATqsoNhcv2hfRy77EvbhrafYcCtz7sJmr%2Fgvrl3fxSq5DCPp8tkBa8hMepAL6uMLXA9LwGOqUBhdjts3jpkMgJ2WYvBhVhJkkAdEAtnMsssLCX91qYIU9mF6MgX%2Bz8ilGb3sey%2FzbQrj6jlVgPeIClYhgdgQxDjAYto83qKU9TxqwMJeyRVZSFb1ANWw%2BHJwuoeiPtDb%2Bo2JgbQ7RXOivuczkRtboJirWR3PgLWKcv%2BmEZonV76lOr%2BLOh%2F9aBU2RJYPtm161r4oHSKqjjqjDcfQ4u2xYhZKaFnFJD&X-Amz-Signature=ce09e3293f7d28b05ced08defa7c11d188f8262046e0d782b2fc8581c93d6b4a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BDQQY7A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOU7DQ%2Br92IVhrpD2A0fVWQOvVqDVHOYSqqz1YhB3eBwIgEKUojlSGxZcR2uL7uyiMDyAMiznPBQ%2B9%2BQlzzY5ynKMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrH7SRcxlAv2V2PkSrcA5e44URmx1fSo7iHXqYeKkLl290o1HxL9dKr6ayzVR7l%2FaHPxz%2BsXX9G%2BxC4SnSqCpbLYzTUEoefDwfFfWV7bcROWPp2jT3%2BQ4zbuQk8R2zCE3ASzOGKNFCMqnxxiqHjSJq3wx9AXIbYVfBNBskBDK%2FbjU%2FbHGo8hrD3GBAlPw%2B1knY5xdOmTElTct1pQTNcggSnBF3thaPNMzldXMYFD117ZTnLgSWdVk4%2FvA9XAemObMDIlO%2FkjjXaKJEaddZ0nla06YwHs0i3kHwUDGC7FHx8w0yKEq2dmfeR%2FQSjhLC%2BXnrE3lJdgy%2BLYeAsE7hgrN2CPS9eP3ZjNiitdix3h86K%2Bsgo9%2Fpc391hW0xknQZLtu6%2B9QAj9K7DIcBr3%2FrUUE6SjT65DFIa94IDxNnxS%2BaUiegSc3Xnm9d%2FgKXBjE5bX1fC7p0qnvCqU9HWARco0TnS8cGmLP%2FwbIXV8MkDFM%2FXRXPa%2F5fDay%2FjI%2FD5z5o5ly21AjBf4puTRN6SZO9I1e4aaREdESJgr%2FNrWpGF47n84TBEdBeOFHYQSuIQ0a4Kb1rIQOn1c%2FiMqlMUUaATqsoNhcv2hfRy77EvbhrafYcCtz7sJmr%2Fgvrl3fxSq5DCPp8tkBa8hMepAL6uMLXA9LwGOqUBhdjts3jpkMgJ2WYvBhVhJkkAdEAtnMsssLCX91qYIU9mF6MgX%2Bz8ilGb3sey%2FzbQrj6jlVgPeIClYhgdgQxDjAYto83qKU9TxqwMJeyRVZSFb1ANWw%2BHJwuoeiPtDb%2Bo2JgbQ7RXOivuczkRtboJirWR3PgLWKcv%2BmEZonV76lOr%2BLOh%2F9aBU2RJYPtm161r4oHSKqjjqjDcfQ4u2xYhZKaFnFJD&X-Amz-Signature=b499838d43beec62958e3cc159e5b9db2b3ba9338d95c59f5ba69eb651aaa4df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BDQQY7A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOU7DQ%2Br92IVhrpD2A0fVWQOvVqDVHOYSqqz1YhB3eBwIgEKUojlSGxZcR2uL7uyiMDyAMiznPBQ%2B9%2BQlzzY5ynKMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrH7SRcxlAv2V2PkSrcA5e44URmx1fSo7iHXqYeKkLl290o1HxL9dKr6ayzVR7l%2FaHPxz%2BsXX9G%2BxC4SnSqCpbLYzTUEoefDwfFfWV7bcROWPp2jT3%2BQ4zbuQk8R2zCE3ASzOGKNFCMqnxxiqHjSJq3wx9AXIbYVfBNBskBDK%2FbjU%2FbHGo8hrD3GBAlPw%2B1knY5xdOmTElTct1pQTNcggSnBF3thaPNMzldXMYFD117ZTnLgSWdVk4%2FvA9XAemObMDIlO%2FkjjXaKJEaddZ0nla06YwHs0i3kHwUDGC7FHx8w0yKEq2dmfeR%2FQSjhLC%2BXnrE3lJdgy%2BLYeAsE7hgrN2CPS9eP3ZjNiitdix3h86K%2Bsgo9%2Fpc391hW0xknQZLtu6%2B9QAj9K7DIcBr3%2FrUUE6SjT65DFIa94IDxNnxS%2BaUiegSc3Xnm9d%2FgKXBjE5bX1fC7p0qnvCqU9HWARco0TnS8cGmLP%2FwbIXV8MkDFM%2FXRXPa%2F5fDay%2FjI%2FD5z5o5ly21AjBf4puTRN6SZO9I1e4aaREdESJgr%2FNrWpGF47n84TBEdBeOFHYQSuIQ0a4Kb1rIQOn1c%2FiMqlMUUaATqsoNhcv2hfRy77EvbhrafYcCtz7sJmr%2Fgvrl3fxSq5DCPp8tkBa8hMepAL6uMLXA9LwGOqUBhdjts3jpkMgJ2WYvBhVhJkkAdEAtnMsssLCX91qYIU9mF6MgX%2Bz8ilGb3sey%2FzbQrj6jlVgPeIClYhgdgQxDjAYto83qKU9TxqwMJeyRVZSFb1ANWw%2BHJwuoeiPtDb%2Bo2JgbQ7RXOivuczkRtboJirWR3PgLWKcv%2BmEZonV76lOr%2BLOh%2F9aBU2RJYPtm161r4oHSKqjjqjDcfQ4u2xYhZKaFnFJD&X-Amz-Signature=ca788b78d620379f01a03b0e4fc0c748465ce322afd41bef3b264a62cd4261eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BDQQY7A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOU7DQ%2Br92IVhrpD2A0fVWQOvVqDVHOYSqqz1YhB3eBwIgEKUojlSGxZcR2uL7uyiMDyAMiznPBQ%2B9%2BQlzzY5ynKMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrH7SRcxlAv2V2PkSrcA5e44URmx1fSo7iHXqYeKkLl290o1HxL9dKr6ayzVR7l%2FaHPxz%2BsXX9G%2BxC4SnSqCpbLYzTUEoefDwfFfWV7bcROWPp2jT3%2BQ4zbuQk8R2zCE3ASzOGKNFCMqnxxiqHjSJq3wx9AXIbYVfBNBskBDK%2FbjU%2FbHGo8hrD3GBAlPw%2B1knY5xdOmTElTct1pQTNcggSnBF3thaPNMzldXMYFD117ZTnLgSWdVk4%2FvA9XAemObMDIlO%2FkjjXaKJEaddZ0nla06YwHs0i3kHwUDGC7FHx8w0yKEq2dmfeR%2FQSjhLC%2BXnrE3lJdgy%2BLYeAsE7hgrN2CPS9eP3ZjNiitdix3h86K%2Bsgo9%2Fpc391hW0xknQZLtu6%2B9QAj9K7DIcBr3%2FrUUE6SjT65DFIa94IDxNnxS%2BaUiegSc3Xnm9d%2FgKXBjE5bX1fC7p0qnvCqU9HWARco0TnS8cGmLP%2FwbIXV8MkDFM%2FXRXPa%2F5fDay%2FjI%2FD5z5o5ly21AjBf4puTRN6SZO9I1e4aaREdESJgr%2FNrWpGF47n84TBEdBeOFHYQSuIQ0a4Kb1rIQOn1c%2FiMqlMUUaATqsoNhcv2hfRy77EvbhrafYcCtz7sJmr%2Fgvrl3fxSq5DCPp8tkBa8hMepAL6uMLXA9LwGOqUBhdjts3jpkMgJ2WYvBhVhJkkAdEAtnMsssLCX91qYIU9mF6MgX%2Bz8ilGb3sey%2FzbQrj6jlVgPeIClYhgdgQxDjAYto83qKU9TxqwMJeyRVZSFb1ANWw%2BHJwuoeiPtDb%2Bo2JgbQ7RXOivuczkRtboJirWR3PgLWKcv%2BmEZonV76lOr%2BLOh%2F9aBU2RJYPtm161r4oHSKqjjqjDcfQ4u2xYhZKaFnFJD&X-Amz-Signature=ab5b289af66560d389ab4fa9834eb3484605ecda6c91862e09967c18b218832b&X-Amz-SignedHeaders=host&x-id=GetObject)
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


