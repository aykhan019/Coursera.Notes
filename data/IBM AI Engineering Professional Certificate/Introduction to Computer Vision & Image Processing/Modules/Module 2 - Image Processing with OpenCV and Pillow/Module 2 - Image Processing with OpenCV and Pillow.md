

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOLZ7HY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBP8r%2F0D6b0prb0AEGq6KU7LSne2ZE4HNEwk0aEPxNyCAiAEm3L7wQb8Lu7aCnzrHNvkWVJ4ZN8zndlLVDyY8JigpyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2uMkxqd1U15%2FHC24KtwDvhowv1iffUi09lArAb55RsrQyfBLvctPFkjdfH2WGYVk2midUoIcuvUkpr%2FKcRVo8%2FLgi%2FlZ9BoB4PMKwc%2FI1Mu9vJZxcxpcC20cq5yZDx%2FsgESBuTbe7jSpMkZj2tkEuYirjKadPeKrCJh5TFTeAiqNesTjoSaxSsw%2BJlgehyuV21rKW%2FxaZ1avg4KS%2BthJQZhVjQgk%2F0wMsFT4IDctvVqAxz1fmcHjKVpbU0xTq%2FhXu06leAx6ucSrweU7j18RqDiRS44ZoeeCXAz%2BGEhpxhJ2JG8kVU2RyEWukJJUImFUgt3vepd%2FgXpNCnTwHZF1ET0gpiN%2B0BW2KKAFcrgyN2J3d8GEKiixZHOp3rBQOpAlArgO5PW9AdY4GNRf%2FFdtC5wVKWAN178rWDp6njiG%2FrQdnRWd3%2BFm3IVDjHsLJyHehG4TrGMNNGPyWJbGMHk1kBV7fAgb%2FHwV%2BAtR4wJKYqzM2ANagUGxuRN%2BpdB58Pbd3WnIrM%2FxPdbHffPhzwo8PDcpK9JF6%2B2y7Rtyl9%2BxmaymKtO8dqsyTTIntxgcZoIQNwnRZHcPqWadWPUW7g56wdeVBOgxxfBEaNGsrb1ir16%2Fz29cLKn9UNxjQiEyyBg6P2lv8Sc2wipEa7kw9pP6vAY6pgH%2FxS4Do2cTJjMkcW0AxWjhZfCldgqvmet8p4kApoLAAKSMGxeAJ1vIUdUlz5aYNU826D%2FTOVz95CcGH1WL%2FdvIwjojZkshD9gHhRNhqNVNyKWrbVVvNDQAU98ovldWQPR6ryQMGTYGYEUyegJ%2B1g5%2Bz8zbHg6WtLrG%2BAYpBjQpn%2F3qT0YKxg2I1Zsh8CSmuz%2Fpvszft5QdBSeL15k6PE5PkcETl9M4&X-Amz-Signature=9564258c6d09670c59af25f8cb866a6c99c0bde4419792b5e19ba75fc6373135&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAYWDHYG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7Xb8k0OjSjyf3v2aK4RLJr2XElG6UPY2NChAVJgmwRAiEA2MfFYmaLS8iYFYM%2Bab0ovF05EGjjQCkBGtQvP5lKzyQqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYT82LTbYsIZuEhjircA8SLaHS2kMg3hjwSzrHhBfZT1YdAbToYwK6JWU6V%2FA9MW%2BjVyZlZnAJ5hN3%2FIOUMIMwpQ8QhM7yYrH05uXUZh0pAnwY4fvwi%2B2ltee6fYDtOKETOfAxQ38sYljVwqzpXkX9Q1KKI53IvF3X0PeboOH5TqNg4izvF68kyU74ekuSi1wFcGYW%2BjjQPQ%2FKNvPdJXzGyAqr5nvnvc6zrcXMjsm5UG9GeMlwgROzNicFe85a9fgXq%2FBR12bs767sO%2BC9WWHVBnJT5Ze7MzzoqQ%2BEtVz2aM7MG8euHRE3IVycmYd2RHEEiaZ%2FyXcZQ0Wn3OSbkewtTI%2B6hJEtp7yTL3IEPzg0buzaCNFxfIw0NzkKVytQwhHhOMz2D0iI%2FrvvjGUb3g9OmERu2YUJQeNEAP7zHTu2EvKzgriZjVWBGI%2BW7IWmqkOXQrZiUiBsoTCSXfdmfFGwJRb2FmoF6JutkFURPpJOCrcrDKJj0cPqFn6bVBFk1nh7yYS5AkndSmgYNHtobKF2jHkR9vZyaZ4NjVoyYBpPrYOug1EqZ%2FHAiAumYVzd6AZzmzjZM24M80%2Furygxsrs0kSjZ9k9HHiYahrV6MNpKMU2Jvdkq04%2FsrpQOAwNqE1zW0fhCCbsppJboQMNGT%2BrwGOqUBsir1UpUFQXIx%2FPY%2BjqFTx9Dk%2BZ9ql0POXJhnWlwUHHhKSCRoZHybI3DBP4JC54n3oQJgwbDzeJf8g2ZflYxTZVNbee70rlAgxsfunCtzM5%2BjA3phAwT%2F5MOqG2ClaukOgVA6UH4lOMIuXTXpoChF5QTSfGPsRZuCGPPxpSCSqknMR3KKW5Wp9x21HMllEMHGAPTx24ocDKsi4luUzZCGrIRUwVyA&X-Amz-Signature=85eaead0aa3c87921f547f58b76485109c8da0222757d18e4470d341a4732aeb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAYWDHYG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7Xb8k0OjSjyf3v2aK4RLJr2XElG6UPY2NChAVJgmwRAiEA2MfFYmaLS8iYFYM%2Bab0ovF05EGjjQCkBGtQvP5lKzyQqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYT82LTbYsIZuEhjircA8SLaHS2kMg3hjwSzrHhBfZT1YdAbToYwK6JWU6V%2FA9MW%2BjVyZlZnAJ5hN3%2FIOUMIMwpQ8QhM7yYrH05uXUZh0pAnwY4fvwi%2B2ltee6fYDtOKETOfAxQ38sYljVwqzpXkX9Q1KKI53IvF3X0PeboOH5TqNg4izvF68kyU74ekuSi1wFcGYW%2BjjQPQ%2FKNvPdJXzGyAqr5nvnvc6zrcXMjsm5UG9GeMlwgROzNicFe85a9fgXq%2FBR12bs767sO%2BC9WWHVBnJT5Ze7MzzoqQ%2BEtVz2aM7MG8euHRE3IVycmYd2RHEEiaZ%2FyXcZQ0Wn3OSbkewtTI%2B6hJEtp7yTL3IEPzg0buzaCNFxfIw0NzkKVytQwhHhOMz2D0iI%2FrvvjGUb3g9OmERu2YUJQeNEAP7zHTu2EvKzgriZjVWBGI%2BW7IWmqkOXQrZiUiBsoTCSXfdmfFGwJRb2FmoF6JutkFURPpJOCrcrDKJj0cPqFn6bVBFk1nh7yYS5AkndSmgYNHtobKF2jHkR9vZyaZ4NjVoyYBpPrYOug1EqZ%2FHAiAumYVzd6AZzmzjZM24M80%2Furygxsrs0kSjZ9k9HHiYahrV6MNpKMU2Jvdkq04%2FsrpQOAwNqE1zW0fhCCbsppJboQMNGT%2BrwGOqUBsir1UpUFQXIx%2FPY%2BjqFTx9Dk%2BZ9ql0POXJhnWlwUHHhKSCRoZHybI3DBP4JC54n3oQJgwbDzeJf8g2ZflYxTZVNbee70rlAgxsfunCtzM5%2BjA3phAwT%2F5MOqG2ClaukOgVA6UH4lOMIuXTXpoChF5QTSfGPsRZuCGPPxpSCSqknMR3KKW5Wp9x21HMllEMHGAPTx24ocDKsi4luUzZCGrIRUwVyA&X-Amz-Signature=c370aed65f51b315bae7ce70c131a8d33c94bb07ec9bf98fc0fdd4ca4fc38f9e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAYWDHYG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7Xb8k0OjSjyf3v2aK4RLJr2XElG6UPY2NChAVJgmwRAiEA2MfFYmaLS8iYFYM%2Bab0ovF05EGjjQCkBGtQvP5lKzyQqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYT82LTbYsIZuEhjircA8SLaHS2kMg3hjwSzrHhBfZT1YdAbToYwK6JWU6V%2FA9MW%2BjVyZlZnAJ5hN3%2FIOUMIMwpQ8QhM7yYrH05uXUZh0pAnwY4fvwi%2B2ltee6fYDtOKETOfAxQ38sYljVwqzpXkX9Q1KKI53IvF3X0PeboOH5TqNg4izvF68kyU74ekuSi1wFcGYW%2BjjQPQ%2FKNvPdJXzGyAqr5nvnvc6zrcXMjsm5UG9GeMlwgROzNicFe85a9fgXq%2FBR12bs767sO%2BC9WWHVBnJT5Ze7MzzoqQ%2BEtVz2aM7MG8euHRE3IVycmYd2RHEEiaZ%2FyXcZQ0Wn3OSbkewtTI%2B6hJEtp7yTL3IEPzg0buzaCNFxfIw0NzkKVytQwhHhOMz2D0iI%2FrvvjGUb3g9OmERu2YUJQeNEAP7zHTu2EvKzgriZjVWBGI%2BW7IWmqkOXQrZiUiBsoTCSXfdmfFGwJRb2FmoF6JutkFURPpJOCrcrDKJj0cPqFn6bVBFk1nh7yYS5AkndSmgYNHtobKF2jHkR9vZyaZ4NjVoyYBpPrYOug1EqZ%2FHAiAumYVzd6AZzmzjZM24M80%2Furygxsrs0kSjZ9k9HHiYahrV6MNpKMU2Jvdkq04%2FsrpQOAwNqE1zW0fhCCbsppJboQMNGT%2BrwGOqUBsir1UpUFQXIx%2FPY%2BjqFTx9Dk%2BZ9ql0POXJhnWlwUHHhKSCRoZHybI3DBP4JC54n3oQJgwbDzeJf8g2ZflYxTZVNbee70rlAgxsfunCtzM5%2BjA3phAwT%2F5MOqG2ClaukOgVA6UH4lOMIuXTXpoChF5QTSfGPsRZuCGPPxpSCSqknMR3KKW5Wp9x21HMllEMHGAPTx24ocDKsi4luUzZCGrIRUwVyA&X-Amz-Signature=41c284d486d9b93e7fb8cd4dd41883e702df39c39adf8f145633b373cd28dad6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAYWDHYG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7Xb8k0OjSjyf3v2aK4RLJr2XElG6UPY2NChAVJgmwRAiEA2MfFYmaLS8iYFYM%2Bab0ovF05EGjjQCkBGtQvP5lKzyQqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYT82LTbYsIZuEhjircA8SLaHS2kMg3hjwSzrHhBfZT1YdAbToYwK6JWU6V%2FA9MW%2BjVyZlZnAJ5hN3%2FIOUMIMwpQ8QhM7yYrH05uXUZh0pAnwY4fvwi%2B2ltee6fYDtOKETOfAxQ38sYljVwqzpXkX9Q1KKI53IvF3X0PeboOH5TqNg4izvF68kyU74ekuSi1wFcGYW%2BjjQPQ%2FKNvPdJXzGyAqr5nvnvc6zrcXMjsm5UG9GeMlwgROzNicFe85a9fgXq%2FBR12bs767sO%2BC9WWHVBnJT5Ze7MzzoqQ%2BEtVz2aM7MG8euHRE3IVycmYd2RHEEiaZ%2FyXcZQ0Wn3OSbkewtTI%2B6hJEtp7yTL3IEPzg0buzaCNFxfIw0NzkKVytQwhHhOMz2D0iI%2FrvvjGUb3g9OmERu2YUJQeNEAP7zHTu2EvKzgriZjVWBGI%2BW7IWmqkOXQrZiUiBsoTCSXfdmfFGwJRb2FmoF6JutkFURPpJOCrcrDKJj0cPqFn6bVBFk1nh7yYS5AkndSmgYNHtobKF2jHkR9vZyaZ4NjVoyYBpPrYOug1EqZ%2FHAiAumYVzd6AZzmzjZM24M80%2Furygxsrs0kSjZ9k9HHiYahrV6MNpKMU2Jvdkq04%2FsrpQOAwNqE1zW0fhCCbsppJboQMNGT%2BrwGOqUBsir1UpUFQXIx%2FPY%2BjqFTx9Dk%2BZ9ql0POXJhnWlwUHHhKSCRoZHybI3DBP4JC54n3oQJgwbDzeJf8g2ZflYxTZVNbee70rlAgxsfunCtzM5%2BjA3phAwT%2F5MOqG2ClaukOgVA6UH4lOMIuXTXpoChF5QTSfGPsRZuCGPPxpSCSqknMR3KKW5Wp9x21HMllEMHGAPTx24ocDKsi4luUzZCGrIRUwVyA&X-Amz-Signature=a6eacee9d65a776b4b61d67f422fe03477e8d49223104b4357c2384fbabed681&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAYWDHYG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7Xb8k0OjSjyf3v2aK4RLJr2XElG6UPY2NChAVJgmwRAiEA2MfFYmaLS8iYFYM%2Bab0ovF05EGjjQCkBGtQvP5lKzyQqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYT82LTbYsIZuEhjircA8SLaHS2kMg3hjwSzrHhBfZT1YdAbToYwK6JWU6V%2FA9MW%2BjVyZlZnAJ5hN3%2FIOUMIMwpQ8QhM7yYrH05uXUZh0pAnwY4fvwi%2B2ltee6fYDtOKETOfAxQ38sYljVwqzpXkX9Q1KKI53IvF3X0PeboOH5TqNg4izvF68kyU74ekuSi1wFcGYW%2BjjQPQ%2FKNvPdJXzGyAqr5nvnvc6zrcXMjsm5UG9GeMlwgROzNicFe85a9fgXq%2FBR12bs767sO%2BC9WWHVBnJT5Ze7MzzoqQ%2BEtVz2aM7MG8euHRE3IVycmYd2RHEEiaZ%2FyXcZQ0Wn3OSbkewtTI%2B6hJEtp7yTL3IEPzg0buzaCNFxfIw0NzkKVytQwhHhOMz2D0iI%2FrvvjGUb3g9OmERu2YUJQeNEAP7zHTu2EvKzgriZjVWBGI%2BW7IWmqkOXQrZiUiBsoTCSXfdmfFGwJRb2FmoF6JutkFURPpJOCrcrDKJj0cPqFn6bVBFk1nh7yYS5AkndSmgYNHtobKF2jHkR9vZyaZ4NjVoyYBpPrYOug1EqZ%2FHAiAumYVzd6AZzmzjZM24M80%2Furygxsrs0kSjZ9k9HHiYahrV6MNpKMU2Jvdkq04%2FsrpQOAwNqE1zW0fhCCbsppJboQMNGT%2BrwGOqUBsir1UpUFQXIx%2FPY%2BjqFTx9Dk%2BZ9ql0POXJhnWlwUHHhKSCRoZHybI3DBP4JC54n3oQJgwbDzeJf8g2ZflYxTZVNbee70rlAgxsfunCtzM5%2BjA3phAwT%2F5MOqG2ClaukOgVA6UH4lOMIuXTXpoChF5QTSfGPsRZuCGPPxpSCSqknMR3KKW5Wp9x21HMllEMHGAPTx24ocDKsi4luUzZCGrIRUwVyA&X-Amz-Signature=94dd81c432e2143f4f40db5cbad3bea860e003b5fec3169f4bcafcf745e5c0c2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOLZ7HY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBP8r%2F0D6b0prb0AEGq6KU7LSne2ZE4HNEwk0aEPxNyCAiAEm3L7wQb8Lu7aCnzrHNvkWVJ4ZN8zndlLVDyY8JigpyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2uMkxqd1U15%2FHC24KtwDvhowv1iffUi09lArAb55RsrQyfBLvctPFkjdfH2WGYVk2midUoIcuvUkpr%2FKcRVo8%2FLgi%2FlZ9BoB4PMKwc%2FI1Mu9vJZxcxpcC20cq5yZDx%2FsgESBuTbe7jSpMkZj2tkEuYirjKadPeKrCJh5TFTeAiqNesTjoSaxSsw%2BJlgehyuV21rKW%2FxaZ1avg4KS%2BthJQZhVjQgk%2F0wMsFT4IDctvVqAxz1fmcHjKVpbU0xTq%2FhXu06leAx6ucSrweU7j18RqDiRS44ZoeeCXAz%2BGEhpxhJ2JG8kVU2RyEWukJJUImFUgt3vepd%2FgXpNCnTwHZF1ET0gpiN%2B0BW2KKAFcrgyN2J3d8GEKiixZHOp3rBQOpAlArgO5PW9AdY4GNRf%2FFdtC5wVKWAN178rWDp6njiG%2FrQdnRWd3%2BFm3IVDjHsLJyHehG4TrGMNNGPyWJbGMHk1kBV7fAgb%2FHwV%2BAtR4wJKYqzM2ANagUGxuRN%2BpdB58Pbd3WnIrM%2FxPdbHffPhzwo8PDcpK9JF6%2B2y7Rtyl9%2BxmaymKtO8dqsyTTIntxgcZoIQNwnRZHcPqWadWPUW7g56wdeVBOgxxfBEaNGsrb1ir16%2Fz29cLKn9UNxjQiEyyBg6P2lv8Sc2wipEa7kw9pP6vAY6pgH%2FxS4Do2cTJjMkcW0AxWjhZfCldgqvmet8p4kApoLAAKSMGxeAJ1vIUdUlz5aYNU826D%2FTOVz95CcGH1WL%2FdvIwjojZkshD9gHhRNhqNVNyKWrbVVvNDQAU98ovldWQPR6ryQMGTYGYEUyegJ%2B1g5%2Bz8zbHg6WtLrG%2BAYpBjQpn%2F3qT0YKxg2I1Zsh8CSmuz%2Fpvszft5QdBSeL15k6PE5PkcETl9M4&X-Amz-Signature=44cc8cd7bbe969479257006c9cf3b70fc3707eb6a724d19f4044352531a2a6c3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOLZ7HY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBP8r%2F0D6b0prb0AEGq6KU7LSne2ZE4HNEwk0aEPxNyCAiAEm3L7wQb8Lu7aCnzrHNvkWVJ4ZN8zndlLVDyY8JigpyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2uMkxqd1U15%2FHC24KtwDvhowv1iffUi09lArAb55RsrQyfBLvctPFkjdfH2WGYVk2midUoIcuvUkpr%2FKcRVo8%2FLgi%2FlZ9BoB4PMKwc%2FI1Mu9vJZxcxpcC20cq5yZDx%2FsgESBuTbe7jSpMkZj2tkEuYirjKadPeKrCJh5TFTeAiqNesTjoSaxSsw%2BJlgehyuV21rKW%2FxaZ1avg4KS%2BthJQZhVjQgk%2F0wMsFT4IDctvVqAxz1fmcHjKVpbU0xTq%2FhXu06leAx6ucSrweU7j18RqDiRS44ZoeeCXAz%2BGEhpxhJ2JG8kVU2RyEWukJJUImFUgt3vepd%2FgXpNCnTwHZF1ET0gpiN%2B0BW2KKAFcrgyN2J3d8GEKiixZHOp3rBQOpAlArgO5PW9AdY4GNRf%2FFdtC5wVKWAN178rWDp6njiG%2FrQdnRWd3%2BFm3IVDjHsLJyHehG4TrGMNNGPyWJbGMHk1kBV7fAgb%2FHwV%2BAtR4wJKYqzM2ANagUGxuRN%2BpdB58Pbd3WnIrM%2FxPdbHffPhzwo8PDcpK9JF6%2B2y7Rtyl9%2BxmaymKtO8dqsyTTIntxgcZoIQNwnRZHcPqWadWPUW7g56wdeVBOgxxfBEaNGsrb1ir16%2Fz29cLKn9UNxjQiEyyBg6P2lv8Sc2wipEa7kw9pP6vAY6pgH%2FxS4Do2cTJjMkcW0AxWjhZfCldgqvmet8p4kApoLAAKSMGxeAJ1vIUdUlz5aYNU826D%2FTOVz95CcGH1WL%2FdvIwjojZkshD9gHhRNhqNVNyKWrbVVvNDQAU98ovldWQPR6ryQMGTYGYEUyegJ%2B1g5%2Bz8zbHg6WtLrG%2BAYpBjQpn%2F3qT0YKxg2I1Zsh8CSmuz%2Fpvszft5QdBSeL15k6PE5PkcETl9M4&X-Amz-Signature=e53c6e41bd35b52854eb17a03fb43878c8f41617ce3285098328cb46a3a0c450&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOLZ7HY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBP8r%2F0D6b0prb0AEGq6KU7LSne2ZE4HNEwk0aEPxNyCAiAEm3L7wQb8Lu7aCnzrHNvkWVJ4ZN8zndlLVDyY8JigpyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2uMkxqd1U15%2FHC24KtwDvhowv1iffUi09lArAb55RsrQyfBLvctPFkjdfH2WGYVk2midUoIcuvUkpr%2FKcRVo8%2FLgi%2FlZ9BoB4PMKwc%2FI1Mu9vJZxcxpcC20cq5yZDx%2FsgESBuTbe7jSpMkZj2tkEuYirjKadPeKrCJh5TFTeAiqNesTjoSaxSsw%2BJlgehyuV21rKW%2FxaZ1avg4KS%2BthJQZhVjQgk%2F0wMsFT4IDctvVqAxz1fmcHjKVpbU0xTq%2FhXu06leAx6ucSrweU7j18RqDiRS44ZoeeCXAz%2BGEhpxhJ2JG8kVU2RyEWukJJUImFUgt3vepd%2FgXpNCnTwHZF1ET0gpiN%2B0BW2KKAFcrgyN2J3d8GEKiixZHOp3rBQOpAlArgO5PW9AdY4GNRf%2FFdtC5wVKWAN178rWDp6njiG%2FrQdnRWd3%2BFm3IVDjHsLJyHehG4TrGMNNGPyWJbGMHk1kBV7fAgb%2FHwV%2BAtR4wJKYqzM2ANagUGxuRN%2BpdB58Pbd3WnIrM%2FxPdbHffPhzwo8PDcpK9JF6%2B2y7Rtyl9%2BxmaymKtO8dqsyTTIntxgcZoIQNwnRZHcPqWadWPUW7g56wdeVBOgxxfBEaNGsrb1ir16%2Fz29cLKn9UNxjQiEyyBg6P2lv8Sc2wipEa7kw9pP6vAY6pgH%2FxS4Do2cTJjMkcW0AxWjhZfCldgqvmet8p4kApoLAAKSMGxeAJ1vIUdUlz5aYNU826D%2FTOVz95CcGH1WL%2FdvIwjojZkshD9gHhRNhqNVNyKWrbVVvNDQAU98ovldWQPR6ryQMGTYGYEUyegJ%2B1g5%2Bz8zbHg6WtLrG%2BAYpBjQpn%2F3qT0YKxg2I1Zsh8CSmuz%2Fpvszft5QdBSeL15k6PE5PkcETl9M4&X-Amz-Signature=e7a8f14eaf481b4c67d05b8f609c1d28833ac3120aa2cf262ec7b9f47e90911f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOLZ7HY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBP8r%2F0D6b0prb0AEGq6KU7LSne2ZE4HNEwk0aEPxNyCAiAEm3L7wQb8Lu7aCnzrHNvkWVJ4ZN8zndlLVDyY8JigpyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2uMkxqd1U15%2FHC24KtwDvhowv1iffUi09lArAb55RsrQyfBLvctPFkjdfH2WGYVk2midUoIcuvUkpr%2FKcRVo8%2FLgi%2FlZ9BoB4PMKwc%2FI1Mu9vJZxcxpcC20cq5yZDx%2FsgESBuTbe7jSpMkZj2tkEuYirjKadPeKrCJh5TFTeAiqNesTjoSaxSsw%2BJlgehyuV21rKW%2FxaZ1avg4KS%2BthJQZhVjQgk%2F0wMsFT4IDctvVqAxz1fmcHjKVpbU0xTq%2FhXu06leAx6ucSrweU7j18RqDiRS44ZoeeCXAz%2BGEhpxhJ2JG8kVU2RyEWukJJUImFUgt3vepd%2FgXpNCnTwHZF1ET0gpiN%2B0BW2KKAFcrgyN2J3d8GEKiixZHOp3rBQOpAlArgO5PW9AdY4GNRf%2FFdtC5wVKWAN178rWDp6njiG%2FrQdnRWd3%2BFm3IVDjHsLJyHehG4TrGMNNGPyWJbGMHk1kBV7fAgb%2FHwV%2BAtR4wJKYqzM2ANagUGxuRN%2BpdB58Pbd3WnIrM%2FxPdbHffPhzwo8PDcpK9JF6%2B2y7Rtyl9%2BxmaymKtO8dqsyTTIntxgcZoIQNwnRZHcPqWadWPUW7g56wdeVBOgxxfBEaNGsrb1ir16%2Fz29cLKn9UNxjQiEyyBg6P2lv8Sc2wipEa7kw9pP6vAY6pgH%2FxS4Do2cTJjMkcW0AxWjhZfCldgqvmet8p4kApoLAAKSMGxeAJ1vIUdUlz5aYNU826D%2FTOVz95CcGH1WL%2FdvIwjojZkshD9gHhRNhqNVNyKWrbVVvNDQAU98ovldWQPR6ryQMGTYGYEUyegJ%2B1g5%2Bz8zbHg6WtLrG%2BAYpBjQpn%2F3qT0YKxg2I1Zsh8CSmuz%2Fpvszft5QdBSeL15k6PE5PkcETl9M4&X-Amz-Signature=6cd0d5ba3d077cfc0adaaa79214c500440901ffa9cae4e50d09749a4bd6fe920&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUOLZ7HY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBP8r%2F0D6b0prb0AEGq6KU7LSne2ZE4HNEwk0aEPxNyCAiAEm3L7wQb8Lu7aCnzrHNvkWVJ4ZN8zndlLVDyY8JigpyqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2uMkxqd1U15%2FHC24KtwDvhowv1iffUi09lArAb55RsrQyfBLvctPFkjdfH2WGYVk2midUoIcuvUkpr%2FKcRVo8%2FLgi%2FlZ9BoB4PMKwc%2FI1Mu9vJZxcxpcC20cq5yZDx%2FsgESBuTbe7jSpMkZj2tkEuYirjKadPeKrCJh5TFTeAiqNesTjoSaxSsw%2BJlgehyuV21rKW%2FxaZ1avg4KS%2BthJQZhVjQgk%2F0wMsFT4IDctvVqAxz1fmcHjKVpbU0xTq%2FhXu06leAx6ucSrweU7j18RqDiRS44ZoeeCXAz%2BGEhpxhJ2JG8kVU2RyEWukJJUImFUgt3vepd%2FgXpNCnTwHZF1ET0gpiN%2B0BW2KKAFcrgyN2J3d8GEKiixZHOp3rBQOpAlArgO5PW9AdY4GNRf%2FFdtC5wVKWAN178rWDp6njiG%2FrQdnRWd3%2BFm3IVDjHsLJyHehG4TrGMNNGPyWJbGMHk1kBV7fAgb%2FHwV%2BAtR4wJKYqzM2ANagUGxuRN%2BpdB58Pbd3WnIrM%2FxPdbHffPhzwo8PDcpK9JF6%2B2y7Rtyl9%2BxmaymKtO8dqsyTTIntxgcZoIQNwnRZHcPqWadWPUW7g56wdeVBOgxxfBEaNGsrb1ir16%2Fz29cLKn9UNxjQiEyyBg6P2lv8Sc2wipEa7kw9pP6vAY6pgH%2FxS4Do2cTJjMkcW0AxWjhZfCldgqvmet8p4kApoLAAKSMGxeAJ1vIUdUlz5aYNU826D%2FTOVz95CcGH1WL%2FdvIwjojZkshD9gHhRNhqNVNyKWrbVVvNDQAU98ovldWQPR6ryQMGTYGYEUyegJ%2B1g5%2Bz8zbHg6WtLrG%2BAYpBjQpn%2F3qT0YKxg2I1Zsh8CSmuz%2Fpvszft5QdBSeL15k6PE5PkcETl9M4&X-Amz-Signature=de157163cf7be3359424f25754fb867a28f47d77867124e46321a239a5a6c808&X-Amz-SignedHeaders=host&x-id=GetObject)
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


