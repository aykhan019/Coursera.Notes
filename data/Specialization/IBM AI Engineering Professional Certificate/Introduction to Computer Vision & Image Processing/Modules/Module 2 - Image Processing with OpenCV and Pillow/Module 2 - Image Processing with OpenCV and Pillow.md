

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWLJDBW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHbGaEXlicKUE6%2BLRDhBWC9DotP%2BXEVSHiVN0%2BCarzOAiEAumJtkzWaRL1j4z90hSd1PA9Pu09qJIqMoS0TCjba66QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaDCm0rkk1UQzwLFircA6lugLjRGjjRx3y5mz2u2hpDahIKot7gm9gpaq9m7V8tBVTL3%2FvZyMZsYrIwJVrCDSDc43ObEkWSqHhJO1lf9%2FU846oGdWNC1c0OywjuMkn%2F1KM7d16EZITD3WZHD1DcL01UCsRZUCJXzJRu2ehodKjJMEI%2BuzAx8ePrs75jog3AVR3cBDl205XpcXDMDsnAY5q0UdJcopHIx8JW%2B%2BTS3hcTNxWHUjXfshXLsHnKys7%2FahasLUGIuSq5U%2Bbf3PypoGI8QMxTPh4eDBfXLv%2Bq%2B1IM%2F1cl%2BcO6taPJ%2BgwB7%2F4G8jEgZY4sMFvGxYMehGmJfUWUffdVl6Q4cQ7PDBkTviz5tC6dv%2Fnw%2BfTeq4Dv1dhosvSaavUxrXZqYKtSfEibVYsbQDkeJrCESgKr7ybfWYff6%2F5br2BBih%2F0WdKUKTYVMnsi%2FX%2BSx4%2FTuH9bYA4gvj4%2FdOE5Cjh%2Fu8GRUQyt6n70naXJeBw5vC%2F28%2FNWSmujs8P4GrQw9icKRCz76Y%2BZ5fP%2FkLRR2XyyJk0PSBeBL6lJ68sGc75SyRT6n30e37Cv1fUk%2F%2BC4ej6TOo7oUEnsa2UBpYuFz9R1m0xedEStyH1fndXkFvJbieN8r1FxEG8tI54qHO%2Bof7zNLXIRMMbQ8LwGOqUBhQmQ5aH87bUrYWCO%2Bvpy%2FL6hxyOCzIqHjBgXDYqpgIll25bBq2vzu59v%2FBdZOVejMBXmIHrIesDkCs0ezehCay1dvGH7XxGSXZWfdVxIiZHozfrk96OYGXRjwjFunkwK%2FKq7AYLgBwh8Dx41FytZuxj4Yz9iqnkHRj64Sy5Z14YMPVF5Ycv2snztRPgiCYZC4sj0JfJb6J%2FDvxRi483OZZ0ifeCQ&X-Amz-Signature=ae6e29930595bafc6e99ee684898a9471dd6675bad2455405419b5752b0156ac&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMNJVZP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID2uDYYYA3Uy39AclbwNPNw1o4Eq92iQcbO8lgkojS5CAiEA0y7iL8VrZCdusqJMzMfaZSoJ%2BGJZjQl0TQb9EC4z%2FpsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQ6reLo9sxjgZH%2FaCrcA6Jp3JDrJbiZ5t2EfnM3xIJaSY%2FNNmqQMw%2FSogisnAaRFIQ5MdpFlWX64b%2F61oB7WdlShCfm%2BYYceGv0uoqSCm7C%2BDt%2BU9fCtpEi0d9ikrMMuJREq%2FPUA8rTBuSFsZsxHbeJtx8YrushW5exmhc4rLU40w4FwxKtnRhmDFG9swotGGDHAECGHddLwrQJXMrGSFoZUcI0Mq7RTG4sxlLT3s4yac2kMya%2F%2FN8Wb9SJ8%2BpOlQPjgVGrbGYhsOAOgWCOjLoHP8pM6U6D0Hv6s39K%2BmaqCwp2cEnmPOqnqxM4uRRer%2FHTsWdnLRhY6t8iHKvhUITJiohh0U9ioE7xF%2FeUGD4sgXb6BXDtEHfWdkS1YokMEnlmgaSCBLyP1hEvf%2BdW9eB4lfRvu1mOJrWDMb6yWAGnBodr%2Bi3beWnc%2FRex2P7a483tMZ88Af7fIxRPhhOVfEaxP8AO%2BXm4Pk8NDgY8OL7sx%2Fz0eueurX8u0tU6v6%2BebHYlswx6qtRJLLs57NOJ0SilmPuagbPCsJD6oON8L6q06z3ryvs%2BBC345ngjWA8FBjYHIyCdadAXOxm91T%2FgYwTR86iMYX7KKYlqQU2rLpzidw1mbakcINsS8T0%2FYxyfOMYIoQl61BkW%2BAMXMJLQ8LwGOqUBTnxbF0ePMj9hBmwF7669myL1L0JAyK7XpWtvl8mUGgkydRdQ6qbFm8kHHgeE%2FKyzrfpG8dNrhICDqnoTAZ47KqFLG9sW%2FxC7dA4SrTT4ZhXyQBCxuMuDPT5ciraBFpUpdBzihptFjHeDqzQYPdEJvOV%2F2Atovvi1HzfKsIcC8F4MjP5bRiTbRXDcZBgzMRikeXHiRLcNveqZbq7y7UvHCLUMoapt&X-Amz-Signature=ea5576b6271ed1142096f750e1284b3ac89f9e21f613d0e214bd3baca1ecd0d3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMNJVZP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID2uDYYYA3Uy39AclbwNPNw1o4Eq92iQcbO8lgkojS5CAiEA0y7iL8VrZCdusqJMzMfaZSoJ%2BGJZjQl0TQb9EC4z%2FpsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQ6reLo9sxjgZH%2FaCrcA6Jp3JDrJbiZ5t2EfnM3xIJaSY%2FNNmqQMw%2FSogisnAaRFIQ5MdpFlWX64b%2F61oB7WdlShCfm%2BYYceGv0uoqSCm7C%2BDt%2BU9fCtpEi0d9ikrMMuJREq%2FPUA8rTBuSFsZsxHbeJtx8YrushW5exmhc4rLU40w4FwxKtnRhmDFG9swotGGDHAECGHddLwrQJXMrGSFoZUcI0Mq7RTG4sxlLT3s4yac2kMya%2F%2FN8Wb9SJ8%2BpOlQPjgVGrbGYhsOAOgWCOjLoHP8pM6U6D0Hv6s39K%2BmaqCwp2cEnmPOqnqxM4uRRer%2FHTsWdnLRhY6t8iHKvhUITJiohh0U9ioE7xF%2FeUGD4sgXb6BXDtEHfWdkS1YokMEnlmgaSCBLyP1hEvf%2BdW9eB4lfRvu1mOJrWDMb6yWAGnBodr%2Bi3beWnc%2FRex2P7a483tMZ88Af7fIxRPhhOVfEaxP8AO%2BXm4Pk8NDgY8OL7sx%2Fz0eueurX8u0tU6v6%2BebHYlswx6qtRJLLs57NOJ0SilmPuagbPCsJD6oON8L6q06z3ryvs%2BBC345ngjWA8FBjYHIyCdadAXOxm91T%2FgYwTR86iMYX7KKYlqQU2rLpzidw1mbakcINsS8T0%2FYxyfOMYIoQl61BkW%2BAMXMJLQ8LwGOqUBTnxbF0ePMj9hBmwF7669myL1L0JAyK7XpWtvl8mUGgkydRdQ6qbFm8kHHgeE%2FKyzrfpG8dNrhICDqnoTAZ47KqFLG9sW%2FxC7dA4SrTT4ZhXyQBCxuMuDPT5ciraBFpUpdBzihptFjHeDqzQYPdEJvOV%2F2Atovvi1HzfKsIcC8F4MjP5bRiTbRXDcZBgzMRikeXHiRLcNveqZbq7y7UvHCLUMoapt&X-Amz-Signature=76a10bae712ea6f23b64e1370cb9f94dd8c636dd798f5380c26e20f4a7c301b1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMNJVZP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID2uDYYYA3Uy39AclbwNPNw1o4Eq92iQcbO8lgkojS5CAiEA0y7iL8VrZCdusqJMzMfaZSoJ%2BGJZjQl0TQb9EC4z%2FpsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQ6reLo9sxjgZH%2FaCrcA6Jp3JDrJbiZ5t2EfnM3xIJaSY%2FNNmqQMw%2FSogisnAaRFIQ5MdpFlWX64b%2F61oB7WdlShCfm%2BYYceGv0uoqSCm7C%2BDt%2BU9fCtpEi0d9ikrMMuJREq%2FPUA8rTBuSFsZsxHbeJtx8YrushW5exmhc4rLU40w4FwxKtnRhmDFG9swotGGDHAECGHddLwrQJXMrGSFoZUcI0Mq7RTG4sxlLT3s4yac2kMya%2F%2FN8Wb9SJ8%2BpOlQPjgVGrbGYhsOAOgWCOjLoHP8pM6U6D0Hv6s39K%2BmaqCwp2cEnmPOqnqxM4uRRer%2FHTsWdnLRhY6t8iHKvhUITJiohh0U9ioE7xF%2FeUGD4sgXb6BXDtEHfWdkS1YokMEnlmgaSCBLyP1hEvf%2BdW9eB4lfRvu1mOJrWDMb6yWAGnBodr%2Bi3beWnc%2FRex2P7a483tMZ88Af7fIxRPhhOVfEaxP8AO%2BXm4Pk8NDgY8OL7sx%2Fz0eueurX8u0tU6v6%2BebHYlswx6qtRJLLs57NOJ0SilmPuagbPCsJD6oON8L6q06z3ryvs%2BBC345ngjWA8FBjYHIyCdadAXOxm91T%2FgYwTR86iMYX7KKYlqQU2rLpzidw1mbakcINsS8T0%2FYxyfOMYIoQl61BkW%2BAMXMJLQ8LwGOqUBTnxbF0ePMj9hBmwF7669myL1L0JAyK7XpWtvl8mUGgkydRdQ6qbFm8kHHgeE%2FKyzrfpG8dNrhICDqnoTAZ47KqFLG9sW%2FxC7dA4SrTT4ZhXyQBCxuMuDPT5ciraBFpUpdBzihptFjHeDqzQYPdEJvOV%2F2Atovvi1HzfKsIcC8F4MjP5bRiTbRXDcZBgzMRikeXHiRLcNveqZbq7y7UvHCLUMoapt&X-Amz-Signature=26671cb1d853b8842dcfe4dd1392c6ab89e54f2a0b04a72c6ea1356eb34c4a73&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMNJVZP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID2uDYYYA3Uy39AclbwNPNw1o4Eq92iQcbO8lgkojS5CAiEA0y7iL8VrZCdusqJMzMfaZSoJ%2BGJZjQl0TQb9EC4z%2FpsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQ6reLo9sxjgZH%2FaCrcA6Jp3JDrJbiZ5t2EfnM3xIJaSY%2FNNmqQMw%2FSogisnAaRFIQ5MdpFlWX64b%2F61oB7WdlShCfm%2BYYceGv0uoqSCm7C%2BDt%2BU9fCtpEi0d9ikrMMuJREq%2FPUA8rTBuSFsZsxHbeJtx8YrushW5exmhc4rLU40w4FwxKtnRhmDFG9swotGGDHAECGHddLwrQJXMrGSFoZUcI0Mq7RTG4sxlLT3s4yac2kMya%2F%2FN8Wb9SJ8%2BpOlQPjgVGrbGYhsOAOgWCOjLoHP8pM6U6D0Hv6s39K%2BmaqCwp2cEnmPOqnqxM4uRRer%2FHTsWdnLRhY6t8iHKvhUITJiohh0U9ioE7xF%2FeUGD4sgXb6BXDtEHfWdkS1YokMEnlmgaSCBLyP1hEvf%2BdW9eB4lfRvu1mOJrWDMb6yWAGnBodr%2Bi3beWnc%2FRex2P7a483tMZ88Af7fIxRPhhOVfEaxP8AO%2BXm4Pk8NDgY8OL7sx%2Fz0eueurX8u0tU6v6%2BebHYlswx6qtRJLLs57NOJ0SilmPuagbPCsJD6oON8L6q06z3ryvs%2BBC345ngjWA8FBjYHIyCdadAXOxm91T%2FgYwTR86iMYX7KKYlqQU2rLpzidw1mbakcINsS8T0%2FYxyfOMYIoQl61BkW%2BAMXMJLQ8LwGOqUBTnxbF0ePMj9hBmwF7669myL1L0JAyK7XpWtvl8mUGgkydRdQ6qbFm8kHHgeE%2FKyzrfpG8dNrhICDqnoTAZ47KqFLG9sW%2FxC7dA4SrTT4ZhXyQBCxuMuDPT5ciraBFpUpdBzihptFjHeDqzQYPdEJvOV%2F2Atovvi1HzfKsIcC8F4MjP5bRiTbRXDcZBgzMRikeXHiRLcNveqZbq7y7UvHCLUMoapt&X-Amz-Signature=f263d2970d4d4e5ece536a8168bdaa807c7d5be370120b17474e828381f303f7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZMNJVZP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID2uDYYYA3Uy39AclbwNPNw1o4Eq92iQcbO8lgkojS5CAiEA0y7iL8VrZCdusqJMzMfaZSoJ%2BGJZjQl0TQb9EC4z%2FpsqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQ6reLo9sxjgZH%2FaCrcA6Jp3JDrJbiZ5t2EfnM3xIJaSY%2FNNmqQMw%2FSogisnAaRFIQ5MdpFlWX64b%2F61oB7WdlShCfm%2BYYceGv0uoqSCm7C%2BDt%2BU9fCtpEi0d9ikrMMuJREq%2FPUA8rTBuSFsZsxHbeJtx8YrushW5exmhc4rLU40w4FwxKtnRhmDFG9swotGGDHAECGHddLwrQJXMrGSFoZUcI0Mq7RTG4sxlLT3s4yac2kMya%2F%2FN8Wb9SJ8%2BpOlQPjgVGrbGYhsOAOgWCOjLoHP8pM6U6D0Hv6s39K%2BmaqCwp2cEnmPOqnqxM4uRRer%2FHTsWdnLRhY6t8iHKvhUITJiohh0U9ioE7xF%2FeUGD4sgXb6BXDtEHfWdkS1YokMEnlmgaSCBLyP1hEvf%2BdW9eB4lfRvu1mOJrWDMb6yWAGnBodr%2Bi3beWnc%2FRex2P7a483tMZ88Af7fIxRPhhOVfEaxP8AO%2BXm4Pk8NDgY8OL7sx%2Fz0eueurX8u0tU6v6%2BebHYlswx6qtRJLLs57NOJ0SilmPuagbPCsJD6oON8L6q06z3ryvs%2BBC345ngjWA8FBjYHIyCdadAXOxm91T%2FgYwTR86iMYX7KKYlqQU2rLpzidw1mbakcINsS8T0%2FYxyfOMYIoQl61BkW%2BAMXMJLQ8LwGOqUBTnxbF0ePMj9hBmwF7669myL1L0JAyK7XpWtvl8mUGgkydRdQ6qbFm8kHHgeE%2FKyzrfpG8dNrhICDqnoTAZ47KqFLG9sW%2FxC7dA4SrTT4ZhXyQBCxuMuDPT5ciraBFpUpdBzihptFjHeDqzQYPdEJvOV%2F2Atovvi1HzfKsIcC8F4MjP5bRiTbRXDcZBgzMRikeXHiRLcNveqZbq7y7UvHCLUMoapt&X-Amz-Signature=a68099757f140b0a4c1f14238015df9b63b2af87e90dbc92b550ead8fe2e07a7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWLJDBW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHbGaEXlicKUE6%2BLRDhBWC9DotP%2BXEVSHiVN0%2BCarzOAiEAumJtkzWaRL1j4z90hSd1PA9Pu09qJIqMoS0TCjba66QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaDCm0rkk1UQzwLFircA6lugLjRGjjRx3y5mz2u2hpDahIKot7gm9gpaq9m7V8tBVTL3%2FvZyMZsYrIwJVrCDSDc43ObEkWSqHhJO1lf9%2FU846oGdWNC1c0OywjuMkn%2F1KM7d16EZITD3WZHD1DcL01UCsRZUCJXzJRu2ehodKjJMEI%2BuzAx8ePrs75jog3AVR3cBDl205XpcXDMDsnAY5q0UdJcopHIx8JW%2B%2BTS3hcTNxWHUjXfshXLsHnKys7%2FahasLUGIuSq5U%2Bbf3PypoGI8QMxTPh4eDBfXLv%2Bq%2B1IM%2F1cl%2BcO6taPJ%2BgwB7%2F4G8jEgZY4sMFvGxYMehGmJfUWUffdVl6Q4cQ7PDBkTviz5tC6dv%2Fnw%2BfTeq4Dv1dhosvSaavUxrXZqYKtSfEibVYsbQDkeJrCESgKr7ybfWYff6%2F5br2BBih%2F0WdKUKTYVMnsi%2FX%2BSx4%2FTuH9bYA4gvj4%2FdOE5Cjh%2Fu8GRUQyt6n70naXJeBw5vC%2F28%2FNWSmujs8P4GrQw9icKRCz76Y%2BZ5fP%2FkLRR2XyyJk0PSBeBL6lJ68sGc75SyRT6n30e37Cv1fUk%2F%2BC4ej6TOo7oUEnsa2UBpYuFz9R1m0xedEStyH1fndXkFvJbieN8r1FxEG8tI54qHO%2Bof7zNLXIRMMbQ8LwGOqUBhQmQ5aH87bUrYWCO%2Bvpy%2FL6hxyOCzIqHjBgXDYqpgIll25bBq2vzu59v%2FBdZOVejMBXmIHrIesDkCs0ezehCay1dvGH7XxGSXZWfdVxIiZHozfrk96OYGXRjwjFunkwK%2FKq7AYLgBwh8Dx41FytZuxj4Yz9iqnkHRj64Sy5Z14YMPVF5Ycv2snztRPgiCYZC4sj0JfJb6J%2FDvxRi483OZZ0ifeCQ&X-Amz-Signature=1df4d2ae9d9587cbe016103e5171797d96c30b354692eaed55de313104b9c7b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWLJDBW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHbGaEXlicKUE6%2BLRDhBWC9DotP%2BXEVSHiVN0%2BCarzOAiEAumJtkzWaRL1j4z90hSd1PA9Pu09qJIqMoS0TCjba66QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaDCm0rkk1UQzwLFircA6lugLjRGjjRx3y5mz2u2hpDahIKot7gm9gpaq9m7V8tBVTL3%2FvZyMZsYrIwJVrCDSDc43ObEkWSqHhJO1lf9%2FU846oGdWNC1c0OywjuMkn%2F1KM7d16EZITD3WZHD1DcL01UCsRZUCJXzJRu2ehodKjJMEI%2BuzAx8ePrs75jog3AVR3cBDl205XpcXDMDsnAY5q0UdJcopHIx8JW%2B%2BTS3hcTNxWHUjXfshXLsHnKys7%2FahasLUGIuSq5U%2Bbf3PypoGI8QMxTPh4eDBfXLv%2Bq%2B1IM%2F1cl%2BcO6taPJ%2BgwB7%2F4G8jEgZY4sMFvGxYMehGmJfUWUffdVl6Q4cQ7PDBkTviz5tC6dv%2Fnw%2BfTeq4Dv1dhosvSaavUxrXZqYKtSfEibVYsbQDkeJrCESgKr7ybfWYff6%2F5br2BBih%2F0WdKUKTYVMnsi%2FX%2BSx4%2FTuH9bYA4gvj4%2FdOE5Cjh%2Fu8GRUQyt6n70naXJeBw5vC%2F28%2FNWSmujs8P4GrQw9icKRCz76Y%2BZ5fP%2FkLRR2XyyJk0PSBeBL6lJ68sGc75SyRT6n30e37Cv1fUk%2F%2BC4ej6TOo7oUEnsa2UBpYuFz9R1m0xedEStyH1fndXkFvJbieN8r1FxEG8tI54qHO%2Bof7zNLXIRMMbQ8LwGOqUBhQmQ5aH87bUrYWCO%2Bvpy%2FL6hxyOCzIqHjBgXDYqpgIll25bBq2vzu59v%2FBdZOVejMBXmIHrIesDkCs0ezehCay1dvGH7XxGSXZWfdVxIiZHozfrk96OYGXRjwjFunkwK%2FKq7AYLgBwh8Dx41FytZuxj4Yz9iqnkHRj64Sy5Z14YMPVF5Ycv2snztRPgiCYZC4sj0JfJb6J%2FDvxRi483OZZ0ifeCQ&X-Amz-Signature=70a907770f5816c94271d9dcc940312f418e6a66955edb2333396cb0312069d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWLJDBW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHbGaEXlicKUE6%2BLRDhBWC9DotP%2BXEVSHiVN0%2BCarzOAiEAumJtkzWaRL1j4z90hSd1PA9Pu09qJIqMoS0TCjba66QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaDCm0rkk1UQzwLFircA6lugLjRGjjRx3y5mz2u2hpDahIKot7gm9gpaq9m7V8tBVTL3%2FvZyMZsYrIwJVrCDSDc43ObEkWSqHhJO1lf9%2FU846oGdWNC1c0OywjuMkn%2F1KM7d16EZITD3WZHD1DcL01UCsRZUCJXzJRu2ehodKjJMEI%2BuzAx8ePrs75jog3AVR3cBDl205XpcXDMDsnAY5q0UdJcopHIx8JW%2B%2BTS3hcTNxWHUjXfshXLsHnKys7%2FahasLUGIuSq5U%2Bbf3PypoGI8QMxTPh4eDBfXLv%2Bq%2B1IM%2F1cl%2BcO6taPJ%2BgwB7%2F4G8jEgZY4sMFvGxYMehGmJfUWUffdVl6Q4cQ7PDBkTviz5tC6dv%2Fnw%2BfTeq4Dv1dhosvSaavUxrXZqYKtSfEibVYsbQDkeJrCESgKr7ybfWYff6%2F5br2BBih%2F0WdKUKTYVMnsi%2FX%2BSx4%2FTuH9bYA4gvj4%2FdOE5Cjh%2Fu8GRUQyt6n70naXJeBw5vC%2F28%2FNWSmujs8P4GrQw9icKRCz76Y%2BZ5fP%2FkLRR2XyyJk0PSBeBL6lJ68sGc75SyRT6n30e37Cv1fUk%2F%2BC4ej6TOo7oUEnsa2UBpYuFz9R1m0xedEStyH1fndXkFvJbieN8r1FxEG8tI54qHO%2Bof7zNLXIRMMbQ8LwGOqUBhQmQ5aH87bUrYWCO%2Bvpy%2FL6hxyOCzIqHjBgXDYqpgIll25bBq2vzu59v%2FBdZOVejMBXmIHrIesDkCs0ezehCay1dvGH7XxGSXZWfdVxIiZHozfrk96OYGXRjwjFunkwK%2FKq7AYLgBwh8Dx41FytZuxj4Yz9iqnkHRj64Sy5Z14YMPVF5Ycv2snztRPgiCYZC4sj0JfJb6J%2FDvxRi483OZZ0ifeCQ&X-Amz-Signature=763bddbb375d287996118e9968da370487bf3ee3b3bf26a68c48ec6210ea1e30&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWLJDBW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHbGaEXlicKUE6%2BLRDhBWC9DotP%2BXEVSHiVN0%2BCarzOAiEAumJtkzWaRL1j4z90hSd1PA9Pu09qJIqMoS0TCjba66QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaDCm0rkk1UQzwLFircA6lugLjRGjjRx3y5mz2u2hpDahIKot7gm9gpaq9m7V8tBVTL3%2FvZyMZsYrIwJVrCDSDc43ObEkWSqHhJO1lf9%2FU846oGdWNC1c0OywjuMkn%2F1KM7d16EZITD3WZHD1DcL01UCsRZUCJXzJRu2ehodKjJMEI%2BuzAx8ePrs75jog3AVR3cBDl205XpcXDMDsnAY5q0UdJcopHIx8JW%2B%2BTS3hcTNxWHUjXfshXLsHnKys7%2FahasLUGIuSq5U%2Bbf3PypoGI8QMxTPh4eDBfXLv%2Bq%2B1IM%2F1cl%2BcO6taPJ%2BgwB7%2F4G8jEgZY4sMFvGxYMehGmJfUWUffdVl6Q4cQ7PDBkTviz5tC6dv%2Fnw%2BfTeq4Dv1dhosvSaavUxrXZqYKtSfEibVYsbQDkeJrCESgKr7ybfWYff6%2F5br2BBih%2F0WdKUKTYVMnsi%2FX%2BSx4%2FTuH9bYA4gvj4%2FdOE5Cjh%2Fu8GRUQyt6n70naXJeBw5vC%2F28%2FNWSmujs8P4GrQw9icKRCz76Y%2BZ5fP%2FkLRR2XyyJk0PSBeBL6lJ68sGc75SyRT6n30e37Cv1fUk%2F%2BC4ej6TOo7oUEnsa2UBpYuFz9R1m0xedEStyH1fndXkFvJbieN8r1FxEG8tI54qHO%2Bof7zNLXIRMMbQ8LwGOqUBhQmQ5aH87bUrYWCO%2Bvpy%2FL6hxyOCzIqHjBgXDYqpgIll25bBq2vzu59v%2FBdZOVejMBXmIHrIesDkCs0ezehCay1dvGH7XxGSXZWfdVxIiZHozfrk96OYGXRjwjFunkwK%2FKq7AYLgBwh8Dx41FytZuxj4Yz9iqnkHRj64Sy5Z14YMPVF5Ycv2snztRPgiCYZC4sj0JfJb6J%2FDvxRi483OZZ0ifeCQ&X-Amz-Signature=d9db1a51b696f5a74bba61f2a4a953bd6975d714e7cc21d9104b26c73889869a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWLJDBW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDHbGaEXlicKUE6%2BLRDhBWC9DotP%2BXEVSHiVN0%2BCarzOAiEAumJtkzWaRL1j4z90hSd1PA9Pu09qJIqMoS0TCjba66QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaDCm0rkk1UQzwLFircA6lugLjRGjjRx3y5mz2u2hpDahIKot7gm9gpaq9m7V8tBVTL3%2FvZyMZsYrIwJVrCDSDc43ObEkWSqHhJO1lf9%2FU846oGdWNC1c0OywjuMkn%2F1KM7d16EZITD3WZHD1DcL01UCsRZUCJXzJRu2ehodKjJMEI%2BuzAx8ePrs75jog3AVR3cBDl205XpcXDMDsnAY5q0UdJcopHIx8JW%2B%2BTS3hcTNxWHUjXfshXLsHnKys7%2FahasLUGIuSq5U%2Bbf3PypoGI8QMxTPh4eDBfXLv%2Bq%2B1IM%2F1cl%2BcO6taPJ%2BgwB7%2F4G8jEgZY4sMFvGxYMehGmJfUWUffdVl6Q4cQ7PDBkTviz5tC6dv%2Fnw%2BfTeq4Dv1dhosvSaavUxrXZqYKtSfEibVYsbQDkeJrCESgKr7ybfWYff6%2F5br2BBih%2F0WdKUKTYVMnsi%2FX%2BSx4%2FTuH9bYA4gvj4%2FdOE5Cjh%2Fu8GRUQyt6n70naXJeBw5vC%2F28%2FNWSmujs8P4GrQw9icKRCz76Y%2BZ5fP%2FkLRR2XyyJk0PSBeBL6lJ68sGc75SyRT6n30e37Cv1fUk%2F%2BC4ej6TOo7oUEnsa2UBpYuFz9R1m0xedEStyH1fndXkFvJbieN8r1FxEG8tI54qHO%2Bof7zNLXIRMMbQ8LwGOqUBhQmQ5aH87bUrYWCO%2Bvpy%2FL6hxyOCzIqHjBgXDYqpgIll25bBq2vzu59v%2FBdZOVejMBXmIHrIesDkCs0ezehCay1dvGH7XxGSXZWfdVxIiZHozfrk96OYGXRjwjFunkwK%2FKq7AYLgBwh8Dx41FytZuxj4Yz9iqnkHRj64Sy5Z14YMPVF5Ycv2snztRPgiCYZC4sj0JfJb6J%2FDvxRi483OZZ0ifeCQ&X-Amz-Signature=7ee05671ea6c5265d79cd04cd0390cb6418011bd5711439054cd5d49ce4866a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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


