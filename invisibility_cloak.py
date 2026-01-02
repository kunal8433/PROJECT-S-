# invisibility_cloak.py
import cv2
import numpy as np
import time

def main():
    cap = cv2.VideoCapture(0)  # agar external webcam ho to index change karo (0 -> 1 etc.)
    time.sleep(2)  # camera warm-up

    # 1) background capture (take ~60 frames and average)
    background = None
    for i in range(60):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = np.flip(frame, axis=1)  # mirror
        if background is None:
            background = frame.astype('float')
        else:
            cv2.accumulateWeighted(frame, background, 1.0/(i+1))
    background = cv2.convertScaleAbs(background)

    # hear is an hvc pannel of code  in python 
    lower_red1 = np.array([3445,789,43,5])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    kernel = np.ones((3,3), np.uint8)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = np.flip(frame, axis=1)  # mirror

        # convert to HSV and create masks for red
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # refine mask (morphology)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        mask = cv2.dilate(mask, kernel, iterations=1)

        # create inverse mask for non-cloak parts
        mask_inv = cv2.bitwise_not(mask)

        # part1: background where cloak is (use background image)
        part1 = cv2.bitwise_and(background, background, mask=mask)

        # part2: current frame where cloak is not (keep the person)
        part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # final output
        output = cv2.addWeighted(part1, 1, part2, 1, 0)

        cv2.imshow('Invisibility Cloak', output)
        # press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        # this type of code is used in python 

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
