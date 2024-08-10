# Smart Car Parking System

## Overview

The Smart Car Parking System is a comprehensive solution designed to optimize parking space management using computer vision, data analytics, and hardware integration. This system includes real-time parking space detection, availability tracking, and predictive analysis to enhance the efficiency of parking operations. It integrates Arduino Nano for hardware control and data collection.

## Features

- **Space Detection**: Uses computer vision to identify available and occupied parking spaces.
- **Availability Tracking**: Provides real-time updates on the status of parking spaces.
- **Predictive Analysis**: Utilizes linear regression to forecast future parking space availability.
- **Hardware Integration**: Employs Arduino Nano for data collection and control.
- **User Interface**: Interactive frontend to display parking status and forecasts.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: PHP
- **Computer Vision**: OpenCV (Python)
- **Predictive Analytics**: Linear Regression (Python)
- **Database**: MongoDB or MySQL
- **Hardware**: Arduino Nano

## Installation

### Prerequisites

1. **Web Server**: Apache or Nginx
2. **PHP**: Version 7.4 or later
3. **Python**: Version 3.8 or later
4. **OpenCV**: Python package
5. **Database**: MongoDB or MySQL
6. **Arduino Nano**: Required for hardware integration

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/smart-car-parking-system.git
    cd smart-car-parking-system
    ```

2. **Install Python Dependencies**

    ```bash
    pip install opencv-python numpy pandas scikit-learn
    ```

3. **Setup Database**

    - **MongoDB**: Follow MongoDB installation and setup instructions to create a database.
    - **MySQL**: Create a database and tables based on the schema provided.

4. **Configure the Web Server**

    - **Apache/Nginx**: Point the web server root to the `frontend` directory.
    - **PHP Configuration**: Ensure that PHP is configured to handle API requests.

5. **Setup Arduino Nano**

    - **Arduino IDE**: Install the Arduino IDE and necessary libraries.
    - **Upload Firmware**: Upload the provided Arduino code to the Arduino Nano to interface with sensors and transmit data.

6. **Run Python Scripts**

    - **Start the Space Detection Script**

        ```bash
        python detect_spaces.py
        ```

    - **Run the Forecast Script**

        ```bash
        python forecast.py
        ```

## Usage

1. **Access the Web Application**

    Open your web browser and navigate to `http://localhost/` or the URL where your web server is hosted.

2. **Interact with the Interface**

    - **Parking Space Availability**: View the current status of parking spaces.
    - **Forecast**: Check the predicted availability of parking spaces for the next 24 hours.

3. **Hardware Operation**

    - The Arduino Nano will be responsible for collecting data from sensors and sending it to the backend server.
    - Ensure that the Arduino Nano is connected and powered correctly.

## API Endpoints

- **`/api/parking-status`**: Returns the current availability of parking spaces.
  - **Method**: GET
  - **Response**: JSON object with `availableSpaces` field.

- **`/api/parking-forecast`**: Provides forecast data for parking space availability.
  - **Method**: GET
  - **Response**: JSON object with `forecast` field containing predicted values.

## Computer Vision

- **Detect Spaces**: The `detect_spaces.py` script uses OpenCV to process camera feeds, detecting and counting parking spaces. Modify this script based on your specific camera setup and detection needs.

## Predictive Analytics

- **Forecast**: The `forecast.py` script uses linear regression to predict future parking space availability based on historical data. Customize the model and data handling as needed.

## Hardware Integration

- **Arduino Nano**: Interfaces with sensors to collect data on parking space occupancy.
  - **Connections**: Connect sensors to the appropriate pins on the Arduino Nano.
  - **Code**: Upload the Arduino firmware to handle sensor data and communicate with the backend.

## Testing

- Ensure all components are working together by performing end-to-end tests.
- Test API endpoints using tools like Postman or cURL.
- Verify computer vision accuracy and prediction results.
- Test Arduino Nano integration and data transmission.

## Troubleshooting

- **Issues with Camera Feed**: Check camera connections and OpenCV installation.
- **API Errors**: Verify PHP configuration and database connections.
- **Predictive Analysis Problems**: Ensure correct Python dependencies and data format.
- **Hardware Issues**: Check Arduino Nano connections and firmware.

## Contributing

We welcome contributions to improve the Smart Car Parking System. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).
