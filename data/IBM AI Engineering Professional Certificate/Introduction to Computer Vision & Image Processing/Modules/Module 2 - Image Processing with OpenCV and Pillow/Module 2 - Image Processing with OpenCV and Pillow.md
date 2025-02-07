

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJVRDFK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFiKDoBsD%2FeaRs8UZAeMPVB3dwC36waKsa4ZsTCdYUxAiEA41K8CyL59O64SfDHn7jc3OVHP7cl7yzNTSnrvcjpKg0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKXe50pIY3gs5mq5rCrcA9rnPqmBjork8Vci1pGYudht1GvSLxgQQDVuw8mUm4%2FY%2FzPT%2FPY%2FfVQYMX9DcVlyDGAILzCoRuixL5Sv5ygDUZ0S79WKbUkAn%2F8iEOpF5WEiS8Bg9ntNmKty9IlSqX%2BQj%2FpU1QXIA1AlMF%2BqpP1UWxxcxS9f341RinqOSwLz1ryVC6Xk6y5McdnEt%2FQZCtPLdfPRn08R7ley8jNnVLYj0j5re9X3P5DY2NbdevHB7RV4dC%2FOA%2B1eJKpEiXoGJ%2B1LEsVhKfS4bCYYsB3ISzYPqDJyUqZnpH1Oc9KmM2A9DSGYzOFYYY%2BUOK2WyQAOBp0CHBTDobshiOb1TVJ3FDo%2BdFGHDayL56JE3OOgHmx7wstYetu07x3XgKk%2BxDhbteF%2Bn6nnaNmlqC1C3hZa5RPrRnrr0Q7fGUwZcKTNpviBQl5nkdiDjBg0mH8BPPbrM7LN99jFsVZW7Kss71EIYjhsujufOJVgNTnzh0MIGzsJewWWS5tz7azpK6E6%2FnM8ftsSuzPSsp4eAhvirAplrT3PDzCG35GmAQHFjB7lUvL0k2mEqp%2BPHS%2BmFT7nOgHiwa9Fr2EE6KWKR5lxwZUa%2FLv8owMJnKZnYZFIACqWVax69aI%2BmUUhtl%2FiDHhrNLAQMKaalb0GOqUB6j8miT6R3LBEvQXEOlHa1WzRvzo8yFHzJJsuYuKSKUIBePMw%2BWLtXfeJOCsCOPYGdTbz8zyNaGUpp0U7ru0WA9l361vNTYW1q%2F9zobERzDHmF1%2FCnMYSQug6MP8OHCJih%2BltQ4UoQy1VGlqHRTDKNUo5ujhPJwXD0v1Sl0JfoP6xwl5kBoLBySsDsjh0gQPd3ZV3IJhGCEE8H5f1ZkoNUE4evdj8&X-Amz-Signature=bf6c95f32debabcf03b72c41431d476e43e4ff7965220853cab95af724fec37d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7VDSRHV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHyzpDuGGZ%2BleEQfeupSQ%2BbpLmEPCWhORWyyMQ0wcWPrAiEAie8YZEr8tlvwZfhrVG%2F9%2BskTDIzeqZXjsBpnZeHSvDYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2FKRsPvoKA2UfqvUCrcAyttPiFURpKdqOjrvwzGx3DFzrQ5X087rQfBa0HbEBS1zJ5x1zZ42oBnuDF3LX9OyPJJU3%2Bn516z6I32bAdgpk0DEZkGl3oN5aNXox4adzJrMvxiF%2BOBcPFW7l0zHX1WlDaFV4Aw%2BSRUICx8YKCA8MS2a5h4%2F%2B8L0nWSVDXmI01f5aksLpfmg90F5TPTaocbuc%2BadB1tF72%2BpEXCidexWw3EjujbrU44bCF7t%2BR0%2F1P2ZSh%2FgB5pATWO%2B3frLeccrZJzlk08TATR3LyqIVLZYWGBXhETfnHGhZ3HiVo8hR0arA4JHD8GzYfMWl6nldU8xEzHo9w4xCpd47SOinIUWmhsJFesCaJWadlxFK7S82foo8D3FhddZaHmY7Aq82XZrY3y2b8hLdslkyYQAnVyYMji49uaYsWrxcjOonWfFBJspFHFXj50EmHMOCdm2jZUW%2BPytKa5A7rRRcy%2F%2FBOVCpT9uiHkdh1TgCm9dgi3u4IFviLOJ87w9pbw93BpEONj5vc5WBQBRBwkfk0OKOxxYRD93XaMbZXq3YwQQJZiQkOczweXgXZF3HeVUf%2F%2BxU7xB9iZViudggJOJ0dJU6E2gbUd0LcmtaNKCUmvxBaDM7wX2r3OZmIKDxT1ijkQMNmalb0GOqUByFvHCC9DysC24hI03BEaqXu5Jl5guCeAZNdlGyzT2S96eJbwsl9d6h%2BhrLnYMMJCcV%2Fr6I%2BsCCUO2gKbPuD2ILxalz1rocxM7vs5kvo9BCGTR5VPWo7L%2FRf48tjZsf34XqZ%2F5rhq5A%2FbC9%2F0VBk8BMgW4ml5rnrHKAk7wFZVt5iTsAUAanj0%2Ff3KmadnP%2FKL8M4QQgyqU%2F44QbrVvKJEheCIuMEf&X-Amz-Signature=b8e9c0664dde13e30fe0abbe7b85f67d9b514c0ccf289493ce741e469dca82d2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7VDSRHV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHyzpDuGGZ%2BleEQfeupSQ%2BbpLmEPCWhORWyyMQ0wcWPrAiEAie8YZEr8tlvwZfhrVG%2F9%2BskTDIzeqZXjsBpnZeHSvDYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2FKRsPvoKA2UfqvUCrcAyttPiFURpKdqOjrvwzGx3DFzrQ5X087rQfBa0HbEBS1zJ5x1zZ42oBnuDF3LX9OyPJJU3%2Bn516z6I32bAdgpk0DEZkGl3oN5aNXox4adzJrMvxiF%2BOBcPFW7l0zHX1WlDaFV4Aw%2BSRUICx8YKCA8MS2a5h4%2F%2B8L0nWSVDXmI01f5aksLpfmg90F5TPTaocbuc%2BadB1tF72%2BpEXCidexWw3EjujbrU44bCF7t%2BR0%2F1P2ZSh%2FgB5pATWO%2B3frLeccrZJzlk08TATR3LyqIVLZYWGBXhETfnHGhZ3HiVo8hR0arA4JHD8GzYfMWl6nldU8xEzHo9w4xCpd47SOinIUWmhsJFesCaJWadlxFK7S82foo8D3FhddZaHmY7Aq82XZrY3y2b8hLdslkyYQAnVyYMji49uaYsWrxcjOonWfFBJspFHFXj50EmHMOCdm2jZUW%2BPytKa5A7rRRcy%2F%2FBOVCpT9uiHkdh1TgCm9dgi3u4IFviLOJ87w9pbw93BpEONj5vc5WBQBRBwkfk0OKOxxYRD93XaMbZXq3YwQQJZiQkOczweXgXZF3HeVUf%2F%2BxU7xB9iZViudggJOJ0dJU6E2gbUd0LcmtaNKCUmvxBaDM7wX2r3OZmIKDxT1ijkQMNmalb0GOqUByFvHCC9DysC24hI03BEaqXu5Jl5guCeAZNdlGyzT2S96eJbwsl9d6h%2BhrLnYMMJCcV%2Fr6I%2BsCCUO2gKbPuD2ILxalz1rocxM7vs5kvo9BCGTR5VPWo7L%2FRf48tjZsf34XqZ%2F5rhq5A%2FbC9%2F0VBk8BMgW4ml5rnrHKAk7wFZVt5iTsAUAanj0%2Ff3KmadnP%2FKL8M4QQgyqU%2F44QbrVvKJEheCIuMEf&X-Amz-Signature=3f23c8b32a92f0ec6bbcacb309be85805731ae708eaf1e63b33fc92a3e7f291c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7VDSRHV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHyzpDuGGZ%2BleEQfeupSQ%2BbpLmEPCWhORWyyMQ0wcWPrAiEAie8YZEr8tlvwZfhrVG%2F9%2BskTDIzeqZXjsBpnZeHSvDYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2FKRsPvoKA2UfqvUCrcAyttPiFURpKdqOjrvwzGx3DFzrQ5X087rQfBa0HbEBS1zJ5x1zZ42oBnuDF3LX9OyPJJU3%2Bn516z6I32bAdgpk0DEZkGl3oN5aNXox4adzJrMvxiF%2BOBcPFW7l0zHX1WlDaFV4Aw%2BSRUICx8YKCA8MS2a5h4%2F%2B8L0nWSVDXmI01f5aksLpfmg90F5TPTaocbuc%2BadB1tF72%2BpEXCidexWw3EjujbrU44bCF7t%2BR0%2F1P2ZSh%2FgB5pATWO%2B3frLeccrZJzlk08TATR3LyqIVLZYWGBXhETfnHGhZ3HiVo8hR0arA4JHD8GzYfMWl6nldU8xEzHo9w4xCpd47SOinIUWmhsJFesCaJWadlxFK7S82foo8D3FhddZaHmY7Aq82XZrY3y2b8hLdslkyYQAnVyYMji49uaYsWrxcjOonWfFBJspFHFXj50EmHMOCdm2jZUW%2BPytKa5A7rRRcy%2F%2FBOVCpT9uiHkdh1TgCm9dgi3u4IFviLOJ87w9pbw93BpEONj5vc5WBQBRBwkfk0OKOxxYRD93XaMbZXq3YwQQJZiQkOczweXgXZF3HeVUf%2F%2BxU7xB9iZViudggJOJ0dJU6E2gbUd0LcmtaNKCUmvxBaDM7wX2r3OZmIKDxT1ijkQMNmalb0GOqUByFvHCC9DysC24hI03BEaqXu5Jl5guCeAZNdlGyzT2S96eJbwsl9d6h%2BhrLnYMMJCcV%2Fr6I%2BsCCUO2gKbPuD2ILxalz1rocxM7vs5kvo9BCGTR5VPWo7L%2FRf48tjZsf34XqZ%2F5rhq5A%2FbC9%2F0VBk8BMgW4ml5rnrHKAk7wFZVt5iTsAUAanj0%2Ff3KmadnP%2FKL8M4QQgyqU%2F44QbrVvKJEheCIuMEf&X-Amz-Signature=ea76e2d762df3ac9f78ec1d2159509c1c2b59f62a280c05a8e1c70e68c68832e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7VDSRHV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHyzpDuGGZ%2BleEQfeupSQ%2BbpLmEPCWhORWyyMQ0wcWPrAiEAie8YZEr8tlvwZfhrVG%2F9%2BskTDIzeqZXjsBpnZeHSvDYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2FKRsPvoKA2UfqvUCrcAyttPiFURpKdqOjrvwzGx3DFzrQ5X087rQfBa0HbEBS1zJ5x1zZ42oBnuDF3LX9OyPJJU3%2Bn516z6I32bAdgpk0DEZkGl3oN5aNXox4adzJrMvxiF%2BOBcPFW7l0zHX1WlDaFV4Aw%2BSRUICx8YKCA8MS2a5h4%2F%2B8L0nWSVDXmI01f5aksLpfmg90F5TPTaocbuc%2BadB1tF72%2BpEXCidexWw3EjujbrU44bCF7t%2BR0%2F1P2ZSh%2FgB5pATWO%2B3frLeccrZJzlk08TATR3LyqIVLZYWGBXhETfnHGhZ3HiVo8hR0arA4JHD8GzYfMWl6nldU8xEzHo9w4xCpd47SOinIUWmhsJFesCaJWadlxFK7S82foo8D3FhddZaHmY7Aq82XZrY3y2b8hLdslkyYQAnVyYMji49uaYsWrxcjOonWfFBJspFHFXj50EmHMOCdm2jZUW%2BPytKa5A7rRRcy%2F%2FBOVCpT9uiHkdh1TgCm9dgi3u4IFviLOJ87w9pbw93BpEONj5vc5WBQBRBwkfk0OKOxxYRD93XaMbZXq3YwQQJZiQkOczweXgXZF3HeVUf%2F%2BxU7xB9iZViudggJOJ0dJU6E2gbUd0LcmtaNKCUmvxBaDM7wX2r3OZmIKDxT1ijkQMNmalb0GOqUByFvHCC9DysC24hI03BEaqXu5Jl5guCeAZNdlGyzT2S96eJbwsl9d6h%2BhrLnYMMJCcV%2Fr6I%2BsCCUO2gKbPuD2ILxalz1rocxM7vs5kvo9BCGTR5VPWo7L%2FRf48tjZsf34XqZ%2F5rhq5A%2FbC9%2F0VBk8BMgW4ml5rnrHKAk7wFZVt5iTsAUAanj0%2Ff3KmadnP%2FKL8M4QQgyqU%2F44QbrVvKJEheCIuMEf&X-Amz-Signature=88ab0407694d102cecaa3eb1c9f9c5566f15d1a91d655417847c74cab2ac25fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7VDSRHV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHyzpDuGGZ%2BleEQfeupSQ%2BbpLmEPCWhORWyyMQ0wcWPrAiEAie8YZEr8tlvwZfhrVG%2F9%2BskTDIzeqZXjsBpnZeHSvDYq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2FKRsPvoKA2UfqvUCrcAyttPiFURpKdqOjrvwzGx3DFzrQ5X087rQfBa0HbEBS1zJ5x1zZ42oBnuDF3LX9OyPJJU3%2Bn516z6I32bAdgpk0DEZkGl3oN5aNXox4adzJrMvxiF%2BOBcPFW7l0zHX1WlDaFV4Aw%2BSRUICx8YKCA8MS2a5h4%2F%2B8L0nWSVDXmI01f5aksLpfmg90F5TPTaocbuc%2BadB1tF72%2BpEXCidexWw3EjujbrU44bCF7t%2BR0%2F1P2ZSh%2FgB5pATWO%2B3frLeccrZJzlk08TATR3LyqIVLZYWGBXhETfnHGhZ3HiVo8hR0arA4JHD8GzYfMWl6nldU8xEzHo9w4xCpd47SOinIUWmhsJFesCaJWadlxFK7S82foo8D3FhddZaHmY7Aq82XZrY3y2b8hLdslkyYQAnVyYMji49uaYsWrxcjOonWfFBJspFHFXj50EmHMOCdm2jZUW%2BPytKa5A7rRRcy%2F%2FBOVCpT9uiHkdh1TgCm9dgi3u4IFviLOJ87w9pbw93BpEONj5vc5WBQBRBwkfk0OKOxxYRD93XaMbZXq3YwQQJZiQkOczweXgXZF3HeVUf%2F%2BxU7xB9iZViudggJOJ0dJU6E2gbUd0LcmtaNKCUmvxBaDM7wX2r3OZmIKDxT1ijkQMNmalb0GOqUByFvHCC9DysC24hI03BEaqXu5Jl5guCeAZNdlGyzT2S96eJbwsl9d6h%2BhrLnYMMJCcV%2Fr6I%2BsCCUO2gKbPuD2ILxalz1rocxM7vs5kvo9BCGTR5VPWo7L%2FRf48tjZsf34XqZ%2F5rhq5A%2FbC9%2F0VBk8BMgW4ml5rnrHKAk7wFZVt5iTsAUAanj0%2Ff3KmadnP%2FKL8M4QQgyqU%2F44QbrVvKJEheCIuMEf&X-Amz-Signature=8bdea4605016f6e8826a992be600bc96c12a75bb41c310a0a42efc76aeea093b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJVRDFK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFiKDoBsD%2FeaRs8UZAeMPVB3dwC36waKsa4ZsTCdYUxAiEA41K8CyL59O64SfDHn7jc3OVHP7cl7yzNTSnrvcjpKg0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKXe50pIY3gs5mq5rCrcA9rnPqmBjork8Vci1pGYudht1GvSLxgQQDVuw8mUm4%2FY%2FzPT%2FPY%2FfVQYMX9DcVlyDGAILzCoRuixL5Sv5ygDUZ0S79WKbUkAn%2F8iEOpF5WEiS8Bg9ntNmKty9IlSqX%2BQj%2FpU1QXIA1AlMF%2BqpP1UWxxcxS9f341RinqOSwLz1ryVC6Xk6y5McdnEt%2FQZCtPLdfPRn08R7ley8jNnVLYj0j5re9X3P5DY2NbdevHB7RV4dC%2FOA%2B1eJKpEiXoGJ%2B1LEsVhKfS4bCYYsB3ISzYPqDJyUqZnpH1Oc9KmM2A9DSGYzOFYYY%2BUOK2WyQAOBp0CHBTDobshiOb1TVJ3FDo%2BdFGHDayL56JE3OOgHmx7wstYetu07x3XgKk%2BxDhbteF%2Bn6nnaNmlqC1C3hZa5RPrRnrr0Q7fGUwZcKTNpviBQl5nkdiDjBg0mH8BPPbrM7LN99jFsVZW7Kss71EIYjhsujufOJVgNTnzh0MIGzsJewWWS5tz7azpK6E6%2FnM8ftsSuzPSsp4eAhvirAplrT3PDzCG35GmAQHFjB7lUvL0k2mEqp%2BPHS%2BmFT7nOgHiwa9Fr2EE6KWKR5lxwZUa%2FLv8owMJnKZnYZFIACqWVax69aI%2BmUUhtl%2FiDHhrNLAQMKaalb0GOqUB6j8miT6R3LBEvQXEOlHa1WzRvzo8yFHzJJsuYuKSKUIBePMw%2BWLtXfeJOCsCOPYGdTbz8zyNaGUpp0U7ru0WA9l361vNTYW1q%2F9zobERzDHmF1%2FCnMYSQug6MP8OHCJih%2BltQ4UoQy1VGlqHRTDKNUo5ujhPJwXD0v1Sl0JfoP6xwl5kBoLBySsDsjh0gQPd3ZV3IJhGCEE8H5f1ZkoNUE4evdj8&X-Amz-Signature=b06a8e31de65759ba4411915c1ba252b3e11df19a5a27cb079ca633de2fb833f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJVRDFK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFiKDoBsD%2FeaRs8UZAeMPVB3dwC36waKsa4ZsTCdYUxAiEA41K8CyL59O64SfDHn7jc3OVHP7cl7yzNTSnrvcjpKg0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKXe50pIY3gs5mq5rCrcA9rnPqmBjork8Vci1pGYudht1GvSLxgQQDVuw8mUm4%2FY%2FzPT%2FPY%2FfVQYMX9DcVlyDGAILzCoRuixL5Sv5ygDUZ0S79WKbUkAn%2F8iEOpF5WEiS8Bg9ntNmKty9IlSqX%2BQj%2FpU1QXIA1AlMF%2BqpP1UWxxcxS9f341RinqOSwLz1ryVC6Xk6y5McdnEt%2FQZCtPLdfPRn08R7ley8jNnVLYj0j5re9X3P5DY2NbdevHB7RV4dC%2FOA%2B1eJKpEiXoGJ%2B1LEsVhKfS4bCYYsB3ISzYPqDJyUqZnpH1Oc9KmM2A9DSGYzOFYYY%2BUOK2WyQAOBp0CHBTDobshiOb1TVJ3FDo%2BdFGHDayL56JE3OOgHmx7wstYetu07x3XgKk%2BxDhbteF%2Bn6nnaNmlqC1C3hZa5RPrRnrr0Q7fGUwZcKTNpviBQl5nkdiDjBg0mH8BPPbrM7LN99jFsVZW7Kss71EIYjhsujufOJVgNTnzh0MIGzsJewWWS5tz7azpK6E6%2FnM8ftsSuzPSsp4eAhvirAplrT3PDzCG35GmAQHFjB7lUvL0k2mEqp%2BPHS%2BmFT7nOgHiwa9Fr2EE6KWKR5lxwZUa%2FLv8owMJnKZnYZFIACqWVax69aI%2BmUUhtl%2FiDHhrNLAQMKaalb0GOqUB6j8miT6R3LBEvQXEOlHa1WzRvzo8yFHzJJsuYuKSKUIBePMw%2BWLtXfeJOCsCOPYGdTbz8zyNaGUpp0U7ru0WA9l361vNTYW1q%2F9zobERzDHmF1%2FCnMYSQug6MP8OHCJih%2BltQ4UoQy1VGlqHRTDKNUo5ujhPJwXD0v1Sl0JfoP6xwl5kBoLBySsDsjh0gQPd3ZV3IJhGCEE8H5f1ZkoNUE4evdj8&X-Amz-Signature=50a32320b0f986d097cb7aa4e4382f47fb0406beefa7ba86a18a58d80e1ee61f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJVRDFK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFiKDoBsD%2FeaRs8UZAeMPVB3dwC36waKsa4ZsTCdYUxAiEA41K8CyL59O64SfDHn7jc3OVHP7cl7yzNTSnrvcjpKg0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKXe50pIY3gs5mq5rCrcA9rnPqmBjork8Vci1pGYudht1GvSLxgQQDVuw8mUm4%2FY%2FzPT%2FPY%2FfVQYMX9DcVlyDGAILzCoRuixL5Sv5ygDUZ0S79WKbUkAn%2F8iEOpF5WEiS8Bg9ntNmKty9IlSqX%2BQj%2FpU1QXIA1AlMF%2BqpP1UWxxcxS9f341RinqOSwLz1ryVC6Xk6y5McdnEt%2FQZCtPLdfPRn08R7ley8jNnVLYj0j5re9X3P5DY2NbdevHB7RV4dC%2FOA%2B1eJKpEiXoGJ%2B1LEsVhKfS4bCYYsB3ISzYPqDJyUqZnpH1Oc9KmM2A9DSGYzOFYYY%2BUOK2WyQAOBp0CHBTDobshiOb1TVJ3FDo%2BdFGHDayL56JE3OOgHmx7wstYetu07x3XgKk%2BxDhbteF%2Bn6nnaNmlqC1C3hZa5RPrRnrr0Q7fGUwZcKTNpviBQl5nkdiDjBg0mH8BPPbrM7LN99jFsVZW7Kss71EIYjhsujufOJVgNTnzh0MIGzsJewWWS5tz7azpK6E6%2FnM8ftsSuzPSsp4eAhvirAplrT3PDzCG35GmAQHFjB7lUvL0k2mEqp%2BPHS%2BmFT7nOgHiwa9Fr2EE6KWKR5lxwZUa%2FLv8owMJnKZnYZFIACqWVax69aI%2BmUUhtl%2FiDHhrNLAQMKaalb0GOqUB6j8miT6R3LBEvQXEOlHa1WzRvzo8yFHzJJsuYuKSKUIBePMw%2BWLtXfeJOCsCOPYGdTbz8zyNaGUpp0U7ru0WA9l361vNTYW1q%2F9zobERzDHmF1%2FCnMYSQug6MP8OHCJih%2BltQ4UoQy1VGlqHRTDKNUo5ujhPJwXD0v1Sl0JfoP6xwl5kBoLBySsDsjh0gQPd3ZV3IJhGCEE8H5f1ZkoNUE4evdj8&X-Amz-Signature=62429d1e625a0e69e5a2972ad68cd657e710d5b8e0bbf03a5e2b7ee79abed284&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJVRDFK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFiKDoBsD%2FeaRs8UZAeMPVB3dwC36waKsa4ZsTCdYUxAiEA41K8CyL59O64SfDHn7jc3OVHP7cl7yzNTSnrvcjpKg0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKXe50pIY3gs5mq5rCrcA9rnPqmBjork8Vci1pGYudht1GvSLxgQQDVuw8mUm4%2FY%2FzPT%2FPY%2FfVQYMX9DcVlyDGAILzCoRuixL5Sv5ygDUZ0S79WKbUkAn%2F8iEOpF5WEiS8Bg9ntNmKty9IlSqX%2BQj%2FpU1QXIA1AlMF%2BqpP1UWxxcxS9f341RinqOSwLz1ryVC6Xk6y5McdnEt%2FQZCtPLdfPRn08R7ley8jNnVLYj0j5re9X3P5DY2NbdevHB7RV4dC%2FOA%2B1eJKpEiXoGJ%2B1LEsVhKfS4bCYYsB3ISzYPqDJyUqZnpH1Oc9KmM2A9DSGYzOFYYY%2BUOK2WyQAOBp0CHBTDobshiOb1TVJ3FDo%2BdFGHDayL56JE3OOgHmx7wstYetu07x3XgKk%2BxDhbteF%2Bn6nnaNmlqC1C3hZa5RPrRnrr0Q7fGUwZcKTNpviBQl5nkdiDjBg0mH8BPPbrM7LN99jFsVZW7Kss71EIYjhsujufOJVgNTnzh0MIGzsJewWWS5tz7azpK6E6%2FnM8ftsSuzPSsp4eAhvirAplrT3PDzCG35GmAQHFjB7lUvL0k2mEqp%2BPHS%2BmFT7nOgHiwa9Fr2EE6KWKR5lxwZUa%2FLv8owMJnKZnYZFIACqWVax69aI%2BmUUhtl%2FiDHhrNLAQMKaalb0GOqUB6j8miT6R3LBEvQXEOlHa1WzRvzo8yFHzJJsuYuKSKUIBePMw%2BWLtXfeJOCsCOPYGdTbz8zyNaGUpp0U7ru0WA9l361vNTYW1q%2F9zobERzDHmF1%2FCnMYSQug6MP8OHCJih%2BltQ4UoQy1VGlqHRTDKNUo5ujhPJwXD0v1Sl0JfoP6xwl5kBoLBySsDsjh0gQPd3ZV3IJhGCEE8H5f1ZkoNUE4evdj8&X-Amz-Signature=1790fea0c7db87d7b0194a88c539788e913daa28f2325f0997a6ed2ed837d182&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJVRDFK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHFiKDoBsD%2FeaRs8UZAeMPVB3dwC36waKsa4ZsTCdYUxAiEA41K8CyL59O64SfDHn7jc3OVHP7cl7yzNTSnrvcjpKg0q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKXe50pIY3gs5mq5rCrcA9rnPqmBjork8Vci1pGYudht1GvSLxgQQDVuw8mUm4%2FY%2FzPT%2FPY%2FfVQYMX9DcVlyDGAILzCoRuixL5Sv5ygDUZ0S79WKbUkAn%2F8iEOpF5WEiS8Bg9ntNmKty9IlSqX%2BQj%2FpU1QXIA1AlMF%2BqpP1UWxxcxS9f341RinqOSwLz1ryVC6Xk6y5McdnEt%2FQZCtPLdfPRn08R7ley8jNnVLYj0j5re9X3P5DY2NbdevHB7RV4dC%2FOA%2B1eJKpEiXoGJ%2B1LEsVhKfS4bCYYsB3ISzYPqDJyUqZnpH1Oc9KmM2A9DSGYzOFYYY%2BUOK2WyQAOBp0CHBTDobshiOb1TVJ3FDo%2BdFGHDayL56JE3OOgHmx7wstYetu07x3XgKk%2BxDhbteF%2Bn6nnaNmlqC1C3hZa5RPrRnrr0Q7fGUwZcKTNpviBQl5nkdiDjBg0mH8BPPbrM7LN99jFsVZW7Kss71EIYjhsujufOJVgNTnzh0MIGzsJewWWS5tz7azpK6E6%2FnM8ftsSuzPSsp4eAhvirAplrT3PDzCG35GmAQHFjB7lUvL0k2mEqp%2BPHS%2BmFT7nOgHiwa9Fr2EE6KWKR5lxwZUa%2FLv8owMJnKZnYZFIACqWVax69aI%2BmUUhtl%2FiDHhrNLAQMKaalb0GOqUB6j8miT6R3LBEvQXEOlHa1WzRvzo8yFHzJJsuYuKSKUIBePMw%2BWLtXfeJOCsCOPYGdTbz8zyNaGUpp0U7ru0WA9l361vNTYW1q%2F9zobERzDHmF1%2FCnMYSQug6MP8OHCJih%2BltQ4UoQy1VGlqHRTDKNUo5ujhPJwXD0v1Sl0JfoP6xwl5kBoLBySsDsjh0gQPd3ZV3IJhGCEE8H5f1ZkoNUE4evdj8&X-Amz-Signature=6381a429bbfbd5ce2a8a311c7102a05c316d4d837ecd58216e9600907bbcd7d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


