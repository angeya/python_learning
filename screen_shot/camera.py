import cv2
import time

cap = cv2.VideoCapture(0)


def camera():
	while True:
		ret, frame = cap.read(0)
		cv2.imshow("camera", frame)
		if cv2.waitKey(1) & 0xFF == ord('k'):
			t = time.time()
			name = str((int(t * 10)))
			cv2.imwrite("./yq" + name + ".jpg", frame)
			time.sleep(1.5)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()
			return


if __name__ == "__main__":
	camera()