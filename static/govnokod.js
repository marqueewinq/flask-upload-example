
function govnokod_add_video(vid_path) {
	return {"video": vid_path, "images": []};
}
function govnokod_select_image(url) {
	image = url
}
function govnokod_send(url) {
	console.log(scene)
}
function govnokod_add_image(position) {
	duration = document.getElementById("duration").value;
	console.log({"image": image, "duration": duration, "point": position})
	scene["images"].push({"image": image, "duration": duration, "point": position});
}