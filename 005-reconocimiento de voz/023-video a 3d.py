import cv2
import open3d as o3d

# Webcam settings
width, height = 640, 480

# Initialize the webcam capture
video_capture = cv2.VideoCapture(0)
video_capture.set(3, width)
video_capture.set(4, height)

# Initialize Open3D visualizer
visualizer = o3d.visualization.Visualizer()
visualizer.create_window(width=width, height=height)

# Point cloud container
point_cloud = o3d.geometry.PointCloud()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the keypoints and descriptors with ORB
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # Create an Open3D point cloud from the keypoints
    if descriptors is not None and len(descriptors) > 0:
        keypoints_3d = []
        for kp in keypoints:
            keypoints_3d.append([kp.pt[0], kp.pt[1], 0])  # Set Z-coordinate as 0 for now

        point_cloud.points = o3d.utility.Vector3dVector(keypoints_3d)

    # Update Open3D visualizer
    visualizer.add_geometry(point_cloud)
    visualizer.update_geometry()
    visualizer.poll_events()
    visualizer.update_renderer()

    # Display the frame
    cv2.imshow('Webcam Feed', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the Open3D visualizer
video_capture.release()
cv2.destroyAllWindows()
visualizer.destroy_window()
