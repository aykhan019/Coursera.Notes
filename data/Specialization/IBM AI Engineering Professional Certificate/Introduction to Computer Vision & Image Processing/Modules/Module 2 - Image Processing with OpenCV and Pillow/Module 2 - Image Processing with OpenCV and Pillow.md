

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DS2NPNU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCOY3P50tGGSTJfZ6RPun6AJc1AsYQAYHbFHnjwUqGhggIgIQwHcNnOKRqDg1%2Fy3d%2BmBlQE9O2WbmJyZyMpG4qjNTkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDApp0MYNPdbMCOujFSrcA8b21NsjFBwYCuuvMmEywtb9GfBN5n3AWopMujLKvqyq963b6kucmZanTsyMUjgjZy1DEq0XvHybIUTWdLm5m0c0bVdD7aOyJVLUNaNwy8vd3WtwwbQ3O1DekT%2BrcUqxlrQiaBjOt9NgCIk2XQYEAx%2BHS06zFqHD5julc5fhmU0ObEyUxtDPYv3ofBJu2QyN62WeR9rtOpRRnOllDVLBqnCltlT4y%2Fy6MXYcp218qBSo33m%2BMdYnLiKf4jZMzVKvZGS07rWDAXDs34Y77IZDcGjuZdEfb2rb402Pat6KK73s4gTKtCye403rRC5D4c4vUCb3qq%2FDTK54biMZIQzBZxbNLn4gU%2FGkdS%2BiZoJ6zt76HmnZnELaC5VM0rxOuMH%2BrXs5JIv4lwSd6JnpRG6Ed4UGGrcvJMucRAPLeVGA9O7MpOw%2ByDkuRf5HklU%2FV5jBQXUq19Xbm46wpZ52PjPOfwVQ9artrFVqAW54LgDjJfHFf8m1STSKDFMjtIRIVIgATOwpdLKbEX26VA7kDSgta2PvLFOH7jIXdmGr33lc%2Bzci9sIB2%2BQzcrC3kO9EmDUBB48c4BdLGagvU8MZkCRFa%2FmBHrL%2Fytqt2zy5%2FyWVwg26HIuIZpPQIzS5g7%2FgMLO75rwGOqUB9OXZYXP5AgQa1l2aSHADmk08c4p%2BCzSDNrBid7PPUdHktRRZyj5T3aOZ%2FNjLZHwfaI9p77t87QKRglOkeVciUBbt3ry8chSo8mdrbV6Aw3tHVRRDASODc1s1%2Flm%2F0n%2FUoHJW7lBQMcuvvY%2Boqk5Ciw5cEa9LhXs1%2BjQzguwAss8U4YL6ickwm1oBKNP%2Ft88fBwqCdEH5tioQTIVlLrUHAaRyzL%2BY&X-Amz-Signature=182edbd9d8d2521ec29f37134095f62167dc034f93277cdd615314d9065ca020&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674AV2OIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDfNeFc6LF6V2TBj4XoV6Z0xfFgHYUZHDHOgxwALBKE8wIgeMNBC%2F5qMaG1qFJ4f6p3kiNoXnY0xln3iYLfPGStTLIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlk7aVkJLYYlxARwyrcA51Bg5LwMa2YtTgyy0BaSmwmbn4PJ%2FYFpRIfoYT0YqDDHo%2FJ79Q1CELKWcuITJeiCifcjL24Xiop%2FnWneVLurqP%2BABPHyvXJ0Ldl6raV4HTLYmhEX6UCc6qP5ftS%2FUV%2Fdu%2FHduqQzXdgsr3s%2BY43iPT1eVg3MIaZBZ5taxvxRd2kblFYpgVfYtfjeTpd1aSvkKk6%2B%2BG%2BQY8KrYKoxonchx95ofoAv%2B2mPSBnGlY9BcxZwy0CSq1Uo22AMeASZr0hJNc8f7GepUEtd0OqoiBNQhVVg4o%2FcrYP%2BMX5UBvKK%2BHFZ7OdU%2Bc7bczWAL5F%2BY211q8eCPTsai%2BsPcFxFZOirP24ben47UVPljC4z%2FYWw9pFw9X4kEbjD6SCCM%2BWzJxvuMDzIOIM1SD0ut%2BPzjNSaev89YNEO3pavDDKl3Z2d0Or07fzvt1SyaGUYsZbuj24u6WHj0fJw5JT8wY%2FmN8NKRIi%2B2rIVc6sIpb6eRxE00%2BrTK122B%2FJ929GcQI%2B0qGskfGtdGykD1LH88RC48q6kP6Hb6lp9uhSw3%2Bp4fFnB6pO1YHBUz8UlutYCkwoI7PDrzONQvfNiEhxVxA5w6kn6X60Si74aySwQ%2FZyQmLsjX2VYhf1Ixnigq0v5K2TMO%2B65rwGOqUBNILbiaNymwrGsdhWx79tz3ibfptRKIJ9MeEmNs6Jsv3Brwr0R%2FDoG7bIgWp4Vy%2Fep8MPU8220Zn4iT82tBfbYYvaVrdLQe8deV4it4ZG0sXVuYQgtgZ98LAwcespKSxR%2FgjR0ev16swR81pnF80tSr2lZ6FZruBKkRcMPhysOzb1EyTYg8ePa7rK2I70GGto%2B08G2RgUOTv7vuuUE1GndP9HAfXW&X-Amz-Signature=47340598779f9dcfa272d0628fa1703d5783279bbbdc1bdd62fb156e04ed0f18&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674AV2OIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDfNeFc6LF6V2TBj4XoV6Z0xfFgHYUZHDHOgxwALBKE8wIgeMNBC%2F5qMaG1qFJ4f6p3kiNoXnY0xln3iYLfPGStTLIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlk7aVkJLYYlxARwyrcA51Bg5LwMa2YtTgyy0BaSmwmbn4PJ%2FYFpRIfoYT0YqDDHo%2FJ79Q1CELKWcuITJeiCifcjL24Xiop%2FnWneVLurqP%2BABPHyvXJ0Ldl6raV4HTLYmhEX6UCc6qP5ftS%2FUV%2Fdu%2FHduqQzXdgsr3s%2BY43iPT1eVg3MIaZBZ5taxvxRd2kblFYpgVfYtfjeTpd1aSvkKk6%2B%2BG%2BQY8KrYKoxonchx95ofoAv%2B2mPSBnGlY9BcxZwy0CSq1Uo22AMeASZr0hJNc8f7GepUEtd0OqoiBNQhVVg4o%2FcrYP%2BMX5UBvKK%2BHFZ7OdU%2Bc7bczWAL5F%2BY211q8eCPTsai%2BsPcFxFZOirP24ben47UVPljC4z%2FYWw9pFw9X4kEbjD6SCCM%2BWzJxvuMDzIOIM1SD0ut%2BPzjNSaev89YNEO3pavDDKl3Z2d0Or07fzvt1SyaGUYsZbuj24u6WHj0fJw5JT8wY%2FmN8NKRIi%2B2rIVc6sIpb6eRxE00%2BrTK122B%2FJ929GcQI%2B0qGskfGtdGykD1LH88RC48q6kP6Hb6lp9uhSw3%2Bp4fFnB6pO1YHBUz8UlutYCkwoI7PDrzONQvfNiEhxVxA5w6kn6X60Si74aySwQ%2FZyQmLsjX2VYhf1Ixnigq0v5K2TMO%2B65rwGOqUBNILbiaNymwrGsdhWx79tz3ibfptRKIJ9MeEmNs6Jsv3Brwr0R%2FDoG7bIgWp4Vy%2Fep8MPU8220Zn4iT82tBfbYYvaVrdLQe8deV4it4ZG0sXVuYQgtgZ98LAwcespKSxR%2FgjR0ev16swR81pnF80tSr2lZ6FZruBKkRcMPhysOzb1EyTYg8ePa7rK2I70GGto%2B08G2RgUOTv7vuuUE1GndP9HAfXW&X-Amz-Signature=b8318c6f28a655997038f2fb124bf7a919a06a9ee22e5abf4d3f4bc4fd3248d4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674AV2OIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDfNeFc6LF6V2TBj4XoV6Z0xfFgHYUZHDHOgxwALBKE8wIgeMNBC%2F5qMaG1qFJ4f6p3kiNoXnY0xln3iYLfPGStTLIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlk7aVkJLYYlxARwyrcA51Bg5LwMa2YtTgyy0BaSmwmbn4PJ%2FYFpRIfoYT0YqDDHo%2FJ79Q1CELKWcuITJeiCifcjL24Xiop%2FnWneVLurqP%2BABPHyvXJ0Ldl6raV4HTLYmhEX6UCc6qP5ftS%2FUV%2Fdu%2FHduqQzXdgsr3s%2BY43iPT1eVg3MIaZBZ5taxvxRd2kblFYpgVfYtfjeTpd1aSvkKk6%2B%2BG%2BQY8KrYKoxonchx95ofoAv%2B2mPSBnGlY9BcxZwy0CSq1Uo22AMeASZr0hJNc8f7GepUEtd0OqoiBNQhVVg4o%2FcrYP%2BMX5UBvKK%2BHFZ7OdU%2Bc7bczWAL5F%2BY211q8eCPTsai%2BsPcFxFZOirP24ben47UVPljC4z%2FYWw9pFw9X4kEbjD6SCCM%2BWzJxvuMDzIOIM1SD0ut%2BPzjNSaev89YNEO3pavDDKl3Z2d0Or07fzvt1SyaGUYsZbuj24u6WHj0fJw5JT8wY%2FmN8NKRIi%2B2rIVc6sIpb6eRxE00%2BrTK122B%2FJ929GcQI%2B0qGskfGtdGykD1LH88RC48q6kP6Hb6lp9uhSw3%2Bp4fFnB6pO1YHBUz8UlutYCkwoI7PDrzONQvfNiEhxVxA5w6kn6X60Si74aySwQ%2FZyQmLsjX2VYhf1Ixnigq0v5K2TMO%2B65rwGOqUBNILbiaNymwrGsdhWx79tz3ibfptRKIJ9MeEmNs6Jsv3Brwr0R%2FDoG7bIgWp4Vy%2Fep8MPU8220Zn4iT82tBfbYYvaVrdLQe8deV4it4ZG0sXVuYQgtgZ98LAwcespKSxR%2FgjR0ev16swR81pnF80tSr2lZ6FZruBKkRcMPhysOzb1EyTYg8ePa7rK2I70GGto%2B08G2RgUOTv7vuuUE1GndP9HAfXW&X-Amz-Signature=67cb5efd3f469e0b0b78d0b5bf2a7502fdbab6c238eeee8dca58e2a3c270180f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674AV2OIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDfNeFc6LF6V2TBj4XoV6Z0xfFgHYUZHDHOgxwALBKE8wIgeMNBC%2F5qMaG1qFJ4f6p3kiNoXnY0xln3iYLfPGStTLIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlk7aVkJLYYlxARwyrcA51Bg5LwMa2YtTgyy0BaSmwmbn4PJ%2FYFpRIfoYT0YqDDHo%2FJ79Q1CELKWcuITJeiCifcjL24Xiop%2FnWneVLurqP%2BABPHyvXJ0Ldl6raV4HTLYmhEX6UCc6qP5ftS%2FUV%2Fdu%2FHduqQzXdgsr3s%2BY43iPT1eVg3MIaZBZ5taxvxRd2kblFYpgVfYtfjeTpd1aSvkKk6%2B%2BG%2BQY8KrYKoxonchx95ofoAv%2B2mPSBnGlY9BcxZwy0CSq1Uo22AMeASZr0hJNc8f7GepUEtd0OqoiBNQhVVg4o%2FcrYP%2BMX5UBvKK%2BHFZ7OdU%2Bc7bczWAL5F%2BY211q8eCPTsai%2BsPcFxFZOirP24ben47UVPljC4z%2FYWw9pFw9X4kEbjD6SCCM%2BWzJxvuMDzIOIM1SD0ut%2BPzjNSaev89YNEO3pavDDKl3Z2d0Or07fzvt1SyaGUYsZbuj24u6WHj0fJw5JT8wY%2FmN8NKRIi%2B2rIVc6sIpb6eRxE00%2BrTK122B%2FJ929GcQI%2B0qGskfGtdGykD1LH88RC48q6kP6Hb6lp9uhSw3%2Bp4fFnB6pO1YHBUz8UlutYCkwoI7PDrzONQvfNiEhxVxA5w6kn6X60Si74aySwQ%2FZyQmLsjX2VYhf1Ixnigq0v5K2TMO%2B65rwGOqUBNILbiaNymwrGsdhWx79tz3ibfptRKIJ9MeEmNs6Jsv3Brwr0R%2FDoG7bIgWp4Vy%2Fep8MPU8220Zn4iT82tBfbYYvaVrdLQe8deV4it4ZG0sXVuYQgtgZ98LAwcespKSxR%2FgjR0ev16swR81pnF80tSr2lZ6FZruBKkRcMPhysOzb1EyTYg8ePa7rK2I70GGto%2B08G2RgUOTv7vuuUE1GndP9HAfXW&X-Amz-Signature=83ae34e97d0aee2972773940f2bfeb561322f2adb206d156ecf81eee9e7b7a69&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674AV2OIY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDfNeFc6LF6V2TBj4XoV6Z0xfFgHYUZHDHOgxwALBKE8wIgeMNBC%2F5qMaG1qFJ4f6p3kiNoXnY0xln3iYLfPGStTLIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlk7aVkJLYYlxARwyrcA51Bg5LwMa2YtTgyy0BaSmwmbn4PJ%2FYFpRIfoYT0YqDDHo%2FJ79Q1CELKWcuITJeiCifcjL24Xiop%2FnWneVLurqP%2BABPHyvXJ0Ldl6raV4HTLYmhEX6UCc6qP5ftS%2FUV%2Fdu%2FHduqQzXdgsr3s%2BY43iPT1eVg3MIaZBZ5taxvxRd2kblFYpgVfYtfjeTpd1aSvkKk6%2B%2BG%2BQY8KrYKoxonchx95ofoAv%2B2mPSBnGlY9BcxZwy0CSq1Uo22AMeASZr0hJNc8f7GepUEtd0OqoiBNQhVVg4o%2FcrYP%2BMX5UBvKK%2BHFZ7OdU%2Bc7bczWAL5F%2BY211q8eCPTsai%2BsPcFxFZOirP24ben47UVPljC4z%2FYWw9pFw9X4kEbjD6SCCM%2BWzJxvuMDzIOIM1SD0ut%2BPzjNSaev89YNEO3pavDDKl3Z2d0Or07fzvt1SyaGUYsZbuj24u6WHj0fJw5JT8wY%2FmN8NKRIi%2B2rIVc6sIpb6eRxE00%2BrTK122B%2FJ929GcQI%2B0qGskfGtdGykD1LH88RC48q6kP6Hb6lp9uhSw3%2Bp4fFnB6pO1YHBUz8UlutYCkwoI7PDrzONQvfNiEhxVxA5w6kn6X60Si74aySwQ%2FZyQmLsjX2VYhf1Ixnigq0v5K2TMO%2B65rwGOqUBNILbiaNymwrGsdhWx79tz3ibfptRKIJ9MeEmNs6Jsv3Brwr0R%2FDoG7bIgWp4Vy%2Fep8MPU8220Zn4iT82tBfbYYvaVrdLQe8deV4it4ZG0sXVuYQgtgZ98LAwcespKSxR%2FgjR0ev16swR81pnF80tSr2lZ6FZruBKkRcMPhysOzb1EyTYg8ePa7rK2I70GGto%2B08G2RgUOTv7vuuUE1GndP9HAfXW&X-Amz-Signature=06db038aa36371bbcae4f8f9a70482b9b8a4d2c1ec53745fcde86f931c011644&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DS2NPNU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCOY3P50tGGSTJfZ6RPun6AJc1AsYQAYHbFHnjwUqGhggIgIQwHcNnOKRqDg1%2Fy3d%2BmBlQE9O2WbmJyZyMpG4qjNTkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDApp0MYNPdbMCOujFSrcA8b21NsjFBwYCuuvMmEywtb9GfBN5n3AWopMujLKvqyq963b6kucmZanTsyMUjgjZy1DEq0XvHybIUTWdLm5m0c0bVdD7aOyJVLUNaNwy8vd3WtwwbQ3O1DekT%2BrcUqxlrQiaBjOt9NgCIk2XQYEAx%2BHS06zFqHD5julc5fhmU0ObEyUxtDPYv3ofBJu2QyN62WeR9rtOpRRnOllDVLBqnCltlT4y%2Fy6MXYcp218qBSo33m%2BMdYnLiKf4jZMzVKvZGS07rWDAXDs34Y77IZDcGjuZdEfb2rb402Pat6KK73s4gTKtCye403rRC5D4c4vUCb3qq%2FDTK54biMZIQzBZxbNLn4gU%2FGkdS%2BiZoJ6zt76HmnZnELaC5VM0rxOuMH%2BrXs5JIv4lwSd6JnpRG6Ed4UGGrcvJMucRAPLeVGA9O7MpOw%2ByDkuRf5HklU%2FV5jBQXUq19Xbm46wpZ52PjPOfwVQ9artrFVqAW54LgDjJfHFf8m1STSKDFMjtIRIVIgATOwpdLKbEX26VA7kDSgta2PvLFOH7jIXdmGr33lc%2Bzci9sIB2%2BQzcrC3kO9EmDUBB48c4BdLGagvU8MZkCRFa%2FmBHrL%2Fytqt2zy5%2FyWVwg26HIuIZpPQIzS5g7%2FgMLO75rwGOqUB9OXZYXP5AgQa1l2aSHADmk08c4p%2BCzSDNrBid7PPUdHktRRZyj5T3aOZ%2FNjLZHwfaI9p77t87QKRglOkeVciUBbt3ry8chSo8mdrbV6Aw3tHVRRDASODc1s1%2Flm%2F0n%2FUoHJW7lBQMcuvvY%2Boqk5Ciw5cEa9LhXs1%2BjQzguwAss8U4YL6ickwm1oBKNP%2Ft88fBwqCdEH5tioQTIVlLrUHAaRyzL%2BY&X-Amz-Signature=a5f551bf8e7d9b07b2c58aca17a2d9bc56ab689650d89d593f43ab7d42036db1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DS2NPNU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCOY3P50tGGSTJfZ6RPun6AJc1AsYQAYHbFHnjwUqGhggIgIQwHcNnOKRqDg1%2Fy3d%2BmBlQE9O2WbmJyZyMpG4qjNTkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDApp0MYNPdbMCOujFSrcA8b21NsjFBwYCuuvMmEywtb9GfBN5n3AWopMujLKvqyq963b6kucmZanTsyMUjgjZy1DEq0XvHybIUTWdLm5m0c0bVdD7aOyJVLUNaNwy8vd3WtwwbQ3O1DekT%2BrcUqxlrQiaBjOt9NgCIk2XQYEAx%2BHS06zFqHD5julc5fhmU0ObEyUxtDPYv3ofBJu2QyN62WeR9rtOpRRnOllDVLBqnCltlT4y%2Fy6MXYcp218qBSo33m%2BMdYnLiKf4jZMzVKvZGS07rWDAXDs34Y77IZDcGjuZdEfb2rb402Pat6KK73s4gTKtCye403rRC5D4c4vUCb3qq%2FDTK54biMZIQzBZxbNLn4gU%2FGkdS%2BiZoJ6zt76HmnZnELaC5VM0rxOuMH%2BrXs5JIv4lwSd6JnpRG6Ed4UGGrcvJMucRAPLeVGA9O7MpOw%2ByDkuRf5HklU%2FV5jBQXUq19Xbm46wpZ52PjPOfwVQ9artrFVqAW54LgDjJfHFf8m1STSKDFMjtIRIVIgATOwpdLKbEX26VA7kDSgta2PvLFOH7jIXdmGr33lc%2Bzci9sIB2%2BQzcrC3kO9EmDUBB48c4BdLGagvU8MZkCRFa%2FmBHrL%2Fytqt2zy5%2FyWVwg26HIuIZpPQIzS5g7%2FgMLO75rwGOqUB9OXZYXP5AgQa1l2aSHADmk08c4p%2BCzSDNrBid7PPUdHktRRZyj5T3aOZ%2FNjLZHwfaI9p77t87QKRglOkeVciUBbt3ry8chSo8mdrbV6Aw3tHVRRDASODc1s1%2Flm%2F0n%2FUoHJW7lBQMcuvvY%2Boqk5Ciw5cEa9LhXs1%2BjQzguwAss8U4YL6ickwm1oBKNP%2Ft88fBwqCdEH5tioQTIVlLrUHAaRyzL%2BY&X-Amz-Signature=4534f30c0c55a1f32ba844dfa2221be9b6fdfe1ac71dd78035c3f824701eab14&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DS2NPNU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCOY3P50tGGSTJfZ6RPun6AJc1AsYQAYHbFHnjwUqGhggIgIQwHcNnOKRqDg1%2Fy3d%2BmBlQE9O2WbmJyZyMpG4qjNTkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDApp0MYNPdbMCOujFSrcA8b21NsjFBwYCuuvMmEywtb9GfBN5n3AWopMujLKvqyq963b6kucmZanTsyMUjgjZy1DEq0XvHybIUTWdLm5m0c0bVdD7aOyJVLUNaNwy8vd3WtwwbQ3O1DekT%2BrcUqxlrQiaBjOt9NgCIk2XQYEAx%2BHS06zFqHD5julc5fhmU0ObEyUxtDPYv3ofBJu2QyN62WeR9rtOpRRnOllDVLBqnCltlT4y%2Fy6MXYcp218qBSo33m%2BMdYnLiKf4jZMzVKvZGS07rWDAXDs34Y77IZDcGjuZdEfb2rb402Pat6KK73s4gTKtCye403rRC5D4c4vUCb3qq%2FDTK54biMZIQzBZxbNLn4gU%2FGkdS%2BiZoJ6zt76HmnZnELaC5VM0rxOuMH%2BrXs5JIv4lwSd6JnpRG6Ed4UGGrcvJMucRAPLeVGA9O7MpOw%2ByDkuRf5HklU%2FV5jBQXUq19Xbm46wpZ52PjPOfwVQ9artrFVqAW54LgDjJfHFf8m1STSKDFMjtIRIVIgATOwpdLKbEX26VA7kDSgta2PvLFOH7jIXdmGr33lc%2Bzci9sIB2%2BQzcrC3kO9EmDUBB48c4BdLGagvU8MZkCRFa%2FmBHrL%2Fytqt2zy5%2FyWVwg26HIuIZpPQIzS5g7%2FgMLO75rwGOqUB9OXZYXP5AgQa1l2aSHADmk08c4p%2BCzSDNrBid7PPUdHktRRZyj5T3aOZ%2FNjLZHwfaI9p77t87QKRglOkeVciUBbt3ry8chSo8mdrbV6Aw3tHVRRDASODc1s1%2Flm%2F0n%2FUoHJW7lBQMcuvvY%2Boqk5Ciw5cEa9LhXs1%2BjQzguwAss8U4YL6ickwm1oBKNP%2Ft88fBwqCdEH5tioQTIVlLrUHAaRyzL%2BY&X-Amz-Signature=b16f4433bdc10fa2c3ba47d17e6e2ce2823ff93666f43476d26ef1213a1d1c73&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DS2NPNU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCOY3P50tGGSTJfZ6RPun6AJc1AsYQAYHbFHnjwUqGhggIgIQwHcNnOKRqDg1%2Fy3d%2BmBlQE9O2WbmJyZyMpG4qjNTkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDApp0MYNPdbMCOujFSrcA8b21NsjFBwYCuuvMmEywtb9GfBN5n3AWopMujLKvqyq963b6kucmZanTsyMUjgjZy1DEq0XvHybIUTWdLm5m0c0bVdD7aOyJVLUNaNwy8vd3WtwwbQ3O1DekT%2BrcUqxlrQiaBjOt9NgCIk2XQYEAx%2BHS06zFqHD5julc5fhmU0ObEyUxtDPYv3ofBJu2QyN62WeR9rtOpRRnOllDVLBqnCltlT4y%2Fy6MXYcp218qBSo33m%2BMdYnLiKf4jZMzVKvZGS07rWDAXDs34Y77IZDcGjuZdEfb2rb402Pat6KK73s4gTKtCye403rRC5D4c4vUCb3qq%2FDTK54biMZIQzBZxbNLn4gU%2FGkdS%2BiZoJ6zt76HmnZnELaC5VM0rxOuMH%2BrXs5JIv4lwSd6JnpRG6Ed4UGGrcvJMucRAPLeVGA9O7MpOw%2ByDkuRf5HklU%2FV5jBQXUq19Xbm46wpZ52PjPOfwVQ9artrFVqAW54LgDjJfHFf8m1STSKDFMjtIRIVIgATOwpdLKbEX26VA7kDSgta2PvLFOH7jIXdmGr33lc%2Bzci9sIB2%2BQzcrC3kO9EmDUBB48c4BdLGagvU8MZkCRFa%2FmBHrL%2Fytqt2zy5%2FyWVwg26HIuIZpPQIzS5g7%2FgMLO75rwGOqUB9OXZYXP5AgQa1l2aSHADmk08c4p%2BCzSDNrBid7PPUdHktRRZyj5T3aOZ%2FNjLZHwfaI9p77t87QKRglOkeVciUBbt3ry8chSo8mdrbV6Aw3tHVRRDASODc1s1%2Flm%2F0n%2FUoHJW7lBQMcuvvY%2Boqk5Ciw5cEa9LhXs1%2BjQzguwAss8U4YL6ickwm1oBKNP%2Ft88fBwqCdEH5tioQTIVlLrUHAaRyzL%2BY&X-Amz-Signature=dd05f523ac4388fbb1531509f39ca7d4ee7136c275c1f875df57ce918decd5d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DS2NPNU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCOY3P50tGGSTJfZ6RPun6AJc1AsYQAYHbFHnjwUqGhggIgIQwHcNnOKRqDg1%2Fy3d%2BmBlQE9O2WbmJyZyMpG4qjNTkqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDApp0MYNPdbMCOujFSrcA8b21NsjFBwYCuuvMmEywtb9GfBN5n3AWopMujLKvqyq963b6kucmZanTsyMUjgjZy1DEq0XvHybIUTWdLm5m0c0bVdD7aOyJVLUNaNwy8vd3WtwwbQ3O1DekT%2BrcUqxlrQiaBjOt9NgCIk2XQYEAx%2BHS06zFqHD5julc5fhmU0ObEyUxtDPYv3ofBJu2QyN62WeR9rtOpRRnOllDVLBqnCltlT4y%2Fy6MXYcp218qBSo33m%2BMdYnLiKf4jZMzVKvZGS07rWDAXDs34Y77IZDcGjuZdEfb2rb402Pat6KK73s4gTKtCye403rRC5D4c4vUCb3qq%2FDTK54biMZIQzBZxbNLn4gU%2FGkdS%2BiZoJ6zt76HmnZnELaC5VM0rxOuMH%2BrXs5JIv4lwSd6JnpRG6Ed4UGGrcvJMucRAPLeVGA9O7MpOw%2ByDkuRf5HklU%2FV5jBQXUq19Xbm46wpZ52PjPOfwVQ9artrFVqAW54LgDjJfHFf8m1STSKDFMjtIRIVIgATOwpdLKbEX26VA7kDSgta2PvLFOH7jIXdmGr33lc%2Bzci9sIB2%2BQzcrC3kO9EmDUBB48c4BdLGagvU8MZkCRFa%2FmBHrL%2Fytqt2zy5%2FyWVwg26HIuIZpPQIzS5g7%2FgMLO75rwGOqUB9OXZYXP5AgQa1l2aSHADmk08c4p%2BCzSDNrBid7PPUdHktRRZyj5T3aOZ%2FNjLZHwfaI9p77t87QKRglOkeVciUBbt3ry8chSo8mdrbV6Aw3tHVRRDASODc1s1%2Flm%2F0n%2FUoHJW7lBQMcuvvY%2Boqk5Ciw5cEa9LhXs1%2BjQzguwAss8U4YL6ickwm1oBKNP%2Ft88fBwqCdEH5tioQTIVlLrUHAaRyzL%2BY&X-Amz-Signature=68cb774dc079d13ecf50b286bb44b761ee2d51e9ac4a4e6307f32f0eae0bc7f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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


