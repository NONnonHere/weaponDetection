from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("YOUR_PATH_OF_MODEL")

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Inference with lower confidence threshold
    results = model(frame, imgsz=640, conf=0.1)
    
    # Get the detection boxes
    boxes = results[0].boxes
    
    # If there are detections, select the one with the highest confidence
    if len(boxes) > 0:
        # Sort boxes by confidence (descending) and pick the top one
        top_box = sorted(boxes, key=lambda x: x.conf, reverse=True)[0]
        
        # Extract box details
        x1, y1, x2, y2 = map(int, top_box.xyxy[0])  # Coordinates
        conf = top_box.conf.item()  # Confidence score
        cls = int(top_box.cls.item())  # Class ID
        label = f"{model.names[cls]} {conf:.2f}"
        
        # Logic for drawing the box
        annotated_frame = frame.copy()
        if cls == 0:  # Class 0 ("automatic")
            if conf > 0.50:  # Only show if confidence > 0.50
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                print(f"Detection: {label}")
            else:
                print(f"Ignored: {label} (Class 0, conf <= 0.50)")
        else:  # Other classes
            # Show box regardless of confidence (as long as it’s > 0.1 from model)
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print(f"Detection: {label}")
    else:
        annotated_frame = frame.copy()  # No detections, use original frame
        print("No detections")

    # Show the annotated frame
    cv2.imshow("YOLO11 Detection", annotated_frame)
    
    # Break loop on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()