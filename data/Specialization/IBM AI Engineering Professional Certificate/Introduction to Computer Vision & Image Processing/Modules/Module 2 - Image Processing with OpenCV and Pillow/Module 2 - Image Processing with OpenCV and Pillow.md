

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG25RASZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bg3rBj9UYflMHgBKfy26JooIECdmO0GODtr1ZImFdKAiB7LMdOAZvMniEni8q%2FL1YrnuI%2FaaTCIqLeWm3zmQOHxyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxX9lu%2BvWb5TRV62KtwDAso15NRU41i3tWzhfJVA0Zuw3gOnO0ZhvIh7Of%2BDb86cG3BPBVQh8mCsMP9qccxaQptYOlpqW4zT57uCBoNhdZe9xFsBBEJlCoaFuplbsLUIrTZ%2BGTAJEtzWI1eO8S7duvRtqJe%2BNfirIgRl6Ca3TcAjPD1Jxa89nIMiWvy3d9wAj11cOfQnU%2Bxcib9mjLPzKMGLRinZiNDAL4uihgmTOQkswCRt5UDIkxP10lMPLjXnilKjd9y1ov3iOwW%2B2T%2BaJk0%2BKPZW3WmYXzn7%2F274g3Jr3sbNfCw07G3rBFeo%2FIFw2vKtfV1YGy64yng76TCFME4EDued1Rx%2B7PHVbe90h%2FqV%2F%2BJk%2FScls%2B0m0bONpgYotxuaCf1PPA4HohXUL2q8xEGlKPubGL2GU6sxpx8V5qQoweIu80FkcDjio4qC1XF2Fh71ZBWNO5ZrWWedSBwd7JzaDzjbfCGV0p57uk%2BZs%2F%2ByquidAfbLsHhR92vIO8cPU6%2F3MNxi7%2B4l48bw7df9FsZVMFSUethja4GGrF0VmX7gLoUAS8c5w%2FvJSkMYAQKP0u0Wo1nCCcO0qfcKK2J4ZwliLONOwvE8Dh45mfnqXWVBN53e%2FA2QyEe42CrEaG2%2BpvZchSawFoafvk8w8sbqvAY6pgFH59OWCeSZctfGYZrOjdk9MNwV8%2BWPTz9KLiVVy9D98al%2FgNLfGaYIDsQCfQMCMbr1QISpQ1Sc1Jy0Z7pXNX%2ByeHafAi0i%2FHmXGBc%2B%2Bq7LxtIV08Gr0goKwHhTD1fp1tUmqtHJKfnOSTVXc0exJNRBwreM7yl0u57U84oseb3Qc%2BTCRWJ7HkXE9PAxEkjcwvVHTL4owJ3RzqWLCocBtGFmsAsjR3uY&X-Amz-Signature=2920294db611cf82430442ac418798ffdca90bdb077f8beb5b01d7cc751bbe62&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZFBMBN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4oyRfNHVkA9i4CpWCc2q0Bq9T%2FybGi60GhXnAepSGowIhAMgLSU5LE51uz%2FbCkShXQWJ7OfJuNZGgwgrDLrPnArfVKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzsiZYKKn02TfZRxAq3AMkiNkFemZnYRtKwWaoL%2BByPujL6ZG%2FjwT2XxqXwHNOcMow3eKHALGvtFdBnPjVhNtEhLYDG%2BnfGWDfV2NafADxFzuvnoi799S1UnVzRbLvPH3CWeByhTNwkD9DVIeOgy5r8vRf0CrJsPJokJcyB0a1eaXeKqtCkkMDZ7vdRQArXBg8yNPEcXy053zS1O0BjiNEVwIAw%2F3KkK1vYbOn6QJgqdJFqM9rMhJUlCa6rkYWsBgi6fbUx8Q6p8QWc95ljVuu%2Ftcz4Ity3Wnxcgj5LrFotCCLlfXO7BNasHSuhcKQvP3pvNDOXiDDHc0abRvg%2Fi6tHj%2F55Rjx3pdetMaCV%2B6CF4QuZ07SHCdjfgRsOE6JMcie3UyWS0hXw4jgM73Ou6WrnHtnJuc4KOxQ50z96e0Fa8CDDzK2I5fHK1SBEVkDE1zgBzgBE4y%2BQ6jPI3GySq8i1NlQ1Ta%2BmVefTujSOBBcW1RJZBE4B6SRbgcuPXPOyQPNt3DbgLctl7Kvt072bLmMdqk5XIVbZ7k577a6Rh5x2TIJvh7bK%2Fm8%2FnGuZco%2F3meh41JJ9DXwG1rtCWB6%2BwI6yd3Ef0AOEy1kZJAT8mh3wldg6AijhOpN1Gf%2FQrjPDTzz2X7TYHqaIqDcATCyxuq8BjqkAdKWGqd9cjh6oYMHdRk9m%2BD5tciVYOxTYybRHOwt0Ioh4Dk7efE4ItpWgXE%2BZmxsiKkk7mNL8%2FN0w2Tw4eY19GgQaMRE1mm%2FNntSpE%2B31VCOUifWZfY4qs0F1JHro6Jx44AYTjEG68BFpLZo4ml6vyrSjxeLLzaJhuALgiPx9sEJv6Khdy8ep5ODpsfDuoexbmQdgW%2FJEpL1KngJj%2B2%2BrgRzYF1C&X-Amz-Signature=daf30f7e0804906233779663256eff96543e04cd82a1e76ef920719762c78a16&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZFBMBN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4oyRfNHVkA9i4CpWCc2q0Bq9T%2FybGi60GhXnAepSGowIhAMgLSU5LE51uz%2FbCkShXQWJ7OfJuNZGgwgrDLrPnArfVKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzsiZYKKn02TfZRxAq3AMkiNkFemZnYRtKwWaoL%2BByPujL6ZG%2FjwT2XxqXwHNOcMow3eKHALGvtFdBnPjVhNtEhLYDG%2BnfGWDfV2NafADxFzuvnoi799S1UnVzRbLvPH3CWeByhTNwkD9DVIeOgy5r8vRf0CrJsPJokJcyB0a1eaXeKqtCkkMDZ7vdRQArXBg8yNPEcXy053zS1O0BjiNEVwIAw%2F3KkK1vYbOn6QJgqdJFqM9rMhJUlCa6rkYWsBgi6fbUx8Q6p8QWc95ljVuu%2Ftcz4Ity3Wnxcgj5LrFotCCLlfXO7BNasHSuhcKQvP3pvNDOXiDDHc0abRvg%2Fi6tHj%2F55Rjx3pdetMaCV%2B6CF4QuZ07SHCdjfgRsOE6JMcie3UyWS0hXw4jgM73Ou6WrnHtnJuc4KOxQ50z96e0Fa8CDDzK2I5fHK1SBEVkDE1zgBzgBE4y%2BQ6jPI3GySq8i1NlQ1Ta%2BmVefTujSOBBcW1RJZBE4B6SRbgcuPXPOyQPNt3DbgLctl7Kvt072bLmMdqk5XIVbZ7k577a6Rh5x2TIJvh7bK%2Fm8%2FnGuZco%2F3meh41JJ9DXwG1rtCWB6%2BwI6yd3Ef0AOEy1kZJAT8mh3wldg6AijhOpN1Gf%2FQrjPDTzz2X7TYHqaIqDcATCyxuq8BjqkAdKWGqd9cjh6oYMHdRk9m%2BD5tciVYOxTYybRHOwt0Ioh4Dk7efE4ItpWgXE%2BZmxsiKkk7mNL8%2FN0w2Tw4eY19GgQaMRE1mm%2FNntSpE%2B31VCOUifWZfY4qs0F1JHro6Jx44AYTjEG68BFpLZo4ml6vyrSjxeLLzaJhuALgiPx9sEJv6Khdy8ep5ODpsfDuoexbmQdgW%2FJEpL1KngJj%2B2%2BrgRzYF1C&X-Amz-Signature=4cdb2bf94d0d6216a670c2b6b8ed0310ead1e6788101229ab846961612b0aa65&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZFBMBN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4oyRfNHVkA9i4CpWCc2q0Bq9T%2FybGi60GhXnAepSGowIhAMgLSU5LE51uz%2FbCkShXQWJ7OfJuNZGgwgrDLrPnArfVKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzsiZYKKn02TfZRxAq3AMkiNkFemZnYRtKwWaoL%2BByPujL6ZG%2FjwT2XxqXwHNOcMow3eKHALGvtFdBnPjVhNtEhLYDG%2BnfGWDfV2NafADxFzuvnoi799S1UnVzRbLvPH3CWeByhTNwkD9DVIeOgy5r8vRf0CrJsPJokJcyB0a1eaXeKqtCkkMDZ7vdRQArXBg8yNPEcXy053zS1O0BjiNEVwIAw%2F3KkK1vYbOn6QJgqdJFqM9rMhJUlCa6rkYWsBgi6fbUx8Q6p8QWc95ljVuu%2Ftcz4Ity3Wnxcgj5LrFotCCLlfXO7BNasHSuhcKQvP3pvNDOXiDDHc0abRvg%2Fi6tHj%2F55Rjx3pdetMaCV%2B6CF4QuZ07SHCdjfgRsOE6JMcie3UyWS0hXw4jgM73Ou6WrnHtnJuc4KOxQ50z96e0Fa8CDDzK2I5fHK1SBEVkDE1zgBzgBE4y%2BQ6jPI3GySq8i1NlQ1Ta%2BmVefTujSOBBcW1RJZBE4B6SRbgcuPXPOyQPNt3DbgLctl7Kvt072bLmMdqk5XIVbZ7k577a6Rh5x2TIJvh7bK%2Fm8%2FnGuZco%2F3meh41JJ9DXwG1rtCWB6%2BwI6yd3Ef0AOEy1kZJAT8mh3wldg6AijhOpN1Gf%2FQrjPDTzz2X7TYHqaIqDcATCyxuq8BjqkAdKWGqd9cjh6oYMHdRk9m%2BD5tciVYOxTYybRHOwt0Ioh4Dk7efE4ItpWgXE%2BZmxsiKkk7mNL8%2FN0w2Tw4eY19GgQaMRE1mm%2FNntSpE%2B31VCOUifWZfY4qs0F1JHro6Jx44AYTjEG68BFpLZo4ml6vyrSjxeLLzaJhuALgiPx9sEJv6Khdy8ep5ODpsfDuoexbmQdgW%2FJEpL1KngJj%2B2%2BrgRzYF1C&X-Amz-Signature=e982c1a3931ee7521592de83440084cea15a999ff87092956ae89dd87026bc12&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZFBMBN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4oyRfNHVkA9i4CpWCc2q0Bq9T%2FybGi60GhXnAepSGowIhAMgLSU5LE51uz%2FbCkShXQWJ7OfJuNZGgwgrDLrPnArfVKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzsiZYKKn02TfZRxAq3AMkiNkFemZnYRtKwWaoL%2BByPujL6ZG%2FjwT2XxqXwHNOcMow3eKHALGvtFdBnPjVhNtEhLYDG%2BnfGWDfV2NafADxFzuvnoi799S1UnVzRbLvPH3CWeByhTNwkD9DVIeOgy5r8vRf0CrJsPJokJcyB0a1eaXeKqtCkkMDZ7vdRQArXBg8yNPEcXy053zS1O0BjiNEVwIAw%2F3KkK1vYbOn6QJgqdJFqM9rMhJUlCa6rkYWsBgi6fbUx8Q6p8QWc95ljVuu%2Ftcz4Ity3Wnxcgj5LrFotCCLlfXO7BNasHSuhcKQvP3pvNDOXiDDHc0abRvg%2Fi6tHj%2F55Rjx3pdetMaCV%2B6CF4QuZ07SHCdjfgRsOE6JMcie3UyWS0hXw4jgM73Ou6WrnHtnJuc4KOxQ50z96e0Fa8CDDzK2I5fHK1SBEVkDE1zgBzgBE4y%2BQ6jPI3GySq8i1NlQ1Ta%2BmVefTujSOBBcW1RJZBE4B6SRbgcuPXPOyQPNt3DbgLctl7Kvt072bLmMdqk5XIVbZ7k577a6Rh5x2TIJvh7bK%2Fm8%2FnGuZco%2F3meh41JJ9DXwG1rtCWB6%2BwI6yd3Ef0AOEy1kZJAT8mh3wldg6AijhOpN1Gf%2FQrjPDTzz2X7TYHqaIqDcATCyxuq8BjqkAdKWGqd9cjh6oYMHdRk9m%2BD5tciVYOxTYybRHOwt0Ioh4Dk7efE4ItpWgXE%2BZmxsiKkk7mNL8%2FN0w2Tw4eY19GgQaMRE1mm%2FNntSpE%2B31VCOUifWZfY4qs0F1JHro6Jx44AYTjEG68BFpLZo4ml6vyrSjxeLLzaJhuALgiPx9sEJv6Khdy8ep5ODpsfDuoexbmQdgW%2FJEpL1KngJj%2B2%2BrgRzYF1C&X-Amz-Signature=cf318846f600978be85678ae3b32843f2917a6185d868f2c7187736afc5665e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZFBMBN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4oyRfNHVkA9i4CpWCc2q0Bq9T%2FybGi60GhXnAepSGowIhAMgLSU5LE51uz%2FbCkShXQWJ7OfJuNZGgwgrDLrPnArfVKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzsiZYKKn02TfZRxAq3AMkiNkFemZnYRtKwWaoL%2BByPujL6ZG%2FjwT2XxqXwHNOcMow3eKHALGvtFdBnPjVhNtEhLYDG%2BnfGWDfV2NafADxFzuvnoi799S1UnVzRbLvPH3CWeByhTNwkD9DVIeOgy5r8vRf0CrJsPJokJcyB0a1eaXeKqtCkkMDZ7vdRQArXBg8yNPEcXy053zS1O0BjiNEVwIAw%2F3KkK1vYbOn6QJgqdJFqM9rMhJUlCa6rkYWsBgi6fbUx8Q6p8QWc95ljVuu%2Ftcz4Ity3Wnxcgj5LrFotCCLlfXO7BNasHSuhcKQvP3pvNDOXiDDHc0abRvg%2Fi6tHj%2F55Rjx3pdetMaCV%2B6CF4QuZ07SHCdjfgRsOE6JMcie3UyWS0hXw4jgM73Ou6WrnHtnJuc4KOxQ50z96e0Fa8CDDzK2I5fHK1SBEVkDE1zgBzgBE4y%2BQ6jPI3GySq8i1NlQ1Ta%2BmVefTujSOBBcW1RJZBE4B6SRbgcuPXPOyQPNt3DbgLctl7Kvt072bLmMdqk5XIVbZ7k577a6Rh5x2TIJvh7bK%2Fm8%2FnGuZco%2F3meh41JJ9DXwG1rtCWB6%2BwI6yd3Ef0AOEy1kZJAT8mh3wldg6AijhOpN1Gf%2FQrjPDTzz2X7TYHqaIqDcATCyxuq8BjqkAdKWGqd9cjh6oYMHdRk9m%2BD5tciVYOxTYybRHOwt0Ioh4Dk7efE4ItpWgXE%2BZmxsiKkk7mNL8%2FN0w2Tw4eY19GgQaMRE1mm%2FNntSpE%2B31VCOUifWZfY4qs0F1JHro6Jx44AYTjEG68BFpLZo4ml6vyrSjxeLLzaJhuALgiPx9sEJv6Khdy8ep5ODpsfDuoexbmQdgW%2FJEpL1KngJj%2B2%2BrgRzYF1C&X-Amz-Signature=656697ee971db65b96a6a741836201ad2d20d4fc4f7b22e0e9c9bf8f7a2c7840&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG25RASZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bg3rBj9UYflMHgBKfy26JooIECdmO0GODtr1ZImFdKAiB7LMdOAZvMniEni8q%2FL1YrnuI%2FaaTCIqLeWm3zmQOHxyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxX9lu%2BvWb5TRV62KtwDAso15NRU41i3tWzhfJVA0Zuw3gOnO0ZhvIh7Of%2BDb86cG3BPBVQh8mCsMP9qccxaQptYOlpqW4zT57uCBoNhdZe9xFsBBEJlCoaFuplbsLUIrTZ%2BGTAJEtzWI1eO8S7duvRtqJe%2BNfirIgRl6Ca3TcAjPD1Jxa89nIMiWvy3d9wAj11cOfQnU%2Bxcib9mjLPzKMGLRinZiNDAL4uihgmTOQkswCRt5UDIkxP10lMPLjXnilKjd9y1ov3iOwW%2B2T%2BaJk0%2BKPZW3WmYXzn7%2F274g3Jr3sbNfCw07G3rBFeo%2FIFw2vKtfV1YGy64yng76TCFME4EDued1Rx%2B7PHVbe90h%2FqV%2F%2BJk%2FScls%2B0m0bONpgYotxuaCf1PPA4HohXUL2q8xEGlKPubGL2GU6sxpx8V5qQoweIu80FkcDjio4qC1XF2Fh71ZBWNO5ZrWWedSBwd7JzaDzjbfCGV0p57uk%2BZs%2F%2ByquidAfbLsHhR92vIO8cPU6%2F3MNxi7%2B4l48bw7df9FsZVMFSUethja4GGrF0VmX7gLoUAS8c5w%2FvJSkMYAQKP0u0Wo1nCCcO0qfcKK2J4ZwliLONOwvE8Dh45mfnqXWVBN53e%2FA2QyEe42CrEaG2%2BpvZchSawFoafvk8w8sbqvAY6pgFH59OWCeSZctfGYZrOjdk9MNwV8%2BWPTz9KLiVVy9D98al%2FgNLfGaYIDsQCfQMCMbr1QISpQ1Sc1Jy0Z7pXNX%2ByeHafAi0i%2FHmXGBc%2B%2Bq7LxtIV08Gr0goKwHhTD1fp1tUmqtHJKfnOSTVXc0exJNRBwreM7yl0u57U84oseb3Qc%2BTCRWJ7HkXE9PAxEkjcwvVHTL4owJ3RzqWLCocBtGFmsAsjR3uY&X-Amz-Signature=0d0461c4248c25c405b4bb2055ff275fa4dda586e9640e7fa0572d687030bd0b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG25RASZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bg3rBj9UYflMHgBKfy26JooIECdmO0GODtr1ZImFdKAiB7LMdOAZvMniEni8q%2FL1YrnuI%2FaaTCIqLeWm3zmQOHxyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxX9lu%2BvWb5TRV62KtwDAso15NRU41i3tWzhfJVA0Zuw3gOnO0ZhvIh7Of%2BDb86cG3BPBVQh8mCsMP9qccxaQptYOlpqW4zT57uCBoNhdZe9xFsBBEJlCoaFuplbsLUIrTZ%2BGTAJEtzWI1eO8S7duvRtqJe%2BNfirIgRl6Ca3TcAjPD1Jxa89nIMiWvy3d9wAj11cOfQnU%2Bxcib9mjLPzKMGLRinZiNDAL4uihgmTOQkswCRt5UDIkxP10lMPLjXnilKjd9y1ov3iOwW%2B2T%2BaJk0%2BKPZW3WmYXzn7%2F274g3Jr3sbNfCw07G3rBFeo%2FIFw2vKtfV1YGy64yng76TCFME4EDued1Rx%2B7PHVbe90h%2FqV%2F%2BJk%2FScls%2B0m0bONpgYotxuaCf1PPA4HohXUL2q8xEGlKPubGL2GU6sxpx8V5qQoweIu80FkcDjio4qC1XF2Fh71ZBWNO5ZrWWedSBwd7JzaDzjbfCGV0p57uk%2BZs%2F%2ByquidAfbLsHhR92vIO8cPU6%2F3MNxi7%2B4l48bw7df9FsZVMFSUethja4GGrF0VmX7gLoUAS8c5w%2FvJSkMYAQKP0u0Wo1nCCcO0qfcKK2J4ZwliLONOwvE8Dh45mfnqXWVBN53e%2FA2QyEe42CrEaG2%2BpvZchSawFoafvk8w8sbqvAY6pgFH59OWCeSZctfGYZrOjdk9MNwV8%2BWPTz9KLiVVy9D98al%2FgNLfGaYIDsQCfQMCMbr1QISpQ1Sc1Jy0Z7pXNX%2ByeHafAi0i%2FHmXGBc%2B%2Bq7LxtIV08Gr0goKwHhTD1fp1tUmqtHJKfnOSTVXc0exJNRBwreM7yl0u57U84oseb3Qc%2BTCRWJ7HkXE9PAxEkjcwvVHTL4owJ3RzqWLCocBtGFmsAsjR3uY&X-Amz-Signature=260850fc1306cc362584347a08df834148d8288831456101c63c9254c69ecda1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG25RASZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bg3rBj9UYflMHgBKfy26JooIECdmO0GODtr1ZImFdKAiB7LMdOAZvMniEni8q%2FL1YrnuI%2FaaTCIqLeWm3zmQOHxyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxX9lu%2BvWb5TRV62KtwDAso15NRU41i3tWzhfJVA0Zuw3gOnO0ZhvIh7Of%2BDb86cG3BPBVQh8mCsMP9qccxaQptYOlpqW4zT57uCBoNhdZe9xFsBBEJlCoaFuplbsLUIrTZ%2BGTAJEtzWI1eO8S7duvRtqJe%2BNfirIgRl6Ca3TcAjPD1Jxa89nIMiWvy3d9wAj11cOfQnU%2Bxcib9mjLPzKMGLRinZiNDAL4uihgmTOQkswCRt5UDIkxP10lMPLjXnilKjd9y1ov3iOwW%2B2T%2BaJk0%2BKPZW3WmYXzn7%2F274g3Jr3sbNfCw07G3rBFeo%2FIFw2vKtfV1YGy64yng76TCFME4EDued1Rx%2B7PHVbe90h%2FqV%2F%2BJk%2FScls%2B0m0bONpgYotxuaCf1PPA4HohXUL2q8xEGlKPubGL2GU6sxpx8V5qQoweIu80FkcDjio4qC1XF2Fh71ZBWNO5ZrWWedSBwd7JzaDzjbfCGV0p57uk%2BZs%2F%2ByquidAfbLsHhR92vIO8cPU6%2F3MNxi7%2B4l48bw7df9FsZVMFSUethja4GGrF0VmX7gLoUAS8c5w%2FvJSkMYAQKP0u0Wo1nCCcO0qfcKK2J4ZwliLONOwvE8Dh45mfnqXWVBN53e%2FA2QyEe42CrEaG2%2BpvZchSawFoafvk8w8sbqvAY6pgFH59OWCeSZctfGYZrOjdk9MNwV8%2BWPTz9KLiVVy9D98al%2FgNLfGaYIDsQCfQMCMbr1QISpQ1Sc1Jy0Z7pXNX%2ByeHafAi0i%2FHmXGBc%2B%2Bq7LxtIV08Gr0goKwHhTD1fp1tUmqtHJKfnOSTVXc0exJNRBwreM7yl0u57U84oseb3Qc%2BTCRWJ7HkXE9PAxEkjcwvVHTL4owJ3RzqWLCocBtGFmsAsjR3uY&X-Amz-Signature=a5ec3c79efde4bb14ab7a892381fad611d7f9f6eb1f85e95e9f1c10ce97fe326&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG25RASZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bg3rBj9UYflMHgBKfy26JooIECdmO0GODtr1ZImFdKAiB7LMdOAZvMniEni8q%2FL1YrnuI%2FaaTCIqLeWm3zmQOHxyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxX9lu%2BvWb5TRV62KtwDAso15NRU41i3tWzhfJVA0Zuw3gOnO0ZhvIh7Of%2BDb86cG3BPBVQh8mCsMP9qccxaQptYOlpqW4zT57uCBoNhdZe9xFsBBEJlCoaFuplbsLUIrTZ%2BGTAJEtzWI1eO8S7duvRtqJe%2BNfirIgRl6Ca3TcAjPD1Jxa89nIMiWvy3d9wAj11cOfQnU%2Bxcib9mjLPzKMGLRinZiNDAL4uihgmTOQkswCRt5UDIkxP10lMPLjXnilKjd9y1ov3iOwW%2B2T%2BaJk0%2BKPZW3WmYXzn7%2F274g3Jr3sbNfCw07G3rBFeo%2FIFw2vKtfV1YGy64yng76TCFME4EDued1Rx%2B7PHVbe90h%2FqV%2F%2BJk%2FScls%2B0m0bONpgYotxuaCf1PPA4HohXUL2q8xEGlKPubGL2GU6sxpx8V5qQoweIu80FkcDjio4qC1XF2Fh71ZBWNO5ZrWWedSBwd7JzaDzjbfCGV0p57uk%2BZs%2F%2ByquidAfbLsHhR92vIO8cPU6%2F3MNxi7%2B4l48bw7df9FsZVMFSUethja4GGrF0VmX7gLoUAS8c5w%2FvJSkMYAQKP0u0Wo1nCCcO0qfcKK2J4ZwliLONOwvE8Dh45mfnqXWVBN53e%2FA2QyEe42CrEaG2%2BpvZchSawFoafvk8w8sbqvAY6pgFH59OWCeSZctfGYZrOjdk9MNwV8%2BWPTz9KLiVVy9D98al%2FgNLfGaYIDsQCfQMCMbr1QISpQ1Sc1Jy0Z7pXNX%2ByeHafAi0i%2FHmXGBc%2B%2Bq7LxtIV08Gr0goKwHhTD1fp1tUmqtHJKfnOSTVXc0exJNRBwreM7yl0u57U84oseb3Qc%2BTCRWJ7HkXE9PAxEkjcwvVHTL4owJ3RzqWLCocBtGFmsAsjR3uY&X-Amz-Signature=0b93e45c450677a4429aa0fdbd95fd6c79dee3921b531deb928f09de7d2fa303&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG25RASZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2Bg3rBj9UYflMHgBKfy26JooIECdmO0GODtr1ZImFdKAiB7LMdOAZvMniEni8q%2FL1YrnuI%2FaaTCIqLeWm3zmQOHxyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxX9lu%2BvWb5TRV62KtwDAso15NRU41i3tWzhfJVA0Zuw3gOnO0ZhvIh7Of%2BDb86cG3BPBVQh8mCsMP9qccxaQptYOlpqW4zT57uCBoNhdZe9xFsBBEJlCoaFuplbsLUIrTZ%2BGTAJEtzWI1eO8S7duvRtqJe%2BNfirIgRl6Ca3TcAjPD1Jxa89nIMiWvy3d9wAj11cOfQnU%2Bxcib9mjLPzKMGLRinZiNDAL4uihgmTOQkswCRt5UDIkxP10lMPLjXnilKjd9y1ov3iOwW%2B2T%2BaJk0%2BKPZW3WmYXzn7%2F274g3Jr3sbNfCw07G3rBFeo%2FIFw2vKtfV1YGy64yng76TCFME4EDued1Rx%2B7PHVbe90h%2FqV%2F%2BJk%2FScls%2B0m0bONpgYotxuaCf1PPA4HohXUL2q8xEGlKPubGL2GU6sxpx8V5qQoweIu80FkcDjio4qC1XF2Fh71ZBWNO5ZrWWedSBwd7JzaDzjbfCGV0p57uk%2BZs%2F%2ByquidAfbLsHhR92vIO8cPU6%2F3MNxi7%2B4l48bw7df9FsZVMFSUethja4GGrF0VmX7gLoUAS8c5w%2FvJSkMYAQKP0u0Wo1nCCcO0qfcKK2J4ZwliLONOwvE8Dh45mfnqXWVBN53e%2FA2QyEe42CrEaG2%2BpvZchSawFoafvk8w8sbqvAY6pgFH59OWCeSZctfGYZrOjdk9MNwV8%2BWPTz9KLiVVy9D98al%2FgNLfGaYIDsQCfQMCMbr1QISpQ1Sc1Jy0Z7pXNX%2ByeHafAi0i%2FHmXGBc%2B%2Bq7LxtIV08Gr0goKwHhTD1fp1tUmqtHJKfnOSTVXc0exJNRBwreM7yl0u57U84oseb3Qc%2BTCRWJ7HkXE9PAxEkjcwvVHTL4owJ3RzqWLCocBtGFmsAsjR3uY&X-Amz-Signature=e8467d3524c88f3e3637088bbaf73651d7e8d98657578a3189009e8488f10dd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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


