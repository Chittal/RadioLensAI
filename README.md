# RadioLensAI
The project aims to develop a compact and efficient vision-language model for automatic radiology report generation. Drawing inspiration from projects like Microsoft’s Maira, the core objective is to create a system that can analyze radiological images (X-rays, MRIs, CT scans) and generate detailed, coherent, and clinically meaningful reports. However, unlike Maira, this model will be significantly smaller in size and computationally lighter, making it more accessible and feasible for real-world applications in resource-constrained environments such as smaller clinics and rural healthcare facilities.

## To run this application
Install python first and follow the below steps to run this application in Windows.
1. Create a virtual environment
   ```python -m venv venv```
2. Activate venv
   ```venv\Scripts\activate```
3. Install requirements
   ```pip install -r requirements.txt```
4. Create .env file and set 'SECRET_KEY'
   ```SECRET_KEY = 'Your value'```
5. Run Flask application
  ```python main.py```
