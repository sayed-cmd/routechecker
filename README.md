# Parcel Routing System

A simple Parcel Routing System that allows users to upload parcel data, fetch tracking details, and display the results in a dynamic table. The system is built with HTML, CSS, and JavaScript, providing a user-friendly interface for seamless parcel tracking and route management.

## Features

- Upload Database: Upload `.xlsx` files to update the parcel database.
- Scan Box: Input tracking IDs to fetch parcel details dynamically.
- Dynamic Table:
  - Displays the most recent parcel details.
  - Ensures the Route column in the first row is visually highlighted.
  - Maintains a maximum of 5 rows to keep the table concise.
- Reset Database: Clear the database and reset the system.
- Responsive design for various screen sizes.

## Screenshot



## How to Use

1. Clone the Repository: git clone https://github.com/sayed-cmd/routechecker.git cd parcel-routing-system
2. Run the Project:
- Open `index.html` in your favorite browser.
- Ensure your server API is running to handle requests (`/get-data`, `/upload-excel`, `/reset-database`).

3. Upload Database:
- Click the Upload button to upload an `.xlsx` file containing parcel details.

4. Fetch Parcel Data:
- Enter the tracking ID in the Scan Box and press Enter to fetch details.

5. Reset Database:
- Click the Reset Database button to clear all parcel data.

## File Structure

parcel-routing-system/ ├── index.html # Main HTML file ├── style.css # Contains styles for the project (if external styles are added) ├── script.js # JavaScript file for handling interactivity ├── /assets # Folder for images/screenshots └── README.md # Project documentation



## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend API: Required for database operations and fetching data
- Excel Parsing: Supports `.xlsx` file uploads

## API Endpoints

- GET /get-data: Fetch parcel data based on tracking ID.
- POST /upload-excel: Upload new parcel database.
- POST /reset-database: Reset the database to its initial state.

## Installation Requirements

- Modern browser (Chrome, Firefox, etc.)
- Backend API or server to handle requests (configure `/get-data`, `/upload-excel`, `/reset-database`).

## Contributing

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Coding! 🚀


