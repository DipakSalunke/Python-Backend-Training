## Tasks

  - Implement the Groceries API using Flask RESTful
    - Use pipenv instead of pip and venv
    - Implement the below endpoints
        - /vegetables
            - POST adds a new veggie
            - GET returns the list of veggies
        - /vegetables/<string:veggiename>
            - GET returns a single veggie matching the name
            - PUT updates a single veggie matching a name
            - DELETE removes a single veggie matching a name
            - all these 3 should return 404 if the veggie doesn't exist

## Bonus Challenge

  - Add a parser to accept veggie name and quantity args in the POST/PUT requests


[![View Requests](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/10137778/TWDZHvsr#0d3bafd1-a587-44f3-bc4d-61d12ec56f98)
