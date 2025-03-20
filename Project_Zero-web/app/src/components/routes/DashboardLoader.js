import { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";

import LoadingSpinner from "../ui/js/LoadingSpinner.js";

const DashboardLoader = () => {
  const [redirect, setRedirect] = useState(false);

  useEffect(() => {
    
    setTimeout(() => {
      setTimeout(() => setRedirect(true), 1000);
    }, 2000);
  }, []);

  if (redirect) {
    return <Navigate to="/dashboard" />;
  }

  return <LoadingSpinner />;
};

export default DashboardLoader;
