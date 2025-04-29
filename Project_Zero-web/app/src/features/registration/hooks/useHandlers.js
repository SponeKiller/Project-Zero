import { useState } from 'react';
import registerUser from '../services/registerService.js';

export const useHandlers = (initialValues) => {
    const [formData, setFormData] = useState(initialValues);
    const [message, setMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
        ...prevData,
        [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            await registerUser(formData);
            setFormData(initialValues);
            setMessage('User registered successfully');
            setErrorMessage('');    
          
          } catch (error) {
            
            const status = error.response.status;
            let errorMessage = 'Something went wrong';

            if (status === 400) errorMessage = "User already exists";
            if (status === 500) errorMessage = "Server error, try again later";
            setErrorMessage(errorMessage);
            setMessage('');       


          }
      };

    return { formData, errorMessage, message, handleChange, handleSubmit };
};