<h3 align="center">
  <img src="img/unstructured_logo.png" height="200">
</h3>

<h3 align="center">
  <p>Pre-Processing OCR Pipeline for PaddleOCR</p>
</h3>


This pipeline processes input image documents in the English language using [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR).
The pipeline works on x86\_64 cpus.

## Developer Quick Start

* Using `pyenv` to manage virtualenv's is recommended
	* Mac install instructions. See [here](https://github.com/Unstructured-IO/community#mac--homebrew) for more detailed instructions.
		* `brew install pyenv-virtualenv`
	  * `pyenv install 3.8.15`
  * Linux instructions are available [here](https://github.com/Unstructured-IO/community#linux).

  * Create a virtualenv to work in and activate it, e.g. for one named `paddleocr`:

	`pyenv  virtualenv 3.8.15 paddleocr` <br />
	`pyenv activate paddleocr`

* Run `make install`
* Start a local jupyter notebook server with `make run-jupyter` <br />
	**OR** <br />
	just start the fast-API locally with `make run-web-app`

#### Extracting whatever from some type of document

Give a description of making API calls using example `curl` commands, and example JSON responses.

For example:
```
curl -X 'POST' \
  'http://localhost:8000/paddleocr/v0.0.1/paddleocr' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@example.pdf' \
  -F 'some_parameter=something'  | jq -C . | less -R
```

It's also nice to show how to call the API function using pure Python.

### Generating Python files from the pipeline notebooks

You can generate the FastAPI APIs from your pipeline notebooks by running `make generate-api`.

## Security Policy

See our [security policy](https://github.com/Unstructured-IO/pipeline-paddleocr/security/policy) for
information on how to report security vulnerabilities.

## Learn more

| Section | Description |
|-|-|
| [Unstructured Community Github](https://github.com/Unstructured-IO/community) | Information about Unstructured.io community projects  |
| [Unstructured Github](https://github.com/Unstructured-IO) | Unstructured.io open source repositories |
| [Company Website](https://unstructured.io) | Unstructured.io product and company info |
