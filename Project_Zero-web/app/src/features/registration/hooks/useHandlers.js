import { useState } from 'react';
import registerUser from '../services/registerService.js';

export const useHandlers = (initialValues) => {
    const [formData, setFormData] = useState(initialValues);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
        ...prevData,
        [name]: value,
        }));
    };

    const handleSubmit = async (data) => async (e) => {
        e.preventDefault();
        try {
            const response = await registerUser(data);
            console.log('User registered:', response);
          } catch (error) {
            console.error('Registration failed:', error);
          }
      };

    return { formData, handleChange, handleSubmit };
};