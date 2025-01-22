# CAMERA_PROJECT-WITH_QUEUE_TREADING_DATABASE

This project demonstrates a multithreaded image processing pipeline that utilizes the YOLOv10n model for object detection in videos. The processed data is saved to a structured SQLite database for further analysis.

## Features

- **YOLOv10n Integration**: Object detection using the YOLOv10n model.
- **Multithreaded Processing**: Processes video frames concurrently using threading.
- **Database Management**: Saves object detection results into SQLite, organized by object classes.
- **Error Handling**: Includes robust mechanisms for managing errors and logging.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.8+
- Required Python packages (install with `pip install -r requirements.txt`):
  - OpenCV
  - SQLite3
  - Colorama
  - Ultralytics (for YOLO)

## File Structure

- `1_MY_PROJECT_CAMERA_QUEUE_TREADING_DATABASE.py`: Main entry point of the application.
- `MODULE_READ_PROCESS.py`: Contains the logic for reading video frames and processing them using the YOLOv10n model.
- `MODULE_SAVA_ENTERE.py`: Handles database interactions, including saving processed data.
- `requirements.txt`: Lists all the dependencies for the project.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Amin-moniry-pr7/CAMERA_PROJECT-WITH_QUEUE_TREADING_DATABASE.git
   cd CAMERA_PROJECT-WITH_QUEUE_TREADING_DATABASE
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your video file:
   Place the video file (`VL_VIDEO.mp4`) in the project directory.

4. Run the main script:
   ```bash
   python 1_MY_PROJECT_CAMERA_QUEUE_TREADING_DATABASE.py
   ```

5. Enter the desired number of threads when prompted.

## Output

- **Processed Images**: Saved in a folder named `⚠️_AMIN_FRAME_⚠️`, categorized by detected classes.
- **Database Records**: Saved in `FRAME_PROCESSING.db` with tables created for each detected class.

## Highlights

- **Frame Processing**: Video frames are extracted and passed through YOLOv10n for object detection.
- **Dynamic Table Creation**: A new table is created for each unique detected class in the database.
- **Scalable Threads**: Users can choose the number of threads for concurrent processing.

## Example Output

- Processed frame counts and class-specific images are saved dynamically.
- SQLite database contains detailed logs and image paths.

## Future Improvements

- Add a graphical user interface (GUI).
- Support for real-time video streams.
- Extend functionality for additional model integration.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.

## Contact

For any queries, please contact:
- **Amin Moniry**: [GitHub Profile](https://github.com/Amin-moniry-pr7)

