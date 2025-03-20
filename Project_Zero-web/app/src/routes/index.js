import { useRoutes } from 'react-router-dom';
import publicRoutes from './PublicRoutes';
import privateRoutes from './PrivateRoutes';
import SecureRoutes from '../components/routes/SecureRoutes';

const AppRoutes = () => {

  const protectedRoutes = privateRoutes.map((route) => ({
    ...route,
    element: (
        <SecureRoutes>{route.element}</SecureRoutes>
    ),
  }));


  const routing = useRoutes([...publicRoutes, ...protectedRoutes]);
  
  return routing;
};

export default AppRoutes;
