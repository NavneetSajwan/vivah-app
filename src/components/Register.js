
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Register() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        gender: '',
        date_of_birth: '',
        marital_status: '',
        religion: '',
        caste: '',
        mother_tongue: '',
        country: '',
        state: '',
        city: ''
    });

    const [religions, setReligions] = useState([]);
    const [castes, setCastes] = useState([]);
    const [motherTongues, setMotherTongues] = useState([]);
    const [countries, setCountries] = useState([]);
    const [states, setStates] = useState([]);
    const [cities, setCities] = useState([]);

    useEffect(() => {
        axios.get('/api/religions').then(response => setReligions(response.data));
        axios.get('/api/castes').then(response => setCastes(response.data));
        axios.get('/api/mother-tongues').then(response => setMotherTongues(response.data));
        axios.get('/api/countries').then(response => setCountries(response.data));
        axios.get('/api/states').then(response => setStates(response.data));
        axios.get('/api/cities').then(response => setCities(response.data));
    }, []);

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData(prevState => ({ ...prevState, [name]: value }));
    };

    const handleSubmit = () => {
        axios.post('/api/register', formData)
            .then(response => {
                // Handle successful registration
            })
            .catch(error => {
                // Handle errors
            });
    };

    return (
        <div>
            <input type="text" name="name" onChange={handleInputChange} placeholder="Name" />
            <input type="email" name="email" onChange={handleInputChange} placeholder="Email" />
            <input type="password" name="password" onChange={handleInputChange} placeholder="Password" />
            <select name="gender" onChange={handleInputChange}>
                <option value="male">Male</option>
                <option value="female">Female</option>
            </select>
            <input type="date" name="date_of_birth" onChange={handleInputChange} />
            <select name="marital_status" onChange={handleInputChange}>
                <option value="single">Single</option>
                <option value="married">Married</option>
            </select>
            <select name="religion" onChange={handleInputChange}>
                {religions.map(religion => (
                    <option key={religion.id} value={religion.id}>{religion.name}</option>
                ))}
            </select>
            <select name="caste" onChange={handleInputChange}>
                {castes.map(caste => (
                    <option key={caste.id} value={caste.id}>{caste.name}</option>
                ))}
            </select>
            <select name="mother_tongue" onChange={handleInputChange}>
                {motherTongues.map(tongue => (
                    <option key={tongue.id} value={tongue.id}>{tongue.name}</option>
                ))}
            </select>
            <select name="country" onChange={handleInputChange}>
                {countries.map(country => (
                    <option key={country.id} value={country.id}>{country.name}</option>
                ))}
            </select>
            <select name="state" onChange={handleInputChange}>
                {states.map(state => (
                    <option key={state.id} value={state.id}>{state.name}</option>
                ))}
            </select>
            <select name="city" onChange={handleInputChange}>
                {cities.map(city => (
                    <option key={city.id} value={city.id}>{city.name}</option>
                ))}
            </select>
            <button onClick={handleSubmit}>Register</button>
        </div>
    );
}

export default Register;
