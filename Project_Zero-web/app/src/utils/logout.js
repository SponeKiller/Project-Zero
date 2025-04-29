export function logout() {
    sessionStorage.removeItem('accessToken');
    window.location.href = '/login';
}
  