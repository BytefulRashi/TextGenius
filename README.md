# Text Generation Web App with FastAPI and Transformers

This project demonstrates a simple web application built with FastAPI to generate text using the Hugging Face Transformers library. It uses a text-to-text generation pipeline to generate text based on user prompts.

## Features

- **FastAPI**: Backend framework for building APIs quickly and efficiently.
- **Transformers**: Integration with Hugging Face's state-of-the-art models for text generation.
- **Jinja2**: Templating engine for rendering HTML templates.

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**

   Make sure you have Python 3.7+ installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**

   Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://localhost:8000`.

## Usage

- **Home Page**: Navigate to `http://localhost:8000/` to access the home page.
- **Text Generation**: Enter a prompt and click the "Generate" button to see the generated text.

## Directory Structure

```
text_generation_fastapi/
│
├── main.py               # FastAPI application setup
├── templates/            # HTML templates for the web app
│   ├── index.html        # Main HTML template
│
└── requirements.txt      # Python dependencies
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
