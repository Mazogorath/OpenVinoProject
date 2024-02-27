from faceChecking import faceCheckings
from dual import duals
from dual import save_dataset
import cv2


if __name__ == "__main__":
    while True:
        total_result = None

        player1 = faceCheckings(file="image3.jpg")
        duals()
        value1 = save_dataset.copy()

        player2 = faceCheckings(file="image1.jpg")
        duals()
        value2 = save_dataset.copy()

        print(value1)
        print(value2)
        if value1 is not None and value2 is not None:
            if value2 > value1:
                total_result = player2
            elif value1 > value2:
                total_result = player1
            elif value1 == value2:
                total_result = player1
            else:
                print("One or both of the values is None.")

        cv2.imshow("Winner", total_result)

        if total_result is not None:
            cv2.imshow("Winner", total_result)
            cv2.putText(total_result, text=str(value1), org=(int(total_result.shape[1] / 5), 100), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 255, 0), thickness=3)
            cv2.putText(total_result, text="Press 'r' to restart", org=(int(total_result.shape[1] / 5), 150), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=3)
            

        key = cv2.waitKey(0)
        if key == ord('r'):
            continue
        elif key == ord('q'):
            break

cv2.destroyAllWindows()
