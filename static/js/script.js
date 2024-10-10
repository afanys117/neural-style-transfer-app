document.addEventListener("DOMContentLoaded", function () {
    const contentInput = document.getElementById('content');
    const styleInput = document.getElementById('style');
    const contentPreview = document.getElementById('content-preview').querySelector('img');
    const stylePreview = document.getElementById('style-preview').querySelector('img');
    const outputPreview = document.getElementById('output-preview').querySelector('img');
    const processingText = document.getElementById('processing-text');
    const generateButton = document.getElementById('generate-button');

    // Function to handle content image upload
    contentInput.addEventListener('change', function () {
        const file = contentInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                contentPreview.src = e.target.result;
                contentPreview.style.display = 'block'; // Show the content image
            }
            reader.readAsDataURL(file);
        }
    });

    // Function to handle style image upload
    styleInput.addEventListener('change', function () {
        const file = styleInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                stylePreview.src = e.target.result;
                stylePreview.style.display = 'block'; // Show the style image
            }
            reader.readAsDataURL(file);
        }
    });

    // Function to handle the generate button click
    generateButton.addEventListener('click', function () {
        // Show processing text and hide the output image initially
        processingText.style.display = 'block';
        outputPreview.style.display = 'none';

        // Implement the AJAX request to send images for processing
        const formData = new FormData();
        formData.append('content', contentInput.files[0]);
        formData.append('style', styleInput.files[0]);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Hide processing text and display the output image
            processingText.style.display = 'none';
            outputPreview.src = data.output_url; // Use the output URL from the response
            outputPreview.style.display = 'block'; // Show the output image
        })
        .catch(error => {
            console.error('Error:', error);
            processingText.innerText = 'Error processing images.';
        });
    });
});
