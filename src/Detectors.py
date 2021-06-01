import cv2,sys,mediapipe as mp,time
from win32api import GetSystemMetrics
mp_drawing=mp.solutions.drawing_utils
mp_face_mesh=mp.solutions.face_mesh
drawing_spec=mp_drawing.DrawingSpec(thickness=1,circle_radius=1)
video=cv2.VideoCapture(0)
print("Screen Resolutions")
print("•Width  =", GetSystemMetrics(0))
print("•Height =", GetSystemMetrics(1))
r=input("This need to access your camera. Would you like to on your webcam?(y,n) ")
if(r=="y" or "Y"):
	print("Starting your webcam...\n")
	try:
		with mp_face_mesh.FaceMesh(min_detection_confidence=0.5,
								   min_tracking_confidence=0.5) as face_mesh:
			while True:
				ret,image=video.read()
				image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
				image.flags.writeable=False
				results=face_mesh.process(image)
				image.flags.writeable=True
				image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
				if results.multi_face_landmarks:
					for face_landmarks in results.multi_face_landmarks:
						mp_drawing.draw_landmarks(image=image,
												  landmark_list=face_landmarks,
												  connections=mp_face_mesh.FACE_CONNECTIONS,
												  landmark_drawing_spec=drawing_spec,
												  connection_drawing_spec=drawing_spec)
				cv2.imshow("Face Mesh By Parth Kabra",image)
				k=cv2.waitKey(1)
				if k==ord("q"):
					sys.exit()
			video.release()
			cv2.destroyAllWindows()
	except:
		print("\n")
		print("Just Broke Up....")
		print("\n")
