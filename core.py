from moviepy.editor import * 

def makevideo(scene):
	vid_path = scene["video"]
	images = scene["images"]

	video = VideoFileClip(vid_path)
	to_concat = []
	prev_ending = 0.0

	images = sorted(images, key = lambda elem: elem["point"])
	
	for elem in images:
		image = elem["img"] 
		point = elem["point"]
		duration = elem["duration"]

		clip = ImageClip(image, transparent = False)
		clip.resize(video.size)
		clip = clip.set_duration(t = duration)
		to_concat.append(video.subclip(t_start = prev_ending, t_end = point))
		to_concat.append(clip.copy())
		prev_ending = point

	to_concat.append(video.subclip(t_start = prev_ending))
	return concatenate_videoclips(to_concat)

scene = {"video": "bin/video/milk.mp4", "images": [{"img": "bin/poster_blue.png", "point": 5, "duration": 2}, {"img": "bin/poster_red.png", "point": 10, "duration": 3}]}
makevideo(scene).write_videofile("result.mp4")

	