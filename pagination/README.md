Pagination in REST API Design

Project Overview

This project demonstrates various methods of implementing pagination in a REST API. It covers three key pagination techniques:

Simple Page and Page Size Parameters: Paginating a dataset using basic page and page size parameters.
Pagination with Hypermedia Metadata: Implementing HATEOAS (Hypermedia as the Engine of Application State) to guide the client on navigating through paginated data.
Deletion-Resilient Pagination: Ensuring pagination consistency even when items are deleted from the dataset.
The dataset used for this project is the Popular_Baby_Names.csv file.

Requirements

Python Version: 3.9
Operating System: Ubuntu 20.04 LTS
Code Style: All code follows the pycodestyle (version 2.5.*) style guide.
File Naming: All Python files should end with a newline and start with #!/usr/bin/env python3.
Documentation: Each module, class, and function is documented to explain its purpose and usage. All functions and coroutines are type-annotated.
Setup Instructions

Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Dependencies: If there are any dependencies, create a virtual environment and install them:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Dataset: Ensure that the Popular_Baby_Names.csv file is in the root directory of the project. This file will be used as the dataset for pagination.
Running the Project

You can run the project by executing the main script:

bash
Copy code
python3 main.py
Replace main.py with the actual name of your entry-point script.

Pagination Methods

1. Simple Page and Page Size Parameters
Use the get_page() function to paginate a dataset by specifying the page number and page size.

Example Usage:

python
Copy code
from pagination import get_page

data = load_dataset()  # Load your dataset here
page = 2
page_size = 20
result = get_page(data, page, page_size)
print(result)
2. Pagination with Hypermedia Metadata
The get_paginated_response() function returns a paginated dataset along with metadata to help navigate through the dataset.

Example Usage:

python
Copy code
from pagination import get_paginated_response

data = load_dataset()  # Load your dataset here
page = 1
page_size = 10
response = get_paginated_response(data, page, page_size)
print(response)
3. Deletion-Resilient Pagination
This method ensures that pagination remains consistent even when items are deleted. It uses unique identifiers to track the last item fetched.

Example Usage:

python
Copy code
from pagination import get_resilient_page

data = load_dataset()  # Load your dataset here
last_item_id = 123  # ID of the last item from the previous page
page_size = 15
result = get_resilient_page(data, last_item_id, page_size)
print(result)
Testing

To test the code and ensure it meets the requirements, you can use the following command:

bash
Copy code
python3 -m unittest discover tests/
Ensure all test cases pass, and the code follows the pycodestyle standards.

License

