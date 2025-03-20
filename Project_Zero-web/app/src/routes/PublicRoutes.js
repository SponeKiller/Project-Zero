import Homepage from '../features/homepage/index.js';
import Registration from '../features/registration/index.js';
import Login from '../features/login/index.js';



const publicRoutes = [
    {path: '/',  element: <Homepage />} ,
    {path: '/register',  element: <Registration />}, 
    {path: '/login', element: <Login />},
];

export default publicRoutes;