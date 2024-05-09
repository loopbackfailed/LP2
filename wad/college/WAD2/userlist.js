document.addEventListener('DOMContentLoaded', function() {
    // Fetch user list from server
    fetch('https://mockapi.io/endpoint')
      .then(response => response.json())
      .then(data => {
        const userList = document.getElementById('userList');
        data.forEach(user => {
          const li = document.createElement('li');
          li.textContent = `Name: ${user.name}, Email: ${user.email}`;
          userList.appendChild(li);
        });
      })
      .catch(error => console.error('Error:', error));
  });
  