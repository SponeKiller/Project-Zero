import "../css/LoadingSpinner.css";

const LoadingSpinner = () => {
  return (
    <div className="loading-container">
      <p className="loading-text">Loading...</p>
      <div className="loading-spinner"></div>
    </div>
  );
};

export default LoadingSpinner;