import Dashboard from '../features/dashboard/index.js';
import Chat from '../features/chat/index.js';


const privateRoutes = [
    {path: '/dashboard',  element: <Dashboard />},
    {path: '/chat',  element: <Chat />},

];


export default privateRoutes;