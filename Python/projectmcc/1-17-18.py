import face_recognition
import cv2

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
process_this_frame = True

while True:
	# Grab a single frame of video
	ret, frame = video_capture.read()
	frame2 = cv2.imread("White.jpg")
	video_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
	video_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
	
	# Resize frame2 to same dimensions as original frame
	frame2 = cv2.resize(frame2, (video_width, video_height))
	# Resize frame of video to 1/4 size for faster face recognition processing
	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
	
	# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
	rgb_small_frame = small_frame[:, :, ::-1]
	
	# Facial landmarks print
	face_landmarks_list = face_recognition.face_landmarks(rgb_small_frame)
	
	if len(face_landmarks_list) == 0:
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame2, "Bring your face into view", (int(video_height/2), int(video_width/2)), font, 1.0, (0, 255, 0), 1)
		
	else:
		for face_landmarks in face_landmarks_list:
		
			# Print the location of each facial feature in this image
			facial_features = [
			'chin',
			'left_eyebrow',
			'right_eyebrow',
			'nose_bridge',
			'nose_tip',
			'left_eye',
			'right_eye',
			'top_lip',
			'bottom_lip'
			]
			
			for facial_feature in facial_features:
				for i in range(len(face_landmarks[facial_feature]) - 1):
					lineThickness = 2
					top = face_landmarks[facial_feature][i][0] * 4, face_landmarks[facial_feature][i][1] * 4
					bottom = face_landmarks[facial_feature][i + 1][0] * 4, face_landmarks[facial_feature][i + 1][1] * 4
					cv2.line(frame2, top, bottom, (0, 255, 0), lineThickness)
					
		frame2 = cv2.flip(frame2, 1)
		
	# Display the resulting image
	cv2.imshow('Video', frame2)
	
	# Hit 'q' on the keyboard to quit!
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

