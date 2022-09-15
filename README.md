# Backend piece for backend dataset upload and validation

## Goal of this repo is to give a short example with some code to get a general idea on codestyle, architecture, etc


# Task
Let's imagine that you are developing a web service for a customer. Your team started developing MVP recently.
Your current task is to create two back-end functions (and few basic tests for them):
1. `def read_file(file_data: BinaryIO) -> <File content in any pythonic format>`
2. `def validate_dataset(dataset: <File content in any pythonic format>) -> List[str]`

Let's take a look at the functions' requirements in more detail.

#### Function `read_file`
##### Input
The function receives binary data of a file, which was uploaded by a user.
A sample of proper data you can find here:
[Link to the sample dataset](https://eforexcel.com/wp/wp-content/uploads/2017/07/10000-Sales-Records.zip)
Supported file formats: CSV, XLSX, XLS.
##### Output
The output of the function you may choose by yourself it should be something convenient to use in further handling (for example it could be a list of objects, generator, pandas.DataFrame, or something else).
##### Additional notes
- The list of supported file formats will be enriched in the future.
- Potentially a user may upload any file and the function should raise an exception in case of invalid file format.
- Feel free to use file fixtures when you will write tests.

#### Function `validate_dataset`
##### Input
The function recieves an object which was returned by function `read_file`.
##### Output
List of messages which highlight all found issues in the dataset.
##### Test cases
1. Region name corresponds to the country name. Should be checked via `First API service`.
2. Priority value exists in the customer's MDM system. Should be checked via `Second API service`.
3. Total Profit value should be not less than 1000.
4. Total Cost value should be not bigger than 5000000.
5. Order Date should be less than Ship Date.
6. Check values by the formula: `Units Sold * Unit Price = Total Revenue`
7. Check values by the formula: `Units Sold * Unit Cost = Total Cost`

##### Additional notes
- The list of checks will be enriched in the future.
- The customer doesn't provide us credentials to API services yet. For testing functionality, you may use mock objects.
- Both limits 1000 and 5000000 could be changed by the customer later.

##### First API service (Country object)
```
swagger: '2.0'
host: api.example.com
basePath: "/MasterData/Country/1"
schemes:
- https
produces:
- application/json
- application/xml
security:
- httpBasicAuth: []
paths:
  "/":
    get:
      description: 'Returns a list of countries. Country properties: code, name, description, region'
      parameters:
      - name: countryName
        in: query
        description: Filter by country name
        required: false
        type: string
```
##### Second API service (Priority object)
```
swagger: '2.0'
host: api-priority.example.com
basePath: "/"
schemes:
- https
produces:
- application/json
- application/xml
security:
- httpBasicAuth: []
paths:		
  "/{priorityCode}":
    get:
      description: 'Returns 1 if priority code exists, otherwise returns 0'
      parameters:
      - name: priorityCode
        in: path
        required: true
        type: string
  "/":
    get:
      description: 'Returns a list of all possible priority codes'
```