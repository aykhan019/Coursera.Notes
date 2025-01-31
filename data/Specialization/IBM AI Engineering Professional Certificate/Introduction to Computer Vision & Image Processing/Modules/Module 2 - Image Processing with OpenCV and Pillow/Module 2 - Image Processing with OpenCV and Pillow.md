

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H5GD5RJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHKGySmqPyZAyxWRywxAYRIk%2FvqChMbMizah0QZs9uRFAiB5yrahYc0FVmtzX57U4kkhXjshIuXqxb%2B2q112lVR%2BrCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYqbJqAierU3JS%2FlKtwDyg5sgQ45yZaiBZca06xMZYpaVE8riWqzopovxjLYeuRFWcy6cuOBNpl8BCMMgis0iocpcblOBNwmQ%2FojXldobox3fcahy%2BA1nYWpTXTh9BnGNRVeHDz9jmh%2FNsNIjWfJ0hREcgNEhNOTiInddxRuwRp5Av7%2Fc4y5emOa8tAqMyMcCpYRPeuQbjc942UzCMa%2F3qFouAkHDdHcJtvmi7WHLBtwYqijSuFi4F92GM3GEq9tw2i4JbL5F5gvvwixH%2BuaN8pTocYCH8gvrfc7Q4HcWM9AAvRq1ce%2FrBEyoValpBQ3oBdjHsZx%2FLpOi%2FBIv2KUcyuFrDsgZcaBuHtcfdDo47Gx52eEqgjHZtJxOEKoKrHeTCRgWupW3L1HtbKpMVUp77AH1R4xhukeKk69FYPhHKHPIPJZuMWU5kIq92J9rvM1jwygUelcvAfRnmJgLQzduY4%2Bad9OwNmQ0fpDBYAtpIG3Yt9PGyNl8grEHkqCVK%2BqUDxj2ZXWCMQqIuRDalUTs7fxt2V3TTV%2FxeR6bFpygsZh0dxNV9RhT2IL2quk%2BjV%2FTbImyG3bDtoq0Icuyyf6hxi8Kxq4c89rgPzOv5NdwWdHGNnpmEHk4oNFMTWzN6IYXhMoj3Yz3BUP3Cww6dbyvAY6pgEETcvQg7bpP9%2BccYElpKSMAp6y%2BRigH73sVzaTOV%2BadDg59duLUDnfxMrtteVuv0iyC0w2%2FAnnbrXjNuz97mYcNG%2FSTtMwEclTOdWBpeVBR27uOwgUBZV3WHwJYwz9kOcdIIgKYPmkE5pSu7VIL3vK%2BzlC4wZj3jtjV3ofpq0IqlleUfOdTWatBg5%2Fv88ymACrLuCJdFnvhSgkgL5h4EJ2%2FeYm0wx%2F&X-Amz-Signature=869ec293228a79adb1396436a68b9dbbb25865dc9d76441a810a9e394ab13e24&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USRDP5AH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxXwYxCH4lRjoTH03drOSey86IPXGgfXdRVcCRsRasvAiBZZ5c7niBgPvxP58779ZKd%2F5gj%2BH3T4%2BDEYLtsUhuQeCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSoygUOjMrnpt5tVsKtwDIXzQiBtFq1G84V3Q504XdWKTC8RtD4aB7JJYtVOyjx2%2FDiNLX1l%2BzqfX1xOWskL0KQuB1vWpfoVhkWFaQjx6nXye2RbpB77ufH5S1vTxzWto6I84Grgx1DtE6YIG9kTc24WFJF%2BXKj0FwuzOtzclbSMFjOQGS%2BBoAfltS3iAoVjSXedGVUBJ2XIVs9QLcymbO4b2sS5c5uLekwG98F88RB2uYTFb2GPZJF3OqMxn3R8nXbkDCMPOkVsRQuZUy94X2ii0iKVxj14AnRxAZkkt8RMaWZcqGWt3nvLZuqGXOppayYqaQd78XBjFWJALMUtegWl%2FhhCGUUQ%2B6wUZdLwfH7HQVmCf5Eg3CYCqOzdbghUkIUyvNutWieQLKOiwp6OLB0M7Mdt3H9wPzSY%2FwSlTx%2FbyPvj1wQjMgtxzzgO4x0iIysfPZo4Hy95eHQTsVnUwsQf4cdm80G0DUphdvw%2B4omuAvkWa3Frh7h0qBKSPGJwCzb8QL4iKZbzhD2UsRNuYfRQ8sLuW%2F7GRKBBZAzNdyYyInbJd%2FHkHPBwB%2FXCWyE%2BVnh%2BcMM0DG6nWPqQh3YscsTJCpWTOR%2FTc9hBSRxZ3ev12Q04a%2BnUo%2FJQ91hPHnYdJZIwORYH6jYN2mHIwt9byvAY6pgFWcTSVzVpLudSKYRV%2BtUWVgUjc2D7I3kBHuFHHEAtBtj1kt5aZ6HeAoFv%2FJh6Ta0liKNu5Gu5%2FiJvCE4pAg5il8x7UhTDPjUQ%2B4kCD0zhzzV9Y945nYzvgeYuqrbWeyQREsjkgBI7HFx5dckxsfD4Nts%2BwyUG9RR1cgPbgiIDI1CfoO%2Bq%2BPYkSiUOK0rQ96f%2BpLBIxA1ZjxMyCbUExAn5i1iCC%2B8RN&X-Amz-Signature=e6d0ccf249752b2f0082bd3f920ae044b3ea82d7d7977db4ff7ea782a06c08ba&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USRDP5AH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxXwYxCH4lRjoTH03drOSey86IPXGgfXdRVcCRsRasvAiBZZ5c7niBgPvxP58779ZKd%2F5gj%2BH3T4%2BDEYLtsUhuQeCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSoygUOjMrnpt5tVsKtwDIXzQiBtFq1G84V3Q504XdWKTC8RtD4aB7JJYtVOyjx2%2FDiNLX1l%2BzqfX1xOWskL0KQuB1vWpfoVhkWFaQjx6nXye2RbpB77ufH5S1vTxzWto6I84Grgx1DtE6YIG9kTc24WFJF%2BXKj0FwuzOtzclbSMFjOQGS%2BBoAfltS3iAoVjSXedGVUBJ2XIVs9QLcymbO4b2sS5c5uLekwG98F88RB2uYTFb2GPZJF3OqMxn3R8nXbkDCMPOkVsRQuZUy94X2ii0iKVxj14AnRxAZkkt8RMaWZcqGWt3nvLZuqGXOppayYqaQd78XBjFWJALMUtegWl%2FhhCGUUQ%2B6wUZdLwfH7HQVmCf5Eg3CYCqOzdbghUkIUyvNutWieQLKOiwp6OLB0M7Mdt3H9wPzSY%2FwSlTx%2FbyPvj1wQjMgtxzzgO4x0iIysfPZo4Hy95eHQTsVnUwsQf4cdm80G0DUphdvw%2B4omuAvkWa3Frh7h0qBKSPGJwCzb8QL4iKZbzhD2UsRNuYfRQ8sLuW%2F7GRKBBZAzNdyYyInbJd%2FHkHPBwB%2FXCWyE%2BVnh%2BcMM0DG6nWPqQh3YscsTJCpWTOR%2FTc9hBSRxZ3ev12Q04a%2BnUo%2FJQ91hPHnYdJZIwORYH6jYN2mHIwt9byvAY6pgFWcTSVzVpLudSKYRV%2BtUWVgUjc2D7I3kBHuFHHEAtBtj1kt5aZ6HeAoFv%2FJh6Ta0liKNu5Gu5%2FiJvCE4pAg5il8x7UhTDPjUQ%2B4kCD0zhzzV9Y945nYzvgeYuqrbWeyQREsjkgBI7HFx5dckxsfD4Nts%2BwyUG9RR1cgPbgiIDI1CfoO%2Bq%2BPYkSiUOK0rQ96f%2BpLBIxA1ZjxMyCbUExAn5i1iCC%2B8RN&X-Amz-Signature=b3e0c2d34a665119f7c054bee050b0f50b3fe211cb62293c097cdb9c6250c116&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USRDP5AH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxXwYxCH4lRjoTH03drOSey86IPXGgfXdRVcCRsRasvAiBZZ5c7niBgPvxP58779ZKd%2F5gj%2BH3T4%2BDEYLtsUhuQeCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSoygUOjMrnpt5tVsKtwDIXzQiBtFq1G84V3Q504XdWKTC8RtD4aB7JJYtVOyjx2%2FDiNLX1l%2BzqfX1xOWskL0KQuB1vWpfoVhkWFaQjx6nXye2RbpB77ufH5S1vTxzWto6I84Grgx1DtE6YIG9kTc24WFJF%2BXKj0FwuzOtzclbSMFjOQGS%2BBoAfltS3iAoVjSXedGVUBJ2XIVs9QLcymbO4b2sS5c5uLekwG98F88RB2uYTFb2GPZJF3OqMxn3R8nXbkDCMPOkVsRQuZUy94X2ii0iKVxj14AnRxAZkkt8RMaWZcqGWt3nvLZuqGXOppayYqaQd78XBjFWJALMUtegWl%2FhhCGUUQ%2B6wUZdLwfH7HQVmCf5Eg3CYCqOzdbghUkIUyvNutWieQLKOiwp6OLB0M7Mdt3H9wPzSY%2FwSlTx%2FbyPvj1wQjMgtxzzgO4x0iIysfPZo4Hy95eHQTsVnUwsQf4cdm80G0DUphdvw%2B4omuAvkWa3Frh7h0qBKSPGJwCzb8QL4iKZbzhD2UsRNuYfRQ8sLuW%2F7GRKBBZAzNdyYyInbJd%2FHkHPBwB%2FXCWyE%2BVnh%2BcMM0DG6nWPqQh3YscsTJCpWTOR%2FTc9hBSRxZ3ev12Q04a%2BnUo%2FJQ91hPHnYdJZIwORYH6jYN2mHIwt9byvAY6pgFWcTSVzVpLudSKYRV%2BtUWVgUjc2D7I3kBHuFHHEAtBtj1kt5aZ6HeAoFv%2FJh6Ta0liKNu5Gu5%2FiJvCE4pAg5il8x7UhTDPjUQ%2B4kCD0zhzzV9Y945nYzvgeYuqrbWeyQREsjkgBI7HFx5dckxsfD4Nts%2BwyUG9RR1cgPbgiIDI1CfoO%2Bq%2BPYkSiUOK0rQ96f%2BpLBIxA1ZjxMyCbUExAn5i1iCC%2B8RN&X-Amz-Signature=2fdeca3c55681e4c3d49f5197f83c4436812a6ab48855abab9212225b487de32&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USRDP5AH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxXwYxCH4lRjoTH03drOSey86IPXGgfXdRVcCRsRasvAiBZZ5c7niBgPvxP58779ZKd%2F5gj%2BH3T4%2BDEYLtsUhuQeCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSoygUOjMrnpt5tVsKtwDIXzQiBtFq1G84V3Q504XdWKTC8RtD4aB7JJYtVOyjx2%2FDiNLX1l%2BzqfX1xOWskL0KQuB1vWpfoVhkWFaQjx6nXye2RbpB77ufH5S1vTxzWto6I84Grgx1DtE6YIG9kTc24WFJF%2BXKj0FwuzOtzclbSMFjOQGS%2BBoAfltS3iAoVjSXedGVUBJ2XIVs9QLcymbO4b2sS5c5uLekwG98F88RB2uYTFb2GPZJF3OqMxn3R8nXbkDCMPOkVsRQuZUy94X2ii0iKVxj14AnRxAZkkt8RMaWZcqGWt3nvLZuqGXOppayYqaQd78XBjFWJALMUtegWl%2FhhCGUUQ%2B6wUZdLwfH7HQVmCf5Eg3CYCqOzdbghUkIUyvNutWieQLKOiwp6OLB0M7Mdt3H9wPzSY%2FwSlTx%2FbyPvj1wQjMgtxzzgO4x0iIysfPZo4Hy95eHQTsVnUwsQf4cdm80G0DUphdvw%2B4omuAvkWa3Frh7h0qBKSPGJwCzb8QL4iKZbzhD2UsRNuYfRQ8sLuW%2F7GRKBBZAzNdyYyInbJd%2FHkHPBwB%2FXCWyE%2BVnh%2BcMM0DG6nWPqQh3YscsTJCpWTOR%2FTc9hBSRxZ3ev12Q04a%2BnUo%2FJQ91hPHnYdJZIwORYH6jYN2mHIwt9byvAY6pgFWcTSVzVpLudSKYRV%2BtUWVgUjc2D7I3kBHuFHHEAtBtj1kt5aZ6HeAoFv%2FJh6Ta0liKNu5Gu5%2FiJvCE4pAg5il8x7UhTDPjUQ%2B4kCD0zhzzV9Y945nYzvgeYuqrbWeyQREsjkgBI7HFx5dckxsfD4Nts%2BwyUG9RR1cgPbgiIDI1CfoO%2Bq%2BPYkSiUOK0rQ96f%2BpLBIxA1ZjxMyCbUExAn5i1iCC%2B8RN&X-Amz-Signature=3e4b2b7936ad07fce89bfc9efe0df2a5bc2d8d67e83bc42119f4ededb73a84fc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USRDP5AH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxXwYxCH4lRjoTH03drOSey86IPXGgfXdRVcCRsRasvAiBZZ5c7niBgPvxP58779ZKd%2F5gj%2BH3T4%2BDEYLtsUhuQeCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSoygUOjMrnpt5tVsKtwDIXzQiBtFq1G84V3Q504XdWKTC8RtD4aB7JJYtVOyjx2%2FDiNLX1l%2BzqfX1xOWskL0KQuB1vWpfoVhkWFaQjx6nXye2RbpB77ufH5S1vTxzWto6I84Grgx1DtE6YIG9kTc24WFJF%2BXKj0FwuzOtzclbSMFjOQGS%2BBoAfltS3iAoVjSXedGVUBJ2XIVs9QLcymbO4b2sS5c5uLekwG98F88RB2uYTFb2GPZJF3OqMxn3R8nXbkDCMPOkVsRQuZUy94X2ii0iKVxj14AnRxAZkkt8RMaWZcqGWt3nvLZuqGXOppayYqaQd78XBjFWJALMUtegWl%2FhhCGUUQ%2B6wUZdLwfH7HQVmCf5Eg3CYCqOzdbghUkIUyvNutWieQLKOiwp6OLB0M7Mdt3H9wPzSY%2FwSlTx%2FbyPvj1wQjMgtxzzgO4x0iIysfPZo4Hy95eHQTsVnUwsQf4cdm80G0DUphdvw%2B4omuAvkWa3Frh7h0qBKSPGJwCzb8QL4iKZbzhD2UsRNuYfRQ8sLuW%2F7GRKBBZAzNdyYyInbJd%2FHkHPBwB%2FXCWyE%2BVnh%2BcMM0DG6nWPqQh3YscsTJCpWTOR%2FTc9hBSRxZ3ev12Q04a%2BnUo%2FJQ91hPHnYdJZIwORYH6jYN2mHIwt9byvAY6pgFWcTSVzVpLudSKYRV%2BtUWVgUjc2D7I3kBHuFHHEAtBtj1kt5aZ6HeAoFv%2FJh6Ta0liKNu5Gu5%2FiJvCE4pAg5il8x7UhTDPjUQ%2B4kCD0zhzzV9Y945nYzvgeYuqrbWeyQREsjkgBI7HFx5dckxsfD4Nts%2BwyUG9RR1cgPbgiIDI1CfoO%2Bq%2BPYkSiUOK0rQ96f%2BpLBIxA1ZjxMyCbUExAn5i1iCC%2B8RN&X-Amz-Signature=a9febc84525577b26f1d34688b16a6b2b38aae3b4063c9f38bef992df525f21b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H5GD5RJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHKGySmqPyZAyxWRywxAYRIk%2FvqChMbMizah0QZs9uRFAiB5yrahYc0FVmtzX57U4kkhXjshIuXqxb%2B2q112lVR%2BrCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYqbJqAierU3JS%2FlKtwDyg5sgQ45yZaiBZca06xMZYpaVE8riWqzopovxjLYeuRFWcy6cuOBNpl8BCMMgis0iocpcblOBNwmQ%2FojXldobox3fcahy%2BA1nYWpTXTh9BnGNRVeHDz9jmh%2FNsNIjWfJ0hREcgNEhNOTiInddxRuwRp5Av7%2Fc4y5emOa8tAqMyMcCpYRPeuQbjc942UzCMa%2F3qFouAkHDdHcJtvmi7WHLBtwYqijSuFi4F92GM3GEq9tw2i4JbL5F5gvvwixH%2BuaN8pTocYCH8gvrfc7Q4HcWM9AAvRq1ce%2FrBEyoValpBQ3oBdjHsZx%2FLpOi%2FBIv2KUcyuFrDsgZcaBuHtcfdDo47Gx52eEqgjHZtJxOEKoKrHeTCRgWupW3L1HtbKpMVUp77AH1R4xhukeKk69FYPhHKHPIPJZuMWU5kIq92J9rvM1jwygUelcvAfRnmJgLQzduY4%2Bad9OwNmQ0fpDBYAtpIG3Yt9PGyNl8grEHkqCVK%2BqUDxj2ZXWCMQqIuRDalUTs7fxt2V3TTV%2FxeR6bFpygsZh0dxNV9RhT2IL2quk%2BjV%2FTbImyG3bDtoq0Icuyyf6hxi8Kxq4c89rgPzOv5NdwWdHGNnpmEHk4oNFMTWzN6IYXhMoj3Yz3BUP3Cww6dbyvAY6pgEETcvQg7bpP9%2BccYElpKSMAp6y%2BRigH73sVzaTOV%2BadDg59duLUDnfxMrtteVuv0iyC0w2%2FAnnbrXjNuz97mYcNG%2FSTtMwEclTOdWBpeVBR27uOwgUBZV3WHwJYwz9kOcdIIgKYPmkE5pSu7VIL3vK%2BzlC4wZj3jtjV3ofpq0IqlleUfOdTWatBg5%2Fv88ymACrLuCJdFnvhSgkgL5h4EJ2%2FeYm0wx%2F&X-Amz-Signature=7196832e5e9876b0206516818251657cffdb675701ff619e27134726ebfd14ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H5GD5RJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHKGySmqPyZAyxWRywxAYRIk%2FvqChMbMizah0QZs9uRFAiB5yrahYc0FVmtzX57U4kkhXjshIuXqxb%2B2q112lVR%2BrCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYqbJqAierU3JS%2FlKtwDyg5sgQ45yZaiBZca06xMZYpaVE8riWqzopovxjLYeuRFWcy6cuOBNpl8BCMMgis0iocpcblOBNwmQ%2FojXldobox3fcahy%2BA1nYWpTXTh9BnGNRVeHDz9jmh%2FNsNIjWfJ0hREcgNEhNOTiInddxRuwRp5Av7%2Fc4y5emOa8tAqMyMcCpYRPeuQbjc942UzCMa%2F3qFouAkHDdHcJtvmi7WHLBtwYqijSuFi4F92GM3GEq9tw2i4JbL5F5gvvwixH%2BuaN8pTocYCH8gvrfc7Q4HcWM9AAvRq1ce%2FrBEyoValpBQ3oBdjHsZx%2FLpOi%2FBIv2KUcyuFrDsgZcaBuHtcfdDo47Gx52eEqgjHZtJxOEKoKrHeTCRgWupW3L1HtbKpMVUp77AH1R4xhukeKk69FYPhHKHPIPJZuMWU5kIq92J9rvM1jwygUelcvAfRnmJgLQzduY4%2Bad9OwNmQ0fpDBYAtpIG3Yt9PGyNl8grEHkqCVK%2BqUDxj2ZXWCMQqIuRDalUTs7fxt2V3TTV%2FxeR6bFpygsZh0dxNV9RhT2IL2quk%2BjV%2FTbImyG3bDtoq0Icuyyf6hxi8Kxq4c89rgPzOv5NdwWdHGNnpmEHk4oNFMTWzN6IYXhMoj3Yz3BUP3Cww6dbyvAY6pgEETcvQg7bpP9%2BccYElpKSMAp6y%2BRigH73sVzaTOV%2BadDg59duLUDnfxMrtteVuv0iyC0w2%2FAnnbrXjNuz97mYcNG%2FSTtMwEclTOdWBpeVBR27uOwgUBZV3WHwJYwz9kOcdIIgKYPmkE5pSu7VIL3vK%2BzlC4wZj3jtjV3ofpq0IqlleUfOdTWatBg5%2Fv88ymACrLuCJdFnvhSgkgL5h4EJ2%2FeYm0wx%2F&X-Amz-Signature=1429399eeb2398fedbfe06882d96669eeb3c3e0dc57d1788c24241fbaa835268&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H5GD5RJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHKGySmqPyZAyxWRywxAYRIk%2FvqChMbMizah0QZs9uRFAiB5yrahYc0FVmtzX57U4kkhXjshIuXqxb%2B2q112lVR%2BrCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYqbJqAierU3JS%2FlKtwDyg5sgQ45yZaiBZca06xMZYpaVE8riWqzopovxjLYeuRFWcy6cuOBNpl8BCMMgis0iocpcblOBNwmQ%2FojXldobox3fcahy%2BA1nYWpTXTh9BnGNRVeHDz9jmh%2FNsNIjWfJ0hREcgNEhNOTiInddxRuwRp5Av7%2Fc4y5emOa8tAqMyMcCpYRPeuQbjc942UzCMa%2F3qFouAkHDdHcJtvmi7WHLBtwYqijSuFi4F92GM3GEq9tw2i4JbL5F5gvvwixH%2BuaN8pTocYCH8gvrfc7Q4HcWM9AAvRq1ce%2FrBEyoValpBQ3oBdjHsZx%2FLpOi%2FBIv2KUcyuFrDsgZcaBuHtcfdDo47Gx52eEqgjHZtJxOEKoKrHeTCRgWupW3L1HtbKpMVUp77AH1R4xhukeKk69FYPhHKHPIPJZuMWU5kIq92J9rvM1jwygUelcvAfRnmJgLQzduY4%2Bad9OwNmQ0fpDBYAtpIG3Yt9PGyNl8grEHkqCVK%2BqUDxj2ZXWCMQqIuRDalUTs7fxt2V3TTV%2FxeR6bFpygsZh0dxNV9RhT2IL2quk%2BjV%2FTbImyG3bDtoq0Icuyyf6hxi8Kxq4c89rgPzOv5NdwWdHGNnpmEHk4oNFMTWzN6IYXhMoj3Yz3BUP3Cww6dbyvAY6pgEETcvQg7bpP9%2BccYElpKSMAp6y%2BRigH73sVzaTOV%2BadDg59duLUDnfxMrtteVuv0iyC0w2%2FAnnbrXjNuz97mYcNG%2FSTtMwEclTOdWBpeVBR27uOwgUBZV3WHwJYwz9kOcdIIgKYPmkE5pSu7VIL3vK%2BzlC4wZj3jtjV3ofpq0IqlleUfOdTWatBg5%2Fv88ymACrLuCJdFnvhSgkgL5h4EJ2%2FeYm0wx%2F&X-Amz-Signature=e5870fa61eedfe545a909b711e39c2cb068b72ec903ab1b7253f20f11928769d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H5GD5RJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHKGySmqPyZAyxWRywxAYRIk%2FvqChMbMizah0QZs9uRFAiB5yrahYc0FVmtzX57U4kkhXjshIuXqxb%2B2q112lVR%2BrCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYqbJqAierU3JS%2FlKtwDyg5sgQ45yZaiBZca06xMZYpaVE8riWqzopovxjLYeuRFWcy6cuOBNpl8BCMMgis0iocpcblOBNwmQ%2FojXldobox3fcahy%2BA1nYWpTXTh9BnGNRVeHDz9jmh%2FNsNIjWfJ0hREcgNEhNOTiInddxRuwRp5Av7%2Fc4y5emOa8tAqMyMcCpYRPeuQbjc942UzCMa%2F3qFouAkHDdHcJtvmi7WHLBtwYqijSuFi4F92GM3GEq9tw2i4JbL5F5gvvwixH%2BuaN8pTocYCH8gvrfc7Q4HcWM9AAvRq1ce%2FrBEyoValpBQ3oBdjHsZx%2FLpOi%2FBIv2KUcyuFrDsgZcaBuHtcfdDo47Gx52eEqgjHZtJxOEKoKrHeTCRgWupW3L1HtbKpMVUp77AH1R4xhukeKk69FYPhHKHPIPJZuMWU5kIq92J9rvM1jwygUelcvAfRnmJgLQzduY4%2Bad9OwNmQ0fpDBYAtpIG3Yt9PGyNl8grEHkqCVK%2BqUDxj2ZXWCMQqIuRDalUTs7fxt2V3TTV%2FxeR6bFpygsZh0dxNV9RhT2IL2quk%2BjV%2FTbImyG3bDtoq0Icuyyf6hxi8Kxq4c89rgPzOv5NdwWdHGNnpmEHk4oNFMTWzN6IYXhMoj3Yz3BUP3Cww6dbyvAY6pgEETcvQg7bpP9%2BccYElpKSMAp6y%2BRigH73sVzaTOV%2BadDg59duLUDnfxMrtteVuv0iyC0w2%2FAnnbrXjNuz97mYcNG%2FSTtMwEclTOdWBpeVBR27uOwgUBZV3WHwJYwz9kOcdIIgKYPmkE5pSu7VIL3vK%2BzlC4wZj3jtjV3ofpq0IqlleUfOdTWatBg5%2Fv88ymACrLuCJdFnvhSgkgL5h4EJ2%2FeYm0wx%2F&X-Amz-Signature=1ba0677335b3009b653ff523d2f2f502b41d3ffce8988f1a8dd5e276597195be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H5GD5RJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHKGySmqPyZAyxWRywxAYRIk%2FvqChMbMizah0QZs9uRFAiB5yrahYc0FVmtzX57U4kkhXjshIuXqxb%2B2q112lVR%2BrCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFYqbJqAierU3JS%2FlKtwDyg5sgQ45yZaiBZca06xMZYpaVE8riWqzopovxjLYeuRFWcy6cuOBNpl8BCMMgis0iocpcblOBNwmQ%2FojXldobox3fcahy%2BA1nYWpTXTh9BnGNRVeHDz9jmh%2FNsNIjWfJ0hREcgNEhNOTiInddxRuwRp5Av7%2Fc4y5emOa8tAqMyMcCpYRPeuQbjc942UzCMa%2F3qFouAkHDdHcJtvmi7WHLBtwYqijSuFi4F92GM3GEq9tw2i4JbL5F5gvvwixH%2BuaN8pTocYCH8gvrfc7Q4HcWM9AAvRq1ce%2FrBEyoValpBQ3oBdjHsZx%2FLpOi%2FBIv2KUcyuFrDsgZcaBuHtcfdDo47Gx52eEqgjHZtJxOEKoKrHeTCRgWupW3L1HtbKpMVUp77AH1R4xhukeKk69FYPhHKHPIPJZuMWU5kIq92J9rvM1jwygUelcvAfRnmJgLQzduY4%2Bad9OwNmQ0fpDBYAtpIG3Yt9PGyNl8grEHkqCVK%2BqUDxj2ZXWCMQqIuRDalUTs7fxt2V3TTV%2FxeR6bFpygsZh0dxNV9RhT2IL2quk%2BjV%2FTbImyG3bDtoq0Icuyyf6hxi8Kxq4c89rgPzOv5NdwWdHGNnpmEHk4oNFMTWzN6IYXhMoj3Yz3BUP3Cww6dbyvAY6pgEETcvQg7bpP9%2BccYElpKSMAp6y%2BRigH73sVzaTOV%2BadDg59duLUDnfxMrtteVuv0iyC0w2%2FAnnbrXjNuz97mYcNG%2FSTtMwEclTOdWBpeVBR27uOwgUBZV3WHwJYwz9kOcdIIgKYPmkE5pSu7VIL3vK%2BzlC4wZj3jtjV3ofpq0IqlleUfOdTWatBg5%2Fv88ymACrLuCJdFnvhSgkgL5h4EJ2%2FeYm0wx%2F&X-Amz-Signature=5d74b20b822fb1aad4284d5d6397814619d23aa2e6fdad3d74695ee8fd109c16&X-Amz-SignedHeaders=host&x-id=GetObject)
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


