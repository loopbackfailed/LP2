document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
  
    form.addEventListener('submit', function(event) {
      event.preventDefault();
      
      const formData = new FormData(form);
      const userData = {
        name: formData.get('name'),
        email: formData.get('email'),
        password: formData.get('password')
      };
  
      // Send data via AJAX POST request
      const xhr = new XMLHttpRequest();
      xhr.open('POST', 'https://mockapi.io/endpoint', true);
      xhr.setRequestHeader('Content-Type', 'application/json');
  
      xhr.onload = function() {
        if (xhr.status === 201) {
          // Data successfully sent, redirect to user list page
          window.location.href = 'userlist.html';
        } else {
          console.error('Error:', xhr.responseText);
        }
      };
  
      xhr.onerror = function() {
        console.error('Request failed');
      };
  
      xhr.send(JSON.stringify(userData));
    });
  });
  