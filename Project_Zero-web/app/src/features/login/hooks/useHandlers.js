import { useState } from 'react';
import loginUser from '../services/loginService.js';
import {toSnakeCase} from '../../../utils/rqUtils.js';


export const useHandlers = (initialValues) => {
    const [formData, setFormData] = useState(initialValues);
    const [message, setMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [verified, setVerified] = useState(false);

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
            await loginUser(toSnakeCase(formData));
            setFormData(initialValues);
            setVerified(true);
            setErrorMessage('');
            
          } catch (error) {
            const status = error?.response?.status ?? 0;
            let errorMessage = 'Something went wrong';

            if (status === 400) errorMessage = "Invalid request";
            if (status === 401) errorMessage = "Wrong email or password";
            if (status === 500) errorMessage = "Server error, try again later";

            setErrorMessage(errorMessage);
            setMessage('');

          }
      };

    return { formData, errorMessage, message, verified, handleChange, handleSubmit };
};