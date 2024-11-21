# **Clothing Store API**

Welcome to the **Clothing Store API**, a FastAPI-based service for managing a store's inventory of clothing. This project allows you to manage categories like sizes, colors, materials, and types, with full CRUD capabilities. It also includes automated testing and GitHub Actions for continuous integration.



## **Features**
- **Category Management**: Organize clothing items by sizes, colors, materials, and types.
- **CRUD Operations**: Add, retrieve, update, and delete items.
- **FastAPI**: High-performance and modern API framework.
- **Database Integration**: Easily extendable to use SQLite, PostgreSQL, or any SQL database.
- **Testing**: Comprehensive unit, integration, regression, performance, and acceptance tests using Pytest.
- **GitHub Actions**: Automated CI pipeline for running tests on every push or pull request.



## **Getting Started**

### **Prerequisites**
Ensure you have the following installed:
- Python 3.10 or later
- Git



### **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/store-api.git
   cd store-api
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   # Activate the virtual environment:
   # On Windows (PowerShell)
   .\venv\Scripts\Activate
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the server locally:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).



## **API Endpoints**

| Method   | Endpoint                   | Description                          |
|----------|----------------------------|--------------------------------------|
| `GET`    | `/`                        | Welcome message                      |
| `GET`    | `/categories/{category}`   | Retrieve all items in a category     |
| `POST`   | `/categories/{category}`   | Add an item to a category            |
| `DELETE` | `/categories/items/{id}`   | Delete an item by ID                 |



## **Running Tests**

To ensure the app works as expected, run the following tests:

1. **Run All Tests**
   ```bash
   pytest
   ```

2. **Run Specific Test Suite**
   ```bash
   pytest tests/test_unit.py
   ```



## **Continuous Integration**

This project includes a GitHub Actions workflow for automated testing:

1. On every **push** or **pull request** to the `main` branch:
   - Dependencies are installed.
   - All test cases are executed.
   - Results are displayed in the GitHub Actions UI.

Check `.github/workflows/ci.yml` for the workflow configuration.



## **Data Structure**

Predefined JSON files for categories:
- `data/sizes.json` (e.g., `["S", "M", "L", "XL"]`)
- `data/colors.json` (e.g., `["red", "blue", "green", "black"]`)
- `data/materials.json` (e.g., `["cotton", "wool", "leather"]`)
- `data/types.json` (e.g., `["t-shirt", "jeans", "jacket"]`)



## **Future Enhancements**
- Add user authentication.
- Extend database to include stock quantities and pricing.
- Include caching with Redis for faster response times.
- Add Swagger documentation for API.



## **Contributing**

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-name
   ```
4. Open a pull request.



## **License**
This project is licensed under the MIT License. See the `LICENSE` file for more information.



## **Contact**
For questions or feedback, feel free to reach out:
- GitHub: [LielySantana](https://github.com/LielySantana)
- Email: [lielysantana12@gmail.com](mailto:lielysantana12@gmail.com)



This `README.md` provides a comprehensive overview of the project and helps both contributors and users get started easily. Adjust placeholders like `LielySantana` or `lielysantana12@gmail.com` as needed.