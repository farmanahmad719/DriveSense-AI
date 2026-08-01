from ultralytics import YOLO

import config


class PhoneDetector:

    def __init__(self):

        self.model = YOLO(
            config.YOLO_MODEL_PATH
        )

        # Number of consecutive frames
        # required to confirm phone detection
        self.required_frames = 3

        self.detected_frames = 0

    # ==================================================

    def detect(self, frame):

        results = self.model(
            frame,
            conf=config.PHONE_CONFIDENCE,
            verbose=False
        )

        phone_detected = False

        phone_confidence = 0.0

        phone_bbox = None

        # ----------------------------------------------

        for result in results:

            for box in result.boxes:

                class_id = int(
                    box.cls[0]
                )

                class_name = self.model.names[
                    class_id
                ]

                confidence = float(
                    box.conf[0]
                )

                # ----------------------------------
                # Check phone
                # ----------------------------------

                if class_name == "cell phone":

                    phone_detected = True

                    # Keep highest confidence
                    if confidence > phone_confidence:

                        phone_confidence = confidence

                        coordinates = box.xyxy[0].tolist()

                        phone_bbox = tuple(
                            map(
                                int,
                                coordinates
                            )
                        )

        # ==================================================
        # TEMPORAL CONFIRMATION
        # ==================================================

        if phone_detected:

            self.detected_frames += 1

        else:

            self.detected_frames = 0

        confirmed_phone = (

            self.detected_frames
            >= self.required_frames
        )

        # ==================================================

        return {

            "detected": confirmed_phone,

            "confidence": phone_confidence,

            "bbox": phone_bbox

        }