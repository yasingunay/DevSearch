// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
    // hljs.highlightAll();
  
    let alertWrapper = document.querySelector('.alert');
    let alertClose = document.querySelector('.alert__close');
  
    if (alertWrapper) {
        alertClose.addEventListener('click', () => {
            console.log('Close button clicked');
            alertWrapper.style.display = 'none';
        });
    }
  
    // Adding a test statement
    console.log('app.js is working!');
    console.log('alertWrapper:', alertWrapper);
    console.log('alertClose:', alertClose);
});