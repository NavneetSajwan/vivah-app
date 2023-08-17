import React, { useState } from 'react';
import axios from 'axios'; // Import axios

function Register() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleRegister = async () => {
    try {
      await axios.post('http://localhost:8000/api/register', formData); // Use the backend URL
      alert('User registered successfully');
    } catch (error) {
      console.error('Error registering user', error);
      alert('An error occurred while registering user');
    }
  };
  
  return (
    <div>
      <h2>Register</h2>
      <input
        type="text"
        name="name"
        placeholder="Name"
        value={formData.name}
        onChange={handleInputChange}
      />
      <input
        type="email"
        name="email"
        placeholder="Email"
        value={formData.email}
        onChange={handleInputChange}
      />
      <input
        type="password"
        name="password"
        placeholder="Password"
        value={formData.password}
        onChange={handleInputChange}
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;
