

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX6VQST%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOEmxWcbGho1uj884u%2Fs0S5ZMf7Ate50dwlDUQrnW9iAIgWZbwNFAlL2dVuawg%2BZqCOsFas80eW8AwntNolWm7%2BVgqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcL7WcqK3Ounq4dDSrcA4DcVvfCJBmFJfm4om%2BgJySckvjj934q5lgNVUl34UGKfnQ4E7V1HynJi3lN9uEpmUnxQY3CZzV1QlxgSJn8%2BAkMPRYJJsZQJKuHEIL0MlbyYnBg3YEXAHUoVlbbUKwZdSzgxQ6tnbJSPMc9289jQYgbBLxs3R63ufsQ8tahbtLYZpNqRv5zHTjNDcwntisb%2Fcmo9ZQ7Ur2AEPUgCqHFBslPiXzPbqa%2BGLoL1luU6qWH3hVe39mcLohv%2B5JMT2NfwqPo7NTuHeGGFjkHEEPZh5vnJq5E8ctniodIhE0n6Zz08ybt%2BKa99Ek%2BGF0zqWeHnYdsrFpRSU1fnKgt1C8Osw0oBAk5FHQkCqm6xaMEbFNtWoEDwU%2F3J3dRhQR6COmZQx3n%2BVazDkebpbihAbq4NFsgNfGvI8zjuQaY90MV1fKfnTZogFkr8k5aHM%2BLOtIeWdCeFfj1PY8UCHygK3W9FSId5%2Fk9%2FTc7DMCn0NzwW3IpdubZjpGNgVA8VqNqB9nx9TQCkVLFSHLFAtWvlr%2BaH0T7meggpn8fBlC0%2BqKr8TF7dHdk8K1ttuNTft5svZCfIxR53OPXcrh3bWLohJL88Cqb2LwBUxeUklFeZ5xqHpAyqmABeAzWdxTJwfE0MOjr7LwGOqUBgiSj6Mdo8o1sAx5tHto8JeDRhdrEP7p8%2BfTpj7lBMPhlZOb02sgGJMFJrykcK0ZbGBcvp0JEkaa3nKC%2BQw%2Fj7%2BfELlVUAzqAXKA%2BSHdxLv240HEjB1PoLM%2BWCCMG7uBDcX6Rll7qFageSBzY9slTJWtuimnM6lz62NM2B4t0gTEKslCRvWk1a2dDqSf%2BCoOc2MDQPSRUzlFYLPk3a8mTffFVVwnK&X-Amz-Signature=1fbdff7bafb77b5b0a5328527312a2a3fb5700a48d3508c77c261930165995bc&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3ZWPEIA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq%2FwlOtrv1Q6zj7MDjuoyTZoY1XRUpYr9a53wp4kCMcQIgM16tNVF17f%2BQ8O2vOgQ45%2BF08I%2BfewXvZ490gKjXrzMqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYqr4xcNY8HCIuuLCrcAyzw2JyLX2lgdjlU2P2w0KLZJhrldKEowBr9KLLBF4%2BYMJUX4ADFwT6Afrq8JyWQufbcbx8hq4bYwj3FUyX%2FzNj90skyGwgcBx0kImQX6bwJa6BOMJeCGYyTYnErrBnWYDAjY94ije8mZMGJxx02eau5fO3U7njT2%2FWpnMJO299y8N3nrWoDPXzoUdcg%2FQrMaie%2BVcPXMWOepAXqoetCQFUB2VWsDVTGtam8SNLxFoh8MxkUngI7UQtkLReP56nu2aam5gExhdpicrBv3RsFf1eELJ%2FWpozHgOX7JII4VlrBYVpOQ9LSoet%2Bs1UUdt4smOXKwKBTgErKJqYixCBGs%2Bk2GrS3MVunYSq7fj5kCDpY0QGKU3jNM%2FXE7CoV3WyBLZtEXiBg7BHjMX0Bb45A%2FVcp0QkvWm8JSQHGzgVeS1Y1VhjnTmr%2FpqEy3gTj6tq0QbOCSuyWE7BeM4d4l%2B64tXS9YYf1oZf3cEu11CTYnfkXczrzRK6eTvmUFQIDH0lnHN0G3zU1LvnCFJ%2B3MoRPCIqmee2odhoDZ05j7MFY%2FFSKkzdPQA66WeUGuBGz4byk06kyimpFTKerezBEARGY6%2FU1XRmcDPR6ZWnseDocR8n0C9S6yv%2B9WrIAjo9RMIfr7LwGOqUBS8ne1NB7zg%2BZ%2F1z1pUhkCp3wz20CuuzaE8OntkiNHFlzwAcRCFXQS1gmU2K%2Fs08iaDa74GCoJ4RsstaBFVpqCj6Fs9RfG7x3OpWgdcZzta05tjLKsUpr39y5jJFclokgijcNYp67xXq1LD2w637xVu4WTYwG3AipDS4J%2F2YK8h55TrACGdXERTe5CYJ%2FcihqpYbrLGlzQowOEpUfT8%2B7kSHuvQHl&X-Amz-Signature=8ba25253086728731efe8894628bbca0586cb5fbf745fa2828bbbe1248d10bf2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3ZWPEIA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq%2FwlOtrv1Q6zj7MDjuoyTZoY1XRUpYr9a53wp4kCMcQIgM16tNVF17f%2BQ8O2vOgQ45%2BF08I%2BfewXvZ490gKjXrzMqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYqr4xcNY8HCIuuLCrcAyzw2JyLX2lgdjlU2P2w0KLZJhrldKEowBr9KLLBF4%2BYMJUX4ADFwT6Afrq8JyWQufbcbx8hq4bYwj3FUyX%2FzNj90skyGwgcBx0kImQX6bwJa6BOMJeCGYyTYnErrBnWYDAjY94ije8mZMGJxx02eau5fO3U7njT2%2FWpnMJO299y8N3nrWoDPXzoUdcg%2FQrMaie%2BVcPXMWOepAXqoetCQFUB2VWsDVTGtam8SNLxFoh8MxkUngI7UQtkLReP56nu2aam5gExhdpicrBv3RsFf1eELJ%2FWpozHgOX7JII4VlrBYVpOQ9LSoet%2Bs1UUdt4smOXKwKBTgErKJqYixCBGs%2Bk2GrS3MVunYSq7fj5kCDpY0QGKU3jNM%2FXE7CoV3WyBLZtEXiBg7BHjMX0Bb45A%2FVcp0QkvWm8JSQHGzgVeS1Y1VhjnTmr%2FpqEy3gTj6tq0QbOCSuyWE7BeM4d4l%2B64tXS9YYf1oZf3cEu11CTYnfkXczrzRK6eTvmUFQIDH0lnHN0G3zU1LvnCFJ%2B3MoRPCIqmee2odhoDZ05j7MFY%2FFSKkzdPQA66WeUGuBGz4byk06kyimpFTKerezBEARGY6%2FU1XRmcDPR6ZWnseDocR8n0C9S6yv%2B9WrIAjo9RMIfr7LwGOqUBS8ne1NB7zg%2BZ%2F1z1pUhkCp3wz20CuuzaE8OntkiNHFlzwAcRCFXQS1gmU2K%2Fs08iaDa74GCoJ4RsstaBFVpqCj6Fs9RfG7x3OpWgdcZzta05tjLKsUpr39y5jJFclokgijcNYp67xXq1LD2w637xVu4WTYwG3AipDS4J%2F2YK8h55TrACGdXERTe5CYJ%2FcihqpYbrLGlzQowOEpUfT8%2B7kSHuvQHl&X-Amz-Signature=35da682296a5c61bcfa9172ca7f63f9fcc28bb3870122bc17e6433bfc90198d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3ZWPEIA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq%2FwlOtrv1Q6zj7MDjuoyTZoY1XRUpYr9a53wp4kCMcQIgM16tNVF17f%2BQ8O2vOgQ45%2BF08I%2BfewXvZ490gKjXrzMqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYqr4xcNY8HCIuuLCrcAyzw2JyLX2lgdjlU2P2w0KLZJhrldKEowBr9KLLBF4%2BYMJUX4ADFwT6Afrq8JyWQufbcbx8hq4bYwj3FUyX%2FzNj90skyGwgcBx0kImQX6bwJa6BOMJeCGYyTYnErrBnWYDAjY94ije8mZMGJxx02eau5fO3U7njT2%2FWpnMJO299y8N3nrWoDPXzoUdcg%2FQrMaie%2BVcPXMWOepAXqoetCQFUB2VWsDVTGtam8SNLxFoh8MxkUngI7UQtkLReP56nu2aam5gExhdpicrBv3RsFf1eELJ%2FWpozHgOX7JII4VlrBYVpOQ9LSoet%2Bs1UUdt4smOXKwKBTgErKJqYixCBGs%2Bk2GrS3MVunYSq7fj5kCDpY0QGKU3jNM%2FXE7CoV3WyBLZtEXiBg7BHjMX0Bb45A%2FVcp0QkvWm8JSQHGzgVeS1Y1VhjnTmr%2FpqEy3gTj6tq0QbOCSuyWE7BeM4d4l%2B64tXS9YYf1oZf3cEu11CTYnfkXczrzRK6eTvmUFQIDH0lnHN0G3zU1LvnCFJ%2B3MoRPCIqmee2odhoDZ05j7MFY%2FFSKkzdPQA66WeUGuBGz4byk06kyimpFTKerezBEARGY6%2FU1XRmcDPR6ZWnseDocR8n0C9S6yv%2B9WrIAjo9RMIfr7LwGOqUBS8ne1NB7zg%2BZ%2F1z1pUhkCp3wz20CuuzaE8OntkiNHFlzwAcRCFXQS1gmU2K%2Fs08iaDa74GCoJ4RsstaBFVpqCj6Fs9RfG7x3OpWgdcZzta05tjLKsUpr39y5jJFclokgijcNYp67xXq1LD2w637xVu4WTYwG3AipDS4J%2F2YK8h55TrACGdXERTe5CYJ%2FcihqpYbrLGlzQowOEpUfT8%2B7kSHuvQHl&X-Amz-Signature=682f20ab02e8d5e8ac898c43f9e1ef1d9c5c8564b7eb2fdd3c8ff4d153917fb6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3ZWPEIA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq%2FwlOtrv1Q6zj7MDjuoyTZoY1XRUpYr9a53wp4kCMcQIgM16tNVF17f%2BQ8O2vOgQ45%2BF08I%2BfewXvZ490gKjXrzMqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYqr4xcNY8HCIuuLCrcAyzw2JyLX2lgdjlU2P2w0KLZJhrldKEowBr9KLLBF4%2BYMJUX4ADFwT6Afrq8JyWQufbcbx8hq4bYwj3FUyX%2FzNj90skyGwgcBx0kImQX6bwJa6BOMJeCGYyTYnErrBnWYDAjY94ije8mZMGJxx02eau5fO3U7njT2%2FWpnMJO299y8N3nrWoDPXzoUdcg%2FQrMaie%2BVcPXMWOepAXqoetCQFUB2VWsDVTGtam8SNLxFoh8MxkUngI7UQtkLReP56nu2aam5gExhdpicrBv3RsFf1eELJ%2FWpozHgOX7JII4VlrBYVpOQ9LSoet%2Bs1UUdt4smOXKwKBTgErKJqYixCBGs%2Bk2GrS3MVunYSq7fj5kCDpY0QGKU3jNM%2FXE7CoV3WyBLZtEXiBg7BHjMX0Bb45A%2FVcp0QkvWm8JSQHGzgVeS1Y1VhjnTmr%2FpqEy3gTj6tq0QbOCSuyWE7BeM4d4l%2B64tXS9YYf1oZf3cEu11CTYnfkXczrzRK6eTvmUFQIDH0lnHN0G3zU1LvnCFJ%2B3MoRPCIqmee2odhoDZ05j7MFY%2FFSKkzdPQA66WeUGuBGz4byk06kyimpFTKerezBEARGY6%2FU1XRmcDPR6ZWnseDocR8n0C9S6yv%2B9WrIAjo9RMIfr7LwGOqUBS8ne1NB7zg%2BZ%2F1z1pUhkCp3wz20CuuzaE8OntkiNHFlzwAcRCFXQS1gmU2K%2Fs08iaDa74GCoJ4RsstaBFVpqCj6Fs9RfG7x3OpWgdcZzta05tjLKsUpr39y5jJFclokgijcNYp67xXq1LD2w637xVu4WTYwG3AipDS4J%2F2YK8h55TrACGdXERTe5CYJ%2FcihqpYbrLGlzQowOEpUfT8%2B7kSHuvQHl&X-Amz-Signature=ee30709b4ff15a8f1d7929b47824a9633bd3fc5f036163b6141a4f851f05bcf3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3ZWPEIA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq%2FwlOtrv1Q6zj7MDjuoyTZoY1XRUpYr9a53wp4kCMcQIgM16tNVF17f%2BQ8O2vOgQ45%2BF08I%2BfewXvZ490gKjXrzMqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYqr4xcNY8HCIuuLCrcAyzw2JyLX2lgdjlU2P2w0KLZJhrldKEowBr9KLLBF4%2BYMJUX4ADFwT6Afrq8JyWQufbcbx8hq4bYwj3FUyX%2FzNj90skyGwgcBx0kImQX6bwJa6BOMJeCGYyTYnErrBnWYDAjY94ije8mZMGJxx02eau5fO3U7njT2%2FWpnMJO299y8N3nrWoDPXzoUdcg%2FQrMaie%2BVcPXMWOepAXqoetCQFUB2VWsDVTGtam8SNLxFoh8MxkUngI7UQtkLReP56nu2aam5gExhdpicrBv3RsFf1eELJ%2FWpozHgOX7JII4VlrBYVpOQ9LSoet%2Bs1UUdt4smOXKwKBTgErKJqYixCBGs%2Bk2GrS3MVunYSq7fj5kCDpY0QGKU3jNM%2FXE7CoV3WyBLZtEXiBg7BHjMX0Bb45A%2FVcp0QkvWm8JSQHGzgVeS1Y1VhjnTmr%2FpqEy3gTj6tq0QbOCSuyWE7BeM4d4l%2B64tXS9YYf1oZf3cEu11CTYnfkXczrzRK6eTvmUFQIDH0lnHN0G3zU1LvnCFJ%2B3MoRPCIqmee2odhoDZ05j7MFY%2FFSKkzdPQA66WeUGuBGz4byk06kyimpFTKerezBEARGY6%2FU1XRmcDPR6ZWnseDocR8n0C9S6yv%2B9WrIAjo9RMIfr7LwGOqUBS8ne1NB7zg%2BZ%2F1z1pUhkCp3wz20CuuzaE8OntkiNHFlzwAcRCFXQS1gmU2K%2Fs08iaDa74GCoJ4RsstaBFVpqCj6Fs9RfG7x3OpWgdcZzta05tjLKsUpr39y5jJFclokgijcNYp67xXq1LD2w637xVu4WTYwG3AipDS4J%2F2YK8h55TrACGdXERTe5CYJ%2FcihqpYbrLGlzQowOEpUfT8%2B7kSHuvQHl&X-Amz-Signature=a58874e2fdbb631a77181930bc5f7f0bab2b95c585895ccade99c7362095f716&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX6VQST%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOEmxWcbGho1uj884u%2Fs0S5ZMf7Ate50dwlDUQrnW9iAIgWZbwNFAlL2dVuawg%2BZqCOsFas80eW8AwntNolWm7%2BVgqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcL7WcqK3Ounq4dDSrcA4DcVvfCJBmFJfm4om%2BgJySckvjj934q5lgNVUl34UGKfnQ4E7V1HynJi3lN9uEpmUnxQY3CZzV1QlxgSJn8%2BAkMPRYJJsZQJKuHEIL0MlbyYnBg3YEXAHUoVlbbUKwZdSzgxQ6tnbJSPMc9289jQYgbBLxs3R63ufsQ8tahbtLYZpNqRv5zHTjNDcwntisb%2Fcmo9ZQ7Ur2AEPUgCqHFBslPiXzPbqa%2BGLoL1luU6qWH3hVe39mcLohv%2B5JMT2NfwqPo7NTuHeGGFjkHEEPZh5vnJq5E8ctniodIhE0n6Zz08ybt%2BKa99Ek%2BGF0zqWeHnYdsrFpRSU1fnKgt1C8Osw0oBAk5FHQkCqm6xaMEbFNtWoEDwU%2F3J3dRhQR6COmZQx3n%2BVazDkebpbihAbq4NFsgNfGvI8zjuQaY90MV1fKfnTZogFkr8k5aHM%2BLOtIeWdCeFfj1PY8UCHygK3W9FSId5%2Fk9%2FTc7DMCn0NzwW3IpdubZjpGNgVA8VqNqB9nx9TQCkVLFSHLFAtWvlr%2BaH0T7meggpn8fBlC0%2BqKr8TF7dHdk8K1ttuNTft5svZCfIxR53OPXcrh3bWLohJL88Cqb2LwBUxeUklFeZ5xqHpAyqmABeAzWdxTJwfE0MOjr7LwGOqUBgiSj6Mdo8o1sAx5tHto8JeDRhdrEP7p8%2BfTpj7lBMPhlZOb02sgGJMFJrykcK0ZbGBcvp0JEkaa3nKC%2BQw%2Fj7%2BfELlVUAzqAXKA%2BSHdxLv240HEjB1PoLM%2BWCCMG7uBDcX6Rll7qFageSBzY9slTJWtuimnM6lz62NM2B4t0gTEKslCRvWk1a2dDqSf%2BCoOc2MDQPSRUzlFYLPk3a8mTffFVVwnK&X-Amz-Signature=9e7b461ba46b5b9418e0d86861c54fb75df2e8f65fbc14eb987a59fe939170ed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX6VQST%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOEmxWcbGho1uj884u%2Fs0S5ZMf7Ate50dwlDUQrnW9iAIgWZbwNFAlL2dVuawg%2BZqCOsFas80eW8AwntNolWm7%2BVgqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcL7WcqK3Ounq4dDSrcA4DcVvfCJBmFJfm4om%2BgJySckvjj934q5lgNVUl34UGKfnQ4E7V1HynJi3lN9uEpmUnxQY3CZzV1QlxgSJn8%2BAkMPRYJJsZQJKuHEIL0MlbyYnBg3YEXAHUoVlbbUKwZdSzgxQ6tnbJSPMc9289jQYgbBLxs3R63ufsQ8tahbtLYZpNqRv5zHTjNDcwntisb%2Fcmo9ZQ7Ur2AEPUgCqHFBslPiXzPbqa%2BGLoL1luU6qWH3hVe39mcLohv%2B5JMT2NfwqPo7NTuHeGGFjkHEEPZh5vnJq5E8ctniodIhE0n6Zz08ybt%2BKa99Ek%2BGF0zqWeHnYdsrFpRSU1fnKgt1C8Osw0oBAk5FHQkCqm6xaMEbFNtWoEDwU%2F3J3dRhQR6COmZQx3n%2BVazDkebpbihAbq4NFsgNfGvI8zjuQaY90MV1fKfnTZogFkr8k5aHM%2BLOtIeWdCeFfj1PY8UCHygK3W9FSId5%2Fk9%2FTc7DMCn0NzwW3IpdubZjpGNgVA8VqNqB9nx9TQCkVLFSHLFAtWvlr%2BaH0T7meggpn8fBlC0%2BqKr8TF7dHdk8K1ttuNTft5svZCfIxR53OPXcrh3bWLohJL88Cqb2LwBUxeUklFeZ5xqHpAyqmABeAzWdxTJwfE0MOjr7LwGOqUBgiSj6Mdo8o1sAx5tHto8JeDRhdrEP7p8%2BfTpj7lBMPhlZOb02sgGJMFJrykcK0ZbGBcvp0JEkaa3nKC%2BQw%2Fj7%2BfELlVUAzqAXKA%2BSHdxLv240HEjB1PoLM%2BWCCMG7uBDcX6Rll7qFageSBzY9slTJWtuimnM6lz62NM2B4t0gTEKslCRvWk1a2dDqSf%2BCoOc2MDQPSRUzlFYLPk3a8mTffFVVwnK&X-Amz-Signature=aeb151514f4a54e963a408dfbdbfc7bea029372c03fa1848d6a34a50493d2035&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX6VQST%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOEmxWcbGho1uj884u%2Fs0S5ZMf7Ate50dwlDUQrnW9iAIgWZbwNFAlL2dVuawg%2BZqCOsFas80eW8AwntNolWm7%2BVgqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcL7WcqK3Ounq4dDSrcA4DcVvfCJBmFJfm4om%2BgJySckvjj934q5lgNVUl34UGKfnQ4E7V1HynJi3lN9uEpmUnxQY3CZzV1QlxgSJn8%2BAkMPRYJJsZQJKuHEIL0MlbyYnBg3YEXAHUoVlbbUKwZdSzgxQ6tnbJSPMc9289jQYgbBLxs3R63ufsQ8tahbtLYZpNqRv5zHTjNDcwntisb%2Fcmo9ZQ7Ur2AEPUgCqHFBslPiXzPbqa%2BGLoL1luU6qWH3hVe39mcLohv%2B5JMT2NfwqPo7NTuHeGGFjkHEEPZh5vnJq5E8ctniodIhE0n6Zz08ybt%2BKa99Ek%2BGF0zqWeHnYdsrFpRSU1fnKgt1C8Osw0oBAk5FHQkCqm6xaMEbFNtWoEDwU%2F3J3dRhQR6COmZQx3n%2BVazDkebpbihAbq4NFsgNfGvI8zjuQaY90MV1fKfnTZogFkr8k5aHM%2BLOtIeWdCeFfj1PY8UCHygK3W9FSId5%2Fk9%2FTc7DMCn0NzwW3IpdubZjpGNgVA8VqNqB9nx9TQCkVLFSHLFAtWvlr%2BaH0T7meggpn8fBlC0%2BqKr8TF7dHdk8K1ttuNTft5svZCfIxR53OPXcrh3bWLohJL88Cqb2LwBUxeUklFeZ5xqHpAyqmABeAzWdxTJwfE0MOjr7LwGOqUBgiSj6Mdo8o1sAx5tHto8JeDRhdrEP7p8%2BfTpj7lBMPhlZOb02sgGJMFJrykcK0ZbGBcvp0JEkaa3nKC%2BQw%2Fj7%2BfELlVUAzqAXKA%2BSHdxLv240HEjB1PoLM%2BWCCMG7uBDcX6Rll7qFageSBzY9slTJWtuimnM6lz62NM2B4t0gTEKslCRvWk1a2dDqSf%2BCoOc2MDQPSRUzlFYLPk3a8mTffFVVwnK&X-Amz-Signature=1aa58518616226acf9010309edac774a45b2b82ba7f7abd1560fa23e549dd07f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX6VQST%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOEmxWcbGho1uj884u%2Fs0S5ZMf7Ate50dwlDUQrnW9iAIgWZbwNFAlL2dVuawg%2BZqCOsFas80eW8AwntNolWm7%2BVgqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcL7WcqK3Ounq4dDSrcA4DcVvfCJBmFJfm4om%2BgJySckvjj934q5lgNVUl34UGKfnQ4E7V1HynJi3lN9uEpmUnxQY3CZzV1QlxgSJn8%2BAkMPRYJJsZQJKuHEIL0MlbyYnBg3YEXAHUoVlbbUKwZdSzgxQ6tnbJSPMc9289jQYgbBLxs3R63ufsQ8tahbtLYZpNqRv5zHTjNDcwntisb%2Fcmo9ZQ7Ur2AEPUgCqHFBslPiXzPbqa%2BGLoL1luU6qWH3hVe39mcLohv%2B5JMT2NfwqPo7NTuHeGGFjkHEEPZh5vnJq5E8ctniodIhE0n6Zz08ybt%2BKa99Ek%2BGF0zqWeHnYdsrFpRSU1fnKgt1C8Osw0oBAk5FHQkCqm6xaMEbFNtWoEDwU%2F3J3dRhQR6COmZQx3n%2BVazDkebpbihAbq4NFsgNfGvI8zjuQaY90MV1fKfnTZogFkr8k5aHM%2BLOtIeWdCeFfj1PY8UCHygK3W9FSId5%2Fk9%2FTc7DMCn0NzwW3IpdubZjpGNgVA8VqNqB9nx9TQCkVLFSHLFAtWvlr%2BaH0T7meggpn8fBlC0%2BqKr8TF7dHdk8K1ttuNTft5svZCfIxR53OPXcrh3bWLohJL88Cqb2LwBUxeUklFeZ5xqHpAyqmABeAzWdxTJwfE0MOjr7LwGOqUBgiSj6Mdo8o1sAx5tHto8JeDRhdrEP7p8%2BfTpj7lBMPhlZOb02sgGJMFJrykcK0ZbGBcvp0JEkaa3nKC%2BQw%2Fj7%2BfELlVUAzqAXKA%2BSHdxLv240HEjB1PoLM%2BWCCMG7uBDcX6Rll7qFageSBzY9slTJWtuimnM6lz62NM2B4t0gTEKslCRvWk1a2dDqSf%2BCoOc2MDQPSRUzlFYLPk3a8mTffFVVwnK&X-Amz-Signature=c5525d81d08f426d72c4857a6195da851ea3673576db586a726cf4f74febc16b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX6VQST%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOEmxWcbGho1uj884u%2Fs0S5ZMf7Ate50dwlDUQrnW9iAIgWZbwNFAlL2dVuawg%2BZqCOsFas80eW8AwntNolWm7%2BVgqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcL7WcqK3Ounq4dDSrcA4DcVvfCJBmFJfm4om%2BgJySckvjj934q5lgNVUl34UGKfnQ4E7V1HynJi3lN9uEpmUnxQY3CZzV1QlxgSJn8%2BAkMPRYJJsZQJKuHEIL0MlbyYnBg3YEXAHUoVlbbUKwZdSzgxQ6tnbJSPMc9289jQYgbBLxs3R63ufsQ8tahbtLYZpNqRv5zHTjNDcwntisb%2Fcmo9ZQ7Ur2AEPUgCqHFBslPiXzPbqa%2BGLoL1luU6qWH3hVe39mcLohv%2B5JMT2NfwqPo7NTuHeGGFjkHEEPZh5vnJq5E8ctniodIhE0n6Zz08ybt%2BKa99Ek%2BGF0zqWeHnYdsrFpRSU1fnKgt1C8Osw0oBAk5FHQkCqm6xaMEbFNtWoEDwU%2F3J3dRhQR6COmZQx3n%2BVazDkebpbihAbq4NFsgNfGvI8zjuQaY90MV1fKfnTZogFkr8k5aHM%2BLOtIeWdCeFfj1PY8UCHygK3W9FSId5%2Fk9%2FTc7DMCn0NzwW3IpdubZjpGNgVA8VqNqB9nx9TQCkVLFSHLFAtWvlr%2BaH0T7meggpn8fBlC0%2BqKr8TF7dHdk8K1ttuNTft5svZCfIxR53OPXcrh3bWLohJL88Cqb2LwBUxeUklFeZ5xqHpAyqmABeAzWdxTJwfE0MOjr7LwGOqUBgiSj6Mdo8o1sAx5tHto8JeDRhdrEP7p8%2BfTpj7lBMPhlZOb02sgGJMFJrykcK0ZbGBcvp0JEkaa3nKC%2BQw%2Fj7%2BfELlVUAzqAXKA%2BSHdxLv240HEjB1PoLM%2BWCCMG7uBDcX6Rll7qFageSBzY9slTJWtuimnM6lz62NM2B4t0gTEKslCRvWk1a2dDqSf%2BCoOc2MDQPSRUzlFYLPk3a8mTffFVVwnK&X-Amz-Signature=366fe61b170de8427ea2f561c09169fc019cc0fce0129587c112d25d712fbe56&X-Amz-SignedHeaders=host&x-id=GetObject)
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


